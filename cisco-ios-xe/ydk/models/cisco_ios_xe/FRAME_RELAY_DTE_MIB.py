""" FRAME_RELAY_DTE_MIB 

The MIB module to describe the use of a Frame Relay
interface by a DTE.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FrameRelayDteMib(Entity):
    """
    
    
    .. attribute:: framerelaytrapcontrol
    
    	
    	**type**\:   :py:class:`Framerelaytrapcontrol <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Framerelaytrapcontrol>`
    
    .. attribute:: frcircuittable
    
    	A table containing information about specific Data Link Connections (DLC) or virtual circuits
    	**type**\:   :py:class:`Frcircuittable <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frcircuittable>`
    
    .. attribute:: frdlcmitable
    
    	The Parameters for the Data Link Connection Management Interface for the frame relay service on this interface
    	**type**\:   :py:class:`Frdlcmitable <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frdlcmitable>`
    
    .. attribute:: frerrtable
    
    	A table containing information about Errors on the Frame Relay interface.  Discontinuities in the counters contained in this table are the same as apply to the ifEntry associated with the Interface
    	**type**\:   :py:class:`Frerrtable <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frerrtable>`
    
    

    """

    _prefix = 'FRAME-RELAY-DTE-MIB'
    _revision = '1997-05-01'

    def __init__(self):
        super(FrameRelayDteMib, self).__init__()
        self._top_entity = None

        self.yang_name = "FRAME-RELAY-DTE-MIB"
        self.yang_parent_name = "FRAME-RELAY-DTE-MIB"

        self.framerelaytrapcontrol = FrameRelayDteMib.Framerelaytrapcontrol()
        self.framerelaytrapcontrol.parent = self
        self._children_name_map["framerelaytrapcontrol"] = "frameRelayTrapControl"
        self._children_yang_names.add("frameRelayTrapControl")

        self.frcircuittable = FrameRelayDteMib.Frcircuittable()
        self.frcircuittable.parent = self
        self._children_name_map["frcircuittable"] = "frCircuitTable"
        self._children_yang_names.add("frCircuitTable")

        self.frdlcmitable = FrameRelayDteMib.Frdlcmitable()
        self.frdlcmitable.parent = self
        self._children_name_map["frdlcmitable"] = "frDlcmiTable"
        self._children_yang_names.add("frDlcmiTable")

        self.frerrtable = FrameRelayDteMib.Frerrtable()
        self.frerrtable.parent = self
        self._children_name_map["frerrtable"] = "frErrTable"
        self._children_yang_names.add("frErrTable")


    class Framerelaytrapcontrol(Entity):
        """
        
        
        .. attribute:: frtrapmaxrate
        
        	This variable indicates the number of milliseconds that must elapse between trap emissions.  If events occur more rapidly, the impementation may simply fail to trap, or may queue traps until an appropriate time
        	**type**\:  int
        
        	**range:** 0..3600000
        
        .. attribute:: frtrapstate
        
        	This variable indicates whether the system produces the frDLCIStatusChange trap
        	**type**\:   :py:class:`Frtrapstate <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Framerelaytrapcontrol.Frtrapstate>`
        
        

        """

        _prefix = 'FRAME-RELAY-DTE-MIB'
        _revision = '1997-05-01'

        def __init__(self):
            super(FrameRelayDteMib.Framerelaytrapcontrol, self).__init__()

            self.yang_name = "frameRelayTrapControl"
            self.yang_parent_name = "FRAME-RELAY-DTE-MIB"

            self.frtrapmaxrate = YLeaf(YType.int32, "frTrapMaxRate")

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
                if name in ("frtrapmaxrate",
                            "frtrapstate") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(FrameRelayDteMib.Framerelaytrapcontrol, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(FrameRelayDteMib.Framerelaytrapcontrol, self).__setattr__(name, value)

        class Frtrapstate(Enum):
            """
            Frtrapstate

            This variable indicates whether the system produces

            the frDLCIStatusChange trap.

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = Enum.YLeaf(1, "enabled")

            disabled = Enum.YLeaf(2, "disabled")


        def has_data(self):
            return (
                self.frtrapmaxrate.is_set or
                self.frtrapstate.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.frtrapmaxrate.yfilter != YFilter.not_set or
                self.frtrapstate.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "frameRelayTrapControl" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.frtrapmaxrate.is_set or self.frtrapmaxrate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.frtrapmaxrate.get_name_leafdata())
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
            if(name == "frTrapMaxRate" or name == "frTrapState"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "frTrapMaxRate"):
                self.frtrapmaxrate = value
                self.frtrapmaxrate.value_namespace = name_space
                self.frtrapmaxrate.value_namespace_prefix = name_space_prefix
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
        
        	The Parameters for a particular Data Link Connection Management Interface
        	**type**\: list of    :py:class:`Frdlcmientry <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frdlcmitable.Frdlcmientry>`
        
        

        """

        _prefix = 'FRAME-RELAY-DTE-MIB'
        _revision = '1997-05-01'

        def __init__(self):
            super(FrameRelayDteMib.Frdlcmitable, self).__init__()

            self.yang_name = "frDlcmiTable"
            self.yang_parent_name = "FRAME-RELAY-DTE-MIB"

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
                        super(FrameRelayDteMib.Frdlcmitable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(FrameRelayDteMib.Frdlcmitable, self).__setattr__(name, value)


        class Frdlcmientry(Entity):
            """
            The Parameters for a particular Data Link Connection
            Management Interface.
            
            .. attribute:: frdlcmiifindex  <key>
            
            	The ifIndex value of the corresponding ifEntry
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: frdlcmiaddress
            
            	This variable states which address format is in use on the Frame Relay interface
            	**type**\:   :py:class:`Frdlcmiaddress <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frdlcmitable.Frdlcmientry.Frdlcmiaddress>`
            
            .. attribute:: frdlcmiaddresslen
            
            	This variable states the address length in octets.  In the case of Q922 format, the length indicates the entire length of the address including the control portion
            	**type**\:   :py:class:`Frdlcmiaddresslen <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frdlcmitable.Frdlcmientry.Frdlcmiaddresslen>`
            
            .. attribute:: frdlcmierrorthreshold
            
            	This is the maximum number of unanswered Status Enquiries the equipment shall accept before declaring the interface down
            	**type**\:  int
            
            	**range:** 1..10
            
            .. attribute:: frdlcmifullenquiryinterval
            
            	Number of status enquiry intervals that pass before issuance of a full status enquiry message
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: frdlcmimaxsupportedvcs
            
            	The maximum number of Virtual Circuits allowed for this interface.  Usually dictated by the Frame Relay network.  In response to a SET, if a value less than zero or higher than the agent's maximal capability is configured, the agent should respond badValue
            	**type**\:  int
            
            	**range:** 0..8388607
            
            .. attribute:: frdlcmimonitoredevents
            
            	This is the number of status polling intervals over which the error threshold is counted.  For example, if within 'MonitoredEvents' number of events the station receives 'ErrorThreshold' number of errors, the interface is marked as down
            	**type**\:  int
            
            	**range:** 1..10
            
            .. attribute:: frdlcmimulticast
            
            	This indicates whether the Frame Relay interface is using a multicast service
            	**type**\:   :py:class:`Frdlcmimulticast <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frdlcmitable.Frdlcmientry.Frdlcmimulticast>`
            
            .. attribute:: frdlcmipollinginterval
            
            	This is the number of seconds between successive status enquiry messages
            	**type**\:  int
            
            	**range:** 5..30
            
            	**units**\: seconds
            
            .. attribute:: frdlcmirowstatus
            
            	SNMP Version 2 Row Status Variable.  Writable objects in the table may be written in any RowStatus state
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: frdlcmistate
            
            	This variable states which Data Link Connection Management scheme is active (and by implication, what DLCI it uses) on the Frame Relay interface
            	**type**\:   :py:class:`Frdlcmistate <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frdlcmitable.Frdlcmientry.Frdlcmistate>`
            
            .. attribute:: frdlcmistatus
            
            	This indicates the status of the Frame Relay interface as determined by the performance of the dlcmi.  If no dlcmi is running, the Frame Relay interface will stay in the running state indefinitely
            	**type**\:   :py:class:`Frdlcmistatus <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frdlcmitable.Frdlcmientry.Frdlcmistatus>`
            
            

            """

            _prefix = 'FRAME-RELAY-DTE-MIB'
            _revision = '1997-05-01'

            def __init__(self):
                super(FrameRelayDteMib.Frdlcmitable.Frdlcmientry, self).__init__()

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

                self.frdlcmirowstatus = YLeaf(YType.enumeration, "frDlcmiRowStatus")

                self.frdlcmistate = YLeaf(YType.enumeration, "frDlcmiState")

                self.frdlcmistatus = YLeaf(YType.enumeration, "frDlcmiStatus")

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
                                "frdlcmirowstatus",
                                "frdlcmistate",
                                "frdlcmistatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(FrameRelayDteMib.Frdlcmitable.Frdlcmientry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(FrameRelayDteMib.Frdlcmitable.Frdlcmientry, self).__setattr__(name, value)

            class Frdlcmiaddress(Enum):
                """
                Frdlcmiaddress

                This variable states which address format is in use on

                the Frame Relay interface.

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

                This variable states the address length in octets.  In

                the case of Q922 format, the length indicates the

                entire length of the address including the control

                portion.

                .. data:: twoOctets = 2

                .. data:: threeOctets = 3

                .. data:: fourOctets = 4

                """

                twoOctets = Enum.YLeaf(2, "twoOctets")

                threeOctets = Enum.YLeaf(3, "threeOctets")

                fourOctets = Enum.YLeaf(4, "fourOctets")


            class Frdlcmimulticast(Enum):
                """
                Frdlcmimulticast

                This indicates whether the Frame Relay interface is

                using a multicast service.

                .. data:: nonBroadcast = 1

                .. data:: broadcast = 2

                """

                nonBroadcast = Enum.YLeaf(1, "nonBroadcast")

                broadcast = Enum.YLeaf(2, "broadcast")


            class Frdlcmistate(Enum):
                """
                Frdlcmistate

                This variable states which Data Link Connection

                Management scheme is active (and by implication, what

                DLCI it uses) on the Frame Relay interface.

                .. data:: noLmiConfigured = 1

                .. data:: lmiRev1 = 2

                .. data:: ansiT1617D = 3

                .. data:: ansiT1617B = 4

                .. data:: itut933A = 5

                .. data:: ansiT1617D1994 = 6

                """

                noLmiConfigured = Enum.YLeaf(1, "noLmiConfigured")

                lmiRev1 = Enum.YLeaf(2, "lmiRev1")

                ansiT1617D = Enum.YLeaf(3, "ansiT1617D")

                ansiT1617B = Enum.YLeaf(4, "ansiT1617B")

                itut933A = Enum.YLeaf(5, "itut933A")

                ansiT1617D1994 = Enum.YLeaf(6, "ansiT1617D1994")


            class Frdlcmistatus(Enum):
                """
                Frdlcmistatus

                This indicates the status of the Frame Relay interface

                as determined by the performance of the dlcmi.  If no

                dlcmi is running, the Frame Relay interface will stay

                in the running state indefinitely.

                .. data:: running = 1

                .. data:: fault = 2

                .. data:: initializing = 3

                """

                running = Enum.YLeaf(1, "running")

                fault = Enum.YLeaf(2, "fault")

                initializing = Enum.YLeaf(3, "initializing")


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
                    self.frdlcmirowstatus.is_set or
                    self.frdlcmistate.is_set or
                    self.frdlcmistatus.is_set)

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
                    self.frdlcmirowstatus.yfilter != YFilter.not_set or
                    self.frdlcmistate.yfilter != YFilter.not_set or
                    self.frdlcmistatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "frDlcmiEntry" + "[frDlcmiIfIndex='" + self.frdlcmiifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/frDlcmiTable/%s" % self.get_segment_path()
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
                if (self.frdlcmirowstatus.is_set or self.frdlcmirowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frdlcmirowstatus.get_name_leafdata())
                if (self.frdlcmistate.is_set or self.frdlcmistate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frdlcmistate.get_name_leafdata())
                if (self.frdlcmistatus.is_set or self.frdlcmistatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frdlcmistatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "frDlcmiIfIndex" or name == "frDlcmiAddress" or name == "frDlcmiAddressLen" or name == "frDlcmiErrorThreshold" or name == "frDlcmiFullEnquiryInterval" or name == "frDlcmiMaxSupportedVCs" or name == "frDlcmiMonitoredEvents" or name == "frDlcmiMulticast" or name == "frDlcmiPollingInterval" or name == "frDlcmiRowStatus" or name == "frDlcmiState" or name == "frDlcmiStatus"):
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
                if(value_path == "frDlcmiRowStatus"):
                    self.frdlcmirowstatus = value
                    self.frdlcmirowstatus.value_namespace = name_space
                    self.frdlcmirowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "frDlcmiState"):
                    self.frdlcmistate = value
                    self.frdlcmistate.value_namespace = name_space
                    self.frdlcmistate.value_namespace_prefix = name_space_prefix
                if(value_path == "frDlcmiStatus"):
                    self.frdlcmistatus = value
                    self.frdlcmistatus.value_namespace = name_space
                    self.frdlcmistatus.value_namespace_prefix = name_space_prefix

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
                path_buffer = "FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/%s" % self.get_segment_path()
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
                c = FrameRelayDteMib.Frdlcmitable.Frdlcmientry()
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
        Link Connections (DLC) or virtual circuits.
        
        .. attribute:: frcircuitentry
        
        	The information regarding a single Data Link Connection.  Discontinuities in the counters contained in this table are indicated by the value in frCircuitCreationTime
        	**type**\: list of    :py:class:`Frcircuitentry <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frcircuittable.Frcircuitentry>`
        
        

        """

        _prefix = 'FRAME-RELAY-DTE-MIB'
        _revision = '1997-05-01'

        def __init__(self):
            super(FrameRelayDteMib.Frcircuittable, self).__init__()

            self.yang_name = "frCircuitTable"
            self.yang_parent_name = "FRAME-RELAY-DTE-MIB"

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
                        super(FrameRelayDteMib.Frcircuittable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(FrameRelayDteMib.Frcircuittable, self).__setattr__(name, value)


        class Frcircuitentry(Entity):
            """
            The information regarding a single Data Link
            Connection.  Discontinuities in the counters contained
            in this table are indicated by the value in
            frCircuitCreationTime.
            
            .. attribute:: frcircuitifindex  <key>
            
            	The ifIndex Value of the ifEntry this virtual circuit is layered onto
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: frcircuitdlci  <key>
            
            	The Data Link Connection Identifier for this virtual circuit
            	**type**\:  int
            
            	**range:** 0..8388607
            
            .. attribute:: frcircuitcommittedburst
            
            	This variable indicates the maximum amount of data, in bits, that the network agrees to transfer under normal conditions, during the measurement interval
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: frcircuitcreationtime
            
            	The value of sysUpTime when the virtual circuit was created, whether by the Data Link Connection Management Interface or by a SetRequest
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitdiscards
            
            	The number of inbound frames dropped because of format errors, or because the VC is inactive
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitexcessburst
            
            	This variable indicates the maximum amount of uncommitted data bits that the network will attempt to deliver over the measurement interval.  By default, if not configured when creating the entry, the Excess Information Burst Size is set to the value of ifSpeed
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: frcircuitlasttimechange
            
            	The value of sysUpTime when last there was a change in the virtual circuit state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitlogicalifindex
            
            	Normally the same value as frDlcmiIfIndex, but different when an implementation associates a virtual ifEntry with a DLC or set of DLCs in order to associate higher layer objects such as the ipAddrEntry with a subset of the virtual circuits on a Frame Relay interface. The type of such ifEntries is defined by the higher layer object; for example, if PPP/Frame Relay is implemented, the ifType of this ifEntry would be PPP. If it is not so defined, as would be the case with an ipAddrEntry, it should be of type Other
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: frcircuitmulticast
            
            	This indicates whether this VC is used as a unicast VC (i.e. not multicast) or the type of multicast service subscribed to
            	**type**\:   :py:class:`Frcircuitmulticast <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frcircuittable.Frcircuitentry.Frcircuitmulticast>`
            
            .. attribute:: frcircuitreceivedbecns
            
            	Number of frames received from the network indicating backward congestion since the virtual circuit was created.  This occurs when the remote DTE sets the BECN flag, or when a switch in the network receives the frame from a trunk whose transmission queue is congested
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceiveddes
            
            	Number of frames received from the network indicating that they were eligible for discard since the virtual circuit was created.  This occurs when the remote DTE sets the DE flag, or when in remote DTE's switch detects that the frame was received as Excess Burst data
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedfecns
            
            	Number of frames received from the network indicating forward congestion since the virtual circuit was created.  This occurs when the remote DTE sets the FECN flag, or when a switch in the network enqueues the frame to a trunk whose transmission queue is congested
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedframes
            
            	Number of frames received over this virtual circuit since it was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedoctets
            
            	Number of octets received over this virtual circuit since it was created.  Octets counted include the full frame relay header, but do not include the flag characters or the CRC
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitrowstatus
            
            	This object is used to create a new row or modify or destroy an existing row in the manner described in the definition of the RowStatus textual convention. Writable objects in the table may be written in any RowStatus state
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: frcircuitsentdes
            
            	Number of frames sent to the network indicating that they were eligible for discard since the virtual circuit was created.   This occurs when the local DTE sets the DE flag, indicating that during Network congestion situations those frames should be discarded in preference of other frames sent without the DE bit set
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitsentframes
            
            	The number of frames sent from this virtual circuit since it was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitsentoctets
            
            	The number of octets sent from this virtual circuit since it was created.  Octets counted are the full frame relay header and the payload, but do not include the flag characters or CRC
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitstate
            
            	Indicates whether the particular virtual circuit is operational.  In the absence of a Data Link Connection Management Interface, virtual circuit entries (rows) may be created by setting virtual circuit state to 'active', or deleted by changing Circuit state to 'invalid'.  Whether or not the row actually disappears is left to the implementation, so this object may actually read as 'invalid' for some arbitrary length of time.  It is also legal to set the state of a virtual circuit to 'inactive' to temporarily disable a given circuit.  The use of 'invalid' is deprecated in this SNMP Version 2 MIB, in favor of frCircuitRowStatus
            	**type**\:   :py:class:`Frcircuitstate <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frcircuittable.Frcircuitentry.Frcircuitstate>`
            
            .. attribute:: frcircuitthroughput
            
            	Throughput is the average number of 'Frame Relay Information Field' bits transferred per second across a user network interface in one direction, measured over the measurement interval.  If the configured committed burst rate and throughput are both non\-zero, the measurement interval, T, is     T=frCircuitCommittedBurst/frCircuitThroughput.  If the configured committed burst rate and throughput are both zero, the measurement interval, T, is            T=frCircuitExcessBurst/ifSpeed
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: frcircuittype
            
            	Indication of whether the VC was manually created (static), or dynamically created (dynamic) via the data link control management interface
            	**type**\:   :py:class:`Frcircuittype <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frcircuittable.Frcircuitentry.Frcircuittype>`
            
            

            """

            _prefix = 'FRAME-RELAY-DTE-MIB'
            _revision = '1997-05-01'

            def __init__(self):
                super(FrameRelayDteMib.Frcircuittable.Frcircuitentry, self).__init__()

                self.yang_name = "frCircuitEntry"
                self.yang_parent_name = "frCircuitTable"

                self.frcircuitifindex = YLeaf(YType.int32, "frCircuitIfIndex")

                self.frcircuitdlci = YLeaf(YType.int32, "frCircuitDlci")

                self.frcircuitcommittedburst = YLeaf(YType.int32, "frCircuitCommittedBurst")

                self.frcircuitcreationtime = YLeaf(YType.uint32, "frCircuitCreationTime")

                self.frcircuitdiscards = YLeaf(YType.uint32, "frCircuitDiscards")

                self.frcircuitexcessburst = YLeaf(YType.int32, "frCircuitExcessBurst")

                self.frcircuitlasttimechange = YLeaf(YType.uint32, "frCircuitLastTimeChange")

                self.frcircuitlogicalifindex = YLeaf(YType.int32, "frCircuitLogicalIfIndex")

                self.frcircuitmulticast = YLeaf(YType.enumeration, "frCircuitMulticast")

                self.frcircuitreceivedbecns = YLeaf(YType.uint32, "frCircuitReceivedBECNs")

                self.frcircuitreceiveddes = YLeaf(YType.uint32, "frCircuitReceivedDEs")

                self.frcircuitreceivedfecns = YLeaf(YType.uint32, "frCircuitReceivedFECNs")

                self.frcircuitreceivedframes = YLeaf(YType.uint32, "frCircuitReceivedFrames")

                self.frcircuitreceivedoctets = YLeaf(YType.uint32, "frCircuitReceivedOctets")

                self.frcircuitrowstatus = YLeaf(YType.enumeration, "frCircuitRowStatus")

                self.frcircuitsentdes = YLeaf(YType.uint32, "frCircuitSentDEs")

                self.frcircuitsentframes = YLeaf(YType.uint32, "frCircuitSentFrames")

                self.frcircuitsentoctets = YLeaf(YType.uint32, "frCircuitSentOctets")

                self.frcircuitstate = YLeaf(YType.enumeration, "frCircuitState")

                self.frcircuitthroughput = YLeaf(YType.int32, "frCircuitThroughput")

                self.frcircuittype = YLeaf(YType.enumeration, "frCircuitType")

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
                                "frcircuitdiscards",
                                "frcircuitexcessburst",
                                "frcircuitlasttimechange",
                                "frcircuitlogicalifindex",
                                "frcircuitmulticast",
                                "frcircuitreceivedbecns",
                                "frcircuitreceiveddes",
                                "frcircuitreceivedfecns",
                                "frcircuitreceivedframes",
                                "frcircuitreceivedoctets",
                                "frcircuitrowstatus",
                                "frcircuitsentdes",
                                "frcircuitsentframes",
                                "frcircuitsentoctets",
                                "frcircuitstate",
                                "frcircuitthroughput",
                                "frcircuittype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(FrameRelayDteMib.Frcircuittable.Frcircuitentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(FrameRelayDteMib.Frcircuittable.Frcircuitentry, self).__setattr__(name, value)

            class Frcircuitmulticast(Enum):
                """
                Frcircuitmulticast

                This indicates whether this VC is used as a unicast VC

                (i.e. not multicast) or the type of multicast service

                subscribed to

                .. data:: unicast = 1

                .. data:: oneWay = 2

                .. data:: twoWay = 3

                .. data:: nWay = 4

                """

                unicast = Enum.YLeaf(1, "unicast")

                oneWay = Enum.YLeaf(2, "oneWay")

                twoWay = Enum.YLeaf(3, "twoWay")

                nWay = Enum.YLeaf(4, "nWay")


            class Frcircuitstate(Enum):
                """
                Frcircuitstate

                Indicates whether the particular virtual circuit is

                operational.  In the absence of a Data Link Connection

                Management Interface, virtual circuit entries (rows)

                may be created by setting virtual circuit state to

                'active', or deleted by changing Circuit state to

                'invalid'.

                Whether or not the row actually disappears is left to

                the implementation, so this object may actually read as

                'invalid' for some arbitrary length of time.  It is

                also legal to set the state of a virtual circuit to

                'inactive' to temporarily disable a given circuit.

                The use of 'invalid' is deprecated in this SNMP Version

                2 MIB, in favor of frCircuitRowStatus.

                .. data:: invalid = 1

                .. data:: active = 2

                .. data:: inactive = 3

                """

                invalid = Enum.YLeaf(1, "invalid")

                active = Enum.YLeaf(2, "active")

                inactive = Enum.YLeaf(3, "inactive")


            class Frcircuittype(Enum):
                """
                Frcircuittype

                Indication of whether the VC was manually created

                (static), or dynamically created (dynamic) via the data

                link control management interface.

                .. data:: static = 1

                .. data:: dynamic = 2

                """

                static = Enum.YLeaf(1, "static")

                dynamic = Enum.YLeaf(2, "dynamic")


            def has_data(self):
                return (
                    self.frcircuitifindex.is_set or
                    self.frcircuitdlci.is_set or
                    self.frcircuitcommittedburst.is_set or
                    self.frcircuitcreationtime.is_set or
                    self.frcircuitdiscards.is_set or
                    self.frcircuitexcessburst.is_set or
                    self.frcircuitlasttimechange.is_set or
                    self.frcircuitlogicalifindex.is_set or
                    self.frcircuitmulticast.is_set or
                    self.frcircuitreceivedbecns.is_set or
                    self.frcircuitreceiveddes.is_set or
                    self.frcircuitreceivedfecns.is_set or
                    self.frcircuitreceivedframes.is_set or
                    self.frcircuitreceivedoctets.is_set or
                    self.frcircuitrowstatus.is_set or
                    self.frcircuitsentdes.is_set or
                    self.frcircuitsentframes.is_set or
                    self.frcircuitsentoctets.is_set or
                    self.frcircuitstate.is_set or
                    self.frcircuitthroughput.is_set or
                    self.frcircuittype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.frcircuitifindex.yfilter != YFilter.not_set or
                    self.frcircuitdlci.yfilter != YFilter.not_set or
                    self.frcircuitcommittedburst.yfilter != YFilter.not_set or
                    self.frcircuitcreationtime.yfilter != YFilter.not_set or
                    self.frcircuitdiscards.yfilter != YFilter.not_set or
                    self.frcircuitexcessburst.yfilter != YFilter.not_set or
                    self.frcircuitlasttimechange.yfilter != YFilter.not_set or
                    self.frcircuitlogicalifindex.yfilter != YFilter.not_set or
                    self.frcircuitmulticast.yfilter != YFilter.not_set or
                    self.frcircuitreceivedbecns.yfilter != YFilter.not_set or
                    self.frcircuitreceiveddes.yfilter != YFilter.not_set or
                    self.frcircuitreceivedfecns.yfilter != YFilter.not_set or
                    self.frcircuitreceivedframes.yfilter != YFilter.not_set or
                    self.frcircuitreceivedoctets.yfilter != YFilter.not_set or
                    self.frcircuitrowstatus.yfilter != YFilter.not_set or
                    self.frcircuitsentdes.yfilter != YFilter.not_set or
                    self.frcircuitsentframes.yfilter != YFilter.not_set or
                    self.frcircuitsentoctets.yfilter != YFilter.not_set or
                    self.frcircuitstate.yfilter != YFilter.not_set or
                    self.frcircuitthroughput.yfilter != YFilter.not_set or
                    self.frcircuittype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "frCircuitEntry" + "[frCircuitIfIndex='" + self.frcircuitifindex.get() + "']" + "[frCircuitDlci='" + self.frcircuitdlci.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/frCircuitTable/%s" % self.get_segment_path()
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
                if (self.frcircuitdiscards.is_set or self.frcircuitdiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitdiscards.get_name_leafdata())
                if (self.frcircuitexcessburst.is_set or self.frcircuitexcessburst.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitexcessburst.get_name_leafdata())
                if (self.frcircuitlasttimechange.is_set or self.frcircuitlasttimechange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitlasttimechange.get_name_leafdata())
                if (self.frcircuitlogicalifindex.is_set or self.frcircuitlogicalifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitlogicalifindex.get_name_leafdata())
                if (self.frcircuitmulticast.is_set or self.frcircuitmulticast.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitmulticast.get_name_leafdata())
                if (self.frcircuitreceivedbecns.is_set or self.frcircuitreceivedbecns.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitreceivedbecns.get_name_leafdata())
                if (self.frcircuitreceiveddes.is_set or self.frcircuitreceiveddes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitreceiveddes.get_name_leafdata())
                if (self.frcircuitreceivedfecns.is_set or self.frcircuitreceivedfecns.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitreceivedfecns.get_name_leafdata())
                if (self.frcircuitreceivedframes.is_set or self.frcircuitreceivedframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitreceivedframes.get_name_leafdata())
                if (self.frcircuitreceivedoctets.is_set or self.frcircuitreceivedoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitreceivedoctets.get_name_leafdata())
                if (self.frcircuitrowstatus.is_set or self.frcircuitrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitrowstatus.get_name_leafdata())
                if (self.frcircuitsentdes.is_set or self.frcircuitsentdes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitsentdes.get_name_leafdata())
                if (self.frcircuitsentframes.is_set or self.frcircuitsentframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitsentframes.get_name_leafdata())
                if (self.frcircuitsentoctets.is_set or self.frcircuitsentoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitsentoctets.get_name_leafdata())
                if (self.frcircuitstate.is_set or self.frcircuitstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitstate.get_name_leafdata())
                if (self.frcircuitthroughput.is_set or self.frcircuitthroughput.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuitthroughput.get_name_leafdata())
                if (self.frcircuittype.is_set or self.frcircuittype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frcircuittype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "frCircuitIfIndex" or name == "frCircuitDlci" or name == "frCircuitCommittedBurst" or name == "frCircuitCreationTime" or name == "frCircuitDiscards" or name == "frCircuitExcessBurst" or name == "frCircuitLastTimeChange" or name == "frCircuitLogicalIfIndex" or name == "frCircuitMulticast" or name == "frCircuitReceivedBECNs" or name == "frCircuitReceivedDEs" or name == "frCircuitReceivedFECNs" or name == "frCircuitReceivedFrames" or name == "frCircuitReceivedOctets" or name == "frCircuitRowStatus" or name == "frCircuitSentDEs" or name == "frCircuitSentFrames" or name == "frCircuitSentOctets" or name == "frCircuitState" or name == "frCircuitThroughput" or name == "frCircuitType"):
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
                if(value_path == "frCircuitDiscards"):
                    self.frcircuitdiscards = value
                    self.frcircuitdiscards.value_namespace = name_space
                    self.frcircuitdiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitExcessBurst"):
                    self.frcircuitexcessburst = value
                    self.frcircuitexcessburst.value_namespace = name_space
                    self.frcircuitexcessburst.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitLastTimeChange"):
                    self.frcircuitlasttimechange = value
                    self.frcircuitlasttimechange.value_namespace = name_space
                    self.frcircuitlasttimechange.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitLogicalIfIndex"):
                    self.frcircuitlogicalifindex = value
                    self.frcircuitlogicalifindex.value_namespace = name_space
                    self.frcircuitlogicalifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitMulticast"):
                    self.frcircuitmulticast = value
                    self.frcircuitmulticast.value_namespace = name_space
                    self.frcircuitmulticast.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitReceivedBECNs"):
                    self.frcircuitreceivedbecns = value
                    self.frcircuitreceivedbecns.value_namespace = name_space
                    self.frcircuitreceivedbecns.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitReceivedDEs"):
                    self.frcircuitreceiveddes = value
                    self.frcircuitreceiveddes.value_namespace = name_space
                    self.frcircuitreceiveddes.value_namespace_prefix = name_space_prefix
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
                if(value_path == "frCircuitRowStatus"):
                    self.frcircuitrowstatus = value
                    self.frcircuitrowstatus.value_namespace = name_space
                    self.frcircuitrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "frCircuitSentDEs"):
                    self.frcircuitsentdes = value
                    self.frcircuitsentdes.value_namespace = name_space
                    self.frcircuitsentdes.value_namespace_prefix = name_space_prefix
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
                if(value_path == "frCircuitType"):
                    self.frcircuittype = value
                    self.frcircuittype.value_namespace = name_space
                    self.frcircuittype.value_namespace_prefix = name_space_prefix

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
                path_buffer = "FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/%s" % self.get_segment_path()
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
                c = FrameRelayDteMib.Frcircuittable.Frcircuitentry()
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
        Frame Relay interface.  Discontinuities in the counters
        contained in this table are the same as apply to the
        ifEntry associated with the Interface.
        
        .. attribute:: frerrentry
        
        	The error information for a single frame relay interface
        	**type**\: list of    :py:class:`Frerrentry <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frerrtable.Frerrentry>`
        
        

        """

        _prefix = 'FRAME-RELAY-DTE-MIB'
        _revision = '1997-05-01'

        def __init__(self):
            super(FrameRelayDteMib.Frerrtable, self).__init__()

            self.yang_name = "frErrTable"
            self.yang_parent_name = "FRAME-RELAY-DTE-MIB"

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
                        super(FrameRelayDteMib.Frerrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(FrameRelayDteMib.Frerrtable, self).__setattr__(name, value)


        class Frerrentry(Entity):
            """
            The error information for a single frame relay
            interface.
            
            .. attribute:: frerrifindex  <key>
            
            	The ifIndex Value of the corresponding ifEntry
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: frerrdata
            
            	An octet string containing as much of the error packet as possible.  As a minimum, it must contain the Q.922 Address or as much as was delivered.  It is desirable to include all header and demultiplexing information
            	**type**\:  str
            
            	**length:** 1..1600
            
            .. attribute:: frerrfaults
            
            	The number of times the interface has gone down since it was initialized
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frerrfaulttime
            
            	The value of sysUpTime at the time when the interface was taken down due to excessive errors.  Excessive errors is defined as the time when a DLCMI exceeds the frDlcmiErrorThreshold number of errors within frDlcmiMonitoredEvents. See FrDlcmiEntry for further details
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frerrtime
            
            	The value of sysUpTime at which the error was detected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frerrtype
            
            	The type of error that was last seen  on  this interface\:  receiveShort\: frame was not long enough to allow         demultiplexing \- the address field was incomplete,         or for virtual circuits using Multiprotocol over         Frame Relay, the protocol identifier was missing         or incomplete.  receiveLong\: frame exceeded maximum length configured for this              interface.  illegalAddress\: address field did not match configured format.  unknownAddress\: frame received on a virtual circuit which was not                 active or administratively disabled.  dlcmiProtoErr\: unspecified error occurred when attempting to                interpret link maintenance frame.  dlcmiUnknownIE\: link maintenance frame contained an Information                 Element type which is not valid for the                 configured link maintenance protocol.  dlcmiSequenceErr\: link maintenance frame contained a sequence                   number other than the expected value.  dlcmiUnknownRpt\: link maintenance frame contained a Report Type                  Information Element whose value was not valid                  for the configured link maintenance protocol.  noErrorSinceReset\: no errors have been detected since the last                    cold start or warm start
            	**type**\:   :py:class:`Frerrtype <ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB.FrameRelayDteMib.Frerrtable.Frerrentry.Frerrtype>`
            
            

            """

            _prefix = 'FRAME-RELAY-DTE-MIB'
            _revision = '1997-05-01'

            def __init__(self):
                super(FrameRelayDteMib.Frerrtable.Frerrentry, self).__init__()

                self.yang_name = "frErrEntry"
                self.yang_parent_name = "frErrTable"

                self.frerrifindex = YLeaf(YType.int32, "frErrIfIndex")

                self.frerrdata = YLeaf(YType.str, "frErrData")

                self.frerrfaults = YLeaf(YType.uint32, "frErrFaults")

                self.frerrfaulttime = YLeaf(YType.uint32, "frErrFaultTime")

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
                                "frerrfaults",
                                "frerrfaulttime",
                                "frerrtime",
                                "frerrtype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(FrameRelayDteMib.Frerrtable.Frerrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(FrameRelayDteMib.Frerrtable.Frerrentry, self).__setattr__(name, value)

            class Frerrtype(Enum):
                """
                Frerrtype

                The type of error that was last seen  on  this interface\:

                receiveShort\: frame was not long enough to allow

                        demultiplexing \- the address field was incomplete,

                        or for virtual circuits using Multiprotocol over

                        Frame Relay, the protocol identifier was missing

                        or incomplete.

                receiveLong\: frame exceeded maximum length configured for this

                             interface.

                illegalAddress\: address field did not match configured format.

                unknownAddress\: frame received on a virtual circuit which was not

                                active or administratively disabled.

                dlcmiProtoErr\: unspecified error occurred when attempting to

                               interpret link maintenance frame.

                dlcmiUnknownIE\: link maintenance frame contained an Information

                                Element type which is not valid for the

                                configured link maintenance protocol.

                dlcmiSequenceErr\: link maintenance frame contained a sequence

                                  number other than the expected value.

                dlcmiUnknownRpt\: link maintenance frame contained a Report Type

                                 Information Element whose value was not valid

                                 for the configured link maintenance protocol.

                noErrorSinceReset\: no errors have been detected since the last

                                   cold start or warm start.

                .. data:: unknownError = 1

                .. data:: receiveShort = 2

                .. data:: receiveLong = 3

                .. data:: illegalAddress = 4

                .. data:: unknownAddress = 5

                .. data:: dlcmiProtoErr = 6

                .. data:: dlcmiUnknownIE = 7

                .. data:: dlcmiSequenceErr = 8

                .. data:: dlcmiUnknownRpt = 9

                .. data:: noErrorSinceReset = 10

                """

                unknownError = Enum.YLeaf(1, "unknownError")

                receiveShort = Enum.YLeaf(2, "receiveShort")

                receiveLong = Enum.YLeaf(3, "receiveLong")

                illegalAddress = Enum.YLeaf(4, "illegalAddress")

                unknownAddress = Enum.YLeaf(5, "unknownAddress")

                dlcmiProtoErr = Enum.YLeaf(6, "dlcmiProtoErr")

                dlcmiUnknownIE = Enum.YLeaf(7, "dlcmiUnknownIE")

                dlcmiSequenceErr = Enum.YLeaf(8, "dlcmiSequenceErr")

                dlcmiUnknownRpt = Enum.YLeaf(9, "dlcmiUnknownRpt")

                noErrorSinceReset = Enum.YLeaf(10, "noErrorSinceReset")


            def has_data(self):
                return (
                    self.frerrifindex.is_set or
                    self.frerrdata.is_set or
                    self.frerrfaults.is_set or
                    self.frerrfaulttime.is_set or
                    self.frerrtime.is_set or
                    self.frerrtype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.frerrifindex.yfilter != YFilter.not_set or
                    self.frerrdata.yfilter != YFilter.not_set or
                    self.frerrfaults.yfilter != YFilter.not_set or
                    self.frerrfaulttime.yfilter != YFilter.not_set or
                    self.frerrtime.yfilter != YFilter.not_set or
                    self.frerrtype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "frErrEntry" + "[frErrIfIndex='" + self.frerrifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/frErrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.frerrifindex.is_set or self.frerrifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frerrifindex.get_name_leafdata())
                if (self.frerrdata.is_set or self.frerrdata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frerrdata.get_name_leafdata())
                if (self.frerrfaults.is_set or self.frerrfaults.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frerrfaults.get_name_leafdata())
                if (self.frerrfaulttime.is_set or self.frerrfaulttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frerrfaulttime.get_name_leafdata())
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
                if(name == "frErrIfIndex" or name == "frErrData" or name == "frErrFaults" or name == "frErrFaultTime" or name == "frErrTime" or name == "frErrType"):
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
                if(value_path == "frErrFaults"):
                    self.frerrfaults = value
                    self.frerrfaults.value_namespace = name_space
                    self.frerrfaults.value_namespace_prefix = name_space_prefix
                if(value_path == "frErrFaultTime"):
                    self.frerrfaulttime = value
                    self.frerrfaulttime.value_namespace = name_space
                    self.frerrfaulttime.value_namespace_prefix = name_space_prefix
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
                path_buffer = "FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB/%s" % self.get_segment_path()
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
                c = FrameRelayDteMib.Frerrtable.Frerrentry()
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
            (self.framerelaytrapcontrol is not None and self.framerelaytrapcontrol.has_data()) or
            (self.frcircuittable is not None and self.frcircuittable.has_data()) or
            (self.frdlcmitable is not None and self.frdlcmitable.has_data()) or
            (self.frerrtable is not None and self.frerrtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.framerelaytrapcontrol is not None and self.framerelaytrapcontrol.has_operation()) or
            (self.frcircuittable is not None and self.frcircuittable.has_operation()) or
            (self.frdlcmitable is not None and self.frdlcmitable.has_operation()) or
            (self.frerrtable is not None and self.frerrtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "FRAME-RELAY-DTE-MIB:FRAME-RELAY-DTE-MIB" + path_buffer

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

        if (child_yang_name == "frameRelayTrapControl"):
            if (self.framerelaytrapcontrol is None):
                self.framerelaytrapcontrol = FrameRelayDteMib.Framerelaytrapcontrol()
                self.framerelaytrapcontrol.parent = self
                self._children_name_map["framerelaytrapcontrol"] = "frameRelayTrapControl"
            return self.framerelaytrapcontrol

        if (child_yang_name == "frCircuitTable"):
            if (self.frcircuittable is None):
                self.frcircuittable = FrameRelayDteMib.Frcircuittable()
                self.frcircuittable.parent = self
                self._children_name_map["frcircuittable"] = "frCircuitTable"
            return self.frcircuittable

        if (child_yang_name == "frDlcmiTable"):
            if (self.frdlcmitable is None):
                self.frdlcmitable = FrameRelayDteMib.Frdlcmitable()
                self.frdlcmitable.parent = self
                self._children_name_map["frdlcmitable"] = "frDlcmiTable"
            return self.frdlcmitable

        if (child_yang_name == "frErrTable"):
            if (self.frerrtable is None):
                self.frerrtable = FrameRelayDteMib.Frerrtable()
                self.frerrtable.parent = self
                self._children_name_map["frerrtable"] = "frErrTable"
            return self.frerrtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "frameRelayTrapControl" or name == "frCircuitTable" or name == "frDlcmiTable" or name == "frErrTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = FrameRelayDteMib()
        return self._top_entity

