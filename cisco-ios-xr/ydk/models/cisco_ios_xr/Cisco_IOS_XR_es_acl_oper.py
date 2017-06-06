""" Cisco_IOS_XR_es_acl_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR es\-acl package operational data.

This module contains definitions
for the following management objects\:
  es\-acl\: Root class of ES ACL Oper schema tree

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_oper as meta
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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_oper as meta
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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_oper as meta
        return meta._meta_table['AclActionEnum']



class EsAcl(object):
    """
    Root class of ES ACL Oper schema tree
    
    .. attribute:: active
    
    	Out Of Resources, Limits to the resources allocatable
    	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active>`
    
    

    """

    _prefix = 'es-acl-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.active = EsAcl.Active()
        self.active.parent = self


    class Active(object):
        """
        Out Of Resources, Limits to the resources
        allocatable
        
        .. attribute:: list
        
        	List containing ACLs
        	**type**\:   :py:class:`List <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.List>`
        
        .. attribute:: oor
        
        	Out Of Resources, Limits to the resources allocatable
        	**type**\:   :py:class:`Oor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.Oor>`
        
        .. attribute:: oor_acls
        
        	Resource occupation details for ACLs
        	**type**\:   :py:class:`OorAcls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.OorAcls>`
        
        .. attribute:: usages
        
        	Table of Usage statistics of ACLs at different nodes
        	**type**\:   :py:class:`Usages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.Usages>`
        
        

        """

        _prefix = 'es-acl-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.list = EsAcl.Active.List()
            self.list.parent = self
            self.oor = EsAcl.Active.Oor()
            self.oor.parent = self
            self.oor_acls = EsAcl.Active.OorAcls()
            self.oor_acls.parent = self
            self.usages = EsAcl.Active.Usages()
            self.usages.parent = self


        class Oor(object):
            """
            Out Of Resources, Limits to the resources
            allocatable
            
            .. attribute:: acl_summary
            
            	Resource Limits pertaining to ACLs only
            	**type**\:   :py:class:`AclSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.Oor.AclSummary>`
            
            

            """

            _prefix = 'es-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.acl_summary = EsAcl.Active.Oor.AclSummary()
                self.acl_summary.parent = self


            class AclSummary(object):
                """
                Resource Limits pertaining to ACLs only
                
                .. attribute:: details
                
                	Details containing the resource limits of the ACLs
                	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.Oor.AclSummary.Details>`
                
                

                """

                _prefix = 'es-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.details = EsAcl.Active.Oor.AclSummary.Details()
                    self.details.parent = self


                class Details(object):
                    """
                    Details containing the resource limits of the
                    ACLs
                    
                    .. attribute:: current_configured_ac_es
                    
                    	Current configured aces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: current_configured_ac_ls
                    
                    	Current configured acls
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: maximum_configurable_ac_es
                    
                    	max configurable aces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: maximum_configurable_ac_ls
                    
                    	max configurable acls
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'es-acl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.current_configured_ac_es = None
                        self.current_configured_ac_ls = None
                        self.maximum_configurable_ac_es = None
                        self.maximum_configurable_ac_ls = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-es-acl-oper:es-acl/Cisco-IOS-XR-es-acl-oper:active/Cisco-IOS-XR-es-acl-oper:oor/Cisco-IOS-XR-es-acl-oper:acl-summary/Cisco-IOS-XR-es-acl-oper:details'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.current_configured_ac_es is not None:
                            return True

                        if self.current_configured_ac_ls is not None:
                            return True

                        if self.maximum_configurable_ac_es is not None:
                            return True

                        if self.maximum_configurable_ac_ls is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_oper as meta
                        return meta._meta_table['EsAcl.Active.Oor.AclSummary.Details']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-es-acl-oper:es-acl/Cisco-IOS-XR-es-acl-oper:active/Cisco-IOS-XR-es-acl-oper:oor/Cisco-IOS-XR-es-acl-oper:acl-summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.details is not None and self.details._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_oper as meta
                    return meta._meta_table['EsAcl.Active.Oor.AclSummary']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-es-acl-oper:es-acl/Cisco-IOS-XR-es-acl-oper:active/Cisco-IOS-XR-es-acl-oper:oor'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.acl_summary is not None and self.acl_summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_oper as meta
                return meta._meta_table['EsAcl.Active.Oor']['meta_info']


        class List(object):
            """
            List containing ACLs
            
            .. attribute:: acls
            
            	ACL class displaying Usage and Entries
            	**type**\:   :py:class:`Acls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.List.Acls>`
            
            

            """

            _prefix = 'es-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.acls = EsAcl.Active.List.Acls()
                self.acls.parent = self


            class Acls(object):
                """
                ACL class displaying Usage and Entries
                
                .. attribute:: acl
                
                	Name of the Access List
                	**type**\: list of    :py:class:`Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.List.Acls.Acl>`
                
                

                """

                _prefix = 'es-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.acl = YList()
                    self.acl.parent = self
                    self.acl.name = 'acl'


                class Acl(object):
                    """
                    Name of the Access List
                    
                    .. attribute:: name  <key>
                    
                    	Name of the Access List
                    	**type**\:  str
                    
                    	**length:** 1..65
                    
                    .. attribute:: acl_sequence_numbers
                    
                    	Table of all the SequenceNumbers per ACL
                    	**type**\:   :py:class:`AclSequenceNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.List.Acls.Acl.AclSequenceNumbers>`
                    
                    

                    """

                    _prefix = 'es-acl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.name = None
                        self.acl_sequence_numbers = EsAcl.Active.List.Acls.Acl.AclSequenceNumbers()
                        self.acl_sequence_numbers.parent = self


                    class AclSequenceNumbers(object):
                        """
                        Table of all the SequenceNumbers per ACL
                        
                        .. attribute:: acl_sequence_number
                        
                        	Sequence Number of an ACL entry
                        	**type**\: list of    :py:class:`AclSequenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.List.Acls.Acl.AclSequenceNumbers.AclSequenceNumber>`
                        
                        

                        """

                        _prefix = 'es-acl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.acl_sequence_number = YList()
                            self.acl_sequence_number.parent = self
                            self.acl_sequence_number.name = 'acl_sequence_number'


                        class AclSequenceNumber(object):
                            """
                            Sequence Number of an ACL entry
                            
                            .. attribute:: sequence_number  <key>
                            
                            	ACLEntry Sequence Number
                            	**type**\:  int
                            
                            	**range:** 1..2147483646
                            
                            .. attribute:: ace_sequence_number
                            
                            	ACE sequence number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ace_type
                            
                            	ACE type (acl, remark)
                            	**type**\:   :py:class:`AclAce1Enum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.AclAce1Enum>`
                            
                            .. attribute:: acl_name
                            
                            	Acl Name
                            	**type**\:  str
                            
                            .. attribute:: capture
                            
                            	Capture option, TRUE if enabled
                            	**type**\:  bool
                            
                            .. attribute:: cos
                            
                            	COS value
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: dei
                            
                            	DEI bit
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: destination_address
                            
                            	Destination MAC address
                            	**type**\:  str
                            
                            	**pattern:** [a\-fA\-F0\-9]{4}(\\.[a\-fA\-F0\-9]{4}){2}
                            
                            .. attribute:: destination_wild_card_bits
                            
                            	Destination wild card bits
                            	**type**\:  str
                            
                            	**pattern:** [a\-fA\-F0\-9]{4}(\\.[a\-fA\-F0\-9]{4}){2}
                            
                            .. attribute:: ether_type_number
                            
                            	Ethernet type Number
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: grant
                            
                            	Grant value permit/deny 
                            	**type**\:   :py:class:`AclActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.AclActionEnum>`
                            
                            .. attribute:: hits
                            
                            	ACE hit number
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: inner_header_cos
                            
                            	Inner header COS value
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: inner_header_dei
                            
                            	Inner header DEI bit
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: inner_header_vlan1
                            
                            	Inner header VLAN ID/range lower limit
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: inner_header_vlan2
                            
                            	Inner header VLAN ID range higher limit
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: log_option
                            
                            	Log option
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: remark
                            
                            	Remark string
                            	**type**\:  str
                            
                            .. attribute:: sequence_string
                            
                            	Sequence Sring
                            	**type**\:  str
                            
                            .. attribute:: source_address
                            
                            	Source MAC address
                            	**type**\:  str
                            
                            	**pattern:** [a\-fA\-F0\-9]{4}(\\.[a\-fA\-F0\-9]{4}){2}
                            
                            .. attribute:: source_wild_card_bits
                            
                            	Source wild card bits
                            	**type**\:  str
                            
                            	**pattern:** [a\-fA\-F0\-9]{4}(\\.[a\-fA\-F0\-9]{4}){2}
                            
                            .. attribute:: vlan1
                            
                            	VLAN ID/range lower limit
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: vlan2
                            
                            	VLAN ID range higher limit
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'es-acl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.sequence_number = None
                                self.ace_sequence_number = None
                                self.ace_type = None
                                self.acl_name = None
                                self.capture = None
                                self.cos = None
                                self.dei = None
                                self.destination_address = None
                                self.destination_wild_card_bits = None
                                self.ether_type_number = None
                                self.grant = None
                                self.hits = None
                                self.inner_header_cos = None
                                self.inner_header_dei = None
                                self.inner_header_vlan1 = None
                                self.inner_header_vlan2 = None
                                self.log_option = None
                                self.remark = None
                                self.sequence_string = None
                                self.source_address = None
                                self.source_wild_card_bits = None
                                self.vlan1 = None
                                self.vlan2 = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.sequence_number is None:
                                    raise YPYModelError('Key property sequence_number is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-es-acl-oper:acl-sequence-number[Cisco-IOS-XR-es-acl-oper:sequence-number = ' + str(self.sequence_number) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sequence_number is not None:
                                    return True

                                if self.ace_sequence_number is not None:
                                    return True

                                if self.ace_type is not None:
                                    return True

                                if self.acl_name is not None:
                                    return True

                                if self.capture is not None:
                                    return True

                                if self.cos is not None:
                                    return True

                                if self.dei is not None:
                                    return True

                                if self.destination_address is not None:
                                    return True

                                if self.destination_wild_card_bits is not None:
                                    return True

                                if self.ether_type_number is not None:
                                    return True

                                if self.grant is not None:
                                    return True

                                if self.hits is not None:
                                    return True

                                if self.inner_header_cos is not None:
                                    return True

                                if self.inner_header_dei is not None:
                                    return True

                                if self.inner_header_vlan1 is not None:
                                    return True

                                if self.inner_header_vlan2 is not None:
                                    return True

                                if self.log_option is not None:
                                    return True

                                if self.remark is not None:
                                    return True

                                if self.sequence_string is not None:
                                    return True

                                if self.source_address is not None:
                                    return True

                                if self.source_wild_card_bits is not None:
                                    return True

                                if self.vlan1 is not None:
                                    return True

                                if self.vlan2 is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_oper as meta
                                return meta._meta_table['EsAcl.Active.List.Acls.Acl.AclSequenceNumbers.AclSequenceNumber']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-es-acl-oper:acl-sequence-numbers'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.acl_sequence_number is not None:
                                for child_ref in self.acl_sequence_number:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_oper as meta
                            return meta._meta_table['EsAcl.Active.List.Acls.Acl.AclSequenceNumbers']['meta_info']

                    @property
                    def _common_path(self):
                        if self.name is None:
                            raise YPYModelError('Key property name is None')

                        return '/Cisco-IOS-XR-es-acl-oper:es-acl/Cisco-IOS-XR-es-acl-oper:active/Cisco-IOS-XR-es-acl-oper:list/Cisco-IOS-XR-es-acl-oper:acls/Cisco-IOS-XR-es-acl-oper:acl[Cisco-IOS-XR-es-acl-oper:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        if self.acl_sequence_numbers is not None and self.acl_sequence_numbers._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_oper as meta
                        return meta._meta_table['EsAcl.Active.List.Acls.Acl']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-es-acl-oper:es-acl/Cisco-IOS-XR-es-acl-oper:active/Cisco-IOS-XR-es-acl-oper:list/Cisco-IOS-XR-es-acl-oper:acls'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.acl is not None:
                        for child_ref in self.acl:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_oper as meta
                    return meta._meta_table['EsAcl.Active.List.Acls']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-es-acl-oper:es-acl/Cisco-IOS-XR-es-acl-oper:active/Cisco-IOS-XR-es-acl-oper:list'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.acls is not None and self.acls._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_oper as meta
                return meta._meta_table['EsAcl.Active.List']['meta_info']


        class OorAcls(object):
            """
            Resource occupation details for ACLs
            
            .. attribute:: oor_acl
            
            	Resource occupation details for a particular ACL
            	**type**\: list of    :py:class:`OorAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.OorAcls.OorAcl>`
            
            

            """

            _prefix = 'es-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.oor_acl = YList()
                self.oor_acl.parent = self
                self.oor_acl.name = 'oor_acl'


            class OorAcl(object):
                """
                Resource occupation details for a particular
                ACL
                
                .. attribute:: name  <key>
                
                	Name of the Access List
                	**type**\:  str
                
                	**length:** 1..65
                
                .. attribute:: current_configured_ac_es
                
                	Current configured aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_configured_ac_ls
                
                	Current configured acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_configurable_ac_es
                
                	max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_configurable_ac_ls
                
                	max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'es-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.current_configured_ac_es = None
                    self.current_configured_ac_ls = None
                    self.maximum_configurable_ac_es = None
                    self.maximum_configurable_ac_ls = None

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XR-es-acl-oper:es-acl/Cisco-IOS-XR-es-acl-oper:active/Cisco-IOS-XR-es-acl-oper:oor-acls/Cisco-IOS-XR-es-acl-oper:oor-acl[Cisco-IOS-XR-es-acl-oper:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.current_configured_ac_es is not None:
                        return True

                    if self.current_configured_ac_ls is not None:
                        return True

                    if self.maximum_configurable_ac_es is not None:
                        return True

                    if self.maximum_configurable_ac_ls is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_oper as meta
                    return meta._meta_table['EsAcl.Active.OorAcls.OorAcl']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-es-acl-oper:es-acl/Cisco-IOS-XR-es-acl-oper:active/Cisco-IOS-XR-es-acl-oper:oor-acls'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.oor_acl is not None:
                    for child_ref in self.oor_acl:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_oper as meta
                return meta._meta_table['EsAcl.Active.OorAcls']['meta_info']


        class Usages(object):
            """
            Table of Usage statistics of ACLs at different
            nodes
            
            .. attribute:: usage
            
            	Usage statistics of an ACL at a node
            	**type**\: list of    :py:class:`Usage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.Usages.Usage>`
            
            

            """

            _prefix = 'es-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.usage = YList()
                self.usage.parent = self
                self.usage.name = 'usage'


            class Usage(object):
                """
                Usage statistics of an ACL at a node
                
                .. attribute:: application_id
                
                	Application ID
                	**type**\:   :py:class:`AclUsageAppIdEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_common_acl_datatypes.AclUsageAppIdEnumEnum>`
                
                .. attribute:: location
                
                	Node where ACL is applied
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: name
                
                	Name of the ACL
                	**type**\:  str
                
                	**length:** 1..65
                
                .. attribute:: usage_details
                
                	Usage Statistics Details
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'es-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.application_id = None
                    self.location = None
                    self.name = None
                    self.usage_details = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-es-acl-oper:es-acl/Cisco-IOS-XR-es-acl-oper:active/Cisco-IOS-XR-es-acl-oper:usages/Cisco-IOS-XR-es-acl-oper:usage'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.application_id is not None:
                        return True

                    if self.location is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.usage_details is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_oper as meta
                    return meta._meta_table['EsAcl.Active.Usages.Usage']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-es-acl-oper:es-acl/Cisco-IOS-XR-es-acl-oper:active/Cisco-IOS-XR-es-acl-oper:usages'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_oper as meta
                return meta._meta_table['EsAcl.Active.Usages']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-es-acl-oper:es-acl/Cisco-IOS-XR-es-acl-oper:active'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.list is not None and self.list._has_data():
                return True

            if self.oor is not None and self.oor._has_data():
                return True

            if self.oor_acls is not None and self.oor_acls._has_data():
                return True

            if self.usages is not None and self.usages._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_oper as meta
            return meta._meta_table['EsAcl.Active']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-es-acl-oper:es-acl'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.active is not None and self.active._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_oper as meta
        return meta._meta_table['EsAcl']['meta_info']


