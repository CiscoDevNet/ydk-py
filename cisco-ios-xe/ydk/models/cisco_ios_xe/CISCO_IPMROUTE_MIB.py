""" CISCO_IPMROUTE_MIB 

The MIB module for management of IP Multicast routing,
but independent of the specific multicast routing protocol
in use.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOIPMROUTEMIB(Entity):
    """
    
    
    .. attribute:: ciscoipmroute
    
    	
    	**type**\:  :py:class:`Ciscoipmroute <ydk.models.cisco_ios_xe.CISCO_IPMROUTE_MIB.CISCOIPMROUTEMIB.Ciscoipmroute>`
    
    .. attribute:: ciscoipmrouteheartbeattable
    
    	The (conceptual) table listing sets of IP Multicast heartbeat parameters.  If no IP Multicast heartbeat is configured, this table would be empty
    	**type**\:  :py:class:`Ciscoipmrouteheartbeattable <ydk.models.cisco_ios_xe.CISCO_IPMROUTE_MIB.CISCOIPMROUTEMIB.Ciscoipmrouteheartbeattable>`
    
    

    """

    _prefix = 'CISCO-IPMROUTE-MIB'
    _revision = '2005-03-07'

    def __init__(self):
        super(CISCOIPMROUTEMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IPMROUTE-MIB"
        self.yang_parent_name = "CISCO-IPMROUTE-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ciscoIpMRoute", ("ciscoipmroute", CISCOIPMROUTEMIB.Ciscoipmroute)), ("ciscoIpMRouteHeartBeatTable", ("ciscoipmrouteheartbeattable", CISCOIPMROUTEMIB.Ciscoipmrouteheartbeattable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ciscoipmroute = CISCOIPMROUTEMIB.Ciscoipmroute()
        self.ciscoipmroute.parent = self
        self._children_name_map["ciscoipmroute"] = "ciscoIpMRoute"
        self._children_yang_names.add("ciscoIpMRoute")

        self.ciscoipmrouteheartbeattable = CISCOIPMROUTEMIB.Ciscoipmrouteheartbeattable()
        self.ciscoipmrouteheartbeattable.parent = self
        self._children_name_map["ciscoipmrouteheartbeattable"] = "ciscoIpMRouteHeartBeatTable"
        self._children_yang_names.add("ciscoIpMRouteHeartBeatTable")
        self._segment_path = lambda: "CISCO-IPMROUTE-MIB:CISCO-IPMROUTE-MIB"


    class Ciscoipmroute(Entity):
        """
        
        
        .. attribute:: ciscoipmroutenumberofentries
        
        	Maintains a count of the number of entries in the ipMRouteTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-IPMROUTE-MIB'
        _revision = '2005-03-07'

        def __init__(self):
            super(CISCOIPMROUTEMIB.Ciscoipmroute, self).__init__()

            self.yang_name = "ciscoIpMRoute"
            self.yang_parent_name = "CISCO-IPMROUTE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ciscoipmroutenumberofentries', YLeaf(YType.uint32, 'ciscoIpMRouteNumberOfEntries')),
            ])
            self.ciscoipmroutenumberofentries = None
            self._segment_path = lambda: "ciscoIpMRoute"
            self._absolute_path = lambda: "CISCO-IPMROUTE-MIB:CISCO-IPMROUTE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPMROUTEMIB.Ciscoipmroute, ['ciscoipmroutenumberofentries'], name, value)


    class Ciscoipmrouteheartbeattable(Entity):
        """
        The (conceptual) table listing sets of IP Multicast
        heartbeat parameters.  If no IP Multicast heartbeat is
        configured, this table would be empty.
        
        .. attribute:: ciscoipmrouteheartbeatentry
        
        	An entry (conceptual row) representing a set of IP Multicast heartbeat parameters
        	**type**\: list of  		 :py:class:`Ciscoipmrouteheartbeatentry <ydk.models.cisco_ios_xe.CISCO_IPMROUTE_MIB.CISCOIPMROUTEMIB.Ciscoipmrouteheartbeattable.Ciscoipmrouteheartbeatentry>`
        
        

        """

        _prefix = 'CISCO-IPMROUTE-MIB'
        _revision = '2005-03-07'

        def __init__(self):
            super(CISCOIPMROUTEMIB.Ciscoipmrouteheartbeattable, self).__init__()

            self.yang_name = "ciscoIpMRouteHeartBeatTable"
            self.yang_parent_name = "CISCO-IPMROUTE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ciscoIpMRouteHeartBeatEntry", ("ciscoipmrouteheartbeatentry", CISCOIPMROUTEMIB.Ciscoipmrouteheartbeattable.Ciscoipmrouteheartbeatentry))])
            self._leafs = OrderedDict()

            self.ciscoipmrouteheartbeatentry = YList(self)
            self._segment_path = lambda: "ciscoIpMRouteHeartBeatTable"
            self._absolute_path = lambda: "CISCO-IPMROUTE-MIB:CISCO-IPMROUTE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPMROUTEMIB.Ciscoipmrouteheartbeattable, [], name, value)


        class Ciscoipmrouteheartbeatentry(Entity):
            """
            An entry (conceptual row) representing a set of IP
            Multicast heartbeat parameters.
            
            .. attribute:: ciscoipmrouteheartbeatgroupaddr  (key)
            
            	Multicast group address used to receive heartbeat packets
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ciscoipmrouteheartbeatsourceaddr
            
            	Source address of the last multicast heartbeat packet received
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ciscoipmrouteheartbeatinterval
            
            	Number of seconds in which a Cisco multicast router expects a valid heartBeat packet from a source.  This value must be a multiple of 10
            	**type**\: int
            
            	**range:** 10..3600
            
            	**units**\: seconds
            
            .. attribute:: ciscoipmrouteheartbeatwindowsize
            
            	Number of ciscoIpMRouteHeartBeatInterval intervals a Cisco multicast router waits before checking if expected number of heartbeat packets are received or not
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: ciscoipmrouteheartbeatcount
            
            	Number of time intervals where multicast packets were received in the last ciscoIpMRouteHeartBeatWindowSize intervals
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoipmrouteheartbeatminimum
            
            	The minimal number of heartbeat packets expected in the last ciscoIpMRouteHeartBeatWindowSize intervals. If ciscoIpMRouteHeartBeatCount falls below this value, an SNMP trap/notification, if configured, will be sent to the NMS
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: ciscoipmrouteheartbeatalerttime
            
            	The value of sysUpTime on the most recent occasion at which a missing IP multicast heartbeat condition occured for the group address specified in this entry.  If no such condition have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoipmrouteheartbeatstatus
            
            	This object is used to create a new row or delete an existing row in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-IPMROUTE-MIB'
            _revision = '2005-03-07'

            def __init__(self):
                super(CISCOIPMROUTEMIB.Ciscoipmrouteheartbeattable.Ciscoipmrouteheartbeatentry, self).__init__()

                self.yang_name = "ciscoIpMRouteHeartBeatEntry"
                self.yang_parent_name = "ciscoIpMRouteHeartBeatTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciscoipmrouteheartbeatgroupaddr']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciscoipmrouteheartbeatgroupaddr', YLeaf(YType.str, 'ciscoIpMRouteHeartBeatGroupAddr')),
                    ('ciscoipmrouteheartbeatsourceaddr', YLeaf(YType.str, 'ciscoIpMRouteHeartBeatSourceAddr')),
                    ('ciscoipmrouteheartbeatinterval', YLeaf(YType.int32, 'ciscoIpMRouteHeartBeatInterval')),
                    ('ciscoipmrouteheartbeatwindowsize', YLeaf(YType.int32, 'ciscoIpMRouteHeartBeatWindowSize')),
                    ('ciscoipmrouteheartbeatcount', YLeaf(YType.uint32, 'ciscoIpMRouteHeartBeatCount')),
                    ('ciscoipmrouteheartbeatminimum', YLeaf(YType.int32, 'ciscoIpMRouteHeartBeatMinimum')),
                    ('ciscoipmrouteheartbeatalerttime', YLeaf(YType.uint32, 'ciscoIpMRouteHeartBeatAlertTime')),
                    ('ciscoipmrouteheartbeatstatus', YLeaf(YType.enumeration, 'ciscoIpMRouteHeartBeatStatus')),
                ])
                self.ciscoipmrouteheartbeatgroupaddr = None
                self.ciscoipmrouteheartbeatsourceaddr = None
                self.ciscoipmrouteheartbeatinterval = None
                self.ciscoipmrouteheartbeatwindowsize = None
                self.ciscoipmrouteheartbeatcount = None
                self.ciscoipmrouteheartbeatminimum = None
                self.ciscoipmrouteheartbeatalerttime = None
                self.ciscoipmrouteheartbeatstatus = None
                self._segment_path = lambda: "ciscoIpMRouteHeartBeatEntry" + "[ciscoIpMRouteHeartBeatGroupAddr='" + str(self.ciscoipmrouteheartbeatgroupaddr) + "']"
                self._absolute_path = lambda: "CISCO-IPMROUTE-MIB:CISCO-IPMROUTE-MIB/ciscoIpMRouteHeartBeatTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPMROUTEMIB.Ciscoipmrouteheartbeattable.Ciscoipmrouteheartbeatentry, ['ciscoipmrouteheartbeatgroupaddr', 'ciscoipmrouteheartbeatsourceaddr', 'ciscoipmrouteheartbeatinterval', 'ciscoipmrouteheartbeatwindowsize', 'ciscoipmrouteheartbeatcount', 'ciscoipmrouteheartbeatminimum', 'ciscoipmrouteheartbeatalerttime', 'ciscoipmrouteheartbeatstatus'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOIPMROUTEMIB()
        return self._top_entity

