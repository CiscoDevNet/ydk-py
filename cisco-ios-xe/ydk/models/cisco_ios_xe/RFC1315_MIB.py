""" RFC1315_MIB 


"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class RFC1315MIB(Entity):
    """
    
    
    .. attribute:: frame_relay_globals
    
    	
    	**type**\:  :py:class:`FrameRelayGlobals <ydk.models.cisco_ios_xe.RFC1315_MIB.RFC1315MIB.FrameRelayGlobals>`
    
    .. attribute:: frdlcmitable
    
    	The Parameters for the Data Link Connection Management Interface for the frame relay service on this interface
    	**type**\:  :py:class:`Frdlcmitable <ydk.models.cisco_ios_xe.RFC1315_MIB.RFC1315MIB.Frdlcmitable>`
    
    .. attribute:: frcircuittable
    
    	A table containing information about specific Data Link Connection Identifiers and corresponding virtual circuits
    	**type**\:  :py:class:`Frcircuittable <ydk.models.cisco_ios_xe.RFC1315_MIB.RFC1315MIB.Frcircuittable>`
    
    .. attribute:: frerrtable
    
    	A table containing information about Errors on the Frame Relay interface
    	**type**\:  :py:class:`Frerrtable <ydk.models.cisco_ios_xe.RFC1315_MIB.RFC1315MIB.Frerrtable>`
    
    

    """

    _prefix = 'RFC1315-MIB'

    def __init__(self):
        super(RFC1315MIB, self).__init__()
        self._top_entity = None

        self.yang_name = "RFC1315-MIB"
        self.yang_parent_name = "RFC1315-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("frame-relay-globals", ("frame_relay_globals", RFC1315MIB.FrameRelayGlobals)), ("frDlcmiTable", ("frdlcmitable", RFC1315MIB.Frdlcmitable)), ("frCircuitTable", ("frcircuittable", RFC1315MIB.Frcircuittable)), ("frErrTable", ("frerrtable", RFC1315MIB.Frerrtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.frame_relay_globals = RFC1315MIB.FrameRelayGlobals()
        self.frame_relay_globals.parent = self
        self._children_name_map["frame_relay_globals"] = "frame-relay-globals"
        self._children_yang_names.add("frame-relay-globals")

        self.frdlcmitable = RFC1315MIB.Frdlcmitable()
        self.frdlcmitable.parent = self
        self._children_name_map["frdlcmitable"] = "frDlcmiTable"
        self._children_yang_names.add("frDlcmiTable")

        self.frcircuittable = RFC1315MIB.Frcircuittable()
        self.frcircuittable.parent = self
        self._children_name_map["frcircuittable"] = "frCircuitTable"
        self._children_yang_names.add("frCircuitTable")

        self.frerrtable = RFC1315MIB.Frerrtable()
        self.frerrtable.parent = self
        self._children_name_map["frerrtable"] = "frErrTable"
        self._children_yang_names.add("frErrTable")
        self._segment_path = lambda: "RFC1315-MIB:RFC1315-MIB"


    class FrameRelayGlobals(Entity):
        """
        
        
        .. attribute:: frtrapstate
        
        	This variable  indicates  whether  the  system produces the frDLCIStatusChange trap
        	**type**\:  :py:class:`Frtrapstate <ydk.models.cisco_ios_xe.RFC1315_MIB.RFC1315MIB.FrameRelayGlobals.Frtrapstate>`
        
        

        """

        _prefix = 'RFC1315-MIB'

        def __init__(self):
            super(RFC1315MIB.FrameRelayGlobals, self).__init__()

            self.yang_name = "frame-relay-globals"
            self.yang_parent_name = "RFC1315-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('frtrapstate', YLeaf(YType.enumeration, 'frTrapState')),
            ])
            self.frtrapstate = None
            self._segment_path = lambda: "frame-relay-globals"
            self._absolute_path = lambda: "RFC1315-MIB:RFC1315-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1315MIB.FrameRelayGlobals, ['frtrapstate'], name, value)

        class Frtrapstate(Enum):
            """
            Frtrapstate (Enum Class)

            This variable  indicates  whether  the  system

            produces the frDLCIStatusChange trap.

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = Enum.YLeaf(1, "enabled")

            disabled = Enum.YLeaf(2, "disabled")



    class Frdlcmitable(Entity):
        """
        The Parameters for the Data Link Connection Management
        Interface for the frame relay service on this
        interface.
        
        .. attribute:: frdlcmientry
        
        	The Parameters for a particular Data Link Con\- nection Management Interface
        	**type**\: list of  		 :py:class:`Frdlcmientry <ydk.models.cisco_ios_xe.RFC1315_MIB.RFC1315MIB.Frdlcmitable.Frdlcmientry>`
        
        

        """

        _prefix = 'RFC1315-MIB'

        def __init__(self):
            super(RFC1315MIB.Frdlcmitable, self).__init__()

            self.yang_name = "frDlcmiTable"
            self.yang_parent_name = "RFC1315-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("frDlcmiEntry", ("frdlcmientry", RFC1315MIB.Frdlcmitable.Frdlcmientry))])
            self._leafs = OrderedDict()

            self.frdlcmientry = YList(self)
            self._segment_path = lambda: "frDlcmiTable"
            self._absolute_path = lambda: "RFC1315-MIB:RFC1315-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1315MIB.Frdlcmitable, [], name, value)


        class Frdlcmientry(Entity):
            """
            The Parameters for a particular Data Link Con\-
            nection Management Interface.
            
            .. attribute:: frdlcmiifindex  (key)
            
            	The ifIndex value of the  corresponding  ifEn\- try
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frdlcmistate
            
            	This variable states which Data  Link  Connec\- tion Management scheme is active (and by impli\- cation, what DLCI it uses) on the  Frame  Relay interface
            	**type**\:  :py:class:`Frdlcmistate <ydk.models.cisco_ios_xe.RFC1315_MIB.RFC1315MIB.Frdlcmitable.Frdlcmientry.Frdlcmistate>`
            
            .. attribute:: frdlcmiaddress
            
            	This variable states which address  format  is in use on the Frame Relay interface
            	**type**\:  :py:class:`Frdlcmiaddress <ydk.models.cisco_ios_xe.RFC1315_MIB.RFC1315MIB.Frdlcmitable.Frdlcmientry.Frdlcmiaddress>`
            
            .. attribute:: frdlcmiaddresslen
            
            	This variable states which address  length  in octets.  In the case of Q922 format, the length indicates the entire length of the address  in\- cluding the control portion
            	**type**\:  :py:class:`Frdlcmiaddresslen <ydk.models.cisco_ios_xe.RFC1315_MIB.RFC1315MIB.Frdlcmitable.Frdlcmientry.Frdlcmiaddresslen>`
            
            .. attribute:: frdlcmipollinginterval
            
            	This is the number of seconds between  succes\- sive status enquiry messages
            	**type**\: int
            
            	**range:** 5..30
            
            .. attribute:: frdlcmifullenquiryinterval
            
            	Number of status enquiry intervals  that  pass before  issuance  of a full status enquiry mes\- sage
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: frdlcmierrorthreshold
            
            	This  is  the  maximum  number  of  unanswered Status Enquiries the equipment shall accept be\- fore declaring the interface down
            	**type**\: int
            
            	**range:** 1..10
            
            .. attribute:: frdlcmimonitoredevents
            
            	This is the number of status polling intervals over which the error threshold is counted.  For example, if within 'MonitoredEvents' number  of events  the  station  receives 'ErrorThreshold' number of errors, the interface  is  marked  as down
            	**type**\: int
            
            	**range:** 1..10
            
            .. attribute:: frdlcmimaxsupportedvcs
            
            	The maximum number of Virtual Circuits allowed for  this  interface.   Usually dictated by the Frame Relay network.  In response to a SET, if a value less than zero or  higher  than the agent's maximal capability is configured, the agent  should  respond  bad\- Value
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frdlcmimulticast
            
            	This indicates whether the Frame Relay  inter\- face is using a multicast service
            	**type**\:  :py:class:`Frdlcmimulticast <ydk.models.cisco_ios_xe.RFC1315_MIB.RFC1315MIB.Frdlcmitable.Frdlcmientry.Frdlcmimulticast>`
            
            

            """

            _prefix = 'RFC1315-MIB'

            def __init__(self):
                super(RFC1315MIB.Frdlcmitable.Frdlcmientry, self).__init__()

                self.yang_name = "frDlcmiEntry"
                self.yang_parent_name = "frDlcmiTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['frdlcmiifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('frdlcmiifindex', YLeaf(YType.int32, 'frDlcmiIfIndex')),
                    ('frdlcmistate', YLeaf(YType.enumeration, 'frDlcmiState')),
                    ('frdlcmiaddress', YLeaf(YType.enumeration, 'frDlcmiAddress')),
                    ('frdlcmiaddresslen', YLeaf(YType.enumeration, 'frDlcmiAddressLen')),
                    ('frdlcmipollinginterval', YLeaf(YType.int32, 'frDlcmiPollingInterval')),
                    ('frdlcmifullenquiryinterval', YLeaf(YType.int32, 'frDlcmiFullEnquiryInterval')),
                    ('frdlcmierrorthreshold', YLeaf(YType.int32, 'frDlcmiErrorThreshold')),
                    ('frdlcmimonitoredevents', YLeaf(YType.int32, 'frDlcmiMonitoredEvents')),
                    ('frdlcmimaxsupportedvcs', YLeaf(YType.int32, 'frDlcmiMaxSupportedVCs')),
                    ('frdlcmimulticast', YLeaf(YType.enumeration, 'frDlcmiMulticast')),
                ])
                self.frdlcmiifindex = None
                self.frdlcmistate = None
                self.frdlcmiaddress = None
                self.frdlcmiaddresslen = None
                self.frdlcmipollinginterval = None
                self.frdlcmifullenquiryinterval = None
                self.frdlcmierrorthreshold = None
                self.frdlcmimonitoredevents = None
                self.frdlcmimaxsupportedvcs = None
                self.frdlcmimulticast = None
                self._segment_path = lambda: "frDlcmiEntry" + "[frDlcmiIfIndex='" + str(self.frdlcmiifindex) + "']"
                self._absolute_path = lambda: "RFC1315-MIB:RFC1315-MIB/frDlcmiTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RFC1315MIB.Frdlcmitable.Frdlcmientry, ['frdlcmiifindex', 'frdlcmistate', 'frdlcmiaddress', 'frdlcmiaddresslen', 'frdlcmipollinginterval', 'frdlcmifullenquiryinterval', 'frdlcmierrorthreshold', 'frdlcmimonitoredevents', 'frdlcmimaxsupportedvcs', 'frdlcmimulticast'], name, value)

            class Frdlcmiaddress(Enum):
                """
                Frdlcmiaddress (Enum Class)

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
                Frdlcmiaddresslen (Enum Class)

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
                Frdlcmimulticast (Enum Class)

                This indicates whether the Frame Relay  inter\-

                face is using a multicast service.

                .. data:: nonBroadcast = 1

                .. data:: broadcast = 2

                """

                nonBroadcast = Enum.YLeaf(1, "nonBroadcast")

                broadcast = Enum.YLeaf(2, "broadcast")


            class Frdlcmistate(Enum):
                """
                Frdlcmistate (Enum Class)

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



    class Frcircuittable(Entity):
        """
        A table containing information about specific Data
        Link Connection Identifiers and corresponding virtual
        circuits.
        
        .. attribute:: frcircuitentry
        
        	The information regarding a single  Data  Link Connection Identifier
        	**type**\: list of  		 :py:class:`Frcircuitentry <ydk.models.cisco_ios_xe.RFC1315_MIB.RFC1315MIB.Frcircuittable.Frcircuitentry>`
        
        

        """

        _prefix = 'RFC1315-MIB'

        def __init__(self):
            super(RFC1315MIB.Frcircuittable, self).__init__()

            self.yang_name = "frCircuitTable"
            self.yang_parent_name = "RFC1315-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("frCircuitEntry", ("frcircuitentry", RFC1315MIB.Frcircuittable.Frcircuitentry))])
            self._leafs = OrderedDict()

            self.frcircuitentry = YList(self)
            self._segment_path = lambda: "frCircuitTable"
            self._absolute_path = lambda: "RFC1315-MIB:RFC1315-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1315MIB.Frcircuittable, [], name, value)


        class Frcircuitentry(Entity):
            """
            The information regarding a single  Data  Link
            Connection Identifier.
            
            .. attribute:: frcircuitifindex  (key)
            
            	The ifIndex Value of the ifEntry this  virtual circuit is layered onto
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitdlci  (key)
            
            	The Data Link Connection Identifier  for  this virtual circuit
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitstate
            
            	Indicates whether the particular virtual  cir\- cuit  is operational.  In the absence of a Data Link Connection Management  Interface,  virtual circuit  entries  (rows) may be created by set\- ting virtual  circuit  state  to  'active',  or deleted by changing Circuit state to 'invalid'. Whether or not the row actually  disappears  is left  to the implementation, so this object may actually read as 'invalid' for  some  arbitrary length  of  time.   It is also legal to set the state of a virtual  circuit  to  'inactive'  to temporarily disable a given circuit
            	**type**\:  :py:class:`Frcircuitstate <ydk.models.cisco_ios_xe.RFC1315_MIB.RFC1315MIB.Frcircuittable.Frcircuitentry.Frcircuitstate>`
            
            .. attribute:: frcircuitreceivedfecns
            
            	Number of frames received from the network in\- dicating  forward  congestion since the virtual circuit was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedbecns
            
            	Number of frames received from the network in\- dicating  backward congestion since the virtual circuit was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitsentframes
            
            	The number of frames sent  from  this  virtual circuit since it was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitsentoctets
            
            	The number of octets sent  from  this  virtual circuit since it was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedframes
            
            	Number of frames received  over  this  virtual circuit since it was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitreceivedoctets
            
            	Number of octets received  over  this  virtual circuit since it was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitcreationtime
            
            	The value of sysUpTime when the  virtual  cir\- cuit was created, whether by the Data Link Con\- nection Management Interface  or  by  a  SetRe\- quest
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitlasttimechange
            
            	The value of sysUpTime when last there  was  a change in the virtual circuit state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: frcircuitcommittedburst
            
            	This variable indicates the maximum amount  of data,  in  bits,  that  the  network  agrees to transfer under normal  conditions,  during  the measurement interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitexcessburst
            
            	This variable indicates the maximum amount  of uncommitted data bits that the network will at\- tempt to deliver over the measurement interval.  By default, if not configured when creating the entry, the Excess Information Burst Size is set to the value of ifSpeed
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frcircuitthroughput
            
            	Throughput is the average number of 'Frame Re\- lay  Information  Field'  bits  transferred per second across a user network interface  in  one direction, measured over the measurement inter\- val.  If the  configured  committed  burst  rate  and throughput  are  both non\-zero, the measurement interval T=frCircuitCommittedBurst/frCircuitThroughput.  If the  configured  committed  burst  rate  and throughput  are  both zero, the measurement in\- terval        T=frCircuitExcessBurst/ifSpeed
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'RFC1315-MIB'

            def __init__(self):
                super(RFC1315MIB.Frcircuittable.Frcircuitentry, self).__init__()

                self.yang_name = "frCircuitEntry"
                self.yang_parent_name = "frCircuitTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['frcircuitifindex','frcircuitdlci']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('frcircuitifindex', YLeaf(YType.int32, 'frCircuitIfIndex')),
                    ('frcircuitdlci', YLeaf(YType.int32, 'frCircuitDlci')),
                    ('frcircuitstate', YLeaf(YType.enumeration, 'frCircuitState')),
                    ('frcircuitreceivedfecns', YLeaf(YType.uint32, 'frCircuitReceivedFECNs')),
                    ('frcircuitreceivedbecns', YLeaf(YType.uint32, 'frCircuitReceivedBECNs')),
                    ('frcircuitsentframes', YLeaf(YType.uint32, 'frCircuitSentFrames')),
                    ('frcircuitsentoctets', YLeaf(YType.uint32, 'frCircuitSentOctets')),
                    ('frcircuitreceivedframes', YLeaf(YType.uint32, 'frCircuitReceivedFrames')),
                    ('frcircuitreceivedoctets', YLeaf(YType.uint32, 'frCircuitReceivedOctets')),
                    ('frcircuitcreationtime', YLeaf(YType.uint32, 'frCircuitCreationTime')),
                    ('frcircuitlasttimechange', YLeaf(YType.uint32, 'frCircuitLastTimeChange')),
                    ('frcircuitcommittedburst', YLeaf(YType.int32, 'frCircuitCommittedBurst')),
                    ('frcircuitexcessburst', YLeaf(YType.int32, 'frCircuitExcessBurst')),
                    ('frcircuitthroughput', YLeaf(YType.int32, 'frCircuitThroughput')),
                ])
                self.frcircuitifindex = None
                self.frcircuitdlci = None
                self.frcircuitstate = None
                self.frcircuitreceivedfecns = None
                self.frcircuitreceivedbecns = None
                self.frcircuitsentframes = None
                self.frcircuitsentoctets = None
                self.frcircuitreceivedframes = None
                self.frcircuitreceivedoctets = None
                self.frcircuitcreationtime = None
                self.frcircuitlasttimechange = None
                self.frcircuitcommittedburst = None
                self.frcircuitexcessburst = None
                self.frcircuitthroughput = None
                self._segment_path = lambda: "frCircuitEntry" + "[frCircuitIfIndex='" + str(self.frcircuitifindex) + "']" + "[frCircuitDlci='" + str(self.frcircuitdlci) + "']"
                self._absolute_path = lambda: "RFC1315-MIB:RFC1315-MIB/frCircuitTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RFC1315MIB.Frcircuittable.Frcircuitentry, ['frcircuitifindex', 'frcircuitdlci', 'frcircuitstate', 'frcircuitreceivedfecns', 'frcircuitreceivedbecns', 'frcircuitsentframes', 'frcircuitsentoctets', 'frcircuitreceivedframes', 'frcircuitreceivedoctets', 'frcircuitcreationtime', 'frcircuitlasttimechange', 'frcircuitcommittedburst', 'frcircuitexcessburst', 'frcircuitthroughput'], name, value)

            class Frcircuitstate(Enum):
                """
                Frcircuitstate (Enum Class)

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



    class Frerrtable(Entity):
        """
        A table containing information about Errors on the
        Frame Relay interface.
        
        .. attribute:: frerrentry
        
        	The error information for a single frame relay interface
        	**type**\: list of  		 :py:class:`Frerrentry <ydk.models.cisco_ios_xe.RFC1315_MIB.RFC1315MIB.Frerrtable.Frerrentry>`
        
        

        """

        _prefix = 'RFC1315-MIB'

        def __init__(self):
            super(RFC1315MIB.Frerrtable, self).__init__()

            self.yang_name = "frErrTable"
            self.yang_parent_name = "RFC1315-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("frErrEntry", ("frerrentry", RFC1315MIB.Frerrtable.Frerrentry))])
            self._leafs = OrderedDict()

            self.frerrentry = YList(self)
            self._segment_path = lambda: "frErrTable"
            self._absolute_path = lambda: "RFC1315-MIB:RFC1315-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1315MIB.Frerrtable, [], name, value)


        class Frerrentry(Entity):
            """
            The error information for a single frame relay
            interface.
            
            .. attribute:: frerrifindex  (key)
            
            	The ifIndex Value of the  corresponding  ifEn\- try
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: frerrtype
            
            	The type of error that was last seen  on  this interface
            	**type**\:  :py:class:`Frerrtype <ydk.models.cisco_ios_xe.RFC1315_MIB.RFC1315MIB.Frerrtable.Frerrentry.Frerrtype>`
            
            .. attribute:: frerrdata
            
            	An octet string containing as much of the  er\- ror  packet as possible.  As a minimum, it must contain the Q.922 Address or  as  much  as  was delivered.   It is desirable to include all in\- formation up to the PDU
            	**type**\: str
            
            .. attribute:: frerrtime
            
            	The value of sysUpTime at which the error  was detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'RFC1315-MIB'

            def __init__(self):
                super(RFC1315MIB.Frerrtable.Frerrentry, self).__init__()

                self.yang_name = "frErrEntry"
                self.yang_parent_name = "frErrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['frerrifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('frerrifindex', YLeaf(YType.int32, 'frErrIfIndex')),
                    ('frerrtype', YLeaf(YType.enumeration, 'frErrType')),
                    ('frerrdata', YLeaf(YType.str, 'frErrData')),
                    ('frerrtime', YLeaf(YType.uint32, 'frErrTime')),
                ])
                self.frerrifindex = None
                self.frerrtype = None
                self.frerrdata = None
                self.frerrtime = None
                self._segment_path = lambda: "frErrEntry" + "[frErrIfIndex='" + str(self.frerrifindex) + "']"
                self._absolute_path = lambda: "RFC1315-MIB:RFC1315-MIB/frErrTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RFC1315MIB.Frerrtable.Frerrentry, ['frerrifindex', 'frerrtype', 'frerrdata', 'frerrtime'], name, value)

            class Frerrtype(Enum):
                """
                Frerrtype (Enum Class)

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


    def clone_ptr(self):
        self._top_entity = RFC1315MIB()
        return self._top_entity

