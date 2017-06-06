""" Cisco_IOS_XR_ipv4_acl_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-acl package operational data.

This module contains definitions
for the following management objects\:
  ipv4\-acl\-and\-prefix\-list\: Root class of IPv4 Oper schema tree

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AclAce1Enum(Enum):
    """
    AclAce1Enum

    ACE Types

    .. data:: normal = 0

    	This is Normal ACE

    .. data:: remark = 1

    	This is Remark ACE

    .. data:: abf = 2

    	This is ABF ACE

    """

    normal = 0

    remark = 1

    abf = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
        return meta._meta_table['AclAce1Enum']


class AclAce1Enum(Enum):
    """
    AclAce1Enum

    ACE Types

    .. data:: normal = 0

    	This is Normal ACE

    .. data:: remark = 1

    	This is Remark ACE

    .. data:: abf = 2

    	This is ABF ACE

    """

    normal = 0

    remark = 1

    abf = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
        return meta._meta_table['AclAce1Enum']


class AclActionEnum(Enum):
    """
    AclActionEnum

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

    deny = 0

    permit = 1

    encrypt = 2

    bypass = 3

    fallthrough = 4

    invalid = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
        return meta._meta_table['AclActionEnum']


class AclLogEnum(Enum):
    """
    AclLogEnum

    Acl log

    .. data:: log_none = 0

    	Log None

    .. data:: log = 1

    	Log Regular

    .. data:: log_input = 2

    	Log Input

    """

    log_none = 0

    log = 1

    log_input = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
        return meta._meta_table['AclLogEnum']


class AclPortOperatorEnum(Enum):
    """
    AclPortOperatorEnum

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

    none = 0

    eq = 1

    gt = 2

    lt = 3

    neq = 4

    range = 5

    onebyte = 8

    twobytes = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
        return meta._meta_table['AclPortOperatorEnum']


class AclPortOperatorEnum(Enum):
    """
    AclPortOperatorEnum

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

    none = 0

    eq = 1

    gt = 2

    lt = 3

    neq = 4

    range = 5

    onebyte = 8

    twobytes = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
        return meta._meta_table['AclPortOperatorEnum']


class AclPortOperatorEnum(Enum):
    """
    AclPortOperatorEnum

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

    none = 0

    eq = 1

    gt = 2

    lt = 3

    neq = 4

    range = 5

    onebyte = 8

    twobytes = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
        return meta._meta_table['AclPortOperatorEnum']


class AclPortOperatorEnum(Enum):
    """
    AclPortOperatorEnum

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

    none = 0

    eq = 1

    gt = 2

    lt = 3

    neq = 4

    range = 5

    onebyte = 8

    twobytes = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
        return meta._meta_table['AclPortOperatorEnum']


class AclTcpflagsOperatorEnum(Enum):
    """
    AclTcpflagsOperatorEnum

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

    match_none = 0

    match_all = 1

    match_any_old = 2

    match_any = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
        return meta._meta_table['AclTcpflagsOperatorEnum']


class BagAclNhAtStatusEnum(Enum):
    """
    BagAclNhAtStatusEnum

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

    unknown = 0

    up = 1

    down = 2

    not_present = 3

    max = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
        return meta._meta_table['BagAclNhAtStatusEnum']


class BagAclNhEnum(Enum):
    """
    BagAclNhEnum

    Bag acl nh

    .. data:: nexthop_none = 0

    	Next Hop None

    .. data:: nexthop_default = 1

    	Nexthop Default

    .. data:: nexthop = 2

    	Nexthop

    """

    nexthop_none = 0

    nexthop_default = 1

    nexthop = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
        return meta._meta_table['BagAclNhEnum']


class BagAclNhStatusEnum(Enum):
    """
    BagAclNhStatusEnum

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

    not_present = 0

    unknown = 1

    down = 2

    up = 3

    max = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
        return meta._meta_table['BagAclNhStatusEnum']



class Ipv4AclAndPrefixList(object):
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
        self.access_list_manager = Ipv4AclAndPrefixList.AccessListManager()
        self.access_list_manager.parent = self
        self.oor = Ipv4AclAndPrefixList.Oor()
        self.oor.parent = self


    class AccessListManager(object):
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
            self.parent = None
            self.accesses = Ipv4AclAndPrefixList.AccessListManager.Accesses()
            self.accesses.parent = self
            self.prefixes = Ipv4AclAndPrefixList.AccessListManager.Prefixes()
            self.prefixes.parent = self
            self.usages = Ipv4AclAndPrefixList.AccessListManager.Usages()
            self.usages.parent = self


        class Prefixes(object):
            """
            Table of prefix lists
            
            .. attribute:: prefix
            
            	Name of the prefix list
            	**type**\: list of    :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.prefix = YList()
                self.prefix.parent = self
                self.prefix.name = 'prefix'


            class Prefix(object):
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
                    self.parent = None
                    self.prefix_list_name = None
                    self.prefix_list_sequences = Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences()
                    self.prefix_list_sequences.parent = self


                class PrefixListSequences(object):
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
                        self.parent = None
                        self.prefix_list_sequence = YList()
                        self.prefix_list_sequence.parent = self
                        self.prefix_list_sequence.name = 'prefix_list_sequence'


                    class PrefixListSequence(object):
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
                        	**type**\:   :py:class:`AclActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclActionEnum>`
                        
                        .. attribute:: hits
                        
                        	Number of hits
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: item_type
                        
                        	ACE type (prefix, remark)
                        	**type**\:   :py:class:`AclAce1Enum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclAce1Enum>`
                        
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
                        	**type**\:   :py:class:`AclPortOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperatorEnum>`
                        
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
                            self.parent = None
                            self.sequence_number = None
                            self.acl_name = None
                            self.grant = None
                            self.hits = None
                            self.item_type = None
                            self.maximum_length = None
                            self.minimum_length = None
                            self.operator = None
                            self.prefix = None
                            self.prefix_length = None
                            self.remark = None
                            self.sequence = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.sequence_number is None:
                                raise YPYModelError('Key property sequence_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-acl-oper:prefix-list-sequence[Cisco-IOS-XR-ipv4-acl-oper:sequence-number = ' + str(self.sequence_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sequence_number is not None:
                                return True

                            if self.acl_name is not None:
                                return True

                            if self.grant is not None:
                                return True

                            if self.hits is not None:
                                return True

                            if self.item_type is not None:
                                return True

                            if self.maximum_length is not None:
                                return True

                            if self.minimum_length is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.prefix is not None:
                                return True

                            if self.prefix_length is not None:
                                return True

                            if self.remark is not None:
                                return True

                            if self.sequence is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                            return meta._meta_table['Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-acl-oper:prefix-list-sequences'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.prefix_list_sequence is not None:
                            for child_ref in self.prefix_list_sequence:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                        return meta._meta_table['Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences']['meta_info']

                @property
                def _common_path(self):
                    if self.prefix_list_name is None:
                        raise YPYModelError('Key property prefix_list_name is None')

                    return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/Cisco-IOS-XR-ipv4-acl-oper:access-list-manager/Cisco-IOS-XR-ipv4-acl-oper:prefixes/Cisco-IOS-XR-ipv4-acl-oper:prefix[Cisco-IOS-XR-ipv4-acl-oper:prefix-list-name = ' + str(self.prefix_list_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.prefix_list_name is not None:
                        return True

                    if self.prefix_list_sequences is not None and self.prefix_list_sequences._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                    return meta._meta_table['Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/Cisco-IOS-XR-ipv4-acl-oper:access-list-manager/Cisco-IOS-XR-ipv4-acl-oper:prefixes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.prefix is not None:
                    for child_ref in self.prefix:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                return meta._meta_table['Ipv4AclAndPrefixList.AccessListManager.Prefixes']['meta_info']


        class Accesses(object):
            """
            Access listL class displaying Usage and Entries
            
            .. attribute:: access
            
            	Name of the Access List
            	**type**\: list of    :py:class:`Access <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.access = YList()
                self.access.parent = self
                self.access.name = 'access'


            class Access(object):
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
                    self.parent = None
                    self.access_list_name = None
                    self.access_list_sequences = Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences()
                    self.access_list_sequences.parent = self
                    self.object_group = Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup()
                    self.object_group.parent = self


                class AccessListSequences(object):
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
                        self.parent = None
                        self.access_list_sequence = YList()
                        self.access_list_sequence.parent = self
                        self.access_list_sequence.name = 'access_list_sequence'


                    class AccessListSequence(object):
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
                        	**type**\:   :py:class:`AclPortOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperatorEnum>`
                        
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
                        	**type**\:   :py:class:`AclPortOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperatorEnum>`
                        
                        .. attribute:: fragments
                        
                        	Fragments
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: grant
                        
                        	Permit/deny
                        	**type**\:   :py:class:`AclActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclActionEnum>`
                        
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
                        	**type**\:   :py:class:`AclAce1Enum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclAce1Enum>`
                        
                        .. attribute:: log_option
                        
                        	Log option
                        	**type**\:   :py:class:`AclLogEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclLogEnum>`
                        
                        .. attribute:: next_hop_info
                        
                        	Next hop info
                        	**type**\: list of    :py:class:`NextHopInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo>`
                        
                        .. attribute:: next_hop_type
                        
                        	Next hop type
                        	**type**\:   :py:class:`BagAclNhEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.BagAclNhEnum>`
                        
                        .. attribute:: no_stats
                        
                        	No stats
                        	**type**\:  bool
                        
                        .. attribute:: port_length1
                        
                        	Port length 1
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: port_length2
                        
                        	Port length 2
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: port_length_operator
                        
                        	Port length operator
                        	**type**\:   :py:class:`AclPortOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperatorEnum>`
                        
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
                        	**type**\:   :py:class:`AclPortOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperatorEnum>`
                        
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
                        	**type**\:   :py:class:`AclPortOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperatorEnum>`
                        
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
                        	**type**\:   :py:class:`AclTcpflagsOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclTcpflagsOperatorEnum>`
                        
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
                        	**type**\:   :py:class:`AclPortOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.AclPortOperatorEnum>`
                        
                        .. attribute:: udf
                        
                        	UDF BAG
                        	**type**\: list of    :py:class:`Udf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf>`
                        
                        

                        """

                        _prefix = 'ipv4-acl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sequence_number = None
                            self.acl_name = None
                            self.capture = None
                            self.counter_name = None
                            self.destination_address = None
                            self.destination_address_mask = None
                            self.destination_operator = None
                            self.destination_port1 = None
                            self.destination_port2 = None
                            self.destination_port_group = None
                            self.destination_prefix_group = None
                            self.dscp = None
                            self.dscp2 = None
                            self.dscp_operator = None
                            self.dscp_present = None
                            self.dynamic = None
                            self.fragment_offset1 = None
                            self.fragment_offset2 = None
                            self.fragment_offset_operator = None
                            self.fragments = None
                            self.grant = None
                            self.hits = None
                            self.hw_next_hop_info = Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo()
                            self.hw_next_hop_info.parent = self
                            self.is_icmp_off = None
                            self.item_type = None
                            self.log_option = None
                            self.next_hop_info = YList()
                            self.next_hop_info.parent = self
                            self.next_hop_info.name = 'next_hop_info'
                            self.next_hop_type = None
                            self.no_stats = None
                            self.port_length1 = None
                            self.port_length2 = None
                            self.port_length_operator = None
                            self.precedence = None
                            self.precedence_present = None
                            self.protocol = None
                            self.protocol2 = None
                            self.protocol_operator = None
                            self.qos_group = None
                            self.remark = None
                            self.sequence = None
                            self.sequence_str = None
                            self.sorce_operator = None
                            self.sorce_port1 = None
                            self.sorce_port2 = None
                            self.source_address = None
                            self.source_address_mask = None
                            self.source_operator = None
                            self.source_port1 = None
                            self.source_port2 = None
                            self.source_port_group = None
                            self.source_prefix_group = None
                            self.tcp_flags = None
                            self.tcp_flags_mask = None
                            self.tcp_flags_operator = None
                            self.ttl1 = None
                            self.ttl2 = None
                            self.ttl_operator = None
                            self.udf = YList()
                            self.udf.parent = self
                            self.udf.name = 'udf'


                        class HwNextHopInfo(object):
                            """
                            HW Next hop info
                            
                            .. attribute:: next_hop
                            
                            	The Next Hop
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type
                            
                            	the next\-hop type
                            	**type**\:   :py:class:`BagAclNhEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.BagAclNhEnum>`
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\:  str
                            
                            	**length:** 0..32
                            
                            

                            """

                            _prefix = 'ipv4-acl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.next_hop = None
                                self.type = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-acl-oper:hw-next-hop-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.next_hop is not None:
                                    return True

                                if self.type is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                                return meta._meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo']['meta_info']


                        class NextHopInfo(object):
                            """
                            Next hop info
                            
                            .. attribute:: at_status
                            
                            	The next hop at status
                            	**type**\:   :py:class:`BagAclNhAtStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.BagAclNhAtStatusEnum>`
                            
                            .. attribute:: is_acl_next_hop_exist
                            
                            	The nexthop exist
                            	**type**\:  bool
                            
                            .. attribute:: next_hop
                            
                            	The next hop
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: status
                            
                            	The next hop status
                            	**type**\:   :py:class:`BagAclNhStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.BagAclNhStatusEnum>`
                            
                            .. attribute:: track_name
                            
                            	Track name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ipv4-acl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.at_status = None
                                self.is_acl_next_hop_exist = None
                                self.next_hop = None
                                self.status = None
                                self.track_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-acl-oper:next-hop-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.at_status is not None:
                                    return True

                                if self.is_acl_next_hop_exist is not None:
                                    return True

                                if self.next_hop is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.track_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                                return meta._meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo']['meta_info']


                        class Udf(object):
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
                                self.parent = None
                                self.udf_mask = None
                                self.udf_name = None
                                self.udf_value = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-acl-oper:udf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.udf_mask is not None:
                                    return True

                                if self.udf_name is not None:
                                    return True

                                if self.udf_value is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                                return meta._meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.sequence_number is None:
                                raise YPYModelError('Key property sequence_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-acl-oper:access-list-sequence[Cisco-IOS-XR-ipv4-acl-oper:sequence-number = ' + str(self.sequence_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sequence_number is not None:
                                return True

                            if self.acl_name is not None:
                                return True

                            if self.capture is not None:
                                return True

                            if self.counter_name is not None:
                                return True

                            if self.destination_address is not None:
                                return True

                            if self.destination_address_mask is not None:
                                return True

                            if self.destination_operator is not None:
                                return True

                            if self.destination_port1 is not None:
                                return True

                            if self.destination_port2 is not None:
                                return True

                            if self.destination_port_group is not None:
                                return True

                            if self.destination_prefix_group is not None:
                                return True

                            if self.dscp is not None:
                                return True

                            if self.dscp2 is not None:
                                return True

                            if self.dscp_operator is not None:
                                return True

                            if self.dscp_present is not None:
                                return True

                            if self.dynamic is not None:
                                return True

                            if self.fragment_offset1 is not None:
                                return True

                            if self.fragment_offset2 is not None:
                                return True

                            if self.fragment_offset_operator is not None:
                                return True

                            if self.fragments is not None:
                                return True

                            if self.grant is not None:
                                return True

                            if self.hits is not None:
                                return True

                            if self.hw_next_hop_info is not None and self.hw_next_hop_info._has_data():
                                return True

                            if self.is_icmp_off is not None:
                                return True

                            if self.item_type is not None:
                                return True

                            if self.log_option is not None:
                                return True

                            if self.next_hop_info is not None:
                                for child_ref in self.next_hop_info:
                                    if child_ref._has_data():
                                        return True

                            if self.next_hop_type is not None:
                                return True

                            if self.no_stats is not None:
                                return True

                            if self.port_length1 is not None:
                                return True

                            if self.port_length2 is not None:
                                return True

                            if self.port_length_operator is not None:
                                return True

                            if self.precedence is not None:
                                return True

                            if self.precedence_present is not None:
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

                            if self.sequence is not None:
                                return True

                            if self.sequence_str is not None:
                                return True

                            if self.sorce_operator is not None:
                                return True

                            if self.sorce_port1 is not None:
                                return True

                            if self.sorce_port2 is not None:
                                return True

                            if self.source_address is not None:
                                return True

                            if self.source_address_mask is not None:
                                return True

                            if self.source_operator is not None:
                                return True

                            if self.source_port1 is not None:
                                return True

                            if self.source_port2 is not None:
                                return True

                            if self.source_port_group is not None:
                                return True

                            if self.source_prefix_group is not None:
                                return True

                            if self.tcp_flags is not None:
                                return True

                            if self.tcp_flags_mask is not None:
                                return True

                            if self.tcp_flags_operator is not None:
                                return True

                            if self.ttl1 is not None:
                                return True

                            if self.ttl2 is not None:
                                return True

                            if self.ttl_operator is not None:
                                return True

                            if self.udf is not None:
                                for child_ref in self.udf:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                            return meta._meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-acl-oper:access-list-sequences'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.access_list_sequence is not None:
                            for child_ref in self.access_list_sequence:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                        return meta._meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences']['meta_info']


                class ObjectGroup(object):
                    """
                    Object Group in an Access list
                    
                    .. attribute:: obj_grp_info
                    
                    	Object\-group info
                    	**type**\: list of    :py:class:`ObjGrpInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup.ObjGrpInfo>`
                    
                    

                    """

                    _prefix = 'ipv4-acl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.obj_grp_info = YList()
                        self.obj_grp_info.parent = self
                        self.obj_grp_info.name = 'obj_grp_info'


                    class ObjGrpInfo(object):
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
                            self.parent = None
                            self.obj_grp_name = None
                            self.obj_grp_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-acl-oper:obj-grp-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.obj_grp_name is not None:
                                return True

                            if self.obj_grp_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                            return meta._meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup.ObjGrpInfo']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-acl-oper:object-group'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.obj_grp_info is not None:
                            for child_ref in self.obj_grp_info:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                        return meta._meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.ObjectGroup']['meta_info']

                @property
                def _common_path(self):
                    if self.access_list_name is None:
                        raise YPYModelError('Key property access_list_name is None')

                    return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/Cisco-IOS-XR-ipv4-acl-oper:access-list-manager/Cisco-IOS-XR-ipv4-acl-oper:accesses/Cisco-IOS-XR-ipv4-acl-oper:access[Cisco-IOS-XR-ipv4-acl-oper:access-list-name = ' + str(self.access_list_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.access_list_name is not None:
                        return True

                    if self.access_list_sequences is not None and self.access_list_sequences._has_data():
                        return True

                    if self.object_group is not None and self.object_group._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                    return meta._meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses.Access']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/Cisco-IOS-XR-ipv4-acl-oper:access-list-manager/Cisco-IOS-XR-ipv4-acl-oper:accesses'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.access is not None:
                    for child_ref in self.access:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                return meta._meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses']['meta_info']


        class Usages(object):
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
                self.parent = None
                self.usage = YList()
                self.usage.parent = self
                self.usage.name = 'usage'


            class Usage(object):
                """
                Usage statistics of an access list at a node
                
                .. attribute:: access_list_name
                
                	Name of the access list
                	**type**\:  str
                
                .. attribute:: application_id
                
                	Application ID
                	**type**\:   :py:class:`AclUsageAppIdEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_common_acl_datatypes.AclUsageAppIdEnumEnum>`
                
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
                    self.parent = None
                    self.access_list_name = None
                    self.application_id = None
                    self.node_name = None
                    self.usage_details = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/Cisco-IOS-XR-ipv4-acl-oper:access-list-manager/Cisco-IOS-XR-ipv4-acl-oper:usages/Cisco-IOS-XR-ipv4-acl-oper:usage'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.access_list_name is not None:
                        return True

                    if self.application_id is not None:
                        return True

                    if self.node_name is not None:
                        return True

                    if self.usage_details is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                    return meta._meta_table['Ipv4AclAndPrefixList.AccessListManager.Usages.Usage']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/Cisco-IOS-XR-ipv4-acl-oper:access-list-manager/Cisco-IOS-XR-ipv4-acl-oper:usages'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.usage is not None:
                    for child_ref in self.usage:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                return meta._meta_table['Ipv4AclAndPrefixList.AccessListManager.Usages']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/Cisco-IOS-XR-ipv4-acl-oper:access-list-manager'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.accesses is not None and self.accesses._has_data():
                return True

            if self.prefixes is not None and self.prefixes._has_data():
                return True

            if self.usages is not None and self.usages._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
            return meta._meta_table['Ipv4AclAndPrefixList.AccessListManager']['meta_info']


    class Oor(object):
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
            self.parent = None
            self.access_list_summary = Ipv4AclAndPrefixList.Oor.AccessListSummary()
            self.access_list_summary.parent = self
            self.details = Ipv4AclAndPrefixList.Oor.Details()
            self.details.parent = self
            self.oor_accesses = Ipv4AclAndPrefixList.Oor.OorAccesses()
            self.oor_accesses.parent = self
            self.oor_prefixes = Ipv4AclAndPrefixList.Oor.OorPrefixes()
            self.oor_prefixes.parent = self
            self.prefix_list_summary = Ipv4AclAndPrefixList.Oor.PrefixListSummary()
            self.prefix_list_summary.parent = self


        class Details(object):
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
                self.parent = None
                self.current_configured_ac_es = None
                self.current_configured_ac_ls = None
                self.current_max_configurable_ac_es = None
                self.current_max_configurable_ac_ls = None
                self.default_max_ac_es = None
                self.default_max_ac_ls = None
                self.max_configurable_ac_es = None
                self.max_configurable_ac_ls = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/Cisco-IOS-XR-ipv4-acl-oper:oor/Cisco-IOS-XR-ipv4-acl-oper:details'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.current_configured_ac_es is not None:
                    return True

                if self.current_configured_ac_ls is not None:
                    return True

                if self.current_max_configurable_ac_es is not None:
                    return True

                if self.current_max_configurable_ac_ls is not None:
                    return True

                if self.default_max_ac_es is not None:
                    return True

                if self.default_max_ac_ls is not None:
                    return True

                if self.max_configurable_ac_es is not None:
                    return True

                if self.max_configurable_ac_ls is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                return meta._meta_table['Ipv4AclAndPrefixList.Oor.Details']['meta_info']


        class OorPrefixes(object):
            """
            Resource occupation details for prefix lists
            
            .. attribute:: oor_prefix
            
            	Resource occupation details for a particular prefix list
            	**type**\: list of    :py:class:`OorPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.OorPrefixes.OorPrefix>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.oor_prefix = YList()
                self.oor_prefix.parent = self
                self.oor_prefix.name = 'oor_prefix'


            class OorPrefix(object):
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
                    self.parent = None
                    self.prefix_list_name = None
                    self.current_configured_ac_es = None
                    self.current_configured_ac_ls = None
                    self.current_max_configurable_ac_es = None
                    self.current_max_configurable_ac_ls = None
                    self.default_max_ac_es = None
                    self.default_max_ac_ls = None
                    self.max_configurable_ac_es = None
                    self.max_configurable_ac_ls = None

                @property
                def _common_path(self):
                    if self.prefix_list_name is None:
                        raise YPYModelError('Key property prefix_list_name is None')

                    return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/Cisco-IOS-XR-ipv4-acl-oper:oor/Cisco-IOS-XR-ipv4-acl-oper:oor-prefixes/Cisco-IOS-XR-ipv4-acl-oper:oor-prefix[Cisco-IOS-XR-ipv4-acl-oper:prefix-list-name = ' + str(self.prefix_list_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.prefix_list_name is not None:
                        return True

                    if self.current_configured_ac_es is not None:
                        return True

                    if self.current_configured_ac_ls is not None:
                        return True

                    if self.current_max_configurable_ac_es is not None:
                        return True

                    if self.current_max_configurable_ac_ls is not None:
                        return True

                    if self.default_max_ac_es is not None:
                        return True

                    if self.default_max_ac_ls is not None:
                        return True

                    if self.max_configurable_ac_es is not None:
                        return True

                    if self.max_configurable_ac_ls is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                    return meta._meta_table['Ipv4AclAndPrefixList.Oor.OorPrefixes.OorPrefix']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/Cisco-IOS-XR-ipv4-acl-oper:oor/Cisco-IOS-XR-ipv4-acl-oper:oor-prefixes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.oor_prefix is not None:
                    for child_ref in self.oor_prefix:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                return meta._meta_table['Ipv4AclAndPrefixList.Oor.OorPrefixes']['meta_info']


        class OorAccesses(object):
            """
            Resource occupation details for access lists
            
            .. attribute:: oor_access
            
            	Resource occupation details for a particular access list
            	**type**\: list of    :py:class:`OorAccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.OorAccesses.OorAccess>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.oor_access = YList()
                self.oor_access.parent = self
                self.oor_access.name = 'oor_access'


            class OorAccess(object):
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
                    self.parent = None
                    self.access_list_name = None
                    self.current_configured_ac_es = None
                    self.current_configured_ac_ls = None
                    self.current_max_configurable_ac_es = None
                    self.current_max_configurable_ac_ls = None
                    self.default_max_ac_es = None
                    self.default_max_ac_ls = None
                    self.max_configurable_ac_es = None
                    self.max_configurable_ac_ls = None

                @property
                def _common_path(self):
                    if self.access_list_name is None:
                        raise YPYModelError('Key property access_list_name is None')

                    return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/Cisco-IOS-XR-ipv4-acl-oper:oor/Cisco-IOS-XR-ipv4-acl-oper:oor-accesses/Cisco-IOS-XR-ipv4-acl-oper:oor-access[Cisco-IOS-XR-ipv4-acl-oper:access-list-name = ' + str(self.access_list_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.access_list_name is not None:
                        return True

                    if self.current_configured_ac_es is not None:
                        return True

                    if self.current_configured_ac_ls is not None:
                        return True

                    if self.current_max_configurable_ac_es is not None:
                        return True

                    if self.current_max_configurable_ac_ls is not None:
                        return True

                    if self.default_max_ac_es is not None:
                        return True

                    if self.default_max_ac_ls is not None:
                        return True

                    if self.max_configurable_ac_es is not None:
                        return True

                    if self.max_configurable_ac_ls is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                    return meta._meta_table['Ipv4AclAndPrefixList.Oor.OorAccesses.OorAccess']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/Cisco-IOS-XR-ipv4-acl-oper:oor/Cisco-IOS-XR-ipv4-acl-oper:oor-accesses'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.oor_access is not None:
                    for child_ref in self.oor_access:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                return meta._meta_table['Ipv4AclAndPrefixList.Oor.OorAccesses']['meta_info']


        class AccessListSummary(object):
            """
            Resource limits pertaining to access lists only
            
            .. attribute:: details
            
            	Details containing the resource limits of the access lists
            	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_oper.Ipv4AclAndPrefixList.Oor.AccessListSummary.Details>`
            
            

            """

            _prefix = 'ipv4-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.details = Ipv4AclAndPrefixList.Oor.AccessListSummary.Details()
                self.details.parent = self


            class Details(object):
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
                    self.parent = None
                    self.current_configured_ac_es = None
                    self.current_configured_ac_ls = None
                    self.current_max_configurable_ac_es = None
                    self.current_max_configurable_ac_ls = None
                    self.default_max_ac_es = None
                    self.default_max_ac_ls = None
                    self.max_configurable_ac_es = None
                    self.max_configurable_ac_ls = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/Cisco-IOS-XR-ipv4-acl-oper:oor/Cisco-IOS-XR-ipv4-acl-oper:access-list-summary/Cisco-IOS-XR-ipv4-acl-oper:details'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.current_configured_ac_es is not None:
                        return True

                    if self.current_configured_ac_ls is not None:
                        return True

                    if self.current_max_configurable_ac_es is not None:
                        return True

                    if self.current_max_configurable_ac_ls is not None:
                        return True

                    if self.default_max_ac_es is not None:
                        return True

                    if self.default_max_ac_ls is not None:
                        return True

                    if self.max_configurable_ac_es is not None:
                        return True

                    if self.max_configurable_ac_ls is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                    return meta._meta_table['Ipv4AclAndPrefixList.Oor.AccessListSummary.Details']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/Cisco-IOS-XR-ipv4-acl-oper:oor/Cisco-IOS-XR-ipv4-acl-oper:access-list-summary'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.details is not None and self.details._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                return meta._meta_table['Ipv4AclAndPrefixList.Oor.AccessListSummary']['meta_info']


        class PrefixListSummary(object):
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
                self.parent = None
                self.details = Ipv4AclAndPrefixList.Oor.PrefixListSummary.Details()
                self.details.parent = self


            class Details(object):
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
                    self.parent = None
                    self.current_configured_ac_es = None
                    self.current_configured_ac_ls = None
                    self.current_max_configurable_ac_es = None
                    self.current_max_configurable_ac_ls = None
                    self.default_max_ac_es = None
                    self.default_max_ac_ls = None
                    self.max_configurable_ac_es = None
                    self.max_configurable_ac_ls = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/Cisco-IOS-XR-ipv4-acl-oper:oor/Cisco-IOS-XR-ipv4-acl-oper:prefix-list-summary/Cisco-IOS-XR-ipv4-acl-oper:details'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.current_configured_ac_es is not None:
                        return True

                    if self.current_configured_ac_ls is not None:
                        return True

                    if self.current_max_configurable_ac_es is not None:
                        return True

                    if self.current_max_configurable_ac_ls is not None:
                        return True

                    if self.default_max_ac_es is not None:
                        return True

                    if self.default_max_ac_ls is not None:
                        return True

                    if self.max_configurable_ac_es is not None:
                        return True

                    if self.max_configurable_ac_ls is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                    return meta._meta_table['Ipv4AclAndPrefixList.Oor.PrefixListSummary.Details']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/Cisco-IOS-XR-ipv4-acl-oper:oor/Cisco-IOS-XR-ipv4-acl-oper:prefix-list-summary'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.details is not None and self.details._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
                return meta._meta_table['Ipv4AclAndPrefixList.Oor.PrefixListSummary']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list/Cisco-IOS-XR-ipv4-acl-oper:oor'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.access_list_summary is not None and self.access_list_summary._has_data():
                return True

            if self.details is not None and self.details._has_data():
                return True

            if self.oor_accesses is not None and self.oor_accesses._has_data():
                return True

            if self.oor_prefixes is not None and self.oor_prefixes._has_data():
                return True

            if self.prefix_list_summary is not None and self.prefix_list_summary._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
            return meta._meta_table['Ipv4AclAndPrefixList.Oor']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-acl-oper:ipv4-acl-and-prefix-list'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.access_list_manager is not None and self.access_list_manager._has_data():
            return True

        if self.oor is not None and self.oor._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_oper as meta
        return meta._meta_table['Ipv4AclAndPrefixList']['meta_info']


