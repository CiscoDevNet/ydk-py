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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ccallcontroljitterdelaymode(Enum):
    """
    Ccallcontroljitterdelaymode

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


class Cgwadminstate(Enum):
    """
    Cgwadminstate

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


class Cgwservicestate(Enum):
    """
    Cgwservicestate

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



class CiscoMediaGatewayMib(Entity):
    """
    
    
    .. attribute:: cmediagwcallcontrolconfigtable
    
    	This table defines general call control attributes for the media gateway
    	**type**\:   :py:class:`Cmediagwcallcontrolconfigtable <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable>`
    
    .. attribute:: cmediagwdnsipconfigtable
    
    	There is only one DNS name server on a gateway and the domain name of the DNS name server is put on  cMediaGwDomainNameConfigTable with 'dnsServer (2)'.  There could be multi IP addresses are associated with the DNS name server, this table is used to store these IP  addresses.  If any domain name using external resolution, the last entry of this table is not allowed to be deleted
    	**type**\:   :py:class:`Cmediagwdnsipconfigtable <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwdnsipconfigtable>`
    
    .. attribute:: cmediagwdomainnameconfigtable
    
    	This table provides the domain names which are configured by  users.  The domain names can be used to represent IP addresses  for\:     gateway     External DNS name server     MGC (call agent) 
    	**type**\:   :py:class:`Cmediagwdomainnameconfigtable <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable>`
    
    .. attribute:: cmediagwipconfigtable
    
    	This table contains a list of media gateway IP address and the IP address associated interface information.  If IP address associated interface is PVC, only  aal5 control PVC or aal5 bearer PVC are valid.        When the PVC is aal5 control, the IP address is used to  communicate to MGC; when the PVC is aal5 bearer, the IP address is used to communicate to other gateway. The PVC information is kept in cwAtmChanExtConfigTable\:  cwacChanPvcType\:      aal5/aal2/aal1  cwacChanApplication\:  control/bearer/signaling  If IP address associated interface is not PVC, refer to the  IP addresses associated interface table for the usage of IP address
    	**type**\:   :py:class:`Cmediagwipconfigtable <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwipconfigtable>`
    
    .. attribute:: cmediagwrscstatstable
    
    	This table stores the gateway resource statistics information
    	**type**\:   :py:class:`Cmediagwrscstatstable <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwrscstatstable>`
    
    .. attribute:: cmediagwtable
    
    	This table contains the global media gateway parameters information. It supports the modification of the global media gateway  parameters
    	**type**\:   :py:class:`Cmediagwtable <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwtable>`
    
    .. attribute:: cmgwliftable
    
    	This table is for managing LIF (Logical Interface)  in a media gateway.   LIF is a logical interface which groups the TDM  DSx1s associated with a set of packet resource partitions  (PVCs) in a media gateway.  LIF is used for\: 1. VoIP switching  2. VoATM switching 
    	**type**\:   :py:class:`Cmgwliftable <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmgwliftable>`
    
    .. attribute:: cmgwsignalprotocoltable
    
    	This table contains the available signaling protocols that are supported by the media gateway for communication with MGCs
    	**type**\:   :py:class:`Cmgwsignalprotocoltable <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmgwsignalprotocoltable>`
    
    

    """

    _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
    _revision = '2009-02-25'

    def __init__(self):
        super(CiscoMediaGatewayMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-MEDIA-GATEWAY-MIB"
        self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"

        self.cmediagwcallcontrolconfigtable = CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable()
        self.cmediagwcallcontrolconfigtable.parent = self
        self._children_name_map["cmediagwcallcontrolconfigtable"] = "cMediaGwCallControlConfigTable"
        self._children_yang_names.add("cMediaGwCallControlConfigTable")

        self.cmediagwdnsipconfigtable = CiscoMediaGatewayMib.Cmediagwdnsipconfigtable()
        self.cmediagwdnsipconfigtable.parent = self
        self._children_name_map["cmediagwdnsipconfigtable"] = "cMediaGwDnsIpConfigTable"
        self._children_yang_names.add("cMediaGwDnsIpConfigTable")

        self.cmediagwdomainnameconfigtable = CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable()
        self.cmediagwdomainnameconfigtable.parent = self
        self._children_name_map["cmediagwdomainnameconfigtable"] = "cMediaGwDomainNameConfigTable"
        self._children_yang_names.add("cMediaGwDomainNameConfigTable")

        self.cmediagwipconfigtable = CiscoMediaGatewayMib.Cmediagwipconfigtable()
        self.cmediagwipconfigtable.parent = self
        self._children_name_map["cmediagwipconfigtable"] = "cMediaGwIpConfigTable"
        self._children_yang_names.add("cMediaGwIpConfigTable")

        self.cmediagwrscstatstable = CiscoMediaGatewayMib.Cmediagwrscstatstable()
        self.cmediagwrscstatstable.parent = self
        self._children_name_map["cmediagwrscstatstable"] = "cMediaGwRscStatsTable"
        self._children_yang_names.add("cMediaGwRscStatsTable")

        self.cmediagwtable = CiscoMediaGatewayMib.Cmediagwtable()
        self.cmediagwtable.parent = self
        self._children_name_map["cmediagwtable"] = "cMediaGwTable"
        self._children_yang_names.add("cMediaGwTable")

        self.cmgwliftable = CiscoMediaGatewayMib.Cmgwliftable()
        self.cmgwliftable.parent = self
        self._children_name_map["cmgwliftable"] = "cmgwLifTable"
        self._children_yang_names.add("cmgwLifTable")

        self.cmgwsignalprotocoltable = CiscoMediaGatewayMib.Cmgwsignalprotocoltable()
        self.cmgwsignalprotocoltable.parent = self
        self._children_name_map["cmgwsignalprotocoltable"] = "cmgwSignalProtocolTable"
        self._children_yang_names.add("cmgwSignalProtocolTable")


    class Cmediagwtable(Entity):
        """
        This table contains the global media gateway parameters
        information.
        It supports the modification of the global media gateway 
        parameters.
        
        .. attribute:: cmediagwentry
        
        	A Media Gateway Entry.   At system power\-up, an entry is created by the agent  if the system detects a media gateway module has been added  to the system, and an entry is deleted if the entry associated media gateway module has been removed from the system
        	**type**\: list of    :py:class:`Cmediagwentry <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry>`
        
        

        """

        _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
        _revision = '2009-02-25'

        def __init__(self):
            super(CiscoMediaGatewayMib.Cmediagwtable, self).__init__()

            self.yang_name = "cMediaGwTable"
            self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"

            self.cmediagwentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoMediaGatewayMib.Cmediagwtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoMediaGatewayMib.Cmediagwtable, self).__setattr__(name, value)


        class Cmediagwentry(Entity):
            """
            A Media Gateway Entry.  
            At system power\-up, an entry is created by the agent 
            if the system detects a media gateway module has been added 
            to the system, and an entry is deleted if the entry associated
            media gateway module has been removed from the system.
            
            .. attribute:: cmgwindex  <key>
            
            	An index that uniquely identifies an entry in the  cMediaGwTable
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cmgwadminstate
            
            	This object is used to change the service state of  the Media Gateway from inService to outOfService or from  outOfService to inService.  The resulting service state of the gateway is represented   by 'cmgwServiceState'
            	**type**\:   :py:class:`Cgwadminstate <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.Cgwadminstate>`
            
            .. attribute:: cmgwdomainname
            
            	This object is used to represent a domain name under which    the Media Gateway could also be registered in a DNS name server.   The value of this object reflects the value of  cmgwConfigDomainName from the entry with a value of  'gateway(1)' for object cmgwConfigDomainNameEntity of  cMediaGwDomainNameConfigTable.  If there is no entry in cMediaGwDomainNameConfigTable with 'gateway(1)' of cmgwConfigDomainNameEntity, then the value of this object will be empty string
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: cmgwgracetime
            
            	This object is used to represent grace period. The grace period (restart delay in RSIP message) is   expressed in a number of seconds.  It means how soon the gateway will be taken out of service. The value \-1 indicates that the grace period time is disabled
            	**type**\:  int
            
            	**range:** \-1..65535
            
            	**units**\: seconds
            
            .. attribute:: cmgwlawinterceptenabled
            
            	This object is used to enable or disable the lawful intercept for government. as follows\:   'true'  \- enable lawful intercept   'false' \- disable lawful intercept
            	**type**\:  bool
            
            .. attribute:: cmgwphysicalindex
            
            	This object represents the entPhysicalIndex of the card in which media gateway is running. It will contain value 0 if the entPhysicalIndex value is not available or  not applicable
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cmgwservicestate
            
            	This object indicates the current service state of the Media  Gateway. This object is controlled by 'cmgwAdminState'  object
            	**type**\:   :py:class:`Cgwservicestate <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.Cgwservicestate>`
            
            .. attribute:: cmgwsrcfilterenabled
            
            	This object is used to enable or disable the source IP and port filtering with MGC for security consideration as follows\:   'true'  \- source IP and port filter is enabled    'false' \- source IP and port filter is disable 
            	**type**\:  bool
            
            .. attribute:: cmgwv23enabled
            
            	This object is to enable or disable V23 tone. Setting the object value to 'true', will cause VXSM (Voice Switching Service Module) to detect V23 tone
            	**type**\:  bool
            
            .. attribute:: cmgwvtmappingmode
            
            	This object is used to represent the VT (sonet Virtual Tributary) counting.  standard \- standard counting (based on Bellcore TR253) titan    \- TITAN5500 counting (based on Tellabs TITAN 5500)  Note\: 'titan' is valid only if sonet line medium type        (sonetMediumType of SONET\-MIB) is 'sonet' and        sonet path payload type (cspSonetPathPayload of       CISCO\-SONET\-MIB) is 'vt15vc11'
            	**type**\:   :py:class:`Cmgwvtmappingmode <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry.Cmgwvtmappingmode>`
            
            

            """

            _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
            _revision = '2009-02-25'

            def __init__(self):
                super(CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry, self).__init__()

                self.yang_name = "cMediaGwEntry"
                self.yang_parent_name = "cMediaGwTable"

                self.cmgwindex = YLeaf(YType.int32, "cmgwIndex")

                self.cmgwadminstate = YLeaf(YType.enumeration, "cmgwAdminState")

                self.cmgwdomainname = YLeaf(YType.str, "cmgwDomainName")

                self.cmgwgracetime = YLeaf(YType.int32, "cmgwGraceTime")

                self.cmgwlawinterceptenabled = YLeaf(YType.boolean, "cmgwLawInterceptEnabled")

                self.cmgwphysicalindex = YLeaf(YType.int32, "cmgwPhysicalIndex")

                self.cmgwservicestate = YLeaf(YType.enumeration, "cmgwServiceState")

                self.cmgwsrcfilterenabled = YLeaf(YType.boolean, "cmgwSrcFilterEnabled")

                self.cmgwv23enabled = YLeaf(YType.boolean, "cmgwV23Enabled")

                self.cmgwvtmappingmode = YLeaf(YType.enumeration, "cmgwVtMappingMode")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cmgwindex",
                                "cmgwadminstate",
                                "cmgwdomainname",
                                "cmgwgracetime",
                                "cmgwlawinterceptenabled",
                                "cmgwphysicalindex",
                                "cmgwservicestate",
                                "cmgwsrcfilterenabled",
                                "cmgwv23enabled",
                                "cmgwvtmappingmode") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry, self).__setattr__(name, value)

            class Cmgwvtmappingmode(Enum):
                """
                Cmgwvtmappingmode

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


            def has_data(self):
                return (
                    self.cmgwindex.is_set or
                    self.cmgwadminstate.is_set or
                    self.cmgwdomainname.is_set or
                    self.cmgwgracetime.is_set or
                    self.cmgwlawinterceptenabled.is_set or
                    self.cmgwphysicalindex.is_set or
                    self.cmgwservicestate.is_set or
                    self.cmgwsrcfilterenabled.is_set or
                    self.cmgwv23enabled.is_set or
                    self.cmgwvtmappingmode.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cmgwindex.yfilter != YFilter.not_set or
                    self.cmgwadminstate.yfilter != YFilter.not_set or
                    self.cmgwdomainname.yfilter != YFilter.not_set or
                    self.cmgwgracetime.yfilter != YFilter.not_set or
                    self.cmgwlawinterceptenabled.yfilter != YFilter.not_set or
                    self.cmgwphysicalindex.yfilter != YFilter.not_set or
                    self.cmgwservicestate.yfilter != YFilter.not_set or
                    self.cmgwsrcfilterenabled.yfilter != YFilter.not_set or
                    self.cmgwv23enabled.yfilter != YFilter.not_set or
                    self.cmgwvtmappingmode.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cMediaGwEntry" + "[cmgwIndex='" + self.cmgwindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/cMediaGwTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cmgwindex.is_set or self.cmgwindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwindex.get_name_leafdata())
                if (self.cmgwadminstate.is_set or self.cmgwadminstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwadminstate.get_name_leafdata())
                if (self.cmgwdomainname.is_set or self.cmgwdomainname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwdomainname.get_name_leafdata())
                if (self.cmgwgracetime.is_set or self.cmgwgracetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwgracetime.get_name_leafdata())
                if (self.cmgwlawinterceptenabled.is_set or self.cmgwlawinterceptenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwlawinterceptenabled.get_name_leafdata())
                if (self.cmgwphysicalindex.is_set or self.cmgwphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwphysicalindex.get_name_leafdata())
                if (self.cmgwservicestate.is_set or self.cmgwservicestate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwservicestate.get_name_leafdata())
                if (self.cmgwsrcfilterenabled.is_set or self.cmgwsrcfilterenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwsrcfilterenabled.get_name_leafdata())
                if (self.cmgwv23enabled.is_set or self.cmgwv23enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwv23enabled.get_name_leafdata())
                if (self.cmgwvtmappingmode.is_set or self.cmgwvtmappingmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwvtmappingmode.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cmgwIndex" or name == "cmgwAdminState" or name == "cmgwDomainName" or name == "cmgwGraceTime" or name == "cmgwLawInterceptEnabled" or name == "cmgwPhysicalIndex" or name == "cmgwServiceState" or name == "cmgwSrcFilterEnabled" or name == "cmgwV23Enabled" or name == "cmgwVtMappingMode"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cmgwIndex"):
                    self.cmgwindex = value
                    self.cmgwindex.value_namespace = name_space
                    self.cmgwindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwAdminState"):
                    self.cmgwadminstate = value
                    self.cmgwadminstate.value_namespace = name_space
                    self.cmgwadminstate.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwDomainName"):
                    self.cmgwdomainname = value
                    self.cmgwdomainname.value_namespace = name_space
                    self.cmgwdomainname.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwGraceTime"):
                    self.cmgwgracetime = value
                    self.cmgwgracetime.value_namespace = name_space
                    self.cmgwgracetime.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwLawInterceptEnabled"):
                    self.cmgwlawinterceptenabled = value
                    self.cmgwlawinterceptenabled.value_namespace = name_space
                    self.cmgwlawinterceptenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwPhysicalIndex"):
                    self.cmgwphysicalindex = value
                    self.cmgwphysicalindex.value_namespace = name_space
                    self.cmgwphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwServiceState"):
                    self.cmgwservicestate = value
                    self.cmgwservicestate.value_namespace = name_space
                    self.cmgwservicestate.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwSrcFilterEnabled"):
                    self.cmgwsrcfilterenabled = value
                    self.cmgwsrcfilterenabled.value_namespace = name_space
                    self.cmgwsrcfilterenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwV23Enabled"):
                    self.cmgwv23enabled = value
                    self.cmgwv23enabled.value_namespace = name_space
                    self.cmgwv23enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwVtMappingMode"):
                    self.cmgwvtmappingmode = value
                    self.cmgwvtmappingmode.value_namespace = name_space
                    self.cmgwvtmappingmode.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cmediagwentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cmediagwentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cMediaGwTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cMediaGwEntry"):
                for c in self.cmediagwentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cmediagwentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cMediaGwEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cmgwsignalprotocoltable(Entity):
        """
        This table contains the available signaling protocols that
        are supported by the media gateway for communication with
        MGCs.
        
        .. attribute:: cmgwsignalprotocolentry
        
        	Each entry represents an signaling protocol supported by the media gateway
        	**type**\: list of    :py:class:`Cmgwsignalprotocolentry <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmgwsignalprotocoltable.Cmgwsignalprotocolentry>`
        
        

        """

        _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
        _revision = '2009-02-25'

        def __init__(self):
            super(CiscoMediaGatewayMib.Cmgwsignalprotocoltable, self).__init__()

            self.yang_name = "cmgwSignalProtocolTable"
            self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"

            self.cmgwsignalprotocolentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoMediaGatewayMib.Cmgwsignalprotocoltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoMediaGatewayMib.Cmgwsignalprotocoltable, self).__setattr__(name, value)


        class Cmgwsignalprotocolentry(Entity):
            """
            Each entry represents an signaling protocol supported
            by the media gateway.
            
            .. attribute:: cmgwindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cmgwsignalprotocolindex  <key>
            
            	An index that uniquely identifies an entry in cmgwSignalProtocolTable
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: cmgwsignalmgcprotocolport
            
            	This object specifies the protocol port of the Media Gateway Controller (MGC). If the value of cmgwSignalProtocol is 'mgcp(2)' or 'tgcp(4)' and the value of cmgwSignalProtcolVersion is '1.0', the default value of this object is '2427'. If the value of cmgwSignalProtocol is 'h248(3)' and the value of cmgwSignalProtcolVersion is '1.0', the default value of this object is '2944'
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cmgwsignalprotocol
            
            	This object is used to represent the protocol type. other \- None of the following types. mgcp  \- Media Gateway Control Protocol h248 \- Media Gateway Control (ITU H.248) tgcp \- Trunking Gateway Control Protocol
            	**type**\:   :py:class:`Cmgwsignalprotocol <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmgwsignalprotocoltable.Cmgwsignalprotocolentry.Cmgwsignalprotocol>`
            
            .. attribute:: cmgwsignalprotocolconfigver
            
            	This object specifies the protocol version used by the gateway in the messages to MGC in order to exchange the service capabilities.  For example cmgwSignalProtocol is 'h248(3)' and this object can be string '1' or '1.0', '2' or '2.0'.   'MAX' is a special string indicating the gateway will use the highest protocol version supported in the  gateway, but it can be changed to lower version after  it negotiates with MGC. The final negotiated protocol version will be indicated in cmgwSignalProtocolVersion.  The version strings other than 'MAX' can be specified for the gateway to communicate with the MGC which doesn't support service capabilities negotiation. For example if a MGC supports only version 1.0 MGCP, this object should be set to '1' to instruct the gateway using MGCP  version 1.0 format messages to communicate with MGC. 
            	**type**\:  str
            
            	**length:** 1..16
            
            .. attribute:: cmgwsignalprotocolport
            
            	This object is used to represent the UDP port associated  with the protocol. If the value of cmgwSignalProtocol is 'mgcp(2)' and the value of cmgwSignalProtcolVersion is '1.0', the default value of this object is '2727'.  If the value of cmgwSignalProtocol is 'h248(3)' and the value of cmgwSignalProtcolVersion is '1.0', the default value of this object is '2944'
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cmgwsignalprotocolpreference
            
            	This object specifies the preference of the signal protocol  supported in the media gateway.  If this object is set to 0, the corresponding signal protocol will not be used by the gateway.   The value of this object is unique within the corresponding gateway. The entry with lower value has higher preference
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cmgwsignalprotocolversion
            
            	This object is used to represent the protocol version.  For example cmgwSignalProtocol is 'mgcp(2)' and this object is string '1.0'. cmgwSignalProtocol is  'h248(3)' and this object is set to '2.0'
            	**type**\:  str
            
            	**length:** 1..16
            
            

            """

            _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
            _revision = '2009-02-25'

            def __init__(self):
                super(CiscoMediaGatewayMib.Cmgwsignalprotocoltable.Cmgwsignalprotocolentry, self).__init__()

                self.yang_name = "cmgwSignalProtocolEntry"
                self.yang_parent_name = "cmgwSignalProtocolTable"

                self.cmgwindex = YLeaf(YType.str, "cmgwIndex")

                self.cmgwsignalprotocolindex = YLeaf(YType.int32, "cmgwSignalProtocolIndex")

                self.cmgwsignalmgcprotocolport = YLeaf(YType.uint16, "cmgwSignalMgcProtocolPort")

                self.cmgwsignalprotocol = YLeaf(YType.enumeration, "cmgwSignalProtocol")

                self.cmgwsignalprotocolconfigver = YLeaf(YType.str, "cmgwSignalProtocolConfigVer")

                self.cmgwsignalprotocolport = YLeaf(YType.int32, "cmgwSignalProtocolPort")

                self.cmgwsignalprotocolpreference = YLeaf(YType.int32, "cmgwSignalProtocolPreference")

                self.cmgwsignalprotocolversion = YLeaf(YType.str, "cmgwSignalProtocolVersion")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cmgwindex",
                                "cmgwsignalprotocolindex",
                                "cmgwsignalmgcprotocolport",
                                "cmgwsignalprotocol",
                                "cmgwsignalprotocolconfigver",
                                "cmgwsignalprotocolport",
                                "cmgwsignalprotocolpreference",
                                "cmgwsignalprotocolversion") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoMediaGatewayMib.Cmgwsignalprotocoltable.Cmgwsignalprotocolentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoMediaGatewayMib.Cmgwsignalprotocoltable.Cmgwsignalprotocolentry, self).__setattr__(name, value)

            class Cmgwsignalprotocol(Enum):
                """
                Cmgwsignalprotocol

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


            def has_data(self):
                return (
                    self.cmgwindex.is_set or
                    self.cmgwsignalprotocolindex.is_set or
                    self.cmgwsignalmgcprotocolport.is_set or
                    self.cmgwsignalprotocol.is_set or
                    self.cmgwsignalprotocolconfigver.is_set or
                    self.cmgwsignalprotocolport.is_set or
                    self.cmgwsignalprotocolpreference.is_set or
                    self.cmgwsignalprotocolversion.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cmgwindex.yfilter != YFilter.not_set or
                    self.cmgwsignalprotocolindex.yfilter != YFilter.not_set or
                    self.cmgwsignalmgcprotocolport.yfilter != YFilter.not_set or
                    self.cmgwsignalprotocol.yfilter != YFilter.not_set or
                    self.cmgwsignalprotocolconfigver.yfilter != YFilter.not_set or
                    self.cmgwsignalprotocolport.yfilter != YFilter.not_set or
                    self.cmgwsignalprotocolpreference.yfilter != YFilter.not_set or
                    self.cmgwsignalprotocolversion.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cmgwSignalProtocolEntry" + "[cmgwIndex='" + self.cmgwindex.get() + "']" + "[cmgwSignalProtocolIndex='" + self.cmgwsignalprotocolindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/cmgwSignalProtocolTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cmgwindex.is_set or self.cmgwindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwindex.get_name_leafdata())
                if (self.cmgwsignalprotocolindex.is_set or self.cmgwsignalprotocolindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwsignalprotocolindex.get_name_leafdata())
                if (self.cmgwsignalmgcprotocolport.is_set or self.cmgwsignalmgcprotocolport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwsignalmgcprotocolport.get_name_leafdata())
                if (self.cmgwsignalprotocol.is_set or self.cmgwsignalprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwsignalprotocol.get_name_leafdata())
                if (self.cmgwsignalprotocolconfigver.is_set or self.cmgwsignalprotocolconfigver.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwsignalprotocolconfigver.get_name_leafdata())
                if (self.cmgwsignalprotocolport.is_set or self.cmgwsignalprotocolport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwsignalprotocolport.get_name_leafdata())
                if (self.cmgwsignalprotocolpreference.is_set or self.cmgwsignalprotocolpreference.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwsignalprotocolpreference.get_name_leafdata())
                if (self.cmgwsignalprotocolversion.is_set or self.cmgwsignalprotocolversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwsignalprotocolversion.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cmgwIndex" or name == "cmgwSignalProtocolIndex" or name == "cmgwSignalMgcProtocolPort" or name == "cmgwSignalProtocol" or name == "cmgwSignalProtocolConfigVer" or name == "cmgwSignalProtocolPort" or name == "cmgwSignalProtocolPreference" or name == "cmgwSignalProtocolVersion"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cmgwIndex"):
                    self.cmgwindex = value
                    self.cmgwindex.value_namespace = name_space
                    self.cmgwindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwSignalProtocolIndex"):
                    self.cmgwsignalprotocolindex = value
                    self.cmgwsignalprotocolindex.value_namespace = name_space
                    self.cmgwsignalprotocolindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwSignalMgcProtocolPort"):
                    self.cmgwsignalmgcprotocolport = value
                    self.cmgwsignalmgcprotocolport.value_namespace = name_space
                    self.cmgwsignalmgcprotocolport.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwSignalProtocol"):
                    self.cmgwsignalprotocol = value
                    self.cmgwsignalprotocol.value_namespace = name_space
                    self.cmgwsignalprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwSignalProtocolConfigVer"):
                    self.cmgwsignalprotocolconfigver = value
                    self.cmgwsignalprotocolconfigver.value_namespace = name_space
                    self.cmgwsignalprotocolconfigver.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwSignalProtocolPort"):
                    self.cmgwsignalprotocolport = value
                    self.cmgwsignalprotocolport.value_namespace = name_space
                    self.cmgwsignalprotocolport.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwSignalProtocolPreference"):
                    self.cmgwsignalprotocolpreference = value
                    self.cmgwsignalprotocolpreference.value_namespace = name_space
                    self.cmgwsignalprotocolpreference.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwSignalProtocolVersion"):
                    self.cmgwsignalprotocolversion = value
                    self.cmgwsignalprotocolversion.value_namespace = name_space
                    self.cmgwsignalprotocolversion.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cmgwsignalprotocolentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cmgwsignalprotocolentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cmgwSignalProtocolTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cmgwSignalProtocolEntry"):
                for c in self.cmgwsignalprotocolentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoMediaGatewayMib.Cmgwsignalprotocoltable.Cmgwsignalprotocolentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cmgwsignalprotocolentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cmgwSignalProtocolEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cmediagwipconfigentry <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwipconfigtable.Cmediagwipconfigentry>`
        
        

        """

        _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
        _revision = '2009-02-25'

        def __init__(self):
            super(CiscoMediaGatewayMib.Cmediagwipconfigtable, self).__init__()

            self.yang_name = "cMediaGwIpConfigTable"
            self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"

            self.cmediagwipconfigentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoMediaGatewayMib.Cmediagwipconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoMediaGatewayMib.Cmediagwipconfigtable, self).__setattr__(name, value)


        class Cmediagwipconfigentry(Entity):
            """
            A Media Gateway IP configuration entry. 
            Each entry represents a media gateway IP address for MGCs
            to communicate with the media gateway.
            
            .. attribute:: cmgwindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cmgwipconfigindex  <key>
            
            	A unique index to identify each media gateway IP address
            	**type**\:  int
            
            	**range:** 1..64
            
            .. attribute:: cmgwipconfigaddress
            
            	The configured IP address of media gateway. This object can not be modified
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cmgwipconfigaddrtype
            
            	This object is the IP address type
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cmgwipconfigdefaultgwip
            
            	This object specifies cmgwIpConfigAddress of the entry will become the default gateway address. This object can be set to 'true' for only one entry in the table
            	**type**\:  bool
            
            .. attribute:: cmgwipconfigforremotemapping
            
            	This object specifies whether the address defined in cmgwIpConfigAddress is the address mapping at the remote end of this PVC.   If this object is set to 'true', the address defined in cmgwIpConfigAddress is for the remote end of the PVC. If this object is set to 'false', the address defined in cmgwIpConfigAddress is for the local end of the PVC
            	**type**\:  bool
            
            .. attribute:: cmgwipconfigifindex
            
            	This object is ifIndex of the interface which is associated to the media gateway IP address.  For ATM interface, the IP address should be associated to an existing PVC\:    cmgwIpConfigIfIndex represents port of the PVC    cmgwIpConfigVpi represents VPI of the PVC    cmgwIpConfigVci represents VCI of the PVC And one PVC only can be associated with one IP address.  If this object is set to zero which means the IP address is not associated to any interface
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cmgwipconfigrowstatus
            
            	This object is used to add and delete an entry.  When an entry of the table is created, the following  objects are mandatory\:     cmgwIpConfigIfIndex     cmgwIpConfigVpi     cmgwIpConfigVci     cmgwIpConfigAddress     cmgwIpConfigSubnetMask  These objects can not be modified after the value of this object is set to 'active'.  Modification can only be done by deleting and re\-adding the  entry again.  After the system verify the validity of the data, it will set the cmgwIpConfigRowStatus to 'active'
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cmgwipconfigsubnetmask
            
            	This object is used to specify the number of leading one    bits which from the mask to be logical\-ANDed with the media   gateway address before being compared to the value in the  cmgwIpCofigAddress.  Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bitwise logical\-AND of the mask formed from x with the value  of the corresponding instance of the cmgwIpCofigAddress  object is not equal to cmgwIpCofigAddress
            	**type**\:  int
            
            	**range:** 0..2040
            
            .. attribute:: cmgwipconfigvci
            
            	This object represents VCI of the PVC which is associated to the IP address. If the IP address is not associated to PVC, the value of this object is set to \-1
            	**type**\:  int
            
            	**range:** \-1..65535
            
            .. attribute:: cmgwipconfigvpi
            
            	This object represents VPI of the PVC which is associated to the IP address. If the IP address is not associated to PVC, the value  of this object is set to \-1
            	**type**\:  int
            
            	**range:** \-1..4095
            
            

            """

            _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
            _revision = '2009-02-25'

            def __init__(self):
                super(CiscoMediaGatewayMib.Cmediagwipconfigtable.Cmediagwipconfigentry, self).__init__()

                self.yang_name = "cMediaGwIpConfigEntry"
                self.yang_parent_name = "cMediaGwIpConfigTable"

                self.cmgwindex = YLeaf(YType.str, "cmgwIndex")

                self.cmgwipconfigindex = YLeaf(YType.int32, "cmgwIpConfigIndex")

                self.cmgwipconfigaddress = YLeaf(YType.str, "cmgwIpConfigAddress")

                self.cmgwipconfigaddrtype = YLeaf(YType.enumeration, "cmgwIpConfigAddrType")

                self.cmgwipconfigdefaultgwip = YLeaf(YType.boolean, "cmgwIpConfigDefaultGwIp")

                self.cmgwipconfigforremotemapping = YLeaf(YType.boolean, "cmgwIpConfigForRemoteMapping")

                self.cmgwipconfigifindex = YLeaf(YType.int32, "cmgwIpConfigIfIndex")

                self.cmgwipconfigrowstatus = YLeaf(YType.enumeration, "cmgwIpConfigRowStatus")

                self.cmgwipconfigsubnetmask = YLeaf(YType.uint32, "cmgwIpConfigSubnetMask")

                self.cmgwipconfigvci = YLeaf(YType.int32, "cmgwIpConfigVci")

                self.cmgwipconfigvpi = YLeaf(YType.int32, "cmgwIpConfigVpi")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cmgwindex",
                                "cmgwipconfigindex",
                                "cmgwipconfigaddress",
                                "cmgwipconfigaddrtype",
                                "cmgwipconfigdefaultgwip",
                                "cmgwipconfigforremotemapping",
                                "cmgwipconfigifindex",
                                "cmgwipconfigrowstatus",
                                "cmgwipconfigsubnetmask",
                                "cmgwipconfigvci",
                                "cmgwipconfigvpi") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoMediaGatewayMib.Cmediagwipconfigtable.Cmediagwipconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoMediaGatewayMib.Cmediagwipconfigtable.Cmediagwipconfigentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cmgwindex.is_set or
                    self.cmgwipconfigindex.is_set or
                    self.cmgwipconfigaddress.is_set or
                    self.cmgwipconfigaddrtype.is_set or
                    self.cmgwipconfigdefaultgwip.is_set or
                    self.cmgwipconfigforremotemapping.is_set or
                    self.cmgwipconfigifindex.is_set or
                    self.cmgwipconfigrowstatus.is_set or
                    self.cmgwipconfigsubnetmask.is_set or
                    self.cmgwipconfigvci.is_set or
                    self.cmgwipconfigvpi.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cmgwindex.yfilter != YFilter.not_set or
                    self.cmgwipconfigindex.yfilter != YFilter.not_set or
                    self.cmgwipconfigaddress.yfilter != YFilter.not_set or
                    self.cmgwipconfigaddrtype.yfilter != YFilter.not_set or
                    self.cmgwipconfigdefaultgwip.yfilter != YFilter.not_set or
                    self.cmgwipconfigforremotemapping.yfilter != YFilter.not_set or
                    self.cmgwipconfigifindex.yfilter != YFilter.not_set or
                    self.cmgwipconfigrowstatus.yfilter != YFilter.not_set or
                    self.cmgwipconfigsubnetmask.yfilter != YFilter.not_set or
                    self.cmgwipconfigvci.yfilter != YFilter.not_set or
                    self.cmgwipconfigvpi.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cMediaGwIpConfigEntry" + "[cmgwIndex='" + self.cmgwindex.get() + "']" + "[cmgwIpConfigIndex='" + self.cmgwipconfigindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/cMediaGwIpConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cmgwindex.is_set or self.cmgwindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwindex.get_name_leafdata())
                if (self.cmgwipconfigindex.is_set or self.cmgwipconfigindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwipconfigindex.get_name_leafdata())
                if (self.cmgwipconfigaddress.is_set or self.cmgwipconfigaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwipconfigaddress.get_name_leafdata())
                if (self.cmgwipconfigaddrtype.is_set or self.cmgwipconfigaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwipconfigaddrtype.get_name_leafdata())
                if (self.cmgwipconfigdefaultgwip.is_set or self.cmgwipconfigdefaultgwip.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwipconfigdefaultgwip.get_name_leafdata())
                if (self.cmgwipconfigforremotemapping.is_set or self.cmgwipconfigforremotemapping.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwipconfigforremotemapping.get_name_leafdata())
                if (self.cmgwipconfigifindex.is_set or self.cmgwipconfigifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwipconfigifindex.get_name_leafdata())
                if (self.cmgwipconfigrowstatus.is_set or self.cmgwipconfigrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwipconfigrowstatus.get_name_leafdata())
                if (self.cmgwipconfigsubnetmask.is_set or self.cmgwipconfigsubnetmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwipconfigsubnetmask.get_name_leafdata())
                if (self.cmgwipconfigvci.is_set or self.cmgwipconfigvci.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwipconfigvci.get_name_leafdata())
                if (self.cmgwipconfigvpi.is_set or self.cmgwipconfigvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwipconfigvpi.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cmgwIndex" or name == "cmgwIpConfigIndex" or name == "cmgwIpConfigAddress" or name == "cmgwIpConfigAddrType" or name == "cmgwIpConfigDefaultGwIp" or name == "cmgwIpConfigForRemoteMapping" or name == "cmgwIpConfigIfIndex" or name == "cmgwIpConfigRowStatus" or name == "cmgwIpConfigSubnetMask" or name == "cmgwIpConfigVci" or name == "cmgwIpConfigVpi"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cmgwIndex"):
                    self.cmgwindex = value
                    self.cmgwindex.value_namespace = name_space
                    self.cmgwindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwIpConfigIndex"):
                    self.cmgwipconfigindex = value
                    self.cmgwipconfigindex.value_namespace = name_space
                    self.cmgwipconfigindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwIpConfigAddress"):
                    self.cmgwipconfigaddress = value
                    self.cmgwipconfigaddress.value_namespace = name_space
                    self.cmgwipconfigaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwIpConfigAddrType"):
                    self.cmgwipconfigaddrtype = value
                    self.cmgwipconfigaddrtype.value_namespace = name_space
                    self.cmgwipconfigaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwIpConfigDefaultGwIp"):
                    self.cmgwipconfigdefaultgwip = value
                    self.cmgwipconfigdefaultgwip.value_namespace = name_space
                    self.cmgwipconfigdefaultgwip.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwIpConfigForRemoteMapping"):
                    self.cmgwipconfigforremotemapping = value
                    self.cmgwipconfigforremotemapping.value_namespace = name_space
                    self.cmgwipconfigforremotemapping.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwIpConfigIfIndex"):
                    self.cmgwipconfigifindex = value
                    self.cmgwipconfigifindex.value_namespace = name_space
                    self.cmgwipconfigifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwIpConfigRowStatus"):
                    self.cmgwipconfigrowstatus = value
                    self.cmgwipconfigrowstatus.value_namespace = name_space
                    self.cmgwipconfigrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwIpConfigSubnetMask"):
                    self.cmgwipconfigsubnetmask = value
                    self.cmgwipconfigsubnetmask.value_namespace = name_space
                    self.cmgwipconfigsubnetmask.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwIpConfigVci"):
                    self.cmgwipconfigvci = value
                    self.cmgwipconfigvci.value_namespace = name_space
                    self.cmgwipconfigvci.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwIpConfigVpi"):
                    self.cmgwipconfigvpi = value
                    self.cmgwipconfigvpi.value_namespace = name_space
                    self.cmgwipconfigvpi.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cmediagwipconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cmediagwipconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cMediaGwIpConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cMediaGwIpConfigEntry"):
                for c in self.cmediagwipconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoMediaGatewayMib.Cmediagwipconfigtable.Cmediagwipconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cmediagwipconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cMediaGwIpConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cmediagwdomainnameconfigentry <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable.Cmediagwdomainnameconfigentry>`
        
        

        """

        _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
        _revision = '2009-02-25'

        def __init__(self):
            super(CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable, self).__init__()

            self.yang_name = "cMediaGwDomainNameConfigTable"
            self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"

            self.cmediagwdomainnameconfigentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable, self).__setattr__(name, value)


        class Cmediagwdomainnameconfigentry(Entity):
            """
            Each entry represents a domain name used in the system.
            
            Creation and deletion are supported. Modification
            is prohibited.
            
            .. attribute:: cmgwindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cmgwconfigdomainnameindex  <key>
            
            	An index that is uniquely identifies a domain name configured in the system
            	**type**\:  int
            
            	**range:** 1..128
            
            .. attribute:: cmgwconfigdomainname
            
            	This object specifies the domain name.  The domain name should be unique if there are more than one entries having the same value in the object  cmgwConfigDomainNameEntity. For example, the gateway domain name should be unique  if the cmgwConfigDomainNameEntity has the value of  'gateway(1)'
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cmgwconfigdomainnameentity
            
            	This object indicates which entity to use this domain name.  gateway(1)   \- The domain name of media gateway.                With the same cmgwIndex, there is one and                 only one entry allowed with the value                 'gateway(1)' of this object.  dnsServer(2) \- The domain name of DNS name server that is used                 by Media gateway to find Internet Network                 Address from a DNS name.  mgc(3)       \- The domain name of a MGC (Media Gateway                Controller) associated with the media                 gateway. 
            	**type**\:   :py:class:`Cmgwconfigdomainnameentity <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable.Cmediagwdomainnameconfigentry.Cmgwconfigdomainnameentity>`
            
            .. attribute:: cmgwconfigdomainnamerowstatus
            
            	This object is used to add and delete an entry.  When an entry is created, the following objects are mandatory\:      cmgwConfigDomainName      cmgwConfigDomainNameEntity  When deleting domain name of DNS name server (cmgwConfigDomainNameEntity is dnsServer (2)), the  cMediaGwDnsIpConfigTable should be empty.  Adding/deleting entry with cmgwConfigDomainNameEntity of 'mgc' will cause adding/deleting entry in  cMgcConfigTable (CISCO\-MGC\-MIB) automatically.  The cmgwConfigDomainName and cmgwConfigDomainNameEntity can not be modified if the value of this object is 'active'. 
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
            _revision = '2009-02-25'

            def __init__(self):
                super(CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable.Cmediagwdomainnameconfigentry, self).__init__()

                self.yang_name = "cMediaGwDomainNameConfigEntry"
                self.yang_parent_name = "cMediaGwDomainNameConfigTable"

                self.cmgwindex = YLeaf(YType.str, "cmgwIndex")

                self.cmgwconfigdomainnameindex = YLeaf(YType.int32, "cmgwConfigDomainNameIndex")

                self.cmgwconfigdomainname = YLeaf(YType.str, "cmgwConfigDomainName")

                self.cmgwconfigdomainnameentity = YLeaf(YType.enumeration, "cmgwConfigDomainNameEntity")

                self.cmgwconfigdomainnamerowstatus = YLeaf(YType.enumeration, "cmgwConfigDomainNameRowStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cmgwindex",
                                "cmgwconfigdomainnameindex",
                                "cmgwconfigdomainname",
                                "cmgwconfigdomainnameentity",
                                "cmgwconfigdomainnamerowstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable.Cmediagwdomainnameconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable.Cmediagwdomainnameconfigentry, self).__setattr__(name, value)

            class Cmgwconfigdomainnameentity(Enum):
                """
                Cmgwconfigdomainnameentity

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


            def has_data(self):
                return (
                    self.cmgwindex.is_set or
                    self.cmgwconfigdomainnameindex.is_set or
                    self.cmgwconfigdomainname.is_set or
                    self.cmgwconfigdomainnameentity.is_set or
                    self.cmgwconfigdomainnamerowstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cmgwindex.yfilter != YFilter.not_set or
                    self.cmgwconfigdomainnameindex.yfilter != YFilter.not_set or
                    self.cmgwconfigdomainname.yfilter != YFilter.not_set or
                    self.cmgwconfigdomainnameentity.yfilter != YFilter.not_set or
                    self.cmgwconfigdomainnamerowstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cMediaGwDomainNameConfigEntry" + "[cmgwIndex='" + self.cmgwindex.get() + "']" + "[cmgwConfigDomainNameIndex='" + self.cmgwconfigdomainnameindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/cMediaGwDomainNameConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cmgwindex.is_set or self.cmgwindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwindex.get_name_leafdata())
                if (self.cmgwconfigdomainnameindex.is_set or self.cmgwconfigdomainnameindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwconfigdomainnameindex.get_name_leafdata())
                if (self.cmgwconfigdomainname.is_set or self.cmgwconfigdomainname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwconfigdomainname.get_name_leafdata())
                if (self.cmgwconfigdomainnameentity.is_set or self.cmgwconfigdomainnameentity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwconfigdomainnameentity.get_name_leafdata())
                if (self.cmgwconfigdomainnamerowstatus.is_set or self.cmgwconfigdomainnamerowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwconfigdomainnamerowstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cmgwIndex" or name == "cmgwConfigDomainNameIndex" or name == "cmgwConfigDomainName" or name == "cmgwConfigDomainNameEntity" or name == "cmgwConfigDomainNameRowStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cmgwIndex"):
                    self.cmgwindex = value
                    self.cmgwindex.value_namespace = name_space
                    self.cmgwindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwConfigDomainNameIndex"):
                    self.cmgwconfigdomainnameindex = value
                    self.cmgwconfigdomainnameindex.value_namespace = name_space
                    self.cmgwconfigdomainnameindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwConfigDomainName"):
                    self.cmgwconfigdomainname = value
                    self.cmgwconfigdomainname.value_namespace = name_space
                    self.cmgwconfigdomainname.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwConfigDomainNameEntity"):
                    self.cmgwconfigdomainnameentity = value
                    self.cmgwconfigdomainnameentity.value_namespace = name_space
                    self.cmgwconfigdomainnameentity.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwConfigDomainNameRowStatus"):
                    self.cmgwconfigdomainnamerowstatus = value
                    self.cmgwconfigdomainnamerowstatus.value_namespace = name_space
                    self.cmgwconfigdomainnamerowstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cmediagwdomainnameconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cmediagwdomainnameconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cMediaGwDomainNameConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cMediaGwDomainNameConfigEntry"):
                for c in self.cmediagwdomainnameconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable.Cmediagwdomainnameconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cmediagwdomainnameconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cMediaGwDomainNameConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cmediagwdnsipconfigentry <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwdnsipconfigtable.Cmediagwdnsipconfigentry>`
        
        

        """

        _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
        _revision = '2009-02-25'

        def __init__(self):
            super(CiscoMediaGatewayMib.Cmediagwdnsipconfigtable, self).__init__()

            self.yang_name = "cMediaGwDnsIpConfigTable"
            self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"

            self.cmediagwdnsipconfigentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoMediaGatewayMib.Cmediagwdnsipconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoMediaGatewayMib.Cmediagwdnsipconfigtable, self).__setattr__(name, value)


        class Cmediagwdnsipconfigentry(Entity):
            """
            Each entry represents an IP address of the DNS name 
            server.
            
            .. attribute:: cmgwindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cmgwdnsipindex  <key>
            
            	An index that uniquely identifies an IP address of DNS name server
            	**type**\:  int
            
            	**range:** 1..6
            
            .. attribute:: cmgwdnsdomainname
            
            	The domain name of DNS name server.  The value of this object reflects the value of  cmgwConfigDomainName from the entry with a value of  'dnsServer(2)' for object cmgwConfigDomainNameEntity of  cMediaGwDomainNameConfigTable.  If there is no entry in cMediaGwDomainNameConfigTable with 'dnsServer(2)' of cmgwConfigDomainNameEntity, then the value of this object will be empty string
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cmgwdnsip
            
            	The IP address of DNS name server. The IP address of DNS name server must be unique in this table
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cmgwdnsiprowstatus
            
            	This object is used to add and delete an entry.  When an entry of the table is created, the value of this object should be set to 'createAndGo' and the following objects are mandatory\:     cmgwDnsIp  When the user wants to delete the entry, the value of this object should be set to 'destroy'.  The entry can not be modified if the value of this  object is 'active'
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cmgwdnsiptype
            
            	DNS name server IP address type
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            

            """

            _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
            _revision = '2009-02-25'

            def __init__(self):
                super(CiscoMediaGatewayMib.Cmediagwdnsipconfigtable.Cmediagwdnsipconfigentry, self).__init__()

                self.yang_name = "cMediaGwDnsIpConfigEntry"
                self.yang_parent_name = "cMediaGwDnsIpConfigTable"

                self.cmgwindex = YLeaf(YType.str, "cmgwIndex")

                self.cmgwdnsipindex = YLeaf(YType.int32, "cmgwDnsIpIndex")

                self.cmgwdnsdomainname = YLeaf(YType.str, "cmgwDnsDomainName")

                self.cmgwdnsip = YLeaf(YType.str, "cmgwDnsIp")

                self.cmgwdnsiprowstatus = YLeaf(YType.enumeration, "cmgwDnsIpRowStatus")

                self.cmgwdnsiptype = YLeaf(YType.enumeration, "cmgwDnsIpType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cmgwindex",
                                "cmgwdnsipindex",
                                "cmgwdnsdomainname",
                                "cmgwdnsip",
                                "cmgwdnsiprowstatus",
                                "cmgwdnsiptype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoMediaGatewayMib.Cmediagwdnsipconfigtable.Cmediagwdnsipconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoMediaGatewayMib.Cmediagwdnsipconfigtable.Cmediagwdnsipconfigentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cmgwindex.is_set or
                    self.cmgwdnsipindex.is_set or
                    self.cmgwdnsdomainname.is_set or
                    self.cmgwdnsip.is_set or
                    self.cmgwdnsiprowstatus.is_set or
                    self.cmgwdnsiptype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cmgwindex.yfilter != YFilter.not_set or
                    self.cmgwdnsipindex.yfilter != YFilter.not_set or
                    self.cmgwdnsdomainname.yfilter != YFilter.not_set or
                    self.cmgwdnsip.yfilter != YFilter.not_set or
                    self.cmgwdnsiprowstatus.yfilter != YFilter.not_set or
                    self.cmgwdnsiptype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cMediaGwDnsIpConfigEntry" + "[cmgwIndex='" + self.cmgwindex.get() + "']" + "[cmgwDnsIpIndex='" + self.cmgwdnsipindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/cMediaGwDnsIpConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cmgwindex.is_set or self.cmgwindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwindex.get_name_leafdata())
                if (self.cmgwdnsipindex.is_set or self.cmgwdnsipindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwdnsipindex.get_name_leafdata())
                if (self.cmgwdnsdomainname.is_set or self.cmgwdnsdomainname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwdnsdomainname.get_name_leafdata())
                if (self.cmgwdnsip.is_set or self.cmgwdnsip.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwdnsip.get_name_leafdata())
                if (self.cmgwdnsiprowstatus.is_set or self.cmgwdnsiprowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwdnsiprowstatus.get_name_leafdata())
                if (self.cmgwdnsiptype.is_set or self.cmgwdnsiptype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwdnsiptype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cmgwIndex" or name == "cmgwDnsIpIndex" or name == "cmgwDnsDomainName" or name == "cmgwDnsIp" or name == "cmgwDnsIpRowStatus" or name == "cmgwDnsIpType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cmgwIndex"):
                    self.cmgwindex = value
                    self.cmgwindex.value_namespace = name_space
                    self.cmgwindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwDnsIpIndex"):
                    self.cmgwdnsipindex = value
                    self.cmgwdnsipindex.value_namespace = name_space
                    self.cmgwdnsipindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwDnsDomainName"):
                    self.cmgwdnsdomainname = value
                    self.cmgwdnsdomainname.value_namespace = name_space
                    self.cmgwdnsdomainname.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwDnsIp"):
                    self.cmgwdnsip = value
                    self.cmgwdnsip.value_namespace = name_space
                    self.cmgwdnsip.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwDnsIpRowStatus"):
                    self.cmgwdnsiprowstatus = value
                    self.cmgwdnsiprowstatus.value_namespace = name_space
                    self.cmgwdnsiprowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwDnsIpType"):
                    self.cmgwdnsiptype = value
                    self.cmgwdnsiptype.value_namespace = name_space
                    self.cmgwdnsiptype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cmediagwdnsipconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cmediagwdnsipconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cMediaGwDnsIpConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cMediaGwDnsIpConfigEntry"):
                for c in self.cmediagwdnsipconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoMediaGatewayMib.Cmediagwdnsipconfigtable.Cmediagwdnsipconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cmediagwdnsipconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cMediaGwDnsIpConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cmgwlifentry <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmgwliftable.Cmgwlifentry>`
        
        

        """

        _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
        _revision = '2009-02-25'

        def __init__(self):
            super(CiscoMediaGatewayMib.Cmgwliftable, self).__init__()

            self.yang_name = "cmgwLifTable"
            self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"

            self.cmgwlifentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoMediaGatewayMib.Cmgwliftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoMediaGatewayMib.Cmgwliftable, self).__setattr__(name, value)


        class Cmgwlifentry(Entity):
            """
            An entry of this table is created by the media gateway
            when it supports the VoIP/VoATM application.
            
            .. attribute:: cmgwindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cmgwlifnumber  <key>
            
            	An index that uniquely identifies a LIF in the  media gateway
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: cmgwlifpvccount
            
            	This object represents the total number of PVC within  this LIF.  When users associate/disassociate a PVC with a LIF  by giving a non\-zero/zero value of cwacChanLifNum in cwAtmChanExtConfigTable, the value of this object  will be incremented/decremented accordingly.  The value zero means there is no PVC associated with  the LIF
            	**type**\:  int
            
            	**range:** 0..10000
            
            .. attribute:: cmgwlifvoiceifcount
            
            	This object represents the total number of Voice Interfaces within this LIF.  When users associate/disassociate a Voice Interface with a LIF by giving a non\-zero/zero value of  ccasVoiceCfgLifNumber for the DS0 group in  ccasVoiceExtCfgTable, the value of this object will be  incremented/decremented accordingly.   The value zero means there is no Voice Interface associated with the LIF
            	**type**\:  int
            
            	**range:** 0..1000
            
            

            """

            _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
            _revision = '2009-02-25'

            def __init__(self):
                super(CiscoMediaGatewayMib.Cmgwliftable.Cmgwlifentry, self).__init__()

                self.yang_name = "cmgwLifEntry"
                self.yang_parent_name = "cmgwLifTable"

                self.cmgwindex = YLeaf(YType.str, "cmgwIndex")

                self.cmgwlifnumber = YLeaf(YType.uint32, "cmgwLifNumber")

                self.cmgwlifpvccount = YLeaf(YType.uint32, "cmgwLifPvcCount")

                self.cmgwlifvoiceifcount = YLeaf(YType.uint32, "cmgwLifVoiceIfCount")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cmgwindex",
                                "cmgwlifnumber",
                                "cmgwlifpvccount",
                                "cmgwlifvoiceifcount") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoMediaGatewayMib.Cmgwliftable.Cmgwlifentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoMediaGatewayMib.Cmgwliftable.Cmgwlifentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cmgwindex.is_set or
                    self.cmgwlifnumber.is_set or
                    self.cmgwlifpvccount.is_set or
                    self.cmgwlifvoiceifcount.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cmgwindex.yfilter != YFilter.not_set or
                    self.cmgwlifnumber.yfilter != YFilter.not_set or
                    self.cmgwlifpvccount.yfilter != YFilter.not_set or
                    self.cmgwlifvoiceifcount.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cmgwLifEntry" + "[cmgwIndex='" + self.cmgwindex.get() + "']" + "[cmgwLifNumber='" + self.cmgwlifnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/cmgwLifTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cmgwindex.is_set or self.cmgwindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwindex.get_name_leafdata())
                if (self.cmgwlifnumber.is_set or self.cmgwlifnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwlifnumber.get_name_leafdata())
                if (self.cmgwlifpvccount.is_set or self.cmgwlifpvccount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwlifpvccount.get_name_leafdata())
                if (self.cmgwlifvoiceifcount.is_set or self.cmgwlifvoiceifcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwlifvoiceifcount.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cmgwIndex" or name == "cmgwLifNumber" or name == "cmgwLifPvcCount" or name == "cmgwLifVoiceIfCount"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cmgwIndex"):
                    self.cmgwindex = value
                    self.cmgwindex.value_namespace = name_space
                    self.cmgwindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwLifNumber"):
                    self.cmgwlifnumber = value
                    self.cmgwlifnumber.value_namespace = name_space
                    self.cmgwlifnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwLifPvcCount"):
                    self.cmgwlifpvccount = value
                    self.cmgwlifpvccount.value_namespace = name_space
                    self.cmgwlifpvccount.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwLifVoiceIfCount"):
                    self.cmgwlifvoiceifcount = value
                    self.cmgwlifvoiceifcount.value_namespace = name_space
                    self.cmgwlifvoiceifcount.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cmgwlifentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cmgwlifentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cmgwLifTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cmgwLifEntry"):
                for c in self.cmgwlifentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoMediaGatewayMib.Cmgwliftable.Cmgwlifentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cmgwlifentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cmgwLifEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cmediagwcallcontrolconfigtable(Entity):
        """
        This table defines general call control attributes for
        the media gateway.
        
        .. attribute:: cmediagwcallcontrolconfigentry
        
        	One entry for each media gateway which supports call control  protocol
        	**type**\: list of    :py:class:`Cmediagwcallcontrolconfigentry <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry>`
        
        

        """

        _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
        _revision = '2009-02-25'

        def __init__(self):
            super(CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable, self).__init__()

            self.yang_name = "cMediaGwCallControlConfigTable"
            self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"

            self.cmediagwcallcontrolconfigentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable, self).__setattr__(name, value)


        class Cmediagwcallcontrolconfigentry(Entity):
            """
            One entry for each media gateway which supports call control 
            protocol.
            
            .. attribute:: cmgwindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cmediagwcccfgaal1svcnameprefix
            
            	This object specifies the prefix of the name schema for voice over AAL1 SVC (Switched Virtual Circuit) terminations. The value of this object must be unique among the  following objects\:        cMediaGwCcCfgDsNamePrefix        cMediaGwCcCfgRtpNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgDefRtpNamePrefix This object can not be modified when there is any AAL1 SVC termination type existing in the media gateway. It is default to 'AAL1/SVC'
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cmediagwcccfgaal2svcnameprefix
            
            	This object specifies the prefix of the name schema for voice over AAL2 SVC (Switched Virtual Circuit) terminations. The value of this object must be unique among the  following objects\:        cMediaGwCcCfgDsNamePrefix        cMediaGwCcCfgRtpNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgDefRtpNamePrefix This object can not be modified when there is any AAL2 SVC termination type existing in the media gateway. It is default to 'AAL2/SVC'
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cmediagwcccfgbearertos
            
            	This object specifies Type Of Service (TOS) field of IP header for the voice payload packet in VoIP application
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cmediagwcccfgclusterenabled
            
            	This object specifies the condition of the cluster generation in the call control.  A cluster is a group of endpoints that share a particular bearer possibility for connections among each other.  disabled(1) \- The generation of the cluster attribute               is disabled. enabled(2) \- Unconditionally generate the cluster              attribute. conditionalEnabled(3) \- The generation of the cluster                attribute is upon MGC request
            	**type**\:   :py:class:`Cmediagwcccfgclusterenabled <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry.Cmediagwcccfgclusterenabled>`
            
            .. attribute:: cmediagwcccfgcontroltos
            
            	This object specifies Type Of Service (TOS) field of IP header for the signaling control packet in VoIP application
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cmediagwcccfgdefaulttoneplanid
            
            	This object specifies the default tone plan index (the value of cvtcTonePlanId) for the media gateway
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: cmediagwcccfgdefbearertraffic
            
            	This object specifies the combination of the network type (IP/ATM), virtual circuit type (PVC/SVC) and ATM adaptation layer type (AAL1/AAL2/AAL5) for the connection used in transporting bearer traffic.      ipPvcAal5 (1) \- The bearer traffic is transported in                     IP network, through Permanent Virtual                     Circuit(PVC) over AAL5 adaptation layer.     atmPvcAal2 (2) \- The bearer traffic is transported in                      ATM network, through Permanent Virtual                      Circuit(PVC) over AAL2 adaptation layer.     atmSvcAal2 (3) \- The bearer traffic is transported in                      ATM network, through Switching Virtual                      Circuit(SVC) over AAL2 adaptation layer.     atmSvcAal1 (4) \- The bearer traffic is transported in                      ATM network, through Switching Virtual                      Circuit(SVC) over AAL1 adaptation layer.  In MGCP, if the call agent specifies the bear traffic type  in the local connection options (CRCX request),  configuration of this object will have no effect,  otherwise the value of this object will be used when  media gateway sending CRCX response
            	**type**\:   :py:class:`Cmediagwcccfgdefbearertraffic <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry.Cmediagwcccfgdefbearertraffic>`
            
            .. attribute:: cmediagwcccfgdefrtpnameprefix
            
            	This object specifies the prefix of the name schema for default RTP terminations. The value of this object must be unique among the  following objects\:        cMediaGwCcCfgDsNamePrefix        cMediaGwCcCfgRtpNamePrefix        cMediaGwCcCfgAal1SvcNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix  It is defaulted to 'TGWRTP'
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cmediagwcccfgdescrinfoenabled
            
            	This object specifies whether the media gateway supports descriptive suffix of the name schema for terminations.  There are two parts in name schema of termination, prefix and suffix. For example the name schema for a DS (Digital Subscriber) termination, can be 'DS/OC3\_2/DS1\_6/DS0\_24'. It represents DS type termination in 2nd OC3 line,  6th DS1 and 24th DS0 channel. In this example, 'DS' is  the prefix, 'OC3\_2/DS1\_6/DS0\_24' is the suffix.  The name schema in above example has a descriptive suffix. The non\-descriptive suffix for the same termination is  '2/6/24' and name schema becomes 'DS/2/6/24'.  This object can not be modified if there is any termination existing in the media gateway
            	**type**\:  bool
            
            .. attribute:: cmediagwcccfgdsnameprefix
            
            	This object specifies the prefix of the name schema for DS (Digital Subscriber) terminations. The value of this object must be unique among the  following objects\:        cMediaGwCcCfgDsNamePrefix        cMediaGwCcCfgRtpNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgDefRtpNamePrefix This object can not be modified when there is any DS termination existing in the media gateway. It is default to 'DS'
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cmediagwcccfgnsepayload
            
            	This object specifies NSE (Network Signaling Events) payload type
            	**type**\:  int
            
            	**range:** 98..117
            
            .. attribute:: cmediagwcccfgnseresptimer
            
            	This object specifies Network Signaling Event (NSE) timeout value
            	**type**\:  int
            
            	**range:** 250..10000
            
            	**units**\: milliseconds
            
            .. attribute:: cmediagwcccfgntepayload
            
            	This object specifies NTE (Named Telephony Events) payload type
            	**type**\:  int
            
            	**range:** 96..127
            
            .. attribute:: cmediagwcccfgrtpnameprefix
            
            	This object specifies the prefix of the name schema for RTP (Real\-Time Transport Protocol) terminations. The value of this object must be unique among the  following objects\:        cMediaGwCcCfgDsNamePrefix        cMediaGwCcCfgRtpNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgAal2SvcNamePrefix        cMediaGwCcCfgDefRtpNamePrefix This object can not be modified when there is any RTP termination type existing in the media gateway. It is default to 'RTP'
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cmediagwcccfgvbdjitterdelaymode
            
            	The object specifies the jitter buffer mode applied to a VBD (Voice Band Data) call connection.  adaptive \- means to use cMediaGwCcCfgVbdJitterNomDelay as            the initial jitter buffers size and let the DSP            pick the optimal value of the jitter buffer            size between the range of            cMediaGwCcCfgVbcJitterMaxDelay and            cMediaGwCcCfgVbcJitterMinDelay.  fixed \- means to use a constant jitter buffer size         which is specified by cMediaGwCcCfgVbdJitterNomDelay
            	**type**\:   :py:class:`Ccallcontroljitterdelaymode <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.Ccallcontroljitterdelaymode>`
            
            .. attribute:: cmediagwcccfgvbdjittermaxdelay
            
            	This object specifies the maximum jitter buffer size  in VBD (Voice Band Data)
            	**type**\:  int
            
            	**range:** 20..135
            
            	**units**\: milliseconds
            
            .. attribute:: cmediagwcccfgvbdjittermindelay
            
            	This object specifies the nominal jitter buffer size  in VBD (Voice Band Data)
            	**type**\:  int
            
            	**range:** 0..135
            
            	**units**\: milliseconds
            
            .. attribute:: cmediagwcccfgvbdjitternomdelay
            
            	This object specifies the nominal jitter buffer size  in VBD (Voice Band Data)
            	**type**\:  int
            
            	**range:** 5..135
            
            	**units**\: milliseconds
            
            

            """

            _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
            _revision = '2009-02-25'

            def __init__(self):
                super(CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry, self).__init__()

                self.yang_name = "cMediaGwCallControlConfigEntry"
                self.yang_parent_name = "cMediaGwCallControlConfigTable"

                self.cmgwindex = YLeaf(YType.str, "cmgwIndex")

                self.cmediagwcccfgaal1svcnameprefix = YLeaf(YType.str, "cMediaGwCcCfgAal1SvcNamePrefix")

                self.cmediagwcccfgaal2svcnameprefix = YLeaf(YType.str, "cMediaGwCcCfgAal2SvcNamePrefix")

                self.cmediagwcccfgbearertos = YLeaf(YType.uint32, "cMediaGwCcCfgBearerTos")

                self.cmediagwcccfgclusterenabled = YLeaf(YType.enumeration, "cMediaGwCcCfgClusterEnabled")

                self.cmediagwcccfgcontroltos = YLeaf(YType.uint32, "cMediaGwCcCfgControlTos")

                self.cmediagwcccfgdefaulttoneplanid = YLeaf(YType.uint32, "cMediaGwCcCfgDefaultTonePlanId")

                self.cmediagwcccfgdefbearertraffic = YLeaf(YType.enumeration, "cMediaGwCcCfgDefBearerTraffic")

                self.cmediagwcccfgdefrtpnameprefix = YLeaf(YType.str, "cMediaGwCcCfgDefRtpNamePrefix")

                self.cmediagwcccfgdescrinfoenabled = YLeaf(YType.boolean, "cMediaGwCcCfgDescrInfoEnabled")

                self.cmediagwcccfgdsnameprefix = YLeaf(YType.str, "cMediaGwCcCfgDsNamePrefix")

                self.cmediagwcccfgnsepayload = YLeaf(YType.uint32, "cMediaGwCcCfgNsePayload")

                self.cmediagwcccfgnseresptimer = YLeaf(YType.uint32, "cMediaGwCcCfgNseRespTimer")

                self.cmediagwcccfgntepayload = YLeaf(YType.uint32, "cMediaGwCcCfgNtePayload")

                self.cmediagwcccfgrtpnameprefix = YLeaf(YType.str, "cMediaGwCcCfgRtpNamePrefix")

                self.cmediagwcccfgvbdjitterdelaymode = YLeaf(YType.enumeration, "cMediaGwCcCfgVbdJitterDelayMode")

                self.cmediagwcccfgvbdjittermaxdelay = YLeaf(YType.uint32, "cMediaGwCcCfgVbdJitterMaxDelay")

                self.cmediagwcccfgvbdjittermindelay = YLeaf(YType.uint32, "cMediaGwCcCfgVbdJitterMinDelay")

                self.cmediagwcccfgvbdjitternomdelay = YLeaf(YType.uint32, "cMediaGwCcCfgVbdJitterNomDelay")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cmgwindex",
                                "cmediagwcccfgaal1svcnameprefix",
                                "cmediagwcccfgaal2svcnameprefix",
                                "cmediagwcccfgbearertos",
                                "cmediagwcccfgclusterenabled",
                                "cmediagwcccfgcontroltos",
                                "cmediagwcccfgdefaulttoneplanid",
                                "cmediagwcccfgdefbearertraffic",
                                "cmediagwcccfgdefrtpnameprefix",
                                "cmediagwcccfgdescrinfoenabled",
                                "cmediagwcccfgdsnameprefix",
                                "cmediagwcccfgnsepayload",
                                "cmediagwcccfgnseresptimer",
                                "cmediagwcccfgntepayload",
                                "cmediagwcccfgrtpnameprefix",
                                "cmediagwcccfgvbdjitterdelaymode",
                                "cmediagwcccfgvbdjittermaxdelay",
                                "cmediagwcccfgvbdjittermindelay",
                                "cmediagwcccfgvbdjitternomdelay") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry, self).__setattr__(name, value)

            class Cmediagwcccfgclusterenabled(Enum):
                """
                Cmediagwcccfgclusterenabled

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
                Cmediagwcccfgdefbearertraffic

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


            def has_data(self):
                return (
                    self.cmgwindex.is_set or
                    self.cmediagwcccfgaal1svcnameprefix.is_set or
                    self.cmediagwcccfgaal2svcnameprefix.is_set or
                    self.cmediagwcccfgbearertos.is_set or
                    self.cmediagwcccfgclusterenabled.is_set or
                    self.cmediagwcccfgcontroltos.is_set or
                    self.cmediagwcccfgdefaulttoneplanid.is_set or
                    self.cmediagwcccfgdefbearertraffic.is_set or
                    self.cmediagwcccfgdefrtpnameprefix.is_set or
                    self.cmediagwcccfgdescrinfoenabled.is_set or
                    self.cmediagwcccfgdsnameprefix.is_set or
                    self.cmediagwcccfgnsepayload.is_set or
                    self.cmediagwcccfgnseresptimer.is_set or
                    self.cmediagwcccfgntepayload.is_set or
                    self.cmediagwcccfgrtpnameprefix.is_set or
                    self.cmediagwcccfgvbdjitterdelaymode.is_set or
                    self.cmediagwcccfgvbdjittermaxdelay.is_set or
                    self.cmediagwcccfgvbdjittermindelay.is_set or
                    self.cmediagwcccfgvbdjitternomdelay.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cmgwindex.yfilter != YFilter.not_set or
                    self.cmediagwcccfgaal1svcnameprefix.yfilter != YFilter.not_set or
                    self.cmediagwcccfgaal2svcnameprefix.yfilter != YFilter.not_set or
                    self.cmediagwcccfgbearertos.yfilter != YFilter.not_set or
                    self.cmediagwcccfgclusterenabled.yfilter != YFilter.not_set or
                    self.cmediagwcccfgcontroltos.yfilter != YFilter.not_set or
                    self.cmediagwcccfgdefaulttoneplanid.yfilter != YFilter.not_set or
                    self.cmediagwcccfgdefbearertraffic.yfilter != YFilter.not_set or
                    self.cmediagwcccfgdefrtpnameprefix.yfilter != YFilter.not_set or
                    self.cmediagwcccfgdescrinfoenabled.yfilter != YFilter.not_set or
                    self.cmediagwcccfgdsnameprefix.yfilter != YFilter.not_set or
                    self.cmediagwcccfgnsepayload.yfilter != YFilter.not_set or
                    self.cmediagwcccfgnseresptimer.yfilter != YFilter.not_set or
                    self.cmediagwcccfgntepayload.yfilter != YFilter.not_set or
                    self.cmediagwcccfgrtpnameprefix.yfilter != YFilter.not_set or
                    self.cmediagwcccfgvbdjitterdelaymode.yfilter != YFilter.not_set or
                    self.cmediagwcccfgvbdjittermaxdelay.yfilter != YFilter.not_set or
                    self.cmediagwcccfgvbdjittermindelay.yfilter != YFilter.not_set or
                    self.cmediagwcccfgvbdjitternomdelay.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cMediaGwCallControlConfigEntry" + "[cmgwIndex='" + self.cmgwindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/cMediaGwCallControlConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cmgwindex.is_set or self.cmgwindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwindex.get_name_leafdata())
                if (self.cmediagwcccfgaal1svcnameprefix.is_set or self.cmediagwcccfgaal1svcnameprefix.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgaal1svcnameprefix.get_name_leafdata())
                if (self.cmediagwcccfgaal2svcnameprefix.is_set or self.cmediagwcccfgaal2svcnameprefix.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgaal2svcnameprefix.get_name_leafdata())
                if (self.cmediagwcccfgbearertos.is_set or self.cmediagwcccfgbearertos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgbearertos.get_name_leafdata())
                if (self.cmediagwcccfgclusterenabled.is_set or self.cmediagwcccfgclusterenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgclusterenabled.get_name_leafdata())
                if (self.cmediagwcccfgcontroltos.is_set or self.cmediagwcccfgcontroltos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgcontroltos.get_name_leafdata())
                if (self.cmediagwcccfgdefaulttoneplanid.is_set or self.cmediagwcccfgdefaulttoneplanid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgdefaulttoneplanid.get_name_leafdata())
                if (self.cmediagwcccfgdefbearertraffic.is_set or self.cmediagwcccfgdefbearertraffic.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgdefbearertraffic.get_name_leafdata())
                if (self.cmediagwcccfgdefrtpnameprefix.is_set or self.cmediagwcccfgdefrtpnameprefix.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgdefrtpnameprefix.get_name_leafdata())
                if (self.cmediagwcccfgdescrinfoenabled.is_set or self.cmediagwcccfgdescrinfoenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgdescrinfoenabled.get_name_leafdata())
                if (self.cmediagwcccfgdsnameprefix.is_set or self.cmediagwcccfgdsnameprefix.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgdsnameprefix.get_name_leafdata())
                if (self.cmediagwcccfgnsepayload.is_set or self.cmediagwcccfgnsepayload.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgnsepayload.get_name_leafdata())
                if (self.cmediagwcccfgnseresptimer.is_set or self.cmediagwcccfgnseresptimer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgnseresptimer.get_name_leafdata())
                if (self.cmediagwcccfgntepayload.is_set or self.cmediagwcccfgntepayload.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgntepayload.get_name_leafdata())
                if (self.cmediagwcccfgrtpnameprefix.is_set or self.cmediagwcccfgrtpnameprefix.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgrtpnameprefix.get_name_leafdata())
                if (self.cmediagwcccfgvbdjitterdelaymode.is_set or self.cmediagwcccfgvbdjitterdelaymode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgvbdjitterdelaymode.get_name_leafdata())
                if (self.cmediagwcccfgvbdjittermaxdelay.is_set or self.cmediagwcccfgvbdjittermaxdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgvbdjittermaxdelay.get_name_leafdata())
                if (self.cmediagwcccfgvbdjittermindelay.is_set or self.cmediagwcccfgvbdjittermindelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgvbdjittermindelay.get_name_leafdata())
                if (self.cmediagwcccfgvbdjitternomdelay.is_set or self.cmediagwcccfgvbdjitternomdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmediagwcccfgvbdjitternomdelay.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cmgwIndex" or name == "cMediaGwCcCfgAal1SvcNamePrefix" or name == "cMediaGwCcCfgAal2SvcNamePrefix" or name == "cMediaGwCcCfgBearerTos" or name == "cMediaGwCcCfgClusterEnabled" or name == "cMediaGwCcCfgControlTos" or name == "cMediaGwCcCfgDefaultTonePlanId" or name == "cMediaGwCcCfgDefBearerTraffic" or name == "cMediaGwCcCfgDefRtpNamePrefix" or name == "cMediaGwCcCfgDescrInfoEnabled" or name == "cMediaGwCcCfgDsNamePrefix" or name == "cMediaGwCcCfgNsePayload" or name == "cMediaGwCcCfgNseRespTimer" or name == "cMediaGwCcCfgNtePayload" or name == "cMediaGwCcCfgRtpNamePrefix" or name == "cMediaGwCcCfgVbdJitterDelayMode" or name == "cMediaGwCcCfgVbdJitterMaxDelay" or name == "cMediaGwCcCfgVbdJitterMinDelay" or name == "cMediaGwCcCfgVbdJitterNomDelay"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cmgwIndex"):
                    self.cmgwindex = value
                    self.cmgwindex.value_namespace = name_space
                    self.cmgwindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgAal1SvcNamePrefix"):
                    self.cmediagwcccfgaal1svcnameprefix = value
                    self.cmediagwcccfgaal1svcnameprefix.value_namespace = name_space
                    self.cmediagwcccfgaal1svcnameprefix.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgAal2SvcNamePrefix"):
                    self.cmediagwcccfgaal2svcnameprefix = value
                    self.cmediagwcccfgaal2svcnameprefix.value_namespace = name_space
                    self.cmediagwcccfgaal2svcnameprefix.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgBearerTos"):
                    self.cmediagwcccfgbearertos = value
                    self.cmediagwcccfgbearertos.value_namespace = name_space
                    self.cmediagwcccfgbearertos.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgClusterEnabled"):
                    self.cmediagwcccfgclusterenabled = value
                    self.cmediagwcccfgclusterenabled.value_namespace = name_space
                    self.cmediagwcccfgclusterenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgControlTos"):
                    self.cmediagwcccfgcontroltos = value
                    self.cmediagwcccfgcontroltos.value_namespace = name_space
                    self.cmediagwcccfgcontroltos.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgDefaultTonePlanId"):
                    self.cmediagwcccfgdefaulttoneplanid = value
                    self.cmediagwcccfgdefaulttoneplanid.value_namespace = name_space
                    self.cmediagwcccfgdefaulttoneplanid.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgDefBearerTraffic"):
                    self.cmediagwcccfgdefbearertraffic = value
                    self.cmediagwcccfgdefbearertraffic.value_namespace = name_space
                    self.cmediagwcccfgdefbearertraffic.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgDefRtpNamePrefix"):
                    self.cmediagwcccfgdefrtpnameprefix = value
                    self.cmediagwcccfgdefrtpnameprefix.value_namespace = name_space
                    self.cmediagwcccfgdefrtpnameprefix.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgDescrInfoEnabled"):
                    self.cmediagwcccfgdescrinfoenabled = value
                    self.cmediagwcccfgdescrinfoenabled.value_namespace = name_space
                    self.cmediagwcccfgdescrinfoenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgDsNamePrefix"):
                    self.cmediagwcccfgdsnameprefix = value
                    self.cmediagwcccfgdsnameprefix.value_namespace = name_space
                    self.cmediagwcccfgdsnameprefix.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgNsePayload"):
                    self.cmediagwcccfgnsepayload = value
                    self.cmediagwcccfgnsepayload.value_namespace = name_space
                    self.cmediagwcccfgnsepayload.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgNseRespTimer"):
                    self.cmediagwcccfgnseresptimer = value
                    self.cmediagwcccfgnseresptimer.value_namespace = name_space
                    self.cmediagwcccfgnseresptimer.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgNtePayload"):
                    self.cmediagwcccfgntepayload = value
                    self.cmediagwcccfgntepayload.value_namespace = name_space
                    self.cmediagwcccfgntepayload.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgRtpNamePrefix"):
                    self.cmediagwcccfgrtpnameprefix = value
                    self.cmediagwcccfgrtpnameprefix.value_namespace = name_space
                    self.cmediagwcccfgrtpnameprefix.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgVbdJitterDelayMode"):
                    self.cmediagwcccfgvbdjitterdelaymode = value
                    self.cmediagwcccfgvbdjitterdelaymode.value_namespace = name_space
                    self.cmediagwcccfgvbdjitterdelaymode.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgVbdJitterMaxDelay"):
                    self.cmediagwcccfgvbdjittermaxdelay = value
                    self.cmediagwcccfgvbdjittermaxdelay.value_namespace = name_space
                    self.cmediagwcccfgvbdjittermaxdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgVbdJitterMinDelay"):
                    self.cmediagwcccfgvbdjittermindelay = value
                    self.cmediagwcccfgvbdjittermindelay.value_namespace = name_space
                    self.cmediagwcccfgvbdjittermindelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cMediaGwCcCfgVbdJitterNomDelay"):
                    self.cmediagwcccfgvbdjitternomdelay = value
                    self.cmediagwcccfgvbdjitternomdelay.value_namespace = name_space
                    self.cmediagwcccfgvbdjitternomdelay.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cmediagwcallcontrolconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cmediagwcallcontrolconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cMediaGwCallControlConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cMediaGwCallControlConfigEntry"):
                for c in self.cmediagwcallcontrolconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cmediagwcallcontrolconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cMediaGwCallControlConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cmediagwrscstatstable(Entity):
        """
        This table stores the gateway resource statistics
        information.
        
        .. attribute:: cmediagwrscstatsentry
        
        	Each entry stores the statistics information for a specific resource
        	**type**\: list of    :py:class:`Cmediagwrscstatsentry <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwrscstatstable.Cmediagwrscstatsentry>`
        
        

        """

        _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
        _revision = '2009-02-25'

        def __init__(self):
            super(CiscoMediaGatewayMib.Cmediagwrscstatstable, self).__init__()

            self.yang_name = "cMediaGwRscStatsTable"
            self.yang_parent_name = "CISCO-MEDIA-GATEWAY-MIB"

            self.cmediagwrscstatsentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoMediaGatewayMib.Cmediagwrscstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoMediaGatewayMib.Cmediagwrscstatstable, self).__setattr__(name, value)


        class Cmediagwrscstatsentry(Entity):
            """
            Each entry stores the statistics
            information for a specific resource.
            
            .. attribute:: cmgwindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cmgwrscstatsindex  <key>
            
            	An index that uniquely identifies a specific gateway resource
            	**type**\:   :py:class:`Cmgwrscstatsindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwrscstatstable.Cmediagwrscstatsentry.Cmgwrscstatsindex>`
            
            .. attribute:: cmgwrscaverageutilization
            
            	This object indicates the average utilization of the resource over the interval specified by the 'cmgwRscSinceLastReset'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmgwrscmaximumutilization
            
            	This object indicates the maximum utilization of the resource over the interval specified by the 'cmgwRscSinceLastReset'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmgwrscminimumutilization
            
            	This object indicates the minimum utilization of the resource over the interval specified by the 'cmgwRscSinceLastReset'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmgwrscsincelastreset
            
            	The elapsed time (in seconds) from the last periodic reset.  The following objects are reset at the last reset\:      'cmgwRscMaximumUtilization'     'cmgwRscMinimumUtilization'     'cmgwRscAverageUtilization'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            

            """

            _prefix = 'CISCO-MEDIA-GATEWAY-MIB'
            _revision = '2009-02-25'

            def __init__(self):
                super(CiscoMediaGatewayMib.Cmediagwrscstatstable.Cmediagwrscstatsentry, self).__init__()

                self.yang_name = "cMediaGwRscStatsEntry"
                self.yang_parent_name = "cMediaGwRscStatsTable"

                self.cmgwindex = YLeaf(YType.str, "cmgwIndex")

                self.cmgwrscstatsindex = YLeaf(YType.enumeration, "cmgwRscStatsIndex")

                self.cmgwrscaverageutilization = YLeaf(YType.uint32, "cmgwRscAverageUtilization")

                self.cmgwrscmaximumutilization = YLeaf(YType.uint32, "cmgwRscMaximumUtilization")

                self.cmgwrscminimumutilization = YLeaf(YType.uint32, "cmgwRscMinimumUtilization")

                self.cmgwrscsincelastreset = YLeaf(YType.uint32, "cmgwRscSinceLastReset")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cmgwindex",
                                "cmgwrscstatsindex",
                                "cmgwrscaverageutilization",
                                "cmgwrscmaximumutilization",
                                "cmgwrscminimumutilization",
                                "cmgwrscsincelastreset") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoMediaGatewayMib.Cmediagwrscstatstable.Cmediagwrscstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoMediaGatewayMib.Cmediagwrscstatstable.Cmediagwrscstatsentry, self).__setattr__(name, value)

            class Cmgwrscstatsindex(Enum):
                """
                Cmgwrscstatsindex

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


            def has_data(self):
                return (
                    self.cmgwindex.is_set or
                    self.cmgwrscstatsindex.is_set or
                    self.cmgwrscaverageutilization.is_set or
                    self.cmgwrscmaximumutilization.is_set or
                    self.cmgwrscminimumutilization.is_set or
                    self.cmgwrscsincelastreset.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cmgwindex.yfilter != YFilter.not_set or
                    self.cmgwrscstatsindex.yfilter != YFilter.not_set or
                    self.cmgwrscaverageutilization.yfilter != YFilter.not_set or
                    self.cmgwrscmaximumutilization.yfilter != YFilter.not_set or
                    self.cmgwrscminimumutilization.yfilter != YFilter.not_set or
                    self.cmgwrscsincelastreset.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cMediaGwRscStatsEntry" + "[cmgwIndex='" + self.cmgwindex.get() + "']" + "[cmgwRscStatsIndex='" + self.cmgwrscstatsindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/cMediaGwRscStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cmgwindex.is_set or self.cmgwindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwindex.get_name_leafdata())
                if (self.cmgwrscstatsindex.is_set or self.cmgwrscstatsindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwrscstatsindex.get_name_leafdata())
                if (self.cmgwrscaverageutilization.is_set or self.cmgwrscaverageutilization.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwrscaverageutilization.get_name_leafdata())
                if (self.cmgwrscmaximumutilization.is_set or self.cmgwrscmaximumutilization.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwrscmaximumutilization.get_name_leafdata())
                if (self.cmgwrscminimumutilization.is_set or self.cmgwrscminimumutilization.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwrscminimumutilization.get_name_leafdata())
                if (self.cmgwrscsincelastreset.is_set or self.cmgwrscsincelastreset.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwrscsincelastreset.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cmgwIndex" or name == "cmgwRscStatsIndex" or name == "cmgwRscAverageUtilization" or name == "cmgwRscMaximumUtilization" or name == "cmgwRscMinimumUtilization" or name == "cmgwRscSinceLastReset"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cmgwIndex"):
                    self.cmgwindex = value
                    self.cmgwindex.value_namespace = name_space
                    self.cmgwindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwRscStatsIndex"):
                    self.cmgwrscstatsindex = value
                    self.cmgwrscstatsindex.value_namespace = name_space
                    self.cmgwrscstatsindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwRscAverageUtilization"):
                    self.cmgwrscaverageutilization = value
                    self.cmgwrscaverageutilization.value_namespace = name_space
                    self.cmgwrscaverageutilization.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwRscMaximumUtilization"):
                    self.cmgwrscmaximumutilization = value
                    self.cmgwrscmaximumutilization.value_namespace = name_space
                    self.cmgwrscmaximumutilization.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwRscMinimumUtilization"):
                    self.cmgwrscminimumutilization = value
                    self.cmgwrscminimumutilization.value_namespace = name_space
                    self.cmgwrscminimumutilization.value_namespace_prefix = name_space_prefix
                if(value_path == "cmgwRscSinceLastReset"):
                    self.cmgwrscsincelastreset = value
                    self.cmgwrscsincelastreset.value_namespace = name_space
                    self.cmgwrscsincelastreset.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cmediagwrscstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cmediagwrscstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cMediaGwRscStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cMediaGwRscStatsEntry"):
                for c in self.cmediagwrscstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoMediaGatewayMib.Cmediagwrscstatstable.Cmediagwrscstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cmediagwrscstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cMediaGwRscStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cmediagwcallcontrolconfigtable is not None and self.cmediagwcallcontrolconfigtable.has_data()) or
            (self.cmediagwdnsipconfigtable is not None and self.cmediagwdnsipconfigtable.has_data()) or
            (self.cmediagwdomainnameconfigtable is not None and self.cmediagwdomainnameconfigtable.has_data()) or
            (self.cmediagwipconfigtable is not None and self.cmediagwipconfigtable.has_data()) or
            (self.cmediagwrscstatstable is not None and self.cmediagwrscstatstable.has_data()) or
            (self.cmediagwtable is not None and self.cmediagwtable.has_data()) or
            (self.cmgwliftable is not None and self.cmgwliftable.has_data()) or
            (self.cmgwsignalprotocoltable is not None and self.cmgwsignalprotocoltable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cmediagwcallcontrolconfigtable is not None and self.cmediagwcallcontrolconfigtable.has_operation()) or
            (self.cmediagwdnsipconfigtable is not None and self.cmediagwdnsipconfigtable.has_operation()) or
            (self.cmediagwdomainnameconfigtable is not None and self.cmediagwdomainnameconfigtable.has_operation()) or
            (self.cmediagwipconfigtable is not None and self.cmediagwipconfigtable.has_operation()) or
            (self.cmediagwrscstatstable is not None and self.cmediagwrscstatstable.has_operation()) or
            (self.cmediagwtable is not None and self.cmediagwtable.has_operation()) or
            (self.cmgwliftable is not None and self.cmgwliftable.has_operation()) or
            (self.cmgwsignalprotocoltable is not None and self.cmgwsignalprotocoltable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-MEDIA-GATEWAY-MIB:CISCO-MEDIA-GATEWAY-MIB" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "cMediaGwCallControlConfigTable"):
            if (self.cmediagwcallcontrolconfigtable is None):
                self.cmediagwcallcontrolconfigtable = CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable()
                self.cmediagwcallcontrolconfigtable.parent = self
                self._children_name_map["cmediagwcallcontrolconfigtable"] = "cMediaGwCallControlConfigTable"
            return self.cmediagwcallcontrolconfigtable

        if (child_yang_name == "cMediaGwDnsIpConfigTable"):
            if (self.cmediagwdnsipconfigtable is None):
                self.cmediagwdnsipconfigtable = CiscoMediaGatewayMib.Cmediagwdnsipconfigtable()
                self.cmediagwdnsipconfigtable.parent = self
                self._children_name_map["cmediagwdnsipconfigtable"] = "cMediaGwDnsIpConfigTable"
            return self.cmediagwdnsipconfigtable

        if (child_yang_name == "cMediaGwDomainNameConfigTable"):
            if (self.cmediagwdomainnameconfigtable is None):
                self.cmediagwdomainnameconfigtable = CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable()
                self.cmediagwdomainnameconfigtable.parent = self
                self._children_name_map["cmediagwdomainnameconfigtable"] = "cMediaGwDomainNameConfigTable"
            return self.cmediagwdomainnameconfigtable

        if (child_yang_name == "cMediaGwIpConfigTable"):
            if (self.cmediagwipconfigtable is None):
                self.cmediagwipconfigtable = CiscoMediaGatewayMib.Cmediagwipconfigtable()
                self.cmediagwipconfigtable.parent = self
                self._children_name_map["cmediagwipconfigtable"] = "cMediaGwIpConfigTable"
            return self.cmediagwipconfigtable

        if (child_yang_name == "cMediaGwRscStatsTable"):
            if (self.cmediagwrscstatstable is None):
                self.cmediagwrscstatstable = CiscoMediaGatewayMib.Cmediagwrscstatstable()
                self.cmediagwrscstatstable.parent = self
                self._children_name_map["cmediagwrscstatstable"] = "cMediaGwRscStatsTable"
            return self.cmediagwrscstatstable

        if (child_yang_name == "cMediaGwTable"):
            if (self.cmediagwtable is None):
                self.cmediagwtable = CiscoMediaGatewayMib.Cmediagwtable()
                self.cmediagwtable.parent = self
                self._children_name_map["cmediagwtable"] = "cMediaGwTable"
            return self.cmediagwtable

        if (child_yang_name == "cmgwLifTable"):
            if (self.cmgwliftable is None):
                self.cmgwliftable = CiscoMediaGatewayMib.Cmgwliftable()
                self.cmgwliftable.parent = self
                self._children_name_map["cmgwliftable"] = "cmgwLifTable"
            return self.cmgwliftable

        if (child_yang_name == "cmgwSignalProtocolTable"):
            if (self.cmgwsignalprotocoltable is None):
                self.cmgwsignalprotocoltable = CiscoMediaGatewayMib.Cmgwsignalprotocoltable()
                self.cmgwsignalprotocoltable.parent = self
                self._children_name_map["cmgwsignalprotocoltable"] = "cmgwSignalProtocolTable"
            return self.cmgwsignalprotocoltable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cMediaGwCallControlConfigTable" or name == "cMediaGwDnsIpConfigTable" or name == "cMediaGwDomainNameConfigTable" or name == "cMediaGwIpConfigTable" or name == "cMediaGwRscStatsTable" or name == "cMediaGwTable" or name == "cmgwLifTable" or name == "cmgwSignalProtocolTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoMediaGatewayMib()
        return self._top_entity

