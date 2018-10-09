""" Cisco_IOS_XR_ipv6_acl_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-acl package operational data.

This module contains definitions
for the following management objects\:
  ipv6\-acl\-and\-prefix\-list\: Root class of IPv6 Oper schema tree

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AclAce1(Enum):
    """
    AclAce1 (Enum Class)

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


class AclAce1_(Enum):
    """
    AclAce1\_ (Enum Class)

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
    AclAction (Enum Class)

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
    AclLog (Enum Class)

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
    AclPortOperator (Enum Class)

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


class AclPortOperator_(Enum):
    """
    AclPortOperator\_ (Enum Class)

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


class AclPortOperator__(Enum):
    """
    AclPortOperator\_\_ (Enum Class)

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


class AclPortOperator___(Enum):
    """
    AclPortOperator\_\_\_ (Enum Class)

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
    AclTcpflagsOperator (Enum Class)

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
    BagAclNh (Enum Class)

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
    BagAclNhAtStatus (Enum Class)

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
    BagAclNhStatus (Enum Class)

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
    	**type**\:  :py:class:`AccessListManager <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager>`
    
    .. attribute:: oor
    
    	Out Of Resources, Limits to the resources allocatable
    	**type**\:  :py:class:`Oor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor>`
    
    

    """

    _prefix = 'ipv6-acl-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(Ipv6AclAndPrefixList, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-acl-and-prefix-list"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-acl-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("access-list-manager", ("access_list_manager", Ipv6AclAndPrefixList.AccessListManager)), ("oor", ("oor", Ipv6AclAndPrefixList.Oor))])
        self._leafs = OrderedDict()

        self.access_list_manager = Ipv6AclAndPrefixList.AccessListManager()
        self.access_list_manager.parent = self
        self._children_name_map["access_list_manager"] = "access-list-manager"

        self.oor = Ipv6AclAndPrefixList.Oor()
        self.oor.parent = self
        self._children_name_map["oor"] = "oor"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv6AclAndPrefixList, [], name, value)


    class AccessListManager(Entity):
        """
        AccessListManager containing ACLs and prefix
        lists
        
        .. attribute:: prefixes
        
        	Table of prefix lists
        	**type**\:  :py:class:`Prefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Prefixes>`
        
        .. attribute:: usages
        
        	Table of Usage statistics of ACLs at different nodes
        	**type**\:  :py:class:`Usages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Usages>`
        
        .. attribute:: accesses
        
        	ACL class displaying Usage and Entries
        	**type**\:  :py:class:`Accesses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses>`
        
        

        """

        _prefix = 'ipv6-acl-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv6AclAndPrefixList.AccessListManager, self).__init__()

            self.yang_name = "access-list-manager"
            self.yang_parent_name = "ipv6-acl-and-prefix-list"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("prefixes", ("prefixes", Ipv6AclAndPrefixList.AccessListManager.Prefixes)), ("usages", ("usages", Ipv6AclAndPrefixList.AccessListManager.Usages)), ("accesses", ("accesses", Ipv6AclAndPrefixList.AccessListManager.Accesses))])
            self._leafs = OrderedDict()

            self.prefixes = Ipv6AclAndPrefixList.AccessListManager.Prefixes()
            self.prefixes.parent = self
            self._children_name_map["prefixes"] = "prefixes"

            self.usages = Ipv6AclAndPrefixList.AccessListManager.Usages()
            self.usages.parent = self
            self._children_name_map["usages"] = "usages"

            self.accesses = Ipv6AclAndPrefixList.AccessListManager.Accesses()
            self.accesses.parent = self
            self._children_name_map["accesses"] = "accesses"
            self._segment_path = lambda: "access-list-manager"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6AclAndPrefixList.AccessListManager, [], name, value)


        class Prefixes(Entity):
            """
            Table of prefix lists
            
            .. attribute:: prefix
            
            	Name of the prefix list
            	**type**\: list of  		 :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv6AclAndPrefixList.AccessListManager.Prefixes, self).__init__()

                self.yang_name = "prefixes"
                self.yang_parent_name = "access-list-manager"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("prefix", ("prefix", Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix))])
                self._leafs = OrderedDict()

                self.prefix = YList(self)
                self._segment_path = lambda: "prefixes"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/access-list-manager/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6AclAndPrefixList.AccessListManager.Prefixes, [], name, value)


            class Prefix(Entity):
                """
                Name of the prefix list
                
                .. attribute:: prefix_list_name  (key)
                
                	Name of the prefix list
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: prefix_list_sequences
                
                	Table of all the SequenceNumbers per prefix list
                	**type**\:  :py:class:`PrefixListSequences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences>`
                
                

                """

                _prefix = 'ipv6-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix, self).__init__()

                    self.yang_name = "prefix"
                    self.yang_parent_name = "prefixes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['prefix_list_name']
                    self._child_classes = OrderedDict([("prefix-list-sequences", ("prefix_list_sequences", Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences))])
                    self._leafs = OrderedDict([
                        ('prefix_list_name', (YLeaf(YType.str, 'prefix-list-name'), ['str'])),
                    ])
                    self.prefix_list_name = None

                    self.prefix_list_sequences = Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences()
                    self.prefix_list_sequences.parent = self
                    self._children_name_map["prefix_list_sequences"] = "prefix-list-sequences"
                    self._segment_path = lambda: "prefix" + "[prefix-list-name='" + str(self.prefix_list_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/access-list-manager/prefixes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix, ['prefix_list_name'], name, value)


                class PrefixListSequences(Entity):
                    """
                    Table of all the SequenceNumbers per prefix
                    list
                    
                    .. attribute:: prefix_list_sequence
                    
                    	Sequence Number of a prefix list entry
                    	**type**\: list of  		 :py:class:`PrefixListSequence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence>`
                    
                    

                    """

                    _prefix = 'ipv6-acl-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences, self).__init__()

                        self.yang_name = "prefix-list-sequences"
                        self.yang_parent_name = "prefix"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("prefix-list-sequence", ("prefix_list_sequence", Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence))])
                        self._leafs = OrderedDict()

                        self.prefix_list_sequence = YList(self)
                        self._segment_path = lambda: "prefix-list-sequences"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences, [], name, value)


                    class PrefixListSequence(Entity):
                        """
                        Sequence Number of a prefix list entry
                        
                        .. attribute:: sequence_number  (key)
                        
                        	Sequence Number of the prefix list entry
                        	**type**\: int
                        
                        	**range:** 1..2147483646
                        
                        .. attribute:: is_ace_type
                        
                        	ACE type (acl, remark)
                        	**type**\:  :py:class:`AclAce1_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclAce1_>`
                        
                        .. attribute:: is_ace_sequence_number
                        
                        	ACLE sequence number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_packet_allow_or_deny
                        
                        	Grant value permit/deny 
                        	**type**\:  :py:class:`AclAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclAction>`
                        
                        .. attribute:: is_address_in_numbers
                        
                        	IPv6 prefix
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: is_address_mask_length
                        
                        	Prefix length 
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_length_operator
                        
                        	Port Operator
                        	**type**\:  :py:class:`AclPortOperator___ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperator___>`
                        
                        .. attribute:: is_packet_minimum_length
                        
                        	Min length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_packet_maximum_length
                        
                        	Maximum length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hits
                        
                        	Number of hits
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_comment_for_entry
                        
                        	Remark String
                        	**type**\: str
                        
                        .. attribute:: acl_name
                        
                        	ACL Name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ipv6-acl-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence, self).__init__()

                            self.yang_name = "prefix-list-sequence"
                            self.yang_parent_name = "prefix-list-sequences"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['sequence_number']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sequence_number', (YLeaf(YType.uint32, 'sequence-number'), ['int'])),
                                ('is_ace_type', (YLeaf(YType.enumeration, 'is-ace-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclAce1_', '')])),
                                ('is_ace_sequence_number', (YLeaf(YType.uint32, 'is-ace-sequence-number'), ['int'])),
                                ('is_packet_allow_or_deny', (YLeaf(YType.enumeration, 'is-packet-allow-or-deny'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclAction', '')])),
                                ('is_address_in_numbers', (YLeaf(YType.str, 'is-address-in-numbers'), ['str'])),
                                ('is_address_mask_length', (YLeaf(YType.uint32, 'is-address-mask-length'), ['int'])),
                                ('is_length_operator', (YLeaf(YType.enumeration, 'is-length-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclPortOperator___', '')])),
                                ('is_packet_minimum_length', (YLeaf(YType.uint32, 'is-packet-minimum-length'), ['int'])),
                                ('is_packet_maximum_length', (YLeaf(YType.uint32, 'is-packet-maximum-length'), ['int'])),
                                ('hits', (YLeaf(YType.uint32, 'hits'), ['int'])),
                                ('is_comment_for_entry', (YLeaf(YType.str, 'is-comment-for-entry'), ['str'])),
                                ('acl_name', (YLeaf(YType.str, 'acl-name'), ['str'])),
                            ])
                            self.sequence_number = None
                            self.is_ace_type = None
                            self.is_ace_sequence_number = None
                            self.is_packet_allow_or_deny = None
                            self.is_address_in_numbers = None
                            self.is_address_mask_length = None
                            self.is_length_operator = None
                            self.is_packet_minimum_length = None
                            self.is_packet_maximum_length = None
                            self.hits = None
                            self.is_comment_for_entry = None
                            self.acl_name = None
                            self._segment_path = lambda: "prefix-list-sequence" + "[sequence-number='" + str(self.sequence_number) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence, ['sequence_number', u'is_ace_type', u'is_ace_sequence_number', u'is_packet_allow_or_deny', u'is_address_in_numbers', u'is_address_mask_length', u'is_length_operator', u'is_packet_minimum_length', u'is_packet_maximum_length', u'hits', u'is_comment_for_entry', u'acl_name'], name, value)


        class Usages(Entity):
            """
            Table of Usage statistics of ACLs at different
            nodes
            
            .. attribute:: usage
            
            	Usage statistics of an ACL at a node
            	**type**\: list of  		 :py:class:`Usage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Usages.Usage>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv6AclAndPrefixList.AccessListManager.Usages, self).__init__()

                self.yang_name = "usages"
                self.yang_parent_name = "access-list-manager"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("usage", ("usage", Ipv6AclAndPrefixList.AccessListManager.Usages.Usage))])
                self._leafs = OrderedDict()

                self.usage = YList(self)
                self._segment_path = lambda: "usages"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/access-list-manager/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6AclAndPrefixList.AccessListManager.Usages, [], name, value)


            class Usage(Entity):
                """
                Usage statistics of an ACL at a node
                
                .. attribute:: node_name
                
                	Node where ACL is applied
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: application_id
                
                	Application ID
                	**type**\:  :py:class:`AclUsageAppIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_common_acl_datatypes.AclUsageAppIdEnum>`
                
                .. attribute:: access_list_name
                
                	Name of the ACL
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: usage_details
                
                	Usage Statistics Details
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ipv6-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.AccessListManager.Usages.Usage, self).__init__()

                    self.yang_name = "usage"
                    self.yang_parent_name = "usages"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                        ('application_id', (YLeaf(YType.enumeration, 'application-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_common_acl_datatypes', 'AclUsageAppIdEnum', '')])),
                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                        ('usage_details', (YLeaf(YType.str, 'usage-details'), ['str'])),
                    ])
                    self.node_name = None
                    self.application_id = None
                    self.access_list_name = None
                    self.usage_details = None
                    self._segment_path = lambda: "usage"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/access-list-manager/usages/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6AclAndPrefixList.AccessListManager.Usages.Usage, ['node_name', 'application_id', 'access_list_name', 'usage_details'], name, value)


        class Accesses(Entity):
            """
            ACL class displaying Usage and Entries
            
            .. attribute:: access
            
            	Name of the Access List
            	**type**\: list of  		 :py:class:`Access <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses.Access>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv6AclAndPrefixList.AccessListManager.Accesses, self).__init__()

                self.yang_name = "accesses"
                self.yang_parent_name = "access-list-manager"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("access", ("access", Ipv6AclAndPrefixList.AccessListManager.Accesses.Access))])
                self._leafs = OrderedDict()

                self.access = YList(self)
                self._segment_path = lambda: "accesses"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/access-list-manager/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6AclAndPrefixList.AccessListManager.Accesses, [], name, value)


            class Access(Entity):
                """
                Name of the Access List
                
                .. attribute:: access_list_name  (key)
                
                	Name of the Access List
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: access_list_sequences
                
                	Table of all the sequence numbers per ACL
                	**type**\:  :py:class:`AccessListSequences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences>`
                
                

                """

                _prefix = 'ipv6-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access, self).__init__()

                    self.yang_name = "access"
                    self.yang_parent_name = "accesses"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['access_list_name']
                    self._child_classes = OrderedDict([("access-list-sequences", ("access_list_sequences", Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences))])
                    self._leafs = OrderedDict([
                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                    ])
                    self.access_list_name = None

                    self.access_list_sequences = Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences()
                    self.access_list_sequences.parent = self
                    self._children_name_map["access_list_sequences"] = "access-list-sequences"
                    self._segment_path = lambda: "access" + "[access-list-name='" + str(self.access_list_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/access-list-manager/accesses/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access, ['access_list_name'], name, value)


                class AccessListSequences(Entity):
                    """
                    Table of all the sequence numbers per ACL
                    
                    .. attribute:: access_list_sequence
                    
                    	Sequence number of an ACL entry
                    	**type**\: list of  		 :py:class:`AccessListSequence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence>`
                    
                    

                    """

                    _prefix = 'ipv6-acl-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences, self).__init__()

                        self.yang_name = "access-list-sequences"
                        self.yang_parent_name = "access"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("access-list-sequence", ("access_list_sequence", Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence))])
                        self._leafs = OrderedDict()

                        self.access_list_sequence = YList(self)
                        self._segment_path = lambda: "access-list-sequences"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences, [], name, value)


                    class AccessListSequence(Entity):
                        """
                        Sequence number of an ACL entry
                        
                        .. attribute:: sequence_number  (key)
                        
                        	ACL entry sequence number
                        	**type**\: int
                        
                        	**range:** 1..2147483646
                        
                        .. attribute:: hw_next_hop_info
                        
                        	HW Next hop info
                        	**type**\:  :py:class:`HwNextHopInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo>`
                        
                        .. attribute:: is_ace_type
                        
                        	ACE type (acl, remark)
                        	**type**\:  :py:class:`AclAce1_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclAce1_>`
                        
                        .. attribute:: is_ace_sequence_number
                        
                        	ACLE sequence number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_packet_allow_or_deny
                        
                        	Grant value permit/deny 
                        	**type**\:  :py:class:`AclAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclAction>`
                        
                        .. attribute:: is_protocol_operator
                        
                        	Protocol operator
                        	**type**\:  :py:class:`AclPortOperator___ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperator___>`
                        
                        .. attribute:: is_ipv6_protocol_type
                        
                        	Protocol 1
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_ipv6_protocol2_type
                        
                        	Protocol 2
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_source_address_in_numbers
                        
                        	IsSourceAddressInNumbers
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: is_source_address_prefix_length
                        
                        	IsSourceAddressPrefixLength
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: source_mask
                        
                        	Source Mask
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: is_destination_address_in_numbers
                        
                        	IsDestinationAddressInNumbers
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: is_destination_address_prefix_length
                        
                        	IsDestinationAddressPrefixLength
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: destination_mask
                        
                        	Destination Mask
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: is_source_operator
                        
                        	eq, ne, lt, etc..
                        	**type**\:  :py:class:`AclPortOperator___ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperator___>`
                        
                        .. attribute:: is_source_port1
                        
                        	IsSourcePort1
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_source_port2
                        
                        	IsSourcePort2
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_destination_operator
                        
                        	eq, ne, lt, etc..
                        	**type**\:  :py:class:`AclPortOperator___ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperator___>`
                        
                        .. attribute:: is_destination_port1
                        
                        	IsDestinationPort1
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_destination_port2
                        
                        	IsDestinationPort2
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_log_option
                        
                        	IsLogOption
                        	**type**\:  :py:class:`AclLog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclLog>`
                        
                        .. attribute:: counter_name
                        
                        	Counter name
                        	**type**\: str
                        
                        .. attribute:: is_tcp_bits_operator
                        
                        	IsTCPBitsOperator
                        	**type**\:  :py:class:`AclTcpflagsOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclTcpflagsOperator>`
                        
                        .. attribute:: is_tcp_bits
                        
                        	IsTCPBits
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_tcp_bits_mask
                        
                        	IsTCPBitsMask
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_dscp_present
                        
                        	IsDSCPPresent
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: dscp_operator
                        
                        	DSCP Operator
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_dscp_valu
                        
                        	IsDSCPValu
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_dscp_valu2
                        
                        	IsDSCPValu2
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_precedence_present
                        
                        	IsPrecedencePresent
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_precedence_value
                        
                        	range from 0 to 7
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_header_matches
                        
                        	Match if routing header is presant
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_packet_length_operator
                        
                        	Match if routing header is presant
                        	**type**\:  :py:class:`AclPortOperator___ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperator___>`
                        
                        .. attribute:: is_packet_length_start
                        
                        	IsPacketLengthStart
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_packet_length_end
                        
                        	IsPacketLengthEnd
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_time_to_live_operator
                        
                        	IsTimeToLiveOperator
                        	**type**\:  :py:class:`AclPortOperator___ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperator___>`
                        
                        .. attribute:: is_time_to_live_start
                        
                        	IsTimeToLiveStart
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_time_to_live_end
                        
                        	IsTimeToLiveEnd
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_stats
                        
                        	no stats
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: hits
                        
                        	hits
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: capture
                        
                        	Capture option, TRUE if enabled
                        	**type**\: bool
                        
                        .. attribute:: undetermined_transport
                        
                        	Undetermined transport option, TRUE if enabled
                        	**type**\: bool
                        
                        .. attribute:: is_icmp_message_off
                        
                        	Don't generate the icmp message
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: qos_group
                        
                        	Set qos\-group
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: is_comment_for_entry
                        
                        	IsCommentForEntry
                        	**type**\: str
                        
                        .. attribute:: next_hop_type
                        
                        	Next hop type
                        	**type**\:  :py:class:`BagAclNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.BagAclNh>`
                        
                        .. attribute:: is_flow_id
                        
                        	IsFlowId
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: source_prefix_group
                        
                        	Source prefix object\-group
                        	**type**\: str
                        
                        .. attribute:: destination_prefix_group
                        
                        	Destination prefix object\-group
                        	**type**\: str
                        
                        .. attribute:: source_port_group
                        
                        	Source port object\-group
                        	**type**\: str
                        
                        .. attribute:: destination_port_group
                        
                        	Destination port object\-group
                        	**type**\: str
                        
                        .. attribute:: acl_name
                        
                        	ACL Name
                        	**type**\: str
                        
                        .. attribute:: sequence_str
                        
                        	Sequence String
                        	**type**\: str
                        
                        .. attribute:: set_ttl
                        
                        	SetTTL
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: next_hop_info
                        
                        	Next hop info
                        	**type**\: list of  		 :py:class:`NextHopInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo>`
                        
                        .. attribute:: udf
                        
                        	UDF
                        	**type**\: list of  		 :py:class:`Udf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence, self).__init__()

                            self.yang_name = "access-list-sequence"
                            self.yang_parent_name = "access-list-sequences"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['sequence_number']
                            self._child_classes = OrderedDict([("hw-next-hop-info", ("hw_next_hop_info", Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo)), ("next-hop-info", ("next_hop_info", Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo)), ("udf", ("udf", Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf))])
                            self._leafs = OrderedDict([
                                ('sequence_number', (YLeaf(YType.uint32, 'sequence-number'), ['int'])),
                                ('is_ace_type', (YLeaf(YType.enumeration, 'is-ace-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclAce1_', '')])),
                                ('is_ace_sequence_number', (YLeaf(YType.uint32, 'is-ace-sequence-number'), ['int'])),
                                ('is_packet_allow_or_deny', (YLeaf(YType.enumeration, 'is-packet-allow-or-deny'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclAction', '')])),
                                ('is_protocol_operator', (YLeaf(YType.enumeration, 'is-protocol-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclPortOperator___', '')])),
                                ('is_ipv6_protocol_type', (YLeaf(YType.int32, 'is-ipv6-protocol-type'), ['int'])),
                                ('is_ipv6_protocol2_type', (YLeaf(YType.int32, 'is-ipv6-protocol2-type'), ['int'])),
                                ('is_source_address_in_numbers', (YLeaf(YType.str, 'is-source-address-in-numbers'), ['str'])),
                                ('is_source_address_prefix_length', (YLeaf(YType.uint32, 'is-source-address-prefix-length'), ['int'])),
                                ('source_mask', (YLeaf(YType.str, 'source-mask'), ['str'])),
                                ('is_destination_address_in_numbers', (YLeaf(YType.str, 'is-destination-address-in-numbers'), ['str'])),
                                ('is_destination_address_prefix_length', (YLeaf(YType.uint32, 'is-destination-address-prefix-length'), ['int'])),
                                ('destination_mask', (YLeaf(YType.str, 'destination-mask'), ['str'])),
                                ('is_source_operator', (YLeaf(YType.enumeration, 'is-source-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclPortOperator___', '')])),
                                ('is_source_port1', (YLeaf(YType.uint32, 'is-source-port1'), ['int'])),
                                ('is_source_port2', (YLeaf(YType.uint32, 'is-source-port2'), ['int'])),
                                ('is_destination_operator', (YLeaf(YType.enumeration, 'is-destination-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclPortOperator___', '')])),
                                ('is_destination_port1', (YLeaf(YType.uint32, 'is-destination-port1'), ['int'])),
                                ('is_destination_port2', (YLeaf(YType.uint32, 'is-destination-port2'), ['int'])),
                                ('is_log_option', (YLeaf(YType.enumeration, 'is-log-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclLog', '')])),
                                ('counter_name', (YLeaf(YType.str, 'counter-name'), ['str'])),
                                ('is_tcp_bits_operator', (YLeaf(YType.enumeration, 'is-tcp-bits-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclTcpflagsOperator', '')])),
                                ('is_tcp_bits', (YLeaf(YType.uint32, 'is-tcp-bits'), ['int'])),
                                ('is_tcp_bits_mask', (YLeaf(YType.uint32, 'is-tcp-bits-mask'), ['int'])),
                                ('is_dscp_present', (YLeaf(YType.int32, 'is-dscp-present'), ['int'])),
                                ('dscp_operator', (YLeaf(YType.uint8, 'dscp-operator'), ['int'])),
                                ('is_dscp_valu', (YLeaf(YType.uint8, 'is-dscp-valu'), ['int'])),
                                ('is_dscp_valu2', (YLeaf(YType.uint8, 'is-dscp-valu2'), ['int'])),
                                ('is_precedence_present', (YLeaf(YType.int32, 'is-precedence-present'), ['int'])),
                                ('is_precedence_value', (YLeaf(YType.uint32, 'is-precedence-value'), ['int'])),
                                ('is_header_matches', (YLeaf(YType.uint32, 'is-header-matches'), ['int'])),
                                ('is_packet_length_operator', (YLeaf(YType.enumeration, 'is-packet-length-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclPortOperator___', '')])),
                                ('is_packet_length_start', (YLeaf(YType.uint32, 'is-packet-length-start'), ['int'])),
                                ('is_packet_length_end', (YLeaf(YType.uint32, 'is-packet-length-end'), ['int'])),
                                ('is_time_to_live_operator', (YLeaf(YType.enumeration, 'is-time-to-live-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclPortOperator___', '')])),
                                ('is_time_to_live_start', (YLeaf(YType.uint32, 'is-time-to-live-start'), ['int'])),
                                ('is_time_to_live_end', (YLeaf(YType.uint32, 'is-time-to-live-end'), ['int'])),
                                ('no_stats', (YLeaf(YType.int32, 'no-stats'), ['int'])),
                                ('hits', (YLeaf(YType.uint64, 'hits'), ['int'])),
                                ('capture', (YLeaf(YType.boolean, 'capture'), ['bool'])),
                                ('undetermined_transport', (YLeaf(YType.boolean, 'undetermined-transport'), ['bool'])),
                                ('is_icmp_message_off', (YLeaf(YType.int32, 'is-icmp-message-off'), ['int'])),
                                ('qos_group', (YLeaf(YType.uint16, 'qos-group'), ['int'])),
                                ('is_comment_for_entry', (YLeaf(YType.str, 'is-comment-for-entry'), ['str'])),
                                ('next_hop_type', (YLeaf(YType.enumeration, 'next-hop-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'BagAclNh', '')])),
                                ('is_flow_id', (YLeaf(YType.uint32, 'is-flow-id'), ['int'])),
                                ('source_prefix_group', (YLeaf(YType.str, 'source-prefix-group'), ['str'])),
                                ('destination_prefix_group', (YLeaf(YType.str, 'destination-prefix-group'), ['str'])),
                                ('source_port_group', (YLeaf(YType.str, 'source-port-group'), ['str'])),
                                ('destination_port_group', (YLeaf(YType.str, 'destination-port-group'), ['str'])),
                                ('acl_name', (YLeaf(YType.str, 'acl-name'), ['str'])),
                                ('sequence_str', (YLeaf(YType.str, 'sequence-str'), ['str'])),
                                ('set_ttl', (YLeaf(YType.uint16, 'set-ttl'), ['int'])),
                            ])
                            self.sequence_number = None
                            self.is_ace_type = None
                            self.is_ace_sequence_number = None
                            self.is_packet_allow_or_deny = None
                            self.is_protocol_operator = None
                            self.is_ipv6_protocol_type = None
                            self.is_ipv6_protocol2_type = None
                            self.is_source_address_in_numbers = None
                            self.is_source_address_prefix_length = None
                            self.source_mask = None
                            self.is_destination_address_in_numbers = None
                            self.is_destination_address_prefix_length = None
                            self.destination_mask = None
                            self.is_source_operator = None
                            self.is_source_port1 = None
                            self.is_source_port2 = None
                            self.is_destination_operator = None
                            self.is_destination_port1 = None
                            self.is_destination_port2 = None
                            self.is_log_option = None
                            self.counter_name = None
                            self.is_tcp_bits_operator = None
                            self.is_tcp_bits = None
                            self.is_tcp_bits_mask = None
                            self.is_dscp_present = None
                            self.dscp_operator = None
                            self.is_dscp_valu = None
                            self.is_dscp_valu2 = None
                            self.is_precedence_present = None
                            self.is_precedence_value = None
                            self.is_header_matches = None
                            self.is_packet_length_operator = None
                            self.is_packet_length_start = None
                            self.is_packet_length_end = None
                            self.is_time_to_live_operator = None
                            self.is_time_to_live_start = None
                            self.is_time_to_live_end = None
                            self.no_stats = None
                            self.hits = None
                            self.capture = None
                            self.undetermined_transport = None
                            self.is_icmp_message_off = None
                            self.qos_group = None
                            self.is_comment_for_entry = None
                            self.next_hop_type = None
                            self.is_flow_id = None
                            self.source_prefix_group = None
                            self.destination_prefix_group = None
                            self.source_port_group = None
                            self.destination_port_group = None
                            self.acl_name = None
                            self.sequence_str = None
                            self.set_ttl = None

                            self.hw_next_hop_info = Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo()
                            self.hw_next_hop_info.parent = self
                            self._children_name_map["hw_next_hop_info"] = "hw-next-hop-info"

                            self.next_hop_info = YList(self)
                            self.udf = YList(self)
                            self._segment_path = lambda: "access-list-sequence" + "[sequence-number='" + str(self.sequence_number) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence, ['sequence_number', u'is_ace_type', u'is_ace_sequence_number', u'is_packet_allow_or_deny', u'is_protocol_operator', u'is_ipv6_protocol_type', u'is_ipv6_protocol2_type', u'is_source_address_in_numbers', u'is_source_address_prefix_length', u'source_mask', u'is_destination_address_in_numbers', u'is_destination_address_prefix_length', u'destination_mask', u'is_source_operator', u'is_source_port1', u'is_source_port2', u'is_destination_operator', u'is_destination_port1', u'is_destination_port2', u'is_log_option', u'counter_name', u'is_tcp_bits_operator', u'is_tcp_bits', u'is_tcp_bits_mask', u'is_dscp_present', u'dscp_operator', u'is_dscp_valu', u'is_dscp_valu2', u'is_precedence_present', u'is_precedence_value', u'is_header_matches', u'is_packet_length_operator', u'is_packet_length_start', u'is_packet_length_end', u'is_time_to_live_operator', u'is_time_to_live_start', u'is_time_to_live_end', u'no_stats', u'hits', u'capture', u'undetermined_transport', u'is_icmp_message_off', u'qos_group', u'is_comment_for_entry', u'next_hop_type', u'is_flow_id', u'source_prefix_group', u'destination_prefix_group', u'source_port_group', u'destination_port_group', u'acl_name', u'sequence_str', u'set_ttl'], name, value)


                        class HwNextHopInfo(Entity):
                            """
                            HW Next hop info
                            
                            .. attribute:: type
                            
                            	The next\-hop type
                            	**type**\:  :py:class:`BagAclNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.BagAclNh>`
                            
                            .. attribute:: next_hop
                            
                            	The Next Hop
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: table_id
                            
                            	Table ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_name
                            
                            	Vrf Name
                            	**type**\: str
                            
                            	**length:** 0..32
                            
                            

                            """

                            _prefix = 'ipv6-acl-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo, self).__init__()

                                self.yang_name = "hw-next-hop-info"
                                self.yang_parent_name = "access-list-sequence"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'BagAclNh', '')])),
                                    ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str'])),
                                    ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                ])
                                self.type = None
                                self.next_hop = None
                                self.table_id = None
                                self.vrf_name = None
                                self._segment_path = lambda: "hw-next-hop-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo, [u'type', u'next_hop', u'table_id', u'vrf_name'], name, value)


                        class NextHopInfo(Entity):
                            """
                            Next hop info
                            
                            .. attribute:: next_hop
                            
                            	The next hop
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	Vrf Name
                            	**type**\: str
                            
                            	**length:** 0..32
                            
                            .. attribute:: track_name
                            
                            	Track name
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: status
                            
                            	The next hop status
                            	**type**\:  :py:class:`BagAclNhStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.BagAclNhStatus>`
                            
                            .. attribute:: at_status
                            
                            	The next hop at status
                            	**type**\:  :py:class:`BagAclNhAtStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.BagAclNhAtStatus>`
                            
                            .. attribute:: acl_nh_exist
                            
                            	The nexthop exist
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'ipv6-acl-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo, self).__init__()

                                self.yang_name = "next-hop-info"
                                self.yang_parent_name = "access-list-sequence"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str'])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                    ('track_name', (YLeaf(YType.str, 'track-name'), ['str'])),
                                    ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'BagAclNhStatus', '')])),
                                    ('at_status', (YLeaf(YType.enumeration, 'at-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'BagAclNhAtStatus', '')])),
                                    ('acl_nh_exist', (YLeaf(YType.int32, 'acl-nh-exist'), ['int'])),
                                ])
                                self.next_hop = None
                                self.vrf_name = None
                                self.track_name = None
                                self.status = None
                                self.at_status = None
                                self.acl_nh_exist = None
                                self._segment_path = lambda: "next-hop-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo, [u'next_hop', u'vrf_name', u'track_name', u'status', u'at_status', u'acl_nh_exist'], name, value)


                        class Udf(Entity):
                            """
                            UDF
                            
                            .. attribute:: udf_name
                            
                            	UDF Name
                            	**type**\: str
                            
                            	**length:** 0..17
                            
                            .. attribute:: udf_value
                            
                            	UDF Value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: udf_mask
                            
                            	UDF Mask
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-acl-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf, self).__init__()

                                self.yang_name = "udf"
                                self.yang_parent_name = "access-list-sequence"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('udf_name', (YLeaf(YType.str, 'udf-name'), ['str'])),
                                    ('udf_value', (YLeaf(YType.uint32, 'udf-value'), ['int'])),
                                    ('udf_mask', (YLeaf(YType.uint32, 'udf-mask'), ['int'])),
                                ])
                                self.udf_name = None
                                self.udf_value = None
                                self.udf_mask = None
                                self._segment_path = lambda: "udf"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf, [u'udf_name', u'udf_value', u'udf_mask'], name, value)


    class Oor(Entity):
        """
        Out Of Resources, Limits to the resources
        allocatable
        
        .. attribute:: details
        
        	Details of the overall out of resource limit
        	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.Details>`
        
        .. attribute:: prefix_list_summary
        
        	Summary of the prefix Lists resource utilization
        	**type**\:  :py:class:`PrefixListSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.PrefixListSummary>`
        
        .. attribute:: oor_accesses
        
        	Resource occupation details for ACLs
        	**type**\:  :py:class:`OorAccesses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.OorAccesses>`
        
        .. attribute:: oor_prefixes
        
        	Resource occupation details for prefix lists
        	**type**\:  :py:class:`OorPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.OorPrefixes>`
        
        .. attribute:: access_list_summary
        
        	Resource Limits pertaining to ACLs only
        	**type**\:  :py:class:`AccessListSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.AccessListSummary>`
        
        

        """

        _prefix = 'ipv6-acl-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv6AclAndPrefixList.Oor, self).__init__()

            self.yang_name = "oor"
            self.yang_parent_name = "ipv6-acl-and-prefix-list"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("details", ("details", Ipv6AclAndPrefixList.Oor.Details)), ("prefix-list-summary", ("prefix_list_summary", Ipv6AclAndPrefixList.Oor.PrefixListSummary)), ("oor-accesses", ("oor_accesses", Ipv6AclAndPrefixList.Oor.OorAccesses)), ("oor-prefixes", ("oor_prefixes", Ipv6AclAndPrefixList.Oor.OorPrefixes)), ("access-list-summary", ("access_list_summary", Ipv6AclAndPrefixList.Oor.AccessListSummary))])
            self._leafs = OrderedDict()

            self.details = Ipv6AclAndPrefixList.Oor.Details()
            self.details.parent = self
            self._children_name_map["details"] = "details"

            self.prefix_list_summary = Ipv6AclAndPrefixList.Oor.PrefixListSummary()
            self.prefix_list_summary.parent = self
            self._children_name_map["prefix_list_summary"] = "prefix-list-summary"

            self.oor_accesses = Ipv6AclAndPrefixList.Oor.OorAccesses()
            self.oor_accesses.parent = self
            self._children_name_map["oor_accesses"] = "oor-accesses"

            self.oor_prefixes = Ipv6AclAndPrefixList.Oor.OorPrefixes()
            self.oor_prefixes.parent = self
            self._children_name_map["oor_prefixes"] = "oor-prefixes"

            self.access_list_summary = Ipv6AclAndPrefixList.Oor.AccessListSummary()
            self.access_list_summary.parent = self
            self._children_name_map["access_list_summary"] = "access-list-summary"
            self._segment_path = lambda: "oor"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6AclAndPrefixList.Oor, [], name, value)


        class Details(Entity):
            """
            Details of the overall out of resource limit
            
            .. attribute:: is_default_maximum_configurable_ac_ls
            
            	default max configurable acls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_default_maximum_configurable_ac_es
            
            	default max configurable aces
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_current_configured_ac_ls
            
            	Current configured acls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_current_configured_aces
            
            	Current configured aces
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_current_maximum_configurable_acls
            
            	Current max configurable acls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_current_maximum_configurable_aces
            
            	Current max configurable aces
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_maximum_configurable_ac_ls
            
            	max configurable acls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_maximum_configurable_ac_es
            
            	max configurable aces
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv6AclAndPrefixList.Oor.Details, self).__init__()

                self.yang_name = "details"
                self.yang_parent_name = "oor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('is_default_maximum_configurable_ac_ls', (YLeaf(YType.uint32, 'is-default-maximum-configurable-ac-ls'), ['int'])),
                    ('is_default_maximum_configurable_ac_es', (YLeaf(YType.uint32, 'is-default-maximum-configurable-ac-es'), ['int'])),
                    ('is_current_configured_ac_ls', (YLeaf(YType.uint32, 'is-current-configured-ac-ls'), ['int'])),
                    ('is_current_configured_aces', (YLeaf(YType.uint32, 'is-current-configured-aces'), ['int'])),
                    ('is_current_maximum_configurable_acls', (YLeaf(YType.uint32, 'is-current-maximum-configurable-acls'), ['int'])),
                    ('is_current_maximum_configurable_aces', (YLeaf(YType.uint32, 'is-current-maximum-configurable-aces'), ['int'])),
                    ('is_maximum_configurable_ac_ls', (YLeaf(YType.uint32, 'is-maximum-configurable-ac-ls'), ['int'])),
                    ('is_maximum_configurable_ac_es', (YLeaf(YType.uint32, 'is-maximum-configurable-ac-es'), ['int'])),
                ])
                self.is_default_maximum_configurable_ac_ls = None
                self.is_default_maximum_configurable_ac_es = None
                self.is_current_configured_ac_ls = None
                self.is_current_configured_aces = None
                self.is_current_maximum_configurable_acls = None
                self.is_current_maximum_configurable_aces = None
                self.is_maximum_configurable_ac_ls = None
                self.is_maximum_configurable_ac_es = None
                self._segment_path = lambda: "details"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6AclAndPrefixList.Oor.Details, [u'is_default_maximum_configurable_ac_ls', u'is_default_maximum_configurable_ac_es', u'is_current_configured_ac_ls', u'is_current_configured_aces', u'is_current_maximum_configurable_acls', u'is_current_maximum_configurable_aces', u'is_maximum_configurable_ac_ls', u'is_maximum_configurable_ac_es'], name, value)


        class PrefixListSummary(Entity):
            """
            Summary of the prefix Lists resource
            utilization
            
            .. attribute:: details
            
            	Summary Detail of the prefix list Resource Utilisation
            	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.PrefixListSummary.Details>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv6AclAndPrefixList.Oor.PrefixListSummary, self).__init__()

                self.yang_name = "prefix-list-summary"
                self.yang_parent_name = "oor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("details", ("details", Ipv6AclAndPrefixList.Oor.PrefixListSummary.Details))])
                self._leafs = OrderedDict()

                self.details = Ipv6AclAndPrefixList.Oor.PrefixListSummary.Details()
                self.details.parent = self
                self._children_name_map["details"] = "details"
                self._segment_path = lambda: "prefix-list-summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6AclAndPrefixList.Oor.PrefixListSummary, [], name, value)


            class Details(Entity):
                """
                Summary Detail of the prefix list Resource
                Utilisation
                
                .. attribute:: is_default_maximum_configurable_ac_ls
                
                	default max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_default_maximum_configurable_ac_es
                
                	default max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_configured_ac_ls
                
                	Current configured acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_configured_aces
                
                	Current configured aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_maximum_configurable_acls
                
                	Current max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_maximum_configurable_aces
                
                	Current max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_configurable_ac_ls
                
                	max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_configurable_ac_es
                
                	max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv6-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.Oor.PrefixListSummary.Details, self).__init__()

                    self.yang_name = "details"
                    self.yang_parent_name = "prefix-list-summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('is_default_maximum_configurable_ac_ls', (YLeaf(YType.uint32, 'is-default-maximum-configurable-ac-ls'), ['int'])),
                        ('is_default_maximum_configurable_ac_es', (YLeaf(YType.uint32, 'is-default-maximum-configurable-ac-es'), ['int'])),
                        ('is_current_configured_ac_ls', (YLeaf(YType.uint32, 'is-current-configured-ac-ls'), ['int'])),
                        ('is_current_configured_aces', (YLeaf(YType.uint32, 'is-current-configured-aces'), ['int'])),
                        ('is_current_maximum_configurable_acls', (YLeaf(YType.uint32, 'is-current-maximum-configurable-acls'), ['int'])),
                        ('is_current_maximum_configurable_aces', (YLeaf(YType.uint32, 'is-current-maximum-configurable-aces'), ['int'])),
                        ('is_maximum_configurable_ac_ls', (YLeaf(YType.uint32, 'is-maximum-configurable-ac-ls'), ['int'])),
                        ('is_maximum_configurable_ac_es', (YLeaf(YType.uint32, 'is-maximum-configurable-ac-es'), ['int'])),
                    ])
                    self.is_default_maximum_configurable_ac_ls = None
                    self.is_default_maximum_configurable_ac_es = None
                    self.is_current_configured_ac_ls = None
                    self.is_current_configured_aces = None
                    self.is_current_maximum_configurable_acls = None
                    self.is_current_maximum_configurable_aces = None
                    self.is_maximum_configurable_ac_ls = None
                    self.is_maximum_configurable_ac_es = None
                    self._segment_path = lambda: "details"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/prefix-list-summary/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6AclAndPrefixList.Oor.PrefixListSummary.Details, [u'is_default_maximum_configurable_ac_ls', u'is_default_maximum_configurable_ac_es', u'is_current_configured_ac_ls', u'is_current_configured_aces', u'is_current_maximum_configurable_acls', u'is_current_maximum_configurable_aces', u'is_maximum_configurable_ac_ls', u'is_maximum_configurable_ac_es'], name, value)


        class OorAccesses(Entity):
            """
            Resource occupation details for ACLs
            
            .. attribute:: oor_access
            
            	Resource occupation details for a particular ACL
            	**type**\: list of  		 :py:class:`OorAccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.OorAccesses.OorAccess>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv6AclAndPrefixList.Oor.OorAccesses, self).__init__()

                self.yang_name = "oor-accesses"
                self.yang_parent_name = "oor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("oor-access", ("oor_access", Ipv6AclAndPrefixList.Oor.OorAccesses.OorAccess))])
                self._leafs = OrderedDict()

                self.oor_access = YList(self)
                self._segment_path = lambda: "oor-accesses"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6AclAndPrefixList.Oor.OorAccesses, [], name, value)


            class OorAccess(Entity):
                """
                Resource occupation details for a particular
                ACL
                
                .. attribute:: access_list_name  (key)
                
                	Name of the Access List
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: is_default_maximum_configurable_ac_ls
                
                	default max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_default_maximum_configurable_ac_es
                
                	default max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_configured_ac_ls
                
                	Current configured acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_configured_aces
                
                	Current configured aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_maximum_configurable_acls
                
                	Current max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_maximum_configurable_aces
                
                	Current max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_configurable_ac_ls
                
                	max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_configurable_ac_es
                
                	max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv6-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.Oor.OorAccesses.OorAccess, self).__init__()

                    self.yang_name = "oor-access"
                    self.yang_parent_name = "oor-accesses"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['access_list_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                        ('is_default_maximum_configurable_ac_ls', (YLeaf(YType.uint32, 'is-default-maximum-configurable-ac-ls'), ['int'])),
                        ('is_default_maximum_configurable_ac_es', (YLeaf(YType.uint32, 'is-default-maximum-configurable-ac-es'), ['int'])),
                        ('is_current_configured_ac_ls', (YLeaf(YType.uint32, 'is-current-configured-ac-ls'), ['int'])),
                        ('is_current_configured_aces', (YLeaf(YType.uint32, 'is-current-configured-aces'), ['int'])),
                        ('is_current_maximum_configurable_acls', (YLeaf(YType.uint32, 'is-current-maximum-configurable-acls'), ['int'])),
                        ('is_current_maximum_configurable_aces', (YLeaf(YType.uint32, 'is-current-maximum-configurable-aces'), ['int'])),
                        ('is_maximum_configurable_ac_ls', (YLeaf(YType.uint32, 'is-maximum-configurable-ac-ls'), ['int'])),
                        ('is_maximum_configurable_ac_es', (YLeaf(YType.uint32, 'is-maximum-configurable-ac-es'), ['int'])),
                    ])
                    self.access_list_name = None
                    self.is_default_maximum_configurable_ac_ls = None
                    self.is_default_maximum_configurable_ac_es = None
                    self.is_current_configured_ac_ls = None
                    self.is_current_configured_aces = None
                    self.is_current_maximum_configurable_acls = None
                    self.is_current_maximum_configurable_aces = None
                    self.is_maximum_configurable_ac_ls = None
                    self.is_maximum_configurable_ac_es = None
                    self._segment_path = lambda: "oor-access" + "[access-list-name='" + str(self.access_list_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/oor-accesses/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6AclAndPrefixList.Oor.OorAccesses.OorAccess, ['access_list_name', u'is_default_maximum_configurable_ac_ls', u'is_default_maximum_configurable_ac_es', u'is_current_configured_ac_ls', u'is_current_configured_aces', u'is_current_maximum_configurable_acls', u'is_current_maximum_configurable_aces', u'is_maximum_configurable_ac_ls', u'is_maximum_configurable_ac_es'], name, value)


        class OorPrefixes(Entity):
            """
            Resource occupation details for prefix lists
            
            .. attribute:: oor_prefix
            
            	Resource occupation details for a particular prefix list
            	**type**\: list of  		 :py:class:`OorPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.OorPrefixes.OorPrefix>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv6AclAndPrefixList.Oor.OorPrefixes, self).__init__()

                self.yang_name = "oor-prefixes"
                self.yang_parent_name = "oor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("oor-prefix", ("oor_prefix", Ipv6AclAndPrefixList.Oor.OorPrefixes.OorPrefix))])
                self._leafs = OrderedDict()

                self.oor_prefix = YList(self)
                self._segment_path = lambda: "oor-prefixes"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6AclAndPrefixList.Oor.OorPrefixes, [], name, value)


            class OorPrefix(Entity):
                """
                Resource occupation details for a particular
                prefix list
                
                .. attribute:: prefix_list_name  (key)
                
                	Name of a prefix list
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: is_default_maximum_configurable_ac_ls
                
                	default max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_default_maximum_configurable_ac_es
                
                	default max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_configured_ac_ls
                
                	Current configured acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_configured_aces
                
                	Current configured aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_maximum_configurable_acls
                
                	Current max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_maximum_configurable_aces
                
                	Current max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_configurable_ac_ls
                
                	max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_configurable_ac_es
                
                	max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv6-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.Oor.OorPrefixes.OorPrefix, self).__init__()

                    self.yang_name = "oor-prefix"
                    self.yang_parent_name = "oor-prefixes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['prefix_list_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('prefix_list_name', (YLeaf(YType.str, 'prefix-list-name'), ['str'])),
                        ('is_default_maximum_configurable_ac_ls', (YLeaf(YType.uint32, 'is-default-maximum-configurable-ac-ls'), ['int'])),
                        ('is_default_maximum_configurable_ac_es', (YLeaf(YType.uint32, 'is-default-maximum-configurable-ac-es'), ['int'])),
                        ('is_current_configured_ac_ls', (YLeaf(YType.uint32, 'is-current-configured-ac-ls'), ['int'])),
                        ('is_current_configured_aces', (YLeaf(YType.uint32, 'is-current-configured-aces'), ['int'])),
                        ('is_current_maximum_configurable_acls', (YLeaf(YType.uint32, 'is-current-maximum-configurable-acls'), ['int'])),
                        ('is_current_maximum_configurable_aces', (YLeaf(YType.uint32, 'is-current-maximum-configurable-aces'), ['int'])),
                        ('is_maximum_configurable_ac_ls', (YLeaf(YType.uint32, 'is-maximum-configurable-ac-ls'), ['int'])),
                        ('is_maximum_configurable_ac_es', (YLeaf(YType.uint32, 'is-maximum-configurable-ac-es'), ['int'])),
                    ])
                    self.prefix_list_name = None
                    self.is_default_maximum_configurable_ac_ls = None
                    self.is_default_maximum_configurable_ac_es = None
                    self.is_current_configured_ac_ls = None
                    self.is_current_configured_aces = None
                    self.is_current_maximum_configurable_acls = None
                    self.is_current_maximum_configurable_aces = None
                    self.is_maximum_configurable_ac_ls = None
                    self.is_maximum_configurable_ac_es = None
                    self._segment_path = lambda: "oor-prefix" + "[prefix-list-name='" + str(self.prefix_list_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/oor-prefixes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6AclAndPrefixList.Oor.OorPrefixes.OorPrefix, ['prefix_list_name', u'is_default_maximum_configurable_ac_ls', u'is_default_maximum_configurable_ac_es', u'is_current_configured_ac_ls', u'is_current_configured_aces', u'is_current_maximum_configurable_acls', u'is_current_maximum_configurable_aces', u'is_maximum_configurable_ac_ls', u'is_maximum_configurable_ac_es'], name, value)


        class AccessListSummary(Entity):
            """
            Resource Limits pertaining to ACLs only
            
            .. attribute:: details
            
            	Details containing the resource limits of the ACLs
            	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.AccessListSummary.Details>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv6AclAndPrefixList.Oor.AccessListSummary, self).__init__()

                self.yang_name = "access-list-summary"
                self.yang_parent_name = "oor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("details", ("details", Ipv6AclAndPrefixList.Oor.AccessListSummary.Details))])
                self._leafs = OrderedDict()

                self.details = Ipv6AclAndPrefixList.Oor.AccessListSummary.Details()
                self.details.parent = self
                self._children_name_map["details"] = "details"
                self._segment_path = lambda: "access-list-summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6AclAndPrefixList.Oor.AccessListSummary, [], name, value)


            class Details(Entity):
                """
                Details containing the resource limits of the
                ACLs
                
                .. attribute:: is_default_maximum_configurable_ac_ls
                
                	default max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_default_maximum_configurable_ac_es
                
                	default max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_configured_ac_ls
                
                	Current configured acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_configured_aces
                
                	Current configured aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_maximum_configurable_acls
                
                	Current max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_maximum_configurable_aces
                
                	Current max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_configurable_ac_ls
                
                	max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_configurable_ac_es
                
                	max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv6-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.Oor.AccessListSummary.Details, self).__init__()

                    self.yang_name = "details"
                    self.yang_parent_name = "access-list-summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('is_default_maximum_configurable_ac_ls', (YLeaf(YType.uint32, 'is-default-maximum-configurable-ac-ls'), ['int'])),
                        ('is_default_maximum_configurable_ac_es', (YLeaf(YType.uint32, 'is-default-maximum-configurable-ac-es'), ['int'])),
                        ('is_current_configured_ac_ls', (YLeaf(YType.uint32, 'is-current-configured-ac-ls'), ['int'])),
                        ('is_current_configured_aces', (YLeaf(YType.uint32, 'is-current-configured-aces'), ['int'])),
                        ('is_current_maximum_configurable_acls', (YLeaf(YType.uint32, 'is-current-maximum-configurable-acls'), ['int'])),
                        ('is_current_maximum_configurable_aces', (YLeaf(YType.uint32, 'is-current-maximum-configurable-aces'), ['int'])),
                        ('is_maximum_configurable_ac_ls', (YLeaf(YType.uint32, 'is-maximum-configurable-ac-ls'), ['int'])),
                        ('is_maximum_configurable_ac_es', (YLeaf(YType.uint32, 'is-maximum-configurable-ac-es'), ['int'])),
                    ])
                    self.is_default_maximum_configurable_ac_ls = None
                    self.is_default_maximum_configurable_ac_es = None
                    self.is_current_configured_ac_ls = None
                    self.is_current_configured_aces = None
                    self.is_current_maximum_configurable_acls = None
                    self.is_current_maximum_configurable_aces = None
                    self.is_maximum_configurable_ac_ls = None
                    self.is_maximum_configurable_ac_es = None
                    self._segment_path = lambda: "details"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/access-list-summary/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6AclAndPrefixList.Oor.AccessListSummary.Details, [u'is_default_maximum_configurable_ac_ls', u'is_default_maximum_configurable_ac_es', u'is_current_configured_ac_ls', u'is_current_configured_aces', u'is_current_maximum_configurable_acls', u'is_current_maximum_configurable_aces', u'is_maximum_configurable_ac_ls', u'is_maximum_configurable_ac_es'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv6AclAndPrefixList()
        return self._top_entity

