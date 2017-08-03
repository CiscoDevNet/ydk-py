""" CISCO_IETF_BFD_MIB 

This document contains the Management information base for
Bidirectional Forwarding Detection(BFD) Protocol as defined
in draft\-ietf\-bfd\-base\-06.txt.

BFD is a protocol intended to detect faults in the
bidirectional path between two forwarding engines, including
interfaces, data link(s), and to the extent possible the forwarding
engines themselves, with potentially very low latency.  It operates
independently of media, data protocols, and routing protocols.

This MIB module is based on the Internet Draft
draft\-ietf\-bfd\-mib\-03.txt and draft\-ietf\-bfd\-mib\-04.txt

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ciscobfddiag(Enum):
    """
    Ciscobfddiag

    A common BFD diagnostic code.

    .. data:: noDiagnostic = 0

    .. data:: controlDetectionTimeExpired = 1

    .. data:: echoFunctionFailed = 2

    .. data:: neighborSignaledSessionDown = 3

    .. data:: forwardingPlaneReset = 4

    .. data:: pathDown = 5

    .. data:: concatenatedPathDown = 6

    .. data:: administrativelyDown = 7

    .. data:: reverseConcatenatedPathDown = 8

    """

    noDiagnostic = Enum.YLeaf(0, "noDiagnostic")

    controlDetectionTimeExpired = Enum.YLeaf(1, "controlDetectionTimeExpired")

    echoFunctionFailed = Enum.YLeaf(2, "echoFunctionFailed")

    neighborSignaledSessionDown = Enum.YLeaf(3, "neighborSignaledSessionDown")

    forwardingPlaneReset = Enum.YLeaf(4, "forwardingPlaneReset")

    pathDown = Enum.YLeaf(5, "pathDown")

    concatenatedPathDown = Enum.YLeaf(6, "concatenatedPathDown")

    administrativelyDown = Enum.YLeaf(7, "administrativelyDown")

    reverseConcatenatedPathDown = Enum.YLeaf(8, "reverseConcatenatedPathDown")



class CiscoIetfBfdMib(Entity):
    """
    
    
    .. attribute:: ciscobfdscalarobjects
    
    	
    	**type**\:   :py:class:`Ciscobfdscalarobjects <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdscalarobjects>`
    
    .. attribute:: ciscobfdsessdiscmaptable
    
    	The BFD Session Discriminator Mapping Table maps a local discriminator value to associated BFD sessions' CiscoBfdSessIndexTC used in the ciscoBfdSessTable
    	**type**\:   :py:class:`Ciscobfdsessdiscmaptable <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsessdiscmaptable>`
    
    .. attribute:: ciscobfdsessipmaptable
    
    	The BFD Session IP Mapping Table maps given ciscoBfdSessInterface, ciscoBfdSessAddrType, and ciscoBbfdSessAddr to an associated BFD sessions' CiscoBfdSessIndexTC used in the ciscoBfdSessTable. This table SHOULD contains those BFD sessions are of IP type\: singleHop(1) and multiHop(2)
    	**type**\:   :py:class:`Ciscobfdsessipmaptable <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsessipmaptable>`
    
    .. attribute:: ciscobfdsessmaptable
    
    	The BFD Session Mapping Table maps the complex indexing of the BFD sessions to the flat  CiscoBfdSessIndexTC used in the ciscoBfdSessTable
    	**type**\:   :py:class:`Ciscobfdsessmaptable <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsessmaptable>`
    
    .. attribute:: ciscobfdsesstable
    
    	The BFD Session Table describes the BFD sessions
    	**type**\:   :py:class:`Ciscobfdsesstable <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable>`
    
    

    """

    _prefix = 'CISCO-IETF-BFD-MIB'
    _revision = '2011-04-16'

    def __init__(self):
        super(CiscoIetfBfdMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-BFD-MIB"
        self.yang_parent_name = "CISCO-IETF-BFD-MIB"

        self.ciscobfdscalarobjects = CiscoIetfBfdMib.Ciscobfdscalarobjects()
        self.ciscobfdscalarobjects.parent = self
        self._children_name_map["ciscobfdscalarobjects"] = "ciscoBfdScalarObjects"
        self._children_yang_names.add("ciscoBfdScalarObjects")

        self.ciscobfdsessdiscmaptable = CiscoIetfBfdMib.Ciscobfdsessdiscmaptable()
        self.ciscobfdsessdiscmaptable.parent = self
        self._children_name_map["ciscobfdsessdiscmaptable"] = "ciscoBfdSessDiscMapTable"
        self._children_yang_names.add("ciscoBfdSessDiscMapTable")

        self.ciscobfdsessipmaptable = CiscoIetfBfdMib.Ciscobfdsessipmaptable()
        self.ciscobfdsessipmaptable.parent = self
        self._children_name_map["ciscobfdsessipmaptable"] = "ciscoBfdSessIpMapTable"
        self._children_yang_names.add("ciscoBfdSessIpMapTable")

        self.ciscobfdsessmaptable = CiscoIetfBfdMib.Ciscobfdsessmaptable()
        self.ciscobfdsessmaptable.parent = self
        self._children_name_map["ciscobfdsessmaptable"] = "ciscoBfdSessMapTable"
        self._children_yang_names.add("ciscoBfdSessMapTable")

        self.ciscobfdsesstable = CiscoIetfBfdMib.Ciscobfdsesstable()
        self.ciscobfdsesstable.parent = self
        self._children_name_map["ciscobfdsesstable"] = "ciscoBfdSessTable"
        self._children_yang_names.add("ciscoBfdSessTable")


    class Ciscobfdscalarobjects(Entity):
        """
        
        
        .. attribute:: ciscobfdadminstatus
        
        	The global administrative status of BFD in this router. The value 'enabled' denotes that the BFD Process is  active on at least one interface; 'disabled' disables   it on all interfaces
        	**type**\:   :py:class:`Ciscobfdadminstatus <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdscalarobjects.Ciscobfdadminstatus>`
        
        .. attribute:: ciscobfdsessnotificationsenable
        
        	If this object is set to true(1), then it enables the emission of ciscoBfdSessUp and ciscoBfdSessDown  notifications; otherwise these notifications are not  emitted
        	**type**\:  bool
        
        .. attribute:: ciscobfdversionnumber
        
        	The current version number of the BFD protocol
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-IETF-BFD-MIB'
        _revision = '2011-04-16'

        def __init__(self):
            super(CiscoIetfBfdMib.Ciscobfdscalarobjects, self).__init__()

            self.yang_name = "ciscoBfdScalarObjects"
            self.yang_parent_name = "CISCO-IETF-BFD-MIB"

            self.ciscobfdadminstatus = YLeaf(YType.enumeration, "ciscoBfdAdminStatus")

            self.ciscobfdsessnotificationsenable = YLeaf(YType.boolean, "ciscoBfdSessNotificationsEnable")

            self.ciscobfdversionnumber = YLeaf(YType.uint32, "ciscoBfdVersionNumber")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ciscobfdadminstatus",
                            "ciscobfdsessnotificationsenable",
                            "ciscobfdversionnumber") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIetfBfdMib.Ciscobfdscalarobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfBfdMib.Ciscobfdscalarobjects, self).__setattr__(name, value)

        class Ciscobfdadminstatus(Enum):
            """
            Ciscobfdadminstatus

            The global administrative status of BFD in this router.

            The value 'enabled' denotes that the BFD Process is 

            active on at least one interface; 'disabled' disables  

            it on all interfaces.

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = Enum.YLeaf(1, "enabled")

            disabled = Enum.YLeaf(2, "disabled")


        def has_data(self):
            return (
                self.ciscobfdadminstatus.is_set or
                self.ciscobfdsessnotificationsenable.is_set or
                self.ciscobfdversionnumber.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ciscobfdadminstatus.yfilter != YFilter.not_set or
                self.ciscobfdsessnotificationsenable.yfilter != YFilter.not_set or
                self.ciscobfdversionnumber.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoBfdScalarObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ciscobfdadminstatus.is_set or self.ciscobfdadminstatus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciscobfdadminstatus.get_name_leafdata())
            if (self.ciscobfdsessnotificationsenable.is_set or self.ciscobfdsessnotificationsenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciscobfdsessnotificationsenable.get_name_leafdata())
            if (self.ciscobfdversionnumber.is_set or self.ciscobfdversionnumber.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciscobfdversionnumber.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoBfdAdminStatus" or name == "ciscoBfdSessNotificationsEnable" or name == "ciscoBfdVersionNumber"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ciscoBfdAdminStatus"):
                self.ciscobfdadminstatus = value
                self.ciscobfdadminstatus.value_namespace = name_space
                self.ciscobfdadminstatus.value_namespace_prefix = name_space_prefix
            if(value_path == "ciscoBfdSessNotificationsEnable"):
                self.ciscobfdsessnotificationsenable = value
                self.ciscobfdsessnotificationsenable.value_namespace = name_space
                self.ciscobfdsessnotificationsenable.value_namespace_prefix = name_space_prefix
            if(value_path == "ciscoBfdVersionNumber"):
                self.ciscobfdversionnumber = value
                self.ciscobfdversionnumber.value_namespace = name_space
                self.ciscobfdversionnumber.value_namespace_prefix = name_space_prefix


    class Ciscobfdsesstable(Entity):
        """
        The BFD Session Table describes the BFD sessions.
        
        .. attribute:: ciscobfdsessentry
        
        	The BFD Session Entry describes BFD session
        	**type**\: list of    :py:class:`Ciscobfdsessentry <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry>`
        
        

        """

        _prefix = 'CISCO-IETF-BFD-MIB'
        _revision = '2011-04-16'

        def __init__(self):
            super(CiscoIetfBfdMib.Ciscobfdsesstable, self).__init__()

            self.yang_name = "ciscoBfdSessTable"
            self.yang_parent_name = "CISCO-IETF-BFD-MIB"

            self.ciscobfdsessentry = YList(self)

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
                        super(CiscoIetfBfdMib.Ciscobfdsesstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfBfdMib.Ciscobfdsesstable, self).__setattr__(name, value)


        class Ciscobfdsessentry(Entity):
            """
            The BFD Session Entry describes BFD session.
            
            .. attribute:: ciscobfdsessindex  <key>
            
            	This object contains an index used to represent a unique BFD session on this device
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscobfdsessaddr
            
            	This object specifies the neighboring IP address which is being monitored with this BFD session. It can also be used to enabled BFD on a specific   interface. The value is set to zero when BFD session is not   associated with a specific interface
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ciscobfdsessaddrtype
            
            	This object specifies IP address type of the neighboring IP address which is being monitored with this BFD session.  Only values unknown(0), ipv4(1) or ipv6(2)  have to be supported.    A value of unknown(0) is allowed only when   the outgoing interface is of type point\-to\-point, or  when the BFD session is not associated with a specific   interface.   If any other unsupported values are attempted in a set  operation, the agent MUST return an inconsistentValue   error
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ciscobfdsessapplicationid
            
            	This object contains an index used to indicate a local application which owns or maintains this  BFD session. For instance, the MPLS VPN process may  maintain a subset of the total number of BFD  sessions.  This application ID provides a convenient  way to segregate sessions by the applications which  maintain them
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessauthenticationtype
            
            	The Authentication Type used for this BFD session. This field is valid only when the Authentication Present bit is set
            	**type**\:   :py:class:`Ciscobfdsessauthenticationtype <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.Ciscobfdsessauthenticationtype>`
            
            .. attribute:: ciscobfdsessauthpresflag
            
            	This object indicates that the local system's desire to use Authentication. Specifically, it is set   to true(1) if the local system wishes the session   to be authenticated or false(0) if not
            	**type**\:  bool
            
            .. attribute:: ciscobfdsesscontrolplanindepflag
            
            	This object indicates that the local system's ability to continue to function through a disruption of   the control plane. Specifically, it is set   to true(1) if the local system BFD implementation is  independent of the control plane. Otherwise, the   value is set to false(0)
            	**type**\:  bool
            
            .. attribute:: ciscobfdsessdemandmodedesiredflag
            
            	This object indicates that the local system's desire to use Demand mode. Specifically, it is set   to true(1) if the local system wishes to use   Demand mode or false(0) if not
            	**type**\:  bool
            
            .. attribute:: ciscobfdsessdesiredmintxinterval
            
            	This object specifies the minimum interval, in microseconds, that the local system would like to use when       transmitting BFD Control packets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessdetectmult
            
            	This object specifies the Detect time multiplier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessdiag
            
            	A diagnostic code specifying the local system's reason for the last transition of the session from up(1)   to some other state
            	**type**\:   :py:class:`Ciscobfddiag <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.Ciscobfddiag>`
            
            .. attribute:: ciscobfdsessdiscriminator
            
            	This object specifies the local discriminator for this BFD session, used to uniquely identify it
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscobfdsessechofuncmodedesiredflag
            
            	This object indicates that the local system's desire to use Echo mode. Specifically, it is set   to true(1) if the local system wishes to use   Echo mode or false(0) if not
            	**type**\:  bool
            
            .. attribute:: ciscobfdsessinterface
            
            	This object contains an interface index used to indicate the interface which this BFD session is running on
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciscobfdsessopermode
            
            	This object specifies current operating mode that BFD session is operating in
            	**type**\:   :py:class:`Ciscobfdsessopermode <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.Ciscobfdsessopermode>`
            
            .. attribute:: ciscobfdsessperfdisctime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of the session counters suffered  a discontinuity.    The relevant counters are the specific instances associated   with this BFD session of any Counter32 object contained in  the ciscoBfdSessPerfTable. If no such discontinuities have occurred   since the last re\-initialization of the local management  subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessperflastcommlostdiag
            
            	The BFD diag code for the last time communication was lost with the neighbor. If no such down event exists this object   contains a zero value
            	**type**\:   :py:class:`Ciscobfddiag <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.Ciscobfddiag>`
            
            .. attribute:: ciscobfdsessperflastsessdowntime
            
            	The value of sysUpTime on the most recent occasion at which the last time communication was lost with the neighbor. If   no such down event exist this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessperfpktin
            
            	The total number of BFD messages received for this BFD session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessperfpktinhc
            
            	This value represents the total number of BFD messages received for this BFD session. It MUST be equal to the  least significant 32 bits of ciscoBfdSessPerfPktIn  if ciscoBfdSessPerfPktInHC is supported according to  the rules spelled out in RFC2863
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscobfdsessperfpktout
            
            	The total number of BFD messages sent for this BFD session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessperfpktouthc
            
            	This value represents the total number of total number of BFD messages transmitted for this   BFD session. It MUST be equal to the  least significant 32 bits of ciscoBfdSessPerfPktIn  if ciscoBfdSessPerfPktOutHC is supported according to  the rules spelled out in RFC2863
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscobfdsessperfsessupcount
            
            	The number of times this session has gone into the Up state since the router last rebooted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessremotediscr
            
            	This object specifies the session discriminator chosen by the remote system for this BFD session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessremoteheardflag
            
            	This object specifies status of BFD packet reception from the remote system. Specifically, it is set to true(1) if  the local system is actively receiving BFD packets from the   remote system, and is set to false(0) if the local system   has not received BFD packets recently (within the detection   time) or if the local system is attempting to tear down  the BFD session
            	**type**\:  bool
            
            .. attribute:: ciscobfdsessreqminechorxinterval
            
            	This object specifies the minimum interval, in microseconds, between received BFD Echo packets that this  system is capable of supporting
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessreqminrxinterval
            
            	This object specifies the minimum interval, in microseconds, between received  BFD Control packets the   local system is capable of supporting
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table. When a row in this  table has a row in the active(1) state, no   objects in this row can be modified except the  ciscoBfdSessRowStatus and ciscoBfdSessStorageType
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ciscobfdsessstate
            
            	The perceived state of the BFD session
            	**type**\:   :py:class:`Ciscobfdsessstate <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.Ciscobfdsessstate>`
            
            .. attribute:: ciscobfdsessstortype
            
            	This variable indicates the storage type for this object. Conceptual rows having the value   'permanent' need not allow write\-access to any   columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: ciscobfdsesstype
            
            	The type of this BFD session
            	**type**\:   :py:class:`Ciscobfdsesstype <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.Ciscobfdsesstype>`
            
            .. attribute:: ciscobfdsessudpport
            
            	The destination UDP Port for BFD. The default value is the well\-known value for this port. BFD State failing(5) is only applicable if this BFD session is running version 0
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: ciscobfdsessuptime
            
            	The value of sysUpTime on the most recent occasion at which the session came up. If no such up event exists this object  contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessversionnumber
            
            	The version number of the BFD protocol that this session is running in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-BFD-MIB'
            _revision = '2011-04-16'

            def __init__(self):
                super(CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry, self).__init__()

                self.yang_name = "ciscoBfdSessEntry"
                self.yang_parent_name = "ciscoBfdSessTable"

                self.ciscobfdsessindex = YLeaf(YType.uint32, "ciscoBfdSessIndex")

                self.ciscobfdsessaddr = YLeaf(YType.str, "ciscoBfdSessAddr")

                self.ciscobfdsessaddrtype = YLeaf(YType.enumeration, "ciscoBfdSessAddrType")

                self.ciscobfdsessapplicationid = YLeaf(YType.uint32, "ciscoBfdSessApplicationId")

                self.ciscobfdsessauthenticationtype = YLeaf(YType.enumeration, "ciscoBfdSessAuthenticationType")

                self.ciscobfdsessauthpresflag = YLeaf(YType.boolean, "ciscoBfdSessAuthPresFlag")

                self.ciscobfdsesscontrolplanindepflag = YLeaf(YType.boolean, "ciscoBfdSessControlPlanIndepFlag")

                self.ciscobfdsessdemandmodedesiredflag = YLeaf(YType.boolean, "ciscoBfdSessDemandModeDesiredFlag")

                self.ciscobfdsessdesiredmintxinterval = YLeaf(YType.uint32, "ciscoBfdSessDesiredMinTxInterval")

                self.ciscobfdsessdetectmult = YLeaf(YType.uint32, "ciscoBfdSessDetectMult")

                self.ciscobfdsessdiag = YLeaf(YType.enumeration, "ciscoBfdSessDiag")

                self.ciscobfdsessdiscriminator = YLeaf(YType.uint32, "ciscoBfdSessDiscriminator")

                self.ciscobfdsessechofuncmodedesiredflag = YLeaf(YType.boolean, "ciscoBfdSessEchoFuncModeDesiredFlag")

                self.ciscobfdsessinterface = YLeaf(YType.int32, "ciscoBfdSessInterface")

                self.ciscobfdsessopermode = YLeaf(YType.enumeration, "ciscoBfdSessOperMode")

                self.ciscobfdsessperfdisctime = YLeaf(YType.uint32, "ciscoBfdSessPerfDiscTime")

                self.ciscobfdsessperflastcommlostdiag = YLeaf(YType.enumeration, "ciscoBfdSessPerfLastCommLostDiag")

                self.ciscobfdsessperflastsessdowntime = YLeaf(YType.uint32, "ciscoBfdSessPerfLastSessDownTime")

                self.ciscobfdsessperfpktin = YLeaf(YType.uint32, "ciscoBfdSessPerfPktIn")

                self.ciscobfdsessperfpktinhc = YLeaf(YType.uint64, "ciscoBfdSessPerfPktInHC")

                self.ciscobfdsessperfpktout = YLeaf(YType.uint32, "ciscoBfdSessPerfPktOut")

                self.ciscobfdsessperfpktouthc = YLeaf(YType.uint64, "ciscoBfdSessPerfPktOutHC")

                self.ciscobfdsessperfsessupcount = YLeaf(YType.uint32, "ciscoBfdSessPerfSessUpCount")

                self.ciscobfdsessremotediscr = YLeaf(YType.uint32, "ciscoBfdSessRemoteDiscr")

                self.ciscobfdsessremoteheardflag = YLeaf(YType.boolean, "ciscoBfdSessRemoteHeardFlag")

                self.ciscobfdsessreqminechorxinterval = YLeaf(YType.uint32, "ciscoBfdSessReqMinEchoRxInterval")

                self.ciscobfdsessreqminrxinterval = YLeaf(YType.uint32, "ciscoBfdSessReqMinRxInterval")

                self.ciscobfdsessrowstatus = YLeaf(YType.enumeration, "ciscoBfdSessRowStatus")

                self.ciscobfdsessstate = YLeaf(YType.enumeration, "ciscoBfdSessState")

                self.ciscobfdsessstortype = YLeaf(YType.enumeration, "ciscoBfdSessStorType")

                self.ciscobfdsesstype = YLeaf(YType.enumeration, "ciscoBfdSessType")

                self.ciscobfdsessudpport = YLeaf(YType.uint16, "ciscoBfdSessUdpPort")

                self.ciscobfdsessuptime = YLeaf(YType.uint32, "ciscoBfdSessUpTime")

                self.ciscobfdsessversionnumber = YLeaf(YType.uint32, "ciscoBfdSessVersionNumber")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscobfdsessindex",
                                "ciscobfdsessaddr",
                                "ciscobfdsessaddrtype",
                                "ciscobfdsessapplicationid",
                                "ciscobfdsessauthenticationtype",
                                "ciscobfdsessauthpresflag",
                                "ciscobfdsesscontrolplanindepflag",
                                "ciscobfdsessdemandmodedesiredflag",
                                "ciscobfdsessdesiredmintxinterval",
                                "ciscobfdsessdetectmult",
                                "ciscobfdsessdiag",
                                "ciscobfdsessdiscriminator",
                                "ciscobfdsessechofuncmodedesiredflag",
                                "ciscobfdsessinterface",
                                "ciscobfdsessopermode",
                                "ciscobfdsessperfdisctime",
                                "ciscobfdsessperflastcommlostdiag",
                                "ciscobfdsessperflastsessdowntime",
                                "ciscobfdsessperfpktin",
                                "ciscobfdsessperfpktinhc",
                                "ciscobfdsessperfpktout",
                                "ciscobfdsessperfpktouthc",
                                "ciscobfdsessperfsessupcount",
                                "ciscobfdsessremotediscr",
                                "ciscobfdsessremoteheardflag",
                                "ciscobfdsessreqminechorxinterval",
                                "ciscobfdsessreqminrxinterval",
                                "ciscobfdsessrowstatus",
                                "ciscobfdsessstate",
                                "ciscobfdsessstortype",
                                "ciscobfdsesstype",
                                "ciscobfdsessudpport",
                                "ciscobfdsessuptime",
                                "ciscobfdsessversionnumber") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry, self).__setattr__(name, value)

            class Ciscobfdsessauthenticationtype(Enum):
                """
                Ciscobfdsessauthenticationtype

                The Authentication Type used for this BFD session. This

                field is valid only when the Authentication Present bit is set

                .. data:: simplePassword = 1

                .. data:: keyedMD5 = 2

                .. data:: meticulousKeyedMD5 = 3

                .. data:: keyedSHA1 = 4

                .. data:: meticulousKeyedSHA1 = 5

                """

                simplePassword = Enum.YLeaf(1, "simplePassword")

                keyedMD5 = Enum.YLeaf(2, "keyedMD5")

                meticulousKeyedMD5 = Enum.YLeaf(3, "meticulousKeyedMD5")

                keyedSHA1 = Enum.YLeaf(4, "keyedSHA1")

                meticulousKeyedSHA1 = Enum.YLeaf(5, "meticulousKeyedSHA1")


            class Ciscobfdsessopermode(Enum):
                """
                Ciscobfdsessopermode

                This object specifies current operating mode that BFD

                session is operating in.

                .. data:: asyncModeWEchoFun = 1

                .. data:: asynchModeWOEchoFun = 2

                .. data:: demandModeWEchoFunction = 3

                .. data:: demandModeWOEchoFunction = 4

                """

                asyncModeWEchoFun = Enum.YLeaf(1, "asyncModeWEchoFun")

                asynchModeWOEchoFun = Enum.YLeaf(2, "asynchModeWOEchoFun")

                demandModeWEchoFunction = Enum.YLeaf(3, "demandModeWEchoFunction")

                demandModeWOEchoFunction = Enum.YLeaf(4, "demandModeWOEchoFunction")


            class Ciscobfdsessstate(Enum):
                """
                Ciscobfdsessstate

                The perceived state of the BFD session.

                .. data:: adminDown = 1

                .. data:: down = 2

                .. data:: init = 3

                .. data:: up = 4

                .. data:: failing = 5

                """

                adminDown = Enum.YLeaf(1, "adminDown")

                down = Enum.YLeaf(2, "down")

                init = Enum.YLeaf(3, "init")

                up = Enum.YLeaf(4, "up")

                failing = Enum.YLeaf(5, "failing")


            class Ciscobfdsesstype(Enum):
                """
                Ciscobfdsesstype

                The type of this BFD session.

                .. data:: singleHop = 1

                .. data:: multiHop = 2

                """

                singleHop = Enum.YLeaf(1, "singleHop")

                multiHop = Enum.YLeaf(2, "multiHop")


            def has_data(self):
                return (
                    self.ciscobfdsessindex.is_set or
                    self.ciscobfdsessaddr.is_set or
                    self.ciscobfdsessaddrtype.is_set or
                    self.ciscobfdsessapplicationid.is_set or
                    self.ciscobfdsessauthenticationtype.is_set or
                    self.ciscobfdsessauthpresflag.is_set or
                    self.ciscobfdsesscontrolplanindepflag.is_set or
                    self.ciscobfdsessdemandmodedesiredflag.is_set or
                    self.ciscobfdsessdesiredmintxinterval.is_set or
                    self.ciscobfdsessdetectmult.is_set or
                    self.ciscobfdsessdiag.is_set or
                    self.ciscobfdsessdiscriminator.is_set or
                    self.ciscobfdsessechofuncmodedesiredflag.is_set or
                    self.ciscobfdsessinterface.is_set or
                    self.ciscobfdsessopermode.is_set or
                    self.ciscobfdsessperfdisctime.is_set or
                    self.ciscobfdsessperflastcommlostdiag.is_set or
                    self.ciscobfdsessperflastsessdowntime.is_set or
                    self.ciscobfdsessperfpktin.is_set or
                    self.ciscobfdsessperfpktinhc.is_set or
                    self.ciscobfdsessperfpktout.is_set or
                    self.ciscobfdsessperfpktouthc.is_set or
                    self.ciscobfdsessperfsessupcount.is_set or
                    self.ciscobfdsessremotediscr.is_set or
                    self.ciscobfdsessremoteheardflag.is_set or
                    self.ciscobfdsessreqminechorxinterval.is_set or
                    self.ciscobfdsessreqminrxinterval.is_set or
                    self.ciscobfdsessrowstatus.is_set or
                    self.ciscobfdsessstate.is_set or
                    self.ciscobfdsessstortype.is_set or
                    self.ciscobfdsesstype.is_set or
                    self.ciscobfdsessudpport.is_set or
                    self.ciscobfdsessuptime.is_set or
                    self.ciscobfdsessversionnumber.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscobfdsessindex.yfilter != YFilter.not_set or
                    self.ciscobfdsessaddr.yfilter != YFilter.not_set or
                    self.ciscobfdsessaddrtype.yfilter != YFilter.not_set or
                    self.ciscobfdsessapplicationid.yfilter != YFilter.not_set or
                    self.ciscobfdsessauthenticationtype.yfilter != YFilter.not_set or
                    self.ciscobfdsessauthpresflag.yfilter != YFilter.not_set or
                    self.ciscobfdsesscontrolplanindepflag.yfilter != YFilter.not_set or
                    self.ciscobfdsessdemandmodedesiredflag.yfilter != YFilter.not_set or
                    self.ciscobfdsessdesiredmintxinterval.yfilter != YFilter.not_set or
                    self.ciscobfdsessdetectmult.yfilter != YFilter.not_set or
                    self.ciscobfdsessdiag.yfilter != YFilter.not_set or
                    self.ciscobfdsessdiscriminator.yfilter != YFilter.not_set or
                    self.ciscobfdsessechofuncmodedesiredflag.yfilter != YFilter.not_set or
                    self.ciscobfdsessinterface.yfilter != YFilter.not_set or
                    self.ciscobfdsessopermode.yfilter != YFilter.not_set or
                    self.ciscobfdsessperfdisctime.yfilter != YFilter.not_set or
                    self.ciscobfdsessperflastcommlostdiag.yfilter != YFilter.not_set or
                    self.ciscobfdsessperflastsessdowntime.yfilter != YFilter.not_set or
                    self.ciscobfdsessperfpktin.yfilter != YFilter.not_set or
                    self.ciscobfdsessperfpktinhc.yfilter != YFilter.not_set or
                    self.ciscobfdsessperfpktout.yfilter != YFilter.not_set or
                    self.ciscobfdsessperfpktouthc.yfilter != YFilter.not_set or
                    self.ciscobfdsessperfsessupcount.yfilter != YFilter.not_set or
                    self.ciscobfdsessremotediscr.yfilter != YFilter.not_set or
                    self.ciscobfdsessremoteheardflag.yfilter != YFilter.not_set or
                    self.ciscobfdsessreqminechorxinterval.yfilter != YFilter.not_set or
                    self.ciscobfdsessreqminrxinterval.yfilter != YFilter.not_set or
                    self.ciscobfdsessrowstatus.yfilter != YFilter.not_set or
                    self.ciscobfdsessstate.yfilter != YFilter.not_set or
                    self.ciscobfdsessstortype.yfilter != YFilter.not_set or
                    self.ciscobfdsesstype.yfilter != YFilter.not_set or
                    self.ciscobfdsessudpport.yfilter != YFilter.not_set or
                    self.ciscobfdsessuptime.yfilter != YFilter.not_set or
                    self.ciscobfdsessversionnumber.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoBfdSessEntry" + "[ciscoBfdSessIndex='" + self.ciscobfdsessindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/ciscoBfdSessTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscobfdsessindex.is_set or self.ciscobfdsessindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessindex.get_name_leafdata())
                if (self.ciscobfdsessaddr.is_set or self.ciscobfdsessaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessaddr.get_name_leafdata())
                if (self.ciscobfdsessaddrtype.is_set or self.ciscobfdsessaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessaddrtype.get_name_leafdata())
                if (self.ciscobfdsessapplicationid.is_set or self.ciscobfdsessapplicationid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessapplicationid.get_name_leafdata())
                if (self.ciscobfdsessauthenticationtype.is_set or self.ciscobfdsessauthenticationtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessauthenticationtype.get_name_leafdata())
                if (self.ciscobfdsessauthpresflag.is_set or self.ciscobfdsessauthpresflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessauthpresflag.get_name_leafdata())
                if (self.ciscobfdsesscontrolplanindepflag.is_set or self.ciscobfdsesscontrolplanindepflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsesscontrolplanindepflag.get_name_leafdata())
                if (self.ciscobfdsessdemandmodedesiredflag.is_set or self.ciscobfdsessdemandmodedesiredflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessdemandmodedesiredflag.get_name_leafdata())
                if (self.ciscobfdsessdesiredmintxinterval.is_set or self.ciscobfdsessdesiredmintxinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessdesiredmintxinterval.get_name_leafdata())
                if (self.ciscobfdsessdetectmult.is_set or self.ciscobfdsessdetectmult.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessdetectmult.get_name_leafdata())
                if (self.ciscobfdsessdiag.is_set or self.ciscobfdsessdiag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessdiag.get_name_leafdata())
                if (self.ciscobfdsessdiscriminator.is_set or self.ciscobfdsessdiscriminator.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessdiscriminator.get_name_leafdata())
                if (self.ciscobfdsessechofuncmodedesiredflag.is_set or self.ciscobfdsessechofuncmodedesiredflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessechofuncmodedesiredflag.get_name_leafdata())
                if (self.ciscobfdsessinterface.is_set or self.ciscobfdsessinterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessinterface.get_name_leafdata())
                if (self.ciscobfdsessopermode.is_set or self.ciscobfdsessopermode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessopermode.get_name_leafdata())
                if (self.ciscobfdsessperfdisctime.is_set or self.ciscobfdsessperfdisctime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessperfdisctime.get_name_leafdata())
                if (self.ciscobfdsessperflastcommlostdiag.is_set or self.ciscobfdsessperflastcommlostdiag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessperflastcommlostdiag.get_name_leafdata())
                if (self.ciscobfdsessperflastsessdowntime.is_set or self.ciscobfdsessperflastsessdowntime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessperflastsessdowntime.get_name_leafdata())
                if (self.ciscobfdsessperfpktin.is_set or self.ciscobfdsessperfpktin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessperfpktin.get_name_leafdata())
                if (self.ciscobfdsessperfpktinhc.is_set or self.ciscobfdsessperfpktinhc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessperfpktinhc.get_name_leafdata())
                if (self.ciscobfdsessperfpktout.is_set or self.ciscobfdsessperfpktout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessperfpktout.get_name_leafdata())
                if (self.ciscobfdsessperfpktouthc.is_set or self.ciscobfdsessperfpktouthc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessperfpktouthc.get_name_leafdata())
                if (self.ciscobfdsessperfsessupcount.is_set or self.ciscobfdsessperfsessupcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessperfsessupcount.get_name_leafdata())
                if (self.ciscobfdsessremotediscr.is_set or self.ciscobfdsessremotediscr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessremotediscr.get_name_leafdata())
                if (self.ciscobfdsessremoteheardflag.is_set or self.ciscobfdsessremoteheardflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessremoteheardflag.get_name_leafdata())
                if (self.ciscobfdsessreqminechorxinterval.is_set or self.ciscobfdsessreqminechorxinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessreqminechorxinterval.get_name_leafdata())
                if (self.ciscobfdsessreqminrxinterval.is_set or self.ciscobfdsessreqminrxinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessreqminrxinterval.get_name_leafdata())
                if (self.ciscobfdsessrowstatus.is_set or self.ciscobfdsessrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessrowstatus.get_name_leafdata())
                if (self.ciscobfdsessstate.is_set or self.ciscobfdsessstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessstate.get_name_leafdata())
                if (self.ciscobfdsessstortype.is_set or self.ciscobfdsessstortype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessstortype.get_name_leafdata())
                if (self.ciscobfdsesstype.is_set or self.ciscobfdsesstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsesstype.get_name_leafdata())
                if (self.ciscobfdsessudpport.is_set or self.ciscobfdsessudpport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessudpport.get_name_leafdata())
                if (self.ciscobfdsessuptime.is_set or self.ciscobfdsessuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessuptime.get_name_leafdata())
                if (self.ciscobfdsessversionnumber.is_set or self.ciscobfdsessversionnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessversionnumber.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoBfdSessIndex" or name == "ciscoBfdSessAddr" or name == "ciscoBfdSessAddrType" or name == "ciscoBfdSessApplicationId" or name == "ciscoBfdSessAuthenticationType" or name == "ciscoBfdSessAuthPresFlag" or name == "ciscoBfdSessControlPlanIndepFlag" or name == "ciscoBfdSessDemandModeDesiredFlag" or name == "ciscoBfdSessDesiredMinTxInterval" or name == "ciscoBfdSessDetectMult" or name == "ciscoBfdSessDiag" or name == "ciscoBfdSessDiscriminator" or name == "ciscoBfdSessEchoFuncModeDesiredFlag" or name == "ciscoBfdSessInterface" or name == "ciscoBfdSessOperMode" or name == "ciscoBfdSessPerfDiscTime" or name == "ciscoBfdSessPerfLastCommLostDiag" or name == "ciscoBfdSessPerfLastSessDownTime" or name == "ciscoBfdSessPerfPktIn" or name == "ciscoBfdSessPerfPktInHC" or name == "ciscoBfdSessPerfPktOut" or name == "ciscoBfdSessPerfPktOutHC" or name == "ciscoBfdSessPerfSessUpCount" or name == "ciscoBfdSessRemoteDiscr" or name == "ciscoBfdSessRemoteHeardFlag" or name == "ciscoBfdSessReqMinEchoRxInterval" or name == "ciscoBfdSessReqMinRxInterval" or name == "ciscoBfdSessRowStatus" or name == "ciscoBfdSessState" or name == "ciscoBfdSessStorType" or name == "ciscoBfdSessType" or name == "ciscoBfdSessUdpPort" or name == "ciscoBfdSessUpTime" or name == "ciscoBfdSessVersionNumber"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoBfdSessIndex"):
                    self.ciscobfdsessindex = value
                    self.ciscobfdsessindex.value_namespace = name_space
                    self.ciscobfdsessindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessAddr"):
                    self.ciscobfdsessaddr = value
                    self.ciscobfdsessaddr.value_namespace = name_space
                    self.ciscobfdsessaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessAddrType"):
                    self.ciscobfdsessaddrtype = value
                    self.ciscobfdsessaddrtype.value_namespace = name_space
                    self.ciscobfdsessaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessApplicationId"):
                    self.ciscobfdsessapplicationid = value
                    self.ciscobfdsessapplicationid.value_namespace = name_space
                    self.ciscobfdsessapplicationid.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessAuthenticationType"):
                    self.ciscobfdsessauthenticationtype = value
                    self.ciscobfdsessauthenticationtype.value_namespace = name_space
                    self.ciscobfdsessauthenticationtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessAuthPresFlag"):
                    self.ciscobfdsessauthpresflag = value
                    self.ciscobfdsessauthpresflag.value_namespace = name_space
                    self.ciscobfdsessauthpresflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessControlPlanIndepFlag"):
                    self.ciscobfdsesscontrolplanindepflag = value
                    self.ciscobfdsesscontrolplanindepflag.value_namespace = name_space
                    self.ciscobfdsesscontrolplanindepflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessDemandModeDesiredFlag"):
                    self.ciscobfdsessdemandmodedesiredflag = value
                    self.ciscobfdsessdemandmodedesiredflag.value_namespace = name_space
                    self.ciscobfdsessdemandmodedesiredflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessDesiredMinTxInterval"):
                    self.ciscobfdsessdesiredmintxinterval = value
                    self.ciscobfdsessdesiredmintxinterval.value_namespace = name_space
                    self.ciscobfdsessdesiredmintxinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessDetectMult"):
                    self.ciscobfdsessdetectmult = value
                    self.ciscobfdsessdetectmult.value_namespace = name_space
                    self.ciscobfdsessdetectmult.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessDiag"):
                    self.ciscobfdsessdiag = value
                    self.ciscobfdsessdiag.value_namespace = name_space
                    self.ciscobfdsessdiag.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessDiscriminator"):
                    self.ciscobfdsessdiscriminator = value
                    self.ciscobfdsessdiscriminator.value_namespace = name_space
                    self.ciscobfdsessdiscriminator.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessEchoFuncModeDesiredFlag"):
                    self.ciscobfdsessechofuncmodedesiredflag = value
                    self.ciscobfdsessechofuncmodedesiredflag.value_namespace = name_space
                    self.ciscobfdsessechofuncmodedesiredflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessInterface"):
                    self.ciscobfdsessinterface = value
                    self.ciscobfdsessinterface.value_namespace = name_space
                    self.ciscobfdsessinterface.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessOperMode"):
                    self.ciscobfdsessopermode = value
                    self.ciscobfdsessopermode.value_namespace = name_space
                    self.ciscobfdsessopermode.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessPerfDiscTime"):
                    self.ciscobfdsessperfdisctime = value
                    self.ciscobfdsessperfdisctime.value_namespace = name_space
                    self.ciscobfdsessperfdisctime.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessPerfLastCommLostDiag"):
                    self.ciscobfdsessperflastcommlostdiag = value
                    self.ciscobfdsessperflastcommlostdiag.value_namespace = name_space
                    self.ciscobfdsessperflastcommlostdiag.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessPerfLastSessDownTime"):
                    self.ciscobfdsessperflastsessdowntime = value
                    self.ciscobfdsessperflastsessdowntime.value_namespace = name_space
                    self.ciscobfdsessperflastsessdowntime.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessPerfPktIn"):
                    self.ciscobfdsessperfpktin = value
                    self.ciscobfdsessperfpktin.value_namespace = name_space
                    self.ciscobfdsessperfpktin.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessPerfPktInHC"):
                    self.ciscobfdsessperfpktinhc = value
                    self.ciscobfdsessperfpktinhc.value_namespace = name_space
                    self.ciscobfdsessperfpktinhc.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessPerfPktOut"):
                    self.ciscobfdsessperfpktout = value
                    self.ciscobfdsessperfpktout.value_namespace = name_space
                    self.ciscobfdsessperfpktout.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessPerfPktOutHC"):
                    self.ciscobfdsessperfpktouthc = value
                    self.ciscobfdsessperfpktouthc.value_namespace = name_space
                    self.ciscobfdsessperfpktouthc.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessPerfSessUpCount"):
                    self.ciscobfdsessperfsessupcount = value
                    self.ciscobfdsessperfsessupcount.value_namespace = name_space
                    self.ciscobfdsessperfsessupcount.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessRemoteDiscr"):
                    self.ciscobfdsessremotediscr = value
                    self.ciscobfdsessremotediscr.value_namespace = name_space
                    self.ciscobfdsessremotediscr.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessRemoteHeardFlag"):
                    self.ciscobfdsessremoteheardflag = value
                    self.ciscobfdsessremoteheardflag.value_namespace = name_space
                    self.ciscobfdsessremoteheardflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessReqMinEchoRxInterval"):
                    self.ciscobfdsessreqminechorxinterval = value
                    self.ciscobfdsessreqminechorxinterval.value_namespace = name_space
                    self.ciscobfdsessreqminechorxinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessReqMinRxInterval"):
                    self.ciscobfdsessreqminrxinterval = value
                    self.ciscobfdsessreqminrxinterval.value_namespace = name_space
                    self.ciscobfdsessreqminrxinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessRowStatus"):
                    self.ciscobfdsessrowstatus = value
                    self.ciscobfdsessrowstatus.value_namespace = name_space
                    self.ciscobfdsessrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessState"):
                    self.ciscobfdsessstate = value
                    self.ciscobfdsessstate.value_namespace = name_space
                    self.ciscobfdsessstate.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessStorType"):
                    self.ciscobfdsessstortype = value
                    self.ciscobfdsessstortype.value_namespace = name_space
                    self.ciscobfdsessstortype.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessType"):
                    self.ciscobfdsesstype = value
                    self.ciscobfdsesstype.value_namespace = name_space
                    self.ciscobfdsesstype.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessUdpPort"):
                    self.ciscobfdsessudpport = value
                    self.ciscobfdsessudpport.value_namespace = name_space
                    self.ciscobfdsessudpport.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessUpTime"):
                    self.ciscobfdsessuptime = value
                    self.ciscobfdsessuptime.value_namespace = name_space
                    self.ciscobfdsessuptime.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessVersionNumber"):
                    self.ciscobfdsessversionnumber = value
                    self.ciscobfdsessversionnumber.value_namespace = name_space
                    self.ciscobfdsessversionnumber.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscobfdsessentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscobfdsessentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoBfdSessTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoBfdSessEntry"):
                for c in self.ciscobfdsessentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscobfdsessentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoBfdSessEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciscobfdsessmaptable(Entity):
        """
        The BFD Session Mapping Table maps the complex
        indexing of the BFD sessions to the flat 
        CiscoBfdSessIndexTC used in the ciscoBfdSessTable.
        
        .. attribute:: ciscobfdsessmapentry
        
        	The BFD Session Entry describes BFD session that is mapped to this index
        	**type**\: list of    :py:class:`Ciscobfdsessmapentry <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsessmaptable.Ciscobfdsessmapentry>`
        
        

        """

        _prefix = 'CISCO-IETF-BFD-MIB'
        _revision = '2011-04-16'

        def __init__(self):
            super(CiscoIetfBfdMib.Ciscobfdsessmaptable, self).__init__()

            self.yang_name = "ciscoBfdSessMapTable"
            self.yang_parent_name = "CISCO-IETF-BFD-MIB"

            self.ciscobfdsessmapentry = YList(self)

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
                        super(CiscoIetfBfdMib.Ciscobfdsessmaptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfBfdMib.Ciscobfdsessmaptable, self).__setattr__(name, value)


        class Ciscobfdsessmapentry(Entity):
            """
            The BFD Session Entry describes BFD session
            that is mapped to this index.
            
            .. attribute:: ciscobfdsessapplicationid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ciscobfdsessapplicationid <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessdiscriminator  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscobfdsessdiscriminator <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessaddrtype  <key>
            
            	
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ciscobfdsessaddr  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`ciscobfdsessaddr <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessmapbfdindex
            
            	This object indicates the CiscoBfdSessIndexTC referred to by the indices of this row. In essence, a mapping is  provided between these indices and the ciscoBfdSessTable
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-BFD-MIB'
            _revision = '2011-04-16'

            def __init__(self):
                super(CiscoIetfBfdMib.Ciscobfdsessmaptable.Ciscobfdsessmapentry, self).__init__()

                self.yang_name = "ciscoBfdSessMapEntry"
                self.yang_parent_name = "ciscoBfdSessMapTable"

                self.ciscobfdsessapplicationid = YLeaf(YType.str, "ciscoBfdSessApplicationId")

                self.ciscobfdsessdiscriminator = YLeaf(YType.str, "ciscoBfdSessDiscriminator")

                self.ciscobfdsessaddrtype = YLeaf(YType.enumeration, "ciscoBfdSessAddrType")

                self.ciscobfdsessaddr = YLeaf(YType.str, "ciscoBfdSessAddr")

                self.ciscobfdsessmapbfdindex = YLeaf(YType.uint32, "ciscoBfdSessMapBfdIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscobfdsessapplicationid",
                                "ciscobfdsessdiscriminator",
                                "ciscobfdsessaddrtype",
                                "ciscobfdsessaddr",
                                "ciscobfdsessmapbfdindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfBfdMib.Ciscobfdsessmaptable.Ciscobfdsessmapentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfBfdMib.Ciscobfdsessmaptable.Ciscobfdsessmapentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ciscobfdsessapplicationid.is_set or
                    self.ciscobfdsessdiscriminator.is_set or
                    self.ciscobfdsessaddrtype.is_set or
                    self.ciscobfdsessaddr.is_set or
                    self.ciscobfdsessmapbfdindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscobfdsessapplicationid.yfilter != YFilter.not_set or
                    self.ciscobfdsessdiscriminator.yfilter != YFilter.not_set or
                    self.ciscobfdsessaddrtype.yfilter != YFilter.not_set or
                    self.ciscobfdsessaddr.yfilter != YFilter.not_set or
                    self.ciscobfdsessmapbfdindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoBfdSessMapEntry" + "[ciscoBfdSessApplicationId='" + self.ciscobfdsessapplicationid.get() + "']" + "[ciscoBfdSessDiscriminator='" + self.ciscobfdsessdiscriminator.get() + "']" + "[ciscoBfdSessAddrType='" + self.ciscobfdsessaddrtype.get() + "']" + "[ciscoBfdSessAddr='" + self.ciscobfdsessaddr.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/ciscoBfdSessMapTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscobfdsessapplicationid.is_set or self.ciscobfdsessapplicationid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessapplicationid.get_name_leafdata())
                if (self.ciscobfdsessdiscriminator.is_set or self.ciscobfdsessdiscriminator.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessdiscriminator.get_name_leafdata())
                if (self.ciscobfdsessaddrtype.is_set or self.ciscobfdsessaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessaddrtype.get_name_leafdata())
                if (self.ciscobfdsessaddr.is_set or self.ciscobfdsessaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessaddr.get_name_leafdata())
                if (self.ciscobfdsessmapbfdindex.is_set or self.ciscobfdsessmapbfdindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessmapbfdindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoBfdSessApplicationId" or name == "ciscoBfdSessDiscriminator" or name == "ciscoBfdSessAddrType" or name == "ciscoBfdSessAddr" or name == "ciscoBfdSessMapBfdIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoBfdSessApplicationId"):
                    self.ciscobfdsessapplicationid = value
                    self.ciscobfdsessapplicationid.value_namespace = name_space
                    self.ciscobfdsessapplicationid.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessDiscriminator"):
                    self.ciscobfdsessdiscriminator = value
                    self.ciscobfdsessdiscriminator.value_namespace = name_space
                    self.ciscobfdsessdiscriminator.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessAddrType"):
                    self.ciscobfdsessaddrtype = value
                    self.ciscobfdsessaddrtype.value_namespace = name_space
                    self.ciscobfdsessaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessAddr"):
                    self.ciscobfdsessaddr = value
                    self.ciscobfdsessaddr.value_namespace = name_space
                    self.ciscobfdsessaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessMapBfdIndex"):
                    self.ciscobfdsessmapbfdindex = value
                    self.ciscobfdsessmapbfdindex.value_namespace = name_space
                    self.ciscobfdsessmapbfdindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscobfdsessmapentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscobfdsessmapentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoBfdSessMapTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoBfdSessMapEntry"):
                for c in self.ciscobfdsessmapentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfBfdMib.Ciscobfdsessmaptable.Ciscobfdsessmapentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscobfdsessmapentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoBfdSessMapEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciscobfdsessdiscmaptable(Entity):
        """
        The BFD Session Discriminator Mapping Table maps a
        local discriminator value to associated BFD sessions'
        CiscoBfdSessIndexTC used in the ciscoBfdSessTable.
        
        .. attribute:: ciscobfdsessdiscmapentry
        
        	Each row contains a mapping between a local discriminator value to an entry in ciscoBfdSessTable
        	**type**\: list of    :py:class:`Ciscobfdsessdiscmapentry <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsessdiscmaptable.Ciscobfdsessdiscmapentry>`
        
        

        """

        _prefix = 'CISCO-IETF-BFD-MIB'
        _revision = '2011-04-16'

        def __init__(self):
            super(CiscoIetfBfdMib.Ciscobfdsessdiscmaptable, self).__init__()

            self.yang_name = "ciscoBfdSessDiscMapTable"
            self.yang_parent_name = "CISCO-IETF-BFD-MIB"

            self.ciscobfdsessdiscmapentry = YList(self)

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
                        super(CiscoIetfBfdMib.Ciscobfdsessdiscmaptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfBfdMib.Ciscobfdsessdiscmaptable, self).__setattr__(name, value)


        class Ciscobfdsessdiscmapentry(Entity):
            """
            Each row contains a mapping between a local discriminator
            value to an entry in ciscoBfdSessTable.
            
            .. attribute:: ciscobfdsessdiscriminator  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscobfdsessdiscriminator <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessdiscmapindex
            
            	This object indicates the CiscoBfdSessIndexTC referred to by the index of this row. In essence, a mapping is  provided between this index and the ciscoBfdSessTable
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-BFD-MIB'
            _revision = '2011-04-16'

            def __init__(self):
                super(CiscoIetfBfdMib.Ciscobfdsessdiscmaptable.Ciscobfdsessdiscmapentry, self).__init__()

                self.yang_name = "ciscoBfdSessDiscMapEntry"
                self.yang_parent_name = "ciscoBfdSessDiscMapTable"

                self.ciscobfdsessdiscriminator = YLeaf(YType.str, "ciscoBfdSessDiscriminator")

                self.ciscobfdsessdiscmapindex = YLeaf(YType.uint32, "ciscoBfdSessDiscMapIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscobfdsessdiscriminator",
                                "ciscobfdsessdiscmapindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfBfdMib.Ciscobfdsessdiscmaptable.Ciscobfdsessdiscmapentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfBfdMib.Ciscobfdsessdiscmaptable.Ciscobfdsessdiscmapentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ciscobfdsessdiscriminator.is_set or
                    self.ciscobfdsessdiscmapindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscobfdsessdiscriminator.yfilter != YFilter.not_set or
                    self.ciscobfdsessdiscmapindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoBfdSessDiscMapEntry" + "[ciscoBfdSessDiscriminator='" + self.ciscobfdsessdiscriminator.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/ciscoBfdSessDiscMapTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscobfdsessdiscriminator.is_set or self.ciscobfdsessdiscriminator.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessdiscriminator.get_name_leafdata())
                if (self.ciscobfdsessdiscmapindex.is_set or self.ciscobfdsessdiscmapindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessdiscmapindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoBfdSessDiscriminator" or name == "ciscoBfdSessDiscMapIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoBfdSessDiscriminator"):
                    self.ciscobfdsessdiscriminator = value
                    self.ciscobfdsessdiscriminator.value_namespace = name_space
                    self.ciscobfdsessdiscriminator.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessDiscMapIndex"):
                    self.ciscobfdsessdiscmapindex = value
                    self.ciscobfdsessdiscmapindex.value_namespace = name_space
                    self.ciscobfdsessdiscmapindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscobfdsessdiscmapentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscobfdsessdiscmapentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoBfdSessDiscMapTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoBfdSessDiscMapEntry"):
                for c in self.ciscobfdsessdiscmapentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfBfdMib.Ciscobfdsessdiscmaptable.Ciscobfdsessdiscmapentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscobfdsessdiscmapentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoBfdSessDiscMapEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciscobfdsessipmaptable(Entity):
        """
        The BFD Session IP Mapping Table maps given
        ciscoBfdSessInterface, ciscoBfdSessAddrType, and
        ciscoBbfdSessAddr to an associated BFD sessions'
        CiscoBfdSessIndexTC used in the ciscoBfdSessTable.
        This table SHOULD contains those BFD sessions are
        of IP type\: singleHop(1) and multiHop(2).
        
        .. attribute:: ciscobfdsessipmapentry
        
        	Each row contains a mapping between ciscoBfdSessInterface, ciscoBfdSessAddrType and ciscoBfdSessAddr values to an  entry in ciscoBfdSessTable
        	**type**\: list of    :py:class:`Ciscobfdsessipmapentry <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsessipmaptable.Ciscobfdsessipmapentry>`
        
        

        """

        _prefix = 'CISCO-IETF-BFD-MIB'
        _revision = '2011-04-16'

        def __init__(self):
            super(CiscoIetfBfdMib.Ciscobfdsessipmaptable, self).__init__()

            self.yang_name = "ciscoBfdSessIpMapTable"
            self.yang_parent_name = "CISCO-IETF-BFD-MIB"

            self.ciscobfdsessipmapentry = YList(self)

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
                        super(CiscoIetfBfdMib.Ciscobfdsessipmaptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfBfdMib.Ciscobfdsessipmaptable, self).__setattr__(name, value)


        class Ciscobfdsessipmapentry(Entity):
            """
            Each row contains a mapping between ciscoBfdSessInterface,
            ciscoBfdSessAddrType and ciscoBfdSessAddr values to an 
            entry in ciscoBfdSessTable.
            
            .. attribute:: ciscobfdsessinterface  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ciscobfdsessinterface <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessaddrtype  <key>
            
            	
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ciscobfdsessaddr  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`ciscobfdsessaddr <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessipmapindex
            
            	This object indicates the CiscoBfdSessIndexTC referred to by the indices of this row. In essence, a mapping is  provided between these indices and an entry in ciscoBfdSessTable
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-BFD-MIB'
            _revision = '2011-04-16'

            def __init__(self):
                super(CiscoIetfBfdMib.Ciscobfdsessipmaptable.Ciscobfdsessipmapentry, self).__init__()

                self.yang_name = "ciscoBfdSessIpMapEntry"
                self.yang_parent_name = "ciscoBfdSessIpMapTable"

                self.ciscobfdsessinterface = YLeaf(YType.str, "ciscoBfdSessInterface")

                self.ciscobfdsessaddrtype = YLeaf(YType.enumeration, "ciscoBfdSessAddrType")

                self.ciscobfdsessaddr = YLeaf(YType.str, "ciscoBfdSessAddr")

                self.ciscobfdsessipmapindex = YLeaf(YType.uint32, "ciscoBfdSessIpMapIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscobfdsessinterface",
                                "ciscobfdsessaddrtype",
                                "ciscobfdsessaddr",
                                "ciscobfdsessipmapindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfBfdMib.Ciscobfdsessipmaptable.Ciscobfdsessipmapentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfBfdMib.Ciscobfdsessipmaptable.Ciscobfdsessipmapentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ciscobfdsessinterface.is_set or
                    self.ciscobfdsessaddrtype.is_set or
                    self.ciscobfdsessaddr.is_set or
                    self.ciscobfdsessipmapindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscobfdsessinterface.yfilter != YFilter.not_set or
                    self.ciscobfdsessaddrtype.yfilter != YFilter.not_set or
                    self.ciscobfdsessaddr.yfilter != YFilter.not_set or
                    self.ciscobfdsessipmapindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoBfdSessIpMapEntry" + "[ciscoBfdSessInterface='" + self.ciscobfdsessinterface.get() + "']" + "[ciscoBfdSessAddrType='" + self.ciscobfdsessaddrtype.get() + "']" + "[ciscoBfdSessAddr='" + self.ciscobfdsessaddr.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/ciscoBfdSessIpMapTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscobfdsessinterface.is_set or self.ciscobfdsessinterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessinterface.get_name_leafdata())
                if (self.ciscobfdsessaddrtype.is_set or self.ciscobfdsessaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessaddrtype.get_name_leafdata())
                if (self.ciscobfdsessaddr.is_set or self.ciscobfdsessaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessaddr.get_name_leafdata())
                if (self.ciscobfdsessipmapindex.is_set or self.ciscobfdsessipmapindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscobfdsessipmapindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoBfdSessInterface" or name == "ciscoBfdSessAddrType" or name == "ciscoBfdSessAddr" or name == "ciscoBfdSessIpMapIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoBfdSessInterface"):
                    self.ciscobfdsessinterface = value
                    self.ciscobfdsessinterface.value_namespace = name_space
                    self.ciscobfdsessinterface.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessAddrType"):
                    self.ciscobfdsessaddrtype = value
                    self.ciscobfdsessaddrtype.value_namespace = name_space
                    self.ciscobfdsessaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessAddr"):
                    self.ciscobfdsessaddr = value
                    self.ciscobfdsessaddr.value_namespace = name_space
                    self.ciscobfdsessaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoBfdSessIpMapIndex"):
                    self.ciscobfdsessipmapindex = value
                    self.ciscobfdsessipmapindex.value_namespace = name_space
                    self.ciscobfdsessipmapindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscobfdsessipmapentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscobfdsessipmapentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoBfdSessIpMapTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoBfdSessIpMapEntry"):
                for c in self.ciscobfdsessipmapentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfBfdMib.Ciscobfdsessipmaptable.Ciscobfdsessipmapentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscobfdsessipmapentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoBfdSessIpMapEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ciscobfdscalarobjects is not None and self.ciscobfdscalarobjects.has_data()) or
            (self.ciscobfdsessdiscmaptable is not None and self.ciscobfdsessdiscmaptable.has_data()) or
            (self.ciscobfdsessipmaptable is not None and self.ciscobfdsessipmaptable.has_data()) or
            (self.ciscobfdsessmaptable is not None and self.ciscobfdsessmaptable.has_data()) or
            (self.ciscobfdsesstable is not None and self.ciscobfdsesstable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ciscobfdscalarobjects is not None and self.ciscobfdscalarobjects.has_operation()) or
            (self.ciscobfdsessdiscmaptable is not None and self.ciscobfdsessdiscmaptable.has_operation()) or
            (self.ciscobfdsessipmaptable is not None and self.ciscobfdsessipmaptable.has_operation()) or
            (self.ciscobfdsessmaptable is not None and self.ciscobfdsessmaptable.has_operation()) or
            (self.ciscobfdsesstable is not None and self.ciscobfdsesstable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB" + path_buffer

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

        if (child_yang_name == "ciscoBfdScalarObjects"):
            if (self.ciscobfdscalarobjects is None):
                self.ciscobfdscalarobjects = CiscoIetfBfdMib.Ciscobfdscalarobjects()
                self.ciscobfdscalarobjects.parent = self
                self._children_name_map["ciscobfdscalarobjects"] = "ciscoBfdScalarObjects"
            return self.ciscobfdscalarobjects

        if (child_yang_name == "ciscoBfdSessDiscMapTable"):
            if (self.ciscobfdsessdiscmaptable is None):
                self.ciscobfdsessdiscmaptable = CiscoIetfBfdMib.Ciscobfdsessdiscmaptable()
                self.ciscobfdsessdiscmaptable.parent = self
                self._children_name_map["ciscobfdsessdiscmaptable"] = "ciscoBfdSessDiscMapTable"
            return self.ciscobfdsessdiscmaptable

        if (child_yang_name == "ciscoBfdSessIpMapTable"):
            if (self.ciscobfdsessipmaptable is None):
                self.ciscobfdsessipmaptable = CiscoIetfBfdMib.Ciscobfdsessipmaptable()
                self.ciscobfdsessipmaptable.parent = self
                self._children_name_map["ciscobfdsessipmaptable"] = "ciscoBfdSessIpMapTable"
            return self.ciscobfdsessipmaptable

        if (child_yang_name == "ciscoBfdSessMapTable"):
            if (self.ciscobfdsessmaptable is None):
                self.ciscobfdsessmaptable = CiscoIetfBfdMib.Ciscobfdsessmaptable()
                self.ciscobfdsessmaptable.parent = self
                self._children_name_map["ciscobfdsessmaptable"] = "ciscoBfdSessMapTable"
            return self.ciscobfdsessmaptable

        if (child_yang_name == "ciscoBfdSessTable"):
            if (self.ciscobfdsesstable is None):
                self.ciscobfdsesstable = CiscoIetfBfdMib.Ciscobfdsesstable()
                self.ciscobfdsesstable.parent = self
                self._children_name_map["ciscobfdsesstable"] = "ciscoBfdSessTable"
            return self.ciscobfdsesstable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ciscoBfdScalarObjects" or name == "ciscoBfdSessDiscMapTable" or name == "ciscoBfdSessIpMapTable" or name == "ciscoBfdSessMapTable" or name == "ciscoBfdSessTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIetfBfdMib()
        return self._top_entity

