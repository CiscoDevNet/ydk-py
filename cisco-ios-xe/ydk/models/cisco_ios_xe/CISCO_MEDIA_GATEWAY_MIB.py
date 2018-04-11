""" CISCO_MEDIA_GATEWAY_MIB 

The MIB module for managing Trunk Media Gateway.  

A Media Gateway is a network element that provides conversion 
between the audio signals carried on telephone circuits and 
data packets carried over the Internet or over other packet 
data networks. 

Trunk Media Gateway interface is between the telephone network 
and a Voice over IP/ATM network. 
The interface on a Trunk Gateway terminates a trunk connected 
to PSTN switch (e.g., Class 5, Class 4, etc.).

Media Gateways use a call control architecture where the call
control 'intelligence' is outside the gateways and handled by
external call control elements, called Media Gateway 
Controllers (MGCs). 
The MGCs or Call Agents, synchronize with each other to 
send coherent commands to the gateways under their control.

MGCs use master/slave protocols to command the gateways under 
their control.  Examples of these protocols are\:
  \*  Simple Gateway Control Protocol
  \*  Media Gateway Control Protocol
  \*  Megaco (H.248)
  \*  Simple Resource Control Protocol

To connect MG to MGCs using these control protocols through 
an IP/UDP Ports which must be configured. To resolve IP 
Addresses, DNS name services may be used.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CCallControlJitterDelayMode(Enum):
    """
    CCallControlJitterDelayMode (Enum Class)

    This textual convention defines the jitter buffer mode in

    a call connection.

    adaptive(1) \- means to use jitter nominal delay as the 

                  initial jitter buffers size and let the DSP

                  pick the optimal value of the jitter buffer

                  size between the range of jitter maximum delay

                  and jitter minimum delay.

    fixed(2) \- means to use a constant jitter buffer size

               which is specified by jitter nominal delay.

    .. data:: adaptive = 1

    .. data:: fixed = 2

    """

    adaptive = Enum.YLeaf(1, "adaptive")

    fixed = Enum.YLeaf(2, "fixed")


class CGwAdminState(Enum):
    """
    CGwAdminState (Enum Class)

    This textual convention defines the administrative state of  

    media gateway.

    The possible administrative states are as follows\:

      inService\: 

          Gateway would be restored to in\-service status 

          and a ServiceChange with method RESTART message will be 

          sent to Call Agent

      forcefulOutOfService\: 

          Gateway would be in Out\-Of\-Service State 

          Any existing connections on the GW will be deleted.

          A ServiceChange with method FORCED message will be 

          sent to call agent.

          New connections would be blocked.       

      gracefulOutOfService\: 

          Gateway would be in in Out\-Of\-Service State 

          Any existing connections on the GW will not be affected.

          A ServiceChange with method GRACEFUL message will be 

          sent to call agent.

          New connections would be blocked.

    .. data:: inService = 1

    .. data:: forcedOutOfService = 2

    .. data:: gracefulOutOfService = 3

    """

    inService = Enum.YLeaf(1, "inService")

    forcedOutOfService = Enum.YLeaf(2, "forcedOutOfService")

    gracefulOutOfService = Enum.YLeaf(3, "gracefulOutOfService")


class CGwServiceState(Enum):
    """
    CGwServiceState (Enum Class)

    This textual convention defines the service state of media 

    gateway.

    The possible service states are\:

      inService\:

        Gateway is ready to provide service. 

        In this state, Gateway will respond to connection control

        requests, send autonomous messages to the call agent

        as applicable, etc.

      forcedOutOfService\:

        Gateway is in Out\-Of\-Service State.

        All calls destroyed on the GW. 

        A Service Change message with FORCED method is sent to CA.

        No new connections are allowed.

      gracefulOutOfService\:

        Gateway is in Out\-Of\-Service State.

        All existing calls will not be affected. 

        A Service Change message with GRACEFUL method is sent to CA.

        No new connections are allowed.

    .. data:: inService = 1

    .. data:: forcedOutOfService = 2

    .. data:: gracefulOutOfService = 3

    """

    inService = Enum.YLeaf(1, "inService")

    forcedOutOfService = Enum.YLeaf(2, "forcedOutOfService")

    gracefulOutOfService = Enum.YLeaf(3, "gracefulOutOfService")



class CISCOMEDIAGATEWAYMIB(Entity):
    """
    
    
    .. attribute:: cmediagwtable
    
    	This table contains the global media gateway parameters information. It supports the modification of the global media gateway  parameters
    	**type**\:  :py:class:`Cmediagwtable <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwtable>`
    
    .. attribute:: cmgwsignalprotocoltable
    
    	This table contains the available signaling protocols that are supported by the media gateway for communication with MGCs
    	**type**\:  :py:class:`Cmgwsignalprotocoltable <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmgwsignalprotocoltable>`
    
    .. attribute:: cmediagwipconfigtable
    
    	This table contains a list of media gateway IP address and the IP address associated interface information.  If IP address associated interface is PVC, only  aal5 control PVC or aal5 bearer PVC are valid.        When the PVC is aal5 control, the IP address is used to  communicate to MGC; when the PVC is aal5 bearer, the IP address is used to communicate to other gateway. The PVC information is kept in cwAtmChanExtConfigTable\:  cwacChanPvcType\:      aal5/aal2/aal1  cwacChanApplication\:  control/bearer/signaling  If IP address associated interface is not PVC, refer to the  IP addresses associated interface table for the usage of IP address
    	**type**\:  :py:class:`Cmediagwipconfigtable <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwipconfigtable>`
    
    .. attribute:: cmediagwdomainnameconfigtable
    
    	This table provides the domain names which are configured by  users.  The domain names can be used to represent IP addresses  for\:     gateway     External DNS name server     MGC (call agent) 
    	**type**\:  :py:class:`Cmediagwdomainnameconfigtable <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwdomainnameconfigtable>`
    
    .. attribute:: cmediagwdnsipconfigtable
    
    	There is only one DNS name server on a gateway and the domain name of the DNS name server is put on  cMediaGwDomainNameConfigTable with 'dnsServer (2)'.  There could be multi IP addresses are associated with the DNS name server, this table is used to store these IP  addresses.  If any domain name using external resolution, the last entry of this table is not allowed to be deleted
    	**type**\:  :py:class:`Cmediagwdnsipconfigtable <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwdnsipconfigtable>`
    
    .. attribute:: cmgwliftable
    
    	This table is for managing LIF (Logical Interface)  in a media gateway.   LIF is a logical interface which groups the TDM  DSx1s associated with a set of packet resource partitions  (PVCs) in a media gateway.  LIF is used for\: 1. VoIP switching  2. VoATM switching 
    	**type**\:  :py:class:`Cmgwliftable <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmgwliftable>`
    
    .. attribute:: cmediagwcallcontrolconfigtable
    
    	This table defines general call control attributes for the media gateway
    	**type**\:  :py:class:`Cmediagwcallcontrolconfigtable <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwcallcontrolconfigtable>`
    
    .. attribute:: cmediagwrscstatstable
    
    	This table stores the gateway resource statistics information
    	**type**\:  :py:class:`Cmediagwrscstatstable <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwrscstatstable>`
    
    

    """

    _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
    _revision = '2009-02-25'

    def __init__(self):
        super(CISCOMEDIAGATEWAYMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-MEDIA-GATEWAY-MIB"
        self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cMediaGwTable", ("cmediagwtable", CISCOMEDIAGATEWAYMIB.Cmediagwtable)), ("cmgwSignalProtocolTable", ("cmgwsignalprotocoltable", CISCOMEDIAGATEWAYMIB.Cmgwsignalprotocoltable)), ("cMediaGwIpConfigTable", ("cmediagwipconfigtable", CISCOMEDIAGATEWAYMIB.Cmediagwipconfigtable)), ("cMediaGwDomainNameConfigTable", ("cmediagwdomainnameconfigtable", CISCOMEDIAGATEWAYMIB.Cmediagwdomainnameconfigtable)), ("cMediaGwDnsIpConfigTable", ("cmediagwdnsipconfigtable", CISCOMEDIAGATEWAYMIB.Cmediagwdnsipconfigtable)), ("cmgwLifTable", ("cmgwliftable", CISCOMEDIAGATEWAYMIB.Cmgwliftable)), ("cMediaGwCallControlConfigTable", ("cmediagwcallcontrolconfigtable", CISCOMEDIAGATEWAYMIB.Cmediagwcallcontrolconfigtable)), ("cMediaGwRscStatsTable", ("cmediagwrscstatstable", CISCOMEDIAGATEWAYMIB.Cmediagwrscstatstable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cmediagwtable = CISCOMEDIAGATEWAYMIB.Cmediagwtable()
        self.cmediagwtable.parent = self
        self._children_name_map["cmediagwtable"] = "cMediaGwTable"
        self._children_yang_names.add("cMediaGwTable")

        self.cmgwsignalprotocoltable = CISCOMEDIAGATEWAYMIB.Cmgwsignalprotocoltable()
        self.cmgwsignalprotocoltable.parent = self
        self._children_name_map["cmgwsignalprotocoltable"] = "cmgwSignalProtocolTable"
        self._children_yang_names.add("cmgwSignalProtocolTable")

        self.cmediagwipconfigtable = CISCOMEDIAGATEWAYMIB.Cmediagwipconfigtable()
        self.cmediagwipconfigtable.parent = self
        self._children_name_map["cmediagwipconfigtable"] = "cMediaGwIpConfigTable"
        self._children_yang_names.add("cMediaGwIpConfigTable")

        self.cmediagwdomainnameconfigtable = CISCOMEDIAGATEWAYMIB.Cmediagwdomainnameconfigtable()
        self.cmediagwdomainnameconfigtable.parent = self
        self._children_name_map["cmediagwdomainnameconfigtable"] = "cMediaGwDomainNameConfigTable"
        self._children_yang_names.add("cMediaGwDomainNameConfigTable")

        self.cmediagwdnsipconfigtable = CISCOMEDIAGATEWAYMIB.Cmediagwdnsipconfigtable()
        self.cmediagwdnsipconfigtable.parent = self
        self._children_name_map["cmediagwdnsipconfigtable"] = "cMediaGwDnsIpConfigTable"
        self._children_yang_names.add("cMediaGwDnsIpConfigTable")

        self.cmgwliftable = CISCOMEDIAGATEWAYMIB.Cmgwliftable()
        self.cmgwliftable.parent = self
        self._children_name_map["cmgwliftable"] = "cmgwLifTable"
        self._children_yang_names.add("cmgwLifTable")

        self.cmediagwcallcontrolconfigtable = CISCOMEDIAGATEWAYMIB.Cmediagwcallcontrolconfigtable()
        self.cmediagwcallcontrolconfigtable.parent = self
        self._children_name_map["cmediagwcallcontrolconfigtable"] = "cMediaGwCallControlConfigTable"
        self._children_yang_names.add("cMediaGwCallControlConfigTable")

        self.cmediagwrscstatstable = CISCOMEDIAGATEWAYMIB.Cmediagwrscstatstable()
        self.cmediagwrscstatstable.parent = self
        self._children_name_map["cmediagwrscstatstable"] = "cMediaGwRscStatsTable"
        self._children_yang_names.add("cMediaGwRscStatsTable")
        self._segment_path = lambda: "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB"


    class Cmediagwtable(Entity):
        """
        This table contains the global media gateway parameters
        information.
        It supports the modification of the global media gateway 
        parameters.
        
        .. attribute:: cmediagwentry
        
        	A Media Gateway Entry.   At system power\-up, an entry is created by the agent  if the system detects a media gateway module has been added  to the system, and an entry is deleted if the entry associated media gateway module has been removed from the system
        	**type**\: list of  		 :py:class:`Cmediagwentry <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwtable.Cmediagwentry>`
        
        

        """

        _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
        _revision = '2009-02-25'

        def __init__(self):
            super(CISCOMEDIAGATEWAYMIB.Cmediagwtable, self).__init__()

            self.yang_name = "cMediaGwTable"
            self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cMediaGwEntry", ("cmediagwentry", CISCOMEDIAGATEWAYMIB.Cmediagwtable.Cmediagwentry))])
            self._leafs = OrderedDict()

            self.cmediagwentry = YList(self)
            self._segment_path = lambda: "cMediaGwTable"
            self._absolute_path = lambda: "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOMEDIAGATEWAYMIB.Cmediagwtable, [], name, value)


        class Cmediagwentry(Entity):
            """
            A Media Gateway Entry.  
            At system power\-up, an entry is created by the agent 
            if the system detects a media gateway module has been added 
            to the system, and an entry is deleted if the entry associated
            media gateway module has been removed from the system.
            
            .. attribute:: cmgwindex  (key)
            
            	An index that uniquely identifies an entry in the  cMediaGwTable
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cmgwdomainname
            
            	This object is used to represent a domain name under which    the Media Gateway could also be registered in a DNS name server.   The value of this object reflects the value of  cmgwConfigDomainName from the entry with a value of  'gateway(1)' for object cmgwConfigDomainNameEntity of  cMediaGwDomainNameConfigTable.  If there is no entry in cMediaGwDomainNameConfigTable with 'gateway(1)' of cmgwConfigDomainNameEntity, then the value of this object will be empty string
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: cmgwphysicalindex
            
            	This object represents the entPhysicalIndex of the card in which media gateway is running. It will contain value 0 if the entPhysicalIndex value is not available or  not applicable
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cmgwservicestate
            
            	This object indicates the current service state of the Media  Gateway. This object is controlled by 'cmgwAdminState'  object
            	**type**\:  :py:class:`CGwServiceState <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CGwServiceState>`
            
            .. attribute:: cmgwadminstate
            
            	This object is used to change the service state of  the Media Gateway from inService to outOfService or from  outOfService to inService.  The resulting service state of the gateway is represented   by 'cmgwServiceState'
            	**type**\:  :py:class:`CGwAdminState <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CGwAdminState>`
            
            .. attribute:: cmgwgracetime
            
            	This object is used to represent grace period. The grace period (restart delay in RSIP message) is   expressed in a number of seconds.  It means how soon the gateway will be taken out of service. The value \-1 indicates that the grace period time is disabled
            	**type**\: int
            
            	**range:** \-1..65535
            
            	**units**\: seconds
            
            .. attribute:: cmgwvtmappingmode
            
            	This object is used to represent the VT (sonet Virtual Tributary) counting.  standard \- standard counting (based on Bellcore TR253) titan    \- TITAN5500 counting (based on Tellabs TITAN 5500)  Note\: 'titan' is valid only if sonet line medium type        (sonetMediumType of SONET\-MIB) is 'sonet' and        sonet path payload type (cspSonetPathPayload of       CISCO\-SONET\-MIB) is 'vt15vc11'
            	**type**\:  :py:class:`Cmgwvtmappingmode <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwtable.Cmediagwentry.Cmgwvtmappingmode>`
            
            .. attribute:: cmgwsrcfilterenabled
            
            	This object is used to enable or disable the source IP and port filtering with MGC for security consideration as follows\:   'true'  \- source IP and port filter is enabled    'false' \- source IP and port filter is disable 
            	**type**\: bool
            
            .. attribute:: cmgwlawinterceptenabled
            
            	This object is used to enable or disable the lawful intercept for government. as follows\:   'true'  \- enable lawful intercept   'false' \- disable lawful intercept
            	**type**\: bool
            
            .. attribute:: cmgwv23enabled
            
            	This object is to enable or disable V23 tone. Setting the object value to 'true', will cause VXSM (Voice Switching Service Module) to detect V23 tone
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
            _revision = '2009-02-25'

            def __init__(self):
                super(CISCOMEDIAGATEWAYMIB.Cmediagwtable.Cmediagwentry, self).__init__()

                self.yang_name = "cMediaGwEntry"
                self.yang_parent_name = "cMediaGwTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cmgwindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cmgwindex', YLeaf(YType.int32, 'cmgwIndex')),
                    ('cmgwdomainname', YLeaf(YType.str, 'cmgwDomainName')),
                    ('cmgwphysicalindex', YLeaf(YType.int32, 'cmgwPhysicalIndex')),
                    ('cmgwservicestate', YLeaf(YType.enumeration, 'cmgwServiceState')),
                    ('cmgwadminstate', YLeaf(YType.enumeration, 'cmgwAdminState')),
                    ('cmgwgracetime', YLeaf(YType.int32, 'cmgwGraceTime')),
                    ('cmgwvtmappingmode', YLeaf(YType.enumeration, 'cmgwVtMappingMode')),
                    ('cmgwsrcfilterenabled', YLeaf(YType.boolean, 'cmgwSrcFilterEnabled')),
                    ('cmgwlawinterceptenabled', YLeaf(YType.boolean, 'cmgwLawInterceptEnabled')),
                    ('cmgwv23enabled', YLeaf(YType.boolean, 'cmgwV23Enabled')),
                ])
                self.cmgwindex = None
                self.cmgwdomainname = None
                self.cmgwphysicalindex = None
                self.cmgwservicestate = None
                self.cmgwadminstate = None
                self.cmgwgracetime = None
                self.cmgwvtmappingmode = None
                self.cmgwsrcfilterenabled = None
                self.cmgwlawinterceptenabled = None
                self.cmgwv23enabled = None
                self._segment_path = lambda: "cMediaGwEntry" + "[cmgwIndex='" + str(self.cmgwindex) + "']"
                self._absolute_path = lambda: "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/cMediaGwTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOMEDIAGATEWAYMIB.Cmediagwtable.Cmediagwentry, ['cmgwindex', 'cmgwdomainname', 'cmgwphysicalindex', 'cmgwservicestate', 'cmgwadminstate', 'cmgwgracetime', 'cmgwvtmappingmode', 'cmgwsrcfilterenabled', 'cmgwlawinterceptenabled', 'cmgwv23enabled'], name, value)

            class Cmgwvtmappingmode(Enum):
                """
                Cmgwvtmappingmode (Enum Class)

                This object is used to represent the VT (sonet Virtual

                Tributary) counting.

                standard \- standard counting (based on Bellcore TR253)

                titan    \- TITAN5500 counting (based on Tellabs TITAN 5500)

                Note\: 'titan' is valid only if sonet line medium type 

                      (sonetMediumType of SONET\-MIB) is 'sonet' and 

                      sonet path payload type (cspSonetPathPayload of

                      CISCO\-SONET\-MIB) is 'vt15vc11'.

                .. data:: standard = 1

                .. data:: titan = 2

                """

                standard = Enum.YLeaf(1, "standard")

                titan = Enum.YLeaf(2, "titan")



    class Cmgwsignalprotocoltable(Entity):
        """
        This table contains the available signaling protocols that
        are supported by the media gateway for communication with
        MGCs.
        
        .. attribute:: cmgwsignalprotocolentry
        
        	Each entry represents an signaling protocol supported by the media gateway
        	**type**\: list of  		 :py:class:`Cmgwsignalprotocolentry <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmgwsignalprotocoltable.Cmgwsignalprotocolentry>`
        
        

        """

        _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
        _revision = '2009-02-25'

        def __init__(self):
            super(CISCOMEDIAGATEWAYMIB.Cmgwsignalprotocoltable, self).__init__()

            self.yang_name = "cmgwSignalProtocolTable"
            self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cmgwSignalProtocolEntry", ("cmgwsignalprotocolentry", CISCOMEDIAGATEWAYMIB.Cmgwsignalprotocoltable.Cmgwsignalprotocolentry))])
            self._leafs = OrderedDict()

            self.cmgwsignalprotocolentry = YList(self)
            self._segment_path = lambda: "cmgwSignalProtocolTable"
            self._absolute_path = lambda: "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOMEDIAGATEWAYMIB.Cmgwsignalprotocoltable, [], name, value)


        class Cmgwsignalprotocolentry(Entity):
            """
            Each entry represents an signaling protocol supported
            by the media gateway.
            
            .. attribute:: cmgwindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cmgwsignalprotocolindex  (key)
            
            	An index that uniquely identifies an entry in cmgwSignalProtocolTable
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: cmgwsignalprotocol
            
            	This object is used to represent the protocol type. other \- None of the following types. mgcp  \- Media Gateway Control Protocol h248 \- Media Gateway Control (ITU H.248) tgcp \- Trunking Gateway Control Protocol
            	**type**\:  :py:class:`Cmgwsignalprotocol <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmgwsignalprotocoltable.Cmgwsignalprotocolentry.Cmgwsignalprotocol>`
            
            .. attribute:: cmgwsignalprotocolversion
            
            	This object is used to represent the protocol version.  For example cmgwSignalProtocol is 'mgcp(2)' and this object is string '1.0'. cmgwSignalProtocol is  'h248(3)' and this object is set to '2.0'
            	**type**\: str
            
            	**length:** 1..16
            
            .. attribute:: cmgwsignalprotocolport
            
            	This object is used to represent the UDP port associated  with the protocol. If the value of cmgwSignalProtocol is 'mgcp(2)' and the value of cmgwSignalProtcolVersion is '1.0', the default value of this object is '2727'.  If the value of cmgwSignalProtocol is 'h248(3)' and the value of cmgwSignalProtcolVersion is '1.0', the default value of this object is '2944'
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cmgwsignalmgcprotocolport
            
            	This object specifies the protocol port of the Media Gateway Controller (MGC). If the value of cmgwSignalProtocol is 'mgcp(2)' or 'tgcp(4)' and the value of cmgwSignalProtcolVersion is '1.0', the default value of this object is '2427'. If the value of cmgwSignalProtocol is 'h248(3)' and the value of cmgwSignalProtcolVersion is '1.0', the default value of this object is '2944'
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cmgwsignalprotocolpreference
            
            	This object specifies the preference of the signal protocol  supported in the media gateway.  If this object is set to 0, the corresponding signal protocol will not be used by the gateway.   The value of this object is unique within the corresponding gateway. The entry with lower value has higher preference
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cmgwsignalprotocolconfigver
            
            	This object specifies the protocol version used by the gateway in the messages to MGC in order to exchange the service capabilities.  For example cmgwSignalProtocol is 'h248(3)' and this object can be string '1' or '1.0', '2' or '2.0'.   'MAX' is a special string indicating the gateway will use the highest protocol version supported in the  gateway, but it can be changed to lower version after  it negotiates with MGC. The final negotiated protocol version will be indicated in cmgwSignalProtocolVersion.  The version strings other than 'MAX' can be specified for the gateway to communicate with the MGC which doesn't support service capabilities negotiation. For example if a MGC supports only version 1.0 MGCP, this object should be set to '1' to instruct the gateway using MGCP  version 1.0 format messages to communicate with MGC. 
            	**type**\: str
            
            	**length:** 1..16
            
            

            """

            _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
            _revision = '2009-02-25'

            def __init__(self):
                super(CISCOMEDIAGATEWAYMIB.Cmgwsignalprotocoltable.Cmgwsignalprotocolentry, self).__init__()

                self.yang_name = "cmgwSignalProtocolEntry"
                self.yang_parent_name = "cmgwSignalProtocolTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cmgwindex','cmgwsignalprotocolindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cmgwindex', YLeaf(YType.str, 'cmgwIndex')),
                    ('cmgwsignalprotocolindex', YLeaf(YType.int32, 'cmgwSignalProtocolIndex')),
                    ('cmgwsignalprotocol', YLeaf(YType.enumeration, 'cmgwSignalProtocol')),
                    ('cmgwsignalprotocolversion', YLeaf(YType.str, 'cmgwSignalProtocolVersion')),
                    ('cmgwsignalprotocolport', YLeaf(YType.int32, 'cmgwSignalProtocolPort')),
                    ('cmgwsignalmgcprotocolport', YLeaf(YType.uint16, 'cmgwSignalMgcProtocolPort')),
                    ('cmgwsignalprotocolpreference', YLeaf(YType.int32, 'cmgwSignalProtocolPreference')),
                    ('cmgwsignalprotocolconfigver', YLeaf(YType.str, 'cmgwSignalProtocolConfigVer')),
                ])
                self.cmgwindex = None
                self.cmgwsignalprotocolindex = None
                self.cmgwsignalprotocol = None
                self.cmgwsignalprotocolversion = None
                self.cmgwsignalprotocolport = None
                self.cmgwsignalmgcprotocolport = None
                self.cmgwsignalprotocolpreference = None
                self.cmgwsignalprotocolconfigver = None
                self._segment_path = lambda: "cmgwSignalProtocolEntry" + "[cmgwIndex='" + str(self.cmgwindex) + "']" + "[cmgwSignalProtocolIndex='" + str(self.cmgwsignalprotocolindex) + "']"
                self._absolute_path = lambda: "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/cmgwSignalProtocolTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOMEDIAGATEWAYMIB.Cmgwsignalprotocoltable.Cmgwsignalprotocolentry, ['cmgwindex', 'cmgwsignalprotocolindex', 'cmgwsignalprotocol', 'cmgwsignalprotocolversion', 'cmgwsignalprotocolport', 'cmgwsignalmgcprotocolport', 'cmgwsignalprotocolpreference', 'cmgwsignalprotocolconfigver'], name, value)

            class Cmgwsignalprotocol(Enum):
                """
                Cmgwsignalprotocol (Enum Class)

                This object is used to represent the protocol type.

                other \- None of the following types.

                mgcp  \- Media Gateway Control Protocol

                h248 \- Media Gateway Control (ITU H.248)

                tgcp \- Trunking Gateway Control Protocol

                .. data:: other = 1

                .. data:: mgcp = 2

                .. data:: h248 = 3

                .. data:: tgcp = 4

                """

                other = Enum.YLeaf(1, "other")

                mgcp = Enum.YLeaf(2, "mgcp")

                h248 = Enum.YLeaf(3, "h248")

                tgcp = Enum.YLeaf(4, "tgcp")



    class Cmediagwipconfigtable(Entity):
        """
        This table contains a list of media gateway IP address and
        the IP address associated interface information.
        
        If IP address associated interface is PVC, only 
        aal5 control PVC or aal5 bearer PVC are valid.       
        When the PVC is aal5 control, the IP address is used to 
        communicate to MGC; when the PVC is aal5 bearer, the IP
        address is used to communicate to other gateway.
        The PVC information is kept in cwAtmChanExtConfigTable\:
         cwacChanPvcType\:      aal5/aal2/aal1
         cwacChanApplication\:  control/bearer/signaling
        
        If IP address associated interface is not PVC, refer to the 
        IP addresses associated interface table for the usage
        of IP address.
        
        .. attribute:: cmediagwipconfigentry
        
        	A Media Gateway IP configuration entry.  Each entry represents a media gateway IP address for MGCs to communicate with the media gateway
        	**type**\: list of  		 :py:class:`Cmediagwipconfigentry <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwipconfigtable.Cmediagwipconfigentry>`
        
        

        """

        _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
        _revision = '2009-02-25'

        def __init__(self):
            super(CISCOMEDIAGATEWAYMIB.Cmediagwipconfigtable, self).__init__()

            self.yang_name = "cMediaGwIpConfigTable"
            self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cMediaGwIpConfigEntry", ("cmediagwipconfigentry", CISCOMEDIAGATEWAYMIB.Cmediagwipconfigtable.Cmediagwipconfigentry))])
            self._leafs = OrderedDict()

            self.cmediagwipconfigentry = YList(self)
            self._segment_path = lambda: "cMediaGwIpConfigTable"
            self._absolute_path = lambda: "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOMEDIAGATEWAYMIB.Cmediagwipconfigtable, [], name, value)


        class Cmediagwipconfigentry(Entity):
            """
            A Media Gateway IP configuration entry. 
            Each entry represents a media gateway IP address for MGCs
            to communicate with the media gateway.
            
            .. attribute:: cmgwindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cmgwipconfigindex  (key)
            
            	A unique index to identify each media gateway IP address
            	**type**\: int
            
            	**range:** 1..64
            
            .. attribute:: cmgwipconfigifindex
            
            	This object is ifIndex of the interface which is associated to the media gateway IP address.  For ATM interface, the IP address should be associated to an existing PVC\:    cmgwIpConfigIfIndex represents port of the PVC    cmgwIpConfigVpi represents VPI of the PVC    cmgwIpConfigVci represents VCI of the PVC And one PVC only can be associated with one IP address.  If this object is set to zero which means the IP address is not associated to any interface
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cmgwipconfigvpi
            
            	This object represents VPI of the PVC which is associated to the IP address. If the IP address is not associated to PVC, the value  of this object is set to \-1
            	**type**\: int
            
            	**range:** \-1..4095
            
            .. attribute:: cmgwipconfigvci
            
            	This object represents VCI of the PVC which is associated to the IP address. If the IP address is not associated to PVC, the value of this object is set to \-1
            	**type**\: int
            
            	**range:** \-1..65535
            
            .. attribute:: cmgwipconfigaddrtype
            
            	This object is the IP address type
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cmgwipconfigaddress
            
            	The configured IP address of media gateway. This object can not be modified
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cmgwipconfigsubnetmask
            
            	This object is used to specify the number of leading one    bits which from the mask to be logical\-ANDed with the media   gateway address before being compared to the value in the  cmgwIpCofigAddress.  Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bitwise logical\-AND of the mask formed from x with the value  of the corresponding instance of the cmgwIpCofigAddress  object is not equal to cmgwIpCofigAddress
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: cmgwipconfigdefaultgwip
            
            	This object specifies cmgwIpConfigAddress of the entry will become the default gateway address. This object can be set to 'true' for only one entry in the table
            	**type**\: bool
            
            .. attribute:: cmgwipconfigforremotemapping
            
            	This object specifies whether the address defined in cmgwIpConfigAddress is the address mapping at the remote end of this PVC.   If this object is set to 'true', the address defined in cmgwIpConfigAddress is for the remote end of the PVC. If this object is set to 'false', the address defined in cmgwIpConfigAddress is for the local end of the PVC
            	**type**\: bool
            
            .. attribute:: cmgwipconfigrowstatus
            
            	This object is used to add and delete an entry.  When an entry of the table is created, the following  objects are mandatory\:     cmgwIpConfigIfIndex     cmgwIpConfigVpi     cmgwIpConfigVci     cmgwIpConfigAddress     cmgwIpConfigSubnetMask  These objects can not be modified after the value of this object is set to 'active'.  Modification can only be done by deleting and re\-adding the  entry again.  After the system verify the validity of the data, it will set the cmgwIpConfigRowStatus to 'active'
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
            _revision = '2009-02-25'

            def __init__(self):
                super(CISCOMEDIAGATEWAYMIB.Cmediagwipconfigtable.Cmediagwipconfigentry, self).__init__()

                self.yang_name = "cMediaGwIpConfigEntry"
                self.yang_parent_name = "cMediaGwIpConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cmgwindex','cmgwipconfigindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cmgwindex', YLeaf(YType.str, 'cmgwIndex')),
                    ('cmgwipconfigindex', YLeaf(YType.int32, 'cmgwIpConfigIndex')),
                    ('cmgwipconfigifindex', YLeaf(YType.int32, 'cmgwIpConfigIfIndex')),
                    ('cmgwipconfigvpi', YLeaf(YType.int32, 'cmgwIpConfigVpi')),
                    ('cmgwipconfigvci', YLeaf(YType.int32, 'cmgwIpConfigVci')),
                    ('cmgwipconfigaddrtype', YLeaf(YType.enumeration, 'cmgwIpConfigAddrType')),
                    ('cmgwipconfigaddress', YLeaf(YType.str, 'cmgwIpConfigAddress')),
                    ('cmgwipconfigsubnetmask', YLeaf(YType.uint32, 'cmgwIpConfigSubnetMask')),
                    ('cmgwipconfigdefaultgwip', YLeaf(YType.boolean, 'cmgwIpConfigDefaultGwIp')),
                    ('cmgwipconfigforremotemapping', YLeaf(YType.boolean, 'cmgwIpConfigForRemoteMapping')),
                    ('cmgwipconfigrowstatus', YLeaf(YType.enumeration, 'cmgwIpConfigRowStatus')),
                ])
                self.cmgwindex = None
                self.cmgwipconfigindex = None
                self.cmgwipconfigifindex = None
                self.cmgwipconfigvpi = None
                self.cmgwipconfigvci = None
                self.cmgwipconfigaddrtype = None
                self.cmgwipconfigaddress = None
                self.cmgwipconfigsubnetmask = None
                self.cmgwipconfigdefaultgwip = None
                self.cmgwipconfigforremotemapping = None
                self.cmgwipconfigrowstatus = None
                self._segment_path = lambda: "cMediaGwIpConfigEntry" + "[cmgwIndex='" + str(self.cmgwindex) + "']" + "[cmgwIpConfigIndex='" + str(self.cmgwipconfigindex) + "']"
                self._absolute_path = lambda: "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/cMediaGwIpConfigTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOMEDIAGATEWAYMIB.Cmediagwipconfigtable.Cmediagwipconfigentry, ['cmgwindex', 'cmgwipconfigindex', 'cmgwipconfigifindex', 'cmgwipconfigvpi', 'cmgwipconfigvci', 'cmgwipconfigaddrtype', 'cmgwipconfigaddress', 'cmgwipconfigsubnetmask', 'cmgwipconfigdefaultgwip', 'cmgwipconfigforremotemapping', 'cmgwipconfigrowstatus'], name, value)


    class Cmediagwdomainnameconfigtable(Entity):
        """
        This table provides the domain names which are configured by 
        users. 
        The domain names can be used to represent IP addresses 
        for\:
            gateway
            External DNS name server
            MGC (call agent) 
        
        .. attribute:: cmediagwdomainnameconfigentry
        
        	Each entry represents a domain name used in the system.  Creation and deletion are supported. Modification is prohibited
        	**type**\: list of  		 :py:class:`Cmediagwdomainnameconfigentry <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwdomainnameconfigtable.Cmediagwdomainnameconfigentry>`
        
        

        """

        _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
        _revision = '2009-02-25'

        def __init__(self):
            super(CISCOMEDIAGATEWAYMIB.Cmediagwdomainnameconfigtable, self).__init__()

            self.yang_name = "cMediaGwDomainNameConfigTable"
            self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cMediaGwDomainNameConfigEntry", ("cmediagwdomainnameconfigentry", CISCOMEDIAGATEWAYMIB.Cmediagwdomainnameconfigtable.Cmediagwdomainnameconfigentry))])
            self._leafs = OrderedDict()

            self.cmediagwdomainnameconfigentry = YList(self)
            self._segment_path = lambda: "cMediaGwDomainNameConfigTable"
            self._absolute_path = lambda: "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOMEDIAGATEWAYMIB.Cmediagwdomainnameconfigtable, [], name, value)


        class Cmediagwdomainnameconfigentry(Entity):
            """
            Each entry represents a domain name used in the system.
            
            Creation and deletion are supported. Modification
            is prohibited.
            
            .. attribute:: cmgwindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cmgwconfigdomainnameindex  (key)
            
            	An index that is uniquely identifies a domain name configured in the system
            	**type**\: int
            
            	**range:** 1..128
            
            .. attribute:: cmgwconfigdomainnameentity
            
            	This object indicates which entity to use this domain name.  gateway(1)   \- The domain name of media gateway.                With the same cmgwIndex, there is one and                 only one entry allowed with the value                 'gateway(1)' of this object.  dnsServer(2) \- The domain name of DNS name server that is used                 by Media gateway to find Internet Network                 Address from a DNS name.  mgc(3)       \- The domain name of a MGC (Media Gateway                Controller) associated with the media                 gateway. 
            	**type**\:  :py:class:`Cmgwconfigdomainnameentity <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwdomainnameconfigtable.Cmediagwdomainnameconfigentry.Cmgwconfigdomainnameentity>`
            
            .. attribute:: cmgwconfigdomainname
            
            	This object specifies the domain name.  The domain name should be unique if there are more than one entries having the same value in the object  cmgwConfigDomainNameEntity. For example, the gateway domain name should be unique  if the cmgwConfigDomainNameEntity has the value of  'gateway(1)'
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: cmgwconfigdomainnamerowstatus
            
            	This object is used to add and delete an entry.  When an entry is created, the following objects are mandatory\:      cmgwConfigDomainName      cmgwConfigDomainNameEntity  When deleting domain name of DNS name server (cmgwConfigDomainNameEntity is dnsServer (2)), the  cMediaGwDnsIpConfigTable should be empty.  Adding/deleting entry with cmgwConfigDomainNameEntity of 'mgc' will cause adding/deleting entry in  cMgcConfigTable (CISCO\-MGC\-MIB) automatically.  The cmgwConfigDomainName and cmgwConfigDomainNameEntity can not be modified if the value of this object is 'active'. 
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
            _revision = '2009-02-25'

            def __init__(self):
                super(CISCOMEDIAGATEWAYMIB.Cmediagwdomainnameconfigtable.Cmediagwdomainnameconfigentry, self).__init__()

                self.yang_name = "cMediaGwDomainNameConfigEntry"
                self.yang_parent_name = "cMediaGwDomainNameConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cmgwindex','cmgwconfigdomainnameindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cmgwindex', YLeaf(YType.str, 'cmgwIndex')),
                    ('cmgwconfigdomainnameindex', YLeaf(YType.int32, 'cmgwConfigDomainNameIndex')),
                    ('cmgwconfigdomainnameentity', YLeaf(YType.enumeration, 'cmgwConfigDomainNameEntity')),
                    ('cmgwconfigdomainname', YLeaf(YType.str, 'cmgwConfigDomainName')),
                    ('cmgwconfigdomainnamerowstatus', YLeaf(YType.enumeration, 'cmgwConfigDomainNameRowStatus')),
                ])
                self.cmgwindex = None
                self.cmgwconfigdomainnameindex = None
                self.cmgwconfigdomainnameentity = None
                self.cmgwconfigdomainname = None
                self.cmgwconfigdomainnamerowstatus = None
                self._segment_path = lambda: "cMediaGwDomainNameConfigEntry" + "[cmgwIndex='" + str(self.cmgwindex) + "']" + "[cmgwConfigDomainNameIndex='" + str(self.cmgwconfigdomainnameindex) + "']"
                self._absolute_path = lambda: "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/cMediaGwDomainNameConfigTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOMEDIAGATEWAYMIB.Cmediagwdomainnameconfigtable.Cmediagwdomainnameconfigentry, ['cmgwindex', 'cmgwconfigdomainnameindex', 'cmgwconfigdomainnameentity', 'cmgwconfigdomainname', 'cmgwconfigdomainnamerowstatus'], name, value)

            class Cmgwconfigdomainnameentity(Enum):
                """
                Cmgwconfigdomainnameentity (Enum Class)

                This object indicates which entity to use this domain name.

                gateway(1)   \- The domain name of media gateway.

                               With the same cmgwIndex, there is one and 

                               only one entry allowed with the value 

                               'gateway(1)' of this object.

                dnsServer(2) \- The domain name of DNS name server that is used 

                               by Media gateway to find Internet Network 

                               Address from a DNS name.

                mgc(3)       \- The domain name of a MGC (Media Gateway

                               Controller) associated with the media 

                               gateway. 

                .. data:: gateway = 1

                .. data:: dnsServer = 2

                .. data:: mgc = 3

                """

                gateway = Enum.YLeaf(1, "gateway")

                dnsServer = Enum.YLeaf(2, "dnsServer")

                mgc = Enum.YLeaf(3, "mgc")



    class Cmediagwdnsipconfigtable(Entity):
        """
        There is only one DNS name server on a gateway
        and the domain name of the DNS name server is put on 
        cMediaGwDomainNameConfigTable with 'dnsServer (2)'.
        
        There could be multi IP addresses are associated with the
        DNS name server, this table is used to store these IP 
        addresses.
        
        If any domain name using external resolution, the last entry
        of this table is not allowed to be deleted.
        
        .. attribute:: cmediagwdnsipconfigentry
        
        	Each entry represents an IP address of the DNS name  server
        	**type**\: list of  		 :py:class:`Cmediagwdnsipconfigentry <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwdnsipconfigtable.Cmediagwdnsipconfigentry>`
        
        

        """

        _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
        _revision = '2009-02-25'

        def __init__(self):
            super(CISCOMEDIAGATEWAYMIB.Cmediagwdnsipconfigtable, self).__init__()

            self.yang_name = "cMediaGwDnsIpConfigTable"
            self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cMediaGwDnsIpConfigEntry", ("cmediagwdnsipconfigentry", CISCOMEDIAGATEWAYMIB.Cmediagwdnsipconfigtable.Cmediagwdnsipconfigentry))])
            self._leafs = OrderedDict()

            self.cmediagwdnsipconfigentry = YList(self)
            self._segment_path = lambda: "cMediaGwDnsIpConfigTable"
            self._absolute_path = lambda: "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOMEDIAGATEWAYMIB.Cmediagwdnsipconfigtable, [], name, value)


        class Cmediagwdnsipconfigentry(Entity):
            """
            Each entry represents an IP address of the DNS name 
            server.
            
            .. attribute:: cmgwindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cmgwdnsipindex  (key)
            
            	An index that uniquely identifies an IP address of DNS name server
            	**type**\: int
            
            	**range:** 1..6
            
            .. attribute:: cmgwdnsdomainname
            
            	The domain name of DNS name server.  The value of this object reflects the value of  cmgwConfigDomainName from the entry with a value of  'dnsServer(2)' for object cmgwConfigDomainNameEntity of  cMediaGwDomainNameConfigTable.  If there is no entry in cMediaGwDomainNameConfigTable with 'dnsServer(2)' of cmgwConfigDomainNameEntity, then the value of this object will be empty string
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: cmgwdnsiptype
            
            	DNS name server IP address type
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cmgwdnsip
            
            	The IP address of DNS name server. The IP address of DNS name server must be unique in this table
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cmgwdnsiprowstatus
            
            	This object is used to add and delete an entry.  When an entry of the table is created, the value of this object should be set to 'createAndGo' and the following objects are mandatory\:     cmgwDnsIp  When the user wants to delete the entry, the value of this object should be set to 'destroy'.  The entry can not be modified if the value of this  object is 'active'
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
            _revision = '2009-02-25'

            def __init__(self):
                super(CISCOMEDIAGATEWAYMIB.Cmediagwdnsipconfigtable.Cmediagwdnsipconfigentry, self).__init__()

                self.yang_name = "cMediaGwDnsIpConfigEntry"
                self.yang_parent_name = "cMediaGwDnsIpConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cmgwindex','cmgwdnsipindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cmgwindex', YLeaf(YType.str, 'cmgwIndex')),
                    ('cmgwdnsipindex', YLeaf(YType.int32, 'cmgwDnsIpIndex')),
                    ('cmgwdnsdomainname', YLeaf(YType.str, 'cmgwDnsDomainName')),
                    ('cmgwdnsiptype', YLeaf(YType.enumeration, 'cmgwDnsIpType')),
                    ('cmgwdnsip', YLeaf(YType.str, 'cmgwDnsIp')),
                    ('cmgwdnsiprowstatus', YLeaf(YType.enumeration, 'cmgwDnsIpRowStatus')),
                ])
                self.cmgwindex = None
                self.cmgwdnsipindex = None
                self.cmgwdnsdomainname = None
                self.cmgwdnsiptype = None
                self.cmgwdnsip = None
                self.cmgwdnsiprowstatus = None
                self._segment_path = lambda: "cMediaGwDnsIpConfigEntry" + "[cmgwIndex='" + str(self.cmgwindex) + "']" + "[cmgwDnsIpIndex='" + str(self.cmgwdnsipindex) + "']"
                self._absolute_path = lambda: "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/cMediaGwDnsIpConfigTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOMEDIAGATEWAYMIB.Cmediagwdnsipconfigtable.Cmediagwdnsipconfigentry, ['cmgwindex', 'cmgwdnsipindex', 'cmgwdnsdomainname', 'cmgwdnsiptype', 'cmgwdnsip', 'cmgwdnsiprowstatus'], name, value)


    class Cmgwliftable(Entity):
        """
        This table is for managing LIF (Logical Interface) 
        in a media gateway. 
        
        LIF is a logical interface which groups the TDM 
        DSx1s associated with a set of packet resource partitions 
        (PVCs) in a media gateway.
        
        LIF is used for\:
        1. VoIP switching 
        2. VoATM switching 
        
        .. attribute:: cmgwlifentry
        
        	An entry of this table is created by the media gateway when it supports the VoIP/VoATM application
        	**type**\: list of  		 :py:class:`Cmgwlifentry <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmgwliftable.Cmgwlifentry>`
        
        

        """

        _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
        _revision = '2009-02-25'

        def __init__(self):
            super(CISCOMEDIAGATEWAYMIB.Cmgwliftable, self).__init__()

            self.yang_name = "cmgwLifTable"
            self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cmgwLifEntry", ("cmgwlifentry", CISCOMEDIAGATEWAYMIB.Cmgwliftable.Cmgwlifentry))])
            self._leafs = OrderedDict()

            self.cmgwlifentry = YList(self)
            self._segment_path = lambda: "cmgwLifTable"
            self._absolute_path = lambda: "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOMEDIAGATEWAYMIB.Cmgwliftable, [], name, value)


        class Cmgwlifentry(Entity):
            """
            An entry of this table is created by the media gateway
            when it supports the VoIP/VoATM application.
            
            .. attribute:: cmgwindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cmgwlifnumber  (key)
            
            	An index that uniquely identifies a LIF in the  media gateway
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: cmgwlifpvccount
            
            	This object represents the total number of PVC within  this LIF.  When users associate/disassociate a PVC with a LIF  by giving a non\-zero/zero value of cwacChanLifNum in cwAtmChanExtConfigTable, the value of this object  will be incremented/decremented accordingly.  The value zero means there is no PVC associated with  the LIF
            	**type**\: int
            
            	**range:** 0..10000
            
            .. attribute:: cmgwlifvoiceifcount
            
            	This object represents the total number of Voice Interfaces within this LIF.  When users associate/disassociate a Voice Interface with a LIF by giving a non\-zero/zero value of  ccasVoiceCfgLifNumber for the DS0 group in  ccasVoiceExtCfgTable, the value of this object will be  incremented/decremented accordingly.   The value zero means there is no Voice Interface associated with the LIF
            	**type**\: int
            
            	**range:** 0..1000
            
            

            """

            _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
            _revision = '2009-02-25'

            def __init__(self):
                super(CISCOMEDIAGATEWAYMIB.Cmgwliftable.Cmgwlifentry, self).__init__()

                self.yang_name = "cmgwLifEntry"
                self.yang_parent_name = "cmgwLifTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cmgwindex','cmgwlifnumber']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cmgwindex', YLeaf(YType.str, 'cmgwIndex')),
                    ('cmgwlifnumber', YLeaf(YType.uint32, 'cmgwLifNumber')),
                    ('cmgwlifpvccount', YLeaf(YType.uint32, 'cmgwLifPvcCount')),
                    ('cmgwlifvoiceifcount', YLeaf(YType.uint32, 'cmgwLifVoiceIfCount')),
                ])
                self.cmgwindex = None
                self.cmgwlifnumber = None
                self.cmgwlifpvccount = None
                self.cmgwlifvoiceifcount = None
                self._segment_path = lambda: "cmgwLifEntry" + "[cmgwIndex='" + str(self.cmgwindex) + "']" + "[cmgwLifNumber='" + str(self.cmgwlifnumber) + "']"
                self._absolute_path = lambda: "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/cmgwLifTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOMEDIAGATEWAYMIB.Cmgwliftable.Cmgwlifentry, ['cmgwindex', 'cmgwlifnumber', 'cmgwlifpvccount', 'cmgwlifvoiceifcount'], name, value)


    class Cmediagwcallcontrolconfigtable(Entity):
        """
        This table defines general call control attributes for
        the media gateway.
        
        .. attribute:: cmediagwcallcontrolconfigentry
        
        	One entry for each media gateway which supports call control  protocol
        	**type**\: list of  		 :py:class:`Cmediagwcallcontrolconfigentry <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry>`
        
        

        """

        _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
        _revision = '2009-02-25'

        def __init__(self):
            super(CISCOMEDIAGATEWAYMIB.Cmediagwcallcontrolconfigtable, self).__init__()

            self.yang_name = "cMediaGwCallControlConfigTable"
            self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cMediaGwCallControlConfigEntry", ("cmediagwcallcontrolconfigentry", CISCOMEDIAGATEWAYMIB.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry))])
            self._leafs = OrderedDict()

            self.cmediagwcallcontrolconfigentry = YList(self)
            self._segment_path = lambda: "cMediaGwCallControlConfigTable"
            self._absolute_path = lambda: "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOMEDIAGATEWAYMIB.Cmediagwcallcontrolconfigtable, [], name, value)


        class Cmediagwcallcontrolconfigentry(Entity):
            """
            One entry for each media gateway which supports call control 
            protocol.
            
            .. attribute:: cmgwindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cmediagwcccfgcontroltos
            
            	This object specifies Type Of Service (TOS) field of IP header for the signaling control packet in VoIP application
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cmediagwcccfgbearertos
            
            	This object specifies Type Of Service (TOS) field of IP header for the voice payload packet in VoIP application
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cmediagwcccfgntepayload
            
            	This object specifies NTE (Named Telephony Events) payload type
            	**type**\: int
            
            	**range:** 96..127
            
            .. attribute:: cmediagwcccfgnsepayload
            
            	This object specifies NSE (Network Signaling Events) payload type
            	**type**\: int
            
            	**range:** 98..117
            
            .. attribute:: cmediagwcccfgnseresptimer
            
            	This object specifies Network Signaling Event (NSE) timeout value
            	**type**\: int
            
            	**range:** 250..10000
            
            	**units**\: milliseconds
            
            .. attribute:: cmediagwcccfgvbdjitterdelaymode
            
            	The object specifies the jitter buffer mode applied to a VBD (Voice Band Data) call connection.  adaptive \- means to use cMediaGwCcCfgVbdJitterNomDelay as            the initial jitter buffers size and let the DSP            pick the optimal value of the jitter buffer            size between the range of            cMediaGwCcCfgVbcJitterMaxDelay and            cMediaGwCcCfgVbcJitterMinDelay.  fixed \- means to use a constant jitter buffer size         which is specified by cMediaGwCcCfgVbdJitterNomDelay
            	**type**\:  :py:class:`CCallControlJitterDelayMode <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CCallControlJitterDelayMode>`
            
            .. attribute:: cmediagwcccfgvbdjittermaxdelay
            
            	This object specifies the maximum jitter buffer size  in VBD (Voice Band Data)
            	**type**\: int
            
            	**range:** 20..135
            
            	**units**\: milliseconds
            
            .. attribute:: cmediagwcccfgvbdjitternomdelay
            
            	This object specifies the nominal jitter buffer size  in VBD (Voice Band Data)
            	**type**\: int
            
            	**range:** 5..135
            
            	**units**\: milliseconds
            
            .. attribute:: cmediagwcccfgvbdjittermindelay
            
            	This object specifies the nominal jitter buffer size  in VBD (Voice Band Data)
            	**type**\: int
            
            	**range:** 0..135
            
            	**units**\: milliseconds
            
            .. attribute:: cmediagwcccfgdefaulttoneplanid
            
            	This object specifies the default tone plan index (the value of cvtcTonePlanId) for the media gateway
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: cmediagwcccfgdescrinfoenabled
            
            	This object specifies whether the media gateway supports descriptive suffix of the name schema for terminations.  There are two parts in name schema of termination, prefix and suffix. For example the name schema for a DS (Digital Subscriber) termination, can be 'DS/OC3\_2/DS1\_6/DS0\_24'. It represents DS type termination in 2nd OC3 line,  6th DS1 and 24th DS0 channel. In this example, 'DS' is  the prefix, 'OC3\_2/DS1\_6/DS0\_24' is the suffix.  The name schema in above example has a descriptive suffix. The non\-descriptive suffix for the same termination is  '2/6/24' and name schema becomes 'DS/2/6/24'.  This object can not be modified if there is any termination existing in the media gateway
            	**type**\: bool
            
            .. attribute:: cmediagwcccfgdsnameprefix
            
            	This object specifies the prefix of the name schema for DS (Digital Subscriber) terminations. The value of this object must be unique among the  following objects\:        cMediaGwCcCfgDsNamePrefix        cMediaGwCcCfgRtpNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgDefRtpNamePrefix This object can not be modified when there is any DS termination existing in the media gateway. It is default to 'DS'
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: cmediagwcccfgrtpnameprefix
            
            	This object specifies the prefix of the name schema for RTP (Real\-Time Transport Protocol) terminations. The value of this object must be unique among the  following objects\:        cMediaGwCcCfgDsNamePrefix        cMediaGwCcCfgRtpNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgDefRtpNamePrefix This object can not be modified when there is any RTP termination type existing in the media gateway. It is default to 'RTP'
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: cmediagwcccfgaal1svcnameprefix
            
            	This object specifies the prefix of the name schema for voice over AAL1 SVC (Switched Virtual Circuit) terminations. The value of this object must be unique among the  following objects\:        cMediaGwCcCfgDsNamePrefix        cMediaGwCcCfgRtpNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgDefRtpNamePrefix This object can not be modified when there is any AAL1 SVC termination type existing in the media gateway. It is default to 'AAL1/SVC'
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: cmediagwcccfgaal2svcnameprefix
            
            	This object specifies the prefix of the name schema for voice over AAL2 SVC (Switched Virtual Circuit) terminations. The value of this object must be unique among the  following objects\:        cMediaGwCcCfgDsNamePrefix        cMediaGwCcCfgRtpNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgDefRtpNamePrefix This object can not be modified when there is any AAL2 SVC termination type existing in the media gateway. It is default to 'AAL2/SVC'
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: cmediagwcccfgclusterenabled
            
            	This object specifies the condition of the cluster generation in the call control.  A cluster is a group of endpoints that share a particular bearer possibility for connections among each other.  disabled(1) \- The generation of the cluster attribute               is disabled. enabled(2) \- Unconditionally generate the cluster              attribute. conditionalEnabled(3) \- The generation of the cluster                attribute is upon MGC request
            	**type**\:  :py:class:`Cmediagwcccfgclusterenabled <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry.Cmediagwcccfgclusterenabled>`
            
            .. attribute:: cmediagwcccfgdefbearertraffic
            
            	This object specifies the combination of the network type (IP/ATM), virtual circuit type (PVC/SVC) and ATM adaptation layer type (AAL1/AAL2/AAL5) for the connection used in transporting bearer traffic.      ipPvcAal5 (1) \- The bearer traffic is transported in                     IP network, through Permanent Virtual                     Circuit(PVC) over AAL5 adaptation layer.     atmPvcAal2 (2) \- The bearer traffic is transported in                      ATM network, through Permanent Virtual                      Circuit(PVC) over AAL2 adaptation layer.     atmSvcAal2 (3) \- The bearer traffic is transported in                      ATM network, through Switching Virtual                      Circuit(SVC) over AAL2 adaptation layer.     atmSvcAal1 (4) \- The bearer traffic is transported in                      ATM network, through Switching Virtual                      Circuit(SVC) over AAL1 adaptation layer.  In MGCP, if the call agent specifies the bear traffic type  in the local connection options (CRCX request),  configuration of this object will have no effect,  otherwise the value of this object will be used when  media gateway sending CRCX response
            	**type**\:  :py:class:`Cmediagwcccfgdefbearertraffic <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry.Cmediagwcccfgdefbearertraffic>`
            
            .. attribute:: cmediagwcccfgdefrtpnameprefix
            
            	This object specifies the prefix of the name schema for default RTP terminations. The value of this object must be unique among the  following objects\:        cMediaGwCcCfgDsNamePrefix        cMediaGwCcCfgRtpNamePrefix        cMediaGwCcCfgAal1SvcNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix  It is defaulted to 'TGWRTP'
            	**type**\: str
            
            	**length:** 1..64
            
            

            """

            _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
            _revision = '2009-02-25'

            def __init__(self):
                super(CISCOMEDIAGATEWAYMIB.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry, self).__init__()

                self.yang_name = "cMediaGwCallControlConfigEntry"
                self.yang_parent_name = "cMediaGwCallControlConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cmgwindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cmgwindex', YLeaf(YType.str, 'cmgwIndex')),
                    ('cmediagwcccfgcontroltos', YLeaf(YType.uint32, 'cMediaGwCcCfgControlTos')),
                    ('cmediagwcccfgbearertos', YLeaf(YType.uint32, 'cMediaGwCcCfgBearerTos')),
                    ('cmediagwcccfgntepayload', YLeaf(YType.uint32, 'cMediaGwCcCfgNtePayload')),
                    ('cmediagwcccfgnsepayload', YLeaf(YType.uint32, 'cMediaGwCcCfgNsePayload')),
                    ('cmediagwcccfgnseresptimer', YLeaf(YType.uint32, 'cMediaGwCcCfgNseRespTimer')),
                    ('cmediagwcccfgvbdjitterdelaymode', YLeaf(YType.enumeration, 'cMediaGwCcCfgVbdJitterDelayMode')),
                    ('cmediagwcccfgvbdjittermaxdelay', YLeaf(YType.uint32, 'cMediaGwCcCfgVbdJitterMaxDelay')),
                    ('cmediagwcccfgvbdjitternomdelay', YLeaf(YType.uint32, 'cMediaGwCcCfgVbdJitterNomDelay')),
                    ('cmediagwcccfgvbdjittermindelay', YLeaf(YType.uint32, 'cMediaGwCcCfgVbdJitterMinDelay')),
                    ('cmediagwcccfgdefaulttoneplanid', YLeaf(YType.uint32, 'cMediaGwCcCfgDefaultTonePlanId')),
                    ('cmediagwcccfgdescrinfoenabled', YLeaf(YType.boolean, 'cMediaGwCcCfgDescrInfoEnabled')),
                    ('cmediagwcccfgdsnameprefix', YLeaf(YType.str, 'cMediaGwCcCfgDsNamePrefix')),
                    ('cmediagwcccfgrtpnameprefix', YLeaf(YType.str, 'cMediaGwCcCfgRtpNamePrefix')),
                    ('cmediagwcccfgaal1svcnameprefix', YLeaf(YType.str, 'cMediaGwCcCfgAal1SvcNamePrefix')),
                    ('cmediagwcccfgaal2svcnameprefix', YLeaf(YType.str, 'cMediaGwCcCfgAal2SvcNamePrefix')),
                    ('cmediagwcccfgclusterenabled', YLeaf(YType.enumeration, 'cMediaGwCcCfgClusterEnabled')),
                    ('cmediagwcccfgdefbearertraffic', YLeaf(YType.enumeration, 'cMediaGwCcCfgDefBearerTraffic')),
                    ('cmediagwcccfgdefrtpnameprefix', YLeaf(YType.str, 'cMediaGwCcCfgDefRtpNamePrefix')),
                ])
                self.cmgwindex = None
                self.cmediagwcccfgcontroltos = None
                self.cmediagwcccfgbearertos = None
                self.cmediagwcccfgntepayload = None
                self.cmediagwcccfgnsepayload = None
                self.cmediagwcccfgnseresptimer = None
                self.cmediagwcccfgvbdjitterdelaymode = None
                self.cmediagwcccfgvbdjittermaxdelay = None
                self.cmediagwcccfgvbdjitternomdelay = None
                self.cmediagwcccfgvbdjittermindelay = None
                self.cmediagwcccfgdefaulttoneplanid = None
                self.cmediagwcccfgdescrinfoenabled = None
                self.cmediagwcccfgdsnameprefix = None
                self.cmediagwcccfgrtpnameprefix = None
                self.cmediagwcccfgaal1svcnameprefix = None
                self.cmediagwcccfgaal2svcnameprefix = None
                self.cmediagwcccfgclusterenabled = None
                self.cmediagwcccfgdefbearertraffic = None
                self.cmediagwcccfgdefrtpnameprefix = None
                self._segment_path = lambda: "cMediaGwCallControlConfigEntry" + "[cmgwIndex='" + str(self.cmgwindex) + "']"
                self._absolute_path = lambda: "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/cMediaGwCallControlConfigTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOMEDIAGATEWAYMIB.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry, ['cmgwindex', 'cmediagwcccfgcontroltos', 'cmediagwcccfgbearertos', 'cmediagwcccfgntepayload', 'cmediagwcccfgnsepayload', 'cmediagwcccfgnseresptimer', 'cmediagwcccfgvbdjitterdelaymode', 'cmediagwcccfgvbdjittermaxdelay', 'cmediagwcccfgvbdjitternomdelay', 'cmediagwcccfgvbdjittermindelay', 'cmediagwcccfgdefaulttoneplanid', 'cmediagwcccfgdescrinfoenabled', 'cmediagwcccfgdsnameprefix', 'cmediagwcccfgrtpnameprefix', 'cmediagwcccfgaal1svcnameprefix', 'cmediagwcccfgaal2svcnameprefix', 'cmediagwcccfgclusterenabled', 'cmediagwcccfgdefbearertraffic', 'cmediagwcccfgdefrtpnameprefix'], name, value)

            class Cmediagwcccfgclusterenabled(Enum):
                """
                Cmediagwcccfgclusterenabled (Enum Class)

                This object specifies the condition of the cluster generation

                in the call control.

                A cluster is a group of endpoints that share a particular

                bearer possibility for connections among each other.

                disabled(1) \- The generation of the cluster attribute

                              is disabled.

                enabled(2) \- Unconditionally generate the cluster

                             attribute.

                conditionalEnabled(3) \- The generation of the cluster 

                              attribute is upon MGC request.

                .. data:: disabled = 1

                .. data:: enabled = 2

                .. data:: conditionalEnabled = 3

                """

                disabled = Enum.YLeaf(1, "disabled")

                enabled = Enum.YLeaf(2, "enabled")

                conditionalEnabled = Enum.YLeaf(3, "conditionalEnabled")


            class Cmediagwcccfgdefbearertraffic(Enum):
                """
                Cmediagwcccfgdefbearertraffic (Enum Class)

                This object specifies the combination of the network

                type (IP/ATM), virtual circuit type (PVC/SVC) and

                ATM adaptation layer type (AAL1/AAL2/AAL5) for the

                connection used in transporting bearer traffic.

                    ipPvcAal5 (1) \- The bearer traffic is transported in

                                    IP network, through Permanent Virtual

                                    Circuit(PVC) over AAL5 adaptation layer.

                    atmPvcAal2 (2) \- The bearer traffic is transported in

                                     ATM network, through Permanent Virtual

                                     Circuit(PVC) over AAL2 adaptation layer.

                    atmSvcAal2 (3) \- The bearer traffic is transported in

                                     ATM network, through Switching Virtual

                                     Circuit(SVC) over AAL2 adaptation layer.

                    atmSvcAal1 (4) \- The bearer traffic is transported in

                                     ATM network, through Switching Virtual

                                     Circuit(SVC) over AAL1 adaptation layer.

                In MGCP, if the call agent specifies the bear traffic type 

                in the local connection options (CRCX request), 

                configuration of this object will have no effect, 

                otherwise the value of this object will be used when 

                media gateway sending CRCX response.

                .. data:: ipPvcAal5 = 1

                .. data:: atmPvcAal2 = 2

                .. data:: atmSvcAal2 = 3

                .. data:: atmSvcAal1 = 4

                """

                ipPvcAal5 = Enum.YLeaf(1, "ipPvcAal5")

                atmPvcAal2 = Enum.YLeaf(2, "atmPvcAal2")

                atmSvcAal2 = Enum.YLeaf(3, "atmSvcAal2")

                atmSvcAal1 = Enum.YLeaf(4, "atmSvcAal1")



    class Cmediagwrscstatstable(Entity):
        """
        This table stores the gateway resource statistics
        information.
        
        .. attribute:: cmediagwrscstatsentry
        
        	Each entry stores the statistics information for a specific resource
        	**type**\: list of  		 :py:class:`Cmediagwrscstatsentry <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwrscstatstable.Cmediagwrscstatsentry>`
        
        

        """

        _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
        _revision = '2009-02-25'

        def __init__(self):
            super(CISCOMEDIAGATEWAYMIB.Cmediagwrscstatstable, self).__init__()

            self.yang_name = "cMediaGwRscStatsTable"
            self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cMediaGwRscStatsEntry", ("cmediagwrscstatsentry", CISCOMEDIAGATEWAYMIB.Cmediagwrscstatstable.Cmediagwrscstatsentry))])
            self._leafs = OrderedDict()

            self.cmediagwrscstatsentry = YList(self)
            self._segment_path = lambda: "cMediaGwRscStatsTable"
            self._absolute_path = lambda: "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOMEDIAGATEWAYMIB.Cmediagwrscstatstable, [], name, value)


        class Cmediagwrscstatsentry(Entity):
            """
            Each entry stores the statistics
            information for a specific resource.
            
            .. attribute:: cmgwindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cmgwrscstatsindex  (key)
            
            	An index that uniquely identifies a specific gateway resource
            	**type**\:  :py:class:`Cmgwrscstatsindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwrscstatstable.Cmediagwrscstatsentry.Cmgwrscstatsindex>`
            
            .. attribute:: cmgwrscmaximumutilization
            
            	This object indicates the maximum utilization of the resource over the interval specified by the 'cmgwRscSinceLastReset'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmgwrscminimumutilization
            
            	This object indicates the minimum utilization of the resource over the interval specified by the 'cmgwRscSinceLastReset'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmgwrscaverageutilization
            
            	This object indicates the average utilization of the resource over the interval specified by the 'cmgwRscSinceLastReset'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmgwrscsincelastreset
            
            	The elapsed time (in seconds) from the last periodic reset.  The following objects are reset at the last reset\:      'cmgwRscMaximumUtilization'     'cmgwRscMinimumUtilization'     'cmgwRscAverageUtilization'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            

            """

            _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
            _revision = '2009-02-25'

            def __init__(self):
                super(CISCOMEDIAGATEWAYMIB.Cmediagwrscstatstable.Cmediagwrscstatsentry, self).__init__()

                self.yang_name = "cMediaGwRscStatsEntry"
                self.yang_parent_name = "cMediaGwRscStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cmgwindex','cmgwrscstatsindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cmgwindex', YLeaf(YType.str, 'cmgwIndex')),
                    ('cmgwrscstatsindex', YLeaf(YType.enumeration, 'cmgwRscStatsIndex')),
                    ('cmgwrscmaximumutilization', YLeaf(YType.uint32, 'cmgwRscMaximumUtilization')),
                    ('cmgwrscminimumutilization', YLeaf(YType.uint32, 'cmgwRscMinimumUtilization')),
                    ('cmgwrscaverageutilization', YLeaf(YType.uint32, 'cmgwRscAverageUtilization')),
                    ('cmgwrscsincelastreset', YLeaf(YType.uint32, 'cmgwRscSinceLastReset')),
                ])
                self.cmgwindex = None
                self.cmgwrscstatsindex = None
                self.cmgwrscmaximumutilization = None
                self.cmgwrscminimumutilization = None
                self.cmgwrscaverageutilization = None
                self.cmgwrscsincelastreset = None
                self._segment_path = lambda: "cMediaGwRscStatsEntry" + "[cmgwIndex='" + str(self.cmgwindex) + "']" + "[cmgwRscStatsIndex='" + str(self.cmgwrscstatsindex) + "']"
                self._absolute_path = lambda: "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/cMediaGwRscStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOMEDIAGATEWAYMIB.Cmediagwrscstatstable.Cmediagwrscstatsentry, ['cmgwindex', 'cmgwrscstatsindex', 'cmgwrscmaximumutilization', 'cmgwrscminimumutilization', 'cmgwrscaverageutilization', 'cmgwrscsincelastreset'], name, value)

            class Cmgwrscstatsindex(Enum):
                """
                Cmgwrscstatsindex (Enum Class)

                An index that uniquely identifies a specific gateway

                resource.

                .. data:: cpu = 1

                .. data:: staticmemory = 2

                .. data:: dynamicmemory = 3

                .. data:: sysmemory = 4

                .. data:: commbuffer = 5

                .. data:: msgq = 6

                .. data:: atmq = 7

                .. data:: svccongestion = 8

                .. data:: rsvpq = 9

                .. data:: dspq = 10

                .. data:: h248congestion = 11

                .. data:: callpersec = 12

                .. data:: smallipcbuffer = 13

                .. data:: mediumipcbuffer = 14

                .. data:: largeipcbuffer = 15

                .. data:: hugeipcbuffer = 16

                .. data:: mblkipcbuffer = 17

                """

                cpu = Enum.YLeaf(1, "cpu")

                staticmemory = Enum.YLeaf(2, "staticmemory")

                dynamicmemory = Enum.YLeaf(3, "dynamicmemory")

                sysmemory = Enum.YLeaf(4, "sysmemory")

                commbuffer = Enum.YLeaf(5, "commbuffer")

                msgq = Enum.YLeaf(6, "msgq")

                atmq = Enum.YLeaf(7, "atmq")

                svccongestion = Enum.YLeaf(8, "svccongestion")

                rsvpq = Enum.YLeaf(9, "rsvpq")

                dspq = Enum.YLeaf(10, "dspq")

                h248congestion = Enum.YLeaf(11, "h248congestion")

                callpersec = Enum.YLeaf(12, "callpersec")

                smallipcbuffer = Enum.YLeaf(13, "smallipcbuffer")

                mediumipcbuffer = Enum.YLeaf(14, "mediumipcbuffer")

                largeipcbuffer = Enum.YLeaf(15, "largeipcbuffer")

                hugeipcbuffer = Enum.YLeaf(16, "hugeipcbuffer")

                mblkipcbuffer = Enum.YLeaf(17, "mblkipcbuffer")


    def clone_ptr(self):
        self._top_entity = CISCOMEDIAGATEWAYMIB()
        return self._top_entity

