""" Cisco_IOS_XR_es_acl_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR es\-acl package operational data.

This module contains definitions
for the following management objects\:
  es\-acl\: Root class of ES ACL Oper schema tree

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



class EsAcl(Entity):
    """
    Root class of ES ACL Oper schema tree
    
    .. attribute:: active
    
    	Out Of Resources, Limits to the resources allocatable
    	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active>`
    
    

    """

    _prefix = 'es-acl-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(EsAcl, self).__init__()
        self._top_entity = None

        self.yang_name = "es-acl"
        self.yang_parent_name = "Cisco-IOS-XR-es-acl-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("active", ("active", EsAcl.Active))])
        self._leafs = OrderedDict()

        self.active = EsAcl.Active()
        self.active.parent = self
        self._children_name_map["active"] = "active"
        self._segment_path = lambda: "Cisco-IOS-XR-es-acl-oper:es-acl"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(EsAcl, [], name, value)


    class Active(Entity):
        """
        Out Of Resources, Limits to the resources
        allocatable
        
        .. attribute:: oor
        
        	Out Of Resources, Limits to the resources allocatable
        	**type**\:  :py:class:`Oor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.Oor>`
        
        .. attribute:: list
        
        	List containing ACLs
        	**type**\:  :py:class:`List <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.List>`
        
        .. attribute:: oor_acls
        
        	Resource occupation details for ACLs
        	**type**\:  :py:class:`OorAcls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.OorAcls>`
        
        .. attribute:: usages
        
        	Table of Usage statistics of ACLs at different nodes
        	**type**\:  :py:class:`Usages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.Usages>`
        
        

        """

        _prefix = 'es-acl-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(EsAcl.Active, self).__init__()

            self.yang_name = "active"
            self.yang_parent_name = "es-acl"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("oor", ("oor", EsAcl.Active.Oor)), ("list", ("list", EsAcl.Active.List)), ("oor-acls", ("oor_acls", EsAcl.Active.OorAcls)), ("usages", ("usages", EsAcl.Active.Usages))])
            self._leafs = OrderedDict()

            self.oor = EsAcl.Active.Oor()
            self.oor.parent = self
            self._children_name_map["oor"] = "oor"

            self.list = EsAcl.Active.List()
            self.list.parent = self
            self._children_name_map["list"] = "list"

            self.oor_acls = EsAcl.Active.OorAcls()
            self.oor_acls.parent = self
            self._children_name_map["oor_acls"] = "oor-acls"

            self.usages = EsAcl.Active.Usages()
            self.usages.parent = self
            self._children_name_map["usages"] = "usages"
            self._segment_path = lambda: "active"
            self._absolute_path = lambda: "Cisco-IOS-XR-es-acl-oper:es-acl/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EsAcl.Active, [], name, value)


        class Oor(Entity):
            """
            Out Of Resources, Limits to the resources
            allocatable
            
            .. attribute:: acl_summary
            
            	Resource Limits pertaining to ACLs only
            	**type**\:  :py:class:`AclSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.Oor.AclSummary>`
            
            

            """

            _prefix = 'es-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(EsAcl.Active.Oor, self).__init__()

                self.yang_name = "oor"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("acl-summary", ("acl_summary", EsAcl.Active.Oor.AclSummary))])
                self._leafs = OrderedDict()

                self.acl_summary = EsAcl.Active.Oor.AclSummary()
                self.acl_summary.parent = self
                self._children_name_map["acl_summary"] = "acl-summary"
                self._segment_path = lambda: "oor"
                self._absolute_path = lambda: "Cisco-IOS-XR-es-acl-oper:es-acl/active/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EsAcl.Active.Oor, [], name, value)


            class AclSummary(Entity):
                """
                Resource Limits pertaining to ACLs only
                
                .. attribute:: details
                
                	Details containing the resource limits of the ACLs
                	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.Oor.AclSummary.Details>`
                
                

                """

                _prefix = 'es-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(EsAcl.Active.Oor.AclSummary, self).__init__()

                    self.yang_name = "acl-summary"
                    self.yang_parent_name = "oor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("details", ("details", EsAcl.Active.Oor.AclSummary.Details))])
                    self._leafs = OrderedDict()

                    self.details = EsAcl.Active.Oor.AclSummary.Details()
                    self.details.parent = self
                    self._children_name_map["details"] = "details"
                    self._segment_path = lambda: "acl-summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-es-acl-oper:es-acl/active/oor/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(EsAcl.Active.Oor.AclSummary, [], name, value)


                class Details(Entity):
                    """
                    Details containing the resource limits of the
                    ACLs
                    
                    .. attribute:: current_configured_ac_ls
                    
                    	Current configured acls
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: current_configured_ac_es
                    
                    	Current configured aces
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: maximum_configurable_ac_ls
                    
                    	max configurable acls
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: maximum_configurable_ac_es
                    
                    	max configurable aces
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'es-acl-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(EsAcl.Active.Oor.AclSummary.Details, self).__init__()

                        self.yang_name = "details"
                        self.yang_parent_name = "acl-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('current_configured_ac_ls', (YLeaf(YType.uint32, 'current-configured-ac-ls'), ['int'])),
                            ('current_configured_ac_es', (YLeaf(YType.uint32, 'current-configured-ac-es'), ['int'])),
                            ('maximum_configurable_ac_ls', (YLeaf(YType.uint32, 'maximum-configurable-ac-ls'), ['int'])),
                            ('maximum_configurable_ac_es', (YLeaf(YType.uint32, 'maximum-configurable-ac-es'), ['int'])),
                        ])
                        self.current_configured_ac_ls = None
                        self.current_configured_ac_es = None
                        self.maximum_configurable_ac_ls = None
                        self.maximum_configurable_ac_es = None
                        self._segment_path = lambda: "details"
                        self._absolute_path = lambda: "Cisco-IOS-XR-es-acl-oper:es-acl/active/oor/acl-summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EsAcl.Active.Oor.AclSummary.Details, ['current_configured_ac_ls', 'current_configured_ac_es', 'maximum_configurable_ac_ls', 'maximum_configurable_ac_es'], name, value)


        class List(Entity):
            """
            List containing ACLs
            
            .. attribute:: acls
            
            	ACL class displaying Usage and Entries
            	**type**\:  :py:class:`Acls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.List.Acls>`
            
            

            """

            _prefix = 'es-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(EsAcl.Active.List, self).__init__()

                self.yang_name = "list"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("acls", ("acls", EsAcl.Active.List.Acls))])
                self._leafs = OrderedDict()

                self.acls = EsAcl.Active.List.Acls()
                self.acls.parent = self
                self._children_name_map["acls"] = "acls"
                self._segment_path = lambda: "list"
                self._absolute_path = lambda: "Cisco-IOS-XR-es-acl-oper:es-acl/active/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EsAcl.Active.List, [], name, value)


            class Acls(Entity):
                """
                ACL class displaying Usage and Entries
                
                .. attribute:: acl
                
                	Name of the Access List
                	**type**\: list of  		 :py:class:`Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.List.Acls.Acl>`
                
                

                """

                _prefix = 'es-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(EsAcl.Active.List.Acls, self).__init__()

                    self.yang_name = "acls"
                    self.yang_parent_name = "list"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("acl", ("acl", EsAcl.Active.List.Acls.Acl))])
                    self._leafs = OrderedDict()

                    self.acl = YList(self)
                    self._segment_path = lambda: "acls"
                    self._absolute_path = lambda: "Cisco-IOS-XR-es-acl-oper:es-acl/active/list/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(EsAcl.Active.List.Acls, [], name, value)


                class Acl(Entity):
                    """
                    Name of the Access List
                    
                    .. attribute:: name  (key)
                    
                    	Name of the Access List
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: acl_sequence_numbers
                    
                    	Table of all the SequenceNumbers per ACL
                    	**type**\:  :py:class:`AclSequenceNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.List.Acls.Acl.AclSequenceNumbers>`
                    
                    

                    """

                    _prefix = 'es-acl-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(EsAcl.Active.List.Acls.Acl, self).__init__()

                        self.yang_name = "acl"
                        self.yang_parent_name = "acls"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([("acl-sequence-numbers", ("acl_sequence_numbers", EsAcl.Active.List.Acls.Acl.AclSequenceNumbers))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None

                        self.acl_sequence_numbers = EsAcl.Active.List.Acls.Acl.AclSequenceNumbers()
                        self.acl_sequence_numbers.parent = self
                        self._children_name_map["acl_sequence_numbers"] = "acl-sequence-numbers"
                        self._segment_path = lambda: "acl" + "[name='" + str(self.name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-es-acl-oper:es-acl/active/list/acls/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EsAcl.Active.List.Acls.Acl, ['name'], name, value)


                    class AclSequenceNumbers(Entity):
                        """
                        Table of all the SequenceNumbers per ACL
                        
                        .. attribute:: acl_sequence_number
                        
                        	Sequence Number of an ACL entry
                        	**type**\: list of  		 :py:class:`AclSequenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.List.Acls.Acl.AclSequenceNumbers.AclSequenceNumber>`
                        
                        

                        """

                        _prefix = 'es-acl-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(EsAcl.Active.List.Acls.Acl.AclSequenceNumbers, self).__init__()

                            self.yang_name = "acl-sequence-numbers"
                            self.yang_parent_name = "acl"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("acl-sequence-number", ("acl_sequence_number", EsAcl.Active.List.Acls.Acl.AclSequenceNumbers.AclSequenceNumber))])
                            self._leafs = OrderedDict()

                            self.acl_sequence_number = YList(self)
                            self._segment_path = lambda: "acl-sequence-numbers"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EsAcl.Active.List.Acls.Acl.AclSequenceNumbers, [], name, value)


                        class AclSequenceNumber(Entity):
                            """
                            Sequence Number of an ACL entry
                            
                            .. attribute:: sequence_number  (key)
                            
                            	ACLEntry Sequence Number
                            	**type**\: int
                            
                            	**range:** 1..2147483646
                            
                            .. attribute:: ace_type
                            
                            	ACE type (acl, remark)
                            	**type**\:  :py:class:`AclAce1_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.AclAce1_>`
                            
                            .. attribute:: ace_sequence_number
                            
                            	ACE sequence number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hits
                            
                            	ACE hit number
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: grant
                            
                            	Grant value permit/deny 
                            	**type**\:  :py:class:`AclAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.AclAction>`
                            
                            .. attribute:: source_address
                            
                            	Source MAC address
                            	**type**\: str
                            
                            	**pattern:** [a\-fA\-F0\-9]{4}(\\.[a\-fA\-F0\-9]{4}){2}
                            
                            .. attribute:: source_wild_card_bits
                            
                            	Source wild card bits
                            	**type**\: str
                            
                            	**pattern:** [a\-fA\-F0\-9]{4}(\\.[a\-fA\-F0\-9]{4}){2}
                            
                            .. attribute:: destination_address
                            
                            	Destination MAC address
                            	**type**\: str
                            
                            	**pattern:** [a\-fA\-F0\-9]{4}(\\.[a\-fA\-F0\-9]{4}){2}
                            
                            .. attribute:: destination_wild_card_bits
                            
                            	Destination wild card bits
                            	**type**\: str
                            
                            	**pattern:** [a\-fA\-F0\-9]{4}(\\.[a\-fA\-F0\-9]{4}){2}
                            
                            .. attribute:: ether_type_number
                            
                            	Ethernet type Number
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: vlan1
                            
                            	VLAN ID/range lower limit
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: vlan2
                            
                            	VLAN ID range higher limit
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: cos
                            
                            	COS value
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: dei
                            
                            	DEI bit
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: inner_header_vlan1
                            
                            	Inner header VLAN ID/range lower limit
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: inner_header_vlan2
                            
                            	Inner header VLAN ID range higher limit
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: inner_header_cos
                            
                            	Inner header COS value
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: inner_header_dei
                            
                            	Inner header DEI bit
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: capture
                            
                            	Capture option, TRUE if enabled
                            	**type**\: bool
                            
                            .. attribute:: log_option
                            
                            	Log option
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: remark
                            
                            	Remark string
                            	**type**\: str
                            
                            .. attribute:: acl_name
                            
                            	Acl Name
                            	**type**\: str
                            
                            .. attribute:: sequence_string
                            
                            	Sequence Sring
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'es-acl-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(EsAcl.Active.List.Acls.Acl.AclSequenceNumbers.AclSequenceNumber, self).__init__()

                                self.yang_name = "acl-sequence-number"
                                self.yang_parent_name = "acl-sequence-numbers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sequence_number']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sequence_number', (YLeaf(YType.uint32, 'sequence-number'), ['int'])),
                                    ('ace_type', (YLeaf(YType.enumeration, 'ace-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper', 'AclAce1_', '')])),
                                    ('ace_sequence_number', (YLeaf(YType.uint32, 'ace-sequence-number'), ['int'])),
                                    ('hits', (YLeaf(YType.uint64, 'hits'), ['int'])),
                                    ('grant', (YLeaf(YType.enumeration, 'grant'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper', 'AclAction', '')])),
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                    ('source_wild_card_bits', (YLeaf(YType.str, 'source-wild-card-bits'), ['str'])),
                                    ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                                    ('destination_wild_card_bits', (YLeaf(YType.str, 'destination-wild-card-bits'), ['str'])),
                                    ('ether_type_number', (YLeaf(YType.uint16, 'ether-type-number'), ['int'])),
                                    ('vlan1', (YLeaf(YType.uint16, 'vlan1'), ['int'])),
                                    ('vlan2', (YLeaf(YType.uint16, 'vlan2'), ['int'])),
                                    ('cos', (YLeaf(YType.uint8, 'cos'), ['int'])),
                                    ('dei', (YLeaf(YType.uint8, 'dei'), ['int'])),
                                    ('inner_header_vlan1', (YLeaf(YType.uint16, 'inner-header-vlan1'), ['int'])),
                                    ('inner_header_vlan2', (YLeaf(YType.uint16, 'inner-header-vlan2'), ['int'])),
                                    ('inner_header_cos', (YLeaf(YType.uint8, 'inner-header-cos'), ['int'])),
                                    ('inner_header_dei', (YLeaf(YType.uint8, 'inner-header-dei'), ['int'])),
                                    ('capture', (YLeaf(YType.boolean, 'capture'), ['bool'])),
                                    ('log_option', (YLeaf(YType.uint8, 'log-option'), ['int'])),
                                    ('remark', (YLeaf(YType.str, 'remark'), ['str'])),
                                    ('acl_name', (YLeaf(YType.str, 'acl-name'), ['str'])),
                                    ('sequence_string', (YLeaf(YType.str, 'sequence-string'), ['str'])),
                                ])
                                self.sequence_number = None
                                self.ace_type = None
                                self.ace_sequence_number = None
                                self.hits = None
                                self.grant = None
                                self.source_address = None
                                self.source_wild_card_bits = None
                                self.destination_address = None
                                self.destination_wild_card_bits = None
                                self.ether_type_number = None
                                self.vlan1 = None
                                self.vlan2 = None
                                self.cos = None
                                self.dei = None
                                self.inner_header_vlan1 = None
                                self.inner_header_vlan2 = None
                                self.inner_header_cos = None
                                self.inner_header_dei = None
                                self.capture = None
                                self.log_option = None
                                self.remark = None
                                self.acl_name = None
                                self.sequence_string = None
                                self._segment_path = lambda: "acl-sequence-number" + "[sequence-number='" + str(self.sequence_number) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(EsAcl.Active.List.Acls.Acl.AclSequenceNumbers.AclSequenceNumber, ['sequence_number', 'ace_type', 'ace_sequence_number', 'hits', 'grant', 'source_address', 'source_wild_card_bits', 'destination_address', 'destination_wild_card_bits', 'ether_type_number', 'vlan1', 'vlan2', 'cos', 'dei', 'inner_header_vlan1', 'inner_header_vlan2', 'inner_header_cos', 'inner_header_dei', 'capture', 'log_option', 'remark', 'acl_name', 'sequence_string'], name, value)


        class OorAcls(Entity):
            """
            Resource occupation details for ACLs
            
            .. attribute:: oor_acl
            
            	Resource occupation details for a particular ACL
            	**type**\: list of  		 :py:class:`OorAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.OorAcls.OorAcl>`
            
            

            """

            _prefix = 'es-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(EsAcl.Active.OorAcls, self).__init__()

                self.yang_name = "oor-acls"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("oor-acl", ("oor_acl", EsAcl.Active.OorAcls.OorAcl))])
                self._leafs = OrderedDict()

                self.oor_acl = YList(self)
                self._segment_path = lambda: "oor-acls"
                self._absolute_path = lambda: "Cisco-IOS-XR-es-acl-oper:es-acl/active/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EsAcl.Active.OorAcls, [], name, value)


            class OorAcl(Entity):
                """
                Resource occupation details for a particular
                ACL
                
                .. attribute:: name  (key)
                
                	Name of the Access List
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: current_configured_ac_ls
                
                	Current configured acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_configured_ac_es
                
                	Current configured aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_configurable_ac_ls
                
                	max configurable acls
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_configurable_ac_es
                
                	max configurable aces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'es-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(EsAcl.Active.OorAcls.OorAcl, self).__init__()

                    self.yang_name = "oor-acl"
                    self.yang_parent_name = "oor-acls"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('current_configured_ac_ls', (YLeaf(YType.uint32, 'current-configured-ac-ls'), ['int'])),
                        ('current_configured_ac_es', (YLeaf(YType.uint32, 'current-configured-ac-es'), ['int'])),
                        ('maximum_configurable_ac_ls', (YLeaf(YType.uint32, 'maximum-configurable-ac-ls'), ['int'])),
                        ('maximum_configurable_ac_es', (YLeaf(YType.uint32, 'maximum-configurable-ac-es'), ['int'])),
                    ])
                    self.name = None
                    self.current_configured_ac_ls = None
                    self.current_configured_ac_es = None
                    self.maximum_configurable_ac_ls = None
                    self.maximum_configurable_ac_es = None
                    self._segment_path = lambda: "oor-acl" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-es-acl-oper:es-acl/active/oor-acls/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(EsAcl.Active.OorAcls.OorAcl, ['name', 'current_configured_ac_ls', 'current_configured_ac_es', 'maximum_configurable_ac_ls', 'maximum_configurable_ac_es'], name, value)


        class Usages(Entity):
            """
            Table of Usage statistics of ACLs at different
            nodes
            
            .. attribute:: usage
            
            	Usage statistics of an ACL at a node
            	**type**\: list of  		 :py:class:`Usage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper.EsAcl.Active.Usages.Usage>`
            
            

            """

            _prefix = 'es-acl-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(EsAcl.Active.Usages, self).__init__()

                self.yang_name = "usages"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("usage", ("usage", EsAcl.Active.Usages.Usage))])
                self._leafs = OrderedDict()

                self.usage = YList(self)
                self._segment_path = lambda: "usages"
                self._absolute_path = lambda: "Cisco-IOS-XR-es-acl-oper:es-acl/active/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EsAcl.Active.Usages, [], name, value)


            class Usage(Entity):
                """
                Usage statistics of an ACL at a node
                
                .. attribute:: location
                
                	Node where ACL is applied
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: application_id
                
                	Application ID
                	**type**\:  :py:class:`AclUsageAppIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_common_acl_datatypes.AclUsageAppIdEnum>`
                
                .. attribute:: name
                
                	Name of the ACL
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: usage_details
                
                	Usage Statistics Details
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'es-acl-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(EsAcl.Active.Usages.Usage, self).__init__()

                    self.yang_name = "usage"
                    self.yang_parent_name = "usages"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                        ('application_id', (YLeaf(YType.enumeration, 'application-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_common_acl_datatypes', 'AclUsageAppIdEnum', '')])),
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('usage_details', (YLeaf(YType.str, 'usage-details'), ['str'])),
                    ])
                    self.location = None
                    self.application_id = None
                    self.name = None
                    self.usage_details = None
                    self._segment_path = lambda: "usage"
                    self._absolute_path = lambda: "Cisco-IOS-XR-es-acl-oper:es-acl/active/usages/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(EsAcl.Active.Usages.Usage, ['location', 'application_id', 'name', 'usage_details'], name, value)

    def clone_ptr(self):
        self._top_entity = EsAcl()
        return self._top_entity

