""" Cisco_IOS_XR_ipv6_acl_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-acl package operational data.

This module contains definitions
for the following management objects\:
  ipv6\-acl\-and\-prefix\-list\: Root class of IPv6 Oper schema tree

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
        return meta._meta_table['BagAclNhStatusEnum']



class Ipv6AclAndPrefixList(object):
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
        self.access_list_manager = Ipv6AclAndPrefixList.AccessListManager()
        self.access_list_manager.parent = self
        self.oor = Ipv6AclAndPrefixList.Oor()
        self.oor.parent = self


    class AccessListManager(object):
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
            self.parent = None
            self.accesses = Ipv6AclAndPrefixList.AccessListManager.Accesses()
            self.accesses.parent = self
            self.prefixes = Ipv6AclAndPrefixList.AccessListManager.Prefixes()
            self.prefixes.parent = self
            self.usages = Ipv6AclAndPrefixList.AccessListManager.Usages()
            self.usages.parent = self


        class Prefixes(object):
            """
            Table of prefix lists
            
            .. attribute:: prefix
            
            	Name of the prefix list
            	**type**\: list of    :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
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
                
                	**length:** 1..65
                
                .. attribute:: prefix_list_sequences
                
                	Table of all the SequenceNumbers per prefix list
                	**type**\:   :py:class:`PrefixListSequences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences>`
                
                

                """

                _prefix = 'ipv6-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.prefix_list_name = None
                    self.prefix_list_sequences = Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences()
                    self.prefix_list_sequences.parent = self


                class PrefixListSequences(object):
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
                        	**type**\:   :py:class:`AclAce1Enum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclAce1Enum>`
                        
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
                        	**type**\:   :py:class:`AclPortOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperatorEnum>`
                        
                        .. attribute:: is_packet_allow_or_deny
                        
                        	Grant value permit/deny 
                        	**type**\:   :py:class:`AclActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclActionEnum>`
                        
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
                            self.parent = None
                            self.sequence_number = None
                            self.acl_name = None
                            self.hits = None
                            self.is_ace_sequence_number = None
                            self.is_ace_type = None
                            self.is_address_in_numbers = None
                            self.is_address_mask_length = None
                            self.is_comment_for_entry = None
                            self.is_length_operator = None
                            self.is_packet_allow_or_deny = None
                            self.is_packet_maximum_length = None
                            self.is_packet_minimum_length = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.sequence_number is None:
                                raise YPYModelError('Key property sequence_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-oper:prefix-list-sequence[Cisco-IOS-XR-ipv6-acl-oper:sequence-number = ' + str(self.sequence_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sequence_number is not None:
                                return True

                            if self.acl_name is not None:
                                return True

                            if self.hits is not None:
                                return True

                            if self.is_ace_sequence_number is not None:
                                return True

                            if self.is_ace_type is not None:
                                return True

                            if self.is_address_in_numbers is not None:
                                return True

                            if self.is_address_mask_length is not None:
                                return True

                            if self.is_comment_for_entry is not None:
                                return True

                            if self.is_length_operator is not None:
                                return True

                            if self.is_packet_allow_or_deny is not None:
                                return True

                            if self.is_packet_maximum_length is not None:
                                return True

                            if self.is_packet_minimum_length is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                            return meta._meta_table['Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-oper:prefix-list-sequences'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                        return meta._meta_table['Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences']['meta_info']

                @property
                def _common_path(self):
                    if self.prefix_list_name is None:
                        raise YPYModelError('Key property prefix_list_name is None')

                    return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-oper:access-list-manager/Cisco-IOS-XR-ipv6-acl-oper:prefixes/Cisco-IOS-XR-ipv6-acl-oper:prefix[Cisco-IOS-XR-ipv6-acl-oper:prefix-list-name = ' + str(self.prefix_list_name) + ']'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                    return meta._meta_table['Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-oper:access-list-manager/Cisco-IOS-XR-ipv6-acl-oper:prefixes'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                return meta._meta_table['Ipv6AclAndPrefixList.AccessListManager.Prefixes']['meta_info']


        class Usages(object):
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
                self.parent = None
                self.usage = YList()
                self.usage.parent = self
                self.usage.name = 'usage'


            class Usage(object):
                """
                Usage statistics of an ACL at a node
                
                .. attribute:: access_list_name
                
                	Name of the ACL
                	**type**\:  str
                
                	**length:** 1..65
                
                .. attribute:: application_id
                
                	Application ID
                	**type**\:   :py:class:`AclUsageAppIdEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_common_acl_datatypes.AclUsageAppIdEnumEnum>`
                
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
                    self.parent = None
                    self.access_list_name = None
                    self.application_id = None
                    self.node_name = None
                    self.usage_details = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-oper:access-list-manager/Cisco-IOS-XR-ipv6-acl-oper:usages/Cisco-IOS-XR-ipv6-acl-oper:usage'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                    return meta._meta_table['Ipv6AclAndPrefixList.AccessListManager.Usages.Usage']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-oper:access-list-manager/Cisco-IOS-XR-ipv6-acl-oper:usages'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                return meta._meta_table['Ipv6AclAndPrefixList.AccessListManager.Usages']['meta_info']


        class Accesses(object):
            """
            ACL class displaying Usage and Entries
            
            .. attribute:: access
            
            	Name of the Access List
            	**type**\: list of    :py:class:`Access <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses.Access>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
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
                
                	**length:** 1..65
                
                .. attribute:: access_list_sequences
                
                	Table of all the sequence numbers per ACL
                	**type**\:   :py:class:`AccessListSequences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences>`
                
                

                """

                _prefix = 'ipv6-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.access_list_name = None
                    self.access_list_sequences = Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences()
                    self.access_list_sequences.parent = self


                class AccessListSequences(object):
                    """
                    Table of all the sequence numbers per ACL
                    
                    .. attribute:: access_list_sequence
                    
                    	Sequence number of an ACL entry
                    	**type**\: list of    :py:class:`AccessListSequence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence>`
                    
                    

                    """

                    _prefix = 'ipv6-acl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.access_list_sequence = YList()
                        self.access_list_sequence.parent = self
                        self.access_list_sequence.name = 'access_list_sequence'


                    class AccessListSequence(object):
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
                        	**type**\:   :py:class:`AclAce1Enum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclAce1Enum>`
                        
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
                        	**type**\:   :py:class:`AclPortOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperatorEnum>`
                        
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
                        	**type**\:   :py:class:`AclLogEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclLogEnum>`
                        
                        .. attribute:: is_packet_allow_or_deny
                        
                        	Grant value permit/deny 
                        	**type**\:   :py:class:`AclActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclActionEnum>`
                        
                        .. attribute:: is_packet_length_end
                        
                        	IsPacketLengthEnd
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_packet_length_operator
                        
                        	Match if routing header is presant
                        	**type**\:   :py:class:`AclPortOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperatorEnum>`
                        
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
                        	**type**\:   :py:class:`AclPortOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperatorEnum>`
                        
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
                        	**type**\:   :py:class:`AclPortOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperatorEnum>`
                        
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
                        	**type**\:   :py:class:`AclTcpflagsOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclTcpflagsOperatorEnum>`
                        
                        .. attribute:: is_time_to_live_end
                        
                        	IsTimeToLiveEnd
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_time_to_live_operator
                        
                        	IsTimeToLiveOperator
                        	**type**\:   :py:class:`AclPortOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperatorEnum>`
                        
                        .. attribute:: is_time_to_live_start
                        
                        	IsTimeToLiveStart
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: next_hop_info
                        
                        	Next hop info
                        	**type**\: list of    :py:class:`NextHopInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo>`
                        
                        .. attribute:: next_hop_type
                        
                        	Next hop type
                        	**type**\:   :py:class:`BagAclNhEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.BagAclNhEnum>`
                        
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
                            self.parent = None
                            self.sequence_number = None
                            self.acl_name = None
                            self.capture = None
                            self.counter_name = None
                            self.destination_mask = None
                            self.destination_port_group = None
                            self.destination_prefix_group = None
                            self.hits = None
                            self.hw_next_hop_info = Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo()
                            self.hw_next_hop_info.parent = self
                            self.is_ace_sequence_number = None
                            self.is_ace_type = None
                            self.is_comment_for_entry = None
                            self.is_destination_address_in_numbers = None
                            self.is_destination_address_prefix_length = None
                            self.is_destination_operator = None
                            self.is_destination_port1 = None
                            self.is_destination_port2 = None
                            self.is_dscp_present = None
                            self.is_dscp_valu = None
                            self.is_flow_id = None
                            self.is_header_matches = None
                            self.is_icmp_message_off = None
                            self.is_ipv6_protocol2_type = None
                            self.is_ipv6_protocol_type = None
                            self.is_log_option = None
                            self.is_packet_allow_or_deny = None
                            self.is_packet_length_end = None
                            self.is_packet_length_operator = None
                            self.is_packet_length_start = None
                            self.is_precedence_present = None
                            self.is_precedence_value = None
                            self.is_protocol_operator = None
                            self.is_source_address_in_numbers = None
                            self.is_source_address_prefix_length = None
                            self.is_source_operator = None
                            self.is_source_port1 = None
                            self.is_source_port2 = None
                            self.is_tcp_bits = None
                            self.is_tcp_bits_mask = None
                            self.is_tcp_bits_operator = None
                            self.is_time_to_live_end = None
                            self.is_time_to_live_operator = None
                            self.is_time_to_live_start = None
                            self.next_hop_info = YList()
                            self.next_hop_info.parent = self
                            self.next_hop_info.name = 'next_hop_info'
                            self.next_hop_type = None
                            self.no_stats = None
                            self.qos_group = None
                            self.sequence_str = None
                            self.source_mask = None
                            self.source_port_group = None
                            self.source_prefix_group = None
                            self.udf = YList()
                            self.udf.parent = self
                            self.udf.name = 'udf'
                            self.undetermined_transport = None


                        class HwNextHopInfo(object):
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
                            	**type**\:   :py:class:`BagAclNhEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.BagAclNhEnum>`
                            
                            .. attribute:: vrf_name
                            
                            	Vrf Name
                            	**type**\:  str
                            
                            	**length:** 0..32
                            
                            

                            """

                            _prefix = 'ipv6-acl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.next_hop = None
                                self.table_id = None
                                self.type = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-oper:hw-next-hop-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.next_hop is not None:
                                    return True

                                if self.table_id is not None:
                                    return True

                                if self.type is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                                return meta._meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo']['meta_info']


                        class NextHopInfo(object):
                            """
                            Next hop info
                            
                            .. attribute:: acl_nh_exist
                            
                            	The nexthop exist
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: at_status
                            
                            	The next hop at status
                            	**type**\:   :py:class:`BagAclNhAtStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.BagAclNhAtStatusEnum>`
                            
                            .. attribute:: next_hop
                            
                            	The next hop
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: status
                            
                            	The next hop status
                            	**type**\:   :py:class:`BagAclNhStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.BagAclNhStatusEnum>`
                            
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
                                self.parent = None
                                self.acl_nh_exist = None
                                self.at_status = None
                                self.next_hop = None
                                self.status = None
                                self.track_name = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-oper:next-hop-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.acl_nh_exist is not None:
                                    return True

                                if self.at_status is not None:
                                    return True

                                if self.next_hop is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.track_name is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                                return meta._meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo']['meta_info']


                        class Udf(object):
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
                                self.parent = None
                                self.udf_mask = None
                                self.udf_name = None
                                self.udf_value = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-oper:udf'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                                return meta._meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.sequence_number is None:
                                raise YPYModelError('Key property sequence_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-oper:access-list-sequence[Cisco-IOS-XR-ipv6-acl-oper:sequence-number = ' + str(self.sequence_number) + ']'

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

                            if self.destination_mask is not None:
                                return True

                            if self.destination_port_group is not None:
                                return True

                            if self.destination_prefix_group is not None:
                                return True

                            if self.hits is not None:
                                return True

                            if self.hw_next_hop_info is not None and self.hw_next_hop_info._has_data():
                                return True

                            if self.is_ace_sequence_number is not None:
                                return True

                            if self.is_ace_type is not None:
                                return True

                            if self.is_comment_for_entry is not None:
                                return True

                            if self.is_destination_address_in_numbers is not None:
                                return True

                            if self.is_destination_address_prefix_length is not None:
                                return True

                            if self.is_destination_operator is not None:
                                return True

                            if self.is_destination_port1 is not None:
                                return True

                            if self.is_destination_port2 is not None:
                                return True

                            if self.is_dscp_present is not None:
                                return True

                            if self.is_dscp_valu is not None:
                                return True

                            if self.is_flow_id is not None:
                                return True

                            if self.is_header_matches is not None:
                                return True

                            if self.is_icmp_message_off is not None:
                                return True

                            if self.is_ipv6_protocol2_type is not None:
                                return True

                            if self.is_ipv6_protocol_type is not None:
                                return True

                            if self.is_log_option is not None:
                                return True

                            if self.is_packet_allow_or_deny is not None:
                                return True

                            if self.is_packet_length_end is not None:
                                return True

                            if self.is_packet_length_operator is not None:
                                return True

                            if self.is_packet_length_start is not None:
                                return True

                            if self.is_precedence_present is not None:
                                return True

                            if self.is_precedence_value is not None:
                                return True

                            if self.is_protocol_operator is not None:
                                return True

                            if self.is_source_address_in_numbers is not None:
                                return True

                            if self.is_source_address_prefix_length is not None:
                                return True

                            if self.is_source_operator is not None:
                                return True

                            if self.is_source_port1 is not None:
                                return True

                            if self.is_source_port2 is not None:
                                return True

                            if self.is_tcp_bits is not None:
                                return True

                            if self.is_tcp_bits_mask is not None:
                                return True

                            if self.is_tcp_bits_operator is not None:
                                return True

                            if self.is_time_to_live_end is not None:
                                return True

                            if self.is_time_to_live_operator is not None:
                                return True

                            if self.is_time_to_live_start is not None:
                                return True

                            if self.next_hop_info is not None:
                                for child_ref in self.next_hop_info:
                                    if child_ref._has_data():
                                        return True

                            if self.next_hop_type is not None:
                                return True

                            if self.no_stats is not None:
                                return True

                            if self.qos_group is not None:
                                return True

                            if self.sequence_str is not None:
                                return True

                            if self.source_mask is not None:
                                return True

                            if self.source_port_group is not None:
                                return True

                            if self.source_prefix_group is not None:
                                return True

                            if self.udf is not None:
                                for child_ref in self.udf:
                                    if child_ref._has_data():
                                        return True

                            if self.undetermined_transport is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                            return meta._meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-oper:access-list-sequences'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                        return meta._meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences']['meta_info']

                @property
                def _common_path(self):
                    if self.access_list_name is None:
                        raise YPYModelError('Key property access_list_name is None')

                    return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-oper:access-list-manager/Cisco-IOS-XR-ipv6-acl-oper:accesses/Cisco-IOS-XR-ipv6-acl-oper:access[Cisco-IOS-XR-ipv6-acl-oper:access-list-name = ' + str(self.access_list_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.access_list_name is not None:
                        return True

                    if self.access_list_sequences is not None and self.access_list_sequences._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                    return meta._meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses.Access']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-oper:access-list-manager/Cisco-IOS-XR-ipv6-acl-oper:accesses'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                return meta._meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-oper:access-list-manager'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
            return meta._meta_table['Ipv6AclAndPrefixList.AccessListManager']['meta_info']


    class Oor(object):
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
            self.parent = None
            self.access_list_summary = Ipv6AclAndPrefixList.Oor.AccessListSummary()
            self.access_list_summary.parent = self
            self.details = Ipv6AclAndPrefixList.Oor.Details()
            self.details.parent = self
            self.oor_accesses = Ipv6AclAndPrefixList.Oor.OorAccesses()
            self.oor_accesses.parent = self
            self.oor_prefixes = Ipv6AclAndPrefixList.Oor.OorPrefixes()
            self.oor_prefixes.parent = self
            self.prefix_list_summary = Ipv6AclAndPrefixList.Oor.PrefixListSummary()
            self.prefix_list_summary.parent = self


        class Details(object):
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
                self.parent = None
                self.is_current_configured_ac_ls = None
                self.is_current_configured_aces = None
                self.is_current_maximum_configurable_aces = None
                self.is_current_maximum_configurable_acls = None
                self.is_default_maximum_configurable_ac_es = None
                self.is_default_maximum_configurable_ac_ls = None
                self.is_maximum_configurable_ac_es = None
                self.is_maximum_configurable_ac_ls = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-oper:oor/Cisco-IOS-XR-ipv6-acl-oper:details'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.is_current_configured_ac_ls is not None:
                    return True

                if self.is_current_configured_aces is not None:
                    return True

                if self.is_current_maximum_configurable_aces is not None:
                    return True

                if self.is_current_maximum_configurable_acls is not None:
                    return True

                if self.is_default_maximum_configurable_ac_es is not None:
                    return True

                if self.is_default_maximum_configurable_ac_ls is not None:
                    return True

                if self.is_maximum_configurable_ac_es is not None:
                    return True

                if self.is_maximum_configurable_ac_ls is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                return meta._meta_table['Ipv6AclAndPrefixList.Oor.Details']['meta_info']


        class PrefixListSummary(object):
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
                self.parent = None
                self.details = Ipv6AclAndPrefixList.Oor.PrefixListSummary.Details()
                self.details.parent = self


            class Details(object):
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
                    self.parent = None
                    self.is_current_configured_ac_ls = None
                    self.is_current_configured_aces = None
                    self.is_current_maximum_configurable_aces = None
                    self.is_current_maximum_configurable_acls = None
                    self.is_default_maximum_configurable_ac_es = None
                    self.is_default_maximum_configurable_ac_ls = None
                    self.is_maximum_configurable_ac_es = None
                    self.is_maximum_configurable_ac_ls = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-oper:oor/Cisco-IOS-XR-ipv6-acl-oper:prefix-list-summary/Cisco-IOS-XR-ipv6-acl-oper:details'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.is_current_configured_ac_ls is not None:
                        return True

                    if self.is_current_configured_aces is not None:
                        return True

                    if self.is_current_maximum_configurable_aces is not None:
                        return True

                    if self.is_current_maximum_configurable_acls is not None:
                        return True

                    if self.is_default_maximum_configurable_ac_es is not None:
                        return True

                    if self.is_default_maximum_configurable_ac_ls is not None:
                        return True

                    if self.is_maximum_configurable_ac_es is not None:
                        return True

                    if self.is_maximum_configurable_ac_ls is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                    return meta._meta_table['Ipv6AclAndPrefixList.Oor.PrefixListSummary.Details']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-oper:oor/Cisco-IOS-XR-ipv6-acl-oper:prefix-list-summary'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.details is not None and self.details._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                return meta._meta_table['Ipv6AclAndPrefixList.Oor.PrefixListSummary']['meta_info']


        class OorAccesses(object):
            """
            Resource occupation details for ACLs
            
            .. attribute:: oor_access
            
            	Resource occupation details for a particular ACL
            	**type**\: list of    :py:class:`OorAccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.OorAccesses.OorAccess>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.oor_access = YList()
                self.oor_access.parent = self
                self.oor_access.name = 'oor_access'


            class OorAccess(object):
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
                    self.parent = None
                    self.access_list_name = None
                    self.is_current_configured_ac_ls = None
                    self.is_current_configured_aces = None
                    self.is_current_maximum_configurable_aces = None
                    self.is_current_maximum_configurable_acls = None
                    self.is_default_maximum_configurable_ac_es = None
                    self.is_default_maximum_configurable_ac_ls = None
                    self.is_maximum_configurable_ac_es = None
                    self.is_maximum_configurable_ac_ls = None

                @property
                def _common_path(self):
                    if self.access_list_name is None:
                        raise YPYModelError('Key property access_list_name is None')

                    return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-oper:oor/Cisco-IOS-XR-ipv6-acl-oper:oor-accesses/Cisco-IOS-XR-ipv6-acl-oper:oor-access[Cisco-IOS-XR-ipv6-acl-oper:access-list-name = ' + str(self.access_list_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.access_list_name is not None:
                        return True

                    if self.is_current_configured_ac_ls is not None:
                        return True

                    if self.is_current_configured_aces is not None:
                        return True

                    if self.is_current_maximum_configurable_aces is not None:
                        return True

                    if self.is_current_maximum_configurable_acls is not None:
                        return True

                    if self.is_default_maximum_configurable_ac_es is not None:
                        return True

                    if self.is_default_maximum_configurable_ac_ls is not None:
                        return True

                    if self.is_maximum_configurable_ac_es is not None:
                        return True

                    if self.is_maximum_configurable_ac_ls is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                    return meta._meta_table['Ipv6AclAndPrefixList.Oor.OorAccesses.OorAccess']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-oper:oor/Cisco-IOS-XR-ipv6-acl-oper:oor-accesses'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                return meta._meta_table['Ipv6AclAndPrefixList.Oor.OorAccesses']['meta_info']


        class OorPrefixes(object):
            """
            Resource occupation details for prefix lists
            
            .. attribute:: oor_prefix
            
            	Resource occupation details for a particular prefix list
            	**type**\: list of    :py:class:`OorPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.OorPrefixes.OorPrefix>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
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
                    self.parent = None
                    self.prefix_list_name = None
                    self.is_current_configured_ac_ls = None
                    self.is_current_configured_aces = None
                    self.is_current_maximum_configurable_aces = None
                    self.is_current_maximum_configurable_acls = None
                    self.is_default_maximum_configurable_ac_es = None
                    self.is_default_maximum_configurable_ac_ls = None
                    self.is_maximum_configurable_ac_es = None
                    self.is_maximum_configurable_ac_ls = None

                @property
                def _common_path(self):
                    if self.prefix_list_name is None:
                        raise YPYModelError('Key property prefix_list_name is None')

                    return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-oper:oor/Cisco-IOS-XR-ipv6-acl-oper:oor-prefixes/Cisco-IOS-XR-ipv6-acl-oper:oor-prefix[Cisco-IOS-XR-ipv6-acl-oper:prefix-list-name = ' + str(self.prefix_list_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.prefix_list_name is not None:
                        return True

                    if self.is_current_configured_ac_ls is not None:
                        return True

                    if self.is_current_configured_aces is not None:
                        return True

                    if self.is_current_maximum_configurable_aces is not None:
                        return True

                    if self.is_current_maximum_configurable_acls is not None:
                        return True

                    if self.is_default_maximum_configurable_ac_es is not None:
                        return True

                    if self.is_default_maximum_configurable_ac_ls is not None:
                        return True

                    if self.is_maximum_configurable_ac_es is not None:
                        return True

                    if self.is_maximum_configurable_ac_ls is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                    return meta._meta_table['Ipv6AclAndPrefixList.Oor.OorPrefixes.OorPrefix']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-oper:oor/Cisco-IOS-XR-ipv6-acl-oper:oor-prefixes'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                return meta._meta_table['Ipv6AclAndPrefixList.Oor.OorPrefixes']['meta_info']


        class AccessListSummary(object):
            """
            Resource Limits pertaining to ACLs only
            
            .. attribute:: details
            
            	Details containing the resource limits of the ACLs
            	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.AccessListSummary.Details>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.details = Ipv6AclAndPrefixList.Oor.AccessListSummary.Details()
                self.details.parent = self


            class Details(object):
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
                    self.parent = None
                    self.is_current_configured_ac_ls = None
                    self.is_current_configured_aces = None
                    self.is_current_maximum_configurable_aces = None
                    self.is_current_maximum_configurable_acls = None
                    self.is_default_maximum_configurable_ac_es = None
                    self.is_default_maximum_configurable_ac_ls = None
                    self.is_maximum_configurable_ac_es = None
                    self.is_maximum_configurable_ac_ls = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-oper:oor/Cisco-IOS-XR-ipv6-acl-oper:access-list-summary/Cisco-IOS-XR-ipv6-acl-oper:details'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.is_current_configured_ac_ls is not None:
                        return True

                    if self.is_current_configured_aces is not None:
                        return True

                    if self.is_current_maximum_configurable_aces is not None:
                        return True

                    if self.is_current_maximum_configurable_acls is not None:
                        return True

                    if self.is_default_maximum_configurable_ac_es is not None:
                        return True

                    if self.is_default_maximum_configurable_ac_ls is not None:
                        return True

                    if self.is_maximum_configurable_ac_es is not None:
                        return True

                    if self.is_maximum_configurable_ac_ls is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                    return meta._meta_table['Ipv6AclAndPrefixList.Oor.AccessListSummary.Details']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-oper:oor/Cisco-IOS-XR-ipv6-acl-oper:access-list-summary'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.details is not None and self.details._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
                return meta._meta_table['Ipv6AclAndPrefixList.Oor.AccessListSummary']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-oper:oor'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
            return meta._meta_table['Ipv6AclAndPrefixList.Oor']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list'

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_oper as meta
        return meta._meta_table['Ipv6AclAndPrefixList']['meta_info']


