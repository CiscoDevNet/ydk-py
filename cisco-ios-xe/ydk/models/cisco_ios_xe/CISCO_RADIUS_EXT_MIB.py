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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCORADIUSEXTMIB(Entity):
    """
    
    
    .. attribute:: creclientglobal
    
    	
    	**type**\:  :py:class:`CreClientGlobal <ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB.CISCORADIUSEXTMIB.CreClientGlobal>`
    
    	**config**\: False
    
    .. attribute:: creclientauthentication
    
    	
    	**type**\:  :py:class:`CreClientAuthentication <ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB.CISCORADIUSEXTMIB.CreClientAuthentication>`
    
    	**config**\: False
    
    .. attribute:: creclientaccounting
    
    	
    	**type**\:  :py:class:`CreClientAccounting <ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB.CISCORADIUSEXTMIB.CreClientAccounting>`
    
    	**config**\: False
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("creClientGlobal", ("creclientglobal", CISCORADIUSEXTMIB.CreClientGlobal)), ("creClientAuthentication", ("creclientauthentication", CISCORADIUSEXTMIB.CreClientAuthentication)), ("creClientAccounting", ("creclientaccounting", CISCORADIUSEXTMIB.CreClientAccounting))])
        self._leafs = OrderedDict()

        self.creclientglobal = CISCORADIUSEXTMIB.CreClientGlobal()
        self.creclientglobal.parent = self
        self._children_name_map["creclientglobal"] = "creClientGlobal"

        self.creclientauthentication = CISCORADIUSEXTMIB.CreClientAuthentication()
        self.creclientauthentication.parent = self
        self._children_name_map["creclientauthentication"] = "creClientAuthentication"

        self.creclientaccounting = CISCORADIUSEXTMIB.CreClientAccounting()
        self.creclientaccounting.parent = self
        self._children_name_map["creclientaccounting"] = "creClientAccounting"
        self._segment_path = lambda: "CISCO-RADIUS-EXT-MIB:CISCO-RADIUS-EXT-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCORADIUSEXTMIB, [], name, value)


    class CreClientGlobal(Entity):
        """
        
        
        .. attribute:: creclienttotalmaxinqlength
        
        	This object indicates the maximum length of the queue which stores the incoming RADIUS packets
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creclienttotalmaxwaitqlength
        
        	This object indicates the maximum length of the queue which stores the pending RADIUS packets for which the responses are outstanding
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creclienttotalmaxdoneqlength
        
        	This object indicates the maximum length of the queue which stores those RADIUS packets for which the responses are received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creclienttotalaccessrejects
        
        	This object indicates the number of access reject packets received by the RADIUS client
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creclienttotalaverageresponsedelay
        
        	This object indicates the overall response delay experienced by RADIUS packets (both authentication and accounting)
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        .. attribute:: creclientsourceportrangestart
        
        	If the 'extended RADIUS source ports' is configured, multiple source ports are used for sending out RADIUS authentication or accounting requests.  This MIB object indicates the port value from where this range starts
        	**type**\: int
        
        	**range:** 0..65535
        
        	**config**\: False
        
        .. attribute:: creclientsourceportrangeend
        
        	If the 'extended RADIUS source port' is configured, multiple source ports are used for sending out RADIUS authentication or accounting requests.  This MIB object indicates the port value where this range ends
        	**type**\: int
        
        	**range:** 0..65535
        
        	**config**\: False
        
        .. attribute:: creclientlastusedsourceport
        
        	If the 'extended RADIUS source ports' is configured, multiple source ports are used for sending out RADIUS authentication or accounting requests.  This MIB object indicates the last source port that was used to send out a RADIUS authentication or accounting request
        	**type**\: int
        
        	**range:** 0..65535
        
        	**config**\: False
        
        .. attribute:: creclientlastusedsourceid
        
        	This MIB object indicates the last source identifier that was used to send out a RADIUS packet when 'extended RADIUS source ports' is configured.  The source identifier is a counter that is incremented everytime a RADIUS authentication or an accounting packet is sent
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RADIUS-EXT-MIB'
        _revision = '2010-05-25'

        def __init__(self):
            super(CISCORADIUSEXTMIB.CreClientGlobal, self).__init__()

            self.yang_name = "creClientGlobal"
            self.yang_parent_name = "CISCO-RADIUS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('creclienttotalmaxinqlength', (YLeaf(YType.uint32, 'creClientTotalMaxInQLength'), ['int'])),
                ('creclienttotalmaxwaitqlength', (YLeaf(YType.uint32, 'creClientTotalMaxWaitQLength'), ['int'])),
                ('creclienttotalmaxdoneqlength', (YLeaf(YType.uint32, 'creClientTotalMaxDoneQLength'), ['int'])),
                ('creclienttotalaccessrejects', (YLeaf(YType.uint32, 'creClientTotalAccessRejects'), ['int'])),
                ('creclienttotalaverageresponsedelay', (YLeaf(YType.int32, 'creClientTotalAverageResponseDelay'), ['int'])),
                ('creclientsourceportrangestart', (YLeaf(YType.uint16, 'creClientSourcePortRangeStart'), ['int'])),
                ('creclientsourceportrangeend', (YLeaf(YType.uint16, 'creClientSourcePortRangeEnd'), ['int'])),
                ('creclientlastusedsourceport', (YLeaf(YType.uint16, 'creClientLastUsedSourcePort'), ['int'])),
                ('creclientlastusedsourceid', (YLeaf(YType.uint32, 'creClientLastUsedSourceId'), ['int'])),
            ])
            self.creclienttotalmaxinqlength = None
            self.creclienttotalmaxwaitqlength = None
            self.creclienttotalmaxdoneqlength = None
            self.creclienttotalaccessrejects = None
            self.creclienttotalaverageresponsedelay = None
            self.creclientsourceportrangestart = None
            self.creclientsourceportrangeend = None
            self.creclientlastusedsourceport = None
            self.creclientlastusedsourceid = None
            self._segment_path = lambda: "creClientGlobal"
            self._absolute_path = lambda: "CISCO-RADIUS-EXT-MIB:CISCO-RADIUS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORADIUSEXTMIB.CreClientGlobal, ['creclienttotalmaxinqlength', 'creclienttotalmaxwaitqlength', 'creclienttotalmaxdoneqlength', 'creclienttotalaccessrejects', 'creclienttotalaverageresponsedelay', 'creclientsourceportrangestart', 'creclientsourceportrangeend', 'creclientlastusedsourceport', 'creclientlastusedsourceid'], name, value)



    class CreClientAuthentication(Entity):
        """
        
        
        .. attribute:: creauthclientbadauthenticators
        
        	This object indicates the number of RADIUS authentication response packets received which contained invalid authenticators
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclientunknownresponses
        
        	This object indicates the number of unknown RADIUS authentication responses received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclienttotalpacketswithresponses
        
        	This object indicates the number of RADIUS authentication packets that received responses
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclientbufferallocfailures
        
        	This object indicates the number of buffer allocation failures encountered during RADIUS request formation
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: buffer failures
        
        .. attribute:: creauthclienttotalresponses
        
        	This object indicates the number of RADIUS authentication response packets received by the RADIUS client
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclienttotalpacketswithoutresponses
        
        	This object indicates the number of RADIUS authentication packets that never received a response
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclientaverageresponsedelay
        
        	This object indicates the average response delay experienced for RADIUS authentication requests
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        .. attribute:: creauthclientmaxresponsedelay
        
        	This object indicates the maximum delay experienced for RADIUS authentication requests
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        .. attribute:: creauthclientmaxbuffersize
        
        	This object indicates the maximum buffer size for RADIUS authentication packet
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: bytes
        
        .. attribute:: creauthclienttimeouts
        
        	This object indicates the number of timeouts that have occurred for RADIUS authentication.  After a timeout the client may retry sending the request to the same server or to a different server or give up depending on the configuration
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: timeouts
        
        .. attribute:: creauthclientdupids
        
        	This object indicates the number of times client has received duplicate authentication responses with the same identifier.  Out of these two packets, the later packet is considered as a true match
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclientmalformedresponses
        
        	This object indicates the number of malformed RADIUS authentication responses received.  Malformed packets include packets with an invalid length
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creauthclientlastusedsourceid
        
        	This MIB object indicates the last source identifier that was used to send out a RADIUS authentication request when 'extended RADIUS source ports' is configured.  The source identifier is a counter that is incremented everytime a RADIUS authentication request is sent
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RADIUS-EXT-MIB'
        _revision = '2010-05-25'

        def __init__(self):
            super(CISCORADIUSEXTMIB.CreClientAuthentication, self).__init__()

            self.yang_name = "creClientAuthentication"
            self.yang_parent_name = "CISCO-RADIUS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('creauthclientbadauthenticators', (YLeaf(YType.uint32, 'creAuthClientBadAuthenticators'), ['int'])),
                ('creauthclientunknownresponses', (YLeaf(YType.uint32, 'creAuthClientUnknownResponses'), ['int'])),
                ('creauthclienttotalpacketswithresponses', (YLeaf(YType.uint32, 'creAuthClientTotalPacketsWithResponses'), ['int'])),
                ('creauthclientbufferallocfailures', (YLeaf(YType.uint32, 'creAuthClientBufferAllocFailures'), ['int'])),
                ('creauthclienttotalresponses', (YLeaf(YType.uint32, 'creAuthClientTotalResponses'), ['int'])),
                ('creauthclienttotalpacketswithoutresponses', (YLeaf(YType.uint32, 'creAuthClientTotalPacketsWithoutResponses'), ['int'])),
                ('creauthclientaverageresponsedelay', (YLeaf(YType.int32, 'creAuthClientAverageResponseDelay'), ['int'])),
                ('creauthclientmaxresponsedelay', (YLeaf(YType.int32, 'creAuthClientMaxResponseDelay'), ['int'])),
                ('creauthclientmaxbuffersize', (YLeaf(YType.uint32, 'creAuthClientMaxBufferSize'), ['int'])),
                ('creauthclienttimeouts', (YLeaf(YType.uint32, 'creAuthClientTimeouts'), ['int'])),
                ('creauthclientdupids', (YLeaf(YType.uint32, 'creAuthClientDupIDs'), ['int'])),
                ('creauthclientmalformedresponses', (YLeaf(YType.uint32, 'creAuthClientMalformedResponses'), ['int'])),
                ('creauthclientlastusedsourceid', (YLeaf(YType.uint32, 'creAuthClientLastUsedSourceId'), ['int'])),
            ])
            self.creauthclientbadauthenticators = None
            self.creauthclientunknownresponses = None
            self.creauthclienttotalpacketswithresponses = None
            self.creauthclientbufferallocfailures = None
            self.creauthclienttotalresponses = None
            self.creauthclienttotalpacketswithoutresponses = None
            self.creauthclientaverageresponsedelay = None
            self.creauthclientmaxresponsedelay = None
            self.creauthclientmaxbuffersize = None
            self.creauthclienttimeouts = None
            self.creauthclientdupids = None
            self.creauthclientmalformedresponses = None
            self.creauthclientlastusedsourceid = None
            self._segment_path = lambda: "creClientAuthentication"
            self._absolute_path = lambda: "CISCO-RADIUS-EXT-MIB:CISCO-RADIUS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORADIUSEXTMIB.CreClientAuthentication, ['creauthclientbadauthenticators', 'creauthclientunknownresponses', 'creauthclienttotalpacketswithresponses', 'creauthclientbufferallocfailures', 'creauthclienttotalresponses', 'creauthclienttotalpacketswithoutresponses', 'creauthclientaverageresponsedelay', 'creauthclientmaxresponsedelay', 'creauthclientmaxbuffersize', 'creauthclienttimeouts', 'creauthclientdupids', 'creauthclientmalformedresponses', 'creauthclientlastusedsourceid'], name, value)



    class CreClientAccounting(Entity):
        """
        
        
        .. attribute:: creacctclientbadauthenticators
        
        	This object indicates the number of RADIUS Accounting\-Response packets received with invalid authenticators
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclientunknownresponses
        
        	This object indicates the number of unknown RADIUS accounting responses received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclienttotalpacketswithresponses
        
        	This object indicates the number of RADIUS accounting packets that received responses
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclientbufferallocfailures
        
        	This object indicates the number of buffer allocation failures encountered for RADIUS accounting request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: buffer failures
        
        .. attribute:: creacctclienttotalresponses
        
        	This object indicates the number of RADIUS accounting response packets received by the RADIUS client
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclienttotalpacketswithoutresponses
        
        	This object indicates the number of RADIUS accounting packets that never received a response
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclientaverageresponsedelay
        
        	This object indicates the average response delay experienced for RADIUS accounting
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        .. attribute:: creacctclientmaxresponsedelay
        
        	This object indicates the maximum delay experienced for RADIUS accounting
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        .. attribute:: creacctclientmaxbuffersize
        
        	This object indicates the maximum buffer size for RADIUS accounting packets
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: bytes
        
        .. attribute:: creacctclienttimeouts
        
        	This object indicates the number of timeouts that have occurred for RADIUS accounting.  After a timeout the client may retry sending the request to the same server or to a different server or give up depending on the configuration
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: timeouts
        
        .. attribute:: creacctclientdupids
        
        	This object indicates the number of times client has received duplicate accounting responses with the same identifier.  Out of these two packets, the later packet is considered as a true match
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclientmalformedresponses
        
        	This object indicates the number of malformed RADIUS accounting responses received.  Malformed packets include packets with an invalid length
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: RADIUS packets
        
        .. attribute:: creacctclientlastusedsourceid
        
        	This MIB object indicates the last source identifier that was used to send out a RADIUS accounting request when 'extended RADIUS source ports' is configured.  The source identifier is a counter that is incremented everytime a RADIUS accounting request is sent
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-RADIUS-EXT-MIB'
        _revision = '2010-05-25'

        def __init__(self):
            super(CISCORADIUSEXTMIB.CreClientAccounting, self).__init__()

            self.yang_name = "creClientAccounting"
            self.yang_parent_name = "CISCO-RADIUS-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('creacctclientbadauthenticators', (YLeaf(YType.uint32, 'creAcctClientBadAuthenticators'), ['int'])),
                ('creacctclientunknownresponses', (YLeaf(YType.uint32, 'creAcctClientUnknownResponses'), ['int'])),
                ('creacctclienttotalpacketswithresponses', (YLeaf(YType.uint32, 'creAcctClientTotalPacketsWithResponses'), ['int'])),
                ('creacctclientbufferallocfailures', (YLeaf(YType.uint32, 'creAcctClientBufferAllocFailures'), ['int'])),
                ('creacctclienttotalresponses', (YLeaf(YType.uint32, 'creAcctClientTotalResponses'), ['int'])),
                ('creacctclienttotalpacketswithoutresponses', (YLeaf(YType.uint32, 'creAcctClientTotalPacketsWithoutResponses'), ['int'])),
                ('creacctclientaverageresponsedelay', (YLeaf(YType.int32, 'creAcctClientAverageResponseDelay'), ['int'])),
                ('creacctclientmaxresponsedelay', (YLeaf(YType.int32, 'creAcctClientMaxResponseDelay'), ['int'])),
                ('creacctclientmaxbuffersize', (YLeaf(YType.uint32, 'creAcctClientMaxBufferSize'), ['int'])),
                ('creacctclienttimeouts', (YLeaf(YType.uint32, 'creAcctClientTimeouts'), ['int'])),
                ('creacctclientdupids', (YLeaf(YType.uint32, 'creAcctClientDupIDs'), ['int'])),
                ('creacctclientmalformedresponses', (YLeaf(YType.uint32, 'creAcctClientMalformedResponses'), ['int'])),
                ('creacctclientlastusedsourceid', (YLeaf(YType.uint32, 'creAcctClientLastUsedSourceId'), ['int'])),
            ])
            self.creacctclientbadauthenticators = None
            self.creacctclientunknownresponses = None
            self.creacctclienttotalpacketswithresponses = None
            self.creacctclientbufferallocfailures = None
            self.creacctclienttotalresponses = None
            self.creacctclienttotalpacketswithoutresponses = None
            self.creacctclientaverageresponsedelay = None
            self.creacctclientmaxresponsedelay = None
            self.creacctclientmaxbuffersize = None
            self.creacctclienttimeouts = None
            self.creacctclientdupids = None
            self.creacctclientmalformedresponses = None
            self.creacctclientlastusedsourceid = None
            self._segment_path = lambda: "creClientAccounting"
            self._absolute_path = lambda: "CISCO-RADIUS-EXT-MIB:CISCO-RADIUS-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORADIUSEXTMIB.CreClientAccounting, ['creacctclientbadauthenticators', 'creacctclientunknownresponses', 'creacctclienttotalpacketswithresponses', 'creacctclientbufferallocfailures', 'creacctclienttotalresponses', 'creacctclienttotalpacketswithoutresponses', 'creacctclientaverageresponsedelay', 'creacctclientmaxresponsedelay', 'creacctclientmaxbuffersize', 'creacctclienttimeouts', 'creacctclientdupids', 'creacctclientmalformedresponses', 'creacctclientlastusedsourceid'], name, value)


    def clone_ptr(self):
        self._top_entity = CISCORADIUSEXTMIB()
        return self._top_entity



