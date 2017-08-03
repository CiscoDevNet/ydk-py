""" RFC1315_MIB 


"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Rfc1315Mib(Entity):
    """
    
    
    .. attribute:: frame_relay_globals
    
    	
    	**type**\:   :py:class:`FrameRelayGlobals <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.FrameRelayGlobals>`
    
    .. attribute:: frcircuittable
    
    	A table containing information about specific Data Link Connection Identifiers and corresponding virtual circuits
    	**type**\:   :py:class:`Frcircuittable <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frcircuittable>`
    
    .. attribute:: frdlcmitable
    
    	The Parameters for the Data Link Connection Management Interface for the frame relay service on this interface
    	**type**\:   :py:class:`Frdlcmitable <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frdlcmitable>`
    
    .. attribute:: frerrtable
    
    	A table containing information about Errors on the Frame Relay interface
    	**type**\:   :py:class:`Frerrtable <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frerrtable>`
    
    

    """

    _prefix = 'RFC1315-MIB'

    def __init__(self):
        super(Rfc1315Mib, self).__init__()
        self._top_entity = None

        self.yang_name = "RFC1315-MIB"
        self.yang_parent_name = "RFC1315-MIB"

        self.frame_relay_globals = Rfc1315Mib.FrameRelayGlobals()
        self.frame_relay_globals.parent = self
        self._children_name_map["frame_relay_globals"] = "frame-relay-globals"
        self._children_yang_names.add("frame-relay-globals")

        self.frcircuittable = Rfc1315Mib.Frcircuittable()
        self.frcircuittable.parent = self
        self._children_name_map["frcircuittable"] = "frCircuitTable"
        self._children_yang_names.add("frCircuitTable")

        self.frdlcmitable = Rfc1315Mib.Frdlcmitable()
        self.frdlcmitable.parent = self
        self._children_name_map["frdlcmitable"] = "frDlcmiTable"
        self._children_yang_names.add("frDlcmiTable")

        self.frerrtable = Rfc1315Mib.Frerrtable()
        self.frerrtable.parent = self
        self._children_name_map["frerrtable"] = "frErrTable"
        self._children_yang_names.add("frErrTable")


    class FrameRelayGlobals(Entity):
        """
        
        
        .. attribute:: frtrapstate
        
        	This variable  indicates  whether  the  system produces the frDLCIStatusChange trap
        	**type**\:   :py:class:`Frtrapstate <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.FrameRelayGlobals.Frtrapstate>`
        
        

        """

        _prefix = 'RFC1315-MIB'

        def __init__(self):
            super(Rfc1315Mib.FrameRelayGlobals, self).__init__()

            self.yang_name = "frame-relay-globals"
            self.yang_parent_name = "RFC1315-MIB"

            self.frtrapstate = YLeaf(YType.enumeration, "frTrapState")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("frtrapstate") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Rfc1315Mib.FrameRelayGlobals, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1315Mib.FrameRelayGlobals, self).__setattr__(name, value)

        class Frtrapstate(Enum):
            """
            Frtrapstate

            This variable  indicates  whether  the  system

            produces the frDLCIStatusChange trap.

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = Enum.YLeaf(1, "enabled")

            disabled = Enum.YLeaf(2, "disabled")


        def has_data(self):
            return self.frtrapstate.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.frtrapstate.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "frame-relay-globals" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RFC1315-MIB:RFC1315-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.frtrapstate.is_set or self.frtrapstate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.frtrapstate.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "frTrapState"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "frTrapState"):
                self.frtrapstate = value
                self.frtrapstate.value_namespace = name_space
                self.frtrapstate.value_namespace_prefix = name_space_prefix


    class Frdlcmitable(Entity):
        """
        The Parameters for the Data Link Connection Management
        Interface for the frame relay service on this
        interface.
        
        .. attribute:: frdlcmientry
        
        	The Parameters for a particular Data Link Con\- nection Management Interface
        	**type**\: list of    :py:class:`Frdlcmientry <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frdlcmitable.Frdlcmientry>`
        
        

        """

        _prefix = 'RFC1315-MIB'

        def __init__(self):
            super(Rfc1315Mib.Frdlcmitable, self).__init__()

            self.yang_name = "frDlcmiTable"
            self.yang_parent_name = "RFC1315-MIB"

            self.frdlcmientry = YList(self)

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
                        super(Rfc1315Mib.Frdlcmitable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1315Mib.Frdlcmitable, self).__setattr__(name, value)


        class Frdlcmientry(Entity):
            """
            The Parameters for a particular Data Link Con\-
            nection Management Interface.
            
            .. attribute:: frdlcmiifindex  <key>
            
            	The ifIndex value of the  corresponding  ifEn\- try
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frdlcmiaddress
            
            	This variable states which address  format  is in use on the Frame Relay interface
            	**type**\:   :py:class:`Frdlcmiaddress <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frdlcmitable.Frdlcmientry.Frdlcmiaddress>`
            
            .. attribute:: frdlcmiaddresslen
            
            	This variable states which address  length  in octets.  In the case of Q922 format, the length indicates the entire length of the address  in\- cluding the control portion
            	**type**\:   :py:class:`Frdlcmiaddresslen <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frdlcmitable.Frdlcmientry.Frdlcmiaddresslen>`
            
            .. attribute:: frdlcmierrorthreshold
            
            	This  is  the  maximum  number  of  unanswered Status Enquiries the equipment shall accept be\- fore declaring the interface down
            	**type**\:  int
            
            	**range:** 1..10
            
            .. attribute:: frdlcmifullenquiryinterval
            
            	Number of status enquiry intervals  that  pass before  issuance  of a full status enquiry mes\- sage
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: frdlcmimaxsupportedvcs
            
            	The maximum number of Virtual Circuits allowed for  this  interface.   Usually dictated by the Frame Relay network.  In response to a SET, if a value less than zero or  higher  than the agent's maximal capability is configured, the agent  should  respond  bad\- Value
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frdlcmimonitoredevents
            
            	This is the number of status polling intervals over which the error threshold is counted.  For example, if within 'MonitoredEvents' number  of events  the  station  receives 'ErrorThreshold' number of errors, the interface  is  marked  as down
            	**type**\:  int
            
            	**range:** 1..10
            
            .. attribute:: frdlcmimulticast
            
            	This indicates whether the Frame Relay  inter\- face is using a multicast service
            	**type**\:   :py:class:`Frdlcmimulticast <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frdlcmitable.Frdlcmientry.Frdlcmimulticast>`
            
            .. attribute:: frdlcmipollinginterval
            
            	This is the number of seconds between  succes\- sive status enquiry messages
            	**type**\:  int
            
            	**range:** 5..30
            
            .. attribute:: frdlcmistate
            
            	This variable states which Data  Link  Connec\- tion Management scheme is active (and by impli\- cation, what DLCI it uses) on the  Frame  Relay interface
            	**type**\:   :py:class:`Frdlcmistate <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frdlcmitable.Frdlcmientry.Frdlcmistate>`
            
            

            """

            _prefix = 'RFC1315-MIB'

            def __init__(self):
                super(Rfc1315Mib.Frdlcmitable.Frdlcmientry, self).__init__()

                self.yang_name = "frDlcmiEntry"
                self.yang_parent_name = "frDlcmiTable"

                self.frdlcmiifindex = YLeaf(YType.int32, "frDlcmiIfIndex")

                self.frdlcmiaddress = YLeaf(YType.enumeration, "frDlcmiAddress")

                self.frdlcmiaddresslen = YLeaf(YType.enumeration, "frDlcmiAddressLen")

                self.frdlcmierrorthreshold = YLeaf(YType.int32, "frDlcmiErrorThreshold")

                self.frdlcmifullenquiryinterval = YLeaf(YType.int32, "frDlcmiFullEnquiryInterval")

                self.frdlcmimaxsupportedvcs = YLeaf(YType.int32, "frDlcmiMaxSupportedVCs")

                self.frdlcmimonitoredevents = YLeaf(YType.int32, "frDlcmiMonitoredEvents")

                self.frdlcmimulticast = YLeaf(YType.enumeration, "frDlcmiMulticast")

                self.frdlcmipollinginterval = YLeaf(YType.int32, "frDlcmiPollingInterval")

                self.frdlcmistate = YLeaf(YType.enumeration, "frDlcmiState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("frdlcmiifindex",
                                "frdlcmiaddress",
                                "frdlcmiaddresslen",
                                "frdlcmierrorthreshold",
                                "frdlcmifullenquiryinterval",
                                "frdlcmimaxsupportedvcs",
                                "frdlcmimonitoredevents",
                                "frdlcmimulticast",
                                "frdlcmipollinginterval",
                                "frdlcmistate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rfc1315Mib.Frdlcmitable.Frdlcmientry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rfc1315Mib.Frdlcmitable.Frdlcmientry, self).__setattr__(name, value)

            class Frdlcmiaddress(Enum):
                """
                Frdlcmiaddress

                This variable states which address  format  is

                in use on the Frame Relay interface.

                .. data:: q921 = 1

                .. data:: q922March90 = 2

                .. data:: q922November90 = 3

                .. data:: q922 = 4

                """

                q921 = Enum.YLeaf(1, "q921")

                q922March90 = Enum.YLeaf(2, "q922March90")

                q922November90 = Enum.YLeaf(3, "q922November90")

                q922 = Enum.YLeaf(4, "q922")


            class Frdlcmiaddresslen(Enum):
                """
                Frdlcmiaddresslen

                This variable states which address  length  in

                octets.  In the case of Q922 format, the length

                indicates the entire length of the address  in\-

                cluding the control portion.

                .. data:: two_octets = 2

                .. data:: three_octets = 3

                .. data:: four_octets = 4

                """

                two_octets = Enum.YLeaf(2, "two-octets")

                three_octets = Enum.YLeaf(3, "three-octets")

                four_octets = Enum.YLeaf(4, "four-octets")


            class Frdlcmimulticast(Enum):
                """
                Frdlcmimulticast

                This indicates whether the Frame Relay  inter\-

                face is using a multicast service.

                .. data:: nonBroadcast = 1

                .. data:: broadcast = 2

                """

                nonBroadcast = Enum.YLeaf(1, "nonBroadcast")

                broadcast = Enum.YLeaf(2, "broadcast")


            class Frdlcmistate(Enum):
                """
                Frdlcmistate

                This variable states which Data  Link  Connec\-

                tion Management scheme is active (and by impli\-

                cation, what DLCI it uses) on the  Frame  Relay

                interface.

                .. data:: noLmiConfigured = 1

                .. data:: lmiRev1 = 2

                .. data:: ansiT1_617_D = 3

                .. data:: ansiT1_617_B = 4

                """

                noLmiConfigured = Enum.YLeaf(1, "noLmiConfigured")

                lmiRev1 = Enum.YLeaf(2, "lmiRev1")

                ansiT1_617_D = Enum.YLeaf(3, "ansiT1-617-D")

                ansiT1_617_B = Enum.YLeaf(4, "ansiT1-617-B")


            def has_data(self):
                return (
                    self.frdlcmiifindex.is_set or
                    self.frdlcmiaddress.is_set or
                    self.frdlcmiaddresslen.is_set or
                    self.frdlcmierrorthreshold.is_set or
                    self.frdlcmifullenquiryinterval.is_set or
                    self.frdlcmimaxsupportedvcs.is_set or
                    self.frdlcmimonitoredevents.is_set or
                    self.frdlcmimulticast.is_set or
                    self.frdlcmipollinginterval.is_set or
                    self.frdlcmistate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.frdlcmiifindex.yfilter != YFilter.not_set or
                    self.frdlcmiaddress.yfilter != YFilter.not_set or
                    self.frdlcmiaddresslen.yfilter != YFilter.not_set or
                    self.frdlcmierrorthreshold.yfilter != YFilter.not_set or
                    self.frdlcmifullenquiryinterval.yfilter != YFilter.not_set or
                    self.frdlcmimaxsupportedvcs.yfilter != YFilter.not_set or
                    self.frdlcmimonitoredevents.yfilter != YFilter.not_set or
                    self.frdlcmimulticast.yfilter != YFilter.not_set or
                    self.frdlcmipollinginterval.yfilter != YFilter.not_set or
                    self.frdlcmistate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "frDlcmiEntry" + "[frDlcmiIfIndex='" + self.frdlcmiifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RFC1315-MIB:RFC1315-MIB/frDlcmiTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.frdlcmiifindex.is_set or self.frdlcmiifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frdlcmiifindex.get_name_leafdata())
                if (self.frdlcmiaddress.is_set or self.frdlcmiaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frdlcmiaddress.get_name_leafdata())
                if (self.frdlcmiaddresslen.is_set or self.frdlcmiaddresslen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frdlcmiaddresslen.get_name_leafdata())
                if (self.frdlcmierrorthreshold.is_set or self.frdlcmierrorthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frdlcmierrorthreshold.get_name_leafdata())
                if (self.frdlcmifullenquiryinterval.is_set or self.frdlcmifullenquiryinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frdlcmifullenquiryinterval.get_name_leafdata())
                if (self.frdlcmimaxsupportedvcs.is_set or self.frdlcmimaxsupportedvcs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frdlcmimaxsupportedvcs.get_name_leafdata())
                if (self.frdlcmimonitoredevents.is_set or self.frdlcmimonitoredevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frdlcmimonitoredevents.get_name_leafdata())
                if (self.frdlcmimulticast.is_set or self.frdlcmimulticast.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frdlcmimulticast.get_name_leafdata())
                if (self.frdlcmipollinginterval.is_set or self.frdlcmipollinginterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frdlcmipollinginterval.get_name_leafdata())
                if (self.frdlcmistate.is_set or self.frdlcmistate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frdlcmistate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "frDlcmiIfIndex" or name == "frDlcmiAddress" or name == "frDlcmiAddressLen" or name == "frDlcmiErrorThreshold" or name == "frDlcmiFullEnquiryInterval" or name == "frDlcmiMaxSupportedVCs" or name == "frDlcmiMonitoredEvents" or name == "frDlcmiMulticast" or name == "frDlcmiPollingInterval" or name == "frDlcmiState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "frDlcmiIfIndex"):
                    self.frdlcmiifindex = value
                    self.frdlcmiifindex.value_namespace = name_space
                    self.frdlcmiifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "frDlcmiAddress"):
                    self.frdlcmiaddress = value
                    self.frdlcmiaddress.value_namespace = name_space
                    self.frdlcmiaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "frDlcmiAddressLen"):
                    self.frdlcmiaddresslen = value
                    self.frdlcmiaddresslen.value_namespace = name_space
                    self.frdlcmiaddresslen.value_namespace_prefix = name_space_prefix
                if(value_path == "frDlcmiErrorThreshold"):
                    self.frdlcmierrorthreshold = value
                    self.frdlcmierrorthreshold.value_namespace = name_space
                    self.frdlcmierrorthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "frDlcmiFullEnquiryInterval"):
                    self.frdlcmifullenquiryinterval = value
                    self.frdlcmifullenquiryinterval.value_namespace = name_space
                    self.frdlcmifullenquiryinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "frDlcmiMaxSupportedVCs"):
                    self.frdlcmimaxsupportedvcs = value
                    self.frdlcmimaxsupportedvcs.value_namespace = name_space
                    self.frdlcmimaxsupportedvcs.value_namespace_prefix = name_space_prefix
                if(value_path == "frDlcmiMonitoredEvents"):
                    self.frdlcmimonitoredevents = value
                    self.frdlcmimonitoredevents.value_namespace = name_space
                    self.frdlcmimonitoredevents.value_namespace_prefix = name_space_prefix
                if(value_path == "frDlcmiMulticast"):
                    self.frdlcmimulticast = value
                    self.frdlcmimulticast.value_namespace = name_space
                    self.frdlcmimulticast.value_namespace_prefix = name_space_prefix
                if(value_path == "frDlcmiPollingInterval"):
                    self.frdlcmipollinginterval = value
                    self.frdlcmipollinginterval.value_namespace = name_space
                    self.frdlcmipollinginterval.value_namespace_prefix = name_space_prefix
                if(value_path == "frDlcmiState"):
                    self.frdlcmistate = value
                    self.frdlcmistate.value_namespace = name_space
                    self.frdlcmistate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.frdlcmientry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.frdlcmientry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "frDlcmiTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RFC1315-MIB:RFC1315-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "frDlcmiEntry"):
                for c in self.frdlcmientry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Rfc1315Mib.Frdlcmitable.Frdlcmientry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.frdlcmientry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "frDlcmiEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Frcircuittable(Entity):
        """
        A table containing information about specific Data
        Link Connection Identifiers and corresponding virtual
        circuits.
        
        .. attribute:: frcircuitentry
        
        	The information regarding a single  Data  Link Connection Identifier
        	**type**\: list of    :py:class:`Frcircuitentry <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frcircuittable.Frcircuitentry>`
        
        

        """

        _prefix = 'RFC1315-MIB'

        def __init__(self):
            super(Rfc1315Mib.Frcircuittable, self).__init__()

            self.yang_name = "frCircuitTable"
            self.yang_parent_name = "RFC1315-MIB"

            self.frcircuitentry = YList(self)

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
                        super(Rfc1315Mib.Frcircuittable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1315Mib.Frcircuittable, self).__setattr__(name, value)


        class Frcircuitentry(Entity):
            """
            The information regarding a single  Data  Link
            Connection Identifier.
            
            .. attribute:: frcircuitifindex  <key>
            
            	The ifIndex Value of the ifEntry this  virtual circuit is layered onto
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitdlci  <key>
            
            	The Data Link Connection Identifier  for  this virtual circuit
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitcommittedburst
            
            	This variable indicates the maximum amount  of data,  in  bits,  that  the  network  agrees to transfer under normal  conditions,  during  the measurement interval
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitcreationtime
            
            	The value of sysUpTime when the  virtual  cir\- cuit was created, whether by the Data Link Con\- nection Management Interface  or  by  a  SetRe\- quest
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitexcessburst
            
            	This variable indicates the maximum amount  of uncommitted data bits that the network will at\- tempt to deliver over the measurement interval.  By default, if not configured when creating the entry, the Excess Information Burst Size is set to the value of ifSpeed
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitlasttimechange
            
            	The value of sysUpTime when last there  was  a change in the virtual circuit state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedbecns
            
            	Number of frames received from the network in\- dicating  backward congestion since the virtual circuit was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedfecns
            
            	Number of frames received from the network in\- dicating  forward  congestion since the virtual circuit was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedframes
            
            	Number of frames received  over  this  virtual circuit since it was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedoctets
            
            	Number of octets received  over  this  virtual circuit since it was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitsentframes
            
            	The number of frames sent  from  this  virtual circuit since it was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitsentoctets
            
            	The number of octets sent  from  this  virtual circuit since it was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitstate
            
            	Indicates whether the particular virtual  cir\- cuit  is operational.  In the absence of a Data Link Connection Management  Interface,  virtual circuit  entries  (rows) may be created by set\- ting virtual  circuit  state  to  'active',  or deleted by changing Circuit state to 'invalid'. Whether or not the row actually  disappears  is left  to the implementation, so this object may actually read as 'invalid' for  some  arbitrary length  of  time.   It is also legal to set the state of a virtual  circuit  to  'inactive'  to temporarily disable a given circuit
            	**type**\:   :py:class:`Frcircuitstate <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frcircuittable.Frcircuitentry.Frcircuitstate>`
            
            .. attribute:: frcircuitthroughput
            
            	Throughput is the average number of 'Frame Re\- lay  Information  Field'  bits  transferred per second across a user network interface  in  one direction, measured over the measurement inter\- val.  If the  configured  committed  burst  rate  and throughput  are  both non\-zero, the measurement interval T=frCircuitCommittedBurst/frCircuitThroughput.  If the  configured  committed  burst  rate  and throughput  are  both zero, the measurement in\- terval        T=frCircuitExcessBurst/ifSpeed
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'RFC1315-MIB'

            def __init__(self):
                super(Rfc1315Mib.Frcircuittable.Frcircuitentry, self).__init__()

                self.yang_name = "frCircuitEntry"
                self.yang_parent_name = "frCircuitTable"

                self.frcircuitifindex = YLeaf(YType.int32, "frCircuitIfIndex")

                self.frcircuitdlci = YLeaf(YType.int32, "frCircuitDlci")

                self.frcircuitcommittedburst = YLeaf(YType.int32, "frCircuitCommittedBurst")

                self.frcircuitcreationtime = YLeaf(YType.uint32, "frCircuitCreationTime")

                self.frcircuitexcessburst = YLeaf(YType.int32, "frCircuitExcessBurst")

                self.frcircuitlasttimechange = YLeaf(YType.uint32, "frCircuitLastTimeChange")

                self.frcircuitreceivedbecns = YLeaf(YType.uint32, "frCircuitReceivedBECNs")

                self.frcircuitreceivedfecns = YLeaf(YType.uint32, "frCircuitReceivedFECNs")

                self.frcircuitreceivedframes = YLeaf(YType.uint32, "frCircuitReceivedFrames")

                self.frcircuitreceivedoctets = YLeaf(YType.uint32, "frCircuitReceivedOctets")

                self.frcircuitsentframes = YLeaf(YType.uint32, "frCircuitSentFrames")

                self.frcircuitsentoctets = YLeaf(YType.uint32, "frCircuitSentOctets")

                self.frcircuitstate = YLeaf(YType.enumeration, "frCircuitState")

                self.frcircuitthroughput = YLeaf(YType.int32, "frCircuitThroughput")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("frcircuitifindex",
                                "frcircuitdlci",
                                "frcircuitcommittedburst",
                                "frcircuitcreationtime",
                                "frcircuitexcessburst",
                                "frcircuitlasttimechange",
                                "frcircuitreceivedbecns",
                                "frcircuitreceivedfecns",
                                "frcircuitreceivedframes",
                                "frcircuitreceivedoctets",
                                "frcircuitsentframes",
                                "frcircuitsentoctets",
                                "frcircuitstate",
                                "frcircuitthroughput") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rfc1315Mib.Frcircuittable.Frcircuitentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rfc1315Mib.Frcircuittable.Frcircuitentry, self).__setattr__(name, value)

            class Frcircuitstate(Enum):
                """
                Frcircuitstate

                Indicates whether the particular virtual  cir\-

                cuit  is operational.  In the absence of a Data

                Link Connection Management  Interface,  virtual

                circuit  entries  (rows) may be created by set\-

                ting virtual  circuit  state  to  'active',  or

                deleted by changing Circuit state to 'invalid'.

                Whether or not the row actually  disappears  is

                left  to the implementation, so this object may

                actually read as 'invalid' for  some  arbitrary

                length  of  time.   It is also legal to set the

                state of a virtual  circuit  to  'inactive'  to

                temporarily disable a given circuit.

                .. data:: invalid = 1

                .. data:: active = 2

                .. data:: inactive = 3

                """

                invalid = Enum.YLeaf(1, "invalid")

                active = Enum.YLeaf(2, "active")

                inactive = Enum.YLeaf(3, "inactive")


            def has_data(self):
                return (
                    self.frcircuitifindex.is_set or
                    self.frcircuitdlci.is_set or
                    self.frcircuitcommittedburst.is_set or
                    self.frcircuitcreationtime.is_set or
                    self.frcircuitexcessburst.is_set or
                    self.frcircuitlasttimechange.is_set or
                    self.frcircuitreceivedbecns.is_set or
                    self.frcircuitreceivedfecns.is_set or
                    self.frcircuitreceivedframes.is_set or
                    self.frcircuitreceivedoctets.is_set or
                    self.frcircuitsentframes.is_set or
                    self.frcircuitsentoctets.is_set or
                    self.frcircuitstate.is_set or
                    self.frcircuitthroughput.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.frcircuitifindex.yfilter != YFilter.not_set or
                    self.frcircuitdlci.yfilter != YFilter.not_set or
                    self.frcircuitcommittedburst.yfilter != YFilter.not_set or
                    self.frcircuitcreationtime.yfilter != YFilter.not_set or
                    self.frcircuitexcessburst.yfilter != YFilter.not_set or
                    self.frcircuitlasttimechange.yfilter != YFilter.not_set or
                    self.frcircuitreceivedbecns.yfilter != YFilter.not_set or
                    self.frcircuitreceivedfecns.yfilter != YFilter.not_set or
                    self.frcircuitreceivedframes.yfilter != YFilter.not_set or
                    self.frcircuitreceivedoctets.yfilter != YFilter.not_set or
                    self.frcircuitsentframes.yfilter != YFilter.not_set or
                    self.frcircuitsentoctets.yfilter != YFilter.not_set or
                    self.frcircuitstate.yfilter != YFilter.not_set or
                    self.frcircuitthroughput.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "frCircuitEntry" + "[frCircuitIfIndex='" + self.frcircuitifindex.get() + "']" + "[frCircuitDlci='" + self.frcircuitdlci.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RFC1315-MIB:RFC1315-MIB/frCircuitTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.frcircuitifindex.is_set or self.frcircuitifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitifindex.get_name_leafdata())
                if (self.frcircuitdlci.is_set or self.frcircuitdlci.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitdlci.get_name_leafdata())
                if (self.frcircuitcommittedburst.is_set or self.frcircuitcommittedburst.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitcommittedburst.get_name_leafdata())
                if (self.frcircuitcreationtime.is_set or self.frcircuitcreationtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitcreationtime.get_name_leafdata())
                if (self.frcircuitexcessburst.is_set or self.frcircuitexcessburst.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitexcessburst.get_name_leafdata())
                if (self.frcircuitlasttimechange.is_set or self.frcircuitlasttimechange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitlasttimechange.get_name_leafdata())
                if (self.frcircuitreceivedbecns.is_set or self.frcircuitreceivedbecns.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitreceivedbecns.get_name_leafdata())
                if (self.frcircuitreceivedfecns.is_set or self.frcircuitreceivedfecns.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitreceivedfecns.get_name_leafdata())
                if (self.frcircuitreceivedframes.is_set or self.frcircuitreceivedframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitreceivedframes.get_name_leafdata())
                if (self.frcircuitreceivedoctets.is_set or self.frcircuitreceivedoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitreceivedoctets.get_name_leafdata())
                if (self.frcircuitsentframes.is_set or self.frcircuitsentframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitsentframes.get_name_leafdata())
                if (self.frcircuitsentoctets.is_set or self.frcircuitsentoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitsentoctets.get_name_leafdata())
                if (self.frcircuitstate.is_set or self.frcircuitstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitstate.get_name_leafdata())
                if (self.frcircuitthroughput.is_set or self.frcircuitthroughput.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitthroughput.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "frCircuitIfIndex" or name == "frCircuitDlci" or name == "frCircuitCommittedBurst" or name == "frCircuitCreationTime" or name == "frCircuitExcessBurst" or name == "frCircuitLastTimeChange" or name == "frCircuitReceivedBECNs" or name == "frCircuitReceivedFECNs" or name == "frCircuitReceivedFrames" or name == "frCircuitReceivedOctets" or name == "frCircuitSentFrames" or name == "frCircuitSentOctets" or name == "frCircuitState" or name == "frCircuitThroughput"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "frCircuitIfIndex"):
                    self.frcircuitifindex = value
                    self.frcircuitifindex.value_namespace = name_space
                    self.frcircuitifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitDlci"):
                    self.frcircuitdlci = value
                    self.frcircuitdlci.value_namespace = name_space
                    self.frcircuitdlci.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitCommittedBurst"):
                    self.frcircuitcommittedburst = value
                    self.frcircuitcommittedburst.value_namespace = name_space
                    self.frcircuitcommittedburst.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitCreationTime"):
                    self.frcircuitcreationtime = value
                    self.frcircuitcreationtime.value_namespace = name_space
                    self.frcircuitcreationtime.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitExcessBurst"):
                    self.frcircuitexcessburst = value
                    self.frcircuitexcessburst.value_namespace = name_space
                    self.frcircuitexcessburst.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitLastTimeChange"):
                    self.frcircuitlasttimechange = value
                    self.frcircuitlasttimechange.value_namespace = name_space
                    self.frcircuitlasttimechange.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitReceivedBECNs"):
                    self.frcircuitreceivedbecns = value
                    self.frcircuitreceivedbecns.value_namespace = name_space
                    self.frcircuitreceivedbecns.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitReceivedFECNs"):
                    self.frcircuitreceivedfecns = value
                    self.frcircuitreceivedfecns.value_namespace = name_space
                    self.frcircuitreceivedfecns.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitReceivedFrames"):
                    self.frcircuitreceivedframes = value
                    self.frcircuitreceivedframes.value_namespace = name_space
                    self.frcircuitreceivedframes.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitReceivedOctets"):
                    self.frcircuitreceivedoctets = value
                    self.frcircuitreceivedoctets.value_namespace = name_space
                    self.frcircuitreceivedoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitSentFrames"):
                    self.frcircuitsentframes = value
                    self.frcircuitsentframes.value_namespace = name_space
                    self.frcircuitsentframes.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitSentOctets"):
                    self.frcircuitsentoctets = value
                    self.frcircuitsentoctets.value_namespace = name_space
                    self.frcircuitsentoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitState"):
                    self.frcircuitstate = value
                    self.frcircuitstate.value_namespace = name_space
                    self.frcircuitstate.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitThroughput"):
                    self.frcircuitthroughput = value
                    self.frcircuitthroughput.value_namespace = name_space
                    self.frcircuitthroughput.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.frcircuitentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.frcircuitentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "frCircuitTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RFC1315-MIB:RFC1315-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "frCircuitEntry"):
                for c in self.frcircuitentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Rfc1315Mib.Frcircuittable.Frcircuitentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.frcircuitentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "frCircuitEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Frerrtable(Entity):
        """
        A table containing information about Errors on the
        Frame Relay interface.
        
        .. attribute:: frerrentry
        
        	The error information for a single frame relay interface
        	**type**\: list of    :py:class:`Frerrentry <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frerrtable.Frerrentry>`
        
        

        """

        _prefix = 'RFC1315-MIB'

        def __init__(self):
            super(Rfc1315Mib.Frerrtable, self).__init__()

            self.yang_name = "frErrTable"
            self.yang_parent_name = "RFC1315-MIB"

            self.frerrentry = YList(self)

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
                        super(Rfc1315Mib.Frerrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1315Mib.Frerrtable, self).__setattr__(name, value)


        class Frerrentry(Entity):
            """
            The error information for a single frame relay
            interface.
            
            .. attribute:: frerrifindex  <key>
            
            	The ifIndex Value of the  corresponding  ifEn\- try
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frerrdata
            
            	An octet string containing as much of the  er\- ror  packet as possible.  As a minimum, it must contain the Q.922 Address or  as  much  as  was delivered.   It is desirable to include all in\- formation up to the PDU
            	**type**\:  str
            
            .. attribute:: frerrtime
            
            	The value of sysUpTime at which the error  was detected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frerrtype
            
            	The type of error that was last seen  on  this interface
            	**type**\:   :py:class:`Frerrtype <ydk.models.cisco_ios_xe.RFC1315_MIB.Rfc1315Mib.Frerrtable.Frerrentry.Frerrtype>`
            
            

            """

            _prefix = 'RFC1315-MIB'

            def __init__(self):
                super(Rfc1315Mib.Frerrtable.Frerrentry, self).__init__()

                self.yang_name = "frErrEntry"
                self.yang_parent_name = "frErrTable"

                self.frerrifindex = YLeaf(YType.int32, "frErrIfIndex")

                self.frerrdata = YLeaf(YType.str, "frErrData")

                self.frerrtime = YLeaf(YType.uint32, "frErrTime")

                self.frerrtype = YLeaf(YType.enumeration, "frErrType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("frerrifindex",
                                "frerrdata",
                                "frerrtime",
                                "frerrtype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rfc1315Mib.Frerrtable.Frerrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rfc1315Mib.Frerrtable.Frerrentry, self).__setattr__(name, value)

            class Frerrtype(Enum):
                """
                Frerrtype

                The type of error that was last seen  on  this

                interface.

                .. data:: unknownError = 1

                .. data:: receiveShort = 2

                .. data:: receiveLong = 3

                .. data:: illegalDLCI = 4

                .. data:: unknownDLCI = 5

                .. data:: dlcmiProtoErr = 6

                .. data:: dlcmiUnknownIE = 7

                .. data:: dlcmiSequenceErr = 8

                .. data:: dlcmiUnknownRpt = 9

                .. data:: noErrorSinceReset = 10

                """

                unknownError = Enum.YLeaf(1, "unknownError")

                receiveShort = Enum.YLeaf(2, "receiveShort")

                receiveLong = Enum.YLeaf(3, "receiveLong")

                illegalDLCI = Enum.YLeaf(4, "illegalDLCI")

                unknownDLCI = Enum.YLeaf(5, "unknownDLCI")

                dlcmiProtoErr = Enum.YLeaf(6, "dlcmiProtoErr")

                dlcmiUnknownIE = Enum.YLeaf(7, "dlcmiUnknownIE")

                dlcmiSequenceErr = Enum.YLeaf(8, "dlcmiSequenceErr")

                dlcmiUnknownRpt = Enum.YLeaf(9, "dlcmiUnknownRpt")

                noErrorSinceReset = Enum.YLeaf(10, "noErrorSinceReset")


            def has_data(self):
                return (
                    self.frerrifindex.is_set or
                    self.frerrdata.is_set or
                    self.frerrtime.is_set or
                    self.frerrtype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.frerrifindex.yfilter != YFilter.not_set or
                    self.frerrdata.yfilter != YFilter.not_set or
                    self.frerrtime.yfilter != YFilter.not_set or
                    self.frerrtype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "frErrEntry" + "[frErrIfIndex='" + self.frerrifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RFC1315-MIB:RFC1315-MIB/frErrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.frerrifindex.is_set or self.frerrifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frerrifindex.get_name_leafdata())
                if (self.frerrdata.is_set or self.frerrdata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frerrdata.get_name_leafdata())
                if (self.frerrtime.is_set or self.frerrtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frerrtime.get_name_leafdata())
                if (self.frerrtype.is_set or self.frerrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frerrtype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "frErrIfIndex" or name == "frErrData" or name == "frErrTime" or name == "frErrType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "frErrIfIndex"):
                    self.frerrifindex = value
                    self.frerrifindex.value_namespace = name_space
                    self.frerrifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "frErrData"):
                    self.frerrdata = value
                    self.frerrdata.value_namespace = name_space
                    self.frerrdata.value_namespace_prefix = name_space_prefix
                if(value_path == "frErrTime"):
                    self.frerrtime = value
                    self.frerrtime.value_namespace = name_space
                    self.frerrtime.value_namespace_prefix = name_space_prefix
                if(value_path == "frErrType"):
                    self.frerrtype = value
                    self.frerrtype.value_namespace = name_space
                    self.frerrtype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.frerrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.frerrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "frErrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RFC1315-MIB:RFC1315-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "frErrEntry"):
                for c in self.frerrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Rfc1315Mib.Frerrtable.Frerrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.frerrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "frErrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.frame_relay_globals is not None and self.frame_relay_globals.has_data()) or
            (self.frcircuittable is not None and self.frcircuittable.has_data()) or
            (self.frdlcmitable is not None and self.frdlcmitable.has_data()) or
            (self.frerrtable is not None and self.frerrtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.frame_relay_globals is not None and self.frame_relay_globals.has_operation()) or
            (self.frcircuittable is not None and self.frcircuittable.has_operation()) or
            (self.frdlcmitable is not None and self.frdlcmitable.has_operation()) or
            (self.frerrtable is not None and self.frerrtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "RFC1315-MIB:RFC1315-MIB" + path_buffer

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

        if (child_yang_name == "frame-relay-globals"):
            if (self.frame_relay_globals is None):
                self.frame_relay_globals = Rfc1315Mib.FrameRelayGlobals()
                self.frame_relay_globals.parent = self
                self._children_name_map["frame_relay_globals"] = "frame-relay-globals"
            return self.frame_relay_globals

        if (child_yang_name == "frCircuitTable"):
            if (self.frcircuittable is None):
                self.frcircuittable = Rfc1315Mib.Frcircuittable()
                self.frcircuittable.parent = self
                self._children_name_map["frcircuittable"] = "frCircuitTable"
            return self.frcircuittable

        if (child_yang_name == "frDlcmiTable"):
            if (self.frdlcmitable is None):
                self.frdlcmitable = Rfc1315Mib.Frdlcmitable()
                self.frdlcmitable.parent = self
                self._children_name_map["frdlcmitable"] = "frDlcmiTable"
            return self.frdlcmitable

        if (child_yang_name == "frErrTable"):
            if (self.frerrtable is None):
                self.frerrtable = Rfc1315Mib.Frerrtable()
                self.frerrtable.parent = self
                self._children_name_map["frerrtable"] = "frErrTable"
            return self.frerrtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "frame-relay-globals" or name == "frCircuitTable" or name == "frDlcmiTable" or name == "frErrTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Rfc1315Mib()
        return self._top_entity

