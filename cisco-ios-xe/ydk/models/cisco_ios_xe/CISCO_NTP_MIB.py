""" CISCO_NTP_MIB 

This MIB module defines a MIB which provides
mechanisms to monitor an NTP server.

The MIB is derived from the Technical Report
#Management of the NTP with SNMP# TR No. 98\-09
authored by A.S. Sethi and Dave Mills in the
University of Delaware.

Below is a brief overview of NTP system architecture
and implementation model. This will help understand
the objects defined below and their relationships.

NTP Intro\:
The Network Time Protocol (NTP) Version 3, is used to
synchronize timekeeping among a set of distributed
time servers and clients.  The service model is based
on a returnable\-time design which depends only on
measured clock offsets, but does not require reliable
message delivery.  The synchronization subnet uses a
self\-organizing, hierarchical master\-slave
configuration, with synchronization paths determined
by a minimum\-weight spanning tree.  While multiple
masters (primary servers) may exist, there is no
requirement for an election protocol.

System Archiecture\:
In the NTP model a number of primary reference
sources, synchronized by wire or radio to national
standards, are connected to widely accessible
resources, such as backbone gateways, and operated as
primary time servers.  The purpose of NTP is to convey
timekeeping information from these servers to other
time servers via the Internet and also to cross\-check
clocks and mitigate errors due to equipment or
propagation failures.  Some number of local\-net hosts
or gateways, acting as secondary time servers, run NTP
with one or more of the primary servers.  In order to
reduce the protocol overhead, the secondary servers
distribute time via NTP to the remaining local\-net
hosts.  In the interest of reliability, selected hosts
can be equipped with less accurate but less expensive
radio clocks and used for backup in case of failure of
the primary and/or secondary servers or communication
paths between them.

NTP is designed to produce three products\: clock
offset, round\-trip delay and dispersion, all of which
are relative to a selected reference clock.  Clock
offset represents the amount to adjust the local clock
to bring it into correspondence with the reference
clock.  Roundtrip delay provides the capability to
launch a message to arrive at the reference clock at a
specified time.  Dispersion represents the maximum
error of the local clock relative to the reference
clock.  Since most host time servers will synchronize
via another peer time server, there are two components
in each of these three products, those determined by
the peer relative to the primary reference source of
standard time and those measured by the host relative
to the peer.  Each of these components are maintained
separately in the protocol in order to facilitate
error control and management of the subnet itself.  
They provide not only precision measurements of offset
and delay, but also definitive maximum error bounds,
so that the user interface can determine not only the
time, but the quality of the time as well.

Implementation Model\:
In what may be the most common client/server model a
client sends an NTP message to one or more servers and
processes the replies as received.  The server
interchanges addresses and ports, overwrites certain
fields in the message, recalculates the checksum and
returns the message immediately.  Information included
in the NTP message allows the client to determine the
server time with respect to local time and adjust the
local clock accordingly.  In addition, the message
includes information to calculate the expected
timekeeping accuracy and reliability, as well as
select the best from possibly several servers.

While the client/server model may suffice for use on
local nets involving a public server and perhaps many
workstation clients, the full generality of NTP
requires distributed participation of a number of
client/servers or peers arranged in a dynamically
reconfigurable, hierarchically distributed
configuration.  It also requires sophisticated
algorithms for association management, data
manipulation and local\-clock control.

Glossary\:
1. Host\: Refers to an instantiation of the NTP
        protocol on a local processor.
2. Peer\: Refers to an instantiation of the NTP
        protocol on a remote processor connected by
        a network path from the local host.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ntpleapindicator(Enum):
    """
    Ntpleapindicator

    This is a two\-bit code warning of an impending leap

    second to be inserted in the NTP timescale.  The bits

    are set before 23\:59 on the day of insertion and reset

    after 00\:00 on the following day.  This causes the

    number of seconds (rollover interval) in the day of

    insertion to be increased or decreased by one.  The two

    bits are coded as below,

    00, no warning

    01, last minute has 61 seconds

    10, last minute has 59 seconds

    11, alarm condition (clock not synchronized)

    .. data:: noWarning = 0

    .. data:: addSecond = 1

    .. data:: subtractSecond = 2

    .. data:: alarm = 3

    """

    noWarning = Enum.YLeaf(0, "noWarning")

    addSecond = Enum.YLeaf(1, "addSecond")

    subtractSecond = Enum.YLeaf(2, "subtractSecond")

    alarm = Enum.YLeaf(3, "alarm")



class CiscoNtpMib(Entity):
    """
    
    
    .. attribute:: cntpfilterregistertable
    
    	The following table contains NTP state variables used by the NTP clock filter and selection algorithms. This table depicts a shift register.  Each stage in the shift register is a 3\-tuple consisting of the measured clock offset, measured clock delay and measured clock dispersion associated with a single observation.  An important factor affecting the accuracy and reliability of time distribution is the complex of algorithms used to reduce the effect of statistical errors and falsetickers due to failure of various subnet components, reference sources or propagation media.  The NTP clock\-filter and selection algorithms are designed to do exactly this.  The objects in the filter register table below are used by these algorthims to minimize the error in the calculated time
    	**type**\:   :py:class:`Cntpfilterregistertable <ydk.models.cisco_ios_xe.CISCO_NTP_MIB.CiscoNtpMib.Cntpfilterregistertable>`
    
    .. attribute:: cntppeersvartable
    
    	This table provides information on the peers with which the local NTP server has associations.  The peers are also NTP servers but running on different hosts
    	**type**\:   :py:class:`Cntppeersvartable <ydk.models.cisco_ios_xe.CISCO_NTP_MIB.CiscoNtpMib.Cntppeersvartable>`
    
    .. attribute:: cntpsystem
    
    	
    	**type**\:   :py:class:`Cntpsystem <ydk.models.cisco_ios_xe.CISCO_NTP_MIB.CiscoNtpMib.Cntpsystem>`
    
    

    """

    _prefix = 'CISCO-NTP-MIB'
    _revision = '2006-07-31'

    def __init__(self):
        super(CiscoNtpMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-NTP-MIB"
        self.yang_parent_name = "CISCO-NTP-MIB"

        self.cntpfilterregistertable = CiscoNtpMib.Cntpfilterregistertable()
        self.cntpfilterregistertable.parent = self
        self._children_name_map["cntpfilterregistertable"] = "cntpFilterRegisterTable"
        self._children_yang_names.add("cntpFilterRegisterTable")

        self.cntppeersvartable = CiscoNtpMib.Cntppeersvartable()
        self.cntppeersvartable.parent = self
        self._children_name_map["cntppeersvartable"] = "cntpPeersVarTable"
        self._children_yang_names.add("cntpPeersVarTable")

        self.cntpsystem = CiscoNtpMib.Cntpsystem()
        self.cntpsystem.parent = self
        self._children_name_map["cntpsystem"] = "cntpSystem"
        self._children_yang_names.add("cntpSystem")


    class Cntpsystem(Entity):
        """
        
        
        .. attribute:: cntpsysclock
        
        	The current local time.  Local time is derived from the hardware clock of the particular machine and increments at intervals depending on the design used
        	**type**\:  str
        
        	**length:** 8
        
        .. attribute:: cntpsysleap
        
        	Two\-bit code warning of an impending leap second to be inserted in the NTP timescale. This object can be set only when the cntpSysStratum has a value of 1
        	**type**\:   :py:class:`Ntpleapindicator <ydk.models.cisco_ios_xe.CISCO_NTP_MIB.Ntpleapindicator>`
        
        .. attribute:: cntpsyspeer
        
        	The current synchronization source.  This will contain the unique association identifier cntpPeersAssocId of the corresponding peer entry in the cntpPeersVarTable of the peer acting as the synchronization source.  If there is no peer, the value will be 0
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: cntpsyspoll
        
        	The interval at which the NTP server polls other NTP servers to synchronize its clock
        	**type**\:  int
        
        	**range:** \-20..20
        
        .. attribute:: cntpsysprecision
        
        	Signed integer indicating the precision of the system clock, in seconds to the nearest power of two.  The value must be rounded to the next larger power of two; for instance, a 50\-Hz (20 ms) or 60\-Hz (16.67 ms) power\-frequency clock would be assigned the value \-5 (31.25 ms), while a 1000\-Hz (1 ms) crystal\-controlled clock would be assigned the value \-9 (1.95 ms)
        	**type**\:  int
        
        	**range:** \-20..20
        
        .. attribute:: cntpsysrefid
        
        	The reference identifier of the local clock
        	**type**\:  str
        
        	**length:** 4
        
        .. attribute:: cntpsysreftime
        
        	The local time when the local clock was last updated.  If the local clock has never been synchronized, the value is zero
        	**type**\:  str
        
        	**length:** 8
        
        .. attribute:: cntpsysrootdelay
        
        	A signed fixed\-point number indicating the total round\-trip delay in seconds, to the primary reference source at the root of the synchronization subnet
        	**type**\:  str
        
        	**length:** 4
        
        	**units**\: seconds
        
        .. attribute:: cntpsysrootdispersion
        
        	The maximum error in seconds, relative to the primary reference source at the root of the synchronization subnet.  Only positive values greater than zero are possible
        	**type**\:  str
        
        	**length:** 4
        
        	**units**\: seconds
        
        .. attribute:: cntpsyssrvstatus
        
        	Current state of the NTP server with values coded as follows\: 1\: server status is unknown 2\: server is not running 3\: server is not synchronized to any time source 4\: server is synchronized to its own local clock 5\: server is synchronized to a local hardware refclock (e.g. GPS) 6\: server is synchronized to a remote NTP server
        	**type**\:   :py:class:`Cntpsyssrvstatus <ydk.models.cisco_ios_xe.CISCO_NTP_MIB.CiscoNtpMib.Cntpsystem.Cntpsyssrvstatus>`
        
        .. attribute:: cntpsysstratum
        
        	The stratum of the local clock. If the value is set to 1, i.e., this is a primary reference, then the Primary\-Clock procedure described in Section 3.4.6, in RFC\-1305 is invoked
        	**type**\:  int
        
        	**range:** 0..255
        
        

        """

        _prefix = 'CISCO-NTP-MIB'
        _revision = '2006-07-31'

        def __init__(self):
            super(CiscoNtpMib.Cntpsystem, self).__init__()

            self.yang_name = "cntpSystem"
            self.yang_parent_name = "CISCO-NTP-MIB"

            self.cntpsysclock = YLeaf(YType.str, "cntpSysClock")

            self.cntpsysleap = YLeaf(YType.enumeration, "cntpSysLeap")

            self.cntpsyspeer = YLeaf(YType.int32, "cntpSysPeer")

            self.cntpsyspoll = YLeaf(YType.int32, "cntpSysPoll")

            self.cntpsysprecision = YLeaf(YType.int32, "cntpSysPrecision")

            self.cntpsysrefid = YLeaf(YType.str, "cntpSysRefId")

            self.cntpsysreftime = YLeaf(YType.str, "cntpSysRefTime")

            self.cntpsysrootdelay = YLeaf(YType.str, "cntpSysRootDelay")

            self.cntpsysrootdispersion = YLeaf(YType.str, "cntpSysRootDispersion")

            self.cntpsyssrvstatus = YLeaf(YType.enumeration, "cntpSysSrvStatus")

            self.cntpsysstratum = YLeaf(YType.int32, "cntpSysStratum")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cntpsysclock",
                            "cntpsysleap",
                            "cntpsyspeer",
                            "cntpsyspoll",
                            "cntpsysprecision",
                            "cntpsysrefid",
                            "cntpsysreftime",
                            "cntpsysrootdelay",
                            "cntpsysrootdispersion",
                            "cntpsyssrvstatus",
                            "cntpsysstratum") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoNtpMib.Cntpsystem, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoNtpMib.Cntpsystem, self).__setattr__(name, value)

        class Cntpsyssrvstatus(Enum):
            """
            Cntpsyssrvstatus

            Current state of the NTP server with values coded as follows\:

            1\: server status is unknown

            2\: server is not running

            3\: server is not synchronized to any time source

            4\: server is synchronized to its own local clock

            5\: server is synchronized to a local hardware refclock (e.g. GPS)

            6\: server is synchronized to a remote NTP server

            .. data:: unknown = 1

            .. data:: notRunning = 2

            .. data:: notSynchronized = 3

            .. data:: syncToLocal = 4

            .. data:: syncToRefclock = 5

            .. data:: syncToRemoteServer = 6

            """

            unknown = Enum.YLeaf(1, "unknown")

            notRunning = Enum.YLeaf(2, "notRunning")

            notSynchronized = Enum.YLeaf(3, "notSynchronized")

            syncToLocal = Enum.YLeaf(4, "syncToLocal")

            syncToRefclock = Enum.YLeaf(5, "syncToRefclock")

            syncToRemoteServer = Enum.YLeaf(6, "syncToRemoteServer")


        def has_data(self):
            return (
                self.cntpsysclock.is_set or
                self.cntpsysleap.is_set or
                self.cntpsyspeer.is_set or
                self.cntpsyspoll.is_set or
                self.cntpsysprecision.is_set or
                self.cntpsysrefid.is_set or
                self.cntpsysreftime.is_set or
                self.cntpsysrootdelay.is_set or
                self.cntpsysrootdispersion.is_set or
                self.cntpsyssrvstatus.is_set or
                self.cntpsysstratum.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cntpsysclock.yfilter != YFilter.not_set or
                self.cntpsysleap.yfilter != YFilter.not_set or
                self.cntpsyspeer.yfilter != YFilter.not_set or
                self.cntpsyspoll.yfilter != YFilter.not_set or
                self.cntpsysprecision.yfilter != YFilter.not_set or
                self.cntpsysrefid.yfilter != YFilter.not_set or
                self.cntpsysreftime.yfilter != YFilter.not_set or
                self.cntpsysrootdelay.yfilter != YFilter.not_set or
                self.cntpsysrootdispersion.yfilter != YFilter.not_set or
                self.cntpsyssrvstatus.yfilter != YFilter.not_set or
                self.cntpsysstratum.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cntpSystem" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-NTP-MIB:CISCO-NTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cntpsysclock.is_set or self.cntpsysclock.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cntpsysclock.get_name_leafdata())
            if (self.cntpsysleap.is_set or self.cntpsysleap.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cntpsysleap.get_name_leafdata())
            if (self.cntpsyspeer.is_set or self.cntpsyspeer.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cntpsyspeer.get_name_leafdata())
            if (self.cntpsyspoll.is_set or self.cntpsyspoll.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cntpsyspoll.get_name_leafdata())
            if (self.cntpsysprecision.is_set or self.cntpsysprecision.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cntpsysprecision.get_name_leafdata())
            if (self.cntpsysrefid.is_set or self.cntpsysrefid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cntpsysrefid.get_name_leafdata())
            if (self.cntpsysreftime.is_set or self.cntpsysreftime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cntpsysreftime.get_name_leafdata())
            if (self.cntpsysrootdelay.is_set or self.cntpsysrootdelay.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cntpsysrootdelay.get_name_leafdata())
            if (self.cntpsysrootdispersion.is_set or self.cntpsysrootdispersion.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cntpsysrootdispersion.get_name_leafdata())
            if (self.cntpsyssrvstatus.is_set or self.cntpsyssrvstatus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cntpsyssrvstatus.get_name_leafdata())
            if (self.cntpsysstratum.is_set or self.cntpsysstratum.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cntpsysstratum.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cntpSysClock" or name == "cntpSysLeap" or name == "cntpSysPeer" or name == "cntpSysPoll" or name == "cntpSysPrecision" or name == "cntpSysRefId" or name == "cntpSysRefTime" or name == "cntpSysRootDelay" or name == "cntpSysRootDispersion" or name == "cntpSysSrvStatus" or name == "cntpSysStratum"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cntpSysClock"):
                self.cntpsysclock = value
                self.cntpsysclock.value_namespace = name_space
                self.cntpsysclock.value_namespace_prefix = name_space_prefix
            if(value_path == "cntpSysLeap"):
                self.cntpsysleap = value
                self.cntpsysleap.value_namespace = name_space
                self.cntpsysleap.value_namespace_prefix = name_space_prefix
            if(value_path == "cntpSysPeer"):
                self.cntpsyspeer = value
                self.cntpsyspeer.value_namespace = name_space
                self.cntpsyspeer.value_namespace_prefix = name_space_prefix
            if(value_path == "cntpSysPoll"):
                self.cntpsyspoll = value
                self.cntpsyspoll.value_namespace = name_space
                self.cntpsyspoll.value_namespace_prefix = name_space_prefix
            if(value_path == "cntpSysPrecision"):
                self.cntpsysprecision = value
                self.cntpsysprecision.value_namespace = name_space
                self.cntpsysprecision.value_namespace_prefix = name_space_prefix
            if(value_path == "cntpSysRefId"):
                self.cntpsysrefid = value
                self.cntpsysrefid.value_namespace = name_space
                self.cntpsysrefid.value_namespace_prefix = name_space_prefix
            if(value_path == "cntpSysRefTime"):
                self.cntpsysreftime = value
                self.cntpsysreftime.value_namespace = name_space
                self.cntpsysreftime.value_namespace_prefix = name_space_prefix
            if(value_path == "cntpSysRootDelay"):
                self.cntpsysrootdelay = value
                self.cntpsysrootdelay.value_namespace = name_space
                self.cntpsysrootdelay.value_namespace_prefix = name_space_prefix
            if(value_path == "cntpSysRootDispersion"):
                self.cntpsysrootdispersion = value
                self.cntpsysrootdispersion.value_namespace = name_space
                self.cntpsysrootdispersion.value_namespace_prefix = name_space_prefix
            if(value_path == "cntpSysSrvStatus"):
                self.cntpsyssrvstatus = value
                self.cntpsyssrvstatus.value_namespace = name_space
                self.cntpsyssrvstatus.value_namespace_prefix = name_space_prefix
            if(value_path == "cntpSysStratum"):
                self.cntpsysstratum = value
                self.cntpsysstratum.value_namespace = name_space
                self.cntpsysstratum.value_namespace_prefix = name_space_prefix


    class Cntppeersvartable(Entity):
        """
        This table provides information on the peers with
        which the local NTP server has associations.  The
        peers are also NTP servers but running on different
        hosts.
        
        .. attribute:: cntppeersvarentry
        
        	Each peers' entry provides NTP information retrieved from a particular peer NTP server.  Each peer is identified by a unique association identifier.  Entries are automatically created when the user configures the NTP server to be associated with remote peers.  Similarly entries are deleted when the user removes the peer association from the NTP server.  Entries can also be created by the management station by setting values for the following objects\: cntpPeersPeerAddress or cntpPeersPeerName,  cntpPeersHostAddress and cntpPeersMode and making the cntpPeersEntryStatus as active(1).  At the least, the management station has to set a value for cntpPeersPeerAddress or cntpPeersPeerName to make the row active
        	**type**\: list of    :py:class:`Cntppeersvarentry <ydk.models.cisco_ios_xe.CISCO_NTP_MIB.CiscoNtpMib.Cntppeersvartable.Cntppeersvarentry>`
        
        

        """

        _prefix = 'CISCO-NTP-MIB'
        _revision = '2006-07-31'

        def __init__(self):
            super(CiscoNtpMib.Cntppeersvartable, self).__init__()

            self.yang_name = "cntpPeersVarTable"
            self.yang_parent_name = "CISCO-NTP-MIB"

            self.cntppeersvarentry = YList(self)

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
                        super(CiscoNtpMib.Cntppeersvartable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoNtpMib.Cntppeersvartable, self).__setattr__(name, value)


        class Cntppeersvarentry(Entity):
            """
            Each peers' entry provides NTP information retrieved
            from a particular peer NTP server.  Each peer is
            identified by a unique association identifier.
            
            Entries are automatically created when the user
            configures the NTP server to be associated with remote
            peers.  Similarly entries are deleted when the user
            removes the peer association from the NTP server.
            
            Entries can also be created by the management station
            by setting values for the following objects\:
            cntpPeersPeerAddress or cntpPeersPeerName, 
            cntpPeersHostAddress and
            cntpPeersMode and making the cntpPeersEntryStatus as
            active(1).  At the least, the management station has
            to set a value for cntpPeersPeerAddress or
            cntpPeersPeerName to make the row active.
            
            .. attribute:: cntppeersassocid  <key>
            
            	An integer value greater than 0 that uniquely identifies a peer with which the local NTP server is associated
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cntppeersconfigured
            
            	This is a bit indicating that the association was created from configuration information and should not be de\-associated even if the peer becomes unreachable
            	**type**\:  bool
            
            .. attribute:: cntppeersdelay
            
            	The estimated round\-trip delay of the peer clock relative to the local clock over the network path between them, in seconds.  The host determines the value of this object using the NTP clock\-filter algorithm
            	**type**\:  str
            
            	**length:** 4
            
            	**units**\: seconds
            
            .. attribute:: cntppeersdispersion
            
            	The estimated maximum error of the peer clock relative to the local clock over the network path between them, in seconds.  The host determines the value of this object using the NTP clock\-filter algorithm
            	**type**\:  str
            
            	**length:** 4
            
            	**units**\: seconds
            
            .. attribute:: cntppeersentrystatus
            
            	The status object for this row. When a management station is creating a new row, it should set the value for cntpPeersPeerAddress at least, before the row can be made active(1)
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cntppeersfiltervalidentries
            
            	The number of valid entries for a peer in the Filter Register Table. Since, the Filter Register Table is optional, this object will have a value 0 if the Filter Register Table is not implemented
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cntppeershostaddress
            
            	The IP address of the local host.  Multi\-homing can be supported using this object
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cntppeershostpoll
            
            	The interval at which the local host polls the peer
            	**type**\:  int
            
            	**range:** \-20..20
            
            .. attribute:: cntppeershostport
            
            	The UDP port number on which the local host receives NTP messages
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: cntppeersleap
            
            	Two\-bit code warning of an impending leap second to be inserted in the NTP timescale of the peer
            	**type**\:   :py:class:`Ntpleapindicator <ydk.models.cisco_ios_xe.CISCO_NTP_MIB.Ntpleapindicator>`
            
            .. attribute:: cntppeersmode
            
            	The association mode of the NTP server, with values coded as follows, 0, unspecified 1, symmetric active \- A host operating in this mode         sends periodic messages regardless of the         reachability state or stratum of its peer.  By         operating in this mode the host announces its         willingness to synchronize and be synchronized         by the peer 2, symmetric passive \- This type of association is         ordinarily created upon arrival of a message         from a peer operating in the symmetric active         mode and persists only as long as the peer is         reachable and operating at a stratum level         less than or equal to the host; otherwise, the         association is dissolved.  However, the         association will always persist until at least         one message has been sent in reply.  By         operating in this mode the host announces its         willingness to synchronize and be synchronized         by the peer 3, client \-  A host operating in this mode sends         periodic messages regardless of the         reachability state or stratum of its peer.  By         operating in this mode the host, usually a LAN         workstation, announces its willingness to be         synchronized by, but not to synchronize the peer 4, server \- This type of association is ordinarily         created upon arrival of a client request message         and exists only in order to reply to that         request, after which the association is         dissolved.  By operating in this mode the host,         usually a LAN time server, announces its         willingness to synchronize, but not to be         synchronized by the peer 5, broadcast \- A host operating in this mode sends         periodic messages regardless of the         reachability state or stratum of the peers.         By operating in this mode the host, usually a         LAN time server operating on a high\-speed         broadcast medium, announces its willingness to         synchronize all of the peers, but not to be         synchronized by any of them 6, reserved for NTP control messages 7, reserved for private use.  When creating a new peer association, if no value is specified for this object, it defaults to symmetricActive(1)
            	**type**\:   :py:class:`Cntppeersmode <ydk.models.cisco_ios_xe.CISCO_NTP_MIB.CiscoNtpMib.Cntppeersvartable.Cntppeersvarentry.Cntppeersmode>`
            
            .. attribute:: cntppeersoffset
            
            	The estimated offset of the peer clock relative to the local clock, in seconds.  The host determines the value of this object using the NTP clock\-filter algorithm
            	**type**\:  str
            
            	**length:** 4
            
            	**units**\: seconds
            
            .. attribute:: cntppeersorgtime
            
            	The local time at the peer, when its latest NTP message was sent.  If the peer becomes unreachable the value is set to zero
            	**type**\:  str
            
            	**length:** 8
            
            .. attribute:: cntppeerspeeraddress
            
            	The IP address of the peer.  When creating a new association, a value should be set either for this object or the corresponding instance of  cntpPeersPeerName, before the row is made active
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cntppeerspeername
            
            	The address of the peer. When creating a new association, a value must be set for either this object or the corresponding instance of cntpPeersPeerAddress object, before the row is made active
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cntppeerspeerpoll
            
            	The interval at which the peer polls the local host
            	**type**\:  int
            
            	**range:** \-20..20
            
            .. attribute:: cntppeerspeerport
            
            	The UDP port number on which the peer receives NTP messages
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: cntppeerspeertype
            
            	Represents the type of the corresponding instance of cntpPeersPeerName object
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cntppeersprecision
            
            	Signed integer indicating the precision of the peer clock, in seconds to the nearest power of two.  The value must be rounded to the next larger power of two; for instance, a 50\-Hz (20 ms) or 60\-Hz (16.67 ms) power\-frequency clock would be assigned the value \-5 (31.25 ms), while a 1000\-Hz (1 ms) crystal\-controlled clock would be assigned the value \-9 (1.95 ms)
            	**type**\:  int
            
            	**range:** \-20..20
            
            .. attribute:: cntppeersprefpeer
            
            	This object specifies whether this peer is the preferred one over the others. By default, when the value of this object is 'false', NTP chooses  the peer with which to synchronize the time on  the local system. If this object is set to 'true', NTP will choose the corresponding peer to synchronize the time with. If multiple entries have this object set to 'true', NTP will choose the first one to be set. This object is a means to override the selection of the peer by NTP
            	**type**\:  bool
            
            .. attribute:: cntppeersreach
            
            	A shift register of used to determine the reachability status of the peer, with bits entering from the least significant (rightmost) end.  A peer is considered reachable if at least one bit in this register is set to one i.e, if the value of this object is non\-zero. The data in the shift register would be populated by the NTP protocol procedures
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cntppeersreceivetime
            
            	The local time, when the latest NTP message from the peer arrived.  If the peer becomes unreachable the value is set to zero
            	**type**\:  str
            
            	**length:** 8
            
            .. attribute:: cntppeersrefid
            
            	The reference identifier of the peer
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: cntppeersreftime
            
            	The local time at the peer when its clock was last updated.  If the peer clock has never been synchronized, the value is zero
            	**type**\:  str
            
            	**length:** 8
            
            .. attribute:: cntppeersrootdelay
            
            	A signed fixed\-point number indicating the total round\-trip delay in seconds, from the peer to the primary reference source at the root of the synchronization subnet
            	**type**\:  str
            
            	**length:** 4
            
            	**units**\: seconds
            
            .. attribute:: cntppeersrootdispersion
            
            	The maximum error in seconds, of the peer clock relative to the primary reference source at the root of the synchronization subnet.  Only positive values greater than zero are possible
            	**type**\:  str
            
            	**length:** 4
            
            	**units**\: seconds
            
            .. attribute:: cntppeersstratum
            
            	The stratum of the peer clock
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cntppeerstimer
            
            	The interval in seconds, between transmitted NTP messages from the local host to the peer
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: cntppeerstransmittime
            
            	The local time at which the NTP message departed the sender
            	**type**\:  str
            
            	**length:** 8
            
            .. attribute:: cntppeersupdatetime
            
            	The local time, when the most recent NTP message was received from the peer that was used to calculate the skew dispersion.  This represents only the 32\-bit integer part of the NTPTimestamp
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: cntppeersupdatetimerev1
            
            	The local time, when the most recent NTP message was received from the peer that was used to calculate the skew dispersion.  This represents only the 32\-bit integer part of the NTPTimestamp
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-NTP-MIB'
            _revision = '2006-07-31'

            def __init__(self):
                super(CiscoNtpMib.Cntppeersvartable.Cntppeersvarentry, self).__init__()

                self.yang_name = "cntpPeersVarEntry"
                self.yang_parent_name = "cntpPeersVarTable"

                self.cntppeersassocid = YLeaf(YType.int32, "cntpPeersAssocId")

                self.cntppeersconfigured = YLeaf(YType.boolean, "cntpPeersConfigured")

                self.cntppeersdelay = YLeaf(YType.str, "cntpPeersDelay")

                self.cntppeersdispersion = YLeaf(YType.str, "cntpPeersDispersion")

                self.cntppeersentrystatus = YLeaf(YType.enumeration, "cntpPeersEntryStatus")

                self.cntppeersfiltervalidentries = YLeaf(YType.uint32, "cntpPeersFilterValidEntries")

                self.cntppeershostaddress = YLeaf(YType.str, "cntpPeersHostAddress")

                self.cntppeershostpoll = YLeaf(YType.int32, "cntpPeersHostPoll")

                self.cntppeershostport = YLeaf(YType.int32, "cntpPeersHostPort")

                self.cntppeersleap = YLeaf(YType.enumeration, "cntpPeersLeap")

                self.cntppeersmode = YLeaf(YType.enumeration, "cntpPeersMode")

                self.cntppeersoffset = YLeaf(YType.str, "cntpPeersOffset")

                self.cntppeersorgtime = YLeaf(YType.str, "cntpPeersOrgTime")

                self.cntppeerspeeraddress = YLeaf(YType.str, "cntpPeersPeerAddress")

                self.cntppeerspeername = YLeaf(YType.str, "cntpPeersPeerName")

                self.cntppeerspeerpoll = YLeaf(YType.int32, "cntpPeersPeerPoll")

                self.cntppeerspeerport = YLeaf(YType.int32, "cntpPeersPeerPort")

                self.cntppeerspeertype = YLeaf(YType.enumeration, "cntpPeersPeerType")

                self.cntppeersprecision = YLeaf(YType.int32, "cntpPeersPrecision")

                self.cntppeersprefpeer = YLeaf(YType.boolean, "cntpPeersPrefPeer")

                self.cntppeersreach = YLeaf(YType.int32, "cntpPeersReach")

                self.cntppeersreceivetime = YLeaf(YType.str, "cntpPeersReceiveTime")

                self.cntppeersrefid = YLeaf(YType.str, "cntpPeersRefId")

                self.cntppeersreftime = YLeaf(YType.str, "cntpPeersRefTime")

                self.cntppeersrootdelay = YLeaf(YType.str, "cntpPeersRootDelay")

                self.cntppeersrootdispersion = YLeaf(YType.str, "cntpPeersRootDispersion")

                self.cntppeersstratum = YLeaf(YType.int32, "cntpPeersStratum")

                self.cntppeerstimer = YLeaf(YType.int32, "cntpPeersTimer")

                self.cntppeerstransmittime = YLeaf(YType.str, "cntpPeersTransmitTime")

                self.cntppeersupdatetime = YLeaf(YType.int32, "cntpPeersUpdateTime")

                self.cntppeersupdatetimerev1 = YLeaf(YType.uint32, "cntpPeersUpdateTimeRev1")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cntppeersassocid",
                                "cntppeersconfigured",
                                "cntppeersdelay",
                                "cntppeersdispersion",
                                "cntppeersentrystatus",
                                "cntppeersfiltervalidentries",
                                "cntppeershostaddress",
                                "cntppeershostpoll",
                                "cntppeershostport",
                                "cntppeersleap",
                                "cntppeersmode",
                                "cntppeersoffset",
                                "cntppeersorgtime",
                                "cntppeerspeeraddress",
                                "cntppeerspeername",
                                "cntppeerspeerpoll",
                                "cntppeerspeerport",
                                "cntppeerspeertype",
                                "cntppeersprecision",
                                "cntppeersprefpeer",
                                "cntppeersreach",
                                "cntppeersreceivetime",
                                "cntppeersrefid",
                                "cntppeersreftime",
                                "cntppeersrootdelay",
                                "cntppeersrootdispersion",
                                "cntppeersstratum",
                                "cntppeerstimer",
                                "cntppeerstransmittime",
                                "cntppeersupdatetime",
                                "cntppeersupdatetimerev1") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoNtpMib.Cntppeersvartable.Cntppeersvarentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoNtpMib.Cntppeersvartable.Cntppeersvarentry, self).__setattr__(name, value)

            class Cntppeersmode(Enum):
                """
                Cntppeersmode

                The association mode of the NTP server, with values

                coded as follows,

                0, unspecified

                1, symmetric active \- A host operating in this mode

                        sends periodic messages regardless of the

                        reachability state or stratum of its peer.  By

                        operating in this mode the host announces its

                        willingness to synchronize and be synchronized

                        by the peer

                2, symmetric passive \- This type of association is

                        ordinarily created upon arrival of a message

                        from a peer operating in the symmetric active

                        mode and persists only as long as the peer is

                        reachable and operating at a stratum level

                        less than or equal to the host; otherwise, the

                        association is dissolved.  However, the

                        association will always persist until at least

                        one message has been sent in reply.  By

                        operating in this mode the host announces its

                        willingness to synchronize and be synchronized

                        by the peer

                3, client \-  A host operating in this mode sends

                        periodic messages regardless of the

                        reachability state or stratum of its peer.  By

                        operating in this mode the host, usually a LAN

                        workstation, announces its willingness to be

                        synchronized by, but not to synchronize the peer

                4, server \- This type of association is ordinarily

                        created upon arrival of a client request message

                        and exists only in order to reply to that

                        request, after which the association is

                        dissolved.  By operating in this mode the host,

                        usually a LAN time server, announces its

                        willingness to synchronize, but not to be

                        synchronized by the peer

                5, broadcast \- A host operating in this mode sends

                        periodic messages regardless of the

                        reachability state or stratum of the peers.

                        By operating in this mode the host, usually a

                        LAN time server operating on a high\-speed

                        broadcast medium, announces its willingness to

                        synchronize all of the peers, but not to be

                        synchronized by any of them

                6, reserved for NTP control messages

                7, reserved for private use.

                When creating a new peer association, if no value

                is specified for this object, it defaults to

                symmetricActive(1).

                .. data:: unspecified = 0

                .. data:: symmetricActive = 1

                .. data:: symmetricPassive = 2

                .. data:: client = 3

                .. data:: server = 4

                .. data:: broadcast = 5

                .. data:: reservedControl = 6

                .. data:: reservedPrivate = 7

                """

                unspecified = Enum.YLeaf(0, "unspecified")

                symmetricActive = Enum.YLeaf(1, "symmetricActive")

                symmetricPassive = Enum.YLeaf(2, "symmetricPassive")

                client = Enum.YLeaf(3, "client")

                server = Enum.YLeaf(4, "server")

                broadcast = Enum.YLeaf(5, "broadcast")

                reservedControl = Enum.YLeaf(6, "reservedControl")

                reservedPrivate = Enum.YLeaf(7, "reservedPrivate")


            def has_data(self):
                return (
                    self.cntppeersassocid.is_set or
                    self.cntppeersconfigured.is_set or
                    self.cntppeersdelay.is_set or
                    self.cntppeersdispersion.is_set or
                    self.cntppeersentrystatus.is_set or
                    self.cntppeersfiltervalidentries.is_set or
                    self.cntppeershostaddress.is_set or
                    self.cntppeershostpoll.is_set or
                    self.cntppeershostport.is_set or
                    self.cntppeersleap.is_set or
                    self.cntppeersmode.is_set or
                    self.cntppeersoffset.is_set or
                    self.cntppeersorgtime.is_set or
                    self.cntppeerspeeraddress.is_set or
                    self.cntppeerspeername.is_set or
                    self.cntppeerspeerpoll.is_set or
                    self.cntppeerspeerport.is_set or
                    self.cntppeerspeertype.is_set or
                    self.cntppeersprecision.is_set or
                    self.cntppeersprefpeer.is_set or
                    self.cntppeersreach.is_set or
                    self.cntppeersreceivetime.is_set or
                    self.cntppeersrefid.is_set or
                    self.cntppeersreftime.is_set or
                    self.cntppeersrootdelay.is_set or
                    self.cntppeersrootdispersion.is_set or
                    self.cntppeersstratum.is_set or
                    self.cntppeerstimer.is_set or
                    self.cntppeerstransmittime.is_set or
                    self.cntppeersupdatetime.is_set or
                    self.cntppeersupdatetimerev1.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cntppeersassocid.yfilter != YFilter.not_set or
                    self.cntppeersconfigured.yfilter != YFilter.not_set or
                    self.cntppeersdelay.yfilter != YFilter.not_set or
                    self.cntppeersdispersion.yfilter != YFilter.not_set or
                    self.cntppeersentrystatus.yfilter != YFilter.not_set or
                    self.cntppeersfiltervalidentries.yfilter != YFilter.not_set or
                    self.cntppeershostaddress.yfilter != YFilter.not_set or
                    self.cntppeershostpoll.yfilter != YFilter.not_set or
                    self.cntppeershostport.yfilter != YFilter.not_set or
                    self.cntppeersleap.yfilter != YFilter.not_set or
                    self.cntppeersmode.yfilter != YFilter.not_set or
                    self.cntppeersoffset.yfilter != YFilter.not_set or
                    self.cntppeersorgtime.yfilter != YFilter.not_set or
                    self.cntppeerspeeraddress.yfilter != YFilter.not_set or
                    self.cntppeerspeername.yfilter != YFilter.not_set or
                    self.cntppeerspeerpoll.yfilter != YFilter.not_set or
                    self.cntppeerspeerport.yfilter != YFilter.not_set or
                    self.cntppeerspeertype.yfilter != YFilter.not_set or
                    self.cntppeersprecision.yfilter != YFilter.not_set or
                    self.cntppeersprefpeer.yfilter != YFilter.not_set or
                    self.cntppeersreach.yfilter != YFilter.not_set or
                    self.cntppeersreceivetime.yfilter != YFilter.not_set or
                    self.cntppeersrefid.yfilter != YFilter.not_set or
                    self.cntppeersreftime.yfilter != YFilter.not_set or
                    self.cntppeersrootdelay.yfilter != YFilter.not_set or
                    self.cntppeersrootdispersion.yfilter != YFilter.not_set or
                    self.cntppeersstratum.yfilter != YFilter.not_set or
                    self.cntppeerstimer.yfilter != YFilter.not_set or
                    self.cntppeerstransmittime.yfilter != YFilter.not_set or
                    self.cntppeersupdatetime.yfilter != YFilter.not_set or
                    self.cntppeersupdatetimerev1.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cntpPeersVarEntry" + "[cntpPeersAssocId='" + self.cntppeersassocid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-NTP-MIB:CISCO-NTP-MIB/cntpPeersVarTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cntppeersassocid.is_set or self.cntppeersassocid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersassocid.get_name_leafdata())
                if (self.cntppeersconfigured.is_set or self.cntppeersconfigured.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersconfigured.get_name_leafdata())
                if (self.cntppeersdelay.is_set or self.cntppeersdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersdelay.get_name_leafdata())
                if (self.cntppeersdispersion.is_set or self.cntppeersdispersion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersdispersion.get_name_leafdata())
                if (self.cntppeersentrystatus.is_set or self.cntppeersentrystatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersentrystatus.get_name_leafdata())
                if (self.cntppeersfiltervalidentries.is_set or self.cntppeersfiltervalidentries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersfiltervalidentries.get_name_leafdata())
                if (self.cntppeershostaddress.is_set or self.cntppeershostaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeershostaddress.get_name_leafdata())
                if (self.cntppeershostpoll.is_set or self.cntppeershostpoll.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeershostpoll.get_name_leafdata())
                if (self.cntppeershostport.is_set or self.cntppeershostport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeershostport.get_name_leafdata())
                if (self.cntppeersleap.is_set or self.cntppeersleap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersleap.get_name_leafdata())
                if (self.cntppeersmode.is_set or self.cntppeersmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersmode.get_name_leafdata())
                if (self.cntppeersoffset.is_set or self.cntppeersoffset.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersoffset.get_name_leafdata())
                if (self.cntppeersorgtime.is_set or self.cntppeersorgtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersorgtime.get_name_leafdata())
                if (self.cntppeerspeeraddress.is_set or self.cntppeerspeeraddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeerspeeraddress.get_name_leafdata())
                if (self.cntppeerspeername.is_set or self.cntppeerspeername.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeerspeername.get_name_leafdata())
                if (self.cntppeerspeerpoll.is_set or self.cntppeerspeerpoll.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeerspeerpoll.get_name_leafdata())
                if (self.cntppeerspeerport.is_set or self.cntppeerspeerport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeerspeerport.get_name_leafdata())
                if (self.cntppeerspeertype.is_set or self.cntppeerspeertype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeerspeertype.get_name_leafdata())
                if (self.cntppeersprecision.is_set or self.cntppeersprecision.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersprecision.get_name_leafdata())
                if (self.cntppeersprefpeer.is_set or self.cntppeersprefpeer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersprefpeer.get_name_leafdata())
                if (self.cntppeersreach.is_set or self.cntppeersreach.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersreach.get_name_leafdata())
                if (self.cntppeersreceivetime.is_set or self.cntppeersreceivetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersreceivetime.get_name_leafdata())
                if (self.cntppeersrefid.is_set or self.cntppeersrefid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersrefid.get_name_leafdata())
                if (self.cntppeersreftime.is_set or self.cntppeersreftime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersreftime.get_name_leafdata())
                if (self.cntppeersrootdelay.is_set or self.cntppeersrootdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersrootdelay.get_name_leafdata())
                if (self.cntppeersrootdispersion.is_set or self.cntppeersrootdispersion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersrootdispersion.get_name_leafdata())
                if (self.cntppeersstratum.is_set or self.cntppeersstratum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersstratum.get_name_leafdata())
                if (self.cntppeerstimer.is_set or self.cntppeerstimer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeerstimer.get_name_leafdata())
                if (self.cntppeerstransmittime.is_set or self.cntppeerstransmittime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeerstransmittime.get_name_leafdata())
                if (self.cntppeersupdatetime.is_set or self.cntppeersupdatetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersupdatetime.get_name_leafdata())
                if (self.cntppeersupdatetimerev1.is_set or self.cntppeersupdatetimerev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersupdatetimerev1.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cntpPeersAssocId" or name == "cntpPeersConfigured" or name == "cntpPeersDelay" or name == "cntpPeersDispersion" or name == "cntpPeersEntryStatus" or name == "cntpPeersFilterValidEntries" or name == "cntpPeersHostAddress" or name == "cntpPeersHostPoll" or name == "cntpPeersHostPort" or name == "cntpPeersLeap" or name == "cntpPeersMode" or name == "cntpPeersOffset" or name == "cntpPeersOrgTime" or name == "cntpPeersPeerAddress" or name == "cntpPeersPeerName" or name == "cntpPeersPeerPoll" or name == "cntpPeersPeerPort" or name == "cntpPeersPeerType" or name == "cntpPeersPrecision" or name == "cntpPeersPrefPeer" or name == "cntpPeersReach" or name == "cntpPeersReceiveTime" or name == "cntpPeersRefId" or name == "cntpPeersRefTime" or name == "cntpPeersRootDelay" or name == "cntpPeersRootDispersion" or name == "cntpPeersStratum" or name == "cntpPeersTimer" or name == "cntpPeersTransmitTime" or name == "cntpPeersUpdateTime" or name == "cntpPeersUpdateTimeRev1"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cntpPeersAssocId"):
                    self.cntppeersassocid = value
                    self.cntppeersassocid.value_namespace = name_space
                    self.cntppeersassocid.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersConfigured"):
                    self.cntppeersconfigured = value
                    self.cntppeersconfigured.value_namespace = name_space
                    self.cntppeersconfigured.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersDelay"):
                    self.cntppeersdelay = value
                    self.cntppeersdelay.value_namespace = name_space
                    self.cntppeersdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersDispersion"):
                    self.cntppeersdispersion = value
                    self.cntppeersdispersion.value_namespace = name_space
                    self.cntppeersdispersion.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersEntryStatus"):
                    self.cntppeersentrystatus = value
                    self.cntppeersentrystatus.value_namespace = name_space
                    self.cntppeersentrystatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersFilterValidEntries"):
                    self.cntppeersfiltervalidentries = value
                    self.cntppeersfiltervalidentries.value_namespace = name_space
                    self.cntppeersfiltervalidentries.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersHostAddress"):
                    self.cntppeershostaddress = value
                    self.cntppeershostaddress.value_namespace = name_space
                    self.cntppeershostaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersHostPoll"):
                    self.cntppeershostpoll = value
                    self.cntppeershostpoll.value_namespace = name_space
                    self.cntppeershostpoll.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersHostPort"):
                    self.cntppeershostport = value
                    self.cntppeershostport.value_namespace = name_space
                    self.cntppeershostport.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersLeap"):
                    self.cntppeersleap = value
                    self.cntppeersleap.value_namespace = name_space
                    self.cntppeersleap.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersMode"):
                    self.cntppeersmode = value
                    self.cntppeersmode.value_namespace = name_space
                    self.cntppeersmode.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersOffset"):
                    self.cntppeersoffset = value
                    self.cntppeersoffset.value_namespace = name_space
                    self.cntppeersoffset.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersOrgTime"):
                    self.cntppeersorgtime = value
                    self.cntppeersorgtime.value_namespace = name_space
                    self.cntppeersorgtime.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersPeerAddress"):
                    self.cntppeerspeeraddress = value
                    self.cntppeerspeeraddress.value_namespace = name_space
                    self.cntppeerspeeraddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersPeerName"):
                    self.cntppeerspeername = value
                    self.cntppeerspeername.value_namespace = name_space
                    self.cntppeerspeername.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersPeerPoll"):
                    self.cntppeerspeerpoll = value
                    self.cntppeerspeerpoll.value_namespace = name_space
                    self.cntppeerspeerpoll.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersPeerPort"):
                    self.cntppeerspeerport = value
                    self.cntppeerspeerport.value_namespace = name_space
                    self.cntppeerspeerport.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersPeerType"):
                    self.cntppeerspeertype = value
                    self.cntppeerspeertype.value_namespace = name_space
                    self.cntppeerspeertype.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersPrecision"):
                    self.cntppeersprecision = value
                    self.cntppeersprecision.value_namespace = name_space
                    self.cntppeersprecision.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersPrefPeer"):
                    self.cntppeersprefpeer = value
                    self.cntppeersprefpeer.value_namespace = name_space
                    self.cntppeersprefpeer.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersReach"):
                    self.cntppeersreach = value
                    self.cntppeersreach.value_namespace = name_space
                    self.cntppeersreach.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersReceiveTime"):
                    self.cntppeersreceivetime = value
                    self.cntppeersreceivetime.value_namespace = name_space
                    self.cntppeersreceivetime.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersRefId"):
                    self.cntppeersrefid = value
                    self.cntppeersrefid.value_namespace = name_space
                    self.cntppeersrefid.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersRefTime"):
                    self.cntppeersreftime = value
                    self.cntppeersreftime.value_namespace = name_space
                    self.cntppeersreftime.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersRootDelay"):
                    self.cntppeersrootdelay = value
                    self.cntppeersrootdelay.value_namespace = name_space
                    self.cntppeersrootdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersRootDispersion"):
                    self.cntppeersrootdispersion = value
                    self.cntppeersrootdispersion.value_namespace = name_space
                    self.cntppeersrootdispersion.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersStratum"):
                    self.cntppeersstratum = value
                    self.cntppeersstratum.value_namespace = name_space
                    self.cntppeersstratum.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersTimer"):
                    self.cntppeerstimer = value
                    self.cntppeerstimer.value_namespace = name_space
                    self.cntppeerstimer.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersTransmitTime"):
                    self.cntppeerstransmittime = value
                    self.cntppeerstransmittime.value_namespace = name_space
                    self.cntppeerstransmittime.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersUpdateTime"):
                    self.cntppeersupdatetime = value
                    self.cntppeersupdatetime.value_namespace = name_space
                    self.cntppeersupdatetime.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpPeersUpdateTimeRev1"):
                    self.cntppeersupdatetimerev1 = value
                    self.cntppeersupdatetimerev1.value_namespace = name_space
                    self.cntppeersupdatetimerev1.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cntppeersvarentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cntppeersvarentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cntpPeersVarTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-NTP-MIB:CISCO-NTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cntpPeersVarEntry"):
                for c in self.cntppeersvarentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoNtpMib.Cntppeersvartable.Cntppeersvarentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cntppeersvarentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cntpPeersVarEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cntpfilterregistertable(Entity):
        """
        The following table contains NTP state variables
        used by the NTP clock filter and selection algorithms.
        This table depicts a shift register.  Each stage in
        the shift register is a 3\-tuple consisting of the
        measured clock offset, measured clock delay and
        measured clock dispersion associated with a single
        observation.
        
        An important factor affecting the accuracy and
        reliability of time distribution is the complex of
        algorithms used to reduce the effect of statistical
        errors and falsetickers due to failure of various
        subnet components, reference sources or propagation
        media.  The NTP clock\-filter and selection algorithms
        are designed to do exactly this.  The objects in the
        filter register table below are used by these
        algorthims to minimize the error in the calculated
        time.
        
        .. attribute:: cntpfilterregisterentry
        
        	Each entry corresponds to one stage of the shift register, i.e., one reading of the variables clock delay, clock offset and clock dispersion.  Entries are automatically created whenever a peer is configured and deleted when the peer is removed
        	**type**\: list of    :py:class:`Cntpfilterregisterentry <ydk.models.cisco_ios_xe.CISCO_NTP_MIB.CiscoNtpMib.Cntpfilterregistertable.Cntpfilterregisterentry>`
        
        

        """

        _prefix = 'CISCO-NTP-MIB'
        _revision = '2006-07-31'

        def __init__(self):
            super(CiscoNtpMib.Cntpfilterregistertable, self).__init__()

            self.yang_name = "cntpFilterRegisterTable"
            self.yang_parent_name = "CISCO-NTP-MIB"

            self.cntpfilterregisterentry = YList(self)

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
                        super(CiscoNtpMib.Cntpfilterregistertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoNtpMib.Cntpfilterregistertable, self).__setattr__(name, value)


        class Cntpfilterregisterentry(Entity):
            """
            Each entry corresponds to one stage of the shift
            register, i.e., one reading of the variables clock
            delay, clock offset and clock dispersion.
            
            Entries are automatically created whenever a peer is
            configured and deleted when the peer is removed.
            
            .. attribute:: cntppeersassocid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`cntppeersassocid <ydk.models.cisco_ios_xe.CISCO_NTP_MIB.CiscoNtpMib.Cntppeersvartable.Cntppeersvarentry>`
            
            .. attribute:: cntpfilterindex  <key>
            
            	An integer value in the specified range that is used to index into the table.  The size of the table is fixed at 8.  Each entry identifies a particular reading of the clock filter variables in the shift register.  Entries are added starting at index 1.  The index wraps back to 1 when it reaches 8.  When the index wraps back, the new entries will overwrite the old entries effectively deleting the old entry
            	**type**\:  int
            
            	**range:** 1..8
            
            .. attribute:: cntpfilterpeersdelay
            
            	Round\-trip delay of the peer clock relative to the local clock over the network path between them, in seconds.  This variable can take on both positive and negative values, depending on clock precision and skew\-error accumulation
            	**type**\:  str
            
            	**length:** 4
            
            	**units**\: seconds
            
            .. attribute:: cntpfilterpeersdispersion
            
            	The maximum error of the peer clock relative to the local clock over the network path between them, in seconds.  Only positive values greater than zero are possible
            	**type**\:  str
            
            	**length:** 4
            
            	**units**\: seconds
            
            .. attribute:: cntpfilterpeersoffset
            
            	The offset of the peer clock relative to the local clock in seconds
            	**type**\:  str
            
            	**length:** 4
            
            	**units**\: seconds
            
            

            """

            _prefix = 'CISCO-NTP-MIB'
            _revision = '2006-07-31'

            def __init__(self):
                super(CiscoNtpMib.Cntpfilterregistertable.Cntpfilterregisterentry, self).__init__()

                self.yang_name = "cntpFilterRegisterEntry"
                self.yang_parent_name = "cntpFilterRegisterTable"

                self.cntppeersassocid = YLeaf(YType.str, "cntpPeersAssocId")

                self.cntpfilterindex = YLeaf(YType.int32, "cntpFilterIndex")

                self.cntpfilterpeersdelay = YLeaf(YType.str, "cntpFilterPeersDelay")

                self.cntpfilterpeersdispersion = YLeaf(YType.str, "cntpFilterPeersDispersion")

                self.cntpfilterpeersoffset = YLeaf(YType.str, "cntpFilterPeersOffset")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cntppeersassocid",
                                "cntpfilterindex",
                                "cntpfilterpeersdelay",
                                "cntpfilterpeersdispersion",
                                "cntpfilterpeersoffset") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoNtpMib.Cntpfilterregistertable.Cntpfilterregisterentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoNtpMib.Cntpfilterregistertable.Cntpfilterregisterentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cntppeersassocid.is_set or
                    self.cntpfilterindex.is_set or
                    self.cntpfilterpeersdelay.is_set or
                    self.cntpfilterpeersdispersion.is_set or
                    self.cntpfilterpeersoffset.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cntppeersassocid.yfilter != YFilter.not_set or
                    self.cntpfilterindex.yfilter != YFilter.not_set or
                    self.cntpfilterpeersdelay.yfilter != YFilter.not_set or
                    self.cntpfilterpeersdispersion.yfilter != YFilter.not_set or
                    self.cntpfilterpeersoffset.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cntpFilterRegisterEntry" + "[cntpPeersAssocId='" + self.cntppeersassocid.get() + "']" + "[cntpFilterIndex='" + self.cntpfilterindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-NTP-MIB:CISCO-NTP-MIB/cntpFilterRegisterTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cntppeersassocid.is_set or self.cntppeersassocid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntppeersassocid.get_name_leafdata())
                if (self.cntpfilterindex.is_set or self.cntpfilterindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntpfilterindex.get_name_leafdata())
                if (self.cntpfilterpeersdelay.is_set or self.cntpfilterpeersdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntpfilterpeersdelay.get_name_leafdata())
                if (self.cntpfilterpeersdispersion.is_set or self.cntpfilterpeersdispersion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntpfilterpeersdispersion.get_name_leafdata())
                if (self.cntpfilterpeersoffset.is_set or self.cntpfilterpeersoffset.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cntpfilterpeersoffset.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cntpPeersAssocId" or name == "cntpFilterIndex" or name == "cntpFilterPeersDelay" or name == "cntpFilterPeersDispersion" or name == "cntpFilterPeersOffset"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cntpPeersAssocId"):
                    self.cntppeersassocid = value
                    self.cntppeersassocid.value_namespace = name_space
                    self.cntppeersassocid.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpFilterIndex"):
                    self.cntpfilterindex = value
                    self.cntpfilterindex.value_namespace = name_space
                    self.cntpfilterindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpFilterPeersDelay"):
                    self.cntpfilterpeersdelay = value
                    self.cntpfilterpeersdelay.value_namespace = name_space
                    self.cntpfilterpeersdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpFilterPeersDispersion"):
                    self.cntpfilterpeersdispersion = value
                    self.cntpfilterpeersdispersion.value_namespace = name_space
                    self.cntpfilterpeersdispersion.value_namespace_prefix = name_space_prefix
                if(value_path == "cntpFilterPeersOffset"):
                    self.cntpfilterpeersoffset = value
                    self.cntpfilterpeersoffset.value_namespace = name_space
                    self.cntpfilterpeersoffset.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cntpfilterregisterentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cntpfilterregisterentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cntpFilterRegisterTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-NTP-MIB:CISCO-NTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cntpFilterRegisterEntry"):
                for c in self.cntpfilterregisterentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoNtpMib.Cntpfilterregistertable.Cntpfilterregisterentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cntpfilterregisterentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cntpFilterRegisterEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cntpfilterregistertable is not None and self.cntpfilterregistertable.has_data()) or
            (self.cntppeersvartable is not None and self.cntppeersvartable.has_data()) or
            (self.cntpsystem is not None and self.cntpsystem.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cntpfilterregistertable is not None and self.cntpfilterregistertable.has_operation()) or
            (self.cntppeersvartable is not None and self.cntppeersvartable.has_operation()) or
            (self.cntpsystem is not None and self.cntpsystem.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-NTP-MIB:CISCO-NTP-MIB" + path_buffer

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

        if (child_yang_name == "cntpFilterRegisterTable"):
            if (self.cntpfilterregistertable is None):
                self.cntpfilterregistertable = CiscoNtpMib.Cntpfilterregistertable()
                self.cntpfilterregistertable.parent = self
                self._children_name_map["cntpfilterregistertable"] = "cntpFilterRegisterTable"
            return self.cntpfilterregistertable

        if (child_yang_name == "cntpPeersVarTable"):
            if (self.cntppeersvartable is None):
                self.cntppeersvartable = CiscoNtpMib.Cntppeersvartable()
                self.cntppeersvartable.parent = self
                self._children_name_map["cntppeersvartable"] = "cntpPeersVarTable"
            return self.cntppeersvartable

        if (child_yang_name == "cntpSystem"):
            if (self.cntpsystem is None):
                self.cntpsystem = CiscoNtpMib.Cntpsystem()
                self.cntpsystem.parent = self
                self._children_name_map["cntpsystem"] = "cntpSystem"
            return self.cntpsystem

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cntpFilterRegisterTable" or name == "cntpPeersVarTable" or name == "cntpSystem"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoNtpMib()
        return self._top_entity

