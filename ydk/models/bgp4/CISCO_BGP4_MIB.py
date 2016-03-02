""" CISCO_BGP4_MIB 

An extension to the IETF BGP4 MIB module defined in
RFC 1657.

Following is the terminology associated with Border
Gateway Protocol(BGP).

UPDATE message
    UPDATE messages are used to transfer routing 
    information between BGP peers. An UPDATE message 
    is used to advertise a single feasible route to a
    peer, or to withdraw multiple unfeasible routes 
    from service.                 

Adj\-RIBs\-In 
   The Adj\-RIBs\-In store routing information that has
   been learned from inbound UPDATE messages. Their 
   contents represent routes that are available as an 
   input to the Decision Process.

Loc\-RIB(BGP table) 
   The Loc\-RIB contains the local routing information
   that the BGP speaker has selected by applying its 
   local policies to the routing information contained 
   in its Adj\-RIBs\-In.

Adj\-RIBs\-Out 
   The Adj\-RIBs\-Out store the information that the
   local BGP speaker has selected for advertisement to 
   its peers. The routing information stored in the 
   Adj\-RIBs\-Out will be carried in the local BGP 
   speaker's UPDATE messages and advertised to its
   peers.

Path Attributes
   A variable length sequence of path attributes is 
   present in every UPDATE. Each path attribute is a 
   triple <attribute type, attribute length, 
   attribute value> of variable length. 

Network Layer Reachability Information(NLRI)
   A variable length field present in UPDATE messages
   which contains a list of Network Layer address 
   prefixes. 

Address Family Identifier(AFI) 
   Primary identifier to indicate the type of the 
   Network Layer Reachability Information(NLRI) being 
   carried.

Subsequent Address Family Identifier(SAFI) 
   Secondary identifier to indicate the type of the 
   Network Layer Reachability Information(NLRI) being 
   carried.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum

class CbgpSafi_Enum(Enum):
    """
    CbgpSafi_Enum

    Subsequent Address Family Identifier(SAFI) is used
    by BGP speaker to indicate the type of the the Network
    Layer Reachability Information(NLRI) being carried. 
    RFC\-2858 has defined the following values for SAFI.
    1 \- Network Layer Reachability Information used for 
        unicast forwarding
    2 \- Network Layer Reachability Information used for 
        multicast forwarding
    3 \- Network Layer Reachability Information used for 
        both unicast and multicast forwarding. 
    SAFI values 128 through 255 are for private use.

    """

    UNICAST = 1

    MULTICAST = 2

    UNICASTANDMULTICAST = 3

    VPN = 128


    @staticmethod
    def _meta_info():
        from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
        return meta._meta_table['CbgpSafi_Enum']



class CISCOBGP4MIB(object):
    """
    
    
    .. attribute:: cbgpglobal
    
    	
    	**type**\: :py:class:`CbgpGlobal <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpGlobal>`
    
    .. attribute:: cbgppeer2addrfamilyprefixtable
    
    	This table contains prefix related information related to address families supported by a peer. Supported address families of a peer are known during BGP connection establishment. When a new supported address family is known, this table is updated with a new entry. When an address family is not supported any more, corresponding entry is deleted from the table
    	**type**\: :py:class:`CbgpPeer2AddrFamilyPrefixTable <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2AddrFamilyPrefixTable>`
    
    .. attribute:: cbgppeer2addrfamilytable
    
    	This table contains information related to address families supported by a peer. Supported address families of a peer are known during BGP connection establishment. When a new supported address family is known, this table is updated with a new entry. When an address family is not supported any more, corresponding entry is deleted from the table
    	**type**\: :py:class:`CbgpPeer2AddrFamilyTable <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2AddrFamilyTable>`
    
    .. attribute:: cbgppeer2capstable
    
    	This table contains the capabilities that are supported by a peer. Capabilities of a peer are received during BGP connection establishment. Values corresponding to each received capability are stored in this table. When a new capability is received, this table is updated with a new entry. When an existing capability is not received during the latest connection establishment, the corresponding entry is deleted from the table
    	**type**\: :py:class:`CbgpPeer2CapsTable <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2CapsTable>`
    
    .. attribute:: cbgppeer2table
    
    	BGP peer table.  This table contains, one entry per BGP peer, information about the connections with BGP peers
    	**type**\: :py:class:`CbgpPeer2Table <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2Table>`
    
    .. attribute:: cbgppeeraddrfamilyprefixtable
    
    	This table contains prefix related information related to address families supported by a peer.  Supported address families of a peer are known  during BGP connection establishment. When a new  supported address family is known, this table  is updated with a new entry. When an address  family is not supported any more, corresponding  entry is deleted from the table
    	**type**\: :py:class:`CbgpPeerAddrFamilyPrefixTable <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeerAddrFamilyPrefixTable>`
    
    .. attribute:: cbgppeeraddrfamilytable
    
    	This table contains information related to address families supported by a peer. Supported address families of a peer are known during BGP  connection establishment. When a new supported  address family is known, this table is updated  with a new entry. When an address family is not  supported any more, corresponding entry is deleted  from the table
    	**type**\: :py:class:`CbgpPeerAddrFamilyTable <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeerAddrFamilyTable>`
    
    .. attribute:: cbgppeercapstable
    
    	This table contains the capabilities that are supported by a peer. Capabilities of a peer are  received during BGP connection establishment. Values corresponding to each received capability are stored in this table. When a new capability  is received, this table is updated with a new  entry. When an existing capability is not received  during the latest connection establishment, the  corresponding entry is deleted from the table
    	**type**\: :py:class:`CbgpPeerCapsTable <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeerCapsTable>`
    
    .. attribute:: cbgproutetable
    
    	This table contains information about routes to destination networks from all BGP4 peers.  Since  BGP4 can carry routes for multiple Network Layer  protocols, this table has the Address Family  Identifier(AFI) of the Network Layer protocol as the  first index. Further for a given AFI, routes carried by BGP4 are distinguished based on Subsequent Address  Family Identifiers(SAFI).  Hence that is used as the second index.  Conceptually there is a separate Loc\-RIB maintained by the BGP speaker for each combination of  AFI and SAFI supported by it
    	**type**\: :py:class:`CbgpRouteTable <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpRouteTable>`
    
    

    """

    _prefix = 'cisco-bgp4'
    _revision = '2010-09-30'

    def __init__(self):
        self.cbgpglobal = CISCOBGP4MIB.CbgpGlobal()
        self.cbgpglobal.parent = self
        self.cbgppeer2addrfamilyprefixtable = CISCOBGP4MIB.CbgpPeer2AddrFamilyPrefixTable()
        self.cbgppeer2addrfamilyprefixtable.parent = self
        self.cbgppeer2addrfamilytable = CISCOBGP4MIB.CbgpPeer2AddrFamilyTable()
        self.cbgppeer2addrfamilytable.parent = self
        self.cbgppeer2capstable = CISCOBGP4MIB.CbgpPeer2CapsTable()
        self.cbgppeer2capstable.parent = self
        self.cbgppeer2table = CISCOBGP4MIB.CbgpPeer2Table()
        self.cbgppeer2table.parent = self
        self.cbgppeeraddrfamilyprefixtable = CISCOBGP4MIB.CbgpPeerAddrFamilyPrefixTable()
        self.cbgppeeraddrfamilyprefixtable.parent = self
        self.cbgppeeraddrfamilytable = CISCOBGP4MIB.CbgpPeerAddrFamilyTable()
        self.cbgppeeraddrfamilytable.parent = self
        self.cbgppeercapstable = CISCOBGP4MIB.CbgpPeerCapsTable()
        self.cbgppeercapstable.parent = self
        self.cbgproutetable = CISCOBGP4MIB.CbgpRouteTable()
        self.cbgproutetable.parent = self


    class CbgpGlobal(object):
        """
        
        
        .. attribute:: cbgplocalas
        
        	The local autonomous system (AS) number
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cbgpnotifsenable
        
        	Indicates whether the specific notifications are enabled.  If notifsEnable(0) bit is set to 1, then the notifications defined in ciscoBgp4NotificationsGroup1 are enabled;  If notifsPeer2Enable(1) bit is set to 1, then the notifications defined in ciscoBgp4Peer2NotificationsGroup are enabled
        	**type**\: :py:class:`CbgpNotifsEnable_Bits <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpGlobal.CbgpNotifsEnable_Bits>`
        
        

        """

        _prefix = 'cisco-bgp4'
        _revision = '2010-09-30'

        def __init__(self):
            self.parent = None
            self.cbgplocalas = None
            self.cbgpnotifsenable = CISCOBGP4MIB.CbgpGlobal.CbgpNotifsEnable_Bits()

        class CbgpNotifsEnable_Bits(FixedBitsDict):
            """
            CbgpNotifsEnable_Bits

            Indicates whether the specific notifications are
            enabled. 
            If notifsEnable(0) bit is set to 1,
            then the notifications defined in
            ciscoBgp4NotificationsGroup1 are enabled; 
            If notifsPeer2Enable(1) bit is set to 1,
            then the notifications defined in
            ciscoBgp4Peer2NotificationsGroup are enabled.
            Keys are:- notifsEnable , notifsPeer2Enable

            """

            def __init__(self):
                self._dictionary = { 
                    'notifsEnable':False,
                    'notifsPeer2Enable':False,
                }
                self._pos_map = { 
                    'notifsEnable':0,
                    'notifsPeer2Enable':1,
                }

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpGlobal'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbgplocalas is not None:
                return True

            if self.cbgpnotifsenable is not None:
                if self.cbgpnotifsenable._has_data():
                    return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CISCOBGP4MIB.CbgpGlobal']['meta_info']


    class CbgpPeer2AddrFamilyPrefixTable(object):
        """
        This table contains prefix related information
        related to address families supported by a peer.
        Supported address families of a peer are known
        during BGP connection establishment. When a new
        supported address family is known, this table
        is updated with a new entry. When an address
        family is not supported any more, corresponding
        entry is deleted from the table.
        
        .. attribute:: cbgppeer2addrfamilyprefixentry
        
        	An entry is identified by an AFI/SAFI pair and peer address. It contains information associated with route prefixes belonging to an address family
        	**type**\: list of :py:class:`CbgpPeer2AddrFamilyPrefixEntry <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2AddrFamilyPrefixTable.CbgpPeer2AddrFamilyPrefixEntry>`
        
        

        """

        _prefix = 'cisco-bgp4'
        _revision = '2010-09-30'

        def __init__(self):
            self.parent = None
            self.cbgppeer2addrfamilyprefixentry = YList()
            self.cbgppeer2addrfamilyprefixentry.parent = self
            self.cbgppeer2addrfamilyprefixentry.name = 'cbgppeer2addrfamilyprefixentry'


        class CbgpPeer2AddrFamilyPrefixEntry(object):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains information associated
            with route prefixes belonging to an address family.
            
            .. attribute:: cbgppeer2addrfamilyafi
            
            	
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cbgppeer2addrfamilysafi
            
            	
            	**type**\: :py:class:`CbgpSafi_Enum <ydk.models.bgp4.CISCO_BGP4_MIB.CbgpSafi_Enum>`
            
            .. attribute:: cbgppeer2remoteaddr
            
            	
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cbgppeer2type
            
            	
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cbgppeer2acceptedprefixes
            
            	Number of accepted route prefixes on this connection, which belong to an address family
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2advertisedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family is advertised on this connection. It is initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2deniedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family, received on this connection is denied. It is initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2prefixadminlimit
            
            	Max number of route prefixes accepted for an address family on this connection
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cbgppeer2prefixclearthreshold
            
            	Prefix threshold value (%) for an address family on this connection at which SNMP clear notification is generated if prefix threshold notification is already generated
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: cbgppeer2prefixthreshold
            
            	Prefix threshold value (%) for an address family on this connection at which warning message stating the prefix count is crossed the threshold or corresponding SNMP notification is generated
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: cbgppeer2suppressedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family is suppressed from being sent on this connection. It is initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2withdrawnprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family, is withdrawn on this connection. It is initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-bgp4'
            _revision = '2010-09-30'

            def __init__(self):
                self.parent = None
                self.cbgppeer2addrfamilyafi = None
                self.cbgppeer2addrfamilysafi = None
                self.cbgppeer2remoteaddr = None
                self.cbgppeer2type = None
                self.cbgppeer2acceptedprefixes = None
                self.cbgppeer2advertisedprefixes = None
                self.cbgppeer2deniedprefixes = None
                self.cbgppeer2prefixadminlimit = None
                self.cbgppeer2prefixclearthreshold = None
                self.cbgppeer2prefixthreshold = None
                self.cbgppeer2suppressedprefixes = None
                self.cbgppeer2withdrawnprefixes = None

            @property
            def _common_path(self):
                if self.cbgppeer2addrfamilyafi is None:
                    raise YPYDataValidationError('Key property cbgppeer2addrfamilyafi is None')
                if self.cbgppeer2addrfamilysafi is None:
                    raise YPYDataValidationError('Key property cbgppeer2addrfamilysafi is None')
                if self.cbgppeer2remoteaddr is None:
                    raise YPYDataValidationError('Key property cbgppeer2remoteaddr is None')
                if self.cbgppeer2type is None:
                    raise YPYDataValidationError('Key property cbgppeer2type is None')

                return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeer2AddrFamilyPrefixTable/CISCO-BGP4-MIB:cbgpPeer2AddrFamilyPrefixEntry[CISCO-BGP4-MIB:cbgpPeer2AddrFamilyAfi = ' + str(self.cbgppeer2addrfamilyafi) + '][CISCO-BGP4-MIB:cbgpPeer2AddrFamilySafi = ' + str(self.cbgppeer2addrfamilysafi) + '][CISCO-BGP4-MIB:cbgpPeer2RemoteAddr = ' + str(self.cbgppeer2remoteaddr) + '][CISCO-BGP4-MIB:cbgpPeer2Type = ' + str(self.cbgppeer2type) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbgppeer2addrfamilyafi is not None:
                    return True

                if self.cbgppeer2addrfamilysafi is not None:
                    return True

                if self.cbgppeer2remoteaddr is not None:
                    return True

                if self.cbgppeer2type is not None:
                    return True

                if self.cbgppeer2acceptedprefixes is not None:
                    return True

                if self.cbgppeer2advertisedprefixes is not None:
                    return True

                if self.cbgppeer2deniedprefixes is not None:
                    return True

                if self.cbgppeer2prefixadminlimit is not None:
                    return True

                if self.cbgppeer2prefixclearthreshold is not None:
                    return True

                if self.cbgppeer2prefixthreshold is not None:
                    return True

                if self.cbgppeer2suppressedprefixes is not None:
                    return True

                if self.cbgppeer2withdrawnprefixes is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
                return meta._meta_table['CISCOBGP4MIB.CbgpPeer2AddrFamilyPrefixTable.CbgpPeer2AddrFamilyPrefixEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeer2AddrFamilyPrefixTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbgppeer2addrfamilyprefixentry is not None:
                for child_ref in self.cbgppeer2addrfamilyprefixentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CISCOBGP4MIB.CbgpPeer2AddrFamilyPrefixTable']['meta_info']


    class CbgpPeer2AddrFamilyTable(object):
        """
        This table contains information related to
        address families supported by a peer. Supported
        address families of a peer are known during BGP
        connection establishment. When a new supported
        address family is known, this table is updated
        with a new entry. When an address family is not
        supported any more, corresponding entry is deleted
        from the table.
        
        .. attribute:: cbgppeer2addrfamilyentry
        
        	An entry is identified by an AFI/SAFI pair and peer address. It contains names associated with an address family
        	**type**\: list of :py:class:`CbgpPeer2AddrFamilyEntry <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2AddrFamilyTable.CbgpPeer2AddrFamilyEntry>`
        
        

        """

        _prefix = 'cisco-bgp4'
        _revision = '2010-09-30'

        def __init__(self):
            self.parent = None
            self.cbgppeer2addrfamilyentry = YList()
            self.cbgppeer2addrfamilyentry.parent = self
            self.cbgppeer2addrfamilyentry.name = 'cbgppeer2addrfamilyentry'


        class CbgpPeer2AddrFamilyEntry(object):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains names associated with
            an address family.
            
            .. attribute:: cbgppeer2addrfamilyafi
            
            	The AFI index of the entry. An implementation is only required to support IPv4 unicast and VPNv4 (Value \- 1) address families
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cbgppeer2addrfamilysafi
            
            	The SAFI index of the entry. An implementation is only required to support IPv4 unicast(Value \- 1) and VPNv4( Value \- 128) address families
            	**type**\: :py:class:`CbgpSafi_Enum <ydk.models.bgp4.CISCO_BGP4_MIB.CbgpSafi_Enum>`
            
            .. attribute:: cbgppeer2remoteaddr
            
            	
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cbgppeer2type
            
            	
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cbgppeer2addrfamilyname
            
            	Implementation specific Address Family name
            	**type**\: str
            
            	**range:** 0..255
            
            

            """

            _prefix = 'cisco-bgp4'
            _revision = '2010-09-30'

            def __init__(self):
                self.parent = None
                self.cbgppeer2addrfamilyafi = None
                self.cbgppeer2addrfamilysafi = None
                self.cbgppeer2remoteaddr = None
                self.cbgppeer2type = None
                self.cbgppeer2addrfamilyname = None

            @property
            def _common_path(self):
                if self.cbgppeer2addrfamilyafi is None:
                    raise YPYDataValidationError('Key property cbgppeer2addrfamilyafi is None')
                if self.cbgppeer2addrfamilysafi is None:
                    raise YPYDataValidationError('Key property cbgppeer2addrfamilysafi is None')
                if self.cbgppeer2remoteaddr is None:
                    raise YPYDataValidationError('Key property cbgppeer2remoteaddr is None')
                if self.cbgppeer2type is None:
                    raise YPYDataValidationError('Key property cbgppeer2type is None')

                return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeer2AddrFamilyTable/CISCO-BGP4-MIB:cbgpPeer2AddrFamilyEntry[CISCO-BGP4-MIB:cbgpPeer2AddrFamilyAfi = ' + str(self.cbgppeer2addrfamilyafi) + '][CISCO-BGP4-MIB:cbgpPeer2AddrFamilySafi = ' + str(self.cbgppeer2addrfamilysafi) + '][CISCO-BGP4-MIB:cbgpPeer2RemoteAddr = ' + str(self.cbgppeer2remoteaddr) + '][CISCO-BGP4-MIB:cbgpPeer2Type = ' + str(self.cbgppeer2type) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbgppeer2addrfamilyafi is not None:
                    return True

                if self.cbgppeer2addrfamilysafi is not None:
                    return True

                if self.cbgppeer2remoteaddr is not None:
                    return True

                if self.cbgppeer2type is not None:
                    return True

                if self.cbgppeer2addrfamilyname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
                return meta._meta_table['CISCOBGP4MIB.CbgpPeer2AddrFamilyTable.CbgpPeer2AddrFamilyEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeer2AddrFamilyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbgppeer2addrfamilyentry is not None:
                for child_ref in self.cbgppeer2addrfamilyentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CISCOBGP4MIB.CbgpPeer2AddrFamilyTable']['meta_info']


    class CbgpPeer2CapsTable(object):
        """
        This table contains the capabilities that are
        supported by a peer. Capabilities of a peer are
        received during BGP connection establishment.
        Values corresponding to each received capability
        are stored in this table. When a new capability
        is received, this table is updated with a new
        entry. When an existing capability is not received
        during the latest connection establishment, the
        corresponding entry is deleted from the table.
        
        .. attribute:: cbgppeer2capsentry
        
        	Each entry represents a capability received from a peer with a particular code and an index. When a capability is received multiple times with different values during a BGP connection establishment, corresponding entries are differentiated with indices
        	**type**\: list of :py:class:`CbgpPeer2CapsEntry <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2CapsTable.CbgpPeer2CapsEntry>`
        
        

        """

        _prefix = 'cisco-bgp4'
        _revision = '2010-09-30'

        def __init__(self):
            self.parent = None
            self.cbgppeer2capsentry = YList()
            self.cbgppeer2capsentry.parent = self
            self.cbgppeer2capsentry.name = 'cbgppeer2capsentry'


        class CbgpPeer2CapsEntry(object):
            """
            Each entry represents a capability received from a
            peer with a particular code and an index. When a
            capability is received multiple times with different
            values during a BGP connection establishment,
            corresponding entries are differentiated with indices.
            
            .. attribute:: cbgppeer2capcode
            
            	The BGP Capability Advertisement Capability Code
            	**type**\: :py:class:`CbgpPeer2CapCode_Enum <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2CapsTable.CbgpPeer2CapsEntry.CbgpPeer2CapCode_Enum>`
            
            .. attribute:: cbgppeer2capindex
            
            	Multiple instances of a given capability may be sent by a BGP speaker.  This variable is used to index them
            	**type**\: int
            
            	**range:** 1..128
            
            .. attribute:: cbgppeer2remoteaddr
            
            	
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cbgppeer2type
            
            	
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cbgppeer2capvalue
            
            	The value of the announced capability. This MIB object value is organized as given below,     Capability \: Route Refresh Capability                  4\-Byte AS Capability                  Null string     Capability \: Multiprotocol Extensions       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     Capability \: Graceful Restart       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Restart Flags (4 bits)           \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Restart Time in seconds (12 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Flags for Address Family (8 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| ...                              \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Flags for Address Family (8 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     Capability \: Additional Paths       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Send/Receive (8 bits)            \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
            	**type**\: str
            
            	**range:** 0..255
            
            

            """

            _prefix = 'cisco-bgp4'
            _revision = '2010-09-30'

            def __init__(self):
                self.parent = None
                self.cbgppeer2capcode = None
                self.cbgppeer2capindex = None
                self.cbgppeer2remoteaddr = None
                self.cbgppeer2type = None
                self.cbgppeer2capvalue = None

            class CbgpPeer2CapCode_Enum(Enum):
                """
                CbgpPeer2CapCode_Enum

                The BGP Capability Advertisement Capability Code.

                """

                MULTIPROTOCOL = 1

                ROUTEREFRESH = 2

                GRACEFULRESTART = 64

                FOURBYTEAS = 65

                ADDPATH = 69

                ROUTEREFRESHOLD = 128


                @staticmethod
                def _meta_info():
                    from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
                    return meta._meta_table['CISCOBGP4MIB.CbgpPeer2CapsTable.CbgpPeer2CapsEntry.CbgpPeer2CapCode_Enum']


            @property
            def _common_path(self):
                if self.cbgppeer2capcode is None:
                    raise YPYDataValidationError('Key property cbgppeer2capcode is None')
                if self.cbgppeer2capindex is None:
                    raise YPYDataValidationError('Key property cbgppeer2capindex is None')
                if self.cbgppeer2remoteaddr is None:
                    raise YPYDataValidationError('Key property cbgppeer2remoteaddr is None')
                if self.cbgppeer2type is None:
                    raise YPYDataValidationError('Key property cbgppeer2type is None')

                return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeer2CapsTable/CISCO-BGP4-MIB:cbgpPeer2CapsEntry[CISCO-BGP4-MIB:cbgpPeer2CapCode = ' + str(self.cbgppeer2capcode) + '][CISCO-BGP4-MIB:cbgpPeer2CapIndex = ' + str(self.cbgppeer2capindex) + '][CISCO-BGP4-MIB:cbgpPeer2RemoteAddr = ' + str(self.cbgppeer2remoteaddr) + '][CISCO-BGP4-MIB:cbgpPeer2Type = ' + str(self.cbgppeer2type) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbgppeer2capcode is not None:
                    return True

                if self.cbgppeer2capindex is not None:
                    return True

                if self.cbgppeer2remoteaddr is not None:
                    return True

                if self.cbgppeer2type is not None:
                    return True

                if self.cbgppeer2capvalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
                return meta._meta_table['CISCOBGP4MIB.CbgpPeer2CapsTable.CbgpPeer2CapsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeer2CapsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbgppeer2capsentry is not None:
                for child_ref in self.cbgppeer2capsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CISCOBGP4MIB.CbgpPeer2CapsTable']['meta_info']


    class CbgpPeer2Table(object):
        """
        BGP peer table.  This table contains,
        one entry per BGP peer, information about
        the connections with BGP peers.
        
        .. attribute:: cbgppeer2entry
        
        	Entry containing information about the connection with a BGP peer
        	**type**\: list of :py:class:`CbgpPeer2Entry <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry>`
        
        

        """

        _prefix = 'cisco-bgp4'
        _revision = '2010-09-30'

        def __init__(self):
            self.parent = None
            self.cbgppeer2entry = YList()
            self.cbgppeer2entry.parent = self
            self.cbgppeer2entry.name = 'cbgppeer2entry'


        class CbgpPeer2Entry(object):
            """
            Entry containing information about the
            connection with a BGP peer.
            
            .. attribute:: cbgppeer2remoteaddr
            
            	The remote IP address of this entry's BGP peer
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cbgppeer2type
            
            	Represents the type of Peer address stored in cbgpPeer2Entry
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cbgppeer2adminstatus
            
            	The desired state of the BGP connection. A transition from 'stop' to 'start' will cause the BGP Manual Start Event to be generated. A transition from 'start' to 'stop' will cause the BGP Manual Stop Event to be generated. This parameter can be used to restart BGP peer connections.  Care should be used in providing write access to this object without adequate authentication
            	**type**\: :py:class:`CbgpPeer2AdminStatus_Enum <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry.CbgpPeer2AdminStatus_Enum>`
            
            .. attribute:: cbgppeer2connectretryinterval
            
            	Time interval (in seconds) for the ConnectRetry timer.  The suggested value for this timer is 120 seconds
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: cbgppeer2fsmestablishedtime
            
            	This timer indicates how long (in seconds) this peer has been in the established state or how long since this peer was last in the established state.  It is set to zero when a new peer is configured or when the router is booted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2fsmestablishedtransitions
            
            	The total number of times the BGP FSM transitioned into the established state for this peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2holdtime
            
            	Time interval (in seconds) for the Hold Timer established with the peer.  The value of this object is calculated by this BGP speaker, using the smaller of the values in cbgpPeer2HoldTimeConfigured and the Hold Time received in the OPEN message.  This value must be at least three seconds if it is not zero (0).  If the Hold Timer has not been established with the peer this object MUST have a value of zero (0).  If the cbgpPeer2HoldTimeConfigured object has a value of (0), then this object MUST have a value of (0)
            	**type**\: int
            
            	**range:** 0 \| 3..65535
            
            .. attribute:: cbgppeer2holdtimeconfigured
            
            	Time interval (in seconds) for the Hold Time configured for this BGP speaker with this peer.  This value is placed in an OPEN message sent to this peer by this BGP speaker, and is compared with the Hold Time field in an OPEN message received from the peer when determining the Hold Time (cbgpPeer2HoldTime) with the peer. This value must not be less than three seconds if it is not zero (0).  If it is zero (0), the Hold Time is NOT to be established with the peer.  The suggested value for this timer is 90 seconds
            	**type**\: int
            
            	**range:** 0 \| 3..65535
            
            .. attribute:: cbgppeer2intotalmessages
            
            	The total number of messages received from the remote peer on this connection
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2inupdateelapsedtime
            
            	Elapsed time (in seconds) since the last BGP UPDATE message was received from the peer. Each time cbgpPeer2InUpdates is incremented, the value of this object is set to zero (0)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2inupdates
            
            	The number of BGP UPDATE messages received on this connection
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2keepalive
            
            	Time interval (in seconds) for the KeepAlive timer established with the peer.  The value of this object is calculated by this BGP speaker such that, when compared with cbgpPeer2HoldTime, it has the same proportion that cbgpPeer2KeepAliveConfigured has, compared with cbgpPeer2HoldTimeConfigured.  If the KeepAlive timer has not been established with the peer, this object MUST have a value of zero (0).  If the of cbgpPeer2KeepAliveConfigured object has a value of (0), then this object MUST have a value of (0)
            	**type**\: int
            
            	**range:** 0..21845
            
            .. attribute:: cbgppeer2keepaliveconfigured
            
            	Time interval (in seconds) for the KeepAlive timer configured for this BGP speaker with this peer.  The value of this object will only determine the KEEPALIVE messages' frequency relative to the value specified in cbgpPeer2HoldTimeConfigured; the actual time interval for the KEEPALIVE messages is indicated by cbgpPeer2KeepAlive.  A reasonable maximum value for this timer would be one third of that of cbgpPeer2HoldTimeConfigured. If the value of this object is zero (0), no periodical KEEPALIVE messages are sent to the peer after the BGP connection has been established.  The suggested value for this timer is 30 seconds
            	**type**\: int
            
            	**range:** 0..21845
            
            .. attribute:: cbgppeer2lasterror
            
            	The last error code and subcode seen by this peer on this connection.  If no error has occurred, this field is zero.  Otherwise, the first byte of this two byte OCTET STRING contains the error code, and the second byte contains the subcode
            	**type**\: str
            
            	**range:** 2
            
            .. attribute:: cbgppeer2lasterrortxt
            
            	Implementation specific error description for bgpPeerLastErrorReceived
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cbgppeer2localaddr
            
            	The local IP address of this entry's BGP connection
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cbgppeer2localas
            
            	The local AS number for this session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2localidentifier
            
            	The BGP Identifier of this entry's BGP peer
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cbgppeer2localport
            
            	The local port for the TCP connection between the BGP peers
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cbgppeer2minasoriginationinterval
            
            	Time interval (in seconds) for the MinASOriginationInterval timer. The suggested value for this timer is 15 seconds
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: cbgppeer2minrouteadvertisementinterval
            
            	Time interval (in seconds) for the MinRouteAdvertisementInterval timer. The suggested value for this timer is 30 seconds for EBGP connections and 5 seconds for IBGP connections
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: cbgppeer2negotiatedversion
            
            	The negotiated version of BGP running between the two peers.  This entry MUST be zero (0) unless the cbgpPeer2State is in the openconfirm or the established state.  Note that legal values for this object are between 0 and 255
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cbgppeer2outtotalmessages
            
            	The total number of messages transmitted to the remote peer on this connection
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2outupdates
            
            	The number of BGP UPDATE messages transmitted on this connection
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2prevstate
            
            	The BGP peer connection previous state
            	**type**\: :py:class:`CbgpPeer2PrevState_Enum <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry.CbgpPeer2PrevState_Enum>`
            
            .. attribute:: cbgppeer2remoteas
            
            	The remote autonomous system number received in the BGP OPEN message
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2remoteidentifier
            
            	The BGP Identifier of this entry's BGP peer. This entry MUST be 0.0.0.0 unless the cbgpPeer2State is in the openconfirm or the established state
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cbgppeer2remoteport
            
            	The remote port for the TCP connection between the BGP peers.  Note that the objects cbgpPeer2LocalAddr, cbgpPeer2LocalPort, cbgpPeer2RemoteAddr, and cbgpPeer2RemotePort provide the appropriate reference to the standard MIB TCP connection table
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cbgppeer2state
            
            	The BGP peer connection state
            	**type**\: :py:class:`CbgpPeer2State_Enum <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry.CbgpPeer2State_Enum>`
            
            

            """

            _prefix = 'cisco-bgp4'
            _revision = '2010-09-30'

            def __init__(self):
                self.parent = None
                self.cbgppeer2remoteaddr = None
                self.cbgppeer2type = None
                self.cbgppeer2adminstatus = None
                self.cbgppeer2connectretryinterval = None
                self.cbgppeer2fsmestablishedtime = None
                self.cbgppeer2fsmestablishedtransitions = None
                self.cbgppeer2holdtime = None
                self.cbgppeer2holdtimeconfigured = None
                self.cbgppeer2intotalmessages = None
                self.cbgppeer2inupdateelapsedtime = None
                self.cbgppeer2inupdates = None
                self.cbgppeer2keepalive = None
                self.cbgppeer2keepaliveconfigured = None
                self.cbgppeer2lasterror = None
                self.cbgppeer2lasterrortxt = None
                self.cbgppeer2localaddr = None
                self.cbgppeer2localas = None
                self.cbgppeer2localidentifier = None
                self.cbgppeer2localport = None
                self.cbgppeer2minasoriginationinterval = None
                self.cbgppeer2minrouteadvertisementinterval = None
                self.cbgppeer2negotiatedversion = None
                self.cbgppeer2outtotalmessages = None
                self.cbgppeer2outupdates = None
                self.cbgppeer2prevstate = None
                self.cbgppeer2remoteas = None
                self.cbgppeer2remoteidentifier = None
                self.cbgppeer2remoteport = None
                self.cbgppeer2state = None

            class CbgpPeer2AdminStatus_Enum(Enum):
                """
                CbgpPeer2AdminStatus_Enum

                The desired state of the BGP connection.
                A transition from 'stop' to 'start' will cause
                the BGP Manual Start Event to be generated.
                A transition from 'start' to 'stop' will cause
                the BGP Manual Stop Event to be generated.
                This parameter can be used to restart BGP peer
                connections.  Care should be used in providing
                write access to this object without adequate
                authentication.

                """

                STOP = 1

                START = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
                    return meta._meta_table['CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry.CbgpPeer2AdminStatus_Enum']


            class CbgpPeer2PrevState_Enum(Enum):
                """
                CbgpPeer2PrevState_Enum

                The BGP peer connection previous state.

                """

                NONE = 0

                IDLE = 1

                CONNECT = 2

                ACTIVE = 3

                OPENSENT = 4

                OPENCONFIRM = 5

                ESTABLISHED = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
                    return meta._meta_table['CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry.CbgpPeer2PrevState_Enum']


            class CbgpPeer2State_Enum(Enum):
                """
                CbgpPeer2State_Enum

                The BGP peer connection state.

                """

                IDLE = 1

                CONNECT = 2

                ACTIVE = 3

                OPENSENT = 4

                OPENCONFIRM = 5

                ESTABLISHED = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
                    return meta._meta_table['CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry.CbgpPeer2State_Enum']


            @property
            def _common_path(self):
                if self.cbgppeer2remoteaddr is None:
                    raise YPYDataValidationError('Key property cbgppeer2remoteaddr is None')
                if self.cbgppeer2type is None:
                    raise YPYDataValidationError('Key property cbgppeer2type is None')

                return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeer2Table/CISCO-BGP4-MIB:cbgpPeer2Entry[CISCO-BGP4-MIB:cbgpPeer2RemoteAddr = ' + str(self.cbgppeer2remoteaddr) + '][CISCO-BGP4-MIB:cbgpPeer2Type = ' + str(self.cbgppeer2type) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbgppeer2remoteaddr is not None:
                    return True

                if self.cbgppeer2type is not None:
                    return True

                if self.cbgppeer2adminstatus is not None:
                    return True

                if self.cbgppeer2connectretryinterval is not None:
                    return True

                if self.cbgppeer2fsmestablishedtime is not None:
                    return True

                if self.cbgppeer2fsmestablishedtransitions is not None:
                    return True

                if self.cbgppeer2holdtime is not None:
                    return True

                if self.cbgppeer2holdtimeconfigured is not None:
                    return True

                if self.cbgppeer2intotalmessages is not None:
                    return True

                if self.cbgppeer2inupdateelapsedtime is not None:
                    return True

                if self.cbgppeer2inupdates is not None:
                    return True

                if self.cbgppeer2keepalive is not None:
                    return True

                if self.cbgppeer2keepaliveconfigured is not None:
                    return True

                if self.cbgppeer2lasterror is not None:
                    return True

                if self.cbgppeer2lasterrortxt is not None:
                    return True

                if self.cbgppeer2localaddr is not None:
                    return True

                if self.cbgppeer2localas is not None:
                    return True

                if self.cbgppeer2localidentifier is not None:
                    return True

                if self.cbgppeer2localport is not None:
                    return True

                if self.cbgppeer2minasoriginationinterval is not None:
                    return True

                if self.cbgppeer2minrouteadvertisementinterval is not None:
                    return True

                if self.cbgppeer2negotiatedversion is not None:
                    return True

                if self.cbgppeer2outtotalmessages is not None:
                    return True

                if self.cbgppeer2outupdates is not None:
                    return True

                if self.cbgppeer2prevstate is not None:
                    return True

                if self.cbgppeer2remoteas is not None:
                    return True

                if self.cbgppeer2remoteidentifier is not None:
                    return True

                if self.cbgppeer2remoteport is not None:
                    return True

                if self.cbgppeer2state is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
                return meta._meta_table['CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeer2Table'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbgppeer2entry is not None:
                for child_ref in self.cbgppeer2entry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CISCOBGP4MIB.CbgpPeer2Table']['meta_info']


    class CbgpPeerAddrFamilyPrefixTable(object):
        """
        This table contains prefix related information
        related to address families supported by a peer. 
        Supported address families of a peer are known 
        during BGP connection establishment. When a new 
        supported address family is known, this table 
        is updated with a new entry. When an address 
        family is not supported any more, corresponding 
        entry is deleted from the table.
        
        .. attribute:: cbgppeeraddrfamilyprefixentry
        
        	An entry is identified by an AFI/SAFI pair and peer address. It contains information associated  with route prefixes belonging to an address family
        	**type**\: list of :py:class:`CbgpPeerAddrFamilyPrefixEntry <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeerAddrFamilyPrefixTable.CbgpPeerAddrFamilyPrefixEntry>`
        
        

        """

        _prefix = 'cisco-bgp4'
        _revision = '2010-09-30'

        def __init__(self):
            self.parent = None
            self.cbgppeeraddrfamilyprefixentry = YList()
            self.cbgppeeraddrfamilyprefixentry.parent = self
            self.cbgppeeraddrfamilyprefixentry.name = 'cbgppeeraddrfamilyprefixentry'


        class CbgpPeerAddrFamilyPrefixEntry(object):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains information associated 
            with route prefixes belonging to an address family.
            
            .. attribute:: bgppeerremoteaddr
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cbgppeeraddrfamilyafi
            
            	
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cbgppeeraddrfamilysafi
            
            	
            	**type**\: :py:class:`CbgpSafi_Enum <ydk.models.bgp4.CISCO_BGP4_MIB.CbgpSafi_Enum>`
            
            .. attribute:: cbgppeeracceptedprefixes
            
            	Number of accepted route prefixes on this connection, which belong to an address family
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeeradvertisedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family is advertised on this connection. It is initialized to zero when  the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeerdeniedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family, received on this  connection is denied. It is initialized to zero when  the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeerprefixadminlimit
            
            	Max number of route prefixes accepted for an address family on this connection
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cbgppeerprefixclearthreshold
            
            	Prefix threshold value (%) for an address family on this connection at which SNMP clear notification is generated if prefix threshold notification is already generated
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: cbgppeerprefixthreshold
            
            	Prefix threshold value (%) for an address family on this connection at which warning message stating the prefix count is crossed the threshold or  corresponding SNMP notification is generated
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: cbgppeersuppressedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family is suppressed from being sent on this connection. It is  initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeerwithdrawnprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family, is withdrawn on this connection. It is initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-bgp4'
            _revision = '2010-09-30'

            def __init__(self):
                self.parent = None
                self.bgppeerremoteaddr = None
                self.cbgppeeraddrfamilyafi = None
                self.cbgppeeraddrfamilysafi = None
                self.cbgppeeracceptedprefixes = None
                self.cbgppeeradvertisedprefixes = None
                self.cbgppeerdeniedprefixes = None
                self.cbgppeerprefixadminlimit = None
                self.cbgppeerprefixclearthreshold = None
                self.cbgppeerprefixthreshold = None
                self.cbgppeersuppressedprefixes = None
                self.cbgppeerwithdrawnprefixes = None

            @property
            def _common_path(self):
                if self.bgppeerremoteaddr is None:
                    raise YPYDataValidationError('Key property bgppeerremoteaddr is None')
                if self.cbgppeeraddrfamilyafi is None:
                    raise YPYDataValidationError('Key property cbgppeeraddrfamilyafi is None')
                if self.cbgppeeraddrfamilysafi is None:
                    raise YPYDataValidationError('Key property cbgppeeraddrfamilysafi is None')

                return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeerAddrFamilyPrefixTable/CISCO-BGP4-MIB:cbgpPeerAddrFamilyPrefixEntry[CISCO-BGP4-MIB:bgpPeerRemoteAddr = ' + str(self.bgppeerremoteaddr) + '][CISCO-BGP4-MIB:cbgpPeerAddrFamilyAfi = ' + str(self.cbgppeeraddrfamilyafi) + '][CISCO-BGP4-MIB:cbgpPeerAddrFamilySafi = ' + str(self.cbgppeeraddrfamilysafi) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.bgppeerremoteaddr is not None:
                    return True

                if self.cbgppeeraddrfamilyafi is not None:
                    return True

                if self.cbgppeeraddrfamilysafi is not None:
                    return True

                if self.cbgppeeracceptedprefixes is not None:
                    return True

                if self.cbgppeeradvertisedprefixes is not None:
                    return True

                if self.cbgppeerdeniedprefixes is not None:
                    return True

                if self.cbgppeerprefixadminlimit is not None:
                    return True

                if self.cbgppeerprefixclearthreshold is not None:
                    return True

                if self.cbgppeerprefixthreshold is not None:
                    return True

                if self.cbgppeersuppressedprefixes is not None:
                    return True

                if self.cbgppeerwithdrawnprefixes is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
                return meta._meta_table['CISCOBGP4MIB.CbgpPeerAddrFamilyPrefixTable.CbgpPeerAddrFamilyPrefixEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeerAddrFamilyPrefixTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbgppeeraddrfamilyprefixentry is not None:
                for child_ref in self.cbgppeeraddrfamilyprefixentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CISCOBGP4MIB.CbgpPeerAddrFamilyPrefixTable']['meta_info']


    class CbgpPeerAddrFamilyTable(object):
        """
        This table contains information related to
        address families supported by a peer. Supported
        address families of a peer are known during BGP 
        connection establishment. When a new supported 
        address family is known, this table is updated 
        with a new entry. When an address family is not 
        supported any more, corresponding entry is deleted 
        from the table.
        
        .. attribute:: cbgppeeraddrfamilyentry
        
        	An entry is identified by an AFI/SAFI pair and peer address. It contains names associated with an address family
        	**type**\: list of :py:class:`CbgpPeerAddrFamilyEntry <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeerAddrFamilyTable.CbgpPeerAddrFamilyEntry>`
        
        

        """

        _prefix = 'cisco-bgp4'
        _revision = '2010-09-30'

        def __init__(self):
            self.parent = None
            self.cbgppeeraddrfamilyentry = YList()
            self.cbgppeeraddrfamilyentry.parent = self
            self.cbgppeeraddrfamilyentry.name = 'cbgppeeraddrfamilyentry'


        class CbgpPeerAddrFamilyEntry(object):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains names associated with
            an address family.
            
            .. attribute:: bgppeerremoteaddr
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cbgppeeraddrfamilyafi
            
            	The AFI index of the entry. An implementation is only required to support IPv4 unicast and  VPNv4 (Value \- 1) address families
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cbgppeeraddrfamilysafi
            
            	The SAFI index of the entry. An implementation is only required to support IPv4 unicast(Value  \- 1) and VPNv4( Value \- 128) address families
            	**type**\: :py:class:`CbgpSafi_Enum <ydk.models.bgp4.CISCO_BGP4_MIB.CbgpSafi_Enum>`
            
            .. attribute:: cbgppeeraddrfamilyname
            
            	Implementation specific Address Family name
            	**type**\: str
            
            	**range:** 0..255
            
            

            """

            _prefix = 'cisco-bgp4'
            _revision = '2010-09-30'

            def __init__(self):
                self.parent = None
                self.bgppeerremoteaddr = None
                self.cbgppeeraddrfamilyafi = None
                self.cbgppeeraddrfamilysafi = None
                self.cbgppeeraddrfamilyname = None

            @property
            def _common_path(self):
                if self.bgppeerremoteaddr is None:
                    raise YPYDataValidationError('Key property bgppeerremoteaddr is None')
                if self.cbgppeeraddrfamilyafi is None:
                    raise YPYDataValidationError('Key property cbgppeeraddrfamilyafi is None')
                if self.cbgppeeraddrfamilysafi is None:
                    raise YPYDataValidationError('Key property cbgppeeraddrfamilysafi is None')

                return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeerAddrFamilyTable/CISCO-BGP4-MIB:cbgpPeerAddrFamilyEntry[CISCO-BGP4-MIB:bgpPeerRemoteAddr = ' + str(self.bgppeerremoteaddr) + '][CISCO-BGP4-MIB:cbgpPeerAddrFamilyAfi = ' + str(self.cbgppeeraddrfamilyafi) + '][CISCO-BGP4-MIB:cbgpPeerAddrFamilySafi = ' + str(self.cbgppeeraddrfamilysafi) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.bgppeerremoteaddr is not None:
                    return True

                if self.cbgppeeraddrfamilyafi is not None:
                    return True

                if self.cbgppeeraddrfamilysafi is not None:
                    return True

                if self.cbgppeeraddrfamilyname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
                return meta._meta_table['CISCOBGP4MIB.CbgpPeerAddrFamilyTable.CbgpPeerAddrFamilyEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeerAddrFamilyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbgppeeraddrfamilyentry is not None:
                for child_ref in self.cbgppeeraddrfamilyentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CISCOBGP4MIB.CbgpPeerAddrFamilyTable']['meta_info']


    class CbgpPeerCapsTable(object):
        """
        This table contains the capabilities that are
        supported by a peer. Capabilities of a peer are 
        received during BGP connection establishment.
        Values corresponding to each received capability
        are stored in this table. When a new capability 
        is received, this table is updated with a new 
        entry. When an existing capability is not received 
        during the latest connection establishment, the 
        corresponding entry is deleted from the table.
        
        .. attribute:: cbgppeercapsentry
        
        	Each entry represents a capability received from a peer with a particular code and an index. When a  capability is received multiple times with different values during a BGP connection establishment,  corresponding entries are differentiated with indices
        	**type**\: list of :py:class:`CbgpPeerCapsEntry <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeerCapsTable.CbgpPeerCapsEntry>`
        
        

        """

        _prefix = 'cisco-bgp4'
        _revision = '2010-09-30'

        def __init__(self):
            self.parent = None
            self.cbgppeercapsentry = YList()
            self.cbgppeercapsentry.parent = self
            self.cbgppeercapsentry.name = 'cbgppeercapsentry'


        class CbgpPeerCapsEntry(object):
            """
            Each entry represents a capability received from a
            peer with a particular code and an index. When a 
            capability is received multiple times with different
            values during a BGP connection establishment, 
            corresponding entries are differentiated with indices.
            
            .. attribute:: bgppeerremoteaddr
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cbgppeercapcode
            
            	The BGP Capability Advertisement Capability Code
            	**type**\: :py:class:`CbgpPeerCapCode_Enum <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeerCapsTable.CbgpPeerCapsEntry.CbgpPeerCapCode_Enum>`
            
            .. attribute:: cbgppeercapindex
            
            	Multiple instances of a given capability may be sent by a BGP speaker.  This variable is used to index them
            	**type**\: int
            
            	**range:** 1..128
            
            .. attribute:: cbgppeercapvalue
            
            	The value of the announced capability. This MIB object value is organized as given below,     Capability \: Route Refresh Capability                  Null string     Capability \: Multiprotocol Extensions       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     Capability \: Graceful Restart       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Restart Flags (4 bits)           \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Restart Time in seconds (12 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Flags for Address Family (8 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| ...                              \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Flags for Address Family (8 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
            	**type**\: str
            
            	**range:** 0..255
            
            

            """

            _prefix = 'cisco-bgp4'
            _revision = '2010-09-30'

            def __init__(self):
                self.parent = None
                self.bgppeerremoteaddr = None
                self.cbgppeercapcode = None
                self.cbgppeercapindex = None
                self.cbgppeercapvalue = None

            class CbgpPeerCapCode_Enum(Enum):
                """
                CbgpPeerCapCode_Enum

                The BGP Capability Advertisement Capability Code.

                """

                MULTIPROTOCOL = 1

                ROUTEREFRESH = 2

                GRACEFULRESTART = 64

                ROUTEREFRESHOLD = 128


                @staticmethod
                def _meta_info():
                    from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
                    return meta._meta_table['CISCOBGP4MIB.CbgpPeerCapsTable.CbgpPeerCapsEntry.CbgpPeerCapCode_Enum']


            @property
            def _common_path(self):
                if self.bgppeerremoteaddr is None:
                    raise YPYDataValidationError('Key property bgppeerremoteaddr is None')
                if self.cbgppeercapcode is None:
                    raise YPYDataValidationError('Key property cbgppeercapcode is None')
                if self.cbgppeercapindex is None:
                    raise YPYDataValidationError('Key property cbgppeercapindex is None')

                return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeerCapsTable/CISCO-BGP4-MIB:cbgpPeerCapsEntry[CISCO-BGP4-MIB:bgpPeerRemoteAddr = ' + str(self.bgppeerremoteaddr) + '][CISCO-BGP4-MIB:cbgpPeerCapCode = ' + str(self.cbgppeercapcode) + '][CISCO-BGP4-MIB:cbgpPeerCapIndex = ' + str(self.cbgppeercapindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.bgppeerremoteaddr is not None:
                    return True

                if self.cbgppeercapcode is not None:
                    return True

                if self.cbgppeercapindex is not None:
                    return True

                if self.cbgppeercapvalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
                return meta._meta_table['CISCOBGP4MIB.CbgpPeerCapsTable.CbgpPeerCapsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeerCapsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbgppeercapsentry is not None:
                for child_ref in self.cbgppeercapsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CISCOBGP4MIB.CbgpPeerCapsTable']['meta_info']


    class CbgpRouteTable(object):
        """
        This table contains information about routes to
        destination networks from all BGP4 peers.  Since 
        BGP4 can carry routes for multiple Network Layer 
        protocols, this table has the Address Family 
        Identifier(AFI) of the Network Layer protocol as the 
        first index. Further for a given AFI, routes carried
        by BGP4 are distinguished based on Subsequent Address 
        Family Identifiers(SAFI).  Hence that is used as the
        second index.  Conceptually there is a separate Loc\-RIB
        maintained by the BGP speaker for each combination of 
        AFI and SAFI supported by it.
        
        .. attribute:: cbgprouteentry
        
        	Information about a path to a network received from a peer
        	**type**\: list of :py:class:`CbgpRouteEntry <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpRouteTable.CbgpRouteEntry>`
        
        

        """

        _prefix = 'cisco-bgp4'
        _revision = '2010-09-30'

        def __init__(self):
            self.parent = None
            self.cbgprouteentry = YList()
            self.cbgprouteentry.parent = self
            self.cbgprouteentry.name = 'cbgprouteentry'


        class CbgpRouteEntry(object):
            """
            Information about a path to a network received from
            a peer.
            
            .. attribute:: cbgprouteaddrprefix
            
            	A Network Address prefix in the Network Layer Reachability Information field of BGP UPDATE message. This object is a Network Address containing the prefix with length specified by cbgpRouteAddrPrefixLen. Any bits beyond the length specified by cbgpRouteAddrPrefixLen are zeroed
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cbgprouteaddrprefixlen
            
            	Length in bits of the Network Address prefix in the Network Layer Reachability Information field
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: cbgprouteafi
            
            	Represents Address Family Identifier(AFI) of the Network Layer protocol associated with the route. An implementation is only required to support IPv4 unicast and VPNv4 (Value \- 1) address families
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cbgproutepeer
            
            	The Network Layer address of the peer where the route information was learned. An implementation is only  required to support an IPv4 peer
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cbgproutepeertype
            
            	Represents the type of Network Layer address stored in cbgpRoutePeer. An implementation is only required to support IPv4 address type(Value \- 1)
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cbgproutesafi
            
            	Represents Subsequent Address Family Identifier(SAFI) of the route. It gives additional information about the type of the route. An implementation is only  required to support IPv4 unicast(Value \- 1) and VPNv4( Value \- 128) address families
            	**type**\: :py:class:`CbgpSafi_Enum <ydk.models.bgp4.CISCO_BGP4_MIB.CbgpSafi_Enum>`
            
            .. attribute:: cbgprouteaggregatoraddr
            
            	The Network Layer address of the last BGP4 speaker that performed route aggregation.  A value of all zeros indicates the absence of this attribute
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cbgprouteaggregatoraddrtype
            
            	Represents the type of Network Layer address stored in cbgpRouteAggregatorAddr
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cbgprouteaggregatoras
            
            	The AS number of the last BGP4 speaker that performed route aggregation.  A value of zero (0) indicates the  absence of this attribute
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cbgprouteaspathsegment
            
            	The sequence of AS path segments.  Each AS path segment is represented by a triple <type, length, value>.  The type is a 1\-octet field which has two possible values\: 1  AS\_SET\: unordered set of ASs a route in the            UPDATE message has traversed 2  AS\_SEQUENCE\: ordered set of ASs a route in the                UPDATE message has traversed.  The length is a 1\-octet field containing the number of ASs in the value field.  The value field contains one or more AS numbers, each AS is represented in the octet string as a pair of octets according to the following algorithm\:  first\-byte\-of\-pair = ASNumber / 256; second\-byte\-of\-pair = ASNumber & 255;
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cbgprouteatomicaggregate
            
            	Whether or not the local system has selected a less specific route without selecting a more specific route
            	**type**\: :py:class:`CbgpRouteAtomicAggregate_Enum <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpRouteTable.CbgpRouteEntry.CbgpRouteAtomicAggregate_Enum>`
            
            .. attribute:: cbgproutebest
            
            	An indication of whether or not this route was chosen as the best BGP4 route
            	**type**\: bool
            
            .. attribute:: cbgproutelocalpref
            
            	The degree of preference calculated by the local BGP4 speaker for the route. The value of this object is  irrelevant if the value of cbgpRouteLocalPrefPresent  is false(2)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgproutelocalprefpresent
            
            	Indicates the presence/absence of LOCAL\_PREF attribute for the route
            	**type**\: bool
            
            .. attribute:: cbgproutemedpresent
            
            	Indicates the presence/absence of MULTI\_EXIT\_DISC attribute for the route
            	**type**\: bool
            
            .. attribute:: cbgproutemultiexitdisc
            
            	This metric is used to discriminate between multiple exit points to an adjacent autonomous system.  The value of this object is irrelevant if the value of of cbgpRouteMedPresent is false(2)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgproutenexthop
            
            	The Network Layer address of the border router that should be used for the destination network
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cbgprouteorigin
            
            	The ultimate origin of the route information
            	**type**\: :py:class:`CbgpRouteOrigin_Enum <ydk.models.bgp4.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpRouteTable.CbgpRouteEntry.CbgpRouteOrigin_Enum>`
            
            .. attribute:: cbgprouteunknownattr
            
            	One or more path attributes not understood by this BGP4 speaker.  Size zero (0) indicates the absence of such attribute(s).  Octets beyond the maximum size, if any, are not recorded by this object.    Each path attribute is a triple <attribute type, attribute length, attribute value> of variable length. Attribute Type is a two\-octet field that consists of the Attribute Flags octet followed by the Attribute Type Code octet.  If the Extended Length bit of the  Attribute Flags octet is set to 0, the third octet of  the Path Attribute contains the length of the attribute data in octets.  If the Extended Length bit  of the Attribute Flags octet is set to 1, then the third and the fourth octets of the path attribute  contain the length of the attribute data in octets. The remaining octets of the Path Attribute represent  the attribute value and are interpreted according to  the Attribute Flags and the Attribute Type Code
            	**type**\: str
            
            	**range:** 0..255
            
            

            """

            _prefix = 'cisco-bgp4'
            _revision = '2010-09-30'

            def __init__(self):
                self.parent = None
                self.cbgprouteaddrprefix = None
                self.cbgprouteaddrprefixlen = None
                self.cbgprouteafi = None
                self.cbgproutepeer = None
                self.cbgproutepeertype = None
                self.cbgproutesafi = None
                self.cbgprouteaggregatoraddr = None
                self.cbgprouteaggregatoraddrtype = None
                self.cbgprouteaggregatoras = None
                self.cbgprouteaspathsegment = None
                self.cbgprouteatomicaggregate = None
                self.cbgproutebest = None
                self.cbgproutelocalpref = None
                self.cbgproutelocalprefpresent = None
                self.cbgproutemedpresent = None
                self.cbgproutemultiexitdisc = None
                self.cbgproutenexthop = None
                self.cbgprouteorigin = None
                self.cbgprouteunknownattr = None

            class CbgpRouteAtomicAggregate_Enum(Enum):
                """
                CbgpRouteAtomicAggregate_Enum

                Whether or not the local system has selected a less
                specific route without selecting a more specific
                route.

                """

                LESSSPECIFICROUTENOTSELECTED = 1

                LESSSPECIFICROUTESELECTED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
                    return meta._meta_table['CISCOBGP4MIB.CbgpRouteTable.CbgpRouteEntry.CbgpRouteAtomicAggregate_Enum']


            class CbgpRouteOrigin_Enum(Enum):
                """
                CbgpRouteOrigin_Enum

                The ultimate origin of the route information.

                """

                IGP = 1

                EGP = 2

                INCOMPLETE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
                    return meta._meta_table['CISCOBGP4MIB.CbgpRouteTable.CbgpRouteEntry.CbgpRouteOrigin_Enum']


            @property
            def _common_path(self):
                if self.cbgprouteaddrprefix is None:
                    raise YPYDataValidationError('Key property cbgprouteaddrprefix is None')
                if self.cbgprouteaddrprefixlen is None:
                    raise YPYDataValidationError('Key property cbgprouteaddrprefixlen is None')
                if self.cbgprouteafi is None:
                    raise YPYDataValidationError('Key property cbgprouteafi is None')
                if self.cbgproutepeer is None:
                    raise YPYDataValidationError('Key property cbgproutepeer is None')
                if self.cbgproutepeertype is None:
                    raise YPYDataValidationError('Key property cbgproutepeertype is None')
                if self.cbgproutesafi is None:
                    raise YPYDataValidationError('Key property cbgproutesafi is None')

                return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpRouteTable/CISCO-BGP4-MIB:cbgpRouteEntry[CISCO-BGP4-MIB:cbgpRouteAddrPrefix = ' + str(self.cbgprouteaddrprefix) + '][CISCO-BGP4-MIB:cbgpRouteAddrPrefixLen = ' + str(self.cbgprouteaddrprefixlen) + '][CISCO-BGP4-MIB:cbgpRouteAfi = ' + str(self.cbgprouteafi) + '][CISCO-BGP4-MIB:cbgpRoutePeer = ' + str(self.cbgproutepeer) + '][CISCO-BGP4-MIB:cbgpRoutePeerType = ' + str(self.cbgproutepeertype) + '][CISCO-BGP4-MIB:cbgpRouteSafi = ' + str(self.cbgproutesafi) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cbgprouteaddrprefix is not None:
                    return True

                if self.cbgprouteaddrprefixlen is not None:
                    return True

                if self.cbgprouteafi is not None:
                    return True

                if self.cbgproutepeer is not None:
                    return True

                if self.cbgproutepeertype is not None:
                    return True

                if self.cbgproutesafi is not None:
                    return True

                if self.cbgprouteaggregatoraddr is not None:
                    return True

                if self.cbgprouteaggregatoraddrtype is not None:
                    return True

                if self.cbgprouteaggregatoras is not None:
                    return True

                if self.cbgprouteaspathsegment is not None:
                    return True

                if self.cbgprouteatomicaggregate is not None:
                    return True

                if self.cbgproutebest is not None:
                    return True

                if self.cbgproutelocalpref is not None:
                    return True

                if self.cbgproutelocalprefpresent is not None:
                    return True

                if self.cbgproutemedpresent is not None:
                    return True

                if self.cbgproutemultiexitdisc is not None:
                    return True

                if self.cbgproutenexthop is not None:
                    return True

                if self.cbgprouteorigin is not None:
                    return True

                if self.cbgprouteunknownattr is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
                return meta._meta_table['CISCOBGP4MIB.CbgpRouteTable.CbgpRouteEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpRouteTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cbgprouteentry is not None:
                for child_ref in self.cbgprouteentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CISCOBGP4MIB.CbgpRouteTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cbgpglobal is not None and self.cbgpglobal._has_data():
            return True

        if self.cbgpglobal is not None and self.cbgpglobal.is_presence():
            return True

        if self.cbgppeer2addrfamilyprefixtable is not None and self.cbgppeer2addrfamilyprefixtable._has_data():
            return True

        if self.cbgppeer2addrfamilyprefixtable is not None and self.cbgppeer2addrfamilyprefixtable.is_presence():
            return True

        if self.cbgppeer2addrfamilytable is not None and self.cbgppeer2addrfamilytable._has_data():
            return True

        if self.cbgppeer2addrfamilytable is not None and self.cbgppeer2addrfamilytable.is_presence():
            return True

        if self.cbgppeer2capstable is not None and self.cbgppeer2capstable._has_data():
            return True

        if self.cbgppeer2capstable is not None and self.cbgppeer2capstable.is_presence():
            return True

        if self.cbgppeer2table is not None and self.cbgppeer2table._has_data():
            return True

        if self.cbgppeer2table is not None and self.cbgppeer2table.is_presence():
            return True

        if self.cbgppeeraddrfamilyprefixtable is not None and self.cbgppeeraddrfamilyprefixtable._has_data():
            return True

        if self.cbgppeeraddrfamilyprefixtable is not None and self.cbgppeeraddrfamilyprefixtable.is_presence():
            return True

        if self.cbgppeeraddrfamilytable is not None and self.cbgppeeraddrfamilytable._has_data():
            return True

        if self.cbgppeeraddrfamilytable is not None and self.cbgppeeraddrfamilytable.is_presence():
            return True

        if self.cbgppeercapstable is not None and self.cbgppeercapstable._has_data():
            return True

        if self.cbgppeercapstable is not None and self.cbgppeercapstable.is_presence():
            return True

        if self.cbgproutetable is not None and self.cbgproutetable._has_data():
            return True

        if self.cbgproutetable is not None and self.cbgproutetable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.bgp4._meta import _CISCO_BGP4_MIB as meta
        return meta._meta_table['CISCOBGP4MIB']['meta_info']


