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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum

class CCallControlJitterDelayMode_Enum(Enum):
    """
    CCallControlJitterDelayMode_Enum

    This textual convention defines the jitter buffer mode in
    a call connection.
    
    adaptive(1) \- means to use jitter nominal delay as the 
                  initial jitter buffers size and let the DSP
                  pick the optimal value of the jitter buffer
                  size between the range of jitter maximum delay
                  and jitter minimum delay.
    
    fixed(2) \- means to use a constant jitter buffer size
               which is specified by jitter nominal delay.

    """

    ADAPTIVE = 1

    FIXED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
        return meta._meta_table['CCallControlJitterDelayMode_Enum']


class CGwAdminState_Enum(Enum):
    """
    CGwAdminState_Enum

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

    """

    INSERVICE = 1

    FORCEDOUTOFSERVICE = 2

    GRACEFULOUTOFSERVICE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
        return meta._meta_table['CGwAdminState_Enum']


class CGwServiceState_Enum(Enum):
    """
    CGwServiceState_Enum

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

    """

    INSERVICE = 1

    FORCEDOUTOFSERVICE = 2

    GRACEFULOUTOFSERVICE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
        return meta._meta_table['CGwServiceState_Enum']



class CISCOMEDIAGATEWAYMIB(object):
    """
    
    
    .. attribute:: cmediagwcallcontrolconfigtable
    
    	This table defines general call control attributes for the media gateway
    	**type**\: :py:class:`CMediaGwCallControlConfigTable <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CMediaGwCallControlConfigTable>`
    
    .. attribute:: cmediagwdnsipconfigtable
    
    	There is only one DNS name server on a gateway and the domain name of the DNS name server is put on  cMediaGwDomainNameConfigTable with 'dnsServer (2)'.  There could be multi IP addresses are associated with the DNS name server, this table is used to store these IP  addresses.  If any domain name using external resolution, the last entry of this table is not allowed to be deleted
    	**type**\: :py:class:`CMediaGwDnsIpConfigTable <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CMediaGwDnsIpConfigTable>`
    
    .. attribute:: cmediagwdomainnameconfigtable
    
    	This table provides the domain names which are configured by  users.  The domain names can be used to represent IP addresses  for\:     gateway     External DNS name server     MGC (call agent) 
    	**type**\: :py:class:`CMediaGwDomainNameConfigTable <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CMediaGwDomainNameConfigTable>`
    
    .. attribute:: cmediagwipconfigtable
    
    	This table contains a list of media gateway IP address and the IP address associated interface information.  If IP address associated interface is PVC, only  aal5 control PVC or aal5 bearer PVC are valid.        When the PVC is aal5 control, the IP address is used to  communicate to MGC; when the PVC is aal5 bearer, the IP address is used to communicate to other gateway. The PVC information is kept in cwAtmChanExtConfigTable\:  cwacChanPvcType\:      aal5/aal2/aal1  cwacChanApplication\:  control/bearer/signaling  If IP address associated interface is not PVC, refer to the  IP addresses associated interface table for the usage of IP address
    	**type**\: :py:class:`CMediaGwIpConfigTable <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CMediaGwIpConfigTable>`
    
    .. attribute:: cmediagwrscstatstable
    
    	This table stores the gateway resource statistics information
    	**type**\: :py:class:`CMediaGwRscStatsTable <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CMediaGwRscStatsTable>`
    
    .. attribute:: cmediagwtable
    
    	This table contains the global media gateway parameters information. It supports the modification of the global media gateway  parameters
    	**type**\: :py:class:`CMediaGwTable <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CMediaGwTable>`
    
    .. attribute:: cmgwliftable
    
    	This table is for managing LIF (Logical Interface)  in a media gateway.   LIF is a logical interface which groups the TDM  DSx1s associated with a set of packet resource partitions  (PVCs) in a media gateway.  LIF is used for\: 1. VoIP switching  2. VoATM switching 
    	**type**\: :py:class:`CmgwLifTable <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CmgwLifTable>`
    
    .. attribute:: cmgwsignalprotocoltable
    
    	This table contains the available signaling protocols that are supported by the media gateway for communication with MGCs
    	**type**\: :py:class:`CmgwSignalProtocolTable <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CmgwSignalProtocolTable>`
    
    

    """

    _prefix = 'cisco-media'
    _revision = '2009-02-25'

    def __init__(self):
        self.cmediagwcallcontrolconfigtable = CISCOMEDIAGATEWAYMIB.CMediaGwCallControlConfigTable()
        self.cmediagwcallcontrolconfigtable.parent = self
        self.cmediagwdnsipconfigtable = CISCOMEDIAGATEWAYMIB.CMediaGwDnsIpConfigTable()
        self.cmediagwdnsipconfigtable.parent = self
        self.cmediagwdomainnameconfigtable = CISCOMEDIAGATEWAYMIB.CMediaGwDomainNameConfigTable()
        self.cmediagwdomainnameconfigtable.parent = self
        self.cmediagwipconfigtable = CISCOMEDIAGATEWAYMIB.CMediaGwIpConfigTable()
        self.cmediagwipconfigtable.parent = self
        self.cmediagwrscstatstable = CISCOMEDIAGATEWAYMIB.CMediaGwRscStatsTable()
        self.cmediagwrscstatstable.parent = self
        self.cmediagwtable = CISCOMEDIAGATEWAYMIB.CMediaGwTable()
        self.cmediagwtable.parent = self
        self.cmgwliftable = CISCOMEDIAGATEWAYMIB.CmgwLifTable()
        self.cmgwliftable.parent = self
        self.cmgwsignalprotocoltable = CISCOMEDIAGATEWAYMIB.CmgwSignalProtocolTable()
        self.cmgwsignalprotocoltable.parent = self


    class CMediaGwCallControlConfigTable(object):
        """
        This table defines general call control attributes for
        the media gateway.
        
        .. attribute:: cmediagwcallcontrolconfigentry
        
        	One entry for each media gateway which supports call control  protocol
        	**type**\: list of :py:class:`CMediaGwCallControlConfigEntry <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CMediaGwCallControlConfigTable.CMediaGwCallControlConfigEntry>`
        
        

        """

        _prefix = 'cisco-media'
        _revision = '2009-02-25'

        def __init__(self):
            self.parent = None
            self.cmediagwcallcontrolconfigentry = YList()
            self.cmediagwcallcontrolconfigentry.parent = self
            self.cmediagwcallcontrolconfigentry.name = 'cmediagwcallcontrolconfigentry'


        class CMediaGwCallControlConfigEntry(object):
            """
            One entry for each media gateway which supports call control 
            protocol.
            
            .. attribute:: cmgwindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cmediagwcccfgaal1svcnameprefix
            
            	This object specifies the prefix of the name schema for voice over AAL1 SVC (Switched Virtual Circuit) terminations. The value of this object must be unique among the  following objects\:        cMediaGwCcCfgDsNamePrefix        cMediaGwCcCfgRtpNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgDefRtpNamePrefix This object can not be modified when there is any AAL1 SVC termination type existing in the media gateway. It is default to 'AAL1/SVC'
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cmediagwcccfgaal2svcnameprefix
            
            	This object specifies the prefix of the name schema for voice over AAL2 SVC (Switched Virtual Circuit) terminations. The value of this object must be unique among the  following objects\:        cMediaGwCcCfgDsNamePrefix        cMediaGwCcCfgRtpNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgDefRtpNamePrefix This object can not be modified when there is any AAL2 SVC termination type existing in the media gateway. It is default to 'AAL2/SVC'
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cmediagwcccfgbearertos
            
            	This object specifies Type Of Service (TOS) field of IP header for the voice payload packet in VoIP application
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cmediagwcccfgclusterenabled
            
            	This object specifies the condition of the cluster generation in the call control.  A cluster is a group of endpoints that share a particular bearer possibility for connections among each other.  disabled(1) \- The generation of the cluster attribute               is disabled. enabled(2) \- Unconditionally generate the cluster              attribute. conditionalEnabled(3) \- The generation of the cluster                attribute is upon MGC request
            	**type**\: :py:class:`CMediaGwCcCfgClusterEnabled_Enum <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CMediaGwCallControlConfigTable.CMediaGwCallControlConfigEntry.CMediaGwCcCfgClusterEnabled_Enum>`
            
            .. attribute:: cmediagwcccfgcontroltos
            
            	This object specifies Type Of Service (TOS) field of IP header for the signaling control packet in VoIP application
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cmediagwcccfgdefaulttoneplanid
            
            	This object specifies the default tone plan index (the value of cvtcTonePlanId) for the media gateway
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: cmediagwcccfgdefbearertraffic
            
            	This object specifies the combination of the network type (IP/ATM), virtual circuit type (PVC/SVC) and ATM adaptation layer type (AAL1/AAL2/AAL5) for the connection used in transporting bearer traffic.      ipPvcAal5 (1) \- The bearer traffic is transported in                     IP network, through Permanent Virtual                     Circuit(PVC) over AAL5 adaptation layer.     atmPvcAal2 (2) \- The bearer traffic is transported in                      ATM network, through Permanent Virtual                      Circuit(PVC) over AAL2 adaptation layer.     atmSvcAal2 (3) \- The bearer traffic is transported in                      ATM network, through Switching Virtual                      Circuit(SVC) over AAL2 adaptation layer.     atmSvcAal1 (4) \- The bearer traffic is transported in                      ATM network, through Switching Virtual                      Circuit(SVC) over AAL1 adaptation layer.  In MGCP, if the call agent specifies the bear traffic type  in the local connection options (CRCX request),  configuration of this object will have no effect,  otherwise the value of this object will be used when  media gateway sending CRCX response
            	**type**\: :py:class:`CMediaGwCcCfgDefBearerTraffic_Enum <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CMediaGwCallControlConfigTable.CMediaGwCallControlConfigEntry.CMediaGwCcCfgDefBearerTraffic_Enum>`
            
            .. attribute:: cmediagwcccfgdefrtpnameprefix
            
            	This object specifies the prefix of the name schema for default RTP terminations. The value of this object must be unique among the  following objects\:        cMediaGwCcCfgDsNamePrefix        cMediaGwCcCfgRtpNamePrefix        cMediaGwCcCfgAal1SvcNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix  It is defaulted to 'TGWRTP'
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cmediagwcccfgdescrinfoenabled
            
            	This object specifies whether the media gateway supports descriptive suffix of the name schema for terminations.  There are two parts in name schema of termination, prefix and suffix. For example the name schema for a DS (Digital Subscriber) termination, can be 'DS/OC3\_2/DS1\_6/DS0\_24'. It represents DS type termination in 2nd OC3 line,  6th DS1 and 24th DS0 channel. In this example, 'DS' is  the prefix, 'OC3\_2/DS1\_6/DS0\_24' is the suffix.  The name schema in above example has a descriptive suffix. The non\-descriptive suffix for the same termination is  '2/6/24' and name schema becomes 'DS/2/6/24'.  This object can not be modified if there is any termination existing in the media gateway
            	**type**\: bool
            
            .. attribute:: cmediagwcccfgdsnameprefix
            
            	This object specifies the prefix of the name schema for DS (Digital Subscriber) terminations. The value of this object must be unique among the  following objects\:        cMediaGwCcCfgDsNamePrefix        cMediaGwCcCfgRtpNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgDefRtpNamePrefix This object can not be modified when there is any DS termination existing in the media gateway. It is default to 'DS'
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cmediagwcccfgnsepayload
            
            	This object specifies NSE (Network Signaling Events) payload type
            	**type**\: int
            
            	**range:** 98..117
            
            .. attribute:: cmediagwcccfgnseresptimer
            
            	This object specifies Network Signaling Event (NSE) timeout value
            	**type**\: int
            
            	**range:** 250..10000
            
            .. attribute:: cmediagwcccfgntepayload
            
            	This object specifies NTE (Named Telephony Events) payload type
            	**type**\: int
            
            	**range:** 96..127
            
            .. attribute:: cmediagwcccfgrtpnameprefix
            
            	This object specifies the prefix of the name schema for RTP (Real\-Time Transport Protocol) terminations. The value of this object must be unique among the  following objects\:        cMediaGwCcCfgDsNamePrefix        cMediaGwCcCfgRtpNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgDefRtpNamePrefix This object can not be modified when there is any RTP termination type existing in the media gateway. It is default to 'RTP'
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cmediagwcccfgvbdjitterdelaymode
            
            	The object specifies the jitter buffer mode applied to a VBD (Voice Band Data) call connection.  adaptive \- means to use cMediaGwCcCfgVbdJitterNomDelay as            the initial jitter buffers size and let the DSP            pick the optimal value of the jitter buffer            size between the range of            cMediaGwCcCfgVbcJitterMaxDelay and            cMediaGwCcCfgVbcJitterMinDelay.  fixed \- means to use a constant jitter buffer size         which is specified by cMediaGwCcCfgVbdJitterNomDelay
            	**type**\: :py:class:`CCallControlJitterDelayMode_Enum <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CCallControlJitterDelayMode_Enum>`
            
            .. attribute:: cmediagwcccfgvbdjittermaxdelay
            
            	This object specifies the maximum jitter buffer size  in VBD (Voice Band Data)
            	**type**\: int
            
            	**range:** 20..135
            
            .. attribute:: cmediagwcccfgvbdjittermindelay
            
            	This object specifies the nominal jitter buffer size  in VBD (Voice Band Data)
            	**type**\: int
            
            	**range:** 0..135
            
            .. attribute:: cmediagwcccfgvbdjitternomdelay
            
            	This object specifies the nominal jitter buffer size  in VBD (Voice Band Data)
            	**type**\: int
            
            	**range:** 5..135
            
            

            """

            _prefix = 'cisco-media'
            _revision = '2009-02-25'

            def __init__(self):
                self.parent = None
                self.cmgwindex = None
                self.cmediagwcccfgaal1svcnameprefix = None
                self.cmediagwcccfgaal2svcnameprefix = None
                self.cmediagwcccfgbearertos = None
                self.cmediagwcccfgclusterenabled = None
                self.cmediagwcccfgcontroltos = None
                self.cmediagwcccfgdefaulttoneplanid = None
                self.cmediagwcccfgdefbearertraffic = None
                self.cmediagwcccfgdefrtpnameprefix = None
                self.cmediagwcccfgdescrinfoenabled = None
                self.cmediagwcccfgdsnameprefix = None
                self.cmediagwcccfgnsepayload = None
                self.cmediagwcccfgnseresptimer = None
                self.cmediagwcccfgntepayload = None
                self.cmediagwcccfgrtpnameprefix = None
                self.cmediagwcccfgvbdjitterdelaymode = None
                self.cmediagwcccfgvbdjittermaxdelay = None
                self.cmediagwcccfgvbdjittermindelay = None
                self.cmediagwcccfgvbdjitternomdelay = None

            class CMediaGwCcCfgClusterEnabled_Enum(Enum):
                """
                CMediaGwCcCfgClusterEnabled_Enum

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

                """

                DISABLED = 1

                ENABLED = 2

                CONDITIONALENABLED = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
                    return meta._meta_table['CISCOMEDIAGATEWAYMIB.CMediaGwCallControlConfigTable.CMediaGwCallControlConfigEntry.CMediaGwCcCfgClusterEnabled_Enum']


            class CMediaGwCcCfgDefBearerTraffic_Enum(Enum):
                """
                CMediaGwCcCfgDefBearerTraffic_Enum

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

                """

                IPPVCAAL5 = 1

                ATMPVCAAL2 = 2

                ATMSVCAAL2 = 3

                ATMSVCAAL1 = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
                    return meta._meta_table['CISCOMEDIAGATEWAYMIB.CMediaGwCallControlConfigTable.CMediaGwCallControlConfigEntry.CMediaGwCcCfgDefBearerTraffic_Enum']


            @property
            def _common_path(self):
                if self.cmgwindex is None:
                    raise YPYDataValidationError('Key property cmgwindex is None')

                return '/CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/CISCO-MEDIA-GATEWAY-MIB:cMediaGwCallControlConfigTable/CISCO-MEDIA-GATEWAY-MIB:cMediaGwCallControlConfigEntry[CISCO-MEDIA-GATEWAY-MIB:cmgwIndex = ' + str(self.cmgwindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cmgwindex is not None:
                    return True

                if self.cmediagwcccfgaal1svcnameprefix is not None:
                    return True

                if self.cmediagwcccfgaal2svcnameprefix is not None:
                    return True

                if self.cmediagwcccfgbearertos is not None:
                    return True

                if self.cmediagwcccfgclusterenabled is not None:
                    return True

                if self.cmediagwcccfgcontroltos is not None:
                    return True

                if self.cmediagwcccfgdefaulttoneplanid is not None:
                    return True

                if self.cmediagwcccfgdefbearertraffic is not None:
                    return True

                if self.cmediagwcccfgdefrtpnameprefix is not None:
                    return True

                if self.cmediagwcccfgdescrinfoenabled is not None:
                    return True

                if self.cmediagwcccfgdsnameprefix is not None:
                    return True

                if self.cmediagwcccfgnsepayload is not None:
                    return True

                if self.cmediagwcccfgnseresptimer is not None:
                    return True

                if self.cmediagwcccfgntepayload is not None:
                    return True

                if self.cmediagwcccfgrtpnameprefix is not None:
                    return True

                if self.cmediagwcccfgvbdjitterdelaymode is not None:
                    return True

                if self.cmediagwcccfgvbdjittermaxdelay is not None:
                    return True

                if self.cmediagwcccfgvbdjittermindelay is not None:
                    return True

                if self.cmediagwcccfgvbdjitternomdelay is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
                return meta._meta_table['CISCOMEDIAGATEWAYMIB.CMediaGwCallControlConfigTable.CMediaGwCallControlConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/CISCO-MEDIA-GATEWAY-MIB:cMediaGwCallControlConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cmediagwcallcontrolconfigentry is not None:
                for child_ref in self.cmediagwcallcontrolconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
            return meta._meta_table['CISCOMEDIAGATEWAYMIB.CMediaGwCallControlConfigTable']['meta_info']


    class CMediaGwDnsIpConfigTable(object):
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
        	**type**\: list of :py:class:`CMediaGwDnsIpConfigEntry <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CMediaGwDnsIpConfigTable.CMediaGwDnsIpConfigEntry>`
        
        

        """

        _prefix = 'cisco-media'
        _revision = '2009-02-25'

        def __init__(self):
            self.parent = None
            self.cmediagwdnsipconfigentry = YList()
            self.cmediagwdnsipconfigentry.parent = self
            self.cmediagwdnsipconfigentry.name = 'cmediagwdnsipconfigentry'


        class CMediaGwDnsIpConfigEntry(object):
            """
            Each entry represents an IP address of the DNS name 
            server.
            
            .. attribute:: cmgwdnsipindex
            
            	An index that uniquely identifies an IP address of DNS name server
            	**type**\: int
            
            	**range:** 1..6
            
            .. attribute:: cmgwindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cmgwdnsdomainname
            
            	The domain name of DNS name server.  The value of this object reflects the value of  cmgwConfigDomainName from the entry with a value of  'dnsServer(2)' for object cmgwConfigDomainNameEntity of  cMediaGwDomainNameConfigTable.  If there is no entry in cMediaGwDomainNameConfigTable with 'dnsServer(2)' of cmgwConfigDomainNameEntity, then the value of this object will be empty string
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cmgwdnsip
            
            	The IP address of DNS name server. The IP address of DNS name server must be unique in this table
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cmgwdnsiprowstatus
            
            	This object is used to add and delete an entry.  When an entry of the table is created, the value of this object should be set to 'createAndGo' and the following objects are mandatory\:     cmgwDnsIp  When the user wants to delete the entry, the value of this object should be set to 'destroy'.  The entry can not be modified if the value of this  object is 'active'
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cmgwdnsiptype
            
            	DNS name server IP address type
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            

            """

            _prefix = 'cisco-media'
            _revision = '2009-02-25'

            def __init__(self):
                self.parent = None
                self.cmgwdnsipindex = None
                self.cmgwindex = None
                self.cmgwdnsdomainname = None
                self.cmgwdnsip = None
                self.cmgwdnsiprowstatus = None
                self.cmgwdnsiptype = None

            @property
            def _common_path(self):
                if self.cmgwdnsipindex is None:
                    raise YPYDataValidationError('Key property cmgwdnsipindex is None')
                if self.cmgwindex is None:
                    raise YPYDataValidationError('Key property cmgwindex is None')

                return '/CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/CISCO-MEDIA-GATEWAY-MIB:cMediaGwDnsIpConfigTable/CISCO-MEDIA-GATEWAY-MIB:cMediaGwDnsIpConfigEntry[CISCO-MEDIA-GATEWAY-MIB:cmgwDnsIpIndex = ' + str(self.cmgwdnsipindex) + '][CISCO-MEDIA-GATEWAY-MIB:cmgwIndex = ' + str(self.cmgwindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cmgwdnsipindex is not None:
                    return True

                if self.cmgwindex is not None:
                    return True

                if self.cmgwdnsdomainname is not None:
                    return True

                if self.cmgwdnsip is not None:
                    return True

                if self.cmgwdnsiprowstatus is not None:
                    return True

                if self.cmgwdnsiptype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
                return meta._meta_table['CISCOMEDIAGATEWAYMIB.CMediaGwDnsIpConfigTable.CMediaGwDnsIpConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/CISCO-MEDIA-GATEWAY-MIB:cMediaGwDnsIpConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cmediagwdnsipconfigentry is not None:
                for child_ref in self.cmediagwdnsipconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
            return meta._meta_table['CISCOMEDIAGATEWAYMIB.CMediaGwDnsIpConfigTable']['meta_info']


    class CMediaGwDomainNameConfigTable(object):
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
        	**type**\: list of :py:class:`CMediaGwDomainNameConfigEntry <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CMediaGwDomainNameConfigTable.CMediaGwDomainNameConfigEntry>`
        
        

        """

        _prefix = 'cisco-media'
        _revision = '2009-02-25'

        def __init__(self):
            self.parent = None
            self.cmediagwdomainnameconfigentry = YList()
            self.cmediagwdomainnameconfigentry.parent = self
            self.cmediagwdomainnameconfigentry.name = 'cmediagwdomainnameconfigentry'


        class CMediaGwDomainNameConfigEntry(object):
            """
            Each entry represents a domain name used in the system.
            
            Creation and deletion are supported. Modification
            is prohibited.
            
            .. attribute:: cmgwconfigdomainnameindex
            
            	An index that is uniquely identifies a domain name configured in the system
            	**type**\: int
            
            	**range:** 1..128
            
            .. attribute:: cmgwindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cmgwconfigdomainname
            
            	This object specifies the domain name.  The domain name should be unique if there are more than one entries having the same value in the object  cmgwConfigDomainNameEntity. For example, the gateway domain name should be unique  if the cmgwConfigDomainNameEntity has the value of  'gateway(1)'
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cmgwconfigdomainnameentity
            
            	This object indicates which entity to use this domain name.  gateway(1)   \- The domain name of media gateway.                With the same cmgwIndex, there is one and                 only one entry allowed with the value                 'gateway(1)' of this object.  dnsServer(2) \- The domain name of DNS name server that is used                 by Media gateway to find Internet Network                 Address from a DNS name.  mgc(3)       \- The domain name of a MGC (Media Gateway                Controller) associated with the media                 gateway. 
            	**type**\: :py:class:`CmgwConfigDomainNameEntity_Enum <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CMediaGwDomainNameConfigTable.CMediaGwDomainNameConfigEntry.CmgwConfigDomainNameEntity_Enum>`
            
            .. attribute:: cmgwconfigdomainnamerowstatus
            
            	This object is used to add and delete an entry.  When an entry is created, the following objects are mandatory\:      cmgwConfigDomainName      cmgwConfigDomainNameEntity  When deleting domain name of DNS name server (cmgwConfigDomainNameEntity is dnsServer (2)), the  cMediaGwDnsIpConfigTable should be empty.  Adding/deleting entry with cmgwConfigDomainNameEntity of 'mgc' will cause adding/deleting entry in  cMgcConfigTable (CISCO\-MGC\-MIB) automatically.  The cmgwConfigDomainName and cmgwConfigDomainNameEntity can not be modified if the value of this object is 'active'. 
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'cisco-media'
            _revision = '2009-02-25'

            def __init__(self):
                self.parent = None
                self.cmgwconfigdomainnameindex = None
                self.cmgwindex = None
                self.cmgwconfigdomainname = None
                self.cmgwconfigdomainnameentity = None
                self.cmgwconfigdomainnamerowstatus = None

            class CmgwConfigDomainNameEntity_Enum(Enum):
                """
                CmgwConfigDomainNameEntity_Enum

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

                """

                GATEWAY = 1

                DNSSERVER = 2

                MGC = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
                    return meta._meta_table['CISCOMEDIAGATEWAYMIB.CMediaGwDomainNameConfigTable.CMediaGwDomainNameConfigEntry.CmgwConfigDomainNameEntity_Enum']


            @property
            def _common_path(self):
                if self.cmgwconfigdomainnameindex is None:
                    raise YPYDataValidationError('Key property cmgwconfigdomainnameindex is None')
                if self.cmgwindex is None:
                    raise YPYDataValidationError('Key property cmgwindex is None')

                return '/CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/CISCO-MEDIA-GATEWAY-MIB:cMediaGwDomainNameConfigTable/CISCO-MEDIA-GATEWAY-MIB:cMediaGwDomainNameConfigEntry[CISCO-MEDIA-GATEWAY-MIB:cmgwConfigDomainNameIndex = ' + str(self.cmgwconfigdomainnameindex) + '][CISCO-MEDIA-GATEWAY-MIB:cmgwIndex = ' + str(self.cmgwindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cmgwconfigdomainnameindex is not None:
                    return True

                if self.cmgwindex is not None:
                    return True

                if self.cmgwconfigdomainname is not None:
                    return True

                if self.cmgwconfigdomainnameentity is not None:
                    return True

                if self.cmgwconfigdomainnamerowstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
                return meta._meta_table['CISCOMEDIAGATEWAYMIB.CMediaGwDomainNameConfigTable.CMediaGwDomainNameConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/CISCO-MEDIA-GATEWAY-MIB:cMediaGwDomainNameConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cmediagwdomainnameconfigentry is not None:
                for child_ref in self.cmediagwdomainnameconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
            return meta._meta_table['CISCOMEDIAGATEWAYMIB.CMediaGwDomainNameConfigTable']['meta_info']


    class CMediaGwIpConfigTable(object):
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
        	**type**\: list of :py:class:`CMediaGwIpConfigEntry <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CMediaGwIpConfigTable.CMediaGwIpConfigEntry>`
        
        

        """

        _prefix = 'cisco-media'
        _revision = '2009-02-25'

        def __init__(self):
            self.parent = None
            self.cmediagwipconfigentry = YList()
            self.cmediagwipconfigentry.parent = self
            self.cmediagwipconfigentry.name = 'cmediagwipconfigentry'


        class CMediaGwIpConfigEntry(object):
            """
            A Media Gateway IP configuration entry. 
            Each entry represents a media gateway IP address for MGCs
            to communicate with the media gateway.
            
            .. attribute:: cmgwindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cmgwipconfigindex
            
            	A unique index to identify each media gateway IP address
            	**type**\: int
            
            	**range:** 1..64
            
            .. attribute:: cmgwipconfigaddress
            
            	The configured IP address of media gateway. This object can not be modified
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cmgwipconfigaddrtype
            
            	This object is the IP address type
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cmgwipconfigdefaultgwip
            
            	This object specifies cmgwIpConfigAddress of the entry will become the default gateway address. This object can be set to 'true' for only one entry in the table
            	**type**\: bool
            
            .. attribute:: cmgwipconfigforremotemapping
            
            	This object specifies whether the address defined in cmgwIpConfigAddress is the address mapping at the remote end of this PVC.   If this object is set to 'true', the address defined in cmgwIpConfigAddress is for the remote end of the PVC. If this object is set to 'false', the address defined in cmgwIpConfigAddress is for the local end of the PVC
            	**type**\: bool
            
            .. attribute:: cmgwipconfigifindex
            
            	This object is ifIndex of the interface which is associated to the media gateway IP address.  For ATM interface, the IP address should be associated to an existing PVC\:    cmgwIpConfigIfIndex represents port of the PVC    cmgwIpConfigVpi represents VPI of the PVC    cmgwIpConfigVci represents VCI of the PVC And one PVC only can be associated with one IP address.  If this object is set to zero which means the IP address is not associated to any interface
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cmgwipconfigrowstatus
            
            	This object is used to add and delete an entry.  When an entry of the table is created, the following  objects are mandatory\:     cmgwIpConfigIfIndex     cmgwIpConfigVpi     cmgwIpConfigVci     cmgwIpConfigAddress     cmgwIpConfigSubnetMask  These objects can not be modified after the value of this object is set to 'active'.  Modification can only be done by deleting and re\-adding the  entry again.  After the system verify the validity of the data, it will set the cmgwIpConfigRowStatus to 'active'
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cmgwipconfigsubnetmask
            
            	This object is used to specify the number of leading one    bits which from the mask to be logical\-ANDed with the media   gateway address before being compared to the value in the  cmgwIpCofigAddress.  Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bitwise logical\-AND of the mask formed from x with the value  of the corresponding instance of the cmgwIpCofigAddress  object is not equal to cmgwIpCofigAddress
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: cmgwipconfigvci
            
            	This object represents VCI of the PVC which is associated to the IP address. If the IP address is not associated to PVC, the value of this object is set to \-1
            	**type**\: int
            
            	**range:** \-1..65535
            
            .. attribute:: cmgwipconfigvpi
            
            	This object represents VPI of the PVC which is associated to the IP address. If the IP address is not associated to PVC, the value  of this object is set to \-1
            	**type**\: int
            
            	**range:** \-1..4095
            
            

            """

            _prefix = 'cisco-media'
            _revision = '2009-02-25'

            def __init__(self):
                self.parent = None
                self.cmgwindex = None
                self.cmgwipconfigindex = None
                self.cmgwipconfigaddress = None
                self.cmgwipconfigaddrtype = None
                self.cmgwipconfigdefaultgwip = None
                self.cmgwipconfigforremotemapping = None
                self.cmgwipconfigifindex = None
                self.cmgwipconfigrowstatus = None
                self.cmgwipconfigsubnetmask = None
                self.cmgwipconfigvci = None
                self.cmgwipconfigvpi = None

            @property
            def _common_path(self):
                if self.cmgwindex is None:
                    raise YPYDataValidationError('Key property cmgwindex is None')
                if self.cmgwipconfigindex is None:
                    raise YPYDataValidationError('Key property cmgwipconfigindex is None')

                return '/CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/CISCO-MEDIA-GATEWAY-MIB:cMediaGwIpConfigTable/CISCO-MEDIA-GATEWAY-MIB:cMediaGwIpConfigEntry[CISCO-MEDIA-GATEWAY-MIB:cmgwIndex = ' + str(self.cmgwindex) + '][CISCO-MEDIA-GATEWAY-MIB:cmgwIpConfigIndex = ' + str(self.cmgwipconfigindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cmgwindex is not None:
                    return True

                if self.cmgwipconfigindex is not None:
                    return True

                if self.cmgwipconfigaddress is not None:
                    return True

                if self.cmgwipconfigaddrtype is not None:
                    return True

                if self.cmgwipconfigdefaultgwip is not None:
                    return True

                if self.cmgwipconfigforremotemapping is not None:
                    return True

                if self.cmgwipconfigifindex is not None:
                    return True

                if self.cmgwipconfigrowstatus is not None:
                    return True

                if self.cmgwipconfigsubnetmask is not None:
                    return True

                if self.cmgwipconfigvci is not None:
                    return True

                if self.cmgwipconfigvpi is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
                return meta._meta_table['CISCOMEDIAGATEWAYMIB.CMediaGwIpConfigTable.CMediaGwIpConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/CISCO-MEDIA-GATEWAY-MIB:cMediaGwIpConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cmediagwipconfigentry is not None:
                for child_ref in self.cmediagwipconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
            return meta._meta_table['CISCOMEDIAGATEWAYMIB.CMediaGwIpConfigTable']['meta_info']


    class CMediaGwRscStatsTable(object):
        """
        This table stores the gateway resource statistics
        information.
        
        .. attribute:: cmediagwrscstatsentry
        
        	Each entry stores the statistics information for a specific resource
        	**type**\: list of :py:class:`CMediaGwRscStatsEntry <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CMediaGwRscStatsTable.CMediaGwRscStatsEntry>`
        
        

        """

        _prefix = 'cisco-media'
        _revision = '2009-02-25'

        def __init__(self):
            self.parent = None
            self.cmediagwrscstatsentry = YList()
            self.cmediagwrscstatsentry.parent = self
            self.cmediagwrscstatsentry.name = 'cmediagwrscstatsentry'


        class CMediaGwRscStatsEntry(object):
            """
            Each entry stores the statistics
            information for a specific resource.
            
            .. attribute:: cmgwindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cmgwrscstatsindex
            
            	An index that uniquely identifies a specific gateway resource
            	**type**\: :py:class:`CmgwRscStatsIndex_Enum <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CMediaGwRscStatsTable.CMediaGwRscStatsEntry.CmgwRscStatsIndex_Enum>`
            
            .. attribute:: cmgwrscaverageutilization
            
            	This object indicates the average utilization of the resource over the interval specified by the 'cmgwRscSinceLastReset'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmgwrscmaximumutilization
            
            	This object indicates the maximum utilization of the resource over the interval specified by the 'cmgwRscSinceLastReset'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmgwrscminimumutilization
            
            	This object indicates the minimum utilization of the resource over the interval specified by the 'cmgwRscSinceLastReset'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmgwrscsincelastreset
            
            	The elapsed time (in seconds) from the last periodic reset.  The following objects are reset at the last reset\:      'cmgwRscMaximumUtilization'     'cmgwRscMinimumUtilization'     'cmgwRscAverageUtilization'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-media'
            _revision = '2009-02-25'

            def __init__(self):
                self.parent = None
                self.cmgwindex = None
                self.cmgwrscstatsindex = None
                self.cmgwrscaverageutilization = None
                self.cmgwrscmaximumutilization = None
                self.cmgwrscminimumutilization = None
                self.cmgwrscsincelastreset = None

            class CmgwRscStatsIndex_Enum(Enum):
                """
                CmgwRscStatsIndex_Enum

                An index that uniquely identifies a specific gateway
                resource.

                """

                CPU = 1

                STATICMEMORY = 2

                DYNAMICMEMORY = 3

                SYSMEMORY = 4

                COMMBUFFER = 5

                MSGQ = 6

                ATMQ = 7

                SVCCONGESTION = 8

                RSVPQ = 9

                DSPQ = 10

                H248CONGESTION = 11

                CALLPERSEC = 12

                SMALLIPCBUFFER = 13

                MEDIUMIPCBUFFER = 14

                LARGEIPCBUFFER = 15

                HUGEIPCBUFFER = 16

                MBLKIPCBUFFER = 17


                @staticmethod
                def _meta_info():
                    from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
                    return meta._meta_table['CISCOMEDIAGATEWAYMIB.CMediaGwRscStatsTable.CMediaGwRscStatsEntry.CmgwRscStatsIndex_Enum']


            @property
            def _common_path(self):
                if self.cmgwindex is None:
                    raise YPYDataValidationError('Key property cmgwindex is None')
                if self.cmgwrscstatsindex is None:
                    raise YPYDataValidationError('Key property cmgwrscstatsindex is None')

                return '/CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/CISCO-MEDIA-GATEWAY-MIB:cMediaGwRscStatsTable/CISCO-MEDIA-GATEWAY-MIB:cMediaGwRscStatsEntry[CISCO-MEDIA-GATEWAY-MIB:cmgwIndex = ' + str(self.cmgwindex) + '][CISCO-MEDIA-GATEWAY-MIB:cmgwRscStatsIndex = ' + str(self.cmgwrscstatsindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cmgwindex is not None:
                    return True

                if self.cmgwrscstatsindex is not None:
                    return True

                if self.cmgwrscaverageutilization is not None:
                    return True

                if self.cmgwrscmaximumutilization is not None:
                    return True

                if self.cmgwrscminimumutilization is not None:
                    return True

                if self.cmgwrscsincelastreset is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
                return meta._meta_table['CISCOMEDIAGATEWAYMIB.CMediaGwRscStatsTable.CMediaGwRscStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/CISCO-MEDIA-GATEWAY-MIB:cMediaGwRscStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cmediagwrscstatsentry is not None:
                for child_ref in self.cmediagwrscstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
            return meta._meta_table['CISCOMEDIAGATEWAYMIB.CMediaGwRscStatsTable']['meta_info']


    class CMediaGwTable(object):
        """
        This table contains the global media gateway parameters
        information.
        It supports the modification of the global media gateway 
        parameters.
        
        .. attribute:: cmediagwentry
        
        	A Media Gateway Entry.   At system power\-up, an entry is created by the agent  if the system detects a media gateway module has been added  to the system, and an entry is deleted if the entry associated media gateway module has been removed from the system
        	**type**\: list of :py:class:`CMediaGwEntry <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CMediaGwTable.CMediaGwEntry>`
        
        

        """

        _prefix = 'cisco-media'
        _revision = '2009-02-25'

        def __init__(self):
            self.parent = None
            self.cmediagwentry = YList()
            self.cmediagwentry.parent = self
            self.cmediagwentry.name = 'cmediagwentry'


        class CMediaGwEntry(object):
            """
            A Media Gateway Entry.  
            At system power\-up, an entry is created by the agent 
            if the system detects a media gateway module has been added 
            to the system, and an entry is deleted if the entry associated
            media gateway module has been removed from the system.
            
            .. attribute:: cmgwindex
            
            	An index that uniquely identifies an entry in the  cMediaGwTable
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cmgwadminstate
            
            	This object is used to change the service state of  the Media Gateway from inService to outOfService or from  outOfService to inService.  The resulting service state of the gateway is represented   by 'cmgwServiceState'
            	**type**\: :py:class:`CGwAdminState_Enum <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CGwAdminState_Enum>`
            
            .. attribute:: cmgwdomainname
            
            	This object is used to represent a domain name under which    the Media Gateway could also be registered in a DNS name server.   The value of this object reflects the value of  cmgwConfigDomainName from the entry with a value of  'gateway(1)' for object cmgwConfigDomainNameEntity of  cMediaGwDomainNameConfigTable.  If there is no entry in cMediaGwDomainNameConfigTable with 'gateway(1)' of cmgwConfigDomainNameEntity, then the value of this object will be empty string
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: cmgwgracetime
            
            	This object is used to represent grace period. The grace period (restart delay in RSIP message) is   expressed in a number of seconds.  It means how soon the gateway will be taken out of service. The value \-1 indicates that the grace period time is disabled
            	**type**\: int
            
            	**range:** \-1..65535
            
            .. attribute:: cmgwlawinterceptenabled
            
            	This object is used to enable or disable the lawful intercept for government. as follows\:   'true'  \- enable lawful intercept   'false' \- disable lawful intercept
            	**type**\: bool
            
            .. attribute:: cmgwphysicalindex
            
            	This object represents the entPhysicalIndex of the card in which media gateway is running. It will contain value 0 if the entPhysicalIndex value is not available or  not applicable
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cmgwservicestate
            
            	This object indicates the current service state of the Media  Gateway. This object is controlled by 'cmgwAdminState'  object
            	**type**\: :py:class:`CGwServiceState_Enum <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CGwServiceState_Enum>`
            
            .. attribute:: cmgwsrcfilterenabled
            
            	This object is used to enable or disable the source IP and port filtering with MGC for security consideration as follows\:   'true'  \- source IP and port filter is enabled    'false' \- source IP and port filter is disable 
            	**type**\: bool
            
            .. attribute:: cmgwv23enabled
            
            	This object is to enable or disable V23 tone. Setting the object value to 'true', will cause VXSM (Voice Switching Service Module) to detect V23 tone
            	**type**\: bool
            
            .. attribute:: cmgwvtmappingmode
            
            	This object is used to represent the VT (sonet Virtual Tributary) counting.  standard \- standard counting (based on Bellcore TR253) titan    \- TITAN5500 counting (based on Tellabs TITAN 5500)  Note\: 'titan' is valid only if sonet line medium type        (sonetMediumType of SONET\-MIB) is 'sonet' and        sonet path payload type (cspSonetPathPayload of       CISCO\-SONET\-MIB) is 'vt15vc11'
            	**type**\: :py:class:`CmgwVtMappingMode_Enum <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CMediaGwTable.CMediaGwEntry.CmgwVtMappingMode_Enum>`
            
            

            """

            _prefix = 'cisco-media'
            _revision = '2009-02-25'

            def __init__(self):
                self.parent = None
                self.cmgwindex = None
                self.cmgwadminstate = None
                self.cmgwdomainname = None
                self.cmgwgracetime = None
                self.cmgwlawinterceptenabled = None
                self.cmgwphysicalindex = None
                self.cmgwservicestate = None
                self.cmgwsrcfilterenabled = None
                self.cmgwv23enabled = None
                self.cmgwvtmappingmode = None

            class CmgwVtMappingMode_Enum(Enum):
                """
                CmgwVtMappingMode_Enum

                This object is used to represent the VT (sonet Virtual
                Tributary) counting.
                
                standard \- standard counting (based on Bellcore TR253)
                titan    \- TITAN5500 counting (based on Tellabs TITAN 5500)
                
                Note\: 'titan' is valid only if sonet line medium type 
                      (sonetMediumType of SONET\-MIB) is 'sonet' and 
                      sonet path payload type (cspSonetPathPayload of
                      CISCO\-SONET\-MIB) is 'vt15vc11'.

                """

                STANDARD = 1

                TITAN = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
                    return meta._meta_table['CISCOMEDIAGATEWAYMIB.CMediaGwTable.CMediaGwEntry.CmgwVtMappingMode_Enum']


            @property
            def _common_path(self):
                if self.cmgwindex is None:
                    raise YPYDataValidationError('Key property cmgwindex is None')

                return '/CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/CISCO-MEDIA-GATEWAY-MIB:cMediaGwTable/CISCO-MEDIA-GATEWAY-MIB:cMediaGwEntry[CISCO-MEDIA-GATEWAY-MIB:cmgwIndex = ' + str(self.cmgwindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cmgwindex is not None:
                    return True

                if self.cmgwadminstate is not None:
                    return True

                if self.cmgwdomainname is not None:
                    return True

                if self.cmgwgracetime is not None:
                    return True

                if self.cmgwlawinterceptenabled is not None:
                    return True

                if self.cmgwphysicalindex is not None:
                    return True

                if self.cmgwservicestate is not None:
                    return True

                if self.cmgwsrcfilterenabled is not None:
                    return True

                if self.cmgwv23enabled is not None:
                    return True

                if self.cmgwvtmappingmode is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
                return meta._meta_table['CISCOMEDIAGATEWAYMIB.CMediaGwTable.CMediaGwEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/CISCO-MEDIA-GATEWAY-MIB:cMediaGwTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cmediagwentry is not None:
                for child_ref in self.cmediagwentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
            return meta._meta_table['CISCOMEDIAGATEWAYMIB.CMediaGwTable']['meta_info']


    class CmgwLifTable(object):
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
        	**type**\: list of :py:class:`CmgwLifEntry <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CmgwLifTable.CmgwLifEntry>`
        
        

        """

        _prefix = 'cisco-media'
        _revision = '2009-02-25'

        def __init__(self):
            self.parent = None
            self.cmgwlifentry = YList()
            self.cmgwlifentry.parent = self
            self.cmgwlifentry.name = 'cmgwlifentry'


        class CmgwLifEntry(object):
            """
            An entry of this table is created by the media gateway
            when it supports the VoIP/VoATM application.
            
            .. attribute:: cmgwindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cmgwlifnumber
            
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

            _prefix = 'cisco-media'
            _revision = '2009-02-25'

            def __init__(self):
                self.parent = None
                self.cmgwindex = None
                self.cmgwlifnumber = None
                self.cmgwlifpvccount = None
                self.cmgwlifvoiceifcount = None

            @property
            def _common_path(self):
                if self.cmgwindex is None:
                    raise YPYDataValidationError('Key property cmgwindex is None')
                if self.cmgwlifnumber is None:
                    raise YPYDataValidationError('Key property cmgwlifnumber is None')

                return '/CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/CISCO-MEDIA-GATEWAY-MIB:cmgwLifTable/CISCO-MEDIA-GATEWAY-MIB:cmgwLifEntry[CISCO-MEDIA-GATEWAY-MIB:cmgwIndex = ' + str(self.cmgwindex) + '][CISCO-MEDIA-GATEWAY-MIB:cmgwLifNumber = ' + str(self.cmgwlifnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cmgwindex is not None:
                    return True

                if self.cmgwlifnumber is not None:
                    return True

                if self.cmgwlifpvccount is not None:
                    return True

                if self.cmgwlifvoiceifcount is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
                return meta._meta_table['CISCOMEDIAGATEWAYMIB.CmgwLifTable.CmgwLifEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/CISCO-MEDIA-GATEWAY-MIB:cmgwLifTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cmgwlifentry is not None:
                for child_ref in self.cmgwlifentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
            return meta._meta_table['CISCOMEDIAGATEWAYMIB.CmgwLifTable']['meta_info']


    class CmgwSignalProtocolTable(object):
        """
        This table contains the available signaling protocols that
        are supported by the media gateway for communication with
        MGCs.
        
        .. attribute:: cmgwsignalprotocolentry
        
        	Each entry represents an signaling protocol supported by the media gateway
        	**type**\: list of :py:class:`CmgwSignalProtocolEntry <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CmgwSignalProtocolTable.CmgwSignalProtocolEntry>`
        
        

        """

        _prefix = 'cisco-media'
        _revision = '2009-02-25'

        def __init__(self):
            self.parent = None
            self.cmgwsignalprotocolentry = YList()
            self.cmgwsignalprotocolentry.parent = self
            self.cmgwsignalprotocolentry.name = 'cmgwsignalprotocolentry'


        class CmgwSignalProtocolEntry(object):
            """
            Each entry represents an signaling protocol supported
            by the media gateway.
            
            .. attribute:: cmgwindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cmgwsignalprotocolindex
            
            	An index that uniquely identifies an entry in cmgwSignalProtocolTable
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: cmgwsignalmgcprotocolport
            
            	This object specifies the protocol port of the Media Gateway Controller (MGC). If the value of cmgwSignalProtocol is 'mgcp(2)' or 'tgcp(4)' and the value of cmgwSignalProtcolVersion is '1.0', the default value of this object is '2427'. If the value of cmgwSignalProtocol is 'h248(3)' and the value of cmgwSignalProtcolVersion is '1.0', the default value of this object is '2944'
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cmgwsignalprotocol
            
            	This object is used to represent the protocol type. other \- None of the following types. mgcp  \- Media Gateway Control Protocol h248 \- Media Gateway Control (ITU H.248) tgcp \- Trunking Gateway Control Protocol
            	**type**\: :py:class:`CmgwSignalProtocol_Enum <ydk.models.media.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.CmgwSignalProtocolTable.CmgwSignalProtocolEntry.CmgwSignalProtocol_Enum>`
            
            .. attribute:: cmgwsignalprotocolconfigver
            
            	This object specifies the protocol version used by the gateway in the messages to MGC in order to exchange the service capabilities.  For example cmgwSignalProtocol is 'h248(3)' and this object can be string '1' or '1.0', '2' or '2.0'.   'MAX' is a special string indicating the gateway will use the highest protocol version supported in the  gateway, but it can be changed to lower version after  it negotiates with MGC. The final negotiated protocol version will be indicated in cmgwSignalProtocolVersion.  The version strings other than 'MAX' can be specified for the gateway to communicate with the MGC which doesn't support service capabilities negotiation. For example if a MGC supports only version 1.0 MGCP, this object should be set to '1' to instruct the gateway using MGCP  version 1.0 format messages to communicate with MGC. 
            	**type**\: str
            
            	**range:** 1..16
            
            .. attribute:: cmgwsignalprotocolport
            
            	This object is used to represent the UDP port associated  with the protocol. If the value of cmgwSignalProtocol is 'mgcp(2)' and the value of cmgwSignalProtcolVersion is '1.0', the default value of this object is '2727'.  If the value of cmgwSignalProtocol is 'h248(3)' and the value of cmgwSignalProtcolVersion is '1.0', the default value of this object is '2944'
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cmgwsignalprotocolpreference
            
            	This object specifies the preference of the signal protocol  supported in the media gateway.  If this object is set to 0, the corresponding signal protocol will not be used by the gateway.   The value of this object is unique within the corresponding gateway. The entry with lower value has higher preference
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cmgwsignalprotocolversion
            
            	This object is used to represent the protocol version.  For example cmgwSignalProtocol is 'mgcp(2)' and this object is string '1.0'. cmgwSignalProtocol is  'h248(3)' and this object is set to '2.0'
            	**type**\: str
            
            	**range:** 1..16
            
            

            """

            _prefix = 'cisco-media'
            _revision = '2009-02-25'

            def __init__(self):
                self.parent = None
                self.cmgwindex = None
                self.cmgwsignalprotocolindex = None
                self.cmgwsignalmgcprotocolport = None
                self.cmgwsignalprotocol = None
                self.cmgwsignalprotocolconfigver = None
                self.cmgwsignalprotocolport = None
                self.cmgwsignalprotocolpreference = None
                self.cmgwsignalprotocolversion = None

            class CmgwSignalProtocol_Enum(Enum):
                """
                CmgwSignalProtocol_Enum

                This object is used to represent the protocol type.
                other \- None of the following types.
                mgcp  \- Media Gateway Control Protocol
                h248 \- Media Gateway Control (ITU H.248)
                tgcp \- Trunking Gateway Control Protocol

                """

                OTHER = 1

                MGCP = 2

                H248 = 3

                TGCP = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
                    return meta._meta_table['CISCOMEDIAGATEWAYMIB.CmgwSignalProtocolTable.CmgwSignalProtocolEntry.CmgwSignalProtocol_Enum']


            @property
            def _common_path(self):
                if self.cmgwindex is None:
                    raise YPYDataValidationError('Key property cmgwindex is None')
                if self.cmgwsignalprotocolindex is None:
                    raise YPYDataValidationError('Key property cmgwsignalprotocolindex is None')

                return '/CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/CISCO-MEDIA-GATEWAY-MIB:cmgwSignalProtocolTable/CISCO-MEDIA-GATEWAY-MIB:cmgwSignalProtocolEntry[CISCO-MEDIA-GATEWAY-MIB:cmgwIndex = ' + str(self.cmgwindex) + '][CISCO-MEDIA-GATEWAY-MIB:cmgwSignalProtocolIndex = ' + str(self.cmgwsignalprotocolindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cmgwindex is not None:
                    return True

                if self.cmgwsignalprotocolindex is not None:
                    return True

                if self.cmgwsignalmgcprotocolport is not None:
                    return True

                if self.cmgwsignalprotocol is not None:
                    return True

                if self.cmgwsignalprotocolconfigver is not None:
                    return True

                if self.cmgwsignalprotocolport is not None:
                    return True

                if self.cmgwsignalprotocolpreference is not None:
                    return True

                if self.cmgwsignalprotocolversion is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
                return meta._meta_table['CISCOMEDIAGATEWAYMIB.CmgwSignalProtocolTable.CmgwSignalProtocolEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/CISCO-MEDIA-GATEWAY-MIB:cmgwSignalProtocolTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cmgwsignalprotocolentry is not None:
                for child_ref in self.cmgwsignalprotocolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
            return meta._meta_table['CISCOMEDIAGATEWAYMIB.CmgwSignalProtocolTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cmediagwcallcontrolconfigtable is not None and self.cmediagwcallcontrolconfigtable._has_data():
            return True

        if self.cmediagwcallcontrolconfigtable is not None and self.cmediagwcallcontrolconfigtable.is_presence():
            return True

        if self.cmediagwdnsipconfigtable is not None and self.cmediagwdnsipconfigtable._has_data():
            return True

        if self.cmediagwdnsipconfigtable is not None and self.cmediagwdnsipconfigtable.is_presence():
            return True

        if self.cmediagwdomainnameconfigtable is not None and self.cmediagwdomainnameconfigtable._has_data():
            return True

        if self.cmediagwdomainnameconfigtable is not None and self.cmediagwdomainnameconfigtable.is_presence():
            return True

        if self.cmediagwipconfigtable is not None and self.cmediagwipconfigtable._has_data():
            return True

        if self.cmediagwipconfigtable is not None and self.cmediagwipconfigtable.is_presence():
            return True

        if self.cmediagwrscstatstable is not None and self.cmediagwrscstatstable._has_data():
            return True

        if self.cmediagwrscstatstable is not None and self.cmediagwrscstatstable.is_presence():
            return True

        if self.cmediagwtable is not None and self.cmediagwtable._has_data():
            return True

        if self.cmediagwtable is not None and self.cmediagwtable.is_presence():
            return True

        if self.cmgwliftable is not None and self.cmgwliftable._has_data():
            return True

        if self.cmgwliftable is not None and self.cmgwliftable.is_presence():
            return True

        if self.cmgwsignalprotocoltable is not None and self.cmgwsignalprotocoltable._has_data():
            return True

        if self.cmgwsignalprotocoltable is not None and self.cmgwsignalprotocoltable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.media._meta import _CISCO_MEDIA_GATEWAY_MIB as meta
        return meta._meta_table['CISCOMEDIAGATEWAYMIB']['meta_info']


