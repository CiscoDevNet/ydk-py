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
    
    	
    	**type**\:  :py:class:`CiscoIpMRoute <ydk.models.cisco_ios_xe.CISCO_IPMROUTE_MIB.CISCOIPMROUTEMIB.CiscoIpMRoute>`
    
    	**config**\: False
    
    .. attribute:: ciscoipmrouteheartbeattable
    
    	The (conceptual) table listing sets of IP Multicast heartbeat parameters.  If no IP Multicast heartbeat is configured, this table would be empty
    	**type**\:  :py:class:`CiscoIpMRouteHeartBeatTable <ydk.models.cisco_ios_xe.CISCO_IPMROUTE_MIB.CISCOIPMROUTEMIB.CiscoIpMRouteHeartBeatTable>`
    
    	**config**\: False
    
    

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
        self._child_classes = OrderedDict([("ciscoIpMRoute", ("ciscoipmroute", CISCOIPMROUTEMIB.CiscoIpMRoute)), ("ciscoIpMRouteHeartBeatTable", ("ciscoipmrouteheartbeattable", CISCOIPMROUTEMIB.CiscoIpMRouteHeartBeatTable))])
        self._leafs = OrderedDict()

        self.ciscoipmroute = CISCOIPMROUTEMIB.CiscoIpMRoute()
        self.ciscoipmroute.parent = self
        self._children_name_map["ciscoipmroute"] = "ciscoIpMRoute"

        self.ciscoipmrouteheartbeattable = CISCOIPMROUTEMIB.CiscoIpMRouteHeartBeatTable()
        self.ciscoipmrouteheartbeattable.parent = self
        self._children_name_map["ciscoipmrouteheartbeattable"] = "ciscoIpMRouteHeartBeatTable"
        self._segment_path = lambda: "CISCO-IPMROUTE-MIB:CISCO-IPMROUTE-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOIPMROUTEMIB, [], name, value)


    class CiscoIpMRoute(Entity):
        """
        
        
        .. attribute:: ciscoipmroutenumberofentries
        
        	Maintains a count of the number of entries in the ipMRouteTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IPMROUTE-MIB'
        _revision = '2005-03-07'

        def __init__(self):
            super(CISCOIPMROUTEMIB.CiscoIpMRoute, self).__init__()

            self.yang_name = "ciscoIpMRoute"
            self.yang_parent_name = "CISCO-IPMROUTE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ciscoipmroutenumberofentries', (YLeaf(YType.uint32, 'ciscoIpMRouteNumberOfEntries'), ['int'])),
            ])
            self.ciscoipmroutenumberofentries = None
            self._segment_path = lambda: "ciscoIpMRoute"
            self._absolute_path = lambda: "CISCO-IPMROUTE-MIB:CISCO-IPMROUTE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPMROUTEMIB.CiscoIpMRoute, ['ciscoipmroutenumberofentries'], name, value)



    class CiscoIpMRouteHeartBeatTable(Entity):
        """
        The (conceptual) table listing sets of IP Multicast
        heartbeat parameters.  If no IP Multicast heartbeat is
        configured, this table would be empty.
        
        .. attribute:: ciscoipmrouteheartbeatentry
        
        	An entry (conceptual row) representing a set of IP Multicast heartbeat parameters
        	**type**\: list of  		 :py:class:`CiscoIpMRouteHeartBeatEntry <ydk.models.cisco_ios_xe.CISCO_IPMROUTE_MIB.CISCOIPMROUTEMIB.CiscoIpMRouteHeartBeatTable.CiscoIpMRouteHeartBeatEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IPMROUTE-MIB'
        _revision = '2005-03-07'

        def __init__(self):
            super(CISCOIPMROUTEMIB.CiscoIpMRouteHeartBeatTable, self).__init__()

            self.yang_name = "ciscoIpMRouteHeartBeatTable"
            self.yang_parent_name = "CISCO-IPMROUTE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ciscoIpMRouteHeartBeatEntry", ("ciscoipmrouteheartbeatentry", CISCOIPMROUTEMIB.CiscoIpMRouteHeartBeatTable.CiscoIpMRouteHeartBeatEntry))])
            self._leafs = OrderedDict()

            self.ciscoipmrouteheartbeatentry = YList(self)
            self._segment_path = lambda: "ciscoIpMRouteHeartBeatTable"
            self._absolute_path = lambda: "CISCO-IPMROUTE-MIB:CISCO-IPMROUTE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPMROUTEMIB.CiscoIpMRouteHeartBeatTable, [], name, value)


        class CiscoIpMRouteHeartBeatEntry(Entity):
            """
            An entry (conceptual row) representing a set of IP
            Multicast heartbeat parameters.
            
            .. attribute:: ciscoipmrouteheartbeatgroupaddr  (key)
            
            	Multicast group address used to receive heartbeat packets
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: ciscoipmrouteheartbeatsourceaddr
            
            	Source address of the last multicast heartbeat packet received
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: ciscoipmrouteheartbeatinterval
            
            	Number of seconds in which a Cisco multicast router expects a valid heartBeat packet from a source.  This value must be a multiple of 10
            	**type**\: int
            
            	**range:** 10..3600
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: ciscoipmrouteheartbeatwindowsize
            
            	Number of ciscoIpMRouteHeartBeatInterval intervals a Cisco multicast router waits before checking if expected number of heartbeat packets are received or not
            	**type**\: int
            
            	**range:** 1..100
            
            	**config**\: False
            
            .. attribute:: ciscoipmrouteheartbeatcount
            
            	Number of time intervals where multicast packets were received in the last ciscoIpMRouteHeartBeatWindowSize intervals
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ciscoipmrouteheartbeatminimum
            
            	The minimal number of heartbeat packets expected in the last ciscoIpMRouteHeartBeatWindowSize intervals. If ciscoIpMRouteHeartBeatCount falls below this value, an SNMP trap/notification, if configured, will be sent to the NMS
            	**type**\: int
            
            	**range:** 1..100
            
            	**config**\: False
            
            .. attribute:: ciscoipmrouteheartbeatalerttime
            
            	The value of sysUpTime on the most recent occasion at which a missing IP multicast heartbeat condition occured for the group address specified in this entry.  If no such condition have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ciscoipmrouteheartbeatstatus
            
            	This object is used to create a new row or delete an existing row in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IPMROUTE-MIB'
            _revision = '2005-03-07'

            def __init__(self):
                super(CISCOIPMROUTEMIB.CiscoIpMRouteHeartBeatTable.CiscoIpMRouteHeartBeatEntry, self).__init__()

                self.yang_name = "ciscoIpMRouteHeartBeatEntry"
                self.yang_parent_name = "ciscoIpMRouteHeartBeatTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciscoipmrouteheartbeatgroupaddr']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciscoipmrouteheartbeatgroupaddr', (YLeaf(YType.str, 'ciscoIpMRouteHeartBeatGroupAddr'), ['str'])),
                    ('ciscoipmrouteheartbeatsourceaddr', (YLeaf(YType.str, 'ciscoIpMRouteHeartBeatSourceAddr'), ['str'])),
                    ('ciscoipmrouteheartbeatinterval', (YLeaf(YType.int32, 'ciscoIpMRouteHeartBeatInterval'), ['int'])),
                    ('ciscoipmrouteheartbeatwindowsize', (YLeaf(YType.int32, 'ciscoIpMRouteHeartBeatWindowSize'), ['int'])),
                    ('ciscoipmrouteheartbeatcount', (YLeaf(YType.uint32, 'ciscoIpMRouteHeartBeatCount'), ['int'])),
                    ('ciscoipmrouteheartbeatminimum', (YLeaf(YType.int32, 'ciscoIpMRouteHeartBeatMinimum'), ['int'])),
                    ('ciscoipmrouteheartbeatalerttime', (YLeaf(YType.uint32, 'ciscoIpMRouteHeartBeatAlertTime'), ['int'])),
                    ('ciscoipmrouteheartbeatstatus', (YLeaf(YType.enumeration, 'ciscoIpMRouteHeartBeatStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPMROUTEMIB.CiscoIpMRouteHeartBeatTable.CiscoIpMRouteHeartBeatEntry, ['ciscoipmrouteheartbeatgroupaddr', 'ciscoipmrouteheartbeatsourceaddr', 'ciscoipmrouteheartbeatinterval', 'ciscoipmrouteheartbeatwindowsize', 'ciscoipmrouteheartbeatcount', 'ciscoipmrouteheartbeatminimum', 'ciscoipmrouteheartbeatalerttime', 'ciscoipmrouteheartbeatstatus'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOIPMROUTEMIB()
        return self._top_entity



