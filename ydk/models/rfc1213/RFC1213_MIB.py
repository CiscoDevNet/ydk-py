""" RFC1213_MIB 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.ianaiftype.IANAifType_MIB import IANAifType_Enum


class RFC1213MIB(object):
    """
    
    
    .. attribute:: attable
    
    	The Address Translation tables contain the NetworkAddress to `physical' address equivalences. Some interfaces do not use translation tables for determining address equivalences (e.g., DDN\-X.25 has an algorithmic method); if all interfaces are of this type, then the Address Translation table is empty, i.e., has zero entries
    	**type**\: :py:class:`AtTable <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.AtTable>`
    
    .. attribute:: egp
    
    	
    	**type**\: :py:class:`Egp <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.Egp>`
    
    .. attribute:: egpneightable
    
    	The EGP neighbor table
    	**type**\: :py:class:`EgpNeighTable <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.EgpNeighTable>`
    
    .. attribute:: icmp
    
    	
    	**type**\: :py:class:`Icmp <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.Icmp>`
    
    .. attribute:: iftable
    
    	A list of interface entries.  The number of entries is given by the value of ifNumber
    	**type**\: :py:class:`IfTable <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.IfTable>`
    
    .. attribute:: interfaces
    
    	
    	**type**\: :py:class:`Interfaces <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.Interfaces>`
    
    .. attribute:: ip
    
    	
    	**type**\: :py:class:`Ip <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.Ip>`
    
    .. attribute:: ipaddrtable
    
    	The table of addressing information relevant to this entity's IP addresses
    	**type**\: :py:class:`IpAddrTable <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.IpAddrTable>`
    
    .. attribute:: ipnettomediatable
    
    	The IP Address Translation table used for mapping from IP addresses to physical addresses
    	**type**\: :py:class:`IpNetToMediaTable <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.IpNetToMediaTable>`
    
    .. attribute:: iproutetable
    
    	This entity's IP Routing table
    	**type**\: :py:class:`IpRouteTable <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.IpRouteTable>`
    
    .. attribute:: snmp
    
    	
    	**type**\: :py:class:`Snmp <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.Snmp>`
    
    .. attribute:: system
    
    	
    	**type**\: :py:class:`System <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.System>`
    
    .. attribute:: tcp
    
    	
    	**type**\: :py:class:`Tcp <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.Tcp>`
    
    .. attribute:: tcpconntable
    
    	A table containing TCP connection\-specific information
    	**type**\: :py:class:`TcpConnTable <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.TcpConnTable>`
    
    .. attribute:: udp
    
    	
    	**type**\: :py:class:`Udp <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.Udp>`
    
    .. attribute:: udptable
    
    	A table containing UDP listener information
    	**type**\: :py:class:`UdpTable <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.UdpTable>`
    
    

    """

    _prefix = 'rfc1213-mib'

    def __init__(self):
        self.attable = RFC1213MIB.AtTable()
        self.attable.parent = self
        self.egp = RFC1213MIB.Egp()
        self.egp.parent = self
        self.egpneightable = RFC1213MIB.EgpNeighTable()
        self.egpneightable.parent = self
        self.icmp = RFC1213MIB.Icmp()
        self.icmp.parent = self
        self.iftable = RFC1213MIB.IfTable()
        self.iftable.parent = self
        self.interfaces = RFC1213MIB.Interfaces()
        self.interfaces.parent = self
        self.ip = RFC1213MIB.Ip()
        self.ip.parent = self
        self.ipaddrtable = RFC1213MIB.IpAddrTable()
        self.ipaddrtable.parent = self
        self.ipnettomediatable = RFC1213MIB.IpNetToMediaTable()
        self.ipnettomediatable.parent = self
        self.iproutetable = RFC1213MIB.IpRouteTable()
        self.iproutetable.parent = self
        self.snmp = RFC1213MIB.Snmp()
        self.snmp.parent = self
        self.system = RFC1213MIB.System()
        self.system.parent = self
        self.tcp = RFC1213MIB.Tcp()
        self.tcp.parent = self
        self.tcpconntable = RFC1213MIB.TcpConnTable()
        self.tcpconntable.parent = self
        self.udp = RFC1213MIB.Udp()
        self.udp.parent = self
        self.udptable = RFC1213MIB.UdpTable()
        self.udptable.parent = self


    class AtTable(object):
        """
        The Address Translation tables contain the
        NetworkAddress to `physical' address equivalences.
        Some interfaces do not use translation tables for
        determining address equivalences (e.g., DDN\-X.25
        has an algorithmic method); if all interfaces are
        of this type, then the Address Translation table
        is empty, i.e., has zero entries.
        
        .. attribute:: atentry
        
        	Each entry contains one NetworkAddress to `physical' address equivalence
        	**type**\: list of :py:class:`AtEntry <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.AtTable.AtEntry>`
        
        

        """

        _prefix = 'rfc1213-mib'

        def __init__(self):
            self.parent = None
            self.atentry = YList()
            self.atentry.parent = self
            self.atentry.name = 'atentry'


        class AtEntry(object):
            """
            Each entry contains one NetworkAddress to
            `physical' address equivalence.
            
            .. attribute:: atifindex
            
            	The interface on which this entry's equivalence is effective.  The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: atnetaddress
            
            	The NetworkAddress (e.g., the IP address) corresponding to the media\-dependent `physical' address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: atphysaddress
            
            	The media\-dependent `physical' address.  Setting this object to a null string (one of zero length) has the effect of invaliding the corresponding entry in the atTable object.  That is, it effectively disassociates the interface identified with said entry from the mapping identified with said entry.  It is an implementation\-specific matter as to whether the agent removes an invalidated entry from the table. Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use. Proper interpretation of such entries requires examination of the relevant atPhysAddress object
            	**type**\: str
            
            

            """

            _prefix = 'rfc1213-mib'

            def __init__(self):
                self.parent = None
                self.atifindex = None
                self.atnetaddress = None
                self.atphysaddress = None

            @property
            def _common_path(self):
                if self.atifindex is None:
                    raise YPYDataValidationError('Key property atifindex is None')
                if self.atnetaddress is None:
                    raise YPYDataValidationError('Key property atnetaddress is None')

                return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:atTable/RFC1213-MIB:atEntry[RFC1213-MIB:atIfIndex = ' + str(self.atifindex) + '][RFC1213-MIB:atNetAddress = ' + str(self.atnetaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.atifindex is not None:
                    return True

                if self.atnetaddress is not None:
                    return True

                if self.atphysaddress is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                return meta._meta_table['RFC1213MIB.AtTable.AtEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:atTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.atentry is not None:
                for child_ref in self.atentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
            return meta._meta_table['RFC1213MIB.AtTable']['meta_info']


    class Egp(object):
        """
        
        
        .. attribute:: egpas
        
        	The autonomous system number of this EGP entity
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: egpinerrors
        
        	The number of EGP messages received that proved to be in error
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: egpinmsgs
        
        	The number of EGP messages received without error
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: egpouterrors
        
        	The number of locally generated EGP messages not sent due to resource limitations within an EGP entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: egpoutmsgs
        
        	The total number of locally generated EGP messages
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'rfc1213-mib'

        def __init__(self):
            self.parent = None
            self.egpas = None
            self.egpinerrors = None
            self.egpinmsgs = None
            self.egpouterrors = None
            self.egpoutmsgs = None

        @property
        def _common_path(self):

            return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:egp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.egpas is not None:
                return True

            if self.egpinerrors is not None:
                return True

            if self.egpinmsgs is not None:
                return True

            if self.egpouterrors is not None:
                return True

            if self.egpoutmsgs is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
            return meta._meta_table['RFC1213MIB.Egp']['meta_info']


    class EgpNeighTable(object):
        """
        The EGP neighbor table.
        
        .. attribute:: egpneighentry
        
        	Information about this entity's relationship with a particular EGP neighbor
        	**type**\: list of :py:class:`EgpNeighEntry <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.EgpNeighTable.EgpNeighEntry>`
        
        

        """

        _prefix = 'rfc1213-mib'

        def __init__(self):
            self.parent = None
            self.egpneighentry = YList()
            self.egpneighentry.parent = self
            self.egpneighentry.name = 'egpneighentry'


        class EgpNeighEntry(object):
            """
            Information about this entity's relationship with
            a particular EGP neighbor.
            
            .. attribute:: egpneighaddr
            
            	The IP address of this entry's EGP neighbor
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: egpneighas
            
            	The autonomous system of this EGP peer.  Zero should be specified if the autonomous system number of the neighbor is not yet known
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: egpneigheventtrigger
            
            	A control variable used to trigger operator\- initiated Start and Stop events.  When read, this variable always returns the most recent value that egpNeighEventTrigger was set to.  If it has not been set since the last initialization of the network management subsystem on the node, it returns a value of `stop'.  When set, this variable causes a Start or Stop event on the specified neighbor, as specified on pages 8\-10 of RFC 904.  Briefly, a Start event causes an Idle peer to begin neighbor acquisition and a non\-Idle peer to reinitiate neighbor acquisition.  A stop event causes a non\-Idle peer to return to the Idle state until a Start event occurs, either via egpNeighEventTrigger or otherwise
            	**type**\: :py:class:`EgpNeighEventTrigger_Enum <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.EgpNeighTable.EgpNeighEntry.EgpNeighEventTrigger_Enum>`
            
            .. attribute:: egpneighinerrmsgs
            
            	The number of EGP\-defined error messages received from this EGP peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighinerrs
            
            	The number of EGP messages received from this EGP peer that proved to be in error (e.g., bad EGP checksum)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighinmsgs
            
            	The number of EGP messages received without error from this EGP peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighintervalhello
            
            	The interval between EGP Hello command retransmissions (in hundredths of a second).  This represents the t1 timer as defined in RFC 904
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: egpneighintervalpoll
            
            	The interval between EGP poll command retransmissions (in hundredths of a second).  This represents the t3 timer as defined in RFC 904
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: egpneighmode
            
            	The polling mode of this EGP entity, either passive or active
            	**type**\: :py:class:`EgpNeighMode_Enum <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.EgpNeighTable.EgpNeighEntry.EgpNeighMode_Enum>`
            
            .. attribute:: egpneighouterrmsgs
            
            	The number of EGP\-defined error messages sent to this EGP peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighouterrs
            
            	The number of locally generated EGP messages not sent to this EGP peer due to resource limitations within an EGP entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighoutmsgs
            
            	The number of locally generated EGP messages to this EGP peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighstate
            
            	The EGP state of the local system with respect to this entry's EGP neighbor.  Each EGP state is represented by a value that is one greater than the numerical value associated with said state in RFC 904
            	**type**\: :py:class:`EgpNeighState_Enum <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.EgpNeighTable.EgpNeighEntry.EgpNeighState_Enum>`
            
            .. attribute:: egpneighstatedowns
            
            	The number of EGP state transitions from the UP state to any other state with this EGP peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighstateups
            
            	The number of EGP state transitions to the UP state with this EGP peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'rfc1213-mib'

            def __init__(self):
                self.parent = None
                self.egpneighaddr = None
                self.egpneighas = None
                self.egpneigheventtrigger = None
                self.egpneighinerrmsgs = None
                self.egpneighinerrs = None
                self.egpneighinmsgs = None
                self.egpneighintervalhello = None
                self.egpneighintervalpoll = None
                self.egpneighmode = None
                self.egpneighouterrmsgs = None
                self.egpneighouterrs = None
                self.egpneighoutmsgs = None
                self.egpneighstate = None
                self.egpneighstatedowns = None
                self.egpneighstateups = None

            class EgpNeighEventTrigger_Enum(Enum):
                """
                EgpNeighEventTrigger_Enum

                A control variable used to trigger operator\-
                initiated Start and Stop events.  When read, this
                variable always returns the most recent value that
                egpNeighEventTrigger was set to.  If it has not
                been set since the last initialization of the
                network management subsystem on the node, it
                returns a value of `stop'.
                
                When set, this variable causes a Start or Stop
                event on the specified neighbor, as specified on
                pages 8\-10 of RFC 904.  Briefly, a Start event
                causes an Idle peer to begin neighbor acquisition
                and a non\-Idle peer to reinitiate neighbor
                acquisition.  A stop event causes a non\-Idle peer
                to return to the Idle state until a Start event
                occurs, either via egpNeighEventTrigger or
                otherwise.

                """

                START = 1

                STOP = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                    return meta._meta_table['RFC1213MIB.EgpNeighTable.EgpNeighEntry.EgpNeighEventTrigger_Enum']


            class EgpNeighMode_Enum(Enum):
                """
                EgpNeighMode_Enum

                The polling mode of this EGP entity, either
                passive or active.

                """

                ACTIVE = 1

                PASSIVE = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                    return meta._meta_table['RFC1213MIB.EgpNeighTable.EgpNeighEntry.EgpNeighMode_Enum']


            class EgpNeighState_Enum(Enum):
                """
                EgpNeighState_Enum

                The EGP state of the local system with respect to
                this entry's EGP neighbor.  Each EGP state is
                represented by a value that is one greater than
                the numerical value associated with said state in
                RFC 904.

                """

                IDLE = 1

                ACQUISITION = 2

                DOWN = 3

                UP = 4

                CEASE = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                    return meta._meta_table['RFC1213MIB.EgpNeighTable.EgpNeighEntry.EgpNeighState_Enum']


            @property
            def _common_path(self):
                if self.egpneighaddr is None:
                    raise YPYDataValidationError('Key property egpneighaddr is None')

                return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:egpNeighTable/RFC1213-MIB:egpNeighEntry[RFC1213-MIB:egpNeighAddr = ' + str(self.egpneighaddr) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.egpneighaddr is not None:
                    return True

                if self.egpneighas is not None:
                    return True

                if self.egpneigheventtrigger is not None:
                    return True

                if self.egpneighinerrmsgs is not None:
                    return True

                if self.egpneighinerrs is not None:
                    return True

                if self.egpneighinmsgs is not None:
                    return True

                if self.egpneighintervalhello is not None:
                    return True

                if self.egpneighintervalpoll is not None:
                    return True

                if self.egpneighmode is not None:
                    return True

                if self.egpneighouterrmsgs is not None:
                    return True

                if self.egpneighouterrs is not None:
                    return True

                if self.egpneighoutmsgs is not None:
                    return True

                if self.egpneighstate is not None:
                    return True

                if self.egpneighstatedowns is not None:
                    return True

                if self.egpneighstateups is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                return meta._meta_table['RFC1213MIB.EgpNeighTable.EgpNeighEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:egpNeighTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.egpneighentry is not None:
                for child_ref in self.egpneighentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
            return meta._meta_table['RFC1213MIB.EgpNeighTable']['meta_info']


    class Icmp(object):
        """
        
        
        .. attribute:: icmpinaddrmaskreps
        
        	The number of ICMP Address Mask Reply messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinaddrmasks
        
        	The number of ICMP Address Mask Request messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpindestunreachs
        
        	The number of ICMP Destination Unreachable messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinechoreps
        
        	The number of ICMP Echo Reply messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinechos
        
        	The number of ICMP Echo (request) messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinerrors
        
        	The number of ICMP messages which the entity received but determined as having ICMP\-specific errors (bad ICMP checksums, bad length, etc.)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinmsgs
        
        	The total number of ICMP messages which the entity received.  Note that this counter includes all those counted by icmpInErrors
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinparmprobs
        
        	The number of ICMP Parameter Problem messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinredirects
        
        	The number of ICMP Redirect messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinsrcquenchs
        
        	The number of ICMP Source Quench messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpintimeexcds
        
        	The number of ICMP Time Exceeded messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpintimestampreps
        
        	The number of ICMP Timestamp Reply messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpintimestamps
        
        	The number of ICMP Timestamp (request) messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutaddrmaskreps
        
        	The number of ICMP Address Mask Reply messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutaddrmasks
        
        	The number of ICMP Address Mask Request messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutdestunreachs
        
        	The number of ICMP Destination Unreachable messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutechoreps
        
        	The number of ICMP Echo Reply messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutechos
        
        	The number of ICMP Echo (request) messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpouterrors
        
        	The number of ICMP messages which this entity did not send due to problems discovered within ICMP such as a lack of buffers.  This value should not include errors discovered outside the ICMP layer such as the inability of IP to route the resultant datagram.  In some implementations there may be no types of error which contribute to this counter's value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutmsgs
        
        	The total number of ICMP messages which this entity attempted to send.  Note that this counter includes all those counted by icmpOutErrors
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutparmprobs
        
        	The number of ICMP Parameter Problem messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutredirects
        
        	The number of ICMP Redirect messages sent.  For a host, this object will always be zero, since hosts do not send redirects
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutsrcquenchs
        
        	The number of ICMP Source Quench messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpouttimeexcds
        
        	The number of ICMP Time Exceeded messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpouttimestampreps
        
        	The number of ICMP Timestamp Reply messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpouttimestamps
        
        	The number of ICMP Timestamp (request) messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'rfc1213-mib'

        def __init__(self):
            self.parent = None
            self.icmpinaddrmaskreps = None
            self.icmpinaddrmasks = None
            self.icmpindestunreachs = None
            self.icmpinechoreps = None
            self.icmpinechos = None
            self.icmpinerrors = None
            self.icmpinmsgs = None
            self.icmpinparmprobs = None
            self.icmpinredirects = None
            self.icmpinsrcquenchs = None
            self.icmpintimeexcds = None
            self.icmpintimestampreps = None
            self.icmpintimestamps = None
            self.icmpoutaddrmaskreps = None
            self.icmpoutaddrmasks = None
            self.icmpoutdestunreachs = None
            self.icmpoutechoreps = None
            self.icmpoutechos = None
            self.icmpouterrors = None
            self.icmpoutmsgs = None
            self.icmpoutparmprobs = None
            self.icmpoutredirects = None
            self.icmpoutsrcquenchs = None
            self.icmpouttimeexcds = None
            self.icmpouttimestampreps = None
            self.icmpouttimestamps = None

        @property
        def _common_path(self):

            return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:icmp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.icmpinaddrmaskreps is not None:
                return True

            if self.icmpinaddrmasks is not None:
                return True

            if self.icmpindestunreachs is not None:
                return True

            if self.icmpinechoreps is not None:
                return True

            if self.icmpinechos is not None:
                return True

            if self.icmpinerrors is not None:
                return True

            if self.icmpinmsgs is not None:
                return True

            if self.icmpinparmprobs is not None:
                return True

            if self.icmpinredirects is not None:
                return True

            if self.icmpinsrcquenchs is not None:
                return True

            if self.icmpintimeexcds is not None:
                return True

            if self.icmpintimestampreps is not None:
                return True

            if self.icmpintimestamps is not None:
                return True

            if self.icmpoutaddrmaskreps is not None:
                return True

            if self.icmpoutaddrmasks is not None:
                return True

            if self.icmpoutdestunreachs is not None:
                return True

            if self.icmpoutechoreps is not None:
                return True

            if self.icmpoutechos is not None:
                return True

            if self.icmpouterrors is not None:
                return True

            if self.icmpoutmsgs is not None:
                return True

            if self.icmpoutparmprobs is not None:
                return True

            if self.icmpoutredirects is not None:
                return True

            if self.icmpoutsrcquenchs is not None:
                return True

            if self.icmpouttimeexcds is not None:
                return True

            if self.icmpouttimestampreps is not None:
                return True

            if self.icmpouttimestamps is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
            return meta._meta_table['RFC1213MIB.Icmp']['meta_info']


    class IfTable(object):
        """
        A list of interface entries.  The number of
        entries is given by the value of ifNumber.
        
        .. attribute:: ifentry
        
        	An interface entry containing objects at the subnetwork layer and below for a particular interface
        	**type**\: list of :py:class:`IfEntry <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.IfTable.IfEntry>`
        
        

        """

        _prefix = 'rfc1213-mib'

        def __init__(self):
            self.parent = None
            self.ifentry = YList()
            self.ifentry.parent = self
            self.ifentry.name = 'ifentry'


        class IfEntry(object):
            """
            An interface entry containing objects at the
            subnetwork layer and below for a particular
            interface.
            
            .. attribute:: ifindex
            
            	A unique value for each interface.  Its value ranges between 1 and the value of ifNumber.  The value for each interface must remain constant at least from one re\-initialization of the entity's network management system to the next re\- initialization
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ifadminstatus
            
            	The desired state of the interface.  The testing(3) state indicates that no operational packets can be passed
            	**type**\: :py:class:`IfAdminStatus_Enum <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.IfTable.IfEntry.IfAdminStatus_Enum>`
            
            .. attribute:: ifdescr
            
            	A textual string containing information about the interface.  This string should include the name of the manufacturer, the product name and the version of the hardware interface
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ifindiscards
            
            	The number of inbound packets which were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher\-layer protocol.  One possible reason for discarding such a packet could be to free up buffer space
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinerrors
            
            	The number of inbound packets that contained errors preventing them from being deliverable to a higher\-layer protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinnucastpkts
            
            	The number of non\-unicast (i.e., subnetwork\- broadcast or subnetwork\-multicast) packets delivered to a higher\-layer protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinoctets
            
            	The total number of octets received on the interface, including framing characters
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinucastpkts
            
            	The number of subnetwork\-unicast packets delivered to a higher\-layer protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinunknownprotos
            
            	The number of packets received via the interface which were discarded because of an unknown or unsupported protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: iflastchange
            
            	The value of sysUpTime at the time the interface entered its current operational state.  If the current state was entered prior to the last re\- initialization of the local network management subsystem, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifmtu
            
            	The size of the largest datagram which can be sent/received on the interface, specified in octets.  For interfaces that are used for transmitting network datagrams, this is the size of the largest network datagram that can be sent on the interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ifoperstatus
            
            	The current operational state of the interface. The testing(3) state indicates that no operational packets can be passed
            	**type**\: :py:class:`IfOperStatus_Enum <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.IfTable.IfEntry.IfOperStatus_Enum>`
            
            .. attribute:: ifoutdiscards
            
            	The number of outbound packets which were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a packet could be to free up buffer space
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifouterrors
            
            	The number of outbound packets that could not be transmitted because of errors
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutnucastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted to a non\- unicast (i.e., a subnetwork\-broadcast or subnetwork\-multicast) address, including those that were discarded or not sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutoctets
            
            	The total number of octets transmitted out of the interface, including framing characters
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutqlen
            
            	The length of the output packet queue (in packets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutucastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted to a subnetwork\-unicast address, including those that were discarded or not sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifphysaddress
            
            	The interface's address at the protocol layer immediately `below' the network layer in the protocol stack.  For interfaces which do not have such an address (e.g., a serial line), this object should contain an octet string of zero length
            	**type**\: str
            
            .. attribute:: ifspecific
            
            	A reference to MIB definitions specific to the particular media being used to realize the interface.  For example, if the interface is realized by an ethernet, then the value of this object refers to a document defining objects specific to ethernet.  If this information is not present, its value should be set to the OBJECT IDENTIFIER { 0 0 }, which is a syntactically valid object identifier, and any conformant implementation of ASN.1 and BER must be able to generate and recognize this value
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: ifspeed
            
            	An estimate of the interface's current bandwidth in bits per second.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: iftype
            
            	The type of interface.  Additional values for ifType are assigned by the Internet Assigned Numbers Authority (IANA), through updating the syntax of the IANAifType textual convention
            	**type**\: :py:class:`IANAifType_Enum <ydk.models.ianaiftype.IANAifType_MIB.IANAifType_Enum>`
            
            

            """

            _prefix = 'rfc1213-mib'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.ifadminstatus = None
                self.ifdescr = None
                self.ifindiscards = None
                self.ifinerrors = None
                self.ifinnucastpkts = None
                self.ifinoctets = None
                self.ifinucastpkts = None
                self.ifinunknownprotos = None
                self.iflastchange = None
                self.ifmtu = None
                self.ifoperstatus = None
                self.ifoutdiscards = None
                self.ifouterrors = None
                self.ifoutnucastpkts = None
                self.ifoutoctets = None
                self.ifoutqlen = None
                self.ifoutucastpkts = None
                self.ifphysaddress = None
                self.ifspecific = None
                self.ifspeed = None
                self.iftype = None

            class IfAdminStatus_Enum(Enum):
                """
                IfAdminStatus_Enum

                The desired state of the interface.  The
                testing(3) state indicates that no operational
                packets can be passed.

                """

                UP = 1

                DOWN = 2

                TESTING = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                    return meta._meta_table['RFC1213MIB.IfTable.IfEntry.IfAdminStatus_Enum']


            class IfOperStatus_Enum(Enum):
                """
                IfOperStatus_Enum

                The current operational state of the interface.
                The testing(3) state indicates that no operational
                packets can be passed.

                """

                UP = 1

                DOWN = 2

                TESTING = 3

                UNKNOWN = 4

                DORMANT = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                    return meta._meta_table['RFC1213MIB.IfTable.IfEntry.IfOperStatus_Enum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:ifTable/RFC1213-MIB:ifEntry[RFC1213-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.ifadminstatus is not None:
                    return True

                if self.ifdescr is not None:
                    return True

                if self.ifindiscards is not None:
                    return True

                if self.ifinerrors is not None:
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

                if self.ifmtu is not None:
                    return True

                if self.ifoperstatus is not None:
                    return True

                if self.ifoutdiscards is not None:
                    return True

                if self.ifouterrors is not None:
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

                if self.ifspecific is not None:
                    return True

                if self.ifspeed is not None:
                    return True

                if self.iftype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                return meta._meta_table['RFC1213MIB.IfTable.IfEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:ifTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ifentry is not None:
                for child_ref in self.ifentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
            return meta._meta_table['RFC1213MIB.IfTable']['meta_info']


    class Interfaces(object):
        """
        
        
        .. attribute:: ifnumber
        
        	The number of network interfaces (regardless of their current state) present on this system
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'rfc1213-mib'

        def __init__(self):
            self.parent = None
            self.ifnumber = None

        @property
        def _common_path(self):

            return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ifnumber is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
            return meta._meta_table['RFC1213MIB.Interfaces']['meta_info']


    class Ip(object):
        """
        
        
        .. attribute:: ipdefaultttl
        
        	The default value inserted into the Time\-To\-Live field of the IP header of datagrams originated at this entity, whenever a TTL value is not supplied by the transport layer protocol
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: ipforwarding
        
        	The indication of whether this entity is acting as an IP gateway in respect to the forwarding of datagrams received by, but not addressed to, this entity.  IP gateways forward datagrams.  IP hosts do not (except those source\-routed via the host).  Note that for some managed nodes, this object may take on only a subset of the values possible. Accordingly, it is appropriate for an agent to return a `badValue' response if a management station attempts to change this object to an inappropriate value
        	**type**\: :py:class:`IpForwarding_Enum <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.Ip.IpForwarding_Enum>`
        
        .. attribute:: ipforwdatagrams
        
        	The number of input datagrams for which this entity was not their final IP destination, as a result of which an attempt was made to find a route to forward them to that final destination. In entities which do not act as IP Gateways, this counter will include only those packets which were Source\-Routed via this entity, and the Source\- Route option processing was successful
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipfragcreates
        
        	The number of IP datagram fragments that have been generated as a result of fragmentation at this entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipfragfails
        
        	The number of IP datagrams that have been discarded because they needed to be fragmented at this entity but could not be, e.g., because their Don't Fragment flag was set
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipfragoks
        
        	The number of IP datagrams that have been successfully fragmented at this entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipinaddrerrors
        
        	The number of input datagrams discarded because the IP address in their IP header's destination field was not a valid address to be received at this entity.  This count includes invalid addresses (e.g., 0.0.0.0) and addresses of unsupported Classes (e.g., Class E).  For entities which are not IP Gateways and therefore do not forward datagrams, this counter includes datagrams discarded because the destination address was not a local address
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipindelivers
        
        	The total number of input datagrams successfully delivered to IP user\-protocols (including ICMP)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipindiscards
        
        	The number of input IP datagrams for which no problems were encountered to prevent their continued processing, but which were discarded (e.g., for lack of buffer space).  Note that this counter does not include any datagrams discarded while awaiting re\-assembly
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipinhdrerrors
        
        	The number of input datagrams discarded due to errors in their IP headers, including bad checksums, version number mismatch, other format errors, time\-to\-live exceeded, errors discovered in processing their IP options, etc
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipinreceives
        
        	The total number of input datagrams received from interfaces, including those received in error
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipinunknownprotos
        
        	The number of locally\-addressed datagrams received successfully but discarded because of an unknown or unsupported protocol
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipoutdiscards
        
        	The number of output IP datagrams for which no problem was encountered to prevent their transmission to their destination, but which were discarded (e.g., for lack of buffer space).  Note that this counter would include datagrams counted in ipForwDatagrams if any such packets met this (discretionary) discard criterion
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipoutnoroutes
        
        	The number of IP datagrams discarded because no route could be found to transmit them to their destination.  Note that this counter includes any packets counted in ipForwDatagrams which meet this `no\-route' criterion.  Note that this includes any datagrams which a host cannot route because all of its default gateways are down
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipoutrequests
        
        	The total number of IP datagrams which local IP user\-protocols (including ICMP) supplied to IP in requests for transmission.  Note that this counter does not include any datagrams counted in ipForwDatagrams
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipreasmfails
        
        	The number of failures detected by the IP re\- assembly algorithm (for whatever reason\: timed out, errors, etc).  Note that this is not necessarily a count of discarded IP fragments since some algorithms (notably the algorithm in RFC 815) can lose track of the number of fragments by combining them as they are received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipreasmoks
        
        	The number of IP datagrams successfully re\- assembled
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipreasmreqds
        
        	The number of IP fragments received which needed to be reassembled at this entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipreasmtimeout
        
        	The maximum number of seconds which received fragments are held while they are awaiting reassembly at this entity
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: iproutingdiscards
        
        	The number of routing entries which were chosen to be discarded even though they are valid.  One possible reason for discarding such an entry could be to free\-up buffer space for other routing entries
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'rfc1213-mib'

        def __init__(self):
            self.parent = None
            self.ipdefaultttl = None
            self.ipforwarding = None
            self.ipforwdatagrams = None
            self.ipfragcreates = None
            self.ipfragfails = None
            self.ipfragoks = None
            self.ipinaddrerrors = None
            self.ipindelivers = None
            self.ipindiscards = None
            self.ipinhdrerrors = None
            self.ipinreceives = None
            self.ipinunknownprotos = None
            self.ipoutdiscards = None
            self.ipoutnoroutes = None
            self.ipoutrequests = None
            self.ipreasmfails = None
            self.ipreasmoks = None
            self.ipreasmreqds = None
            self.ipreasmtimeout = None
            self.iproutingdiscards = None

        class IpForwarding_Enum(Enum):
            """
            IpForwarding_Enum

            The indication of whether this entity is acting
            as an IP gateway in respect to the forwarding of
            datagrams received by, but not addressed to, this
            entity.  IP gateways forward datagrams.  IP hosts
            do not (except those source\-routed via the host).
            
            Note that for some managed nodes, this object may
            take on only a subset of the values possible.
            Accordingly, it is appropriate for an agent to
            return a `badValue' response if a management
            station attempts to change this object to an
            inappropriate value.

            """

            FORWARDING = 1

            NOT_FORWARDING = 2


            @staticmethod
            def _meta_info():
                from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                return meta._meta_table['RFC1213MIB.Ip.IpForwarding_Enum']


        @property
        def _common_path(self):

            return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:ip'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ipdefaultttl is not None:
                return True

            if self.ipforwarding is not None:
                return True

            if self.ipforwdatagrams is not None:
                return True

            if self.ipfragcreates is not None:
                return True

            if self.ipfragfails is not None:
                return True

            if self.ipfragoks is not None:
                return True

            if self.ipinaddrerrors is not None:
                return True

            if self.ipindelivers is not None:
                return True

            if self.ipindiscards is not None:
                return True

            if self.ipinhdrerrors is not None:
                return True

            if self.ipinreceives is not None:
                return True

            if self.ipinunknownprotos is not None:
                return True

            if self.ipoutdiscards is not None:
                return True

            if self.ipoutnoroutes is not None:
                return True

            if self.ipoutrequests is not None:
                return True

            if self.ipreasmfails is not None:
                return True

            if self.ipreasmoks is not None:
                return True

            if self.ipreasmreqds is not None:
                return True

            if self.ipreasmtimeout is not None:
                return True

            if self.iproutingdiscards is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
            return meta._meta_table['RFC1213MIB.Ip']['meta_info']


    class IpAddrTable(object):
        """
        The table of addressing information relevant to
        this entity's IP addresses.
        
        .. attribute:: ipaddrentry
        
        	The addressing information for one of this entity's IP addresses
        	**type**\: list of :py:class:`IpAddrEntry <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.IpAddrTable.IpAddrEntry>`
        
        

        """

        _prefix = 'rfc1213-mib'

        def __init__(self):
            self.parent = None
            self.ipaddrentry = YList()
            self.ipaddrentry.parent = self
            self.ipaddrentry.name = 'ipaddrentry'


        class IpAddrEntry(object):
            """
            The addressing information for one of this
            entity's IP addresses.
            
            .. attribute:: ipadentaddr
            
            	The IP address to which this entry's addressing information pertains
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipadentbcastaddr
            
            	The value of the least\-significant bit in the IP broadcast address used for sending datagrams on the (logical) interface associated with the IP address of this entry.  For example, when the Internet standard all\-ones broadcast address is used, the value will be 1.  This value applies to both the subnet and network broadcasts addresses used by the entity on this (logical) interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipadentifindex
            
            	The index value which uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipadentnetmask
            
            	The subnet mask associated with the IP address of this entry.  The value of the mask is an IP address with all the network bits set to 1 and all the hosts bits set to 0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipadentreasmmaxsize
            
            	The size of the largest IP datagram which this entity can re\-assemble from incoming IP fragmented datagrams received on this interface
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'rfc1213-mib'

            def __init__(self):
                self.parent = None
                self.ipadentaddr = None
                self.ipadentbcastaddr = None
                self.ipadentifindex = None
                self.ipadentnetmask = None
                self.ipadentreasmmaxsize = None

            @property
            def _common_path(self):
                if self.ipadentaddr is None:
                    raise YPYDataValidationError('Key property ipadentaddr is None')

                return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:ipAddrTable/RFC1213-MIB:ipAddrEntry[RFC1213-MIB:ipAdEntAddr = ' + str(self.ipadentaddr) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ipadentaddr is not None:
                    return True

                if self.ipadentbcastaddr is not None:
                    return True

                if self.ipadentifindex is not None:
                    return True

                if self.ipadentnetmask is not None:
                    return True

                if self.ipadentreasmmaxsize is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                return meta._meta_table['RFC1213MIB.IpAddrTable.IpAddrEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:ipAddrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ipaddrentry is not None:
                for child_ref in self.ipaddrentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
            return meta._meta_table['RFC1213MIB.IpAddrTable']['meta_info']


    class IpNetToMediaTable(object):
        """
        The IP Address Translation table used for mapping
        from IP addresses to physical addresses.
        
        .. attribute:: ipnettomediaentry
        
        	Each entry contains one IpAddress to `physical' address equivalence
        	**type**\: list of :py:class:`IpNetToMediaEntry <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.IpNetToMediaTable.IpNetToMediaEntry>`
        
        

        """

        _prefix = 'rfc1213-mib'

        def __init__(self):
            self.parent = None
            self.ipnettomediaentry = YList()
            self.ipnettomediaentry.parent = self
            self.ipnettomediaentry.name = 'ipnettomediaentry'


        class IpNetToMediaEntry(object):
            """
            Each entry contains one IpAddress to `physical'
            address equivalence.
            
            .. attribute:: ipnettomediaifindex
            
            	The interface on which this entry's equivalence is effective.  The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipnettomedianetaddress
            
            	The IpAddress corresponding to the media\- dependent `physical' address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipnettomediaphysaddress
            
            	The media\-dependent `physical' address
            	**type**\: str
            
            .. attribute:: ipnettomediatype
            
            	The type of mapping.  Setting this object to the value invalid(2) has the effect of invalidating the corresponding entry in the ipNetToMediaTable.  That is, it effectively disassociates the interface identified with said entry from the mapping identified with said entry. It is an implementation\-specific matter as to whether the agent removes an invalidated entry from the table.  Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use.  Proper interpretation of such entries requires examination of the relevant ipNetToMediaType object
            	**type**\: :py:class:`IpNetToMediaType_Enum <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.IpNetToMediaTable.IpNetToMediaEntry.IpNetToMediaType_Enum>`
            
            

            """

            _prefix = 'rfc1213-mib'

            def __init__(self):
                self.parent = None
                self.ipnettomediaifindex = None
                self.ipnettomedianetaddress = None
                self.ipnettomediaphysaddress = None
                self.ipnettomediatype = None

            class IpNetToMediaType_Enum(Enum):
                """
                IpNetToMediaType_Enum

                The type of mapping.
                
                Setting this object to the value invalid(2) has
                the effect of invalidating the corresponding entry
                in the ipNetToMediaTable.  That is, it effectively
                disassociates the interface identified with said
                entry from the mapping identified with said entry.
                It is an implementation\-specific matter as to
                whether the agent removes an invalidated entry
                from the table.  Accordingly, management stations
                must be prepared to receive tabular information
                from agents that corresponds to entries not
                currently in use.  Proper interpretation of such
                entries requires examination of the relevant
                ipNetToMediaType object.

                """

                OTHER = 1

                INVALID = 2

                DYNAMIC = 3

                STATIC = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                    return meta._meta_table['RFC1213MIB.IpNetToMediaTable.IpNetToMediaEntry.IpNetToMediaType_Enum']


            @property
            def _common_path(self):
                if self.ipnettomediaifindex is None:
                    raise YPYDataValidationError('Key property ipnettomediaifindex is None')
                if self.ipnettomedianetaddress is None:
                    raise YPYDataValidationError('Key property ipnettomedianetaddress is None')

                return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:ipNetToMediaTable/RFC1213-MIB:ipNetToMediaEntry[RFC1213-MIB:ipNetToMediaIfIndex = ' + str(self.ipnettomediaifindex) + '][RFC1213-MIB:ipNetToMediaNetAddress = ' + str(self.ipnettomedianetaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ipnettomediaifindex is not None:
                    return True

                if self.ipnettomedianetaddress is not None:
                    return True

                if self.ipnettomediaphysaddress is not None:
                    return True

                if self.ipnettomediatype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                return meta._meta_table['RFC1213MIB.IpNetToMediaTable.IpNetToMediaEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:ipNetToMediaTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ipnettomediaentry is not None:
                for child_ref in self.ipnettomediaentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
            return meta._meta_table['RFC1213MIB.IpNetToMediaTable']['meta_info']


    class IpRouteTable(object):
        """
        This entity's IP Routing table.
        
        .. attribute:: iprouteentry
        
        	A route to a particular destination
        	**type**\: list of :py:class:`IpRouteEntry <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.IpRouteTable.IpRouteEntry>`
        
        

        """

        _prefix = 'rfc1213-mib'

        def __init__(self):
            self.parent = None
            self.iprouteentry = YList()
            self.iprouteentry.parent = self
            self.iprouteentry.name = 'iprouteentry'


        class IpRouteEntry(object):
            """
            A route to a particular destination.
            
            .. attribute:: iproutedest
            
            	The destination IP address of this route.  An entry with a value of 0.0.0.0 is considered a default route.  Multiple routes to a single destination can appear in the table, but access to such multiple entries is dependent on the table\- access mechanisms defined by the network management protocol in use
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: iprouteage
            
            	The number of seconds since this route was last updated or otherwise determined to be correct. Note that no semantics of `too old' can be implied except through knowledge of the routing protocol by which the route was learned
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iprouteifindex
            
            	The index value which uniquely identifies the local interface through which the next hop of this route should be reached.  The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iprouteinfo
            
            	A reference to MIB definitions specific to the particular routing protocol which is responsible for this route, as determined by the value specified in the route's ipRouteProto value.  If this information is not present, its value should be set to the OBJECT IDENTIFIER { 0 0 }, which is a syntactically valid object identifier, and any conformant implementation of ASN.1 and BER must be able to generate and recognize this value
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: iproutemask
            
            	Indicate the mask to be logical\-ANDed with the destination address before being compared to the value in the ipRouteDest field.  For those systems that do not support arbitrary subnet masks, an agent constructs the value of the ipRouteMask by determining whether the value of the correspondent ipRouteDest field belong to a class\-A, B, or C network, and then using one of\:       mask           network      255.0.0.0      class\-A      255.255.0.0    class\-B      255.255.255.0  class\-C  If the value of the ipRouteDest is 0.0.0.0 (a default route), then the mask value is also 0.0.0.0.  It should be noted that all IP routing subsystems implicitly use this mechanism
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: iproutemetric1
            
            	The primary routing metric for this route.  The semantics of this metric are determined by the routing\-protocol specified in the route's ipRouteProto value.  If this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iproutemetric2
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing\-protocol specified in the route's ipRouteProto value.  If this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iproutemetric3
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing\-protocol specified in the route's ipRouteProto value.  If this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iproutemetric4
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing\-protocol specified in the route's ipRouteProto value.  If this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iproutemetric5
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing\-protocol specified in the route's ipRouteProto value.  If this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iproutenexthop
            
            	The IP address of the next hop of this route. (In the case of a route bound to an interface which is realized via a broadcast media, the value of this field is the agent's IP address on that interface.)
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: iprouteproto
            
            	The routing mechanism via which this route was learned.  Inclusion of values for gateway routing protocols is not intended to imply that hosts should support those protocols
            	**type**\: :py:class:`IpRouteProto_Enum <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.IpRouteTable.IpRouteEntry.IpRouteProto_Enum>`
            
            .. attribute:: iproutetype
            
            	The type of route.  Note that the values direct(3) and indirect(4) refer to the notion of direct and indirect routing in the IP architecture.  Setting this object to the value invalid(2) has the effect of invalidating the corresponding entry in the ipRouteTable object.  That is, it effectively disassociates the destination identified with said entry from the route identified with said entry.  It is an implementation\-specific matter as to whether the agent removes an invalidated entry from the table. Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use. Proper interpretation of such entries requires examination of the relevant ipRouteType object
            	**type**\: :py:class:`IpRouteType_Enum <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.IpRouteTable.IpRouteEntry.IpRouteType_Enum>`
            
            

            """

            _prefix = 'rfc1213-mib'

            def __init__(self):
                self.parent = None
                self.iproutedest = None
                self.iprouteage = None
                self.iprouteifindex = None
                self.iprouteinfo = None
                self.iproutemask = None
                self.iproutemetric1 = None
                self.iproutemetric2 = None
                self.iproutemetric3 = None
                self.iproutemetric4 = None
                self.iproutemetric5 = None
                self.iproutenexthop = None
                self.iprouteproto = None
                self.iproutetype = None

            class IpRouteProto_Enum(Enum):
                """
                IpRouteProto_Enum

                The routing mechanism via which this route was
                learned.  Inclusion of values for gateway routing
                protocols is not intended to imply that hosts
                should support those protocols.

                """

                OTHER = 1

                LOCAL = 2

                NETMGMT = 3

                ICMP = 4

                EGP = 5

                GGP = 6

                HELLO = 7

                RIP = 8

                IS_IS = 9

                ES_IS = 10

                CISCOIGRP = 11

                BBNSPFIGP = 12

                OSPF = 13

                BGP = 14


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                    return meta._meta_table['RFC1213MIB.IpRouteTable.IpRouteEntry.IpRouteProto_Enum']


            class IpRouteType_Enum(Enum):
                """
                IpRouteType_Enum

                The type of route.  Note that the values
                direct(3) and indirect(4) refer to the notion of
                direct and indirect routing in the IP
                architecture.
                
                Setting this object to the value invalid(2) has
                the effect of invalidating the corresponding entry
                in the ipRouteTable object.  That is, it
                effectively disassociates the destination
                identified with said entry from the route
                identified with said entry.  It is an
                implementation\-specific matter as to whether the
                agent removes an invalidated entry from the table.
                Accordingly, management stations must be prepared
                to receive tabular information from agents that
                corresponds to entries not currently in use.
                Proper interpretation of such entries requires
                examination of the relevant ipRouteType object.

                """

                OTHER = 1

                INVALID = 2

                DIRECT = 3

                INDIRECT = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                    return meta._meta_table['RFC1213MIB.IpRouteTable.IpRouteEntry.IpRouteType_Enum']


            @property
            def _common_path(self):
                if self.iproutedest is None:
                    raise YPYDataValidationError('Key property iproutedest is None')

                return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:ipRouteTable/RFC1213-MIB:ipRouteEntry[RFC1213-MIB:ipRouteDest = ' + str(self.iproutedest) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.iproutedest is not None:
                    return True

                if self.iprouteage is not None:
                    return True

                if self.iprouteifindex is not None:
                    return True

                if self.iprouteinfo is not None:
                    return True

                if self.iproutemask is not None:
                    return True

                if self.iproutemetric1 is not None:
                    return True

                if self.iproutemetric2 is not None:
                    return True

                if self.iproutemetric3 is not None:
                    return True

                if self.iproutemetric4 is not None:
                    return True

                if self.iproutemetric5 is not None:
                    return True

                if self.iproutenexthop is not None:
                    return True

                if self.iprouteproto is not None:
                    return True

                if self.iproutetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                return meta._meta_table['RFC1213MIB.IpRouteTable.IpRouteEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:ipRouteTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.iprouteentry is not None:
                for child_ref in self.iprouteentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
            return meta._meta_table['RFC1213MIB.IpRouteTable']['meta_info']


    class Snmp(object):
        """
        
        
        .. attribute:: snmpenableauthentraps
        
        	Indicates whether the SNMP agent process is permitted to generate authentication\-failure traps.  The value of this object overrides any configuration information; as such, it provides a means whereby all authentication\-failure traps may be disabled.  Note that it is strongly recommended that this object be stored in non\-volatile memory so that it remains constant between re\-initializations of the network management system
        	**type**\: :py:class:`SnmpEnableAuthenTraps_Enum <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.Snmp.SnmpEnableAuthenTraps_Enum>`
        
        .. attribute:: snmpinasnparseerrs
        
        	The total number of ASN.1 or BER errors encountered by the SNMP protocol entity when decoding received SNMP Messages
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadcommunitynames
        
        	The total number of SNMP Messages delivered to the SNMP protocol entity which used a SNMP community name not known to said entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadcommunityuses
        
        	The total number of SNMP Messages delivered to the SNMP protocol entity which represented an SNMP operation which was not allowed by the SNMP community named in the Message
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadvalues
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field is `badValue'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadversions
        
        	The total number of SNMP Messages which were delivered to the SNMP protocol entity and were for an unsupported SNMP version
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpingenerrs
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field is `genErr'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpingetnexts
        
        	The total number of SNMP Get\-Next PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpingetrequests
        
        	The total number of SNMP Get\-Request PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpingetresponses
        
        	The total number of SNMP Get\-Response PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinnosuchnames
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field is `noSuchName'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinpkts
        
        	The total number of Messages delivered to the SNMP entity from the transport service
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinreadonlys
        
        	The total number valid SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field is `readOnly'.  It should be noted that it is a protocol error to generate an SNMP PDU which contains the value `readOnly' in the error\-status field, as such this object is provided as a means of detecting incorrect implementations of the SNMP
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinsetrequests
        
        	The total number of SNMP Set\-Request PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpintoobigs
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field is `tooBig'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpintotalreqvars
        
        	The total number of MIB objects which have been retrieved successfully by the SNMP protocol entity as the result of receiving valid SNMP Get\-Request and Get\-Next PDUs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpintotalsetvars
        
        	The total number of MIB objects which have been altered successfully by the SNMP protocol entity as the result of receiving valid SNMP Set\-Request PDUs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpintraps
        
        	The total number of SNMP Trap PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutbadvalues
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status field is `badValue'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutgenerrs
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status field is `genErr'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutgetnexts
        
        	The total number of SNMP Get\-Next PDUs which have been generated by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutgetrequests
        
        	The total number of SNMP Get\-Request PDUs which have been generated by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutgetresponses
        
        	The total number of SNMP Get\-Response PDUs which have been generated by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutnosuchnames
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status is `noSuchName'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutpkts
        
        	The total number of SNMP Messages which were passed from the SNMP protocol entity to the transport service
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutsetrequests
        
        	The total number of SNMP Set\-Request PDUs which have been generated by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpouttoobigs
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status field is `tooBig.'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpouttraps
        
        	The total number of SNMP Trap PDUs which have been generated by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'rfc1213-mib'

        def __init__(self):
            self.parent = None
            self.snmpenableauthentraps = None
            self.snmpinasnparseerrs = None
            self.snmpinbadcommunitynames = None
            self.snmpinbadcommunityuses = None
            self.snmpinbadvalues = None
            self.snmpinbadversions = None
            self.snmpingenerrs = None
            self.snmpingetnexts = None
            self.snmpingetrequests = None
            self.snmpingetresponses = None
            self.snmpinnosuchnames = None
            self.snmpinpkts = None
            self.snmpinreadonlys = None
            self.snmpinsetrequests = None
            self.snmpintoobigs = None
            self.snmpintotalreqvars = None
            self.snmpintotalsetvars = None
            self.snmpintraps = None
            self.snmpoutbadvalues = None
            self.snmpoutgenerrs = None
            self.snmpoutgetnexts = None
            self.snmpoutgetrequests = None
            self.snmpoutgetresponses = None
            self.snmpoutnosuchnames = None
            self.snmpoutpkts = None
            self.snmpoutsetrequests = None
            self.snmpouttoobigs = None
            self.snmpouttraps = None

        class SnmpEnableAuthenTraps_Enum(Enum):
            """
            SnmpEnableAuthenTraps_Enum

            Indicates whether the SNMP agent process is
            permitted to generate authentication\-failure
            traps.  The value of this object overrides any
            configuration information; as such, it provides a
            means whereby all authentication\-failure traps may
            be disabled.
            
            Note that it is strongly recommended that this
            object be stored in non\-volatile memory so that it
            remains constant between re\-initializations of the
            network management system.

            """

            ENABLED = 1

            DISABLED = 2


            @staticmethod
            def _meta_info():
                from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                return meta._meta_table['RFC1213MIB.Snmp.SnmpEnableAuthenTraps_Enum']


        @property
        def _common_path(self):

            return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:snmp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.snmpenableauthentraps is not None:
                return True

            if self.snmpinasnparseerrs is not None:
                return True

            if self.snmpinbadcommunitynames is not None:
                return True

            if self.snmpinbadcommunityuses is not None:
                return True

            if self.snmpinbadvalues is not None:
                return True

            if self.snmpinbadversions is not None:
                return True

            if self.snmpingenerrs is not None:
                return True

            if self.snmpingetnexts is not None:
                return True

            if self.snmpingetrequests is not None:
                return True

            if self.snmpingetresponses is not None:
                return True

            if self.snmpinnosuchnames is not None:
                return True

            if self.snmpinpkts is not None:
                return True

            if self.snmpinreadonlys is not None:
                return True

            if self.snmpinsetrequests is not None:
                return True

            if self.snmpintoobigs is not None:
                return True

            if self.snmpintotalreqvars is not None:
                return True

            if self.snmpintotalsetvars is not None:
                return True

            if self.snmpintraps is not None:
                return True

            if self.snmpoutbadvalues is not None:
                return True

            if self.snmpoutgenerrs is not None:
                return True

            if self.snmpoutgetnexts is not None:
                return True

            if self.snmpoutgetrequests is not None:
                return True

            if self.snmpoutgetresponses is not None:
                return True

            if self.snmpoutnosuchnames is not None:
                return True

            if self.snmpoutpkts is not None:
                return True

            if self.snmpoutsetrequests is not None:
                return True

            if self.snmpouttoobigs is not None:
                return True

            if self.snmpouttraps is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
            return meta._meta_table['RFC1213MIB.Snmp']['meta_info']


    class System(object):
        """
        
        
        .. attribute:: syscontact
        
        	The textual identification of the contact person for this managed node, together with information on how to contact this person
        	**type**\: str
        
        	**range:** 0..255
        
        .. attribute:: sysdescr
        
        	A textual description of the entity.  This value should include the full name and version identification of the system's hardware type, software operating\-system, and networking software.  It is mandatory that this only contain printable ASCII characters
        	**type**\: str
        
        	**range:** 0..255
        
        .. attribute:: syslocation
        
        	The physical location of this node (e.g., `telephone closet, 3rd floor')
        	**type**\: str
        
        	**range:** 0..255
        
        .. attribute:: sysname
        
        	An administratively\-assigned name for this managed node.  By convention, this is the node's fully\-qualified domain name
        	**type**\: str
        
        	**range:** 0..255
        
        .. attribute:: sysobjectid
        
        	The vendor's authoritative identification of the network management subsystem contained in the entity.  This value is allocated within the SMI enterprises subtree (1.3.6.1.4.1) and provides an easy and unambiguous means for determining `what kind of box' is being managed.  For example, if vendor `Flintstones, Inc.' was assigned the subtree 1.3.6.1.4.1.4242, it could assign the identifier 1.3.6.1.4.1.4242.1.1 to its `Fred Router'
        	**type**\: str
        
        	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
        
        .. attribute:: sysservices
        
        	A value which indicates the set of services that this entity primarily offers.  The value is a sum.  This sum initially takes the value zero, Then, for each layer, L, in the range 1 through 7, that this node performs transactions for, 2 raised to (L \- 1) is added to the sum.  For example, a node which performs primarily routing functions would have a value of 4 (2^(3\-1)).  In contrast, a node which is a host offering application services would have a value of 72 (2^(4\-1) + 2^(7\-1)).  Note that in the context of the Internet suite of protocols, values should be calculated accordingly\:       layer  functionality          1  physical (e.g., repeaters)          2  datalink/subnetwork (e.g., bridges)          3  internet (e.g., IP gateways)          4  end\-to\-end  (e.g., IP hosts)          7  applications (e.g., mail relays)  For systems including OSI protocols, layers 5 and 6 may also be counted
        	**type**\: int
        
        	**range:** 0..127
        
        .. attribute:: sysuptime
        
        	The time (in hundredths of a second) since the network management portion of the system was last re\-initialized
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'rfc1213-mib'

        def __init__(self):
            self.parent = None
            self.syscontact = None
            self.sysdescr = None
            self.syslocation = None
            self.sysname = None
            self.sysobjectid = None
            self.sysservices = None
            self.sysuptime = None

        @property
        def _common_path(self):

            return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:system'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.syscontact is not None:
                return True

            if self.sysdescr is not None:
                return True

            if self.syslocation is not None:
                return True

            if self.sysname is not None:
                return True

            if self.sysobjectid is not None:
                return True

            if self.sysservices is not None:
                return True

            if self.sysuptime is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
            return meta._meta_table['RFC1213MIB.System']['meta_info']


    class Tcp(object):
        """
        
        
        .. attribute:: tcpactiveopens
        
        	The number of times TCP connections have made a direct transition to the SYN\-SENT state from the CLOSED state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpattemptfails
        
        	The number of times TCP connections have made a direct transition to the CLOSED state from either the SYN\-SENT state or the SYN\-RCVD state, plus the number of times TCP connections have made a direct transition to the LISTEN state from the SYN\-RCVD state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpcurrestab
        
        	The number of TCP connections for which the current state is either ESTABLISHED or CLOSE\- WAIT
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpestabresets
        
        	The number of times TCP connections have made a direct transition to the CLOSED state from either the ESTABLISHED state or the CLOSE\-WAIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpinerrs
        
        	The total number of segments received in error (e.g., bad TCP checksums)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpinsegs
        
        	The total number of segments received, including those received in error.  This count includes segments received on currently established connections
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpmaxconn
        
        	The limit on the total number of TCP connections the entity can support.  In entities where the maximum number of connections is dynamic, this object should contain the value \-1
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: tcpoutrsts
        
        	The number of TCP segments sent containing the RST flag
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpoutsegs
        
        	The total number of segments sent, including those on current connections but excluding those containing only retransmitted octets
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcppassiveopens
        
        	The number of times TCP connections have made a direct transition to the SYN\-RCVD state from the LISTEN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpretranssegs
        
        	The total number of segments retransmitted \- that is, the number of TCP segments transmitted containing one or more previously transmitted octets
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcprtoalgorithm
        
        	The algorithm used to determine the timeout value used for retransmitting unacknowledged octets
        	**type**\: :py:class:`TcpRtoAlgorithm_Enum <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.Tcp.TcpRtoAlgorithm_Enum>`
        
        .. attribute:: tcprtomax
        
        	The maximum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds.  More refined semantics for objects of this type depend upon the algorithm used to determine the retransmission timeout.  In particular, when the timeout algorithm is rsre(3), an object of this type has the semantics of the UBOUND quantity described in RFC 793
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: tcprtomin
        
        	The minimum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds.  More refined semantics for objects of this type depend upon the algorithm used to determine the retransmission timeout.  In particular, when the timeout algorithm is rsre(3), an object of this type has the semantics of the LBOUND quantity described in RFC 793
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'rfc1213-mib'

        def __init__(self):
            self.parent = None
            self.tcpactiveopens = None
            self.tcpattemptfails = None
            self.tcpcurrestab = None
            self.tcpestabresets = None
            self.tcpinerrs = None
            self.tcpinsegs = None
            self.tcpmaxconn = None
            self.tcpoutrsts = None
            self.tcpoutsegs = None
            self.tcppassiveopens = None
            self.tcpretranssegs = None
            self.tcprtoalgorithm = None
            self.tcprtomax = None
            self.tcprtomin = None

        class TcpRtoAlgorithm_Enum(Enum):
            """
            TcpRtoAlgorithm_Enum

            The algorithm used to determine the timeout value
            used for retransmitting unacknowledged octets.

            """

            OTHER = 1

            CONSTANT = 2

            RSRE = 3

            VANJ = 4


            @staticmethod
            def _meta_info():
                from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                return meta._meta_table['RFC1213MIB.Tcp.TcpRtoAlgorithm_Enum']


        @property
        def _common_path(self):

            return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:tcp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.tcpactiveopens is not None:
                return True

            if self.tcpattemptfails is not None:
                return True

            if self.tcpcurrestab is not None:
                return True

            if self.tcpestabresets is not None:
                return True

            if self.tcpinerrs is not None:
                return True

            if self.tcpinsegs is not None:
                return True

            if self.tcpmaxconn is not None:
                return True

            if self.tcpoutrsts is not None:
                return True

            if self.tcpoutsegs is not None:
                return True

            if self.tcppassiveopens is not None:
                return True

            if self.tcpretranssegs is not None:
                return True

            if self.tcprtoalgorithm is not None:
                return True

            if self.tcprtomax is not None:
                return True

            if self.tcprtomin is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
            return meta._meta_table['RFC1213MIB.Tcp']['meta_info']


    class TcpConnTable(object):
        """
        A table containing TCP connection\-specific
        information.
        
        .. attribute:: tcpconnentry
        
        	Information about a particular current TCP connection.  An object of this type is transient, in that it ceases to exist when (or soon after) the connection makes the transition to the CLOSED state
        	**type**\: list of :py:class:`TcpConnEntry <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.TcpConnTable.TcpConnEntry>`
        
        

        """

        _prefix = 'rfc1213-mib'

        def __init__(self):
            self.parent = None
            self.tcpconnentry = YList()
            self.tcpconnentry.parent = self
            self.tcpconnentry.name = 'tcpconnentry'


        class TcpConnEntry(object):
            """
            Information about a particular current TCP
            connection.  An object of this type is transient,
            in that it ceases to exist when (or soon after)
            the connection makes the transition to the CLOSED
            state.
            
            .. attribute:: tcpconnlocaladdress
            
            	The local IP address for this TCP connection.  In the case of a connection in the listen state which is willing to accept connections for any IP interface associated with the node, the value 0.0.0.0 is used
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: tcpconnlocalport
            
            	The local port number for this TCP connection
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: tcpconnremaddress
            
            	The remote IP address for this TCP connection
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: tcpconnremport
            
            	The remote port number for this TCP connection
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: tcpconnstate
            
            	The state of this TCP connection.  The only value which may be set by a management station is deleteTCB(12).  Accordingly, it is appropriate for an agent to return a `badValue' response if a management station attempts to set this object to any other value.  If a management station sets this object to the value deleteTCB(12), then this has the effect of deleting the TCB (as defined in RFC 793) of the corresponding connection on the managed node, resulting in immediate termination of the connection.  As an implementation\-specific option, a RST segment may be sent from the managed node to the other TCP endpoint (note however that RST segments are not sent reliably)
            	**type**\: :py:class:`TcpConnState_Enum <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.TcpConnTable.TcpConnEntry.TcpConnState_Enum>`
            
            

            """

            _prefix = 'rfc1213-mib'

            def __init__(self):
                self.parent = None
                self.tcpconnlocaladdress = None
                self.tcpconnlocalport = None
                self.tcpconnremaddress = None
                self.tcpconnremport = None
                self.tcpconnstate = None

            class TcpConnState_Enum(Enum):
                """
                TcpConnState_Enum

                The state of this TCP connection.
                
                The only value which may be set by a management
                station is deleteTCB(12).  Accordingly, it is
                appropriate for an agent to return a `badValue'
                response if a management station attempts to set
                this object to any other value.
                
                If a management station sets this object to the
                value deleteTCB(12), then this has the effect of
                deleting the TCB (as defined in RFC 793) of the
                corresponding connection on the managed node,
                resulting in immediate termination of the
                connection.
                
                As an implementation\-specific option, a RST
                segment may be sent from the managed node to the
                other TCP endpoint (note however that RST segments
                are not sent reliably).

                """

                CLOSED = 1

                LISTEN = 2

                SYNSENT = 3

                SYNRECEIVED = 4

                ESTABLISHED = 5

                FINWAIT1 = 6

                FINWAIT2 = 7

                CLOSEWAIT = 8

                LASTACK = 9

                CLOSING = 10

                TIMEWAIT = 11

                DELETETCB = 12


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                    return meta._meta_table['RFC1213MIB.TcpConnTable.TcpConnEntry.TcpConnState_Enum']


            @property
            def _common_path(self):
                if self.tcpconnlocaladdress is None:
                    raise YPYDataValidationError('Key property tcpconnlocaladdress is None')
                if self.tcpconnlocalport is None:
                    raise YPYDataValidationError('Key property tcpconnlocalport is None')
                if self.tcpconnremaddress is None:
                    raise YPYDataValidationError('Key property tcpconnremaddress is None')
                if self.tcpconnremport is None:
                    raise YPYDataValidationError('Key property tcpconnremport is None')

                return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:tcpConnTable/RFC1213-MIB:tcpConnEntry[RFC1213-MIB:tcpConnLocalAddress = ' + str(self.tcpconnlocaladdress) + '][RFC1213-MIB:tcpConnLocalPort = ' + str(self.tcpconnlocalport) + '][RFC1213-MIB:tcpConnRemAddress = ' + str(self.tcpconnremaddress) + '][RFC1213-MIB:tcpConnRemPort = ' + str(self.tcpconnremport) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.tcpconnlocaladdress is not None:
                    return True

                if self.tcpconnlocalport is not None:
                    return True

                if self.tcpconnremaddress is not None:
                    return True

                if self.tcpconnremport is not None:
                    return True

                if self.tcpconnstate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                return meta._meta_table['RFC1213MIB.TcpConnTable.TcpConnEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:tcpConnTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.tcpconnentry is not None:
                for child_ref in self.tcpconnentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
            return meta._meta_table['RFC1213MIB.TcpConnTable']['meta_info']


    class Udp(object):
        """
        
        
        .. attribute:: udpindatagrams
        
        	The total number of UDP datagrams delivered to UDP users
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpinerrors
        
        	The number of received UDP datagrams that could not be delivered for reasons other than the lack of an application at the destination port
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpnoports
        
        	The total number of received UDP datagrams for which there was no application at the destination port
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpoutdatagrams
        
        	The total number of UDP datagrams sent from this entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'rfc1213-mib'

        def __init__(self):
            self.parent = None
            self.udpindatagrams = None
            self.udpinerrors = None
            self.udpnoports = None
            self.udpoutdatagrams = None

        @property
        def _common_path(self):

            return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:udp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.udpindatagrams is not None:
                return True

            if self.udpinerrors is not None:
                return True

            if self.udpnoports is not None:
                return True

            if self.udpoutdatagrams is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
            return meta._meta_table['RFC1213MIB.Udp']['meta_info']


    class UdpTable(object):
        """
        A table containing UDP listener information.
        
        .. attribute:: udpentry
        
        	Information about a particular current UDP listener
        	**type**\: list of :py:class:`UdpEntry <ydk.models.rfc1213.RFC1213_MIB.RFC1213MIB.UdpTable.UdpEntry>`
        
        

        """

        _prefix = 'rfc1213-mib'

        def __init__(self):
            self.parent = None
            self.udpentry = YList()
            self.udpentry.parent = self
            self.udpentry.name = 'udpentry'


        class UdpEntry(object):
            """
            Information about a particular current UDP
            listener.
            
            .. attribute:: udplocaladdress
            
            	The local IP address for this UDP listener.  In the case of a UDP listener which is willing to accept datagrams for any IP interface associated with the node, the value 0.0.0.0 is used
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: udplocalport
            
            	The local port number for this UDP listener
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'rfc1213-mib'

            def __init__(self):
                self.parent = None
                self.udplocaladdress = None
                self.udplocalport = None

            @property
            def _common_path(self):
                if self.udplocaladdress is None:
                    raise YPYDataValidationError('Key property udplocaladdress is None')
                if self.udplocalport is None:
                    raise YPYDataValidationError('Key property udplocalport is None')

                return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:udpTable/RFC1213-MIB:udpEntry[RFC1213-MIB:udpLocalAddress = ' + str(self.udplocaladdress) + '][RFC1213-MIB:udpLocalPort = ' + str(self.udplocalport) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.udplocaladdress is not None:
                    return True

                if self.udplocalport is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
                return meta._meta_table['RFC1213MIB.UdpTable.UdpEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1213-MIB:RFC1213-MIB/RFC1213-MIB:udpTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.udpentry is not None:
                for child_ref in self.udpentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
            return meta._meta_table['RFC1213MIB.UdpTable']['meta_info']

    @property
    def _common_path(self):

        return '/RFC1213-MIB:RFC1213-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.attable is not None and self.attable._has_data():
            return True

        if self.attable is not None and self.attable.is_presence():
            return True

        if self.egp is not None and self.egp._has_data():
            return True

        if self.egp is not None and self.egp.is_presence():
            return True

        if self.egpneightable is not None and self.egpneightable._has_data():
            return True

        if self.egpneightable is not None and self.egpneightable.is_presence():
            return True

        if self.icmp is not None and self.icmp._has_data():
            return True

        if self.icmp is not None and self.icmp.is_presence():
            return True

        if self.iftable is not None and self.iftable._has_data():
            return True

        if self.iftable is not None and self.iftable.is_presence():
            return True

        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.interfaces is not None and self.interfaces.is_presence():
            return True

        if self.ip is not None and self.ip._has_data():
            return True

        if self.ip is not None and self.ip.is_presence():
            return True

        if self.ipaddrtable is not None and self.ipaddrtable._has_data():
            return True

        if self.ipaddrtable is not None and self.ipaddrtable.is_presence():
            return True

        if self.ipnettomediatable is not None and self.ipnettomediatable._has_data():
            return True

        if self.ipnettomediatable is not None and self.ipnettomediatable.is_presence():
            return True

        if self.iproutetable is not None and self.iproutetable._has_data():
            return True

        if self.iproutetable is not None and self.iproutetable.is_presence():
            return True

        if self.snmp is not None and self.snmp._has_data():
            return True

        if self.snmp is not None and self.snmp.is_presence():
            return True

        if self.system is not None and self.system._has_data():
            return True

        if self.system is not None and self.system.is_presence():
            return True

        if self.tcp is not None and self.tcp._has_data():
            return True

        if self.tcp is not None and self.tcp.is_presence():
            return True

        if self.tcpconntable is not None and self.tcpconntable._has_data():
            return True

        if self.tcpconntable is not None and self.tcpconntable.is_presence():
            return True

        if self.udp is not None and self.udp._has_data():
            return True

        if self.udp is not None and self.udp.is_presence():
            return True

        if self.udptable is not None and self.udptable._has_data():
            return True

        if self.udptable is not None and self.udptable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.rfc1213._meta import _RFC1213_MIB as meta
        return meta._meta_table['RFC1213MIB']['meta_info']


