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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoRadiusExtMib(Entity):
    """
    
    
    .. attribute:: creclientaccounting
    
    	
    	**type**\:   :py:class:`Creclientaccounting <ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB.CiscoRadiusExtMib.Creclientaccounting>`
    
    .. attribute:: creclientauthentication
    
    	
    	**type**\:   :py:class:`Creclientauthentication <ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB.CiscoRadiusExtMib.Creclientauthentication>`
    
    .. attribute:: creclientglobal
    
    	
    	**type**\:   :py:class:`Creclientglobal <ydk.models.cisco_ios_xe.CISCO_RADIUS_EXT_MIB.CiscoRadiusExtMib.Creclientglobal>`
    
    

    """

    _prefix = 'CISCO-RADIUS-EXT-MIB'
    _revision = '2010-05-25'

    def __init__(self):
        super(CiscoRadiusExtMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-RADIUS-EXT-MIB"
        self.yang_parent_name = "CISCO-RADIUS-EXT-MIB"

        self.creclientaccounting = CiscoRadiusExtMib.Creclientaccounting()
        self.creclientaccounting.parent = self
        self._children_name_map["creclientaccounting"] = "creClientAccounting"
        self._children_yang_names.add("creClientAccounting")

        self.creclientauthentication = CiscoRadiusExtMib.Creclientauthentication()
        self.creclientauthentication.parent = self
        self._children_name_map["creclientauthentication"] = "creClientAuthentication"
        self._children_yang_names.add("creClientAuthentication")

        self.creclientglobal = CiscoRadiusExtMib.Creclientglobal()
        self.creclientglobal.parent = self
        self._children_name_map["creclientglobal"] = "creClientGlobal"
        self._children_yang_names.add("creClientGlobal")


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
            super(CiscoRadiusExtMib.Creclientglobal, self).__init__()

            self.yang_name = "creClientGlobal"
            self.yang_parent_name = "CISCO-RADIUS-EXT-MIB"

            self.creclientlastusedsourceid = YLeaf(YType.uint32, "creClientLastUsedSourceId")

            self.creclientlastusedsourceport = YLeaf(YType.uint16, "creClientLastUsedSourcePort")

            self.creclientsourceportrangeend = YLeaf(YType.uint16, "creClientSourcePortRangeEnd")

            self.creclientsourceportrangestart = YLeaf(YType.uint16, "creClientSourcePortRangeStart")

            self.creclienttotalaccessrejects = YLeaf(YType.uint32, "creClientTotalAccessRejects")

            self.creclienttotalaverageresponsedelay = YLeaf(YType.int32, "creClientTotalAverageResponseDelay")

            self.creclienttotalmaxdoneqlength = YLeaf(YType.uint32, "creClientTotalMaxDoneQLength")

            self.creclienttotalmaxinqlength = YLeaf(YType.uint32, "creClientTotalMaxInQLength")

            self.creclienttotalmaxwaitqlength = YLeaf(YType.uint32, "creClientTotalMaxWaitQLength")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("creclientlastusedsourceid",
                            "creclientlastusedsourceport",
                            "creclientsourceportrangeend",
                            "creclientsourceportrangestart",
                            "creclienttotalaccessrejects",
                            "creclienttotalaverageresponsedelay",
                            "creclienttotalmaxdoneqlength",
                            "creclienttotalmaxinqlength",
                            "creclienttotalmaxwaitqlength") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoRadiusExtMib.Creclientglobal, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRadiusExtMib.Creclientglobal, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.creclientlastusedsourceid.is_set or
                self.creclientlastusedsourceport.is_set or
                self.creclientsourceportrangeend.is_set or
                self.creclientsourceportrangestart.is_set or
                self.creclienttotalaccessrejects.is_set or
                self.creclienttotalaverageresponsedelay.is_set or
                self.creclienttotalmaxdoneqlength.is_set or
                self.creclienttotalmaxinqlength.is_set or
                self.creclienttotalmaxwaitqlength.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.creclientlastusedsourceid.yfilter != YFilter.not_set or
                self.creclientlastusedsourceport.yfilter != YFilter.not_set or
                self.creclientsourceportrangeend.yfilter != YFilter.not_set or
                self.creclientsourceportrangestart.yfilter != YFilter.not_set or
                self.creclienttotalaccessrejects.yfilter != YFilter.not_set or
                self.creclienttotalaverageresponsedelay.yfilter != YFilter.not_set or
                self.creclienttotalmaxdoneqlength.yfilter != YFilter.not_set or
                self.creclienttotalmaxinqlength.yfilter != YFilter.not_set or
                self.creclienttotalmaxwaitqlength.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "creClientGlobal" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RADIUS-EXT-MIB:CISCO-RADIUS-EXT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.creclientlastusedsourceid.is_set or self.creclientlastusedsourceid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creclientlastusedsourceid.get_name_leafdata())
            if (self.creclientlastusedsourceport.is_set or self.creclientlastusedsourceport.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creclientlastusedsourceport.get_name_leafdata())
            if (self.creclientsourceportrangeend.is_set or self.creclientsourceportrangeend.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creclientsourceportrangeend.get_name_leafdata())
            if (self.creclientsourceportrangestart.is_set or self.creclientsourceportrangestart.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creclientsourceportrangestart.get_name_leafdata())
            if (self.creclienttotalaccessrejects.is_set or self.creclienttotalaccessrejects.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creclienttotalaccessrejects.get_name_leafdata())
            if (self.creclienttotalaverageresponsedelay.is_set or self.creclienttotalaverageresponsedelay.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creclienttotalaverageresponsedelay.get_name_leafdata())
            if (self.creclienttotalmaxdoneqlength.is_set or self.creclienttotalmaxdoneqlength.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creclienttotalmaxdoneqlength.get_name_leafdata())
            if (self.creclienttotalmaxinqlength.is_set or self.creclienttotalmaxinqlength.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creclienttotalmaxinqlength.get_name_leafdata())
            if (self.creclienttotalmaxwaitqlength.is_set or self.creclienttotalmaxwaitqlength.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creclienttotalmaxwaitqlength.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "creClientLastUsedSourceId" or name == "creClientLastUsedSourcePort" or name == "creClientSourcePortRangeEnd" or name == "creClientSourcePortRangeStart" or name == "creClientTotalAccessRejects" or name == "creClientTotalAverageResponseDelay" or name == "creClientTotalMaxDoneQLength" or name == "creClientTotalMaxInQLength" or name == "creClientTotalMaxWaitQLength"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "creClientLastUsedSourceId"):
                self.creclientlastusedsourceid = value
                self.creclientlastusedsourceid.value_namespace = name_space
                self.creclientlastusedsourceid.value_namespace_prefix = name_space_prefix
            if(value_path == "creClientLastUsedSourcePort"):
                self.creclientlastusedsourceport = value
                self.creclientlastusedsourceport.value_namespace = name_space
                self.creclientlastusedsourceport.value_namespace_prefix = name_space_prefix
            if(value_path == "creClientSourcePortRangeEnd"):
                self.creclientsourceportrangeend = value
                self.creclientsourceportrangeend.value_namespace = name_space
                self.creclientsourceportrangeend.value_namespace_prefix = name_space_prefix
            if(value_path == "creClientSourcePortRangeStart"):
                self.creclientsourceportrangestart = value
                self.creclientsourceportrangestart.value_namespace = name_space
                self.creclientsourceportrangestart.value_namespace_prefix = name_space_prefix
            if(value_path == "creClientTotalAccessRejects"):
                self.creclienttotalaccessrejects = value
                self.creclienttotalaccessrejects.value_namespace = name_space
                self.creclienttotalaccessrejects.value_namespace_prefix = name_space_prefix
            if(value_path == "creClientTotalAverageResponseDelay"):
                self.creclienttotalaverageresponsedelay = value
                self.creclienttotalaverageresponsedelay.value_namespace = name_space
                self.creclienttotalaverageresponsedelay.value_namespace_prefix = name_space_prefix
            if(value_path == "creClientTotalMaxDoneQLength"):
                self.creclienttotalmaxdoneqlength = value
                self.creclienttotalmaxdoneqlength.value_namespace = name_space
                self.creclienttotalmaxdoneqlength.value_namespace_prefix = name_space_prefix
            if(value_path == "creClientTotalMaxInQLength"):
                self.creclienttotalmaxinqlength = value
                self.creclienttotalmaxinqlength.value_namespace = name_space
                self.creclienttotalmaxinqlength.value_namespace_prefix = name_space_prefix
            if(value_path == "creClientTotalMaxWaitQLength"):
                self.creclienttotalmaxwaitqlength = value
                self.creclienttotalmaxwaitqlength.value_namespace = name_space
                self.creclienttotalmaxwaitqlength.value_namespace_prefix = name_space_prefix


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
            super(CiscoRadiusExtMib.Creclientauthentication, self).__init__()

            self.yang_name = "creClientAuthentication"
            self.yang_parent_name = "CISCO-RADIUS-EXT-MIB"

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

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("creauthclientaverageresponsedelay",
                            "creauthclientbadauthenticators",
                            "creauthclientbufferallocfailures",
                            "creauthclientdupids",
                            "creauthclientlastusedsourceid",
                            "creauthclientmalformedresponses",
                            "creauthclientmaxbuffersize",
                            "creauthclientmaxresponsedelay",
                            "creauthclienttimeouts",
                            "creauthclienttotalpacketswithoutresponses",
                            "creauthclienttotalpacketswithresponses",
                            "creauthclienttotalresponses",
                            "creauthclientunknownresponses") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoRadiusExtMib.Creclientauthentication, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRadiusExtMib.Creclientauthentication, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.creauthclientaverageresponsedelay.is_set or
                self.creauthclientbadauthenticators.is_set or
                self.creauthclientbufferallocfailures.is_set or
                self.creauthclientdupids.is_set or
                self.creauthclientlastusedsourceid.is_set or
                self.creauthclientmalformedresponses.is_set or
                self.creauthclientmaxbuffersize.is_set or
                self.creauthclientmaxresponsedelay.is_set or
                self.creauthclienttimeouts.is_set or
                self.creauthclienttotalpacketswithoutresponses.is_set or
                self.creauthclienttotalpacketswithresponses.is_set or
                self.creauthclienttotalresponses.is_set or
                self.creauthclientunknownresponses.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.creauthclientaverageresponsedelay.yfilter != YFilter.not_set or
                self.creauthclientbadauthenticators.yfilter != YFilter.not_set or
                self.creauthclientbufferallocfailures.yfilter != YFilter.not_set or
                self.creauthclientdupids.yfilter != YFilter.not_set or
                self.creauthclientlastusedsourceid.yfilter != YFilter.not_set or
                self.creauthclientmalformedresponses.yfilter != YFilter.not_set or
                self.creauthclientmaxbuffersize.yfilter != YFilter.not_set or
                self.creauthclientmaxresponsedelay.yfilter != YFilter.not_set or
                self.creauthclienttimeouts.yfilter != YFilter.not_set or
                self.creauthclienttotalpacketswithoutresponses.yfilter != YFilter.not_set or
                self.creauthclienttotalpacketswithresponses.yfilter != YFilter.not_set or
                self.creauthclienttotalresponses.yfilter != YFilter.not_set or
                self.creauthclientunknownresponses.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "creClientAuthentication" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RADIUS-EXT-MIB:CISCO-RADIUS-EXT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.creauthclientaverageresponsedelay.is_set or self.creauthclientaverageresponsedelay.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creauthclientaverageresponsedelay.get_name_leafdata())
            if (self.creauthclientbadauthenticators.is_set or self.creauthclientbadauthenticators.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creauthclientbadauthenticators.get_name_leafdata())
            if (self.creauthclientbufferallocfailures.is_set or self.creauthclientbufferallocfailures.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creauthclientbufferallocfailures.get_name_leafdata())
            if (self.creauthclientdupids.is_set or self.creauthclientdupids.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creauthclientdupids.get_name_leafdata())
            if (self.creauthclientlastusedsourceid.is_set or self.creauthclientlastusedsourceid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creauthclientlastusedsourceid.get_name_leafdata())
            if (self.creauthclientmalformedresponses.is_set or self.creauthclientmalformedresponses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creauthclientmalformedresponses.get_name_leafdata())
            if (self.creauthclientmaxbuffersize.is_set or self.creauthclientmaxbuffersize.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creauthclientmaxbuffersize.get_name_leafdata())
            if (self.creauthclientmaxresponsedelay.is_set or self.creauthclientmaxresponsedelay.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creauthclientmaxresponsedelay.get_name_leafdata())
            if (self.creauthclienttimeouts.is_set or self.creauthclienttimeouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creauthclienttimeouts.get_name_leafdata())
            if (self.creauthclienttotalpacketswithoutresponses.is_set or self.creauthclienttotalpacketswithoutresponses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creauthclienttotalpacketswithoutresponses.get_name_leafdata())
            if (self.creauthclienttotalpacketswithresponses.is_set or self.creauthclienttotalpacketswithresponses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creauthclienttotalpacketswithresponses.get_name_leafdata())
            if (self.creauthclienttotalresponses.is_set or self.creauthclienttotalresponses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creauthclienttotalresponses.get_name_leafdata())
            if (self.creauthclientunknownresponses.is_set or self.creauthclientunknownresponses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creauthclientunknownresponses.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "creAuthClientAverageResponseDelay" or name == "creAuthClientBadAuthenticators" or name == "creAuthClientBufferAllocFailures" or name == "creAuthClientDupIDs" or name == "creAuthClientLastUsedSourceId" or name == "creAuthClientMalformedResponses" or name == "creAuthClientMaxBufferSize" or name == "creAuthClientMaxResponseDelay" or name == "creAuthClientTimeouts" or name == "creAuthClientTotalPacketsWithoutResponses" or name == "creAuthClientTotalPacketsWithResponses" or name == "creAuthClientTotalResponses" or name == "creAuthClientUnknownResponses"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "creAuthClientAverageResponseDelay"):
                self.creauthclientaverageresponsedelay = value
                self.creauthclientaverageresponsedelay.value_namespace = name_space
                self.creauthclientaverageresponsedelay.value_namespace_prefix = name_space_prefix
            if(value_path == "creAuthClientBadAuthenticators"):
                self.creauthclientbadauthenticators = value
                self.creauthclientbadauthenticators.value_namespace = name_space
                self.creauthclientbadauthenticators.value_namespace_prefix = name_space_prefix
            if(value_path == "creAuthClientBufferAllocFailures"):
                self.creauthclientbufferallocfailures = value
                self.creauthclientbufferallocfailures.value_namespace = name_space
                self.creauthclientbufferallocfailures.value_namespace_prefix = name_space_prefix
            if(value_path == "creAuthClientDupIDs"):
                self.creauthclientdupids = value
                self.creauthclientdupids.value_namespace = name_space
                self.creauthclientdupids.value_namespace_prefix = name_space_prefix
            if(value_path == "creAuthClientLastUsedSourceId"):
                self.creauthclientlastusedsourceid = value
                self.creauthclientlastusedsourceid.value_namespace = name_space
                self.creauthclientlastusedsourceid.value_namespace_prefix = name_space_prefix
            if(value_path == "creAuthClientMalformedResponses"):
                self.creauthclientmalformedresponses = value
                self.creauthclientmalformedresponses.value_namespace = name_space
                self.creauthclientmalformedresponses.value_namespace_prefix = name_space_prefix
            if(value_path == "creAuthClientMaxBufferSize"):
                self.creauthclientmaxbuffersize = value
                self.creauthclientmaxbuffersize.value_namespace = name_space
                self.creauthclientmaxbuffersize.value_namespace_prefix = name_space_prefix
            if(value_path == "creAuthClientMaxResponseDelay"):
                self.creauthclientmaxresponsedelay = value
                self.creauthclientmaxresponsedelay.value_namespace = name_space
                self.creauthclientmaxresponsedelay.value_namespace_prefix = name_space_prefix
            if(value_path == "creAuthClientTimeouts"):
                self.creauthclienttimeouts = value
                self.creauthclienttimeouts.value_namespace = name_space
                self.creauthclienttimeouts.value_namespace_prefix = name_space_prefix
            if(value_path == "creAuthClientTotalPacketsWithoutResponses"):
                self.creauthclienttotalpacketswithoutresponses = value
                self.creauthclienttotalpacketswithoutresponses.value_namespace = name_space
                self.creauthclienttotalpacketswithoutresponses.value_namespace_prefix = name_space_prefix
            if(value_path == "creAuthClientTotalPacketsWithResponses"):
                self.creauthclienttotalpacketswithresponses = value
                self.creauthclienttotalpacketswithresponses.value_namespace = name_space
                self.creauthclienttotalpacketswithresponses.value_namespace_prefix = name_space_prefix
            if(value_path == "creAuthClientTotalResponses"):
                self.creauthclienttotalresponses = value
                self.creauthclienttotalresponses.value_namespace = name_space
                self.creauthclienttotalresponses.value_namespace_prefix = name_space_prefix
            if(value_path == "creAuthClientUnknownResponses"):
                self.creauthclientunknownresponses = value
                self.creauthclientunknownresponses.value_namespace = name_space
                self.creauthclientunknownresponses.value_namespace_prefix = name_space_prefix


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
            super(CiscoRadiusExtMib.Creclientaccounting, self).__init__()

            self.yang_name = "creClientAccounting"
            self.yang_parent_name = "CISCO-RADIUS-EXT-MIB"

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

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("creacctclientaverageresponsedelay",
                            "creacctclientbadauthenticators",
                            "creacctclientbufferallocfailures",
                            "creacctclientdupids",
                            "creacctclientlastusedsourceid",
                            "creacctclientmalformedresponses",
                            "creacctclientmaxbuffersize",
                            "creacctclientmaxresponsedelay",
                            "creacctclienttimeouts",
                            "creacctclienttotalpacketswithoutresponses",
                            "creacctclienttotalpacketswithresponses",
                            "creacctclienttotalresponses",
                            "creacctclientunknownresponses") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoRadiusExtMib.Creclientaccounting, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRadiusExtMib.Creclientaccounting, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.creacctclientaverageresponsedelay.is_set or
                self.creacctclientbadauthenticators.is_set or
                self.creacctclientbufferallocfailures.is_set or
                self.creacctclientdupids.is_set or
                self.creacctclientlastusedsourceid.is_set or
                self.creacctclientmalformedresponses.is_set or
                self.creacctclientmaxbuffersize.is_set or
                self.creacctclientmaxresponsedelay.is_set or
                self.creacctclienttimeouts.is_set or
                self.creacctclienttotalpacketswithoutresponses.is_set or
                self.creacctclienttotalpacketswithresponses.is_set or
                self.creacctclienttotalresponses.is_set or
                self.creacctclientunknownresponses.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.creacctclientaverageresponsedelay.yfilter != YFilter.not_set or
                self.creacctclientbadauthenticators.yfilter != YFilter.not_set or
                self.creacctclientbufferallocfailures.yfilter != YFilter.not_set or
                self.creacctclientdupids.yfilter != YFilter.not_set or
                self.creacctclientlastusedsourceid.yfilter != YFilter.not_set or
                self.creacctclientmalformedresponses.yfilter != YFilter.not_set or
                self.creacctclientmaxbuffersize.yfilter != YFilter.not_set or
                self.creacctclientmaxresponsedelay.yfilter != YFilter.not_set or
                self.creacctclienttimeouts.yfilter != YFilter.not_set or
                self.creacctclienttotalpacketswithoutresponses.yfilter != YFilter.not_set or
                self.creacctclienttotalpacketswithresponses.yfilter != YFilter.not_set or
                self.creacctclienttotalresponses.yfilter != YFilter.not_set or
                self.creacctclientunknownresponses.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "creClientAccounting" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RADIUS-EXT-MIB:CISCO-RADIUS-EXT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.creacctclientaverageresponsedelay.is_set or self.creacctclientaverageresponsedelay.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creacctclientaverageresponsedelay.get_name_leafdata())
            if (self.creacctclientbadauthenticators.is_set or self.creacctclientbadauthenticators.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creacctclientbadauthenticators.get_name_leafdata())
            if (self.creacctclientbufferallocfailures.is_set or self.creacctclientbufferallocfailures.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creacctclientbufferallocfailures.get_name_leafdata())
            if (self.creacctclientdupids.is_set or self.creacctclientdupids.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creacctclientdupids.get_name_leafdata())
            if (self.creacctclientlastusedsourceid.is_set or self.creacctclientlastusedsourceid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creacctclientlastusedsourceid.get_name_leafdata())
            if (self.creacctclientmalformedresponses.is_set or self.creacctclientmalformedresponses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creacctclientmalformedresponses.get_name_leafdata())
            if (self.creacctclientmaxbuffersize.is_set or self.creacctclientmaxbuffersize.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creacctclientmaxbuffersize.get_name_leafdata())
            if (self.creacctclientmaxresponsedelay.is_set or self.creacctclientmaxresponsedelay.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creacctclientmaxresponsedelay.get_name_leafdata())
            if (self.creacctclienttimeouts.is_set or self.creacctclienttimeouts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creacctclienttimeouts.get_name_leafdata())
            if (self.creacctclienttotalpacketswithoutresponses.is_set or self.creacctclienttotalpacketswithoutresponses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creacctclienttotalpacketswithoutresponses.get_name_leafdata())
            if (self.creacctclienttotalpacketswithresponses.is_set or self.creacctclienttotalpacketswithresponses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creacctclienttotalpacketswithresponses.get_name_leafdata())
            if (self.creacctclienttotalresponses.is_set or self.creacctclienttotalresponses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creacctclienttotalresponses.get_name_leafdata())
            if (self.creacctclientunknownresponses.is_set or self.creacctclientunknownresponses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.creacctclientunknownresponses.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "creAcctClientAverageResponseDelay" or name == "creAcctClientBadAuthenticators" or name == "creAcctClientBufferAllocFailures" or name == "creAcctClientDupIDs" or name == "creAcctClientLastUsedSourceId" or name == "creAcctClientMalformedResponses" or name == "creAcctClientMaxBufferSize" or name == "creAcctClientMaxResponseDelay" or name == "creAcctClientTimeouts" or name == "creAcctClientTotalPacketsWithoutResponses" or name == "creAcctClientTotalPacketsWithResponses" or name == "creAcctClientTotalResponses" or name == "creAcctClientUnknownResponses"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "creAcctClientAverageResponseDelay"):
                self.creacctclientaverageresponsedelay = value
                self.creacctclientaverageresponsedelay.value_namespace = name_space
                self.creacctclientaverageresponsedelay.value_namespace_prefix = name_space_prefix
            if(value_path == "creAcctClientBadAuthenticators"):
                self.creacctclientbadauthenticators = value
                self.creacctclientbadauthenticators.value_namespace = name_space
                self.creacctclientbadauthenticators.value_namespace_prefix = name_space_prefix
            if(value_path == "creAcctClientBufferAllocFailures"):
                self.creacctclientbufferallocfailures = value
                self.creacctclientbufferallocfailures.value_namespace = name_space
                self.creacctclientbufferallocfailures.value_namespace_prefix = name_space_prefix
            if(value_path == "creAcctClientDupIDs"):
                self.creacctclientdupids = value
                self.creacctclientdupids.value_namespace = name_space
                self.creacctclientdupids.value_namespace_prefix = name_space_prefix
            if(value_path == "creAcctClientLastUsedSourceId"):
                self.creacctclientlastusedsourceid = value
                self.creacctclientlastusedsourceid.value_namespace = name_space
                self.creacctclientlastusedsourceid.value_namespace_prefix = name_space_prefix
            if(value_path == "creAcctClientMalformedResponses"):
                self.creacctclientmalformedresponses = value
                self.creacctclientmalformedresponses.value_namespace = name_space
                self.creacctclientmalformedresponses.value_namespace_prefix = name_space_prefix
            if(value_path == "creAcctClientMaxBufferSize"):
                self.creacctclientmaxbuffersize = value
                self.creacctclientmaxbuffersize.value_namespace = name_space
                self.creacctclientmaxbuffersize.value_namespace_prefix = name_space_prefix
            if(value_path == "creAcctClientMaxResponseDelay"):
                self.creacctclientmaxresponsedelay = value
                self.creacctclientmaxresponsedelay.value_namespace = name_space
                self.creacctclientmaxresponsedelay.value_namespace_prefix = name_space_prefix
            if(value_path == "creAcctClientTimeouts"):
                self.creacctclienttimeouts = value
                self.creacctclienttimeouts.value_namespace = name_space
                self.creacctclienttimeouts.value_namespace_prefix = name_space_prefix
            if(value_path == "creAcctClientTotalPacketsWithoutResponses"):
                self.creacctclienttotalpacketswithoutresponses = value
                self.creacctclienttotalpacketswithoutresponses.value_namespace = name_space
                self.creacctclienttotalpacketswithoutresponses.value_namespace_prefix = name_space_prefix
            if(value_path == "creAcctClientTotalPacketsWithResponses"):
                self.creacctclienttotalpacketswithresponses = value
                self.creacctclienttotalpacketswithresponses.value_namespace = name_space
                self.creacctclienttotalpacketswithresponses.value_namespace_prefix = name_space_prefix
            if(value_path == "creAcctClientTotalResponses"):
                self.creacctclienttotalresponses = value
                self.creacctclienttotalresponses.value_namespace = name_space
                self.creacctclienttotalresponses.value_namespace_prefix = name_space_prefix
            if(value_path == "creAcctClientUnknownResponses"):
                self.creacctclientunknownresponses = value
                self.creacctclientunknownresponses.value_namespace = name_space
                self.creacctclientunknownresponses.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.creclientaccounting is not None and self.creclientaccounting.has_data()) or
            (self.creclientauthentication is not None and self.creclientauthentication.has_data()) or
            (self.creclientglobal is not None and self.creclientglobal.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.creclientaccounting is not None and self.creclientaccounting.has_operation()) or
            (self.creclientauthentication is not None and self.creclientauthentication.has_operation()) or
            (self.creclientglobal is not None and self.creclientglobal.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-RADIUS-EXT-MIB:CISCO-RADIUS-EXT-MIB" + path_buffer

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

        if (child_yang_name == "creClientAccounting"):
            if (self.creclientaccounting is None):
                self.creclientaccounting = CiscoRadiusExtMib.Creclientaccounting()
                self.creclientaccounting.parent = self
                self._children_name_map["creclientaccounting"] = "creClientAccounting"
            return self.creclientaccounting

        if (child_yang_name == "creClientAuthentication"):
            if (self.creclientauthentication is None):
                self.creclientauthentication = CiscoRadiusExtMib.Creclientauthentication()
                self.creclientauthentication.parent = self
                self._children_name_map["creclientauthentication"] = "creClientAuthentication"
            return self.creclientauthentication

        if (child_yang_name == "creClientGlobal"):
            if (self.creclientglobal is None):
                self.creclientglobal = CiscoRadiusExtMib.Creclientglobal()
                self.creclientglobal.parent = self
                self._children_name_map["creclientglobal"] = "creClientGlobal"
            return self.creclientglobal

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "creClientAccounting" or name == "creClientAuthentication" or name == "creClientGlobal"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoRadiusExtMib()
        return self._top_entity

