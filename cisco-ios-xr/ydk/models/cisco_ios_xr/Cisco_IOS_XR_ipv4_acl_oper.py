""" Cisco_IOS_XR_ipv4_acl_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-acl package operational data.

This module contains definitions
for the following management objects\:
  ipv4\-acl\-and\-prefix\-list\: Root class of IPv4 Oper schema tree

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



class Ipv4AclAndPrefixList(Entity):
    """
    Root class of IPv4 Oper schema tree
    
    .. attribute:: access_list_manager
    
    	Access list manager containing access lists and prefix lists
    	**type**\:   :py:class:`AccessListManager <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager>`
    
    .. attribute:: oor
    
    	Out Of Resources, Limits to the resources allocatable
    	**type**\:   :py:class:`Oor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor>`
    
    

    """

    _prefix = 'ipv4-acl-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ipv4AclAndPrefixList, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4-acl-and-prefix-list"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-acl-oper"

        self.access_list_manager = Ipv4AclAndPrefixList.AccessListManager()
        self.access_list_manager.parent = self
        self._children_name_map["access_list_manager"] = "access-list-manager"
        self._children_yang_names.add("access-list-manager")

        self.oor = Ipv4AclAndPrefixList.Oor()
        self.oor.parent = self
        self._children_name_map["oor"] = "oor"
        self._children_yang_names.add("oor")


    class AccessListManager(Entity):
        """
        Access list manager containing access lists and
        prefix lists
        
        .. attribute:: accesses
        
        	Access listL class displaying Usage and Entries
        	**type**\:   :py:class:`Accesses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses>`
        
        .. attribute:: prefixes
        
        	Table of prefix lists
        	**type**\:   :py:class:`Prefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Prefixes>`
        
        .. attribute:: usages
        
        	Table of Usage statistics of access lists at different nodes
        	**type**\:   :py:class:`Usages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Usages>`
        
        

        """

        _prefix = 'ipv4-acl-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv4AclAndPrefixList.AccessListManager, self).__init__()

            self.yang_name = "access-list-manager"
            self.yang_parent_name = "ipv4-acl-and-prefix-list"

            self.accesses = Ipv4AclAndPrefixList.AccessListManager.Accesses()
            self.accesses.parent = self
            self._children_name_map["accesses"] = "accesses"
            self._children_yang_names.add("accesses")

            self.prefixes = Ipv4AclAndPrefixList.AccessListManager.Prefixes()
            self.prefixes.parent = self
            self._children_name_map["prefixes"] = "prefixes"
            self._children_yang_names.add("prefixes")

            self.usages = Ipv4AclAndPrefixList.AccessListManager.Usages()
            self.usages.parent = self
            self._children_name_map["usages"] = "usages"
            self._children_yang_names.add("usages")


        class Prefixes(Entity):
            """
            Table of prefix lists
            
            .. attribute:: prefix
            
            	Name of the prefix list
            	**type**\: list of    :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv4AclAndPrefixList.AccessListManager.Prefixes, self).__init__()

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
                            super(Ipv4AclAndPrefixList.AccessListManager.Prefixes, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv4AclAndPrefixList.AccessListManager.Prefixes, self).__setattr__(name, value)


            class Prefix(Entity):
                """
                Name of the prefix list
                
                .. attribute:: prefix_list_name  <key>
                
                	Name of the prefix list
                	**type**\:  str
                
                .. attribute:: prefix_list_sequences
                
                	Table of all the SequenceNumbers per prefix list
                	**type**\:   :py:class:`PrefixListSequences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences>`
                
                

                """

                _prefix = 'ipv4-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix, self).__init__()

                    self.yang_name = "prefix"
                    self.yang_parent_name = "prefixes"

                    self.prefix_list_name = YLeaf(YType.str, "prefix-list-name")

                    self.prefix_list_sequences = Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences()
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
                                super(Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix, self).__setattr__(name, value)


                class PrefixListSequences(Entity):
                    """
                    Table of all the SequenceNumbers per prefix
                    list
                    
                    .. attribute:: prefix_list_sequence
                    
                    	Sequence Number of a prefix list entry
                    	**type**\: list of    :py:class:`PrefixListSequence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence>`
                    
                    

                    """

                    _prefix = 'ipv4-acl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences, self).__init__()

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
                                    super(Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences, self).__setattr__(name, value)


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
                        
                        .. attribute:: grant
                        
                        	Grant value permit/deny 
                        	**type**\:   :py:class:`AclAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclAction>`
                        
                        .. attribute:: hits
                        
                        	Number of hits
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: item_type
                        
                        	ACE type (prefix, remark)
                        	**type**\:   :py:class:`AclAce1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclAce1>`
                        
                        .. attribute:: maximum_length
                        
                        	Maximum length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: minimum_length
                        
                        	Min length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Port Operator
                        	**type**\:   :py:class:`AclPortOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperator>`
                        
                        .. attribute:: prefix
                        
                        	Prefix
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length 
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remark
                        
                        	Remark String
                        	**type**\:  str
                        
                        .. attribute:: sequence
                        
                        	ACLE sequence number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-acl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence, self).__init__()

                            self.yang_name = "prefix-list-sequence"
                            self.yang_parent_name = "prefix-list-sequences"

                            self.sequence_number = YLeaf(YType.uint32, "sequence-number")

                            self.acl_name = YLeaf(YType.str, "acl-name")

                            self.grant = YLeaf(YType.enumeration, "grant")

                            self.hits = YLeaf(YType.uint32, "hits")

                            self.item_type = YLeaf(YType.enumeration, "item-type")

                            self.maximum_length = YLeaf(YType.uint32, "maximum-length")

                            self.minimum_length = YLeaf(YType.uint32, "minimum-length")

                            self.operator = YLeaf(YType.enumeration, "operator")

                            self.prefix = YLeaf(YType.str, "prefix")

                            self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                            self.remark = YLeaf(YType.str, "remark")

                            self.sequence = YLeaf(YType.uint32, "sequence")

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
                                            "grant",
                                            "hits",
                                            "item_type",
                                            "maximum_length",
                                            "minimum_length",
                                            "operator",
                                            "prefix",
                                            "prefix_length",
                                            "remark",
                                            "sequence") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.sequence_number.is_set or
                                self.acl_name.is_set or
                                self.grant.is_set or
                                self.hits.is_set or
                                self.item_type.is_set or
                                self.maximum_length.is_set or
                                self.minimum_length.is_set or
                                self.operator.is_set or
                                self.prefix.is_set or
                                self.prefix_length.is_set or
                                self.remark.is_set or
                                self.sequence.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.sequence_number.yfilter != YFilter.not_set or
                                self.acl_name.yfilter != YFilter.not_set or
                                self.grant.yfilter != YFilter.not_set or
                                self.hits.yfilter != YFilter.not_set or
                                self.item_type.yfilter != YFilter.not_set or
                                self.maximum_length.yfilter != YFilter.not_set or
                                self.minimum_length.yfilter != YFilter.not_set or
                                self.operator.yfilter != YFilter.not_set or
                                self.prefix.yfilter != YFilter.not_set or
                                self.prefix_length.yfilter != YFilter.not_set or
                                self.remark.yfilter != YFilter.not_set or
                                self.sequence.yfilter != YFilter.not_set)

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
                            if (self.grant.is_set or self.grant.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.grant.get_name_leafdata())
                            if (self.hits.is_set or self.hits.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hits.get_name_leafdata())
                            if (self.item_type.is_set or self.item_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.item_type.get_name_leafdata())
                            if (self.maximum_length.is_set or self.maximum_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.maximum_length.get_name_leafdata())
                            if (self.minimum_length.is_set or self.minimum_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.minimum_length.get_name_leafdata())
                            if (self.operator.is_set or self.operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.operator.get_name_leafdata())
                            if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix.get_name_leafdata())
                            if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_length.get_name_leafdata())
                            if (self.remark.is_set or self.remark.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.remark.get_name_leafdata())
                            if (self.sequence.is_set or self.sequence.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sequence.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sequence-number" or name == "acl-name" or name == "grant" or name == "hits" or name == "item-type" or name == "maximum-length" or name == "minimum-length" or name == "operator" or name == "prefix" or name == "prefix-length" or name == "remark" or name == "sequence"):
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
                            if(value_path == "grant"):
                                self.grant = value
                                self.grant.value_namespace = name_space
                                self.grant.value_namespace_prefix = name_space_prefix
                            if(value_path == "hits"):
                                self.hits = value
                                self.hits.value_namespace = name_space
                                self.hits.value_namespace_prefix = name_space_prefix
                            if(value_path == "item-type"):
                                self.item_type = value
                                self.item_type.value_namespace = name_space
                                self.item_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "maximum-length"):
                                self.maximum_length = value
                                self.maximum_length.value_namespace = name_space
                                self.maximum_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "minimum-length"):
                                self.minimum_length = value
                                self.minimum_length.value_namespace = name_space
                                self.minimum_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "operator"):
                                self.operator = value
                                self.operator.value_namespace = name_space
                                self.operator.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix"):
                                self.prefix = value
                                self.prefix.value_namespace = name_space
                                self.prefix.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix-length"):
                                self.prefix_length = value
                                self.prefix_length.value_namespace = name_space
                                self.prefix_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "remark"):
                                self.remark = value
                                self.remark.value_namespace = name_space
                                self.remark.value_namespace_prefix = name_space_prefix
                            if(value_path == "sequence"):
                                self.sequence = value
                                self.sequence.value_namespace = name_space
                                self.sequence.value_namespace_prefix = name_space_prefix

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
                            c = Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence()
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
                        path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/access-list-manager/prefixes/%s" % self.get_segment_path()
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
                            self.prefix_list_sequences = Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences()
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
                    path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/access-list-manager/%s" % self.get_segment_path()
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
                    c = Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix()
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


        class Accesses(Entity):
            """
            Access listL class displaying Usage and Entries
            
            .. attribute:: access
            
            	Name of the Access List
            	**type**\: list of    :py:class:`Access <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv4AclAndPrefixList.AccessListManager.Accesses, self).__init__()

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
                            super(Ipv4AclAndPrefixList.AccessListManager.Accesses, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv4AclAndPrefixList.AccessListManager.Accesses, self).__setattr__(name, value)


            class Access(Entity):
                """
                Name of the Access List
                
                .. attribute:: access_list_name  <key>
                
                	Name of the Access List
                	**type**\:  str
                
                .. attribute:: access_list_sequences
                
                	Table of all the SequenceNumbers per access list
                	**type**\:   :py:class:`AccessListSequences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences>`
                
                .. attribute:: object_group
                
                	Object Group in an Access list
                	**type**\:   :py:class:`ObjectGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup>`
                
                

                """

                _prefix = 'ipv4-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access, self).__init__()

                    self.yang_name = "access"
                    self.yang_parent_name = "accesses"

                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                    self.access_list_sequences = Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences()
                    self.access_list_sequences.parent = self
                    self._children_name_map["access_list_sequences"] = "access-list-sequences"
                    self._children_yang_names.add("access-list-sequences")

                    self.object_group = Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup()
                    self.object_group.parent = self
                    self._children_name_map["object_group"] = "object-group"
                    self._children_yang_names.add("object-group")

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
                                super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access, self).__setattr__(name, value)


                class AccessListSequences(Entity):
                    """
                    Table of all the SequenceNumbers per access
                    list
                    
                    .. attribute:: access_list_sequence
                    
                    	Sequence Number of an access list entry
                    	**type**\: list of    :py:class:`AccessListSequence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence>`
                    
                    

                    """

                    _prefix = 'ipv4-acl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences, self).__init__()

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
                                    super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences, self).__setattr__(name, value)


                    class AccessListSequence(Entity):
                        """
                        Sequence Number of an access list entry
                        
                        .. attribute:: sequence_number  <key>
                        
                        	ACLEntry Sequence Number
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
                        
                        .. attribute:: destination_address
                        
                        	Destination address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: destination_address_mask
                        
                        	Destination mask
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: destination_operator
                        
                        	Destination operator
                        	**type**\:   :py:class:`AclPortOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperator>`
                        
                        .. attribute:: destination_port1
                        
                        	Destination port 1
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: destination_port2
                        
                        	Destination port 2
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: destination_port_group
                        
                        	Destination port object\-group
                        	**type**\:  str
                        
                        .. attribute:: destination_prefix_group
                        
                        	Destination prefix object\-group
                        	**type**\:  str
                        
                        .. attribute:: dscp
                        
                        	DSCP or DSCP range start
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: dscp2
                        
                        	DSCP Range End
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: dscp_operator
                        
                        	DSCP Operator
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: dscp_present
                        
                        	DSCP present
                        	**type**\:  bool
                        
                        .. attribute:: dynamic
                        
                        	Is dynamic ACE
                        	**type**\:  bool
                        
                        .. attribute:: fragment_offset1
                        
                        	Fragment offset 1
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: fragment_offset2
                        
                        	Fragment offset 2
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: fragment_offset_operator
                        
                        	Fragment offset operator
                        	**type**\:   :py:class:`AclPortOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperator>`
                        
                        .. attribute:: fragments
                        
                        	Fragments
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: grant
                        
                        	Permit/deny
                        	**type**\:   :py:class:`AclAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclAction>`
                        
                        .. attribute:: hits
                        
                        	Number of hits
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: hw_next_hop_info
                        
                        	HW Next hop info
                        	**type**\:   :py:class:`HwNextHopInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo>`
                        
                        .. attribute:: is_icmp_off
                        
                        	True if ICMP off
                        	**type**\:  bool
                        
                        .. attribute:: item_type
                        
                        	ACE type (acl, remark)
                        	**type**\:   :py:class:`AclAce1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclAce1>`
                        
                        .. attribute:: log_option
                        
                        	Log option
                        	**type**\:   :py:class:`AclLog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclLog>`
                        
                        .. attribute:: next_hop_info
                        
                        	Next hop info
                        	**type**\: list of    :py:class:`NextHopInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo>`
                        
                        .. attribute:: next_hop_type
                        
                        	Next hop type
                        	**type**\:   :py:class:`BagAclNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.BagAclNh>`
                        
                        .. attribute:: no_stats
                        
                        	No stats
                        	**type**\:  bool
                        
                        .. attribute:: packet_length1
                        
                        	Packet length 1
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: packet_length2
                        
                        	Packet length 2
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: packet_length_operator
                        
                        	Packet length operator
                        	**type**\:   :py:class:`AclPortOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperator>`
                        
                        .. attribute:: precedence
                        
                        	Precedence
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: precedence_present
                        
                        	Precedence present
                        	**type**\:  bool
                        
                        .. attribute:: protocol
                        
                        	IPv4 protocol type
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: protocol2
                        
                        	IPv4 protocol 2
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: protocol_operator
                        
                        	IPv4 protocol operator
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: qos_group
                        
                        	Qos group number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: remark
                        
                        	Remark String
                        	**type**\:  str
                        
                        .. attribute:: sequence
                        
                        	ACLE sequence number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sequence_str
                        
                        	Sequence String
                        	**type**\:  str
                        
                        .. attribute:: sorce_operator
                        
                        	Deprecated by Source operator
                        	**type**\:   :py:class:`AclPortOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperator>`
                        
                        .. attribute:: sorce_port1
                        
                        	Deprecated by SourcePort1
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: sorce_port2
                        
                        	Deprecated by SourcePort2
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: source_address
                        
                        	Source address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address_mask
                        
                        	Source mask
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_operator
                        
                        	Source operator
                        	**type**\:   :py:class:`AclPortOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperator>`
                        
                        .. attribute:: source_port1
                        
                        	Source port 1
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: source_port2
                        
                        	Source port 2
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: source_port_group
                        
                        	Source port object\-group
                        	**type**\:  str
                        
                        .. attribute:: source_prefix_group
                        
                        	Source prefix object\-group
                        	**type**\:  str
                        
                        .. attribute:: tcp_flags
                        
                        	TCP flags
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: tcp_flags_mask
                        
                        	TCP flags mask
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: tcp_flags_operator
                        
                        	TCP flags operator
                        	**type**\:   :py:class:`AclTcpflagsOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclTcpflagsOperator>`
                        
                        .. attribute:: ttl1
                        
                        	TTL 1
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: ttl2
                        
                        	TTL 2
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: ttl_operator
                        
                        	TTL operator
                        	**type**\:   :py:class:`AclPortOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperator>`
                        
                        .. attribute:: udf
                        
                        	UDF BAG
                        	**type**\: list of    :py:class:`Udf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf>`
                        
                        

                        """

                        _prefix = 'ipv4-acl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence, self).__init__()

                            self.yang_name = "access-list-sequence"
                            self.yang_parent_name = "access-list-sequences"

                            self.sequence_number = YLeaf(YType.uint32, "sequence-number")

                            self.acl_name = YLeaf(YType.str, "acl-name")

                            self.capture = YLeaf(YType.boolean, "capture")

                            self.counter_name = YLeaf(YType.str, "counter-name")

                            self.destination_address = YLeaf(YType.str, "destination-address")

                            self.destination_address_mask = YLeaf(YType.str, "destination-address-mask")

                            self.destination_operator = YLeaf(YType.enumeration, "destination-operator")

                            self.destination_port1 = YLeaf(YType.uint16, "destination-port1")

                            self.destination_port2 = YLeaf(YType.uint16, "destination-port2")

                            self.destination_port_group = YLeaf(YType.str, "destination-port-group")

                            self.destination_prefix_group = YLeaf(YType.str, "destination-prefix-group")

                            self.dscp = YLeaf(YType.uint8, "dscp")

                            self.dscp2 = YLeaf(YType.uint8, "dscp2")

                            self.dscp_operator = YLeaf(YType.uint8, "dscp-operator")

                            self.dscp_present = YLeaf(YType.boolean, "dscp-present")

                            self.dynamic = YLeaf(YType.boolean, "dynamic")

                            self.fragment_offset1 = YLeaf(YType.uint16, "fragment-offset1")

                            self.fragment_offset2 = YLeaf(YType.uint16, "fragment-offset2")

                            self.fragment_offset_operator = YLeaf(YType.enumeration, "fragment-offset-operator")

                            self.fragments = YLeaf(YType.uint8, "fragments")

                            self.grant = YLeaf(YType.enumeration, "grant")

                            self.hits = YLeaf(YType.uint64, "hits")

                            self.is_icmp_off = YLeaf(YType.boolean, "is-icmp-off")

                            self.item_type = YLeaf(YType.enumeration, "item-type")

                            self.log_option = YLeaf(YType.enumeration, "log-option")

                            self.next_hop_type = YLeaf(YType.enumeration, "next-hop-type")

                            self.no_stats = YLeaf(YType.boolean, "no-stats")

                            self.packet_length1 = YLeaf(YType.uint16, "packet-length1")

                            self.packet_length2 = YLeaf(YType.uint16, "packet-length2")

                            self.packet_length_operator = YLeaf(YType.enumeration, "packet-length-operator")

                            self.precedence = YLeaf(YType.uint8, "precedence")

                            self.precedence_present = YLeaf(YType.boolean, "precedence-present")

                            self.protocol = YLeaf(YType.uint16, "protocol")

                            self.protocol2 = YLeaf(YType.uint16, "protocol2")

                            self.protocol_operator = YLeaf(YType.uint16, "protocol-operator")

                            self.qos_group = YLeaf(YType.uint16, "qos-group")

                            self.remark = YLeaf(YType.str, "remark")

                            self.sequence = YLeaf(YType.uint32, "sequence")

                            self.sequence_str = YLeaf(YType.str, "sequence-str")

                            self.sorce_operator = YLeaf(YType.enumeration, "sorce-operator")

                            self.sorce_port1 = YLeaf(YType.uint16, "sorce-port1")

                            self.sorce_port2 = YLeaf(YType.uint16, "sorce-port2")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.source_address_mask = YLeaf(YType.str, "source-address-mask")

                            self.source_operator = YLeaf(YType.enumeration, "source-operator")

                            self.source_port1 = YLeaf(YType.uint16, "source-port1")

                            self.source_port2 = YLeaf(YType.uint16, "source-port2")

                            self.source_port_group = YLeaf(YType.str, "source-port-group")

                            self.source_prefix_group = YLeaf(YType.str, "source-prefix-group")

                            self.tcp_flags = YLeaf(YType.uint8, "tcp-flags")

                            self.tcp_flags_mask = YLeaf(YType.uint8, "tcp-flags-mask")

                            self.tcp_flags_operator = YLeaf(YType.enumeration, "tcp-flags-operator")

                            self.ttl1 = YLeaf(YType.uint16, "ttl1")

                            self.ttl2 = YLeaf(YType.uint16, "ttl2")

                            self.ttl_operator = YLeaf(YType.enumeration, "ttl-operator")

                            self.hw_next_hop_info = Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo()
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
                                            "destination_address",
                                            "destination_address_mask",
                                            "destination_operator",
                                            "destination_port1",
                                            "destination_port2",
                                            "destination_port_group",
                                            "destination_prefix_group",
                                            "dscp",
                                            "dscp2",
                                            "dscp_operator",
                                            "dscp_present",
                                            "dynamic",
                                            "fragment_offset1",
                                            "fragment_offset2",
                                            "fragment_offset_operator",
                                            "fragments",
                                            "grant",
                                            "hits",
                                            "is_icmp_off",
                                            "item_type",
                                            "log_option",
                                            "next_hop_type",
                                            "no_stats",
                                            "packet_length1",
                                            "packet_length2",
                                            "packet_length_operator",
                                            "precedence",
                                            "precedence_present",
                                            "protocol",
                                            "protocol2",
                                            "protocol_operator",
                                            "qos_group",
                                            "remark",
                                            "sequence",
                                            "sequence_str",
                                            "sorce_operator",
                                            "sorce_port1",
                                            "sorce_port2",
                                            "source_address",
                                            "source_address_mask",
                                            "source_operator",
                                            "source_port1",
                                            "source_port2",
                                            "source_port_group",
                                            "source_prefix_group",
                                            "tcp_flags",
                                            "tcp_flags_mask",
                                            "tcp_flags_operator",
                                            "ttl1",
                                            "ttl2",
                                            "ttl_operator") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence, self).__setattr__(name, value)


                        class HwNextHopInfo(Entity):
                            """
                            HW Next hop info
                            
                            .. attribute:: next_hop
                            
                            	The Next Hop
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type
                            
                            	the next\-hop type
                            	**type**\:   :py:class:`BagAclNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.BagAclNh>`
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            	**length:** 0..32
                            
                            

                            """

                            _prefix = 'ipv4-acl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo, self).__init__()

                                self.yang_name = "hw-next-hop-info"
                                self.yang_parent_name = "access-list-sequence"

                                self.next_hop = YLeaf(YType.uint32, "next-hop")

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
                                                "type",
                                                "vrf_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.next_hop.is_set or
                                    self.type.is_set or
                                    self.vrf_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.next_hop.yfilter != YFilter.not_set or
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
                                if(name == "next-hop" or name == "type" or name == "vrf-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "next-hop"):
                                    self.next_hop = value
                                    self.next_hop.value_namespace = name_space
                                    self.next_hop.value_namespace_prefix = name_space_prefix
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
                            
                            .. attribute:: at_status
                            
                            	The next hop at status
                            	**type**\:   :py:class:`BagAclNhAtStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.BagAclNhAtStatus>`
                            
                            .. attribute:: is_acl_next_hop_exist
                            
                            	The nexthop exist
                            	**type**\:  bool
                            
                            .. attribute:: next_hop
                            
                            	The next hop
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: status
                            
                            	The next hop status
                            	**type**\:   :py:class:`BagAclNhStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.BagAclNhStatus>`
                            
                            .. attribute:: track_name
                            
                            	Track name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ipv4-acl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo, self).__init__()

                                self.yang_name = "next-hop-info"
                                self.yang_parent_name = "access-list-sequence"

                                self.at_status = YLeaf(YType.enumeration, "at-status")

                                self.is_acl_next_hop_exist = YLeaf(YType.boolean, "is-acl-next-hop-exist")

                                self.next_hop = YLeaf(YType.str, "next-hop")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.track_name = YLeaf(YType.str, "track-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("at_status",
                                                "is_acl_next_hop_exist",
                                                "next_hop",
                                                "status",
                                                "track_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.at_status.is_set or
                                    self.is_acl_next_hop_exist.is_set or
                                    self.next_hop.is_set or
                                    self.status.is_set or
                                    self.track_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.at_status.yfilter != YFilter.not_set or
                                    self.is_acl_next_hop_exist.yfilter != YFilter.not_set or
                                    self.next_hop.yfilter != YFilter.not_set or
                                    self.status.yfilter != YFilter.not_set or
                                    self.track_name.yfilter != YFilter.not_set)

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
                                if (self.at_status.is_set or self.at_status.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.at_status.get_name_leafdata())
                                if (self.is_acl_next_hop_exist.is_set or self.is_acl_next_hop_exist.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_acl_next_hop_exist.get_name_leafdata())
                                if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.next_hop.get_name_leafdata())
                                if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.status.get_name_leafdata())
                                if (self.track_name.is_set or self.track_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.track_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "at-status" or name == "is-acl-next-hop-exist" or name == "next-hop" or name == "status" or name == "track-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "at-status"):
                                    self.at_status = value
                                    self.at_status.value_namespace = name_space
                                    self.at_status.value_namespace_prefix = name_space_prefix
                                if(value_path == "is-acl-next-hop-exist"):
                                    self.is_acl_next_hop_exist = value
                                    self.is_acl_next_hop_exist.value_namespace = name_space
                                    self.is_acl_next_hop_exist.value_namespace_prefix = name_space_prefix
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


                        class Udf(Entity):
                            """
                            UDF BAG
                            
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

                            _prefix = 'ipv4-acl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf, self).__init__()

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
                                            super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf, self).__setattr__(name, value)

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
                                self.destination_address.is_set or
                                self.destination_address_mask.is_set or
                                self.destination_operator.is_set or
                                self.destination_port1.is_set or
                                self.destination_port2.is_set or
                                self.destination_port_group.is_set or
                                self.destination_prefix_group.is_set or
                                self.dscp.is_set or
                                self.dscp2.is_set or
                                self.dscp_operator.is_set or
                                self.dscp_present.is_set or
                                self.dynamic.is_set or
                                self.fragment_offset1.is_set or
                                self.fragment_offset2.is_set or
                                self.fragment_offset_operator.is_set or
                                self.fragments.is_set or
                                self.grant.is_set or
                                self.hits.is_set or
                                self.is_icmp_off.is_set or
                                self.item_type.is_set or
                                self.log_option.is_set or
                                self.next_hop_type.is_set or
                                self.no_stats.is_set or
                                self.packet_length1.is_set or
                                self.packet_length2.is_set or
                                self.packet_length_operator.is_set or
                                self.precedence.is_set or
                                self.precedence_present.is_set or
                                self.protocol.is_set or
                                self.protocol2.is_set or
                                self.protocol_operator.is_set or
                                self.qos_group.is_set or
                                self.remark.is_set or
                                self.sequence.is_set or
                                self.sequence_str.is_set or
                                self.sorce_operator.is_set or
                                self.sorce_port1.is_set or
                                self.sorce_port2.is_set or
                                self.source_address.is_set or
                                self.source_address_mask.is_set or
                                self.source_operator.is_set or
                                self.source_port1.is_set or
                                self.source_port2.is_set or
                                self.source_port_group.is_set or
                                self.source_prefix_group.is_set or
                                self.tcp_flags.is_set or
                                self.tcp_flags_mask.is_set or
                                self.tcp_flags_operator.is_set or
                                self.ttl1.is_set or
                                self.ttl2.is_set or
                                self.ttl_operator.is_set or
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
                                self.destination_address.yfilter != YFilter.not_set or
                                self.destination_address_mask.yfilter != YFilter.not_set or
                                self.destination_operator.yfilter != YFilter.not_set or
                                self.destination_port1.yfilter != YFilter.not_set or
                                self.destination_port2.yfilter != YFilter.not_set or
                                self.destination_port_group.yfilter != YFilter.not_set or
                                self.destination_prefix_group.yfilter != YFilter.not_set or
                                self.dscp.yfilter != YFilter.not_set or
                                self.dscp2.yfilter != YFilter.not_set or
                                self.dscp_operator.yfilter != YFilter.not_set or
                                self.dscp_present.yfilter != YFilter.not_set or
                                self.dynamic.yfilter != YFilter.not_set or
                                self.fragment_offset1.yfilter != YFilter.not_set or
                                self.fragment_offset2.yfilter != YFilter.not_set or
                                self.fragment_offset_operator.yfilter != YFilter.not_set or
                                self.fragments.yfilter != YFilter.not_set or
                                self.grant.yfilter != YFilter.not_set or
                                self.hits.yfilter != YFilter.not_set or
                                self.is_icmp_off.yfilter != YFilter.not_set or
                                self.item_type.yfilter != YFilter.not_set or
                                self.log_option.yfilter != YFilter.not_set or
                                self.next_hop_type.yfilter != YFilter.not_set or
                                self.no_stats.yfilter != YFilter.not_set or
                                self.packet_length1.yfilter != YFilter.not_set or
                                self.packet_length2.yfilter != YFilter.not_set or
                                self.packet_length_operator.yfilter != YFilter.not_set or
                                self.precedence.yfilter != YFilter.not_set or
                                self.precedence_present.yfilter != YFilter.not_set or
                                self.protocol.yfilter != YFilter.not_set or
                                self.protocol2.yfilter != YFilter.not_set or
                                self.protocol_operator.yfilter != YFilter.not_set or
                                self.qos_group.yfilter != YFilter.not_set or
                                self.remark.yfilter != YFilter.not_set or
                                self.sequence.yfilter != YFilter.not_set or
                                self.sequence_str.yfilter != YFilter.not_set or
                                self.sorce_operator.yfilter != YFilter.not_set or
                                self.sorce_port1.yfilter != YFilter.not_set or
                                self.sorce_port2.yfilter != YFilter.not_set or
                                self.source_address.yfilter != YFilter.not_set or
                                self.source_address_mask.yfilter != YFilter.not_set or
                                self.source_operator.yfilter != YFilter.not_set or
                                self.source_port1.yfilter != YFilter.not_set or
                                self.source_port2.yfilter != YFilter.not_set or
                                self.source_port_group.yfilter != YFilter.not_set or
                                self.source_prefix_group.yfilter != YFilter.not_set or
                                self.tcp_flags.yfilter != YFilter.not_set or
                                self.tcp_flags_mask.yfilter != YFilter.not_set or
                                self.tcp_flags_operator.yfilter != YFilter.not_set or
                                self.ttl1.yfilter != YFilter.not_set or
                                self.ttl2.yfilter != YFilter.not_set or
                                self.ttl_operator.yfilter != YFilter.not_set or
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
                            if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_address.get_name_leafdata())
                            if (self.destination_address_mask.is_set or self.destination_address_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_address_mask.get_name_leafdata())
                            if (self.destination_operator.is_set or self.destination_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_operator.get_name_leafdata())
                            if (self.destination_port1.is_set or self.destination_port1.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_port1.get_name_leafdata())
                            if (self.destination_port2.is_set or self.destination_port2.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_port2.get_name_leafdata())
                            if (self.destination_port_group.is_set or self.destination_port_group.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_port_group.get_name_leafdata())
                            if (self.destination_prefix_group.is_set or self.destination_prefix_group.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_prefix_group.get_name_leafdata())
                            if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dscp.get_name_leafdata())
                            if (self.dscp2.is_set or self.dscp2.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dscp2.get_name_leafdata())
                            if (self.dscp_operator.is_set or self.dscp_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dscp_operator.get_name_leafdata())
                            if (self.dscp_present.is_set or self.dscp_present.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dscp_present.get_name_leafdata())
                            if (self.dynamic.is_set or self.dynamic.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dynamic.get_name_leafdata())
                            if (self.fragment_offset1.is_set or self.fragment_offset1.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fragment_offset1.get_name_leafdata())
                            if (self.fragment_offset2.is_set or self.fragment_offset2.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fragment_offset2.get_name_leafdata())
                            if (self.fragment_offset_operator.is_set or self.fragment_offset_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fragment_offset_operator.get_name_leafdata())
                            if (self.fragments.is_set or self.fragments.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fragments.get_name_leafdata())
                            if (self.grant.is_set or self.grant.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.grant.get_name_leafdata())
                            if (self.hits.is_set or self.hits.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hits.get_name_leafdata())
                            if (self.is_icmp_off.is_set or self.is_icmp_off.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_icmp_off.get_name_leafdata())
                            if (self.item_type.is_set or self.item_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.item_type.get_name_leafdata())
                            if (self.log_option.is_set or self.log_option.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.log_option.get_name_leafdata())
                            if (self.next_hop_type.is_set or self.next_hop_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_hop_type.get_name_leafdata())
                            if (self.no_stats.is_set or self.no_stats.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_stats.get_name_leafdata())
                            if (self.packet_length1.is_set or self.packet_length1.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packet_length1.get_name_leafdata())
                            if (self.packet_length2.is_set or self.packet_length2.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packet_length2.get_name_leafdata())
                            if (self.packet_length_operator.is_set or self.packet_length_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packet_length_operator.get_name_leafdata())
                            if (self.precedence.is_set or self.precedence.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.precedence.get_name_leafdata())
                            if (self.precedence_present.is_set or self.precedence_present.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.precedence_present.get_name_leafdata())
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
                            if (self.sequence.is_set or self.sequence.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sequence.get_name_leafdata())
                            if (self.sequence_str.is_set or self.sequence_str.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sequence_str.get_name_leafdata())
                            if (self.sorce_operator.is_set or self.sorce_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sorce_operator.get_name_leafdata())
                            if (self.sorce_port1.is_set or self.sorce_port1.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sorce_port1.get_name_leafdata())
                            if (self.sorce_port2.is_set or self.sorce_port2.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sorce_port2.get_name_leafdata())
                            if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address.get_name_leafdata())
                            if (self.source_address_mask.is_set or self.source_address_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address_mask.get_name_leafdata())
                            if (self.source_operator.is_set or self.source_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_operator.get_name_leafdata())
                            if (self.source_port1.is_set or self.source_port1.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_port1.get_name_leafdata())
                            if (self.source_port2.is_set or self.source_port2.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_port2.get_name_leafdata())
                            if (self.source_port_group.is_set or self.source_port_group.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_port_group.get_name_leafdata())
                            if (self.source_prefix_group.is_set or self.source_prefix_group.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_prefix_group.get_name_leafdata())
                            if (self.tcp_flags.is_set or self.tcp_flags.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tcp_flags.get_name_leafdata())
                            if (self.tcp_flags_mask.is_set or self.tcp_flags_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tcp_flags_mask.get_name_leafdata())
                            if (self.tcp_flags_operator.is_set or self.tcp_flags_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tcp_flags_operator.get_name_leafdata())
                            if (self.ttl1.is_set or self.ttl1.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ttl1.get_name_leafdata())
                            if (self.ttl2.is_set or self.ttl2.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ttl2.get_name_leafdata())
                            if (self.ttl_operator.is_set or self.ttl_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ttl_operator.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "hw-next-hop-info"):
                                if (self.hw_next_hop_info is None):
                                    self.hw_next_hop_info = Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo()
                                    self.hw_next_hop_info.parent = self
                                    self._children_name_map["hw_next_hop_info"] = "hw-next-hop-info"
                                return self.hw_next_hop_info

                            if (child_yang_name == "next-hop-info"):
                                for c in self.next_hop_info:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo()
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
                                c = Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.udf.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "hw-next-hop-info" or name == "next-hop-info" or name == "udf" or name == "sequence-number" or name == "acl-name" or name == "capture" or name == "counter-name" or name == "destination-address" or name == "destination-address-mask" or name == "destination-operator" or name == "destination-port1" or name == "destination-port2" or name == "destination-port-group" or name == "destination-prefix-group" or name == "dscp" or name == "dscp2" or name == "dscp-operator" or name == "dscp-present" or name == "dynamic" or name == "fragment-offset1" or name == "fragment-offset2" or name == "fragment-offset-operator" or name == "fragments" or name == "grant" or name == "hits" or name == "is-icmp-off" or name == "item-type" or name == "log-option" or name == "next-hop-type" or name == "no-stats" or name == "packet-length1" or name == "packet-length2" or name == "packet-length-operator" or name == "precedence" or name == "precedence-present" or name == "protocol" or name == "protocol2" or name == "protocol-operator" or name == "qos-group" or name == "remark" or name == "sequence" or name == "sequence-str" or name == "sorce-operator" or name == "sorce-port1" or name == "sorce-port2" or name == "source-address" or name == "source-address-mask" or name == "source-operator" or name == "source-port1" or name == "source-port2" or name == "source-port-group" or name == "source-prefix-group" or name == "tcp-flags" or name == "tcp-flags-mask" or name == "tcp-flags-operator" or name == "ttl1" or name == "ttl2" or name == "ttl-operator"):
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
                            if(value_path == "destination-address"):
                                self.destination_address = value
                                self.destination_address.value_namespace = name_space
                                self.destination_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-address-mask"):
                                self.destination_address_mask = value
                                self.destination_address_mask.value_namespace = name_space
                                self.destination_address_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-operator"):
                                self.destination_operator = value
                                self.destination_operator.value_namespace = name_space
                                self.destination_operator.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-port1"):
                                self.destination_port1 = value
                                self.destination_port1.value_namespace = name_space
                                self.destination_port1.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-port2"):
                                self.destination_port2 = value
                                self.destination_port2.value_namespace = name_space
                                self.destination_port2.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-port-group"):
                                self.destination_port_group = value
                                self.destination_port_group.value_namespace = name_space
                                self.destination_port_group.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-prefix-group"):
                                self.destination_prefix_group = value
                                self.destination_prefix_group.value_namespace = name_space
                                self.destination_prefix_group.value_namespace_prefix = name_space_prefix
                            if(value_path == "dscp"):
                                self.dscp = value
                                self.dscp.value_namespace = name_space
                                self.dscp.value_namespace_prefix = name_space_prefix
                            if(value_path == "dscp2"):
                                self.dscp2 = value
                                self.dscp2.value_namespace = name_space
                                self.dscp2.value_namespace_prefix = name_space_prefix
                            if(value_path == "dscp-operator"):
                                self.dscp_operator = value
                                self.dscp_operator.value_namespace = name_space
                                self.dscp_operator.value_namespace_prefix = name_space_prefix
                            if(value_path == "dscp-present"):
                                self.dscp_present = value
                                self.dscp_present.value_namespace = name_space
                                self.dscp_present.value_namespace_prefix = name_space_prefix
                            if(value_path == "dynamic"):
                                self.dynamic = value
                                self.dynamic.value_namespace = name_space
                                self.dynamic.value_namespace_prefix = name_space_prefix
                            if(value_path == "fragment-offset1"):
                                self.fragment_offset1 = value
                                self.fragment_offset1.value_namespace = name_space
                                self.fragment_offset1.value_namespace_prefix = name_space_prefix
                            if(value_path == "fragment-offset2"):
                                self.fragment_offset2 = value
                                self.fragment_offset2.value_namespace = name_space
                                self.fragment_offset2.value_namespace_prefix = name_space_prefix
                            if(value_path == "fragment-offset-operator"):
                                self.fragment_offset_operator = value
                                self.fragment_offset_operator.value_namespace = name_space
                                self.fragment_offset_operator.value_namespace_prefix = name_space_prefix
                            if(value_path == "fragments"):
                                self.fragments = value
                                self.fragments.value_namespace = name_space
                                self.fragments.value_namespace_prefix = name_space_prefix
                            if(value_path == "grant"):
                                self.grant = value
                                self.grant.value_namespace = name_space
                                self.grant.value_namespace_prefix = name_space_prefix
                            if(value_path == "hits"):
                                self.hits = value
                                self.hits.value_namespace = name_space
                                self.hits.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-icmp-off"):
                                self.is_icmp_off = value
                                self.is_icmp_off.value_namespace = name_space
                                self.is_icmp_off.value_namespace_prefix = name_space_prefix
                            if(value_path == "item-type"):
                                self.item_type = value
                                self.item_type.value_namespace = name_space
                                self.item_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "log-option"):
                                self.log_option = value
                                self.log_option.value_namespace = name_space
                                self.log_option.value_namespace_prefix = name_space_prefix
                            if(value_path == "next-hop-type"):
                                self.next_hop_type = value
                                self.next_hop_type.value_namespace = name_space
                                self.next_hop_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-stats"):
                                self.no_stats = value
                                self.no_stats.value_namespace = name_space
                                self.no_stats.value_namespace_prefix = name_space_prefix
                            if(value_path == "packet-length1"):
                                self.packet_length1 = value
                                self.packet_length1.value_namespace = name_space
                                self.packet_length1.value_namespace_prefix = name_space_prefix
                            if(value_path == "packet-length2"):
                                self.packet_length2 = value
                                self.packet_length2.value_namespace = name_space
                                self.packet_length2.value_namespace_prefix = name_space_prefix
                            if(value_path == "packet-length-operator"):
                                self.packet_length_operator = value
                                self.packet_length_operator.value_namespace = name_space
                                self.packet_length_operator.value_namespace_prefix = name_space_prefix
                            if(value_path == "precedence"):
                                self.precedence = value
                                self.precedence.value_namespace = name_space
                                self.precedence.value_namespace_prefix = name_space_prefix
                            if(value_path == "precedence-present"):
                                self.precedence_present = value
                                self.precedence_present.value_namespace = name_space
                                self.precedence_present.value_namespace_prefix = name_space_prefix
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
                            if(value_path == "sequence"):
                                self.sequence = value
                                self.sequence.value_namespace = name_space
                                self.sequence.value_namespace_prefix = name_space_prefix
                            if(value_path == "sequence-str"):
                                self.sequence_str = value
                                self.sequence_str.value_namespace = name_space
                                self.sequence_str.value_namespace_prefix = name_space_prefix
                            if(value_path == "sorce-operator"):
                                self.sorce_operator = value
                                self.sorce_operator.value_namespace = name_space
                                self.sorce_operator.value_namespace_prefix = name_space_prefix
                            if(value_path == "sorce-port1"):
                                self.sorce_port1 = value
                                self.sorce_port1.value_namespace = name_space
                                self.sorce_port1.value_namespace_prefix = name_space_prefix
                            if(value_path == "sorce-port2"):
                                self.sorce_port2 = value
                                self.sorce_port2.value_namespace = name_space
                                self.sorce_port2.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address"):
                                self.source_address = value
                                self.source_address.value_namespace = name_space
                                self.source_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address-mask"):
                                self.source_address_mask = value
                                self.source_address_mask.value_namespace = name_space
                                self.source_address_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-operator"):
                                self.source_operator = value
                                self.source_operator.value_namespace = name_space
                                self.source_operator.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-port1"):
                                self.source_port1 = value
                                self.source_port1.value_namespace = name_space
                                self.source_port1.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-port2"):
                                self.source_port2 = value
                                self.source_port2.value_namespace = name_space
                                self.source_port2.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-port-group"):
                                self.source_port_group = value
                                self.source_port_group.value_namespace = name_space
                                self.source_port_group.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-prefix-group"):
                                self.source_prefix_group = value
                                self.source_prefix_group.value_namespace = name_space
                                self.source_prefix_group.value_namespace_prefix = name_space_prefix
                            if(value_path == "tcp-flags"):
                                self.tcp_flags = value
                                self.tcp_flags.value_namespace = name_space
                                self.tcp_flags.value_namespace_prefix = name_space_prefix
                            if(value_path == "tcp-flags-mask"):
                                self.tcp_flags_mask = value
                                self.tcp_flags_mask.value_namespace = name_space
                                self.tcp_flags_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "tcp-flags-operator"):
                                self.tcp_flags_operator = value
                                self.tcp_flags_operator.value_namespace = name_space
                                self.tcp_flags_operator.value_namespace_prefix = name_space_prefix
                            if(value_path == "ttl1"):
                                self.ttl1 = value
                                self.ttl1.value_namespace = name_space
                                self.ttl1.value_namespace_prefix = name_space_prefix
                            if(value_path == "ttl2"):
                                self.ttl2 = value
                                self.ttl2.value_namespace = name_space
                                self.ttl2.value_namespace_prefix = name_space_prefix
                            if(value_path == "ttl-operator"):
                                self.ttl_operator = value
                                self.ttl_operator.value_namespace = name_space
                                self.ttl_operator.value_namespace_prefix = name_space_prefix

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
                            c = Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence()
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


                class ObjectGroup(Entity):
                    """
                    Object Group in an Access list
                    
                    .. attribute:: obj_grp_info
                    
                    	Object\-group info
                    	**type**\: list of    :py:class:`ObjGrpInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup.ObjGrpInfo>`
                    
                    

                    """

                    _prefix = 'ipv4-acl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup, self).__init__()

                        self.yang_name = "object-group"
                        self.yang_parent_name = "access"

                        self.obj_grp_info = YList(self)

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
                                    super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup, self).__setattr__(name, value)


                    class ObjGrpInfo(Entity):
                        """
                        Object\-group info
                        
                        .. attribute:: obj_grp_name
                        
                        	Object\-group name
                        	**type**\:  str
                        
                        	**length:** 0..64
                        
                        .. attribute:: obj_grp_type
                        
                        	Object\-group Type
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-acl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup.ObjGrpInfo, self).__init__()

                            self.yang_name = "obj-grp-info"
                            self.yang_parent_name = "object-group"

                            self.obj_grp_name = YLeaf(YType.str, "obj-grp-name")

                            self.obj_grp_type = YLeaf(YType.uint32, "obj-grp-type")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("obj_grp_name",
                                            "obj_grp_type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup.ObjGrpInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup.ObjGrpInfo, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.obj_grp_name.is_set or
                                self.obj_grp_type.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.obj_grp_name.yfilter != YFilter.not_set or
                                self.obj_grp_type.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "obj-grp-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.obj_grp_name.is_set or self.obj_grp_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.obj_grp_name.get_name_leafdata())
                            if (self.obj_grp_type.is_set or self.obj_grp_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.obj_grp_type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "obj-grp-name" or name == "obj-grp-type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "obj-grp-name"):
                                self.obj_grp_name = value
                                self.obj_grp_name.value_namespace = name_space
                                self.obj_grp_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "obj-grp-type"):
                                self.obj_grp_type = value
                                self.obj_grp_type.value_namespace = name_space
                                self.obj_grp_type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.obj_grp_info:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.obj_grp_info:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "object-group" + path_buffer

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

                        if (child_yang_name == "obj-grp-info"):
                            for c in self.obj_grp_info:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup.ObjGrpInfo()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.obj_grp_info.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "obj-grp-info"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.access_list_name.is_set or
                        (self.access_list_sequences is not None and self.access_list_sequences.has_data()) or
                        (self.object_group is not None and self.object_group.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.access_list_name.yfilter != YFilter.not_set or
                        (self.access_list_sequences is not None and self.access_list_sequences.has_operation()) or
                        (self.object_group is not None and self.object_group.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "access" + "[access-list-name='" + self.access_list_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/access-list-manager/accesses/%s" % self.get_segment_path()
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
                            self.access_list_sequences = Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences()
                            self.access_list_sequences.parent = self
                            self._children_name_map["access_list_sequences"] = "access-list-sequences"
                        return self.access_list_sequences

                    if (child_yang_name == "object-group"):
                        if (self.object_group is None):
                            self.object_group = Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup()
                            self.object_group.parent = self
                            self._children_name_map["object_group"] = "object-group"
                        return self.object_group

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "access-list-sequences" or name == "object-group" or name == "access-list-name"):
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
                    path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/access-list-manager/%s" % self.get_segment_path()
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
                    c = Ipv4AclAndPrefixList.AccessListManager.Accesses.Access()
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


        class Usages(Entity):
            """
            Table of Usage statistics of access lists at
            different nodes
            
            .. attribute:: usage
            
            	Usage statistics of an access list at a node
            	**type**\: list of    :py:class:`Usage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Usages.Usage>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv4AclAndPrefixList.AccessListManager.Usages, self).__init__()

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
                            super(Ipv4AclAndPrefixList.AccessListManager.Usages, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv4AclAndPrefixList.AccessListManager.Usages, self).__setattr__(name, value)


            class Usage(Entity):
                """
                Usage statistics of an access list at a node
                
                .. attribute:: access_list_name
                
                	Name of the access list
                	**type**\:  str
                
                .. attribute:: application_id
                
                	Application ID
                	**type**\:   :py:class:`AclUsageAppIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_common_acl_datatypes.AclUsageAppIdEnum>`
                
                .. attribute:: node_name
                
                	Node where access list is applied
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: usage_details
                
                	Usage Statistics Details
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ipv4-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.AccessListManager.Usages.Usage, self).__init__()

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
                                super(Ipv4AclAndPrefixList.AccessListManager.Usages.Usage, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4AclAndPrefixList.AccessListManager.Usages.Usage, self).__setattr__(name, value)

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
                        path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/access-list-manager/usages/%s" % self.get_segment_path()
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
                    path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/access-list-manager/%s" % self.get_segment_path()
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
                    c = Ipv4AclAndPrefixList.AccessListManager.Usages.Usage()
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
                path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/%s" % self.get_segment_path()
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
                    self.accesses = Ipv4AclAndPrefixList.AccessListManager.Accesses()
                    self.accesses.parent = self
                    self._children_name_map["accesses"] = "accesses"
                return self.accesses

            if (child_yang_name == "prefixes"):
                if (self.prefixes is None):
                    self.prefixes = Ipv4AclAndPrefixList.AccessListManager.Prefixes()
                    self.prefixes.parent = self
                    self._children_name_map["prefixes"] = "prefixes"
                return self.prefixes

            if (child_yang_name == "usages"):
                if (self.usages is None):
                    self.usages = Ipv4AclAndPrefixList.AccessListManager.Usages()
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
        
        	Resource limits pertaining to access lists only
        	**type**\:   :py:class:`AccessListSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.AccessListSummary>`
        
        .. attribute:: details
        
        	Details of the Overall Out Of Resources Limits
        	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.Details>`
        
        .. attribute:: oor_accesses
        
        	Resource occupation details for access lists
        	**type**\:   :py:class:`OorAccesses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.OorAccesses>`
        
        .. attribute:: oor_prefixes
        
        	Resource occupation details for prefix lists
        	**type**\:   :py:class:`OorPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.OorPrefixes>`
        
        .. attribute:: prefix_list_summary
        
        	Summary of the prefix Lists resource utilization
        	**type**\:   :py:class:`PrefixListSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.PrefixListSummary>`
        
        

        """

        _prefix = 'ipv4-acl-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv4AclAndPrefixList.Oor, self).__init__()

            self.yang_name = "oor"
            self.yang_parent_name = "ipv4-acl-and-prefix-list"

            self.access_list_summary = Ipv4AclAndPrefixList.Oor.AccessListSummary()
            self.access_list_summary.parent = self
            self._children_name_map["access_list_summary"] = "access-list-summary"
            self._children_yang_names.add("access-list-summary")

            self.details = Ipv4AclAndPrefixList.Oor.Details()
            self.details.parent = self
            self._children_name_map["details"] = "details"
            self._children_yang_names.add("details")

            self.oor_accesses = Ipv4AclAndPrefixList.Oor.OorAccesses()
            self.oor_accesses.parent = self
            self._children_name_map["oor_accesses"] = "oor-accesses"
            self._children_yang_names.add("oor-accesses")

            self.oor_prefixes = Ipv4AclAndPrefixList.Oor.OorPrefixes()
            self.oor_prefixes.parent = self
            self._children_name_map["oor_prefixes"] = "oor-prefixes"
            self._children_yang_names.add("oor-prefixes")

            self.prefix_list_summary = Ipv4AclAndPrefixList.Oor.PrefixListSummary()
            self.prefix_list_summary.parent = self
            self._children_name_map["prefix_list_summary"] = "prefix-list-summary"
            self._children_yang_names.add("prefix-list-summary")


        class Details(Entity):
            """
            Details of the Overall Out Of Resources Limits
            
            .. attribute:: current_configured_ac_es
            
            	Current configured aces
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: current_configured_ac_ls
            
            	Current configured acls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: current_max_configurable_ac_es
            
            	Current max configurable aces
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: current_max_configurable_ac_ls
            
            	Current max configurable acls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: default_max_ac_es
            
            	default max configurable aces
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: default_max_ac_ls
            
            	default max configurable acls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_configurable_ac_es
            
            	max configurable aces
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_configurable_ac_ls
            
            	max configurable acls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv4AclAndPrefixList.Oor.Details, self).__init__()

                self.yang_name = "details"
                self.yang_parent_name = "oor"

                self.current_configured_ac_es = YLeaf(YType.uint32, "current-configured-ac-es")

                self.current_configured_ac_ls = YLeaf(YType.uint32, "current-configured-ac-ls")

                self.current_max_configurable_ac_es = YLeaf(YType.uint32, "current-max-configurable-ac-es")

                self.current_max_configurable_ac_ls = YLeaf(YType.uint32, "current-max-configurable-ac-ls")

                self.default_max_ac_es = YLeaf(YType.uint32, "default-max-ac-es")

                self.default_max_ac_ls = YLeaf(YType.uint32, "default-max-ac-ls")

                self.max_configurable_ac_es = YLeaf(YType.uint32, "max-configurable-ac-es")

                self.max_configurable_ac_ls = YLeaf(YType.uint32, "max-configurable-ac-ls")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("current_configured_ac_es",
                                "current_configured_ac_ls",
                                "current_max_configurable_ac_es",
                                "current_max_configurable_ac_ls",
                                "default_max_ac_es",
                                "default_max_ac_ls",
                                "max_configurable_ac_es",
                                "max_configurable_ac_ls") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ipv4AclAndPrefixList.Oor.Details, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv4AclAndPrefixList.Oor.Details, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.current_configured_ac_es.is_set or
                    self.current_configured_ac_ls.is_set or
                    self.current_max_configurable_ac_es.is_set or
                    self.current_max_configurable_ac_ls.is_set or
                    self.default_max_ac_es.is_set or
                    self.default_max_ac_ls.is_set or
                    self.max_configurable_ac_es.is_set or
                    self.max_configurable_ac_ls.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.current_configured_ac_es.yfilter != YFilter.not_set or
                    self.current_configured_ac_ls.yfilter != YFilter.not_set or
                    self.current_max_configurable_ac_es.yfilter != YFilter.not_set or
                    self.current_max_configurable_ac_ls.yfilter != YFilter.not_set or
                    self.default_max_ac_es.yfilter != YFilter.not_set or
                    self.default_max_ac_ls.yfilter != YFilter.not_set or
                    self.max_configurable_ac_es.yfilter != YFilter.not_set or
                    self.max_configurable_ac_ls.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "details" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.current_configured_ac_es.is_set or self.current_configured_ac_es.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.current_configured_ac_es.get_name_leafdata())
                if (self.current_configured_ac_ls.is_set or self.current_configured_ac_ls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.current_configured_ac_ls.get_name_leafdata())
                if (self.current_max_configurable_ac_es.is_set or self.current_max_configurable_ac_es.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.current_max_configurable_ac_es.get_name_leafdata())
                if (self.current_max_configurable_ac_ls.is_set or self.current_max_configurable_ac_ls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.current_max_configurable_ac_ls.get_name_leafdata())
                if (self.default_max_ac_es.is_set or self.default_max_ac_es.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.default_max_ac_es.get_name_leafdata())
                if (self.default_max_ac_ls.is_set or self.default_max_ac_ls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.default_max_ac_ls.get_name_leafdata())
                if (self.max_configurable_ac_es.is_set or self.max_configurable_ac_es.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_configurable_ac_es.get_name_leafdata())
                if (self.max_configurable_ac_ls.is_set or self.max_configurable_ac_ls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_configurable_ac_ls.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "current-configured-ac-es" or name == "current-configured-ac-ls" or name == "current-max-configurable-ac-es" or name == "current-max-configurable-ac-ls" or name == "default-max-ac-es" or name == "default-max-ac-ls" or name == "max-configurable-ac-es" or name == "max-configurable-ac-ls"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "current-configured-ac-es"):
                    self.current_configured_ac_es = value
                    self.current_configured_ac_es.value_namespace = name_space
                    self.current_configured_ac_es.value_namespace_prefix = name_space_prefix
                if(value_path == "current-configured-ac-ls"):
                    self.current_configured_ac_ls = value
                    self.current_configured_ac_ls.value_namespace = name_space
                    self.current_configured_ac_ls.value_namespace_prefix = name_space_prefix
                if(value_path == "current-max-configurable-ac-es"):
                    self.current_max_configurable_ac_es = value
                    self.current_max_configurable_ac_es.value_namespace = name_space
                    self.current_max_configurable_ac_es.value_namespace_prefix = name_space_prefix
                if(value_path == "current-max-configurable-ac-ls"):
                    self.current_max_configurable_ac_ls = value
                    self.current_max_configurable_ac_ls.value_namespace = name_space
                    self.current_max_configurable_ac_ls.value_namespace_prefix = name_space_prefix
                if(value_path == "default-max-ac-es"):
                    self.default_max_ac_es = value
                    self.default_max_ac_es.value_namespace = name_space
                    self.default_max_ac_es.value_namespace_prefix = name_space_prefix
                if(value_path == "default-max-ac-ls"):
                    self.default_max_ac_ls = value
                    self.default_max_ac_ls.value_namespace = name_space
                    self.default_max_ac_ls.value_namespace_prefix = name_space_prefix
                if(value_path == "max-configurable-ac-es"):
                    self.max_configurable_ac_es = value
                    self.max_configurable_ac_es.value_namespace = name_space
                    self.max_configurable_ac_es.value_namespace_prefix = name_space_prefix
                if(value_path == "max-configurable-ac-ls"):
                    self.max_configurable_ac_ls = value
                    self.max_configurable_ac_ls.value_namespace = name_space
                    self.max_configurable_ac_ls.value_namespace_prefix = name_space_prefix


        class OorPrefixes(Entity):
            """
            Resource occupation details for prefix lists
            
            .. attribute:: oor_prefix
            
            	Resource occupation details for a particular prefix list
            	**type**\: list of    :py:class:`OorPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.OorPrefixes.OorPrefix>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv4AclAndPrefixList.Oor.OorPrefixes, self).__init__()

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
                            super(Ipv4AclAndPrefixList.Oor.OorPrefixes, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv4AclAndPrefixList.Oor.OorPrefixes, self).__setattr__(name, value)


            class OorPrefix(Entity):
                """
                Resource occupation details for a particular
                prefix list
                
                .. attribute:: prefix_list_name  <key>
                
                	Name of a prefix list
                	**type**\:  str
                
                .. attribute:: current_configured_ac_es
                
                	Current configured aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_configured_ac_ls
                
                	Current configured acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_max_configurable_ac_es
                
                	Current max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_max_configurable_ac_ls
                
                	Current max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: default_max_ac_es
                
                	default max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: default_max_ac_ls
                
                	default max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_configurable_ac_es
                
                	max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_configurable_ac_ls
                
                	max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.Oor.OorPrefixes.OorPrefix, self).__init__()

                    self.yang_name = "oor-prefix"
                    self.yang_parent_name = "oor-prefixes"

                    self.prefix_list_name = YLeaf(YType.str, "prefix-list-name")

                    self.current_configured_ac_es = YLeaf(YType.uint32, "current-configured-ac-es")

                    self.current_configured_ac_ls = YLeaf(YType.uint32, "current-configured-ac-ls")

                    self.current_max_configurable_ac_es = YLeaf(YType.uint32, "current-max-configurable-ac-es")

                    self.current_max_configurable_ac_ls = YLeaf(YType.uint32, "current-max-configurable-ac-ls")

                    self.default_max_ac_es = YLeaf(YType.uint32, "default-max-ac-es")

                    self.default_max_ac_ls = YLeaf(YType.uint32, "default-max-ac-ls")

                    self.max_configurable_ac_es = YLeaf(YType.uint32, "max-configurable-ac-es")

                    self.max_configurable_ac_ls = YLeaf(YType.uint32, "max-configurable-ac-ls")

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
                                    "current_configured_ac_es",
                                    "current_configured_ac_ls",
                                    "current_max_configurable_ac_es",
                                    "current_max_configurable_ac_ls",
                                    "default_max_ac_es",
                                    "default_max_ac_ls",
                                    "max_configurable_ac_es",
                                    "max_configurable_ac_ls") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv4AclAndPrefixList.Oor.OorPrefixes.OorPrefix, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4AclAndPrefixList.Oor.OorPrefixes.OorPrefix, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.prefix_list_name.is_set or
                        self.current_configured_ac_es.is_set or
                        self.current_configured_ac_ls.is_set or
                        self.current_max_configurable_ac_es.is_set or
                        self.current_max_configurable_ac_ls.is_set or
                        self.default_max_ac_es.is_set or
                        self.default_max_ac_ls.is_set or
                        self.max_configurable_ac_es.is_set or
                        self.max_configurable_ac_ls.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.prefix_list_name.yfilter != YFilter.not_set or
                        self.current_configured_ac_es.yfilter != YFilter.not_set or
                        self.current_configured_ac_ls.yfilter != YFilter.not_set or
                        self.current_max_configurable_ac_es.yfilter != YFilter.not_set or
                        self.current_max_configurable_ac_ls.yfilter != YFilter.not_set or
                        self.default_max_ac_es.yfilter != YFilter.not_set or
                        self.default_max_ac_ls.yfilter != YFilter.not_set or
                        self.max_configurable_ac_es.yfilter != YFilter.not_set or
                        self.max_configurable_ac_ls.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "oor-prefix" + "[prefix-list-name='" + self.prefix_list_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/oor-prefixes/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.prefix_list_name.is_set or self.prefix_list_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_list_name.get_name_leafdata())
                    if (self.current_configured_ac_es.is_set or self.current_configured_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_configured_ac_es.get_name_leafdata())
                    if (self.current_configured_ac_ls.is_set or self.current_configured_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_configured_ac_ls.get_name_leafdata())
                    if (self.current_max_configurable_ac_es.is_set or self.current_max_configurable_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_max_configurable_ac_es.get_name_leafdata())
                    if (self.current_max_configurable_ac_ls.is_set or self.current_max_configurable_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_max_configurable_ac_ls.get_name_leafdata())
                    if (self.default_max_ac_es.is_set or self.default_max_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.default_max_ac_es.get_name_leafdata())
                    if (self.default_max_ac_ls.is_set or self.default_max_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.default_max_ac_ls.get_name_leafdata())
                    if (self.max_configurable_ac_es.is_set or self.max_configurable_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_configurable_ac_es.get_name_leafdata())
                    if (self.max_configurable_ac_ls.is_set or self.max_configurable_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_configurable_ac_ls.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "prefix-list-name" or name == "current-configured-ac-es" or name == "current-configured-ac-ls" or name == "current-max-configurable-ac-es" or name == "current-max-configurable-ac-ls" or name == "default-max-ac-es" or name == "default-max-ac-ls" or name == "max-configurable-ac-es" or name == "max-configurable-ac-ls"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "prefix-list-name"):
                        self.prefix_list_name = value
                        self.prefix_list_name.value_namespace = name_space
                        self.prefix_list_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-configured-ac-es"):
                        self.current_configured_ac_es = value
                        self.current_configured_ac_es.value_namespace = name_space
                        self.current_configured_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-configured-ac-ls"):
                        self.current_configured_ac_ls = value
                        self.current_configured_ac_ls.value_namespace = name_space
                        self.current_configured_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-max-configurable-ac-es"):
                        self.current_max_configurable_ac_es = value
                        self.current_max_configurable_ac_es.value_namespace = name_space
                        self.current_max_configurable_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-max-configurable-ac-ls"):
                        self.current_max_configurable_ac_ls = value
                        self.current_max_configurable_ac_ls.value_namespace = name_space
                        self.current_max_configurable_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "default-max-ac-es"):
                        self.default_max_ac_es = value
                        self.default_max_ac_es.value_namespace = name_space
                        self.default_max_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "default-max-ac-ls"):
                        self.default_max_ac_ls = value
                        self.default_max_ac_ls.value_namespace = name_space
                        self.default_max_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-configurable-ac-es"):
                        self.max_configurable_ac_es = value
                        self.max_configurable_ac_es.value_namespace = name_space
                        self.max_configurable_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-configurable-ac-ls"):
                        self.max_configurable_ac_ls = value
                        self.max_configurable_ac_ls.value_namespace = name_space
                        self.max_configurable_ac_ls.value_namespace_prefix = name_space_prefix

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
                    path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/%s" % self.get_segment_path()
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
                    c = Ipv4AclAndPrefixList.Oor.OorPrefixes.OorPrefix()
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


        class OorAccesses(Entity):
            """
            Resource occupation details for access lists
            
            .. attribute:: oor_access
            
            	Resource occupation details for a particular access list
            	**type**\: list of    :py:class:`OorAccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.OorAccesses.OorAccess>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv4AclAndPrefixList.Oor.OorAccesses, self).__init__()

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
                            super(Ipv4AclAndPrefixList.Oor.OorAccesses, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv4AclAndPrefixList.Oor.OorAccesses, self).__setattr__(name, value)


            class OorAccess(Entity):
                """
                Resource occupation details for a particular
                access list
                
                .. attribute:: access_list_name  <key>
                
                	Name of the Access List
                	**type**\:  str
                
                .. attribute:: current_configured_ac_es
                
                	Current configured aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_configured_ac_ls
                
                	Current configured acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_max_configurable_ac_es
                
                	Current max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_max_configurable_ac_ls
                
                	Current max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: default_max_ac_es
                
                	default max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: default_max_ac_ls
                
                	default max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_configurable_ac_es
                
                	max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_configurable_ac_ls
                
                	max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.Oor.OorAccesses.OorAccess, self).__init__()

                    self.yang_name = "oor-access"
                    self.yang_parent_name = "oor-accesses"

                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                    self.current_configured_ac_es = YLeaf(YType.uint32, "current-configured-ac-es")

                    self.current_configured_ac_ls = YLeaf(YType.uint32, "current-configured-ac-ls")

                    self.current_max_configurable_ac_es = YLeaf(YType.uint32, "current-max-configurable-ac-es")

                    self.current_max_configurable_ac_ls = YLeaf(YType.uint32, "current-max-configurable-ac-ls")

                    self.default_max_ac_es = YLeaf(YType.uint32, "default-max-ac-es")

                    self.default_max_ac_ls = YLeaf(YType.uint32, "default-max-ac-ls")

                    self.max_configurable_ac_es = YLeaf(YType.uint32, "max-configurable-ac-es")

                    self.max_configurable_ac_ls = YLeaf(YType.uint32, "max-configurable-ac-ls")

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
                                    "current_configured_ac_es",
                                    "current_configured_ac_ls",
                                    "current_max_configurable_ac_es",
                                    "current_max_configurable_ac_ls",
                                    "default_max_ac_es",
                                    "default_max_ac_ls",
                                    "max_configurable_ac_es",
                                    "max_configurable_ac_ls") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv4AclAndPrefixList.Oor.OorAccesses.OorAccess, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4AclAndPrefixList.Oor.OorAccesses.OorAccess, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.access_list_name.is_set or
                        self.current_configured_ac_es.is_set or
                        self.current_configured_ac_ls.is_set or
                        self.current_max_configurable_ac_es.is_set or
                        self.current_max_configurable_ac_ls.is_set or
                        self.default_max_ac_es.is_set or
                        self.default_max_ac_ls.is_set or
                        self.max_configurable_ac_es.is_set or
                        self.max_configurable_ac_ls.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.access_list_name.yfilter != YFilter.not_set or
                        self.current_configured_ac_es.yfilter != YFilter.not_set or
                        self.current_configured_ac_ls.yfilter != YFilter.not_set or
                        self.current_max_configurable_ac_es.yfilter != YFilter.not_set or
                        self.current_max_configurable_ac_ls.yfilter != YFilter.not_set or
                        self.default_max_ac_es.yfilter != YFilter.not_set or
                        self.default_max_ac_ls.yfilter != YFilter.not_set or
                        self.max_configurable_ac_es.yfilter != YFilter.not_set or
                        self.max_configurable_ac_ls.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "oor-access" + "[access-list-name='" + self.access_list_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/oor-accesses/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_list_name.get_name_leafdata())
                    if (self.current_configured_ac_es.is_set or self.current_configured_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_configured_ac_es.get_name_leafdata())
                    if (self.current_configured_ac_ls.is_set or self.current_configured_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_configured_ac_ls.get_name_leafdata())
                    if (self.current_max_configurable_ac_es.is_set or self.current_max_configurable_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_max_configurable_ac_es.get_name_leafdata())
                    if (self.current_max_configurable_ac_ls.is_set or self.current_max_configurable_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_max_configurable_ac_ls.get_name_leafdata())
                    if (self.default_max_ac_es.is_set or self.default_max_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.default_max_ac_es.get_name_leafdata())
                    if (self.default_max_ac_ls.is_set or self.default_max_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.default_max_ac_ls.get_name_leafdata())
                    if (self.max_configurable_ac_es.is_set or self.max_configurable_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_configurable_ac_es.get_name_leafdata())
                    if (self.max_configurable_ac_ls.is_set or self.max_configurable_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_configurable_ac_ls.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "access-list-name" or name == "current-configured-ac-es" or name == "current-configured-ac-ls" or name == "current-max-configurable-ac-es" or name == "current-max-configurable-ac-ls" or name == "default-max-ac-es" or name == "default-max-ac-ls" or name == "max-configurable-ac-es" or name == "max-configurable-ac-ls"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "access-list-name"):
                        self.access_list_name = value
                        self.access_list_name.value_namespace = name_space
                        self.access_list_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-configured-ac-es"):
                        self.current_configured_ac_es = value
                        self.current_configured_ac_es.value_namespace = name_space
                        self.current_configured_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-configured-ac-ls"):
                        self.current_configured_ac_ls = value
                        self.current_configured_ac_ls.value_namespace = name_space
                        self.current_configured_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-max-configurable-ac-es"):
                        self.current_max_configurable_ac_es = value
                        self.current_max_configurable_ac_es.value_namespace = name_space
                        self.current_max_configurable_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-max-configurable-ac-ls"):
                        self.current_max_configurable_ac_ls = value
                        self.current_max_configurable_ac_ls.value_namespace = name_space
                        self.current_max_configurable_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "default-max-ac-es"):
                        self.default_max_ac_es = value
                        self.default_max_ac_es.value_namespace = name_space
                        self.default_max_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "default-max-ac-ls"):
                        self.default_max_ac_ls = value
                        self.default_max_ac_ls.value_namespace = name_space
                        self.default_max_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-configurable-ac-es"):
                        self.max_configurable_ac_es = value
                        self.max_configurable_ac_es.value_namespace = name_space
                        self.max_configurable_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-configurable-ac-ls"):
                        self.max_configurable_ac_ls = value
                        self.max_configurable_ac_ls.value_namespace = name_space
                        self.max_configurable_ac_ls.value_namespace_prefix = name_space_prefix

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
                    path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/%s" % self.get_segment_path()
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
                    c = Ipv4AclAndPrefixList.Oor.OorAccesses.OorAccess()
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


        class AccessListSummary(Entity):
            """
            Resource limits pertaining to access lists only
            
            .. attribute:: details
            
            	Details containing the resource limits of the access lists
            	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.AccessListSummary.Details>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv4AclAndPrefixList.Oor.AccessListSummary, self).__init__()

                self.yang_name = "access-list-summary"
                self.yang_parent_name = "oor"

                self.details = Ipv4AclAndPrefixList.Oor.AccessListSummary.Details()
                self.details.parent = self
                self._children_name_map["details"] = "details"
                self._children_yang_names.add("details")


            class Details(Entity):
                """
                Details containing the resource limits of the
                access lists
                
                .. attribute:: current_configured_ac_es
                
                	Current configured aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_configured_ac_ls
                
                	Current configured acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_max_configurable_ac_es
                
                	Current max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_max_configurable_ac_ls
                
                	Current max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: default_max_ac_es
                
                	default max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: default_max_ac_ls
                
                	default max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_configurable_ac_es
                
                	max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_configurable_ac_ls
                
                	max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.Oor.AccessListSummary.Details, self).__init__()

                    self.yang_name = "details"
                    self.yang_parent_name = "access-list-summary"

                    self.current_configured_ac_es = YLeaf(YType.uint32, "current-configured-ac-es")

                    self.current_configured_ac_ls = YLeaf(YType.uint32, "current-configured-ac-ls")

                    self.current_max_configurable_ac_es = YLeaf(YType.uint32, "current-max-configurable-ac-es")

                    self.current_max_configurable_ac_ls = YLeaf(YType.uint32, "current-max-configurable-ac-ls")

                    self.default_max_ac_es = YLeaf(YType.uint32, "default-max-ac-es")

                    self.default_max_ac_ls = YLeaf(YType.uint32, "default-max-ac-ls")

                    self.max_configurable_ac_es = YLeaf(YType.uint32, "max-configurable-ac-es")

                    self.max_configurable_ac_ls = YLeaf(YType.uint32, "max-configurable-ac-ls")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("current_configured_ac_es",
                                    "current_configured_ac_ls",
                                    "current_max_configurable_ac_es",
                                    "current_max_configurable_ac_ls",
                                    "default_max_ac_es",
                                    "default_max_ac_ls",
                                    "max_configurable_ac_es",
                                    "max_configurable_ac_ls") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv4AclAndPrefixList.Oor.AccessListSummary.Details, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4AclAndPrefixList.Oor.AccessListSummary.Details, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.current_configured_ac_es.is_set or
                        self.current_configured_ac_ls.is_set or
                        self.current_max_configurable_ac_es.is_set or
                        self.current_max_configurable_ac_ls.is_set or
                        self.default_max_ac_es.is_set or
                        self.default_max_ac_ls.is_set or
                        self.max_configurable_ac_es.is_set or
                        self.max_configurable_ac_ls.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.current_configured_ac_es.yfilter != YFilter.not_set or
                        self.current_configured_ac_ls.yfilter != YFilter.not_set or
                        self.current_max_configurable_ac_es.yfilter != YFilter.not_set or
                        self.current_max_configurable_ac_ls.yfilter != YFilter.not_set or
                        self.default_max_ac_es.yfilter != YFilter.not_set or
                        self.default_max_ac_ls.yfilter != YFilter.not_set or
                        self.max_configurable_ac_es.yfilter != YFilter.not_set or
                        self.max_configurable_ac_ls.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "details" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/access-list-summary/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.current_configured_ac_es.is_set or self.current_configured_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_configured_ac_es.get_name_leafdata())
                    if (self.current_configured_ac_ls.is_set or self.current_configured_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_configured_ac_ls.get_name_leafdata())
                    if (self.current_max_configurable_ac_es.is_set or self.current_max_configurable_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_max_configurable_ac_es.get_name_leafdata())
                    if (self.current_max_configurable_ac_ls.is_set or self.current_max_configurable_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_max_configurable_ac_ls.get_name_leafdata())
                    if (self.default_max_ac_es.is_set or self.default_max_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.default_max_ac_es.get_name_leafdata())
                    if (self.default_max_ac_ls.is_set or self.default_max_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.default_max_ac_ls.get_name_leafdata())
                    if (self.max_configurable_ac_es.is_set or self.max_configurable_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_configurable_ac_es.get_name_leafdata())
                    if (self.max_configurable_ac_ls.is_set or self.max_configurable_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_configurable_ac_ls.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "current-configured-ac-es" or name == "current-configured-ac-ls" or name == "current-max-configurable-ac-es" or name == "current-max-configurable-ac-ls" or name == "default-max-ac-es" or name == "default-max-ac-ls" or name == "max-configurable-ac-es" or name == "max-configurable-ac-ls"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "current-configured-ac-es"):
                        self.current_configured_ac_es = value
                        self.current_configured_ac_es.value_namespace = name_space
                        self.current_configured_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-configured-ac-ls"):
                        self.current_configured_ac_ls = value
                        self.current_configured_ac_ls.value_namespace = name_space
                        self.current_configured_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-max-configurable-ac-es"):
                        self.current_max_configurable_ac_es = value
                        self.current_max_configurable_ac_es.value_namespace = name_space
                        self.current_max_configurable_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-max-configurable-ac-ls"):
                        self.current_max_configurable_ac_ls = value
                        self.current_max_configurable_ac_ls.value_namespace = name_space
                        self.current_max_configurable_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "default-max-ac-es"):
                        self.default_max_ac_es = value
                        self.default_max_ac_es.value_namespace = name_space
                        self.default_max_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "default-max-ac-ls"):
                        self.default_max_ac_ls = value
                        self.default_max_ac_ls.value_namespace = name_space
                        self.default_max_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-configurable-ac-es"):
                        self.max_configurable_ac_es = value
                        self.max_configurable_ac_es.value_namespace = name_space
                        self.max_configurable_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-configurable-ac-ls"):
                        self.max_configurable_ac_ls = value
                        self.max_configurable_ac_ls.value_namespace = name_space
                        self.max_configurable_ac_ls.value_namespace_prefix = name_space_prefix

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
                    path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/%s" % self.get_segment_path()
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
                        self.details = Ipv4AclAndPrefixList.Oor.AccessListSummary.Details()
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


        class PrefixListSummary(Entity):
            """
            Summary of the prefix Lists resource
            utilization
            
            .. attribute:: details
            
            	Summary Detail of the prefix list Resource Utilisation
            	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.PrefixListSummary.Details>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv4AclAndPrefixList.Oor.PrefixListSummary, self).__init__()

                self.yang_name = "prefix-list-summary"
                self.yang_parent_name = "oor"

                self.details = Ipv4AclAndPrefixList.Oor.PrefixListSummary.Details()
                self.details.parent = self
                self._children_name_map["details"] = "details"
                self._children_yang_names.add("details")


            class Details(Entity):
                """
                Summary Detail of the prefix list Resource
                Utilisation
                
                .. attribute:: current_configured_ac_es
                
                	Current configured aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_configured_ac_ls
                
                	Current configured acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_max_configurable_ac_es
                
                	Current max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_max_configurable_ac_ls
                
                	Current max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: default_max_ac_es
                
                	default max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: default_max_ac_ls
                
                	default max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_configurable_ac_es
                
                	max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_configurable_ac_ls
                
                	max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.Oor.PrefixListSummary.Details, self).__init__()

                    self.yang_name = "details"
                    self.yang_parent_name = "prefix-list-summary"

                    self.current_configured_ac_es = YLeaf(YType.uint32, "current-configured-ac-es")

                    self.current_configured_ac_ls = YLeaf(YType.uint32, "current-configured-ac-ls")

                    self.current_max_configurable_ac_es = YLeaf(YType.uint32, "current-max-configurable-ac-es")

                    self.current_max_configurable_ac_ls = YLeaf(YType.uint32, "current-max-configurable-ac-ls")

                    self.default_max_ac_es = YLeaf(YType.uint32, "default-max-ac-es")

                    self.default_max_ac_ls = YLeaf(YType.uint32, "default-max-ac-ls")

                    self.max_configurable_ac_es = YLeaf(YType.uint32, "max-configurable-ac-es")

                    self.max_configurable_ac_ls = YLeaf(YType.uint32, "max-configurable-ac-ls")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("current_configured_ac_es",
                                    "current_configured_ac_ls",
                                    "current_max_configurable_ac_es",
                                    "current_max_configurable_ac_ls",
                                    "default_max_ac_es",
                                    "default_max_ac_ls",
                                    "max_configurable_ac_es",
                                    "max_configurable_ac_ls") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv4AclAndPrefixList.Oor.PrefixListSummary.Details, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4AclAndPrefixList.Oor.PrefixListSummary.Details, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.current_configured_ac_es.is_set or
                        self.current_configured_ac_ls.is_set or
                        self.current_max_configurable_ac_es.is_set or
                        self.current_max_configurable_ac_ls.is_set or
                        self.default_max_ac_es.is_set or
                        self.default_max_ac_ls.is_set or
                        self.max_configurable_ac_es.is_set or
                        self.max_configurable_ac_ls.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.current_configured_ac_es.yfilter != YFilter.not_set or
                        self.current_configured_ac_ls.yfilter != YFilter.not_set or
                        self.current_max_configurable_ac_es.yfilter != YFilter.not_set or
                        self.current_max_configurable_ac_ls.yfilter != YFilter.not_set or
                        self.default_max_ac_es.yfilter != YFilter.not_set or
                        self.default_max_ac_ls.yfilter != YFilter.not_set or
                        self.max_configurable_ac_es.yfilter != YFilter.not_set or
                        self.max_configurable_ac_ls.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "details" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/prefix-list-summary/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.current_configured_ac_es.is_set or self.current_configured_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_configured_ac_es.get_name_leafdata())
                    if (self.current_configured_ac_ls.is_set or self.current_configured_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_configured_ac_ls.get_name_leafdata())
                    if (self.current_max_configurable_ac_es.is_set or self.current_max_configurable_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_max_configurable_ac_es.get_name_leafdata())
                    if (self.current_max_configurable_ac_ls.is_set or self.current_max_configurable_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_max_configurable_ac_ls.get_name_leafdata())
                    if (self.default_max_ac_es.is_set or self.default_max_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.default_max_ac_es.get_name_leafdata())
                    if (self.default_max_ac_ls.is_set or self.default_max_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.default_max_ac_ls.get_name_leafdata())
                    if (self.max_configurable_ac_es.is_set or self.max_configurable_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_configurable_ac_es.get_name_leafdata())
                    if (self.max_configurable_ac_ls.is_set or self.max_configurable_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_configurable_ac_ls.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "current-configured-ac-es" or name == "current-configured-ac-ls" or name == "current-max-configurable-ac-es" or name == "current-max-configurable-ac-ls" or name == "default-max-ac-es" or name == "default-max-ac-ls" or name == "max-configurable-ac-es" or name == "max-configurable-ac-ls"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "current-configured-ac-es"):
                        self.current_configured_ac_es = value
                        self.current_configured_ac_es.value_namespace = name_space
                        self.current_configured_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-configured-ac-ls"):
                        self.current_configured_ac_ls = value
                        self.current_configured_ac_ls.value_namespace = name_space
                        self.current_configured_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-max-configurable-ac-es"):
                        self.current_max_configurable_ac_es = value
                        self.current_max_configurable_ac_es.value_namespace = name_space
                        self.current_max_configurable_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-max-configurable-ac-ls"):
                        self.current_max_configurable_ac_ls = value
                        self.current_max_configurable_ac_ls.value_namespace = name_space
                        self.current_max_configurable_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "default-max-ac-es"):
                        self.default_max_ac_es = value
                        self.default_max_ac_es.value_namespace = name_space
                        self.default_max_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "default-max-ac-ls"):
                        self.default_max_ac_ls = value
                        self.default_max_ac_ls.value_namespace = name_space
                        self.default_max_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-configurable-ac-es"):
                        self.max_configurable_ac_es = value
                        self.max_configurable_ac_es.value_namespace = name_space
                        self.max_configurable_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-configurable-ac-ls"):
                        self.max_configurable_ac_ls = value
                        self.max_configurable_ac_ls.value_namespace = name_space
                        self.max_configurable_ac_ls.value_namespace_prefix = name_space_prefix

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
                    path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/%s" % self.get_segment_path()
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
                        self.details = Ipv4AclAndPrefixList.Oor.PrefixListSummary.Details()
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
                path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/%s" % self.get_segment_path()
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
                    self.access_list_summary = Ipv4AclAndPrefixList.Oor.AccessListSummary()
                    self.access_list_summary.parent = self
                    self._children_name_map["access_list_summary"] = "access-list-summary"
                return self.access_list_summary

            if (child_yang_name == "details"):
                if (self.details is None):
                    self.details = Ipv4AclAndPrefixList.Oor.Details()
                    self.details.parent = self
                    self._children_name_map["details"] = "details"
                return self.details

            if (child_yang_name == "oor-accesses"):
                if (self.oor_accesses is None):
                    self.oor_accesses = Ipv4AclAndPrefixList.Oor.OorAccesses()
                    self.oor_accesses.parent = self
                    self._children_name_map["oor_accesses"] = "oor-accesses"
                return self.oor_accesses

            if (child_yang_name == "oor-prefixes"):
                if (self.oor_prefixes is None):
                    self.oor_prefixes = Ipv4AclAndPrefixList.Oor.OorPrefixes()
                    self.oor_prefixes.parent = self
                    self._children_name_map["oor_prefixes"] = "oor-prefixes"
                return self.oor_prefixes

            if (child_yang_name == "prefix-list-summary"):
                if (self.prefix_list_summary is None):
                    self.prefix_list_summary = Ipv4AclAndPrefixList.Oor.PrefixListSummary()
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
        path_buffer = "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list" + path_buffer

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
                self.access_list_manager = Ipv4AclAndPrefixList.AccessListManager()
                self.access_list_manager.parent = self
                self._children_name_map["access_list_manager"] = "access-list-manager"
            return self.access_list_manager

        if (child_yang_name == "oor"):
            if (self.oor is None):
                self.oor = Ipv4AclAndPrefixList.Oor()
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
        self._top_entity = Ipv4AclAndPrefixList()
        return self._top_entity

