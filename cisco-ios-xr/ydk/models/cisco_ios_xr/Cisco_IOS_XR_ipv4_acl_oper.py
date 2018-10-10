""" Cisco_IOS_XR_ipv4_acl_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-acl package operational data.

This module contains definitions
for the following management objects\:
  ipv4\-acl\-and\-prefix\-list\: Root class of IPv4 Oper schema tree

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



class Ipv4AclAndPrefixList(Entity):
    """
    Root class of IPv4 Oper schema tree
    
    .. attribute:: access_list_manager
    
    	Access list manager containing access lists and prefix lists
    	**type**\:  :py:class:`AccessListManager <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager>`
    
    .. attribute:: oor
    
    	Out Of Resources, Limits to the resources allocatable
    	**type**\:  :py:class:`Oor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor>`
    
    

    """

    _prefix = 'ipv4-acl-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(Ipv4AclAndPrefixList, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4-acl-and-prefix-list"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-acl-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("access-list-manager", ("access_list_manager", Ipv4AclAndPrefixList.AccessListManager)), ("oor", ("oor", Ipv4AclAndPrefixList.Oor))])
        self._leafs = OrderedDict()

        self.access_list_manager = Ipv4AclAndPrefixList.AccessListManager()
        self.access_list_manager.parent = self
        self._children_name_map["access_list_manager"] = "access-list-manager"

        self.oor = Ipv4AclAndPrefixList.Oor()
        self.oor.parent = self
        self._children_name_map["oor"] = "oor"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv4AclAndPrefixList, [], name, value)


    class AccessListManager(Entity):
        """
        Access list manager containing access lists and
        prefix lists
        
        .. attribute:: prefixes
        
        	Table of prefix lists
        	**type**\:  :py:class:`Prefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Prefixes>`
        
        .. attribute:: accesses
        
        	Access listL class displaying Usage and Entries
        	**type**\:  :py:class:`Accesses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses>`
        
        .. attribute:: usages
        
        	Table of Usage statistics of access lists at different nodes
        	**type**\:  :py:class:`Usages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Usages>`
        
        

        """

        _prefix = 'ipv4-acl-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv4AclAndPrefixList.AccessListManager, self).__init__()

            self.yang_name = "access-list-manager"
            self.yang_parent_name = "ipv4-acl-and-prefix-list"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("prefixes", ("prefixes", Ipv4AclAndPrefixList.AccessListManager.Prefixes)), ("accesses", ("accesses", Ipv4AclAndPrefixList.AccessListManager.Accesses)), ("usages", ("usages", Ipv4AclAndPrefixList.AccessListManager.Usages))])
            self._leafs = OrderedDict()

            self.prefixes = Ipv4AclAndPrefixList.AccessListManager.Prefixes()
            self.prefixes.parent = self
            self._children_name_map["prefixes"] = "prefixes"

            self.accesses = Ipv4AclAndPrefixList.AccessListManager.Accesses()
            self.accesses.parent = self
            self._children_name_map["accesses"] = "accesses"

            self.usages = Ipv4AclAndPrefixList.AccessListManager.Usages()
            self.usages.parent = self
            self._children_name_map["usages"] = "usages"
            self._segment_path = lambda: "access-list-manager"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4AclAndPrefixList.AccessListManager, [], name, value)


        class Prefixes(Entity):
            """
            Table of prefix lists
            
            .. attribute:: prefix
            
            	Name of the prefix list
            	**type**\: list of  		 :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv4AclAndPrefixList.AccessListManager.Prefixes, self).__init__()

                self.yang_name = "prefixes"
                self.yang_parent_name = "access-list-manager"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("prefix", ("prefix", Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix))])
                self._leafs = OrderedDict()

                self.prefix = YList(self)
                self._segment_path = lambda: "prefixes"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/access-list-manager/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4AclAndPrefixList.AccessListManager.Prefixes, [], name, value)


            class Prefix(Entity):
                """
                Name of the prefix list
                
                .. attribute:: prefix_list_name  (key)
                
                	Name of the prefix list
                	**type**\: str
                
                .. attribute:: prefix_list_sequences
                
                	Table of all the SequenceNumbers per prefix list
                	**type**\:  :py:class:`PrefixListSequences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences>`
                
                

                """

                _prefix = 'ipv4-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix, self).__init__()

                    self.yang_name = "prefix"
                    self.yang_parent_name = "prefixes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['prefix_list_name']
                    self._child_classes = OrderedDict([("prefix-list-sequences", ("prefix_list_sequences", Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences))])
                    self._leafs = OrderedDict([
                        ('prefix_list_name', (YLeaf(YType.str, 'prefix-list-name'), ['str'])),
                    ])
                    self.prefix_list_name = None

                    self.prefix_list_sequences = Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences()
                    self.prefix_list_sequences.parent = self
                    self._children_name_map["prefix_list_sequences"] = "prefix-list-sequences"
                    self._segment_path = lambda: "prefix" + "[prefix-list-name='" + str(self.prefix_list_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/access-list-manager/prefixes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix, ['prefix_list_name'], name, value)


                class PrefixListSequences(Entity):
                    """
                    Table of all the SequenceNumbers per prefix
                    list
                    
                    .. attribute:: prefix_list_sequence
                    
                    	Sequence Number of a prefix list entry
                    	**type**\: list of  		 :py:class:`PrefixListSequence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence>`
                    
                    

                    """

                    _prefix = 'ipv4-acl-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences, self).__init__()

                        self.yang_name = "prefix-list-sequences"
                        self.yang_parent_name = "prefix"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("prefix-list-sequence", ("prefix_list_sequence", Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence))])
                        self._leafs = OrderedDict()

                        self.prefix_list_sequence = YList(self)
                        self._segment_path = lambda: "prefix-list-sequences"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences, [], name, value)


                    class PrefixListSequence(Entity):
                        """
                        Sequence Number of a prefix list entry
                        
                        .. attribute:: sequence_number  (key)
                        
                        	Sequence Number of the prefix list entry
                        	**type**\: int
                        
                        	**range:** 1..2147483646
                        
                        .. attribute:: item_type
                        
                        	ACE type (prefix, remark)
                        	**type**\:  :py:class:`AclAce1_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclAce1_>`
                        
                        .. attribute:: sequence
                        
                        	ACLE sequence number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: grant
                        
                        	Grant value permit/deny 
                        	**type**\:  :py:class:`AclAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclAction>`
                        
                        .. attribute:: prefix
                        
                        	Prefix
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length 
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Port Operator
                        	**type**\:  :py:class:`AclPortOperator___ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperator___>`
                        
                        .. attribute:: minimum_length
                        
                        	Min length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: maximum_length
                        
                        	Maximum length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hits
                        
                        	Number of hits
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remark
                        
                        	Remark String
                        	**type**\: str
                        
                        .. attribute:: acl_name
                        
                        	ACL Name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ipv4-acl-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence, self).__init__()

                            self.yang_name = "prefix-list-sequence"
                            self.yang_parent_name = "prefix-list-sequences"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['sequence_number']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sequence_number', (YLeaf(YType.uint32, 'sequence-number'), ['int'])),
                                ('item_type', (YLeaf(YType.enumeration, 'item-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper', 'AclAce1_', '')])),
                                ('sequence', (YLeaf(YType.uint32, 'sequence'), ['int'])),
                                ('grant', (YLeaf(YType.enumeration, 'grant'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper', 'AclAction', '')])),
                                ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper', 'AclPortOperator___', '')])),
                                ('minimum_length', (YLeaf(YType.uint32, 'minimum-length'), ['int'])),
                                ('maximum_length', (YLeaf(YType.uint32, 'maximum-length'), ['int'])),
                                ('hits', (YLeaf(YType.uint32, 'hits'), ['int'])),
                                ('remark', (YLeaf(YType.str, 'remark'), ['str'])),
                                ('acl_name', (YLeaf(YType.str, 'acl-name'), ['str'])),
                            ])
                            self.sequence_number = None
                            self.item_type = None
                            self.sequence = None
                            self.grant = None
                            self.prefix = None
                            self.prefix_length = None
                            self.operator = None
                            self.minimum_length = None
                            self.maximum_length = None
                            self.hits = None
                            self.remark = None
                            self.acl_name = None
                            self._segment_path = lambda: "prefix-list-sequence" + "[sequence-number='" + str(self.sequence_number) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence, ['sequence_number', u'item_type', u'sequence', u'grant', u'prefix', u'prefix_length', u'operator', u'minimum_length', u'maximum_length', u'hits', u'remark', u'acl_name'], name, value)


        class Accesses(Entity):
            """
            Access listL class displaying Usage and Entries
            
            .. attribute:: access
            
            	Name of the Access List
            	**type**\: list of  		 :py:class:`Access <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv4AclAndPrefixList.AccessListManager.Accesses, self).__init__()

                self.yang_name = "accesses"
                self.yang_parent_name = "access-list-manager"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("access", ("access", Ipv4AclAndPrefixList.AccessListManager.Accesses.Access))])
                self._leafs = OrderedDict()

                self.access = YList(self)
                self._segment_path = lambda: "accesses"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/access-list-manager/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4AclAndPrefixList.AccessListManager.Accesses, [], name, value)


            class Access(Entity):
                """
                Name of the Access List
                
                .. attribute:: access_list_name  (key)
                
                	Name of the Access List
                	**type**\: str
                
                .. attribute:: access_list_sequences
                
                	Table of all the SequenceNumbers per access list
                	**type**\:  :py:class:`AccessListSequences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences>`
                
                .. attribute:: object_group
                
                	Object Group in an Access list
                	**type**\:  :py:class:`ObjectGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup>`
                
                

                """

                _prefix = 'ipv4-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access, self).__init__()

                    self.yang_name = "access"
                    self.yang_parent_name = "accesses"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['access_list_name']
                    self._child_classes = OrderedDict([("access-list-sequences", ("access_list_sequences", Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences)), ("object-group", ("object_group", Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup))])
                    self._leafs = OrderedDict([
                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                    ])
                    self.access_list_name = None

                    self.access_list_sequences = Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences()
                    self.access_list_sequences.parent = self
                    self._children_name_map["access_list_sequences"] = "access-list-sequences"

                    self.object_group = Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup()
                    self.object_group.parent = self
                    self._children_name_map["object_group"] = "object-group"
                    self._segment_path = lambda: "access" + "[access-list-name='" + str(self.access_list_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/access-list-manager/accesses/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access, ['access_list_name'], name, value)


                class AccessListSequences(Entity):
                    """
                    Table of all the SequenceNumbers per access
                    list
                    
                    .. attribute:: access_list_sequence
                    
                    	Sequence Number of an access list entry
                    	**type**\: list of  		 :py:class:`AccessListSequence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence>`
                    
                    

                    """

                    _prefix = 'ipv4-acl-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences, self).__init__()

                        self.yang_name = "access-list-sequences"
                        self.yang_parent_name = "access"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("access-list-sequence", ("access_list_sequence", Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence))])
                        self._leafs = OrderedDict()

                        self.access_list_sequence = YList(self)
                        self._segment_path = lambda: "access-list-sequences"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences, [], name, value)


                    class AccessListSequence(Entity):
                        """
                        Sequence Number of an access list entry
                        
                        .. attribute:: sequence_number  (key)
                        
                        	ACLEntry Sequence Number
                        	**type**\: int
                        
                        	**range:** 1..2147483646
                        
                        .. attribute:: hw_next_hop_info
                        
                        	HW Next hop info
                        	**type**\:  :py:class:`HwNextHopInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo>`
                        
                        .. attribute:: item_type
                        
                        	ACE type (acl, remark)
                        	**type**\:  :py:class:`AclAce1_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclAce1_>`
                        
                        .. attribute:: sequence
                        
                        	ACLE sequence number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: grant
                        
                        	Permit/deny
                        	**type**\:  :py:class:`AclAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclAction>`
                        
                        .. attribute:: protocol_operator
                        
                        	IPv4 protocol operator
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: protocol
                        
                        	IPv4 protocol type
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: protocol2
                        
                        	IPv4 protocol 2
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: source_address
                        
                        	Source address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address_mask
                        
                        	Source mask
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: destination_address
                        
                        	Destination address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: destination_address_mask
                        
                        	Destination mask
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_operator
                        
                        	Source operator
                        	**type**\:  :py:class:`AclPortOperator___ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperator___>`
                        
                        .. attribute:: source_port1
                        
                        	Source port 1
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: source_port2
                        
                        	Source port 2
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: sorce_operator
                        
                        	Deprecated by Source operator
                        	**type**\:  :py:class:`AclPortOperator___ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperator___>`
                        
                        .. attribute:: sorce_port1
                        
                        	Deprecated by SourcePort1
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: sorce_port2
                        
                        	Deprecated by SourcePort2
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: destination_operator
                        
                        	Destination operator
                        	**type**\:  :py:class:`AclPortOperator___ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperator___>`
                        
                        .. attribute:: destination_port1
                        
                        	Destination port 1
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: destination_port2
                        
                        	Destination port 2
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: log_option
                        
                        	Log option
                        	**type**\:  :py:class:`AclLog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclLog>`
                        
                        .. attribute:: counter_name
                        
                        	Counter name
                        	**type**\: str
                        
                        .. attribute:: capture
                        
                        	Capture option, TRUE if enabled
                        	**type**\: bool
                        
                        .. attribute:: dscp_present
                        
                        	DSCP present
                        	**type**\: bool
                        
                        .. attribute:: dscp
                        
                        	DSCP or DSCP range start
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: dscp2
                        
                        	DSCP Range End
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: dscp_operator
                        
                        	DSCP Operator
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: precedence_present
                        
                        	Precedence present
                        	**type**\: bool
                        
                        .. attribute:: precedence
                        
                        	Precedence
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: tcp_flags_operator
                        
                        	TCP flags operator
                        	**type**\:  :py:class:`AclTcpflagsOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclTcpflagsOperator>`
                        
                        .. attribute:: tcp_flags
                        
                        	TCP flags
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: tcp_flags_mask
                        
                        	TCP flags mask
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: fragments
                        
                        	Fragments
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: packet_length_operator
                        
                        	Packet length operator
                        	**type**\:  :py:class:`AclPortOperator___ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperator___>`
                        
                        .. attribute:: packet_length1
                        
                        	Packet length 1
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: packet_length2
                        
                        	Packet length 2
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: ttl_operator
                        
                        	TTL operator
                        	**type**\:  :py:class:`AclPortOperator___ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperator___>`
                        
                        .. attribute:: ttl1
                        
                        	TTL 1
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: ttl2
                        
                        	TTL 2
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: no_stats
                        
                        	No stats
                        	**type**\: bool
                        
                        .. attribute:: hits
                        
                        	Number of hits
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_icmp_off
                        
                        	True if ICMP off
                        	**type**\: bool
                        
                        .. attribute:: qos_group
                        
                        	Qos group number
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: next_hop_type
                        
                        	Next hop type
                        	**type**\:  :py:class:`BagAclNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.BagAclNh>`
                        
                        .. attribute:: remark
                        
                        	Remark String
                        	**type**\: str
                        
                        .. attribute:: dynamic
                        
                        	Is dynamic ACE
                        	**type**\: bool
                        
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
                        
                        .. attribute:: fragment_offset_operator
                        
                        	Fragment offset operator
                        	**type**\:  :py:class:`AclPortOperator___ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperator___>`
                        
                        .. attribute:: fragment_offset1
                        
                        	Fragment offset 1
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: fragment_offset2
                        
                        	Fragment offset 2
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: set_ttl
                        
                        	SET TTL
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: fragment_flags
                        
                        	Fragment flags
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: next_hop_info
                        
                        	Next hop info
                        	**type**\: list of  		 :py:class:`NextHopInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo>`
                        
                        .. attribute:: udf
                        
                        	UDF BAG
                        	**type**\: list of  		 :py:class:`Udf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf>`
                        
                        

                        """

                        _prefix = 'ipv4-acl-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence, self).__init__()

                            self.yang_name = "access-list-sequence"
                            self.yang_parent_name = "access-list-sequences"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['sequence_number']
                            self._child_classes = OrderedDict([("hw-next-hop-info", ("hw_next_hop_info", Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo)), ("next-hop-info", ("next_hop_info", Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo)), ("udf", ("udf", Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf))])
                            self._leafs = OrderedDict([
                                ('sequence_number', (YLeaf(YType.uint32, 'sequence-number'), ['int'])),
                                ('item_type', (YLeaf(YType.enumeration, 'item-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper', 'AclAce1_', '')])),
                                ('sequence', (YLeaf(YType.uint32, 'sequence'), ['int'])),
                                ('grant', (YLeaf(YType.enumeration, 'grant'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper', 'AclAction', '')])),
                                ('protocol_operator', (YLeaf(YType.uint16, 'protocol-operator'), ['int'])),
                                ('protocol', (YLeaf(YType.uint16, 'protocol'), ['int'])),
                                ('protocol2', (YLeaf(YType.uint16, 'protocol2'), ['int'])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                ('source_address_mask', (YLeaf(YType.str, 'source-address-mask'), ['str'])),
                                ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                                ('destination_address_mask', (YLeaf(YType.str, 'destination-address-mask'), ['str'])),
                                ('source_operator', (YLeaf(YType.enumeration, 'source-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper', 'AclPortOperator___', '')])),
                                ('source_port1', (YLeaf(YType.uint16, 'source-port1'), ['int'])),
                                ('source_port2', (YLeaf(YType.uint16, 'source-port2'), ['int'])),
                                ('sorce_operator', (YLeaf(YType.enumeration, 'sorce-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper', 'AclPortOperator___', '')])),
                                ('sorce_port1', (YLeaf(YType.uint16, 'sorce-port1'), ['int'])),
                                ('sorce_port2', (YLeaf(YType.uint16, 'sorce-port2'), ['int'])),
                                ('destination_operator', (YLeaf(YType.enumeration, 'destination-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper', 'AclPortOperator___', '')])),
                                ('destination_port1', (YLeaf(YType.uint16, 'destination-port1'), ['int'])),
                                ('destination_port2', (YLeaf(YType.uint16, 'destination-port2'), ['int'])),
                                ('log_option', (YLeaf(YType.enumeration, 'log-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper', 'AclLog', '')])),
                                ('counter_name', (YLeaf(YType.str, 'counter-name'), ['str'])),
                                ('capture', (YLeaf(YType.boolean, 'capture'), ['bool'])),
                                ('dscp_present', (YLeaf(YType.boolean, 'dscp-present'), ['bool'])),
                                ('dscp', (YLeaf(YType.uint8, 'dscp'), ['int'])),
                                ('dscp2', (YLeaf(YType.uint8, 'dscp2'), ['int'])),
                                ('dscp_operator', (YLeaf(YType.uint8, 'dscp-operator'), ['int'])),
                                ('precedence_present', (YLeaf(YType.boolean, 'precedence-present'), ['bool'])),
                                ('precedence', (YLeaf(YType.uint8, 'precedence'), ['int'])),
                                ('tcp_flags_operator', (YLeaf(YType.enumeration, 'tcp-flags-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper', 'AclTcpflagsOperator', '')])),
                                ('tcp_flags', (YLeaf(YType.uint8, 'tcp-flags'), ['int'])),
                                ('tcp_flags_mask', (YLeaf(YType.uint8, 'tcp-flags-mask'), ['int'])),
                                ('fragments', (YLeaf(YType.uint8, 'fragments'), ['int'])),
                                ('packet_length_operator', (YLeaf(YType.enumeration, 'packet-length-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper', 'AclPortOperator___', '')])),
                                ('packet_length1', (YLeaf(YType.uint16, 'packet-length1'), ['int'])),
                                ('packet_length2', (YLeaf(YType.uint16, 'packet-length2'), ['int'])),
                                ('ttl_operator', (YLeaf(YType.enumeration, 'ttl-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper', 'AclPortOperator___', '')])),
                                ('ttl1', (YLeaf(YType.uint16, 'ttl1'), ['int'])),
                                ('ttl2', (YLeaf(YType.uint16, 'ttl2'), ['int'])),
                                ('no_stats', (YLeaf(YType.boolean, 'no-stats'), ['bool'])),
                                ('hits', (YLeaf(YType.uint64, 'hits'), ['int'])),
                                ('is_icmp_off', (YLeaf(YType.boolean, 'is-icmp-off'), ['bool'])),
                                ('qos_group', (YLeaf(YType.uint16, 'qos-group'), ['int'])),
                                ('next_hop_type', (YLeaf(YType.enumeration, 'next-hop-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper', 'BagAclNh', '')])),
                                ('remark', (YLeaf(YType.str, 'remark'), ['str'])),
                                ('dynamic', (YLeaf(YType.boolean, 'dynamic'), ['bool'])),
                                ('source_prefix_group', (YLeaf(YType.str, 'source-prefix-group'), ['str'])),
                                ('destination_prefix_group', (YLeaf(YType.str, 'destination-prefix-group'), ['str'])),
                                ('source_port_group', (YLeaf(YType.str, 'source-port-group'), ['str'])),
                                ('destination_port_group', (YLeaf(YType.str, 'destination-port-group'), ['str'])),
                                ('acl_name', (YLeaf(YType.str, 'acl-name'), ['str'])),
                                ('sequence_str', (YLeaf(YType.str, 'sequence-str'), ['str'])),
                                ('fragment_offset_operator', (YLeaf(YType.enumeration, 'fragment-offset-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper', 'AclPortOperator___', '')])),
                                ('fragment_offset1', (YLeaf(YType.uint16, 'fragment-offset1'), ['int'])),
                                ('fragment_offset2', (YLeaf(YType.uint16, 'fragment-offset2'), ['int'])),
                                ('set_ttl', (YLeaf(YType.uint16, 'set-ttl'), ['int'])),
                                ('fragment_flags', (YLeaf(YType.uint8, 'fragment-flags'), ['int'])),
                            ])
                            self.sequence_number = None
                            self.item_type = None
                            self.sequence = None
                            self.grant = None
                            self.protocol_operator = None
                            self.protocol = None
                            self.protocol2 = None
                            self.source_address = None
                            self.source_address_mask = None
                            self.destination_address = None
                            self.destination_address_mask = None
                            self.source_operator = None
                            self.source_port1 = None
                            self.source_port2 = None
                            self.sorce_operator = None
                            self.sorce_port1 = None
                            self.sorce_port2 = None
                            self.destination_operator = None
                            self.destination_port1 = None
                            self.destination_port2 = None
                            self.log_option = None
                            self.counter_name = None
                            self.capture = None
                            self.dscp_present = None
                            self.dscp = None
                            self.dscp2 = None
                            self.dscp_operator = None
                            self.precedence_present = None
                            self.precedence = None
                            self.tcp_flags_operator = None
                            self.tcp_flags = None
                            self.tcp_flags_mask = None
                            self.fragments = None
                            self.packet_length_operator = None
                            self.packet_length1 = None
                            self.packet_length2 = None
                            self.ttl_operator = None
                            self.ttl1 = None
                            self.ttl2 = None
                            self.no_stats = None
                            self.hits = None
                            self.is_icmp_off = None
                            self.qos_group = None
                            self.next_hop_type = None
                            self.remark = None
                            self.dynamic = None
                            self.source_prefix_group = None
                            self.destination_prefix_group = None
                            self.source_port_group = None
                            self.destination_port_group = None
                            self.acl_name = None
                            self.sequence_str = None
                            self.fragment_offset_operator = None
                            self.fragment_offset1 = None
                            self.fragment_offset2 = None
                            self.set_ttl = None
                            self.fragment_flags = None

                            self.hw_next_hop_info = Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo()
                            self.hw_next_hop_info.parent = self
                            self._children_name_map["hw_next_hop_info"] = "hw-next-hop-info"

                            self.next_hop_info = YList(self)
                            self.udf = YList(self)
                            self._segment_path = lambda: "access-list-sequence" + "[sequence-number='" + str(self.sequence_number) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence, ['sequence_number', u'item_type', u'sequence', u'grant', u'protocol_operator', u'protocol', u'protocol2', u'source_address', u'source_address_mask', u'destination_address', u'destination_address_mask', u'source_operator', u'source_port1', u'source_port2', u'sorce_operator', u'sorce_port1', u'sorce_port2', u'destination_operator', u'destination_port1', u'destination_port2', u'log_option', u'counter_name', u'capture', u'dscp_present', u'dscp', u'dscp2', u'dscp_operator', u'precedence_present', u'precedence', u'tcp_flags_operator', u'tcp_flags', u'tcp_flags_mask', u'fragments', u'packet_length_operator', u'packet_length1', u'packet_length2', u'ttl_operator', u'ttl1', u'ttl2', u'no_stats', u'hits', u'is_icmp_off', u'qos_group', u'next_hop_type', u'remark', u'dynamic', u'source_prefix_group', u'destination_prefix_group', u'source_port_group', u'destination_port_group', u'acl_name', u'sequence_str', u'fragment_offset_operator', u'fragment_offset1', u'fragment_offset2', u'set_ttl', u'fragment_flags'], name, value)


                        class HwNextHopInfo(Entity):
                            """
                            HW Next hop info
                            
                            .. attribute:: next_hop
                            
                            	The Next Hop
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type
                            
                            	the next\-hop type
                            	**type**\:  :py:class:`BagAclNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.BagAclNh>`
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: str
                            
                            	**length:** 0..32
                            
                            

                            """

                            _prefix = 'ipv4-acl-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo, self).__init__()

                                self.yang_name = "hw-next-hop-info"
                                self.yang_parent_name = "access-list-sequence"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('next_hop', (YLeaf(YType.uint32, 'next-hop'), ['int'])),
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper', 'BagAclNh', '')])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                ])
                                self.next_hop = None
                                self.type = None
                                self.vrf_name = None
                                self._segment_path = lambda: "hw-next-hop-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo, [u'next_hop', u'type', u'vrf_name'], name, value)


                        class NextHopInfo(Entity):
                            """
                            Next hop info
                            
                            .. attribute:: next_hop
                            
                            	The next hop
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: track_name
                            
                            	Track name
                            	**type**\: str
                            
                            .. attribute:: status
                            
                            	The next hop status
                            	**type**\:  :py:class:`BagAclNhStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.BagAclNhStatus>`
                            
                            .. attribute:: at_status
                            
                            	The next hop at status
                            	**type**\:  :py:class:`BagAclNhAtStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.BagAclNhAtStatus>`
                            
                            .. attribute:: is_acl_next_hop_exist
                            
                            	The nexthop exist
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'ipv4-acl-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo, self).__init__()

                                self.yang_name = "next-hop-info"
                                self.yang_parent_name = "access-list-sequence"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str'])),
                                    ('track_name', (YLeaf(YType.str, 'track-name'), ['str'])),
                                    ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper', 'BagAclNhStatus', '')])),
                                    ('at_status', (YLeaf(YType.enumeration, 'at-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper', 'BagAclNhAtStatus', '')])),
                                    ('is_acl_next_hop_exist', (YLeaf(YType.boolean, 'is-acl-next-hop-exist'), ['bool'])),
                                ])
                                self.next_hop = None
                                self.track_name = None
                                self.status = None
                                self.at_status = None
                                self.is_acl_next_hop_exist = None
                                self._segment_path = lambda: "next-hop-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo, [u'next_hop', u'track_name', u'status', u'at_status', u'is_acl_next_hop_exist'], name, value)


                        class Udf(Entity):
                            """
                            UDF BAG
                            
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

                            _prefix = 'ipv4-acl-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf, self).__init__()

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
                                self._perform_setattr(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf, [u'udf_name', u'udf_value', u'udf_mask'], name, value)


                class ObjectGroup(Entity):
                    """
                    Object Group in an Access list
                    
                    .. attribute:: obj_grp_info
                    
                    	Object\-group info
                    	**type**\: list of  		 :py:class:`ObjGrpInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup.ObjGrpInfo>`
                    
                    

                    """

                    _prefix = 'ipv4-acl-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup, self).__init__()

                        self.yang_name = "object-group"
                        self.yang_parent_name = "access"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("obj-grp-info", ("obj_grp_info", Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup.ObjGrpInfo))])
                        self._leafs = OrderedDict()

                        self.obj_grp_info = YList(self)
                        self._segment_path = lambda: "object-group"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup, [], name, value)


                    class ObjGrpInfo(Entity):
                        """
                        Object\-group info
                        
                        .. attribute:: obj_grp_name
                        
                        	Object\-group name
                        	**type**\: str
                        
                        	**length:** 0..64
                        
                        .. attribute:: obj_grp_type
                        
                        	Object\-group Type
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-acl-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup.ObjGrpInfo, self).__init__()

                            self.yang_name = "obj-grp-info"
                            self.yang_parent_name = "object-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('obj_grp_name', (YLeaf(YType.str, 'obj-grp-name'), ['str'])),
                                ('obj_grp_type', (YLeaf(YType.uint32, 'obj-grp-type'), ['int'])),
                            ])
                            self.obj_grp_name = None
                            self.obj_grp_type = None
                            self._segment_path = lambda: "obj-grp-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup.ObjGrpInfo, [u'obj_grp_name', u'obj_grp_type'], name, value)


        class Usages(Entity):
            """
            Table of Usage statistics of access lists at
            different nodes
            
            .. attribute:: usage
            
            	Usage statistics of an access list at a node
            	**type**\: list of  		 :py:class:`Usage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Usages.Usage>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv4AclAndPrefixList.AccessListManager.Usages, self).__init__()

                self.yang_name = "usages"
                self.yang_parent_name = "access-list-manager"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("usage", ("usage", Ipv4AclAndPrefixList.AccessListManager.Usages.Usage))])
                self._leafs = OrderedDict()

                self.usage = YList(self)
                self._segment_path = lambda: "usages"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/access-list-manager/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4AclAndPrefixList.AccessListManager.Usages, [], name, value)


            class Usage(Entity):
                """
                Usage statistics of an access list at a node
                
                .. attribute:: node_name
                
                	Node where access list is applied
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: application_id
                
                	Application ID
                	**type**\:  :py:class:`AclUsageAppIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_common_acl_datatypes.AclUsageAppIdEnum>`
                
                .. attribute:: access_list_name
                
                	Name of the access list
                	**type**\: str
                
                .. attribute:: usage_details
                
                	Usage Statistics Details
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ipv4-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.AccessListManager.Usages.Usage, self).__init__()

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
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/access-list-manager/usages/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4AclAndPrefixList.AccessListManager.Usages.Usage, ['node_name', 'application_id', 'access_list_name', 'usage_details'], name, value)


    class Oor(Entity):
        """
        Out Of Resources, Limits to the resources
        allocatable
        
        .. attribute:: details
        
        	Details of the Overall Out Of Resources Limits
        	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.Details>`
        
        .. attribute:: oor_prefixes
        
        	Resource occupation details for prefix lists
        	**type**\:  :py:class:`OorPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.OorPrefixes>`
        
        .. attribute:: oor_accesses
        
        	Resource occupation details for access lists
        	**type**\:  :py:class:`OorAccesses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.OorAccesses>`
        
        .. attribute:: access_list_summary
        
        	Resource limits pertaining to access lists only
        	**type**\:  :py:class:`AccessListSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.AccessListSummary>`
        
        .. attribute:: prefix_list_summary
        
        	Summary of the prefix Lists resource utilization
        	**type**\:  :py:class:`PrefixListSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.PrefixListSummary>`
        
        

        """

        _prefix = 'ipv4-acl-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv4AclAndPrefixList.Oor, self).__init__()

            self.yang_name = "oor"
            self.yang_parent_name = "ipv4-acl-and-prefix-list"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("details", ("details", Ipv4AclAndPrefixList.Oor.Details)), ("oor-prefixes", ("oor_prefixes", Ipv4AclAndPrefixList.Oor.OorPrefixes)), ("oor-accesses", ("oor_accesses", Ipv4AclAndPrefixList.Oor.OorAccesses)), ("access-list-summary", ("access_list_summary", Ipv4AclAndPrefixList.Oor.AccessListSummary)), ("prefix-list-summary", ("prefix_list_summary", Ipv4AclAndPrefixList.Oor.PrefixListSummary))])
            self._leafs = OrderedDict()

            self.details = Ipv4AclAndPrefixList.Oor.Details()
            self.details.parent = self
            self._children_name_map["details"] = "details"

            self.oor_prefixes = Ipv4AclAndPrefixList.Oor.OorPrefixes()
            self.oor_prefixes.parent = self
            self._children_name_map["oor_prefixes"] = "oor-prefixes"

            self.oor_accesses = Ipv4AclAndPrefixList.Oor.OorAccesses()
            self.oor_accesses.parent = self
            self._children_name_map["oor_accesses"] = "oor-accesses"

            self.access_list_summary = Ipv4AclAndPrefixList.Oor.AccessListSummary()
            self.access_list_summary.parent = self
            self._children_name_map["access_list_summary"] = "access-list-summary"

            self.prefix_list_summary = Ipv4AclAndPrefixList.Oor.PrefixListSummary()
            self.prefix_list_summary.parent = self
            self._children_name_map["prefix_list_summary"] = "prefix-list-summary"
            self._segment_path = lambda: "oor"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4AclAndPrefixList.Oor, [], name, value)


        class Details(Entity):
            """
            Details of the Overall Out Of Resources Limits
            
            .. attribute:: default_max_ac_ls
            
            	default max configurable acls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: default_max_ac_es
            
            	default max configurable aces
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: current_configured_ac_ls
            
            	Current configured acls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: current_configured_ac_es
            
            	Current configured aces
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: current_max_configurable_ac_ls
            
            	Current max configurable acls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: current_max_configurable_ac_es
            
            	Current max configurable aces
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_configurable_ac_ls
            
            	max configurable acls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_configurable_ac_es
            
            	max configurable aces
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv4AclAndPrefixList.Oor.Details, self).__init__()

                self.yang_name = "details"
                self.yang_parent_name = "oor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('default_max_ac_ls', (YLeaf(YType.uint32, 'default-max-ac-ls'), ['int'])),
                    ('default_max_ac_es', (YLeaf(YType.uint32, 'default-max-ac-es'), ['int'])),
                    ('current_configured_ac_ls', (YLeaf(YType.uint32, 'current-configured-ac-ls'), ['int'])),
                    ('current_configured_ac_es', (YLeaf(YType.uint32, 'current-configured-ac-es'), ['int'])),
                    ('current_max_configurable_ac_ls', (YLeaf(YType.uint32, 'current-max-configurable-ac-ls'), ['int'])),
                    ('current_max_configurable_ac_es', (YLeaf(YType.uint32, 'current-max-configurable-ac-es'), ['int'])),
                    ('max_configurable_ac_ls', (YLeaf(YType.uint32, 'max-configurable-ac-ls'), ['int'])),
                    ('max_configurable_ac_es', (YLeaf(YType.uint32, 'max-configurable-ac-es'), ['int'])),
                ])
                self.default_max_ac_ls = None
                self.default_max_ac_es = None
                self.current_configured_ac_ls = None
                self.current_configured_ac_es = None
                self.current_max_configurable_ac_ls = None
                self.current_max_configurable_ac_es = None
                self.max_configurable_ac_ls = None
                self.max_configurable_ac_es = None
                self._segment_path = lambda: "details"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4AclAndPrefixList.Oor.Details, [u'default_max_ac_ls', u'default_max_ac_es', u'current_configured_ac_ls', u'current_configured_ac_es', u'current_max_configurable_ac_ls', u'current_max_configurable_ac_es', u'max_configurable_ac_ls', u'max_configurable_ac_es'], name, value)


        class OorPrefixes(Entity):
            """
            Resource occupation details for prefix lists
            
            .. attribute:: oor_prefix
            
            	Resource occupation details for a particular prefix list
            	**type**\: list of  		 :py:class:`OorPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.OorPrefixes.OorPrefix>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv4AclAndPrefixList.Oor.OorPrefixes, self).__init__()

                self.yang_name = "oor-prefixes"
                self.yang_parent_name = "oor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("oor-prefix", ("oor_prefix", Ipv4AclAndPrefixList.Oor.OorPrefixes.OorPrefix))])
                self._leafs = OrderedDict()

                self.oor_prefix = YList(self)
                self._segment_path = lambda: "oor-prefixes"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4AclAndPrefixList.Oor.OorPrefixes, [], name, value)


            class OorPrefix(Entity):
                """
                Resource occupation details for a particular
                prefix list
                
                .. attribute:: prefix_list_name  (key)
                
                	Name of a prefix list
                	**type**\: str
                
                .. attribute:: default_max_ac_ls
                
                	default max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: default_max_ac_es
                
                	default max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_configured_ac_ls
                
                	Current configured acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_configured_ac_es
                
                	Current configured aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_max_configurable_ac_ls
                
                	Current max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_max_configurable_ac_es
                
                	Current max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_configurable_ac_ls
                
                	max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_configurable_ac_es
                
                	max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.Oor.OorPrefixes.OorPrefix, self).__init__()

                    self.yang_name = "oor-prefix"
                    self.yang_parent_name = "oor-prefixes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['prefix_list_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('prefix_list_name', (YLeaf(YType.str, 'prefix-list-name'), ['str'])),
                        ('default_max_ac_ls', (YLeaf(YType.uint32, 'default-max-ac-ls'), ['int'])),
                        ('default_max_ac_es', (YLeaf(YType.uint32, 'default-max-ac-es'), ['int'])),
                        ('current_configured_ac_ls', (YLeaf(YType.uint32, 'current-configured-ac-ls'), ['int'])),
                        ('current_configured_ac_es', (YLeaf(YType.uint32, 'current-configured-ac-es'), ['int'])),
                        ('current_max_configurable_ac_ls', (YLeaf(YType.uint32, 'current-max-configurable-ac-ls'), ['int'])),
                        ('current_max_configurable_ac_es', (YLeaf(YType.uint32, 'current-max-configurable-ac-es'), ['int'])),
                        ('max_configurable_ac_ls', (YLeaf(YType.uint32, 'max-configurable-ac-ls'), ['int'])),
                        ('max_configurable_ac_es', (YLeaf(YType.uint32, 'max-configurable-ac-es'), ['int'])),
                    ])
                    self.prefix_list_name = None
                    self.default_max_ac_ls = None
                    self.default_max_ac_es = None
                    self.current_configured_ac_ls = None
                    self.current_configured_ac_es = None
                    self.current_max_configurable_ac_ls = None
                    self.current_max_configurable_ac_es = None
                    self.max_configurable_ac_ls = None
                    self.max_configurable_ac_es = None
                    self._segment_path = lambda: "oor-prefix" + "[prefix-list-name='" + str(self.prefix_list_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/oor-prefixes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4AclAndPrefixList.Oor.OorPrefixes.OorPrefix, ['prefix_list_name', u'default_max_ac_ls', u'default_max_ac_es', u'current_configured_ac_ls', u'current_configured_ac_es', u'current_max_configurable_ac_ls', u'current_max_configurable_ac_es', u'max_configurable_ac_ls', u'max_configurable_ac_es'], name, value)


        class OorAccesses(Entity):
            """
            Resource occupation details for access lists
            
            .. attribute:: oor_access
            
            	Resource occupation details for a particular access list
            	**type**\: list of  		 :py:class:`OorAccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.OorAccesses.OorAccess>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv4AclAndPrefixList.Oor.OorAccesses, self).__init__()

                self.yang_name = "oor-accesses"
                self.yang_parent_name = "oor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("oor-access", ("oor_access", Ipv4AclAndPrefixList.Oor.OorAccesses.OorAccess))])
                self._leafs = OrderedDict()

                self.oor_access = YList(self)
                self._segment_path = lambda: "oor-accesses"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4AclAndPrefixList.Oor.OorAccesses, [], name, value)


            class OorAccess(Entity):
                """
                Resource occupation details for a particular
                access list
                
                .. attribute:: access_list_name  (key)
                
                	Name of the Access List
                	**type**\: str
                
                .. attribute:: default_max_ac_ls
                
                	default max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: default_max_ac_es
                
                	default max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_configured_ac_ls
                
                	Current configured acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_configured_ac_es
                
                	Current configured aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_max_configurable_ac_ls
                
                	Current max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_max_configurable_ac_es
                
                	Current max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_configurable_ac_ls
                
                	max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_configurable_ac_es
                
                	max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.Oor.OorAccesses.OorAccess, self).__init__()

                    self.yang_name = "oor-access"
                    self.yang_parent_name = "oor-accesses"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['access_list_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                        ('default_max_ac_ls', (YLeaf(YType.uint32, 'default-max-ac-ls'), ['int'])),
                        ('default_max_ac_es', (YLeaf(YType.uint32, 'default-max-ac-es'), ['int'])),
                        ('current_configured_ac_ls', (YLeaf(YType.uint32, 'current-configured-ac-ls'), ['int'])),
                        ('current_configured_ac_es', (YLeaf(YType.uint32, 'current-configured-ac-es'), ['int'])),
                        ('current_max_configurable_ac_ls', (YLeaf(YType.uint32, 'current-max-configurable-ac-ls'), ['int'])),
                        ('current_max_configurable_ac_es', (YLeaf(YType.uint32, 'current-max-configurable-ac-es'), ['int'])),
                        ('max_configurable_ac_ls', (YLeaf(YType.uint32, 'max-configurable-ac-ls'), ['int'])),
                        ('max_configurable_ac_es', (YLeaf(YType.uint32, 'max-configurable-ac-es'), ['int'])),
                    ])
                    self.access_list_name = None
                    self.default_max_ac_ls = None
                    self.default_max_ac_es = None
                    self.current_configured_ac_ls = None
                    self.current_configured_ac_es = None
                    self.current_max_configurable_ac_ls = None
                    self.current_max_configurable_ac_es = None
                    self.max_configurable_ac_ls = None
                    self.max_configurable_ac_es = None
                    self._segment_path = lambda: "oor-access" + "[access-list-name='" + str(self.access_list_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/oor-accesses/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4AclAndPrefixList.Oor.OorAccesses.OorAccess, ['access_list_name', u'default_max_ac_ls', u'default_max_ac_es', u'current_configured_ac_ls', u'current_configured_ac_es', u'current_max_configurable_ac_ls', u'current_max_configurable_ac_es', u'max_configurable_ac_ls', u'max_configurable_ac_es'], name, value)


        class AccessListSummary(Entity):
            """
            Resource limits pertaining to access lists only
            
            .. attribute:: details
            
            	Details containing the resource limits of the access lists
            	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.AccessListSummary.Details>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv4AclAndPrefixList.Oor.AccessListSummary, self).__init__()

                self.yang_name = "access-list-summary"
                self.yang_parent_name = "oor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("details", ("details", Ipv4AclAndPrefixList.Oor.AccessListSummary.Details))])
                self._leafs = OrderedDict()

                self.details = Ipv4AclAndPrefixList.Oor.AccessListSummary.Details()
                self.details.parent = self
                self._children_name_map["details"] = "details"
                self._segment_path = lambda: "access-list-summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4AclAndPrefixList.Oor.AccessListSummary, [], name, value)


            class Details(Entity):
                """
                Details containing the resource limits of the
                access lists
                
                .. attribute:: default_max_ac_ls
                
                	default max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: default_max_ac_es
                
                	default max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_configured_ac_ls
                
                	Current configured acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_configured_ac_es
                
                	Current configured aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_max_configurable_ac_ls
                
                	Current max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_max_configurable_ac_es
                
                	Current max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_configurable_ac_ls
                
                	max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_configurable_ac_es
                
                	max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.Oor.AccessListSummary.Details, self).__init__()

                    self.yang_name = "details"
                    self.yang_parent_name = "access-list-summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('default_max_ac_ls', (YLeaf(YType.uint32, 'default-max-ac-ls'), ['int'])),
                        ('default_max_ac_es', (YLeaf(YType.uint32, 'default-max-ac-es'), ['int'])),
                        ('current_configured_ac_ls', (YLeaf(YType.uint32, 'current-configured-ac-ls'), ['int'])),
                        ('current_configured_ac_es', (YLeaf(YType.uint32, 'current-configured-ac-es'), ['int'])),
                        ('current_max_configurable_ac_ls', (YLeaf(YType.uint32, 'current-max-configurable-ac-ls'), ['int'])),
                        ('current_max_configurable_ac_es', (YLeaf(YType.uint32, 'current-max-configurable-ac-es'), ['int'])),
                        ('max_configurable_ac_ls', (YLeaf(YType.uint32, 'max-configurable-ac-ls'), ['int'])),
                        ('max_configurable_ac_es', (YLeaf(YType.uint32, 'max-configurable-ac-es'), ['int'])),
                    ])
                    self.default_max_ac_ls = None
                    self.default_max_ac_es = None
                    self.current_configured_ac_ls = None
                    self.current_configured_ac_es = None
                    self.current_max_configurable_ac_ls = None
                    self.current_max_configurable_ac_es = None
                    self.max_configurable_ac_ls = None
                    self.max_configurable_ac_es = None
                    self._segment_path = lambda: "details"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/access-list-summary/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4AclAndPrefixList.Oor.AccessListSummary.Details, [u'default_max_ac_ls', u'default_max_ac_es', u'current_configured_ac_ls', u'current_configured_ac_es', u'current_max_configurable_ac_ls', u'current_max_configurable_ac_es', u'max_configurable_ac_ls', u'max_configurable_ac_es'], name, value)


        class PrefixListSummary(Entity):
            """
            Summary of the prefix Lists resource
            utilization
            
            .. attribute:: details
            
            	Summary Detail of the prefix list Resource Utilisation
            	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.PrefixListSummary.Details>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv4AclAndPrefixList.Oor.PrefixListSummary, self).__init__()

                self.yang_name = "prefix-list-summary"
                self.yang_parent_name = "oor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("details", ("details", Ipv4AclAndPrefixList.Oor.PrefixListSummary.Details))])
                self._leafs = OrderedDict()

                self.details = Ipv4AclAndPrefixList.Oor.PrefixListSummary.Details()
                self.details.parent = self
                self._children_name_map["details"] = "details"
                self._segment_path = lambda: "prefix-list-summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4AclAndPrefixList.Oor.PrefixListSummary, [], name, value)


            class Details(Entity):
                """
                Summary Detail of the prefix list Resource
                Utilisation
                
                .. attribute:: default_max_ac_ls
                
                	default max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: default_max_ac_es
                
                	default max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_configured_ac_ls
                
                	Current configured acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_configured_ac_es
                
                	Current configured aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_max_configurable_ac_ls
                
                	Current max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_max_configurable_ac_es
                
                	Current max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_configurable_ac_ls
                
                	max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_configurable_ac_es
                
                	max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.Oor.PrefixListSummary.Details, self).__init__()

                    self.yang_name = "details"
                    self.yang_parent_name = "prefix-list-summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('default_max_ac_ls', (YLeaf(YType.uint32, 'default-max-ac-ls'), ['int'])),
                        ('default_max_ac_es', (YLeaf(YType.uint32, 'default-max-ac-es'), ['int'])),
                        ('current_configured_ac_ls', (YLeaf(YType.uint32, 'current-configured-ac-ls'), ['int'])),
                        ('current_configured_ac_es', (YLeaf(YType.uint32, 'current-configured-ac-es'), ['int'])),
                        ('current_max_configurable_ac_ls', (YLeaf(YType.uint32, 'current-max-configurable-ac-ls'), ['int'])),
                        ('current_max_configurable_ac_es', (YLeaf(YType.uint32, 'current-max-configurable-ac-es'), ['int'])),
                        ('max_configurable_ac_ls', (YLeaf(YType.uint32, 'max-configurable-ac-ls'), ['int'])),
                        ('max_configurable_ac_es', (YLeaf(YType.uint32, 'max-configurable-ac-es'), ['int'])),
                    ])
                    self.default_max_ac_ls = None
                    self.default_max_ac_es = None
                    self.current_configured_ac_ls = None
                    self.current_configured_ac_es = None
                    self.current_max_configurable_ac_ls = None
                    self.current_max_configurable_ac_es = None
                    self.max_configurable_ac_ls = None
                    self.max_configurable_ac_es = None
                    self._segment_path = lambda: "details"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/oor/prefix-list-summary/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4AclAndPrefixList.Oor.PrefixListSummary.Details, [u'default_max_ac_ls', u'default_max_ac_es', u'current_configured_ac_ls', u'current_configured_ac_es', u'current_max_configurable_ac_ls', u'current_max_configurable_ac_es', u'max_configurable_ac_ls', u'max_configurable_ac_es'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv4AclAndPrefixList()
        return self._top_entity

