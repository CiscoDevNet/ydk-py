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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class NtpleapindicatorEnum(Enum):
    """
    NtpleapindicatorEnum

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

    noWarning = 0

    addSecond = 1

    subtractSecond = 2

    alarm = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_NTP_MIB as meta
        return meta._meta_table['NtpleapindicatorEnum']



class CiscoNtpMib(object):
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
        self.cntpfilterregistertable = CiscoNtpMib.Cntpfilterregistertable()
        self.cntpfilterregistertable.parent = self
        self.cntppeersvartable = CiscoNtpMib.Cntppeersvartable()
        self.cntppeersvartable.parent = self
        self.cntpsystem = CiscoNtpMib.Cntpsystem()
        self.cntpsystem.parent = self


    class Cntpsystem(object):
        """
        
        
        .. attribute:: cntpsysclock
        
        	The current local time.  Local time is derived from the hardware clock of the particular machine and increments at intervals depending on the design used
        	**type**\:  str
        
        	**length:** 8
        
        .. attribute:: cntpsysleap
        
        	Two\-bit code warning of an impending leap second to be inserted in the NTP timescale. This object can be set only when the cntpSysStratum has a value of 1
        	**type**\:   :py:class:`NtpleapindicatorEnum <ydk.models.cisco_ios_xe.CISCO_NTP_MIB.NtpleapindicatorEnum>`
        
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
        	**type**\:   :py:class:`CntpsyssrvstatusEnum <ydk.models.cisco_ios_xe.CISCO_NTP_MIB.CiscoNtpMib.Cntpsystem.CntpsyssrvstatusEnum>`
        
        .. attribute:: cntpsysstratum
        
        	The stratum of the local clock. If the value is set to 1, i.e., this is a primary reference, then the Primary\-Clock procedure described in Section 3.4.6, in RFC\-1305 is invoked
        	**type**\:  int
        
        	**range:** 0..255
        
        

        """

        _prefix = 'CISCO-NTP-MIB'
        _revision = '2006-07-31'

        def __init__(self):
            self.parent = None
            self.cntpsysclock = None
            self.cntpsysleap = None
            self.cntpsyspeer = None
            self.cntpsyspoll = None
            self.cntpsysprecision = None
            self.cntpsysrefid = None
            self.cntpsysreftime = None
            self.cntpsysrootdelay = None
            self.cntpsysrootdispersion = None
            self.cntpsyssrvstatus = None
            self.cntpsysstratum = None

        class CntpsyssrvstatusEnum(Enum):
            """
            CntpsyssrvstatusEnum

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

            unknown = 1

            notRunning = 2

            notSynchronized = 3

            syncToLocal = 4

            syncToRefclock = 5

            syncToRemoteServer = 6


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_NTP_MIB as meta
                return meta._meta_table['CiscoNtpMib.Cntpsystem.CntpsyssrvstatusEnum']


        @property
        def _common_path(self):

            return '/CISCO-NTP-MIB:CISCO-NTP-MIB/CISCO-NTP-MIB:cntpSystem'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cntpsysclock is not None:
                return True

            if self.cntpsysleap is not None:
                return True

            if self.cntpsyspeer is not None:
                return True

            if self.cntpsyspoll is not None:
                return True

            if self.cntpsysprecision is not None:
                return True

            if self.cntpsysrefid is not None:
                return True

            if self.cntpsysreftime is not None:
                return True

            if self.cntpsysrootdelay is not None:
                return True

            if self.cntpsysrootdispersion is not None:
                return True

            if self.cntpsyssrvstatus is not None:
                return True

            if self.cntpsysstratum is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_NTP_MIB as meta
            return meta._meta_table['CiscoNtpMib.Cntpsystem']['meta_info']


    class Cntppeersvartable(object):
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
            self.parent = None
            self.cntppeersvarentry = YList()
            self.cntppeersvarentry.parent = self
            self.cntppeersvarentry.name = 'cntppeersvarentry'


        class Cntppeersvarentry(object):
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
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
            	**type**\:   :py:class:`NtpleapindicatorEnum <ydk.models.cisco_ios_xe.CISCO_NTP_MIB.NtpleapindicatorEnum>`
            
            .. attribute:: cntppeersmode
            
            	The association mode of the NTP server, with values coded as follows, 0, unspecified 1, symmetric active \- A host operating in this mode         sends periodic messages regardless of the         reachability state or stratum of its peer.  By         operating in this mode the host announces its         willingness to synchronize and be synchronized         by the peer 2, symmetric passive \- This type of association is         ordinarily created upon arrival of a message         from a peer operating in the symmetric active         mode and persists only as long as the peer is         reachable and operating at a stratum level         less than or equal to the host; otherwise, the         association is dissolved.  However, the         association will always persist until at least         one message has been sent in reply.  By         operating in this mode the host announces its         willingness to synchronize and be synchronized         by the peer 3, client \-  A host operating in this mode sends         periodic messages regardless of the         reachability state or stratum of its peer.  By         operating in this mode the host, usually a LAN         workstation, announces its willingness to be         synchronized by, but not to synchronize the peer 4, server \- This type of association is ordinarily         created upon arrival of a client request message         and exists only in order to reply to that         request, after which the association is         dissolved.  By operating in this mode the host,         usually a LAN time server, announces its         willingness to synchronize, but not to be         synchronized by the peer 5, broadcast \- A host operating in this mode sends         periodic messages regardless of the         reachability state or stratum of the peers.         By operating in this mode the host, usually a         LAN time server operating on a high\-speed         broadcast medium, announces its willingness to         synchronize all of the peers, but not to be         synchronized by any of them 6, reserved for NTP control messages 7, reserved for private use.  When creating a new peer association, if no value is specified for this object, it defaults to symmetricActive(1)
            	**type**\:   :py:class:`CntppeersmodeEnum <ydk.models.cisco_ios_xe.CISCO_NTP_MIB.CiscoNtpMib.Cntppeersvartable.Cntppeersvarentry.CntppeersmodeEnum>`
            
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
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
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
                self.parent = None
                self.cntppeersassocid = None
                self.cntppeersconfigured = None
                self.cntppeersdelay = None
                self.cntppeersdispersion = None
                self.cntppeersentrystatus = None
                self.cntppeersfiltervalidentries = None
                self.cntppeershostaddress = None
                self.cntppeershostpoll = None
                self.cntppeershostport = None
                self.cntppeersleap = None
                self.cntppeersmode = None
                self.cntppeersoffset = None
                self.cntppeersorgtime = None
                self.cntppeerspeeraddress = None
                self.cntppeerspeername = None
                self.cntppeerspeerpoll = None
                self.cntppeerspeerport = None
                self.cntppeerspeertype = None
                self.cntppeersprecision = None
                self.cntppeersprefpeer = None
                self.cntppeersreach = None
                self.cntppeersreceivetime = None
                self.cntppeersrefid = None
                self.cntppeersreftime = None
                self.cntppeersrootdelay = None
                self.cntppeersrootdispersion = None
                self.cntppeersstratum = None
                self.cntppeerstimer = None
                self.cntppeerstransmittime = None
                self.cntppeersupdatetime = None
                self.cntppeersupdatetimerev1 = None

            class CntppeersmodeEnum(Enum):
                """
                CntppeersmodeEnum

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

                unspecified = 0

                symmetricActive = 1

                symmetricPassive = 2

                client = 3

                server = 4

                broadcast = 5

                reservedControl = 6

                reservedPrivate = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_NTP_MIB as meta
                    return meta._meta_table['CiscoNtpMib.Cntppeersvartable.Cntppeersvarentry.CntppeersmodeEnum']


            @property
            def _common_path(self):
                if self.cntppeersassocid is None:
                    raise YPYModelError('Key property cntppeersassocid is None')

                return '/CISCO-NTP-MIB:CISCO-NTP-MIB/CISCO-NTP-MIB:cntpPeersVarTable/CISCO-NTP-MIB:cntpPeersVarEntry[CISCO-NTP-MIB:cntpPeersAssocId = ' + str(self.cntppeersassocid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cntppeersassocid is not None:
                    return True

                if self.cntppeersconfigured is not None:
                    return True

                if self.cntppeersdelay is not None:
                    return True

                if self.cntppeersdispersion is not None:
                    return True

                if self.cntppeersentrystatus is not None:
                    return True

                if self.cntppeersfiltervalidentries is not None:
                    return True

                if self.cntppeershostaddress is not None:
                    return True

                if self.cntppeershostpoll is not None:
                    return True

                if self.cntppeershostport is not None:
                    return True

                if self.cntppeersleap is not None:
                    return True

                if self.cntppeersmode is not None:
                    return True

                if self.cntppeersoffset is not None:
                    return True

                if self.cntppeersorgtime is not None:
                    return True

                if self.cntppeerspeeraddress is not None:
                    return True

                if self.cntppeerspeername is not None:
                    return True

                if self.cntppeerspeerpoll is not None:
                    return True

                if self.cntppeerspeerport is not None:
                    return True

                if self.cntppeerspeertype is not None:
                    return True

                if self.cntppeersprecision is not None:
                    return True

                if self.cntppeersprefpeer is not None:
                    return True

                if self.cntppeersreach is not None:
                    return True

                if self.cntppeersreceivetime is not None:
                    return True

                if self.cntppeersrefid is not None:
                    return True

                if self.cntppeersreftime is not None:
                    return True

                if self.cntppeersrootdelay is not None:
                    return True

                if self.cntppeersrootdispersion is not None:
                    return True

                if self.cntppeersstratum is not None:
                    return True

                if self.cntppeerstimer is not None:
                    return True

                if self.cntppeerstransmittime is not None:
                    return True

                if self.cntppeersupdatetime is not None:
                    return True

                if self.cntppeersupdatetimerev1 is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_NTP_MIB as meta
                return meta._meta_table['CiscoNtpMib.Cntppeersvartable.Cntppeersvarentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NTP-MIB:CISCO-NTP-MIB/CISCO-NTP-MIB:cntpPeersVarTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cntppeersvarentry is not None:
                for child_ref in self.cntppeersvarentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_NTP_MIB as meta
            return meta._meta_table['CiscoNtpMib.Cntppeersvartable']['meta_info']


    class Cntpfilterregistertable(object):
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
            self.parent = None
            self.cntpfilterregisterentry = YList()
            self.cntpfilterregisterentry.parent = self
            self.cntpfilterregisterentry.name = 'cntpfilterregisterentry'


        class Cntpfilterregisterentry(object):
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
                self.parent = None
                self.cntppeersassocid = None
                self.cntpfilterindex = None
                self.cntpfilterpeersdelay = None
                self.cntpfilterpeersdispersion = None
                self.cntpfilterpeersoffset = None

            @property
            def _common_path(self):
                if self.cntppeersassocid is None:
                    raise YPYModelError('Key property cntppeersassocid is None')
                if self.cntpfilterindex is None:
                    raise YPYModelError('Key property cntpfilterindex is None')

                return '/CISCO-NTP-MIB:CISCO-NTP-MIB/CISCO-NTP-MIB:cntpFilterRegisterTable/CISCO-NTP-MIB:cntpFilterRegisterEntry[CISCO-NTP-MIB:cntpPeersAssocId = ' + str(self.cntppeersassocid) + '][CISCO-NTP-MIB:cntpFilterIndex = ' + str(self.cntpfilterindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cntppeersassocid is not None:
                    return True

                if self.cntpfilterindex is not None:
                    return True

                if self.cntpfilterpeersdelay is not None:
                    return True

                if self.cntpfilterpeersdispersion is not None:
                    return True

                if self.cntpfilterpeersoffset is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_NTP_MIB as meta
                return meta._meta_table['CiscoNtpMib.Cntpfilterregistertable.Cntpfilterregisterentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-NTP-MIB:CISCO-NTP-MIB/CISCO-NTP-MIB:cntpFilterRegisterTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cntpfilterregisterentry is not None:
                for child_ref in self.cntpfilterregisterentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_NTP_MIB as meta
            return meta._meta_table['CiscoNtpMib.Cntpfilterregistertable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-NTP-MIB:CISCO-NTP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cntpfilterregistertable is not None and self.cntpfilterregistertable._has_data():
            return True

        if self.cntppeersvartable is not None and self.cntppeersvartable._has_data():
            return True

        if self.cntpsystem is not None and self.cntpsystem._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_NTP_MIB as meta
        return meta._meta_table['CiscoNtpMib']['meta_info']


