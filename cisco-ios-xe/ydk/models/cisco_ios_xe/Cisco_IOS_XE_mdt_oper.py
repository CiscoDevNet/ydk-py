""" Cisco_IOS_XE_mdt_oper 

This module contains a collection of YANG 
definitions for operational data of streaming telemetry.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MdtConState(Enum):
    """
    MdtConState

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
    MdtReceiverState

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
    MdtSubState

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
    MdtSubType

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

    """

    sub_type_dynamic = Enum.YLeaf(1, "sub-type-dynamic")

    sub_type_static = Enum.YLeaf(2, "sub-type-static")



class MdtOperData(Entity):
    """
    MDT operational data.
    
    .. attribute:: mdt_streams
    
    	MDT streams table. The list of supported streams
    	**type**\:  :py:class:`MdtStreams <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtStreams>`
    
    .. attribute:: mdt_subscriptions
    
    	MDT subscription operational data
    	**type**\: list of  		 :py:class:`MdtSubscriptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtSubscriptions>`
    
    .. attribute:: mdt_connections
    
    	MDT subscription connection operational data
    	**type**\: list of  		 :py:class:`MdtConnections <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtConnections>`
    
    

    """

    _prefix = 'mdt-oper'
    _revision = '2017-07-01'

    def __init__(self):
        super(MdtOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "mdt-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-mdt-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"mdt-streams" : ("mdt_streams", MdtOperData.MdtStreams)}
        self._child_list_classes = {"mdt-subscriptions" : ("mdt_subscriptions", MdtOperData.MdtSubscriptions), "mdt-connections" : ("mdt_connections", MdtOperData.MdtConnections)}

        self.mdt_streams = MdtOperData.MdtStreams()
        self.mdt_streams.parent = self
        self._children_name_map["mdt_streams"] = "mdt-streams"
        self._children_yang_names.add("mdt-streams")

        self.mdt_subscriptions = YList(self)
        self.mdt_connections = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-mdt-oper:mdt-oper-data"

    def __setattr__(self, name, value):
        self._perform_setattr(MdtOperData, [], name, value)


    class MdtStreams(Entity):
        """
        MDT streams table. The list of supported streams.
        
        .. attribute:: stream
        
        	Name of a supported stream
        	**type**\: list of str
        
        

        """

        _prefix = 'mdt-oper'
        _revision = '2017-07-01'

        def __init__(self):
            super(MdtOperData.MdtStreams, self).__init__()

            self.yang_name = "mdt-streams"
            self.yang_parent_name = "mdt-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.stream = YLeafList(YType.str, "stream")
            self._segment_path = lambda: "mdt-streams"
            self._absolute_path = lambda: "Cisco-IOS-XE-mdt-oper:mdt-oper-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MdtOperData.MdtStreams, ['stream'], name, value)


    class MdtSubscriptions(Entity):
        """
        MDT subscription operational data.
        
        .. attribute:: subscription_id  <key>
        
        	Unique subscription identifier
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: base
        
        	Common subscription information
        	**type**\:  :py:class:`Base <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtSubscriptions.Base>`
        
        .. attribute:: type
        
        	Subscription type
        	**type**\:  :py:class:`MdtSubType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtSubType>`
        
        .. attribute:: state
        
        	Subscription state
        	**type**\:  :py:class:`MdtSubState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtSubState>`
        
        .. attribute:: comments
        
        	Comments related to subcription state
        	**type**\: str
        
        .. attribute:: updates_in
        
        	Number of updates received from sensors as candidates for notifications
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: updates_dampened
        
        	Number of updates dropped due to dampening
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: updates_dropped
        
        	Number of updates dropped to other causes
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: mdt_receivers
        
        	List of MDT receivers
        	**type**\: list of  		 :py:class:`MdtReceivers <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtSubscriptions.MdtReceivers>`
        
        

        """

        _prefix = 'mdt-oper'
        _revision = '2017-07-01'

        def __init__(self):
            super(MdtOperData.MdtSubscriptions, self).__init__()

            self.yang_name = "mdt-subscriptions"
            self.yang_parent_name = "mdt-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"base" : ("base", MdtOperData.MdtSubscriptions.Base)}
            self._child_list_classes = {"mdt-receivers" : ("mdt_receivers", MdtOperData.MdtSubscriptions.MdtReceivers)}

            self.subscription_id = YLeaf(YType.uint32, "subscription-id")

            self.type = YLeaf(YType.enumeration, "type")

            self.state = YLeaf(YType.enumeration, "state")

            self.comments = YLeaf(YType.str, "comments")

            self.updates_in = YLeaf(YType.uint64, "updates-in")

            self.updates_dampened = YLeaf(YType.uint64, "updates-dampened")

            self.updates_dropped = YLeaf(YType.uint64, "updates-dropped")

            self.base = MdtOperData.MdtSubscriptions.Base()
            self.base.parent = self
            self._children_name_map["base"] = "base"
            self._children_yang_names.add("base")

            self.mdt_receivers = YList(self)
            self._segment_path = lambda: "mdt-subscriptions" + "[subscription-id='" + self.subscription_id.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-mdt-oper:mdt-oper-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MdtOperData.MdtSubscriptions, ['subscription_id', 'type', 'state', 'comments', 'updates_in', 'updates_dampened', 'updates_dropped'], name, value)


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

            _prefix = 'mdt-oper'
            _revision = '2017-07-01'

            def __init__(self):
                super(MdtOperData.MdtSubscriptions.Base, self).__init__()

                self.yang_name = "base"
                self.yang_parent_name = "mdt-subscriptions"
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
                self._perform_setattr(MdtOperData.MdtSubscriptions.Base, ['stream', 'encoding', 'source_vrf', 'source_address', 'no_trigger', 'period', 'no_synch_on_start', 'no_filter', 'xpath', 'tdl_uri'], name, value)


        class MdtReceivers(Entity):
            """
            List of MDT receivers.
            
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
            
            .. attribute:: state
            
            	Receiver state
            	**type**\:  :py:class:`MdtReceiverState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtReceiverState>`
            
            .. attribute:: comments
            
            	Comments related to receiver state
            	**type**\: str
            
            

            """

            _prefix = 'mdt-oper'
            _revision = '2017-07-01'

            def __init__(self):
                super(MdtOperData.MdtSubscriptions.MdtReceivers, self).__init__()

                self.yang_name = "mdt-receivers"
                self.yang_parent_name = "mdt-subscriptions"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.address = YLeaf(YType.str, "address")

                self.port = YLeaf(YType.uint16, "port")

                self.protocol = YLeaf(YType.str, "protocol")

                self.state = YLeaf(YType.enumeration, "state")

                self.comments = YLeaf(YType.str, "comments")
                self._segment_path = lambda: "mdt-receivers" + "[address='" + self.address.get() + "']" + "[port='" + self.port.get() + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(MdtOperData.MdtSubscriptions.MdtReceivers, ['address', 'port', 'protocol', 'state', 'comments'], name, value)


    class MdtConnections(Entity):
        """
        MDT subscription connection operational data.
        
        .. attribute:: address  <key>
        
        	IP address
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: port  <key>
        
        	Network port
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: source_vrf  <key>
        
        	Network instance name for the VRF that the connection originates from
        	**type**\: str
        
        .. attribute:: source_address  <key>
        
        	The source address used for the connection
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: transport
        
        	Transport protocol on this connection See transport\-protocol from subscribed\-notifications for possible values
        	**type**\: str
        
        .. attribute:: peer_id
        
        	Identity of the peer at the other end of the connection. May be empty, depending on connection state
        	**type**\: str
        
        .. attribute:: state
        
        	Connection state
        	**type**\:  :py:class:`MdtConState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtConState>`
        
        .. attribute:: mdt_sub_con_stats
        
        	List of subscription specific statistics for this connection
        	**type**\: list of  		 :py:class:`MdtSubConStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtConnections.MdtSubConStats>`
        
        

        """

        _prefix = 'mdt-oper'
        _revision = '2017-07-01'

        def __init__(self):
            super(MdtOperData.MdtConnections, self).__init__()

            self.yang_name = "mdt-connections"
            self.yang_parent_name = "mdt-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"mdt-sub-con-stats" : ("mdt_sub_con_stats", MdtOperData.MdtConnections.MdtSubConStats)}

            self.address = YLeaf(YType.str, "address")

            self.port = YLeaf(YType.uint16, "port")

            self.source_vrf = YLeaf(YType.str, "source-vrf")

            self.source_address = YLeaf(YType.str, "source-address")

            self.transport = YLeaf(YType.str, "transport")

            self.peer_id = YLeaf(YType.str, "peer-id")

            self.state = YLeaf(YType.enumeration, "state")

            self.mdt_sub_con_stats = YList(self)
            self._segment_path = lambda: "mdt-connections" + "[address='" + self.address.get() + "']" + "[port='" + self.port.get() + "']" + "[source-vrf='" + self.source_vrf.get() + "']" + "[source-address='" + self.source_address.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-mdt-oper:mdt-oper-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MdtOperData.MdtConnections, ['address', 'port', 'source_vrf', 'source_address', 'transport', 'peer_id', 'state'], name, value)


        class MdtSubConStats(Entity):
            """
            List of subscription specific statistics for this
            connection.
            
            .. attribute:: sub_id  <key>
            
            	Subscription identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: updates_sent
            
            	Number of update notifications sent to the receiver using this subscription
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: updates_dropped
            
            	Number of dropped update notifications due to error or events not in other counters using this subscription
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'mdt-oper'
            _revision = '2017-07-01'

            def __init__(self):
                super(MdtOperData.MdtConnections.MdtSubConStats, self).__init__()

                self.yang_name = "mdt-sub-con-stats"
                self.yang_parent_name = "mdt-connections"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.sub_id = YLeaf(YType.uint32, "sub-id")

                self.updates_sent = YLeaf(YType.uint64, "updates-sent")

                self.updates_dropped = YLeaf(YType.uint64, "updates-dropped")
                self._segment_path = lambda: "mdt-sub-con-stats" + "[sub-id='" + self.sub_id.get() + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(MdtOperData.MdtConnections.MdtSubConStats, ['sub_id', 'updates_sent', 'updates_dropped'], name, value)

    def clone_ptr(self):
        self._top_entity = MdtOperData()
        return self._top_entity

