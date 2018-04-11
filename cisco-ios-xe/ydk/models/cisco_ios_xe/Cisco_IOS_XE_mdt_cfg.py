""" Cisco_IOS_XE_mdt_cfg 

This module contains a collection of YANG 
definitions for configuration of streaming telemetry.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MdtXfrmAttrType(Enum):
    """
    MdtXfrmAttrType (Enum Class)

    Types of subscription transform attribute type

    .. data:: mdt_xfrm_attr_none = 0

    	Indicates that no filter has been 

    	specified.

    .. data:: mandatory = 1

    	Indicates that mandatory filter is set.

    """

    mdt_xfrm_attr_none = Enum.YLeaf(0, "mdt-xfrm-attr-none")

    mandatory = Enum.YLeaf(1, "mandatory")


class MdtXfrmLogicOp(Enum):
    """
    MdtXfrmLogicOp (Enum Class)

    Types of subscription transform 

    logical operations.

    .. data:: mdt_xfrm_lop_none = 0

    	Indicates that no logical operation 

    	is selected

    .. data:: and_ = 1

    	Indicates that logical operation 

    	is 'and' 

    .. data:: or_ = 2

    	Indicates that logical operation is 'or' 

    """

    mdt_xfrm_lop_none = Enum.YLeaf(0, "mdt-xfrm-lop-none")

    and_ = Enum.YLeaf(1, "and")

    or_ = Enum.YLeaf(2, "or")


class MdtXfrmOpType(Enum):
    """
    MdtXfrmOpType (Enum Class)

    Types of subscription transform operations.

    .. data:: sub_record = 0

    	Indicates that operation type is 

    	sub-record

    .. data:: delta = 1

    	Indicates that operation type is delta

    """

    sub_record = Enum.YLeaf(0, "sub-record")

    delta = Enum.YLeaf(1, "delta")


class MdtXfrmOperator(Enum):
    """
    MdtXfrmOperator (Enum Class)

    Supported operator types

    .. data:: operator_none = 0

    	Default operator

    .. data:: eq = 1

    	Equal operator

    .. data:: ne = 2

    	Not equal operator

    .. data:: gt = 3

    	Greater than operator

    .. data:: ge = 4

    	Greater than or equal operator

    .. data:: lt = 5

    	Less than operator

    .. data:: le = 6

    	Less than or equal operator

    """

    operator_none = Enum.YLeaf(0, "operator-none")

    eq = Enum.YLeaf(1, "eq")

    ne = Enum.YLeaf(2, "ne")

    gt = Enum.YLeaf(3, "gt")

    ge = Enum.YLeaf(4, "ge")

    lt = Enum.YLeaf(5, "lt")

    le = Enum.YLeaf(6, "le")



class MdtSubscriptions(Entity):
    """
    Subscription configuration
    
    .. attribute:: mdt_subscription
    
    	List of subscriptions
    	**type**\: list of  		 :py:class:`MdtSubscription <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtSubscriptions.MdtSubscription>`
    
    .. attribute:: mdt_xfrm
    
    	List of subscription transforms
    	**type**\: list of  		 :py:class:`MdtXfrm <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtSubscriptions.MdtXfrm>`
    
    

    """

    _prefix = 'mdt-cfg'
    _revision = '2017-10-29'

    def __init__(self):
        super(MdtSubscriptions, self).__init__()
        self._top_entity = None

        self.yang_name = "mdt-subscriptions"
        self.yang_parent_name = "Cisco-IOS-XE-mdt-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("mdt-subscription", ("mdt_subscription", MdtSubscriptions.MdtSubscription)), ("mdt-xfrm", ("mdt_xfrm", MdtSubscriptions.MdtXfrm))])
        self._leafs = OrderedDict()

        self.mdt_subscription = YList(self)
        self.mdt_xfrm = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-mdt-cfg:mdt-subscriptions"

    def __setattr__(self, name, value):
        self._perform_setattr(MdtSubscriptions, [], name, value)


    class MdtSubscription(Entity):
        """
        List of subscriptions
        
        .. attribute:: subscription_id  (key)
        
        	Unique subscription identifier
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: base
        
        	Common subscription information
        	**type**\:  :py:class:`Base <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtSubscriptions.MdtSubscription.Base>`
        
        .. attribute:: mdt_receivers
        
        	Configuration of receivers of configured  subscriptions
        	**type**\: list of  		 :py:class:`MdtReceivers <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtSubscriptions.MdtSubscription.MdtReceivers>`
        
        

        """

        _prefix = 'mdt-cfg'
        _revision = '2017-10-29'

        def __init__(self):
            super(MdtSubscriptions.MdtSubscription, self).__init__()

            self.yang_name = "mdt-subscription"
            self.yang_parent_name = "mdt-subscriptions"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['subscription_id']
            self._child_container_classes = OrderedDict([("base", ("base", MdtSubscriptions.MdtSubscription.Base))])
            self._child_list_classes = OrderedDict([("mdt-receivers", ("mdt_receivers", MdtSubscriptions.MdtSubscription.MdtReceivers))])
            self._leafs = OrderedDict([
                ('subscription_id', YLeaf(YType.uint32, 'subscription-id')),
            ])
            self.subscription_id = None

            self.base = MdtSubscriptions.MdtSubscription.Base()
            self.base.parent = self
            self._children_name_map["base"] = "base"
            self._children_yang_names.add("base")

            self.mdt_receivers = YList(self)
            self._segment_path = lambda: "mdt-subscription" + "[subscription-id='" + str(self.subscription_id) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-mdt-cfg:mdt-subscriptions/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MdtSubscriptions.MdtSubscription, ['subscription_id'], name, value)


        class Base(Entity):
            """
            Common subscription information.
            
            .. attribute:: stream
            
            	The name of the event stream being subscribed to
            	**type**\: str
            
            	**default value**\: NETCONF
            
            .. attribute:: encoding
            
            	Update notification encoding
            	**type**\: str
            
            	**default value**\: encode-xml
            
            .. attribute:: source_vrf
            
            	Network instance name for the VRF
            	**type**\: str
            
            .. attribute:: source_address
            
            	The source address for the notifications
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: no_trigger
            
            	Placeholder for unset value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**default value**\: 0
            
            .. attribute:: period
            
            	Period of update notifications in 100ths of a second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            	**units**\: centiseconds
            
            .. attribute:: no_synch_on_start
            
            	If true, there is no initial update notification with the current value of all the data. NOT CURRENTLY SUPPORTED. If specified, must be false
            	**type**\: bool
            
            .. attribute:: no_filter
            
            	Placeholder for unset value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**default value**\: 0
            
            .. attribute:: xpath
            
            	XPath expression describing the set of objects wanted as part of the subscription
            	**type**\: str
            
            .. attribute:: tdl_uri
            
            	TDL\-URI expression describing the set of objects wanted as part of the subscription
            	**type**\: str
            
            .. attribute:: transform_name
            
            	Transform name is the reference to  tdl transform scheme
            	**type**\: str
            
            

            """

            _prefix = 'mdt-cfg'
            _revision = '2017-10-29'

            def __init__(self):
                super(MdtSubscriptions.MdtSubscription.Base, self).__init__()

                self.yang_name = "base"
                self.yang_parent_name = "mdt-subscription"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stream', YLeaf(YType.str, 'stream')),
                    ('encoding', YLeaf(YType.str, 'encoding')),
                    ('source_vrf', YLeaf(YType.str, 'source-vrf')),
                    ('source_address', YLeaf(YType.str, 'source-address')),
                    ('no_trigger', YLeaf(YType.uint32, 'no-trigger')),
                    ('period', YLeaf(YType.uint32, 'period')),
                    ('no_synch_on_start', YLeaf(YType.boolean, 'no-synch-on-start')),
                    ('no_filter', YLeaf(YType.uint32, 'no-filter')),
                    ('xpath', YLeaf(YType.str, 'xpath')),
                    ('tdl_uri', YLeaf(YType.str, 'tdl-uri')),
                    ('transform_name', YLeaf(YType.str, 'transform-name')),
                ])
                self.stream = None
                self.encoding = None
                self.source_vrf = None
                self.source_address = None
                self.no_trigger = None
                self.period = None
                self.no_synch_on_start = None
                self.no_filter = None
                self.xpath = None
                self.tdl_uri = None
                self.transform_name = None
                self._segment_path = lambda: "base"

            def __setattr__(self, name, value):
                self._perform_setattr(MdtSubscriptions.MdtSubscription.Base, ['stream', 'encoding', 'source_vrf', 'source_address', 'no_trigger', 'period', 'no_synch_on_start', 'no_filter', 'xpath', 'tdl_uri', 'transform_name'], name, value)


        class MdtReceivers(Entity):
            """
            Configuration of receivers of configured 
            subscriptions.
            
            .. attribute:: address  (key)
            
            	IP address of the receiver
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            	**mandatory**\: True
            
            .. attribute:: port  (key)
            
            	Network port of the receiver
            	**type**\: int
            
            	**range:** 0..65535
            
            	**mandatory**\: True
            
            .. attribute:: protocol
            
            	Receiver transport protocol
            	**type**\: str
            
            	**default value**\: netconf
            
            .. attribute:: security_profile
            
            	Receiver security profile
            	**type**\: str
            
            

            """

            _prefix = 'mdt-cfg'
            _revision = '2017-10-29'

            def __init__(self):
                super(MdtSubscriptions.MdtSubscription.MdtReceivers, self).__init__()

                self.yang_name = "mdt-receivers"
                self.yang_parent_name = "mdt-subscription"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['address','port']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('address', YLeaf(YType.str, 'address')),
                    ('port', YLeaf(YType.uint16, 'port')),
                    ('protocol', YLeaf(YType.str, 'protocol')),
                    ('security_profile', YLeaf(YType.str, 'security-profile')),
                ])
                self.address = None
                self.port = None
                self.protocol = None
                self.security_profile = None
                self._segment_path = lambda: "mdt-receivers" + "[address='" + str(self.address) + "']" + "[port='" + str(self.port) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(MdtSubscriptions.MdtSubscription.MdtReceivers, ['address', 'port', 'protocol', 'security_profile'], name, value)


    class MdtXfrm(Entity):
        """
        List of subscription transforms
        
        .. attribute:: name  (key)
        
        	Unique transform identifier
        	**type**\: str
        
        .. attribute:: fully_specify
        
        	When fully\-specify is set,  fully\-specify field identifier is sent  in the response record along with field value
        	**type**\: bool
        
        .. attribute:: mdt_xfrm_input
        
        	Transform input information
        	**type**\: list of  		 :py:class:`MdtXfrmInput <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtSubscriptions.MdtXfrm.MdtXfrmInput>`
        
        .. attribute:: mdt_xfrm_op
        
        	Transform operations information
        	**type**\: list of  		 :py:class:`MdtXfrmOp <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtSubscriptions.MdtXfrm.MdtXfrmOp>`
        
        

        """

        _prefix = 'mdt-cfg'
        _revision = '2017-10-29'

        def __init__(self):
            super(MdtSubscriptions.MdtXfrm, self).__init__()

            self.yang_name = "mdt-xfrm"
            self.yang_parent_name = "mdt-subscriptions"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mdt-xfrm-input", ("mdt_xfrm_input", MdtSubscriptions.MdtXfrm.MdtXfrmInput)), ("mdt-xfrm-op", ("mdt_xfrm_op", MdtSubscriptions.MdtXfrm.MdtXfrmOp))])
            self._leafs = OrderedDict([
                ('name', YLeaf(YType.str, 'name')),
                ('fully_specify', YLeaf(YType.boolean, 'fully-specify')),
            ])
            self.name = None
            self.fully_specify = None

            self.mdt_xfrm_input = YList(self)
            self.mdt_xfrm_op = YList(self)
            self._segment_path = lambda: "mdt-xfrm" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-mdt-cfg:mdt-subscriptions/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MdtSubscriptions.MdtXfrm, ['name', 'fully_specify'], name, value)


        class MdtXfrmInput(Entity):
            """
            Transform input information
            
            .. attribute:: table_name  (key)
            
            	Transform input URI table name
            	**type**\: str
            
            .. attribute:: uri
            
            	Transform input URI full\-path
            	**type**\: str
            
            .. attribute:: mdt_xfrm_input_field
            
            	Transform input URI table fields
            	**type**\: list of  		 :py:class:`MdtXfrmInputField <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtSubscriptions.MdtXfrm.MdtXfrmInput.MdtXfrmInputField>`
            
            .. attribute:: join_key
            
            	Transform input table join\-key
            	**type**\: str
            
            .. attribute:: attr_type
            
            	Transform input table attribute type  e.g. table is mandatory for join record
            	**type**\:  :py:class:`MdtXfrmAttrType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtXfrmAttrType>`
            
            .. attribute:: lop
            
            	Logical operation with next input table event
            	**type**\:  :py:class:`MdtXfrmLogicOp <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtXfrmLogicOp>`
            
            

            """

            _prefix = 'mdt-cfg'
            _revision = '2017-10-29'

            def __init__(self):
                super(MdtSubscriptions.MdtXfrm.MdtXfrmInput, self).__init__()

                self.yang_name = "mdt-xfrm-input"
                self.yang_parent_name = "mdt-xfrm"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['table_name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("mdt-xfrm-input-field", ("mdt_xfrm_input_field", MdtSubscriptions.MdtXfrm.MdtXfrmInput.MdtXfrmInputField))])
                self._leafs = OrderedDict([
                    ('table_name', YLeaf(YType.str, 'table-name')),
                    ('uri', YLeaf(YType.str, 'uri')),
                    ('join_key', YLeaf(YType.str, 'join-key')),
                    ('attr_type', YLeaf(YType.enumeration, 'attr-type')),
                    ('lop', YLeaf(YType.enumeration, 'lop')),
                ])
                self.table_name = None
                self.uri = None
                self.join_key = None
                self.attr_type = None
                self.lop = None

                self.mdt_xfrm_input_field = YList(self)
                self._segment_path = lambda: "mdt-xfrm-input" + "[table-name='" + str(self.table_name) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(MdtSubscriptions.MdtXfrm.MdtXfrmInput, ['table_name', 'uri', 'join_key', 'attr_type', 'lop'], name, value)


            class MdtXfrmInputField(Entity):
                """
                Transform input URI table fields
                
                .. attribute:: field  (key)
                
                	Transform input URI table field name
                	**type**\: str
                
                

                """

                _prefix = 'mdt-cfg'
                _revision = '2017-10-29'

                def __init__(self):
                    super(MdtSubscriptions.MdtXfrm.MdtXfrmInput.MdtXfrmInputField, self).__init__()

                    self.yang_name = "mdt-xfrm-input-field"
                    self.yang_parent_name = "mdt-xfrm-input"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['field']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('field', YLeaf(YType.str, 'field')),
                    ])
                    self.field = None
                    self._segment_path = lambda: "mdt-xfrm-input-field" + "[field='" + str(self.field) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(MdtSubscriptions.MdtXfrm.MdtXfrmInput.MdtXfrmInputField, ['field'], name, value)


        class MdtXfrmOp(Entity):
            """
            Transform operations information
            
            .. attribute:: id  (key)
            
            	Unique transform operation id
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mdt_xfrm_op_filters
            
            	Transform operation filters.  These are evaluated before performing transform action (e.g. subrecord)  on the response record
            	**type**\: list of  		 :py:class:`MdtXfrmOpFilters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFilters>`
            
            .. attribute:: mdt_xfrm_op_fields
            
            	Transform operation fields.  Default operation is subrecord. It is performed on each field
            	**type**\: list of  		 :py:class:`MdtXfrmOpFields <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFields>`
            
            

            """

            _prefix = 'mdt-cfg'
            _revision = '2017-10-29'

            def __init__(self):
                super(MdtSubscriptions.MdtXfrm.MdtXfrmOp, self).__init__()

                self.yang_name = "mdt-xfrm-op"
                self.yang_parent_name = "mdt-xfrm"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['id']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("mdt-xfrm-op-filters", ("mdt_xfrm_op_filters", MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFilters)), ("mdt-xfrm-op-fields", ("mdt_xfrm_op_fields", MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFields))])
                self._leafs = OrderedDict([
                    ('id', YLeaf(YType.uint32, 'id')),
                ])
                self.id = None

                self.mdt_xfrm_op_filters = YList(self)
                self.mdt_xfrm_op_fields = YList(self)
                self._segment_path = lambda: "mdt-xfrm-op" + "[id='" + str(self.id) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(MdtSubscriptions.MdtXfrm.MdtXfrmOp, ['id'], name, value)


            class MdtXfrmOpFilters(Entity):
                """
                Transform operation filters. 
                These are evaluated before performing
                transform action (e.g. subrecord) 
                on the response record
                
                .. attribute:: filter_id  (key)
                
                	filters will be evaluated in sequence based  on filter\_id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: field
                
                	Transform operation filter field name
                	**type**\: str
                
                .. attribute:: op_event
                
                	Transform operation event flag (e.g. onchange)
                	**type**\:  :py:class:`OpEvent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFilters.OpEvent>`
                
                .. attribute:: lop
                
                	logical operation with condition
                	**type**\:  :py:class:`MdtXfrmLogicOp <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtXfrmLogicOp>`
                
                .. attribute:: condition
                
                	Per field condition (e.g. f1 eq 'name')
                	**type**\:  :py:class:`Condition <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFilters.Condition>`
                
                .. attribute:: next_lop
                
                	logical operation with next filter condition
                	**type**\:  :py:class:`MdtXfrmLogicOp <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtXfrmLogicOp>`
                
                

                """

                _prefix = 'mdt-cfg'
                _revision = '2017-10-29'

                def __init__(self):
                    super(MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFilters, self).__init__()

                    self.yang_name = "mdt-xfrm-op-filters"
                    self.yang_parent_name = "mdt-xfrm-op"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['filter_id']
                    self._child_container_classes = OrderedDict([("op-event", ("op_event", MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFilters.OpEvent)), ("condition", ("condition", MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFilters.Condition))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('filter_id', YLeaf(YType.uint32, 'filter-id')),
                        ('field', YLeaf(YType.str, 'field')),
                        ('lop', YLeaf(YType.enumeration, 'lop')),
                        ('next_lop', YLeaf(YType.enumeration, 'next-lop')),
                    ])
                    self.filter_id = None
                    self.field = None
                    self.lop = None
                    self.next_lop = None

                    self.op_event = MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFilters.OpEvent()
                    self.op_event.parent = self
                    self._children_name_map["op_event"] = "op-event"
                    self._children_yang_names.add("op-event")

                    self.condition = MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFilters.Condition()
                    self.condition.parent = self
                    self._children_name_map["condition"] = "condition"
                    self._children_yang_names.add("condition")
                    self._segment_path = lambda: "mdt-xfrm-op-filters" + "[filter-id='" + str(self.filter_id) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFilters, ['filter_id', 'field', 'lop', 'next_lop'], name, value)


                class OpEvent(Entity):
                    """
                    Transform operation event flag (e.g. onchange)
                    
                    .. attribute:: onchange
                    
                    	Indicates that onchange filter is set
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'mdt-cfg'
                    _revision = '2017-10-29'

                    def __init__(self):
                        super(MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFilters.OpEvent, self).__init__()

                        self.yang_name = "op-event"
                        self.yang_parent_name = "mdt-xfrm-op-filters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('onchange', YLeaf(YType.boolean, 'onchange')),
                        ])
                        self.onchange = None
                        self._segment_path = lambda: "op-event"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFilters.OpEvent, ['onchange'], name, value)


                class Condition(Entity):
                    """
                    Per field condition (e.g. f1 eq 'name')
                    
                    .. attribute:: operator
                    
                    	Type of operator
                    	**type**\:  :py:class:`MdtXfrmOperator <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtXfrmOperator>`
                    
                    .. attribute:: value
                    
                    	Field value to operate on
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'mdt-cfg'
                    _revision = '2017-10-29'

                    def __init__(self):
                        super(MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFilters.Condition, self).__init__()

                        self.yang_name = "condition"
                        self.yang_parent_name = "mdt-xfrm-op-filters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('operator', YLeaf(YType.enumeration, 'operator')),
                            ('value', YLeaf(YType.str, 'value')),
                        ])
                        self.operator = None
                        self.value = None
                        self._segment_path = lambda: "condition"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFilters.Condition, ['operator', 'value'], name, value)


            class MdtXfrmOpFields(Entity):
                """
                Transform operation fields. 
                Default operation is subrecord.
                It is performed on each field
                
                .. attribute:: field_id  (key)
                
                	Transform operation response field\-id, part of response record. It is used to uniquely identify response record field
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: field
                
                	Subscription transform field name on  which transform operation is performed
                	**type**\: str
                
                .. attribute:: op_type
                
                	Subscription transform operation type
                	**type**\:  :py:class:`MdtXfrmOpType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtXfrmOpType>`
                
                

                """

                _prefix = 'mdt-cfg'
                _revision = '2017-10-29'

                def __init__(self):
                    super(MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFields, self).__init__()

                    self.yang_name = "mdt-xfrm-op-fields"
                    self.yang_parent_name = "mdt-xfrm-op"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['field_id']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('field_id', YLeaf(YType.uint32, 'field-id')),
                        ('field', YLeaf(YType.str, 'field')),
                        ('op_type', YLeaf(YType.enumeration, 'op-type')),
                    ])
                    self.field_id = None
                    self.field = None
                    self.op_type = None
                    self._segment_path = lambda: "mdt-xfrm-op-fields" + "[field-id='" + str(self.field_id) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(MdtSubscriptions.MdtXfrm.MdtXfrmOp.MdtXfrmOpFields, ['field_id', 'field', 'op_type'], name, value)

    def clone_ptr(self):
        self._top_entity = MdtSubscriptions()
        return self._top_entity

