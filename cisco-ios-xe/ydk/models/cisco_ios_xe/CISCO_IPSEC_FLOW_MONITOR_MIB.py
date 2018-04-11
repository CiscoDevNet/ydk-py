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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AuthAlgo(Enum):
    """
    AuthAlgo (Enum Class)

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
    CompAlgo (Enum Class)

    The compression algorithm used by a

    security association of an IPsec Phase\-2 Tunnel.

    .. data:: none = 1

    .. data:: ldf = 2

    """

    none = Enum.YLeaf(1, "none")

    ldf = Enum.YLeaf(2, "ldf")


class DiffHellmanGrp(Enum):
    """
    DiffHellmanGrp (Enum Class)

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
    EncapMode (Enum Class)

    The encapsulation mode used by an IPsec Phase\-2

    Tunnel.

    .. data:: tunnel = 1

    .. data:: transport = 2

    """

    tunnel = Enum.YLeaf(1, "tunnel")

    transport = Enum.YLeaf(2, "transport")


class EncryptAlgo(Enum):
    """
    EncryptAlgo (Enum Class)

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
    EndPtType (Enum Class)

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
    IkeAuthMethod (Enum Class)

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
    IkeHashAlgo (Enum Class)

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
    IkeNegoMode (Enum Class)

    The IPsec Phase\-1 IKE negotiation mode.

    .. data:: main = 1

    .. data:: aggressive = 2

    """

    main = Enum.YLeaf(1, "main")

    aggressive = Enum.YLeaf(2, "aggressive")


class IkePeerType(Enum):
    """
    IkePeerType (Enum Class)

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
    KeyType (Enum Class)

    The type of key used by an IPsec Phase\-2 Tunnel.

    .. data:: ike = 1

    .. data:: manual = 2

    """

    ike = Enum.YLeaf(1, "ike")

    manual = Enum.YLeaf(2, "manual")


class TrapStatus(Enum):
    """
    TrapStatus (Enum Class)

    The administrative status for sending a TRAP.

    .. data:: enabled = 1

    .. data:: disabled = 2

    """

    enabled = Enum.YLeaf(1, "enabled")

    disabled = Enum.YLeaf(2, "disabled")


class TunnelStatus(Enum):
    """
    TunnelStatus (Enum Class)

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
    
    
    .. attribute:: cipseclevels
    
    	
    	**type**\:  :py:class:`Cipseclevels <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipseclevels>`
    
    .. attribute:: cikeglobalstats
    
    	
    	**type**\:  :py:class:`Cikeglobalstats <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikeglobalstats>`
    
    .. attribute:: cipsecglobalstats
    
    	
    	**type**\:  :py:class:`Cipsecglobalstats <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecglobalstats>`
    
    .. attribute:: cipsechistglobalcntl
    
    	
    	**type**\:  :py:class:`Cipsechistglobalcntl <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsechistglobalcntl>`
    
    .. attribute:: cipsecfailglobalcntl
    
    	
    	**type**\:  :py:class:`Cipsecfailglobalcntl <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecfailglobalcntl>`
    
    .. attribute:: cipsectrapcntl
    
    	
    	**type**\:  :py:class:`Cipsectrapcntl <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsectrapcntl>`
    
    .. attribute:: cikepeertable
    
    	The IPsec Phase\-1 Internet Key Exchange Peer Table. There is one entry in this table for each IPsec Phase\-1 IKE peer association which is currently associated with an active IPsec Phase\-1 Tunnel. The IPsec Phase\-1 IKE Tunnel associated with this IPsec Phase\-1 IKE peer association may or may not be currently active
    	**type**\:  :py:class:`Cikepeertable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikepeertable>`
    
    .. attribute:: ciketunneltable
    
    	The IPsec Phase\-1 Internet Key Exchange Tunnel Table. There is one entry in this table for each active IPsec Phase\-1 IKE Tunnel
    	**type**\:  :py:class:`Ciketunneltable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Ciketunneltable>`
    
    .. attribute:: cikepeercorrtable
    
    	The IPsec Phase\-1 Internet Key Exchange Peer Association to IPsec Phase\-2 Tunnel Correlation Table. There is one entry in this table for each active IPsec Phase\-2 Tunnel
    	**type**\:  :py:class:`Cikepeercorrtable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikepeercorrtable>`
    
    .. attribute:: cikephase1gwstatstable
    
    	Phase\-1 IKE stats information is included in this table. Each entry is related to a specific gateway which is  identified by 'cmgwIndex'
    	**type**\:  :py:class:`Cikephase1Gwstatstable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikephase1Gwstatstable>`
    
    .. attribute:: cipsectunneltable
    
    	The IPsec Phase\-2 Tunnel Table. There is one entry in this table for  each active IPsec Phase\-2 Tunnel
    	**type**\:  :py:class:`Cipsectunneltable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsectunneltable>`
    
    .. attribute:: cipsecendpttable
    
    	The IPsec Phase\-2 Tunnel Endpoint Table. This table contains an entry for each  active endpoint associated with an IPsec  Phase\-2 Tunnel
    	**type**\:  :py:class:`Cipsecendpttable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecendpttable>`
    
    .. attribute:: cipsecspitable
    
    	The IPsec Phase\-2 Security Protection Index Table. This table contains an entry for each active  and expiring security  association
    	**type**\:  :py:class:`Cipsecspitable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecspitable>`
    
    .. attribute:: cipsecphase2gwstatstable
    
    	Phase\-2 IPsec stats information is included in this table. Each entry is related to a specific gateway which is  identified by 'cmgwIndex'
    	**type**\:  :py:class:`Cipsecphase2Gwstatstable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecphase2Gwstatstable>`
    
    .. attribute:: ciketunnelhisttable
    
    	The IPsec Phase\-1 Internet Key Exchange Tunnel History Table.  This table is implemented as a  sliding window in which only the last n entries  are maintained.  The maximum number of entries  is specified by the cipSecHistTableSize object
    	**type**\:  :py:class:`Ciketunnelhisttable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable>`
    
    .. attribute:: cipsectunnelhisttable
    
    	The IPsec Phase\-2 Tunnel History Table. This table is implemented as a sliding  window in which only the last n entries are maintained.  The maximum number  of entries is specified by the cipSecHistTableSize object
    	**type**\:  :py:class:`Cipsectunnelhisttable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable>`
    
    .. attribute:: cipsecendpthisttable
    
    	The IPsec Phase\-2 Tunnel Endpoint History Table. This table is implemented as a  sliding window in which only the last n entries are maintained.   The maximum number of entries is specified by the cipSecHistTableSize object
    	**type**\:  :py:class:`Cipsecendpthisttable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable>`
    
    .. attribute:: cikefailtable
    
    	The IPsec Phase\-1 Failure Table. This table is implemented as a sliding  window in which only the last n entries are  maintained.  The maximum number of entries is specified by the cipSecFailTableSize object
    	**type**\:  :py:class:`Cikefailtable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikefailtable>`
    
    .. attribute:: cipsecfailtable
    
    	The IPsec Phase\-2 Failure Table. This table is implemented as a sliding window  in which only the last n entries are maintained.   The maximum number of entries is specified by the cipSecFailTableSize object
    	**type**\:  :py:class:`Cipsecfailtable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecfailtable>`
    
    

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
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cipSecLevels", ("cipseclevels", CISCOIPSECFLOWMONITORMIB.Cipseclevels)), ("cikeGlobalStats", ("cikeglobalstats", CISCOIPSECFLOWMONITORMIB.Cikeglobalstats)), ("cipSecGlobalStats", ("cipsecglobalstats", CISCOIPSECFLOWMONITORMIB.Cipsecglobalstats)), ("cipSecHistGlobalCntl", ("cipsechistglobalcntl", CISCOIPSECFLOWMONITORMIB.Cipsechistglobalcntl)), ("cipSecFailGlobalCntl", ("cipsecfailglobalcntl", CISCOIPSECFLOWMONITORMIB.Cipsecfailglobalcntl)), ("cipSecTrapCntl", ("cipsectrapcntl", CISCOIPSECFLOWMONITORMIB.Cipsectrapcntl)), ("cikePeerTable", ("cikepeertable", CISCOIPSECFLOWMONITORMIB.Cikepeertable)), ("cikeTunnelTable", ("ciketunneltable", CISCOIPSECFLOWMONITORMIB.Ciketunneltable)), ("cikePeerCorrTable", ("cikepeercorrtable", CISCOIPSECFLOWMONITORMIB.Cikepeercorrtable)), ("cikePhase1GWStatsTable", ("cikephase1gwstatstable", CISCOIPSECFLOWMONITORMIB.Cikephase1Gwstatstable)), ("cipSecTunnelTable", ("cipsectunneltable", CISCOIPSECFLOWMONITORMIB.Cipsectunneltable)), ("cipSecEndPtTable", ("cipsecendpttable", CISCOIPSECFLOWMONITORMIB.Cipsecendpttable)), ("cipSecSpiTable", ("cipsecspitable", CISCOIPSECFLOWMONITORMIB.Cipsecspitable)), ("cipSecPhase2GWStatsTable", ("cipsecphase2gwstatstable", CISCOIPSECFLOWMONITORMIB.Cipsecphase2Gwstatstable)), ("cikeTunnelHistTable", ("ciketunnelhisttable", CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable)), ("cipSecTunnelHistTable", ("cipsectunnelhisttable", CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable)), ("cipSecEndPtHistTable", ("cipsecendpthisttable", CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable)), ("cikeFailTable", ("cikefailtable", CISCOIPSECFLOWMONITORMIB.Cikefailtable)), ("cipSecFailTable", ("cipsecfailtable", CISCOIPSECFLOWMONITORMIB.Cipsecfailtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cipseclevels = CISCOIPSECFLOWMONITORMIB.Cipseclevels()
        self.cipseclevels.parent = self
        self._children_name_map["cipseclevels"] = "cipSecLevels"
        self._children_yang_names.add("cipSecLevels")

        self.cikeglobalstats = CISCOIPSECFLOWMONITORMIB.Cikeglobalstats()
        self.cikeglobalstats.parent = self
        self._children_name_map["cikeglobalstats"] = "cikeGlobalStats"
        self._children_yang_names.add("cikeGlobalStats")

        self.cipsecglobalstats = CISCOIPSECFLOWMONITORMIB.Cipsecglobalstats()
        self.cipsecglobalstats.parent = self
        self._children_name_map["cipsecglobalstats"] = "cipSecGlobalStats"
        self._children_yang_names.add("cipSecGlobalStats")

        self.cipsechistglobalcntl = CISCOIPSECFLOWMONITORMIB.Cipsechistglobalcntl()
        self.cipsechistglobalcntl.parent = self
        self._children_name_map["cipsechistglobalcntl"] = "cipSecHistGlobalCntl"
        self._children_yang_names.add("cipSecHistGlobalCntl")

        self.cipsecfailglobalcntl = CISCOIPSECFLOWMONITORMIB.Cipsecfailglobalcntl()
        self.cipsecfailglobalcntl.parent = self
        self._children_name_map["cipsecfailglobalcntl"] = "cipSecFailGlobalCntl"
        self._children_yang_names.add("cipSecFailGlobalCntl")

        self.cipsectrapcntl = CISCOIPSECFLOWMONITORMIB.Cipsectrapcntl()
        self.cipsectrapcntl.parent = self
        self._children_name_map["cipsectrapcntl"] = "cipSecTrapCntl"
        self._children_yang_names.add("cipSecTrapCntl")

        self.cikepeertable = CISCOIPSECFLOWMONITORMIB.Cikepeertable()
        self.cikepeertable.parent = self
        self._children_name_map["cikepeertable"] = "cikePeerTable"
        self._children_yang_names.add("cikePeerTable")

        self.ciketunneltable = CISCOIPSECFLOWMONITORMIB.Ciketunneltable()
        self.ciketunneltable.parent = self
        self._children_name_map["ciketunneltable"] = "cikeTunnelTable"
        self._children_yang_names.add("cikeTunnelTable")

        self.cikepeercorrtable = CISCOIPSECFLOWMONITORMIB.Cikepeercorrtable()
        self.cikepeercorrtable.parent = self
        self._children_name_map["cikepeercorrtable"] = "cikePeerCorrTable"
        self._children_yang_names.add("cikePeerCorrTable")

        self.cikephase1gwstatstable = CISCOIPSECFLOWMONITORMIB.Cikephase1Gwstatstable()
        self.cikephase1gwstatstable.parent = self
        self._children_name_map["cikephase1gwstatstable"] = "cikePhase1GWStatsTable"
        self._children_yang_names.add("cikePhase1GWStatsTable")

        self.cipsectunneltable = CISCOIPSECFLOWMONITORMIB.Cipsectunneltable()
        self.cipsectunneltable.parent = self
        self._children_name_map["cipsectunneltable"] = "cipSecTunnelTable"
        self._children_yang_names.add("cipSecTunnelTable")

        self.cipsecendpttable = CISCOIPSECFLOWMONITORMIB.Cipsecendpttable()
        self.cipsecendpttable.parent = self
        self._children_name_map["cipsecendpttable"] = "cipSecEndPtTable"
        self._children_yang_names.add("cipSecEndPtTable")

        self.cipsecspitable = CISCOIPSECFLOWMONITORMIB.Cipsecspitable()
        self.cipsecspitable.parent = self
        self._children_name_map["cipsecspitable"] = "cipSecSpiTable"
        self._children_yang_names.add("cipSecSpiTable")

        self.cipsecphase2gwstatstable = CISCOIPSECFLOWMONITORMIB.Cipsecphase2Gwstatstable()
        self.cipsecphase2gwstatstable.parent = self
        self._children_name_map["cipsecphase2gwstatstable"] = "cipSecPhase2GWStatsTable"
        self._children_yang_names.add("cipSecPhase2GWStatsTable")

        self.ciketunnelhisttable = CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable()
        self.ciketunnelhisttable.parent = self
        self._children_name_map["ciketunnelhisttable"] = "cikeTunnelHistTable"
        self._children_yang_names.add("cikeTunnelHistTable")

        self.cipsectunnelhisttable = CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable()
        self.cipsectunnelhisttable.parent = self
        self._children_name_map["cipsectunnelhisttable"] = "cipSecTunnelHistTable"
        self._children_yang_names.add("cipSecTunnelHistTable")

        self.cipsecendpthisttable = CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable()
        self.cipsecendpthisttable.parent = self
        self._children_name_map["cipsecendpthisttable"] = "cipSecEndPtHistTable"
        self._children_yang_names.add("cipSecEndPtHistTable")

        self.cikefailtable = CISCOIPSECFLOWMONITORMIB.Cikefailtable()
        self.cikefailtable.parent = self
        self._children_name_map["cikefailtable"] = "cikeFailTable"
        self._children_yang_names.add("cikeFailTable")

        self.cipsecfailtable = CISCOIPSECFLOWMONITORMIB.Cipsecfailtable()
        self.cipsecfailtable.parent = self
        self._children_name_map["cipsecfailtable"] = "cipSecFailTable"
        self._children_yang_names.add("cipSecFailTable")
        self._segment_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB"


    class Cipseclevels(Entity):
        """
        
        
        .. attribute:: cipsecmiblevel
        
        	The level of the IPsec MIB
        	**type**\: int
        
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
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cipsecmiblevel', YLeaf(YType.int32, 'cipSecMibLevel')),
            ])
            self.cipsecmiblevel = None
            self._segment_path = lambda: "cipSecLevels"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipseclevels, ['cipsecmiblevel'], name, value)


    class Cikeglobalstats(Entity):
        """
        
        
        .. attribute:: cikeglobalactivetunnels
        
        	The number of currently active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cikeglobalprevioustunnels
        
        	The total number of previously active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: SAs
        
        .. attribute:: cikeglobalinoctets
        
        	The total number of octets received by all currently and previously active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Octets
        
        .. attribute:: cikeglobalinpkts
        
        	The total number of packets received by all currently and previously active IPsec  Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cikeglobalindroppkts
        
        	The total number of packets which were dropped during receive processing by all  currently and previously  active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cikeglobalinnotifys
        
        	The total number of notifys received by all currently and previously active IPsec  Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Notification Payloads
        
        .. attribute:: cikeglobalinp2exchgs
        
        	The total number of IPsec Phase\-2 exchanges received by all currently and previously  active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: SA Payloads
        
        .. attribute:: cikeglobalinp2exchginvalids
        
        	The total number of IPsec Phase\-2 exchanges which were received and found to be invalid  by all currently and previously active IPsec  Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: SA Payloads
        
        .. attribute:: cikeglobalinp2exchgrejects
        
        	The total number of IPsec Phase\-2 exchanges which were received and rejected by all  currently and previously active IPsec Phase\-1  IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: SA Payloads
        
        .. attribute:: cikeglobalinp2sadelrequests
        
        	The total number of IPsec Phase\-2 security association delete requests received by all  currently and previously  active and IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Notification Payloads
        
        .. attribute:: cikeglobaloutoctets
        
        	The total number of octets sent by all currently and previously active and IPsec Phase\-1  IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Octets
        
        .. attribute:: cikeglobaloutpkts
        
        	The total number of packets sent by all currently and previously active and IPsec Phase\-1  Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cikeglobaloutdroppkts
        
        	The total number of packets which were dropped during send processing by all currently  and previously  active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cikeglobaloutnotifys
        
        	The total number of notifys sent by all currently and previously active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Notification Payloads
        
        .. attribute:: cikeglobaloutp2exchgs
        
        	The total number of IPsec Phase\-2 exchanges which were sent by all currently and previously  active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: SA Payloads
        
        .. attribute:: cikeglobaloutp2exchginvalids
        
        	The total number of IPsec Phase\-2 exchanges which were sent and found to be invalid by  all currently and previously active IPsec Phase\-1  Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: SA Payloads
        
        .. attribute:: cikeglobaloutp2exchgrejects
        
        	The total number of IPsec Phase\-2 exchanges which were sent and rejected by all currently and  previously active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: SA Payloads
        
        .. attribute:: cikeglobaloutp2sadelrequests
        
        	The total number of IPsec Phase\-2 SA delete requests sent by all currently and  previously active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Notification Payloads
        
        .. attribute:: cikeglobalinittunnels
        
        	The total number of IPsec Phase\-1 IKE Tunnels which were locally initiated
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: SAs
        
        .. attribute:: cikeglobalinittunnelfails
        
        	The total number of IPsec Phase\-1 IKE Tunnels which were locally initiated and failed to activate
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: SAs
        
        .. attribute:: cikeglobalresptunnelfails
        
        	The total number of IPsec Phase\-1 IKE Tunnels which were remotely initiated and failed to activate
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: SAs
        
        .. attribute:: cikeglobalsyscapfails
        
        	The total number of system capacity failures which occurred during processing of all current  and previously active IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cikeglobalauthfails
        
        	The total number of authentications which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cikeglobaldecryptfails
        
        	The total number of decryptions which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cikeglobalhashvalidfails
        
        	The total number of hash validations which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cikeglobalnosafails
        
        	The total number of non\-existent Security Association in failures which occurred during processing of  all current and previous IPsec Phase\-1 IKE Tunnels
        	**type**\: int
        
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
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cikeglobalactivetunnels', YLeaf(YType.uint32, 'cikeGlobalActiveTunnels')),
                ('cikeglobalprevioustunnels', YLeaf(YType.uint32, 'cikeGlobalPreviousTunnels')),
                ('cikeglobalinoctets', YLeaf(YType.uint32, 'cikeGlobalInOctets')),
                ('cikeglobalinpkts', YLeaf(YType.uint32, 'cikeGlobalInPkts')),
                ('cikeglobalindroppkts', YLeaf(YType.uint32, 'cikeGlobalInDropPkts')),
                ('cikeglobalinnotifys', YLeaf(YType.uint32, 'cikeGlobalInNotifys')),
                ('cikeglobalinp2exchgs', YLeaf(YType.uint32, 'cikeGlobalInP2Exchgs')),
                ('cikeglobalinp2exchginvalids', YLeaf(YType.uint32, 'cikeGlobalInP2ExchgInvalids')),
                ('cikeglobalinp2exchgrejects', YLeaf(YType.uint32, 'cikeGlobalInP2ExchgRejects')),
                ('cikeglobalinp2sadelrequests', YLeaf(YType.uint32, 'cikeGlobalInP2SaDelRequests')),
                ('cikeglobaloutoctets', YLeaf(YType.uint32, 'cikeGlobalOutOctets')),
                ('cikeglobaloutpkts', YLeaf(YType.uint32, 'cikeGlobalOutPkts')),
                ('cikeglobaloutdroppkts', YLeaf(YType.uint32, 'cikeGlobalOutDropPkts')),
                ('cikeglobaloutnotifys', YLeaf(YType.uint32, 'cikeGlobalOutNotifys')),
                ('cikeglobaloutp2exchgs', YLeaf(YType.uint32, 'cikeGlobalOutP2Exchgs')),
                ('cikeglobaloutp2exchginvalids', YLeaf(YType.uint32, 'cikeGlobalOutP2ExchgInvalids')),
                ('cikeglobaloutp2exchgrejects', YLeaf(YType.uint32, 'cikeGlobalOutP2ExchgRejects')),
                ('cikeglobaloutp2sadelrequests', YLeaf(YType.uint32, 'cikeGlobalOutP2SaDelRequests')),
                ('cikeglobalinittunnels', YLeaf(YType.uint32, 'cikeGlobalInitTunnels')),
                ('cikeglobalinittunnelfails', YLeaf(YType.uint32, 'cikeGlobalInitTunnelFails')),
                ('cikeglobalresptunnelfails', YLeaf(YType.uint32, 'cikeGlobalRespTunnelFails')),
                ('cikeglobalsyscapfails', YLeaf(YType.uint32, 'cikeGlobalSysCapFails')),
                ('cikeglobalauthfails', YLeaf(YType.uint32, 'cikeGlobalAuthFails')),
                ('cikeglobaldecryptfails', YLeaf(YType.uint32, 'cikeGlobalDecryptFails')),
                ('cikeglobalhashvalidfails', YLeaf(YType.uint32, 'cikeGlobalHashValidFails')),
                ('cikeglobalnosafails', YLeaf(YType.uint32, 'cikeGlobalNoSaFails')),
            ])
            self.cikeglobalactivetunnels = None
            self.cikeglobalprevioustunnels = None
            self.cikeglobalinoctets = None
            self.cikeglobalinpkts = None
            self.cikeglobalindroppkts = None
            self.cikeglobalinnotifys = None
            self.cikeglobalinp2exchgs = None
            self.cikeglobalinp2exchginvalids = None
            self.cikeglobalinp2exchgrejects = None
            self.cikeglobalinp2sadelrequests = None
            self.cikeglobaloutoctets = None
            self.cikeglobaloutpkts = None
            self.cikeglobaloutdroppkts = None
            self.cikeglobaloutnotifys = None
            self.cikeglobaloutp2exchgs = None
            self.cikeglobaloutp2exchginvalids = None
            self.cikeglobaloutp2exchgrejects = None
            self.cikeglobaloutp2sadelrequests = None
            self.cikeglobalinittunnels = None
            self.cikeglobalinittunnelfails = None
            self.cikeglobalresptunnelfails = None
            self.cikeglobalsyscapfails = None
            self.cikeglobalauthfails = None
            self.cikeglobaldecryptfails = None
            self.cikeglobalhashvalidfails = None
            self.cikeglobalnosafails = None
            self._segment_path = lambda: "cikeGlobalStats"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cikeglobalstats, ['cikeglobalactivetunnels', 'cikeglobalprevioustunnels', 'cikeglobalinoctets', 'cikeglobalinpkts', 'cikeglobalindroppkts', 'cikeglobalinnotifys', 'cikeglobalinp2exchgs', 'cikeglobalinp2exchginvalids', 'cikeglobalinp2exchgrejects', 'cikeglobalinp2sadelrequests', 'cikeglobaloutoctets', 'cikeglobaloutpkts', 'cikeglobaloutdroppkts', 'cikeglobaloutnotifys', 'cikeglobaloutp2exchgs', 'cikeglobaloutp2exchginvalids', 'cikeglobaloutp2exchgrejects', 'cikeglobaloutp2sadelrequests', 'cikeglobalinittunnels', 'cikeglobalinittunnelfails', 'cikeglobalresptunnelfails', 'cikeglobalsyscapfails', 'cikeglobalauthfails', 'cikeglobaldecryptfails', 'cikeglobalhashvalidfails', 'cikeglobalnosafails'], name, value)


    class Cipsecglobalstats(Entity):
        """
        
        
        .. attribute:: cipsecglobalactivetunnels
        
        	The total number of currently active IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsecglobalprevioustunnels
        
        	The total number of previously active IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Phase-2 Tunnels
        
        .. attribute:: cipsecglobalinoctets
        
        	The total number of octets received by all current and previous IPsec Phase\-2 Tunnels.  This value is accumulated BEFORE determining whether or not the packet should be decompressed. See also cipSecGlobalInOctWraps for the number of times this counter has wrapped
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Octets
        
        .. attribute:: cipsecglobalhcinoctets
        
        	A high capacity count of the total number of octets received by all current and previous IPsec Phase\-2 Tunnels. This value is accumulated BEFORE determining whether or not the packet should be decompressed
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: cipsecglobalinoctwraps
        
        	The number of times the global octets received counter (cipSecGlobalInOctets) has wrapped
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Integral units
        
        .. attribute:: cipsecglobalindecompoctets
        
        	The total number of decompressed octets received by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated AFTER the packet is  decompressed. If compression is not being used,  this value will match the value of cipSecGlobalInOctets.  See also cipSecGlobalInDecompOctWraps  for the number of times this counter has wrapped
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Octets
        
        .. attribute:: cipsecglobalhcindecompoctets
        
        	A high capacity count of the total number of decompressed octets received by all current  and previous IPsec Phase\-2 Tunnels.  This value  is accumulated AFTER the packet is decompressed.  If compression is not being used, this value   will match the value of cipSecGlobalHcInOctets
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: cipsecglobalindecompoctwraps
        
        	The number of times the global decompressed octets received counter  (cipSecGlobalInDecompOctets) has wrapped
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Integral units
        
        .. attribute:: cipsecglobalinpkts
        
        	The total number of packets received by all current and previous  IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cipsecglobalindrops
        
        	The total number of packets dropped during receive processing by all current and previous  IPsec Phase\-2 Tunnels. This count does NOT include packets dropped due to  Anti\-Replay processing
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cipsecglobalinreplaydrops
        
        	The total number of packets dropped during receive processing due to Anti\-Replay  processing by all current and previous IPsec  Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cipsecglobalinauths
        
        	The total number of inbound authentication's performed by all current and previous IPsec  Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Events
        
        .. attribute:: cipsecglobalinauthfails
        
        	The total number of inbound authentication's which ended in failure by all current and previous  IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cipsecglobalindecrypts
        
        	The total number of inbound decryption's performed by all current and previous IPsec  Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cipsecglobalindecryptfails
        
        	The total number of inbound decryption's which ended in failure by all current and  previous IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cipsecglobaloutoctets
        
        	The total number of octets sent by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated AFTER determining  whether or not the packet should be compressed.   See also cipSecGlobalOutOctWraps for the  number of times this counter has wrapped
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Octets
        
        .. attribute:: cipsecglobalhcoutoctets
        
        	A high capacity count of the total number of octets sent by all current and previous  IPsec Phase\-2 Tunnels.  This value is accumulated  AFTER determining whether or not the packet should  be compressed
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: cipsecglobaloutoctwraps
        
        	The number of times the global octets sent counter (cipSecGlobalOutOctets) has wrapped
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Integral units
        
        .. attribute:: cipsecglobaloutuncompoctets
        
        	The total number of uncompressed octets sent by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated BEFORE the packet is  compressed. If compression is not being used, this  value will match the value of cipSecGlobalOutOctets.  See also cipSecGlobalOutDecompOctWraps for the number  of times this counter has wrapped
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Octets
        
        .. attribute:: cipsecglobalhcoutuncompoctets
        
        	A high capacity count of the total number of uncompressed octets sent by all current and previous  IPsec Phase\-2 Tunnels.  This value is accumulated  BEFORE the packet is compressed.  If compression is  not being used, this value will match the       value of cipSecGlobalHcOutOctets
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: Octets
        
        .. attribute:: cipsecglobaloutuncompoctwraps
        
        	The number of times the global uncompressed octets sent counter (cipSecGlobalOutUncompOctets)  has wrapped
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Integral units
        
        .. attribute:: cipsecglobaloutpkts
        
        	The total number of packets sent by all current and previous  IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cipsecglobaloutdrops
        
        	The total number of packets dropped during send processing by all current and previous IPsec  Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cipsecglobaloutauths
        
        	The total number of outbound authentication's performed by all current and previous IPsec  Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Events
        
        .. attribute:: cipsecglobaloutauthfails
        
        	The total number of outbound authentication's which ended in failure  by all current and previous IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cipsecglobaloutencrypts
        
        	The total number of outbound encryption's performed by all current and previous IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Packets
        
        .. attribute:: cipsecglobaloutencryptfails
        
        	The total number of outbound encryption's which ended in failure by all current and  previous IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cipsecglobalprotocolusefails
        
        	The total number of protocol use failures which occurred during processing of all current  and previously active IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cipsecglobalnosafails
        
        	The total number of non\-existent Security Association in failures which occurred  during processing of all current  and previous IPsec Phase\-2 Tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Failures
        
        .. attribute:: cipsecglobalsyscapfails
        
        	The total number of system capacity failures which occurred during processing of all current  and previously active IPsec Phase\-2 Tunnels
        	**type**\: int
        
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
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cipsecglobalactivetunnels', YLeaf(YType.uint32, 'cipSecGlobalActiveTunnels')),
                ('cipsecglobalprevioustunnels', YLeaf(YType.uint32, 'cipSecGlobalPreviousTunnels')),
                ('cipsecglobalinoctets', YLeaf(YType.uint32, 'cipSecGlobalInOctets')),
                ('cipsecglobalhcinoctets', YLeaf(YType.uint64, 'cipSecGlobalHcInOctets')),
                ('cipsecglobalinoctwraps', YLeaf(YType.uint32, 'cipSecGlobalInOctWraps')),
                ('cipsecglobalindecompoctets', YLeaf(YType.uint32, 'cipSecGlobalInDecompOctets')),
                ('cipsecglobalhcindecompoctets', YLeaf(YType.uint64, 'cipSecGlobalHcInDecompOctets')),
                ('cipsecglobalindecompoctwraps', YLeaf(YType.uint32, 'cipSecGlobalInDecompOctWraps')),
                ('cipsecglobalinpkts', YLeaf(YType.uint32, 'cipSecGlobalInPkts')),
                ('cipsecglobalindrops', YLeaf(YType.uint32, 'cipSecGlobalInDrops')),
                ('cipsecglobalinreplaydrops', YLeaf(YType.uint32, 'cipSecGlobalInReplayDrops')),
                ('cipsecglobalinauths', YLeaf(YType.uint32, 'cipSecGlobalInAuths')),
                ('cipsecglobalinauthfails', YLeaf(YType.uint32, 'cipSecGlobalInAuthFails')),
                ('cipsecglobalindecrypts', YLeaf(YType.uint32, 'cipSecGlobalInDecrypts')),
                ('cipsecglobalindecryptfails', YLeaf(YType.uint32, 'cipSecGlobalInDecryptFails')),
                ('cipsecglobaloutoctets', YLeaf(YType.uint32, 'cipSecGlobalOutOctets')),
                ('cipsecglobalhcoutoctets', YLeaf(YType.uint64, 'cipSecGlobalHcOutOctets')),
                ('cipsecglobaloutoctwraps', YLeaf(YType.uint32, 'cipSecGlobalOutOctWraps')),
                ('cipsecglobaloutuncompoctets', YLeaf(YType.uint32, 'cipSecGlobalOutUncompOctets')),
                ('cipsecglobalhcoutuncompoctets', YLeaf(YType.uint64, 'cipSecGlobalHcOutUncompOctets')),
                ('cipsecglobaloutuncompoctwraps', YLeaf(YType.uint32, 'cipSecGlobalOutUncompOctWraps')),
                ('cipsecglobaloutpkts', YLeaf(YType.uint32, 'cipSecGlobalOutPkts')),
                ('cipsecglobaloutdrops', YLeaf(YType.uint32, 'cipSecGlobalOutDrops')),
                ('cipsecglobaloutauths', YLeaf(YType.uint32, 'cipSecGlobalOutAuths')),
                ('cipsecglobaloutauthfails', YLeaf(YType.uint32, 'cipSecGlobalOutAuthFails')),
                ('cipsecglobaloutencrypts', YLeaf(YType.uint32, 'cipSecGlobalOutEncrypts')),
                ('cipsecglobaloutencryptfails', YLeaf(YType.uint32, 'cipSecGlobalOutEncryptFails')),
                ('cipsecglobalprotocolusefails', YLeaf(YType.uint32, 'cipSecGlobalProtocolUseFails')),
                ('cipsecglobalnosafails', YLeaf(YType.uint32, 'cipSecGlobalNoSaFails')),
                ('cipsecglobalsyscapfails', YLeaf(YType.uint32, 'cipSecGlobalSysCapFails')),
            ])
            self.cipsecglobalactivetunnels = None
            self.cipsecglobalprevioustunnels = None
            self.cipsecglobalinoctets = None
            self.cipsecglobalhcinoctets = None
            self.cipsecglobalinoctwraps = None
            self.cipsecglobalindecompoctets = None
            self.cipsecglobalhcindecompoctets = None
            self.cipsecglobalindecompoctwraps = None
            self.cipsecglobalinpkts = None
            self.cipsecglobalindrops = None
            self.cipsecglobalinreplaydrops = None
            self.cipsecglobalinauths = None
            self.cipsecglobalinauthfails = None
            self.cipsecglobalindecrypts = None
            self.cipsecglobalindecryptfails = None
            self.cipsecglobaloutoctets = None
            self.cipsecglobalhcoutoctets = None
            self.cipsecglobaloutoctwraps = None
            self.cipsecglobaloutuncompoctets = None
            self.cipsecglobalhcoutuncompoctets = None
            self.cipsecglobaloutuncompoctwraps = None
            self.cipsecglobaloutpkts = None
            self.cipsecglobaloutdrops = None
            self.cipsecglobaloutauths = None
            self.cipsecglobaloutauthfails = None
            self.cipsecglobaloutencrypts = None
            self.cipsecglobaloutencryptfails = None
            self.cipsecglobalprotocolusefails = None
            self.cipsecglobalnosafails = None
            self.cipsecglobalsyscapfails = None
            self._segment_path = lambda: "cipSecGlobalStats"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecglobalstats, ['cipsecglobalactivetunnels', 'cipsecglobalprevioustunnels', 'cipsecglobalinoctets', 'cipsecglobalhcinoctets', 'cipsecglobalinoctwraps', 'cipsecglobalindecompoctets', 'cipsecglobalhcindecompoctets', 'cipsecglobalindecompoctwraps', 'cipsecglobalinpkts', 'cipsecglobalindrops', 'cipsecglobalinreplaydrops', 'cipsecglobalinauths', 'cipsecglobalinauthfails', 'cipsecglobalindecrypts', 'cipsecglobalindecryptfails', 'cipsecglobaloutoctets', 'cipsecglobalhcoutoctets', 'cipsecglobaloutoctwraps', 'cipsecglobaloutuncompoctets', 'cipsecglobalhcoutuncompoctets', 'cipsecglobaloutuncompoctwraps', 'cipsecglobaloutpkts', 'cipsecglobaloutdrops', 'cipsecglobaloutauths', 'cipsecglobaloutauthfails', 'cipsecglobaloutencrypts', 'cipsecglobaloutencryptfails', 'cipsecglobalprotocolusefails', 'cipsecglobalnosafails', 'cipsecglobalsyscapfails'], name, value)


    class Cipsechistglobalcntl(Entity):
        """
        
        
        .. attribute:: cipsechisttablesize
        
        	The window size of the IPsec Phase\-1 and Phase\-2 History Tables.  The IPsec Phase\-1 and Phase\-2 History Tables are implemented as a sliding window in which only the last n entries are maintained.  This object is used specify the number of entries which will be  maintained in the IPsec Phase\-1 and  Phase\-2 History Tables.  An implementation may choose suitable minimum and  maximum values for this element based on the local  policy and available resources. If an SNMP SET request  specifies a value outside this window for this element,  a BAD VALUE may be returned
        	**type**\: int
        
        	**range:** 1..2147483647
        
        .. attribute:: cipsechistcheckpoint
        
        	The current state of check point processing.  This object will return ready when the agent is  ready to create on\-demand history entries for  active IPsec Tunnels or checkPoint when the  agent is currently creating on\-demand history  entries for active IPsec Tunnels.  By setting this value to checkPoint, the agent  will create\: a) an entry in the IPsec Phase\-1 Tunnel History     for each active IPsec Phase\-1 Tunnel and b) an entry in the IPsec Phase\-2 Tunnel History     Table and an entry in the IPsec Phase\-2     Tunnel EndPoint History Table    for each active IPsec Phase\-2 Tunnel
        	**type**\:  :py:class:`Cipsechistcheckpoint <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsechistglobalcntl.Cipsechistcheckpoint>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsechistglobalcntl, self).__init__()

            self.yang_name = "cipSecHistGlobalCntl"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cipsechisttablesize', YLeaf(YType.int32, 'cipSecHistTableSize')),
                ('cipsechistcheckpoint', YLeaf(YType.enumeration, 'cipSecHistCheckPoint')),
            ])
            self.cipsechisttablesize = None
            self.cipsechistcheckpoint = None
            self._segment_path = lambda: "cipSecHistGlobalCntl"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsechistglobalcntl, ['cipsechisttablesize', 'cipsechistcheckpoint'], name, value)

        class Cipsechistcheckpoint(Enum):
            """
            Cipsechistcheckpoint (Enum Class)

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



    class Cipsecfailglobalcntl(Entity):
        """
        
        
        .. attribute:: cipsecfailtablesize
        
        	The window size of the IPsec Phase\-1 and Phase\-2 Failure Tables.  The IPsec Phase\-1 and Phase\-2 Failure Tables are implemented as a sliding window in which only the last n entries are maintained.  This object is used specify the number of entries which will be  maintained in the IPsec Phase\-1 and Phase\-2 Failure  Tables.  An implementation may choose suitable minimum and  maximum values for this element based on the local  policy and available resources. If an SNMP SET request  specifies a value outside this window for this element,  a BAD VALUE may be returned
        	**type**\: int
        
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
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cipsecfailtablesize', YLeaf(YType.int32, 'cipSecFailTableSize')),
            ])
            self.cipsecfailtablesize = None
            self._segment_path = lambda: "cipSecFailGlobalCntl"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecfailglobalcntl, ['cipsecfailtablesize'], name, value)


    class Cipsectrapcntl(Entity):
        """
        
        
        .. attribute:: cipsectrapcntliketunnelstart
        
        	This object defines the administrative state of sending the IPsec IKE Phase\-1 Tunnel Start TRAP
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntliketunnelstop
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 Tunnel Stop TRAP
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlikesysfailure
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 System Failure TRAP
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlikecertcrlfailure
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 Certificate/CRL Failure TRAP
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlikeprotocolfail
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 Protocol Failure TRAP
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlikenosa
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 No Security Association TRAP
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlipsectunnelstart
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Tunnel Start TRAP
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlipsectunnelstop
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Tunnel Stop TRAP
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlipsecsysfailure
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 System Failure TRAP
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlipsecsetupfailure
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Set Up Failure TRAP
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlipsecearlytunterm
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Early Tunnel Termination TRAP
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlipsecprotocolfail
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Protocol Failure TRAP
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        .. attribute:: cipsectrapcntlipsecnosa
        
        	This object defines the administrative state of sending the IPsec  Phase\-2  No Security Association TRAP
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapStatus>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsectrapcntl, self).__init__()

            self.yang_name = "cipSecTrapCntl"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cipsectrapcntliketunnelstart', YLeaf(YType.enumeration, 'cipSecTrapCntlIkeTunnelStart')),
                ('cipsectrapcntliketunnelstop', YLeaf(YType.enumeration, 'cipSecTrapCntlIkeTunnelStop')),
                ('cipsectrapcntlikesysfailure', YLeaf(YType.enumeration, 'cipSecTrapCntlIkeSysFailure')),
                ('cipsectrapcntlikecertcrlfailure', YLeaf(YType.enumeration, 'cipSecTrapCntlIkeCertCrlFailure')),
                ('cipsectrapcntlikeprotocolfail', YLeaf(YType.enumeration, 'cipSecTrapCntlIkeProtocolFail')),
                ('cipsectrapcntlikenosa', YLeaf(YType.enumeration, 'cipSecTrapCntlIkeNoSa')),
                ('cipsectrapcntlipsectunnelstart', YLeaf(YType.enumeration, 'cipSecTrapCntlIpSecTunnelStart')),
                ('cipsectrapcntlipsectunnelstop', YLeaf(YType.enumeration, 'cipSecTrapCntlIpSecTunnelStop')),
                ('cipsectrapcntlipsecsysfailure', YLeaf(YType.enumeration, 'cipSecTrapCntlIpSecSysFailure')),
                ('cipsectrapcntlipsecsetupfailure', YLeaf(YType.enumeration, 'cipSecTrapCntlIpSecSetUpFailure')),
                ('cipsectrapcntlipsecearlytunterm', YLeaf(YType.enumeration, 'cipSecTrapCntlIpSecEarlyTunTerm')),
                ('cipsectrapcntlipsecprotocolfail', YLeaf(YType.enumeration, 'cipSecTrapCntlIpSecProtocolFail')),
                ('cipsectrapcntlipsecnosa', YLeaf(YType.enumeration, 'cipSecTrapCntlIpSecNoSa')),
            ])
            self.cipsectrapcntliketunnelstart = None
            self.cipsectrapcntliketunnelstop = None
            self.cipsectrapcntlikesysfailure = None
            self.cipsectrapcntlikecertcrlfailure = None
            self.cipsectrapcntlikeprotocolfail = None
            self.cipsectrapcntlikenosa = None
            self.cipsectrapcntlipsectunnelstart = None
            self.cipsectrapcntlipsectunnelstop = None
            self.cipsectrapcntlipsecsysfailure = None
            self.cipsectrapcntlipsecsetupfailure = None
            self.cipsectrapcntlipsecearlytunterm = None
            self.cipsectrapcntlipsecprotocolfail = None
            self.cipsectrapcntlipsecnosa = None
            self._segment_path = lambda: "cipSecTrapCntl"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsectrapcntl, ['cipsectrapcntliketunnelstart', 'cipsectrapcntliketunnelstop', 'cipsectrapcntlikesysfailure', 'cipsectrapcntlikecertcrlfailure', 'cipsectrapcntlikeprotocolfail', 'cipsectrapcntlikenosa', 'cipsectrapcntlipsectunnelstart', 'cipsectrapcntlipsectunnelstop', 'cipsectrapcntlipsecsysfailure', 'cipsectrapcntlipsecsetupfailure', 'cipsectrapcntlipsecearlytunterm', 'cipsectrapcntlipsecprotocolfail', 'cipsectrapcntlipsecnosa'], name, value)


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
        	**type**\: list of  		 :py:class:`Cikepeerentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikepeertable.Cikepeerentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cikepeertable, self).__init__()

            self.yang_name = "cikePeerTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cikePeerEntry", ("cikepeerentry", CISCOIPSECFLOWMONITORMIB.Cikepeertable.Cikepeerentry))])
            self._leafs = OrderedDict()

            self.cikepeerentry = YList(self)
            self._segment_path = lambda: "cikePeerTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cikepeertable, [], name, value)


        class Cikepeerentry(Entity):
            """
            Each entry contains the attributes associated
            with an IPsec Phase\-1 IKE peer association.
            
            .. attribute:: cikepeerlocaltype  (key)
            
            	The type of local peer identity.  The local peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\:  :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: cikepeerlocalvalue  (key)
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\: str
            
            .. attribute:: cikepeerremotetype  (key)
            
            	The type of remote peer identity.  The remote peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\:  :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: cikepeerremotevalue  (key)
            
            	The value of the remote peer identity.  If the remote peer type is an IP Address, then this is the IP Address used to identify the remote peer.  If the remote peer type is a host name, then this is the host name used to identify the remote peer
            	**type**\: str
            
            .. attribute:: cikepeerintindex  (key)
            
            	The internal index of the local\-remote peer association.  This internal index is used  to uniquely identify multiple associations between  the local and remote peer
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cikepeerlocaladdr
            
            	The IP address of the local peer
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: cikepeerremoteaddr
            
            	The IP address of the remote peer
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: cikepeeractivetime
            
            	The length of time that the peer association has existed in hundredths of a second
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cikepeeractivetunnelindex
            
            	The index of the active IPsec Phase\-1 IKE Tunnel (cikeTunIndex in the cikeTunnelTable) for this peer association.  If an IPsec Phase\-1 IKE Tunnel is not currently active, then the value of this object will be zero
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cikepeertable.Cikepeerentry, self).__init__()

                self.yang_name = "cikePeerEntry"
                self.yang_parent_name = "cikePeerTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cikepeerlocaltype','cikepeerlocalvalue','cikepeerremotetype','cikepeerremotevalue','cikepeerintindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cikepeerlocaltype', YLeaf(YType.enumeration, 'cikePeerLocalType')),
                    ('cikepeerlocalvalue', YLeaf(YType.str, 'cikePeerLocalValue')),
                    ('cikepeerremotetype', YLeaf(YType.enumeration, 'cikePeerRemoteType')),
                    ('cikepeerremotevalue', YLeaf(YType.str, 'cikePeerRemoteValue')),
                    ('cikepeerintindex', YLeaf(YType.int32, 'cikePeerIntIndex')),
                    ('cikepeerlocaladdr', YLeaf(YType.str, 'cikePeerLocalAddr')),
                    ('cikepeerremoteaddr', YLeaf(YType.str, 'cikePeerRemoteAddr')),
                    ('cikepeeractivetime', YLeaf(YType.int32, 'cikePeerActiveTime')),
                    ('cikepeeractivetunnelindex', YLeaf(YType.int32, 'cikePeerActiveTunnelIndex')),
                ])
                self.cikepeerlocaltype = None
                self.cikepeerlocalvalue = None
                self.cikepeerremotetype = None
                self.cikepeerremotevalue = None
                self.cikepeerintindex = None
                self.cikepeerlocaladdr = None
                self.cikepeerremoteaddr = None
                self.cikepeeractivetime = None
                self.cikepeeractivetunnelindex = None
                self._segment_path = lambda: "cikePeerEntry" + "[cikePeerLocalType='" + str(self.cikepeerlocaltype) + "']" + "[cikePeerLocalValue='" + str(self.cikepeerlocalvalue) + "']" + "[cikePeerRemoteType='" + str(self.cikepeerremotetype) + "']" + "[cikePeerRemoteValue='" + str(self.cikepeerremotevalue) + "']" + "[cikePeerIntIndex='" + str(self.cikepeerintindex) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikePeerTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cikepeertable.Cikepeerentry, ['cikepeerlocaltype', 'cikepeerlocalvalue', 'cikepeerremotetype', 'cikepeerremotevalue', 'cikepeerintindex', 'cikepeerlocaladdr', 'cikepeerremoteaddr', 'cikepeeractivetime', 'cikepeeractivetunnelindex'], name, value)


    class Ciketunneltable(Entity):
        """
        The IPsec Phase\-1 Internet Key Exchange Tunnel Table.
        There is one entry in this table for each active IPsec
        Phase\-1 IKE Tunnel.
        
        .. attribute:: ciketunnelentry
        
        	Each entry contains the attributes associated with an active IPsec Phase\-1 IKE Tunnel
        	**type**\: list of  		 :py:class:`Ciketunnelentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Ciketunneltable.Ciketunnelentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Ciketunneltable, self).__init__()

            self.yang_name = "cikeTunnelTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cikeTunnelEntry", ("ciketunnelentry", CISCOIPSECFLOWMONITORMIB.Ciketunneltable.Ciketunnelentry))])
            self._leafs = OrderedDict()

            self.ciketunnelentry = YList(self)
            self._segment_path = lambda: "cikeTunnelTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Ciketunneltable, [], name, value)


        class Ciketunnelentry(Entity):
            """
            Each entry contains the attributes associated with
            an active IPsec Phase\-1 IKE Tunnel.
            
            .. attribute:: ciketunindex  (key)
            
            	The index of the IPsec Phase\-1 IKE Tunnel Table. The value of the index is a number which begins  at one and is incremented with each tunnel that  is created. The value of this object will  wrap at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciketunlocaltype
            
            	The type of local peer identity.  The local peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\:  :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: ciketunlocalvalue
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\: str
            
            .. attribute:: ciketunlocaladdr
            
            	The IP address of the local endpoint for the IPsec Phase\-1 IKE Tunnel
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: ciketunlocalname
            
            	The DNS name of the local IP address for the IPsec Phase\-1 IKE Tunnel. If the DNS  name associated with the local tunnel endpoint  is not known, then the value of this  object will be a NULL string
            	**type**\: str
            
            .. attribute:: ciketunremotetype
            
            	The type of remote peer identity. The remote peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\:  :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: ciketunremotevalue
            
            	The value of the remote peer identity.  If the remote peer type is an IP Address, then this is the IP Address used to identify the remote peer.  If the remote peer type is a host name, then  this is the host name used to identify the  remote peer
            	**type**\: str
            
            .. attribute:: ciketunremoteaddr
            
            	The IP address of the remote endpoint for the IPsec Phase\-1 IKE Tunnel
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: ciketunremotename
            
            	The DNS name of the remote IP address of IPsec Phase\-1 IKE Tunnel. If the DNS name associated with the remote tunnel endpoint is not known, then the value of this object will be a NULL string
            	**type**\: str
            
            .. attribute:: ciketunnegomode
            
            	The negotiation mode of the IPsec Phase\-1 IKE Tunnel
            	**type**\:  :py:class:`IkeNegoMode <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeNegoMode>`
            
            .. attribute:: ciketundiffhellmangrp
            
            	The Diffie Hellman Group used in IPsec Phase\-1 IKE negotiations
            	**type**\:  :py:class:`DiffHellmanGrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp>`
            
            .. attribute:: ciketunencryptalgo
            
            	The encryption algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\:  :py:class:`EncryptAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo>`
            
            .. attribute:: ciketunhashalgo
            
            	The hash algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\:  :py:class:`IkeHashAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeHashAlgo>`
            
            .. attribute:: ciketunauthmethod
            
            	The authentication method used in IPsec Phase\-1 IKE negotiations
            	**type**\:  :py:class:`IkeAuthMethod <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeAuthMethod>`
            
            .. attribute:: ciketunlifetime
            
            	The negotiated LifeTime of the IPsec Phase\-1 IKE Tunnel in seconds
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ciketunactivetime
            
            	The length of time the IPsec Phase\-1 IKE tunnel has been active in hundredths of seconds
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciketunsarefreshthreshold
            
            	The security association refresh threshold in seconds
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**units**\: seconds
            
            .. attribute:: ciketuntotalrefreshes
            
            	The total number of security associations refreshes performed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: QM Exchanges
            
            .. attribute:: ciketuninoctets
            
            	The total number of octets received by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: ciketuninpkts
            
            	The total number of packets received by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: ciketunindroppkts
            
            	The total number of packets dropped by this IPsec Phase\-1 IKE Tunnel during  receive processing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: ciketuninnotifys
            
            	The total number of notifys received by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: ciketuninp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges received by  this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketuninp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges received and found to be invalid  by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketuninp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges received and rejected by this IPsec Phase\-1  Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketuninp2sadelrequests
            
            	The total number of IPsec Phase\-2 security association delete requests received  by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: ciketunoutoctets
            
            	The total number of octets sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: ciketunoutpkts
            
            	The total number of packets sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: ciketunoutdroppkts
            
            	The total number of packets dropped by this IPsec Phase\-1 IKE Tunnel during send processing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: ciketunoutnotifys
            
            	The total number of notifys sent by this IPsec Phase\-1 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: ciketunoutp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunoutp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges sent and found to be invalid by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunoutp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges sent and rejected by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunoutp2sadelrequests
            
            	The total number of IPsec Phase\-2 security association delete requests sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: ciketunstatus
            
            	The status of the MIB table row.  This object can be used to bring the tunnel down  by setting value of this object to destroy(2).  This object cannot be used to create  a MIB table row
            	**type**\:  :py:class:`TunnelStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TunnelStatus>`
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Ciketunneltable.Ciketunnelentry, self).__init__()

                self.yang_name = "cikeTunnelEntry"
                self.yang_parent_name = "cikeTunnelTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciketunindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciketunindex', YLeaf(YType.int32, 'cikeTunIndex')),
                    ('ciketunlocaltype', YLeaf(YType.enumeration, 'cikeTunLocalType')),
                    ('ciketunlocalvalue', YLeaf(YType.str, 'cikeTunLocalValue')),
                    ('ciketunlocaladdr', YLeaf(YType.str, 'cikeTunLocalAddr')),
                    ('ciketunlocalname', YLeaf(YType.str, 'cikeTunLocalName')),
                    ('ciketunremotetype', YLeaf(YType.enumeration, 'cikeTunRemoteType')),
                    ('ciketunremotevalue', YLeaf(YType.str, 'cikeTunRemoteValue')),
                    ('ciketunremoteaddr', YLeaf(YType.str, 'cikeTunRemoteAddr')),
                    ('ciketunremotename', YLeaf(YType.str, 'cikeTunRemoteName')),
                    ('ciketunnegomode', YLeaf(YType.enumeration, 'cikeTunNegoMode')),
                    ('ciketundiffhellmangrp', YLeaf(YType.enumeration, 'cikeTunDiffHellmanGrp')),
                    ('ciketunencryptalgo', YLeaf(YType.enumeration, 'cikeTunEncryptAlgo')),
                    ('ciketunhashalgo', YLeaf(YType.enumeration, 'cikeTunHashAlgo')),
                    ('ciketunauthmethod', YLeaf(YType.enumeration, 'cikeTunAuthMethod')),
                    ('ciketunlifetime', YLeaf(YType.int32, 'cikeTunLifeTime')),
                    ('ciketunactivetime', YLeaf(YType.int32, 'cikeTunActiveTime')),
                    ('ciketunsarefreshthreshold', YLeaf(YType.int32, 'cikeTunSaRefreshThreshold')),
                    ('ciketuntotalrefreshes', YLeaf(YType.uint32, 'cikeTunTotalRefreshes')),
                    ('ciketuninoctets', YLeaf(YType.uint32, 'cikeTunInOctets')),
                    ('ciketuninpkts', YLeaf(YType.uint32, 'cikeTunInPkts')),
                    ('ciketunindroppkts', YLeaf(YType.uint32, 'cikeTunInDropPkts')),
                    ('ciketuninnotifys', YLeaf(YType.uint32, 'cikeTunInNotifys')),
                    ('ciketuninp2exchgs', YLeaf(YType.uint32, 'cikeTunInP2Exchgs')),
                    ('ciketuninp2exchginvalids', YLeaf(YType.uint32, 'cikeTunInP2ExchgInvalids')),
                    ('ciketuninp2exchgrejects', YLeaf(YType.uint32, 'cikeTunInP2ExchgRejects')),
                    ('ciketuninp2sadelrequests', YLeaf(YType.uint32, 'cikeTunInP2SaDelRequests')),
                    ('ciketunoutoctets', YLeaf(YType.uint32, 'cikeTunOutOctets')),
                    ('ciketunoutpkts', YLeaf(YType.uint32, 'cikeTunOutPkts')),
                    ('ciketunoutdroppkts', YLeaf(YType.uint32, 'cikeTunOutDropPkts')),
                    ('ciketunoutnotifys', YLeaf(YType.uint32, 'cikeTunOutNotifys')),
                    ('ciketunoutp2exchgs', YLeaf(YType.uint32, 'cikeTunOutP2Exchgs')),
                    ('ciketunoutp2exchginvalids', YLeaf(YType.uint32, 'cikeTunOutP2ExchgInvalids')),
                    ('ciketunoutp2exchgrejects', YLeaf(YType.uint32, 'cikeTunOutP2ExchgRejects')),
                    ('ciketunoutp2sadelrequests', YLeaf(YType.uint32, 'cikeTunOutP2SaDelRequests')),
                    ('ciketunstatus', YLeaf(YType.enumeration, 'cikeTunStatus')),
                ])
                self.ciketunindex = None
                self.ciketunlocaltype = None
                self.ciketunlocalvalue = None
                self.ciketunlocaladdr = None
                self.ciketunlocalname = None
                self.ciketunremotetype = None
                self.ciketunremotevalue = None
                self.ciketunremoteaddr = None
                self.ciketunremotename = None
                self.ciketunnegomode = None
                self.ciketundiffhellmangrp = None
                self.ciketunencryptalgo = None
                self.ciketunhashalgo = None
                self.ciketunauthmethod = None
                self.ciketunlifetime = None
                self.ciketunactivetime = None
                self.ciketunsarefreshthreshold = None
                self.ciketuntotalrefreshes = None
                self.ciketuninoctets = None
                self.ciketuninpkts = None
                self.ciketunindroppkts = None
                self.ciketuninnotifys = None
                self.ciketuninp2exchgs = None
                self.ciketuninp2exchginvalids = None
                self.ciketuninp2exchgrejects = None
                self.ciketuninp2sadelrequests = None
                self.ciketunoutoctets = None
                self.ciketunoutpkts = None
                self.ciketunoutdroppkts = None
                self.ciketunoutnotifys = None
                self.ciketunoutp2exchgs = None
                self.ciketunoutp2exchginvalids = None
                self.ciketunoutp2exchgrejects = None
                self.ciketunoutp2sadelrequests = None
                self.ciketunstatus = None
                self._segment_path = lambda: "cikeTunnelEntry" + "[cikeTunIndex='" + str(self.ciketunindex) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikeTunnelTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Ciketunneltable.Ciketunnelentry, ['ciketunindex', 'ciketunlocaltype', 'ciketunlocalvalue', 'ciketunlocaladdr', 'ciketunlocalname', 'ciketunremotetype', 'ciketunremotevalue', 'ciketunremoteaddr', 'ciketunremotename', 'ciketunnegomode', 'ciketundiffhellmangrp', 'ciketunencryptalgo', 'ciketunhashalgo', 'ciketunauthmethod', 'ciketunlifetime', 'ciketunactivetime', 'ciketunsarefreshthreshold', 'ciketuntotalrefreshes', 'ciketuninoctets', 'ciketuninpkts', 'ciketunindroppkts', 'ciketuninnotifys', 'ciketuninp2exchgs', 'ciketuninp2exchginvalids', 'ciketuninp2exchgrejects', 'ciketuninp2sadelrequests', 'ciketunoutoctets', 'ciketunoutpkts', 'ciketunoutdroppkts', 'ciketunoutnotifys', 'ciketunoutp2exchgs', 'ciketunoutp2exchginvalids', 'ciketunoutp2exchgrejects', 'ciketunoutp2sadelrequests', 'ciketunstatus'], name, value)


    class Cikepeercorrtable(Entity):
        """
        The IPsec Phase\-1 Internet Key Exchange Peer
        Association to IPsec Phase\-2 Tunnel
        Correlation Table. There is one entry in
        this table for each active IPsec Phase\-2
        Tunnel.
        
        .. attribute:: cikepeercorrentry
        
        	Each entry contains the attributes of an IPsec Phase\-1 IKE Peer Association to IPsec Phase\-2 Tunnel Correlation
        	**type**\: list of  		 :py:class:`Cikepeercorrentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikepeercorrtable.Cikepeercorrentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cikepeercorrtable, self).__init__()

            self.yang_name = "cikePeerCorrTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cikePeerCorrEntry", ("cikepeercorrentry", CISCOIPSECFLOWMONITORMIB.Cikepeercorrtable.Cikepeercorrentry))])
            self._leafs = OrderedDict()

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
            
            .. attribute:: cikepeercorrlocaltype  (key)
            
            	The type of local peer identity. The local peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\:  :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: cikepeercorrlocalvalue  (key)
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\: str
            
            .. attribute:: cikepeercorrremotetype  (key)
            
            	The type of remote peer identity. The remote peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\:  :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: cikepeercorrremotevalue  (key)
            
            	The value of the remote peer identity.  If the remote peer type is an IP Address, then this is the IP Address used to identify the remote peer.  If the remote peer type is a host name, then this is the host name used to identify the remote peer
            	**type**\: str
            
            .. attribute:: cikepeercorrintindex  (key)
            
            	The internal index of the local\-remote peer association.  This internal index is  used to uniquely identify multiple associations  between the local and remote peer
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cikepeercorrseqnum  (key)
            
            	The sequence number of the local\-remote peer association.  This sequence number is  used to uniquely identify multiple instances  of an unique association between  the local and remote peer
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cikepeercorripsectunindex
            
            	The index of the active IPsec Phase\-2 Tunnel (cipSecTunIndex in the cipSecTunnelTable) for this IPsec Phase\-1 IKE Peer Association
            	**type**\: int
            
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
                self.ylist_key_names = ['cikepeercorrlocaltype','cikepeercorrlocalvalue','cikepeercorrremotetype','cikepeercorrremotevalue','cikepeercorrintindex','cikepeercorrseqnum']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cikepeercorrlocaltype', YLeaf(YType.enumeration, 'cikePeerCorrLocalType')),
                    ('cikepeercorrlocalvalue', YLeaf(YType.str, 'cikePeerCorrLocalValue')),
                    ('cikepeercorrremotetype', YLeaf(YType.enumeration, 'cikePeerCorrRemoteType')),
                    ('cikepeercorrremotevalue', YLeaf(YType.str, 'cikePeerCorrRemoteValue')),
                    ('cikepeercorrintindex', YLeaf(YType.int32, 'cikePeerCorrIntIndex')),
                    ('cikepeercorrseqnum', YLeaf(YType.int32, 'cikePeerCorrSeqNum')),
                    ('cikepeercorripsectunindex', YLeaf(YType.int32, 'cikePeerCorrIpSecTunIndex')),
                ])
                self.cikepeercorrlocaltype = None
                self.cikepeercorrlocalvalue = None
                self.cikepeercorrremotetype = None
                self.cikepeercorrremotevalue = None
                self.cikepeercorrintindex = None
                self.cikepeercorrseqnum = None
                self.cikepeercorripsectunindex = None
                self._segment_path = lambda: "cikePeerCorrEntry" + "[cikePeerCorrLocalType='" + str(self.cikepeercorrlocaltype) + "']" + "[cikePeerCorrLocalValue='" + str(self.cikepeercorrlocalvalue) + "']" + "[cikePeerCorrRemoteType='" + str(self.cikepeercorrremotetype) + "']" + "[cikePeerCorrRemoteValue='" + str(self.cikepeercorrremotevalue) + "']" + "[cikePeerCorrIntIndex='" + str(self.cikepeercorrintindex) + "']" + "[cikePeerCorrSeqNum='" + str(self.cikepeercorrseqnum) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikePeerCorrTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cikepeercorrtable.Cikepeercorrentry, ['cikepeercorrlocaltype', 'cikepeercorrlocalvalue', 'cikepeercorrremotetype', 'cikepeercorrremotevalue', 'cikepeercorrintindex', 'cikepeercorrseqnum', 'cikepeercorripsectunindex'], name, value)


    class Cikephase1Gwstatstable(Entity):
        """
        Phase\-1 IKE stats information is included in this table.
        Each entry is related to a specific gateway which is 
        identified by 'cmgwIndex'.
        
        .. attribute:: cikephase1gwstatsentry
        
        	Each entry contains the attributes of an Phase\-1 IKE stats information for the related gateway.  There is only one entry for each gateway. The entry  is created when a gateway up and cannot be deleted
        	**type**\: list of  		 :py:class:`Cikephase1Gwstatsentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikephase1Gwstatstable.Cikephase1Gwstatsentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cikephase1Gwstatstable, self).__init__()

            self.yang_name = "cikePhase1GWStatsTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cikePhase1GWStatsEntry", ("cikephase1gwstatsentry", CISCOIPSECFLOWMONITORMIB.Cikephase1Gwstatstable.Cikephase1Gwstatsentry))])
            self._leafs = OrderedDict()

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
            
            .. attribute:: cmgwindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cikephase1gwactivetunnels
            
            	The number of currently active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikephase1gwprevioustunnels
            
            	The total number of previously active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SAs
            
            .. attribute:: cikephase1gwinoctets
            
            	The total number of octets received by all currently and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cikephase1gwinpkts
            
            	The total number of packets received by all currently and previously active IPsec  Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cikephase1gwindroppkts
            
            	The total number of packets which were dropped during receive processing by all  currently and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cikephase1gwinnotifys
            
            	The total number of notifys received by all currently and previously active IPsec  Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: cikephase1gwinp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges received by all currently and previously  active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: cikephase1gwinp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges which were received and found to be invalid  by all currently and previously active IPsec  Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: cikephase1gwinp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges which were received and rejected by all  currently and previously active IPsec Phase\-1  IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: cikephase1gwinp2sadelrequests
            
            	The total number of IPsec Phase\-2 'Security Association' delete requests received by all  currently and previously active and IPsec  Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: cikephase1gwoutoctets
            
            	The total number of octets sent by all currently and previously active and IPsec Phase\-1  IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cikephase1gwoutpkts
            
            	The total number of packets sent by all currently and previously active and IPsec Phase\-1  Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cikephase1gwoutdroppkts
            
            	The total number of packets which were dropped during send processing by all currently  and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cikephase1gwoutnotifys
            
            	The total number of notifys sent by all currently and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: cikephase1gwoutp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges which were sent by all currently and previously  active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: cikephase1gwoutp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges which were sent and found to be invalid by  all currently and previously active IPsec Phase\-1  Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: cikephase1gwoutp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges which were sent and rejected by all currently and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: cikephase1gwoutp2sadelrequests
            
            	The total number of IPsec Phase\-2 SA delete requests sent by all currently and  previously active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: cikephase1gwinittunnels
            
            	The total number of IPsec Phase\-1 IKE Tunnels which were locally initiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SAs
            
            .. attribute:: cikephase1gwinittunnelfails
            
            	The total number of IPsec Phase\-1 IKE Tunnels which were locally initiated and failed to activate
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SAs
            
            .. attribute:: cikephase1gwresptunnelfails
            
            	The total number of IPsec Phase\-1 IKE Tunnels which were remotely initiated and failed to activate
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SAs
            
            .. attribute:: cikephase1gwsyscapfails
            
            	The total number of system capacity failures which occurred during processing of all current  and previously active IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cikephase1gwauthfails
            
            	The total number of authentications which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cikephase1gwdecryptfails
            
            	The total number of decryptions which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cikephase1gwhashvalidfails
            
            	The total number of hash validations which ended in failure by all current and previous IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cikephase1gwnosafails
            
            	The total number of non\-existent 'Security Association' failures occurred during processing of current and  previous IPsec Phase\-1 IKE Tunnels
            	**type**\: int
            
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
                self.ylist_key_names = ['cmgwindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cmgwindex', YLeaf(YType.str, 'cmgwIndex')),
                    ('cikephase1gwactivetunnels', YLeaf(YType.uint32, 'cikePhase1GWActiveTunnels')),
                    ('cikephase1gwprevioustunnels', YLeaf(YType.uint32, 'cikePhase1GWPreviousTunnels')),
                    ('cikephase1gwinoctets', YLeaf(YType.uint32, 'cikePhase1GWInOctets')),
                    ('cikephase1gwinpkts', YLeaf(YType.uint32, 'cikePhase1GWInPkts')),
                    ('cikephase1gwindroppkts', YLeaf(YType.uint32, 'cikePhase1GWInDropPkts')),
                    ('cikephase1gwinnotifys', YLeaf(YType.uint32, 'cikePhase1GWInNotifys')),
                    ('cikephase1gwinp2exchgs', YLeaf(YType.uint32, 'cikePhase1GWInP2Exchgs')),
                    ('cikephase1gwinp2exchginvalids', YLeaf(YType.uint32, 'cikePhase1GWInP2ExchgInvalids')),
                    ('cikephase1gwinp2exchgrejects', YLeaf(YType.uint32, 'cikePhase1GWInP2ExchgRejects')),
                    ('cikephase1gwinp2sadelrequests', YLeaf(YType.uint32, 'cikePhase1GWInP2SaDelRequests')),
                    ('cikephase1gwoutoctets', YLeaf(YType.uint32, 'cikePhase1GWOutOctets')),
                    ('cikephase1gwoutpkts', YLeaf(YType.uint32, 'cikePhase1GWOutPkts')),
                    ('cikephase1gwoutdroppkts', YLeaf(YType.uint32, 'cikePhase1GWOutDropPkts')),
                    ('cikephase1gwoutnotifys', YLeaf(YType.uint32, 'cikePhase1GWOutNotifys')),
                    ('cikephase1gwoutp2exchgs', YLeaf(YType.uint32, 'cikePhase1GWOutP2Exchgs')),
                    ('cikephase1gwoutp2exchginvalids', YLeaf(YType.uint32, 'cikePhase1GWOutP2ExchgInvalids')),
                    ('cikephase1gwoutp2exchgrejects', YLeaf(YType.uint32, 'cikePhase1GWOutP2ExchgRejects')),
                    ('cikephase1gwoutp2sadelrequests', YLeaf(YType.uint32, 'cikePhase1GWOutP2SaDelRequests')),
                    ('cikephase1gwinittunnels', YLeaf(YType.uint32, 'cikePhase1GWInitTunnels')),
                    ('cikephase1gwinittunnelfails', YLeaf(YType.uint32, 'cikePhase1GWInitTunnelFails')),
                    ('cikephase1gwresptunnelfails', YLeaf(YType.uint32, 'cikePhase1GWRespTunnelFails')),
                    ('cikephase1gwsyscapfails', YLeaf(YType.uint32, 'cikePhase1GWSysCapFails')),
                    ('cikephase1gwauthfails', YLeaf(YType.uint32, 'cikePhase1GWAuthFails')),
                    ('cikephase1gwdecryptfails', YLeaf(YType.uint32, 'cikePhase1GWDecryptFails')),
                    ('cikephase1gwhashvalidfails', YLeaf(YType.uint32, 'cikePhase1GWHashValidFails')),
                    ('cikephase1gwnosafails', YLeaf(YType.uint32, 'cikePhase1GWNoSaFails')),
                ])
                self.cmgwindex = None
                self.cikephase1gwactivetunnels = None
                self.cikephase1gwprevioustunnels = None
                self.cikephase1gwinoctets = None
                self.cikephase1gwinpkts = None
                self.cikephase1gwindroppkts = None
                self.cikephase1gwinnotifys = None
                self.cikephase1gwinp2exchgs = None
                self.cikephase1gwinp2exchginvalids = None
                self.cikephase1gwinp2exchgrejects = None
                self.cikephase1gwinp2sadelrequests = None
                self.cikephase1gwoutoctets = None
                self.cikephase1gwoutpkts = None
                self.cikephase1gwoutdroppkts = None
                self.cikephase1gwoutnotifys = None
                self.cikephase1gwoutp2exchgs = None
                self.cikephase1gwoutp2exchginvalids = None
                self.cikephase1gwoutp2exchgrejects = None
                self.cikephase1gwoutp2sadelrequests = None
                self.cikephase1gwinittunnels = None
                self.cikephase1gwinittunnelfails = None
                self.cikephase1gwresptunnelfails = None
                self.cikephase1gwsyscapfails = None
                self.cikephase1gwauthfails = None
                self.cikephase1gwdecryptfails = None
                self.cikephase1gwhashvalidfails = None
                self.cikephase1gwnosafails = None
                self._segment_path = lambda: "cikePhase1GWStatsEntry" + "[cmgwIndex='" + str(self.cmgwindex) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikePhase1GWStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cikephase1Gwstatstable.Cikephase1Gwstatsentry, ['cmgwindex', 'cikephase1gwactivetunnels', 'cikephase1gwprevioustunnels', 'cikephase1gwinoctets', 'cikephase1gwinpkts', 'cikephase1gwindroppkts', 'cikephase1gwinnotifys', 'cikephase1gwinp2exchgs', 'cikephase1gwinp2exchginvalids', 'cikephase1gwinp2exchgrejects', 'cikephase1gwinp2sadelrequests', 'cikephase1gwoutoctets', 'cikephase1gwoutpkts', 'cikephase1gwoutdroppkts', 'cikephase1gwoutnotifys', 'cikephase1gwoutp2exchgs', 'cikephase1gwoutp2exchginvalids', 'cikephase1gwoutp2exchgrejects', 'cikephase1gwoutp2sadelrequests', 'cikephase1gwinittunnels', 'cikephase1gwinittunnelfails', 'cikephase1gwresptunnelfails', 'cikephase1gwsyscapfails', 'cikephase1gwauthfails', 'cikephase1gwdecryptfails', 'cikephase1gwhashvalidfails', 'cikephase1gwnosafails'], name, value)


    class Cipsectunneltable(Entity):
        """
        The IPsec Phase\-2 Tunnel Table.
        There is one entry in this table for 
        each active IPsec Phase\-2 Tunnel.
        
        .. attribute:: cipsectunnelentry
        
        	Each entry contains the attributes associated with an active IPsec Phase\-2 Tunnel
        	**type**\: list of  		 :py:class:`Cipsectunnelentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsectunneltable.Cipsectunnelentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsectunneltable, self).__init__()

            self.yang_name = "cipSecTunnelTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipSecTunnelEntry", ("cipsectunnelentry", CISCOIPSECFLOWMONITORMIB.Cipsectunneltable.Cipsectunnelentry))])
            self._leafs = OrderedDict()

            self.cipsectunnelentry = YList(self)
            self._segment_path = lambda: "cipSecTunnelTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsectunneltable, [], name, value)


        class Cipsectunnelentry(Entity):
            """
            Each entry contains the attributes
            associated with an active IPsec Phase\-2 Tunnel.
            
            .. attribute:: cipsectunindex  (key)
            
            	The index of the IPsec Phase\-2 Tunnel Table. The value of the index is a number which begins  at one and is incremented with each tunnel that  is created. The value of this object will wrap  at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectuniketunnelindex
            
            	The index of the associated IPsec Phase\-1 IKE Tunnel.  (cikeTunIndex in the cikeTunnelTable)
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectuniketunnelalive
            
            	An indicator which specifies whether or not the IPsec Phase\-1 IKE Tunnel currently exists
            	**type**\: bool
            
            .. attribute:: cipsectunlocaladdr
            
            	The IP address of the local endpoint for the IPsec Phase\-2 Tunnel
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsectunremoteaddr
            
            	The IP address of the remote endpoint for the IPsec Phase\-2 Tunnel
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsectunkeytype
            
            	The type of key used by the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`KeyType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.KeyType>`
            
            .. attribute:: cipsectunencapmode
            
            	The encapsulation mode used by the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`EncapMode <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncapMode>`
            
            .. attribute:: cipsectunlifesize
            
            	The negotiated LifeSize of the IPsec Phase\-2 Tunnel in kilobytes
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**units**\: KBytes
            
            .. attribute:: cipsectunlifetime
            
            	The negotiated LifeTime of the IPsec Phase\-2 Tunnel in seconds
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**units**\: Seconds
            
            .. attribute:: cipsectunactivetime
            
            	The length of time the IPsec Phase\-2 Tunnel has been  active in hundredths of seconds
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cipsectunsalifesizethreshold
            
            	The security association LifeSize refresh threshold in kilobytes
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**units**\: KBytes
            
            .. attribute:: cipsectunsalifetimethreshold
            
            	The security association LifeTime refresh threshold in seconds
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**units**\: Seconds
            
            .. attribute:: cipsectuntotalrefreshes
            
            	The total number of security association refreshes performed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: QM Exchanges
            
            .. attribute:: cipsectunexpiredsainstances
            
            	The total number of security associations which have expired
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SAs
            
            .. attribute:: cipsectuncurrentsainstances
            
            	The number of security associations which are currently active or expiring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectuninsadiffhellmangrp
            
            	The Diffie Hellman Group used by the inbound security association of the  IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`DiffHellmanGrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp>`
            
            .. attribute:: cipsectuninsaencryptalgo
            
            	The encryption algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`EncryptAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo>`
            
            .. attribute:: cipsectuninsaahauthalgo
            
            	The authentication algorithm used by the inbound authentication header (AH) security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`AuthAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo>`
            
            .. attribute:: cipsectuninsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP) security  association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`AuthAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo>`
            
            .. attribute:: cipsectuninsadecompalgo
            
            	The decompression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`CompAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CompAlgo>`
            
            .. attribute:: cipsectunoutsadiffhellmangrp
            
            	The Diffie Hellman Group used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`DiffHellmanGrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp>`
            
            .. attribute:: cipsectunoutsaencryptalgo
            
            	The encryption algorithm used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`EncryptAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo>`
            
            .. attribute:: cipsectunoutsaahauthalgo
            
            	The authentication algorithm used by the outbound authentication header (AH) security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`AuthAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo>`
            
            .. attribute:: cipsectunoutsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP)  security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`AuthAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo>`
            
            .. attribute:: cipsectunoutsacompalgo
            
            	The compression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`CompAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CompAlgo>`
            
            .. attribute:: cipsectuninoctets
            
            	The total number of octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated BEFORE determining whether or not the packet should be decompressed.  See also cipSecTunInOctWraps for the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsectunhcinoctets
            
            	A high capacity count of the total number of octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated BEFORE determining whether or not the packet should be decompressed
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: Octets
            
            .. attribute:: cipsectuninoctwraps
            
            	The number of times the octets received counter (cipSecTunInOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsectunindecompoctets
            
            	The total number of decompressed octets received by this IPsec Phase\-2 Tunnel. This value is  accumulated AFTER the packet is decompressed.  If compression is not being  used, this value will match the value of   cipSecTunInOctets.  See also cipSecTunInDecompOctWraps   for the number of times  this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsectunhcindecompoctets
            
            	A high capacity count of the total number of decompressed octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER the packet is decompressed. If compression is not being used, this value will match the value of cipSecTunHcInOctets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunindecompoctwraps
            
            	The number of times the decompressed octets received counter  (cipSecTunInDecompOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsectuninpkts
            
            	The total number of packets received by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunindroppkts
            
            	The total number of packets dropped during receive processing by this IPsec Phase\-2  Tunnel. This count does NOT include  packets dropped due to Anti\-Replay processing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectuninreplaydroppkts
            
            	The total number of packets dropped during receive processing due to Anti\-Replay processing  by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectuninauths
            
            	The total number of inbound authentication's performed by this  IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Events
            
            .. attribute:: cipsectuninauthfails
            
            	The total number of inbound authentication's which ended in  failure by this IPsec Phase\-2 Tunnel 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsectunindecrypts
            
            	The total number of inbound decryption's performed by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunindecryptfails
            
            	The total number of inbound decryption's which ended in failure  by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsectunoutoctets
            
            	The total number of octets sent by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER determining whether or not the packet should  be compressed.  See also cipSecTunOutOctWraps for the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsectunhcoutoctets
            
            	A high capacity count of the total number of octets sent by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER determining whether or not the  packet should be compressed
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunoutoctwraps
            
            	The number of times the out octets counter (cipSecTunOutOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsectunoutuncompoctets
            
            	The total number of uncompressed octets sent by this IPsec Phase\-2 Tunnel.  This value  is accumulated BEFORE the packet is compressed.  If compression is not being used, this value  will match the value of cipSecTunOutOctets.  See also cipSecTunOutDecompOctWraps for the   number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsectunhcoutuncompoctets
            
            	A high capacity count of the total number of uncompressed octets sent by this IPsec  Phase\-2 Tunnel.  This value is accumulated BEFORE  the packet is compressed. If compression  is not being used, this value will match the value  of cipSecTunHcOutOctets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunoutuncompoctwraps
            
            	The number of times the uncompressed octets sent counter (cipSecTunOutUncompOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsectunoutpkts
            
            	The total number of packets sent by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunoutdroppkts
            
            	The total number of packets dropped during send processing by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunoutauths
            
            	The total number of outbound authentication's performed by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Events
            
            .. attribute:: cipsectunoutauthfails
            
            	The total number of outbound authentication's which ended in failure  by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsectunoutencrypts
            
            	The total number of outbound encryption's performed by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunoutencryptfails
            
            	The total number of outbound encryption's which ended in failure by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsectunstatus
            
            	The status of the MIB table row.  This object can be used to bring the tunnel down by setting value of this object to destroy(2). When the value is set to destroy(2), the SA bundle is destroyed and this row is deleted from this table.  When this MIB value is queried, the value of active(1) is always returned, if the instance  exists.  This object cannot be used to create a MIB  table row
            	**type**\:  :py:class:`TunnelStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TunnelStatus>`
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cipsectunneltable.Cipsectunnelentry, self).__init__()

                self.yang_name = "cipSecTunnelEntry"
                self.yang_parent_name = "cipSecTunnelTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipsectunindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipsectunindex', YLeaf(YType.int32, 'cipSecTunIndex')),
                    ('cipsectuniketunnelindex', YLeaf(YType.int32, 'cipSecTunIkeTunnelIndex')),
                    ('cipsectuniketunnelalive', YLeaf(YType.boolean, 'cipSecTunIkeTunnelAlive')),
                    ('cipsectunlocaladdr', YLeaf(YType.str, 'cipSecTunLocalAddr')),
                    ('cipsectunremoteaddr', YLeaf(YType.str, 'cipSecTunRemoteAddr')),
                    ('cipsectunkeytype', YLeaf(YType.enumeration, 'cipSecTunKeyType')),
                    ('cipsectunencapmode', YLeaf(YType.enumeration, 'cipSecTunEncapMode')),
                    ('cipsectunlifesize', YLeaf(YType.int32, 'cipSecTunLifeSize')),
                    ('cipsectunlifetime', YLeaf(YType.int32, 'cipSecTunLifeTime')),
                    ('cipsectunactivetime', YLeaf(YType.int32, 'cipSecTunActiveTime')),
                    ('cipsectunsalifesizethreshold', YLeaf(YType.int32, 'cipSecTunSaLifeSizeThreshold')),
                    ('cipsectunsalifetimethreshold', YLeaf(YType.int32, 'cipSecTunSaLifeTimeThreshold')),
                    ('cipsectuntotalrefreshes', YLeaf(YType.uint32, 'cipSecTunTotalRefreshes')),
                    ('cipsectunexpiredsainstances', YLeaf(YType.uint32, 'cipSecTunExpiredSaInstances')),
                    ('cipsectuncurrentsainstances', YLeaf(YType.uint32, 'cipSecTunCurrentSaInstances')),
                    ('cipsectuninsadiffhellmangrp', YLeaf(YType.enumeration, 'cipSecTunInSaDiffHellmanGrp')),
                    ('cipsectuninsaencryptalgo', YLeaf(YType.enumeration, 'cipSecTunInSaEncryptAlgo')),
                    ('cipsectuninsaahauthalgo', YLeaf(YType.enumeration, 'cipSecTunInSaAhAuthAlgo')),
                    ('cipsectuninsaespauthalgo', YLeaf(YType.enumeration, 'cipSecTunInSaEspAuthAlgo')),
                    ('cipsectuninsadecompalgo', YLeaf(YType.enumeration, 'cipSecTunInSaDecompAlgo')),
                    ('cipsectunoutsadiffhellmangrp', YLeaf(YType.enumeration, 'cipSecTunOutSaDiffHellmanGrp')),
                    ('cipsectunoutsaencryptalgo', YLeaf(YType.enumeration, 'cipSecTunOutSaEncryptAlgo')),
                    ('cipsectunoutsaahauthalgo', YLeaf(YType.enumeration, 'cipSecTunOutSaAhAuthAlgo')),
                    ('cipsectunoutsaespauthalgo', YLeaf(YType.enumeration, 'cipSecTunOutSaEspAuthAlgo')),
                    ('cipsectunoutsacompalgo', YLeaf(YType.enumeration, 'cipSecTunOutSaCompAlgo')),
                    ('cipsectuninoctets', YLeaf(YType.uint32, 'cipSecTunInOctets')),
                    ('cipsectunhcinoctets', YLeaf(YType.uint64, 'cipSecTunHcInOctets')),
                    ('cipsectuninoctwraps', YLeaf(YType.uint32, 'cipSecTunInOctWraps')),
                    ('cipsectunindecompoctets', YLeaf(YType.uint32, 'cipSecTunInDecompOctets')),
                    ('cipsectunhcindecompoctets', YLeaf(YType.uint64, 'cipSecTunHcInDecompOctets')),
                    ('cipsectunindecompoctwraps', YLeaf(YType.uint32, 'cipSecTunInDecompOctWraps')),
                    ('cipsectuninpkts', YLeaf(YType.uint32, 'cipSecTunInPkts')),
                    ('cipsectunindroppkts', YLeaf(YType.uint32, 'cipSecTunInDropPkts')),
                    ('cipsectuninreplaydroppkts', YLeaf(YType.uint32, 'cipSecTunInReplayDropPkts')),
                    ('cipsectuninauths', YLeaf(YType.uint32, 'cipSecTunInAuths')),
                    ('cipsectuninauthfails', YLeaf(YType.uint32, 'cipSecTunInAuthFails')),
                    ('cipsectunindecrypts', YLeaf(YType.uint32, 'cipSecTunInDecrypts')),
                    ('cipsectunindecryptfails', YLeaf(YType.uint32, 'cipSecTunInDecryptFails')),
                    ('cipsectunoutoctets', YLeaf(YType.uint32, 'cipSecTunOutOctets')),
                    ('cipsectunhcoutoctets', YLeaf(YType.uint64, 'cipSecTunHcOutOctets')),
                    ('cipsectunoutoctwraps', YLeaf(YType.uint32, 'cipSecTunOutOctWraps')),
                    ('cipsectunoutuncompoctets', YLeaf(YType.uint32, 'cipSecTunOutUncompOctets')),
                    ('cipsectunhcoutuncompoctets', YLeaf(YType.uint64, 'cipSecTunHcOutUncompOctets')),
                    ('cipsectunoutuncompoctwraps', YLeaf(YType.uint32, 'cipSecTunOutUncompOctWraps')),
                    ('cipsectunoutpkts', YLeaf(YType.uint32, 'cipSecTunOutPkts')),
                    ('cipsectunoutdroppkts', YLeaf(YType.uint32, 'cipSecTunOutDropPkts')),
                    ('cipsectunoutauths', YLeaf(YType.uint32, 'cipSecTunOutAuths')),
                    ('cipsectunoutauthfails', YLeaf(YType.uint32, 'cipSecTunOutAuthFails')),
                    ('cipsectunoutencrypts', YLeaf(YType.uint32, 'cipSecTunOutEncrypts')),
                    ('cipsectunoutencryptfails', YLeaf(YType.uint32, 'cipSecTunOutEncryptFails')),
                    ('cipsectunstatus', YLeaf(YType.enumeration, 'cipSecTunStatus')),
                ])
                self.cipsectunindex = None
                self.cipsectuniketunnelindex = None
                self.cipsectuniketunnelalive = None
                self.cipsectunlocaladdr = None
                self.cipsectunremoteaddr = None
                self.cipsectunkeytype = None
                self.cipsectunencapmode = None
                self.cipsectunlifesize = None
                self.cipsectunlifetime = None
                self.cipsectunactivetime = None
                self.cipsectunsalifesizethreshold = None
                self.cipsectunsalifetimethreshold = None
                self.cipsectuntotalrefreshes = None
                self.cipsectunexpiredsainstances = None
                self.cipsectuncurrentsainstances = None
                self.cipsectuninsadiffhellmangrp = None
                self.cipsectuninsaencryptalgo = None
                self.cipsectuninsaahauthalgo = None
                self.cipsectuninsaespauthalgo = None
                self.cipsectuninsadecompalgo = None
                self.cipsectunoutsadiffhellmangrp = None
                self.cipsectunoutsaencryptalgo = None
                self.cipsectunoutsaahauthalgo = None
                self.cipsectunoutsaespauthalgo = None
                self.cipsectunoutsacompalgo = None
                self.cipsectuninoctets = None
                self.cipsectunhcinoctets = None
                self.cipsectuninoctwraps = None
                self.cipsectunindecompoctets = None
                self.cipsectunhcindecompoctets = None
                self.cipsectunindecompoctwraps = None
                self.cipsectuninpkts = None
                self.cipsectunindroppkts = None
                self.cipsectuninreplaydroppkts = None
                self.cipsectuninauths = None
                self.cipsectuninauthfails = None
                self.cipsectunindecrypts = None
                self.cipsectunindecryptfails = None
                self.cipsectunoutoctets = None
                self.cipsectunhcoutoctets = None
                self.cipsectunoutoctwraps = None
                self.cipsectunoutuncompoctets = None
                self.cipsectunhcoutuncompoctets = None
                self.cipsectunoutuncompoctwraps = None
                self.cipsectunoutpkts = None
                self.cipsectunoutdroppkts = None
                self.cipsectunoutauths = None
                self.cipsectunoutauthfails = None
                self.cipsectunoutencrypts = None
                self.cipsectunoutencryptfails = None
                self.cipsectunstatus = None
                self._segment_path = lambda: "cipSecTunnelEntry" + "[cipSecTunIndex='" + str(self.cipsectunindex) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecTunnelTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsectunneltable.Cipsectunnelentry, ['cipsectunindex', 'cipsectuniketunnelindex', 'cipsectuniketunnelalive', 'cipsectunlocaladdr', 'cipsectunremoteaddr', 'cipsectunkeytype', 'cipsectunencapmode', 'cipsectunlifesize', 'cipsectunlifetime', 'cipsectunactivetime', 'cipsectunsalifesizethreshold', 'cipsectunsalifetimethreshold', 'cipsectuntotalrefreshes', 'cipsectunexpiredsainstances', 'cipsectuncurrentsainstances', 'cipsectuninsadiffhellmangrp', 'cipsectuninsaencryptalgo', 'cipsectuninsaahauthalgo', 'cipsectuninsaespauthalgo', 'cipsectuninsadecompalgo', 'cipsectunoutsadiffhellmangrp', 'cipsectunoutsaencryptalgo', 'cipsectunoutsaahauthalgo', 'cipsectunoutsaespauthalgo', 'cipsectunoutsacompalgo', 'cipsectuninoctets', 'cipsectunhcinoctets', 'cipsectuninoctwraps', 'cipsectunindecompoctets', 'cipsectunhcindecompoctets', 'cipsectunindecompoctwraps', 'cipsectuninpkts', 'cipsectunindroppkts', 'cipsectuninreplaydroppkts', 'cipsectuninauths', 'cipsectuninauthfails', 'cipsectunindecrypts', 'cipsectunindecryptfails', 'cipsectunoutoctets', 'cipsectunhcoutoctets', 'cipsectunoutoctwraps', 'cipsectunoutuncompoctets', 'cipsectunhcoutuncompoctets', 'cipsectunoutuncompoctwraps', 'cipsectunoutpkts', 'cipsectunoutdroppkts', 'cipsectunoutauths', 'cipsectunoutauthfails', 'cipsectunoutencrypts', 'cipsectunoutencryptfails', 'cipsectunstatus'], name, value)


    class Cipsecendpttable(Entity):
        """
        The IPsec Phase\-2 Tunnel Endpoint Table.
        This table contains an entry for each 
        active endpoint associated with an IPsec
         Phase\-2 Tunnel.
        
        .. attribute:: cipsecendptentry
        
        	An IPsec Phase\-2 Tunnel Endpoint entry
        	**type**\: list of  		 :py:class:`Cipsecendptentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecendpttable.Cipsecendptentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsecendpttable, self).__init__()

            self.yang_name = "cipSecEndPtTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipSecEndPtEntry", ("cipsecendptentry", CISCOIPSECFLOWMONITORMIB.Cipsecendpttable.Cipsecendptentry))])
            self._leafs = OrderedDict()

            self.cipsecendptentry = YList(self)
            self._segment_path = lambda: "cipSecEndPtTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecendpttable, [], name, value)


        class Cipsecendptentry(Entity):
            """
            An IPsec Phase\-2 Tunnel Endpoint entry.
            
            .. attribute:: cipsectunindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cipsectunindex <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsectunneltable.Cipsectunnelentry>`
            
            .. attribute:: cipsecendptindex  (key)
            
            	The number of the Endpoint associated with the IPsec Phase\-2 Tunnel Table.  The value of this index is a number which begins at one and  is incremented with each Endpoint associated  with an IPsec Phase\-2 Tunnel. The value of this object will wrap at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecendptlocalname
            
            	The DNS name of the local Endpoint
            	**type**\: str
            
            .. attribute:: cipsecendptlocaltype
            
            	The type of identity for the local Endpoint. Possible values are\: 1) a single IP address, or 2) an IP address range, or 3) an IP subnet
            	**type**\:  :py:class:`EndPtType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EndPtType>`
            
            .. attribute:: cipsecendptlocaladdr1
            
            	The local Endpoint's first IP address specification.  If the local Endpoint type is single IP address,  then this is the value of the IP address.  If the local Endpoint type is IP subnet, then this is the value of the subnet.  If the local Endpoint type is IP address range,  then this is the value of beginning IP address  of the range
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecendptlocaladdr2
            
            	The local Endpoint's second IP address specification.  If the local Endpoint type is single IP address,  then this is the value of the IP address.  If the local Endpoint type is IP subnet, then this is the value of the subnet mask.  If the local Endpoint type is IP address range,  then this is the value of ending IP address  of the range
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecendptlocalprotocol
            
            	The protocol number of the local Endpoint's traffic
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cipsecendptlocalport
            
            	The port number of the local Endpoint's traffic
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cipsecendptremotename
            
            	The DNS name of the remote Endpoint
            	**type**\: str
            
            .. attribute:: cipsecendptremotetype
            
            	The type of identity for the remote Endpoint. Possible values are\: 1) a single IP address, or 2) an IP address range, or 3) an IP subnet
            	**type**\:  :py:class:`EndPtType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EndPtType>`
            
            .. attribute:: cipsecendptremoteaddr1
            
            	The remote Endpoint's first IP address specification.  If the remote Endpoint type is single IP address,  then this is the value of the IP address.  If the remote Endpoint type is IP subnet, then this is the value of the subnet.  If the remote Endpoint type is IP address range,  then this is the value of beginning IP address  of the range
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecendptremoteaddr2
            
            	The remote Endpoint's second IP address specification.  If the remote Endpoint type is single IP address,  then this is the value of the IP address.  If the remote Endpoint type is IP subnet, then this is the value of the subnet mask.  If the remote Endpoint type is IP address range,  then this is the value of ending IP address of  the range
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecendptremoteprotocol
            
            	The protocol number of the remote Endpoint's traffic
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cipsecendptremoteport
            
            	The port number of the remote Endpoint's traffic
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cipsecendpttable.Cipsecendptentry, self).__init__()

                self.yang_name = "cipSecEndPtEntry"
                self.yang_parent_name = "cipSecEndPtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipsectunindex','cipsecendptindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipsectunindex', YLeaf(YType.str, 'cipSecTunIndex')),
                    ('cipsecendptindex', YLeaf(YType.int32, 'cipSecEndPtIndex')),
                    ('cipsecendptlocalname', YLeaf(YType.str, 'cipSecEndPtLocalName')),
                    ('cipsecendptlocaltype', YLeaf(YType.enumeration, 'cipSecEndPtLocalType')),
                    ('cipsecendptlocaladdr1', YLeaf(YType.str, 'cipSecEndPtLocalAddr1')),
                    ('cipsecendptlocaladdr2', YLeaf(YType.str, 'cipSecEndPtLocalAddr2')),
                    ('cipsecendptlocalprotocol', YLeaf(YType.int32, 'cipSecEndPtLocalProtocol')),
                    ('cipsecendptlocalport', YLeaf(YType.int32, 'cipSecEndPtLocalPort')),
                    ('cipsecendptremotename', YLeaf(YType.str, 'cipSecEndPtRemoteName')),
                    ('cipsecendptremotetype', YLeaf(YType.enumeration, 'cipSecEndPtRemoteType')),
                    ('cipsecendptremoteaddr1', YLeaf(YType.str, 'cipSecEndPtRemoteAddr1')),
                    ('cipsecendptremoteaddr2', YLeaf(YType.str, 'cipSecEndPtRemoteAddr2')),
                    ('cipsecendptremoteprotocol', YLeaf(YType.int32, 'cipSecEndPtRemoteProtocol')),
                    ('cipsecendptremoteport', YLeaf(YType.int32, 'cipSecEndPtRemotePort')),
                ])
                self.cipsectunindex = None
                self.cipsecendptindex = None
                self.cipsecendptlocalname = None
                self.cipsecendptlocaltype = None
                self.cipsecendptlocaladdr1 = None
                self.cipsecendptlocaladdr2 = None
                self.cipsecendptlocalprotocol = None
                self.cipsecendptlocalport = None
                self.cipsecendptremotename = None
                self.cipsecendptremotetype = None
                self.cipsecendptremoteaddr1 = None
                self.cipsecendptremoteaddr2 = None
                self.cipsecendptremoteprotocol = None
                self.cipsecendptremoteport = None
                self._segment_path = lambda: "cipSecEndPtEntry" + "[cipSecTunIndex='" + str(self.cipsectunindex) + "']" + "[cipSecEndPtIndex='" + str(self.cipsecendptindex) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecEndPtTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecendpttable.Cipsecendptentry, ['cipsectunindex', 'cipsecendptindex', 'cipsecendptlocalname', 'cipsecendptlocaltype', 'cipsecendptlocaladdr1', 'cipsecendptlocaladdr2', 'cipsecendptlocalprotocol', 'cipsecendptlocalport', 'cipsecendptremotename', 'cipsecendptremotetype', 'cipsecendptremoteaddr1', 'cipsecendptremoteaddr2', 'cipsecendptremoteprotocol', 'cipsecendptremoteport'], name, value)


    class Cipsecspitable(Entity):
        """
        The IPsec Phase\-2 Security Protection Index Table.
        This table contains an entry for each active 
        and expiring security
         association.
        
        .. attribute:: cipsecspientry
        
        	Each entry contains the attributes associated with active and expiring IPsec Phase\-2  security associations
        	**type**\: list of  		 :py:class:`Cipsecspientry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecspitable.Cipsecspientry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsecspitable, self).__init__()

            self.yang_name = "cipSecSpiTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipSecSpiEntry", ("cipsecspientry", CISCOIPSECFLOWMONITORMIB.Cipsecspitable.Cipsecspientry))])
            self._leafs = OrderedDict()

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
            
            .. attribute:: cipsectunindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cipsectunindex <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsectunneltable.Cipsectunnelentry>`
            
            .. attribute:: cipsecspiindex  (key)
            
            	The number of the SPI associated with the Phase\-2 Tunnel Table.  The value of this  index is a number which begins at one and is  incremented with each SPI associated with an  IPsec Phase\-2 Tunnel.  The value of this  object will wrap at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecspidirection
            
            	The direction of the SPI
            	**type**\:  :py:class:`Cipsecspidirection <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecspitable.Cipsecspientry.Cipsecspidirection>`
            
            .. attribute:: cipsecspivalue
            
            	The value of the SPI
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cipsecspiprotocol
            
            	The protocol of the SPI
            	**type**\:  :py:class:`Cipsecspiprotocol <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecspitable.Cipsecspientry.Cipsecspiprotocol>`
            
            .. attribute:: cipsecspistatus
            
            	The status of the SPI
            	**type**\:  :py:class:`Cipsecspistatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecspitable.Cipsecspientry.Cipsecspistatus>`
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cipsecspitable.Cipsecspientry, self).__init__()

                self.yang_name = "cipSecSpiEntry"
                self.yang_parent_name = "cipSecSpiTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipsectunindex','cipsecspiindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipsectunindex', YLeaf(YType.str, 'cipSecTunIndex')),
                    ('cipsecspiindex', YLeaf(YType.int32, 'cipSecSpiIndex')),
                    ('cipsecspidirection', YLeaf(YType.enumeration, 'cipSecSpiDirection')),
                    ('cipsecspivalue', YLeaf(YType.uint32, 'cipSecSpiValue')),
                    ('cipsecspiprotocol', YLeaf(YType.enumeration, 'cipSecSpiProtocol')),
                    ('cipsecspistatus', YLeaf(YType.enumeration, 'cipSecSpiStatus')),
                ])
                self.cipsectunindex = None
                self.cipsecspiindex = None
                self.cipsecspidirection = None
                self.cipsecspivalue = None
                self.cipsecspiprotocol = None
                self.cipsecspistatus = None
                self._segment_path = lambda: "cipSecSpiEntry" + "[cipSecTunIndex='" + str(self.cipsectunindex) + "']" + "[cipSecSpiIndex='" + str(self.cipsecspiindex) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecSpiTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecspitable.Cipsecspientry, ['cipsectunindex', 'cipsecspiindex', 'cipsecspidirection', 'cipsecspivalue', 'cipsecspiprotocol', 'cipsecspistatus'], name, value)

            class Cipsecspidirection(Enum):
                """
                Cipsecspidirection (Enum Class)

                The direction of the SPI.

                .. data:: in_ = 1

                .. data:: out = 2

                """

                in_ = Enum.YLeaf(1, "in")

                out = Enum.YLeaf(2, "out")


            class Cipsecspiprotocol(Enum):
                """
                Cipsecspiprotocol (Enum Class)

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
                Cipsecspistatus (Enum Class)

                The status of the SPI.

                .. data:: active = 1

                .. data:: expiring = 2

                """

                active = Enum.YLeaf(1, "active")

                expiring = Enum.YLeaf(2, "expiring")



    class Cipsecphase2Gwstatstable(Entity):
        """
        Phase\-2 IPsec stats information is included in this table.
        Each entry is related to a specific gateway which is 
        identified by 'cmgwIndex'
        
        .. attribute:: cipsecphase2gwstatsentry
        
        	Each entry contains the attributes of an Phase\-2 IPsec stats information for the related gateway.  There is only one entry for each gateway. The entry  is created when a gateway up and cannot be deleted
        	**type**\: list of  		 :py:class:`Cipsecphase2Gwstatsentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecphase2Gwstatstable.Cipsecphase2Gwstatsentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsecphase2Gwstatstable, self).__init__()

            self.yang_name = "cipSecPhase2GWStatsTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipSecPhase2GWStatsEntry", ("cipsecphase2gwstatsentry", CISCOIPSECFLOWMONITORMIB.Cipsecphase2Gwstatstable.Cipsecphase2Gwstatsentry))])
            self._leafs = OrderedDict()

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
            
            .. attribute:: cmgwindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CISCOMEDIAGATEWAYMIB.Cmediagwtable.Cmediagwentry>`
            
            .. attribute:: cipsecphase2gwactivetunnels
            
            	The total number of currently active IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecphase2gwprevioustunnels
            
            	The total number of previously active IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Phase-2 Tunnels
            
            .. attribute:: cipsecphase2gwinoctets
            
            	The total number of octets received by all current and previous IPsec Phase\-2 Tunnels.  This value is accumulated BEFORE determining  whether or not the packet should be decompressed.  See also cipSecGlobalInOctWraps for the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsecphase2gwinoctwraps
            
            	The number of times the global octets received counter (cipSecGlobalInOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsecphase2gwindecompoctets
            
            	The total number of decompressed octets received by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated AFTER the packet is  decompressed. If compression is not being used,  this value will match the value of cipSecGlobalInOctets.  See also cipSecGlobalInDecompOctWraps for the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsecphase2gwindecompoctwraps
            
            	The number of times the global decompressed octets received counter (cipSecGlobalInDecompOctets)  has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsecphase2gwinpkts
            
            	The total number of packets received by all current and previous IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsecphase2gwindrops
            
            	The total number of packets dropped during receive processing by all current and previous  IPsec Phase\-2 Tunnels. This count does NOT include  packets dropped due to Anti\-Replay processing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsecphase2gwinreplaydrops
            
            	The total number of packets dropped during receive processing due to Anti\-Replay  processing by all current and previous IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsecphase2gwinauths
            
            	The total number of inbound authentication's performed by all current and previous IPsec  Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Events
            
            .. attribute:: cipsecphase2gwinauthfails
            
            	The total number of inbound authentication's which ended in failure by all current and previous  IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsecphase2gwindecrypts
            
            	The total number of inbound decryption's performed by all current and previous IPsec  Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsecphase2gwindecryptfails
            
            	The total number of inbound decryption's which ended in failure by all current and  previous IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsecphase2gwoutoctets
            
            	The total number of octets sent by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated AFTER determining  whether or not the packet should be compressed.   See also cipSecGlobalOutOctWraps for the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsecphase2gwoutoctwraps
            
            	The number of times the global octets sent counter (cipSecGlobalOutOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsecphase2gwoutuncompoctets
            
            	The total number of uncompressed octets sent by all current and previous IPsec Phase\-2 Tunnels.   This value is accumulated BEFORE the packet is  compressed. If compression is not being used, this  value will match the value of cipSecGlobalOutOctets.  See also cipSecGlobalOutDecompOctWraps for the number  of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsecphase2gwoutuncompoctwraps
            
            	The number of times the global uncompressed octets sent counter (cipSecGlobalOutUncompOctets)  has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsecphase2gwoutpkts
            
            	The total number of packets sent by all current and previous IPsec Phase\-2  Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsecphase2gwoutdrops
            
            	The total number of packets dropped during send processing by all current and previous IPsec  Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsecphase2gwoutauths
            
            	The total number of outbound authentication's performed by all current and previous IPsec  Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Events
            
            .. attribute:: cipsecphase2gwoutauthfails
            
            	The total number of outbound authentication's which ended in failure by all current and previous IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsecphase2gwoutencrypts
            
            	The total number of outbound encryption's performed by all current and previous IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsecphase2gwoutencryptfails
            
            	The total number of outbound encryption's which ended in failure by all current and  previous IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsecphase2gwprotocolusefails
            
            	The total number of protocol use failures which occurred during processing of all current  and previously active IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsecphase2gwnosafails
            
            	The total number of non\-existent Security Association in failures which occurred  during processing of all current and previous IPsec Phase\-2 Tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsecphase2gwsyscapfails
            
            	The total number of system capacity failures which occurred during processing of all current  and previously active IPsec Phase\-2 Tunnels
            	**type**\: int
            
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
                self.ylist_key_names = ['cmgwindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cmgwindex', YLeaf(YType.str, 'cmgwIndex')),
                    ('cipsecphase2gwactivetunnels', YLeaf(YType.uint32, 'cipSecPhase2GWActiveTunnels')),
                    ('cipsecphase2gwprevioustunnels', YLeaf(YType.uint32, 'cipSecPhase2GWPreviousTunnels')),
                    ('cipsecphase2gwinoctets', YLeaf(YType.uint32, 'cipSecPhase2GWInOctets')),
                    ('cipsecphase2gwinoctwraps', YLeaf(YType.uint32, 'cipSecPhase2GWInOctWraps')),
                    ('cipsecphase2gwindecompoctets', YLeaf(YType.uint32, 'cipSecPhase2GWInDecompOctets')),
                    ('cipsecphase2gwindecompoctwraps', YLeaf(YType.uint32, 'cipSecPhase2GWInDecompOctWraps')),
                    ('cipsecphase2gwinpkts', YLeaf(YType.uint32, 'cipSecPhase2GWInPkts')),
                    ('cipsecphase2gwindrops', YLeaf(YType.uint32, 'cipSecPhase2GWInDrops')),
                    ('cipsecphase2gwinreplaydrops', YLeaf(YType.uint32, 'cipSecPhase2GWInReplayDrops')),
                    ('cipsecphase2gwinauths', YLeaf(YType.uint32, 'cipSecPhase2GWInAuths')),
                    ('cipsecphase2gwinauthfails', YLeaf(YType.uint32, 'cipSecPhase2GWInAuthFails')),
                    ('cipsecphase2gwindecrypts', YLeaf(YType.uint32, 'cipSecPhase2GWInDecrypts')),
                    ('cipsecphase2gwindecryptfails', YLeaf(YType.uint32, 'cipSecPhase2GWInDecryptFails')),
                    ('cipsecphase2gwoutoctets', YLeaf(YType.uint32, 'cipSecPhase2GWOutOctets')),
                    ('cipsecphase2gwoutoctwraps', YLeaf(YType.uint32, 'cipSecPhase2GWOutOctWraps')),
                    ('cipsecphase2gwoutuncompoctets', YLeaf(YType.uint32, 'cipSecPhase2GWOutUncompOctets')),
                    ('cipsecphase2gwoutuncompoctwraps', YLeaf(YType.uint32, 'cipSecPhase2GWOutUncompOctWraps')),
                    ('cipsecphase2gwoutpkts', YLeaf(YType.uint32, 'cipSecPhase2GWOutPkts')),
                    ('cipsecphase2gwoutdrops', YLeaf(YType.uint32, 'cipSecPhase2GWOutDrops')),
                    ('cipsecphase2gwoutauths', YLeaf(YType.uint32, 'cipSecPhase2GWOutAuths')),
                    ('cipsecphase2gwoutauthfails', YLeaf(YType.uint32, 'cipSecPhase2GWOutAuthFails')),
                    ('cipsecphase2gwoutencrypts', YLeaf(YType.uint32, 'cipSecPhase2GWOutEncrypts')),
                    ('cipsecphase2gwoutencryptfails', YLeaf(YType.uint32, 'cipSecPhase2GWOutEncryptFails')),
                    ('cipsecphase2gwprotocolusefails', YLeaf(YType.uint32, 'cipSecPhase2GWProtocolUseFails')),
                    ('cipsecphase2gwnosafails', YLeaf(YType.uint32, 'cipSecPhase2GWNoSaFails')),
                    ('cipsecphase2gwsyscapfails', YLeaf(YType.uint32, 'cipSecPhase2GWSysCapFails')),
                ])
                self.cmgwindex = None
                self.cipsecphase2gwactivetunnels = None
                self.cipsecphase2gwprevioustunnels = None
                self.cipsecphase2gwinoctets = None
                self.cipsecphase2gwinoctwraps = None
                self.cipsecphase2gwindecompoctets = None
                self.cipsecphase2gwindecompoctwraps = None
                self.cipsecphase2gwinpkts = None
                self.cipsecphase2gwindrops = None
                self.cipsecphase2gwinreplaydrops = None
                self.cipsecphase2gwinauths = None
                self.cipsecphase2gwinauthfails = None
                self.cipsecphase2gwindecrypts = None
                self.cipsecphase2gwindecryptfails = None
                self.cipsecphase2gwoutoctets = None
                self.cipsecphase2gwoutoctwraps = None
                self.cipsecphase2gwoutuncompoctets = None
                self.cipsecphase2gwoutuncompoctwraps = None
                self.cipsecphase2gwoutpkts = None
                self.cipsecphase2gwoutdrops = None
                self.cipsecphase2gwoutauths = None
                self.cipsecphase2gwoutauthfails = None
                self.cipsecphase2gwoutencrypts = None
                self.cipsecphase2gwoutencryptfails = None
                self.cipsecphase2gwprotocolusefails = None
                self.cipsecphase2gwnosafails = None
                self.cipsecphase2gwsyscapfails = None
                self._segment_path = lambda: "cipSecPhase2GWStatsEntry" + "[cmgwIndex='" + str(self.cmgwindex) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecPhase2GWStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecphase2Gwstatstable.Cipsecphase2Gwstatsentry, ['cmgwindex', 'cipsecphase2gwactivetunnels', 'cipsecphase2gwprevioustunnels', 'cipsecphase2gwinoctets', 'cipsecphase2gwinoctwraps', 'cipsecphase2gwindecompoctets', 'cipsecphase2gwindecompoctwraps', 'cipsecphase2gwinpkts', 'cipsecphase2gwindrops', 'cipsecphase2gwinreplaydrops', 'cipsecphase2gwinauths', 'cipsecphase2gwinauthfails', 'cipsecphase2gwindecrypts', 'cipsecphase2gwindecryptfails', 'cipsecphase2gwoutoctets', 'cipsecphase2gwoutoctwraps', 'cipsecphase2gwoutuncompoctets', 'cipsecphase2gwoutuncompoctwraps', 'cipsecphase2gwoutpkts', 'cipsecphase2gwoutdrops', 'cipsecphase2gwoutauths', 'cipsecphase2gwoutauthfails', 'cipsecphase2gwoutencrypts', 'cipsecphase2gwoutencryptfails', 'cipsecphase2gwprotocolusefails', 'cipsecphase2gwnosafails', 'cipsecphase2gwsyscapfails'], name, value)


    class Ciketunnelhisttable(Entity):
        """
        The IPsec Phase\-1 Internet Key Exchange Tunnel
        History Table.  This table is implemented as a 
        sliding window in which only the last n entries 
        are maintained.  The maximum number of entries
         is specified by the cipSecHistTableSize object.
        
        .. attribute:: ciketunnelhistentry
        
        	Each entry contains the attributes associated with a previously active IPsec  Phase\-1 IKE Tunnel
        	**type**\: list of  		 :py:class:`Ciketunnelhistentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable.Ciketunnelhistentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable, self).__init__()

            self.yang_name = "cikeTunnelHistTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cikeTunnelHistEntry", ("ciketunnelhistentry", CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable.Ciketunnelhistentry))])
            self._leafs = OrderedDict()

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
            
            .. attribute:: ciketunhistindex  (key)
            
            	The index of the IPsec Phase\-1 IKE Tunnel History Table.  The value of the index is a number which  begins at one and is incremented with each  tunnel that ends. The value of this object  will wrap at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciketunhisttermreason
            
            	The reason the IPsec Phase\-1 IKE Tunnel was terminated. Possible reasons include\: 1 = other 2 = normal termination 3 = operator request 4 = peer delete request was received 5 = contact with peer was lost 6 = local failure occurred. 7 = operator initiated check point request
            	**type**\:  :py:class:`Ciketunhisttermreason <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable.Ciketunnelhistentry.Ciketunhisttermreason>`
            
            .. attribute:: ciketunhistactiveindex
            
            	The index of the previously active IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciketunhistpeerlocaltype
            
            	The type of local peer identity.  The local peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\:  :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: ciketunhistpeerlocalvalue
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\: str
            
            .. attribute:: ciketunhistpeerintindex
            
            	The internal index of the local\-remote peer association.  This internal index is used to  uniquely identify multiple associations between  the local and remote peer
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciketunhistpeerremotetype
            
            	The type of remote peer identity.  The remote peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\:  :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: ciketunhistpeerremotevalue
            
            	The value of the remote peer identity.  If the remote peer type is an IP Address, then this is the IP Address used to identify the remote peer.  If the remote peer type is a host name, then this is the host name used to identify the remote peer
            	**type**\: str
            
            .. attribute:: ciketunhistlocaladdr
            
            	The IP address of the local endpoint for the IPsec Phase\-1 IKE Tunnel
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: ciketunhistlocalname
            
            	The DNS name of the local IP address for the IPsec Phase\-1 IKE Tunnel. If the DNS  name associated with the local tunnel endpoint  is not known, then the value of this  object will be a NULL string
            	**type**\: str
            
            .. attribute:: ciketunhistremoteaddr
            
            	The IP address of the remote endpoint for the IPsec Phase\-1 IKE Tunnel
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: ciketunhistremotename
            
            	The DNS name of the remote IP address of IPsec Phase\-1 IKE Tunnel. If the DNS name associated with the remote tunnel endpoint is not known, then the value of this object will be a NULL string
            	**type**\: str
            
            .. attribute:: ciketunhistnegomode
            
            	The negotiation mode of the IPsec Phase\-1 IKE Tunnel
            	**type**\:  :py:class:`IkeNegoMode <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeNegoMode>`
            
            .. attribute:: ciketunhistdiffhellmangrp
            
            	The Diffie Hellman Group used in IPsec Phase\-1 IKE negotiations
            	**type**\:  :py:class:`DiffHellmanGrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp>`
            
            .. attribute:: ciketunhistencryptalgo
            
            	The encryption algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\:  :py:class:`EncryptAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo>`
            
            .. attribute:: ciketunhisthashalgo
            
            	The hash algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\:  :py:class:`IkeHashAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeHashAlgo>`
            
            .. attribute:: ciketunhistauthmethod
            
            	The authentication method used in IPsec Phase\-1 IKE negotiations
            	**type**\:  :py:class:`IkeAuthMethod <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeAuthMethod>`
            
            .. attribute:: ciketunhistlifetime
            
            	The negotiated LifeTime of the IPsec Phase\-1 IKE Tunnel in seconds
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciketunhiststarttime
            
            	The value of sysUpTime in hundredths of seconds when the IPsec Phase\-1 IKE tunnel was started
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciketunhistactivetime
            
            	The length of time the IPsec Phase\-1 IKE tunnel was been active in hundredths of seconds
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciketunhisttotalrefreshes
            
            	The total number of security associations refreshes performed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: QM Exchanges
            
            .. attribute:: ciketunhisttotalsas
            
            	The total number of security associations used during the  life of the IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SAs
            
            .. attribute:: ciketunhistinoctets
            
            	The total number of octets received by this IPsec Phase\-1  IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: ciketunhistinpkts
            
            	The total number of packets received by this IPsec Phase\-1  IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: ciketunhistindroppkts
            
            	The total number of packets dropped by this IPsec Phase\-1  IKE Tunnel during receive processing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: ciketunhistinnotifys
            
            	The total number of notifys received by this IPsec Phase\-1  IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: ciketunhistinp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges received by  this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunhistinp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges received and  found to be invalid by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunhistinp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges received and  rejected by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunhistinp2sadelrequests
            
            	The total number of IPsec Phase\-2 security association delete requests received by this IPsec  Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: ciketunhistoutoctets
            
            	The total number of octets sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: ciketunhistoutpkts
            
            	The total number of packets sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: ciketunhistoutdroppkts
            
            	The total number of packets dropped by this IPsec Phase\-1  IKE Tunnel during send processing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: ciketunhistoutnotifys
            
            	The total number of notifys sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            .. attribute:: ciketunhistoutp2exchgs
            
            	The total number of IPsec Phase\-2 exchanges sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunhistoutp2exchginvalids
            
            	The total number of IPsec Phase\-2 exchanges sent and found to be invalid by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunhistoutp2exchgrejects
            
            	The total number of IPsec Phase\-2 exchanges sent and rejected by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SA Payloads
            
            .. attribute:: ciketunhistoutp2sadelrequests
            
            	The total number of IPsec Phase\-2 security association delete requests sent by this IPsec Phase\-1 IKE Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Notification Payloads
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable.Ciketunnelhistentry, self).__init__()

                self.yang_name = "cikeTunnelHistEntry"
                self.yang_parent_name = "cikeTunnelHistTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciketunhistindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciketunhistindex', YLeaf(YType.int32, 'cikeTunHistIndex')),
                    ('ciketunhisttermreason', YLeaf(YType.enumeration, 'cikeTunHistTermReason')),
                    ('ciketunhistactiveindex', YLeaf(YType.int32, 'cikeTunHistActiveIndex')),
                    ('ciketunhistpeerlocaltype', YLeaf(YType.enumeration, 'cikeTunHistPeerLocalType')),
                    ('ciketunhistpeerlocalvalue', YLeaf(YType.str, 'cikeTunHistPeerLocalValue')),
                    ('ciketunhistpeerintindex', YLeaf(YType.int32, 'cikeTunHistPeerIntIndex')),
                    ('ciketunhistpeerremotetype', YLeaf(YType.enumeration, 'cikeTunHistPeerRemoteType')),
                    ('ciketunhistpeerremotevalue', YLeaf(YType.str, 'cikeTunHistPeerRemoteValue')),
                    ('ciketunhistlocaladdr', YLeaf(YType.str, 'cikeTunHistLocalAddr')),
                    ('ciketunhistlocalname', YLeaf(YType.str, 'cikeTunHistLocalName')),
                    ('ciketunhistremoteaddr', YLeaf(YType.str, 'cikeTunHistRemoteAddr')),
                    ('ciketunhistremotename', YLeaf(YType.str, 'cikeTunHistRemoteName')),
                    ('ciketunhistnegomode', YLeaf(YType.enumeration, 'cikeTunHistNegoMode')),
                    ('ciketunhistdiffhellmangrp', YLeaf(YType.enumeration, 'cikeTunHistDiffHellmanGrp')),
                    ('ciketunhistencryptalgo', YLeaf(YType.enumeration, 'cikeTunHistEncryptAlgo')),
                    ('ciketunhisthashalgo', YLeaf(YType.enumeration, 'cikeTunHistHashAlgo')),
                    ('ciketunhistauthmethod', YLeaf(YType.enumeration, 'cikeTunHistAuthMethod')),
                    ('ciketunhistlifetime', YLeaf(YType.int32, 'cikeTunHistLifeTime')),
                    ('ciketunhiststarttime', YLeaf(YType.uint32, 'cikeTunHistStartTime')),
                    ('ciketunhistactivetime', YLeaf(YType.int32, 'cikeTunHistActiveTime')),
                    ('ciketunhisttotalrefreshes', YLeaf(YType.uint32, 'cikeTunHistTotalRefreshes')),
                    ('ciketunhisttotalsas', YLeaf(YType.uint32, 'cikeTunHistTotalSas')),
                    ('ciketunhistinoctets', YLeaf(YType.uint32, 'cikeTunHistInOctets')),
                    ('ciketunhistinpkts', YLeaf(YType.uint32, 'cikeTunHistInPkts')),
                    ('ciketunhistindroppkts', YLeaf(YType.uint32, 'cikeTunHistInDropPkts')),
                    ('ciketunhistinnotifys', YLeaf(YType.uint32, 'cikeTunHistInNotifys')),
                    ('ciketunhistinp2exchgs', YLeaf(YType.uint32, 'cikeTunHistInP2Exchgs')),
                    ('ciketunhistinp2exchginvalids', YLeaf(YType.uint32, 'cikeTunHistInP2ExchgInvalids')),
                    ('ciketunhistinp2exchgrejects', YLeaf(YType.uint32, 'cikeTunHistInP2ExchgRejects')),
                    ('ciketunhistinp2sadelrequests', YLeaf(YType.uint32, 'cikeTunHistInP2SaDelRequests')),
                    ('ciketunhistoutoctets', YLeaf(YType.uint32, 'cikeTunHistOutOctets')),
                    ('ciketunhistoutpkts', YLeaf(YType.uint32, 'cikeTunHistOutPkts')),
                    ('ciketunhistoutdroppkts', YLeaf(YType.uint32, 'cikeTunHistOutDropPkts')),
                    ('ciketunhistoutnotifys', YLeaf(YType.uint32, 'cikeTunHistOutNotifys')),
                    ('ciketunhistoutp2exchgs', YLeaf(YType.uint32, 'cikeTunHistOutP2Exchgs')),
                    ('ciketunhistoutp2exchginvalids', YLeaf(YType.uint32, 'cikeTunHistOutP2ExchgInvalids')),
                    ('ciketunhistoutp2exchgrejects', YLeaf(YType.uint32, 'cikeTunHistOutP2ExchgRejects')),
                    ('ciketunhistoutp2sadelrequests', YLeaf(YType.uint32, 'cikeTunHistOutP2SaDelRequests')),
                ])
                self.ciketunhistindex = None
                self.ciketunhisttermreason = None
                self.ciketunhistactiveindex = None
                self.ciketunhistpeerlocaltype = None
                self.ciketunhistpeerlocalvalue = None
                self.ciketunhistpeerintindex = None
                self.ciketunhistpeerremotetype = None
                self.ciketunhistpeerremotevalue = None
                self.ciketunhistlocaladdr = None
                self.ciketunhistlocalname = None
                self.ciketunhistremoteaddr = None
                self.ciketunhistremotename = None
                self.ciketunhistnegomode = None
                self.ciketunhistdiffhellmangrp = None
                self.ciketunhistencryptalgo = None
                self.ciketunhisthashalgo = None
                self.ciketunhistauthmethod = None
                self.ciketunhistlifetime = None
                self.ciketunhiststarttime = None
                self.ciketunhistactivetime = None
                self.ciketunhisttotalrefreshes = None
                self.ciketunhisttotalsas = None
                self.ciketunhistinoctets = None
                self.ciketunhistinpkts = None
                self.ciketunhistindroppkts = None
                self.ciketunhistinnotifys = None
                self.ciketunhistinp2exchgs = None
                self.ciketunhistinp2exchginvalids = None
                self.ciketunhistinp2exchgrejects = None
                self.ciketunhistinp2sadelrequests = None
                self.ciketunhistoutoctets = None
                self.ciketunhistoutpkts = None
                self.ciketunhistoutdroppkts = None
                self.ciketunhistoutnotifys = None
                self.ciketunhistoutp2exchgs = None
                self.ciketunhistoutp2exchginvalids = None
                self.ciketunhistoutp2exchgrejects = None
                self.ciketunhistoutp2sadelrequests = None
                self._segment_path = lambda: "cikeTunnelHistEntry" + "[cikeTunHistIndex='" + str(self.ciketunhistindex) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikeTunnelHistTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Ciketunnelhisttable.Ciketunnelhistentry, ['ciketunhistindex', 'ciketunhisttermreason', 'ciketunhistactiveindex', 'ciketunhistpeerlocaltype', 'ciketunhistpeerlocalvalue', 'ciketunhistpeerintindex', 'ciketunhistpeerremotetype', 'ciketunhistpeerremotevalue', 'ciketunhistlocaladdr', 'ciketunhistlocalname', 'ciketunhistremoteaddr', 'ciketunhistremotename', 'ciketunhistnegomode', 'ciketunhistdiffhellmangrp', 'ciketunhistencryptalgo', 'ciketunhisthashalgo', 'ciketunhistauthmethod', 'ciketunhistlifetime', 'ciketunhiststarttime', 'ciketunhistactivetime', 'ciketunhisttotalrefreshes', 'ciketunhisttotalsas', 'ciketunhistinoctets', 'ciketunhistinpkts', 'ciketunhistindroppkts', 'ciketunhistinnotifys', 'ciketunhistinp2exchgs', 'ciketunhistinp2exchginvalids', 'ciketunhistinp2exchgrejects', 'ciketunhistinp2sadelrequests', 'ciketunhistoutoctets', 'ciketunhistoutpkts', 'ciketunhistoutdroppkts', 'ciketunhistoutnotifys', 'ciketunhistoutp2exchgs', 'ciketunhistoutp2exchginvalids', 'ciketunhistoutp2exchgrejects', 'ciketunhistoutp2sadelrequests'], name, value)

            class Ciketunhisttermreason(Enum):
                """
                Ciketunhisttermreason (Enum Class)

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
        	**type**\: list of  		 :py:class:`Cipsectunnelhistentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable.Cipsectunnelhistentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable, self).__init__()

            self.yang_name = "cipSecTunnelHistTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipSecTunnelHistEntry", ("cipsectunnelhistentry", CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable.Cipsectunnelhistentry))])
            self._leafs = OrderedDict()

            self.cipsectunnelhistentry = YList(self)
            self._segment_path = lambda: "cipSecTunnelHistTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable, [], name, value)


        class Cipsectunnelhistentry(Entity):
            """
            Each entry contains the attributes associated with
            a previously active IPsec Phase\-2 Tunnel.
            
            .. attribute:: cipsectunhistindex  (key)
            
            	The index of the IPsec Phase\-2 Tunnel History Table. The value of the index is a number which  begins at one and is incremented with each tunnel  that ends. The value of this object will wrap at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunhisttermreason
            
            	The reason the IPsec Phase\-2 Tunnel was terminated. Possible reasons include\: 1 = other 2 = normal termination 3 = operator request 4 = peer delete request was received 5 = contact with peer was lost 6 = local failure occurred 7 = operator initiated check point request
            	**type**\:  :py:class:`Cipsectunhisttermreason <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable.Cipsectunnelhistentry.Cipsectunhisttermreason>`
            
            .. attribute:: cipsectunhistactiveindex
            
            	The index of the previously active IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunhistiketunnelindex
            
            	The index of the associated IPsec Phase\-1 Tunnel (cikeTunIndex in the cikeTunnelTable)
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsectunhistlocaladdr
            
            	The IP address of the local endpoint for the IPsec Phase\-2 Tunnel
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsectunhistremoteaddr
            
            	The IP address of the remote endpoint for the IPsec Phase\-2 Tunnel
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsectunhistkeytype
            
            	The type of key used by the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`KeyType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.KeyType>`
            
            .. attribute:: cipsectunhistencapmode
            
            	The encapsulation mode used by the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`EncapMode <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncapMode>`
            
            .. attribute:: cipsectunhistlifesize
            
            	The negotiated LifeSize of the IPsec Phase\-2 Tunnel in kilobytes
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**units**\: KBytes
            
            .. attribute:: cipsectunhistlifetime
            
            	The negotiated LifeTime of the IPsec Phase\-2 Tunnel in seconds
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**units**\: Seconds
            
            .. attribute:: cipsectunhiststarttime
            
            	The value of sysUpTime in hundredths of seconds when the IPsec Phase\-2 Tunnel was started
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsectunhistactivetime
            
            	The length of time the IPsec Phase\-2 Tunnel has been active in hundredths of seconds
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cipsectunhisttotalrefreshes
            
            	The total number of security association refreshes performed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: QM Exchanges
            
            .. attribute:: cipsectunhisttotalsas
            
            	The total number of security associations used during the  life of the IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: SAs
            
            .. attribute:: cipsectunhistinsadiffhellmangrp
            
            	The Diffie Hellman Group used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`DiffHellmanGrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp>`
            
            .. attribute:: cipsectunhistinsaencryptalgo
            
            	The encryption algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`EncryptAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo>`
            
            .. attribute:: cipsectunhistinsaahauthalgo
            
            	The authentication algorithm used by the inbound authentication header (AH) security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`AuthAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo>`
            
            .. attribute:: cipsectunhistinsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP)  security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`AuthAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo>`
            
            .. attribute:: cipsectunhistinsadecompalgo
            
            	The decompression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`CompAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CompAlgo>`
            
            .. attribute:: cipsectunhistoutsadiffhellmangrp
            
            	The Diffie Hellman Group used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`DiffHellmanGrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffHellmanGrp>`
            
            .. attribute:: cipsectunhistoutsaencryptalgo
            
            	The encryption algorithm used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`EncryptAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptAlgo>`
            
            .. attribute:: cipsectunhistoutsaahauthalgo
            
            	The authentication algorithm used by the outbound authentication header (AH) security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`AuthAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo>`
            
            .. attribute:: cipsectunhistoutsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP)  security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`AuthAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthAlgo>`
            
            .. attribute:: cipsectunhistoutsacompalgo
            
            	The compression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:  :py:class:`CompAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CompAlgo>`
            
            .. attribute:: cipsectunhistinoctets
            
            	The total number of octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated BEFORE determining whether or not the packet should  be decompressed.  See also cipSecTunInOctWraps for  the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsectunhisthcinoctets
            
            	A high capacity count of the total number of octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated BEFORE determining whether or not  the packet should be decompressed
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunhistinoctwraps
            
            	The number of times the octets received counter (cipSecTunInOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsectunhistindecompoctets
            
            	The total number of decompressed octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER the packet is decompressed. If compression is not being used, this value will match the value of cipSecTunHistInOctets. See also cipSecTunInDecompOctWraps for the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsectunhisthcindecompoctets
            
            	A high capacity count of the total number of decompressed octets received by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER the packet is decompressed. If compression is not being used, this value will match the value of cipSecTunHistHcInOctets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunhistindecompoctwraps
            
            	The number of times the decompressed octets received counter (cipSecTunInDecompOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsectunhistinpkts
            
            	The total number of packets received by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunhistindroppkts
            
            	The total number of packets dropped during receive processing by this IPsec Phase\-2 Tunnel.  This count does NOT include packets  dropped due to Anti\-Replay processing
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunhistinreplaydroppkts
            
            	The total number of packets dropped during receive processing due to Anti\-Replay processing  by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunhistinauths
            
            	The total number of inbound authentication's performed  by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Events
            
            .. attribute:: cipsectunhistinauthfails
            
            	The total number of inbound authentication's which ended in  failure by this IPsec Phase\-2 Tunnel 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsectunhistindecrypts
            
            	The total number of inbound decryption's performed by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunhistindecryptfails
            
            	The total number of inbound decryption's which ended in failure  by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsectunhistoutoctets
            
            	The total number of octets sent by this IPsec Phase\-2 Tunnel.  This value is accumulated AFTER determining whether or not the  packet should be compressed.  See also cipSecTunOutOctWraps for the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsectunhisthcoutoctets
            
            	A high capacity count of the total number of octets sent by this IPsec Phase\-2 Tunnel.  This value  is accumulated AFTER determining whether or not  the packet should be compressed
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cipsectunhistoutoctwraps
            
            	The number of times the octets sent counter (cipSecTunOutOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsectunhistoutuncompoctets
            
            	The total number of uncompressed octets sent by this IPsec Phase\-2 Tunnel.  This value is accumulated BEFORE the packet is compressed. If compression is not being used, this value will match the value of  cipSecTunHistOutOctets.  See also  cipSecTunOutDecompOctWraps for the number of times this counter has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Octets
            
            .. attribute:: cipsectunhisthcoutuncompoctets
            
            	A high capacity count of the total number of uncompressed octets sent by this  IPsec Phase\-2 Tunnel.  This value is accumulated  BEFORE the packet is compressed. If compression is not being used, this value will match the value of cipSecTunHistHcOutOctets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: Octets
            
            .. attribute:: cipsectunhistoutuncompoctwraps
            
            	The number of times the uncompressed octets sent counter (cipSecTunOutUncompOctets) has wrapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Integral units
            
            .. attribute:: cipsectunhistoutpkts
            
            	The total number of packets sent by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunhistoutdroppkts
            
            	The total number of packets dropped during send processing  by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunhistoutauths
            
            	The total number of outbound authentication's performed by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Events
            
            .. attribute:: cipsectunhistoutauthfails
            
            	The total number of outbound authentication's which ended in  failure by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            .. attribute:: cipsectunhistoutencrypts
            
            	The total number of outbound encryption's performed by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Packets
            
            .. attribute:: cipsectunhistoutencryptfails
            
            	The total number of outbound encryption's which ended in failure  by this IPsec Phase\-2 Tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Failures
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable.Cipsectunnelhistentry, self).__init__()

                self.yang_name = "cipSecTunnelHistEntry"
                self.yang_parent_name = "cipSecTunnelHistTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipsectunhistindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipsectunhistindex', YLeaf(YType.int32, 'cipSecTunHistIndex')),
                    ('cipsectunhisttermreason', YLeaf(YType.enumeration, 'cipSecTunHistTermReason')),
                    ('cipsectunhistactiveindex', YLeaf(YType.int32, 'cipSecTunHistActiveIndex')),
                    ('cipsectunhistiketunnelindex', YLeaf(YType.int32, 'cipSecTunHistIkeTunnelIndex')),
                    ('cipsectunhistlocaladdr', YLeaf(YType.str, 'cipSecTunHistLocalAddr')),
                    ('cipsectunhistremoteaddr', YLeaf(YType.str, 'cipSecTunHistRemoteAddr')),
                    ('cipsectunhistkeytype', YLeaf(YType.enumeration, 'cipSecTunHistKeyType')),
                    ('cipsectunhistencapmode', YLeaf(YType.enumeration, 'cipSecTunHistEncapMode')),
                    ('cipsectunhistlifesize', YLeaf(YType.int32, 'cipSecTunHistLifeSize')),
                    ('cipsectunhistlifetime', YLeaf(YType.int32, 'cipSecTunHistLifeTime')),
                    ('cipsectunhiststarttime', YLeaf(YType.uint32, 'cipSecTunHistStartTime')),
                    ('cipsectunhistactivetime', YLeaf(YType.int32, 'cipSecTunHistActiveTime')),
                    ('cipsectunhisttotalrefreshes', YLeaf(YType.uint32, 'cipSecTunHistTotalRefreshes')),
                    ('cipsectunhisttotalsas', YLeaf(YType.uint32, 'cipSecTunHistTotalSas')),
                    ('cipsectunhistinsadiffhellmangrp', YLeaf(YType.enumeration, 'cipSecTunHistInSaDiffHellmanGrp')),
                    ('cipsectunhistinsaencryptalgo', YLeaf(YType.enumeration, 'cipSecTunHistInSaEncryptAlgo')),
                    ('cipsectunhistinsaahauthalgo', YLeaf(YType.enumeration, 'cipSecTunHistInSaAhAuthAlgo')),
                    ('cipsectunhistinsaespauthalgo', YLeaf(YType.enumeration, 'cipSecTunHistInSaEspAuthAlgo')),
                    ('cipsectunhistinsadecompalgo', YLeaf(YType.enumeration, 'cipSecTunHistInSaDecompAlgo')),
                    ('cipsectunhistoutsadiffhellmangrp', YLeaf(YType.enumeration, 'cipSecTunHistOutSaDiffHellmanGrp')),
                    ('cipsectunhistoutsaencryptalgo', YLeaf(YType.enumeration, 'cipSecTunHistOutSaEncryptAlgo')),
                    ('cipsectunhistoutsaahauthalgo', YLeaf(YType.enumeration, 'cipSecTunHistOutSaAhAuthAlgo')),
                    ('cipsectunhistoutsaespauthalgo', YLeaf(YType.enumeration, 'cipSecTunHistOutSaEspAuthAlgo')),
                    ('cipsectunhistoutsacompalgo', YLeaf(YType.enumeration, 'cipSecTunHistOutSaCompAlgo')),
                    ('cipsectunhistinoctets', YLeaf(YType.uint32, 'cipSecTunHistInOctets')),
                    ('cipsectunhisthcinoctets', YLeaf(YType.uint64, 'cipSecTunHistHcInOctets')),
                    ('cipsectunhistinoctwraps', YLeaf(YType.uint32, 'cipSecTunHistInOctWraps')),
                    ('cipsectunhistindecompoctets', YLeaf(YType.uint32, 'cipSecTunHistInDecompOctets')),
                    ('cipsectunhisthcindecompoctets', YLeaf(YType.uint64, 'cipSecTunHistHcInDecompOctets')),
                    ('cipsectunhistindecompoctwraps', YLeaf(YType.uint32, 'cipSecTunHistInDecompOctWraps')),
                    ('cipsectunhistinpkts', YLeaf(YType.uint32, 'cipSecTunHistInPkts')),
                    ('cipsectunhistindroppkts', YLeaf(YType.uint32, 'cipSecTunHistInDropPkts')),
                    ('cipsectunhistinreplaydroppkts', YLeaf(YType.uint32, 'cipSecTunHistInReplayDropPkts')),
                    ('cipsectunhistinauths', YLeaf(YType.uint32, 'cipSecTunHistInAuths')),
                    ('cipsectunhistinauthfails', YLeaf(YType.uint32, 'cipSecTunHistInAuthFails')),
                    ('cipsectunhistindecrypts', YLeaf(YType.uint32, 'cipSecTunHistInDecrypts')),
                    ('cipsectunhistindecryptfails', YLeaf(YType.uint32, 'cipSecTunHistInDecryptFails')),
                    ('cipsectunhistoutoctets', YLeaf(YType.uint32, 'cipSecTunHistOutOctets')),
                    ('cipsectunhisthcoutoctets', YLeaf(YType.uint64, 'cipSecTunHistHcOutOctets')),
                    ('cipsectunhistoutoctwraps', YLeaf(YType.uint32, 'cipSecTunHistOutOctWraps')),
                    ('cipsectunhistoutuncompoctets', YLeaf(YType.uint32, 'cipSecTunHistOutUncompOctets')),
                    ('cipsectunhisthcoutuncompoctets', YLeaf(YType.uint64, 'cipSecTunHistHcOutUncompOctets')),
                    ('cipsectunhistoutuncompoctwraps', YLeaf(YType.uint32, 'cipSecTunHistOutUncompOctWraps')),
                    ('cipsectunhistoutpkts', YLeaf(YType.uint32, 'cipSecTunHistOutPkts')),
                    ('cipsectunhistoutdroppkts', YLeaf(YType.uint32, 'cipSecTunHistOutDropPkts')),
                    ('cipsectunhistoutauths', YLeaf(YType.uint32, 'cipSecTunHistOutAuths')),
                    ('cipsectunhistoutauthfails', YLeaf(YType.uint32, 'cipSecTunHistOutAuthFails')),
                    ('cipsectunhistoutencrypts', YLeaf(YType.uint32, 'cipSecTunHistOutEncrypts')),
                    ('cipsectunhistoutencryptfails', YLeaf(YType.uint32, 'cipSecTunHistOutEncryptFails')),
                ])
                self.cipsectunhistindex = None
                self.cipsectunhisttermreason = None
                self.cipsectunhistactiveindex = None
                self.cipsectunhistiketunnelindex = None
                self.cipsectunhistlocaladdr = None
                self.cipsectunhistremoteaddr = None
                self.cipsectunhistkeytype = None
                self.cipsectunhistencapmode = None
                self.cipsectunhistlifesize = None
                self.cipsectunhistlifetime = None
                self.cipsectunhiststarttime = None
                self.cipsectunhistactivetime = None
                self.cipsectunhisttotalrefreshes = None
                self.cipsectunhisttotalsas = None
                self.cipsectunhistinsadiffhellmangrp = None
                self.cipsectunhistinsaencryptalgo = None
                self.cipsectunhistinsaahauthalgo = None
                self.cipsectunhistinsaespauthalgo = None
                self.cipsectunhistinsadecompalgo = None
                self.cipsectunhistoutsadiffhellmangrp = None
                self.cipsectunhistoutsaencryptalgo = None
                self.cipsectunhistoutsaahauthalgo = None
                self.cipsectunhistoutsaespauthalgo = None
                self.cipsectunhistoutsacompalgo = None
                self.cipsectunhistinoctets = None
                self.cipsectunhisthcinoctets = None
                self.cipsectunhistinoctwraps = None
                self.cipsectunhistindecompoctets = None
                self.cipsectunhisthcindecompoctets = None
                self.cipsectunhistindecompoctwraps = None
                self.cipsectunhistinpkts = None
                self.cipsectunhistindroppkts = None
                self.cipsectunhistinreplaydroppkts = None
                self.cipsectunhistinauths = None
                self.cipsectunhistinauthfails = None
                self.cipsectunhistindecrypts = None
                self.cipsectunhistindecryptfails = None
                self.cipsectunhistoutoctets = None
                self.cipsectunhisthcoutoctets = None
                self.cipsectunhistoutoctwraps = None
                self.cipsectunhistoutuncompoctets = None
                self.cipsectunhisthcoutuncompoctets = None
                self.cipsectunhistoutuncompoctwraps = None
                self.cipsectunhistoutpkts = None
                self.cipsectunhistoutdroppkts = None
                self.cipsectunhistoutauths = None
                self.cipsectunhistoutauthfails = None
                self.cipsectunhistoutencrypts = None
                self.cipsectunhistoutencryptfails = None
                self._segment_path = lambda: "cipSecTunnelHistEntry" + "[cipSecTunHistIndex='" + str(self.cipsectunhistindex) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecTunnelHistTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsectunnelhisttable.Cipsectunnelhistentry, ['cipsectunhistindex', 'cipsectunhisttermreason', 'cipsectunhistactiveindex', 'cipsectunhistiketunnelindex', 'cipsectunhistlocaladdr', 'cipsectunhistremoteaddr', 'cipsectunhistkeytype', 'cipsectunhistencapmode', 'cipsectunhistlifesize', 'cipsectunhistlifetime', 'cipsectunhiststarttime', 'cipsectunhistactivetime', 'cipsectunhisttotalrefreshes', 'cipsectunhisttotalsas', 'cipsectunhistinsadiffhellmangrp', 'cipsectunhistinsaencryptalgo', 'cipsectunhistinsaahauthalgo', 'cipsectunhistinsaespauthalgo', 'cipsectunhistinsadecompalgo', 'cipsectunhistoutsadiffhellmangrp', 'cipsectunhistoutsaencryptalgo', 'cipsectunhistoutsaahauthalgo', 'cipsectunhistoutsaespauthalgo', 'cipsectunhistoutsacompalgo', 'cipsectunhistinoctets', 'cipsectunhisthcinoctets', 'cipsectunhistinoctwraps', 'cipsectunhistindecompoctets', 'cipsectunhisthcindecompoctets', 'cipsectunhistindecompoctwraps', 'cipsectunhistinpkts', 'cipsectunhistindroppkts', 'cipsectunhistinreplaydroppkts', 'cipsectunhistinauths', 'cipsectunhistinauthfails', 'cipsectunhistindecrypts', 'cipsectunhistindecryptfails', 'cipsectunhistoutoctets', 'cipsectunhisthcoutoctets', 'cipsectunhistoutoctwraps', 'cipsectunhistoutuncompoctets', 'cipsectunhisthcoutuncompoctets', 'cipsectunhistoutuncompoctwraps', 'cipsectunhistoutpkts', 'cipsectunhistoutdroppkts', 'cipsectunhistoutauths', 'cipsectunhistoutauthfails', 'cipsectunhistoutencrypts', 'cipsectunhistoutencryptfails'], name, value)

            class Cipsectunhisttermreason(Enum):
                """
                Cipsectunhisttermreason (Enum Class)

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
        	**type**\: list of  		 :py:class:`Cipsecendpthistentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable.Cipsecendpthistentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable, self).__init__()

            self.yang_name = "cipSecEndPtHistTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipSecEndPtHistEntry", ("cipsecendpthistentry", CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable.Cipsecendpthistentry))])
            self._leafs = OrderedDict()

            self.cipsecendpthistentry = YList(self)
            self._segment_path = lambda: "cipSecEndPtHistTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable, [], name, value)


        class Cipsecendpthistentry(Entity):
            """
            Each entry contains the attributes associated with
            a previously active IPsec Phase\-2 Tunnel Endpoint.
            
            .. attribute:: cipsecendpthistindex  (key)
            
            	The number of the previously active Endpoint associated  with a IPsec Phase\-2 Tunnel Table.  The value   of this index is a number which begins at   one and is incremented with each Endpoint   associated with an IPsec Phase\-2 Tunnel.  The value of this object will wrap at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecendpthisttunindex
            
            	The index  of the previously active IPsec Phase\-2 Tunnel Table
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecendpthistactiveindex
            
            	The index  of the previously active Endpoint
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecendpthistlocalname
            
            	The DNS name of the local Endpoint
            	**type**\: str
            
            .. attribute:: cipsecendpthistlocaltype
            
            	The type of identity for the local Endpoint. Possible values are\: 1) a single IP address, or 2) an IP address range, or 3) an IP subnet
            	**type**\:  :py:class:`EndPtType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EndPtType>`
            
            .. attribute:: cipsecendpthistlocaladdr1
            
            	The local Endpoint's first IP address specification.  If the local Endpoint type is single IP address,  then this is the value of the IP address.  If the local Endpoint type is IP subnet, then this is the value of the subnet.  If the local Endpoint type is IP address range,  then this is the value of beginning IP address of  the range
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecendpthistlocaladdr2
            
            	The local Endpoint's second IP address specification.  If the local Endpoint type is single IP address,  then this is the value of the IP address.  If the local Endpoint type is IP subnet, then this is the value of the subnet mask.  If the local Endpoint type is IP address range,  then this is the value of ending IP address of the range
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecendpthistlocalprotocol
            
            	The protocol number of the local Endpoint's traffic
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cipsecendpthistlocalport
            
            	The port number of the local Endpoint's traffic
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cipsecendpthistremotename
            
            	The DNS name of the remote Endpoint
            	**type**\: str
            
            .. attribute:: cipsecendpthistremotetype
            
            	The type of identity for the remote Endpoint. Possible values are\: 1) a single IP address, or 2) an IP address range, or 3) an IP subnet
            	**type**\:  :py:class:`EndPtType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EndPtType>`
            
            .. attribute:: cipsecendpthistremoteaddr1
            
            	The remote Endpoint's first IP address specification.  If the remote Endpoint type is single IP address,  then this is the value of the IP address.  If the remote Endpoint type is IP subnet, then this is the value of the subnet.  If the remote Endpoint type is IP address range,  then this is the value of beginning IP address of the range
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecendpthistremoteaddr2
            
            	The remote Endpoint's second IP address specification.  If the remote Endpoint type is single IP address,  then this is the value of the IP address.  If the remote Endpoint type is IP subnet, then this is the value of the subnet mask.  If the remote Endpoint type is IP address range,  then this is the value of ending IP address of the range
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecendpthistremoteprotocol
            
            	The protocol number of the remote Endpoint's traffic
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cipsecendpthistremoteport
            
            	The port number of the remote Endpoint's traffic
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable.Cipsecendpthistentry, self).__init__()

                self.yang_name = "cipSecEndPtHistEntry"
                self.yang_parent_name = "cipSecEndPtHistTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipsecendpthistindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipsecendpthistindex', YLeaf(YType.int32, 'cipSecEndPtHistIndex')),
                    ('cipsecendpthisttunindex', YLeaf(YType.int32, 'cipSecEndPtHistTunIndex')),
                    ('cipsecendpthistactiveindex', YLeaf(YType.int32, 'cipSecEndPtHistActiveIndex')),
                    ('cipsecendpthistlocalname', YLeaf(YType.str, 'cipSecEndPtHistLocalName')),
                    ('cipsecendpthistlocaltype', YLeaf(YType.enumeration, 'cipSecEndPtHistLocalType')),
                    ('cipsecendpthistlocaladdr1', YLeaf(YType.str, 'cipSecEndPtHistLocalAddr1')),
                    ('cipsecendpthistlocaladdr2', YLeaf(YType.str, 'cipSecEndPtHistLocalAddr2')),
                    ('cipsecendpthistlocalprotocol', YLeaf(YType.int32, 'cipSecEndPtHistLocalProtocol')),
                    ('cipsecendpthistlocalport', YLeaf(YType.int32, 'cipSecEndPtHistLocalPort')),
                    ('cipsecendpthistremotename', YLeaf(YType.str, 'cipSecEndPtHistRemoteName')),
                    ('cipsecendpthistremotetype', YLeaf(YType.enumeration, 'cipSecEndPtHistRemoteType')),
                    ('cipsecendpthistremoteaddr1', YLeaf(YType.str, 'cipSecEndPtHistRemoteAddr1')),
                    ('cipsecendpthistremoteaddr2', YLeaf(YType.str, 'cipSecEndPtHistRemoteAddr2')),
                    ('cipsecendpthistremoteprotocol', YLeaf(YType.int32, 'cipSecEndPtHistRemoteProtocol')),
                    ('cipsecendpthistremoteport', YLeaf(YType.int32, 'cipSecEndPtHistRemotePort')),
                ])
                self.cipsecendpthistindex = None
                self.cipsecendpthisttunindex = None
                self.cipsecendpthistactiveindex = None
                self.cipsecendpthistlocalname = None
                self.cipsecendpthistlocaltype = None
                self.cipsecendpthistlocaladdr1 = None
                self.cipsecendpthistlocaladdr2 = None
                self.cipsecendpthistlocalprotocol = None
                self.cipsecendpthistlocalport = None
                self.cipsecendpthistremotename = None
                self.cipsecendpthistremotetype = None
                self.cipsecendpthistremoteaddr1 = None
                self.cipsecendpthistremoteaddr2 = None
                self.cipsecendpthistremoteprotocol = None
                self.cipsecendpthistremoteport = None
                self._segment_path = lambda: "cipSecEndPtHistEntry" + "[cipSecEndPtHistIndex='" + str(self.cipsecendpthistindex) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecEndPtHistTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecendpthisttable.Cipsecendpthistentry, ['cipsecendpthistindex', 'cipsecendpthisttunindex', 'cipsecendpthistactiveindex', 'cipsecendpthistlocalname', 'cipsecendpthistlocaltype', 'cipsecendpthistlocaladdr1', 'cipsecendpthistlocaladdr2', 'cipsecendpthistlocalprotocol', 'cipsecendpthistlocalport', 'cipsecendpthistremotename', 'cipsecendpthistremotetype', 'cipsecendpthistremoteaddr1', 'cipsecendpthistremoteaddr2', 'cipsecendpthistremoteprotocol', 'cipsecendpthistremoteport'], name, value)


    class Cikefailtable(Entity):
        """
        The IPsec Phase\-1 Failure Table.
        This table is implemented as a sliding 
        window in which only the last n entries are 
        maintained.  The maximum number of entries
        is specified by the cipSecFailTableSize object.
        
        .. attribute:: cikefailentry
        
        	Each entry contains the attributes associated with  an IPsec Phase\-1 failure
        	**type**\: list of  		 :py:class:`Cikefailentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikefailtable.Cikefailentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cikefailtable, self).__init__()

            self.yang_name = "cikeFailTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cikeFailEntry", ("cikefailentry", CISCOIPSECFLOWMONITORMIB.Cikefailtable.Cikefailentry))])
            self._leafs = OrderedDict()

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
            
            .. attribute:: cikefailindex  (key)
            
            	The IPsec Phase\-1 Failure Table index. The value of the index is a number which  begins at one and is incremented with each  IPsec Phase\-1 failure. The value of this object will wrap at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cikefailreason
            
            	The reason for the failure.  Possible reasons include\: 1 = other 2 = peer delete request was received 3 = contact with peer was lost 4 = local failure occurred 5 = authentication failure 6 = hash validation failure 7 = encryption failure 8 = internal error occurred 9 = system capacity failure 10 = proposal failure 11 = peer's certificate is unavailable 12 = peer's certificate was found invalid 13 = local certificate expired 14 = certificate revoke list (crl) failure 15 = peer encoding error 16 = non\-existent security association 17 = operator requested termination
            	**type**\:  :py:class:`Cikefailreason <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cikefailtable.Cikefailentry.Cikefailreason>`
            
            .. attribute:: cikefailtime
            
            	The value of sysUpTime in hundredths of seconds at the time of the failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cikefaillocaltype
            
            	The type of local peer identity.  The local peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\:  :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: cikefaillocalvalue
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\: str
            
            .. attribute:: cikefailremotetype
            
            	The type of remote peer identity.  The remote peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\:  :py:class:`IkePeerType <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkePeerType>`
            
            .. attribute:: cikefailremotevalue
            
            	The value of the remote peer identity.  If the remote peer type is an IP Address, then this is the IP Address used to identify the remote peer.  If the remote peer type is a host name, then this is the host name used to identify the remote peer
            	**type**\: str
            
            .. attribute:: cikefaillocaladdr
            
            	The IP address of the local peer
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: cikefailremoteaddr
            
            	The IP address of the remote peer
            	**type**\: str
            
            	**length:** 4 \| 16
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cikefailtable.Cikefailentry, self).__init__()

                self.yang_name = "cikeFailEntry"
                self.yang_parent_name = "cikeFailTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cikefailindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cikefailindex', YLeaf(YType.int32, 'cikeFailIndex')),
                    ('cikefailreason', YLeaf(YType.enumeration, 'cikeFailReason')),
                    ('cikefailtime', YLeaf(YType.uint32, 'cikeFailTime')),
                    ('cikefaillocaltype', YLeaf(YType.enumeration, 'cikeFailLocalType')),
                    ('cikefaillocalvalue', YLeaf(YType.str, 'cikeFailLocalValue')),
                    ('cikefailremotetype', YLeaf(YType.enumeration, 'cikeFailRemoteType')),
                    ('cikefailremotevalue', YLeaf(YType.str, 'cikeFailRemoteValue')),
                    ('cikefaillocaladdr', YLeaf(YType.str, 'cikeFailLocalAddr')),
                    ('cikefailremoteaddr', YLeaf(YType.str, 'cikeFailRemoteAddr')),
                ])
                self.cikefailindex = None
                self.cikefailreason = None
                self.cikefailtime = None
                self.cikefaillocaltype = None
                self.cikefaillocalvalue = None
                self.cikefailremotetype = None
                self.cikefailremotevalue = None
                self.cikefaillocaladdr = None
                self.cikefailremoteaddr = None
                self._segment_path = lambda: "cikeFailEntry" + "[cikeFailIndex='" + str(self.cikefailindex) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikeFailTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cikefailtable.Cikefailentry, ['cikefailindex', 'cikefailreason', 'cikefailtime', 'cikefaillocaltype', 'cikefaillocalvalue', 'cikefailremotetype', 'cikefailremotevalue', 'cikefaillocaladdr', 'cikefailremoteaddr'], name, value)

            class Cikefailreason(Enum):
                """
                Cikefailreason (Enum Class)

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



    class Cipsecfailtable(Entity):
        """
        The IPsec Phase\-2 Failure Table.
        This table is implemented as a sliding window 
        in which only the last n entries are maintained.  
        The maximum number of entries
        is specified by the cipSecFailTableSize object.
        
        .. attribute:: cipsecfailentry
        
        	Each entry contains the attributes associated with an IPsec Phase\-1 failure
        	**type**\: list of  		 :py:class:`Cipsecfailentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecfailtable.Cipsecfailentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CISCOIPSECFLOWMONITORMIB.Cipsecfailtable, self).__init__()

            self.yang_name = "cipSecFailTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipSecFailEntry", ("cipsecfailentry", CISCOIPSECFLOWMONITORMIB.Cipsecfailtable.Cipsecfailentry))])
            self._leafs = OrderedDict()

            self.cipsecfailentry = YList(self)
            self._segment_path = lambda: "cipSecFailTable"
            self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecfailtable, [], name, value)


        class Cipsecfailentry(Entity):
            """
            Each entry contains the attributes associated with
            an IPsec Phase\-1 failure.
            
            .. attribute:: cipsecfailindex  (key)
            
            	The IPsec Phase\-2 Failure Table index. The value of the index is a number which  begins at one and is incremented with each  IPsec Phase\-1 failure. The value of this object will wrap at 2,147,483,647
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecfailreason
            
            	The reason for the failure.  Possible reasons include\:   1 = other   2 = internal error occurred   3 = peer encoding error   4 = proposal failure   5 = protocol use failure   6 = non\-existent security association   7 = decryption failure   8 = encryption failure   9 = inbound authentication failure  10 = outbound authentication failure  11 = compression failure  12 = system capacity failure  13 = peer delete request was received  14 = contact with peer was lost  15 = sequence number rolled over  16 = operator requested termination
            	**type**\:  :py:class:`Cipsecfailreason <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CISCOIPSECFLOWMONITORMIB.Cipsecfailtable.Cipsecfailentry.Cipsecfailreason>`
            
            .. attribute:: cipsecfailtime
            
            	The value of sysUpTime in hundredths of seconds at the time of the failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsecfailtunnelindex
            
            	The Phase\-2 Tunnel index (cipSecTunIndex)
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecfailsaspi
            
            	The security association SPI value
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cipsecfailpktsrcaddr
            
            	The packet's source IP address
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsecfailpktdstaddr
            
            	The packet's destination IP address
            	**type**\: str
            
            	**length:** 4 \| 16
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CISCOIPSECFLOWMONITORMIB.Cipsecfailtable.Cipsecfailentry, self).__init__()

                self.yang_name = "cipSecFailEntry"
                self.yang_parent_name = "cipSecFailTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipsecfailindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipsecfailindex', YLeaf(YType.int32, 'cipSecFailIndex')),
                    ('cipsecfailreason', YLeaf(YType.enumeration, 'cipSecFailReason')),
                    ('cipsecfailtime', YLeaf(YType.uint32, 'cipSecFailTime')),
                    ('cipsecfailtunnelindex', YLeaf(YType.int32, 'cipSecFailTunnelIndex')),
                    ('cipsecfailsaspi', YLeaf(YType.int32, 'cipSecFailSaSpi')),
                    ('cipsecfailpktsrcaddr', YLeaf(YType.str, 'cipSecFailPktSrcAddr')),
                    ('cipsecfailpktdstaddr', YLeaf(YType.str, 'cipSecFailPktDstAddr')),
                ])
                self.cipsecfailindex = None
                self.cipsecfailreason = None
                self.cipsecfailtime = None
                self.cipsecfailtunnelindex = None
                self.cipsecfailsaspi = None
                self.cipsecfailpktsrcaddr = None
                self.cipsecfailpktdstaddr = None
                self._segment_path = lambda: "cipSecFailEntry" + "[cipSecFailIndex='" + str(self.cipsecfailindex) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecFailTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECFLOWMONITORMIB.Cipsecfailtable.Cipsecfailentry, ['cipsecfailindex', 'cipsecfailreason', 'cipsecfailtime', 'cipsecfailtunnelindex', 'cipsecfailsaspi', 'cipsecfailpktsrcaddr', 'cipsecfailpktdstaddr'], name, value)

            class Cipsecfailreason(Enum):
                """
                Cipsecfailreason (Enum Class)

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


    def clone_ptr(self):
        self._top_entity = CISCOIPSECFLOWMONITORMIB()
        return self._top_entity

