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
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AuthAlgo(Enum):
    """
    AuthAlgo

    The authentication algorithm used by a

    security association of an IPsec Phase\-2 Tunnel.

    .. data:: none = 1

    .. data:: hmacMd5 = 2

    .. data:: hmacSha = 3

    """

    none = Enum.YLeaf(1, "none")

    hmacMd5 = Enum.YLeaf(2, "hmacMd5")

    hmacSha = Enum.YLeaf(3, "hmacSha")


class CompAlgo(Enum):
    """
    CompAlgo

    The compression algorithm used by a

    security association of an IPsec Phase\-2 Tunnel.

    .. data:: none = 1

    .. data:: ldf = 2

    """

    none = Enum.YLeaf(1, "none")

    ldf = Enum.YLeaf(2, "ldf")


class DiffHellmanGrp(Enum):
    """
    DiffHellmanGrp

    The Diffie Hellman Group used in negotiations.

    .. data:: none = 1

    .. data:: dhGroup1 = 2

    .. data:: dhGroup2 = 3

    """

    none = Enum.YLeaf(1, "none")

    dhGroup1 = Enum.YLeaf(2, "dhGroup1")

    dhGroup2 = Enum.YLeaf(3, "dhGroup2")


class EncapMode(Enum):
    """
    EncapMode

    The encapsulation mode used by an IPsec Phase\-2

    Tunnel.

    .. data:: tunnel = 1

    .. data:: transport = 2

    """

    tunnel = Enum.YLeaf(1, "tunnel")

    transport = Enum.YLeaf(2, "transport")


class EncryptAlgo(Enum):
    """
    EncryptAlgo

    The encryption algorithm used in negotiations.

    .. data:: none = 1

    .. data:: des = 2

    .. data:: des3 = 3

    """

    none = Enum.YLeaf(1, "none")

    des = Enum.YLeaf(2, "des")

    des3 = Enum.YLeaf(3, "des3")


class EndPtType(Enum):
    """
    EndPtType

    The type of identity use to specify an IPsec End Point.

    .. data:: singleIpAddr = 1

    .. data:: ipAddrRange = 2

    .. data:: ipSubnet = 3

    """

    singleIpAddr = Enum.YLeaf(1, "singleIpAddr")

    ipAddrRange = Enum.YLeaf(2, "ipAddrRange")

    ipSubnet = Enum.YLeaf(3, "ipSubnet")


class IkeAuthMethod(Enum):
    """
    IkeAuthMethod

    The authentication method used in IPsec Phase\-1 IKE

    negotiations.

    .. data:: none = 1

    .. data:: preSharedKey = 2

    .. data:: rsaSig = 3

    .. data:: rsaEncrypt = 4

    .. data:: revPublicKey = 5

    """

    none = Enum.YLeaf(1, "none")

    preSharedKey = Enum.YLeaf(2, "preSharedKey")

    rsaSig = Enum.YLeaf(3, "rsaSig")

    rsaEncrypt = Enum.YLeaf(4, "rsaEncrypt")

    revPublicKey = Enum.YLeaf(5, "revPublicKey")


class IkeHashAlgo(Enum):
    """
    IkeHashAlgo

    The hash algorithm used in IPsec Phase\-1

    IKE negotiations.

    .. data:: none = 1

    .. data:: md5 = 2

    .. data:: sha = 3

    """

    none = Enum.YLeaf(1, "none")

    md5 = Enum.YLeaf(2, "md5")

    sha = Enum.YLeaf(3, "sha")


class IkeNegoMode(Enum):
    """
    IkeNegoMode

    The IPsec Phase\-1 IKE negotiation mode.

    .. data:: main = 1

    .. data:: aggressive = 2

    """

    main = Enum.YLeaf(1, "main")

    aggressive = Enum.YLeaf(2, "aggressive")


class IkePeerType(Enum):
    """
    IkePeerType

    The type of IPsec Phase\-1 IKE peer identity.

    The IKE peer may be identified by\:

     1. an IP address, or

     2. a host name.

    .. data:: ipAddrPeer = 1

    .. data:: namePeer = 2

    """

    ipAddrPeer = Enum.YLeaf(1, "ipAddrPeer")

    namePeer = Enum.YLeaf(2, "namePeer")


class KeyType(Enum):
    """
    KeyType

    The type of key used by an IPsec Phase\-2 Tunnel.

    .. data:: ike = 1

    .. data:: manual = 2

    """

    ike = Enum.YLeaf(1, "ike")

    manual = Enum.YLeaf(2, "manual")


class TrapStatus(Enum):
    """
    TrapStatus

    The administrative status for sending a TRAP.

    .. data:: enabled = 1

    .. data:: disabled = 2

    """

    enabled = Enum.YLeaf(1, "enabled")

    disabled = Enum.YLeaf(2, "disabled")


class TunnelStatus(Enum):
    """
    TunnelStatus

    The status of a Tunnel.  Objects of this type may

    be used to bring the tunnel down by setting

    value of this object to destroy(2).  Objects of this

    type cannot be used to create a Tunnel.

    .. data:: active = 1

    .. data:: destroy = 2

    """

    active = Enum.YLeaf(1, "active")

    destroy = Enum.YLeaf(2, "destroy")



class CISCOIPSECFLOWMONITORMIB(Entity):
    """
    
    
    .. attribute:: cikefailtable
    
    	The IPsec Phase\-1 Failure Table. This table is implemented as a sliding  window in which only the last n entries are  maintained.  The maximum number of entries is specified by the cipSecFailTableSize object
    	**type**\:   :py:class:`Cikefailtable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikefailtable>`
    
    .. attribute:: cikeglobalstats
    
    	
    	**type**\:   :py:class:`Cikeglobalstats <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikeglobalstats>`
    
    .. attribute:: cikepeercorrtable
    
    	The IPsec Phase\-1 Internet Key Exchange Peer Association to IPsec Phase\-2 Tunnel Correlation Table. There is one entry in this table for each active IPsec Phase\-2 Tunnel
    	**type**\:   :py:class:`Cikepeercorrtable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikepeercorrtable>`
    
    .. attribute:: cikepeertable
    
    	The IPsec Phase\-1 Internet Key Exchange Peer Table. There is one entry in this table for each IPsec Phase\-1 IKE peer association which is currently associated with an active IPsec Phase\-1 Tunnel. The IPsec Phase\-1 IKE Tunnel associated with this IPsec Phase\-1 IKE peer association may or may not be currently active
    	**type**\:   :py:class:`Cikepeertable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikepeertable>`
    
    .. attribute:: cikephase1gwstatstable
    
    	Phase\-1 IKE stats information is included in this table. Each entry is related to a specific gateway which is  identified by 'cmgwIndex'
    	**type**\:   :py:class:`Cikephase1Gwstatstable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikephase1Gwstatstable>`
    
    .. attribute:: ciketunnelhisttable
    
    	The IPsec Phase\-1 Internet Key Exchange Tunnel History Table.  This table is implemented as a  sliding window in which only the last n entries  are maintained.  The maximum number of entries  is specified by the cipSecHistTableSize object
    	**type**\:   :py:class:`Ciketunnelhisttable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable>`
    
    .. attribute:: ciketunneltable
    
    	The IPsec Phase\-1 Internet Key Exchange Tunnel Table. There is one entry in this table for each active IPsec Phase\-1 IKE Tunnel
    	**type**\:   :py:class:`Ciketunneltable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Ciketunneltable>`
    
    .. attribute:: cipsecendpthisttable
    
    	The IPsec Phase\-2 Tunnel Endpoint History Table. This table is implemented as a  sliding window in which only the last n entries are maintained.   The maximum number of entries is specified by the cipSecHistTableSize object
    	**type**\:   :py:class:`Cipsecendpthisttable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable>`
    
    .. attribute:: cipsecendpttable
    
    	The IPsec Phase\-2 Tunnel Endpoint Table. This table contains an entry for each  active endpoint associated with an IPsec  Phase\-2 Tunnel
    	**type**\:   :py:class:`Cipsecendpttable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecendpttable>`
    
    .. attribute:: cipsecfailglobalcntl
    
    	
    	**type**\:   :py:class:`Cipsecfailglobalcntl <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecfailglobalcntl>`
    
    .. attribute:: cipsecfailtable
    
    	The IPsec Phase\-2 Failure Table. This table is implemented as a sliding window  in which only the last n entries are maintained.   The maximum number of entries is specified by the cipSecFailTableSize object
    	**type**\:   :py:class:`Cipsecfailtable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecfailtable>`
    
    .. attribute:: cipsecglobalstats
    
    	
    	**type**\:   :py:class:`Cipsecglobalstats <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecglobalstats>`
    
    .. attribute:: cipsechistglobalcntl
    
    	
    	**type**\:   :py:class:`Cipsechistglobalcntl <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsechistglobalcntl>`
    
    .. attribute:: cipseclevels
    
    	
    	**type**\:   :py:class:`Cipseclevels <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipseclevels>`
    
    .. attribute:: cipsecphase2gwstatstable
    
    	Phase\-2 IPsec stats information is included in this table. Each entry is related to a specific gateway which is  identified by 'cmgwIndex'
    	**type**\:   :py:class:`Cipsecphase2Gwstatstable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecphase2Gwstatstable>`
    
    .. attribute:: cipsecspitable
    
    	The IPsec Phase\-2 Security Protection Index Table. This table contains an entry for each active  and expiring security  association
    	**type**\:   :py:class:`Cipsecspitable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecspitable>`
    
    .. attribute:: cipsectrapcntl
    
    	
    	**type**\:   :py:class:`Cipsectrapcntl <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsectrapcntl>`
    
    .. attribute:: cipsectunnelhisttable
    
    	The IPsec Phase\-2 Tunnel History Table. This table is implemented as a sliding  window in which only the last n entries are maintained.  The maximum number  of entries is specified by the cipSecHistTableSize object
    	**type**\:   :py:class:`Cipsectunnelhisttable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable>`
    
    .. attribute:: cipsectunneltable
    
    	The IPsec Phase\-2 Tunnel Table. There is one entry in this table for  each active IPsec Phase\-2 Tunnel
    	**type**\:   :py:class:`Cipsectunneltable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsectunneltable>`
    
    

    """

    _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
    _revision = '2007-10-24'

    def __init__(self):
        super(CISCOIPSECFLOWMONITORMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
        self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"cikeFailTable" : ("cikefailtable", CISCOIPSECFLOWMONITORMIB.Cikefailtable), "cikeGlobalStats" : ("cikeglobalstats", CISCOIPSECFLOWMONITORMIB.Cikeglobalstats), "cikePeerCorrTable" : ("cikepeercorrtable", CISCOIPSECFLOWMONITORMIB.Cikepeercorrtable), "cikePeerTable" : ("cikepeertable", CISCOIPSECFLOWMONITORMIB.Cikepeertable), "cikePhase1GWStatsTable" : ("cikephase1gwstatstable", CISCOIPSECFLOWMONITORMIB.Cikephase1Gwstatstable), "cikeTunnelHistTable" : ("ciketunnelhisttable", CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable), "cikeTunnelTable" : ("ciketunneltable", CISCOIPSECFLOWMONITORMIB.Ciketunneltable), "cipSecEndPtHistTable" : ("cipsecendpthisttable", CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable), "cipSecEndPtTable" : ("cipsecendpttable", CISCOIPSECFLOWMONITORMIB.Cipsecendpttable), "cipSecFailGlobalCntl" : ("cipsecfailglobalcntl", CISCOIPSECFLOWMONITORMIB.Cipsecfailglobalcntl), "cipSecFailTable" : ("cipsecfailtable", CISCOIPSECFLOWMONITORMIB.Cipsecfailtable), "cipSecGlobalStats" : ("cipsecglobalstats", CISCOIPSECFLOWMONITORMIB.Cipsecglobalstats), "cipSecHistGlobalCntl" : ("cipsechistglobalcntl", CISCOIPSECFLOWMONITORMIB.Cipsechistglobalcntl), "cipSecLevels" : ("cipseclevels", CISCOIPSECFLOWMONITORMIB.Cipseclevels), "cipSecPhase2GWStatsTable" : ("cipsecphase2gwstatstable", CISCOIPSECFLOWMONITORMIB.Cipsecphase2Gwstatstable), "cipSecSpiTable" : ("cipsecspitable", CISCOIPSECFLOWMONITORMIB.Cipsecspitable), "cipSecTrapCntl" : ("cipsectrapcntl", CISCOIPSECFLOWMONITORMIB.Cipsectrapcntl), "cipSecTunnelHistTable" : ("cipsectunnelhisttable", CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable), "cipSecTunnelTable" : ("cipsectunneltable", CISCOIPSECFLOWMONITORMIB.Cipsectunneltable)}
        self._child_list_classes = {}

        self.cikefailtable = CISCOIPSECFLOWMONITORMIB.Cikefailtable()
        self.cikefailtable.parent = self
        self._children_name_map["cikefailtable"] = "cikeFailTable"
        self._children_yang_names.add("cikeFailTable")

        self.cikeglobalstats = CISCOIPSECFLOWMONITORMIB.Cikeglobalstats()
        self.cikeglobalstats.parent = self
        self._children_name_map["cikeglobalstats"] = "cikeGlobalStats"
        self._children_yang_names.add("cikeGlobalStats")

        self.cikepeercorrtable = CISCOIPSECFLOWMONITORMIB.Cikepeercorrtable()
        self.cikepeercorrtable.parent = self
        self._children_name_map["cikepeercorrtable"] = "cikePeerCorrTable"
        self._children_yang_names.add("cikePeerCorrTable")

        self.cikepeertable = CISCOIPSECFLOWMONITORMIB.Cikepeertable()
        self.cikepeertable.parent = self
        self._children_name_map["cikepeertable"] = "cikePeerTable"
        self._children_yang_names.add("cikePeerTable")

        self.cikephase1gwstatstable = CISCOIPSECFLOWMONITORMIB.Cikephase1Gwstatstable()
        self.cikephase1gwstatstable.parent = self
        self._children_name_map["cikephase1gwstatstable"] = "cikePhase1GWStatsTable"
        self._children_yang_names.add("cikePhase1GWStatsTable")

        self.ciketunnelhisttable = CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable()
        self.ciketunnelhisttable.parent = self
        self._children_name_map["ciketunnelhisttable"] = "cikeTunnelHistTable"
        self._children_yang_names.add("cikeTunnelHistTable")

        self.ciketunneltable = CISCOIPSECFLOWMONITORMIB.Ciketunneltable()
        self.ciketunneltable.parent = self
        self._children_name_map["ciketunneltable"] = "cikeTunnelTable"
        self._children_yang_names.add("cikeTunnelTable")

        self.cipsecendpthisttable = CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable()
        self.cipsecendpthisttable.parent = self
        self._children_name_map["cipsecendpthisttable"] = "cipSecEndPtHistTable"
        self._children_yang_names.add("cipSecEndPtHistTable")

        self.cipsecendpttable = CISCOIPSECFLOWMONITORMIB.Cipsecendpttable()
        self.cipsecendpttable.parent = self
        self._children_name_map["cipsecendpttable"] = "cipSecEndPtTable"
        self._children_yang_names.add("cipSecEndPtTable")

        self.cipsecfailglobalcntl = CISCOIPSECFLOWMONITORMIB.Cipsecfailglobalcntl()
        self.cipsecfailglobalcntl.parent = self
        self._children_name_map["cipsecfailglobalcntl"] = "cipSecFailGlobalCntl"
        self._children_yang_names.add("cipSecFailGlobalCntl")

        self.cipsecfailtable = CISCOIPSECFLOWMONITORMIB.Cipsecfailtable()
        self.cipsecfailtable.parent = self
        self._children_name_map["cipsecfailtable"] = "cipSecFailTable"
        self._children_yang_names.add("cipSecFailTable")

        self.cipsecglobalstats = CISCOIPSECFLOWMONITORMIB.Cipsecglobalstats()
        self.cipsecglobalstats.parent = self
        self._children_name_map["cipsecglobalstats"] = "cipSecGlobalStats"
        self._children_yang_names.add("cipSecGlobalStats")

        self.cipsechistglobalcntl = CISCOIPSECFLOWMONITORMIB.Cipsechistglobalcntl()
        self.cipsechistglobalcntl.parent = self
        self._children_name_map["cipsechistglobalcntl"] = "cipSecHistGlobalCntl"
        self._children_yang_names.add("cipSecHistGlobalCntl")

        self.cipseclevels = CISCOIPSECFLOWMONITORMIB.Cipseclevels()
        self.cipseclevels.parent = self
        self._children_name_map["cipseclevels"] = "cipSecLevels"
        self._children_yang_names.add("cipSecLevels")

        self.cipsecphase2gwstatstable = CISCOIPSECFLOWMONITORMIB.Cipsecphase2Gwstatstable()
        self.cipsecphase2gwstatstable.parent = self
        self._children_name_map["cipsecphase2gwstatstable"] = "cipSecPhase2GWStatsTable"
        self._children_yang_names.add("cipSecPhase2GWStatsTable")

        self.cipsecspitable = CISCOIPSECFLOWMONITORMIB.Cipsecspitable()
        self.cipsecspitable.parent = self
        self._children_name_map["cipsecspitable"] = "cipSecSpiTable"
        self._children_yang_names.add("cipSecSpiTable")

        self.cipsectrapcntl = CISCOIPSECFLOWMONITORMIB.Cipsectrapcntl()
        self.cipsectrapcntl.parent = self
        self._children_name_map["cipsectrapcntl"] = "cipSecTrapCntl"
        self._children_yang_names.add("cipSecTrapCntl")

        self.cipsectunnelhisttable = CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable()
        self.cipsectunnelhisttable.parent = self
        self._children_name_map["cipsectunnelhisttable"] = "cipSecTunnelHistTable"
        self._children_yang_names.add("cipSecTunnelHistTable")

        self.cipsectunneltable = CISCOIPSECFLOWMONITORMIB.Cipsectunneltable()
        self.cipsectunneltable.parent = self
        self._children_name_map["cipsectunneltable"] = "cipSecTunnelTable"
        self._children_yang_names.add("cipSecTunnelTable")
        self._segment_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB"


    class Cikefailtable(Entity):
        """
        The IPsec Phase\-1 Failure Table.
        This table is implemented as a sliding 
        window in which only the last n entries are 
        maintained.  The maximum number of entries
        is specified by the cipSecFailTableSize object.
        
        .. attribute:: cikefailentry
        
        	Each entry contains the attributes associated with  an IPsec Phase\-1 failure
        	**type**\: list of    :py:class:`Cikefailentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikefailtable.Cikefailentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cikefailtable, self).__init__()

            self.yang_name = "cikeFailTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cikeFailEntry" : ("cikefailentry", CISCOIPSECFLOWMONITORMIB.Cikefailtable.Cikefailentry)}

            self.cikefailentry = YList(self)
            self._segment_path = lambda: "cikeFailTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cikefailtable, [], name, value)


        class Cikefailentry(Entity):
            """
            Each entry contains the attributes associated
            with
             an IPsec Phase\-1 failure.
            
            .. attribute:: cikefailindex  <key>
            
            	The IPsec Phase\-1 Failure Table index. The value of the index is a number which  begins at one and is incremented with each  IPsec Phase\-1 failure. The value of this object will wrap at 2,147,483,647
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cikefaillocaladdr
            
            	The IP address of the local peer
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cikefaillocaltype
            
            	The type of local peer identity.  The local peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\:   :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: cikefaillocalvalue
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\:  str
            
            .. attribute:: cikefailreason
            
            	The reason for the failure.  Possible reasons include\: 1 = other 2 = peer delete request was received 3 = contact with peer was lost 4 = local failure occurred 5 = authentication failure 6 = hash validation failure 7 = encryption failure 8 = internal error occurred 9 = system capacity failure 10 = proposal failure 11 = peer's certificate is unavailable 12 = peer's certificate was found invalid 13 = local certificate expired 14 = certificate revoke list (crl) failure 15 = peer encoding error 16 = non\-existent security association 17 = operator requested termination
            	**type**\:   :py:class:`Cikefailreason <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikefailtable.Cikefailentry.Cikefailreason>`
            
            .. attribute:: cikefailremoteaddr
            
            	The IP address of the remote peer
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cikefailremotetype
            
            	The type of remote peer identity.  The remote peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\:   :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: cikefailremotevalue
            
            	The value of the remote peer identity.  If the remote peer type is an IP Address, then this is the IP Address used to identify the remote peer.  If the remote peer type is a host name, then this is the host name used to identify the remote peer
            	**type**\:  str
            
            .. attribute:: cikefailtime
            
            	The value of sysUpTime in hundredths of seconds at the time of the failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cikefailtable.Cikefailentry, self).__init__()

                self.yang_name = "cikeFailEntry"
                self.yang_parent_name = "cikeFailTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cikefailindex = YLeaf(YType.int32, "cikeFailIndex")

                self.cikefaillocaladdr = YLeaf(YType.str, "cikeFailLocalAddr")

                self.cikefaillocaltype = YLeaf(YType.enumeration, "cikeFailLocalType")

                self.cikefaillocalvalue = YLeaf(YType.str, "cikeFailLocalValue")

                self.cikefailreason = YLeaf(YType.enumeration, "cikeFailReason")

                self.cikefailremoteaddr = YLeaf(YType.str, "cikeFailRemoteAddr")

                self.cikefailremotetype = YLeaf(YType.enumeration, "cikeFailRemoteType")

                self.cikefailremotevalue = YLeaf(YType.str, "cikeFailRemoteValue")

                self.cikefailtime = YLeaf(YType.uint32, "cikeFailTime")
                self._segment_path = lambda: "cikeFailEntry" + "[cikeFailIndex='" + self.cikefailindex.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikeFailTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cikefailtable.Cikefailentry, ['cikefailindex', 'cikefaillocaladdr', 'cikefaillocaltype', 'cikefaillocalvalue', 'cikefailreason', 'cikefailremoteaddr', 'cikefailremotetype', 'cikefailremotevalue', 'cikefailtime'], name, value)

            class Cikefailreason(Enum):
                """
                Cikefailreason

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

                .. data:: other = 1

                .. data:: peerDelRequest = 2

                .. data:: peerLost = 3

                .. data:: localFailure = 4

                .. data:: authFailure = 5

                .. data:: hashValidation = 6

                .. data:: encryptFailure = 7

                .. data:: internalError = 8

                .. data:: sysCapExceeded = 9

                .. data:: proposalFailure = 10

                .. data:: peerCertUnavailable = 11

                .. data:: peerCertNotValid = 12

                .. data:: localCertExpired = 13

                .. data:: crlFailure = 14

                .. data:: peerEncodingError = 15

                .. data:: nonExistentSa = 16

                .. data:: operRequest = 17

                """

                other = Enum.YLeaf(1, "other")

                peerDelRequest = Enum.YLeaf(2, "peerDelRequest")

                peerLost = Enum.YLeaf(3, "peerLost")

                localFailure = Enum.YLeaf(4, "localFailure")

                authFailure = Enum.YLeaf(5, "authFailure")

                hashValidation = Enum.YLeaf(6, "hashValidation")

                encryptFailure = Enum.YLeaf(7, "encryptFailure")

                internalError = Enum.YLeaf(8, "internalError")

                sysCapExceeded = Enum.YLeaf(9, "sysCapExceeded")

                proposalFailure = Enum.YLeaf(10, "proposalFailure")

                peerCertUnavailable = Enum.YLeaf(11, "peerCertUnavailable")

                peerCertNotValid = Enum.YLeaf(12, "peerCertNotValid")

                localCertExpired = Enum.YLeaf(13, "localCertExpired")

                crlFailure = Enum.YLeaf(14, "crlFailure")

                peerEncodingError = Enum.YLeaf(15, "peerEncodingError")

                nonExistentSa = Enum.YLeaf(16, "nonExistentSa")

                operRequest = Enum.YLeaf(17, "operRequest")



    class Cikeglobalstats(Entity):
        """
        
        
        .. attribute:: cikeglobalactivetunnels
        
        	The number of currently active IPsec Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalauthfails
        
        	The total number of authentications which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cikeglobaldecryptfails
        
        	The total number of decryptions which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cikeglobalhashvalidfails
        
        	The total number of hash validations which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cikeglobalindroppkts
        
        	The total number of packets which were dropped during receive processing by all  currently and previously  active IPsec Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cikeglobalinittunnelfails
        
        	The total number of IPsec Phase\-1 IKE Tunnels which were locally initiated and failed to activate
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: SAs
        
        .. attribute:: cikeglobalinittunnels
        
        	The total number of IPsec Phase\-1 IKE Tunnels which were locally initiated
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: SAs
        
        .. attribute:: cikeglobalinnotifys
        
        	The total number of notifys received by all currently and previously active IPsec  Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Notification Payloads
        
        .. attribute:: cikeglobalinoctets
        
        	The total number of octets received by all currently and previously active IPsec Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Octets
        
        .. attribute:: cikeglobalinp2exchginvalids
        
        	The total number of IPsec Phase\-2 exchanges which were received and found to be invalid  by all currently and previously active IPsec  Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: SA Payloads
        
        .. attribute:: cikeglobalinp2exchgrejects
        
        	The total number of IPsec Phase\-2 exchanges which were received and rejected by all  currently and previously active IPsec Phase\-1  IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: SA Payloads
        
        .. attribute:: cikeglobalinp2exchgs
        
        	The total number of IPsec Phase\-2 exchanges received by all currently and previously  active IPsec Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: SA Payloads
        
        .. attribute:: cikeglobalinp2sadelrequests
        
        	The total number of IPsec Phase\-2 security association delete requests received by all  currently and previously  active and IPsec Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Notification Payloads
        
        .. attribute:: cikeglobalinpkts
        
        	The total number of packets received by all currently and previously active IPsec  Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cikeglobalnosafails
        
        	The total number of non\-existent Security Association in failures which occurred during processing of  all current and previous IPsec Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cikeglobaloutdroppkts
        
        	The total number of packets which were dropped during send processing by all currently  and previously  active IPsec Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cikeglobaloutnotifys
        
        	The total number of notifys sent by all currently and previously active IPsec Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Notification Payloads
        
        .. attribute:: cikeglobaloutoctets
        
        	The total number of octets sent by all currently and previously active and IPsec Phase\-1  IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Octets
        
        .. attribute:: cikeglobaloutp2exchginvalids
        
        	The total number of IPsec Phase\-2 exchanges which were sent and found to be invalid by  all currently and previously active IPsec Phase\-1  Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: SA Payloads
        
        .. attribute:: cikeglobaloutp2exchgrejects
        
        	The total number of IPsec Phase\-2 exchanges which were sent and rejected by all currently and  previously active IPsec Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: SA Payloads
        
        .. attribute:: cikeglobaloutp2exchgs
        
        	The total number of IPsec Phase\-2 exchanges which were sent by all currently and previously  active IPsec Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: SA Payloads
        
        .. attribute:: cikeglobaloutp2sadelrequests
        
        	The total number of IPsec Phase\-2 SA delete requests sent by all currently and  previously active IPsec Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Notification Payloads
        
        .. attribute:: cikeglobaloutpkts
        
        	The total number of packets sent by all currently and previously active and IPsec Phase\-1  Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cikeglobalprevioustunnels
        
        	The total number of previously active IPsec Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: SAs
        
        .. attribute:: cikeglobalresptunnelfails
        
        	The total number of IPsec Phase\-1 IKE Tunnels which were remotely initiated and failed to activate
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: SAs
        
        .. attribute:: cikeglobalsyscapfails
        
        	The total number of system capacity failures which occurred during processing of all current  and previously active IPsec Phase\-1 IKE Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cikeglobalstats, self).__init__()

            self.yang_name = "cikeGlobalStats"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.cikeglobalactivetunnels = YLeaf(YType.uint32, "cikeGlobalActiveTunnels")

            self.cikeglobalauthfails = YLeaf(YType.uint32, "cikeGlobalAuthFails")

            self.cikeglobaldecryptfails = YLeaf(YType.uint32, "cikeGlobalDecryptFails")

            self.cikeglobalhashvalidfails = YLeaf(YType.uint32, "cikeGlobalHashValidFails")

            self.cikeglobalindroppkts = YLeaf(YType.uint32, "cikeGlobalInDropPkts")

            self.cikeglobalinittunnelfails = YLeaf(YType.uint32, "cikeGlobalInitTunnelFails")

            self.cikeglobalinittunnels = YLeaf(YType.uint32, "cikeGlobalInitTunnels")

            self.cikeglobalinnotifys = YLeaf(YType.uint32, "cikeGlobalInNotifys")

            self.cikeglobalinoctets = YLeaf(YType.uint32, "cikeGlobalInOctets")

            self.cikeglobalinp2exchginvalids = YLeaf(YType.uint32, "cikeGlobalInP2ExchgInvalids")

            self.cikeglobalinp2exchgrejects = YLeaf(YType.uint32, "cikeGlobalInP2ExchgRejects")

            self.cikeglobalinp2exchgs = YLeaf(YType.uint32, "cikeGlobalInP2Exchgs")

            self.cikeglobalinp2sadelrequests = YLeaf(YType.uint32, "cikeGlobalInP2SaDelRequests")

            self.cikeglobalinpkts = YLeaf(YType.uint32, "cikeGlobalInPkts")

            self.cikeglobalnosafails = YLeaf(YType.uint32, "cikeGlobalNoSaFails")

            self.cikeglobaloutdroppkts = YLeaf(YType.uint32, "cikeGlobalOutDropPkts")

            self.cikeglobaloutnotifys = YLeaf(YType.uint32, "cikeGlobalOutNotifys")

            self.cikeglobaloutoctets = YLeaf(YType.uint32, "cikeGlobalOutOctets")

            self.cikeglobaloutp2exchginvalids = YLeaf(YType.uint32, "cikeGlobalOutP2ExchgInvalids")

            self.cikeglobaloutp2exchgrejects = YLeaf(YType.uint32, "cikeGlobalOutP2ExchgRejects")

            self.cikeglobaloutp2exchgs = YLeaf(YType.uint32, "cikeGlobalOutP2Exchgs")

            self.cikeglobaloutp2sadelrequests = YLeaf(YType.uint32, "cikeGlobalOutP2SaDelRequests")

            self.cikeglobaloutpkts = YLeaf(YType.uint32, "cikeGlobalOutPkts")

            self.cikeglobalprevioustunnels = YLeaf(YType.uint32, "cikeGlobalPreviousTunnels")

            self.cikeglobalresptunnelfails = YLeaf(YType.uint32, "cikeGlobalRespTunnelFails")

            self.cikeglobalsyscapfails = YLeaf(YType.uint32, "cikeGlobalSysCapFails")
            self._segment_path = lambda: "cikeGlobalStats"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cikeglobalstats, ['cikeglobalactivetunnels', 'cikeglobalauthfails', 'cikeglobaldecryptfails', 'cikeglobalhashvalidfails', 'cikeglobalindroppkts', 'cikeglobalinittunnelfails', 'cikeglobalinittunnels', 'cikeglobalinnotifys', 'cikeglobalinoctets', 'cikeglobalinp2exchginvalids', 'cikeglobalinp2exchgrejects', 'cikeglobalinp2exchgs', 'cikeglobalinp2sadelrequests', 'cikeglobalinpkts', 'cikeglobalnosafails', 'cikeglobaloutdroppkts', 'cikeglobaloutnotifys', 'cikeglobaloutoctets', 'cikeglobaloutp2exchginvalids', 'cikeglobaloutp2exchgrejects', 'cikeglobaloutp2exchgs', 'cikeglobaloutp2sadelrequests', 'cikeglobaloutpkts', 'cikeglobalprevioustunnels', 'cikeglobalresptunnelfails', 'cikeglobalsyscapfails'], name, value)


    class Cikepeercorrtable(Entity):
        """
        The IPsec Phase\-1 Internet Key Exchange Peer
        Association to IPsec Phase\-2 Tunnel
        Correlation Table. There is one entry in
        this table for each active IPsec Phase\-2
        Tunnel.
        
        .. attribute:: cikepeercorrentry
        
        	Each entry contains the attributes of an IPsec Phase\-1 IKE Peer Association to IPsec Phase\-2 Tunnel Correlation
        	**type**\: list of    :py:class:`Cikepeercorrentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikepeercorrtable.Cikepeercorrentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cikepeercorrtable, self).__init__()

            self.yang_name = "cikePeerCorrTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cikePeerCorrEntry" : ("cikepeercorrentry", CISCOIPSECFLOWMONITORMIB.Cikepeercorrtable.Cikepeercorrentry)}

            self.cikepeercorrentry = YList(self)
            self._segment_path = lambda: "cikePeerCorrTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cikepeercorrtable, [], name, value)


        class Cikepeercorrentry(Entity):
            """
            Each entry contains the attributes of an
            IPsec Phase\-1 IKE Peer Association to IPsec
            Phase\-2 Tunnel Correlation.
            
            .. attribute:: cikepeercorrlocaltype  <key>
            
            	The type of local peer identity. The local peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\:   :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: cikepeercorrlocalvalue  <key>
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\:  str
            
            .. attribute:: cikepeercorrremotetype  <key>
            
            	The type of remote peer identity. The remote peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\:   :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: cikepeercorrremotevalue  <key>
            
            	The value of the remote peer identity.  If the remote peer type is an IP Address, then this is the IP Address used to identify the remote peer.  If the remote peer type is a host name, then this is the host name used to identify the remote peer
            	**type**\:  str
            
            .. attribute:: cikepeercorrintindex  <key>
            
            	The internal index of the local\-remote peer association.  This internal index is  used to uniquely identify multiple associations  between the local and remote peer
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cikepeercorrseqnum  <key>
            
            	The sequence number of the local\-remote peer association.  This sequence number is  used to uniquely identify multiple instances  of an unique association between  the local and remote peer
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cikepeercorripsectunindex
            
            	The index of the active IPsec Phase\-2 Tunnel (cipSecTunIndex in the cipSecTunnelTable) for this IPsec Phase\-1 IKE Peer Association
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cikepeercorrtable.Cikepeercorrentry, self).__init__()

                self.yang_name = "cikePeerCorrEntry"
                self.yang_parent_name = "cikePeerCorrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cikepeercorrlocaltype = YLeaf(YType.enumeration, "cikePeerCorrLocalType")

                self.cikepeercorrlocalvalue = YLeaf(YType.str, "cikePeerCorrLocalValue")

                self.cikepeercorrremotetype = YLeaf(YType.enumeration, "cikePeerCorrRemoteType")

                self.cikepeercorrremotevalue = YLeaf(YType.str, "cikePeerCorrRemoteValue")

                self.cikepeercorrintindex = YLeaf(YType.int32, "cikePeerCorrIntIndex")

                self.cikepeercorrseqnum = YLeaf(YType.int32, "cikePeerCorrSeqNum")

                self.cikepeercorripsectunindex = YLeaf(YType.int32, "cikePeerCorrIpSecTunIndex")
                self._segment_path = lambda: "cikePeerCorrEntry" + "[cikePeerCorrLocalType='" + self.cikepeercorrlocaltype.get() + "']" + "[cikePeerCorrLocalValue='" + self.cikepeercorrlocalvalue.get() + "']" + "[cikePeerCorrRemoteType='" + self.cikepeercorrremotetype.get() + "']" + "[cikePeerCorrRemoteValue='" + self.cikepeercorrremotevalue.get() + "']" + "[cikePeerCorrIntIndex='" + self.cikepeercorrintindex.get() + "']" + "[cikePeerCorrSeqNum='" + self.cikepeercorrseqnum.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikePeerCorrTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cikepeercorrtable.Cikepeercorrentry, ['cikepeercorrlocaltype', 'cikepeercorrlocalvalue', 'cikepeercorrremotetype', 'cikepeercorrremotevalue', 'cikepeercorrintindex', 'cikepeercorrseqnum', 'cikepeercorripsectunindex'], name, value)


    class Cikepeertable(Entity):
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
        	**type**\: list of    :py:class:`Cikepeerentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikepeertable.Cikepeerentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cikepeertable, self).__init__()

            self.yang_name = "cikePeerTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cikePeerEntry" : ("cikepeerentry", CISCOIPSECFLOWMONITORMIB.Cikepeertable.Cikepeerentry)}

            self.cikepeerentry = YList(self)
            self._segment_path = lambda: "cikePeerTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cikepeertable, [], name, value)


        class Cikepeerentry(Entity):
            """
            Each entry contains the attributes associated
            with an IPsec Phase\-1 IKE peer association.
            
            .. attribute:: cikepeerlocaltype  <key>
            
            	The type of local peer identity.  The local peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\:   :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: cikepeerlocalvalue  <key>
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\:  str
            
            .. attribute:: cikepeerremotetype  <key>
            
            	The type of remote peer identity.  The remote peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\:   :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: cikepeerremotevalue  <key>
            
            	The value of the remote peer identity.  If the remote peer type is an IP Address, then this is the IP Address used to identify the remote peer.  If the remote peer type is a host name, then this is the host name used to identify the remote peer
            	**type**\:  str
            
            .. attribute:: cikepeerintindex  <key>
            
            	The internal index of the local\-remote peer association.  This internal index is used  to uniquely identify multiple associations between  the local and remote peer
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cikepeeractivetime
            
            	The length of time that the peer association has existed in hundredths of a second
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cikepeeractivetunnelindex
            
            	The index of the active IPsec Phase\-1 IKE Tunnel (cikeTunIndex in the cikeTunnelTable) for this peer association.  If an IPsec Phase\-1 IKE Tunnel is not currently active, then the value of this object will be zero
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cikepeerlocaladdr
            
            	The IP address of the local peer
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cikepeerremoteaddr
            
            	The IP address of the remote peer
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cikepeertable.Cikepeerentry, self).__init__()

                self.yang_name = "cikePeerEntry"
                self.yang_parent_name = "cikePeerTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cikepeerlocaltype = YLeaf(YType.enumeration, "cikePeerLocalType")

                self.cikepeerlocalvalue = YLeaf(YType.str, "cikePeerLocalValue")

                self.cikepeerremotetype = YLeaf(YType.enumeration, "cikePeerRemoteType")

                self.cikepeerremotevalue = YLeaf(YType.str, "cikePeerRemoteValue")

                self.cikepeerintindex = YLeaf(YType.int32, "cikePeerIntIndex")

                self.cikepeeractivetime = YLeaf(YType.int32, "cikePeerActiveTime")

                self.cikepeeractivetunnelindex = YLeaf(YType.int32, "cikePeerActiveTunnelIndex")

                self.cikepeerlocaladdr = YLeaf(YType.str, "cikePeerLocalAddr")

                self.cikepeerremoteaddr = YLeaf(YType.str, "cikePeerRemoteAddr")
                self._segment_path = lambda: "cikePeerEntry" + "[cikePeerLocalType='" + self.cikepeerlocaltype.get() + "']" + "[cikePeerLocalValue='" + self.cikepeerlocalvalue.get() + "']" + "[cikePeerRemoteType='" + self.cikepeerremotetype.get() + "']" + "[cikePeerRemoteValue='" + self.cikepeerremotevalue.get() + "']" + "[cikePeerIntIndex='" + self.cikepeerintindex.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikePeerTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cikepeertable.Cikepeerentry, ['cikepeerlocaltype', 'cikepeerlocalvalue', 'cikepeerremotetype', 'cikepeerremotevalue', 'cikepeerintindex', 'cikepeeractivetime', 'cikepeeractivetunnelindex', 'cikepeerlocaladdr', 'cikepeerremoteaddr'], name, value)


    class Cikephase1Gwstatstable(Entity):
        """
        Phase\-1 IKE stats information is included in this table.
        Each entry is related to a specific gateway which is 
        identified by 'cmgwIndex'.
        
        .. attribute:: cikephase1gwstatsentry
        
        	Each entry contains the attributes of an Phase\-1 IKE stats information for the related gateway.  There is only one entry for each gateway. The entry  is created when a gateway up and cannot be deleted
        	**type**\: list of    :py:class:`Cikephase1Gwstatsentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikephase1Gwstatstable.Cikephase1Gwstatsentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cikephase1Gwstatstable, self).__init__()

            self.yang_name = "cikePhase1GWStatsTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cikePhase1GWStatsEntry" : ("cikephase1gwstatsentry", CISCOIPSECFLOWMONITORMIB.Cikephase1Gwstatstable.Cikephase1Gwstatsentry)}

            self.cikephase1gwstatsentry = YList(self)
            self._segment_path = lambda: "cikePhase1GWStatsTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cikephase1Gwstatstable, [], name, value)


        class Cikephase1Gwstatsentry(Entity):
            """
            Each entry contains the attributes of an Phase\-1 IKE stats
            information for the related gateway.
            
            There is only one entry for each gateway. The entry 
            is created when a gateway up and cannot be deleted.
            
            .. attribute:: cmgwindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cikephase1gwactivetunnels
            
            	The number of currently active IPsec Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwauthfails
            
            	The total number of authentications which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cikephase1gwdecryptfails
            
            	The total number of decryptions which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cikephase1gwhashvalidfails
            
            	The total number of hash validations which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cikephase1gwindroppkts
            
            	The total number of packets which were dropped during receive processing by all  currently and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cikephase1gwinittunnelfails
            
            	The total number of IPsec Phase\-1 IKE Tunnels which were locally initiated and failed to activate
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SAs
            
            .. attribute:: cikephase1gwinittunnels
            
            	The total number of IPsec Phase\-1 IKE Tunnels which were locally initiated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SAs
            
            .. attribute:: cikephase1gwinnotifys
            
            	The total number of notifys received by all currently and previously active IPsec  Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: cikephase1gwinoctets
            
            	The total number of octets received by all currently and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cikephase1gwinp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges which were received and found to be invalid  by all currently and previously active IPsec  Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: cikephase1gwinp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges which were received and rejected by all  currently and previously active IPsec Phase\-1  IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: cikephase1gwinp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges received by all currently and previously  active IPsec Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: cikephase1gwinp2sadelrequests
            
            	The total number of IPsec Phase\-2 'Security Association' delete requests received by all  currently and previously active and IPsec  Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: cikephase1gwinpkts
            
            	The total number of packets received by all currently and previously active IPsec  Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cikephase1gwnosafails
            
            	The total number of non\-existent 'Security Association' failures occurred during processing of current and  previous IPsec Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cikephase1gwoutdroppkts
            
            	The total number of packets which were dropped during send processing by all currently  and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cikephase1gwoutnotifys
            
            	The total number of notifys sent by all currently and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: cikephase1gwoutoctets
            
            	The total number of octets sent by all currently and previously active and IPsec Phase\-1  IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cikephase1gwoutp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges which were sent and found to be invalid by  all currently and previously active IPsec Phase\-1  Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: cikephase1gwoutp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges which were sent and rejected by all currently and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: cikephase1gwoutp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges which were sent by all currently and previously  active IPsec Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: cikephase1gwoutp2sadelrequests
            
            	The total number of IPsec Phase\-2 SA delete requests sent by all currently and  previously active IPsec Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: cikephase1gwoutpkts
            
            	The total number of packets sent by all currently and previously active and IPsec Phase\-1  Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cikephase1gwprevioustunnels
            
            	The total number of previously active IPsec Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SAs
            
            .. attribute:: cikephase1gwresptunnelfails
            
            	The total number of IPsec Phase\-1 IKE Tunnels which were remotely initiated and failed to activate
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SAs
            
            .. attribute:: cikephase1gwsyscapfails
            
            	The total number of system capacity failures which occurred during processing of all current  and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cikephase1Gwstatstable.Cikephase1Gwstatsentry, self).__init__()

                self.yang_name = "cikePhase1GWStatsEntry"
                self.yang_parent_name = "cikePhase1GWStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cmgwindex = YLeaf(YType.str, "cmgwIndex")

                self.cikephase1gwactivetunnels = YLeaf(YType.uint32, "cikePhase1GWActiveTunnels")

                self.cikephase1gwauthfails = YLeaf(YType.uint32, "cikePhase1GWAuthFails")

                self.cikephase1gwdecryptfails = YLeaf(YType.uint32, "cikePhase1GWDecryptFails")

                self.cikephase1gwhashvalidfails = YLeaf(YType.uint32, "cikePhase1GWHashValidFails")

                self.cikephase1gwindroppkts = YLeaf(YType.uint32, "cikePhase1GWInDropPkts")

                self.cikephase1gwinittunnelfails = YLeaf(YType.uint32, "cikePhase1GWInitTunnelFails")

                self.cikephase1gwinittunnels = YLeaf(YType.uint32, "cikePhase1GWInitTunnels")

                self.cikephase1gwinnotifys = YLeaf(YType.uint32, "cikePhase1GWInNotifys")

                self.cikephase1gwinoctets = YLeaf(YType.uint32, "cikePhase1GWInOctets")

                self.cikephase1gwinp2exchginvalids = YLeaf(YType.uint32, "cikePhase1GWInP2ExchgInvalids")

                self.cikephase1gwinp2exchgrejects = YLeaf(YType.uint32, "cikePhase1GWInP2ExchgRejects")

                self.cikephase1gwinp2exchgs = YLeaf(YType.uint32, "cikePhase1GWInP2Exchgs")

                self.cikephase1gwinp2sadelrequests = YLeaf(YType.uint32, "cikePhase1GWInP2SaDelRequests")

                self.cikephase1gwinpkts = YLeaf(YType.uint32, "cikePhase1GWInPkts")

                self.cikephase1gwnosafails = YLeaf(YType.uint32, "cikePhase1GWNoSaFails")

                self.cikephase1gwoutdroppkts = YLeaf(YType.uint32, "cikePhase1GWOutDropPkts")

                self.cikephase1gwoutnotifys = YLeaf(YType.uint32, "cikePhase1GWOutNotifys")

                self.cikephase1gwoutoctets = YLeaf(YType.uint32, "cikePhase1GWOutOctets")

                self.cikephase1gwoutp2exchginvalids = YLeaf(YType.uint32, "cikePhase1GWOutP2ExchgInvalids")

                self.cikephase1gwoutp2exchgrejects = YLeaf(YType.uint32, "cikePhase1GWOutP2ExchgRejects")

                self.cikephase1gwoutp2exchgs = YLeaf(YType.uint32, "cikePhase1GWOutP2Exchgs")

                self.cikephase1gwoutp2sadelrequests = YLeaf(YType.uint32, "cikePhase1GWOutP2SaDelRequests")

                self.cikephase1gwoutpkts = YLeaf(YType.uint32, "cikePhase1GWOutPkts")

                self.cikephase1gwprevioustunnels = YLeaf(YType.uint32, "cikePhase1GWPreviousTunnels")

                self.cikephase1gwresptunnelfails = YLeaf(YType.uint32, "cikePhase1GWRespTunnelFails")

                self.cikephase1gwsyscapfails = YLeaf(YType.uint32, "cikePhase1GWSysCapFails")
                self._segment_path = lambda: "cikePhase1GWStatsEntry" + "[cmgwIndex='" + self.cmgwindex.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikePhase1GWStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cikephase1Gwstatstable.Cikephase1Gwstatsentry, ['cmgwindex', 'cikephase1gwactivetunnels', 'cikephase1gwauthfails', 'cikephase1gwdecryptfails', 'cikephase1gwhashvalidfails', 'cikephase1gwindroppkts', 'cikephase1gwinittunnelfails', 'cikephase1gwinittunnels', 'cikephase1gwinnotifys', 'cikephase1gwinoctets', 'cikephase1gwinp2exchginvalids', 'cikephase1gwinp2exchgrejects', 'cikephase1gwinp2exchgs', 'cikephase1gwinp2sadelrequests', 'cikephase1gwinpkts', 'cikephase1gwnosafails', 'cikephase1gwoutdroppkts', 'cikephase1gwoutnotifys', 'cikephase1gwoutoctets', 'cikephase1gwoutp2exchginvalids', 'cikephase1gwoutp2exchgrejects', 'cikephase1gwoutp2exchgs', 'cikephase1gwoutp2sadelrequests', 'cikephase1gwoutpkts', 'cikephase1gwprevioustunnels', 'cikephase1gwresptunnelfails', 'cikephase1gwsyscapfails'], name, value)


    class Ciketunnelhisttable(Entity):
        """
        The IPsec Phase\-1 Internet Key Exchange Tunnel
        History Table.  This table is implemented as a 
        sliding window in which only the last n entries 
        are maintained.  The maximum number of entries
         is specified by the cipSecHistTableSize object.
        
        .. attribute:: ciketunnelhistentry
        
        	Each entry contains the attributes associated with a previously active IPsec  Phase\-1 IKE Tunnel
        	**type**\: list of    :py:class:`Ciketunnelhistentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable.Ciketunnelhistentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable, self).__init__()

            self.yang_name = "cikeTunnelHistTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cikeTunnelHistEntry" : ("ciketunnelhistentry", CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable.Ciketunnelhistentry)}

            self.ciketunnelhistentry = YList(self)
            self._segment_path = lambda: "cikeTunnelHistTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable, [], name, value)


        class Ciketunnelhistentry(Entity):
            """
            Each entry contains the attributes
            associated with a previously active IPsec 
            Phase\-1 IKE Tunnel.
            
            .. attribute:: ciketunhistindex  <key>
            
            	The index of the IPsec Phase\-1 IKE Tunnel History Table.  The value of the index is a number which  begins at one and is incremented with each  tunnel that ends. The value of this object  will wrap at 2,147,483,647
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciketunhistactiveindex
            
            	The index of the previously active IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciketunhistactivetime
            
            	The length of time the IPsec Phase\-1 IKE tunnel was been active in hundredths of seconds
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciketunhistauthmethod
            
            	The authentication method used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`IkeAuthMethod <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeAuthMethod>`
            
            .. attribute:: ciketunhistdiffhellmangrp
            
            	The Diffie Hellman Group used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`DiffHellmanGrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp>`
            
            .. attribute:: ciketunhistencryptalgo
            
            	The encryption algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`EncryptAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo>`
            
            .. attribute:: ciketunhisthashalgo
            
            	The hash algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`IkeHashAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeHashAlgo>`
            
            .. attribute:: ciketunhistindroppkts
            
            	The total number of packets dropped by this IPsec Phase\-1  IKE Tunnel during receive processing
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: ciketunhistinnotifys
            
            	The total number of notifys received by this IPsec Phase\-1  IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: ciketunhistinoctets
            
            	The total number of octets received by this IPsec Phase\-1  IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: ciketunhistinp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges received and  found to be invalid by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunhistinp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges received and  rejected by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunhistinp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges received by  this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunhistinp2sadelrequests
            
            	The total number of IPsec Phase\-2 security association delete requests received by this IPsec  Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: ciketunhistinpkts
            
            	The total number of packets received by this IPsec Phase\-1  IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: ciketunhistlifetime
            
            	The negotiated LifeTime of the IPsec Phase\-1 IKE Tunnel in seconds
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciketunhistlocaladdr
            
            	The IP address of the local endpoint for the IPsec Phase\-1 IKE Tunnel
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: ciketunhistlocalname
            
            	The DNS name of the local IP address for the IPsec Phase\-1 IKE Tunnel. If the DNS  name associated with the local tunnel endpoint  is not known, then the value of this  object will be a NULL string
            	**type**\:  str
            
            .. attribute:: ciketunhistnegomode
            
            	The negotiation mode of the IPsec Phase\-1 IKE Tunnel
            	**type**\:   :py:class:`IkeNegoMode <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeNegoMode>`
            
            .. attribute:: ciketunhistoutdroppkts
            
            	The total number of packets dropped by this IPsec Phase\-1  IKE Tunnel during send processing
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: ciketunhistoutnotifys
            
            	The total number of notifys sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: ciketunhistoutoctets
            
            	The total number of octets sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: ciketunhistoutp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges sent and found to be invalid by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunhistoutp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges sent and rejected by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunhistoutp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunhistoutp2sadelrequests
            
            	The total number of IPsec Phase\-2 security association delete requests sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: ciketunhistoutpkts
            
            	The total number of packets sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: ciketunhistpeerintindex
            
            	The internal index of the local\-remote peer association.  This internal index is used to  uniquely identify multiple associations between  the local and remote peer
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciketunhistpeerlocaltype
            
            	The type of local peer identity.  The local peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\:   :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: ciketunhistpeerlocalvalue
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\:  str
            
            .. attribute:: ciketunhistpeerremotetype
            
            	The type of remote peer identity.  The remote peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\:   :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: ciketunhistpeerremotevalue
            
            	The value of the remote peer identity.  If the remote peer type is an IP Address, then this is the IP Address used to identify the remote peer.  If the remote peer type is a host name, then this is the host name used to identify the remote peer
            	**type**\:  str
            
            .. attribute:: ciketunhistremoteaddr
            
            	The IP address of the remote endpoint for the IPsec Phase\-1 IKE Tunnel
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: ciketunhistremotename
            
            	The DNS name of the remote IP address of IPsec Phase\-1 IKE Tunnel. If the DNS name associated with the remote tunnel endpoint is not known, then the value of this object will be a NULL string
            	**type**\:  str
            
            .. attribute:: ciketunhiststarttime
            
            	The value of sysUpTime in hundredths of seconds when the IPsec Phase\-1 IKE tunnel was started
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhisttermreason
            
            	The reason the IPsec Phase\-1 IKE Tunnel was terminated. Possible reasons include\: 1 = other 2 = normal termination 3 = operator request 4 = peer delete request was received 5 = contact with peer was lost 6 = local failure occurred. 7 = operator initiated check point request
            	**type**\:   :py:class:`Ciketunhisttermreason <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable.Ciketunnelhistentry.Ciketunhisttermreason>`
            
            .. attribute:: ciketunhisttotalrefreshes
            
            	The total number of security associations refreshes performed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: QM Exchanges
            
            .. attribute:: ciketunhisttotalsas
            
            	The total number of security associations used during the  life of the IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SAs
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable.Ciketunnelhistentry, self).__init__()

                self.yang_name = "cikeTunnelHistEntry"
                self.yang_parent_name = "cikeTunnelHistTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ciketunhistindex = YLeaf(YType.int32, "cikeTunHistIndex")

                self.ciketunhistactiveindex = YLeaf(YType.int32, "cikeTunHistActiveIndex")

                self.ciketunhistactivetime = YLeaf(YType.int32, "cikeTunHistActiveTime")

                self.ciketunhistauthmethod = YLeaf(YType.enumeration, "cikeTunHistAuthMethod")

                self.ciketunhistdiffhellmangrp = YLeaf(YType.enumeration, "cikeTunHistDiffHellmanGrp")

                self.ciketunhistencryptalgo = YLeaf(YType.enumeration, "cikeTunHistEncryptAlgo")

                self.ciketunhisthashalgo = YLeaf(YType.enumeration, "cikeTunHistHashAlgo")

                self.ciketunhistindroppkts = YLeaf(YType.uint32, "cikeTunHistInDropPkts")

                self.ciketunhistinnotifys = YLeaf(YType.uint32, "cikeTunHistInNotifys")

                self.ciketunhistinoctets = YLeaf(YType.uint32, "cikeTunHistInOctets")

                self.ciketunhistinp2exchginvalids = YLeaf(YType.uint32, "cikeTunHistInP2ExchgInvalids")

                self.ciketunhistinp2exchgrejects = YLeaf(YType.uint32, "cikeTunHistInP2ExchgRejects")

                self.ciketunhistinp2exchgs = YLeaf(YType.uint32, "cikeTunHistInP2Exchgs")

                self.ciketunhistinp2sadelrequests = YLeaf(YType.uint32, "cikeTunHistInP2SaDelRequests")

                self.ciketunhistinpkts = YLeaf(YType.uint32, "cikeTunHistInPkts")

                self.ciketunhistlifetime = YLeaf(YType.int32, "cikeTunHistLifeTime")

                self.ciketunhistlocaladdr = YLeaf(YType.str, "cikeTunHistLocalAddr")

                self.ciketunhistlocalname = YLeaf(YType.str, "cikeTunHistLocalName")

                self.ciketunhistnegomode = YLeaf(YType.enumeration, "cikeTunHistNegoMode")

                self.ciketunhistoutdroppkts = YLeaf(YType.uint32, "cikeTunHistOutDropPkts")

                self.ciketunhistoutnotifys = YLeaf(YType.uint32, "cikeTunHistOutNotifys")

                self.ciketunhistoutoctets = YLeaf(YType.uint32, "cikeTunHistOutOctets")

                self.ciketunhistoutp2exchginvalids = YLeaf(YType.uint32, "cikeTunHistOutP2ExchgInvalids")

                self.ciketunhistoutp2exchgrejects = YLeaf(YType.uint32, "cikeTunHistOutP2ExchgRejects")

                self.ciketunhistoutp2exchgs = YLeaf(YType.uint32, "cikeTunHistOutP2Exchgs")

                self.ciketunhistoutp2sadelrequests = YLeaf(YType.uint32, "cikeTunHistOutP2SaDelRequests")

                self.ciketunhistoutpkts = YLeaf(YType.uint32, "cikeTunHistOutPkts")

                self.ciketunhistpeerintindex = YLeaf(YType.int32, "cikeTunHistPeerIntIndex")

                self.ciketunhistpeerlocaltype = YLeaf(YType.enumeration, "cikeTunHistPeerLocalType")

                self.ciketunhistpeerlocalvalue = YLeaf(YType.str, "cikeTunHistPeerLocalValue")

                self.ciketunhistpeerremotetype = YLeaf(YType.enumeration, "cikeTunHistPeerRemoteType")

                self.ciketunhistpeerremotevalue = YLeaf(YType.str, "cikeTunHistPeerRemoteValue")

                self.ciketunhistremoteaddr = YLeaf(YType.str, "cikeTunHistRemoteAddr")

                self.ciketunhistremotename = YLeaf(YType.str, "cikeTunHistRemoteName")

                self.ciketunhiststarttime = YLeaf(YType.uint32, "cikeTunHistStartTime")

                self.ciketunhisttermreason = YLeaf(YType.enumeration, "cikeTunHistTermReason")

                self.ciketunhisttotalrefreshes = YLeaf(YType.uint32, "cikeTunHistTotalRefreshes")

                self.ciketunhisttotalsas = YLeaf(YType.uint32, "cikeTunHistTotalSas")
                self._segment_path = lambda: "cikeTunnelHistEntry" + "[cikeTunHistIndex='" + self.ciketunhistindex.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikeTunnelHistTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable.Ciketunnelhistentry, ['ciketunhistindex', 'ciketunhistactiveindex', 'ciketunhistactivetime', 'ciketunhistauthmethod', 'ciketunhistdiffhellmangrp', 'ciketunhistencryptalgo', 'ciketunhisthashalgo', 'ciketunhistindroppkts', 'ciketunhistinnotifys', 'ciketunhistinoctets', 'ciketunhistinp2exchginvalids', 'ciketunhistinp2exchgrejects', 'ciketunhistinp2exchgs', 'ciketunhistinp2sadelrequests', 'ciketunhistinpkts', 'ciketunhistlifetime', 'ciketunhistlocaladdr', 'ciketunhistlocalname', 'ciketunhistnegomode', 'ciketunhistoutdroppkts', 'ciketunhistoutnotifys', 'ciketunhistoutoctets', 'ciketunhistoutp2exchginvalids', 'ciketunhistoutp2exchgrejects', 'ciketunhistoutp2exchgs', 'ciketunhistoutp2sadelrequests', 'ciketunhistoutpkts', 'ciketunhistpeerintindex', 'ciketunhistpeerlocaltype', 'ciketunhistpeerlocalvalue', 'ciketunhistpeerremotetype', 'ciketunhistpeerremotevalue', 'ciketunhistremoteaddr', 'ciketunhistremotename', 'ciketunhiststarttime', 'ciketunhisttermreason', 'ciketunhisttotalrefreshes', 'ciketunhisttotalsas'], name, value)

            class Ciketunhisttermreason(Enum):
                """
                Ciketunhisttermreason

                The reason the IPsec Phase\-1 IKE Tunnel was terminated.

                Possible reasons include\:

                1 = other

                2 = normal termination

                3 = operator request

                4 = peer delete request was received

                5 = contact with peer was lost

                6 = local failure occurred.

                7 = operator initiated check point request

                .. data:: other = 1

                .. data:: normal = 2

                .. data:: operRequest = 3

                .. data:: peerDelRequest = 4

                .. data:: peerLost = 5

                .. data:: localFailure = 6

                .. data:: checkPointReg = 7

                """

                other = Enum.YLeaf(1, "other")

                normal = Enum.YLeaf(2, "normal")

                operRequest = Enum.YLeaf(3, "operRequest")

                peerDelRequest = Enum.YLeaf(4, "peerDelRequest")

                peerLost = Enum.YLeaf(5, "peerLost")

                localFailure = Enum.YLeaf(6, "localFailure")

                checkPointReg = Enum.YLeaf(7, "checkPointReg")



    class Ciketunneltable(Entity):
        """
        The IPsec Phase\-1 Internet Key Exchange Tunnel Table.
        There is one entry in this table for each active IPsec
        Phase\-1 IKE Tunnel.
        
        .. attribute:: ciketunnelentry
        
        	Each entry contains the attributes associated with an active IPsec Phase\-1 IKE Tunnel
        	**type**\: list of    :py:class:`Ciketunnelentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Ciketunneltable.Ciketunnelentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Ciketunneltable, self).__init__()

            self.yang_name = "cikeTunnelTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cikeTunnelEntry" : ("ciketunnelentry", CISCOIPSECFLOWMONITORMIB.Ciketunneltable.Ciketunnelentry)}

            self.ciketunnelentry = YList(self)
            self._segment_path = lambda: "cikeTunnelTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Ciketunneltable, [], name, value)


        class Ciketunnelentry(Entity):
            """
            Each entry contains the attributes associated with
            an active IPsec Phase\-1 IKE Tunnel.
            
            .. attribute:: ciketunindex  <key>
            
            	The index of the IPsec Phase\-1 IKE Tunnel Table. The value of the index is a number which begins  at one and is incremented with each tunnel that  is created. The value of this object will  wrap at 2,147,483,647
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciketunactivetime
            
            	The length of time the IPsec Phase\-1 IKE tunnel has been active in hundredths of seconds
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciketunauthmethod
            
            	The authentication method used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`IkeAuthMethod <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeAuthMethod>`
            
            .. attribute:: ciketundiffhellmangrp
            
            	The Diffie Hellman Group used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`DiffHellmanGrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp>`
            
            .. attribute:: ciketunencryptalgo
            
            	The encryption algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`EncryptAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo>`
            
            .. attribute:: ciketunhashalgo
            
            	The hash algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`IkeHashAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeHashAlgo>`
            
            .. attribute:: ciketunindroppkts
            
            	The total number of packets dropped by this IPsec Phase\-1 IKE Tunnel during  receive processing
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: ciketuninnotifys
            
            	The total number of notifys received by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: ciketuninoctets
            
            	The total number of octets received by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: ciketuninp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges received and found to be invalid  by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketuninp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges received and rejected by this IPsec Phase\-1  Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketuninp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges received by  this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketuninp2sadelrequests
            
            	The total number of IPsec Phase\-2 security association delete requests received  by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: ciketuninpkts
            
            	The total number of packets received by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: ciketunlifetime
            
            	The negotiated LifeTime of the IPsec Phase\-1 IKE Tunnel in seconds
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ciketunlocaladdr
            
            	The IP address of the local endpoint for the IPsec Phase\-1 IKE Tunnel
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: ciketunlocalname
            
            	The DNS name of the local IP address for the IPsec Phase\-1 IKE Tunnel. If the DNS  name associated with the local tunnel endpoint  is not known, then the value of this  object will be a NULL string
            	**type**\:  str
            
            .. attribute:: ciketunlocaltype
            
            	The type of local peer identity.  The local peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\:   :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: ciketunlocalvalue
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\:  str
            
            .. attribute:: ciketunnegomode
            
            	The negotiation mode of the IPsec Phase\-1 IKE Tunnel
            	**type**\:   :py:class:`IkeNegoMode <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeNegoMode>`
            
            .. attribute:: ciketunoutdroppkts
            
            	The total number of packets dropped by this IPsec Phase\-1 IKE Tunnel during send processing
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: ciketunoutnotifys
            
            	The total number of notifys sent by this IPsec Phase\-1 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: ciketunoutoctets
            
            	The total number of octets sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: ciketunoutp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges sent and found to be invalid by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunoutp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges sent and rejected by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunoutp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunoutp2sadelrequests
            
            	The total number of IPsec Phase\-2 security association delete requests sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: ciketunoutpkts
            
            	The total number of packets sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: ciketunremoteaddr
            
            	The IP address of the remote endpoint for the IPsec Phase\-1 IKE Tunnel
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: ciketunremotename
            
            	The DNS name of the remote IP address of IPsec Phase\-1 IKE Tunnel. If the DNS name associated with the remote tunnel endpoint is not known, then the value of this object will be a NULL string
            	**type**\:  str
            
            .. attribute:: ciketunremotetype
            
            	The type of remote peer identity. The remote peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\:   :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: ciketunremotevalue
            
            	The value of the remote peer identity.  If the remote peer type is an IP Address, then this is the IP Address used to identify the remote peer.  If the remote peer type is a host name, then  this is the host name used to identify the  remote peer
            	**type**\:  str
            
            .. attribute:: ciketunsarefreshthreshold
            
            	The security association refresh threshold in seconds
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ciketunstatus
            
            	The status of the MIB table row.  This object can be used to bring the tunnel down  by setting value of this object to destroy(2).  This object cannot be used to create  a MIB table row
            	**type**\:   :py:class:`TunnelStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TunnelStatus>`
            
            .. attribute:: ciketuntotalrefreshes
            
            	The total number of security associations refreshes performed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: QM Exchanges
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Ciketunneltable.Ciketunnelentry, self).__init__()

                self.yang_name = "cikeTunnelEntry"
                self.yang_parent_name = "cikeTunnelTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ciketunindex = YLeaf(YType.int32, "cikeTunIndex")

                self.ciketunactivetime = YLeaf(YType.int32, "cikeTunActiveTime")

                self.ciketunauthmethod = YLeaf(YType.enumeration, "cikeTunAuthMethod")

                self.ciketundiffhellmangrp = YLeaf(YType.enumeration, "cikeTunDiffHellmanGrp")

                self.ciketunencryptalgo = YLeaf(YType.enumeration, "cikeTunEncryptAlgo")

                self.ciketunhashalgo = YLeaf(YType.enumeration, "cikeTunHashAlgo")

                self.ciketunindroppkts = YLeaf(YType.uint32, "cikeTunInDropPkts")

                self.ciketuninnotifys = YLeaf(YType.uint32, "cikeTunInNotifys")

                self.ciketuninoctets = YLeaf(YType.uint32, "cikeTunInOctets")

                self.ciketuninp2exchginvalids = YLeaf(YType.uint32, "cikeTunInP2ExchgInvalids")

                self.ciketuninp2exchgrejects = YLeaf(YType.uint32, "cikeTunInP2ExchgRejects")

                self.ciketuninp2exchgs = YLeaf(YType.uint32, "cikeTunInP2Exchgs")

                self.ciketuninp2sadelrequests = YLeaf(YType.uint32, "cikeTunInP2SaDelRequests")

                self.ciketuninpkts = YLeaf(YType.uint32, "cikeTunInPkts")

                self.ciketunlifetime = YLeaf(YType.int32, "cikeTunLifeTime")

                self.ciketunlocaladdr = YLeaf(YType.str, "cikeTunLocalAddr")

                self.ciketunlocalname = YLeaf(YType.str, "cikeTunLocalName")

                self.ciketunlocaltype = YLeaf(YType.enumeration, "cikeTunLocalType")

                self.ciketunlocalvalue = YLeaf(YType.str, "cikeTunLocalValue")

                self.ciketunnegomode = YLeaf(YType.enumeration, "cikeTunNegoMode")

                self.ciketunoutdroppkts = YLeaf(YType.uint32, "cikeTunOutDropPkts")

                self.ciketunoutnotifys = YLeaf(YType.uint32, "cikeTunOutNotifys")

                self.ciketunoutoctets = YLeaf(YType.uint32, "cikeTunOutOctets")

                self.ciketunoutp2exchginvalids = YLeaf(YType.uint32, "cikeTunOutP2ExchgInvalids")

                self.ciketunoutp2exchgrejects = YLeaf(YType.uint32, "cikeTunOutP2ExchgRejects")

                self.ciketunoutp2exchgs = YLeaf(YType.uint32, "cikeTunOutP2Exchgs")

                self.ciketunoutp2sadelrequests = YLeaf(YType.uint32, "cikeTunOutP2SaDelRequests")

                self.ciketunoutpkts = YLeaf(YType.uint32, "cikeTunOutPkts")

                self.ciketunremoteaddr = YLeaf(YType.str, "cikeTunRemoteAddr")

                self.ciketunremotename = YLeaf(YType.str, "cikeTunRemoteName")

                self.ciketunremotetype = YLeaf(YType.enumeration, "cikeTunRemoteType")

                self.ciketunremotevalue = YLeaf(YType.str, "cikeTunRemoteValue")

                self.ciketunsarefreshthreshold = YLeaf(YType.int32, "cikeTunSaRefreshThreshold")

                self.ciketunstatus = YLeaf(YType.enumeration, "cikeTunStatus")

                self.ciketuntotalrefreshes = YLeaf(YType.uint32, "cikeTunTotalRefreshes")
                self._segment_path = lambda: "cikeTunnelEntry" + "[cikeTunIndex='" + self.ciketunindex.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikeTunnelTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Ciketunneltable.Ciketunnelentry, ['ciketunindex', 'ciketunactivetime', 'ciketunauthmethod', 'ciketundiffhellmangrp', 'ciketunencryptalgo', 'ciketunhashalgo', 'ciketunindroppkts', 'ciketuninnotifys', 'ciketuninoctets', 'ciketuninp2exchginvalids', 'ciketuninp2exchgrejects', 'ciketuninp2exchgs', 'ciketuninp2sadelrequests', 'ciketuninpkts', 'ciketunlifetime', 'ciketunlocaladdr', 'ciketunlocalname', 'ciketunlocaltype', 'ciketunlocalvalue', 'ciketunnegomode', 'ciketunoutdroppkts', 'ciketunoutnotifys', 'ciketunoutoctets', 'ciketunoutp2exchginvalids', 'ciketunoutp2exchgrejects', 'ciketunoutp2exchgs', 'ciketunoutp2sadelrequests', 'ciketunoutpkts', 'ciketunremoteaddr', 'ciketunremotename', 'ciketunremotetype', 'ciketunremotevalue', 'ciketunsarefreshthreshold', 'ciketunstatus', 'ciketuntotalrefreshes'], name, value)


    class Cipsecendpthisttable(Entity):
        """
        The IPsec Phase\-2 Tunnel Endpoint History Table.
        This table is implemented as a 
        sliding window in which only the
        last n entries are maintained.  
        The maximum number of entries
        is specified by the cipSecHistTableSize object.
        
        .. attribute:: cipsecendpthistentry
        
        	Each entry contains the attributes associated with a previously active IPsec Phase\-2 Tunnel Endpoint
        	**type**\: list of    :py:class:`Cipsecendpthistentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable.Cipsecendpthistentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable, self).__init__()

            self.yang_name = "cipSecEndPtHistTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cipSecEndPtHistEntry" : ("cipsecendpthistentry", CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable.Cipsecendpthistentry)}

            self.cipsecendpthistentry = YList(self)
            self._segment_path = lambda: "cipSecEndPtHistTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable, [], name, value)


        class Cipsecendpthistentry(Entity):
            """
            Each entry contains the attributes associated with
            a previously active IPsec Phase\-2 Tunnel Endpoint.
            
            .. attribute:: cipsecendpthistindex  <key>
            
            	The number of the previously active Endpoint associated  with a IPsec Phase\-2 Tunnel Table.  The value   of this index is a number which begins at   one and is incremented with each Endpoint   associated with an IPsec Phase\-2 Tunnel.  The value of this object will wrap at 2,147,483,647
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecendpthistactiveindex
            
            	The index  of the previously active Endpoint
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecendpthistlocaladdr1
            
            	The local Endpoint's first IP address specification.  If the local Endpoint type is single IP address,  then this is the value of the IP address.  If the local Endpoint type is IP subnet, then this is the value of the subnet.  If the local Endpoint type is IP address range,  then this is the value of beginning IP address of  the range
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecendpthistlocaladdr2
            
            	The local Endpoint's second IP address specification.  If the local Endpoint type is single IP address,  then this is the value of the IP address.  If the local Endpoint type is IP subnet, then this is the value of the subnet mask.  If the local Endpoint type is IP address range,  then this is the value of ending IP address of the range
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecendpthistlocalname
            
            	The DNS name of the local Endpoint
            	**type**\:  str
            
            .. attribute:: cipsecendpthistlocalport
            
            	The port number of the local Endpoint's traffic
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cipsecendpthistlocalprotocol
            
            	The protocol number of the local Endpoint's traffic
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cipsecendpthistlocaltype
            
            	The type of identity for the local Endpoint. Possible values are\: 1) a single IP address, or 2) an IP address range, or 3) an IP subnet
            	**type**\:   :py:class:`EndPtType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EndPtType>`
            
            .. attribute:: cipsecendpthistremoteaddr1
            
            	The remote Endpoint's first IP address specification.  If the remote Endpoint type is single IP address,  then this is the value of the IP address.  If the remote Endpoint type is IP subnet, then this is the value of the subnet.  If the remote Endpoint type is IP address range,  then this is the value of beginning IP address of the range
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecendpthistremoteaddr2
            
            	The remote Endpoint's second IP address specification.  If the remote Endpoint type is single IP address,  then this is the value of the IP address.  If the remote Endpoint type is IP subnet, then this is the value of the subnet mask.  If the remote Endpoint type is IP address range,  then this is the value of ending IP address of the range
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecendpthistremotename
            
            	The DNS name of the remote Endpoint
            	**type**\:  str
            
            .. attribute:: cipsecendpthistremoteport
            
            	The port number of the remote Endpoint's traffic
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cipsecendpthistremoteprotocol
            
            	The protocol number of the remote Endpoint's traffic
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cipsecendpthistremotetype
            
            	The type of identity for the remote Endpoint. Possible values are\: 1) a single IP address, or 2) an IP address range, or 3) an IP subnet
            	**type**\:   :py:class:`EndPtType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EndPtType>`
            
            .. attribute:: cipsecendpthisttunindex
            
            	The index  of the previously active IPsec Phase\-2 Tunnel Table
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable.Cipsecendpthistentry, self).__init__()

                self.yang_name = "cipSecEndPtHistEntry"
                self.yang_parent_name = "cipSecEndPtHistTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cipsecendpthistindex = YLeaf(YType.int32, "cipSecEndPtHistIndex")

                self.cipsecendpthistactiveindex = YLeaf(YType.int32, "cipSecEndPtHistActiveIndex")

                self.cipsecendpthistlocaladdr1 = YLeaf(YType.str, "cipSecEndPtHistLocalAddr1")

                self.cipsecendpthistlocaladdr2 = YLeaf(YType.str, "cipSecEndPtHistLocalAddr2")

                self.cipsecendpthistlocalname = YLeaf(YType.str, "cipSecEndPtHistLocalName")

                self.cipsecendpthistlocalport = YLeaf(YType.int32, "cipSecEndPtHistLocalPort")

                self.cipsecendpthistlocalprotocol = YLeaf(YType.int32, "cipSecEndPtHistLocalProtocol")

                self.cipsecendpthistlocaltype = YLeaf(YType.enumeration, "cipSecEndPtHistLocalType")

                self.cipsecendpthistremoteaddr1 = YLeaf(YType.str, "cipSecEndPtHistRemoteAddr1")

                self.cipsecendpthistremoteaddr2 = YLeaf(YType.str, "cipSecEndPtHistRemoteAddr2")

                self.cipsecendpthistremotename = YLeaf(YType.str, "cipSecEndPtHistRemoteName")

                self.cipsecendpthistremoteport = YLeaf(YType.int32, "cipSecEndPtHistRemotePort")

                self.cipsecendpthistremoteprotocol = YLeaf(YType.int32, "cipSecEndPtHistRemoteProtocol")

                self.cipsecendpthistremotetype = YLeaf(YType.enumeration, "cipSecEndPtHistRemoteType")

                self.cipsecendpthisttunindex = YLeaf(YType.int32, "cipSecEndPtHistTunIndex")
                self._segment_path = lambda: "cipSecEndPtHistEntry" + "[cipSecEndPtHistIndex='" + self.cipsecendpthistindex.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecEndPtHistTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable.Cipsecendpthistentry, ['cipsecendpthistindex', 'cipsecendpthistactiveindex', 'cipsecendpthistlocaladdr1', 'cipsecendpthistlocaladdr2', 'cipsecendpthistlocalname', 'cipsecendpthistlocalport', 'cipsecendpthistlocalprotocol', 'cipsecendpthistlocaltype', 'cipsecendpthistremoteaddr1', 'cipsecendpthistremoteaddr2', 'cipsecendpthistremotename', 'cipsecendpthistremoteport', 'cipsecendpthistremoteprotocol', 'cipsecendpthistremotetype', 'cipsecendpthisttunindex'], name, value)


    class Cipsecendpttable(Entity):
        """
        The IPsec Phase\-2 Tunnel Endpoint Table.
        This table contains an entry for each 
        active endpoint associated with an IPsec
         Phase\-2 Tunnel.
        
        .. attribute:: cipsecendptentry
        
        	An IPsec Phase\-2 Tunnel Endpoint entry
        	**type**\: list of    :py:class:`Cipsecendptentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecendpttable.Cipsecendptentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsecendpttable, self).__init__()

            self.yang_name = "cipSecEndPtTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cipSecEndPtEntry" : ("cipsecendptentry", CISCOIPSECFLOWMONITORMIB.Cipsecendpttable.Cipsecendptentry)}

            self.cipsecendptentry = YList(self)
            self._segment_path = lambda: "cipSecEndPtTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecendpttable, [], name, value)


        class Cipsecendptentry(Entity):
            """
            An IPsec Phase\-2 Tunnel Endpoint entry.
            
            .. attribute:: cipsectunindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cipsectunindex <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsectunneltable.Cipsectunnelentry>`
            
            .. attribute:: cipsecendptindex  <key>
            
            	The number of the Endpoint associated with the IPsec Phase\-2 Tunnel Table.  The value of this index is a number which begins at one and  is incremented with each Endpoint associated  with an IPsec Phase\-2 Tunnel. The value of this object will wrap at 2,147,483,647
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecendptlocaladdr1
            
            	The local Endpoint's first IP address specification.  If the local Endpoint type is single IP address,  then this is the value of the IP address.  If the local Endpoint type is IP subnet, then this is the value of the subnet.  If the local Endpoint type is IP address range,  then this is the value of beginning IP address  of the range
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecendptlocaladdr2
            
            	The local Endpoint's second IP address specification.  If the local Endpoint type is single IP address,  then this is the value of the IP address.  If the local Endpoint type is IP subnet, then this is the value of the subnet mask.  If the local Endpoint type is IP address range,  then this is the value of ending IP address  of the range
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecendptlocalname
            
            	The DNS name of the local Endpoint
            	**type**\:  str
            
            .. attribute:: cipsecendptlocalport
            
            	The port number of the local Endpoint's traffic
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cipsecendptlocalprotocol
            
            	The protocol number of the local Endpoint's traffic
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cipsecendptlocaltype
            
            	The type of identity for the local Endpoint. Possible values are\: 1) a single IP address, or 2) an IP address range, or 3) an IP subnet
            	**type**\:   :py:class:`EndPtType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EndPtType>`
            
            .. attribute:: cipsecendptremoteaddr1
            
            	The remote Endpoint's first IP address specification.  If the remote Endpoint type is single IP address,  then this is the value of the IP address.  If the remote Endpoint type is IP subnet, then this is the value of the subnet.  If the remote Endpoint type is IP address range,  then this is the value of beginning IP address  of the range
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecendptremoteaddr2
            
            	The remote Endpoint's second IP address specification.  If the remote Endpoint type is single IP address,  then this is the value of the IP address.  If the remote Endpoint type is IP subnet, then this is the value of the subnet mask.  If the remote Endpoint type is IP address range,  then this is the value of ending IP address of  the range
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecendptremotename
            
            	The DNS name of the remote Endpoint
            	**type**\:  str
            
            .. attribute:: cipsecendptremoteport
            
            	The port number of the remote Endpoint's traffic
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cipsecendptremoteprotocol
            
            	The protocol number of the remote Endpoint's traffic
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cipsecendptremotetype
            
            	The type of identity for the remote Endpoint. Possible values are\: 1) a single IP address, or 2) an IP address range, or 3) an IP subnet
            	**type**\:   :py:class:`EndPtType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EndPtType>`
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cipsecendpttable.Cipsecendptentry, self).__init__()

                self.yang_name = "cipSecEndPtEntry"
                self.yang_parent_name = "cipSecEndPtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cipsectunindex = YLeaf(YType.str, "cipSecTunIndex")

                self.cipsecendptindex = YLeaf(YType.int32, "cipSecEndPtIndex")

                self.cipsecendptlocaladdr1 = YLeaf(YType.str, "cipSecEndPtLocalAddr1")

                self.cipsecendptlocaladdr2 = YLeaf(YType.str, "cipSecEndPtLocalAddr2")

                self.cipsecendptlocalname = YLeaf(YType.str, "cipSecEndPtLocalName")

                self.cipsecendptlocalport = YLeaf(YType.int32, "cipSecEndPtLocalPort")

                self.cipsecendptlocalprotocol = YLeaf(YType.int32, "cipSecEndPtLocalProtocol")

                self.cipsecendptlocaltype = YLeaf(YType.enumeration, "cipSecEndPtLocalType")

                self.cipsecendptremoteaddr1 = YLeaf(YType.str, "cipSecEndPtRemoteAddr1")

                self.cipsecendptremoteaddr2 = YLeaf(YType.str, "cipSecEndPtRemoteAddr2")

                self.cipsecendptremotename = YLeaf(YType.str, "cipSecEndPtRemoteName")

                self.cipsecendptremoteport = YLeaf(YType.int32, "cipSecEndPtRemotePort")

                self.cipsecendptremoteprotocol = YLeaf(YType.int32, "cipSecEndPtRemoteProtocol")

                self.cipsecendptremotetype = YLeaf(YType.enumeration, "cipSecEndPtRemoteType")
                self._segment_path = lambda: "cipSecEndPtEntry" + "[cipSecTunIndex='" + self.cipsectunindex.get() + "']" + "[cipSecEndPtIndex='" + self.cipsecendptindex.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecEndPtTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecendpttable.Cipsecendptentry, ['cipsectunindex', 'cipsecendptindex', 'cipsecendptlocaladdr1', 'cipsecendptlocaladdr2', 'cipsecendptlocalname', 'cipsecendptlocalport', 'cipsecendptlocalprotocol', 'cipsecendptlocaltype', 'cipsecendptremoteaddr1', 'cipsecendptremoteaddr2', 'cipsecendptremotename', 'cipsecendptremoteport', 'cipsecendptremoteprotocol', 'cipsecendptremotetype'], name, value)


    class Cipsecfailglobalcntl(Entity):
        """
        
        
        .. attribute:: cipsecfailtablesize
        
        	The window size of the IPsec Phase\-1 and Phase\-2 Failure Tables.  The IPsec Phase\-1 and Phase\-2 Failure Tables are implemented as a sliding window in which only the last n entries are maintained.  This object is used specify the number of entries which will be  maintained in the IPsec Phase\-1 and Phase\-2 Failure  Tables.  An implementation may choose suitable minimum and  maximum values for this element based on the local  policy and available resources. If an SNMP SET request  specifies a value outside this window for this element,  a BAD VALUE may be returned
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsecfailglobalcntl, self).__init__()

            self.yang_name = "cipSecFailGlobalCntl"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.cipsecfailtablesize = YLeaf(YType.int32, "cipSecFailTableSize")
            self._segment_path = lambda: "cipSecFailGlobalCntl"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecfailglobalcntl, ['cipsecfailtablesize'], name, value)


    class Cipsecfailtable(Entity):
        """
        The IPsec Phase\-2 Failure Table.
        This table is implemented as a sliding window 
        in which only the last n entries are maintained.  
        The maximum number of entries
        is specified by the cipSecFailTableSize object.
        
        .. attribute:: cipsecfailentry
        
        	Each entry contains the attributes associated with an IPsec Phase\-1 failure
        	**type**\: list of    :py:class:`Cipsecfailentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecfailtable.Cipsecfailentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsecfailtable, self).__init__()

            self.yang_name = "cipSecFailTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cipSecFailEntry" : ("cipsecfailentry", CISCOIPSECFLOWMONITORMIB.Cipsecfailtable.Cipsecfailentry)}

            self.cipsecfailentry = YList(self)
            self._segment_path = lambda: "cipSecFailTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecfailtable, [], name, value)


        class Cipsecfailentry(Entity):
            """
            Each entry contains the attributes associated with
            an IPsec Phase\-1 failure.
            
            .. attribute:: cipsecfailindex  <key>
            
            	The IPsec Phase\-2 Failure Table index. The value of the index is a number which  begins at one and is incremented with each  IPsec Phase\-1 failure. The value of this object will wrap at 2,147,483,647
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecfailpktdstaddr
            
            	The packet's destination IP address
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecfailpktsrcaddr
            
            	The packet's source IP address
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecfailreason
            
            	The reason for the failure.  Possible reasons include\:   1 = other   2 = internal error occurred   3 = peer encoding error   4 = proposal failure   5 = protocol use failure   6 = non\-existent security association   7 = decryption failure   8 = encryption failure   9 = inbound authentication failure  10 = outbound authentication failure  11 = compression failure  12 = system capacity failure  13 = peer delete request was received  14 = contact with peer was lost  15 = sequence number rolled over  16 = operator requested termination
            	**type**\:   :py:class:`Cipsecfailreason <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecfailtable.Cipsecfailentry.Cipsecfailreason>`
            
            .. attribute:: cipsecfailsaspi
            
            	The security association SPI value
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cipsecfailtime
            
            	The value of sysUpTime in hundredths of seconds at the time of the failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecfailtunnelindex
            
            	The Phase\-2 Tunnel index (cipSecTunIndex)
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cipsecfailtable.Cipsecfailentry, self).__init__()

                self.yang_name = "cipSecFailEntry"
                self.yang_parent_name = "cipSecFailTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cipsecfailindex = YLeaf(YType.int32, "cipSecFailIndex")

                self.cipsecfailpktdstaddr = YLeaf(YType.str, "cipSecFailPktDstAddr")

                self.cipsecfailpktsrcaddr = YLeaf(YType.str, "cipSecFailPktSrcAddr")

                self.cipsecfailreason = YLeaf(YType.enumeration, "cipSecFailReason")

                self.cipsecfailsaspi = YLeaf(YType.int32, "cipSecFailSaSpi")

                self.cipsecfailtime = YLeaf(YType.uint32, "cipSecFailTime")

                self.cipsecfailtunnelindex = YLeaf(YType.int32, "cipSecFailTunnelIndex")
                self._segment_path = lambda: "cipSecFailEntry" + "[cipSecFailIndex='" + self.cipsecfailindex.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecFailTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecfailtable.Cipsecfailentry, ['cipsecfailindex', 'cipsecfailpktdstaddr', 'cipsecfailpktsrcaddr', 'cipsecfailreason', 'cipsecfailsaspi', 'cipsecfailtime', 'cipsecfailtunnelindex'], name, value)

            class Cipsecfailreason(Enum):
                """
                Cipsecfailreason

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

                .. data:: other = 1

                .. data:: internalError = 2

                .. data:: peerEncodingError = 3

                .. data:: proposalFailure = 4

                .. data:: protocolUseFail = 5

                .. data:: nonExistentSa = 6

                .. data:: decryptFailure = 7

                .. data:: encryptFailure = 8

                .. data:: inAuthFailure = 9

                .. data:: outAuthFailure = 10

                .. data:: compression = 11

                .. data:: sysCapExceeded = 12

                .. data:: peerDelRequest = 13

                .. data:: peerLost = 14

                .. data:: seqNumRollOver = 15

                .. data:: operRequest = 16

                """

                other = Enum.YLeaf(1, "other")

                internalError = Enum.YLeaf(2, "internalError")

                peerEncodingError = Enum.YLeaf(3, "peerEncodingError")

                proposalFailure = Enum.YLeaf(4, "proposalFailure")

                protocolUseFail = Enum.YLeaf(5, "protocolUseFail")

                nonExistentSa = Enum.YLeaf(6, "nonExistentSa")

                decryptFailure = Enum.YLeaf(7, "decryptFailure")

                encryptFailure = Enum.YLeaf(8, "encryptFailure")

                inAuthFailure = Enum.YLeaf(9, "inAuthFailure")

                outAuthFailure = Enum.YLeaf(10, "outAuthFailure")

                compression = Enum.YLeaf(11, "compression")

                sysCapExceeded = Enum.YLeaf(12, "sysCapExceeded")

                peerDelRequest = Enum.YLeaf(13, "peerDelRequest")

                peerLost = Enum.YLeaf(14, "peerLost")

                seqNumRollOver = Enum.YLeaf(15, "seqNumRollOver")

                operRequest = Enum.YLeaf(16, "operRequest")



    class Cipsecglobalstats(Entity):
        """
        
        
        .. attribute:: cipsecglobalactivetunnels
        
        	The total number of currently active IPsec Phase\-2 Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobalhcindecompoctets
        
        	A high capacity count of the total number of decompressed octets received by all current  and previous IPsec Phase\-2 Tunnels.  This value  is accumulated AFTER the packet is decompressed.  If compression is not being used, this value   will match the value of cipSecGlobalHcInOctets
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: cipsecglobalhcinoctets
        
        	A high capacity count of the total number of octets received by all current and previous IPsec Phase\-2 Tunnels. This value is accumulated BEFORE determining whether or not the packet should be decompressed
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: cipsecglobalhcoutoctets
        
        	A high capacity count of the total number of octets sent by all current and previous  IPsec Phase\-2 Tunnels.  This value is accumulated  AFTER determining whether or not the packet should  be compressed
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: cipsecglobalhcoutuncompoctets
        
        	A high capacity count of the total number of uncompressed octets sent by all current and previous  IPsec Phase\-2 Tunnels.  This value is accumulated  BEFORE the packet is compressed.  If compression is  not being used, this value will match the       value of cipSecGlobalHcOutOctets
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: Octets
        
        .. attribute:: cipsecglobalinauthfails
        
        	The total number of inbound authentication's which ended in failure by all current and previous  IPsec Phase\-2 Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cipsecglobalinauths
        
        	The total number of inbound authentication's performed by all current and previous IPsec  Phase\-2 Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Events
        
        .. attribute:: cipsecglobalindecompoctets
        
        	The total number of decompressed octets received by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated AFTER the packet is  decompressed. If compression is not being used,  this value will match the value of cipSecGlobalInOctets.  See also cipSecGlobalInDecompOctWraps  for the number of times this counter has wrapped
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Octets
        
        .. attribute:: cipsecglobalindecompoctwraps
        
        	The number of times the global decompressed octets received counter  (cipSecGlobalInDecompOctets) has wrapped
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Integral units
        
        .. attribute:: cipsecglobalindecryptfails
        
        	The total number of inbound decryption's which ended in failure by all current and  previous IPsec Phase\-2 Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cipsecglobalindecrypts
        
        	The total number of inbound decryption's performed by all current and previous IPsec  Phase\-2 Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cipsecglobalindrops
        
        	The total number of packets dropped during receive processing by all current and previous  IPsec Phase\-2 Tunnels. This count does NOT include packets dropped due to  Anti\-Replay processing
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cipsecglobalinoctets
        
        	The total number of octets received by all current and previous IPsec Phase\-2 Tunnels.  This value is accumulated BEFORE determining whether or not the packet should be decompressed. See also cipSecGlobalInOctWraps for the number of times this counter has wrapped
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Octets
        
        .. attribute:: cipsecglobalinoctwraps
        
        	The number of times the global octets received counter (cipSecGlobalInOctets) has wrapped
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Integral units
        
        .. attribute:: cipsecglobalinpkts
        
        	The total number of packets received by all current and previous  IPsec Phase\-2 Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cipsecglobalinreplaydrops
        
        	The total number of packets dropped during receive processing due to Anti\-Replay  processing by all current and previous IPsec  Phase\-2 Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cipsecglobalnosafails
        
        	The total number of non\-existent Security Association in failures which occurred  during processing of all current  and previous IPsec Phase\-2 Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cipsecglobaloutauthfails
        
        	The total number of outbound authentication's which ended in failure  by all current and previous IPsec Phase\-2 Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cipsecglobaloutauths
        
        	The total number of outbound authentication's performed by all current and previous IPsec  Phase\-2 Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Events
        
        .. attribute:: cipsecglobaloutdrops
        
        	The total number of packets dropped during send processing by all current and previous IPsec  Phase\-2 Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cipsecglobaloutencryptfails
        
        	The total number of outbound encryption's which ended in failure by all current and  previous IPsec Phase\-2 Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cipsecglobaloutencrypts
        
        	The total number of outbound encryption's performed by all current and previous IPsec Phase\-2 Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cipsecglobaloutoctets
        
        	The total number of octets sent by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated AFTER determining  whether or not the packet should be compressed.   See also cipSecGlobalOutOctWraps for the  number of times this counter has wrapped
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Octets
        
        .. attribute:: cipsecglobaloutoctwraps
        
        	The number of times the global octets sent counter (cipSecGlobalOutOctets) has wrapped
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Integral units
        
        .. attribute:: cipsecglobaloutpkts
        
        	The total number of packets sent by all current and previous  IPsec Phase\-2 Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cipsecglobaloutuncompoctets
        
        	The total number of uncompressed octets sent by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated BEFORE the packet is  compressed. If compression is not being used, this  value will match the value of cipSecGlobalOutOctets.  See also cipSecGlobalOutDecompOctWraps for the number  of times this counter has wrapped
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Octets
        
        .. attribute:: cipsecglobaloutuncompoctwraps
        
        	The number of times the global uncompressed octets sent counter (cipSecGlobalOutUncompOctets)  has wrapped
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Integral units
        
        .. attribute:: cipsecglobalprevioustunnels
        
        	The total number of previously active IPsec Phase\-2 Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Phase-2 Tunnels
        
        .. attribute:: cipsecglobalprotocolusefails
        
        	The total number of protocol use failures which occurred during processing of all current  and previously active IPsec Phase\-2 Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cipsecglobalsyscapfails
        
        	The total number of system capacity failures which occurred during processing of all current  and previously active IPsec Phase\-2 Tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsecglobalstats, self).__init__()

            self.yang_name = "cipSecGlobalStats"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.cipsecglobalactivetunnels = YLeaf(YType.uint32, "cipSecGlobalActiveTunnels")

            self.cipsecglobalhcindecompoctets = YLeaf(YType.uint64, "cipSecGlobalHcInDecompOctets")

            self.cipsecglobalhcinoctets = YLeaf(YType.uint64, "cipSecGlobalHcInOctets")

            self.cipsecglobalhcoutoctets = YLeaf(YType.uint64, "cipSecGlobalHcOutOctets")

            self.cipsecglobalhcoutuncompoctets = YLeaf(YType.uint64, "cipSecGlobalHcOutUncompOctets")

            self.cipsecglobalinauthfails = YLeaf(YType.uint32, "cipSecGlobalInAuthFails")

            self.cipsecglobalinauths = YLeaf(YType.uint32, "cipSecGlobalInAuths")

            self.cipsecglobalindecompoctets = YLeaf(YType.uint32, "cipSecGlobalInDecompOctets")

            self.cipsecglobalindecompoctwraps = YLeaf(YType.uint32, "cipSecGlobalInDecompOctWraps")

            self.cipsecglobalindecryptfails = YLeaf(YType.uint32, "cipSecGlobalInDecryptFails")

            self.cipsecglobalindecrypts = YLeaf(YType.uint32, "cipSecGlobalInDecrypts")

            self.cipsecglobalindrops = YLeaf(YType.uint32, "cipSecGlobalInDrops")

            self.cipsecglobalinoctets = YLeaf(YType.uint32, "cipSecGlobalInOctets")

            self.cipsecglobalinoctwraps = YLeaf(YType.uint32, "cipSecGlobalInOctWraps")

            self.cipsecglobalinpkts = YLeaf(YType.uint32, "cipSecGlobalInPkts")

            self.cipsecglobalinreplaydrops = YLeaf(YType.uint32, "cipSecGlobalInReplayDrops")

            self.cipsecglobalnosafails = YLeaf(YType.uint32, "cipSecGlobalNoSaFails")

            self.cipsecglobaloutauthfails = YLeaf(YType.uint32, "cipSecGlobalOutAuthFails")

            self.cipsecglobaloutauths = YLeaf(YType.uint32, "cipSecGlobalOutAuths")

            self.cipsecglobaloutdrops = YLeaf(YType.uint32, "cipSecGlobalOutDrops")

            self.cipsecglobaloutencryptfails = YLeaf(YType.uint32, "cipSecGlobalOutEncryptFails")

            self.cipsecglobaloutencrypts = YLeaf(YType.uint32, "cipSecGlobalOutEncrypts")

            self.cipsecglobaloutoctets = YLeaf(YType.uint32, "cipSecGlobalOutOctets")

            self.cipsecglobaloutoctwraps = YLeaf(YType.uint32, "cipSecGlobalOutOctWraps")

            self.cipsecglobaloutpkts = YLeaf(YType.uint32, "cipSecGlobalOutPkts")

            self.cipsecglobaloutuncompoctets = YLeaf(YType.uint32, "cipSecGlobalOutUncompOctets")

            self.cipsecglobaloutuncompoctwraps = YLeaf(YType.uint32, "cipSecGlobalOutUncompOctWraps")

            self.cipsecglobalprevioustunnels = YLeaf(YType.uint32, "cipSecGlobalPreviousTunnels")

            self.cipsecglobalprotocolusefails = YLeaf(YType.uint32, "cipSecGlobalProtocolUseFails")

            self.cipsecglobalsyscapfails = YLeaf(YType.uint32, "cipSecGlobalSysCapFails")
            self._segment_path = lambda: "cipSecGlobalStats"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecglobalstats, ['cipsecglobalactivetunnels', 'cipsecglobalhcindecompoctets', 'cipsecglobalhcinoctets', 'cipsecglobalhcoutoctets', 'cipsecglobalhcoutuncompoctets', 'cipsecglobalinauthfails', 'cipsecglobalinauths', 'cipsecglobalindecompoctets', 'cipsecglobalindecompoctwraps', 'cipsecglobalindecryptfails', 'cipsecglobalindecrypts', 'cipsecglobalindrops', 'cipsecglobalinoctets', 'cipsecglobalinoctwraps', 'cipsecglobalinpkts', 'cipsecglobalinreplaydrops', 'cipsecglobalnosafails', 'cipsecglobaloutauthfails', 'cipsecglobaloutauths', 'cipsecglobaloutdrops', 'cipsecglobaloutencryptfails', 'cipsecglobaloutencrypts', 'cipsecglobaloutoctets', 'cipsecglobaloutoctwraps', 'cipsecglobaloutpkts', 'cipsecglobaloutuncompoctets', 'cipsecglobaloutuncompoctwraps', 'cipsecglobalprevioustunnels', 'cipsecglobalprotocolusefails', 'cipsecglobalsyscapfails'], name, value)


    class Cipsechistglobalcntl(Entity):
        """
        
        
        .. attribute:: cipsechistcheckpoint
        
        	The current state of check point processing.  This object will return ready when the agent is  ready to create on\-demand history entries for  active IPsec Tunnels or checkPoint when the  agent is currently creating on\-demand history  entries for active IPsec Tunnels.  By setting this value to checkPoint, the agent  will create\: a) an entry in the IPsec Phase\-1 Tunnel History     for each active IPsec Phase\-1 Tunnel and b) an entry in the IPsec Phase\-2 Tunnel History     Table and an entry in the IPsec Phase\-2     Tunnel EndPoint History Table    for each active IPsec Phase\-2 Tunnel
        	**type**\:   :py:class:`Cipsechistcheckpoint <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsechistglobalcntl.Cipsechistcheckpoint>`
        
        .. attribute:: cipsechisttablesize
        
        	The window size of the IPsec Phase\-1 and Phase\-2 History Tables.  The IPsec Phase\-1 and Phase\-2 History Tables are implemented as a sliding window in which only the last n entries are maintained.  This object is used specify the number of entries which will be  maintained in the IPsec Phase\-1 and  Phase\-2 History Tables.  An implementation may choose suitable minimum and  maximum values for this element based on the local  policy and available resources. If an SNMP SET request  specifies a value outside this window for this element,  a BAD VALUE may be returned
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsechistglobalcntl, self).__init__()

            self.yang_name = "cipSecHistGlobalCntl"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.cipsechistcheckpoint = YLeaf(YType.enumeration, "cipSecHistCheckPoint")

            self.cipsechisttablesize = YLeaf(YType.int32, "cipSecHistTableSize")
            self._segment_path = lambda: "cipSecHistGlobalCntl"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsechistglobalcntl, ['cipsechistcheckpoint', 'cipsechisttablesize'], name, value)

        class Cipsechistcheckpoint(Enum):
            """
            Cipsechistcheckpoint

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

            .. data:: ready = 1

            .. data:: checkPoint = 2

            """

            ready = Enum.YLeaf(1, "ready")

            checkPoint = Enum.YLeaf(2, "checkPoint")



    class Cipseclevels(Entity):
        """
        
        
        .. attribute:: cipsecmiblevel
        
        	The level of the IPsec MIB
        	**type**\:  int
        
        	**range:** 1..4096
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipseclevels, self).__init__()

            self.yang_name = "cipSecLevels"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.cipsecmiblevel = YLeaf(YType.int32, "cipSecMibLevel")
            self._segment_path = lambda: "cipSecLevels"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipseclevels, ['cipsecmiblevel'], name, value)


    class Cipsecphase2Gwstatstable(Entity):
        """
        Phase\-2 IPsec stats information is included in this table.
        Each entry is related to a specific gateway which is 
        identified by 'cmgwIndex'
        
        .. attribute:: cipsecphase2gwstatsentry
        
        	Each entry contains the attributes of an Phase\-2 IPsec stats information for the related gateway.  There is only one entry for each gateway. The entry  is created when a gateway up and cannot be deleted
        	**type**\: list of    :py:class:`Cipsecphase2Gwstatsentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecphase2Gwstatstable.Cipsecphase2Gwstatsentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsecphase2Gwstatstable, self).__init__()

            self.yang_name = "cipSecPhase2GWStatsTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cipSecPhase2GWStatsEntry" : ("cipsecphase2gwstatsentry", CISCOIPSECFLOWMONITORMIB.Cipsecphase2Gwstatstable.Cipsecphase2Gwstatsentry)}

            self.cipsecphase2gwstatsentry = YList(self)
            self._segment_path = lambda: "cipSecPhase2GWStatsTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecphase2Gwstatstable, [], name, value)


        class Cipsecphase2Gwstatsentry(Entity):
            """
            Each entry contains the attributes of an Phase\-2 IPsec stats
            information for the related gateway.
            
            There is only one entry for each gateway. The entry 
            is created when a gateway up and cannot be deleted.
            
            .. attribute:: cmgwindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cipsecphase2gwactivetunnels
            
            	The total number of currently active IPsec Phase\-2 Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwinauthfails
            
            	The total number of inbound authentication's which ended in failure by all current and previous  IPsec Phase\-2 Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsecphase2gwinauths
            
            	The total number of inbound authentication's performed by all current and previous IPsec  Phase\-2 Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Events
            
            .. attribute:: cipsecphase2gwindecompoctets
            
            	The total number of decompressed octets received by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated AFTER the packet is  decompressed. If compression is not being used,  this value will match the value of cipSecGlobalInOctets.  See also cipSecGlobalInDecompOctWraps for the number of times this counter has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsecphase2gwindecompoctwraps
            
            	The number of times the global decompressed octets received counter (cipSecGlobalInDecompOctets)  has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsecphase2gwindecryptfails
            
            	The total number of inbound decryption's which ended in failure by all current and  previous IPsec Phase\-2 Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsecphase2gwindecrypts
            
            	The total number of inbound decryption's performed by all current and previous IPsec  Phase\-2 Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsecphase2gwindrops
            
            	The total number of packets dropped during receive processing by all current and previous  IPsec Phase\-2 Tunnels. This count does NOT include  packets dropped due to Anti\-Replay processing
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsecphase2gwinoctets
            
            	The total number of octets received by all current and previous IPsec Phase\-2 Tunnels.  This value is accumulated BEFORE determining  whether or not the packet should be decompressed.  See also cipSecGlobalInOctWraps for the number of times this counter has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsecphase2gwinoctwraps
            
            	The number of times the global octets received counter (cipSecGlobalInOctets) has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsecphase2gwinpkts
            
            	The total number of packets received by all current and previous IPsec Phase\-2 Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsecphase2gwinreplaydrops
            
            	The total number of packets dropped during receive processing due to Anti\-Replay  processing by all current and previous IPsec Phase\-2 Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsecphase2gwnosafails
            
            	The total number of non\-existent Security Association in failures which occurred  during processing of all current and previous IPsec Phase\-2 Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsecphase2gwoutauthfails
            
            	The total number of outbound authentication's which ended in failure by all current and previous IPsec Phase\-2 Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsecphase2gwoutauths
            
            	The total number of outbound authentication's performed by all current and previous IPsec  Phase\-2 Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Events
            
            .. attribute:: cipsecphase2gwoutdrops
            
            	The total number of packets dropped during send processing by all current and previous IPsec  Phase\-2 Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsecphase2gwoutencryptfails
            
            	The total number of outbound encryption's which ended in failure by all current and  previous IPsec Phase\-2 Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsecphase2gwoutencrypts
            
            	The total number of outbound encryption's performed by all current and previous IPsec Phase\-2 Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsecphase2gwoutoctets
            
            	The total number of octets sent by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated AFTER determining  whether or not the packet should be compressed.   See also cipSecGlobalOutOctWraps for the number of times this counter has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsecphase2gwoutoctwraps
            
            	The number of times the global octets sent counter (cipSecGlobalOutOctets) has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsecphase2gwoutpkts
            
            	The total number of packets sent by all current and previous IPsec Phase\-2  Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsecphase2gwoutuncompoctets
            
            	The total number of uncompressed octets sent by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated BEFORE the packet is  compressed. If compression is not being used, this  value will match the value of cipSecGlobalOutOctets.  See also cipSecGlobalOutDecompOctWraps for the number  of times this counter has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsecphase2gwoutuncompoctwraps
            
            	The number of times the global uncompressed octets sent counter (cipSecGlobalOutUncompOctets)  has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsecphase2gwprevioustunnels
            
            	The total number of previously active IPsec Phase\-2 Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Phase-2 Tunnels
            
            .. attribute:: cipsecphase2gwprotocolusefails
            
            	The total number of protocol use failures which occurred during processing of all current  and previously active IPsec Phase\-2 Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsecphase2gwsyscapfails
            
            	The total number of system capacity failures which occurred during processing of all current  and previously active IPsec Phase\-2 Tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cipsecphase2Gwstatstable.Cipsecphase2Gwstatsentry, self).__init__()

                self.yang_name = "cipSecPhase2GWStatsEntry"
                self.yang_parent_name = "cipSecPhase2GWStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cmgwindex = YLeaf(YType.str, "cmgwIndex")

                self.cipsecphase2gwactivetunnels = YLeaf(YType.uint32, "cipSecPhase2GWActiveTunnels")

                self.cipsecphase2gwinauthfails = YLeaf(YType.uint32, "cipSecPhase2GWInAuthFails")

                self.cipsecphase2gwinauths = YLeaf(YType.uint32, "cipSecPhase2GWInAuths")

                self.cipsecphase2gwindecompoctets = YLeaf(YType.uint32, "cipSecPhase2GWInDecompOctets")

                self.cipsecphase2gwindecompoctwraps = YLeaf(YType.uint32, "cipSecPhase2GWInDecompOctWraps")

                self.cipsecphase2gwindecryptfails = YLeaf(YType.uint32, "cipSecPhase2GWInDecryptFails")

                self.cipsecphase2gwindecrypts = YLeaf(YType.uint32, "cipSecPhase2GWInDecrypts")

                self.cipsecphase2gwindrops = YLeaf(YType.uint32, "cipSecPhase2GWInDrops")

                self.cipsecphase2gwinoctets = YLeaf(YType.uint32, "cipSecPhase2GWInOctets")

                self.cipsecphase2gwinoctwraps = YLeaf(YType.uint32, "cipSecPhase2GWInOctWraps")

                self.cipsecphase2gwinpkts = YLeaf(YType.uint32, "cipSecPhase2GWInPkts")

                self.cipsecphase2gwinreplaydrops = YLeaf(YType.uint32, "cipSecPhase2GWInReplayDrops")

                self.cipsecphase2gwnosafails = YLeaf(YType.uint32, "cipSecPhase2GWNoSaFails")

                self.cipsecphase2gwoutauthfails = YLeaf(YType.uint32, "cipSecPhase2GWOutAuthFails")

                self.cipsecphase2gwoutauths = YLeaf(YType.uint32, "cipSecPhase2GWOutAuths")

                self.cipsecphase2gwoutdrops = YLeaf(YType.uint32, "cipSecPhase2GWOutDrops")

                self.cipsecphase2gwoutencryptfails = YLeaf(YType.uint32, "cipSecPhase2GWOutEncryptFails")

                self.cipsecphase2gwoutencrypts = YLeaf(YType.uint32, "cipSecPhase2GWOutEncrypts")

                self.cipsecphase2gwoutoctets = YLeaf(YType.uint32, "cipSecPhase2GWOutOctets")

                self.cipsecphase2gwoutoctwraps = YLeaf(YType.uint32, "cipSecPhase2GWOutOctWraps")

                self.cipsecphase2gwoutpkts = YLeaf(YType.uint32, "cipSecPhase2GWOutPkts")

                self.cipsecphase2gwoutuncompoctets = YLeaf(YType.uint32, "cipSecPhase2GWOutUncompOctets")

                self.cipsecphase2gwoutuncompoctwraps = YLeaf(YType.uint32, "cipSecPhase2GWOutUncompOctWraps")

                self.cipsecphase2gwprevioustunnels = YLeaf(YType.uint32, "cipSecPhase2GWPreviousTunnels")

                self.cipsecphase2gwprotocolusefails = YLeaf(YType.uint32, "cipSecPhase2GWProtocolUseFails")

                self.cipsecphase2gwsyscapfails = YLeaf(YType.uint32, "cipSecPhase2GWSysCapFails")
                self._segment_path = lambda: "cipSecPhase2GWStatsEntry" + "[cmgwIndex='" + self.cmgwindex.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecPhase2GWStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecphase2Gwstatstable.Cipsecphase2Gwstatsentry, ['cmgwindex', 'cipsecphase2gwactivetunnels', 'cipsecphase2gwinauthfails', 'cipsecphase2gwinauths', 'cipsecphase2gwindecompoctets', 'cipsecphase2gwindecompoctwraps', 'cipsecphase2gwindecryptfails', 'cipsecphase2gwindecrypts', 'cipsecphase2gwindrops', 'cipsecphase2gwinoctets', 'cipsecphase2gwinoctwraps', 'cipsecphase2gwinpkts', 'cipsecphase2gwinreplaydrops', 'cipsecphase2gwnosafails', 'cipsecphase2gwoutauthfails', 'cipsecphase2gwoutauths', 'cipsecphase2gwoutdrops', 'cipsecphase2gwoutencryptfails', 'cipsecphase2gwoutencrypts', 'cipsecphase2gwoutoctets', 'cipsecphase2gwoutoctwraps', 'cipsecphase2gwoutpkts', 'cipsecphase2gwoutuncompoctets', 'cipsecphase2gwoutuncompoctwraps', 'cipsecphase2gwprevioustunnels', 'cipsecphase2gwprotocolusefails', 'cipsecphase2gwsyscapfails'], name, value)


    class Cipsecspitable(Entity):
        """
        The IPsec Phase\-2 Security Protection Index Table.
        This table contains an entry for each active 
        and expiring security
         association.
        
        .. attribute:: cipsecspientry
        
        	Each entry contains the attributes associated with active and expiring IPsec Phase\-2  security associations
        	**type**\: list of    :py:class:`Cipsecspientry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecspitable.Cipsecspientry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsecspitable, self).__init__()

            self.yang_name = "cipSecSpiTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cipSecSpiEntry" : ("cipsecspientry", CISCOIPSECFLOWMONITORMIB.Cipsecspitable.Cipsecspientry)}

            self.cipsecspientry = YList(self)
            self._segment_path = lambda: "cipSecSpiTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecspitable, [], name, value)


        class Cipsecspientry(Entity):
            """
            Each entry contains the attributes associated with
            active and expiring IPsec Phase\-2 
            security associations.
            
            .. attribute:: cipsectunindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cipsectunindex <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsectunneltable.Cipsectunnelentry>`
            
            .. attribute:: cipsecspiindex  <key>
            
            	The number of the SPI associated with the Phase\-2 Tunnel Table.  The value of this  index is a number which begins at one and is  incremented with each SPI associated with an  IPsec Phase\-2 Tunnel.  The value of this  object will wrap at 2,147,483,647
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecspidirection
            
            	The direction of the SPI
            	**type**\:   :py:class:`Cipsecspidirection <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecspitable.Cipsecspientry.Cipsecspidirection>`
            
            .. attribute:: cipsecspiprotocol
            
            	The protocol of the SPI
            	**type**\:   :py:class:`Cipsecspiprotocol <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecspitable.Cipsecspientry.Cipsecspiprotocol>`
            
            .. attribute:: cipsecspistatus
            
            	The status of the SPI
            	**type**\:   :py:class:`Cipsecspistatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecspitable.Cipsecspientry.Cipsecspistatus>`
            
            .. attribute:: cipsecspivalue
            
            	The value of the SPI
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cipsecspitable.Cipsecspientry, self).__init__()

                self.yang_name = "cipSecSpiEntry"
                self.yang_parent_name = "cipSecSpiTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cipsectunindex = YLeaf(YType.str, "cipSecTunIndex")

                self.cipsecspiindex = YLeaf(YType.int32, "cipSecSpiIndex")

                self.cipsecspidirection = YLeaf(YType.enumeration, "cipSecSpiDirection")

                self.cipsecspiprotocol = YLeaf(YType.enumeration, "cipSecSpiProtocol")

                self.cipsecspistatus = YLeaf(YType.enumeration, "cipSecSpiStatus")

                self.cipsecspivalue = YLeaf(YType.uint32, "cipSecSpiValue")
                self._segment_path = lambda: "cipSecSpiEntry" + "[cipSecTunIndex='" + self.cipsectunindex.get() + "']" + "[cipSecSpiIndex='" + self.cipsecspiindex.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecSpiTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecspitable.Cipsecspientry, ['cipsectunindex', 'cipsecspiindex', 'cipsecspidirection', 'cipsecspiprotocol', 'cipsecspistatus', 'cipsecspivalue'], name, value)

            class Cipsecspidirection(Enum):
                """
                Cipsecspidirection

                The direction of the SPI.

                .. data:: in_ = 1

                .. data:: out = 2

                """

                in_ = Enum.YLeaf(1, "in")

                out = Enum.YLeaf(2, "out")


            class Cipsecspiprotocol(Enum):
                """
                Cipsecspiprotocol

                The protocol of the SPI.

                .. data:: ah = 1

                .. data:: esp = 2

                .. data:: ipcomp = 3

                """

                ah = Enum.YLeaf(1, "ah")

                esp = Enum.YLeaf(2, "esp")

                ipcomp = Enum.YLeaf(3, "ipcomp")


            class Cipsecspistatus(Enum):
                """
                Cipsecspistatus

                The status of the SPI.

                .. data:: active = 1

                .. data:: expiring = 2

                """

                active = Enum.YLeaf(1, "active")

                expiring = Enum.YLeaf(2, "expiring")



    class Cipsectrapcntl(Entity):
        """
        
        
        .. attribute:: cipsectrapcntlikecertcrlfailure
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 Certificate/CRL Failure TRAP
        	**type**\:   :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlikenosa
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 No Security Association TRAP
        	**type**\:   :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlikeprotocolfail
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 Protocol Failure TRAP
        	**type**\:   :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlikesysfailure
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 System Failure TRAP
        	**type**\:   :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntliketunnelstart
        
        	This object defines the administrative state of sending the IPsec IKE Phase\-1 Tunnel Start TRAP
        	**type**\:   :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntliketunnelstop
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 Tunnel Stop TRAP
        	**type**\:   :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlipsecearlytunterm
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Early Tunnel Termination TRAP
        	**type**\:   :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlipsecnosa
        
        	This object defines the administrative state of sending the IPsec  Phase\-2  No Security Association TRAP
        	**type**\:   :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlipsecprotocolfail
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Protocol Failure TRAP
        	**type**\:   :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlipsecsetupfailure
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Set Up Failure TRAP
        	**type**\:   :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlipsecsysfailure
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 System Failure TRAP
        	**type**\:   :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlipsectunnelstart
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Tunnel Start TRAP
        	**type**\:   :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlipsectunnelstop
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Tunnel Stop TRAP
        	**type**\:   :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsectrapcntl, self).__init__()

            self.yang_name = "cipSecTrapCntl"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.cipsectrapcntlikecertcrlfailure = YLeaf(YType.enumeration, "cipSecTrapCntlIkeCertCrlFailure")

            self.cipsectrapcntlikenosa = YLeaf(YType.enumeration, "cipSecTrapCntlIkeNoSa")

            self.cipsectrapcntlikeprotocolfail = YLeaf(YType.enumeration, "cipSecTrapCntlIkeProtocolFail")

            self.cipsectrapcntlikesysfailure = YLeaf(YType.enumeration, "cipSecTrapCntlIkeSysFailure")

            self.cipsectrapcntliketunnelstart = YLeaf(YType.enumeration, "cipSecTrapCntlIkeTunnelStart")

            self.cipsectrapcntliketunnelstop = YLeaf(YType.enumeration, "cipSecTrapCntlIkeTunnelStop")

            self.cipsectrapcntlipsecearlytunterm = YLeaf(YType.enumeration, "cipSecTrapCntlIpSecEarlyTunTerm")

            self.cipsectrapcntlipsecnosa = YLeaf(YType.enumeration, "cipSecTrapCntlIpSecNoSa")

            self.cipsectrapcntlipsecprotocolfail = YLeaf(YType.enumeration, "cipSecTrapCntlIpSecProtocolFail")

            self.cipsectrapcntlipsecsetupfailure = YLeaf(YType.enumeration, "cipSecTrapCntlIpSecSetUpFailure")

            self.cipsectrapcntlipsecsysfailure = YLeaf(YType.enumeration, "cipSecTrapCntlIpSecSysFailure")

            self.cipsectrapcntlipsectunnelstart = YLeaf(YType.enumeration, "cipSecTrapCntlIpSecTunnelStart")

            self.cipsectrapcntlipsectunnelstop = YLeaf(YType.enumeration, "cipSecTrapCntlIpSecTunnelStop")
            self._segment_path = lambda: "cipSecTrapCntl"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsectrapcntl, ['cipsectrapcntlikecertcrlfailure', 'cipsectrapcntlikenosa', 'cipsectrapcntlikeprotocolfail', 'cipsectrapcntlikesysfailure', 'cipsectrapcntliketunnelstart', 'cipsectrapcntliketunnelstop', 'cipsectrapcntlipsecearlytunterm', 'cipsectrapcntlipsecnosa', 'cipsectrapcntlipsecprotocolfail', 'cipsectrapcntlipsecsetupfailure', 'cipsectrapcntlipsecsysfailure', 'cipsectrapcntlipsectunnelstart', 'cipsectrapcntlipsectunnelstop'], name, value)


    class Cipsectunnelhisttable(Entity):
        """
        The IPsec Phase\-2 Tunnel History Table.
        This table is implemented as a sliding 
        window in which only the
        last n entries are maintained.  The maximum number 
        of entries
        is specified by the cipSecHistTableSize object.
        
        .. attribute:: cipsectunnelhistentry
        
        	Each entry contains the attributes associated with a previously active IPsec Phase\-2 Tunnel
        	**type**\: list of    :py:class:`Cipsectunnelhistentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable.Cipsectunnelhistentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable, self).__init__()

            self.yang_name = "cipSecTunnelHistTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cipSecTunnelHistEntry" : ("cipsectunnelhistentry", CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable.Cipsectunnelhistentry)}

            self.cipsectunnelhistentry = YList(self)
            self._segment_path = lambda: "cipSecTunnelHistTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable, [], name, value)


        class Cipsectunnelhistentry(Entity):
            """
            Each entry contains the attributes associated with
            a previously active IPsec Phase\-2 Tunnel.
            
            .. attribute:: cipsectunhistindex  <key>
            
            	The index of the IPsec Phase\-2 Tunnel History Table. The value of the index is a number which  begins at one and is incremented with each tunnel  that ends. The value of this object will wrap at 2,147,483,647
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunhistactiveindex
            
            	The index of the previously active IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunhistactivetime
            
            	The length of time the IPsec Phase\-2 Tunnel has been active in hundredths of seconds
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cipsectunhistencapmode
            
            	The encapsulation mode used by the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`EncapMode <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncapMode>`
            
            .. attribute:: cipsectunhisthcindecompoctets
            
            	A high capacity count of the total number of decompressed octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER the packet is decompressed. If compression is not being used, this value will match the value of cipSecTunHistHcInOctets
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunhisthcinoctets
            
            	A high capacity count of the total number of octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated BEFORE determining whether or not  the packet should be decompressed
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunhisthcoutoctets
            
            	A high capacity count of the total number of octets sent by this IPsec Phase\-2 Tunnel.  This value  is accumulated AFTER determining whether or not  the packet should be compressed
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunhisthcoutuncompoctets
            
            	A high capacity count of the total number of uncompressed octets sent by this  IPsec Phase\-2 Tunnel.  This value is accumulated  BEFORE the packet is compressed. If compression is not being used, this value will match the value of cipSecTunHistHcOutOctets
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: Octets
            
            .. attribute:: cipsectunhistiketunnelindex
            
            	The index of the associated IPsec Phase\-1 Tunnel (cikeTunIndex in the cikeTunnelTable)
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunhistinauthfails
            
            	The total number of inbound authentication's which ended in  failure by this IPsec Phase\-2 Tunnel 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsectunhistinauths
            
            	The total number of inbound authentication's performed  by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Events
            
            .. attribute:: cipsectunhistindecompoctets
            
            	The total number of decompressed octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER the packet is decompressed. If compression is not being used, this value will match the value of cipSecTunHistInOctets. See also cipSecTunInDecompOctWraps for the number of times this counter has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsectunhistindecompoctwraps
            
            	The number of times the decompressed octets received counter (cipSecTunInDecompOctets) has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsectunhistindecryptfails
            
            	The total number of inbound decryption's which ended in failure  by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsectunhistindecrypts
            
            	The total number of inbound decryption's performed by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunhistindroppkts
            
            	The total number of packets dropped during receive processing by this IPsec Phase\-2 Tunnel.  This count does NOT include packets  dropped due to Anti\-Replay processing
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunhistinoctets
            
            	The total number of octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated BEFORE determining whether or not the packet should  be decompressed.  See also cipSecTunInOctWraps for  the number of times this counter has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsectunhistinoctwraps
            
            	The number of times the octets received counter (cipSecTunInOctets) has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsectunhistinpkts
            
            	The total number of packets received by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunhistinreplaydroppkts
            
            	The total number of packets dropped during receive processing due to Anti\-Replay processing  by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunhistinsaahauthalgo
            
            	The authentication algorithm used by the inbound authentication header (AH) security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`AuthAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo>`
            
            .. attribute:: cipsectunhistinsadecompalgo
            
            	The decompression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`CompAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CompAlgo>`
            
            .. attribute:: cipsectunhistinsadiffhellmangrp
            
            	The Diffie Hellman Group used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`DiffHellmanGrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp>`
            
            .. attribute:: cipsectunhistinsaencryptalgo
            
            	The encryption algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`EncryptAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo>`
            
            .. attribute:: cipsectunhistinsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP)  security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`AuthAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo>`
            
            .. attribute:: cipsectunhistkeytype
            
            	The type of key used by the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`KeyType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.KeyType>`
            
            .. attribute:: cipsectunhistlifesize
            
            	The negotiated LifeSize of the IPsec Phase\-2 Tunnel in kilobytes
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**units**\: KBytes
            
            .. attribute:: cipsectunhistlifetime
            
            	The negotiated LifeTime of the IPsec Phase\-2 Tunnel in seconds
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**units**\: Seconds
            
            .. attribute:: cipsectunhistlocaladdr
            
            	The IP address of the local endpoint for the IPsec Phase\-2 Tunnel
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsectunhistoutauthfails
            
            	The total number of outbound authentication's which ended in  failure by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsectunhistoutauths
            
            	The total number of outbound authentication's performed by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Events
            
            .. attribute:: cipsectunhistoutdroppkts
            
            	The total number of packets dropped during send processing  by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunhistoutencryptfails
            
            	The total number of outbound encryption's which ended in failure  by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsectunhistoutencrypts
            
            	The total number of outbound encryption's performed by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunhistoutoctets
            
            	The total number of octets sent by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER determining whether or not the  packet should be compressed.  See also cipSecTunOutOctWraps for the number of times this counter has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsectunhistoutoctwraps
            
            	The number of times the octets sent counter (cipSecTunOutOctets) has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsectunhistoutpkts
            
            	The total number of packets sent by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunhistoutsaahauthalgo
            
            	The authentication algorithm used by the outbound authentication header (AH) security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`AuthAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo>`
            
            .. attribute:: cipsectunhistoutsacompalgo
            
            	The compression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`CompAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CompAlgo>`
            
            .. attribute:: cipsectunhistoutsadiffhellmangrp
            
            	The Diffie Hellman Group used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`DiffHellmanGrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp>`
            
            .. attribute:: cipsectunhistoutsaencryptalgo
            
            	The encryption algorithm used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`EncryptAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo>`
            
            .. attribute:: cipsectunhistoutsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP)  security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`AuthAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo>`
            
            .. attribute:: cipsectunhistoutuncompoctets
            
            	The total number of uncompressed octets sent by this IPsec Phase\-2 Tunnel.  This value is accumulated BEFORE the packet is compressed. If compression is not being used, this value will match the value of  cipSecTunHistOutOctets.  See also  cipSecTunOutDecompOctWraps for the number of times this counter has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsectunhistoutuncompoctwraps
            
            	The number of times the uncompressed octets sent counter (cipSecTunOutUncompOctets) has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsectunhistremoteaddr
            
            	The IP address of the remote endpoint for the IPsec Phase\-2 Tunnel
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsectunhiststarttime
            
            	The value of sysUpTime in hundredths of seconds when the IPsec Phase\-2 Tunnel was started
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhisttermreason
            
            	The reason the IPsec Phase\-2 Tunnel was terminated. Possible reasons include\: 1 = other 2 = normal termination 3 = operator request 4 = peer delete request was received 5 = contact with peer was lost 6 = local failure occurred 7 = operator initiated check point request
            	**type**\:   :py:class:`Cipsectunhisttermreason <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable.Cipsectunnelhistentry.Cipsectunhisttermreason>`
            
            .. attribute:: cipsectunhisttotalrefreshes
            
            	The total number of security association refreshes performed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: QM Exchanges
            
            .. attribute:: cipsectunhisttotalsas
            
            	The total number of security associations used during the  life of the IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SAs
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable.Cipsectunnelhistentry, self).__init__()

                self.yang_name = "cipSecTunnelHistEntry"
                self.yang_parent_name = "cipSecTunnelHistTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cipsectunhistindex = YLeaf(YType.int32, "cipSecTunHistIndex")

                self.cipsectunhistactiveindex = YLeaf(YType.int32, "cipSecTunHistActiveIndex")

                self.cipsectunhistactivetime = YLeaf(YType.int32, "cipSecTunHistActiveTime")

                self.cipsectunhistencapmode = YLeaf(YType.enumeration, "cipSecTunHistEncapMode")

                self.cipsectunhisthcindecompoctets = YLeaf(YType.uint64, "cipSecTunHistHcInDecompOctets")

                self.cipsectunhisthcinoctets = YLeaf(YType.uint64, "cipSecTunHistHcInOctets")

                self.cipsectunhisthcoutoctets = YLeaf(YType.uint64, "cipSecTunHistHcOutOctets")

                self.cipsectunhisthcoutuncompoctets = YLeaf(YType.uint64, "cipSecTunHistHcOutUncompOctets")

                self.cipsectunhistiketunnelindex = YLeaf(YType.int32, "cipSecTunHistIkeTunnelIndex")

                self.cipsectunhistinauthfails = YLeaf(YType.uint32, "cipSecTunHistInAuthFails")

                self.cipsectunhistinauths = YLeaf(YType.uint32, "cipSecTunHistInAuths")

                self.cipsectunhistindecompoctets = YLeaf(YType.uint32, "cipSecTunHistInDecompOctets")

                self.cipsectunhistindecompoctwraps = YLeaf(YType.uint32, "cipSecTunHistInDecompOctWraps")

                self.cipsectunhistindecryptfails = YLeaf(YType.uint32, "cipSecTunHistInDecryptFails")

                self.cipsectunhistindecrypts = YLeaf(YType.uint32, "cipSecTunHistInDecrypts")

                self.cipsectunhistindroppkts = YLeaf(YType.uint32, "cipSecTunHistInDropPkts")

                self.cipsectunhistinoctets = YLeaf(YType.uint32, "cipSecTunHistInOctets")

                self.cipsectunhistinoctwraps = YLeaf(YType.uint32, "cipSecTunHistInOctWraps")

                self.cipsectunhistinpkts = YLeaf(YType.uint32, "cipSecTunHistInPkts")

                self.cipsectunhistinreplaydroppkts = YLeaf(YType.uint32, "cipSecTunHistInReplayDropPkts")

                self.cipsectunhistinsaahauthalgo = YLeaf(YType.enumeration, "cipSecTunHistInSaAhAuthAlgo")

                self.cipsectunhistinsadecompalgo = YLeaf(YType.enumeration, "cipSecTunHistInSaDecompAlgo")

                self.cipsectunhistinsadiffhellmangrp = YLeaf(YType.enumeration, "cipSecTunHistInSaDiffHellmanGrp")

                self.cipsectunhistinsaencryptalgo = YLeaf(YType.enumeration, "cipSecTunHistInSaEncryptAlgo")

                self.cipsectunhistinsaespauthalgo = YLeaf(YType.enumeration, "cipSecTunHistInSaEspAuthAlgo")

                self.cipsectunhistkeytype = YLeaf(YType.enumeration, "cipSecTunHistKeyType")

                self.cipsectunhistlifesize = YLeaf(YType.int32, "cipSecTunHistLifeSize")

                self.cipsectunhistlifetime = YLeaf(YType.int32, "cipSecTunHistLifeTime")

                self.cipsectunhistlocaladdr = YLeaf(YType.str, "cipSecTunHistLocalAddr")

                self.cipsectunhistoutauthfails = YLeaf(YType.uint32, "cipSecTunHistOutAuthFails")

                self.cipsectunhistoutauths = YLeaf(YType.uint32, "cipSecTunHistOutAuths")

                self.cipsectunhistoutdroppkts = YLeaf(YType.uint32, "cipSecTunHistOutDropPkts")

                self.cipsectunhistoutencryptfails = YLeaf(YType.uint32, "cipSecTunHistOutEncryptFails")

                self.cipsectunhistoutencrypts = YLeaf(YType.uint32, "cipSecTunHistOutEncrypts")

                self.cipsectunhistoutoctets = YLeaf(YType.uint32, "cipSecTunHistOutOctets")

                self.cipsectunhistoutoctwraps = YLeaf(YType.uint32, "cipSecTunHistOutOctWraps")

                self.cipsectunhistoutpkts = YLeaf(YType.uint32, "cipSecTunHistOutPkts")

                self.cipsectunhistoutsaahauthalgo = YLeaf(YType.enumeration, "cipSecTunHistOutSaAhAuthAlgo")

                self.cipsectunhistoutsacompalgo = YLeaf(YType.enumeration, "cipSecTunHistOutSaCompAlgo")

                self.cipsectunhistoutsadiffhellmangrp = YLeaf(YType.enumeration, "cipSecTunHistOutSaDiffHellmanGrp")

                self.cipsectunhistoutsaencryptalgo = YLeaf(YType.enumeration, "cipSecTunHistOutSaEncryptAlgo")

                self.cipsectunhistoutsaespauthalgo = YLeaf(YType.enumeration, "cipSecTunHistOutSaEspAuthAlgo")

                self.cipsectunhistoutuncompoctets = YLeaf(YType.uint32, "cipSecTunHistOutUncompOctets")

                self.cipsectunhistoutuncompoctwraps = YLeaf(YType.uint32, "cipSecTunHistOutUncompOctWraps")

                self.cipsectunhistremoteaddr = YLeaf(YType.str, "cipSecTunHistRemoteAddr")

                self.cipsectunhiststarttime = YLeaf(YType.uint32, "cipSecTunHistStartTime")

                self.cipsectunhisttermreason = YLeaf(YType.enumeration, "cipSecTunHistTermReason")

                self.cipsectunhisttotalrefreshes = YLeaf(YType.uint32, "cipSecTunHistTotalRefreshes")

                self.cipsectunhisttotalsas = YLeaf(YType.uint32, "cipSecTunHistTotalSas")
                self._segment_path = lambda: "cipSecTunnelHistEntry" + "[cipSecTunHistIndex='" + self.cipsectunhistindex.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecTunnelHistTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable.Cipsectunnelhistentry, ['cipsectunhistindex', 'cipsectunhistactiveindex', 'cipsectunhistactivetime', 'cipsectunhistencapmode', 'cipsectunhisthcindecompoctets', 'cipsectunhisthcinoctets', 'cipsectunhisthcoutoctets', 'cipsectunhisthcoutuncompoctets', 'cipsectunhistiketunnelindex', 'cipsectunhistinauthfails', 'cipsectunhistinauths', 'cipsectunhistindecompoctets', 'cipsectunhistindecompoctwraps', 'cipsectunhistindecryptfails', 'cipsectunhistindecrypts', 'cipsectunhistindroppkts', 'cipsectunhistinoctets', 'cipsectunhistinoctwraps', 'cipsectunhistinpkts', 'cipsectunhistinreplaydroppkts', 'cipsectunhistinsaahauthalgo', 'cipsectunhistinsadecompalgo', 'cipsectunhistinsadiffhellmangrp', 'cipsectunhistinsaencryptalgo', 'cipsectunhistinsaespauthalgo', 'cipsectunhistkeytype', 'cipsectunhistlifesize', 'cipsectunhistlifetime', 'cipsectunhistlocaladdr', 'cipsectunhistoutauthfails', 'cipsectunhistoutauths', 'cipsectunhistoutdroppkts', 'cipsectunhistoutencryptfails', 'cipsectunhistoutencrypts', 'cipsectunhistoutoctets', 'cipsectunhistoutoctwraps', 'cipsectunhistoutpkts', 'cipsectunhistoutsaahauthalgo', 'cipsectunhistoutsacompalgo', 'cipsectunhistoutsadiffhellmangrp', 'cipsectunhistoutsaencryptalgo', 'cipsectunhistoutsaespauthalgo', 'cipsectunhistoutuncompoctets', 'cipsectunhistoutuncompoctwraps', 'cipsectunhistremoteaddr', 'cipsectunhiststarttime', 'cipsectunhisttermreason', 'cipsectunhisttotalrefreshes', 'cipsectunhisttotalsas'], name, value)

            class Cipsectunhisttermreason(Enum):
                """
                Cipsectunhisttermreason

                The reason the IPsec Phase\-2 Tunnel was terminated.

                Possible reasons include\:

                1 = other

                2 = normal termination

                3 = operator request

                4 = peer delete request was received

                5 = contact with peer was lost

                6 = local failure occurred

                7 = operator initiated check point request

                .. data:: other = 1

                .. data:: normal = 2

                .. data:: operRequest = 3

                .. data:: peerDelRequest = 4

                .. data:: peerLost = 5

                .. data:: seqNumRollOver = 6

                .. data:: checkPointReq = 7

                """

                other = Enum.YLeaf(1, "other")

                normal = Enum.YLeaf(2, "normal")

                operRequest = Enum.YLeaf(3, "operRequest")

                peerDelRequest = Enum.YLeaf(4, "peerDelRequest")

                peerLost = Enum.YLeaf(5, "peerLost")

                seqNumRollOver = Enum.YLeaf(6, "seqNumRollOver")

                checkPointReq = Enum.YLeaf(7, "checkPointReq")



    class Cipsectunneltable(Entity):
        """
        The IPsec Phase\-2 Tunnel Table.
        There is one entry in this table for 
        each active IPsec Phase\-2 Tunnel.
        
        .. attribute:: cipsectunnelentry
        
        	Each entry contains the attributes associated with an active IPsec Phase\-2 Tunnel
        	**type**\: list of    :py:class:`Cipsectunnelentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsectunneltable.Cipsectunnelentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsectunneltable, self).__init__()

            self.yang_name = "cipSecTunnelTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cipSecTunnelEntry" : ("cipsectunnelentry", CISCOIPSECFLOWMONITORMIB.Cipsectunneltable.Cipsectunnelentry)}

            self.cipsectunnelentry = YList(self)
            self._segment_path = lambda: "cipSecTunnelTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsectunneltable, [], name, value)


        class Cipsectunnelentry(Entity):
            """
            Each entry contains the attributes
            associated with an active IPsec Phase\-2 Tunnel.
            
            .. attribute:: cipsectunindex  <key>
            
            	The index of the IPsec Phase\-2 Tunnel Table. The value of the index is a number which begins  at one and is incremented with each tunnel that  is created. The value of this object will wrap  at 2,147,483,647
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunactivetime
            
            	The length of time the IPsec Phase\-2 Tunnel has been  active in hundredths of seconds
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cipsectuncurrentsainstances
            
            	The number of security associations which are currently active or expiring
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunencapmode
            
            	The encapsulation mode used by the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`EncapMode <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncapMode>`
            
            .. attribute:: cipsectunexpiredsainstances
            
            	The total number of security associations which have expired
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: SAs
            
            .. attribute:: cipsectunhcindecompoctets
            
            	A high capacity count of the total number of decompressed octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER the packet is decompressed. If compression is not being used, this value will match the value of cipSecTunHcInOctets
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunhcinoctets
            
            	A high capacity count of the total number of octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated BEFORE determining whether or not the packet should be decompressed
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: Octets
            
            .. attribute:: cipsectunhcoutoctets
            
            	A high capacity count of the total number of octets sent by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER determining whether or not the  packet should be compressed
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunhcoutuncompoctets
            
            	A high capacity count of the total number of uncompressed octets sent by this IPsec  Phase\-2 Tunnel.  This value is accumulated BEFORE  the packet is compressed. If compression  is not being used, this value will match the value  of cipSecTunHcOutOctets
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectuniketunnelalive
            
            	An indicator which specifies whether or not the IPsec Phase\-1 IKE Tunnel currently exists
            	**type**\:  bool
            
            .. attribute:: cipsectuniketunnelindex
            
            	The index of the associated IPsec Phase\-1 IKE Tunnel.  (cikeTunIndex in the cikeTunnelTable)
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectuninauthfails
            
            	The total number of inbound authentication's which ended in  failure by this IPsec Phase\-2 Tunnel 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsectuninauths
            
            	The total number of inbound authentication's performed by this  IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Events
            
            .. attribute:: cipsectunindecompoctets
            
            	The total number of decompressed octets received by this IPsec Phase\-2 Tunnel. This value is  accumulated AFTER the packet is decompressed.  If compression is not being  used, this value will match the value of   cipSecTunInOctets.  See also cipSecTunInDecompOctWraps   for the number of times  this counter has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsectunindecompoctwraps
            
            	The number of times the decompressed octets received counter  (cipSecTunInDecompOctets) has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsectunindecryptfails
            
            	The total number of inbound decryption's which ended in failure  by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsectunindecrypts
            
            	The total number of inbound decryption's performed by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunindroppkts
            
            	The total number of packets dropped during receive processing by this IPsec Phase\-2  Tunnel. This count does NOT include  packets dropped due to Anti\-Replay processing
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectuninoctets
            
            	The total number of octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated BEFORE determining whether or not the packet should be decompressed.  See also cipSecTunInOctWraps for the number of times this counter has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsectuninoctwraps
            
            	The number of times the octets received counter (cipSecTunInOctets) has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsectuninpkts
            
            	The total number of packets received by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectuninreplaydroppkts
            
            	The total number of packets dropped during receive processing due to Anti\-Replay processing  by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectuninsaahauthalgo
            
            	The authentication algorithm used by the inbound authentication header (AH) security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`AuthAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo>`
            
            .. attribute:: cipsectuninsadecompalgo
            
            	The decompression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`CompAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CompAlgo>`
            
            .. attribute:: cipsectuninsadiffhellmangrp
            
            	The Diffie Hellman Group used by the inbound security association of the  IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`DiffHellmanGrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp>`
            
            .. attribute:: cipsectuninsaencryptalgo
            
            	The encryption algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`EncryptAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo>`
            
            .. attribute:: cipsectuninsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP) security  association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`AuthAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo>`
            
            .. attribute:: cipsectunkeytype
            
            	The type of key used by the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`KeyType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.KeyType>`
            
            .. attribute:: cipsectunlifesize
            
            	The negotiated LifeSize of the IPsec Phase\-2 Tunnel in kilobytes
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**units**\: KBytes
            
            .. attribute:: cipsectunlifetime
            
            	The negotiated LifeTime of the IPsec Phase\-2 Tunnel in seconds
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**units**\: Seconds
            
            .. attribute:: cipsectunlocaladdr
            
            	The IP address of the local endpoint for the IPsec Phase\-2 Tunnel
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsectunoutauthfails
            
            	The total number of outbound authentication's which ended in failure  by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsectunoutauths
            
            	The total number of outbound authentication's performed by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Events
            
            .. attribute:: cipsectunoutdroppkts
            
            	The total number of packets dropped during send processing by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunoutencryptfails
            
            	The total number of outbound encryption's which ended in failure by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsectunoutencrypts
            
            	The total number of outbound encryption's performed by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunoutoctets
            
            	The total number of octets sent by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER determining whether or not the packet should  be compressed.  See also cipSecTunOutOctWraps for the number of times this counter has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsectunoutoctwraps
            
            	The number of times the out octets counter (cipSecTunOutOctets) has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsectunoutpkts
            
            	The total number of packets sent by this IPsec Phase\-2 Tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunoutsaahauthalgo
            
            	The authentication algorithm used by the outbound authentication header (AH) security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`AuthAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo>`
            
            .. attribute:: cipsectunoutsacompalgo
            
            	The compression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`CompAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CompAlgo>`
            
            .. attribute:: cipsectunoutsadiffhellmangrp
            
            	The Diffie Hellman Group used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`DiffHellmanGrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp>`
            
            .. attribute:: cipsectunoutsaencryptalgo
            
            	The encryption algorithm used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`EncryptAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo>`
            
            .. attribute:: cipsectunoutsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP)  security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`AuthAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo>`
            
            .. attribute:: cipsectunoutuncompoctets
            
            	The total number of uncompressed octets sent by this IPsec Phase\-2 Tunnel.  This value  is accumulated BEFORE the packet is compressed.  If compression is not being used, this value  will match the value of cipSecTunOutOctets.  See also cipSecTunOutDecompOctWraps for the   number of times this counter has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsectunoutuncompoctwraps
            
            	The number of times the uncompressed octets sent counter (cipSecTunOutUncompOctets) has wrapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsectunremoteaddr
            
            	The IP address of the remote endpoint for the IPsec Phase\-2 Tunnel
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsectunsalifesizethreshold
            
            	The security association LifeSize refresh threshold in kilobytes
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**units**\: KBytes
            
            .. attribute:: cipsectunsalifetimethreshold
            
            	The security association LifeTime refresh threshold in seconds
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**units**\: Seconds
            
            .. attribute:: cipsectunstatus
            
            	The status of the MIB table row.  This object can be used to bring the tunnel down by setting value of this object to destroy(2). When the value is set to destroy(2), the SA bundle is destroyed and this row is deleted from this table.  When this MIB value is queried, the value of active(1) is always returned, if the instance  exists.  This object cannot be used to create a MIB  table row
            	**type**\:   :py:class:`TunnelStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TunnelStatus>`
            
            .. attribute:: cipsectuntotalrefreshes
            
            	The total number of security association refreshes performed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: QM Exchanges
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cipsectunneltable.Cipsectunnelentry, self).__init__()

                self.yang_name = "cipSecTunnelEntry"
                self.yang_parent_name = "cipSecTunnelTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cipsectunindex = YLeaf(YType.int32, "cipSecTunIndex")

                self.cipsectunactivetime = YLeaf(YType.int32, "cipSecTunActiveTime")

                self.cipsectuncurrentsainstances = YLeaf(YType.uint32, "cipSecTunCurrentSaInstances")

                self.cipsectunencapmode = YLeaf(YType.enumeration, "cipSecTunEncapMode")

                self.cipsectunexpiredsainstances = YLeaf(YType.uint32, "cipSecTunExpiredSaInstances")

                self.cipsectunhcindecompoctets = YLeaf(YType.uint64, "cipSecTunHcInDecompOctets")

                self.cipsectunhcinoctets = YLeaf(YType.uint64, "cipSecTunHcInOctets")

                self.cipsectunhcoutoctets = YLeaf(YType.uint64, "cipSecTunHcOutOctets")

                self.cipsectunhcoutuncompoctets = YLeaf(YType.uint64, "cipSecTunHcOutUncompOctets")

                self.cipsectuniketunnelalive = YLeaf(YType.boolean, "cipSecTunIkeTunnelAlive")

                self.cipsectuniketunnelindex = YLeaf(YType.int32, "cipSecTunIkeTunnelIndex")

                self.cipsectuninauthfails = YLeaf(YType.uint32, "cipSecTunInAuthFails")

                self.cipsectuninauths = YLeaf(YType.uint32, "cipSecTunInAuths")

                self.cipsectunindecompoctets = YLeaf(YType.uint32, "cipSecTunInDecompOctets")

                self.cipsectunindecompoctwraps = YLeaf(YType.uint32, "cipSecTunInDecompOctWraps")

                self.cipsectunindecryptfails = YLeaf(YType.uint32, "cipSecTunInDecryptFails")

                self.cipsectunindecrypts = YLeaf(YType.uint32, "cipSecTunInDecrypts")

                self.cipsectunindroppkts = YLeaf(YType.uint32, "cipSecTunInDropPkts")

                self.cipsectuninoctets = YLeaf(YType.uint32, "cipSecTunInOctets")

                self.cipsectuninoctwraps = YLeaf(YType.uint32, "cipSecTunInOctWraps")

                self.cipsectuninpkts = YLeaf(YType.uint32, "cipSecTunInPkts")

                self.cipsectuninreplaydroppkts = YLeaf(YType.uint32, "cipSecTunInReplayDropPkts")

                self.cipsectuninsaahauthalgo = YLeaf(YType.enumeration, "cipSecTunInSaAhAuthAlgo")

                self.cipsectuninsadecompalgo = YLeaf(YType.enumeration, "cipSecTunInSaDecompAlgo")

                self.cipsectuninsadiffhellmangrp = YLeaf(YType.enumeration, "cipSecTunInSaDiffHellmanGrp")

                self.cipsectuninsaencryptalgo = YLeaf(YType.enumeration, "cipSecTunInSaEncryptAlgo")

                self.cipsectuninsaespauthalgo = YLeaf(YType.enumeration, "cipSecTunInSaEspAuthAlgo")

                self.cipsectunkeytype = YLeaf(YType.enumeration, "cipSecTunKeyType")

                self.cipsectunlifesize = YLeaf(YType.int32, "cipSecTunLifeSize")

                self.cipsectunlifetime = YLeaf(YType.int32, "cipSecTunLifeTime")

                self.cipsectunlocaladdr = YLeaf(YType.str, "cipSecTunLocalAddr")

                self.cipsectunoutauthfails = YLeaf(YType.uint32, "cipSecTunOutAuthFails")

                self.cipsectunoutauths = YLeaf(YType.uint32, "cipSecTunOutAuths")

                self.cipsectunoutdroppkts = YLeaf(YType.uint32, "cipSecTunOutDropPkts")

                self.cipsectunoutencryptfails = YLeaf(YType.uint32, "cipSecTunOutEncryptFails")

                self.cipsectunoutencrypts = YLeaf(YType.uint32, "cipSecTunOutEncrypts")

                self.cipsectunoutoctets = YLeaf(YType.uint32, "cipSecTunOutOctets")

                self.cipsectunoutoctwraps = YLeaf(YType.uint32, "cipSecTunOutOctWraps")

                self.cipsectunoutpkts = YLeaf(YType.uint32, "cipSecTunOutPkts")

                self.cipsectunoutsaahauthalgo = YLeaf(YType.enumeration, "cipSecTunOutSaAhAuthAlgo")

                self.cipsectunoutsacompalgo = YLeaf(YType.enumeration, "cipSecTunOutSaCompAlgo")

                self.cipsectunoutsadiffhellmangrp = YLeaf(YType.enumeration, "cipSecTunOutSaDiffHellmanGrp")

                self.cipsectunoutsaencryptalgo = YLeaf(YType.enumeration, "cipSecTunOutSaEncryptAlgo")

                self.cipsectunoutsaespauthalgo = YLeaf(YType.enumeration, "cipSecTunOutSaEspAuthAlgo")

                self.cipsectunoutuncompoctets = YLeaf(YType.uint32, "cipSecTunOutUncompOctets")

                self.cipsectunoutuncompoctwraps = YLeaf(YType.uint32, "cipSecTunOutUncompOctWraps")

                self.cipsectunremoteaddr = YLeaf(YType.str, "cipSecTunRemoteAddr")

                self.cipsectunsalifesizethreshold = YLeaf(YType.int32, "cipSecTunSaLifeSizeThreshold")

                self.cipsectunsalifetimethreshold = YLeaf(YType.int32, "cipSecTunSaLifeTimeThreshold")

                self.cipsectunstatus = YLeaf(YType.enumeration, "cipSecTunStatus")

                self.cipsectuntotalrefreshes = YLeaf(YType.uint32, "cipSecTunTotalRefreshes")
                self._segment_path = lambda: "cipSecTunnelEntry" + "[cipSecTunIndex='" + self.cipsectunindex.get() + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecTunnelTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsectunneltable.Cipsectunnelentry, ['cipsectunindex', 'cipsectunactivetime', 'cipsectuncurrentsainstances', 'cipsectunencapmode', 'cipsectunexpiredsainstances', 'cipsectunhcindecompoctets', 'cipsectunhcinoctets', 'cipsectunhcoutoctets', 'cipsectunhcoutuncompoctets', 'cipsectuniketunnelalive', 'cipsectuniketunnelindex', 'cipsectuninauthfails', 'cipsectuninauths', 'cipsectunindecompoctets', 'cipsectunindecompoctwraps', 'cipsectunindecryptfails', 'cipsectunindecrypts', 'cipsectunindroppkts', 'cipsectuninoctets', 'cipsectuninoctwraps', 'cipsectuninpkts', 'cipsectuninreplaydroppkts', 'cipsectuninsaahauthalgo', 'cipsectuninsadecompalgo', 'cipsectuninsadiffhellmangrp', 'cipsectuninsaencryptalgo', 'cipsectuninsaespauthalgo', 'cipsectunkeytype', 'cipsectunlifesize', 'cipsectunlifetime', 'cipsectunlocaladdr', 'cipsectunoutauthfails', 'cipsectunoutauths', 'cipsectunoutdroppkts', 'cipsectunoutencryptfails', 'cipsectunoutencrypts', 'cipsectunoutoctets', 'cipsectunoutoctwraps', 'cipsectunoutpkts', 'cipsectunoutsaahauthalgo', 'cipsectunoutsacompalgo', 'cipsectunoutsadiffhellmangrp', 'cipsectunoutsaencryptalgo', 'cipsectunoutsaespauthalgo', 'cipsectunoutuncompoctets', 'cipsectunoutuncompoctwraps', 'cipsectunremoteaddr', 'cipsectunsalifesizethreshold', 'cipsectunsalifetimethreshold', 'cipsectunstatus', 'cipsectuntotalrefreshes'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOIPSECFLOWMONITORMIB()
        return self._top_entity

