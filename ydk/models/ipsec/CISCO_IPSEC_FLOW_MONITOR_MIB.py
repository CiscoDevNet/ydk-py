""" CISCO_IPSEC_FLOW_MONITOR_MIB 

This is a MIB Module for monitoring the
structures in IPSec\-based Virtual Private Networks.
The MIB has been designed to be adopted as an IETF
standard. Hence Cisco\-specific features of IPSec
protocol are excluded from this MIB. 

Acronyms
The following acronyms are used in this document\:

 IPSec\:      Secure IP Protocol

 VPN\:        Virtual Private Network

 ISAKMP\:     Internet Security Association and Key Exchange
             Protocol

 IKE\:        Internet Key Exchange Protocol

 SA\:         Security Association

 MM\:         Main Mode \- the process of setting up
             a Phase 1 SA to secure the exchanges
             required to setup Phase 2 SAs

 QM\:         Quick Mode \- the process of setting up
             Phase 2 Security Associations using 
             a Phase 1 SA.


 Overview of IPsec MIB

The MIB contains six major groups of objects which are
used to manage the IPSec Protocol. These groups include
a Levels Group, a Phase\-1 Group, a Phase\-2 Group,
a History Group, a Failure Group and a TRAP Control Group.
The following table illustrates the structure of the
IPSec MIB.

The Phase 1 group models objects pertaining to
IKE negotiations and tunnels.

The Phase 2 group models objects pertaining to
IPSec data tunnels.

The History group is to aid applications that do
trending analysis.

The Failure group is to enable an operator to
do troubleshooting and debugging of the VPN Router.
Further, counters are supported to aid Intrusion 
Detection.

In addition to the five major MIB Groups, there are
a number of Notifications. The following table
illustrates the name and description of the 
IPSec TRAPs.

For a detailed discussion, please refer to the IETF
draft draft\-ietf\-ipsec\-flow\-monitoring\-mib\-00.txt.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class AuthAlgo_Enum(Enum):
    """
    AuthAlgo_Enum

    The authentication algorithm used by a
    security association of an IPsec Phase\-2 Tunnel.

    """

    NONE = 1

    HMACMD5 = 2

    HMACSHA = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['AuthAlgo_Enum']


class CompAlgo_Enum(Enum):
    """
    CompAlgo_Enum

    The compression algorithm used by a
    security association of an IPsec Phase\-2 Tunnel.

    """

    NONE = 1

    LDF = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['CompAlgo_Enum']


class DiffHellmanGrp_Enum(Enum):
    """
    DiffHellmanGrp_Enum

    The Diffie Hellman Group used in negotiations.

    """

    NONE = 1

    DHGROUP1 = 2

    DHGROUP2 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['DiffHellmanGrp_Enum']


class EncapMode_Enum(Enum):
    """
    EncapMode_Enum

    The encapsulation mode used by an IPsec Phase\-2
    Tunnel.

    """

    TUNNEL = 1

    TRANSPORT = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['EncapMode_Enum']


class EncryptAlgo_Enum(Enum):
    """
    EncryptAlgo_Enum

    The encryption algorithm used in negotiations.

    """

    NONE = 1

    DES = 2

    DES3 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['EncryptAlgo_Enum']


class EndPtType_Enum(Enum):
    """
    EndPtType_Enum

    The type of identity use to specify an IPsec End Point.

    """

    SINGLEIPADDR = 1

    IPADDRRANGE = 2

    IPSUBNET = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['EndPtType_Enum']


class IkeAuthMethod_Enum(Enum):
    """
    IkeAuthMethod_Enum

    The authentication method used in IPsec Phase\-1 IKE
    negotiations.

    """

    NONE = 1

    PRESHAREDKEY = 2

    RSASIG = 3

    RSAENCRYPT = 4

    REVPUBLICKEY = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['IkeAuthMethod_Enum']


class IkeHashAlgo_Enum(Enum):
    """
    IkeHashAlgo_Enum

    The hash algorithm used in IPsec Phase\-1
    IKE negotiations.

    """

    NONE = 1

    MD5 = 2

    SHA = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['IkeHashAlgo_Enum']


class IkeNegoMode_Enum(Enum):
    """
    IkeNegoMode_Enum

    The IPsec Phase\-1 IKE negotiation mode.

    """

    MAIN = 1

    AGGRESSIVE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['IkeNegoMode_Enum']


class IkePeerType_Enum(Enum):
    """
    IkePeerType_Enum

    The type of IPsec Phase\-1 IKE peer identity.
    The IKE peer may be identified by\:
     1. an IP address, or
     2. a host name.

    """

    IPADDRPEER = 1

    NAMEPEER = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['IkePeerType_Enum']


class KeyType_Enum(Enum):
    """
    KeyType_Enum

    The type of key used by an IPsec Phase\-2 Tunnel.

    """

    IKE = 1

    MANUAL = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['KeyType_Enum']


class TrapStatus_Enum(Enum):
    """
    TrapStatus_Enum

    The administrative status for sending a TRAP.

    """

    ENABLED = 1

    DISABLED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['TrapStatus_Enum']


class TunnelStatus_Enum(Enum):
    """
    TunnelStatus_Enum

    The status of a Tunnel.  Objects of this type may
    be used to bring the tunnel down by setting
    value of this object to destroy(2).  Objects of this
    type cannot be used to create a Tunnel.

    """

    ACTIVE = 1

    DESTROY = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['TunnelStatus_Enum']



class CISCOIPSECFLOWMONITORMIB(object):
    """
    
    
    .. attribute:: cikefailtable
    
    	The IPsec Phase\-1 Failure Table. This table is implemented as a sliding  window in which only the last n entries are  maintained.  The maximum number of entries is specified by the cipSecFailTableSize object
    	**type**\: :py:class:`CikeFailTable <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CikeFailTable>`
    
    .. attribute:: cikeglobalstats
    
    	
    	**type**\: :py:class:`CikeGlobalStats <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CikeGlobalStats>`
    
    .. attribute:: cikepeercorrtable
    
    	The IPsec Phase\-1 Internet Key Exchange Peer Association to IPsec Phase\-2 Tunnel Correlation Table. There is one entry in this table for each active IPsec Phase\-2 Tunnel
    	**type**\: :py:class:`CikePeerCorrTable <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CikePeerCorrTable>`
    
    .. attribute:: cikepeertable
    
    	The IPsec Phase\-1 Internet Key Exchange Peer Table. There is one entry in this table for each IPsec Phase\-1 IKE peer association which is currently associated with an active IPsec Phase\-1 Tunnel. The IPsec Phase\-1 IKE Tunnel associated with this IPsec Phase\-1 IKE peer association may or may not be currently active
    	**type**\: :py:class:`CikePeerTable <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CikePeerTable>`
    
    .. attribute:: cikephase1gwstatstable
    
    	Phase\-1 IKE stats information is included in this table. Each entry is related to a specific gateway which is  identified by 'cmgwIndex'
    	**type**\: :py:class:`CikePhase1GWStatsTable <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CikePhase1GWStatsTable>`
    
    .. attribute:: ciketunnelhisttable
    
    	The IPsec Phase\-1 Internet Key Exchange Tunnel History Table.  This table is implemented as a  sliding window in which only the last n entries  are maintained.  The maximum number of entries  is specified by the cipSecHistTableSize object
    	**type**\: :py:class:`CikeTunnelHistTable <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable>`
    
    .. attribute:: ciketunneltable
    
    	The IPsec Phase\-1 Internet Key Exchange Tunnel Table. There is one entry in this table for each active IPsec Phase\-1 IKE Tunnel
    	**type**\: :py:class:`CikeTunnelTable <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CikeTunnelTable>`
    
    .. attribute:: cipsecendpthisttable
    
    	The IPsec Phase\-2 Tunnel Endpoint History Table. This table is implemented as a  sliding window in which only the last n entries are maintained.   The maximum number of entries is specified by the cipSecHistTableSize object
    	**type**\: :py:class:`CipSecEndPtHistTable <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecEndPtHistTable>`
    
    .. attribute:: cipsecendpttable
    
    	The IPsec Phase\-2 Tunnel Endpoint Table. This table contains an entry for each  active endpoint associated with an IPsec  Phase\-2 Tunnel
    	**type**\: :py:class:`CipSecEndPtTable <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecEndPtTable>`
    
    .. attribute:: cipsecfailglobalcntl
    
    	
    	**type**\: :py:class:`CipSecFailGlobalCntl <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecFailGlobalCntl>`
    
    .. attribute:: cipsecfailtable
    
    	The IPsec Phase\-2 Failure Table. This table is implemented as a sliding window  in which only the last n entries are maintained.   The maximum number of entries is specified by the cipSecFailTableSize object
    	**type**\: :py:class:`CipSecFailTable <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecFailTable>`
    
    .. attribute:: cipsecglobalstats
    
    	
    	**type**\: :py:class:`CipSecGlobalStats <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecGlobalStats>`
    
    .. attribute:: cipsechistglobalcntl
    
    	
    	**type**\: :py:class:`CipSecHistGlobalCntl <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecHistGlobalCntl>`
    
    .. attribute:: cipseclevels
    
    	
    	**type**\: :py:class:`CipSecLevels <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecLevels>`
    
    .. attribute:: cipsecphase2gwstatstable
    
    	Phase\-2 IPsec stats information is included in this table. Each entry is related to a specific gateway which is  identified by 'cmgwIndex'
    	**type**\: :py:class:`CipSecPhase2GWStatsTable <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecPhase2GWStatsTable>`
    
    .. attribute:: cipsecspitable
    
    	The IPsec Phase\-2 Security Protection Index Table. This table contains an entry for each active  and expiring security  association
    	**type**\: :py:class:`CipSecSpiTable <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecSpiTable>`
    
    .. attribute:: cipsectrapcntl
    
    	
    	**type**\: :py:class:`CipSecTrapCntl <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecTrapCntl>`
    
    .. attribute:: cipsectunnelhisttable
    
    	The IPsec Phase\-2 Tunnel History Table. This table is implemented as a sliding  window in which only the last n entries are maintained.  The maximum number  of entries is specified by the cipSecHistTableSize object
    	**type**\: :py:class:`CipSecTunnelHistTable <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable>`
    
    .. attribute:: cipsectunneltable
    
    	The IPsec Phase\-2 Tunnel Table. There is one entry in this table for  each active IPsec Phase\-2 Tunnel
    	**type**\: :py:class:`CipSecTunnelTable <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecTunnelTable>`
    
    

    """

    _prefix = 'cisco-ipsec'
    _revision = '2007-10-24'

    def __init__(self):
        self.cikefailtable = CISCOIPSECFLOWMONITORMIB.CikeFailTable()
        self.cikefailtable.parent = self
        self.cikeglobalstats = CISCOIPSECFLOWMONITORMIB.CikeGlobalStats()
        self.cikeglobalstats.parent = self
        self.cikepeercorrtable = CISCOIPSECFLOWMONITORMIB.CikePeerCorrTable()
        self.cikepeercorrtable.parent = self
        self.cikepeertable = CISCOIPSECFLOWMONITORMIB.CikePeerTable()
        self.cikepeertable.parent = self
        self.cikephase1gwstatstable = CISCOIPSECFLOWMONITORMIB.CikePhase1GWStatsTable()
        self.cikephase1gwstatstable.parent = self
        self.ciketunnelhisttable = CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable()
        self.ciketunnelhisttable.parent = self
        self.ciketunneltable = CISCOIPSECFLOWMONITORMIB.CikeTunnelTable()
        self.ciketunneltable.parent = self
        self.cipsecendpthisttable = CISCOIPSECFLOWMONITORMIB.CipSecEndPtHistTable()
        self.cipsecendpthisttable.parent = self
        self.cipsecendpttable = CISCOIPSECFLOWMONITORMIB.CipSecEndPtTable()
        self.cipsecendpttable.parent = self
        self.cipsecfailglobalcntl = CISCOIPSECFLOWMONITORMIB.CipSecFailGlobalCntl()
        self.cipsecfailglobalcntl.parent = self
        self.cipsecfailtable = CISCOIPSECFLOWMONITORMIB.CipSecFailTable()
        self.cipsecfailtable.parent = self
        self.cipsecglobalstats = CISCOIPSECFLOWMONITORMIB.CipSecGlobalStats()
        self.cipsecglobalstats.parent = self
        self.cipsechistglobalcntl = CISCOIPSECFLOWMONITORMIB.CipSecHistGlobalCntl()
        self.cipsechistglobalcntl.parent = self
        self.cipseclevels = CISCOIPSECFLOWMONITORMIB.CipSecLevels()
        self.cipseclevels.parent = self
        self.cipsecphase2gwstatstable = CISCOIPSECFLOWMONITORMIB.CipSecPhase2GWStatsTable()
        self.cipsecphase2gwstatstable.parent = self
        self.cipsecspitable = CISCOIPSECFLOWMONITORMIB.CipSecSpiTable()
        self.cipsecspitable.parent = self
        self.cipsectrapcntl = CISCOIPSECFLOWMONITORMIB.CipSecTrapCntl()
        self.cipsectrapcntl.parent = self
        self.cipsectunnelhisttable = CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable()
        self.cipsectunnelhisttable.parent = self
        self.cipsectunneltable = CISCOIPSECFLOWMONITORMIB.CipSecTunnelTable()
        self.cipsectunneltable.parent = self


    class CikeFailTable(object):
        """
        The IPsec Phase\-1 Failure Table.
        This table is implemented as a sliding 
        window in which only the last n entries are 
        maintained.  The maximum number of entries
        is specified by the cipSecFailTableSize object.
        
        .. attribute:: cikefailentry
        
        	Each entry contains the attributes associated with  an IPsec Phase\-1 failure
        	**type**\: list of :py:class:`CikeFailEntry <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CikeFailTable.CikeFailEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cikefailentry = YList()
            self.cikefailentry.parent = self
            self.cikefailentry.name = 'cikefailentry'


        class CikeFailEntry(object):
            """
            Each entry contains the attributes associated
            with
             an IPsec Phase\-1 failure.
            
            .. attribute:: cikefailindex
            
            	The IPsec Phase\-1 Failure Table index. The value of the index is a number which  begins at one and is incremented with each  IPsec Phase\-1 failure. The value of this object will wrap at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cikefaillocaladdr
            
            	The IP address of the local peer
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cikefaillocaltype
            
            	The type of local peer identity.  The local peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\: :py:class:`IkePeerType_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType_Enum>`
            
            .. attribute:: cikefaillocalvalue
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cikefailreason
            
            	The reason for the failure.  Possible reasons include\: 1 = other 2 = peer delete request was received 3 = contact with peer was lost 4 = local failure occurred 5 = authentication failure 6 = hash validation failure 7 = encryption failure 8 = internal error occurred 9 = system capacity failure 10 = proposal failure 11 = peer's certificate is unavailable 12 = peer's certificate was found invalid 13 = local certificate expired 14 = certificate revoke list (crl) failure 15 = peer encoding error 16 = non\-existent security association 17 = operator requested termination
            	**type**\: :py:class:`CikeFailReason_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CikeFailTable.CikeFailEntry.CikeFailReason_Enum>`
            
            .. attribute:: cikefailremoteaddr
            
            	The IP address of the remote peer
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cikefailremotetype
            
            	The type of remote peer identity.  The remote peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\: :py:class:`IkePeerType_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType_Enum>`
            
            .. attribute:: cikefailremotevalue
            
            	The value of the remote peer identity.  If the remote peer type is an IP Address, then this is the IP Address used to identify the remote peer.  If the remote peer type is a host name, then this is the host name used to identify the remote peer
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cikefailtime
            
            	The value of sysUpTime in hundredths of seconds at the time of the failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2007-10-24'

            def __init__(self):
                self.parent = None
                self.cikefailindex = None
                self.cikefaillocaladdr = None
                self.cikefaillocaltype = None
                self.cikefaillocalvalue = None
                self.cikefailreason = None
                self.cikefailremoteaddr = None
                self.cikefailremotetype = None
                self.cikefailremotevalue = None
                self.cikefailtime = None

            class CikeFailReason_Enum(Enum):
                """
                CikeFailReason_Enum

                The reason for the failure.  Possible reasons include\:
                1 = other
                2 = peer delete request was received
                3 = contact with peer was lost
                4 = local failure occurred
                5 = authentication failure
                6 = hash validation failure
                7 = encryption failure
                8 = internal error occurred
                9 = system capacity failure
                10 = proposal failure
                11 = peer's certificate is unavailable
                12 = peer's certificate was found invalid
                13 = local certificate expired
                14 = certificate revoke list (crl) failure
                15 = peer encoding error
                16 = non\-existent security association
                17 = operator requested termination.

                """

                OTHER = 1

                PEERDELREQUEST = 2

                PEERLOST = 3

                LOCALFAILURE = 4

                AUTHFAILURE = 5

                HASHVALIDATION = 6

                ENCRYPTFAILURE = 7

                INTERNALERROR = 8

                SYSCAPEXCEEDED = 9

                PROPOSALFAILURE = 10

                PEERCERTUNAVAILABLE = 11

                PEERCERTNOTVALID = 12

                LOCALCERTEXPIRED = 13

                CRLFAILURE = 14

                PEERENCODINGERROR = 15

                NONEXISTENTSA = 16

                OPERREQUEST = 17


                @staticmethod
                def _meta_info():
                    from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                    return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CikeFailTable.CikeFailEntry.CikeFailReason_Enum']


            @property
            def _common_path(self):
                if self.cikefailindex is None:
                    raise YPYDataValidationError('Key property cikefailindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeFailTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeFailEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cikeFailIndex = ' + str(self.cikefailindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cikefailindex is not None:
                    return True

                if self.cikefaillocaladdr is not None:
                    return True

                if self.cikefaillocaltype is not None:
                    return True

                if self.cikefaillocalvalue is not None:
                    return True

                if self.cikefailreason is not None:
                    return True

                if self.cikefailremoteaddr is not None:
                    return True

                if self.cikefailremotetype is not None:
                    return True

                if self.cikefailremotevalue is not None:
                    return True

                if self.cikefailtime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CikeFailTable.CikeFailEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeFailTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cikefailentry is not None:
                for child_ref in self.cikefailentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CikeFailTable']['meta_info']


    class CikeGlobalStats(object):
        """
        
        
        .. attribute:: cikeglobalactivetunnels
        
        	The number of currently active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalauthfails
        
        	The total number of authentications which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobaldecryptfails
        
        	The total number of decryptions which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalhashvalidfails
        
        	The total number of hash validations which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalindroppkts
        
        	The total number of packets which were dropped during receive processing by all  currently and previously  active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalinittunnelfails
        
        	The total number of IPsec Phase\-1 IKE Tunnels which were locally initiated and failed to activate
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalinittunnels
        
        	The total number of IPsec Phase\-1 IKE Tunnels which were locally initiated
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalinnotifys
        
        	The total number of notifys received by all currently and previously active IPsec  Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalinoctets
        
        	The total number of octets received by all currently and previously active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalinp2exchginvalids
        
        	The total number of IPsec Phase\-2 exchanges which were received and found to be invalid  by all currently and previously active IPsec  Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalinp2exchgrejects
        
        	The total number of IPsec Phase\-2 exchanges which were received and rejected by all  currently and previously active IPsec Phase\-1  IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalinp2exchgs
        
        	The total number of IPsec Phase\-2 exchanges received by all currently and previously  active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalinp2sadelrequests
        
        	The total number of IPsec Phase\-2 security association delete requests received by all  currently and previously  active and IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalinpkts
        
        	The total number of packets received by all currently and previously active IPsec  Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalnosafails
        
        	The total number of non\-existent Security Association in failures which occurred during processing of  all current and previous IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobaloutdroppkts
        
        	The total number of packets which were dropped during send processing by all currently  and previously  active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobaloutnotifys
        
        	The total number of notifys sent by all currently and previously active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobaloutoctets
        
        	The total number of octets sent by all currently and previously active and IPsec Phase\-1  IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobaloutp2exchginvalids
        
        	The total number of IPsec Phase\-2 exchanges which were sent and found to be invalid by  all currently and previously active IPsec Phase\-1  Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobaloutp2exchgrejects
        
        	The total number of IPsec Phase\-2 exchanges which were sent and rejected by all currently and  previously active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobaloutp2exchgs
        
        	The total number of IPsec Phase\-2 exchanges which were sent by all currently and previously  active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobaloutp2sadelrequests
        
        	The total number of IPsec Phase\-2 SA delete requests sent by all currently and  previously active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobaloutpkts
        
        	The total number of packets sent by all currently and previously active and IPsec Phase\-1  Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalprevioustunnels
        
        	The total number of previously active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalresptunnelfails
        
        	The total number of IPsec Phase\-1 IKE Tunnels which were remotely initiated and failed to activate
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalsyscapfails
        
        	The total number of system capacity failures which occurred during processing of all current  and previously active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cikeglobalactivetunnels = None
            self.cikeglobalauthfails = None
            self.cikeglobaldecryptfails = None
            self.cikeglobalhashvalidfails = None
            self.cikeglobalindroppkts = None
            self.cikeglobalinittunnelfails = None
            self.cikeglobalinittunnels = None
            self.cikeglobalinnotifys = None
            self.cikeglobalinoctets = None
            self.cikeglobalinp2exchginvalids = None
            self.cikeglobalinp2exchgrejects = None
            self.cikeglobalinp2exchgs = None
            self.cikeglobalinp2sadelrequests = None
            self.cikeglobalinpkts = None
            self.cikeglobalnosafails = None
            self.cikeglobaloutdroppkts = None
            self.cikeglobaloutnotifys = None
            self.cikeglobaloutoctets = None
            self.cikeglobaloutp2exchginvalids = None
            self.cikeglobaloutp2exchgrejects = None
            self.cikeglobaloutp2exchgs = None
            self.cikeglobaloutp2sadelrequests = None
            self.cikeglobaloutpkts = None
            self.cikeglobalprevioustunnels = None
            self.cikeglobalresptunnelfails = None
            self.cikeglobalsyscapfails = None

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeGlobalStats'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cikeglobalactivetunnels is not None:
                return True

            if self.cikeglobalauthfails is not None:
                return True

            if self.cikeglobaldecryptfails is not None:
                return True

            if self.cikeglobalhashvalidfails is not None:
                return True

            if self.cikeglobalindroppkts is not None:
                return True

            if self.cikeglobalinittunnelfails is not None:
                return True

            if self.cikeglobalinittunnels is not None:
                return True

            if self.cikeglobalinnotifys is not None:
                return True

            if self.cikeglobalinoctets is not None:
                return True

            if self.cikeglobalinp2exchginvalids is not None:
                return True

            if self.cikeglobalinp2exchgrejects is not None:
                return True

            if self.cikeglobalinp2exchgs is not None:
                return True

            if self.cikeglobalinp2sadelrequests is not None:
                return True

            if self.cikeglobalinpkts is not None:
                return True

            if self.cikeglobalnosafails is not None:
                return True

            if self.cikeglobaloutdroppkts is not None:
                return True

            if self.cikeglobaloutnotifys is not None:
                return True

            if self.cikeglobaloutoctets is not None:
                return True

            if self.cikeglobaloutp2exchginvalids is not None:
                return True

            if self.cikeglobaloutp2exchgrejects is not None:
                return True

            if self.cikeglobaloutp2exchgs is not None:
                return True

            if self.cikeglobaloutp2sadelrequests is not None:
                return True

            if self.cikeglobaloutpkts is not None:
                return True

            if self.cikeglobalprevioustunnels is not None:
                return True

            if self.cikeglobalresptunnelfails is not None:
                return True

            if self.cikeglobalsyscapfails is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CikeGlobalStats']['meta_info']


    class CikePeerCorrTable(object):
        """
        The IPsec Phase\-1 Internet Key Exchange Peer
        Association to IPsec Phase\-2 Tunnel
        Correlation Table. There is one entry in
        this table for each active IPsec Phase\-2
        Tunnel.
        
        .. attribute:: cikepeercorrentry
        
        	Each entry contains the attributes of an IPsec Phase\-1 IKE Peer Association to IPsec Phase\-2 Tunnel Correlation
        	**type**\: list of :py:class:`CikePeerCorrEntry <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CikePeerCorrTable.CikePeerCorrEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cikepeercorrentry = YList()
            self.cikepeercorrentry.parent = self
            self.cikepeercorrentry.name = 'cikepeercorrentry'


        class CikePeerCorrEntry(object):
            """
            Each entry contains the attributes of an
            IPsec Phase\-1 IKE Peer Association to IPsec
            Phase\-2 Tunnel Correlation.
            
            .. attribute:: cikepeercorrintindex
            
            	The internal index of the local\-remote peer association.  This internal index is  used to uniquely identify multiple associations  between the local and remote peer
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cikepeercorrlocaltype
            
            	The type of local peer identity. The local peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\: :py:class:`IkePeerType_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType_Enum>`
            
            .. attribute:: cikepeercorrlocalvalue
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cikepeercorrremotetype
            
            	The type of remote peer identity. The remote peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\: :py:class:`IkePeerType_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType_Enum>`
            
            .. attribute:: cikepeercorrremotevalue
            
            	The value of the remote peer identity.  If the remote peer type is an IP Address, then this is the IP Address used to identify the remote peer.  If the remote peer type is a host name, then this is the host name used to identify the remote peer
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cikepeercorrseqnum
            
            	The sequence number of the local\-remote peer association.  This sequence number is  used to uniquely identify multiple instances  of an unique association between  the local and remote peer
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cikepeercorripsectunindex
            
            	The index of the active IPsec Phase\-2 Tunnel (cipSecTunIndex in the cipSecTunnelTable) for this IPsec Phase\-1 IKE Peer Association
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2007-10-24'

            def __init__(self):
                self.parent = None
                self.cikepeercorrintindex = None
                self.cikepeercorrlocaltype = None
                self.cikepeercorrlocalvalue = None
                self.cikepeercorrremotetype = None
                self.cikepeercorrremotevalue = None
                self.cikepeercorrseqnum = None
                self.cikepeercorripsectunindex = None

            @property
            def _common_path(self):
                if self.cikepeercorrintindex is None:
                    raise YPYDataValidationError('Key property cikepeercorrintindex is None')
                if self.cikepeercorrlocaltype is None:
                    raise YPYDataValidationError('Key property cikepeercorrlocaltype is None')
                if self.cikepeercorrlocalvalue is None:
                    raise YPYDataValidationError('Key property cikepeercorrlocalvalue is None')
                if self.cikepeercorrremotetype is None:
                    raise YPYDataValidationError('Key property cikepeercorrremotetype is None')
                if self.cikepeercorrremotevalue is None:
                    raise YPYDataValidationError('Key property cikepeercorrremotevalue is None')
                if self.cikepeercorrseqnum is None:
                    raise YPYDataValidationError('Key property cikepeercorrseqnum is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrIntIndex = ' + str(self.cikepeercorrintindex) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrLocalType = ' + str(self.cikepeercorrlocaltype) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrLocalValue = ' + str(self.cikepeercorrlocalvalue) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrRemoteType = ' + str(self.cikepeercorrremotetype) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrRemoteValue = ' + str(self.cikepeercorrremotevalue) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrSeqNum = ' + str(self.cikepeercorrseqnum) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cikepeercorrintindex is not None:
                    return True

                if self.cikepeercorrlocaltype is not None:
                    return True

                if self.cikepeercorrlocalvalue is not None:
                    return True

                if self.cikepeercorrremotetype is not None:
                    return True

                if self.cikepeercorrremotevalue is not None:
                    return True

                if self.cikepeercorrseqnum is not None:
                    return True

                if self.cikepeercorripsectunindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CikePeerCorrTable.CikePeerCorrEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cikepeercorrentry is not None:
                for child_ref in self.cikepeercorrentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CikePeerCorrTable']['meta_info']


    class CikePeerTable(object):
        """
        The IPsec Phase\-1 Internet Key Exchange Peer Table.
        There is one entry in this table for each IPsec
        Phase\-1 IKE peer association which is currently
        associated with an active IPsec Phase\-1 Tunnel.
        The IPsec Phase\-1 IKE Tunnel associated with this
        IPsec Phase\-1 IKE peer association may or may not
        be currently active.
        
        .. attribute:: cikepeerentry
        
        	Each entry contains the attributes associated with an IPsec Phase\-1 IKE peer association
        	**type**\: list of :py:class:`CikePeerEntry <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CikePeerTable.CikePeerEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cikepeerentry = YList()
            self.cikepeerentry.parent = self
            self.cikepeerentry.name = 'cikepeerentry'


        class CikePeerEntry(object):
            """
            Each entry contains the attributes associated
            with an IPsec Phase\-1 IKE peer association.
            
            .. attribute:: cikepeerintindex
            
            	The internal index of the local\-remote peer association.  This internal index is used  to uniquely identify multiple associations between  the local and remote peer
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cikepeerlocaltype
            
            	The type of local peer identity.  The local peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\: :py:class:`IkePeerType_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType_Enum>`
            
            .. attribute:: cikepeerlocalvalue
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cikepeerremotetype
            
            	The type of remote peer identity.  The remote peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\: :py:class:`IkePeerType_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType_Enum>`
            
            .. attribute:: cikepeerremotevalue
            
            	The value of the remote peer identity.  If the remote peer type is an IP Address, then this is the IP Address used to identify the remote peer.  If the remote peer type is a host name, then this is the host name used to identify the remote peer
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cikepeeractivetime
            
            	The length of time that the peer association has existed in hundredths of a second
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cikepeeractivetunnelindex
            
            	The index of the active IPsec Phase\-1 IKE Tunnel (cikeTunIndex in the cikeTunnelTable) for this peer association.  If an IPsec Phase\-1 IKE Tunnel is not currently active, then the value of this object will be zero
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cikepeerlocaladdr
            
            	The IP address of the local peer
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cikepeerremoteaddr
            
            	The IP address of the remote peer
            	**type**\: str
            
            	**range:** 4 \| 16
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2007-10-24'

            def __init__(self):
                self.parent = None
                self.cikepeerintindex = None
                self.cikepeerlocaltype = None
                self.cikepeerlocalvalue = None
                self.cikepeerremotetype = None
                self.cikepeerremotevalue = None
                self.cikepeeractivetime = None
                self.cikepeeractivetunnelindex = None
                self.cikepeerlocaladdr = None
                self.cikepeerremoteaddr = None

            @property
            def _common_path(self):
                if self.cikepeerintindex is None:
                    raise YPYDataValidationError('Key property cikepeerintindex is None')
                if self.cikepeerlocaltype is None:
                    raise YPYDataValidationError('Key property cikepeerlocaltype is None')
                if self.cikepeerlocalvalue is None:
                    raise YPYDataValidationError('Key property cikepeerlocalvalue is None')
                if self.cikepeerremotetype is None:
                    raise YPYDataValidationError('Key property cikepeerremotetype is None')
                if self.cikepeerremotevalue is None:
                    raise YPYDataValidationError('Key property cikepeerremotevalue is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerIntIndex = ' + str(self.cikepeerintindex) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerLocalType = ' + str(self.cikepeerlocaltype) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerLocalValue = ' + str(self.cikepeerlocalvalue) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerRemoteType = ' + str(self.cikepeerremotetype) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerRemoteValue = ' + str(self.cikepeerremotevalue) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cikepeerintindex is not None:
                    return True

                if self.cikepeerlocaltype is not None:
                    return True

                if self.cikepeerlocalvalue is not None:
                    return True

                if self.cikepeerremotetype is not None:
                    return True

                if self.cikepeerremotevalue is not None:
                    return True

                if self.cikepeeractivetime is not None:
                    return True

                if self.cikepeeractivetunnelindex is not None:
                    return True

                if self.cikepeerlocaladdr is not None:
                    return True

                if self.cikepeerremoteaddr is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CikePeerTable.CikePeerEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cikepeerentry is not None:
                for child_ref in self.cikepeerentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CikePeerTable']['meta_info']


    class CikePhase1GWStatsTable(object):
        """
        Phase\-1 IKE stats information is included in this table.
        Each entry is related to a specific gateway which is 
        identified by 'cmgwIndex'.
        
        .. attribute:: cikephase1gwstatsentry
        
        	Each entry contains the attributes of an Phase\-1 IKE stats information for the related gateway.  There is only one entry for each gateway. The entry  is created when a gateway up and cannot be deleted
        	**type**\: list of :py:class:`CikePhase1GWStatsEntry <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CikePhase1GWStatsTable.CikePhase1GWStatsEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cikephase1gwstatsentry = YList()
            self.cikephase1gwstatsentry.parent = self
            self.cikephase1gwstatsentry.name = 'cikephase1gwstatsentry'


        class CikePhase1GWStatsEntry(object):
            """
            Each entry contains the attributes of an Phase\-1 IKE stats
            information for the related gateway.
            
            There is only one entry for each gateway. The entry 
            is created when a gateway up and cannot be deleted.
            
            .. attribute:: cmgwindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cikephase1gwactivetunnels
            
            	The number of currently active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwauthfails
            
            	The total number of authentications which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwdecryptfails
            
            	The total number of decryptions which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwhashvalidfails
            
            	The total number of hash validations which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwindroppkts
            
            	The total number of packets which were dropped during receive processing by all  currently and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwinittunnelfails
            
            	The total number of IPsec Phase\-1 IKE Tunnels which were locally initiated and failed to activate
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwinittunnels
            
            	The total number of IPsec Phase\-1 IKE Tunnels which were locally initiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwinnotifys
            
            	The total number of notifys received by all currently and previously active IPsec  Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwinoctets
            
            	The total number of octets received by all currently and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwinp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges which were received and found to be invalid  by all currently and previously active IPsec  Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwinp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges which were received and rejected by all  currently and previously active IPsec Phase\-1  IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwinp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges received by all currently and previously  active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwinp2sadelrequests
            
            	The total number of IPsec Phase\-2 'Security Association' delete requests received by all  currently and previously active and IPsec  Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwinpkts
            
            	The total number of packets received by all currently and previously active IPsec  Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwnosafails
            
            	The total number of non\-existent 'Security Association' failures occurred during processing of current and  previous IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwoutdroppkts
            
            	The total number of packets which were dropped during send processing by all currently  and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwoutnotifys
            
            	The total number of notifys sent by all currently and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwoutoctets
            
            	The total number of octets sent by all currently and previously active and IPsec Phase\-1  IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwoutp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges which were sent and found to be invalid by  all currently and previously active IPsec Phase\-1  Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwoutp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges which were sent and rejected by all currently and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwoutp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges which were sent by all currently and previously  active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwoutp2sadelrequests
            
            	The total number of IPsec Phase\-2 SA delete requests sent by all currently and  previously active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwoutpkts
            
            	The total number of packets sent by all currently and previously active and IPsec Phase\-1  Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwprevioustunnels
            
            	The total number of previously active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwresptunnelfails
            
            	The total number of IPsec Phase\-1 IKE Tunnels which were remotely initiated and failed to activate
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwsyscapfails
            
            	The total number of system capacity failures which occurred during processing of all current  and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2007-10-24'

            def __init__(self):
                self.parent = None
                self.cmgwindex = None
                self.cikephase1gwactivetunnels = None
                self.cikephase1gwauthfails = None
                self.cikephase1gwdecryptfails = None
                self.cikephase1gwhashvalidfails = None
                self.cikephase1gwindroppkts = None
                self.cikephase1gwinittunnelfails = None
                self.cikephase1gwinittunnels = None
                self.cikephase1gwinnotifys = None
                self.cikephase1gwinoctets = None
                self.cikephase1gwinp2exchginvalids = None
                self.cikephase1gwinp2exchgrejects = None
                self.cikephase1gwinp2exchgs = None
                self.cikephase1gwinp2sadelrequests = None
                self.cikephase1gwinpkts = None
                self.cikephase1gwnosafails = None
                self.cikephase1gwoutdroppkts = None
                self.cikephase1gwoutnotifys = None
                self.cikephase1gwoutoctets = None
                self.cikephase1gwoutp2exchginvalids = None
                self.cikephase1gwoutp2exchgrejects = None
                self.cikephase1gwoutp2exchgs = None
                self.cikephase1gwoutp2sadelrequests = None
                self.cikephase1gwoutpkts = None
                self.cikephase1gwprevioustunnels = None
                self.cikephase1gwresptunnelfails = None
                self.cikephase1gwsyscapfails = None

            @property
            def _common_path(self):
                if self.cmgwindex is None:
                    raise YPYDataValidationError('Key property cmgwindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePhase1GWStatsTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePhase1GWStatsEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cmgwIndex = ' + str(self.cmgwindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cmgwindex is not None:
                    return True

                if self.cikephase1gwactivetunnels is not None:
                    return True

                if self.cikephase1gwauthfails is not None:
                    return True

                if self.cikephase1gwdecryptfails is not None:
                    return True

                if self.cikephase1gwhashvalidfails is not None:
                    return True

                if self.cikephase1gwindroppkts is not None:
                    return True

                if self.cikephase1gwinittunnelfails is not None:
                    return True

                if self.cikephase1gwinittunnels is not None:
                    return True

                if self.cikephase1gwinnotifys is not None:
                    return True

                if self.cikephase1gwinoctets is not None:
                    return True

                if self.cikephase1gwinp2exchginvalids is not None:
                    return True

                if self.cikephase1gwinp2exchgrejects is not None:
                    return True

                if self.cikephase1gwinp2exchgs is not None:
                    return True

                if self.cikephase1gwinp2sadelrequests is not None:
                    return True

                if self.cikephase1gwinpkts is not None:
                    return True

                if self.cikephase1gwnosafails is not None:
                    return True

                if self.cikephase1gwoutdroppkts is not None:
                    return True

                if self.cikephase1gwoutnotifys is not None:
                    return True

                if self.cikephase1gwoutoctets is not None:
                    return True

                if self.cikephase1gwoutp2exchginvalids is not None:
                    return True

                if self.cikephase1gwoutp2exchgrejects is not None:
                    return True

                if self.cikephase1gwoutp2exchgs is not None:
                    return True

                if self.cikephase1gwoutp2sadelrequests is not None:
                    return True

                if self.cikephase1gwoutpkts is not None:
                    return True

                if self.cikephase1gwprevioustunnels is not None:
                    return True

                if self.cikephase1gwresptunnelfails is not None:
                    return True

                if self.cikephase1gwsyscapfails is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CikePhase1GWStatsTable.CikePhase1GWStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePhase1GWStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cikephase1gwstatsentry is not None:
                for child_ref in self.cikephase1gwstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CikePhase1GWStatsTable']['meta_info']


    class CikeTunnelHistTable(object):
        """
        The IPsec Phase\-1 Internet Key Exchange Tunnel
        History Table.  This table is implemented as a 
        sliding window in which only the last n entries 
        are maintained.  The maximum number of entries
         is specified by the cipSecHistTableSize object.
        
        .. attribute:: ciketunnelhistentry
        
        	Each entry contains the attributes associated with a previously active IPsec  Phase\-1 IKE Tunnel
        	**type**\: list of :py:class:`CikeTunnelHistEntry <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable.CikeTunnelHistEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.ciketunnelhistentry = YList()
            self.ciketunnelhistentry.parent = self
            self.ciketunnelhistentry.name = 'ciketunnelhistentry'


        class CikeTunnelHistEntry(object):
            """
            Each entry contains the attributes
            associated with a previously active IPsec 
            Phase\-1 IKE Tunnel.
            
            .. attribute:: ciketunhistindex
            
            	The index of the IPsec Phase\-1 IKE Tunnel History Table.  The value of the index is a number which  begins at one and is incremented with each  tunnel that ends. The value of this object  will wrap at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciketunhistactiveindex
            
            	The index of the previously active IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciketunhistactivetime
            
            	The length of time the IPsec Phase\-1 IKE tunnel was been active in hundredths of seconds
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciketunhistauthmethod
            
            	The authentication method used in IPsec Phase\-1 IKE negotiations
            	**type**\: :py:class:`IkeAuthMethod_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeAuthMethod_Enum>`
            
            .. attribute:: ciketunhistdiffhellmangrp
            
            	The Diffie Hellman Group used in IPsec Phase\-1 IKE negotiations
            	**type**\: :py:class:`DiffHellmanGrp_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp_Enum>`
            
            .. attribute:: ciketunhistencryptalgo
            
            	The encryption algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\: :py:class:`EncryptAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo_Enum>`
            
            .. attribute:: ciketunhisthashalgo
            
            	The hash algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\: :py:class:`IkeHashAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeHashAlgo_Enum>`
            
            .. attribute:: ciketunhistindroppkts
            
            	The total number of packets dropped by this IPsec Phase\-1  IKE Tunnel during receive processing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhistinnotifys
            
            	The total number of notifys received by this IPsec Phase\-1  IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhistinoctets
            
            	The total number of octets received by this IPsec Phase\-1  IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhistinp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges received and  found to be invalid by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhistinp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges received and  rejected by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhistinp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges received by  this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhistinp2sadelrequests
            
            	The total number of IPsec Phase\-2 security association delete requests received by this IPsec  Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhistinpkts
            
            	The total number of packets received by this IPsec Phase\-1  IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhistlifetime
            
            	The negotiated LifeTime of the IPsec Phase\-1 IKE Tunnel in seconds
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciketunhistlocaladdr
            
            	The IP address of the local endpoint for the IPsec Phase\-1 IKE Tunnel
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: ciketunhistlocalname
            
            	The DNS name of the local IP address for the IPsec Phase\-1 IKE Tunnel. If the DNS  name associated with the local tunnel endpoint  is not known, then the value of this  object will be a NULL string
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: ciketunhistnegomode
            
            	The negotiation mode of the IPsec Phase\-1 IKE Tunnel
            	**type**\: :py:class:`IkeNegoMode_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeNegoMode_Enum>`
            
            .. attribute:: ciketunhistoutdroppkts
            
            	The total number of packets dropped by this IPsec Phase\-1  IKE Tunnel during send processing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhistoutnotifys
            
            	The total number of notifys sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhistoutoctets
            
            	The total number of octets sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhistoutp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges sent and found to be invalid by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhistoutp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges sent and rejected by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhistoutp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhistoutp2sadelrequests
            
            	The total number of IPsec Phase\-2 security association delete requests sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhistoutpkts
            
            	The total number of packets sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhistpeerintindex
            
            	The internal index of the local\-remote peer association.  This internal index is used to  uniquely identify multiple associations between  the local and remote peer
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciketunhistpeerlocaltype
            
            	The type of local peer identity.  The local peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\: :py:class:`IkePeerType_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType_Enum>`
            
            .. attribute:: ciketunhistpeerlocalvalue
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: ciketunhistpeerremotetype
            
            	The type of remote peer identity.  The remote peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\: :py:class:`IkePeerType_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType_Enum>`
            
            .. attribute:: ciketunhistpeerremotevalue
            
            	The value of the remote peer identity.  If the remote peer type is an IP Address, then this is the IP Address used to identify the remote peer.  If the remote peer type is a host name, then this is the host name used to identify the remote peer
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: ciketunhistremoteaddr
            
            	The IP address of the remote endpoint for the IPsec Phase\-1 IKE Tunnel
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: ciketunhistremotename
            
            	The DNS name of the remote IP address of IPsec Phase\-1 IKE Tunnel. If the DNS name associated with the remote tunnel endpoint is not known, then the value of this object will be a NULL string
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: ciketunhiststarttime
            
            	The value of sysUpTime in hundredths of seconds when the IPsec Phase\-1 IKE tunnel was started
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhisttermreason
            
            	The reason the IPsec Phase\-1 IKE Tunnel was terminated. Possible reasons include\: 1 = other 2 = normal termination 3 = operator request 4 = peer delete request was received 5 = contact with peer was lost 6 = local failure occurred. 7 = operator initiated check point request
            	**type**\: :py:class:`CikeTunHistTermReason_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable.CikeTunnelHistEntry.CikeTunHistTermReason_Enum>`
            
            .. attribute:: ciketunhisttotalrefreshes
            
            	The total number of security associations refreshes performed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhisttotalsas
            
            	The total number of security associations used during the  life of the IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2007-10-24'

            def __init__(self):
                self.parent = None
                self.ciketunhistindex = None
                self.ciketunhistactiveindex = None
                self.ciketunhistactivetime = None
                self.ciketunhistauthmethod = None
                self.ciketunhistdiffhellmangrp = None
                self.ciketunhistencryptalgo = None
                self.ciketunhisthashalgo = None
                self.ciketunhistindroppkts = None
                self.ciketunhistinnotifys = None
                self.ciketunhistinoctets = None
                self.ciketunhistinp2exchginvalids = None
                self.ciketunhistinp2exchgrejects = None
                self.ciketunhistinp2exchgs = None
                self.ciketunhistinp2sadelrequests = None
                self.ciketunhistinpkts = None
                self.ciketunhistlifetime = None
                self.ciketunhistlocaladdr = None
                self.ciketunhistlocalname = None
                self.ciketunhistnegomode = None
                self.ciketunhistoutdroppkts = None
                self.ciketunhistoutnotifys = None
                self.ciketunhistoutoctets = None
                self.ciketunhistoutp2exchginvalids = None
                self.ciketunhistoutp2exchgrejects = None
                self.ciketunhistoutp2exchgs = None
                self.ciketunhistoutp2sadelrequests = None
                self.ciketunhistoutpkts = None
                self.ciketunhistpeerintindex = None
                self.ciketunhistpeerlocaltype = None
                self.ciketunhistpeerlocalvalue = None
                self.ciketunhistpeerremotetype = None
                self.ciketunhistpeerremotevalue = None
                self.ciketunhistremoteaddr = None
                self.ciketunhistremotename = None
                self.ciketunhiststarttime = None
                self.ciketunhisttermreason = None
                self.ciketunhisttotalrefreshes = None
                self.ciketunhisttotalsas = None

            class CikeTunHistTermReason_Enum(Enum):
                """
                CikeTunHistTermReason_Enum

                The reason the IPsec Phase\-1 IKE Tunnel was terminated.
                Possible reasons include\:
                1 = other
                2 = normal termination
                3 = operator request
                4 = peer delete request was received
                5 = contact with peer was lost
                6 = local failure occurred.
                7 = operator initiated check point request

                """

                OTHER = 1

                NORMAL = 2

                OPERREQUEST = 3

                PEERDELREQUEST = 4

                PEERLOST = 5

                LOCALFAILURE = 6

                CHECKPOINTREG = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                    return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable.CikeTunnelHistEntry.CikeTunHistTermReason_Enum']


            @property
            def _common_path(self):
                if self.ciketunhistindex is None:
                    raise YPYDataValidationError('Key property ciketunhistindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeTunnelHistTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeTunnelHistEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cikeTunHistIndex = ' + str(self.ciketunhistindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciketunhistindex is not None:
                    return True

                if self.ciketunhistactiveindex is not None:
                    return True

                if self.ciketunhistactivetime is not None:
                    return True

                if self.ciketunhistauthmethod is not None:
                    return True

                if self.ciketunhistdiffhellmangrp is not None:
                    return True

                if self.ciketunhistencryptalgo is not None:
                    return True

                if self.ciketunhisthashalgo is not None:
                    return True

                if self.ciketunhistindroppkts is not None:
                    return True

                if self.ciketunhistinnotifys is not None:
                    return True

                if self.ciketunhistinoctets is not None:
                    return True

                if self.ciketunhistinp2exchginvalids is not None:
                    return True

                if self.ciketunhistinp2exchgrejects is not None:
                    return True

                if self.ciketunhistinp2exchgs is not None:
                    return True

                if self.ciketunhistinp2sadelrequests is not None:
                    return True

                if self.ciketunhistinpkts is not None:
                    return True

                if self.ciketunhistlifetime is not None:
                    return True

                if self.ciketunhistlocaladdr is not None:
                    return True

                if self.ciketunhistlocalname is not None:
                    return True

                if self.ciketunhistnegomode is not None:
                    return True

                if self.ciketunhistoutdroppkts is not None:
                    return True

                if self.ciketunhistoutnotifys is not None:
                    return True

                if self.ciketunhistoutoctets is not None:
                    return True

                if self.ciketunhistoutp2exchginvalids is not None:
                    return True

                if self.ciketunhistoutp2exchgrejects is not None:
                    return True

                if self.ciketunhistoutp2exchgs is not None:
                    return True

                if self.ciketunhistoutp2sadelrequests is not None:
                    return True

                if self.ciketunhistoutpkts is not None:
                    return True

                if self.ciketunhistpeerintindex is not None:
                    return True

                if self.ciketunhistpeerlocaltype is not None:
                    return True

                if self.ciketunhistpeerlocalvalue is not None:
                    return True

                if self.ciketunhistpeerremotetype is not None:
                    return True

                if self.ciketunhistpeerremotevalue is not None:
                    return True

                if self.ciketunhistremoteaddr is not None:
                    return True

                if self.ciketunhistremotename is not None:
                    return True

                if self.ciketunhiststarttime is not None:
                    return True

                if self.ciketunhisttermreason is not None:
                    return True

                if self.ciketunhisttotalrefreshes is not None:
                    return True

                if self.ciketunhisttotalsas is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable.CikeTunnelHistEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeTunnelHistTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciketunnelhistentry is not None:
                for child_ref in self.ciketunnelhistentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable']['meta_info']


    class CikeTunnelTable(object):
        """
        The IPsec Phase\-1 Internet Key Exchange Tunnel Table.
        There is one entry in this table for each active IPsec
        Phase\-1 IKE Tunnel.
        
        .. attribute:: ciketunnelentry
        
        	Each entry contains the attributes associated with an active IPsec Phase\-1 IKE Tunnel
        	**type**\: list of :py:class:`CikeTunnelEntry <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CikeTunnelTable.CikeTunnelEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.ciketunnelentry = YList()
            self.ciketunnelentry.parent = self
            self.ciketunnelentry.name = 'ciketunnelentry'


        class CikeTunnelEntry(object):
            """
            Each entry contains the attributes associated with
            an active IPsec Phase\-1 IKE Tunnel.
            
            .. attribute:: ciketunindex
            
            	The index of the IPsec Phase\-1 IKE Tunnel Table. The value of the index is a number which begins  at one and is incremented with each tunnel that  is created. The value of this object will  wrap at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciketunactivetime
            
            	The length of time the IPsec Phase\-1 IKE tunnel has been active in hundredths of seconds
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciketunauthmethod
            
            	The authentication method used in IPsec Phase\-1 IKE negotiations
            	**type**\: :py:class:`IkeAuthMethod_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeAuthMethod_Enum>`
            
            .. attribute:: ciketundiffhellmangrp
            
            	The Diffie Hellman Group used in IPsec Phase\-1 IKE negotiations
            	**type**\: :py:class:`DiffHellmanGrp_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp_Enum>`
            
            .. attribute:: ciketunencryptalgo
            
            	The encryption algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\: :py:class:`EncryptAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo_Enum>`
            
            .. attribute:: ciketunhashalgo
            
            	The hash algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\: :py:class:`IkeHashAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeHashAlgo_Enum>`
            
            .. attribute:: ciketunindroppkts
            
            	The total number of packets dropped by this IPsec Phase\-1 IKE Tunnel during  receive processing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketuninnotifys
            
            	The total number of notifys received by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketuninoctets
            
            	The total number of octets received by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketuninp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges received and found to be invalid  by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketuninp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges received and rejected by this IPsec Phase\-1  Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketuninp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges received by  this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketuninp2sadelrequests
            
            	The total number of IPsec Phase\-2 security association delete requests received  by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketuninpkts
            
            	The total number of packets received by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunlifetime
            
            	The negotiated LifeTime of the IPsec Phase\-1 IKE Tunnel in seconds
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciketunlocaladdr
            
            	The IP address of the local endpoint for the IPsec Phase\-1 IKE Tunnel
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: ciketunlocalname
            
            	The DNS name of the local IP address for the IPsec Phase\-1 IKE Tunnel. If the DNS  name associated with the local tunnel endpoint  is not known, then the value of this  object will be a NULL string
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: ciketunlocaltype
            
            	The type of local peer identity.  The local peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\: :py:class:`IkePeerType_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType_Enum>`
            
            .. attribute:: ciketunlocalvalue
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: ciketunnegomode
            
            	The negotiation mode of the IPsec Phase\-1 IKE Tunnel
            	**type**\: :py:class:`IkeNegoMode_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeNegoMode_Enum>`
            
            .. attribute:: ciketunoutdroppkts
            
            	The total number of packets dropped by this IPsec Phase\-1 IKE Tunnel during send processing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunoutnotifys
            
            	The total number of notifys sent by this IPsec Phase\-1 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunoutoctets
            
            	The total number of octets sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunoutp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges sent and found to be invalid by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunoutp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges sent and rejected by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunoutp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunoutp2sadelrequests
            
            	The total number of IPsec Phase\-2 security association delete requests sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunoutpkts
            
            	The total number of packets sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunremoteaddr
            
            	The IP address of the remote endpoint for the IPsec Phase\-1 IKE Tunnel
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: ciketunremotename
            
            	The DNS name of the remote IP address of IPsec Phase\-1 IKE Tunnel. If the DNS name associated with the remote tunnel endpoint is not known, then the value of this object will be a NULL string
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: ciketunremotetype
            
            	The type of remote peer identity. The remote peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\: :py:class:`IkePeerType_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType_Enum>`
            
            .. attribute:: ciketunremotevalue
            
            	The value of the remote peer identity.  If the remote peer type is an IP Address, then this is the IP Address used to identify the remote peer.  If the remote peer type is a host name, then  this is the host name used to identify the  remote peer
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: ciketunsarefreshthreshold
            
            	The security association refresh threshold in seconds
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciketunstatus
            
            	The status of the MIB table row.  This object can be used to bring the tunnel down  by setting value of this object to destroy(2).  This object cannot be used to create  a MIB table row
            	**type**\: :py:class:`TunnelStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.TunnelStatus_Enum>`
            
            .. attribute:: ciketuntotalrefreshes
            
            	The total number of security associations refreshes performed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2007-10-24'

            def __init__(self):
                self.parent = None
                self.ciketunindex = None
                self.ciketunactivetime = None
                self.ciketunauthmethod = None
                self.ciketundiffhellmangrp = None
                self.ciketunencryptalgo = None
                self.ciketunhashalgo = None
                self.ciketunindroppkts = None
                self.ciketuninnotifys = None
                self.ciketuninoctets = None
                self.ciketuninp2exchginvalids = None
                self.ciketuninp2exchgrejects = None
                self.ciketuninp2exchgs = None
                self.ciketuninp2sadelrequests = None
                self.ciketuninpkts = None
                self.ciketunlifetime = None
                self.ciketunlocaladdr = None
                self.ciketunlocalname = None
                self.ciketunlocaltype = None
                self.ciketunlocalvalue = None
                self.ciketunnegomode = None
                self.ciketunoutdroppkts = None
                self.ciketunoutnotifys = None
                self.ciketunoutoctets = None
                self.ciketunoutp2exchginvalids = None
                self.ciketunoutp2exchgrejects = None
                self.ciketunoutp2exchgs = None
                self.ciketunoutp2sadelrequests = None
                self.ciketunoutpkts = None
                self.ciketunremoteaddr = None
                self.ciketunremotename = None
                self.ciketunremotetype = None
                self.ciketunremotevalue = None
                self.ciketunsarefreshthreshold = None
                self.ciketunstatus = None
                self.ciketuntotalrefreshes = None

            @property
            def _common_path(self):
                if self.ciketunindex is None:
                    raise YPYDataValidationError('Key property ciketunindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeTunnelTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeTunnelEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cikeTunIndex = ' + str(self.ciketunindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciketunindex is not None:
                    return True

                if self.ciketunactivetime is not None:
                    return True

                if self.ciketunauthmethod is not None:
                    return True

                if self.ciketundiffhellmangrp is not None:
                    return True

                if self.ciketunencryptalgo is not None:
                    return True

                if self.ciketunhashalgo is not None:
                    return True

                if self.ciketunindroppkts is not None:
                    return True

                if self.ciketuninnotifys is not None:
                    return True

                if self.ciketuninoctets is not None:
                    return True

                if self.ciketuninp2exchginvalids is not None:
                    return True

                if self.ciketuninp2exchgrejects is not None:
                    return True

                if self.ciketuninp2exchgs is not None:
                    return True

                if self.ciketuninp2sadelrequests is not None:
                    return True

                if self.ciketuninpkts is not None:
                    return True

                if self.ciketunlifetime is not None:
                    return True

                if self.ciketunlocaladdr is not None:
                    return True

                if self.ciketunlocalname is not None:
                    return True

                if self.ciketunlocaltype is not None:
                    return True

                if self.ciketunlocalvalue is not None:
                    return True

                if self.ciketunnegomode is not None:
                    return True

                if self.ciketunoutdroppkts is not None:
                    return True

                if self.ciketunoutnotifys is not None:
                    return True

                if self.ciketunoutoctets is not None:
                    return True

                if self.ciketunoutp2exchginvalids is not None:
                    return True

                if self.ciketunoutp2exchgrejects is not None:
                    return True

                if self.ciketunoutp2exchgs is not None:
                    return True

                if self.ciketunoutp2sadelrequests is not None:
                    return True

                if self.ciketunoutpkts is not None:
                    return True

                if self.ciketunremoteaddr is not None:
                    return True

                if self.ciketunremotename is not None:
                    return True

                if self.ciketunremotetype is not None:
                    return True

                if self.ciketunremotevalue is not None:
                    return True

                if self.ciketunsarefreshthreshold is not None:
                    return True

                if self.ciketunstatus is not None:
                    return True

                if self.ciketuntotalrefreshes is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CikeTunnelTable.CikeTunnelEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeTunnelTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciketunnelentry is not None:
                for child_ref in self.ciketunnelentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CikeTunnelTable']['meta_info']


    class CipSecEndPtHistTable(object):
        """
        The IPsec Phase\-2 Tunnel Endpoint History Table.
        This table is implemented as a 
        sliding window in which only the
        last n entries are maintained.  
        The maximum number of entries
        is specified by the cipSecHistTableSize object.
        
        .. attribute:: cipsecendpthistentry
        
        	Each entry contains the attributes associated with a previously active IPsec Phase\-2 Tunnel Endpoint
        	**type**\: list of :py:class:`CipSecEndPtHistEntry <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecEndPtHistTable.CipSecEndPtHistEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cipsecendpthistentry = YList()
            self.cipsecendpthistentry.parent = self
            self.cipsecendpthistentry.name = 'cipsecendpthistentry'


        class CipSecEndPtHistEntry(object):
            """
            Each entry contains the attributes associated with
            a previously active IPsec Phase\-2 Tunnel Endpoint.
            
            .. attribute:: cipsecendpthistindex
            
            	The number of the previously active Endpoint associated  with a IPsec Phase\-2 Tunnel Table.  The value   of this index is a number which begins at   one and is incremented with each Endpoint   associated with an IPsec Phase\-2 Tunnel.  The value of this object will wrap at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecendpthistactiveindex
            
            	The index  of the previously active Endpoint
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecendpthistlocaladdr1
            
            	The local Endpoint's first IP address specification.  If the local Endpoint type is single IP address,  then this is the value of the IP address.  If the local Endpoint type is IP subnet, then this is the value of the subnet.  If the local Endpoint type is IP address range,  then this is the value of beginning IP address of  the range
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cipsecendpthistlocaladdr2
            
            	The local Endpoint's second IP address specification.  If the local Endpoint type is single IP address,  then this is the value of the IP address.  If the local Endpoint type is IP subnet, then this is the value of the subnet mask.  If the local Endpoint type is IP address range,  then this is the value of ending IP address of the range
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cipsecendpthistlocalname
            
            	The DNS name of the local Endpoint
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cipsecendpthistlocalport
            
            	The port number of the local Endpoint's traffic
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cipsecendpthistlocalprotocol
            
            	The protocol number of the local Endpoint's traffic
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cipsecendpthistlocaltype
            
            	The type of identity for the local Endpoint. Possible values are\: 1) a single IP address, or 2) an IP address range, or 3) an IP subnet
            	**type**\: :py:class:`EndPtType_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.EndPtType_Enum>`
            
            .. attribute:: cipsecendpthistremoteaddr1
            
            	The remote Endpoint's first IP address specification.  If the remote Endpoint type is single IP address,  then this is the value of the IP address.  If the remote Endpoint type is IP subnet, then this is the value of the subnet.  If the remote Endpoint type is IP address range,  then this is the value of beginning IP address of the range
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cipsecendpthistremoteaddr2
            
            	The remote Endpoint's second IP address specification.  If the remote Endpoint type is single IP address,  then this is the value of the IP address.  If the remote Endpoint type is IP subnet, then this is the value of the subnet mask.  If the remote Endpoint type is IP address range,  then this is the value of ending IP address of the range
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cipsecendpthistremotename
            
            	The DNS name of the remote Endpoint
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cipsecendpthistremoteport
            
            	The port number of the remote Endpoint's traffic
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cipsecendpthistremoteprotocol
            
            	The protocol number of the remote Endpoint's traffic
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cipsecendpthistremotetype
            
            	The type of identity for the remote Endpoint. Possible values are\: 1) a single IP address, or 2) an IP address range, or 3) an IP subnet
            	**type**\: :py:class:`EndPtType_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.EndPtType_Enum>`
            
            .. attribute:: cipsecendpthisttunindex
            
            	The index  of the previously active IPsec Phase\-2 Tunnel Table
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2007-10-24'

            def __init__(self):
                self.parent = None
                self.cipsecendpthistindex = None
                self.cipsecendpthistactiveindex = None
                self.cipsecendpthistlocaladdr1 = None
                self.cipsecendpthistlocaladdr2 = None
                self.cipsecendpthistlocalname = None
                self.cipsecendpthistlocalport = None
                self.cipsecendpthistlocalprotocol = None
                self.cipsecendpthistlocaltype = None
                self.cipsecendpthistremoteaddr1 = None
                self.cipsecendpthistremoteaddr2 = None
                self.cipsecendpthistremotename = None
                self.cipsecendpthistremoteport = None
                self.cipsecendpthistremoteprotocol = None
                self.cipsecendpthistremotetype = None
                self.cipsecendpthisttunindex = None

            @property
            def _common_path(self):
                if self.cipsecendpthistindex is None:
                    raise YPYDataValidationError('Key property cipsecendpthistindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecEndPtHistTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecEndPtHistEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecEndPtHistIndex = ' + str(self.cipsecendpthistindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cipsecendpthistindex is not None:
                    return True

                if self.cipsecendpthistactiveindex is not None:
                    return True

                if self.cipsecendpthistlocaladdr1 is not None:
                    return True

                if self.cipsecendpthistlocaladdr2 is not None:
                    return True

                if self.cipsecendpthistlocalname is not None:
                    return True

                if self.cipsecendpthistlocalport is not None:
                    return True

                if self.cipsecendpthistlocalprotocol is not None:
                    return True

                if self.cipsecendpthistlocaltype is not None:
                    return True

                if self.cipsecendpthistremoteaddr1 is not None:
                    return True

                if self.cipsecendpthistremoteaddr2 is not None:
                    return True

                if self.cipsecendpthistremotename is not None:
                    return True

                if self.cipsecendpthistremoteport is not None:
                    return True

                if self.cipsecendpthistremoteprotocol is not None:
                    return True

                if self.cipsecendpthistremotetype is not None:
                    return True

                if self.cipsecendpthisttunindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecEndPtHistTable.CipSecEndPtHistEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecEndPtHistTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsecendpthistentry is not None:
                for child_ref in self.cipsecendpthistentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecEndPtHistTable']['meta_info']


    class CipSecEndPtTable(object):
        """
        The IPsec Phase\-2 Tunnel Endpoint Table.
        This table contains an entry for each 
        active endpoint associated with an IPsec
         Phase\-2 Tunnel.
        
        .. attribute:: cipsecendptentry
        
        	An IPsec Phase\-2 Tunnel Endpoint entry
        	**type**\: list of :py:class:`CipSecEndPtEntry <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecEndPtTable.CipSecEndPtEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cipsecendptentry = YList()
            self.cipsecendptentry.parent = self
            self.cipsecendptentry.name = 'cipsecendptentry'


        class CipSecEndPtEntry(object):
            """
            An IPsec Phase\-2 Tunnel Endpoint entry.
            
            .. attribute:: cipsecendptindex
            
            	The number of the Endpoint associated with the IPsec Phase\-2 Tunnel Table.  The value of this index is a number which begins at one and  is incremented with each Endpoint associated  with an IPsec Phase\-2 Tunnel. The value of this object will wrap at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecendptlocaladdr1
            
            	The local Endpoint's first IP address specification.  If the local Endpoint type is single IP address,  then this is the value of the IP address.  If the local Endpoint type is IP subnet, then this is the value of the subnet.  If the local Endpoint type is IP address range,  then this is the value of beginning IP address  of the range
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cipsecendptlocaladdr2
            
            	The local Endpoint's second IP address specification.  If the local Endpoint type is single IP address,  then this is the value of the IP address.  If the local Endpoint type is IP subnet, then this is the value of the subnet mask.  If the local Endpoint type is IP address range,  then this is the value of ending IP address  of the range
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cipsecendptlocalname
            
            	The DNS name of the local Endpoint
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cipsecendptlocalport
            
            	The port number of the local Endpoint's traffic
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cipsecendptlocalprotocol
            
            	The protocol number of the local Endpoint's traffic
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cipsecendptlocaltype
            
            	The type of identity for the local Endpoint. Possible values are\: 1) a single IP address, or 2) an IP address range, or 3) an IP subnet
            	**type**\: :py:class:`EndPtType_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.EndPtType_Enum>`
            
            .. attribute:: cipsecendptremoteaddr1
            
            	The remote Endpoint's first IP address specification.  If the remote Endpoint type is single IP address,  then this is the value of the IP address.  If the remote Endpoint type is IP subnet, then this is the value of the subnet.  If the remote Endpoint type is IP address range,  then this is the value of beginning IP address  of the range
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cipsecendptremoteaddr2
            
            	The remote Endpoint's second IP address specification.  If the remote Endpoint type is single IP address,  then this is the value of the IP address.  If the remote Endpoint type is IP subnet, then this is the value of the subnet mask.  If the remote Endpoint type is IP address range,  then this is the value of ending IP address of  the range
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cipsecendptremotename
            
            	The DNS name of the remote Endpoint
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cipsecendptremoteport
            
            	The port number of the remote Endpoint's traffic
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cipsecendptremoteprotocol
            
            	The protocol number of the remote Endpoint's traffic
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cipsecendptremotetype
            
            	The type of identity for the remote Endpoint. Possible values are\: 1) a single IP address, or 2) an IP address range, or 3) an IP subnet
            	**type**\: :py:class:`EndPtType_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.EndPtType_Enum>`
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2007-10-24'

            def __init__(self):
                self.parent = None
                self.cipsecendptindex = None
                self.cipsectunindex = None
                self.cipsecendptlocaladdr1 = None
                self.cipsecendptlocaladdr2 = None
                self.cipsecendptlocalname = None
                self.cipsecendptlocalport = None
                self.cipsecendptlocalprotocol = None
                self.cipsecendptlocaltype = None
                self.cipsecendptremoteaddr1 = None
                self.cipsecendptremoteaddr2 = None
                self.cipsecendptremotename = None
                self.cipsecendptremoteport = None
                self.cipsecendptremoteprotocol = None
                self.cipsecendptremotetype = None

            @property
            def _common_path(self):
                if self.cipsecendptindex is None:
                    raise YPYDataValidationError('Key property cipsecendptindex is None')
                if self.cipsectunindex is None:
                    raise YPYDataValidationError('Key property cipsectunindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecEndPtTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecEndPtEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecEndPtIndex = ' + str(self.cipsecendptindex) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunIndex = ' + str(self.cipsectunindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cipsecendptindex is not None:
                    return True

                if self.cipsectunindex is not None:
                    return True

                if self.cipsecendptlocaladdr1 is not None:
                    return True

                if self.cipsecendptlocaladdr2 is not None:
                    return True

                if self.cipsecendptlocalname is not None:
                    return True

                if self.cipsecendptlocalport is not None:
                    return True

                if self.cipsecendptlocalprotocol is not None:
                    return True

                if self.cipsecendptlocaltype is not None:
                    return True

                if self.cipsecendptremoteaddr1 is not None:
                    return True

                if self.cipsecendptremoteaddr2 is not None:
                    return True

                if self.cipsecendptremotename is not None:
                    return True

                if self.cipsecendptremoteport is not None:
                    return True

                if self.cipsecendptremoteprotocol is not None:
                    return True

                if self.cipsecendptremotetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecEndPtTable.CipSecEndPtEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecEndPtTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsecendptentry is not None:
                for child_ref in self.cipsecendptentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecEndPtTable']['meta_info']


    class CipSecFailGlobalCntl(object):
        """
        
        
        .. attribute:: cipsecfailtablesize
        
        	The window size of the IPsec Phase\-1 and Phase\-2 Failure Tables.  The IPsec Phase\-1 and Phase\-2 Failure Tables are implemented as a sliding window in which only the last n entries are maintained.  This object is used specify the number of entries which will be  maintained in the IPsec Phase\-1 and Phase\-2 Failure  Tables.  An implementation may choose suitable minimum and  maximum values for this element based on the local  policy and available resources. If an SNMP SET request  specifies a value outside this window for this element,  a BAD VALUE may be returned
        	**type**\: int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cipsecfailtablesize = None

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecFailGlobalCntl'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsecfailtablesize is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecFailGlobalCntl']['meta_info']


    class CipSecFailTable(object):
        """
        The IPsec Phase\-2 Failure Table.
        This table is implemented as a sliding window 
        in which only the last n entries are maintained.  
        The maximum number of entries
        is specified by the cipSecFailTableSize object.
        
        .. attribute:: cipsecfailentry
        
        	Each entry contains the attributes associated with an IPsec Phase\-1 failure
        	**type**\: list of :py:class:`CipSecFailEntry <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecFailTable.CipSecFailEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cipsecfailentry = YList()
            self.cipsecfailentry.parent = self
            self.cipsecfailentry.name = 'cipsecfailentry'


        class CipSecFailEntry(object):
            """
            Each entry contains the attributes associated with
            an IPsec Phase\-1 failure.
            
            .. attribute:: cipsecfailindex
            
            	The IPsec Phase\-2 Failure Table index. The value of the index is a number which  begins at one and is incremented with each  IPsec Phase\-1 failure. The value of this object will wrap at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecfailpktdstaddr
            
            	The packet's destination IP address
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cipsecfailpktsrcaddr
            
            	The packet's source IP address
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cipsecfailreason
            
            	The reason for the failure.  Possible reasons include\:   1 = other   2 = internal error occurred   3 = peer encoding error   4 = proposal failure   5 = protocol use failure   6 = non\-existent security association   7 = decryption failure   8 = encryption failure   9 = inbound authentication failure  10 = outbound authentication failure  11 = compression failure  12 = system capacity failure  13 = peer delete request was received  14 = contact with peer was lost  15 = sequence number rolled over  16 = operator requested termination
            	**type**\: :py:class:`CipSecFailReason_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecFailTable.CipSecFailEntry.CipSecFailReason_Enum>`
            
            .. attribute:: cipsecfailsaspi
            
            	The security association SPI value
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cipsecfailtime
            
            	The value of sysUpTime in hundredths of seconds at the time of the failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecfailtunnelindex
            
            	The Phase\-2 Tunnel index (cipSecTunIndex)
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2007-10-24'

            def __init__(self):
                self.parent = None
                self.cipsecfailindex = None
                self.cipsecfailpktdstaddr = None
                self.cipsecfailpktsrcaddr = None
                self.cipsecfailreason = None
                self.cipsecfailsaspi = None
                self.cipsecfailtime = None
                self.cipsecfailtunnelindex = None

            class CipSecFailReason_Enum(Enum):
                """
                CipSecFailReason_Enum

                The reason for the failure.  Possible reasons
                include\:
                  1 = other
                  2 = internal error occurred
                  3 = peer encoding error
                  4 = proposal failure
                  5 = protocol use failure
                  6 = non\-existent security association
                  7 = decryption failure
                  8 = encryption failure
                  9 = inbound authentication failure
                 10 = outbound authentication failure
                 11 = compression failure
                 12 = system capacity failure
                 13 = peer delete request was received
                 14 = contact with peer was lost
                 15 = sequence number rolled over
                 16 = operator requested termination.

                """

                OTHER = 1

                INTERNALERROR = 2

                PEERENCODINGERROR = 3

                PROPOSALFAILURE = 4

                PROTOCOLUSEFAIL = 5

                NONEXISTENTSA = 6

                DECRYPTFAILURE = 7

                ENCRYPTFAILURE = 8

                INAUTHFAILURE = 9

                OUTAUTHFAILURE = 10

                COMPRESSION = 11

                SYSCAPEXCEEDED = 12

                PEERDELREQUEST = 13

                PEERLOST = 14

                SEQNUMROLLOVER = 15

                OPERREQUEST = 16


                @staticmethod
                def _meta_info():
                    from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                    return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecFailTable.CipSecFailEntry.CipSecFailReason_Enum']


            @property
            def _common_path(self):
                if self.cipsecfailindex is None:
                    raise YPYDataValidationError('Key property cipsecfailindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecFailTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecFailEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecFailIndex = ' + str(self.cipsecfailindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cipsecfailindex is not None:
                    return True

                if self.cipsecfailpktdstaddr is not None:
                    return True

                if self.cipsecfailpktsrcaddr is not None:
                    return True

                if self.cipsecfailreason is not None:
                    return True

                if self.cipsecfailsaspi is not None:
                    return True

                if self.cipsecfailtime is not None:
                    return True

                if self.cipsecfailtunnelindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecFailTable.CipSecFailEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecFailTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsecfailentry is not None:
                for child_ref in self.cipsecfailentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecFailTable']['meta_info']


    class CipSecGlobalStats(object):
        """
        
        
        .. attribute:: cipsecglobalactivetunnels
        
        	The total number of currently active IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobalhcindecompoctets
        
        	A high capacity count of the total number of decompressed octets received by all current  and previous IPsec Phase\-2 Tunnels.  This value  is accumulated AFTER the packet is decompressed.  If compression is not being used, this value   will match the value of cipSecGlobalHcInOctets
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: cipsecglobalhcinoctets
        
        	A high capacity count of the total number of octets received by all current and previous IPsec Phase\-2 Tunnels. This value is accumulated BEFORE determining whether or not the packet should be decompressed
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: cipsecglobalhcoutoctets
        
        	A high capacity count of the total number of octets sent by all current and previous  IPsec Phase\-2 Tunnels.  This value is accumulated  AFTER determining whether or not the packet should  be compressed
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: cipsecglobalhcoutuncompoctets
        
        	A high capacity count of the total number of uncompressed octets sent by all current and previous  IPsec Phase\-2 Tunnels.  This value is accumulated  BEFORE the packet is compressed.  If compression is  not being used, this value will match the       value of cipSecGlobalHcOutOctets
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: cipsecglobalinauthfails
        
        	The total number of inbound authentication's which ended in failure by all current and previous  IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobalinauths
        
        	The total number of inbound authentication's performed by all current and previous IPsec  Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobalindecompoctets
        
        	The total number of decompressed octets received by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated AFTER the packet is  decompressed. If compression is not being used,  this value will match the value of cipSecGlobalInOctets.  See also cipSecGlobalInDecompOctWraps  for the number of times this counter has wrapped
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobalindecompoctwraps
        
        	The number of times the global decompressed octets received counter  (cipSecGlobalInDecompOctets) has wrapped
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobalindecryptfails
        
        	The total number of inbound decryption's which ended in failure by all current and  previous IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobalindecrypts
        
        	The total number of inbound decryption's performed by all current and previous IPsec  Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobalindrops
        
        	The total number of packets dropped during receive processing by all current and previous  IPsec Phase\-2 Tunnels. This count does NOT include packets dropped due to  Anti\-Replay processing
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobalinoctets
        
        	The total number of octets received by all current and previous IPsec Phase\-2 Tunnels.  This value is accumulated BEFORE determining whether or not the packet should be decompressed. See also cipSecGlobalInOctWraps for the number of times this counter has wrapped
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobalinoctwraps
        
        	The number of times the global octets received counter (cipSecGlobalInOctets) has wrapped
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobalinpkts
        
        	The total number of packets received by all current and previous  IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobalinreplaydrops
        
        	The total number of packets dropped during receive processing due to Anti\-Replay  processing by all current and previous IPsec  Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobalnosafails
        
        	The total number of non\-existent Security Association in failures which occurred  during processing of all current  and previous IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobaloutauthfails
        
        	The total number of outbound authentication's which ended in failure  by all current and previous IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobaloutauths
        
        	The total number of outbound authentication's performed by all current and previous IPsec  Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobaloutdrops
        
        	The total number of packets dropped during send processing by all current and previous IPsec  Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobaloutencryptfails
        
        	The total number of outbound encryption's which ended in failure by all current and  previous IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobaloutencrypts
        
        	The total number of outbound encryption's performed by all current and previous IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobaloutoctets
        
        	The total number of octets sent by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated AFTER determining  whether or not the packet should be compressed.   See also cipSecGlobalOutOctWraps for the  number of times this counter has wrapped
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobaloutoctwraps
        
        	The number of times the global octets sent counter (cipSecGlobalOutOctets) has wrapped
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobaloutpkts
        
        	The total number of packets sent by all current and previous  IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobaloutuncompoctets
        
        	The total number of uncompressed octets sent by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated BEFORE the packet is  compressed. If compression is not being used, this  value will match the value of cipSecGlobalOutOctets.  See also cipSecGlobalOutDecompOctWraps for the number  of times this counter has wrapped
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobaloutuncompoctwraps
        
        	The number of times the global uncompressed octets sent counter (cipSecGlobalOutUncompOctets)  has wrapped
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobalprevioustunnels
        
        	The total number of previously active IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobalprotocolusefails
        
        	The total number of protocol use failures which occurred during processing of all current  and previously active IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobalsyscapfails
        
        	The total number of system capacity failures which occurred during processing of all current  and previously active IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cipsecglobalactivetunnels = None
            self.cipsecglobalhcindecompoctets = None
            self.cipsecglobalhcinoctets = None
            self.cipsecglobalhcoutoctets = None
            self.cipsecglobalhcoutuncompoctets = None
            self.cipsecglobalinauthfails = None
            self.cipsecglobalinauths = None
            self.cipsecglobalindecompoctets = None
            self.cipsecglobalindecompoctwraps = None
            self.cipsecglobalindecryptfails = None
            self.cipsecglobalindecrypts = None
            self.cipsecglobalindrops = None
            self.cipsecglobalinoctets = None
            self.cipsecglobalinoctwraps = None
            self.cipsecglobalinpkts = None
            self.cipsecglobalinreplaydrops = None
            self.cipsecglobalnosafails = None
            self.cipsecglobaloutauthfails = None
            self.cipsecglobaloutauths = None
            self.cipsecglobaloutdrops = None
            self.cipsecglobaloutencryptfails = None
            self.cipsecglobaloutencrypts = None
            self.cipsecglobaloutoctets = None
            self.cipsecglobaloutoctwraps = None
            self.cipsecglobaloutpkts = None
            self.cipsecglobaloutuncompoctets = None
            self.cipsecglobaloutuncompoctwraps = None
            self.cipsecglobalprevioustunnels = None
            self.cipsecglobalprotocolusefails = None
            self.cipsecglobalsyscapfails = None

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecGlobalStats'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsecglobalactivetunnels is not None:
                return True

            if self.cipsecglobalhcindecompoctets is not None:
                return True

            if self.cipsecglobalhcinoctets is not None:
                return True

            if self.cipsecglobalhcoutoctets is not None:
                return True

            if self.cipsecglobalhcoutuncompoctets is not None:
                return True

            if self.cipsecglobalinauthfails is not None:
                return True

            if self.cipsecglobalinauths is not None:
                return True

            if self.cipsecglobalindecompoctets is not None:
                return True

            if self.cipsecglobalindecompoctwraps is not None:
                return True

            if self.cipsecglobalindecryptfails is not None:
                return True

            if self.cipsecglobalindecrypts is not None:
                return True

            if self.cipsecglobalindrops is not None:
                return True

            if self.cipsecglobalinoctets is not None:
                return True

            if self.cipsecglobalinoctwraps is not None:
                return True

            if self.cipsecglobalinpkts is not None:
                return True

            if self.cipsecglobalinreplaydrops is not None:
                return True

            if self.cipsecglobalnosafails is not None:
                return True

            if self.cipsecglobaloutauthfails is not None:
                return True

            if self.cipsecglobaloutauths is not None:
                return True

            if self.cipsecglobaloutdrops is not None:
                return True

            if self.cipsecglobaloutencryptfails is not None:
                return True

            if self.cipsecglobaloutencrypts is not None:
                return True

            if self.cipsecglobaloutoctets is not None:
                return True

            if self.cipsecglobaloutoctwraps is not None:
                return True

            if self.cipsecglobaloutpkts is not None:
                return True

            if self.cipsecglobaloutuncompoctets is not None:
                return True

            if self.cipsecglobaloutuncompoctwraps is not None:
                return True

            if self.cipsecglobalprevioustunnels is not None:
                return True

            if self.cipsecglobalprotocolusefails is not None:
                return True

            if self.cipsecglobalsyscapfails is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecGlobalStats']['meta_info']


    class CipSecHistGlobalCntl(object):
        """
        
        
        .. attribute:: cipsechistcheckpoint
        
        	The current state of check point processing.  This object will return ready when the agent is  ready to create on\-demand history entries for  active IPsec Tunnels or checkPoint when the  agent is currently creating on\-demand history  entries for active IPsec Tunnels.  By setting this value to checkPoint, the agent  will create\: a) an entry in the IPsec Phase\-1 Tunnel History     for each active IPsec Phase\-1 Tunnel and b) an entry in the IPsec Phase\-2 Tunnel History     Table and an entry in the IPsec Phase\-2     Tunnel EndPoint History Table    for each active IPsec Phase\-2 Tunnel
        	**type**\: :py:class:`CipSecHistCheckPoint_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecHistGlobalCntl.CipSecHistCheckPoint_Enum>`
        
        .. attribute:: cipsechisttablesize
        
        	The window size of the IPsec Phase\-1 and Phase\-2 History Tables.  The IPsec Phase\-1 and Phase\-2 History Tables are implemented as a sliding window in which only the last n entries are maintained.  This object is used specify the number of entries which will be  maintained in the IPsec Phase\-1 and  Phase\-2 History Tables.  An implementation may choose suitable minimum and  maximum values for this element based on the local  policy and available resources. If an SNMP SET request  specifies a value outside this window for this element,  a BAD VALUE may be returned
        	**type**\: int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cipsechistcheckpoint = None
            self.cipsechisttablesize = None

        class CipSecHistCheckPoint_Enum(Enum):
            """
            CipSecHistCheckPoint_Enum

            The current state of check point processing.
            
            This object will return ready when the agent is 
            ready to create on\-demand history entries for 
            active IPsec Tunnels or checkPoint when the 
            agent is currently creating on\-demand history 
            entries for active IPsec Tunnels.
            
            By setting this value to checkPoint, the agent 
            will create\:
            a) an entry in the IPsec Phase\-1 Tunnel History 
               for each active IPsec Phase\-1 Tunnel and
            b) an entry in the IPsec Phase\-2 Tunnel History 
               Table and an entry in the IPsec Phase\-2 
               Tunnel EndPoint History Table
               for each active IPsec Phase\-2 Tunnel.

            """

            READY = 1

            CHECKPOINT = 2


            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecHistGlobalCntl.CipSecHistCheckPoint_Enum']


        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecHistGlobalCntl'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsechistcheckpoint is not None:
                return True

            if self.cipsechisttablesize is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecHistGlobalCntl']['meta_info']


    class CipSecLevels(object):
        """
        
        
        .. attribute:: cipsecmiblevel
        
        	The level of the IPsec MIB
        	**type**\: int
        
        	**range:** 1..4096
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cipsecmiblevel = None

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecLevels'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsecmiblevel is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecLevels']['meta_info']


    class CipSecPhase2GWStatsTable(object):
        """
        Phase\-2 IPsec stats information is included in this table.
        Each entry is related to a specific gateway which is 
        identified by 'cmgwIndex'
        
        .. attribute:: cipsecphase2gwstatsentry
        
        	Each entry contains the attributes of an Phase\-2 IPsec stats information for the related gateway.  There is only one entry for each gateway. The entry  is created when a gateway up and cannot be deleted
        	**type**\: list of :py:class:`CipSecPhase2GWStatsEntry <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecPhase2GWStatsTable.CipSecPhase2GWStatsEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cipsecphase2gwstatsentry = YList()
            self.cipsecphase2gwstatsentry.parent = self
            self.cipsecphase2gwstatsentry.name = 'cipsecphase2gwstatsentry'


        class CipSecPhase2GWStatsEntry(object):
            """
            Each entry contains the attributes of an Phase\-2 IPsec stats
            information for the related gateway.
            
            There is only one entry for each gateway. The entry 
            is created when a gateway up and cannot be deleted.
            
            .. attribute:: cmgwindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecphase2gwactivetunnels
            
            	The total number of currently active IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwinauthfails
            
            	The total number of inbound authentication's which ended in failure by all current and previous  IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwinauths
            
            	The total number of inbound authentication's performed by all current and previous IPsec  Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwindecompoctets
            
            	The total number of decompressed octets received by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated AFTER the packet is  decompressed. If compression is not being used,  this value will match the value of cipSecGlobalInOctets.  See also cipSecGlobalInDecompOctWraps for the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwindecompoctwraps
            
            	The number of times the global decompressed octets received counter (cipSecGlobalInDecompOctets)  has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwindecryptfails
            
            	The total number of inbound decryption's which ended in failure by all current and  previous IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwindecrypts
            
            	The total number of inbound decryption's performed by all current and previous IPsec  Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwindrops
            
            	The total number of packets dropped during receive processing by all current and previous  IPsec Phase\-2 Tunnels. This count does NOT include  packets dropped due to Anti\-Replay processing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwinoctets
            
            	The total number of octets received by all current and previous IPsec Phase\-2 Tunnels.  This value is accumulated BEFORE determining  whether or not the packet should be decompressed.  See also cipSecGlobalInOctWraps for the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwinoctwraps
            
            	The number of times the global octets received counter (cipSecGlobalInOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwinpkts
            
            	The total number of packets received by all current and previous IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwinreplaydrops
            
            	The total number of packets dropped during receive processing due to Anti\-Replay  processing by all current and previous IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwnosafails
            
            	The total number of non\-existent Security Association in failures which occurred  during processing of all current and previous IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwoutauthfails
            
            	The total number of outbound authentication's which ended in failure by all current and previous IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwoutauths
            
            	The total number of outbound authentication's performed by all current and previous IPsec  Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwoutdrops
            
            	The total number of packets dropped during send processing by all current and previous IPsec  Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwoutencryptfails
            
            	The total number of outbound encryption's which ended in failure by all current and  previous IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwoutencrypts
            
            	The total number of outbound encryption's performed by all current and previous IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwoutoctets
            
            	The total number of octets sent by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated AFTER determining  whether or not the packet should be compressed.   See also cipSecGlobalOutOctWraps for the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwoutoctwraps
            
            	The number of times the global octets sent counter (cipSecGlobalOutOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwoutpkts
            
            	The total number of packets sent by all current and previous IPsec Phase\-2  Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwoutuncompoctets
            
            	The total number of uncompressed octets sent by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated BEFORE the packet is  compressed. If compression is not being used, this  value will match the value of cipSecGlobalOutOctets.  See also cipSecGlobalOutDecompOctWraps for the number  of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwoutuncompoctwraps
            
            	The number of times the global uncompressed octets sent counter (cipSecGlobalOutUncompOctets)  has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwprevioustunnels
            
            	The total number of previously active IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwprotocolusefails
            
            	The total number of protocol use failures which occurred during processing of all current  and previously active IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwsyscapfails
            
            	The total number of system capacity failures which occurred during processing of all current  and previously active IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2007-10-24'

            def __init__(self):
                self.parent = None
                self.cmgwindex = None
                self.cipsecphase2gwactivetunnels = None
                self.cipsecphase2gwinauthfails = None
                self.cipsecphase2gwinauths = None
                self.cipsecphase2gwindecompoctets = None
                self.cipsecphase2gwindecompoctwraps = None
                self.cipsecphase2gwindecryptfails = None
                self.cipsecphase2gwindecrypts = None
                self.cipsecphase2gwindrops = None
                self.cipsecphase2gwinoctets = None
                self.cipsecphase2gwinoctwraps = None
                self.cipsecphase2gwinpkts = None
                self.cipsecphase2gwinreplaydrops = None
                self.cipsecphase2gwnosafails = None
                self.cipsecphase2gwoutauthfails = None
                self.cipsecphase2gwoutauths = None
                self.cipsecphase2gwoutdrops = None
                self.cipsecphase2gwoutencryptfails = None
                self.cipsecphase2gwoutencrypts = None
                self.cipsecphase2gwoutoctets = None
                self.cipsecphase2gwoutoctwraps = None
                self.cipsecphase2gwoutpkts = None
                self.cipsecphase2gwoutuncompoctets = None
                self.cipsecphase2gwoutuncompoctwraps = None
                self.cipsecphase2gwprevioustunnels = None
                self.cipsecphase2gwprotocolusefails = None
                self.cipsecphase2gwsyscapfails = None

            @property
            def _common_path(self):
                if self.cmgwindex is None:
                    raise YPYDataValidationError('Key property cmgwindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecPhase2GWStatsTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecPhase2GWStatsEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cmgwIndex = ' + str(self.cmgwindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cmgwindex is not None:
                    return True

                if self.cipsecphase2gwactivetunnels is not None:
                    return True

                if self.cipsecphase2gwinauthfails is not None:
                    return True

                if self.cipsecphase2gwinauths is not None:
                    return True

                if self.cipsecphase2gwindecompoctets is not None:
                    return True

                if self.cipsecphase2gwindecompoctwraps is not None:
                    return True

                if self.cipsecphase2gwindecryptfails is not None:
                    return True

                if self.cipsecphase2gwindecrypts is not None:
                    return True

                if self.cipsecphase2gwindrops is not None:
                    return True

                if self.cipsecphase2gwinoctets is not None:
                    return True

                if self.cipsecphase2gwinoctwraps is not None:
                    return True

                if self.cipsecphase2gwinpkts is not None:
                    return True

                if self.cipsecphase2gwinreplaydrops is not None:
                    return True

                if self.cipsecphase2gwnosafails is not None:
                    return True

                if self.cipsecphase2gwoutauthfails is not None:
                    return True

                if self.cipsecphase2gwoutauths is not None:
                    return True

                if self.cipsecphase2gwoutdrops is not None:
                    return True

                if self.cipsecphase2gwoutencryptfails is not None:
                    return True

                if self.cipsecphase2gwoutencrypts is not None:
                    return True

                if self.cipsecphase2gwoutoctets is not None:
                    return True

                if self.cipsecphase2gwoutoctwraps is not None:
                    return True

                if self.cipsecphase2gwoutpkts is not None:
                    return True

                if self.cipsecphase2gwoutuncompoctets is not None:
                    return True

                if self.cipsecphase2gwoutuncompoctwraps is not None:
                    return True

                if self.cipsecphase2gwprevioustunnels is not None:
                    return True

                if self.cipsecphase2gwprotocolusefails is not None:
                    return True

                if self.cipsecphase2gwsyscapfails is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecPhase2GWStatsTable.CipSecPhase2GWStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecPhase2GWStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsecphase2gwstatsentry is not None:
                for child_ref in self.cipsecphase2gwstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecPhase2GWStatsTable']['meta_info']


    class CipSecSpiTable(object):
        """
        The IPsec Phase\-2 Security Protection Index Table.
        This table contains an entry for each active 
        and expiring security
         association.
        
        .. attribute:: cipsecspientry
        
        	Each entry contains the attributes associated with active and expiring IPsec Phase\-2  security associations
        	**type**\: list of :py:class:`CipSecSpiEntry <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cipsecspientry = YList()
            self.cipsecspientry.parent = self
            self.cipsecspientry.name = 'cipsecspientry'


        class CipSecSpiEntry(object):
            """
            Each entry contains the attributes associated with
            active and expiring IPsec Phase\-2 
            security associations.
            
            .. attribute:: cipsecspiindex
            
            	The number of the SPI associated with the Phase\-2 Tunnel Table.  The value of this  index is a number which begins at one and is  incremented with each SPI associated with an  IPsec Phase\-2 Tunnel.  The value of this  object will wrap at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecspidirection
            
            	The direction of the SPI
            	**type**\: :py:class:`CipSecSpiDirection_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry.CipSecSpiDirection_Enum>`
            
            .. attribute:: cipsecspiprotocol
            
            	The protocol of the SPI
            	**type**\: :py:class:`CipSecSpiProtocol_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry.CipSecSpiProtocol_Enum>`
            
            .. attribute:: cipsecspistatus
            
            	The status of the SPI
            	**type**\: :py:class:`CipSecSpiStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry.CipSecSpiStatus_Enum>`
            
            .. attribute:: cipsecspivalue
            
            	The value of the SPI
            	**type**\: int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2007-10-24'

            def __init__(self):
                self.parent = None
                self.cipsecspiindex = None
                self.cipsectunindex = None
                self.cipsecspidirection = None
                self.cipsecspiprotocol = None
                self.cipsecspistatus = None
                self.cipsecspivalue = None

            class CipSecSpiDirection_Enum(Enum):
                """
                CipSecSpiDirection_Enum

                The direction of the SPI.

                """

                IN = 1

                OUT = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                    return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry.CipSecSpiDirection_Enum']


            class CipSecSpiProtocol_Enum(Enum):
                """
                CipSecSpiProtocol_Enum

                The protocol of the SPI.

                """

                AH = 1

                ESP = 2

                IPCOMP = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                    return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry.CipSecSpiProtocol_Enum']


            class CipSecSpiStatus_Enum(Enum):
                """
                CipSecSpiStatus_Enum

                The status of the SPI.

                """

                ACTIVE = 1

                EXPIRING = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                    return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry.CipSecSpiStatus_Enum']


            @property
            def _common_path(self):
                if self.cipsecspiindex is None:
                    raise YPYDataValidationError('Key property cipsecspiindex is None')
                if self.cipsectunindex is None:
                    raise YPYDataValidationError('Key property cipsectunindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecSpiTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecSpiEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecSpiIndex = ' + str(self.cipsecspiindex) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunIndex = ' + str(self.cipsectunindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cipsecspiindex is not None:
                    return True

                if self.cipsectunindex is not None:
                    return True

                if self.cipsecspidirection is not None:
                    return True

                if self.cipsecspiprotocol is not None:
                    return True

                if self.cipsecspistatus is not None:
                    return True

                if self.cipsecspivalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecSpiTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsecspientry is not None:
                for child_ref in self.cipsecspientry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecSpiTable']['meta_info']


    class CipSecTrapCntl(object):
        """
        
        
        .. attribute:: cipsectrapcntlikecertcrlfailure
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 Certificate/CRL Failure TRAP
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipsectrapcntlikenosa
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 No Security Association TRAP
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipsectrapcntlikeprotocolfail
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 Protocol Failure TRAP
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipsectrapcntlikesysfailure
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 System Failure TRAP
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipsectrapcntliketunnelstart
        
        	This object defines the administrative state of sending the IPsec IKE Phase\-1 Tunnel Start TRAP
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipsectrapcntliketunnelstop
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 Tunnel Stop TRAP
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipsectrapcntlipsecearlytunterm
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Early Tunnel Termination TRAP
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipsectrapcntlipsecnosa
        
        	This object defines the administrative state of sending the IPsec  Phase\-2  No Security Association TRAP
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipsectrapcntlipsecprotocolfail
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Protocol Failure TRAP
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipsectrapcntlipsecsetupfailure
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Set Up Failure TRAP
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipsectrapcntlipsecsysfailure
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 System Failure TRAP
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipsectrapcntlipsectunnelstart
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Tunnel Start TRAP
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipsectrapcntlipsectunnelstop
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Tunnel Stop TRAP
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus_Enum>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cipsectrapcntlikecertcrlfailure = None
            self.cipsectrapcntlikenosa = None
            self.cipsectrapcntlikeprotocolfail = None
            self.cipsectrapcntlikesysfailure = None
            self.cipsectrapcntliketunnelstart = None
            self.cipsectrapcntliketunnelstop = None
            self.cipsectrapcntlipsecearlytunterm = None
            self.cipsectrapcntlipsecnosa = None
            self.cipsectrapcntlipsecprotocolfail = None
            self.cipsectrapcntlipsecsetupfailure = None
            self.cipsectrapcntlipsecsysfailure = None
            self.cipsectrapcntlipsectunnelstart = None
            self.cipsectrapcntlipsectunnelstop = None

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTrapCntl'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsectrapcntlikecertcrlfailure is not None:
                return True

            if self.cipsectrapcntlikenosa is not None:
                return True

            if self.cipsectrapcntlikeprotocolfail is not None:
                return True

            if self.cipsectrapcntlikesysfailure is not None:
                return True

            if self.cipsectrapcntliketunnelstart is not None:
                return True

            if self.cipsectrapcntliketunnelstop is not None:
                return True

            if self.cipsectrapcntlipsecearlytunterm is not None:
                return True

            if self.cipsectrapcntlipsecnosa is not None:
                return True

            if self.cipsectrapcntlipsecprotocolfail is not None:
                return True

            if self.cipsectrapcntlipsecsetupfailure is not None:
                return True

            if self.cipsectrapcntlipsecsysfailure is not None:
                return True

            if self.cipsectrapcntlipsectunnelstart is not None:
                return True

            if self.cipsectrapcntlipsectunnelstop is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecTrapCntl']['meta_info']


    class CipSecTunnelHistTable(object):
        """
        The IPsec Phase\-2 Tunnel History Table.
        This table is implemented as a sliding 
        window in which only the
        last n entries are maintained.  The maximum number 
        of entries
        is specified by the cipSecHistTableSize object.
        
        .. attribute:: cipsectunnelhistentry
        
        	Each entry contains the attributes associated with a previously active IPsec Phase\-2 Tunnel
        	**type**\: list of :py:class:`CipSecTunnelHistEntry <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable.CipSecTunnelHistEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cipsectunnelhistentry = YList()
            self.cipsectunnelhistentry.parent = self
            self.cipsectunnelhistentry.name = 'cipsectunnelhistentry'


        class CipSecTunnelHistEntry(object):
            """
            Each entry contains the attributes associated with
            a previously active IPsec Phase\-2 Tunnel.
            
            .. attribute:: cipsectunhistindex
            
            	The index of the IPsec Phase\-2 Tunnel History Table. The value of the index is a number which  begins at one and is incremented with each tunnel  that ends. The value of this object will wrap at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunhistactiveindex
            
            	The index of the previously active IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunhistactivetime
            
            	The length of time the IPsec Phase\-2 Tunnel has been active in hundredths of seconds
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cipsectunhistencapmode
            
            	The encapsulation mode used by the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`EncapMode_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.EncapMode_Enum>`
            
            .. attribute:: cipsectunhisthcindecompoctets
            
            	A high capacity count of the total number of decompressed octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER the packet is decompressed. If compression is not being used, this value will match the value of cipSecTunHistHcInOctets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunhisthcinoctets
            
            	A high capacity count of the total number of octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated BEFORE determining whether or not  the packet should be decompressed
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunhisthcoutoctets
            
            	A high capacity count of the total number of octets sent by this IPsec Phase\-2 Tunnel.  This value  is accumulated AFTER determining whether or not  the packet should be compressed
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunhisthcoutuncompoctets
            
            	A high capacity count of the total number of uncompressed octets sent by this  IPsec Phase\-2 Tunnel.  This value is accumulated  BEFORE the packet is compressed. If compression is not being used, this value will match the value of cipSecTunHistHcOutOctets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunhistiketunnelindex
            
            	The index of the associated IPsec Phase\-1 Tunnel (cikeTunIndex in the cikeTunnelTable)
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunhistinauthfails
            
            	The total number of inbound authentication's which ended in  failure by this IPsec Phase\-2 Tunnel 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistinauths
            
            	The total number of inbound authentication's performed  by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistindecompoctets
            
            	The total number of decompressed octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER the packet is decompressed. If compression is not being used, this value will match the value of cipSecTunHistInOctets. See also cipSecTunInDecompOctWraps for the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistindecompoctwraps
            
            	The number of times the decompressed octets received counter (cipSecTunInDecompOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistindecryptfails
            
            	The total number of inbound decryption's which ended in failure  by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistindecrypts
            
            	The total number of inbound decryption's performed by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistindroppkts
            
            	The total number of packets dropped during receive processing by this IPsec Phase\-2 Tunnel.  This count does NOT include packets  dropped due to Anti\-Replay processing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistinoctets
            
            	The total number of octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated BEFORE determining whether or not the packet should  be decompressed.  See also cipSecTunInOctWraps for  the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistinoctwraps
            
            	The number of times the octets received counter (cipSecTunInOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistinpkts
            
            	The total number of packets received by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistinreplaydroppkts
            
            	The total number of packets dropped during receive processing due to Anti\-Replay processing  by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistinsaahauthalgo
            
            	The authentication algorithm used by the inbound authentication header (AH) security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`AuthAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo_Enum>`
            
            .. attribute:: cipsectunhistinsadecompalgo
            
            	The decompression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`CompAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CompAlgo_Enum>`
            
            .. attribute:: cipsectunhistinsadiffhellmangrp
            
            	The Diffie Hellman Group used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`DiffHellmanGrp_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp_Enum>`
            
            .. attribute:: cipsectunhistinsaencryptalgo
            
            	The encryption algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`EncryptAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo_Enum>`
            
            .. attribute:: cipsectunhistinsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP)  security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`AuthAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo_Enum>`
            
            .. attribute:: cipsectunhistkeytype
            
            	The type of key used by the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`KeyType_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.KeyType_Enum>`
            
            .. attribute:: cipsectunhistlifesize
            
            	The negotiated LifeSize of the IPsec Phase\-2 Tunnel in kilobytes
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunhistlifetime
            
            	The negotiated LifeTime of the IPsec Phase\-2 Tunnel in seconds
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunhistlocaladdr
            
            	The IP address of the local endpoint for the IPsec Phase\-2 Tunnel
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cipsectunhistoutauthfails
            
            	The total number of outbound authentication's which ended in  failure by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistoutauths
            
            	The total number of outbound authentication's performed by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistoutdroppkts
            
            	The total number of packets dropped during send processing  by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistoutencryptfails
            
            	The total number of outbound encryption's which ended in failure  by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistoutencrypts
            
            	The total number of outbound encryption's performed by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistoutoctets
            
            	The total number of octets sent by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER determining whether or not the  packet should be compressed.  See also cipSecTunOutOctWraps for the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistoutoctwraps
            
            	The number of times the octets sent counter (cipSecTunOutOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistoutpkts
            
            	The total number of packets sent by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistoutsaahauthalgo
            
            	The authentication algorithm used by the outbound authentication header (AH) security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`AuthAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo_Enum>`
            
            .. attribute:: cipsectunhistoutsacompalgo
            
            	The compression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`CompAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CompAlgo_Enum>`
            
            .. attribute:: cipsectunhistoutsadiffhellmangrp
            
            	The Diffie Hellman Group used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`DiffHellmanGrp_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp_Enum>`
            
            .. attribute:: cipsectunhistoutsaencryptalgo
            
            	The encryption algorithm used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`EncryptAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo_Enum>`
            
            .. attribute:: cipsectunhistoutsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP)  security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`AuthAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo_Enum>`
            
            .. attribute:: cipsectunhistoutuncompoctets
            
            	The total number of uncompressed octets sent by this IPsec Phase\-2 Tunnel.  This value is accumulated BEFORE the packet is compressed. If compression is not being used, this value will match the value of  cipSecTunHistOutOctets.  See also  cipSecTunOutDecompOctWraps for the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistoutuncompoctwraps
            
            	The number of times the uncompressed octets sent counter (cipSecTunOutUncompOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistremoteaddr
            
            	The IP address of the remote endpoint for the IPsec Phase\-2 Tunnel
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cipsectunhiststarttime
            
            	The value of sysUpTime in hundredths of seconds when the IPsec Phase\-2 Tunnel was started
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhisttermreason
            
            	The reason the IPsec Phase\-2 Tunnel was terminated. Possible reasons include\: 1 = other 2 = normal termination 3 = operator request 4 = peer delete request was received 5 = contact with peer was lost 6 = local failure occurred 7 = operator initiated check point request
            	**type**\: :py:class:`CipSecTunHistTermReason_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable.CipSecTunnelHistEntry.CipSecTunHistTermReason_Enum>`
            
            .. attribute:: cipsectunhisttotalrefreshes
            
            	The total number of security association refreshes performed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhisttotalsas
            
            	The total number of security associations used during the  life of the IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2007-10-24'

            def __init__(self):
                self.parent = None
                self.cipsectunhistindex = None
                self.cipsectunhistactiveindex = None
                self.cipsectunhistactivetime = None
                self.cipsectunhistencapmode = None
                self.cipsectunhisthcindecompoctets = None
                self.cipsectunhisthcinoctets = None
                self.cipsectunhisthcoutoctets = None
                self.cipsectunhisthcoutuncompoctets = None
                self.cipsectunhistiketunnelindex = None
                self.cipsectunhistinauthfails = None
                self.cipsectunhistinauths = None
                self.cipsectunhistindecompoctets = None
                self.cipsectunhistindecompoctwraps = None
                self.cipsectunhistindecryptfails = None
                self.cipsectunhistindecrypts = None
                self.cipsectunhistindroppkts = None
                self.cipsectunhistinoctets = None
                self.cipsectunhistinoctwraps = None
                self.cipsectunhistinpkts = None
                self.cipsectunhistinreplaydroppkts = None
                self.cipsectunhistinsaahauthalgo = None
                self.cipsectunhistinsadecompalgo = None
                self.cipsectunhistinsadiffhellmangrp = None
                self.cipsectunhistinsaencryptalgo = None
                self.cipsectunhistinsaespauthalgo = None
                self.cipsectunhistkeytype = None
                self.cipsectunhistlifesize = None
                self.cipsectunhistlifetime = None
                self.cipsectunhistlocaladdr = None
                self.cipsectunhistoutauthfails = None
                self.cipsectunhistoutauths = None
                self.cipsectunhistoutdroppkts = None
                self.cipsectunhistoutencryptfails = None
                self.cipsectunhistoutencrypts = None
                self.cipsectunhistoutoctets = None
                self.cipsectunhistoutoctwraps = None
                self.cipsectunhistoutpkts = None
                self.cipsectunhistoutsaahauthalgo = None
                self.cipsectunhistoutsacompalgo = None
                self.cipsectunhistoutsadiffhellmangrp = None
                self.cipsectunhistoutsaencryptalgo = None
                self.cipsectunhistoutsaespauthalgo = None
                self.cipsectunhistoutuncompoctets = None
                self.cipsectunhistoutuncompoctwraps = None
                self.cipsectunhistremoteaddr = None
                self.cipsectunhiststarttime = None
                self.cipsectunhisttermreason = None
                self.cipsectunhisttotalrefreshes = None
                self.cipsectunhisttotalsas = None

            class CipSecTunHistTermReason_Enum(Enum):
                """
                CipSecTunHistTermReason_Enum

                The reason the IPsec Phase\-2 Tunnel was terminated.
                Possible reasons include\:
                1 = other
                2 = normal termination
                3 = operator request
                4 = peer delete request was received
                5 = contact with peer was lost
                6 = local failure occurred
                7 = operator initiated check point request

                """

                OTHER = 1

                NORMAL = 2

                OPERREQUEST = 3

                PEERDELREQUEST = 4

                PEERLOST = 5

                SEQNUMROLLOVER = 6

                CHECKPOINTREQ = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                    return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable.CipSecTunnelHistEntry.CipSecTunHistTermReason_Enum']


            @property
            def _common_path(self):
                if self.cipsectunhistindex is None:
                    raise YPYDataValidationError('Key property cipsectunhistindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunnelHistTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunnelHistEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunHistIndex = ' + str(self.cipsectunhistindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cipsectunhistindex is not None:
                    return True

                if self.cipsectunhistactiveindex is not None:
                    return True

                if self.cipsectunhistactivetime is not None:
                    return True

                if self.cipsectunhistencapmode is not None:
                    return True

                if self.cipsectunhisthcindecompoctets is not None:
                    return True

                if self.cipsectunhisthcinoctets is not None:
                    return True

                if self.cipsectunhisthcoutoctets is not None:
                    return True

                if self.cipsectunhisthcoutuncompoctets is not None:
                    return True

                if self.cipsectunhistiketunnelindex is not None:
                    return True

                if self.cipsectunhistinauthfails is not None:
                    return True

                if self.cipsectunhistinauths is not None:
                    return True

                if self.cipsectunhistindecompoctets is not None:
                    return True

                if self.cipsectunhistindecompoctwraps is not None:
                    return True

                if self.cipsectunhistindecryptfails is not None:
                    return True

                if self.cipsectunhistindecrypts is not None:
                    return True

                if self.cipsectunhistindroppkts is not None:
                    return True

                if self.cipsectunhistinoctets is not None:
                    return True

                if self.cipsectunhistinoctwraps is not None:
                    return True

                if self.cipsectunhistinpkts is not None:
                    return True

                if self.cipsectunhistinreplaydroppkts is not None:
                    return True

                if self.cipsectunhistinsaahauthalgo is not None:
                    return True

                if self.cipsectunhistinsadecompalgo is not None:
                    return True

                if self.cipsectunhistinsadiffhellmangrp is not None:
                    return True

                if self.cipsectunhistinsaencryptalgo is not None:
                    return True

                if self.cipsectunhistinsaespauthalgo is not None:
                    return True

                if self.cipsectunhistkeytype is not None:
                    return True

                if self.cipsectunhistlifesize is not None:
                    return True

                if self.cipsectunhistlifetime is not None:
                    return True

                if self.cipsectunhistlocaladdr is not None:
                    return True

                if self.cipsectunhistoutauthfails is not None:
                    return True

                if self.cipsectunhistoutauths is not None:
                    return True

                if self.cipsectunhistoutdroppkts is not None:
                    return True

                if self.cipsectunhistoutencryptfails is not None:
                    return True

                if self.cipsectunhistoutencrypts is not None:
                    return True

                if self.cipsectunhistoutoctets is not None:
                    return True

                if self.cipsectunhistoutoctwraps is not None:
                    return True

                if self.cipsectunhistoutpkts is not None:
                    return True

                if self.cipsectunhistoutsaahauthalgo is not None:
                    return True

                if self.cipsectunhistoutsacompalgo is not None:
                    return True

                if self.cipsectunhistoutsadiffhellmangrp is not None:
                    return True

                if self.cipsectunhistoutsaencryptalgo is not None:
                    return True

                if self.cipsectunhistoutsaespauthalgo is not None:
                    return True

                if self.cipsectunhistoutuncompoctets is not None:
                    return True

                if self.cipsectunhistoutuncompoctwraps is not None:
                    return True

                if self.cipsectunhistremoteaddr is not None:
                    return True

                if self.cipsectunhiststarttime is not None:
                    return True

                if self.cipsectunhisttermreason is not None:
                    return True

                if self.cipsectunhisttotalrefreshes is not None:
                    return True

                if self.cipsectunhisttotalsas is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable.CipSecTunnelHistEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunnelHistTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsectunnelhistentry is not None:
                for child_ref in self.cipsectunnelhistentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable']['meta_info']


    class CipSecTunnelTable(object):
        """
        The IPsec Phase\-2 Tunnel Table.
        There is one entry in this table for 
        each active IPsec Phase\-2 Tunnel.
        
        .. attribute:: cipsectunnelentry
        
        	Each entry contains the attributes associated with an active IPsec Phase\-2 Tunnel
        	**type**\: list of :py:class:`CipSecTunnelEntry <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.CipSecTunnelTable.CipSecTunnelEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cipsectunnelentry = YList()
            self.cipsectunnelentry.parent = self
            self.cipsectunnelentry.name = 'cipsectunnelentry'


        class CipSecTunnelEntry(object):
            """
            Each entry contains the attributes
            associated with an active IPsec Phase\-2 Tunnel.
            
            .. attribute:: cipsectunindex
            
            	The index of the IPsec Phase\-2 Tunnel Table. The value of the index is a number which begins  at one and is incremented with each tunnel that  is created. The value of this object will wrap  at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunactivetime
            
            	The length of time the IPsec Phase\-2 Tunnel has been  active in hundredths of seconds
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cipsectuncurrentsainstances
            
            	The number of security associations which are currently active or expiring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunencapmode
            
            	The encapsulation mode used by the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`EncapMode_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.EncapMode_Enum>`
            
            .. attribute:: cipsectunexpiredsainstances
            
            	The total number of security associations which have expired
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhcindecompoctets
            
            	A high capacity count of the total number of decompressed octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER the packet is decompressed. If compression is not being used, this value will match the value of cipSecTunHcInOctets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunhcinoctets
            
            	A high capacity count of the total number of octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated BEFORE determining whether or not the packet should be decompressed
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunhcoutoctets
            
            	A high capacity count of the total number of octets sent by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER determining whether or not the  packet should be compressed
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunhcoutuncompoctets
            
            	A high capacity count of the total number of uncompressed octets sent by this IPsec  Phase\-2 Tunnel.  This value is accumulated BEFORE  the packet is compressed. If compression  is not being used, this value will match the value  of cipSecTunHcOutOctets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectuniketunnelalive
            
            	An indicator which specifies whether or not the IPsec Phase\-1 IKE Tunnel currently exists
            	**type**\: bool
            
            .. attribute:: cipsectuniketunnelindex
            
            	The index of the associated IPsec Phase\-1 IKE Tunnel.  (cikeTunIndex in the cikeTunnelTable)
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectuninauthfails
            
            	The total number of inbound authentication's which ended in  failure by this IPsec Phase\-2 Tunnel 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectuninauths
            
            	The total number of inbound authentication's performed by this  IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunindecompoctets
            
            	The total number of decompressed octets received by this IPsec Phase\-2 Tunnel. This value is  accumulated AFTER the packet is decompressed.  If compression is not being  used, this value will match the value of   cipSecTunInOctets.  See also cipSecTunInDecompOctWraps   for the number of times  this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunindecompoctwraps
            
            	The number of times the decompressed octets received counter  (cipSecTunInDecompOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunindecryptfails
            
            	The total number of inbound decryption's which ended in failure  by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunindecrypts
            
            	The total number of inbound decryption's performed by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunindroppkts
            
            	The total number of packets dropped during receive processing by this IPsec Phase\-2  Tunnel. This count does NOT include  packets dropped due to Anti\-Replay processing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectuninoctets
            
            	The total number of octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated BEFORE determining whether or not the packet should be decompressed.  See also cipSecTunInOctWraps for the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectuninoctwraps
            
            	The number of times the octets received counter (cipSecTunInOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectuninpkts
            
            	The total number of packets received by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectuninreplaydroppkts
            
            	The total number of packets dropped during receive processing due to Anti\-Replay processing  by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectuninsaahauthalgo
            
            	The authentication algorithm used by the inbound authentication header (AH) security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`AuthAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo_Enum>`
            
            .. attribute:: cipsectuninsadecompalgo
            
            	The decompression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`CompAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CompAlgo_Enum>`
            
            .. attribute:: cipsectuninsadiffhellmangrp
            
            	The Diffie Hellman Group used by the inbound security association of the  IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`DiffHellmanGrp_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp_Enum>`
            
            .. attribute:: cipsectuninsaencryptalgo
            
            	The encryption algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`EncryptAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo_Enum>`
            
            .. attribute:: cipsectuninsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP) security  association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`AuthAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo_Enum>`
            
            .. attribute:: cipsectunkeytype
            
            	The type of key used by the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`KeyType_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.KeyType_Enum>`
            
            .. attribute:: cipsectunlifesize
            
            	The negotiated LifeSize of the IPsec Phase\-2 Tunnel in kilobytes
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunlifetime
            
            	The negotiated LifeTime of the IPsec Phase\-2 Tunnel in seconds
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunlocaladdr
            
            	The IP address of the local endpoint for the IPsec Phase\-2 Tunnel
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cipsectunoutauthfails
            
            	The total number of outbound authentication's which ended in failure  by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunoutauths
            
            	The total number of outbound authentication's performed by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunoutdroppkts
            
            	The total number of packets dropped during send processing by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunoutencryptfails
            
            	The total number of outbound encryption's which ended in failure by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunoutencrypts
            
            	The total number of outbound encryption's performed by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunoutoctets
            
            	The total number of octets sent by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER determining whether or not the packet should  be compressed.  See also cipSecTunOutOctWraps for the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunoutoctwraps
            
            	The number of times the out octets counter (cipSecTunOutOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunoutpkts
            
            	The total number of packets sent by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunoutsaahauthalgo
            
            	The authentication algorithm used by the outbound authentication header (AH) security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`AuthAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo_Enum>`
            
            .. attribute:: cipsectunoutsacompalgo
            
            	The compression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`CompAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.CompAlgo_Enum>`
            
            .. attribute:: cipsectunoutsadiffhellmangrp
            
            	The Diffie Hellman Group used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`DiffHellmanGrp_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp_Enum>`
            
            .. attribute:: cipsectunoutsaencryptalgo
            
            	The encryption algorithm used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`EncryptAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo_Enum>`
            
            .. attribute:: cipsectunoutsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP)  security association of the IPsec Phase\-2 Tunnel
            	**type**\: :py:class:`AuthAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo_Enum>`
            
            .. attribute:: cipsectunoutuncompoctets
            
            	The total number of uncompressed octets sent by this IPsec Phase\-2 Tunnel.  This value  is accumulated BEFORE the packet is compressed.  If compression is not being used, this value  will match the value of cipSecTunOutOctets.  See also cipSecTunOutDecompOctWraps for the   number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunoutuncompoctwraps
            
            	The number of times the uncompressed octets sent counter (cipSecTunOutUncompOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunremoteaddr
            
            	The IP address of the remote endpoint for the IPsec Phase\-2 Tunnel
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cipsectunsalifesizethreshold
            
            	The security association LifeSize refresh threshold in kilobytes
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunsalifetimethreshold
            
            	The security association LifeTime refresh threshold in seconds
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunstatus
            
            	The status of the MIB table row.  This object can be used to bring the tunnel down by setting value of this object to destroy(2). When the value is set to destroy(2), the SA bundle is destroyed and this row is deleted from this table.  When this MIB value is queried, the value of active(1) is always returned, if the instance  exists.  This object cannot be used to create a MIB  table row
            	**type**\: :py:class:`TunnelStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB.TunnelStatus_Enum>`
            
            .. attribute:: cipsectuntotalrefreshes
            
            	The total number of security association refreshes performed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2007-10-24'

            def __init__(self):
                self.parent = None
                self.cipsectunindex = None
                self.cipsectunactivetime = None
                self.cipsectuncurrentsainstances = None
                self.cipsectunencapmode = None
                self.cipsectunexpiredsainstances = None
                self.cipsectunhcindecompoctets = None
                self.cipsectunhcinoctets = None
                self.cipsectunhcoutoctets = None
                self.cipsectunhcoutuncompoctets = None
                self.cipsectuniketunnelalive = None
                self.cipsectuniketunnelindex = None
                self.cipsectuninauthfails = None
                self.cipsectuninauths = None
                self.cipsectunindecompoctets = None
                self.cipsectunindecompoctwraps = None
                self.cipsectunindecryptfails = None
                self.cipsectunindecrypts = None
                self.cipsectunindroppkts = None
                self.cipsectuninoctets = None
                self.cipsectuninoctwraps = None
                self.cipsectuninpkts = None
                self.cipsectuninreplaydroppkts = None
                self.cipsectuninsaahauthalgo = None
                self.cipsectuninsadecompalgo = None
                self.cipsectuninsadiffhellmangrp = None
                self.cipsectuninsaencryptalgo = None
                self.cipsectuninsaespauthalgo = None
                self.cipsectunkeytype = None
                self.cipsectunlifesize = None
                self.cipsectunlifetime = None
                self.cipsectunlocaladdr = None
                self.cipsectunoutauthfails = None
                self.cipsectunoutauths = None
                self.cipsectunoutdroppkts = None
                self.cipsectunoutencryptfails = None
                self.cipsectunoutencrypts = None
                self.cipsectunoutoctets = None
                self.cipsectunoutoctwraps = None
                self.cipsectunoutpkts = None
                self.cipsectunoutsaahauthalgo = None
                self.cipsectunoutsacompalgo = None
                self.cipsectunoutsadiffhellmangrp = None
                self.cipsectunoutsaencryptalgo = None
                self.cipsectunoutsaespauthalgo = None
                self.cipsectunoutuncompoctets = None
                self.cipsectunoutuncompoctwraps = None
                self.cipsectunremoteaddr = None
                self.cipsectunsalifesizethreshold = None
                self.cipsectunsalifetimethreshold = None
                self.cipsectunstatus = None
                self.cipsectuntotalrefreshes = None

            @property
            def _common_path(self):
                if self.cipsectunindex is None:
                    raise YPYDataValidationError('Key property cipsectunindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunnelTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunnelEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunIndex = ' + str(self.cipsectunindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cipsectunindex is not None:
                    return True

                if self.cipsectunactivetime is not None:
                    return True

                if self.cipsectuncurrentsainstances is not None:
                    return True

                if self.cipsectunencapmode is not None:
                    return True

                if self.cipsectunexpiredsainstances is not None:
                    return True

                if self.cipsectunhcindecompoctets is not None:
                    return True

                if self.cipsectunhcinoctets is not None:
                    return True

                if self.cipsectunhcoutoctets is not None:
                    return True

                if self.cipsectunhcoutuncompoctets is not None:
                    return True

                if self.cipsectuniketunnelalive is not None:
                    return True

                if self.cipsectuniketunnelindex is not None:
                    return True

                if self.cipsectuninauthfails is not None:
                    return True

                if self.cipsectuninauths is not None:
                    return True

                if self.cipsectunindecompoctets is not None:
                    return True

                if self.cipsectunindecompoctwraps is not None:
                    return True

                if self.cipsectunindecryptfails is not None:
                    return True

                if self.cipsectunindecrypts is not None:
                    return True

                if self.cipsectunindroppkts is not None:
                    return True

                if self.cipsectuninoctets is not None:
                    return True

                if self.cipsectuninoctwraps is not None:
                    return True

                if self.cipsectuninpkts is not None:
                    return True

                if self.cipsectuninreplaydroppkts is not None:
                    return True

                if self.cipsectuninsaahauthalgo is not None:
                    return True

                if self.cipsectuninsadecompalgo is not None:
                    return True

                if self.cipsectuninsadiffhellmangrp is not None:
                    return True

                if self.cipsectuninsaencryptalgo is not None:
                    return True

                if self.cipsectuninsaespauthalgo is not None:
                    return True

                if self.cipsectunkeytype is not None:
                    return True

                if self.cipsectunlifesize is not None:
                    return True

                if self.cipsectunlifetime is not None:
                    return True

                if self.cipsectunlocaladdr is not None:
                    return True

                if self.cipsectunoutauthfails is not None:
                    return True

                if self.cipsectunoutauths is not None:
                    return True

                if self.cipsectunoutdroppkts is not None:
                    return True

                if self.cipsectunoutencryptfails is not None:
                    return True

                if self.cipsectunoutencrypts is not None:
                    return True

                if self.cipsectunoutoctets is not None:
                    return True

                if self.cipsectunoutoctwraps is not None:
                    return True

                if self.cipsectunoutpkts is not None:
                    return True

                if self.cipsectunoutsaahauthalgo is not None:
                    return True

                if self.cipsectunoutsacompalgo is not None:
                    return True

                if self.cipsectunoutsadiffhellmangrp is not None:
                    return True

                if self.cipsectunoutsaencryptalgo is not None:
                    return True

                if self.cipsectunoutsaespauthalgo is not None:
                    return True

                if self.cipsectunoutuncompoctets is not None:
                    return True

                if self.cipsectunoutuncompoctwraps is not None:
                    return True

                if self.cipsectunremoteaddr is not None:
                    return True

                if self.cipsectunsalifesizethreshold is not None:
                    return True

                if self.cipsectunsalifetimethreshold is not None:
                    return True

                if self.cipsectunstatus is not None:
                    return True

                if self.cipsectuntotalrefreshes is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecTunnelTable.CipSecTunnelEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunnelTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsectunnelentry is not None:
                for child_ref in self.cipsectunnelentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CISCOIPSECFLOWMONITORMIB.CipSecTunnelTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cikefailtable is not None and self.cikefailtable._has_data():
            return True

        if self.cikefailtable is not None and self.cikefailtable.is_presence():
            return True

        if self.cikeglobalstats is not None and self.cikeglobalstats._has_data():
            return True

        if self.cikeglobalstats is not None and self.cikeglobalstats.is_presence():
            return True

        if self.cikepeercorrtable is not None and self.cikepeercorrtable._has_data():
            return True

        if self.cikepeercorrtable is not None and self.cikepeercorrtable.is_presence():
            return True

        if self.cikepeertable is not None and self.cikepeertable._has_data():
            return True

        if self.cikepeertable is not None and self.cikepeertable.is_presence():
            return True

        if self.cikephase1gwstatstable is not None and self.cikephase1gwstatstable._has_data():
            return True

        if self.cikephase1gwstatstable is not None and self.cikephase1gwstatstable.is_presence():
            return True

        if self.ciketunnelhisttable is not None and self.ciketunnelhisttable._has_data():
            return True

        if self.ciketunnelhisttable is not None and self.ciketunnelhisttable.is_presence():
            return True

        if self.ciketunneltable is not None and self.ciketunneltable._has_data():
            return True

        if self.ciketunneltable is not None and self.ciketunneltable.is_presence():
            return True

        if self.cipsecendpthisttable is not None and self.cipsecendpthisttable._has_data():
            return True

        if self.cipsecendpthisttable is not None and self.cipsecendpthisttable.is_presence():
            return True

        if self.cipsecendpttable is not None and self.cipsecendpttable._has_data():
            return True

        if self.cipsecendpttable is not None and self.cipsecendpttable.is_presence():
            return True

        if self.cipsecfailglobalcntl is not None and self.cipsecfailglobalcntl._has_data():
            return True

        if self.cipsecfailglobalcntl is not None and self.cipsecfailglobalcntl.is_presence():
            return True

        if self.cipsecfailtable is not None and self.cipsecfailtable._has_data():
            return True

        if self.cipsecfailtable is not None and self.cipsecfailtable.is_presence():
            return True

        if self.cipsecglobalstats is not None and self.cipsecglobalstats._has_data():
            return True

        if self.cipsecglobalstats is not None and self.cipsecglobalstats.is_presence():
            return True

        if self.cipsechistglobalcntl is not None and self.cipsechistglobalcntl._has_data():
            return True

        if self.cipsechistglobalcntl is not None and self.cipsechistglobalcntl.is_presence():
            return True

        if self.cipseclevels is not None and self.cipseclevels._has_data():
            return True

        if self.cipseclevels is not None and self.cipseclevels.is_presence():
            return True

        if self.cipsecphase2gwstatstable is not None and self.cipsecphase2gwstatstable._has_data():
            return True

        if self.cipsecphase2gwstatstable is not None and self.cipsecphase2gwstatstable.is_presence():
            return True

        if self.cipsecspitable is not None and self.cipsecspitable._has_data():
            return True

        if self.cipsecspitable is not None and self.cipsecspitable.is_presence():
            return True

        if self.cipsectrapcntl is not None and self.cipsectrapcntl._has_data():
            return True

        if self.cipsectrapcntl is not None and self.cipsectrapcntl.is_presence():
            return True

        if self.cipsectunnelhisttable is not None and self.cipsectunnelhisttable._has_data():
            return True

        if self.cipsectunnelhisttable is not None and self.cipsectunnelhisttable.is_presence():
            return True

        if self.cipsectunneltable is not None and self.cipsectunneltable._has_data():
            return True

        if self.cipsectunneltable is not None and self.cipsectunneltable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']


