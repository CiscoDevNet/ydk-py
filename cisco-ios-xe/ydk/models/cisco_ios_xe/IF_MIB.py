""" IF_MIB 

The MIB module to describe generic objects for network
interface sub\-layers.  This MIB is an updated version of
MIB\-II's ifTable, and incorporates the extensions defined in
RFC 1229.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class IfMib(object):
    """
    
    
    .. attribute:: ifmibobjects
    
    	
    	**type**\:   :py:class:`Ifmibobjects <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Ifmibobjects>`
    
    .. attribute:: ifrcvaddresstable
    
    	This table contains an entry for each address (broadcast, multicast, or uni\-cast) for which the system will receive packets/frames on a particular interface, except as follows\:  \- for an interface operating in promiscuous mode, entries are only required for those addresses for which the system would receive frames were it not operating in promiscuous mode.  \- for 802.5 functional addresses, only one entry is required, for the address which has the functional address bit ANDed with the bit mask of all functional addresses for which the interface will accept frames.  A system is normally able to use any unicast address which corresponds to an entry in this table as a source address
    	**type**\:   :py:class:`Ifrcvaddresstable <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Ifrcvaddresstable>`
    
    .. attribute:: ifstacktable
    
    	The table containing information on the relationships between the multiple sub\-layers of network interfaces.  In particular, it contains information on which sub\-layers run 'on top of' which other sub\-layers, where each sub\-layer corresponds to a conceptual row in the ifTable.  For example, when the sub\-layer with ifIndex value x runs over the sub\-layer with ifIndex value y, then this table contains\:    ifStackStatus.x.y=active  For each ifIndex value, I, which identifies an active interface, there are always at least two instantiated rows in this table associated with I.  For one of these rows, I is the value of ifStackHigherLayer; for the other, I is the value of ifStackLowerLayer.  (If I is not involved in multiplexing, then these are the only two rows associated with I.)  For example, two rows exist even for an interface which has no others stacked on top or below it\:    ifStackStatus.0.x=active   ifStackStatus.x.0=active 
    	**type**\:   :py:class:`Ifstacktable <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Ifstacktable>`
    
    .. attribute:: iftable
    
    	A list of interface entries.  The number of entries is given by the value of ifNumber
    	**type**\:   :py:class:`Iftable <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable>`
    
    .. attribute:: interfaces
    
    	
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Interfaces>`
    
    

    """

    _prefix = 'IF-MIB'
    _revision = '2000-06-14'

    def __init__(self):
        self.ifmibobjects = IfMib.Ifmibobjects()
        self.ifmibobjects.parent = self
        self.ifrcvaddresstable = IfMib.Ifrcvaddresstable()
        self.ifrcvaddresstable.parent = self
        self.ifstacktable = IfMib.Ifstacktable()
        self.ifstacktable.parent = self
        self.iftable = IfMib.Iftable()
        self.iftable.parent = self
        self.interfaces = IfMib.Interfaces()
        self.interfaces.parent = self


    class Interfaces(object):
        """
        
        
        .. attribute:: ifnumber
        
        	The number of network interfaces (regardless of their current state) present on this system
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'IF-MIB'
        _revision = '2000-06-14'

        def __init__(self):
            self.parent = None
            self.ifnumber = None

        @property
        def _common_path(self):

            return '/IF-MIB:IF-MIB/IF-MIB:interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ifnumber is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IF_MIB as meta
            return meta._meta_table['IfMib.Interfaces']['meta_info']


    class Ifmibobjects(object):
        """
        
        
        .. attribute:: ifstacklastchange
        
        	The value of sysUpTime at the time of the last change of the (whole) interface stack.  A change of the interface stack is defined to be any creation, deletion, or change in value of any instance of ifStackStatus.  If the interface stack has been unchanged since the last re\-initialization of the local network management subsystem, then this object contains a zero value
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: iftablelastchange
        
        	The value of sysUpTime at the time of the last creation or deletion of an entry in the ifTable.  If the number of entries has been unchanged since the last re\-initialization of the local network management subsystem, then this object contains a zero value
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'IF-MIB'
        _revision = '2000-06-14'

        def __init__(self):
            self.parent = None
            self.ifstacklastchange = None
            self.iftablelastchange = None

        @property
        def _common_path(self):

            return '/IF-MIB:IF-MIB/IF-MIB:ifMIBObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ifstacklastchange is not None:
                return True

            if self.iftablelastchange is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IF_MIB as meta
            return meta._meta_table['IfMib.Ifmibobjects']['meta_info']


    class Iftable(object):
        """
        A list of interface entries.  The number of entries is
        given by the value of ifNumber.
        
        .. attribute:: ifentry
        
        	An entry containing management information applicable to a particular interface
        	**type**\: list of    :py:class:`Ifentry <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
        
        

        """

        _prefix = 'IF-MIB'
        _revision = '2000-06-14'

        def __init__(self):
            self.parent = None
            self.ifentry = YList()
            self.ifentry.parent = self
            self.ifentry.name = 'ifentry'


        class Ifentry(object):
            """
            An entry containing management information applicable to a
            particular interface.
            
            .. attribute:: ifindex  <key>
            
            	A unique value, greater than zero, for each interface.  It is recommended that values are assigned contiguously starting from 1.  The value for each interface sub\-layer must remain constant at least from one re\-initialization of the entity's network management system to the next re\- initialization
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ifadminstatus
            
            	The desired state of the interface.  The testing(3) state indicates that no operational packets can be passed.  When a managed system initializes, all interfaces start with ifAdminStatus in the down(2) state.  As a result of either explicit management action or per configuration information retained by the managed system, ifAdminStatus is then changed to either the up(1) or testing(3) states (or remains in the down(2) state)
            	**type**\:   :py:class:`IfadminstatusEnum <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry.IfadminstatusEnum>`
            
            .. attribute:: ifalias
            
            	This object is an 'alias' name for the interface as specified by a network manager, and provides a non\-volatile 'handle' for the interface.  On the first instantiation of an interface, the value of ifAlias associated with that interface is the zero\-length string.  As and when a value is written into an instance of ifAlias through a network management set operation, then the agent must retain the supplied value in the ifAlias instance associated with the same interface for as long as that interface remains instantiated, including across all re\- initializations/reboots of the network management system, including those which result in a change of the interface's ifIndex value.  An example of the value which a network manager might store in this object for a WAN interface is the (Telco's) circuit number/identifier of the interface.  Some agents may support write\-access only for interfaces having particular values of ifType.  An agent which supports write access to this object is required to keep the value in non\-volatile storage, but it may limit the length of new values depending on how much storage is already occupied by the current values for other interfaces
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: ifconnectorpresent
            
            	This object has the value 'true(1)' if the interface sublayer has a physical connector and the value 'false(2)' otherwise
            	**type**\:  bool
            
            .. attribute:: ifcounterdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this interface's counters suffered a discontinuity.  The relevant counters are the specific instances associated with this interface of any Counter32 or Counter64 object contained in the ifTable or ifXTable.  If no such discontinuities have occurred since the last re\- initialization of the local management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifdescr
            
            	A textual string containing information about the interface.  This string should include the name of the manufacturer, the product name and the version of the interface hardware/software
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ifhcinbroadcastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were addressed to a broadcast address at this sub\-layer.  This object is a 64\-bit version of ifInBroadcastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcinmulticastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were addressed to a multicast address at this sub\-layer.  For a MAC layer protocol, this includes both Group and Functional addresses.  This object is a 64\-bit version of ifInMulticastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcinoctets
            
            	The total number of octets received on the interface, including framing characters.  This object is a 64\-bit version of ifInOctets.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcinucastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were not addressed to a multicast or broadcast address at this sub\-layer.  This object is a 64\-bit version of ifInUcastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcoutbroadcastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were addressed to a broadcast address at this sub\-layer, including those that were discarded or not sent.  This object is a 64\-bit version of ifOutBroadcastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcoutmulticastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were addressed to a multicast address at this sub\-layer, including those that were discarded or not sent.  For a MAC layer protocol, this includes both Group and Functional addresses.  This object is a 64\-bit version of ifOutMulticastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcoutoctets
            
            	The total number of octets transmitted out of the interface, including framing characters.  This object is a 64\-bit version of ifOutOctets.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcoutucastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were not addressed to a multicast or broadcast address at this sub\-layer, including those that were discarded or not sent.  This object is a 64\-bit version of ifOutUcastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhighspeed
            
            	An estimate of the interface's current bandwidth in units of 1,000,000 bits per second.  If this object reports a value of `n' then the speed of the interface is somewhere in the range of `n\-500,000' to `n+499,999'.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth.  For a sub\-layer which has no concept of bandwidth, this object should be zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinbroadcastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were addressed to a broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifindiscards
            
            	The number of inbound packets which were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher\-layer protocol.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinerrors
            
            	For packet\-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher\-layer protocol.  For character\- oriented or fixed\-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher\-layer protocol.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinmulticastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were addressed to a multicast address at this sub\-layer.  For a MAC layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinnucastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were addressed to a multicast or broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.  This object is deprecated in favour of ifInMulticastPkts and ifInBroadcastPkts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ifinoctets
            
            	The total number of octets received on the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinucastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were not addressed to a multicast or broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinunknownprotos
            
            	For packet\-oriented interfaces, the number of packets received via the interface which were discarded because of an unknown or unsupported protocol.  For character\-oriented or fixed\-length interfaces that support protocol multiplexing the number of transmission units received via the interface which were discarded because of an unknown or unsupported protocol.  For any interface that does not support protocol multiplexing, this counter will always be 0.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: iflastchange
            
            	The value of sysUpTime at the time the interface entered its current operational state.  If the current state was entered prior to the last re\-initialization of the local network management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: iflinkupdowntrapenable
            
            	Indicates whether linkUp/linkDown traps should be generated for this interface.  By default, this object should have the value enabled(1) for interfaces which do not operate on 'top' of any other interface (as defined in the ifStackTable), and disabled(2) otherwise
            	**type**\:   :py:class:`IflinkupdowntrapenableEnum <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry.IflinkupdowntrapenableEnum>`
            
            .. attribute:: ifmtu
            
            	The size of the largest packet which can be sent/received on the interface, specified in octets.  For interfaces that are used for transmitting network datagrams, this is the size of the largest network datagram that can be sent on the interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ifname
            
            	The textual name of the interface.  The value of this object should be the name of the interface as assigned by the local device and should be suitable for use in commands entered at the device's `console'.  This might be a text name, such as `le0' or a simple port number, such as `1', depending on the interface naming syntax of the device.  If several entries in the ifTable together represent a single interface as named by the device, then each will have the same value of ifName.  Note that for an agent which responds to SNMP queries concerning an interface on some other (proxied) device, then the value of ifName for such an interface is the proxied device's local name for it.  If there is no local name, or this object is otherwise not applicable, then this object contains a zero\-length string
            	**type**\:  str
            
            .. attribute:: ifoperstatus
            
            	The current operational state of the interface.  The testing(3) state indicates that no operational packets can be passed.  If ifAdminStatus is down(2) then ifOperStatus should be down(2).  If ifAdminStatus is changed to up(1) then ifOperStatus should change to up(1) if the interface is ready to transmit and receive network traffic; it should change to dormant(5) if the interface is waiting for external actions (such as a serial line waiting for an incoming connection); it should remain in the down(2) state if and only if there is a fault that prevents it from going to the up(1) state; it should remain in the notPresent(6) state if the interface has missing (typically, hardware) components
            	**type**\:   :py:class:`IfoperstatusEnum <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry.IfoperstatusEnum>`
            
            .. attribute:: ifoutbroadcastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were addressed to a broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutdiscards
            
            	The number of outbound packets which were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifouterrors
            
            	For packet\-oriented interfaces, the number of outbound packets that could not be transmitted because of errors. For character\-oriented or fixed\-length interfaces, the number of outbound transmission units that could not be transmitted because of errors.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutmulticastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were addressed to a multicast address at this sub\-layer, including those that were discarded or not sent.  For a MAC layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutnucastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were addressed to a multicast or broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.  This object is deprecated in favour of ifOutMulticastPkts and ifOutBroadcastPkts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ifoutoctets
            
            	The total number of octets transmitted out of the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutqlen
            
            	The length of the output packet queue (in packets)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ifoutucastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were not addressed to a multicast or broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifphysaddress
            
            	The interface's address at its protocol sub\-layer.  For example, for an 802.x interface, this object normally contains a MAC address.  The interface's media\-specific MIB must define the bit and byte ordering and the format of the value of this object.  For interfaces which do not have such an address (e.g., a serial line), this object should contain an octet string of zero length
            	**type**\:  str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: ifpromiscuousmode
            
            	This object has a value of false(2) if this interface only accepts packets/frames that are addressed to this station. This object has a value of true(1) when the station accepts all packets/frames transmitted on the media.  The value true(1) is only legal on certain types of media.  If legal, setting this object to a value of true(1) may require the interface to be reset before becoming effective.  The value of ifPromiscuousMode does not affect the reception of broadcast and multicast packets/frames by the interface
            	**type**\:  bool
            
            .. attribute:: ifspecific
            
            	A reference to MIB definitions specific to the particular media being used to realize the interface.  It is recommended that this value point to an instance of a MIB object in the media\-specific MIB, i.e., that this object have the semantics associated with the InstancePointer textual convention defined in RFC 2579.  In fact, it is recommended that the media\-specific MIB specify what value ifSpecific should/can take for values of ifType.  If no MIB definitions specific to the particular media are available, the value should be set to the OBJECT IDENTIFIER { 0 0 }
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**status**\: deprecated
            
            .. attribute:: ifspeed
            
            	An estimate of the interface's current bandwidth in bits per second.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth.  If the bandwidth of the interface is greater than the maximum value reportable by this object then this object should report its maximum value (4,294,967,295) and ifHighSpeed must be used to report the interace's speed.  For a sub\-layer which has no concept of bandwidth, this object should be zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: iftestcode
            
            	This object contains a code which contains more specific information on the test result, for example an error\-code after a failed test.  Error codes and other values this object may take are specific to the type of interface and/or test.  The value may have the semantics of either the AutonomousType or InstancePointer textual conventions as defined in RFC 2579.  The identifier\:      testCodeUnknown  OBJECT IDENTIFIER \:\:= { 0 0 }  is defined for use if no additional result code is available
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**status**\: deprecated
            
            .. attribute:: iftestid
            
            	This object identifies the current invocation of the interface's test
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: iftestowner
            
            	The entity which currently has the 'ownership' required to invoke a test on this interface
            	**type**\:  str
            
            	**status**\: deprecated
            
            .. attribute:: iftestresult
            
            	This object contains the result of the most recently requested test, or the value none(1) if no tests have been requested since the last reset.  Note that this facility provides no provision for saving the results of one test when starting another, as could be required if used by multiple managers concurrently
            	**type**\:   :py:class:`IftestresultEnum <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry.IftestresultEnum>`
            
            	**status**\: deprecated
            
            .. attribute:: ifteststatus
            
            	This object indicates whether or not some manager currently has the necessary 'ownership' required to invoke a test on this interface.  A write to this object is only successful when it changes its value from 'notInUse(1)' to 'inUse(2)'. After completion of a test, the agent resets the value back to 'notInUse(1)'
            	**type**\:   :py:class:`IfteststatusEnum <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry.IfteststatusEnum>`
            
            	**status**\: deprecated
            
            .. attribute:: iftesttype
            
            	A control variable used to start and stop operator\- initiated interface tests.  Most OBJECT IDENTIFIER values assigned to tests are defined elsewhere, in association with specific types of interface.  However, this document assigns a value for a full\-duplex loopback test, and defines the special meanings of the subject identifier\:      noTest  OBJECT IDENTIFIER \:\:= { 0 0 }  When the value noTest is written to this object, no action is taken unless a test is in progress, in which case the test is aborted.  Writing any other value to this object is only valid when no test is currently in progress, in which case the indicated test is initiated.  When read, this object always returns the most recent value that ifTestType was set to.  If it has not been set since the last initialization of the network management subsystem on the agent, a value of noTest is returned
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**status**\: deprecated
            
            .. attribute:: iftype
            
            	The type of interface.  Additional values for ifType are assigned by the Internet Assigned Numbers Authority (IANA), through updating the syntax of the IANAifType textual convention
            	**type**\:   :py:class:`IanaiftypeEnum <ydk.models.cisco_ios_xe.IANAifType_MIB.IanaiftypeEnum>`
            
            

            """

            _prefix = 'IF-MIB'
            _revision = '2000-06-14'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.ifadminstatus = None
                self.ifalias = None
                self.ifconnectorpresent = None
                self.ifcounterdiscontinuitytime = None
                self.ifdescr = None
                self.ifhcinbroadcastpkts = None
                self.ifhcinmulticastpkts = None
                self.ifhcinoctets = None
                self.ifhcinucastpkts = None
                self.ifhcoutbroadcastpkts = None
                self.ifhcoutmulticastpkts = None
                self.ifhcoutoctets = None
                self.ifhcoutucastpkts = None
                self.ifhighspeed = None
                self.ifinbroadcastpkts = None
                self.ifindiscards = None
                self.ifinerrors = None
                self.ifinmulticastpkts = None
                self.ifinnucastpkts = None
                self.ifinoctets = None
                self.ifinucastpkts = None
                self.ifinunknownprotos = None
                self.iflastchange = None
                self.iflinkupdowntrapenable = None
                self.ifmtu = None
                self.ifname = None
                self.ifoperstatus = None
                self.ifoutbroadcastpkts = None
                self.ifoutdiscards = None
                self.ifouterrors = None
                self.ifoutmulticastpkts = None
                self.ifoutnucastpkts = None
                self.ifoutoctets = None
                self.ifoutqlen = None
                self.ifoutucastpkts = None
                self.ifphysaddress = None
                self.ifpromiscuousmode = None
                self.ifspecific = None
                self.ifspeed = None
                self.iftestcode = None
                self.iftestid = None
                self.iftestowner = None
                self.iftestresult = None
                self.ifteststatus = None
                self.iftesttype = None
                self.iftype = None

            class IfadminstatusEnum(Enum):
                """
                IfadminstatusEnum

                The desired state of the interface.  The testing(3) state

                indicates that no operational packets can be passed.  When a

                managed system initializes, all interfaces start with

                ifAdminStatus in the down(2) state.  As a result of either

                explicit management action or per configuration information

                retained by the managed system, ifAdminStatus is then

                changed to either the up(1) or testing(3) states (or remains

                in the down(2) state).

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                """

                up = 1

                down = 2

                testing = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IF_MIB as meta
                    return meta._meta_table['IfMib.Iftable.Ifentry.IfadminstatusEnum']


            class IflinkupdowntrapenableEnum(Enum):
                """
                IflinkupdowntrapenableEnum

                Indicates whether linkUp/linkDown traps should be generated

                for this interface.

                By default, this object should have the value enabled(1) for

                interfaces which do not operate on 'top' of any other

                interface (as defined in the ifStackTable), and disabled(2)

                otherwise.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = 1

                disabled = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IF_MIB as meta
                    return meta._meta_table['IfMib.Iftable.Ifentry.IflinkupdowntrapenableEnum']


            class IfoperstatusEnum(Enum):
                """
                IfoperstatusEnum

                The current operational state of the interface.  The

                testing(3) state indicates that no operational packets can

                be passed.  If ifAdminStatus is down(2) then ifOperStatus

                should be down(2).  If ifAdminStatus is changed to up(1)

                then ifOperStatus should change to up(1) if the interface is

                ready to transmit and receive network traffic; it should

                change to dormant(5) if the interface is waiting for

                external actions (such as a serial line waiting for an

                incoming connection); it should remain in the down(2) state

                if and only if there is a fault that prevents it from going

                to the up(1) state; it should remain in the notPresent(6)

                state if the interface has missing (typically, hardware)

                components.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                .. data:: unknown = 4

                .. data:: dormant = 5

                .. data:: notPresent = 6

                .. data:: lowerLayerDown = 7

                """

                up = 1

                down = 2

                testing = 3

                unknown = 4

                dormant = 5

                notPresent = 6

                lowerLayerDown = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IF_MIB as meta
                    return meta._meta_table['IfMib.Iftable.Ifentry.IfoperstatusEnum']


            class IftestresultEnum(Enum):
                """
                IftestresultEnum

                This object contains the result of the most recently

                requested test, or the value none(1) if no tests have been

                requested since the last reset.  Note that this facility

                provides no provision for saving the results of one test

                when starting another, as could be required if used by

                multiple managers concurrently.

                .. data:: none = 1

                .. data:: success = 2

                .. data:: inProgress = 3

                .. data:: notSupported = 4

                .. data:: unAbleToRun = 5

                .. data:: aborted = 6

                .. data:: failed = 7

                """

                none = 1

                success = 2

                inProgress = 3

                notSupported = 4

                unAbleToRun = 5

                aborted = 6

                failed = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IF_MIB as meta
                    return meta._meta_table['IfMib.Iftable.Ifentry.IftestresultEnum']


            class IfteststatusEnum(Enum):
                """
                IfteststatusEnum

                This object indicates whether or not some manager currently

                has the necessary 'ownership' required to invoke a test on

                this interface.  A write to this object is only successful

                when it changes its value from 'notInUse(1)' to 'inUse(2)'.

                After completion of a test, the agent resets the value back

                to 'notInUse(1)'.

                .. data:: notInUse = 1

                .. data:: inUse = 2

                """

                notInUse = 1

                inUse = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IF_MIB as meta
                    return meta._meta_table['IfMib.Iftable.Ifentry.IfteststatusEnum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/IF-MIB:IF-MIB/IF-MIB:ifTable/IF-MIB:ifEntry[IF-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.ifadminstatus is not None:
                    return True

                if self.ifalias is not None:
                    return True

                if self.ifconnectorpresent is not None:
                    return True

                if self.ifcounterdiscontinuitytime is not None:
                    return True

                if self.ifdescr is not None:
                    return True

                if self.ifhcinbroadcastpkts is not None:
                    return True

                if self.ifhcinmulticastpkts is not None:
                    return True

                if self.ifhcinoctets is not None:
                    return True

                if self.ifhcinucastpkts is not None:
                    return True

                if self.ifhcoutbroadcastpkts is not None:
                    return True

                if self.ifhcoutmulticastpkts is not None:
                    return True

                if self.ifhcoutoctets is not None:
                    return True

                if self.ifhcoutucastpkts is not None:
                    return True

                if self.ifhighspeed is not None:
                    return True

                if self.ifinbroadcastpkts is not None:
                    return True

                if self.ifindiscards is not None:
                    return True

                if self.ifinerrors is not None:
                    return True

                if self.ifinmulticastpkts is not None:
                    return True

                if self.ifinnucastpkts is not None:
                    return True

                if self.ifinoctets is not None:
                    return True

                if self.ifinucastpkts is not None:
                    return True

                if self.ifinunknownprotos is not None:
                    return True

                if self.iflastchange is not None:
                    return True

                if self.iflinkupdowntrapenable is not None:
                    return True

                if self.ifmtu is not None:
                    return True

                if self.ifname is not None:
                    return True

                if self.ifoperstatus is not None:
                    return True

                if self.ifoutbroadcastpkts is not None:
                    return True

                if self.ifoutdiscards is not None:
                    return True

                if self.ifouterrors is not None:
                    return True

                if self.ifoutmulticastpkts is not None:
                    return True

                if self.ifoutnucastpkts is not None:
                    return True

                if self.ifoutoctets is not None:
                    return True

                if self.ifoutqlen is not None:
                    return True

                if self.ifoutucastpkts is not None:
                    return True

                if self.ifphysaddress is not None:
                    return True

                if self.ifpromiscuousmode is not None:
                    return True

                if self.ifspecific is not None:
                    return True

                if self.ifspeed is not None:
                    return True

                if self.iftestcode is not None:
                    return True

                if self.iftestid is not None:
                    return True

                if self.iftestowner is not None:
                    return True

                if self.iftestresult is not None:
                    return True

                if self.ifteststatus is not None:
                    return True

                if self.iftesttype is not None:
                    return True

                if self.iftype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IF_MIB as meta
                return meta._meta_table['IfMib.Iftable.Ifentry']['meta_info']

        @property
        def _common_path(self):

            return '/IF-MIB:IF-MIB/IF-MIB:ifTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ifentry is not None:
                for child_ref in self.ifentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IF_MIB as meta
            return meta._meta_table['IfMib.Iftable']['meta_info']


    class Ifstacktable(object):
        """
        The table containing information on the relationships
        between the multiple sub\-layers of network interfaces.  In
        particular, it contains information on which sub\-layers run
        'on top of' which other sub\-layers, where each sub\-layer
        corresponds to a conceptual row in the ifTable.  For
        example, when the sub\-layer with ifIndex value x runs over
        the sub\-layer with ifIndex value y, then this table
        contains\:
        
          ifStackStatus.x.y=active
        
        For each ifIndex value, I, which identifies an active
        interface, there are always at least two instantiated rows
        in this table associated with I.  For one of these rows, I
        is the value of ifStackHigherLayer; for the other, I is the
        value of ifStackLowerLayer.  (If I is not involved in
        multiplexing, then these are the only two rows associated
        with I.)
        
        For example, two rows exist even for an interface which has
        no others stacked on top or below it\:
        
          ifStackStatus.0.x=active
          ifStackStatus.x.0=active 
        
        .. attribute:: ifstackentry
        
        	Information on a particular relationship between two sub\- layers, specifying that one sub\-layer runs on 'top' of the other sub\-layer.  Each sub\-layer corresponds to a conceptual row in the ifTable
        	**type**\: list of    :py:class:`Ifstackentry <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Ifstacktable.Ifstackentry>`
        
        

        """

        _prefix = 'IF-MIB'
        _revision = '2000-06-14'

        def __init__(self):
            self.parent = None
            self.ifstackentry = YList()
            self.ifstackentry.parent = self
            self.ifstackentry.name = 'ifstackentry'


        class Ifstackentry(object):
            """
            Information on a particular relationship between two sub\-
            layers, specifying that one sub\-layer runs on 'top' of the
            other sub\-layer.  Each sub\-layer corresponds to a conceptual
            row in the ifTable.
            
            .. attribute:: ifstackhigherlayer  <key>
            
            	The value of ifIndex corresponding to the higher sub\-layer of the relationship, i.e., the sub\-layer which runs on 'top' of the sub\-layer identified by the corresponding instance of ifStackLowerLayer.  If there is no higher sub\-layer (below the internetwork layer), then this object has the value 0
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ifstacklowerlayer  <key>
            
            	The value of ifIndex corresponding to the lower sub\-layer of the relationship, i.e., the sub\-layer which runs 'below' the sub\-layer identified by the corresponding instance of ifStackHigherLayer.  If there is no lower sub\-layer, then this object has the value 0
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ifstackstatus
            
            	The status of the relationship between two sub\-layers.  Changing the value of this object from 'active' to 'notInService' or 'destroy' will likely have consequences up and down the interface stack.  Thus, write access to this object is likely to be inappropriate for some types of interfaces, and many implementations will choose not to support write\-access for any type of interface
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'IF-MIB'
            _revision = '2000-06-14'

            def __init__(self):
                self.parent = None
                self.ifstackhigherlayer = None
                self.ifstacklowerlayer = None
                self.ifstackstatus = None

            @property
            def _common_path(self):
                if self.ifstackhigherlayer is None:
                    raise YPYModelError('Key property ifstackhigherlayer is None')
                if self.ifstacklowerlayer is None:
                    raise YPYModelError('Key property ifstacklowerlayer is None')

                return '/IF-MIB:IF-MIB/IF-MIB:ifStackTable/IF-MIB:ifStackEntry[IF-MIB:ifStackHigherLayer = ' + str(self.ifstackhigherlayer) + '][IF-MIB:ifStackLowerLayer = ' + str(self.ifstacklowerlayer) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifstackhigherlayer is not None:
                    return True

                if self.ifstacklowerlayer is not None:
                    return True

                if self.ifstackstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IF_MIB as meta
                return meta._meta_table['IfMib.Ifstacktable.Ifstackentry']['meta_info']

        @property
        def _common_path(self):

            return '/IF-MIB:IF-MIB/IF-MIB:ifStackTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ifstackentry is not None:
                for child_ref in self.ifstackentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IF_MIB as meta
            return meta._meta_table['IfMib.Ifstacktable']['meta_info']


    class Ifrcvaddresstable(object):
        """
        This table contains an entry for each address (broadcast,
        multicast, or uni\-cast) for which the system will receive
        packets/frames on a particular interface, except as follows\:
        
        \- for an interface operating in promiscuous mode, entries
        are only required for those addresses for which the system
        would receive frames were it not operating in promiscuous
        mode.
        
        \- for 802.5 functional addresses, only one entry is
        required, for the address which has the functional address
        bit ANDed with the bit mask of all functional addresses for
        which the interface will accept frames.
        
        A system is normally able to use any unicast address which
        corresponds to an entry in this table as a source address.
        
        .. attribute:: ifrcvaddressentry
        
        	A list of objects identifying an address for which the system will accept packets/frames on the particular interface identified by the index value ifIndex
        	**type**\: list of    :py:class:`Ifrcvaddressentry <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Ifrcvaddresstable.Ifrcvaddressentry>`
        
        

        """

        _prefix = 'IF-MIB'
        _revision = '2000-06-14'

        def __init__(self):
            self.parent = None
            self.ifrcvaddressentry = YList()
            self.ifrcvaddressentry.parent = self
            self.ifrcvaddressentry.name = 'ifrcvaddressentry'


        class Ifrcvaddressentry(object):
            """
            A list of objects identifying an address for which the
            system will accept packets/frames on the particular
            interface identified by the index value ifIndex.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: ifrcvaddressaddress  <key>
            
            	An address for which the system will accept packets/frames on this entry's interface
            	**type**\:  str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: ifrcvaddressstatus
            
            	This object is used to create and delete rows in the ifRcvAddressTable
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: ifrcvaddresstype
            
            	This object has the value nonVolatile(3) for those entries in the table which are valid and will not be deleted by the next restart of the managed system.  Entries having the value volatile(2) are valid and exist, but have not been saved, so that will not exist after the next restart of the managed system.  Entries having the value other(1) are valid and exist but are not classified as to whether they will continue to exist after the next restart
            	**type**\:   :py:class:`IfrcvaddresstypeEnum <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Ifrcvaddresstable.Ifrcvaddressentry.IfrcvaddresstypeEnum>`
            
            

            """

            _prefix = 'IF-MIB'
            _revision = '2000-06-14'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.ifrcvaddressaddress = None
                self.ifrcvaddressstatus = None
                self.ifrcvaddresstype = None

            class IfrcvaddresstypeEnum(Enum):
                """
                IfrcvaddresstypeEnum

                This object has the value nonVolatile(3) for those entries

                in the table which are valid and will not be deleted by the

                next restart of the managed system.  Entries having the

                value volatile(2) are valid and exist, but have not been

                saved, so that will not exist after the next restart of the

                managed system.  Entries having the value other(1) are valid

                and exist but are not classified as to whether they will

                continue to exist after the next restart.

                .. data:: other = 1

                .. data:: volatile = 2

                .. data:: nonVolatile = 3

                """

                other = 1

                volatile = 2

                nonVolatile = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IF_MIB as meta
                    return meta._meta_table['IfMib.Ifrcvaddresstable.Ifrcvaddressentry.IfrcvaddresstypeEnum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.ifrcvaddressaddress is None:
                    raise YPYModelError('Key property ifrcvaddressaddress is None')

                return '/IF-MIB:IF-MIB/IF-MIB:ifRcvAddressTable/IF-MIB:ifRcvAddressEntry[IF-MIB:ifIndex = ' + str(self.ifindex) + '][IF-MIB:ifRcvAddressAddress = ' + str(self.ifrcvaddressaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.ifrcvaddressaddress is not None:
                    return True

                if self.ifrcvaddressstatus is not None:
                    return True

                if self.ifrcvaddresstype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IF_MIB as meta
                return meta._meta_table['IfMib.Ifrcvaddresstable.Ifrcvaddressentry']['meta_info']

        @property
        def _common_path(self):

            return '/IF-MIB:IF-MIB/IF-MIB:ifRcvAddressTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ifrcvaddressentry is not None:
                for child_ref in self.ifrcvaddressentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IF_MIB as meta
            return meta._meta_table['IfMib.Ifrcvaddresstable']['meta_info']

    @property
    def _common_path(self):

        return '/IF-MIB:IF-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ifmibobjects is not None and self.ifmibobjects._has_data():
            return True

        if self.ifrcvaddresstable is not None and self.ifrcvaddresstable._has_data():
            return True

        if self.ifstacktable is not None and self.ifstacktable._has_data():
            return True

        if self.iftable is not None and self.iftable._has_data():
            return True

        if self.interfaces is not None and self.interfaces._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _IF_MIB as meta
        return meta._meta_table['IfMib']['meta_info']


