""" Cisco_IOS_XE_mdt_cfg 

This module contains a collection of YANG 
definitions for configuration of streaming telemetry.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MdtSubscriptions(Entity):
    """
    Subscription configuration
    
    .. attribute:: mdt_subscription
    
    	List of subscriptions
    	**type**\: list of  		 :py:class:`MdtSubscription <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtSubscriptions.MdtSubscription>`
    
    

    """

    _prefix = 'mdt-cfg'
    _revision = '2017-03-02'

    def __init__(self):
        super(MdtSubscriptions, self).__init__()
        self._top_entity = None

        self.yang_name = "mdt-subscriptions"
        self.yang_parent_name = "Cisco-IOS-XE-mdt-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"mdt-subscription" : ("mdt_subscription", MdtSubscriptions.MdtSubscription)}

        self.mdt_subscription = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-mdt-cfg:mdt-subscriptions"

    def __setattr__(self, name, value):
        self._perform_setattr(MdtSubscriptions, [], name, value)


    class MdtSubscription(Entity):
        """
        List of subscriptions
        
        .. attribute:: subscription_id  <key>
        
        	Unique subscription identifier
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: base
        
        	Common subscription information
        	**type**\:  :py:class:`Base <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtSubscriptions.MdtSubscription.Base>`
        
        .. attribute:: mdt_receivers
        
        	Configuration of receivers of configured subscriptions
        	**type**\: list of  		 :py:class:`MdtReceivers <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtSubscriptions.MdtSubscription.MdtReceivers>`
        
        

        """

        _prefix = 'mdt-cfg'
        _revision = '2017-03-02'

        def __init__(self):
            super(MdtSubscriptions.MdtSubscription, self).__init__()

            self.yang_name = "mdt-subscription"
            self.yang_parent_name = "mdt-subscriptions"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"base" : ("base", MdtSubscriptions.MdtSubscription.Base)}
            self._child_list_classes = {"mdt-receivers" : ("mdt_receivers", MdtSubscriptions.MdtSubscription.MdtReceivers)}

            self.subscription_id = YLeaf(YType.uint32, "subscription-id")

            self.base = MdtSubscriptions.MdtSubscription.Base()
            self.base.parent = self
            self._children_name_map["base"] = "base"
            self._children_yang_names.add("base")

            self.mdt_receivers = YList(self)
            self._segment_path = lambda: "mdt-subscription" + "[subscription-id='" + self.subscription_id.get() + "']"
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
            
            

            """

            _prefix = 'mdt-cfg'
            _revision = '2017-03-02'

            def __init__(self):
                super(MdtSubscriptions.MdtSubscription.Base, self).__init__()

                self.yang_name = "base"
                self.yang_parent_name = "mdt-subscription"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.stream = YLeaf(YType.str, "stream")

                self.encoding = YLeaf(YType.str, "encoding")

                self.source_vrf = YLeaf(YType.str, "source-vrf")

                self.source_address = YLeaf(YType.str, "source-address")

                self.no_trigger = YLeaf(YType.uint32, "no-trigger")

                self.period = YLeaf(YType.uint32, "period")

                self.no_synch_on_start = YLeaf(YType.boolean, "no-synch-on-start")

                self.no_filter = YLeaf(YType.uint32, "no-filter")

                self.xpath = YLeaf(YType.str, "xpath")

                self.tdl_uri = YLeaf(YType.str, "tdl-uri")
                self._segment_path = lambda: "base"

            def __setattr__(self, name, value):
                self._perform_setattr(MdtSubscriptions.MdtSubscription.Base, ['stream', 'encoding', 'source_vrf', 'source_address', 'no_trigger', 'period', 'no_synch_on_start', 'no_filter', 'xpath', 'tdl_uri'], name, value)


        class MdtReceivers(Entity):
            """
            Configuration of receivers of configured subscriptions.
            
            .. attribute:: address  <key>
            
            	IP address of the receiver
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            	**mandatory**\: True
            
            .. attribute:: port  <key>
            
            	Network port of the receiver
            	**type**\: int
            
            	**range:** 0..65535
            
            	**mandatory**\: True
            
            .. attribute:: protocol
            
            	Receiver transport protocol
            	**type**\: str
            
            	**default value**\: netconf
            
            

            """

            _prefix = 'mdt-cfg'
            _revision = '2017-03-02'

            def __init__(self):
                super(MdtSubscriptions.MdtSubscription.MdtReceivers, self).__init__()

                self.yang_name = "mdt-receivers"
                self.yang_parent_name = "mdt-subscription"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.address = YLeaf(YType.str, "address")

                self.port = YLeaf(YType.uint16, "port")

                self.protocol = YLeaf(YType.str, "protocol")
                self._segment_path = lambda: "mdt-receivers" + "[address='" + self.address.get() + "']" + "[port='" + self.port.get() + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(MdtSubscriptions.MdtSubscription.MdtReceivers, ['address', 'port', 'protocol'], name, value)

    def clone_ptr(self):
        self._top_entity = MdtSubscriptions()
        return self._top_entity

