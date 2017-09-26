""" CISCO_RADIUS_EXT_MIB 

This MIB module defines objects describing RADIUS (Remote
Access Dialin User Service), serving as an extension of the
following MIB modules\: 
\- 
    \- RADIUS\-AUTH\-CLIENT\-MIB [RFC4668] 
    \- RADIUS\-AUTH\-SERVER\-MIB [RFC4669] 
    \- RADIUS\-ACC\-CLIENT\-MIB [RFC4670] 
    \- RADIUS\-ACC\-SERVER\-MIB [RFC4671] 
    \- RADIUS\-DYNAUTH\-CLIENT\-MIB [RFC4672] 
    \- RADIUS\-DYNAUTH\-SERVER\-MIB [RFC4673] 
\- 
[RFC4668] D. Nelson, RADIUS Authentication Client MIB for IPv6,

RFC\-4668, August 2006. 
\- 
[RFC4669] D. Nelson, RADIUS Authentication Server MIB for IPv6,

RFC\-4669, August 2006. 
\- 
[RFC4670] D. Nelson, RADIUS Accounting Client MIB for IPv6,
RFC\-4670, August 2006. 
\- 
[RFC4671] D. Nelson, RADIUS Accounting Server MIB for IPv6,
RFC\-4671, August 2006. 
\- 
[RFC4672] S. De Cnodder, N. Jonnala, M. Chiba, RADIUS Dynamic 
Authorization Client MIB, RFC\-4672, September 2006. 
\- 
[RFC4673] S. De Cnodder, N. Jonnala, M. Chiba, RADIUS Dynamic 
Authorization Server MIB, RFC\-4673, September 2006.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCORADIUSEXTMIB(Entity):
    """
    
    
    .. attribute:: creclientaccounting
    
    	
    	**type**\:   :py:class:`Creclientaccounting <ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB.CISCORADIUSEXTMIB.Creclientaccounting>`
    
    .. attribute:: creclientauthentication
    
    	
    	**type**\:   :py:class:`Creclientauthentication <ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB.CISCORADIUSEXTMIB.Creclientauthentication>`
    
    .. attribute:: creclientglobal
    
    	
    	**type**\:   :py:class:`Creclientglobal <ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB.CISCORADIUSEXTMIB.Creclientglobal>`
    
    

    """

    _prefix = 'CISCO-RADIUS-EXT-MIB'
    _revision = '2010-05-25'

    def __init__(self):
        super(CISCORADIUSEXTMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-RADIUS-EXT-MIB"
        self.yang_parent_name = "CISCO-RADIUS-EXT-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"creClientAccounting" : ("creclientaccounting", CISCORADIUSEXTMIB.Creclientaccounting), "creClientAuthentication" : ("creclientauthentication", CISCORADIUSEXTMIB.Creclientauthentication), "creClientGlobal" : ("creclientglobal", CISCORADIUSEXTMIB.Creclientglobal)}
        self._child_list_classes = {}

        self.creclientaccounting = CISCORADIUSEXTMIB.Creclientaccounting()
        self.creclientaccounting.parent = self
        self._children_name_map["creclientaccounting"] = "creClientAccounting"
        self._children_yang_names.add("creClientAccounting")

        self.creclientauthentication = CISCORADIUSEXTMIB.Creclientauthentication()
        self.creclientauthentication.parent = self
        self._children_name_map["creclientauthentication"] = "creClientAuthentication"
        self._children_yang_names.add("creClientAuthentication")

        self.creclientglobal = CISCORADIUSEXTMIB.Creclientglobal()
        self.creclientglobal.parent = self
        self._children_name_map["creclientglobal"] = "creClientGlobal"
        self._children_yang_names.add("creClientGlobal")
        self._segment_path = lambda: "CISCO-RADIUS-EXT-MIB:CISCO-RADIUS-EXT-MIB"


    class Creclientaccounting(Entity):
        """
        
        
        .. attribute:: creacctclientaverageresponsedelay
        
        	This object indicates the average response delay experienced for RADIUS accounting
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: creacctclientbadauthenticators
        
        	This object indicates the number of RADIUS Accounting\-Response packets received with invalid authenticators
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclientbufferallocfailures
        
        	This object indicates the number of buffer allocation failures encountered for RADIUS accounting request
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: buffer failures
        
        .. attribute:: creacctclientdupids
        
        	This object indicates the number of times client has received duplicate accounting responses with the same identifier.  Out of these two packets, the later packet is considered as a true match
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclientlastusedsourceid
        
        	This MIB object indicates the last source identifier that was used to send out a RADIUS accounting request when 'extended RADIUS source ports' is configured.  The source identifier is a counter that is incremented everytime a RADIUS accounting request is sent
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: creacctclientmalformedresponses
        
        	This object indicates the number of malformed RADIUS accounting responses received.  Malformed packets include packets with an invalid length
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclientmaxbuffersize
        
        	This object indicates the maximum buffer size for RADIUS accounting packets
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: bytes
        
        .. attribute:: creacctclientmaxresponsedelay
        
        	This object indicates the maximum delay experienced for RADIUS accounting
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: creacctclienttimeouts
        
        	This object indicates the number of timeouts that have occurred for RADIUS accounting.  After a timeout the client may retry sending the request to the same server or to a different server or give up depending on the configuration
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: timeouts
        
        .. attribute:: creacctclienttotalpacketswithoutresponses
        
        	This object indicates the number of RADIUS accounting packets that never received a response
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclienttotalpacketswithresponses
        
        	This object indicates the number of RADIUS accounting packets that received responses
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclienttotalresponses
        
        	This object indicates the number of RADIUS accounting response packets received by the RADIUS client
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclientunknownresponses
        
        	This object indicates the number of unknown RADIUS accounting responses received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        

        """

        _prefix = 'CISCO-RADIUS-EXT-MIB'
        _revision = '2010-05-25'

        def __init__(self):
            super(CISCORADIUSEXTMIB.Creclientaccounting, self).__init__()

            self.yang_name = "creClientAccounting"
            self.yang_parent_name = "CISCO-RADIUS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.creacctclientaverageresponsedelay = YLeaf(YType.int32, "creAcctClientAverageResponseDelay")

            self.creacctclientbadauthenticators = YLeaf(YType.uint32, "creAcctClientBadAuthenticators")

            self.creacctclientbufferallocfailures = YLeaf(YType.uint32, "creAcctClientBufferAllocFailures")

            self.creacctclientdupids = YLeaf(YType.uint32, "creAcctClientDupIDs")

            self.creacctclientlastusedsourceid = YLeaf(YType.uint32, "creAcctClientLastUsedSourceId")

            self.creacctclientmalformedresponses = YLeaf(YType.uint32, "creAcctClientMalformedResponses")

            self.creacctclientmaxbuffersize = YLeaf(YType.uint32, "creAcctClientMaxBufferSize")

            self.creacctclientmaxresponsedelay = YLeaf(YType.int32, "creAcctClientMaxResponseDelay")

            self.creacctclienttimeouts = YLeaf(YType.uint32, "creAcctClientTimeouts")

            self.creacctclienttotalpacketswithoutresponses = YLeaf(YType.uint32, "creAcctClientTotalPacketsWithoutResponses")

            self.creacctclienttotalpacketswithresponses = YLeaf(YType.uint32, "creAcctClientTotalPacketsWithResponses")

            self.creacctclienttotalresponses = YLeaf(YType.uint32, "creAcctClientTotalResponses")

            self.creacctclientunknownresponses = YLeaf(YType.uint32, "creAcctClientUnknownResponses")
            self._segment_path = lambda: "creClientAccounting"
            self._absolute_path = lambda: "CISCO-RADIUS-EXT-MIB:CISCO-RADIUS-EXT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORADIUSEXTMIB.Creclientaccounting, ['creacctclientaverageresponsedelay', 'creacctclientbadauthenticators', 'creacctclientbufferallocfailures', 'creacctclientdupids', 'creacctclientlastusedsourceid', 'creacctclientmalformedresponses', 'creacctclientmaxbuffersize', 'creacctclientmaxresponsedelay', 'creacctclienttimeouts', 'creacctclienttotalpacketswithoutresponses', 'creacctclienttotalpacketswithresponses', 'creacctclienttotalresponses', 'creacctclientunknownresponses'], name, value)


    class Creclientauthentication(Entity):
        """
        
        
        .. attribute:: creauthclientaverageresponsedelay
        
        	This object indicates the average response delay experienced for RADIUS authentication requests
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: creauthclientbadauthenticators
        
        	This object indicates the number of RADIUS authentication response packets received which contained invalid authenticators
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclientbufferallocfailures
        
        	This object indicates the number of buffer allocation failures encountered during RADIUS request formation
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: buffer failures
        
        .. attribute:: creauthclientdupids
        
        	This object indicates the number of times client has received duplicate authentication responses with the same identifier.  Out of these two packets, the later packet is considered as a true match
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclientlastusedsourceid
        
        	This MIB object indicates the last source identifier that was used to send out a RADIUS authentication request when 'extended RADIUS source ports' is configured.  The source identifier is a counter that is incremented everytime a RADIUS authentication request is sent
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: creauthclientmalformedresponses
        
        	This object indicates the number of malformed RADIUS authentication responses received.  Malformed packets include packets with an invalid length
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclientmaxbuffersize
        
        	This object indicates the maximum buffer size for RADIUS authentication packet
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: bytes
        
        .. attribute:: creauthclientmaxresponsedelay
        
        	This object indicates the maximum delay experienced for RADIUS authentication requests
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: creauthclienttimeouts
        
        	This object indicates the number of timeouts that have occurred for RADIUS authentication.  After a timeout the client may retry sending the request to the same server or to a different server or give up depending on the configuration
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: timeouts
        
        .. attribute:: creauthclienttotalpacketswithoutresponses
        
        	This object indicates the number of RADIUS authentication packets that never received a response
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclienttotalpacketswithresponses
        
        	This object indicates the number of RADIUS authentication packets that received responses
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclienttotalresponses
        
        	This object indicates the number of RADIUS authentication response packets received by the RADIUS client
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclientunknownresponses
        
        	This object indicates the number of unknown RADIUS authentication responses received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        

        """

        _prefix = 'CISCO-RADIUS-EXT-MIB'
        _revision = '2010-05-25'

        def __init__(self):
            super(CISCORADIUSEXTMIB.Creclientauthentication, self).__init__()

            self.yang_name = "creClientAuthentication"
            self.yang_parent_name = "CISCO-RADIUS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.creauthclientaverageresponsedelay = YLeaf(YType.int32, "creAuthClientAverageResponseDelay")

            self.creauthclientbadauthenticators = YLeaf(YType.uint32, "creAuthClientBadAuthenticators")

            self.creauthclientbufferallocfailures = YLeaf(YType.uint32, "creAuthClientBufferAllocFailures")

            self.creauthclientdupids = YLeaf(YType.uint32, "creAuthClientDupIDs")

            self.creauthclientlastusedsourceid = YLeaf(YType.uint32, "creAuthClientLastUsedSourceId")

            self.creauthclientmalformedresponses = YLeaf(YType.uint32, "creAuthClientMalformedResponses")

            self.creauthclientmaxbuffersize = YLeaf(YType.uint32, "creAuthClientMaxBufferSize")

            self.creauthclientmaxresponsedelay = YLeaf(YType.int32, "creAuthClientMaxResponseDelay")

            self.creauthclienttimeouts = YLeaf(YType.uint32, "creAuthClientTimeouts")

            self.creauthclienttotalpacketswithoutresponses = YLeaf(YType.uint32, "creAuthClientTotalPacketsWithoutResponses")

            self.creauthclienttotalpacketswithresponses = YLeaf(YType.uint32, "creAuthClientTotalPacketsWithResponses")

            self.creauthclienttotalresponses = YLeaf(YType.uint32, "creAuthClientTotalResponses")

            self.creauthclientunknownresponses = YLeaf(YType.uint32, "creAuthClientUnknownResponses")
            self._segment_path = lambda: "creClientAuthentication"
            self._absolute_path = lambda: "CISCO-RADIUS-EXT-MIB:CISCO-RADIUS-EXT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORADIUSEXTMIB.Creclientauthentication, ['creauthclientaverageresponsedelay', 'creauthclientbadauthenticators', 'creauthclientbufferallocfailures', 'creauthclientdupids', 'creauthclientlastusedsourceid', 'creauthclientmalformedresponses', 'creauthclientmaxbuffersize', 'creauthclientmaxresponsedelay', 'creauthclienttimeouts', 'creauthclienttotalpacketswithoutresponses', 'creauthclienttotalpacketswithresponses', 'creauthclienttotalresponses', 'creauthclientunknownresponses'], name, value)


    class Creclientglobal(Entity):
        """
        
        
        .. attribute:: creclientlastusedsourceid
        
        	This MIB object indicates the last source identifier that was used to send out a RADIUS packet when 'extended RADIUS source ports' is configured.  The source identifier is a counter that is incremented everytime a RADIUS authentication or an accounting packet is sent
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: creclientlastusedsourceport
        
        	If the 'extended RADIUS source ports' is configured, multiple source ports are used for sending out RADIUS authentication or accounting requests.  This MIB object indicates the last source port that was used to send out a RADIUS authentication or accounting request
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: creclientsourceportrangeend
        
        	If the 'extended RADIUS source port' is configured, multiple source ports are used for sending out RADIUS authentication or accounting requests.  This MIB object indicates the port value where this range ends
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: creclientsourceportrangestart
        
        	If the 'extended RADIUS source ports' is configured, multiple source ports are used for sending out RADIUS authentication or accounting requests.  This MIB object indicates the port value from where this range starts
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: creclienttotalaccessrejects
        
        	This object indicates the number of access reject packets received by the RADIUS client
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creclienttotalaverageresponsedelay
        
        	This object indicates the overall response delay experienced by RADIUS packets (both authentication and accounting)
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: creclienttotalmaxdoneqlength
        
        	This object indicates the maximum length of the queue which stores those RADIUS packets for which the responses are received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creclienttotalmaxinqlength
        
        	This object indicates the maximum length of the queue which stores the incoming RADIUS packets
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        .. attribute:: creclienttotalmaxwaitqlength
        
        	This object indicates the maximum length of the queue which stores the pending RADIUS packets for which the responses are outstanding
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: RADIUS packets
        
        

        """

        _prefix = 'CISCO-RADIUS-EXT-MIB'
        _revision = '2010-05-25'

        def __init__(self):
            super(CISCORADIUSEXTMIB.Creclientglobal, self).__init__()

            self.yang_name = "creClientGlobal"
            self.yang_parent_name = "CISCO-RADIUS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.creclientlastusedsourceid = YLeaf(YType.uint32, "creClientLastUsedSourceId")

            self.creclientlastusedsourceport = YLeaf(YType.uint16, "creClientLastUsedSourcePort")

            self.creclientsourceportrangeend = YLeaf(YType.uint16, "creClientSourcePortRangeEnd")

            self.creclientsourceportrangestart = YLeaf(YType.uint16, "creClientSourcePortRangeStart")

            self.creclienttotalaccessrejects = YLeaf(YType.uint32, "creClientTotalAccessRejects")

            self.creclienttotalaverageresponsedelay = YLeaf(YType.int32, "creClientTotalAverageResponseDelay")

            self.creclienttotalmaxdoneqlength = YLeaf(YType.uint32, "creClientTotalMaxDoneQLength")

            self.creclienttotalmaxinqlength = YLeaf(YType.uint32, "creClientTotalMaxInQLength")

            self.creclienttotalmaxwaitqlength = YLeaf(YType.uint32, "creClientTotalMaxWaitQLength")
            self._segment_path = lambda: "creClientGlobal"
            self._absolute_path = lambda: "CISCO-RADIUS-EXT-MIB:CISCO-RADIUS-EXT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORADIUSEXTMIB.Creclientglobal, ['creclientlastusedsourceid', 'creclientlastusedsourceport', 'creclientsourceportrangeend', 'creclientsourceportrangestart', 'creclienttotalaccessrejects', 'creclienttotalaverageresponsedelay', 'creclienttotalmaxdoneqlength', 'creclienttotalmaxinqlength', 'creclienttotalmaxwaitqlength'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCORADIUSEXTMIB()
        return self._top_entity

