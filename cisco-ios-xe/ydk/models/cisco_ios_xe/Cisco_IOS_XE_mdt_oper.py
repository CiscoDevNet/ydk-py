""" Cisco_IOS_XE_mdt_oper 

This module contains a collection of YANG 
definitions for operational data of streaming telemetry.
Copyright (c) 2016\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MdtConState(Enum):
    """
    MdtConState (Enum Class)

    Connection states.

    .. data:: con_state_active = 0

    	The connection is active and usable.

    .. data:: con_state_connecting = 1

    	An attempt is being made to set the connection up.

    .. data:: con_state_pending = 2

    	The connection is down, but between connection

    	attempts. It is in this state, for example, during

    	the idle time between retries.

    .. data:: con_state_disconnecting = 3

    	The connection is the process of being disconnected.

    """

    con_state_active = Enum.YLeaf(0, "con-state-active")

    con_state_connecting = Enum.YLeaf(1, "con-state-connecting")

    con_state_pending = Enum.YLeaf(2, "con-state-pending")

    con_state_disconnecting = Enum.YLeaf(3, "con-state-disconnecting")


class MdtReceiverState(Enum):
    """
    MdtReceiverState (Enum Class)

    Receiver states.

    .. data:: rcvr_state_invalid = 1

    	The receiver configuration is invalid and

    	cannot be used.

    .. data:: rcvr_state_disconnected = 2

    	The receiver is disconnected and there is no

    	attempt being made to connect to it.

    .. data:: rcvr_state_connecting = 3

    	An attempt is being made to connect to the receiver.

    .. data:: rcvr_state_connected = 4

    	The receiver is connected, and update notifications

    	are being sent to the receiver when they occur

    """

    rcvr_state_invalid = Enum.YLeaf(1, "rcvr-state-invalid")

    rcvr_state_disconnected = Enum.YLeaf(2, "rcvr-state-disconnected")

    rcvr_state_connecting = Enum.YLeaf(3, "rcvr-state-connecting")

    rcvr_state_connected = Enum.YLeaf(4, "rcvr-state-connected")


class MdtSubState(Enum):
    """
    MdtSubState (Enum Class)

    Subscription states

    .. data:: sub_state_valid = 0

    	The subscription is valid and may be sending updates.

    .. data:: sub_state_suspended = 1

    	The subscription has been suspended and is not

    	sending notifications even if there are updates.

    .. data:: sub_state_terminated = 2

    	The subscription is terminated. This state is valid

    	only for static subscriptions.

    .. data:: sub_state_invalid = 3

    	The subscription is invalid. This state is valid

    	only for static subscriptions.

    """

    sub_state_valid = Enum.YLeaf(0, "sub-state-valid")

    sub_state_suspended = Enum.YLeaf(1, "sub-state-suspended")

    sub_state_terminated = Enum.YLeaf(2, "sub-state-terminated")

    sub_state_invalid = Enum.YLeaf(3, "sub-state-invalid")


class MdtSubType(Enum):
    """
    MdtSubType (Enum Class)

    Subscription types

    .. data:: sub_type_dynamic = 1

    	Dynamic subscriptions

    	-do not survive reboot

    	-existence tied to connection they are created on

    	-send updates only to peer that creates them

    .. data:: sub_type_static = 2

    	Static subscriptions

    	-created, (modified), and deleted by management operations

    	-survive reboot

    	-receivers are configured 

    .. data:: sub_type_permanent = 3

    	Permanent subscriptions

    	-created during system startup, can not be modified

    """

    sub_type_dynamic = Enum.YLeaf(1, "sub-type-dynamic")

    sub_type_static = Enum.YLeaf(2, "sub-type-static")

    sub_type_permanent = Enum.YLeaf(3, "sub-type-permanent")



class MdtOperData(Entity):
    """
    MDT operational data.
    
    .. attribute:: mdt_streams
    
    	MDT streams table. The list of supported streams
    	**type**\:  :py:class:`MdtStreams <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtStreams>`
    
    	**config**\: False
    
    .. attribute:: mdt_subscriptions
    
    	MDT subscription operational data
    	**type**\: list of  		 :py:class:`MdtSubscriptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtSubscriptions>`
    
    	**config**\: False
    
    .. attribute:: mdt_connections
    
    	MDT subscription connection operational data
    	**type**\: list of  		 :py:class:`MdtConnections <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtConnections>`
    
    	**config**\: False
    
    

    """

    _prefix = 'mdt-oper'
    _revision = '2018-03-06'

    def __init__(self):
        super(MdtOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "mdt-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-mdt-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("mdt-streams", ("mdt_streams", MdtOperData.MdtStreams)), ("mdt-subscriptions", ("mdt_subscriptions", MdtOperData.MdtSubscriptions)), ("mdt-connections", ("mdt_connections", MdtOperData.MdtConnections))])
        self._leafs = OrderedDict()

        self.mdt_streams = MdtOperData.MdtStreams()
        self.mdt_streams.parent = self
        self._children_name_map["mdt_streams"] = "mdt-streams"

        self.mdt_subscriptions = YList(self)
        self.mdt_connections = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-mdt-oper:mdt-oper-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MdtOperData, [], name, value)


    class MdtStreams(Entity):
        """
        MDT streams table. The list of supported streams.
        
        .. attribute:: stream
        
        	Name of a supported stream
        	**type**\: list of str
        
        	**config**\: False
        
        

        """

        _prefix = 'mdt-oper'
        _revision = '2018-03-06'

        def __init__(self):
            super(MdtOperData.MdtStreams, self).__init__()

            self.yang_name = "mdt-streams"
            self.yang_parent_name = "mdt-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('stream', (YLeafList(YType.str, 'stream'), ['str'])),
            ])
            self.stream = []
            self._segment_path = lambda: "mdt-streams"
            self._absolute_path = lambda: "Cisco-IOS-XE-mdt-oper:mdt-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MdtOperData.MdtStreams, ['stream'], name, value)



    class MdtSubscriptions(Entity):
        """
        MDT subscription operational data.
        
        .. attribute:: subscription_id  (key)
        
        	Unique subscription identifier
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: base
        
        	Common subscription information
        	**type**\:  :py:class:`Base <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtSubscriptions.Base>`
        
        	**config**\: False
        
        .. attribute:: type
        
        	Subscription type
        	**type**\:  :py:class:`MdtSubType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtSubType>`
        
        	**config**\: False
        
        .. attribute:: state
        
        	Subscription state
        	**type**\:  :py:class:`MdtSubState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtSubState>`
        
        	**config**\: False
        
        .. attribute:: comments
        
        	Comments related to subcription state
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: updates_in
        
        	Number of updates received from sensors as candidates for notifications
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: updates_dampened
        
        	Number of updates dropped due to dampening
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: updates_dropped
        
        	Number of updates dropped to other causes
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: mdt_receivers
        
        	List of MDT receivers
        	**type**\: list of  		 :py:class:`MdtReceivers <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtSubscriptions.MdtReceivers>`
        
        	**config**\: False
        
        

        """

        _prefix = 'mdt-oper'
        _revision = '2018-03-06'

        def __init__(self):
            super(MdtOperData.MdtSubscriptions, self).__init__()

            self.yang_name = "mdt-subscriptions"
            self.yang_parent_name = "mdt-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['subscription_id']
            self._child_classes = OrderedDict([("base", ("base", MdtOperData.MdtSubscriptions.Base)), ("mdt-receivers", ("mdt_receivers", MdtOperData.MdtSubscriptions.MdtReceivers))])
            self._leafs = OrderedDict([
                ('subscription_id', (YLeaf(YType.uint32, 'subscription-id'), ['int'])),
                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper', 'MdtSubType', '')])),
                ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper', 'MdtSubState', '')])),
                ('comments', (YLeaf(YType.str, 'comments'), ['str'])),
                ('updates_in', (YLeaf(YType.uint64, 'updates-in'), ['int'])),
                ('updates_dampened', (YLeaf(YType.uint64, 'updates-dampened'), ['int'])),
                ('updates_dropped', (YLeaf(YType.uint64, 'updates-dropped'), ['int'])),
            ])
            self.subscription_id = None
            self.type = None
            self.state = None
            self.comments = None
            self.updates_in = None
            self.updates_dampened = None
            self.updates_dropped = None

            self.base = MdtOperData.MdtSubscriptions.Base()
            self.base.parent = self
            self._children_name_map["base"] = "base"

            self.mdt_receivers = YList(self)
            self._segment_path = lambda: "mdt-subscriptions" + "[subscription-id='" + str(self.subscription_id) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-mdt-oper:mdt-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MdtOperData.MdtSubscriptions, ['subscription_id', 'type', 'state', 'comments', 'updates_in', 'updates_dampened', 'updates_dropped'], name, value)


        class Base(Entity):
            """
            Common subscription information.
            
            .. attribute:: stream
            
            	The name of the event stream being subscribed to
            	**type**\: str
            
            	**config**\: False
            
            	**default value**\: NETCONF
            
            .. attribute:: encoding
            
            	Update notification encoding
            	**type**\: str
            
            	**config**\: False
            
            	**default value**\: encode-xml
            
            .. attribute:: source_vrf
            
            	Network instance name for the VRF
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: source_address
            
            	The source address for the notifications
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: no_trigger
            
            	Placeholder for unset value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**default value**\: 0
            
            .. attribute:: period
            
            	Period of update notifications in 100ths of a second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            	**config**\: False
            
            	**units**\: centiseconds
            
            .. attribute:: no_synch_on_start
            
            	If true, there is no initial update notification with the current value of all the data. NOT CURRENTLY SUPPORTED. If specified, must be false
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: no_filter
            
            	Placeholder for unset value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**default value**\: 0
            
            .. attribute:: xpath
            
            	XPath expression describing the set of objects wanted as part of the subscription
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: tdl_uri
            
            	TDL\-URI expression describing the set of objects wanted as part of the subscription
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: transform_name
            
            	Transform name is the reference to  tdl transform scheme
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'mdt-oper'
            _revision = '2018-03-06'

            def __init__(self):
                super(MdtOperData.MdtSubscriptions.Base, self).__init__()

                self.yang_name = "base"
                self.yang_parent_name = "mdt-subscriptions"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stream', (YLeaf(YType.str, 'stream'), ['str'])),
                    ('encoding', (YLeaf(YType.str, 'encoding'), ['str'])),
                    ('source_vrf', (YLeaf(YType.str, 'source-vrf'), ['str'])),
                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                    ('no_trigger', (YLeaf(YType.uint32, 'no-trigger'), ['int'])),
                    ('period', (YLeaf(YType.uint32, 'period'), ['int'])),
                    ('no_synch_on_start', (YLeaf(YType.boolean, 'no-synch-on-start'), ['bool'])),
                    ('no_filter', (YLeaf(YType.uint32, 'no-filter'), ['int'])),
                    ('xpath', (YLeaf(YType.str, 'xpath'), ['str'])),
                    ('tdl_uri', (YLeaf(YType.str, 'tdl-uri'), ['str'])),
                    ('transform_name', (YLeaf(YType.str, 'transform-name'), ['str'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MdtOperData.MdtSubscriptions.Base, ['stream', 'encoding', 'source_vrf', 'source_address', 'no_trigger', 'period', 'no_synch_on_start', 'no_filter', 'xpath', 'tdl_uri', 'transform_name'], name, value)



        class MdtReceivers(Entity):
            """
            List of MDT receivers.
            
            .. attribute:: address  (key)
            
            	IP address of the receiver
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            	**mandatory**\: True
            
            	**config**\: False
            
            .. attribute:: port  (key)
            
            	Network port of the receiver
            	**type**\: int
            
            	**range:** 0..65535
            
            	**mandatory**\: True
            
            	**config**\: False
            
            .. attribute:: protocol
            
            	Receiver transport protocol
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: state
            
            	Receiver state
            	**type**\:  :py:class:`MdtReceiverState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtReceiverState>`
            
            	**config**\: False
            
            .. attribute:: comments
            
            	Comments related to receiver state
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: profile
            
            	Receiver's protocol profile name
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'mdt-oper'
            _revision = '2018-03-06'

            def __init__(self):
                super(MdtOperData.MdtSubscriptions.MdtReceivers, self).__init__()

                self.yang_name = "mdt-receivers"
                self.yang_parent_name = "mdt-subscriptions"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['address','port']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                    ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                    ('protocol', (YLeaf(YType.str, 'protocol'), ['str'])),
                    ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper', 'MdtReceiverState', '')])),
                    ('comments', (YLeaf(YType.str, 'comments'), ['str'])),
                    ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
                ])
                self.address = None
                self.port = None
                self.protocol = None
                self.state = None
                self.comments = None
                self.profile = None
                self._segment_path = lambda: "mdt-receivers" + "[address='" + str(self.address) + "']" + "[port='" + str(self.port) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MdtOperData.MdtSubscriptions.MdtReceivers, ['address', 'port', 'protocol', 'state', 'comments', 'profile'], name, value)




    class MdtConnections(Entity):
        """
        MDT subscription connection operational data.
        
        .. attribute:: address  (key)
        
        	IP address
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        	**config**\: False
        
        .. attribute:: port  (key)
        
        	Network port
        	**type**\: int
        
        	**range:** 0..65535
        
        	**config**\: False
        
        .. attribute:: source_vrf  (key)
        
        	Network instance name for the VRF that the connection originates from
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: source_address  (key)
        
        	The source address used for the connection
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        	**config**\: False
        
        .. attribute:: transport
        
        	Transport protocol on this connection See transport\-protocol from subscribed\-notifications for possible values
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: peer_id
        
        	Identity of the peer at the other end of the connection. May be empty, depending on connection state
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: state
        
        	Connection state
        	**type**\:  :py:class:`MdtConState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtConState>`
        
        	**config**\: False
        
        .. attribute:: mdt_sub_con_stats
        
        	List of subscription specific statistics for this connection
        	**type**\: list of  		 :py:class:`MdtSubConStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtConnections.MdtSubConStats>`
        
        	**config**\: False
        
        .. attribute:: profile
        
        	Protocol profile used with this connection
        	**type**\: str
        
        	**config**\: False
        
        

        """

        _prefix = 'mdt-oper'
        _revision = '2018-03-06'

        def __init__(self):
            super(MdtOperData.MdtConnections, self).__init__()

            self.yang_name = "mdt-connections"
            self.yang_parent_name = "mdt-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['address','port','source_vrf','source_address']
            self._child_classes = OrderedDict([("mdt-sub-con-stats", ("mdt_sub_con_stats", MdtOperData.MdtConnections.MdtSubConStats))])
            self._leafs = OrderedDict([
                ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                ('source_vrf', (YLeaf(YType.str, 'source-vrf'), ['str'])),
                ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                ('transport', (YLeaf(YType.str, 'transport'), ['str'])),
                ('peer_id', (YLeaf(YType.str, 'peer-id'), ['str'])),
                ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper', 'MdtConState', '')])),
                ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
            ])
            self.address = None
            self.port = None
            self.source_vrf = None
            self.source_address = None
            self.transport = None
            self.peer_id = None
            self.state = None
            self.profile = None

            self.mdt_sub_con_stats = YList(self)
            self._segment_path = lambda: "mdt-connections" + "[address='" + str(self.address) + "']" + "[port='" + str(self.port) + "']" + "[source-vrf='" + str(self.source_vrf) + "']" + "[source-address='" + str(self.source_address) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-mdt-oper:mdt-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MdtOperData.MdtConnections, ['address', 'port', 'source_vrf', 'source_address', 'transport', 'peer_id', 'state', 'profile'], name, value)


        class MdtSubConStats(Entity):
            """
            List of subscription specific statistics for this
            connection.
            
            .. attribute:: sub_id  (key)
            
            	Subscription identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: updates_sent
            
            	Number of update notifications sent to the receiver using this subscription
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: updates_dropped
            
            	Number of dropped update notifications due to error or events not in other counters using this subscription
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'mdt-oper'
            _revision = '2018-03-06'

            def __init__(self):
                super(MdtOperData.MdtConnections.MdtSubConStats, self).__init__()

                self.yang_name = "mdt-sub-con-stats"
                self.yang_parent_name = "mdt-connections"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['sub_id']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('sub_id', (YLeaf(YType.uint32, 'sub-id'), ['int'])),
                    ('updates_sent', (YLeaf(YType.uint64, 'updates-sent'), ['int'])),
                    ('updates_dropped', (YLeaf(YType.uint64, 'updates-dropped'), ['int'])),
                ])
                self.sub_id = None
                self.updates_sent = None
                self.updates_dropped = None
                self._segment_path = lambda: "mdt-sub-con-stats" + "[sub-id='" + str(self.sub_id) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MdtOperData.MdtConnections.MdtSubConStats, ['sub_id', 'updates_sent', 'updates_dropped'], name, value)



    def clone_ptr(self):
        self._top_entity = MdtOperData()
        return self._top_entity



