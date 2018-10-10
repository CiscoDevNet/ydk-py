""" Cisco_IOS_XR_manageability_object_tracking_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR manageability\-object\-tracking package configuration.

This module contains definitions
for the following management objects\:
  object\-trackings\: Object Tracking configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ObjectTrackings(Entity):
    """
    Object Tracking configuration
    
    .. attribute:: object_tracking
    
    	Track name \- maximum 32 characters
    	**type**\: list of  		 :py:class:`ObjectTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking>`
    
    

    """

    _prefix = 'manageability-object-tracking-cfg'
    _revision = '2017-09-07'

    def __init__(self):
        super(ObjectTrackings, self).__init__()
        self._top_entity = None

        self.yang_name = "object-trackings"
        self.yang_parent_name = "Cisco-IOS-XR-manageability-object-tracking-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("object-tracking", ("object_tracking", ObjectTrackings.ObjectTracking))])
        self._leafs = OrderedDict()

        self.object_tracking = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-cfg:object-trackings"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ObjectTrackings, [], name, value)


    class ObjectTracking(Entity):
        """
        Track name \- maximum 32 characters
        
        .. attribute:: track_name  (key)
        
        	Track name
        	**type**\: str
        
        	**length:** 1..32
        
        .. attribute:: action
        
        	Actions associated with track state changes
        	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.Action>`
        
        .. attribute:: type_bfd_rtr
        
        	Track type BFD RTR (BFD Response Time Reporter)
        	**type**\:  :py:class:`TypeBfdRtr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeBfdRtr>`
        
        .. attribute:: type_interface
        
        	Track type line\-protocol
        	**type**\:  :py:class:`TypeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeInterface>`
        
        .. attribute:: type_rtr
        
        	Track type RTR (Response Time Reporter \- IPSLA)
        	**type**\:  :py:class:`TypeRtr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeRtr>`
        
        .. attribute:: type_list
        
        	Track type boolean list
        	**type**\:  :py:class:`TypeList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList>`
        
        .. attribute:: type_route
        
        	Track type route ipv4
        	**type**\:  :py:class:`TypeRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeRoute>`
        
        .. attribute:: type_boolean_list
        
        	Track type boolean list
        	**type**\:  :py:class:`TypeBooleanList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeBooleanList>`
        
        .. attribute:: delay_up
        
        	Delay up in seconds
        	**type**\: int
        
        	**range:** 1..180
        
        	**units**\: second
        
        .. attribute:: enable
        
        	Enable the Track
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: delay_down
        
        	Track delay down time
        	**type**\: int
        
        	**range:** 1..180
        
        	**units**\: second
        
        .. attribute:: type_interface_enable
        
        	Enable track type Interface
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: type_route_enable
        
        	Enable track type Route
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: type_boolean_list_and_enable
        
        	Enable track type boolean list and
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: type_boolean_list_or_enable
        
        	Enable track type boolean list or
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'manageability-object-tracking-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(ObjectTrackings.ObjectTracking, self).__init__()

            self.yang_name = "object-tracking"
            self.yang_parent_name = "object-trackings"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['track_name']
            self._child_classes = OrderedDict([("action", ("action", ObjectTrackings.ObjectTracking.Action)), ("type-bfd-rtr", ("type_bfd_rtr", ObjectTrackings.ObjectTracking.TypeBfdRtr)), ("type-interface", ("type_interface", ObjectTrackings.ObjectTracking.TypeInterface)), ("type-rtr", ("type_rtr", ObjectTrackings.ObjectTracking.TypeRtr)), ("type-list", ("type_list", ObjectTrackings.ObjectTracking.TypeList)), ("type-route", ("type_route", ObjectTrackings.ObjectTracking.TypeRoute)), ("type-boolean-list", ("type_boolean_list", ObjectTrackings.ObjectTracking.TypeBooleanList))])
            self._leafs = OrderedDict([
                ('track_name', (YLeaf(YType.str, 'track-name'), ['str'])),
                ('delay_up', (YLeaf(YType.uint32, 'delay-up'), ['int'])),
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ('delay_down', (YLeaf(YType.uint32, 'delay-down'), ['int'])),
                ('type_interface_enable', (YLeaf(YType.empty, 'type-interface-enable'), ['Empty'])),
                ('type_route_enable', (YLeaf(YType.empty, 'type-route-enable'), ['Empty'])),
                ('type_boolean_list_and_enable', (YLeaf(YType.empty, 'type-boolean-list-and-enable'), ['Empty'])),
                ('type_boolean_list_or_enable', (YLeaf(YType.empty, 'type-boolean-list-or-enable'), ['Empty'])),
            ])
            self.track_name = None
            self.delay_up = None
            self.enable = None
            self.delay_down = None
            self.type_interface_enable = None
            self.type_route_enable = None
            self.type_boolean_list_and_enable = None
            self.type_boolean_list_or_enable = None

            self.action = ObjectTrackings.ObjectTracking.Action()
            self.action.parent = self
            self._children_name_map["action"] = "action"

            self.type_bfd_rtr = ObjectTrackings.ObjectTracking.TypeBfdRtr()
            self.type_bfd_rtr.parent = self
            self._children_name_map["type_bfd_rtr"] = "type-bfd-rtr"

            self.type_interface = ObjectTrackings.ObjectTracking.TypeInterface()
            self.type_interface.parent = self
            self._children_name_map["type_interface"] = "type-interface"

            self.type_rtr = ObjectTrackings.ObjectTracking.TypeRtr()
            self.type_rtr.parent = self
            self._children_name_map["type_rtr"] = "type-rtr"

            self.type_list = ObjectTrackings.ObjectTracking.TypeList()
            self.type_list.parent = self
            self._children_name_map["type_list"] = "type-list"

            self.type_route = ObjectTrackings.ObjectTracking.TypeRoute()
            self.type_route.parent = self
            self._children_name_map["type_route"] = "type-route"

            self.type_boolean_list = ObjectTrackings.ObjectTracking.TypeBooleanList()
            self.type_boolean_list.parent = self
            self._children_name_map["type_boolean_list"] = "type-boolean-list"
            self._segment_path = lambda: "object-tracking" + "[track-name='" + str(self.track_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-cfg:object-trackings/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectTrackings.ObjectTracking, ['track_name', 'delay_up', 'enable', 'delay_down', 'type_interface_enable', 'type_route_enable', 'type_boolean_list_and_enable', 'type_boolean_list_or_enable'], name, value)


        class Action(Entity):
            """
            Actions associated with track state changes
            
            .. attribute:: action_err_dis
            
            	The list of all track actions
            	**type**\:  :py:class:`ActionErrDis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.Action.ActionErrDis>`
            
            .. attribute:: actions_enable
            
            	Enable track actions
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'manageability-object-tracking-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(ObjectTrackings.ObjectTracking.Action, self).__init__()

                self.yang_name = "action"
                self.yang_parent_name = "object-tracking"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("action-err-dis", ("action_err_dis", ObjectTrackings.ObjectTracking.Action.ActionErrDis))])
                self._leafs = OrderedDict([
                    ('actions_enable', (YLeaf(YType.empty, 'actions-enable'), ['Empty'])),
                ])
                self.actions_enable = None

                self.action_err_dis = ObjectTrackings.ObjectTracking.Action.ActionErrDis()
                self.action_err_dis.parent = self
                self._children_name_map["action_err_dis"] = "action-err-dis"
                self._segment_path = lambda: "action"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTrackings.ObjectTracking.Action, ['actions_enable'], name, value)


            class ActionErrDis(Entity):
                """
                The list of all track actions
                
                .. attribute:: action_err_di
                
                	Error disable track action
                	**type**\: list of  		 :py:class:`ActionErrDi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.Action.ActionErrDis.ActionErrDi>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(ObjectTrackings.ObjectTracking.Action.ActionErrDis, self).__init__()

                    self.yang_name = "action-err-dis"
                    self.yang_parent_name = "action"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("action-err-di", ("action_err_di", ObjectTrackings.ObjectTracking.Action.ActionErrDis.ActionErrDi))])
                    self._leafs = OrderedDict()

                    self.action_err_di = YList(self)
                    self._segment_path = lambda: "action-err-dis"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTrackings.ObjectTracking.Action.ActionErrDis, [], name, value)


                class ActionErrDi(Entity):
                    """
                    Error disable track action
                    
                    .. attribute:: track_state_type  (key)
                    
                    	Track State Type
                    	**type**\: int
                    
                    	**range:** 0..1
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface to be error\-disabled
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(ObjectTrackings.ObjectTracking.Action.ActionErrDis.ActionErrDi, self).__init__()

                        self.yang_name = "action-err-di"
                        self.yang_parent_name = "action-err-dis"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['track_state_type','interface_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('track_state_type', (YLeaf(YType.uint32, 'track-state-type'), ['int'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.track_state_type = None
                        self.interface_name = None
                        self._segment_path = lambda: "action-err-di" + "[track-state-type='" + str(self.track_state_type) + "']" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTrackings.ObjectTracking.Action.ActionErrDis.ActionErrDi, ['track_state_type', 'interface_name'], name, value)


        class TypeBfdRtr(Entity):
            """
            Track type BFD RTR (BFD Response Time Reporter)
            
            .. attribute:: bfd_rtr
            
            	BFD session related parameters
            	**type**\:  :py:class:`BfdRtr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeBfdRtr.BfdRtr>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'manageability-object-tracking-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(ObjectTrackings.ObjectTracking.TypeBfdRtr, self).__init__()

                self.yang_name = "type-bfd-rtr"
                self.yang_parent_name = "object-tracking"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("bfd-rtr", ("bfd_rtr", ObjectTrackings.ObjectTracking.TypeBfdRtr.BfdRtr))])
                self._leafs = OrderedDict()

                self.bfd_rtr = None
                self._children_name_map["bfd_rtr"] = "bfd-rtr"
                self._segment_path = lambda: "type-bfd-rtr"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTrackings.ObjectTracking.TypeBfdRtr, [], name, value)


            class BfdRtr(Entity):
                """
                BFD session related parameters
                
                .. attribute:: rate
                
                	Tx interval in ms
                	**type**\: int
                
                	**range:** 1..5000
                
                	**mandatory**\: True
                
                .. attribute:: debounce_count
                
                	Debounce Count
                	**type**\: int
                
                	**range:** 1..10
                
                	**mandatory**\: True
                
                .. attribute:: interface_name
                
                	Interface to be used for BFD session
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                	**mandatory**\: True
                
                .. attribute:: dest_address
                
                	Destination IP Address to track via BFD
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(ObjectTrackings.ObjectTracking.TypeBfdRtr.BfdRtr, self).__init__()

                    self.yang_name = "bfd-rtr"
                    self.yang_parent_name = "type-bfd-rtr"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                        ('debounce_count', (YLeaf(YType.uint32, 'debounce-count'), ['int'])),
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('dest_address', (YLeaf(YType.str, 'dest-address'), ['str'])),
                    ])
                    self.rate = None
                    self.debounce_count = None
                    self.interface_name = None
                    self.dest_address = None
                    self._segment_path = lambda: "bfd-rtr"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTrackings.ObjectTracking.TypeBfdRtr.BfdRtr, ['rate', 'debounce_count', 'interface_name', 'dest_address'], name, value)


        class TypeInterface(Entity):
            """
            Track type line\-protocol
            
            .. attribute:: interface
            
            	The name of the interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            

            """

            _prefix = 'manageability-object-tracking-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(ObjectTrackings.ObjectTracking.TypeInterface, self).__init__()

                self.yang_name = "type-interface"
                self.yang_parent_name = "object-tracking"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                ])
                self.interface = None
                self._segment_path = lambda: "type-interface"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTrackings.ObjectTracking.TypeInterface, ['interface'], name, value)


        class TypeRtr(Entity):
            """
            Track type RTR (Response Time Reporter \- IPSLA)
            
            .. attribute:: rtr
            
            	IPSLA Operation ID
            	**type**\: int
            
            	**range:** 1..2048
            
            

            """

            _prefix = 'manageability-object-tracking-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(ObjectTrackings.ObjectTracking.TypeRtr, self).__init__()

                self.yang_name = "type-rtr"
                self.yang_parent_name = "object-tracking"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rtr', (YLeaf(YType.uint32, 'rtr'), ['int'])),
                ])
                self.rtr = None
                self._segment_path = lambda: "type-rtr"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTrackings.ObjectTracking.TypeRtr, ['rtr'], name, value)


        class TypeList(Entity):
            """
            Track type boolean list
            
            .. attribute:: threshold_weight
            
            	Track type threshold weight
            	**type**\:  :py:class:`ThresholdWeight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight>`
            
            .. attribute:: threshold_percentage_object
            
            	Track type threshold percentage
            	**type**\:  :py:class:`ThresholdPercentageObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject>`
            
            .. attribute:: threshold_percentage
            
            	Track type threshold percentage
            	**type**\:  :py:class:`ThresholdPercentage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage>`
            
            .. attribute:: threshold_weight_object
            
            	Track type threshold weight
            	**type**\:  :py:class:`ThresholdWeightObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject>`
            
            .. attribute:: threshold_percentage_object_enable
            
            	Enable threshold based on percentage
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            	**units**\: percentage
            
            .. attribute:: threshold_weight_object_enable
            
            	Enable threshold based on weighted sum
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'manageability-object-tracking-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(ObjectTrackings.ObjectTracking.TypeList, self).__init__()

                self.yang_name = "type-list"
                self.yang_parent_name = "object-tracking"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("threshold-weight", ("threshold_weight", ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight)), ("threshold-percentage-object", ("threshold_percentage_object", ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject)), ("threshold-percentage", ("threshold_percentage", ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage)), ("threshold-weight-object", ("threshold_weight_object", ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject))])
                self._leafs = OrderedDict([
                    ('threshold_percentage_object_enable', (YLeaf(YType.empty, 'threshold-percentage-object-enable'), ['Empty'])),
                    ('threshold_weight_object_enable', (YLeaf(YType.empty, 'threshold-weight-object-enable'), ['Empty'])),
                ])
                self.threshold_percentage_object_enable = None
                self.threshold_weight_object_enable = None

                self.threshold_weight = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight()
                self.threshold_weight.parent = self
                self._children_name_map["threshold_weight"] = "threshold-weight"

                self.threshold_percentage_object = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject()
                self.threshold_percentage_object.parent = self
                self._children_name_map["threshold_percentage_object"] = "threshold-percentage-object"

                self.threshold_percentage = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage()
                self.threshold_percentage.parent = self
                self._children_name_map["threshold_percentage"] = "threshold-percentage"

                self.threshold_weight_object = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject()
                self.threshold_weight_object.parent = self
                self._children_name_map["threshold_weight_object"] = "threshold-weight-object"
                self._segment_path = lambda: "type-list"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTrackings.ObjectTracking.TypeList, ['threshold_percentage_object_enable', 'threshold_weight_object_enable'], name, value)


            class ThresholdWeight(Entity):
                """
                Track type threshold weight
                
                .. attribute:: threshold_limits
                
                	Threshold Limits
                	**type**\:  :py:class:`ThresholdLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight, self).__init__()

                    self.yang_name = "threshold-weight"
                    self.yang_parent_name = "type-list"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("threshold-limits", ("threshold_limits", ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits))])
                    self._leafs = OrderedDict()

                    self.threshold_limits = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits()
                    self.threshold_limits.parent = self
                    self._children_name_map["threshold_limits"] = "threshold-limits"
                    self._segment_path = lambda: "threshold-weight"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight, [], name, value)


                class ThresholdLimits(Entity):
                    """
                    Threshold Limits
                    
                    .. attribute:: threshold_up_values
                    
                    	Threshold limit at which track is set to UP state
                    	**type**\:  :py:class:`ThresholdUpValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits, self).__init__()

                        self.yang_name = "threshold-limits"
                        self.yang_parent_name = "threshold-weight"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("threshold-up-values", ("threshold_up_values", ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues))])
                        self._leafs = OrderedDict()

                        self.threshold_up_values = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues()
                        self.threshold_up_values.parent = self
                        self._children_name_map["threshold_up_values"] = "threshold-up-values"
                        self._segment_path = lambda: "threshold-limits"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits, [], name, value)


                    class ThresholdUpValues(Entity):
                        """
                        Threshold limit at which track is set to UP
                        state
                        
                        .. attribute:: threshold_up_value
                        
                        	Threshold limit at which track is set to UP state
                        	**type**\: list of  		 :py:class:`ThresholdUpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues.ThresholdUpValue>`
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues, self).__init__()

                            self.yang_name = "threshold-up-values"
                            self.yang_parent_name = "threshold-limits"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("threshold-up-value", ("threshold_up_value", ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues.ThresholdUpValue))])
                            self._leafs = OrderedDict()

                            self.threshold_up_value = YList(self)
                            self._segment_path = lambda: "threshold-up-values"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues, [], name, value)


                        class ThresholdUpValue(Entity):
                            """
                            Threshold limit at which track is set to UP
                            state
                            
                            .. attribute:: up  (key)
                            
                            	Up value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: threshold_down
                            
                            	Threshold limit at which track is set to Down state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 0
                            
                            

                            """

                            _prefix = 'manageability-object-tracking-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues.ThresholdUpValue, self).__init__()

                                self.yang_name = "threshold-up-value"
                                self.yang_parent_name = "threshold-up-values"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['up']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('up', (YLeaf(YType.uint32, 'up'), ['int'])),
                                    ('threshold_down', (YLeaf(YType.uint32, 'threshold-down'), ['int'])),
                                ])
                                self.up = None
                                self.threshold_down = None
                                self._segment_path = lambda: "threshold-up-value" + "[up='" + str(self.up) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues.ThresholdUpValue, ['up', 'threshold_down'], name, value)


            class ThresholdPercentageObject(Entity):
                """
                Track type threshold percentage
                
                .. attribute:: object
                
                	Track name object
                	**type**\: list of  		 :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject.Object>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject, self).__init__()

                    self.yang_name = "threshold-percentage-object"
                    self.yang_parent_name = "type-list"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("object", ("object", ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject.Object))])
                    self._leafs = OrderedDict()

                    self.object = YList(self)
                    self._segment_path = lambda: "threshold-percentage-object"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject, [], name, value)


                class Object(Entity):
                    """
                    Track name object
                    
                    .. attribute:: object  (key)
                    
                    	Object name
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: object_weight
                    
                    	Weight of object
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 1
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject.Object, self).__init__()

                        self.yang_name = "object"
                        self.yang_parent_name = "threshold-percentage-object"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['object']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('object', (YLeaf(YType.str, 'object'), ['str'])),
                            ('object_weight', (YLeaf(YType.uint32, 'object-weight'), ['int'])),
                        ])
                        self.object = None
                        self.object_weight = None
                        self._segment_path = lambda: "object" + "[object='" + str(self.object) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject.Object, ['object', 'object_weight'], name, value)


            class ThresholdPercentage(Entity):
                """
                Track type threshold percentage
                
                .. attribute:: threshold_limits
                
                	Threshold Limits
                	**type**\:  :py:class:`ThresholdLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage, self).__init__()

                    self.yang_name = "threshold-percentage"
                    self.yang_parent_name = "type-list"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("threshold-limits", ("threshold_limits", ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits))])
                    self._leafs = OrderedDict()

                    self.threshold_limits = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits()
                    self.threshold_limits.parent = self
                    self._children_name_map["threshold_limits"] = "threshold-limits"
                    self._segment_path = lambda: "threshold-percentage"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage, [], name, value)


                class ThresholdLimits(Entity):
                    """
                    Threshold Limits
                    
                    .. attribute:: threshold_up_values
                    
                    	Threshold limit at which track is set to UP state
                    	**type**\:  :py:class:`ThresholdUpValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits, self).__init__()

                        self.yang_name = "threshold-limits"
                        self.yang_parent_name = "threshold-percentage"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("threshold-up-values", ("threshold_up_values", ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues))])
                        self._leafs = OrderedDict()

                        self.threshold_up_values = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues()
                        self.threshold_up_values.parent = self
                        self._children_name_map["threshold_up_values"] = "threshold-up-values"
                        self._segment_path = lambda: "threshold-limits"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits, [], name, value)


                    class ThresholdUpValues(Entity):
                        """
                        Threshold limit at which track is set to UP
                        state
                        
                        .. attribute:: threshold_up_value
                        
                        	Threshold limit at which track is set to UP state
                        	**type**\: list of  		 :py:class:`ThresholdUpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues.ThresholdUpValue>`
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues, self).__init__()

                            self.yang_name = "threshold-up-values"
                            self.yang_parent_name = "threshold-limits"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("threshold-up-value", ("threshold_up_value", ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues.ThresholdUpValue))])
                            self._leafs = OrderedDict()

                            self.threshold_up_value = YList(self)
                            self._segment_path = lambda: "threshold-up-values"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues, [], name, value)


                        class ThresholdUpValue(Entity):
                            """
                            Threshold limit at which track is set to UP
                            state
                            
                            .. attribute:: up  (key)
                            
                            	Up value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: threshold_down
                            
                            	Threshold limit at which track is set to Down state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 0
                            
                            

                            """

                            _prefix = 'manageability-object-tracking-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues.ThresholdUpValue, self).__init__()

                                self.yang_name = "threshold-up-value"
                                self.yang_parent_name = "threshold-up-values"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['up']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('up', (YLeaf(YType.uint32, 'up'), ['int'])),
                                    ('threshold_down', (YLeaf(YType.uint32, 'threshold-down'), ['int'])),
                                ])
                                self.up = None
                                self.threshold_down = None
                                self._segment_path = lambda: "threshold-up-value" + "[up='" + str(self.up) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues.ThresholdUpValue, ['up', 'threshold_down'], name, value)


            class ThresholdWeightObject(Entity):
                """
                Track type threshold weight
                
                .. attribute:: object
                
                	Track name object
                	**type**\: list of  		 :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject.Object>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject, self).__init__()

                    self.yang_name = "threshold-weight-object"
                    self.yang_parent_name = "type-list"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("object", ("object", ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject.Object))])
                    self._leafs = OrderedDict()

                    self.object = YList(self)
                    self._segment_path = lambda: "threshold-weight-object"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject, [], name, value)


                class Object(Entity):
                    """
                    Track name object
                    
                    .. attribute:: object  (key)
                    
                    	Object name
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: object_weight
                    
                    	Weight of object
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 1
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject.Object, self).__init__()

                        self.yang_name = "object"
                        self.yang_parent_name = "threshold-weight-object"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['object']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('object', (YLeaf(YType.str, 'object'), ['str'])),
                            ('object_weight', (YLeaf(YType.uint32, 'object-weight'), ['int'])),
                        ])
                        self.object = None
                        self.object_weight = None
                        self._segment_path = lambda: "object" + "[object='" + str(self.object) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject.Object, ['object', 'object_weight'], name, value)


        class TypeRoute(Entity):
            """
            Track type route ipv4
            
            .. attribute:: ip_address
            
            	set track IPv4 address
            	**type**\:  :py:class:`IpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeRoute.IpAddress>`
            
            	**presence node**\: True
            
            .. attribute:: vrf
            
            	VRF tag \- use 'default' for the DEFAULT vrf
            	**type**\: str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'manageability-object-tracking-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(ObjectTrackings.ObjectTracking.TypeRoute, self).__init__()

                self.yang_name = "type-route"
                self.yang_parent_name = "object-tracking"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ip-address", ("ip_address", ObjectTrackings.ObjectTracking.TypeRoute.IpAddress))])
                self._leafs = OrderedDict([
                    ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                ])
                self.vrf = None

                self.ip_address = None
                self._children_name_map["ip_address"] = "ip-address"
                self._segment_path = lambda: "type-route"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTrackings.ObjectTracking.TypeRoute, ['vrf'], name, value)


            class IpAddress(Entity):
                """
                set track IPv4 address
                
                .. attribute:: address
                
                	IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: mask
                
                	Mask
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(ObjectTrackings.ObjectTracking.TypeRoute.IpAddress, self).__init__()

                    self.yang_name = "ip-address"
                    self.yang_parent_name = "type-route"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                        ('mask', (YLeaf(YType.str, 'mask'), ['str'])),
                    ])
                    self.address = None
                    self.mask = None
                    self._segment_path = lambda: "ip-address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTrackings.ObjectTracking.TypeRoute.IpAddress, ['address', 'mask'], name, value)


        class TypeBooleanList(Entity):
            """
            Track type boolean list
            
            .. attribute:: or_objects
            
            	Track type boolean or list
            	**type**\:  :py:class:`OrObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects>`
            
            .. attribute:: and_objects
            
            	Track type boolean and list
            	**type**\:  :py:class:`AndObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects>`
            
            

            """

            _prefix = 'manageability-object-tracking-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(ObjectTrackings.ObjectTracking.TypeBooleanList, self).__init__()

                self.yang_name = "type-boolean-list"
                self.yang_parent_name = "object-tracking"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("or-objects", ("or_objects", ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects)), ("and-objects", ("and_objects", ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects))])
                self._leafs = OrderedDict()

                self.or_objects = ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects()
                self.or_objects.parent = self
                self._children_name_map["or_objects"] = "or-objects"

                self.and_objects = ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects()
                self.and_objects.parent = self
                self._children_name_map["and_objects"] = "and-objects"
                self._segment_path = lambda: "type-boolean-list"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTrackings.ObjectTracking.TypeBooleanList, [], name, value)


            class OrObjects(Entity):
                """
                Track type boolean or list
                
                .. attribute:: or_object
                
                	Track name \- maximum 32 characters
                	**type**\: list of  		 :py:class:`OrObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects.OrObject>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects, self).__init__()

                    self.yang_name = "or-objects"
                    self.yang_parent_name = "type-boolean-list"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("or-object", ("or_object", ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects.OrObject))])
                    self._leafs = OrderedDict()

                    self.or_object = YList(self)
                    self._segment_path = lambda: "or-objects"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects, [], name, value)


                class OrObject(Entity):
                    """
                    Track name \- maximum 32 characters
                    
                    .. attribute:: object  (key)
                    
                    	Object name
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: object_sign
                    
                    	Tracked Object sign (with or without not)
                    	**type**\:  :py:class:`ObjectTrackingBooleanSign <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_datatypes.ObjectTrackingBooleanSign>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects.OrObject, self).__init__()

                        self.yang_name = "or-object"
                        self.yang_parent_name = "or-objects"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['object']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('object', (YLeaf(YType.str, 'object'), ['str'])),
                            ('object_sign', (YLeaf(YType.enumeration, 'object-sign'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_datatypes', 'ObjectTrackingBooleanSign', '')])),
                        ])
                        self.object = None
                        self.object_sign = None
                        self._segment_path = lambda: "or-object" + "[object='" + str(self.object) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects.OrObject, ['object', 'object_sign'], name, value)


            class AndObjects(Entity):
                """
                Track type boolean and list
                
                .. attribute:: and_object
                
                	Track name \- maximum 32 characters
                	**type**\: list of  		 :py:class:`AndObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects.AndObject>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects, self).__init__()

                    self.yang_name = "and-objects"
                    self.yang_parent_name = "type-boolean-list"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("and-object", ("and_object", ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects.AndObject))])
                    self._leafs = OrderedDict()

                    self.and_object = YList(self)
                    self._segment_path = lambda: "and-objects"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects, [], name, value)


                class AndObject(Entity):
                    """
                    Track name \- maximum 32 characters
                    
                    .. attribute:: object_name  (key)
                    
                    	Object name
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: object_sign
                    
                    	Tracked Object sign (with or without not)
                    	**type**\:  :py:class:`ObjectTrackingBooleanSign <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_datatypes.ObjectTrackingBooleanSign>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects.AndObject, self).__init__()

                        self.yang_name = "and-object"
                        self.yang_parent_name = "and-objects"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['object_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                            ('object_sign', (YLeaf(YType.enumeration, 'object-sign'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_datatypes', 'ObjectTrackingBooleanSign', '')])),
                        ])
                        self.object_name = None
                        self.object_sign = None
                        self._segment_path = lambda: "and-object" + "[object-name='" + str(self.object_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects.AndObject, ['object_name', 'object_sign'], name, value)

    def clone_ptr(self):
        self._top_entity = ObjectTrackings()
        return self._top_entity

