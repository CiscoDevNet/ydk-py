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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Authalgo(Enum):
    """
    Authalgo

    The authentication algorithm used by a

    security association of an IPsec Phase\-2 Tunnel.

    .. data:: none = 1

    .. data:: hmacMd5 = 2

    .. data:: hmacSha = 3

    """

    none = Enum.YLeaf(1, "none")

    hmacMd5 = Enum.YLeaf(2, "hmacMd5")

    hmacSha = Enum.YLeaf(3, "hmacSha")


class Compalgo(Enum):
    """
    Compalgo

    The compression algorithm used by a

    security association of an IPsec Phase\-2 Tunnel.

    .. data:: none = 1

    .. data:: ldf = 2

    """

    none = Enum.YLeaf(1, "none")

    ldf = Enum.YLeaf(2, "ldf")


class Diffhellmangrp(Enum):
    """
    Diffhellmangrp

    The Diffie Hellman Group used in negotiations.

    .. data:: none = 1

    .. data:: dhGroup1 = 2

    .. data:: dhGroup2 = 3

    """

    none = Enum.YLeaf(1, "none")

    dhGroup1 = Enum.YLeaf(2, "dhGroup1")

    dhGroup2 = Enum.YLeaf(3, "dhGroup2")


class Encapmode(Enum):
    """
    Encapmode

    The encapsulation mode used by an IPsec Phase\-2

    Tunnel.

    .. data:: tunnel = 1

    .. data:: transport = 2

    """

    tunnel = Enum.YLeaf(1, "tunnel")

    transport = Enum.YLeaf(2, "transport")


class Encryptalgo(Enum):
    """
    Encryptalgo

    The encryption algorithm used in negotiations.

    .. data:: none = 1

    .. data:: des = 2

    .. data:: des3 = 3

    """

    none = Enum.YLeaf(1, "none")

    des = Enum.YLeaf(2, "des")

    des3 = Enum.YLeaf(3, "des3")


class Endpttype(Enum):
    """
    Endpttype

    The type of identity use to specify an IPsec End Point.

    .. data:: singleIpAddr = 1

    .. data:: ipAddrRange = 2

    .. data:: ipSubnet = 3

    """

    singleIpAddr = Enum.YLeaf(1, "singleIpAddr")

    ipAddrRange = Enum.YLeaf(2, "ipAddrRange")

    ipSubnet = Enum.YLeaf(3, "ipSubnet")


class Ikeauthmethod(Enum):
    """
    Ikeauthmethod

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


class Ikehashalgo(Enum):
    """
    Ikehashalgo

    The hash algorithm used in IPsec Phase\-1

    IKE negotiations.

    .. data:: none = 1

    .. data:: md5 = 2

    .. data:: sha = 3

    """

    none = Enum.YLeaf(1, "none")

    md5 = Enum.YLeaf(2, "md5")

    sha = Enum.YLeaf(3, "sha")


class Ikenegomode(Enum):
    """
    Ikenegomode

    The IPsec Phase\-1 IKE negotiation mode.

    .. data:: main = 1

    .. data:: aggressive = 2

    """

    main = Enum.YLeaf(1, "main")

    aggressive = Enum.YLeaf(2, "aggressive")


class Ikepeertype(Enum):
    """
    Ikepeertype

    The type of IPsec Phase\-1 IKE peer identity.

    The IKE peer may be identified by\:

     1. an IP address, or

     2. a host name.

    .. data:: ipAddrPeer = 1

    .. data:: namePeer = 2

    """

    ipAddrPeer = Enum.YLeaf(1, "ipAddrPeer")

    namePeer = Enum.YLeaf(2, "namePeer")


class Keytype(Enum):
    """
    Keytype

    The type of key used by an IPsec Phase\-2 Tunnel.

    .. data:: ike = 1

    .. data:: manual = 2

    """

    ike = Enum.YLeaf(1, "ike")

    manual = Enum.YLeaf(2, "manual")


class Trapstatus(Enum):
    """
    Trapstatus

    The administrative status for sending a TRAP.

    .. data:: enabled = 1

    .. data:: disabled = 2

    """

    enabled = Enum.YLeaf(1, "enabled")

    disabled = Enum.YLeaf(2, "disabled")


class Tunnelstatus(Enum):
    """
    Tunnelstatus

    The status of a Tunnel.  Objects of this type may

    be used to bring the tunnel down by setting

    value of this object to destroy(2).  Objects of this

    type cannot be used to create a Tunnel.

    .. data:: active = 1

    .. data:: destroy = 2

    """

    active = Enum.YLeaf(1, "active")

    destroy = Enum.YLeaf(2, "destroy")



class CiscoIpsecFlowMonitorMib(Entity):
    """
    
    
    .. attribute:: cikefailtable
    
    	The IPsec Phase\-1 Failure Table. This table is implemented as a sliding  window in which only the last n entries are  maintained.  The maximum number of entries is specified by the cipSecFailTableSize object
    	**type**\:   :py:class:`Cikefailtable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cikefailtable>`
    
    .. attribute:: cikeglobalstats
    
    	
    	**type**\:   :py:class:`Cikeglobalstats <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cikeglobalstats>`
    
    .. attribute:: cikepeercorrtable
    
    	The IPsec Phase\-1 Internet Key Exchange Peer Association to IPsec Phase\-2 Tunnel Correlation Table. There is one entry in this table for each active IPsec Phase\-2 Tunnel
    	**type**\:   :py:class:`Cikepeercorrtable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cikepeercorrtable>`
    
    .. attribute:: cikepeertable
    
    	The IPsec Phase\-1 Internet Key Exchange Peer Table. There is one entry in this table for each IPsec Phase\-1 IKE peer association which is currently associated with an active IPsec Phase\-1 Tunnel. The IPsec Phase\-1 IKE Tunnel associated with this IPsec Phase\-1 IKE peer association may or may not be currently active
    	**type**\:   :py:class:`Cikepeertable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cikepeertable>`
    
    .. attribute:: cikephase1gwstatstable
    
    	Phase\-1 IKE stats information is included in this table. Each entry is related to a specific gateway which is  identified by 'cmgwIndex'
    	**type**\:   :py:class:`Cikephase1Gwstatstable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cikephase1Gwstatstable>`
    
    .. attribute:: ciketunnelhisttable
    
    	The IPsec Phase\-1 Internet Key Exchange Tunnel History Table.  This table is implemented as a  sliding window in which only the last n entries  are maintained.  The maximum number of entries  is specified by the cipSecHistTableSize object
    	**type**\:   :py:class:`Ciketunnelhisttable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Ciketunnelhisttable>`
    
    .. attribute:: ciketunneltable
    
    	The IPsec Phase\-1 Internet Key Exchange Tunnel Table. There is one entry in this table for each active IPsec Phase\-1 IKE Tunnel
    	**type**\:   :py:class:`Ciketunneltable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Ciketunneltable>`
    
    .. attribute:: cipsecendpthisttable
    
    	The IPsec Phase\-2 Tunnel Endpoint History Table. This table is implemented as a  sliding window in which only the last n entries are maintained.   The maximum number of entries is specified by the cipSecHistTableSize object
    	**type**\:   :py:class:`Cipsecendpthisttable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecendpthisttable>`
    
    .. attribute:: cipsecendpttable
    
    	The IPsec Phase\-2 Tunnel Endpoint Table. This table contains an entry for each  active endpoint associated with an IPsec  Phase\-2 Tunnel
    	**type**\:   :py:class:`Cipsecendpttable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecendpttable>`
    
    .. attribute:: cipsecfailglobalcntl
    
    	
    	**type**\:   :py:class:`Cipsecfailglobalcntl <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecfailglobalcntl>`
    
    .. attribute:: cipsecfailtable
    
    	The IPsec Phase\-2 Failure Table. This table is implemented as a sliding window  in which only the last n entries are maintained.   The maximum number of entries is specified by the cipSecFailTableSize object
    	**type**\:   :py:class:`Cipsecfailtable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecfailtable>`
    
    .. attribute:: cipsecglobalstats
    
    	
    	**type**\:   :py:class:`Cipsecglobalstats <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecglobalstats>`
    
    .. attribute:: cipsechistglobalcntl
    
    	
    	**type**\:   :py:class:`Cipsechistglobalcntl <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsechistglobalcntl>`
    
    .. attribute:: cipseclevels
    
    	
    	**type**\:   :py:class:`Cipseclevels <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipseclevels>`
    
    .. attribute:: cipsecphase2gwstatstable
    
    	Phase\-2 IPsec stats information is included in this table. Each entry is related to a specific gateway which is  identified by 'cmgwIndex'
    	**type**\:   :py:class:`Cipsecphase2Gwstatstable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecphase2Gwstatstable>`
    
    .. attribute:: cipsecspitable
    
    	The IPsec Phase\-2 Security Protection Index Table. This table contains an entry for each active  and expiring security  association
    	**type**\:   :py:class:`Cipsecspitable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecspitable>`
    
    .. attribute:: cipsectrapcntl
    
    	
    	**type**\:   :py:class:`Cipsectrapcntl <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsectrapcntl>`
    
    .. attribute:: cipsectunnelhisttable
    
    	The IPsec Phase\-2 Tunnel History Table. This table is implemented as a sliding  window in which only the last n entries are maintained.  The maximum number  of entries is specified by the cipSecHistTableSize object
    	**type**\:   :py:class:`Cipsectunnelhisttable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsectunnelhisttable>`
    
    .. attribute:: cipsectunneltable
    
    	The IPsec Phase\-2 Tunnel Table. There is one entry in this table for  each active IPsec Phase\-2 Tunnel
    	**type**\:   :py:class:`Cipsectunneltable <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsectunneltable>`
    
    

    """

    _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
    _revision = '2007-10-24'

    def __init__(self):
        super(CiscoIpsecFlowMonitorMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"
        self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

        self.cikefailtable = CiscoIpsecFlowMonitorMib.Cikefailtable()
        self.cikefailtable.parent = self
        self._children_name_map["cikefailtable"] = "cikeFailTable"
        self._children_yang_names.add("cikeFailTable")

        self.cikeglobalstats = CiscoIpsecFlowMonitorMib.Cikeglobalstats()
        self.cikeglobalstats.parent = self
        self._children_name_map["cikeglobalstats"] = "cikeGlobalStats"
        self._children_yang_names.add("cikeGlobalStats")

        self.cikepeercorrtable = CiscoIpsecFlowMonitorMib.Cikepeercorrtable()
        self.cikepeercorrtable.parent = self
        self._children_name_map["cikepeercorrtable"] = "cikePeerCorrTable"
        self._children_yang_names.add("cikePeerCorrTable")

        self.cikepeertable = CiscoIpsecFlowMonitorMib.Cikepeertable()
        self.cikepeertable.parent = self
        self._children_name_map["cikepeertable"] = "cikePeerTable"
        self._children_yang_names.add("cikePeerTable")

        self.cikephase1gwstatstable = CiscoIpsecFlowMonitorMib.Cikephase1Gwstatstable()
        self.cikephase1gwstatstable.parent = self
        self._children_name_map["cikephase1gwstatstable"] = "cikePhase1GWStatsTable"
        self._children_yang_names.add("cikePhase1GWStatsTable")

        self.ciketunnelhisttable = CiscoIpsecFlowMonitorMib.Ciketunnelhisttable()
        self.ciketunnelhisttable.parent = self
        self._children_name_map["ciketunnelhisttable"] = "cikeTunnelHistTable"
        self._children_yang_names.add("cikeTunnelHistTable")

        self.ciketunneltable = CiscoIpsecFlowMonitorMib.Ciketunneltable()
        self.ciketunneltable.parent = self
        self._children_name_map["ciketunneltable"] = "cikeTunnelTable"
        self._children_yang_names.add("cikeTunnelTable")

        self.cipsecendpthisttable = CiscoIpsecFlowMonitorMib.Cipsecendpthisttable()
        self.cipsecendpthisttable.parent = self
        self._children_name_map["cipsecendpthisttable"] = "cipSecEndPtHistTable"
        self._children_yang_names.add("cipSecEndPtHistTable")

        self.cipsecendpttable = CiscoIpsecFlowMonitorMib.Cipsecendpttable()
        self.cipsecendpttable.parent = self
        self._children_name_map["cipsecendpttable"] = "cipSecEndPtTable"
        self._children_yang_names.add("cipSecEndPtTable")

        self.cipsecfailglobalcntl = CiscoIpsecFlowMonitorMib.Cipsecfailglobalcntl()
        self.cipsecfailglobalcntl.parent = self
        self._children_name_map["cipsecfailglobalcntl"] = "cipSecFailGlobalCntl"
        self._children_yang_names.add("cipSecFailGlobalCntl")

        self.cipsecfailtable = CiscoIpsecFlowMonitorMib.Cipsecfailtable()
        self.cipsecfailtable.parent = self
        self._children_name_map["cipsecfailtable"] = "cipSecFailTable"
        self._children_yang_names.add("cipSecFailTable")

        self.cipsecglobalstats = CiscoIpsecFlowMonitorMib.Cipsecglobalstats()
        self.cipsecglobalstats.parent = self
        self._children_name_map["cipsecglobalstats"] = "cipSecGlobalStats"
        self._children_yang_names.add("cipSecGlobalStats")

        self.cipsechistglobalcntl = CiscoIpsecFlowMonitorMib.Cipsechistglobalcntl()
        self.cipsechistglobalcntl.parent = self
        self._children_name_map["cipsechistglobalcntl"] = "cipSecHistGlobalCntl"
        self._children_yang_names.add("cipSecHistGlobalCntl")

        self.cipseclevels = CiscoIpsecFlowMonitorMib.Cipseclevels()
        self.cipseclevels.parent = self
        self._children_name_map["cipseclevels"] = "cipSecLevels"
        self._children_yang_names.add("cipSecLevels")

        self.cipsecphase2gwstatstable = CiscoIpsecFlowMonitorMib.Cipsecphase2Gwstatstable()
        self.cipsecphase2gwstatstable.parent = self
        self._children_name_map["cipsecphase2gwstatstable"] = "cipSecPhase2GWStatsTable"
        self._children_yang_names.add("cipSecPhase2GWStatsTable")

        self.cipsecspitable = CiscoIpsecFlowMonitorMib.Cipsecspitable()
        self.cipsecspitable.parent = self
        self._children_name_map["cipsecspitable"] = "cipSecSpiTable"
        self._children_yang_names.add("cipSecSpiTable")

        self.cipsectrapcntl = CiscoIpsecFlowMonitorMib.Cipsectrapcntl()
        self.cipsectrapcntl.parent = self
        self._children_name_map["cipsectrapcntl"] = "cipSecTrapCntl"
        self._children_yang_names.add("cipSecTrapCntl")

        self.cipsectunnelhisttable = CiscoIpsecFlowMonitorMib.Cipsectunnelhisttable()
        self.cipsectunnelhisttable.parent = self
        self._children_name_map["cipsectunnelhisttable"] = "cipSecTunnelHistTable"
        self._children_yang_names.add("cipSecTunnelHistTable")

        self.cipsectunneltable = CiscoIpsecFlowMonitorMib.Cipsectunneltable()
        self.cipsectunneltable.parent = self
        self._children_name_map["cipsectunneltable"] = "cipSecTunnelTable"
        self._children_yang_names.add("cipSecTunnelTable")


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
            super(CiscoIpsecFlowMonitorMib.Cipseclevels, self).__init__()

            self.yang_name = "cipSecLevels"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

            self.cipsecmiblevel = YLeaf(YType.int32, "cipSecMibLevel")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cipsecmiblevel") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpsecFlowMonitorMib.Cipseclevels, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Cipseclevels, self).__setattr__(name, value)

        def has_data(self):
            return self.cipsecmiblevel.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cipsecmiblevel.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipSecLevels" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cipsecmiblevel.is_set or self.cipsecmiblevel.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecmiblevel.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipSecMibLevel"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cipSecMibLevel"):
                self.cipsecmiblevel = value
                self.cipsecmiblevel.value_namespace = name_space
                self.cipsecmiblevel.value_namespace_prefix = name_space_prefix


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
            super(CiscoIpsecFlowMonitorMib.Cikeglobalstats, self).__init__()

            self.yang_name = "cikeGlobalStats"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

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

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cikeglobalactivetunnels",
                            "cikeglobalauthfails",
                            "cikeglobaldecryptfails",
                            "cikeglobalhashvalidfails",
                            "cikeglobalindroppkts",
                            "cikeglobalinittunnelfails",
                            "cikeglobalinittunnels",
                            "cikeglobalinnotifys",
                            "cikeglobalinoctets",
                            "cikeglobalinp2exchginvalids",
                            "cikeglobalinp2exchgrejects",
                            "cikeglobalinp2exchgs",
                            "cikeglobalinp2sadelrequests",
                            "cikeglobalinpkts",
                            "cikeglobalnosafails",
                            "cikeglobaloutdroppkts",
                            "cikeglobaloutnotifys",
                            "cikeglobaloutoctets",
                            "cikeglobaloutp2exchginvalids",
                            "cikeglobaloutp2exchgrejects",
                            "cikeglobaloutp2exchgs",
                            "cikeglobaloutp2sadelrequests",
                            "cikeglobaloutpkts",
                            "cikeglobalprevioustunnels",
                            "cikeglobalresptunnelfails",
                            "cikeglobalsyscapfails") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpsecFlowMonitorMib.Cikeglobalstats, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Cikeglobalstats, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cikeglobalactivetunnels.is_set or
                self.cikeglobalauthfails.is_set or
                self.cikeglobaldecryptfails.is_set or
                self.cikeglobalhashvalidfails.is_set or
                self.cikeglobalindroppkts.is_set or
                self.cikeglobalinittunnelfails.is_set or
                self.cikeglobalinittunnels.is_set or
                self.cikeglobalinnotifys.is_set or
                self.cikeglobalinoctets.is_set or
                self.cikeglobalinp2exchginvalids.is_set or
                self.cikeglobalinp2exchgrejects.is_set or
                self.cikeglobalinp2exchgs.is_set or
                self.cikeglobalinp2sadelrequests.is_set or
                self.cikeglobalinpkts.is_set or
                self.cikeglobalnosafails.is_set or
                self.cikeglobaloutdroppkts.is_set or
                self.cikeglobaloutnotifys.is_set or
                self.cikeglobaloutoctets.is_set or
                self.cikeglobaloutp2exchginvalids.is_set or
                self.cikeglobaloutp2exchgrejects.is_set or
                self.cikeglobaloutp2exchgs.is_set or
                self.cikeglobaloutp2sadelrequests.is_set or
                self.cikeglobaloutpkts.is_set or
                self.cikeglobalprevioustunnels.is_set or
                self.cikeglobalresptunnelfails.is_set or
                self.cikeglobalsyscapfails.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cikeglobalactivetunnels.yfilter != YFilter.not_set or
                self.cikeglobalauthfails.yfilter != YFilter.not_set or
                self.cikeglobaldecryptfails.yfilter != YFilter.not_set or
                self.cikeglobalhashvalidfails.yfilter != YFilter.not_set or
                self.cikeglobalindroppkts.yfilter != YFilter.not_set or
                self.cikeglobalinittunnelfails.yfilter != YFilter.not_set or
                self.cikeglobalinittunnels.yfilter != YFilter.not_set or
                self.cikeglobalinnotifys.yfilter != YFilter.not_set or
                self.cikeglobalinoctets.yfilter != YFilter.not_set or
                self.cikeglobalinp2exchginvalids.yfilter != YFilter.not_set or
                self.cikeglobalinp2exchgrejects.yfilter != YFilter.not_set or
                self.cikeglobalinp2exchgs.yfilter != YFilter.not_set or
                self.cikeglobalinp2sadelrequests.yfilter != YFilter.not_set or
                self.cikeglobalinpkts.yfilter != YFilter.not_set or
                self.cikeglobalnosafails.yfilter != YFilter.not_set or
                self.cikeglobaloutdroppkts.yfilter != YFilter.not_set or
                self.cikeglobaloutnotifys.yfilter != YFilter.not_set or
                self.cikeglobaloutoctets.yfilter != YFilter.not_set or
                self.cikeglobaloutp2exchginvalids.yfilter != YFilter.not_set or
                self.cikeglobaloutp2exchgrejects.yfilter != YFilter.not_set or
                self.cikeglobaloutp2exchgs.yfilter != YFilter.not_set or
                self.cikeglobaloutp2sadelrequests.yfilter != YFilter.not_set or
                self.cikeglobaloutpkts.yfilter != YFilter.not_set or
                self.cikeglobalprevioustunnels.yfilter != YFilter.not_set or
                self.cikeglobalresptunnelfails.yfilter != YFilter.not_set or
                self.cikeglobalsyscapfails.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cikeGlobalStats" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cikeglobalactivetunnels.is_set or self.cikeglobalactivetunnels.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobalactivetunnels.get_name_leafdata())
            if (self.cikeglobalauthfails.is_set or self.cikeglobalauthfails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobalauthfails.get_name_leafdata())
            if (self.cikeglobaldecryptfails.is_set or self.cikeglobaldecryptfails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobaldecryptfails.get_name_leafdata())
            if (self.cikeglobalhashvalidfails.is_set or self.cikeglobalhashvalidfails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobalhashvalidfails.get_name_leafdata())
            if (self.cikeglobalindroppkts.is_set or self.cikeglobalindroppkts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobalindroppkts.get_name_leafdata())
            if (self.cikeglobalinittunnelfails.is_set or self.cikeglobalinittunnelfails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobalinittunnelfails.get_name_leafdata())
            if (self.cikeglobalinittunnels.is_set or self.cikeglobalinittunnels.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobalinittunnels.get_name_leafdata())
            if (self.cikeglobalinnotifys.is_set or self.cikeglobalinnotifys.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobalinnotifys.get_name_leafdata())
            if (self.cikeglobalinoctets.is_set or self.cikeglobalinoctets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobalinoctets.get_name_leafdata())
            if (self.cikeglobalinp2exchginvalids.is_set or self.cikeglobalinp2exchginvalids.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobalinp2exchginvalids.get_name_leafdata())
            if (self.cikeglobalinp2exchgrejects.is_set or self.cikeglobalinp2exchgrejects.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobalinp2exchgrejects.get_name_leafdata())
            if (self.cikeglobalinp2exchgs.is_set or self.cikeglobalinp2exchgs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobalinp2exchgs.get_name_leafdata())
            if (self.cikeglobalinp2sadelrequests.is_set or self.cikeglobalinp2sadelrequests.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobalinp2sadelrequests.get_name_leafdata())
            if (self.cikeglobalinpkts.is_set or self.cikeglobalinpkts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobalinpkts.get_name_leafdata())
            if (self.cikeglobalnosafails.is_set or self.cikeglobalnosafails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobalnosafails.get_name_leafdata())
            if (self.cikeglobaloutdroppkts.is_set or self.cikeglobaloutdroppkts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobaloutdroppkts.get_name_leafdata())
            if (self.cikeglobaloutnotifys.is_set or self.cikeglobaloutnotifys.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobaloutnotifys.get_name_leafdata())
            if (self.cikeglobaloutoctets.is_set or self.cikeglobaloutoctets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobaloutoctets.get_name_leafdata())
            if (self.cikeglobaloutp2exchginvalids.is_set or self.cikeglobaloutp2exchginvalids.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobaloutp2exchginvalids.get_name_leafdata())
            if (self.cikeglobaloutp2exchgrejects.is_set or self.cikeglobaloutp2exchgrejects.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobaloutp2exchgrejects.get_name_leafdata())
            if (self.cikeglobaloutp2exchgs.is_set or self.cikeglobaloutp2exchgs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobaloutp2exchgs.get_name_leafdata())
            if (self.cikeglobaloutp2sadelrequests.is_set or self.cikeglobaloutp2sadelrequests.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobaloutp2sadelrequests.get_name_leafdata())
            if (self.cikeglobaloutpkts.is_set or self.cikeglobaloutpkts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobaloutpkts.get_name_leafdata())
            if (self.cikeglobalprevioustunnels.is_set or self.cikeglobalprevioustunnels.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobalprevioustunnels.get_name_leafdata())
            if (self.cikeglobalresptunnelfails.is_set or self.cikeglobalresptunnelfails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobalresptunnelfails.get_name_leafdata())
            if (self.cikeglobalsyscapfails.is_set or self.cikeglobalsyscapfails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cikeglobalsyscapfails.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cikeGlobalActiveTunnels" or name == "cikeGlobalAuthFails" or name == "cikeGlobalDecryptFails" or name == "cikeGlobalHashValidFails" or name == "cikeGlobalInDropPkts" or name == "cikeGlobalInitTunnelFails" or name == "cikeGlobalInitTunnels" or name == "cikeGlobalInNotifys" or name == "cikeGlobalInOctets" or name == "cikeGlobalInP2ExchgInvalids" or name == "cikeGlobalInP2ExchgRejects" or name == "cikeGlobalInP2Exchgs" or name == "cikeGlobalInP2SaDelRequests" or name == "cikeGlobalInPkts" or name == "cikeGlobalNoSaFails" or name == "cikeGlobalOutDropPkts" or name == "cikeGlobalOutNotifys" or name == "cikeGlobalOutOctets" or name == "cikeGlobalOutP2ExchgInvalids" or name == "cikeGlobalOutP2ExchgRejects" or name == "cikeGlobalOutP2Exchgs" or name == "cikeGlobalOutP2SaDelRequests" or name == "cikeGlobalOutPkts" or name == "cikeGlobalPreviousTunnels" or name == "cikeGlobalRespTunnelFails" or name == "cikeGlobalSysCapFails"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cikeGlobalActiveTunnels"):
                self.cikeglobalactivetunnels = value
                self.cikeglobalactivetunnels.value_namespace = name_space
                self.cikeglobalactivetunnels.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalAuthFails"):
                self.cikeglobalauthfails = value
                self.cikeglobalauthfails.value_namespace = name_space
                self.cikeglobalauthfails.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalDecryptFails"):
                self.cikeglobaldecryptfails = value
                self.cikeglobaldecryptfails.value_namespace = name_space
                self.cikeglobaldecryptfails.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalHashValidFails"):
                self.cikeglobalhashvalidfails = value
                self.cikeglobalhashvalidfails.value_namespace = name_space
                self.cikeglobalhashvalidfails.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalInDropPkts"):
                self.cikeglobalindroppkts = value
                self.cikeglobalindroppkts.value_namespace = name_space
                self.cikeglobalindroppkts.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalInitTunnelFails"):
                self.cikeglobalinittunnelfails = value
                self.cikeglobalinittunnelfails.value_namespace = name_space
                self.cikeglobalinittunnelfails.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalInitTunnels"):
                self.cikeglobalinittunnels = value
                self.cikeglobalinittunnels.value_namespace = name_space
                self.cikeglobalinittunnels.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalInNotifys"):
                self.cikeglobalinnotifys = value
                self.cikeglobalinnotifys.value_namespace = name_space
                self.cikeglobalinnotifys.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalInOctets"):
                self.cikeglobalinoctets = value
                self.cikeglobalinoctets.value_namespace = name_space
                self.cikeglobalinoctets.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalInP2ExchgInvalids"):
                self.cikeglobalinp2exchginvalids = value
                self.cikeglobalinp2exchginvalids.value_namespace = name_space
                self.cikeglobalinp2exchginvalids.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalInP2ExchgRejects"):
                self.cikeglobalinp2exchgrejects = value
                self.cikeglobalinp2exchgrejects.value_namespace = name_space
                self.cikeglobalinp2exchgrejects.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalInP2Exchgs"):
                self.cikeglobalinp2exchgs = value
                self.cikeglobalinp2exchgs.value_namespace = name_space
                self.cikeglobalinp2exchgs.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalInP2SaDelRequests"):
                self.cikeglobalinp2sadelrequests = value
                self.cikeglobalinp2sadelrequests.value_namespace = name_space
                self.cikeglobalinp2sadelrequests.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalInPkts"):
                self.cikeglobalinpkts = value
                self.cikeglobalinpkts.value_namespace = name_space
                self.cikeglobalinpkts.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalNoSaFails"):
                self.cikeglobalnosafails = value
                self.cikeglobalnosafails.value_namespace = name_space
                self.cikeglobalnosafails.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalOutDropPkts"):
                self.cikeglobaloutdroppkts = value
                self.cikeglobaloutdroppkts.value_namespace = name_space
                self.cikeglobaloutdroppkts.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalOutNotifys"):
                self.cikeglobaloutnotifys = value
                self.cikeglobaloutnotifys.value_namespace = name_space
                self.cikeglobaloutnotifys.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalOutOctets"):
                self.cikeglobaloutoctets = value
                self.cikeglobaloutoctets.value_namespace = name_space
                self.cikeglobaloutoctets.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalOutP2ExchgInvalids"):
                self.cikeglobaloutp2exchginvalids = value
                self.cikeglobaloutp2exchginvalids.value_namespace = name_space
                self.cikeglobaloutp2exchginvalids.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalOutP2ExchgRejects"):
                self.cikeglobaloutp2exchgrejects = value
                self.cikeglobaloutp2exchgrejects.value_namespace = name_space
                self.cikeglobaloutp2exchgrejects.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalOutP2Exchgs"):
                self.cikeglobaloutp2exchgs = value
                self.cikeglobaloutp2exchgs.value_namespace = name_space
                self.cikeglobaloutp2exchgs.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalOutP2SaDelRequests"):
                self.cikeglobaloutp2sadelrequests = value
                self.cikeglobaloutp2sadelrequests.value_namespace = name_space
                self.cikeglobaloutp2sadelrequests.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalOutPkts"):
                self.cikeglobaloutpkts = value
                self.cikeglobaloutpkts.value_namespace = name_space
                self.cikeglobaloutpkts.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalPreviousTunnels"):
                self.cikeglobalprevioustunnels = value
                self.cikeglobalprevioustunnels.value_namespace = name_space
                self.cikeglobalprevioustunnels.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalRespTunnelFails"):
                self.cikeglobalresptunnelfails = value
                self.cikeglobalresptunnelfails.value_namespace = name_space
                self.cikeglobalresptunnelfails.value_namespace_prefix = name_space_prefix
            if(value_path == "cikeGlobalSysCapFails"):
                self.cikeglobalsyscapfails = value
                self.cikeglobalsyscapfails.value_namespace = name_space
                self.cikeglobalsyscapfails.value_namespace_prefix = name_space_prefix


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
            super(CiscoIpsecFlowMonitorMib.Cipsecglobalstats, self).__init__()

            self.yang_name = "cipSecGlobalStats"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

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

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cipsecglobalactivetunnels",
                            "cipsecglobalhcindecompoctets",
                            "cipsecglobalhcinoctets",
                            "cipsecglobalhcoutoctets",
                            "cipsecglobalhcoutuncompoctets",
                            "cipsecglobalinauthfails",
                            "cipsecglobalinauths",
                            "cipsecglobalindecompoctets",
                            "cipsecglobalindecompoctwraps",
                            "cipsecglobalindecryptfails",
                            "cipsecglobalindecrypts",
                            "cipsecglobalindrops",
                            "cipsecglobalinoctets",
                            "cipsecglobalinoctwraps",
                            "cipsecglobalinpkts",
                            "cipsecglobalinreplaydrops",
                            "cipsecglobalnosafails",
                            "cipsecglobaloutauthfails",
                            "cipsecglobaloutauths",
                            "cipsecglobaloutdrops",
                            "cipsecglobaloutencryptfails",
                            "cipsecglobaloutencrypts",
                            "cipsecglobaloutoctets",
                            "cipsecglobaloutoctwraps",
                            "cipsecglobaloutpkts",
                            "cipsecglobaloutuncompoctets",
                            "cipsecglobaloutuncompoctwraps",
                            "cipsecglobalprevioustunnels",
                            "cipsecglobalprotocolusefails",
                            "cipsecglobalsyscapfails") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpsecFlowMonitorMib.Cipsecglobalstats, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Cipsecglobalstats, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cipsecglobalactivetunnels.is_set or
                self.cipsecglobalhcindecompoctets.is_set or
                self.cipsecglobalhcinoctets.is_set or
                self.cipsecglobalhcoutoctets.is_set or
                self.cipsecglobalhcoutuncompoctets.is_set or
                self.cipsecglobalinauthfails.is_set or
                self.cipsecglobalinauths.is_set or
                self.cipsecglobalindecompoctets.is_set or
                self.cipsecglobalindecompoctwraps.is_set or
                self.cipsecglobalindecryptfails.is_set or
                self.cipsecglobalindecrypts.is_set or
                self.cipsecglobalindrops.is_set or
                self.cipsecglobalinoctets.is_set or
                self.cipsecglobalinoctwraps.is_set or
                self.cipsecglobalinpkts.is_set or
                self.cipsecglobalinreplaydrops.is_set or
                self.cipsecglobalnosafails.is_set or
                self.cipsecglobaloutauthfails.is_set or
                self.cipsecglobaloutauths.is_set or
                self.cipsecglobaloutdrops.is_set or
                self.cipsecglobaloutencryptfails.is_set or
                self.cipsecglobaloutencrypts.is_set or
                self.cipsecglobaloutoctets.is_set or
                self.cipsecglobaloutoctwraps.is_set or
                self.cipsecglobaloutpkts.is_set or
                self.cipsecglobaloutuncompoctets.is_set or
                self.cipsecglobaloutuncompoctwraps.is_set or
                self.cipsecglobalprevioustunnels.is_set or
                self.cipsecglobalprotocolusefails.is_set or
                self.cipsecglobalsyscapfails.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cipsecglobalactivetunnels.yfilter != YFilter.not_set or
                self.cipsecglobalhcindecompoctets.yfilter != YFilter.not_set or
                self.cipsecglobalhcinoctets.yfilter != YFilter.not_set or
                self.cipsecglobalhcoutoctets.yfilter != YFilter.not_set or
                self.cipsecglobalhcoutuncompoctets.yfilter != YFilter.not_set or
                self.cipsecglobalinauthfails.yfilter != YFilter.not_set or
                self.cipsecglobalinauths.yfilter != YFilter.not_set or
                self.cipsecglobalindecompoctets.yfilter != YFilter.not_set or
                self.cipsecglobalindecompoctwraps.yfilter != YFilter.not_set or
                self.cipsecglobalindecryptfails.yfilter != YFilter.not_set or
                self.cipsecglobalindecrypts.yfilter != YFilter.not_set or
                self.cipsecglobalindrops.yfilter != YFilter.not_set or
                self.cipsecglobalinoctets.yfilter != YFilter.not_set or
                self.cipsecglobalinoctwraps.yfilter != YFilter.not_set or
                self.cipsecglobalinpkts.yfilter != YFilter.not_set or
                self.cipsecglobalinreplaydrops.yfilter != YFilter.not_set or
                self.cipsecglobalnosafails.yfilter != YFilter.not_set or
                self.cipsecglobaloutauthfails.yfilter != YFilter.not_set or
                self.cipsecglobaloutauths.yfilter != YFilter.not_set or
                self.cipsecglobaloutdrops.yfilter != YFilter.not_set or
                self.cipsecglobaloutencryptfails.yfilter != YFilter.not_set or
                self.cipsecglobaloutencrypts.yfilter != YFilter.not_set or
                self.cipsecglobaloutoctets.yfilter != YFilter.not_set or
                self.cipsecglobaloutoctwraps.yfilter != YFilter.not_set or
                self.cipsecglobaloutpkts.yfilter != YFilter.not_set or
                self.cipsecglobaloutuncompoctets.yfilter != YFilter.not_set or
                self.cipsecglobaloutuncompoctwraps.yfilter != YFilter.not_set or
                self.cipsecglobalprevioustunnels.yfilter != YFilter.not_set or
                self.cipsecglobalprotocolusefails.yfilter != YFilter.not_set or
                self.cipsecglobalsyscapfails.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipSecGlobalStats" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cipsecglobalactivetunnels.is_set or self.cipsecglobalactivetunnels.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalactivetunnels.get_name_leafdata())
            if (self.cipsecglobalhcindecompoctets.is_set or self.cipsecglobalhcindecompoctets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalhcindecompoctets.get_name_leafdata())
            if (self.cipsecglobalhcinoctets.is_set or self.cipsecglobalhcinoctets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalhcinoctets.get_name_leafdata())
            if (self.cipsecglobalhcoutoctets.is_set or self.cipsecglobalhcoutoctets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalhcoutoctets.get_name_leafdata())
            if (self.cipsecglobalhcoutuncompoctets.is_set or self.cipsecglobalhcoutuncompoctets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalhcoutuncompoctets.get_name_leafdata())
            if (self.cipsecglobalinauthfails.is_set or self.cipsecglobalinauthfails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalinauthfails.get_name_leafdata())
            if (self.cipsecglobalinauths.is_set or self.cipsecglobalinauths.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalinauths.get_name_leafdata())
            if (self.cipsecglobalindecompoctets.is_set or self.cipsecglobalindecompoctets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalindecompoctets.get_name_leafdata())
            if (self.cipsecglobalindecompoctwraps.is_set or self.cipsecglobalindecompoctwraps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalindecompoctwraps.get_name_leafdata())
            if (self.cipsecglobalindecryptfails.is_set or self.cipsecglobalindecryptfails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalindecryptfails.get_name_leafdata())
            if (self.cipsecglobalindecrypts.is_set or self.cipsecglobalindecrypts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalindecrypts.get_name_leafdata())
            if (self.cipsecglobalindrops.is_set or self.cipsecglobalindrops.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalindrops.get_name_leafdata())
            if (self.cipsecglobalinoctets.is_set or self.cipsecglobalinoctets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalinoctets.get_name_leafdata())
            if (self.cipsecglobalinoctwraps.is_set or self.cipsecglobalinoctwraps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalinoctwraps.get_name_leafdata())
            if (self.cipsecglobalinpkts.is_set or self.cipsecglobalinpkts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalinpkts.get_name_leafdata())
            if (self.cipsecglobalinreplaydrops.is_set or self.cipsecglobalinreplaydrops.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalinreplaydrops.get_name_leafdata())
            if (self.cipsecglobalnosafails.is_set or self.cipsecglobalnosafails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalnosafails.get_name_leafdata())
            if (self.cipsecglobaloutauthfails.is_set or self.cipsecglobaloutauthfails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobaloutauthfails.get_name_leafdata())
            if (self.cipsecglobaloutauths.is_set or self.cipsecglobaloutauths.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobaloutauths.get_name_leafdata())
            if (self.cipsecglobaloutdrops.is_set or self.cipsecglobaloutdrops.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobaloutdrops.get_name_leafdata())
            if (self.cipsecglobaloutencryptfails.is_set or self.cipsecglobaloutencryptfails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobaloutencryptfails.get_name_leafdata())
            if (self.cipsecglobaloutencrypts.is_set or self.cipsecglobaloutencrypts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobaloutencrypts.get_name_leafdata())
            if (self.cipsecglobaloutoctets.is_set or self.cipsecglobaloutoctets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobaloutoctets.get_name_leafdata())
            if (self.cipsecglobaloutoctwraps.is_set or self.cipsecglobaloutoctwraps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobaloutoctwraps.get_name_leafdata())
            if (self.cipsecglobaloutpkts.is_set or self.cipsecglobaloutpkts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobaloutpkts.get_name_leafdata())
            if (self.cipsecglobaloutuncompoctets.is_set or self.cipsecglobaloutuncompoctets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobaloutuncompoctets.get_name_leafdata())
            if (self.cipsecglobaloutuncompoctwraps.is_set or self.cipsecglobaloutuncompoctwraps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobaloutuncompoctwraps.get_name_leafdata())
            if (self.cipsecglobalprevioustunnels.is_set or self.cipsecglobalprevioustunnels.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalprevioustunnels.get_name_leafdata())
            if (self.cipsecglobalprotocolusefails.is_set or self.cipsecglobalprotocolusefails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalprotocolusefails.get_name_leafdata())
            if (self.cipsecglobalsyscapfails.is_set or self.cipsecglobalsyscapfails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecglobalsyscapfails.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipSecGlobalActiveTunnels" or name == "cipSecGlobalHcInDecompOctets" or name == "cipSecGlobalHcInOctets" or name == "cipSecGlobalHcOutOctets" or name == "cipSecGlobalHcOutUncompOctets" or name == "cipSecGlobalInAuthFails" or name == "cipSecGlobalInAuths" or name == "cipSecGlobalInDecompOctets" or name == "cipSecGlobalInDecompOctWraps" or name == "cipSecGlobalInDecryptFails" or name == "cipSecGlobalInDecrypts" or name == "cipSecGlobalInDrops" or name == "cipSecGlobalInOctets" or name == "cipSecGlobalInOctWraps" or name == "cipSecGlobalInPkts" or name == "cipSecGlobalInReplayDrops" or name == "cipSecGlobalNoSaFails" or name == "cipSecGlobalOutAuthFails" or name == "cipSecGlobalOutAuths" or name == "cipSecGlobalOutDrops" or name == "cipSecGlobalOutEncryptFails" or name == "cipSecGlobalOutEncrypts" or name == "cipSecGlobalOutOctets" or name == "cipSecGlobalOutOctWraps" or name == "cipSecGlobalOutPkts" or name == "cipSecGlobalOutUncompOctets" or name == "cipSecGlobalOutUncompOctWraps" or name == "cipSecGlobalPreviousTunnels" or name == "cipSecGlobalProtocolUseFails" or name == "cipSecGlobalSysCapFails"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cipSecGlobalActiveTunnels"):
                self.cipsecglobalactivetunnels = value
                self.cipsecglobalactivetunnels.value_namespace = name_space
                self.cipsecglobalactivetunnels.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalHcInDecompOctets"):
                self.cipsecglobalhcindecompoctets = value
                self.cipsecglobalhcindecompoctets.value_namespace = name_space
                self.cipsecglobalhcindecompoctets.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalHcInOctets"):
                self.cipsecglobalhcinoctets = value
                self.cipsecglobalhcinoctets.value_namespace = name_space
                self.cipsecglobalhcinoctets.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalHcOutOctets"):
                self.cipsecglobalhcoutoctets = value
                self.cipsecglobalhcoutoctets.value_namespace = name_space
                self.cipsecglobalhcoutoctets.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalHcOutUncompOctets"):
                self.cipsecglobalhcoutuncompoctets = value
                self.cipsecglobalhcoutuncompoctets.value_namespace = name_space
                self.cipsecglobalhcoutuncompoctets.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalInAuthFails"):
                self.cipsecglobalinauthfails = value
                self.cipsecglobalinauthfails.value_namespace = name_space
                self.cipsecglobalinauthfails.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalInAuths"):
                self.cipsecglobalinauths = value
                self.cipsecglobalinauths.value_namespace = name_space
                self.cipsecglobalinauths.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalInDecompOctets"):
                self.cipsecglobalindecompoctets = value
                self.cipsecglobalindecompoctets.value_namespace = name_space
                self.cipsecglobalindecompoctets.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalInDecompOctWraps"):
                self.cipsecglobalindecompoctwraps = value
                self.cipsecglobalindecompoctwraps.value_namespace = name_space
                self.cipsecglobalindecompoctwraps.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalInDecryptFails"):
                self.cipsecglobalindecryptfails = value
                self.cipsecglobalindecryptfails.value_namespace = name_space
                self.cipsecglobalindecryptfails.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalInDecrypts"):
                self.cipsecglobalindecrypts = value
                self.cipsecglobalindecrypts.value_namespace = name_space
                self.cipsecglobalindecrypts.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalInDrops"):
                self.cipsecglobalindrops = value
                self.cipsecglobalindrops.value_namespace = name_space
                self.cipsecglobalindrops.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalInOctets"):
                self.cipsecglobalinoctets = value
                self.cipsecglobalinoctets.value_namespace = name_space
                self.cipsecglobalinoctets.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalInOctWraps"):
                self.cipsecglobalinoctwraps = value
                self.cipsecglobalinoctwraps.value_namespace = name_space
                self.cipsecglobalinoctwraps.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalInPkts"):
                self.cipsecglobalinpkts = value
                self.cipsecglobalinpkts.value_namespace = name_space
                self.cipsecglobalinpkts.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalInReplayDrops"):
                self.cipsecglobalinreplaydrops = value
                self.cipsecglobalinreplaydrops.value_namespace = name_space
                self.cipsecglobalinreplaydrops.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalNoSaFails"):
                self.cipsecglobalnosafails = value
                self.cipsecglobalnosafails.value_namespace = name_space
                self.cipsecglobalnosafails.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalOutAuthFails"):
                self.cipsecglobaloutauthfails = value
                self.cipsecglobaloutauthfails.value_namespace = name_space
                self.cipsecglobaloutauthfails.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalOutAuths"):
                self.cipsecglobaloutauths = value
                self.cipsecglobaloutauths.value_namespace = name_space
                self.cipsecglobaloutauths.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalOutDrops"):
                self.cipsecglobaloutdrops = value
                self.cipsecglobaloutdrops.value_namespace = name_space
                self.cipsecglobaloutdrops.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalOutEncryptFails"):
                self.cipsecglobaloutencryptfails = value
                self.cipsecglobaloutencryptfails.value_namespace = name_space
                self.cipsecglobaloutencryptfails.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalOutEncrypts"):
                self.cipsecglobaloutencrypts = value
                self.cipsecglobaloutencrypts.value_namespace = name_space
                self.cipsecglobaloutencrypts.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalOutOctets"):
                self.cipsecglobaloutoctets = value
                self.cipsecglobaloutoctets.value_namespace = name_space
                self.cipsecglobaloutoctets.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalOutOctWraps"):
                self.cipsecglobaloutoctwraps = value
                self.cipsecglobaloutoctwraps.value_namespace = name_space
                self.cipsecglobaloutoctwraps.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalOutPkts"):
                self.cipsecglobaloutpkts = value
                self.cipsecglobaloutpkts.value_namespace = name_space
                self.cipsecglobaloutpkts.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalOutUncompOctets"):
                self.cipsecglobaloutuncompoctets = value
                self.cipsecglobaloutuncompoctets.value_namespace = name_space
                self.cipsecglobaloutuncompoctets.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalOutUncompOctWraps"):
                self.cipsecglobaloutuncompoctwraps = value
                self.cipsecglobaloutuncompoctwraps.value_namespace = name_space
                self.cipsecglobaloutuncompoctwraps.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalPreviousTunnels"):
                self.cipsecglobalprevioustunnels = value
                self.cipsecglobalprevioustunnels.value_namespace = name_space
                self.cipsecglobalprevioustunnels.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalProtocolUseFails"):
                self.cipsecglobalprotocolusefails = value
                self.cipsecglobalprotocolusefails.value_namespace = name_space
                self.cipsecglobalprotocolusefails.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecGlobalSysCapFails"):
                self.cipsecglobalsyscapfails = value
                self.cipsecglobalsyscapfails.value_namespace = name_space
                self.cipsecglobalsyscapfails.value_namespace_prefix = name_space_prefix


    class Cipsechistglobalcntl(Entity):
        """
        
        
        .. attribute:: cipsechistcheckpoint
        
        	The current state of check point processing.  This object will return ready when the agent is  ready to create on\-demand history entries for  active IPsec Tunnels or checkPoint when the  agent is currently creating on\-demand history  entries for active IPsec Tunnels.  By setting this value to checkPoint, the agent  will create\: a) an entry in the IPsec Phase\-1 Tunnel History     for each active IPsec Phase\-1 Tunnel and b) an entry in the IPsec Phase\-2 Tunnel History     Table and an entry in the IPsec Phase\-2     Tunnel EndPoint History Table    for each active IPsec Phase\-2 Tunnel
        	**type**\:   :py:class:`Cipsechistcheckpoint <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsechistglobalcntl.Cipsechistcheckpoint>`
        
        .. attribute:: cipsechisttablesize
        
        	The window size of the IPsec Phase\-1 and Phase\-2 History Tables.  The IPsec Phase\-1 and Phase\-2 History Tables are implemented as a sliding window in which only the last n entries are maintained.  This object is used specify the number of entries which will be  maintained in the IPsec Phase\-1 and  Phase\-2 History Tables.  An implementation may choose suitable minimum and  maximum values for this element based on the local  policy and available resources. If an SNMP SET request  specifies a value outside this window for this element,  a BAD VALUE may be returned
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CiscoIpsecFlowMonitorMib.Cipsechistglobalcntl, self).__init__()

            self.yang_name = "cipSecHistGlobalCntl"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

            self.cipsechistcheckpoint = YLeaf(YType.enumeration, "cipSecHistCheckPoint")

            self.cipsechisttablesize = YLeaf(YType.int32, "cipSecHistTableSize")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cipsechistcheckpoint",
                            "cipsechisttablesize") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpsecFlowMonitorMib.Cipsechistglobalcntl, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Cipsechistglobalcntl, self).__setattr__(name, value)

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


        def has_data(self):
            return (
                self.cipsechistcheckpoint.is_set or
                self.cipsechisttablesize.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cipsechistcheckpoint.yfilter != YFilter.not_set or
                self.cipsechisttablesize.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipSecHistGlobalCntl" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cipsechistcheckpoint.is_set or self.cipsechistcheckpoint.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsechistcheckpoint.get_name_leafdata())
            if (self.cipsechisttablesize.is_set or self.cipsechisttablesize.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsechisttablesize.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipSecHistCheckPoint" or name == "cipSecHistTableSize"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cipSecHistCheckPoint"):
                self.cipsechistcheckpoint = value
                self.cipsechistcheckpoint.value_namespace = name_space
                self.cipsechistcheckpoint.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecHistTableSize"):
                self.cipsechisttablesize = value
                self.cipsechisttablesize.value_namespace = name_space
                self.cipsechisttablesize.value_namespace_prefix = name_space_prefix


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
            super(CiscoIpsecFlowMonitorMib.Cipsecfailglobalcntl, self).__init__()

            self.yang_name = "cipSecFailGlobalCntl"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

            self.cipsecfailtablesize = YLeaf(YType.int32, "cipSecFailTableSize")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cipsecfailtablesize") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpsecFlowMonitorMib.Cipsecfailglobalcntl, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Cipsecfailglobalcntl, self).__setattr__(name, value)

        def has_data(self):
            return self.cipsecfailtablesize.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cipsecfailtablesize.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipSecFailGlobalCntl" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cipsecfailtablesize.is_set or self.cipsecfailtablesize.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsecfailtablesize.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipSecFailTableSize"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cipSecFailTableSize"):
                self.cipsecfailtablesize = value
                self.cipsecfailtablesize.value_namespace = name_space
                self.cipsecfailtablesize.value_namespace_prefix = name_space_prefix


    class Cipsectrapcntl(Entity):
        """
        
        
        .. attribute:: cipsectrapcntlikecertcrlfailure
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 Certificate/CRL Failure TRAP
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Trapstatus>`
        
        .. attribute:: cipsectrapcntlikenosa
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 No Security Association TRAP
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Trapstatus>`
        
        .. attribute:: cipsectrapcntlikeprotocolfail
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 Protocol Failure TRAP
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Trapstatus>`
        
        .. attribute:: cipsectrapcntlikesysfailure
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 System Failure TRAP
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Trapstatus>`
        
        .. attribute:: cipsectrapcntliketunnelstart
        
        	This object defines the administrative state of sending the IPsec IKE Phase\-1 Tunnel Start TRAP
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Trapstatus>`
        
        .. attribute:: cipsectrapcntliketunnelstop
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 Tunnel Stop TRAP
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Trapstatus>`
        
        .. attribute:: cipsectrapcntlipsecearlytunterm
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Early Tunnel Termination TRAP
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Trapstatus>`
        
        .. attribute:: cipsectrapcntlipsecnosa
        
        	This object defines the administrative state of sending the IPsec  Phase\-2  No Security Association TRAP
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Trapstatus>`
        
        .. attribute:: cipsectrapcntlipsecprotocolfail
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Protocol Failure TRAP
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Trapstatus>`
        
        .. attribute:: cipsectrapcntlipsecsetupfailure
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Set Up Failure TRAP
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Trapstatus>`
        
        .. attribute:: cipsectrapcntlipsecsysfailure
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 System Failure TRAP
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Trapstatus>`
        
        .. attribute:: cipsectrapcntlipsectunnelstart
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Tunnel Start TRAP
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Trapstatus>`
        
        .. attribute:: cipsectrapcntlipsectunnelstop
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Tunnel Stop TRAP
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Trapstatus>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CiscoIpsecFlowMonitorMib.Cipsectrapcntl, self).__init__()

            self.yang_name = "cipSecTrapCntl"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

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

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cipsectrapcntlikecertcrlfailure",
                            "cipsectrapcntlikenosa",
                            "cipsectrapcntlikeprotocolfail",
                            "cipsectrapcntlikesysfailure",
                            "cipsectrapcntliketunnelstart",
                            "cipsectrapcntliketunnelstop",
                            "cipsectrapcntlipsecearlytunterm",
                            "cipsectrapcntlipsecnosa",
                            "cipsectrapcntlipsecprotocolfail",
                            "cipsectrapcntlipsecsetupfailure",
                            "cipsectrapcntlipsecsysfailure",
                            "cipsectrapcntlipsectunnelstart",
                            "cipsectrapcntlipsectunnelstop") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpsecFlowMonitorMib.Cipsectrapcntl, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Cipsectrapcntl, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cipsectrapcntlikecertcrlfailure.is_set or
                self.cipsectrapcntlikenosa.is_set or
                self.cipsectrapcntlikeprotocolfail.is_set or
                self.cipsectrapcntlikesysfailure.is_set or
                self.cipsectrapcntliketunnelstart.is_set or
                self.cipsectrapcntliketunnelstop.is_set or
                self.cipsectrapcntlipsecearlytunterm.is_set or
                self.cipsectrapcntlipsecnosa.is_set or
                self.cipsectrapcntlipsecprotocolfail.is_set or
                self.cipsectrapcntlipsecsetupfailure.is_set or
                self.cipsectrapcntlipsecsysfailure.is_set or
                self.cipsectrapcntlipsectunnelstart.is_set or
                self.cipsectrapcntlipsectunnelstop.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cipsectrapcntlikecertcrlfailure.yfilter != YFilter.not_set or
                self.cipsectrapcntlikenosa.yfilter != YFilter.not_set or
                self.cipsectrapcntlikeprotocolfail.yfilter != YFilter.not_set or
                self.cipsectrapcntlikesysfailure.yfilter != YFilter.not_set or
                self.cipsectrapcntliketunnelstart.yfilter != YFilter.not_set or
                self.cipsectrapcntliketunnelstop.yfilter != YFilter.not_set or
                self.cipsectrapcntlipsecearlytunterm.yfilter != YFilter.not_set or
                self.cipsectrapcntlipsecnosa.yfilter != YFilter.not_set or
                self.cipsectrapcntlipsecprotocolfail.yfilter != YFilter.not_set or
                self.cipsectrapcntlipsecsetupfailure.yfilter != YFilter.not_set or
                self.cipsectrapcntlipsecsysfailure.yfilter != YFilter.not_set or
                self.cipsectrapcntlipsectunnelstart.yfilter != YFilter.not_set or
                self.cipsectrapcntlipsectunnelstop.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipSecTrapCntl" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cipsectrapcntlikecertcrlfailure.is_set or self.cipsectrapcntlikecertcrlfailure.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsectrapcntlikecertcrlfailure.get_name_leafdata())
            if (self.cipsectrapcntlikenosa.is_set or self.cipsectrapcntlikenosa.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsectrapcntlikenosa.get_name_leafdata())
            if (self.cipsectrapcntlikeprotocolfail.is_set or self.cipsectrapcntlikeprotocolfail.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsectrapcntlikeprotocolfail.get_name_leafdata())
            if (self.cipsectrapcntlikesysfailure.is_set or self.cipsectrapcntlikesysfailure.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsectrapcntlikesysfailure.get_name_leafdata())
            if (self.cipsectrapcntliketunnelstart.is_set or self.cipsectrapcntliketunnelstart.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsectrapcntliketunnelstart.get_name_leafdata())
            if (self.cipsectrapcntliketunnelstop.is_set or self.cipsectrapcntliketunnelstop.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsectrapcntliketunnelstop.get_name_leafdata())
            if (self.cipsectrapcntlipsecearlytunterm.is_set or self.cipsectrapcntlipsecearlytunterm.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsectrapcntlipsecearlytunterm.get_name_leafdata())
            if (self.cipsectrapcntlipsecnosa.is_set or self.cipsectrapcntlipsecnosa.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsectrapcntlipsecnosa.get_name_leafdata())
            if (self.cipsectrapcntlipsecprotocolfail.is_set or self.cipsectrapcntlipsecprotocolfail.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsectrapcntlipsecprotocolfail.get_name_leafdata())
            if (self.cipsectrapcntlipsecsetupfailure.is_set or self.cipsectrapcntlipsecsetupfailure.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsectrapcntlipsecsetupfailure.get_name_leafdata())
            if (self.cipsectrapcntlipsecsysfailure.is_set or self.cipsectrapcntlipsecsysfailure.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsectrapcntlipsecsysfailure.get_name_leafdata())
            if (self.cipsectrapcntlipsectunnelstart.is_set or self.cipsectrapcntlipsectunnelstart.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsectrapcntlipsectunnelstart.get_name_leafdata())
            if (self.cipsectrapcntlipsectunnelstop.is_set or self.cipsectrapcntlipsectunnelstop.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsectrapcntlipsectunnelstop.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipSecTrapCntlIkeCertCrlFailure" or name == "cipSecTrapCntlIkeNoSa" or name == "cipSecTrapCntlIkeProtocolFail" or name == "cipSecTrapCntlIkeSysFailure" or name == "cipSecTrapCntlIkeTunnelStart" or name == "cipSecTrapCntlIkeTunnelStop" or name == "cipSecTrapCntlIpSecEarlyTunTerm" or name == "cipSecTrapCntlIpSecNoSa" or name == "cipSecTrapCntlIpSecProtocolFail" or name == "cipSecTrapCntlIpSecSetUpFailure" or name == "cipSecTrapCntlIpSecSysFailure" or name == "cipSecTrapCntlIpSecTunnelStart" or name == "cipSecTrapCntlIpSecTunnelStop"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cipSecTrapCntlIkeCertCrlFailure"):
                self.cipsectrapcntlikecertcrlfailure = value
                self.cipsectrapcntlikecertcrlfailure.value_namespace = name_space
                self.cipsectrapcntlikecertcrlfailure.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecTrapCntlIkeNoSa"):
                self.cipsectrapcntlikenosa = value
                self.cipsectrapcntlikenosa.value_namespace = name_space
                self.cipsectrapcntlikenosa.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecTrapCntlIkeProtocolFail"):
                self.cipsectrapcntlikeprotocolfail = value
                self.cipsectrapcntlikeprotocolfail.value_namespace = name_space
                self.cipsectrapcntlikeprotocolfail.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecTrapCntlIkeSysFailure"):
                self.cipsectrapcntlikesysfailure = value
                self.cipsectrapcntlikesysfailure.value_namespace = name_space
                self.cipsectrapcntlikesysfailure.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecTrapCntlIkeTunnelStart"):
                self.cipsectrapcntliketunnelstart = value
                self.cipsectrapcntliketunnelstart.value_namespace = name_space
                self.cipsectrapcntliketunnelstart.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecTrapCntlIkeTunnelStop"):
                self.cipsectrapcntliketunnelstop = value
                self.cipsectrapcntliketunnelstop.value_namespace = name_space
                self.cipsectrapcntliketunnelstop.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecTrapCntlIpSecEarlyTunTerm"):
                self.cipsectrapcntlipsecearlytunterm = value
                self.cipsectrapcntlipsecearlytunterm.value_namespace = name_space
                self.cipsectrapcntlipsecearlytunterm.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecTrapCntlIpSecNoSa"):
                self.cipsectrapcntlipsecnosa = value
                self.cipsectrapcntlipsecnosa.value_namespace = name_space
                self.cipsectrapcntlipsecnosa.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecTrapCntlIpSecProtocolFail"):
                self.cipsectrapcntlipsecprotocolfail = value
                self.cipsectrapcntlipsecprotocolfail.value_namespace = name_space
                self.cipsectrapcntlipsecprotocolfail.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecTrapCntlIpSecSetUpFailure"):
                self.cipsectrapcntlipsecsetupfailure = value
                self.cipsectrapcntlipsecsetupfailure.value_namespace = name_space
                self.cipsectrapcntlipsecsetupfailure.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecTrapCntlIpSecSysFailure"):
                self.cipsectrapcntlipsecsysfailure = value
                self.cipsectrapcntlipsecsysfailure.value_namespace = name_space
                self.cipsectrapcntlipsecsysfailure.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecTrapCntlIpSecTunnelStart"):
                self.cipsectrapcntlipsectunnelstart = value
                self.cipsectrapcntlipsectunnelstart.value_namespace = name_space
                self.cipsectrapcntlipsectunnelstart.value_namespace_prefix = name_space_prefix
            if(value_path == "cipSecTrapCntlIpSecTunnelStop"):
                self.cipsectrapcntlipsectunnelstop = value
                self.cipsectrapcntlipsectunnelstop.value_namespace = name_space
                self.cipsectrapcntlipsectunnelstop.value_namespace_prefix = name_space_prefix


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
        	**type**\: list of    :py:class:`Cikepeerentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cikepeertable.Cikepeerentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CiscoIpsecFlowMonitorMib.Cikepeertable, self).__init__()

            self.yang_name = "cikePeerTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

            self.cikepeerentry = YList(self)

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
                        super(CiscoIpsecFlowMonitorMib.Cikepeertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Cikepeertable, self).__setattr__(name, value)


        class Cikepeerentry(Entity):
            """
            Each entry contains the attributes associated
            with an IPsec Phase\-1 IKE peer association.
            
            .. attribute:: cikepeerlocaltype  <key>
            
            	The type of local peer identity.  The local peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\:   :py:class:`Ikepeertype <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Ikepeertype>`
            
            .. attribute:: cikepeerlocalvalue  <key>
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\:  str
            
            .. attribute:: cikepeerremotetype  <key>
            
            	The type of remote peer identity.  The remote peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\:   :py:class:`Ikepeertype <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Ikepeertype>`
            
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
                super(CiscoIpsecFlowMonitorMib.Cikepeertable.Cikepeerentry, self).__init__()

                self.yang_name = "cikePeerEntry"
                self.yang_parent_name = "cikePeerTable"

                self.cikepeerlocaltype = YLeaf(YType.enumeration, "cikePeerLocalType")

                self.cikepeerlocalvalue = YLeaf(YType.str, "cikePeerLocalValue")

                self.cikepeerremotetype = YLeaf(YType.enumeration, "cikePeerRemoteType")

                self.cikepeerremotevalue = YLeaf(YType.str, "cikePeerRemoteValue")

                self.cikepeerintindex = YLeaf(YType.int32, "cikePeerIntIndex")

                self.cikepeeractivetime = YLeaf(YType.int32, "cikePeerActiveTime")

                self.cikepeeractivetunnelindex = YLeaf(YType.int32, "cikePeerActiveTunnelIndex")

                self.cikepeerlocaladdr = YLeaf(YType.str, "cikePeerLocalAddr")

                self.cikepeerremoteaddr = YLeaf(YType.str, "cikePeerRemoteAddr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cikepeerlocaltype",
                                "cikepeerlocalvalue",
                                "cikepeerremotetype",
                                "cikepeerremotevalue",
                                "cikepeerintindex",
                                "cikepeeractivetime",
                                "cikepeeractivetunnelindex",
                                "cikepeerlocaladdr",
                                "cikepeerremoteaddr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecFlowMonitorMib.Cikepeertable.Cikepeerentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecFlowMonitorMib.Cikepeertable.Cikepeerentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cikepeerlocaltype.is_set or
                    self.cikepeerlocalvalue.is_set or
                    self.cikepeerremotetype.is_set or
                    self.cikepeerremotevalue.is_set or
                    self.cikepeerintindex.is_set or
                    self.cikepeeractivetime.is_set or
                    self.cikepeeractivetunnelindex.is_set or
                    self.cikepeerlocaladdr.is_set or
                    self.cikepeerremoteaddr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cikepeerlocaltype.yfilter != YFilter.not_set or
                    self.cikepeerlocalvalue.yfilter != YFilter.not_set or
                    self.cikepeerremotetype.yfilter != YFilter.not_set or
                    self.cikepeerremotevalue.yfilter != YFilter.not_set or
                    self.cikepeerintindex.yfilter != YFilter.not_set or
                    self.cikepeeractivetime.yfilter != YFilter.not_set or
                    self.cikepeeractivetunnelindex.yfilter != YFilter.not_set or
                    self.cikepeerlocaladdr.yfilter != YFilter.not_set or
                    self.cikepeerremoteaddr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cikePeerEntry" + "[cikePeerLocalType='" + self.cikepeerlocaltype.get() + "']" + "[cikePeerLocalValue='" + self.cikepeerlocalvalue.get() + "']" + "[cikePeerRemoteType='" + self.cikepeerremotetype.get() + "']" + "[cikePeerRemoteValue='" + self.cikepeerremotevalue.get() + "']" + "[cikePeerIntIndex='" + self.cikepeerintindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikePeerTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cikepeerlocaltype.is_set or self.cikepeerlocaltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikepeerlocaltype.get_name_leafdata())
                if (self.cikepeerlocalvalue.is_set or self.cikepeerlocalvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikepeerlocalvalue.get_name_leafdata())
                if (self.cikepeerremotetype.is_set or self.cikepeerremotetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikepeerremotetype.get_name_leafdata())
                if (self.cikepeerremotevalue.is_set or self.cikepeerremotevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikepeerremotevalue.get_name_leafdata())
                if (self.cikepeerintindex.is_set or self.cikepeerintindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikepeerintindex.get_name_leafdata())
                if (self.cikepeeractivetime.is_set or self.cikepeeractivetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikepeeractivetime.get_name_leafdata())
                if (self.cikepeeractivetunnelindex.is_set or self.cikepeeractivetunnelindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikepeeractivetunnelindex.get_name_leafdata())
                if (self.cikepeerlocaladdr.is_set or self.cikepeerlocaladdr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikepeerlocaladdr.get_name_leafdata())
                if (self.cikepeerremoteaddr.is_set or self.cikepeerremoteaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikepeerremoteaddr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cikePeerLocalType" or name == "cikePeerLocalValue" or name == "cikePeerRemoteType" or name == "cikePeerRemoteValue" or name == "cikePeerIntIndex" or name == "cikePeerActiveTime" or name == "cikePeerActiveTunnelIndex" or name == "cikePeerLocalAddr" or name == "cikePeerRemoteAddr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cikePeerLocalType"):
                    self.cikepeerlocaltype = value
                    self.cikepeerlocaltype.value_namespace = name_space
                    self.cikepeerlocaltype.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePeerLocalValue"):
                    self.cikepeerlocalvalue = value
                    self.cikepeerlocalvalue.value_namespace = name_space
                    self.cikepeerlocalvalue.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePeerRemoteType"):
                    self.cikepeerremotetype = value
                    self.cikepeerremotetype.value_namespace = name_space
                    self.cikepeerremotetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePeerRemoteValue"):
                    self.cikepeerremotevalue = value
                    self.cikepeerremotevalue.value_namespace = name_space
                    self.cikepeerremotevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePeerIntIndex"):
                    self.cikepeerintindex = value
                    self.cikepeerintindex.value_namespace = name_space
                    self.cikepeerintindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePeerActiveTime"):
                    self.cikepeeractivetime = value
                    self.cikepeeractivetime.value_namespace = name_space
                    self.cikepeeractivetime.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePeerActiveTunnelIndex"):
                    self.cikepeeractivetunnelindex = value
                    self.cikepeeractivetunnelindex.value_namespace = name_space
                    self.cikepeeractivetunnelindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePeerLocalAddr"):
                    self.cikepeerlocaladdr = value
                    self.cikepeerlocaladdr.value_namespace = name_space
                    self.cikepeerlocaladdr.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePeerRemoteAddr"):
                    self.cikepeerremoteaddr = value
                    self.cikepeerremoteaddr.value_namespace = name_space
                    self.cikepeerremoteaddr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cikepeerentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cikepeerentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cikePeerTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cikePeerEntry"):
                for c in self.cikepeerentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecFlowMonitorMib.Cikepeertable.Cikepeerentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cikepeerentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cikePeerEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciketunneltable(Entity):
        """
        The IPsec Phase\-1 Internet Key Exchange Tunnel Table.
        There is one entry in this table for each active IPsec
        Phase\-1 IKE Tunnel.
        
        .. attribute:: ciketunnelentry
        
        	Each entry contains the attributes associated with an active IPsec Phase\-1 IKE Tunnel
        	**type**\: list of    :py:class:`Ciketunnelentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Ciketunneltable.Ciketunnelentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CiscoIpsecFlowMonitorMib.Ciketunneltable, self).__init__()

            self.yang_name = "cikeTunnelTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

            self.ciketunnelentry = YList(self)

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
                        super(CiscoIpsecFlowMonitorMib.Ciketunneltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Ciketunneltable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Ikeauthmethod <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Ikeauthmethod>`
            
            .. attribute:: ciketundiffhellmangrp
            
            	The Diffie Hellman Group used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`Diffhellmangrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Diffhellmangrp>`
            
            .. attribute:: ciketunencryptalgo
            
            	The encryption algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`Encryptalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Encryptalgo>`
            
            .. attribute:: ciketunhashalgo
            
            	The hash algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`Ikehashalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Ikehashalgo>`
            
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
            	**type**\:   :py:class:`Ikepeertype <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Ikepeertype>`
            
            .. attribute:: ciketunlocalvalue
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\:  str
            
            .. attribute:: ciketunnegomode
            
            	The negotiation mode of the IPsec Phase\-1 IKE Tunnel
            	**type**\:   :py:class:`Ikenegomode <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Ikenegomode>`
            
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
            	**type**\:   :py:class:`Ikepeertype <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Ikepeertype>`
            
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
            	**type**\:   :py:class:`Tunnelstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Tunnelstatus>`
            
            .. attribute:: ciketuntotalrefreshes
            
            	The total number of security associations refreshes performed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: QM Exchanges
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CiscoIpsecFlowMonitorMib.Ciketunneltable.Ciketunnelentry, self).__init__()

                self.yang_name = "cikeTunnelEntry"
                self.yang_parent_name = "cikeTunnelTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciketunindex",
                                "ciketunactivetime",
                                "ciketunauthmethod",
                                "ciketundiffhellmangrp",
                                "ciketunencryptalgo",
                                "ciketunhashalgo",
                                "ciketunindroppkts",
                                "ciketuninnotifys",
                                "ciketuninoctets",
                                "ciketuninp2exchginvalids",
                                "ciketuninp2exchgrejects",
                                "ciketuninp2exchgs",
                                "ciketuninp2sadelrequests",
                                "ciketuninpkts",
                                "ciketunlifetime",
                                "ciketunlocaladdr",
                                "ciketunlocalname",
                                "ciketunlocaltype",
                                "ciketunlocalvalue",
                                "ciketunnegomode",
                                "ciketunoutdroppkts",
                                "ciketunoutnotifys",
                                "ciketunoutoctets",
                                "ciketunoutp2exchginvalids",
                                "ciketunoutp2exchgrejects",
                                "ciketunoutp2exchgs",
                                "ciketunoutp2sadelrequests",
                                "ciketunoutpkts",
                                "ciketunremoteaddr",
                                "ciketunremotename",
                                "ciketunremotetype",
                                "ciketunremotevalue",
                                "ciketunsarefreshthreshold",
                                "ciketunstatus",
                                "ciketuntotalrefreshes") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecFlowMonitorMib.Ciketunneltable.Ciketunnelentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecFlowMonitorMib.Ciketunneltable.Ciketunnelentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ciketunindex.is_set or
                    self.ciketunactivetime.is_set or
                    self.ciketunauthmethod.is_set or
                    self.ciketundiffhellmangrp.is_set or
                    self.ciketunencryptalgo.is_set or
                    self.ciketunhashalgo.is_set or
                    self.ciketunindroppkts.is_set or
                    self.ciketuninnotifys.is_set or
                    self.ciketuninoctets.is_set or
                    self.ciketuninp2exchginvalids.is_set or
                    self.ciketuninp2exchgrejects.is_set or
                    self.ciketuninp2exchgs.is_set or
                    self.ciketuninp2sadelrequests.is_set or
                    self.ciketuninpkts.is_set or
                    self.ciketunlifetime.is_set or
                    self.ciketunlocaladdr.is_set or
                    self.ciketunlocalname.is_set or
                    self.ciketunlocaltype.is_set or
                    self.ciketunlocalvalue.is_set or
                    self.ciketunnegomode.is_set or
                    self.ciketunoutdroppkts.is_set or
                    self.ciketunoutnotifys.is_set or
                    self.ciketunoutoctets.is_set or
                    self.ciketunoutp2exchginvalids.is_set or
                    self.ciketunoutp2exchgrejects.is_set or
                    self.ciketunoutp2exchgs.is_set or
                    self.ciketunoutp2sadelrequests.is_set or
                    self.ciketunoutpkts.is_set or
                    self.ciketunremoteaddr.is_set or
                    self.ciketunremotename.is_set or
                    self.ciketunremotetype.is_set or
                    self.ciketunremotevalue.is_set or
                    self.ciketunsarefreshthreshold.is_set or
                    self.ciketunstatus.is_set or
                    self.ciketuntotalrefreshes.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciketunindex.yfilter != YFilter.not_set or
                    self.ciketunactivetime.yfilter != YFilter.not_set or
                    self.ciketunauthmethod.yfilter != YFilter.not_set or
                    self.ciketundiffhellmangrp.yfilter != YFilter.not_set or
                    self.ciketunencryptalgo.yfilter != YFilter.not_set or
                    self.ciketunhashalgo.yfilter != YFilter.not_set or
                    self.ciketunindroppkts.yfilter != YFilter.not_set or
                    self.ciketuninnotifys.yfilter != YFilter.not_set or
                    self.ciketuninoctets.yfilter != YFilter.not_set or
                    self.ciketuninp2exchginvalids.yfilter != YFilter.not_set or
                    self.ciketuninp2exchgrejects.yfilter != YFilter.not_set or
                    self.ciketuninp2exchgs.yfilter != YFilter.not_set or
                    self.ciketuninp2sadelrequests.yfilter != YFilter.not_set or
                    self.ciketuninpkts.yfilter != YFilter.not_set or
                    self.ciketunlifetime.yfilter != YFilter.not_set or
                    self.ciketunlocaladdr.yfilter != YFilter.not_set or
                    self.ciketunlocalname.yfilter != YFilter.not_set or
                    self.ciketunlocaltype.yfilter != YFilter.not_set or
                    self.ciketunlocalvalue.yfilter != YFilter.not_set or
                    self.ciketunnegomode.yfilter != YFilter.not_set or
                    self.ciketunoutdroppkts.yfilter != YFilter.not_set or
                    self.ciketunoutnotifys.yfilter != YFilter.not_set or
                    self.ciketunoutoctets.yfilter != YFilter.not_set or
                    self.ciketunoutp2exchginvalids.yfilter != YFilter.not_set or
                    self.ciketunoutp2exchgrejects.yfilter != YFilter.not_set or
                    self.ciketunoutp2exchgs.yfilter != YFilter.not_set or
                    self.ciketunoutp2sadelrequests.yfilter != YFilter.not_set or
                    self.ciketunoutpkts.yfilter != YFilter.not_set or
                    self.ciketunremoteaddr.yfilter != YFilter.not_set or
                    self.ciketunremotename.yfilter != YFilter.not_set or
                    self.ciketunremotetype.yfilter != YFilter.not_set or
                    self.ciketunremotevalue.yfilter != YFilter.not_set or
                    self.ciketunsarefreshthreshold.yfilter != YFilter.not_set or
                    self.ciketunstatus.yfilter != YFilter.not_set or
                    self.ciketuntotalrefreshes.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cikeTunnelEntry" + "[cikeTunIndex='" + self.ciketunindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikeTunnelTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciketunindex.is_set or self.ciketunindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunindex.get_name_leafdata())
                if (self.ciketunactivetime.is_set or self.ciketunactivetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunactivetime.get_name_leafdata())
                if (self.ciketunauthmethod.is_set or self.ciketunauthmethod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunauthmethod.get_name_leafdata())
                if (self.ciketundiffhellmangrp.is_set or self.ciketundiffhellmangrp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketundiffhellmangrp.get_name_leafdata())
                if (self.ciketunencryptalgo.is_set or self.ciketunencryptalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunencryptalgo.get_name_leafdata())
                if (self.ciketunhashalgo.is_set or self.ciketunhashalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhashalgo.get_name_leafdata())
                if (self.ciketunindroppkts.is_set or self.ciketunindroppkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunindroppkts.get_name_leafdata())
                if (self.ciketuninnotifys.is_set or self.ciketuninnotifys.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketuninnotifys.get_name_leafdata())
                if (self.ciketuninoctets.is_set or self.ciketuninoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketuninoctets.get_name_leafdata())
                if (self.ciketuninp2exchginvalids.is_set or self.ciketuninp2exchginvalids.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketuninp2exchginvalids.get_name_leafdata())
                if (self.ciketuninp2exchgrejects.is_set or self.ciketuninp2exchgrejects.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketuninp2exchgrejects.get_name_leafdata())
                if (self.ciketuninp2exchgs.is_set or self.ciketuninp2exchgs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketuninp2exchgs.get_name_leafdata())
                if (self.ciketuninp2sadelrequests.is_set or self.ciketuninp2sadelrequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketuninp2sadelrequests.get_name_leafdata())
                if (self.ciketuninpkts.is_set or self.ciketuninpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketuninpkts.get_name_leafdata())
                if (self.ciketunlifetime.is_set or self.ciketunlifetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunlifetime.get_name_leafdata())
                if (self.ciketunlocaladdr.is_set or self.ciketunlocaladdr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunlocaladdr.get_name_leafdata())
                if (self.ciketunlocalname.is_set or self.ciketunlocalname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunlocalname.get_name_leafdata())
                if (self.ciketunlocaltype.is_set or self.ciketunlocaltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunlocaltype.get_name_leafdata())
                if (self.ciketunlocalvalue.is_set or self.ciketunlocalvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunlocalvalue.get_name_leafdata())
                if (self.ciketunnegomode.is_set or self.ciketunnegomode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunnegomode.get_name_leafdata())
                if (self.ciketunoutdroppkts.is_set or self.ciketunoutdroppkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunoutdroppkts.get_name_leafdata())
                if (self.ciketunoutnotifys.is_set or self.ciketunoutnotifys.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunoutnotifys.get_name_leafdata())
                if (self.ciketunoutoctets.is_set or self.ciketunoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunoutoctets.get_name_leafdata())
                if (self.ciketunoutp2exchginvalids.is_set or self.ciketunoutp2exchginvalids.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunoutp2exchginvalids.get_name_leafdata())
                if (self.ciketunoutp2exchgrejects.is_set or self.ciketunoutp2exchgrejects.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunoutp2exchgrejects.get_name_leafdata())
                if (self.ciketunoutp2exchgs.is_set or self.ciketunoutp2exchgs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunoutp2exchgs.get_name_leafdata())
                if (self.ciketunoutp2sadelrequests.is_set or self.ciketunoutp2sadelrequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunoutp2sadelrequests.get_name_leafdata())
                if (self.ciketunoutpkts.is_set or self.ciketunoutpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunoutpkts.get_name_leafdata())
                if (self.ciketunremoteaddr.is_set or self.ciketunremoteaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunremoteaddr.get_name_leafdata())
                if (self.ciketunremotename.is_set or self.ciketunremotename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunremotename.get_name_leafdata())
                if (self.ciketunremotetype.is_set or self.ciketunremotetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunremotetype.get_name_leafdata())
                if (self.ciketunremotevalue.is_set or self.ciketunremotevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunremotevalue.get_name_leafdata())
                if (self.ciketunsarefreshthreshold.is_set or self.ciketunsarefreshthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunsarefreshthreshold.get_name_leafdata())
                if (self.ciketunstatus.is_set or self.ciketunstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunstatus.get_name_leafdata())
                if (self.ciketuntotalrefreshes.is_set or self.ciketuntotalrefreshes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketuntotalrefreshes.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cikeTunIndex" or name == "cikeTunActiveTime" or name == "cikeTunAuthMethod" or name == "cikeTunDiffHellmanGrp" or name == "cikeTunEncryptAlgo" or name == "cikeTunHashAlgo" or name == "cikeTunInDropPkts" or name == "cikeTunInNotifys" or name == "cikeTunInOctets" or name == "cikeTunInP2ExchgInvalids" or name == "cikeTunInP2ExchgRejects" or name == "cikeTunInP2Exchgs" or name == "cikeTunInP2SaDelRequests" or name == "cikeTunInPkts" or name == "cikeTunLifeTime" or name == "cikeTunLocalAddr" or name == "cikeTunLocalName" or name == "cikeTunLocalType" or name == "cikeTunLocalValue" or name == "cikeTunNegoMode" or name == "cikeTunOutDropPkts" or name == "cikeTunOutNotifys" or name == "cikeTunOutOctets" or name == "cikeTunOutP2ExchgInvalids" or name == "cikeTunOutP2ExchgRejects" or name == "cikeTunOutP2Exchgs" or name == "cikeTunOutP2SaDelRequests" or name == "cikeTunOutPkts" or name == "cikeTunRemoteAddr" or name == "cikeTunRemoteName" or name == "cikeTunRemoteType" or name == "cikeTunRemoteValue" or name == "cikeTunSaRefreshThreshold" or name == "cikeTunStatus" or name == "cikeTunTotalRefreshes"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cikeTunIndex"):
                    self.ciketunindex = value
                    self.ciketunindex.value_namespace = name_space
                    self.ciketunindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunActiveTime"):
                    self.ciketunactivetime = value
                    self.ciketunactivetime.value_namespace = name_space
                    self.ciketunactivetime.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunAuthMethod"):
                    self.ciketunauthmethod = value
                    self.ciketunauthmethod.value_namespace = name_space
                    self.ciketunauthmethod.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunDiffHellmanGrp"):
                    self.ciketundiffhellmangrp = value
                    self.ciketundiffhellmangrp.value_namespace = name_space
                    self.ciketundiffhellmangrp.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunEncryptAlgo"):
                    self.ciketunencryptalgo = value
                    self.ciketunencryptalgo.value_namespace = name_space
                    self.ciketunencryptalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHashAlgo"):
                    self.ciketunhashalgo = value
                    self.ciketunhashalgo.value_namespace = name_space
                    self.ciketunhashalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunInDropPkts"):
                    self.ciketunindroppkts = value
                    self.ciketunindroppkts.value_namespace = name_space
                    self.ciketunindroppkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunInNotifys"):
                    self.ciketuninnotifys = value
                    self.ciketuninnotifys.value_namespace = name_space
                    self.ciketuninnotifys.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunInOctets"):
                    self.ciketuninoctets = value
                    self.ciketuninoctets.value_namespace = name_space
                    self.ciketuninoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunInP2ExchgInvalids"):
                    self.ciketuninp2exchginvalids = value
                    self.ciketuninp2exchginvalids.value_namespace = name_space
                    self.ciketuninp2exchginvalids.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunInP2ExchgRejects"):
                    self.ciketuninp2exchgrejects = value
                    self.ciketuninp2exchgrejects.value_namespace = name_space
                    self.ciketuninp2exchgrejects.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunInP2Exchgs"):
                    self.ciketuninp2exchgs = value
                    self.ciketuninp2exchgs.value_namespace = name_space
                    self.ciketuninp2exchgs.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunInP2SaDelRequests"):
                    self.ciketuninp2sadelrequests = value
                    self.ciketuninp2sadelrequests.value_namespace = name_space
                    self.ciketuninp2sadelrequests.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunInPkts"):
                    self.ciketuninpkts = value
                    self.ciketuninpkts.value_namespace = name_space
                    self.ciketuninpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunLifeTime"):
                    self.ciketunlifetime = value
                    self.ciketunlifetime.value_namespace = name_space
                    self.ciketunlifetime.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunLocalAddr"):
                    self.ciketunlocaladdr = value
                    self.ciketunlocaladdr.value_namespace = name_space
                    self.ciketunlocaladdr.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunLocalName"):
                    self.ciketunlocalname = value
                    self.ciketunlocalname.value_namespace = name_space
                    self.ciketunlocalname.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunLocalType"):
                    self.ciketunlocaltype = value
                    self.ciketunlocaltype.value_namespace = name_space
                    self.ciketunlocaltype.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunLocalValue"):
                    self.ciketunlocalvalue = value
                    self.ciketunlocalvalue.value_namespace = name_space
                    self.ciketunlocalvalue.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunNegoMode"):
                    self.ciketunnegomode = value
                    self.ciketunnegomode.value_namespace = name_space
                    self.ciketunnegomode.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunOutDropPkts"):
                    self.ciketunoutdroppkts = value
                    self.ciketunoutdroppkts.value_namespace = name_space
                    self.ciketunoutdroppkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunOutNotifys"):
                    self.ciketunoutnotifys = value
                    self.ciketunoutnotifys.value_namespace = name_space
                    self.ciketunoutnotifys.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunOutOctets"):
                    self.ciketunoutoctets = value
                    self.ciketunoutoctets.value_namespace = name_space
                    self.ciketunoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunOutP2ExchgInvalids"):
                    self.ciketunoutp2exchginvalids = value
                    self.ciketunoutp2exchginvalids.value_namespace = name_space
                    self.ciketunoutp2exchginvalids.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunOutP2ExchgRejects"):
                    self.ciketunoutp2exchgrejects = value
                    self.ciketunoutp2exchgrejects.value_namespace = name_space
                    self.ciketunoutp2exchgrejects.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunOutP2Exchgs"):
                    self.ciketunoutp2exchgs = value
                    self.ciketunoutp2exchgs.value_namespace = name_space
                    self.ciketunoutp2exchgs.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunOutP2SaDelRequests"):
                    self.ciketunoutp2sadelrequests = value
                    self.ciketunoutp2sadelrequests.value_namespace = name_space
                    self.ciketunoutp2sadelrequests.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunOutPkts"):
                    self.ciketunoutpkts = value
                    self.ciketunoutpkts.value_namespace = name_space
                    self.ciketunoutpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunRemoteAddr"):
                    self.ciketunremoteaddr = value
                    self.ciketunremoteaddr.value_namespace = name_space
                    self.ciketunremoteaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunRemoteName"):
                    self.ciketunremotename = value
                    self.ciketunremotename.value_namespace = name_space
                    self.ciketunremotename.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunRemoteType"):
                    self.ciketunremotetype = value
                    self.ciketunremotetype.value_namespace = name_space
                    self.ciketunremotetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunRemoteValue"):
                    self.ciketunremotevalue = value
                    self.ciketunremotevalue.value_namespace = name_space
                    self.ciketunremotevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunSaRefreshThreshold"):
                    self.ciketunsarefreshthreshold = value
                    self.ciketunsarefreshthreshold.value_namespace = name_space
                    self.ciketunsarefreshthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunStatus"):
                    self.ciketunstatus = value
                    self.ciketunstatus.value_namespace = name_space
                    self.ciketunstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunTotalRefreshes"):
                    self.ciketuntotalrefreshes = value
                    self.ciketuntotalrefreshes.value_namespace = name_space
                    self.ciketuntotalrefreshes.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciketunnelentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciketunnelentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cikeTunnelTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cikeTunnelEntry"):
                for c in self.ciketunnelentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecFlowMonitorMib.Ciketunneltable.Ciketunnelentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciketunnelentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cikeTunnelEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cikepeercorrtable(Entity):
        """
        The IPsec Phase\-1 Internet Key Exchange Peer
        Association to IPsec Phase\-2 Tunnel
        Correlation Table. There is one entry in
        this table for each active IPsec Phase\-2
        Tunnel.
        
        .. attribute:: cikepeercorrentry
        
        	Each entry contains the attributes of an IPsec Phase\-1 IKE Peer Association to IPsec Phase\-2 Tunnel Correlation
        	**type**\: list of    :py:class:`Cikepeercorrentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cikepeercorrtable.Cikepeercorrentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CiscoIpsecFlowMonitorMib.Cikepeercorrtable, self).__init__()

            self.yang_name = "cikePeerCorrTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

            self.cikepeercorrentry = YList(self)

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
                        super(CiscoIpsecFlowMonitorMib.Cikepeercorrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Cikepeercorrtable, self).__setattr__(name, value)


        class Cikepeercorrentry(Entity):
            """
            Each entry contains the attributes of an
            IPsec Phase\-1 IKE Peer Association to IPsec
            Phase\-2 Tunnel Correlation.
            
            .. attribute:: cikepeercorrlocaltype  <key>
            
            	The type of local peer identity. The local peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\:   :py:class:`Ikepeertype <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Ikepeertype>`
            
            .. attribute:: cikepeercorrlocalvalue  <key>
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\:  str
            
            .. attribute:: cikepeercorrremotetype  <key>
            
            	The type of remote peer identity. The remote peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\:   :py:class:`Ikepeertype <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Ikepeertype>`
            
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
                super(CiscoIpsecFlowMonitorMib.Cikepeercorrtable.Cikepeercorrentry, self).__init__()

                self.yang_name = "cikePeerCorrEntry"
                self.yang_parent_name = "cikePeerCorrTable"

                self.cikepeercorrlocaltype = YLeaf(YType.enumeration, "cikePeerCorrLocalType")

                self.cikepeercorrlocalvalue = YLeaf(YType.str, "cikePeerCorrLocalValue")

                self.cikepeercorrremotetype = YLeaf(YType.enumeration, "cikePeerCorrRemoteType")

                self.cikepeercorrremotevalue = YLeaf(YType.str, "cikePeerCorrRemoteValue")

                self.cikepeercorrintindex = YLeaf(YType.int32, "cikePeerCorrIntIndex")

                self.cikepeercorrseqnum = YLeaf(YType.int32, "cikePeerCorrSeqNum")

                self.cikepeercorripsectunindex = YLeaf(YType.int32, "cikePeerCorrIpSecTunIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cikepeercorrlocaltype",
                                "cikepeercorrlocalvalue",
                                "cikepeercorrremotetype",
                                "cikepeercorrremotevalue",
                                "cikepeercorrintindex",
                                "cikepeercorrseqnum",
                                "cikepeercorripsectunindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecFlowMonitorMib.Cikepeercorrtable.Cikepeercorrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecFlowMonitorMib.Cikepeercorrtable.Cikepeercorrentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cikepeercorrlocaltype.is_set or
                    self.cikepeercorrlocalvalue.is_set or
                    self.cikepeercorrremotetype.is_set or
                    self.cikepeercorrremotevalue.is_set or
                    self.cikepeercorrintindex.is_set or
                    self.cikepeercorrseqnum.is_set or
                    self.cikepeercorripsectunindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cikepeercorrlocaltype.yfilter != YFilter.not_set or
                    self.cikepeercorrlocalvalue.yfilter != YFilter.not_set or
                    self.cikepeercorrremotetype.yfilter != YFilter.not_set or
                    self.cikepeercorrremotevalue.yfilter != YFilter.not_set or
                    self.cikepeercorrintindex.yfilter != YFilter.not_set or
                    self.cikepeercorrseqnum.yfilter != YFilter.not_set or
                    self.cikepeercorripsectunindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cikePeerCorrEntry" + "[cikePeerCorrLocalType='" + self.cikepeercorrlocaltype.get() + "']" + "[cikePeerCorrLocalValue='" + self.cikepeercorrlocalvalue.get() + "']" + "[cikePeerCorrRemoteType='" + self.cikepeercorrremotetype.get() + "']" + "[cikePeerCorrRemoteValue='" + self.cikepeercorrremotevalue.get() + "']" + "[cikePeerCorrIntIndex='" + self.cikepeercorrintindex.get() + "']" + "[cikePeerCorrSeqNum='" + self.cikepeercorrseqnum.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikePeerCorrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cikepeercorrlocaltype.is_set or self.cikepeercorrlocaltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikepeercorrlocaltype.get_name_leafdata())
                if (self.cikepeercorrlocalvalue.is_set or self.cikepeercorrlocalvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikepeercorrlocalvalue.get_name_leafdata())
                if (self.cikepeercorrremotetype.is_set or self.cikepeercorrremotetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikepeercorrremotetype.get_name_leafdata())
                if (self.cikepeercorrremotevalue.is_set or self.cikepeercorrremotevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikepeercorrremotevalue.get_name_leafdata())
                if (self.cikepeercorrintindex.is_set or self.cikepeercorrintindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikepeercorrintindex.get_name_leafdata())
                if (self.cikepeercorrseqnum.is_set or self.cikepeercorrseqnum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikepeercorrseqnum.get_name_leafdata())
                if (self.cikepeercorripsectunindex.is_set or self.cikepeercorripsectunindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikepeercorripsectunindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cikePeerCorrLocalType" or name == "cikePeerCorrLocalValue" or name == "cikePeerCorrRemoteType" or name == "cikePeerCorrRemoteValue" or name == "cikePeerCorrIntIndex" or name == "cikePeerCorrSeqNum" or name == "cikePeerCorrIpSecTunIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cikePeerCorrLocalType"):
                    self.cikepeercorrlocaltype = value
                    self.cikepeercorrlocaltype.value_namespace = name_space
                    self.cikepeercorrlocaltype.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePeerCorrLocalValue"):
                    self.cikepeercorrlocalvalue = value
                    self.cikepeercorrlocalvalue.value_namespace = name_space
                    self.cikepeercorrlocalvalue.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePeerCorrRemoteType"):
                    self.cikepeercorrremotetype = value
                    self.cikepeercorrremotetype.value_namespace = name_space
                    self.cikepeercorrremotetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePeerCorrRemoteValue"):
                    self.cikepeercorrremotevalue = value
                    self.cikepeercorrremotevalue.value_namespace = name_space
                    self.cikepeercorrremotevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePeerCorrIntIndex"):
                    self.cikepeercorrintindex = value
                    self.cikepeercorrintindex.value_namespace = name_space
                    self.cikepeercorrintindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePeerCorrSeqNum"):
                    self.cikepeercorrseqnum = value
                    self.cikepeercorrseqnum.value_namespace = name_space
                    self.cikepeercorrseqnum.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePeerCorrIpSecTunIndex"):
                    self.cikepeercorripsectunindex = value
                    self.cikepeercorripsectunindex.value_namespace = name_space
                    self.cikepeercorripsectunindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cikepeercorrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cikepeercorrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cikePeerCorrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cikePeerCorrEntry"):
                for c in self.cikepeercorrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecFlowMonitorMib.Cikepeercorrtable.Cikepeercorrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cikepeercorrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cikePeerCorrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cikephase1Gwstatstable(Entity):
        """
        Phase\-1 IKE stats information is included in this table.
        Each entry is related to a specific gateway which is 
        identified by 'cmgwIndex'.
        
        .. attribute:: cikephase1gwstatsentry
        
        	Each entry contains the attributes of an Phase\-1 IKE stats information for the related gateway.  There is only one entry for each gateway. The entry  is created when a gateway up and cannot be deleted
        	**type**\: list of    :py:class:`Cikephase1Gwstatsentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cikephase1Gwstatstable.Cikephase1Gwstatsentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CiscoIpsecFlowMonitorMib.Cikephase1Gwstatstable, self).__init__()

            self.yang_name = "cikePhase1GWStatsTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

            self.cikephase1gwstatsentry = YList(self)

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
                        super(CiscoIpsecFlowMonitorMib.Cikephase1Gwstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Cikephase1Gwstatstable, self).__setattr__(name, value)


        class Cikephase1Gwstatsentry(Entity):
            """
            Each entry contains the attributes of an Phase\-1 IKE stats
            information for the related gateway.
            
            There is only one entry for each gateway. The entry 
            is created when a gateway up and cannot be deleted.
            
            .. attribute:: cmgwindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry>`
            
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
                super(CiscoIpsecFlowMonitorMib.Cikephase1Gwstatstable.Cikephase1Gwstatsentry, self).__init__()

                self.yang_name = "cikePhase1GWStatsEntry"
                self.yang_parent_name = "cikePhase1GWStatsTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cmgwindex",
                                "cikephase1gwactivetunnels",
                                "cikephase1gwauthfails",
                                "cikephase1gwdecryptfails",
                                "cikephase1gwhashvalidfails",
                                "cikephase1gwindroppkts",
                                "cikephase1gwinittunnelfails",
                                "cikephase1gwinittunnels",
                                "cikephase1gwinnotifys",
                                "cikephase1gwinoctets",
                                "cikephase1gwinp2exchginvalids",
                                "cikephase1gwinp2exchgrejects",
                                "cikephase1gwinp2exchgs",
                                "cikephase1gwinp2sadelrequests",
                                "cikephase1gwinpkts",
                                "cikephase1gwnosafails",
                                "cikephase1gwoutdroppkts",
                                "cikephase1gwoutnotifys",
                                "cikephase1gwoutoctets",
                                "cikephase1gwoutp2exchginvalids",
                                "cikephase1gwoutp2exchgrejects",
                                "cikephase1gwoutp2exchgs",
                                "cikephase1gwoutp2sadelrequests",
                                "cikephase1gwoutpkts",
                                "cikephase1gwprevioustunnels",
                                "cikephase1gwresptunnelfails",
                                "cikephase1gwsyscapfails") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecFlowMonitorMib.Cikephase1Gwstatstable.Cikephase1Gwstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecFlowMonitorMib.Cikephase1Gwstatstable.Cikephase1Gwstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cmgwindex.is_set or
                    self.cikephase1gwactivetunnels.is_set or
                    self.cikephase1gwauthfails.is_set or
                    self.cikephase1gwdecryptfails.is_set or
                    self.cikephase1gwhashvalidfails.is_set or
                    self.cikephase1gwindroppkts.is_set or
                    self.cikephase1gwinittunnelfails.is_set or
                    self.cikephase1gwinittunnels.is_set or
                    self.cikephase1gwinnotifys.is_set or
                    self.cikephase1gwinoctets.is_set or
                    self.cikephase1gwinp2exchginvalids.is_set or
                    self.cikephase1gwinp2exchgrejects.is_set or
                    self.cikephase1gwinp2exchgs.is_set or
                    self.cikephase1gwinp2sadelrequests.is_set or
                    self.cikephase1gwinpkts.is_set or
                    self.cikephase1gwnosafails.is_set or
                    self.cikephase1gwoutdroppkts.is_set or
                    self.cikephase1gwoutnotifys.is_set or
                    self.cikephase1gwoutoctets.is_set or
                    self.cikephase1gwoutp2exchginvalids.is_set or
                    self.cikephase1gwoutp2exchgrejects.is_set or
                    self.cikephase1gwoutp2exchgs.is_set or
                    self.cikephase1gwoutp2sadelrequests.is_set or
                    self.cikephase1gwoutpkts.is_set or
                    self.cikephase1gwprevioustunnels.is_set or
                    self.cikephase1gwresptunnelfails.is_set or
                    self.cikephase1gwsyscapfails.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cmgwindex.yfilter != YFilter.not_set or
                    self.cikephase1gwactivetunnels.yfilter != YFilter.not_set or
                    self.cikephase1gwauthfails.yfilter != YFilter.not_set or
                    self.cikephase1gwdecryptfails.yfilter != YFilter.not_set or
                    self.cikephase1gwhashvalidfails.yfilter != YFilter.not_set or
                    self.cikephase1gwindroppkts.yfilter != YFilter.not_set or
                    self.cikephase1gwinittunnelfails.yfilter != YFilter.not_set or
                    self.cikephase1gwinittunnels.yfilter != YFilter.not_set or
                    self.cikephase1gwinnotifys.yfilter != YFilter.not_set or
                    self.cikephase1gwinoctets.yfilter != YFilter.not_set or
                    self.cikephase1gwinp2exchginvalids.yfilter != YFilter.not_set or
                    self.cikephase1gwinp2exchgrejects.yfilter != YFilter.not_set or
                    self.cikephase1gwinp2exchgs.yfilter != YFilter.not_set or
                    self.cikephase1gwinp2sadelrequests.yfilter != YFilter.not_set or
                    self.cikephase1gwinpkts.yfilter != YFilter.not_set or
                    self.cikephase1gwnosafails.yfilter != YFilter.not_set or
                    self.cikephase1gwoutdroppkts.yfilter != YFilter.not_set or
                    self.cikephase1gwoutnotifys.yfilter != YFilter.not_set or
                    self.cikephase1gwoutoctets.yfilter != YFilter.not_set or
                    self.cikephase1gwoutp2exchginvalids.yfilter != YFilter.not_set or
                    self.cikephase1gwoutp2exchgrejects.yfilter != YFilter.not_set or
                    self.cikephase1gwoutp2exchgs.yfilter != YFilter.not_set or
                    self.cikephase1gwoutp2sadelrequests.yfilter != YFilter.not_set or
                    self.cikephase1gwoutpkts.yfilter != YFilter.not_set or
                    self.cikephase1gwprevioustunnels.yfilter != YFilter.not_set or
                    self.cikephase1gwresptunnelfails.yfilter != YFilter.not_set or
                    self.cikephase1gwsyscapfails.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cikePhase1GWStatsEntry" + "[cmgwIndex='" + self.cmgwindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikePhase1GWStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cmgwindex.is_set or self.cmgwindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwindex.get_name_leafdata())
                if (self.cikephase1gwactivetunnels.is_set or self.cikephase1gwactivetunnels.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwactivetunnels.get_name_leafdata())
                if (self.cikephase1gwauthfails.is_set or self.cikephase1gwauthfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwauthfails.get_name_leafdata())
                if (self.cikephase1gwdecryptfails.is_set or self.cikephase1gwdecryptfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwdecryptfails.get_name_leafdata())
                if (self.cikephase1gwhashvalidfails.is_set or self.cikephase1gwhashvalidfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwhashvalidfails.get_name_leafdata())
                if (self.cikephase1gwindroppkts.is_set or self.cikephase1gwindroppkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwindroppkts.get_name_leafdata())
                if (self.cikephase1gwinittunnelfails.is_set or self.cikephase1gwinittunnelfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwinittunnelfails.get_name_leafdata())
                if (self.cikephase1gwinittunnels.is_set or self.cikephase1gwinittunnels.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwinittunnels.get_name_leafdata())
                if (self.cikephase1gwinnotifys.is_set or self.cikephase1gwinnotifys.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwinnotifys.get_name_leafdata())
                if (self.cikephase1gwinoctets.is_set or self.cikephase1gwinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwinoctets.get_name_leafdata())
                if (self.cikephase1gwinp2exchginvalids.is_set or self.cikephase1gwinp2exchginvalids.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwinp2exchginvalids.get_name_leafdata())
                if (self.cikephase1gwinp2exchgrejects.is_set or self.cikephase1gwinp2exchgrejects.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwinp2exchgrejects.get_name_leafdata())
                if (self.cikephase1gwinp2exchgs.is_set or self.cikephase1gwinp2exchgs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwinp2exchgs.get_name_leafdata())
                if (self.cikephase1gwinp2sadelrequests.is_set or self.cikephase1gwinp2sadelrequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwinp2sadelrequests.get_name_leafdata())
                if (self.cikephase1gwinpkts.is_set or self.cikephase1gwinpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwinpkts.get_name_leafdata())
                if (self.cikephase1gwnosafails.is_set or self.cikephase1gwnosafails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwnosafails.get_name_leafdata())
                if (self.cikephase1gwoutdroppkts.is_set or self.cikephase1gwoutdroppkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwoutdroppkts.get_name_leafdata())
                if (self.cikephase1gwoutnotifys.is_set or self.cikephase1gwoutnotifys.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwoutnotifys.get_name_leafdata())
                if (self.cikephase1gwoutoctets.is_set or self.cikephase1gwoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwoutoctets.get_name_leafdata())
                if (self.cikephase1gwoutp2exchginvalids.is_set or self.cikephase1gwoutp2exchginvalids.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwoutp2exchginvalids.get_name_leafdata())
                if (self.cikephase1gwoutp2exchgrejects.is_set or self.cikephase1gwoutp2exchgrejects.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwoutp2exchgrejects.get_name_leafdata())
                if (self.cikephase1gwoutp2exchgs.is_set or self.cikephase1gwoutp2exchgs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwoutp2exchgs.get_name_leafdata())
                if (self.cikephase1gwoutp2sadelrequests.is_set or self.cikephase1gwoutp2sadelrequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwoutp2sadelrequests.get_name_leafdata())
                if (self.cikephase1gwoutpkts.is_set or self.cikephase1gwoutpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwoutpkts.get_name_leafdata())
                if (self.cikephase1gwprevioustunnels.is_set or self.cikephase1gwprevioustunnels.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwprevioustunnels.get_name_leafdata())
                if (self.cikephase1gwresptunnelfails.is_set or self.cikephase1gwresptunnelfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwresptunnelfails.get_name_leafdata())
                if (self.cikephase1gwsyscapfails.is_set or self.cikephase1gwsyscapfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikephase1gwsyscapfails.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cmgwIndex" or name == "cikePhase1GWActiveTunnels" or name == "cikePhase1GWAuthFails" or name == "cikePhase1GWDecryptFails" or name == "cikePhase1GWHashValidFails" or name == "cikePhase1GWInDropPkts" or name == "cikePhase1GWInitTunnelFails" or name == "cikePhase1GWInitTunnels" or name == "cikePhase1GWInNotifys" or name == "cikePhase1GWInOctets" or name == "cikePhase1GWInP2ExchgInvalids" or name == "cikePhase1GWInP2ExchgRejects" or name == "cikePhase1GWInP2Exchgs" or name == "cikePhase1GWInP2SaDelRequests" or name == "cikePhase1GWInPkts" or name == "cikePhase1GWNoSaFails" or name == "cikePhase1GWOutDropPkts" or name == "cikePhase1GWOutNotifys" or name == "cikePhase1GWOutOctets" or name == "cikePhase1GWOutP2ExchgInvalids" or name == "cikePhase1GWOutP2ExchgRejects" or name == "cikePhase1GWOutP2Exchgs" or name == "cikePhase1GWOutP2SaDelRequests" or name == "cikePhase1GWOutPkts" or name == "cikePhase1GWPreviousTunnels" or name == "cikePhase1GWRespTunnelFails" or name == "cikePhase1GWSysCapFails"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cmgwIndex"):
                    self.cmgwindex = value
                    self.cmgwindex.value_namespace = name_space
                    self.cmgwindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWActiveTunnels"):
                    self.cikephase1gwactivetunnels = value
                    self.cikephase1gwactivetunnels.value_namespace = name_space
                    self.cikephase1gwactivetunnels.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWAuthFails"):
                    self.cikephase1gwauthfails = value
                    self.cikephase1gwauthfails.value_namespace = name_space
                    self.cikephase1gwauthfails.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWDecryptFails"):
                    self.cikephase1gwdecryptfails = value
                    self.cikephase1gwdecryptfails.value_namespace = name_space
                    self.cikephase1gwdecryptfails.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWHashValidFails"):
                    self.cikephase1gwhashvalidfails = value
                    self.cikephase1gwhashvalidfails.value_namespace = name_space
                    self.cikephase1gwhashvalidfails.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWInDropPkts"):
                    self.cikephase1gwindroppkts = value
                    self.cikephase1gwindroppkts.value_namespace = name_space
                    self.cikephase1gwindroppkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWInitTunnelFails"):
                    self.cikephase1gwinittunnelfails = value
                    self.cikephase1gwinittunnelfails.value_namespace = name_space
                    self.cikephase1gwinittunnelfails.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWInitTunnels"):
                    self.cikephase1gwinittunnels = value
                    self.cikephase1gwinittunnels.value_namespace = name_space
                    self.cikephase1gwinittunnels.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWInNotifys"):
                    self.cikephase1gwinnotifys = value
                    self.cikephase1gwinnotifys.value_namespace = name_space
                    self.cikephase1gwinnotifys.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWInOctets"):
                    self.cikephase1gwinoctets = value
                    self.cikephase1gwinoctets.value_namespace = name_space
                    self.cikephase1gwinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWInP2ExchgInvalids"):
                    self.cikephase1gwinp2exchginvalids = value
                    self.cikephase1gwinp2exchginvalids.value_namespace = name_space
                    self.cikephase1gwinp2exchginvalids.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWInP2ExchgRejects"):
                    self.cikephase1gwinp2exchgrejects = value
                    self.cikephase1gwinp2exchgrejects.value_namespace = name_space
                    self.cikephase1gwinp2exchgrejects.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWInP2Exchgs"):
                    self.cikephase1gwinp2exchgs = value
                    self.cikephase1gwinp2exchgs.value_namespace = name_space
                    self.cikephase1gwinp2exchgs.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWInP2SaDelRequests"):
                    self.cikephase1gwinp2sadelrequests = value
                    self.cikephase1gwinp2sadelrequests.value_namespace = name_space
                    self.cikephase1gwinp2sadelrequests.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWInPkts"):
                    self.cikephase1gwinpkts = value
                    self.cikephase1gwinpkts.value_namespace = name_space
                    self.cikephase1gwinpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWNoSaFails"):
                    self.cikephase1gwnosafails = value
                    self.cikephase1gwnosafails.value_namespace = name_space
                    self.cikephase1gwnosafails.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWOutDropPkts"):
                    self.cikephase1gwoutdroppkts = value
                    self.cikephase1gwoutdroppkts.value_namespace = name_space
                    self.cikephase1gwoutdroppkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWOutNotifys"):
                    self.cikephase1gwoutnotifys = value
                    self.cikephase1gwoutnotifys.value_namespace = name_space
                    self.cikephase1gwoutnotifys.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWOutOctets"):
                    self.cikephase1gwoutoctets = value
                    self.cikephase1gwoutoctets.value_namespace = name_space
                    self.cikephase1gwoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWOutP2ExchgInvalids"):
                    self.cikephase1gwoutp2exchginvalids = value
                    self.cikephase1gwoutp2exchginvalids.value_namespace = name_space
                    self.cikephase1gwoutp2exchginvalids.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWOutP2ExchgRejects"):
                    self.cikephase1gwoutp2exchgrejects = value
                    self.cikephase1gwoutp2exchgrejects.value_namespace = name_space
                    self.cikephase1gwoutp2exchgrejects.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWOutP2Exchgs"):
                    self.cikephase1gwoutp2exchgs = value
                    self.cikephase1gwoutp2exchgs.value_namespace = name_space
                    self.cikephase1gwoutp2exchgs.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWOutP2SaDelRequests"):
                    self.cikephase1gwoutp2sadelrequests = value
                    self.cikephase1gwoutp2sadelrequests.value_namespace = name_space
                    self.cikephase1gwoutp2sadelrequests.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWOutPkts"):
                    self.cikephase1gwoutpkts = value
                    self.cikephase1gwoutpkts.value_namespace = name_space
                    self.cikephase1gwoutpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWPreviousTunnels"):
                    self.cikephase1gwprevioustunnels = value
                    self.cikephase1gwprevioustunnels.value_namespace = name_space
                    self.cikephase1gwprevioustunnels.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWRespTunnelFails"):
                    self.cikephase1gwresptunnelfails = value
                    self.cikephase1gwresptunnelfails.value_namespace = name_space
                    self.cikephase1gwresptunnelfails.value_namespace_prefix = name_space_prefix
                if(value_path == "cikePhase1GWSysCapFails"):
                    self.cikephase1gwsyscapfails = value
                    self.cikephase1gwsyscapfails.value_namespace = name_space
                    self.cikephase1gwsyscapfails.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cikephase1gwstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cikephase1gwstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cikePhase1GWStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cikePhase1GWStatsEntry"):
                for c in self.cikephase1gwstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecFlowMonitorMib.Cikephase1Gwstatstable.Cikephase1Gwstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cikephase1gwstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cikePhase1GWStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cipsectunneltable(Entity):
        """
        The IPsec Phase\-2 Tunnel Table.
        There is one entry in this table for 
        each active IPsec Phase\-2 Tunnel.
        
        .. attribute:: cipsectunnelentry
        
        	Each entry contains the attributes associated with an active IPsec Phase\-2 Tunnel
        	**type**\: list of    :py:class:`Cipsectunnelentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsectunneltable.Cipsectunnelentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CiscoIpsecFlowMonitorMib.Cipsectunneltable, self).__init__()

            self.yang_name = "cipSecTunnelTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

            self.cipsectunnelentry = YList(self)

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
                        super(CiscoIpsecFlowMonitorMib.Cipsectunneltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Cipsectunneltable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Encapmode <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Encapmode>`
            
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
            	**type**\:   :py:class:`Authalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Authalgo>`
            
            .. attribute:: cipsectuninsadecompalgo
            
            	The decompression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Compalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Compalgo>`
            
            .. attribute:: cipsectuninsadiffhellmangrp
            
            	The Diffie Hellman Group used by the inbound security association of the  IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Diffhellmangrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Diffhellmangrp>`
            
            .. attribute:: cipsectuninsaencryptalgo
            
            	The encryption algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Encryptalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Encryptalgo>`
            
            .. attribute:: cipsectuninsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP) security  association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Authalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Authalgo>`
            
            .. attribute:: cipsectunkeytype
            
            	The type of key used by the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Keytype <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Keytype>`
            
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
            	**type**\:   :py:class:`Authalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Authalgo>`
            
            .. attribute:: cipsectunoutsacompalgo
            
            	The compression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Compalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Compalgo>`
            
            .. attribute:: cipsectunoutsadiffhellmangrp
            
            	The Diffie Hellman Group used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Diffhellmangrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Diffhellmangrp>`
            
            .. attribute:: cipsectunoutsaencryptalgo
            
            	The encryption algorithm used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Encryptalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Encryptalgo>`
            
            .. attribute:: cipsectunoutsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP)  security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Authalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Authalgo>`
            
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
            	**type**\:   :py:class:`Tunnelstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Tunnelstatus>`
            
            .. attribute:: cipsectuntotalrefreshes
            
            	The total number of security association refreshes performed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: QM Exchanges
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CiscoIpsecFlowMonitorMib.Cipsectunneltable.Cipsectunnelentry, self).__init__()

                self.yang_name = "cipSecTunnelEntry"
                self.yang_parent_name = "cipSecTunnelTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipsectunindex",
                                "cipsectunactivetime",
                                "cipsectuncurrentsainstances",
                                "cipsectunencapmode",
                                "cipsectunexpiredsainstances",
                                "cipsectunhcindecompoctets",
                                "cipsectunhcinoctets",
                                "cipsectunhcoutoctets",
                                "cipsectunhcoutuncompoctets",
                                "cipsectuniketunnelalive",
                                "cipsectuniketunnelindex",
                                "cipsectuninauthfails",
                                "cipsectuninauths",
                                "cipsectunindecompoctets",
                                "cipsectunindecompoctwraps",
                                "cipsectunindecryptfails",
                                "cipsectunindecrypts",
                                "cipsectunindroppkts",
                                "cipsectuninoctets",
                                "cipsectuninoctwraps",
                                "cipsectuninpkts",
                                "cipsectuninreplaydroppkts",
                                "cipsectuninsaahauthalgo",
                                "cipsectuninsadecompalgo",
                                "cipsectuninsadiffhellmangrp",
                                "cipsectuninsaencryptalgo",
                                "cipsectuninsaespauthalgo",
                                "cipsectunkeytype",
                                "cipsectunlifesize",
                                "cipsectunlifetime",
                                "cipsectunlocaladdr",
                                "cipsectunoutauthfails",
                                "cipsectunoutauths",
                                "cipsectunoutdroppkts",
                                "cipsectunoutencryptfails",
                                "cipsectunoutencrypts",
                                "cipsectunoutoctets",
                                "cipsectunoutoctwraps",
                                "cipsectunoutpkts",
                                "cipsectunoutsaahauthalgo",
                                "cipsectunoutsacompalgo",
                                "cipsectunoutsadiffhellmangrp",
                                "cipsectunoutsaencryptalgo",
                                "cipsectunoutsaespauthalgo",
                                "cipsectunoutuncompoctets",
                                "cipsectunoutuncompoctwraps",
                                "cipsectunremoteaddr",
                                "cipsectunsalifesizethreshold",
                                "cipsectunsalifetimethreshold",
                                "cipsectunstatus",
                                "cipsectuntotalrefreshes") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecFlowMonitorMib.Cipsectunneltable.Cipsectunnelentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecFlowMonitorMib.Cipsectunneltable.Cipsectunnelentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cipsectunindex.is_set or
                    self.cipsectunactivetime.is_set or
                    self.cipsectuncurrentsainstances.is_set or
                    self.cipsectunencapmode.is_set or
                    self.cipsectunexpiredsainstances.is_set or
                    self.cipsectunhcindecompoctets.is_set or
                    self.cipsectunhcinoctets.is_set or
                    self.cipsectunhcoutoctets.is_set or
                    self.cipsectunhcoutuncompoctets.is_set or
                    self.cipsectuniketunnelalive.is_set or
                    self.cipsectuniketunnelindex.is_set or
                    self.cipsectuninauthfails.is_set or
                    self.cipsectuninauths.is_set or
                    self.cipsectunindecompoctets.is_set or
                    self.cipsectunindecompoctwraps.is_set or
                    self.cipsectunindecryptfails.is_set or
                    self.cipsectunindecrypts.is_set or
                    self.cipsectunindroppkts.is_set or
                    self.cipsectuninoctets.is_set or
                    self.cipsectuninoctwraps.is_set or
                    self.cipsectuninpkts.is_set or
                    self.cipsectuninreplaydroppkts.is_set or
                    self.cipsectuninsaahauthalgo.is_set or
                    self.cipsectuninsadecompalgo.is_set or
                    self.cipsectuninsadiffhellmangrp.is_set or
                    self.cipsectuninsaencryptalgo.is_set or
                    self.cipsectuninsaespauthalgo.is_set or
                    self.cipsectunkeytype.is_set or
                    self.cipsectunlifesize.is_set or
                    self.cipsectunlifetime.is_set or
                    self.cipsectunlocaladdr.is_set or
                    self.cipsectunoutauthfails.is_set or
                    self.cipsectunoutauths.is_set or
                    self.cipsectunoutdroppkts.is_set or
                    self.cipsectunoutencryptfails.is_set or
                    self.cipsectunoutencrypts.is_set or
                    self.cipsectunoutoctets.is_set or
                    self.cipsectunoutoctwraps.is_set or
                    self.cipsectunoutpkts.is_set or
                    self.cipsectunoutsaahauthalgo.is_set or
                    self.cipsectunoutsacompalgo.is_set or
                    self.cipsectunoutsadiffhellmangrp.is_set or
                    self.cipsectunoutsaencryptalgo.is_set or
                    self.cipsectunoutsaespauthalgo.is_set or
                    self.cipsectunoutuncompoctets.is_set or
                    self.cipsectunoutuncompoctwraps.is_set or
                    self.cipsectunremoteaddr.is_set or
                    self.cipsectunsalifesizethreshold.is_set or
                    self.cipsectunsalifetimethreshold.is_set or
                    self.cipsectunstatus.is_set or
                    self.cipsectuntotalrefreshes.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipsectunindex.yfilter != YFilter.not_set or
                    self.cipsectunactivetime.yfilter != YFilter.not_set or
                    self.cipsectuncurrentsainstances.yfilter != YFilter.not_set or
                    self.cipsectunencapmode.yfilter != YFilter.not_set or
                    self.cipsectunexpiredsainstances.yfilter != YFilter.not_set or
                    self.cipsectunhcindecompoctets.yfilter != YFilter.not_set or
                    self.cipsectunhcinoctets.yfilter != YFilter.not_set or
                    self.cipsectunhcoutoctets.yfilter != YFilter.not_set or
                    self.cipsectunhcoutuncompoctets.yfilter != YFilter.not_set or
                    self.cipsectuniketunnelalive.yfilter != YFilter.not_set or
                    self.cipsectuniketunnelindex.yfilter != YFilter.not_set or
                    self.cipsectuninauthfails.yfilter != YFilter.not_set or
                    self.cipsectuninauths.yfilter != YFilter.not_set or
                    self.cipsectunindecompoctets.yfilter != YFilter.not_set or
                    self.cipsectunindecompoctwraps.yfilter != YFilter.not_set or
                    self.cipsectunindecryptfails.yfilter != YFilter.not_set or
                    self.cipsectunindecrypts.yfilter != YFilter.not_set or
                    self.cipsectunindroppkts.yfilter != YFilter.not_set or
                    self.cipsectuninoctets.yfilter != YFilter.not_set or
                    self.cipsectuninoctwraps.yfilter != YFilter.not_set or
                    self.cipsectuninpkts.yfilter != YFilter.not_set or
                    self.cipsectuninreplaydroppkts.yfilter != YFilter.not_set or
                    self.cipsectuninsaahauthalgo.yfilter != YFilter.not_set or
                    self.cipsectuninsadecompalgo.yfilter != YFilter.not_set or
                    self.cipsectuninsadiffhellmangrp.yfilter != YFilter.not_set or
                    self.cipsectuninsaencryptalgo.yfilter != YFilter.not_set or
                    self.cipsectuninsaespauthalgo.yfilter != YFilter.not_set or
                    self.cipsectunkeytype.yfilter != YFilter.not_set or
                    self.cipsectunlifesize.yfilter != YFilter.not_set or
                    self.cipsectunlifetime.yfilter != YFilter.not_set or
                    self.cipsectunlocaladdr.yfilter != YFilter.not_set or
                    self.cipsectunoutauthfails.yfilter != YFilter.not_set or
                    self.cipsectunoutauths.yfilter != YFilter.not_set or
                    self.cipsectunoutdroppkts.yfilter != YFilter.not_set or
                    self.cipsectunoutencryptfails.yfilter != YFilter.not_set or
                    self.cipsectunoutencrypts.yfilter != YFilter.not_set or
                    self.cipsectunoutoctets.yfilter != YFilter.not_set or
                    self.cipsectunoutoctwraps.yfilter != YFilter.not_set or
                    self.cipsectunoutpkts.yfilter != YFilter.not_set or
                    self.cipsectunoutsaahauthalgo.yfilter != YFilter.not_set or
                    self.cipsectunoutsacompalgo.yfilter != YFilter.not_set or
                    self.cipsectunoutsadiffhellmangrp.yfilter != YFilter.not_set or
                    self.cipsectunoutsaencryptalgo.yfilter != YFilter.not_set or
                    self.cipsectunoutsaespauthalgo.yfilter != YFilter.not_set or
                    self.cipsectunoutuncompoctets.yfilter != YFilter.not_set or
                    self.cipsectunoutuncompoctwraps.yfilter != YFilter.not_set or
                    self.cipsectunremoteaddr.yfilter != YFilter.not_set or
                    self.cipsectunsalifesizethreshold.yfilter != YFilter.not_set or
                    self.cipsectunsalifetimethreshold.yfilter != YFilter.not_set or
                    self.cipsectunstatus.yfilter != YFilter.not_set or
                    self.cipsectuntotalrefreshes.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipSecTunnelEntry" + "[cipSecTunIndex='" + self.cipsectunindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecTunnelTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipsectunindex.is_set or self.cipsectunindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunindex.get_name_leafdata())
                if (self.cipsectunactivetime.is_set or self.cipsectunactivetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunactivetime.get_name_leafdata())
                if (self.cipsectuncurrentsainstances.is_set or self.cipsectuncurrentsainstances.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectuncurrentsainstances.get_name_leafdata())
                if (self.cipsectunencapmode.is_set or self.cipsectunencapmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunencapmode.get_name_leafdata())
                if (self.cipsectunexpiredsainstances.is_set or self.cipsectunexpiredsainstances.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunexpiredsainstances.get_name_leafdata())
                if (self.cipsectunhcindecompoctets.is_set or self.cipsectunhcindecompoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhcindecompoctets.get_name_leafdata())
                if (self.cipsectunhcinoctets.is_set or self.cipsectunhcinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhcinoctets.get_name_leafdata())
                if (self.cipsectunhcoutoctets.is_set or self.cipsectunhcoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhcoutoctets.get_name_leafdata())
                if (self.cipsectunhcoutuncompoctets.is_set or self.cipsectunhcoutuncompoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhcoutuncompoctets.get_name_leafdata())
                if (self.cipsectuniketunnelalive.is_set or self.cipsectuniketunnelalive.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectuniketunnelalive.get_name_leafdata())
                if (self.cipsectuniketunnelindex.is_set or self.cipsectuniketunnelindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectuniketunnelindex.get_name_leafdata())
                if (self.cipsectuninauthfails.is_set or self.cipsectuninauthfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectuninauthfails.get_name_leafdata())
                if (self.cipsectuninauths.is_set or self.cipsectuninauths.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectuninauths.get_name_leafdata())
                if (self.cipsectunindecompoctets.is_set or self.cipsectunindecompoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunindecompoctets.get_name_leafdata())
                if (self.cipsectunindecompoctwraps.is_set or self.cipsectunindecompoctwraps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunindecompoctwraps.get_name_leafdata())
                if (self.cipsectunindecryptfails.is_set or self.cipsectunindecryptfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunindecryptfails.get_name_leafdata())
                if (self.cipsectunindecrypts.is_set or self.cipsectunindecrypts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunindecrypts.get_name_leafdata())
                if (self.cipsectunindroppkts.is_set or self.cipsectunindroppkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunindroppkts.get_name_leafdata())
                if (self.cipsectuninoctets.is_set or self.cipsectuninoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectuninoctets.get_name_leafdata())
                if (self.cipsectuninoctwraps.is_set or self.cipsectuninoctwraps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectuninoctwraps.get_name_leafdata())
                if (self.cipsectuninpkts.is_set or self.cipsectuninpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectuninpkts.get_name_leafdata())
                if (self.cipsectuninreplaydroppkts.is_set or self.cipsectuninreplaydroppkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectuninreplaydroppkts.get_name_leafdata())
                if (self.cipsectuninsaahauthalgo.is_set or self.cipsectuninsaahauthalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectuninsaahauthalgo.get_name_leafdata())
                if (self.cipsectuninsadecompalgo.is_set or self.cipsectuninsadecompalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectuninsadecompalgo.get_name_leafdata())
                if (self.cipsectuninsadiffhellmangrp.is_set or self.cipsectuninsadiffhellmangrp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectuninsadiffhellmangrp.get_name_leafdata())
                if (self.cipsectuninsaencryptalgo.is_set or self.cipsectuninsaencryptalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectuninsaencryptalgo.get_name_leafdata())
                if (self.cipsectuninsaespauthalgo.is_set or self.cipsectuninsaespauthalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectuninsaespauthalgo.get_name_leafdata())
                if (self.cipsectunkeytype.is_set or self.cipsectunkeytype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunkeytype.get_name_leafdata())
                if (self.cipsectunlifesize.is_set or self.cipsectunlifesize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunlifesize.get_name_leafdata())
                if (self.cipsectunlifetime.is_set or self.cipsectunlifetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunlifetime.get_name_leafdata())
                if (self.cipsectunlocaladdr.is_set or self.cipsectunlocaladdr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunlocaladdr.get_name_leafdata())
                if (self.cipsectunoutauthfails.is_set or self.cipsectunoutauthfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunoutauthfails.get_name_leafdata())
                if (self.cipsectunoutauths.is_set or self.cipsectunoutauths.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunoutauths.get_name_leafdata())
                if (self.cipsectunoutdroppkts.is_set or self.cipsectunoutdroppkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunoutdroppkts.get_name_leafdata())
                if (self.cipsectunoutencryptfails.is_set or self.cipsectunoutencryptfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunoutencryptfails.get_name_leafdata())
                if (self.cipsectunoutencrypts.is_set or self.cipsectunoutencrypts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunoutencrypts.get_name_leafdata())
                if (self.cipsectunoutoctets.is_set or self.cipsectunoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunoutoctets.get_name_leafdata())
                if (self.cipsectunoutoctwraps.is_set or self.cipsectunoutoctwraps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunoutoctwraps.get_name_leafdata())
                if (self.cipsectunoutpkts.is_set or self.cipsectunoutpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunoutpkts.get_name_leafdata())
                if (self.cipsectunoutsaahauthalgo.is_set or self.cipsectunoutsaahauthalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunoutsaahauthalgo.get_name_leafdata())
                if (self.cipsectunoutsacompalgo.is_set or self.cipsectunoutsacompalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunoutsacompalgo.get_name_leafdata())
                if (self.cipsectunoutsadiffhellmangrp.is_set or self.cipsectunoutsadiffhellmangrp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunoutsadiffhellmangrp.get_name_leafdata())
                if (self.cipsectunoutsaencryptalgo.is_set or self.cipsectunoutsaencryptalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunoutsaencryptalgo.get_name_leafdata())
                if (self.cipsectunoutsaespauthalgo.is_set or self.cipsectunoutsaespauthalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunoutsaespauthalgo.get_name_leafdata())
                if (self.cipsectunoutuncompoctets.is_set or self.cipsectunoutuncompoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunoutuncompoctets.get_name_leafdata())
                if (self.cipsectunoutuncompoctwraps.is_set or self.cipsectunoutuncompoctwraps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunoutuncompoctwraps.get_name_leafdata())
                if (self.cipsectunremoteaddr.is_set or self.cipsectunremoteaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunremoteaddr.get_name_leafdata())
                if (self.cipsectunsalifesizethreshold.is_set or self.cipsectunsalifesizethreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunsalifesizethreshold.get_name_leafdata())
                if (self.cipsectunsalifetimethreshold.is_set or self.cipsectunsalifetimethreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunsalifetimethreshold.get_name_leafdata())
                if (self.cipsectunstatus.is_set or self.cipsectunstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunstatus.get_name_leafdata())
                if (self.cipsectuntotalrefreshes.is_set or self.cipsectuntotalrefreshes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectuntotalrefreshes.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipSecTunIndex" or name == "cipSecTunActiveTime" or name == "cipSecTunCurrentSaInstances" or name == "cipSecTunEncapMode" or name == "cipSecTunExpiredSaInstances" or name == "cipSecTunHcInDecompOctets" or name == "cipSecTunHcInOctets" or name == "cipSecTunHcOutOctets" or name == "cipSecTunHcOutUncompOctets" or name == "cipSecTunIkeTunnelAlive" or name == "cipSecTunIkeTunnelIndex" or name == "cipSecTunInAuthFails" or name == "cipSecTunInAuths" or name == "cipSecTunInDecompOctets" or name == "cipSecTunInDecompOctWraps" or name == "cipSecTunInDecryptFails" or name == "cipSecTunInDecrypts" or name == "cipSecTunInDropPkts" or name == "cipSecTunInOctets" or name == "cipSecTunInOctWraps" or name == "cipSecTunInPkts" or name == "cipSecTunInReplayDropPkts" or name == "cipSecTunInSaAhAuthAlgo" or name == "cipSecTunInSaDecompAlgo" or name == "cipSecTunInSaDiffHellmanGrp" or name == "cipSecTunInSaEncryptAlgo" or name == "cipSecTunInSaEspAuthAlgo" or name == "cipSecTunKeyType" or name == "cipSecTunLifeSize" or name == "cipSecTunLifeTime" or name == "cipSecTunLocalAddr" or name == "cipSecTunOutAuthFails" or name == "cipSecTunOutAuths" or name == "cipSecTunOutDropPkts" or name == "cipSecTunOutEncryptFails" or name == "cipSecTunOutEncrypts" or name == "cipSecTunOutOctets" or name == "cipSecTunOutOctWraps" or name == "cipSecTunOutPkts" or name == "cipSecTunOutSaAhAuthAlgo" or name == "cipSecTunOutSaCompAlgo" or name == "cipSecTunOutSaDiffHellmanGrp" or name == "cipSecTunOutSaEncryptAlgo" or name == "cipSecTunOutSaEspAuthAlgo" or name == "cipSecTunOutUncompOctets" or name == "cipSecTunOutUncompOctWraps" or name == "cipSecTunRemoteAddr" or name == "cipSecTunSaLifeSizeThreshold" or name == "cipSecTunSaLifeTimeThreshold" or name == "cipSecTunStatus" or name == "cipSecTunTotalRefreshes"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipSecTunIndex"):
                    self.cipsectunindex = value
                    self.cipsectunindex.value_namespace = name_space
                    self.cipsectunindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunActiveTime"):
                    self.cipsectunactivetime = value
                    self.cipsectunactivetime.value_namespace = name_space
                    self.cipsectunactivetime.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunCurrentSaInstances"):
                    self.cipsectuncurrentsainstances = value
                    self.cipsectuncurrentsainstances.value_namespace = name_space
                    self.cipsectuncurrentsainstances.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunEncapMode"):
                    self.cipsectunencapmode = value
                    self.cipsectunencapmode.value_namespace = name_space
                    self.cipsectunencapmode.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunExpiredSaInstances"):
                    self.cipsectunexpiredsainstances = value
                    self.cipsectunexpiredsainstances.value_namespace = name_space
                    self.cipsectunexpiredsainstances.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHcInDecompOctets"):
                    self.cipsectunhcindecompoctets = value
                    self.cipsectunhcindecompoctets.value_namespace = name_space
                    self.cipsectunhcindecompoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHcInOctets"):
                    self.cipsectunhcinoctets = value
                    self.cipsectunhcinoctets.value_namespace = name_space
                    self.cipsectunhcinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHcOutOctets"):
                    self.cipsectunhcoutoctets = value
                    self.cipsectunhcoutoctets.value_namespace = name_space
                    self.cipsectunhcoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHcOutUncompOctets"):
                    self.cipsectunhcoutuncompoctets = value
                    self.cipsectunhcoutuncompoctets.value_namespace = name_space
                    self.cipsectunhcoutuncompoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunIkeTunnelAlive"):
                    self.cipsectuniketunnelalive = value
                    self.cipsectuniketunnelalive.value_namespace = name_space
                    self.cipsectuniketunnelalive.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunIkeTunnelIndex"):
                    self.cipsectuniketunnelindex = value
                    self.cipsectuniketunnelindex.value_namespace = name_space
                    self.cipsectuniketunnelindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunInAuthFails"):
                    self.cipsectuninauthfails = value
                    self.cipsectuninauthfails.value_namespace = name_space
                    self.cipsectuninauthfails.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunInAuths"):
                    self.cipsectuninauths = value
                    self.cipsectuninauths.value_namespace = name_space
                    self.cipsectuninauths.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunInDecompOctets"):
                    self.cipsectunindecompoctets = value
                    self.cipsectunindecompoctets.value_namespace = name_space
                    self.cipsectunindecompoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunInDecompOctWraps"):
                    self.cipsectunindecompoctwraps = value
                    self.cipsectunindecompoctwraps.value_namespace = name_space
                    self.cipsectunindecompoctwraps.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunInDecryptFails"):
                    self.cipsectunindecryptfails = value
                    self.cipsectunindecryptfails.value_namespace = name_space
                    self.cipsectunindecryptfails.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunInDecrypts"):
                    self.cipsectunindecrypts = value
                    self.cipsectunindecrypts.value_namespace = name_space
                    self.cipsectunindecrypts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunInDropPkts"):
                    self.cipsectunindroppkts = value
                    self.cipsectunindroppkts.value_namespace = name_space
                    self.cipsectunindroppkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunInOctets"):
                    self.cipsectuninoctets = value
                    self.cipsectuninoctets.value_namespace = name_space
                    self.cipsectuninoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunInOctWraps"):
                    self.cipsectuninoctwraps = value
                    self.cipsectuninoctwraps.value_namespace = name_space
                    self.cipsectuninoctwraps.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunInPkts"):
                    self.cipsectuninpkts = value
                    self.cipsectuninpkts.value_namespace = name_space
                    self.cipsectuninpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunInReplayDropPkts"):
                    self.cipsectuninreplaydroppkts = value
                    self.cipsectuninreplaydroppkts.value_namespace = name_space
                    self.cipsectuninreplaydroppkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunInSaAhAuthAlgo"):
                    self.cipsectuninsaahauthalgo = value
                    self.cipsectuninsaahauthalgo.value_namespace = name_space
                    self.cipsectuninsaahauthalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunInSaDecompAlgo"):
                    self.cipsectuninsadecompalgo = value
                    self.cipsectuninsadecompalgo.value_namespace = name_space
                    self.cipsectuninsadecompalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunInSaDiffHellmanGrp"):
                    self.cipsectuninsadiffhellmangrp = value
                    self.cipsectuninsadiffhellmangrp.value_namespace = name_space
                    self.cipsectuninsadiffhellmangrp.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunInSaEncryptAlgo"):
                    self.cipsectuninsaencryptalgo = value
                    self.cipsectuninsaencryptalgo.value_namespace = name_space
                    self.cipsectuninsaencryptalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunInSaEspAuthAlgo"):
                    self.cipsectuninsaespauthalgo = value
                    self.cipsectuninsaespauthalgo.value_namespace = name_space
                    self.cipsectuninsaespauthalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunKeyType"):
                    self.cipsectunkeytype = value
                    self.cipsectunkeytype.value_namespace = name_space
                    self.cipsectunkeytype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunLifeSize"):
                    self.cipsectunlifesize = value
                    self.cipsectunlifesize.value_namespace = name_space
                    self.cipsectunlifesize.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunLifeTime"):
                    self.cipsectunlifetime = value
                    self.cipsectunlifetime.value_namespace = name_space
                    self.cipsectunlifetime.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunLocalAddr"):
                    self.cipsectunlocaladdr = value
                    self.cipsectunlocaladdr.value_namespace = name_space
                    self.cipsectunlocaladdr.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunOutAuthFails"):
                    self.cipsectunoutauthfails = value
                    self.cipsectunoutauthfails.value_namespace = name_space
                    self.cipsectunoutauthfails.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunOutAuths"):
                    self.cipsectunoutauths = value
                    self.cipsectunoutauths.value_namespace = name_space
                    self.cipsectunoutauths.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunOutDropPkts"):
                    self.cipsectunoutdroppkts = value
                    self.cipsectunoutdroppkts.value_namespace = name_space
                    self.cipsectunoutdroppkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunOutEncryptFails"):
                    self.cipsectunoutencryptfails = value
                    self.cipsectunoutencryptfails.value_namespace = name_space
                    self.cipsectunoutencryptfails.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunOutEncrypts"):
                    self.cipsectunoutencrypts = value
                    self.cipsectunoutencrypts.value_namespace = name_space
                    self.cipsectunoutencrypts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunOutOctets"):
                    self.cipsectunoutoctets = value
                    self.cipsectunoutoctets.value_namespace = name_space
                    self.cipsectunoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunOutOctWraps"):
                    self.cipsectunoutoctwraps = value
                    self.cipsectunoutoctwraps.value_namespace = name_space
                    self.cipsectunoutoctwraps.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunOutPkts"):
                    self.cipsectunoutpkts = value
                    self.cipsectunoutpkts.value_namespace = name_space
                    self.cipsectunoutpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunOutSaAhAuthAlgo"):
                    self.cipsectunoutsaahauthalgo = value
                    self.cipsectunoutsaahauthalgo.value_namespace = name_space
                    self.cipsectunoutsaahauthalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunOutSaCompAlgo"):
                    self.cipsectunoutsacompalgo = value
                    self.cipsectunoutsacompalgo.value_namespace = name_space
                    self.cipsectunoutsacompalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunOutSaDiffHellmanGrp"):
                    self.cipsectunoutsadiffhellmangrp = value
                    self.cipsectunoutsadiffhellmangrp.value_namespace = name_space
                    self.cipsectunoutsadiffhellmangrp.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunOutSaEncryptAlgo"):
                    self.cipsectunoutsaencryptalgo = value
                    self.cipsectunoutsaencryptalgo.value_namespace = name_space
                    self.cipsectunoutsaencryptalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunOutSaEspAuthAlgo"):
                    self.cipsectunoutsaespauthalgo = value
                    self.cipsectunoutsaespauthalgo.value_namespace = name_space
                    self.cipsectunoutsaespauthalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunOutUncompOctets"):
                    self.cipsectunoutuncompoctets = value
                    self.cipsectunoutuncompoctets.value_namespace = name_space
                    self.cipsectunoutuncompoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunOutUncompOctWraps"):
                    self.cipsectunoutuncompoctwraps = value
                    self.cipsectunoutuncompoctwraps.value_namespace = name_space
                    self.cipsectunoutuncompoctwraps.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunRemoteAddr"):
                    self.cipsectunremoteaddr = value
                    self.cipsectunremoteaddr.value_namespace = name_space
                    self.cipsectunremoteaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunSaLifeSizeThreshold"):
                    self.cipsectunsalifesizethreshold = value
                    self.cipsectunsalifesizethreshold.value_namespace = name_space
                    self.cipsectunsalifesizethreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunSaLifeTimeThreshold"):
                    self.cipsectunsalifetimethreshold = value
                    self.cipsectunsalifetimethreshold.value_namespace = name_space
                    self.cipsectunsalifetimethreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunStatus"):
                    self.cipsectunstatus = value
                    self.cipsectunstatus.value_namespace = name_space
                    self.cipsectunstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunTotalRefreshes"):
                    self.cipsectuntotalrefreshes = value
                    self.cipsectuntotalrefreshes.value_namespace = name_space
                    self.cipsectuntotalrefreshes.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipsectunnelentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipsectunnelentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipSecTunnelTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipSecTunnelEntry"):
                for c in self.cipsectunnelentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecFlowMonitorMib.Cipsectunneltable.Cipsectunnelentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipsectunnelentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipSecTunnelEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cipsecendpttable(Entity):
        """
        The IPsec Phase\-2 Tunnel Endpoint Table.
        This table contains an entry for each 
        active endpoint associated with an IPsec
         Phase\-2 Tunnel.
        
        .. attribute:: cipsecendptentry
        
        	An IPsec Phase\-2 Tunnel Endpoint entry
        	**type**\: list of    :py:class:`Cipsecendptentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecendpttable.Cipsecendptentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CiscoIpsecFlowMonitorMib.Cipsecendpttable, self).__init__()

            self.yang_name = "cipSecEndPtTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

            self.cipsecendptentry = YList(self)

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
                        super(CiscoIpsecFlowMonitorMib.Cipsecendpttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Cipsecendpttable, self).__setattr__(name, value)


        class Cipsecendptentry(Entity):
            """
            An IPsec Phase\-2 Tunnel Endpoint entry.
            
            .. attribute:: cipsectunindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cipsectunindex <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsectunneltable.Cipsectunnelentry>`
            
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
            	**type**\:   :py:class:`Endpttype <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Endpttype>`
            
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
            	**type**\:   :py:class:`Endpttype <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Endpttype>`
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CiscoIpsecFlowMonitorMib.Cipsecendpttable.Cipsecendptentry, self).__init__()

                self.yang_name = "cipSecEndPtEntry"
                self.yang_parent_name = "cipSecEndPtTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipsectunindex",
                                "cipsecendptindex",
                                "cipsecendptlocaladdr1",
                                "cipsecendptlocaladdr2",
                                "cipsecendptlocalname",
                                "cipsecendptlocalport",
                                "cipsecendptlocalprotocol",
                                "cipsecendptlocaltype",
                                "cipsecendptremoteaddr1",
                                "cipsecendptremoteaddr2",
                                "cipsecendptremotename",
                                "cipsecendptremoteport",
                                "cipsecendptremoteprotocol",
                                "cipsecendptremotetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecFlowMonitorMib.Cipsecendpttable.Cipsecendptentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecFlowMonitorMib.Cipsecendpttable.Cipsecendptentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cipsectunindex.is_set or
                    self.cipsecendptindex.is_set or
                    self.cipsecendptlocaladdr1.is_set or
                    self.cipsecendptlocaladdr2.is_set or
                    self.cipsecendptlocalname.is_set or
                    self.cipsecendptlocalport.is_set or
                    self.cipsecendptlocalprotocol.is_set or
                    self.cipsecendptlocaltype.is_set or
                    self.cipsecendptremoteaddr1.is_set or
                    self.cipsecendptremoteaddr2.is_set or
                    self.cipsecendptremotename.is_set or
                    self.cipsecendptremoteport.is_set or
                    self.cipsecendptremoteprotocol.is_set or
                    self.cipsecendptremotetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipsectunindex.yfilter != YFilter.not_set or
                    self.cipsecendptindex.yfilter != YFilter.not_set or
                    self.cipsecendptlocaladdr1.yfilter != YFilter.not_set or
                    self.cipsecendptlocaladdr2.yfilter != YFilter.not_set or
                    self.cipsecendptlocalname.yfilter != YFilter.not_set or
                    self.cipsecendptlocalport.yfilter != YFilter.not_set or
                    self.cipsecendptlocalprotocol.yfilter != YFilter.not_set or
                    self.cipsecendptlocaltype.yfilter != YFilter.not_set or
                    self.cipsecendptremoteaddr1.yfilter != YFilter.not_set or
                    self.cipsecendptremoteaddr2.yfilter != YFilter.not_set or
                    self.cipsecendptremotename.yfilter != YFilter.not_set or
                    self.cipsecendptremoteport.yfilter != YFilter.not_set or
                    self.cipsecendptremoteprotocol.yfilter != YFilter.not_set or
                    self.cipsecendptremotetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipSecEndPtEntry" + "[cipSecTunIndex='" + self.cipsectunindex.get() + "']" + "[cipSecEndPtIndex='" + self.cipsecendptindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecEndPtTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipsectunindex.is_set or self.cipsectunindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunindex.get_name_leafdata())
                if (self.cipsecendptindex.is_set or self.cipsecendptindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendptindex.get_name_leafdata())
                if (self.cipsecendptlocaladdr1.is_set or self.cipsecendptlocaladdr1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendptlocaladdr1.get_name_leafdata())
                if (self.cipsecendptlocaladdr2.is_set or self.cipsecendptlocaladdr2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendptlocaladdr2.get_name_leafdata())
                if (self.cipsecendptlocalname.is_set or self.cipsecendptlocalname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendptlocalname.get_name_leafdata())
                if (self.cipsecendptlocalport.is_set or self.cipsecendptlocalport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendptlocalport.get_name_leafdata())
                if (self.cipsecendptlocalprotocol.is_set or self.cipsecendptlocalprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendptlocalprotocol.get_name_leafdata())
                if (self.cipsecendptlocaltype.is_set or self.cipsecendptlocaltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendptlocaltype.get_name_leafdata())
                if (self.cipsecendptremoteaddr1.is_set or self.cipsecendptremoteaddr1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendptremoteaddr1.get_name_leafdata())
                if (self.cipsecendptremoteaddr2.is_set or self.cipsecendptremoteaddr2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendptremoteaddr2.get_name_leafdata())
                if (self.cipsecendptremotename.is_set or self.cipsecendptremotename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendptremotename.get_name_leafdata())
                if (self.cipsecendptremoteport.is_set or self.cipsecendptremoteport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendptremoteport.get_name_leafdata())
                if (self.cipsecendptremoteprotocol.is_set or self.cipsecendptremoteprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendptremoteprotocol.get_name_leafdata())
                if (self.cipsecendptremotetype.is_set or self.cipsecendptremotetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendptremotetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipSecTunIndex" or name == "cipSecEndPtIndex" or name == "cipSecEndPtLocalAddr1" or name == "cipSecEndPtLocalAddr2" or name == "cipSecEndPtLocalName" or name == "cipSecEndPtLocalPort" or name == "cipSecEndPtLocalProtocol" or name == "cipSecEndPtLocalType" or name == "cipSecEndPtRemoteAddr1" or name == "cipSecEndPtRemoteAddr2" or name == "cipSecEndPtRemoteName" or name == "cipSecEndPtRemotePort" or name == "cipSecEndPtRemoteProtocol" or name == "cipSecEndPtRemoteType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipSecTunIndex"):
                    self.cipsectunindex = value
                    self.cipsectunindex.value_namespace = name_space
                    self.cipsectunindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtIndex"):
                    self.cipsecendptindex = value
                    self.cipsecendptindex.value_namespace = name_space
                    self.cipsecendptindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtLocalAddr1"):
                    self.cipsecendptlocaladdr1 = value
                    self.cipsecendptlocaladdr1.value_namespace = name_space
                    self.cipsecendptlocaladdr1.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtLocalAddr2"):
                    self.cipsecendptlocaladdr2 = value
                    self.cipsecendptlocaladdr2.value_namespace = name_space
                    self.cipsecendptlocaladdr2.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtLocalName"):
                    self.cipsecendptlocalname = value
                    self.cipsecendptlocalname.value_namespace = name_space
                    self.cipsecendptlocalname.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtLocalPort"):
                    self.cipsecendptlocalport = value
                    self.cipsecendptlocalport.value_namespace = name_space
                    self.cipsecendptlocalport.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtLocalProtocol"):
                    self.cipsecendptlocalprotocol = value
                    self.cipsecendptlocalprotocol.value_namespace = name_space
                    self.cipsecendptlocalprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtLocalType"):
                    self.cipsecendptlocaltype = value
                    self.cipsecendptlocaltype.value_namespace = name_space
                    self.cipsecendptlocaltype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtRemoteAddr1"):
                    self.cipsecendptremoteaddr1 = value
                    self.cipsecendptremoteaddr1.value_namespace = name_space
                    self.cipsecendptremoteaddr1.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtRemoteAddr2"):
                    self.cipsecendptremoteaddr2 = value
                    self.cipsecendptremoteaddr2.value_namespace = name_space
                    self.cipsecendptremoteaddr2.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtRemoteName"):
                    self.cipsecendptremotename = value
                    self.cipsecendptremotename.value_namespace = name_space
                    self.cipsecendptremotename.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtRemotePort"):
                    self.cipsecendptremoteport = value
                    self.cipsecendptremoteport.value_namespace = name_space
                    self.cipsecendptremoteport.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtRemoteProtocol"):
                    self.cipsecendptremoteprotocol = value
                    self.cipsecendptremoteprotocol.value_namespace = name_space
                    self.cipsecendptremoteprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtRemoteType"):
                    self.cipsecendptremotetype = value
                    self.cipsecendptremotetype.value_namespace = name_space
                    self.cipsecendptremotetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipsecendptentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipsecendptentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipSecEndPtTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipSecEndPtEntry"):
                for c in self.cipsecendptentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecFlowMonitorMib.Cipsecendpttable.Cipsecendptentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipsecendptentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipSecEndPtEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cipsecspitable(Entity):
        """
        The IPsec Phase\-2 Security Protection Index Table.
        This table contains an entry for each active 
        and expiring security
         association.
        
        .. attribute:: cipsecspientry
        
        	Each entry contains the attributes associated with active and expiring IPsec Phase\-2  security associations
        	**type**\: list of    :py:class:`Cipsecspientry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecspitable.Cipsecspientry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CiscoIpsecFlowMonitorMib.Cipsecspitable, self).__init__()

            self.yang_name = "cipSecSpiTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

            self.cipsecspientry = YList(self)

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
                        super(CiscoIpsecFlowMonitorMib.Cipsecspitable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Cipsecspitable, self).__setattr__(name, value)


        class Cipsecspientry(Entity):
            """
            Each entry contains the attributes associated with
            active and expiring IPsec Phase\-2 
            security associations.
            
            .. attribute:: cipsectunindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cipsectunindex <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsectunneltable.Cipsectunnelentry>`
            
            .. attribute:: cipsecspiindex  <key>
            
            	The number of the SPI associated with the Phase\-2 Tunnel Table.  The value of this  index is a number which begins at one and is  incremented with each SPI associated with an  IPsec Phase\-2 Tunnel.  The value of this  object will wrap at 2,147,483,647
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipsecspidirection
            
            	The direction of the SPI
            	**type**\:   :py:class:`Cipsecspidirection <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecspitable.Cipsecspientry.Cipsecspidirection>`
            
            .. attribute:: cipsecspiprotocol
            
            	The protocol of the SPI
            	**type**\:   :py:class:`Cipsecspiprotocol <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecspitable.Cipsecspientry.Cipsecspiprotocol>`
            
            .. attribute:: cipsecspistatus
            
            	The status of the SPI
            	**type**\:   :py:class:`Cipsecspistatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecspitable.Cipsecspientry.Cipsecspistatus>`
            
            .. attribute:: cipsecspivalue
            
            	The value of the SPI
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CiscoIpsecFlowMonitorMib.Cipsecspitable.Cipsecspientry, self).__init__()

                self.yang_name = "cipSecSpiEntry"
                self.yang_parent_name = "cipSecSpiTable"

                self.cipsectunindex = YLeaf(YType.str, "cipSecTunIndex")

                self.cipsecspiindex = YLeaf(YType.int32, "cipSecSpiIndex")

                self.cipsecspidirection = YLeaf(YType.enumeration, "cipSecSpiDirection")

                self.cipsecspiprotocol = YLeaf(YType.enumeration, "cipSecSpiProtocol")

                self.cipsecspistatus = YLeaf(YType.enumeration, "cipSecSpiStatus")

                self.cipsecspivalue = YLeaf(YType.uint32, "cipSecSpiValue")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipsectunindex",
                                "cipsecspiindex",
                                "cipsecspidirection",
                                "cipsecspiprotocol",
                                "cipsecspistatus",
                                "cipsecspivalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecFlowMonitorMib.Cipsecspitable.Cipsecspientry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecFlowMonitorMib.Cipsecspitable.Cipsecspientry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.cipsectunindex.is_set or
                    self.cipsecspiindex.is_set or
                    self.cipsecspidirection.is_set or
                    self.cipsecspiprotocol.is_set or
                    self.cipsecspistatus.is_set or
                    self.cipsecspivalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipsectunindex.yfilter != YFilter.not_set or
                    self.cipsecspiindex.yfilter != YFilter.not_set or
                    self.cipsecspidirection.yfilter != YFilter.not_set or
                    self.cipsecspiprotocol.yfilter != YFilter.not_set or
                    self.cipsecspistatus.yfilter != YFilter.not_set or
                    self.cipsecspivalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipSecSpiEntry" + "[cipSecTunIndex='" + self.cipsectunindex.get() + "']" + "[cipSecSpiIndex='" + self.cipsecspiindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecSpiTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipsectunindex.is_set or self.cipsectunindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunindex.get_name_leafdata())
                if (self.cipsecspiindex.is_set or self.cipsecspiindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecspiindex.get_name_leafdata())
                if (self.cipsecspidirection.is_set or self.cipsecspidirection.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecspidirection.get_name_leafdata())
                if (self.cipsecspiprotocol.is_set or self.cipsecspiprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecspiprotocol.get_name_leafdata())
                if (self.cipsecspistatus.is_set or self.cipsecspistatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecspistatus.get_name_leafdata())
                if (self.cipsecspivalue.is_set or self.cipsecspivalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecspivalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipSecTunIndex" or name == "cipSecSpiIndex" or name == "cipSecSpiDirection" or name == "cipSecSpiProtocol" or name == "cipSecSpiStatus" or name == "cipSecSpiValue"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipSecTunIndex"):
                    self.cipsectunindex = value
                    self.cipsectunindex.value_namespace = name_space
                    self.cipsectunindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecSpiIndex"):
                    self.cipsecspiindex = value
                    self.cipsecspiindex.value_namespace = name_space
                    self.cipsecspiindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecSpiDirection"):
                    self.cipsecspidirection = value
                    self.cipsecspidirection.value_namespace = name_space
                    self.cipsecspidirection.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecSpiProtocol"):
                    self.cipsecspiprotocol = value
                    self.cipsecspiprotocol.value_namespace = name_space
                    self.cipsecspiprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecSpiStatus"):
                    self.cipsecspistatus = value
                    self.cipsecspistatus.value_namespace = name_space
                    self.cipsecspistatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecSpiValue"):
                    self.cipsecspivalue = value
                    self.cipsecspivalue.value_namespace = name_space
                    self.cipsecspivalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipsecspientry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipsecspientry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipSecSpiTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipSecSpiEntry"):
                for c in self.cipsecspientry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecFlowMonitorMib.Cipsecspitable.Cipsecspientry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipsecspientry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipSecSpiEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cipsecphase2Gwstatstable(Entity):
        """
        Phase\-2 IPsec stats information is included in this table.
        Each entry is related to a specific gateway which is 
        identified by 'cmgwIndex'
        
        .. attribute:: cipsecphase2gwstatsentry
        
        	Each entry contains the attributes of an Phase\-2 IPsec stats information for the related gateway.  There is only one entry for each gateway. The entry  is created when a gateway up and cannot be deleted
        	**type**\: list of    :py:class:`Cipsecphase2Gwstatsentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecphase2Gwstatstable.Cipsecphase2Gwstatsentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CiscoIpsecFlowMonitorMib.Cipsecphase2Gwstatstable, self).__init__()

            self.yang_name = "cipSecPhase2GWStatsTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

            self.cipsecphase2gwstatsentry = YList(self)

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
                        super(CiscoIpsecFlowMonitorMib.Cipsecphase2Gwstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Cipsecphase2Gwstatstable, self).__setattr__(name, value)


        class Cipsecphase2Gwstatsentry(Entity):
            """
            Each entry contains the attributes of an Phase\-2 IPsec stats
            information for the related gateway.
            
            There is only one entry for each gateway. The entry 
            is created when a gateway up and cannot be deleted.
            
            .. attribute:: cmgwindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cmgwindex <ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB.CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry>`
            
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
                super(CiscoIpsecFlowMonitorMib.Cipsecphase2Gwstatstable.Cipsecphase2Gwstatsentry, self).__init__()

                self.yang_name = "cipSecPhase2GWStatsEntry"
                self.yang_parent_name = "cipSecPhase2GWStatsTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cmgwindex",
                                "cipsecphase2gwactivetunnels",
                                "cipsecphase2gwinauthfails",
                                "cipsecphase2gwinauths",
                                "cipsecphase2gwindecompoctets",
                                "cipsecphase2gwindecompoctwraps",
                                "cipsecphase2gwindecryptfails",
                                "cipsecphase2gwindecrypts",
                                "cipsecphase2gwindrops",
                                "cipsecphase2gwinoctets",
                                "cipsecphase2gwinoctwraps",
                                "cipsecphase2gwinpkts",
                                "cipsecphase2gwinreplaydrops",
                                "cipsecphase2gwnosafails",
                                "cipsecphase2gwoutauthfails",
                                "cipsecphase2gwoutauths",
                                "cipsecphase2gwoutdrops",
                                "cipsecphase2gwoutencryptfails",
                                "cipsecphase2gwoutencrypts",
                                "cipsecphase2gwoutoctets",
                                "cipsecphase2gwoutoctwraps",
                                "cipsecphase2gwoutpkts",
                                "cipsecphase2gwoutuncompoctets",
                                "cipsecphase2gwoutuncompoctwraps",
                                "cipsecphase2gwprevioustunnels",
                                "cipsecphase2gwprotocolusefails",
                                "cipsecphase2gwsyscapfails") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecFlowMonitorMib.Cipsecphase2Gwstatstable.Cipsecphase2Gwstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecFlowMonitorMib.Cipsecphase2Gwstatstable.Cipsecphase2Gwstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cmgwindex.is_set or
                    self.cipsecphase2gwactivetunnels.is_set or
                    self.cipsecphase2gwinauthfails.is_set or
                    self.cipsecphase2gwinauths.is_set or
                    self.cipsecphase2gwindecompoctets.is_set or
                    self.cipsecphase2gwindecompoctwraps.is_set or
                    self.cipsecphase2gwindecryptfails.is_set or
                    self.cipsecphase2gwindecrypts.is_set or
                    self.cipsecphase2gwindrops.is_set or
                    self.cipsecphase2gwinoctets.is_set or
                    self.cipsecphase2gwinoctwraps.is_set or
                    self.cipsecphase2gwinpkts.is_set or
                    self.cipsecphase2gwinreplaydrops.is_set or
                    self.cipsecphase2gwnosafails.is_set or
                    self.cipsecphase2gwoutauthfails.is_set or
                    self.cipsecphase2gwoutauths.is_set or
                    self.cipsecphase2gwoutdrops.is_set or
                    self.cipsecphase2gwoutencryptfails.is_set or
                    self.cipsecphase2gwoutencrypts.is_set or
                    self.cipsecphase2gwoutoctets.is_set or
                    self.cipsecphase2gwoutoctwraps.is_set or
                    self.cipsecphase2gwoutpkts.is_set or
                    self.cipsecphase2gwoutuncompoctets.is_set or
                    self.cipsecphase2gwoutuncompoctwraps.is_set or
                    self.cipsecphase2gwprevioustunnels.is_set or
                    self.cipsecphase2gwprotocolusefails.is_set or
                    self.cipsecphase2gwsyscapfails.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cmgwindex.yfilter != YFilter.not_set or
                    self.cipsecphase2gwactivetunnels.yfilter != YFilter.not_set or
                    self.cipsecphase2gwinauthfails.yfilter != YFilter.not_set or
                    self.cipsecphase2gwinauths.yfilter != YFilter.not_set or
                    self.cipsecphase2gwindecompoctets.yfilter != YFilter.not_set or
                    self.cipsecphase2gwindecompoctwraps.yfilter != YFilter.not_set or
                    self.cipsecphase2gwindecryptfails.yfilter != YFilter.not_set or
                    self.cipsecphase2gwindecrypts.yfilter != YFilter.not_set or
                    self.cipsecphase2gwindrops.yfilter != YFilter.not_set or
                    self.cipsecphase2gwinoctets.yfilter != YFilter.not_set or
                    self.cipsecphase2gwinoctwraps.yfilter != YFilter.not_set or
                    self.cipsecphase2gwinpkts.yfilter != YFilter.not_set or
                    self.cipsecphase2gwinreplaydrops.yfilter != YFilter.not_set or
                    self.cipsecphase2gwnosafails.yfilter != YFilter.not_set or
                    self.cipsecphase2gwoutauthfails.yfilter != YFilter.not_set or
                    self.cipsecphase2gwoutauths.yfilter != YFilter.not_set or
                    self.cipsecphase2gwoutdrops.yfilter != YFilter.not_set or
                    self.cipsecphase2gwoutencryptfails.yfilter != YFilter.not_set or
                    self.cipsecphase2gwoutencrypts.yfilter != YFilter.not_set or
                    self.cipsecphase2gwoutoctets.yfilter != YFilter.not_set or
                    self.cipsecphase2gwoutoctwraps.yfilter != YFilter.not_set or
                    self.cipsecphase2gwoutpkts.yfilter != YFilter.not_set or
                    self.cipsecphase2gwoutuncompoctets.yfilter != YFilter.not_set or
                    self.cipsecphase2gwoutuncompoctwraps.yfilter != YFilter.not_set or
                    self.cipsecphase2gwprevioustunnels.yfilter != YFilter.not_set or
                    self.cipsecphase2gwprotocolusefails.yfilter != YFilter.not_set or
                    self.cipsecphase2gwsyscapfails.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipSecPhase2GWStatsEntry" + "[cmgwIndex='" + self.cmgwindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecPhase2GWStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cmgwindex.is_set or self.cmgwindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmgwindex.get_name_leafdata())
                if (self.cipsecphase2gwactivetunnels.is_set or self.cipsecphase2gwactivetunnels.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwactivetunnels.get_name_leafdata())
                if (self.cipsecphase2gwinauthfails.is_set or self.cipsecphase2gwinauthfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwinauthfails.get_name_leafdata())
                if (self.cipsecphase2gwinauths.is_set or self.cipsecphase2gwinauths.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwinauths.get_name_leafdata())
                if (self.cipsecphase2gwindecompoctets.is_set or self.cipsecphase2gwindecompoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwindecompoctets.get_name_leafdata())
                if (self.cipsecphase2gwindecompoctwraps.is_set or self.cipsecphase2gwindecompoctwraps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwindecompoctwraps.get_name_leafdata())
                if (self.cipsecphase2gwindecryptfails.is_set or self.cipsecphase2gwindecryptfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwindecryptfails.get_name_leafdata())
                if (self.cipsecphase2gwindecrypts.is_set or self.cipsecphase2gwindecrypts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwindecrypts.get_name_leafdata())
                if (self.cipsecphase2gwindrops.is_set or self.cipsecphase2gwindrops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwindrops.get_name_leafdata())
                if (self.cipsecphase2gwinoctets.is_set or self.cipsecphase2gwinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwinoctets.get_name_leafdata())
                if (self.cipsecphase2gwinoctwraps.is_set or self.cipsecphase2gwinoctwraps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwinoctwraps.get_name_leafdata())
                if (self.cipsecphase2gwinpkts.is_set or self.cipsecphase2gwinpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwinpkts.get_name_leafdata())
                if (self.cipsecphase2gwinreplaydrops.is_set or self.cipsecphase2gwinreplaydrops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwinreplaydrops.get_name_leafdata())
                if (self.cipsecphase2gwnosafails.is_set or self.cipsecphase2gwnosafails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwnosafails.get_name_leafdata())
                if (self.cipsecphase2gwoutauthfails.is_set or self.cipsecphase2gwoutauthfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwoutauthfails.get_name_leafdata())
                if (self.cipsecphase2gwoutauths.is_set or self.cipsecphase2gwoutauths.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwoutauths.get_name_leafdata())
                if (self.cipsecphase2gwoutdrops.is_set or self.cipsecphase2gwoutdrops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwoutdrops.get_name_leafdata())
                if (self.cipsecphase2gwoutencryptfails.is_set or self.cipsecphase2gwoutencryptfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwoutencryptfails.get_name_leafdata())
                if (self.cipsecphase2gwoutencrypts.is_set or self.cipsecphase2gwoutencrypts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwoutencrypts.get_name_leafdata())
                if (self.cipsecphase2gwoutoctets.is_set or self.cipsecphase2gwoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwoutoctets.get_name_leafdata())
                if (self.cipsecphase2gwoutoctwraps.is_set or self.cipsecphase2gwoutoctwraps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwoutoctwraps.get_name_leafdata())
                if (self.cipsecphase2gwoutpkts.is_set or self.cipsecphase2gwoutpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwoutpkts.get_name_leafdata())
                if (self.cipsecphase2gwoutuncompoctets.is_set or self.cipsecphase2gwoutuncompoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwoutuncompoctets.get_name_leafdata())
                if (self.cipsecphase2gwoutuncompoctwraps.is_set or self.cipsecphase2gwoutuncompoctwraps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwoutuncompoctwraps.get_name_leafdata())
                if (self.cipsecphase2gwprevioustunnels.is_set or self.cipsecphase2gwprevioustunnels.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwprevioustunnels.get_name_leafdata())
                if (self.cipsecphase2gwprotocolusefails.is_set or self.cipsecphase2gwprotocolusefails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwprotocolusefails.get_name_leafdata())
                if (self.cipsecphase2gwsyscapfails.is_set or self.cipsecphase2gwsyscapfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecphase2gwsyscapfails.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cmgwIndex" or name == "cipSecPhase2GWActiveTunnels" or name == "cipSecPhase2GWInAuthFails" or name == "cipSecPhase2GWInAuths" or name == "cipSecPhase2GWInDecompOctets" or name == "cipSecPhase2GWInDecompOctWraps" or name == "cipSecPhase2GWInDecryptFails" or name == "cipSecPhase2GWInDecrypts" or name == "cipSecPhase2GWInDrops" or name == "cipSecPhase2GWInOctets" or name == "cipSecPhase2GWInOctWraps" or name == "cipSecPhase2GWInPkts" or name == "cipSecPhase2GWInReplayDrops" or name == "cipSecPhase2GWNoSaFails" or name == "cipSecPhase2GWOutAuthFails" or name == "cipSecPhase2GWOutAuths" or name == "cipSecPhase2GWOutDrops" or name == "cipSecPhase2GWOutEncryptFails" or name == "cipSecPhase2GWOutEncrypts" or name == "cipSecPhase2GWOutOctets" or name == "cipSecPhase2GWOutOctWraps" or name == "cipSecPhase2GWOutPkts" or name == "cipSecPhase2GWOutUncompOctets" or name == "cipSecPhase2GWOutUncompOctWraps" or name == "cipSecPhase2GWPreviousTunnels" or name == "cipSecPhase2GWProtocolUseFails" or name == "cipSecPhase2GWSysCapFails"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cmgwIndex"):
                    self.cmgwindex = value
                    self.cmgwindex.value_namespace = name_space
                    self.cmgwindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWActiveTunnels"):
                    self.cipsecphase2gwactivetunnels = value
                    self.cipsecphase2gwactivetunnels.value_namespace = name_space
                    self.cipsecphase2gwactivetunnels.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWInAuthFails"):
                    self.cipsecphase2gwinauthfails = value
                    self.cipsecphase2gwinauthfails.value_namespace = name_space
                    self.cipsecphase2gwinauthfails.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWInAuths"):
                    self.cipsecphase2gwinauths = value
                    self.cipsecphase2gwinauths.value_namespace = name_space
                    self.cipsecphase2gwinauths.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWInDecompOctets"):
                    self.cipsecphase2gwindecompoctets = value
                    self.cipsecphase2gwindecompoctets.value_namespace = name_space
                    self.cipsecphase2gwindecompoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWInDecompOctWraps"):
                    self.cipsecphase2gwindecompoctwraps = value
                    self.cipsecphase2gwindecompoctwraps.value_namespace = name_space
                    self.cipsecphase2gwindecompoctwraps.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWInDecryptFails"):
                    self.cipsecphase2gwindecryptfails = value
                    self.cipsecphase2gwindecryptfails.value_namespace = name_space
                    self.cipsecphase2gwindecryptfails.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWInDecrypts"):
                    self.cipsecphase2gwindecrypts = value
                    self.cipsecphase2gwindecrypts.value_namespace = name_space
                    self.cipsecphase2gwindecrypts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWInDrops"):
                    self.cipsecphase2gwindrops = value
                    self.cipsecphase2gwindrops.value_namespace = name_space
                    self.cipsecphase2gwindrops.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWInOctets"):
                    self.cipsecphase2gwinoctets = value
                    self.cipsecphase2gwinoctets.value_namespace = name_space
                    self.cipsecphase2gwinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWInOctWraps"):
                    self.cipsecphase2gwinoctwraps = value
                    self.cipsecphase2gwinoctwraps.value_namespace = name_space
                    self.cipsecphase2gwinoctwraps.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWInPkts"):
                    self.cipsecphase2gwinpkts = value
                    self.cipsecphase2gwinpkts.value_namespace = name_space
                    self.cipsecphase2gwinpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWInReplayDrops"):
                    self.cipsecphase2gwinreplaydrops = value
                    self.cipsecphase2gwinreplaydrops.value_namespace = name_space
                    self.cipsecphase2gwinreplaydrops.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWNoSaFails"):
                    self.cipsecphase2gwnosafails = value
                    self.cipsecphase2gwnosafails.value_namespace = name_space
                    self.cipsecphase2gwnosafails.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWOutAuthFails"):
                    self.cipsecphase2gwoutauthfails = value
                    self.cipsecphase2gwoutauthfails.value_namespace = name_space
                    self.cipsecphase2gwoutauthfails.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWOutAuths"):
                    self.cipsecphase2gwoutauths = value
                    self.cipsecphase2gwoutauths.value_namespace = name_space
                    self.cipsecphase2gwoutauths.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWOutDrops"):
                    self.cipsecphase2gwoutdrops = value
                    self.cipsecphase2gwoutdrops.value_namespace = name_space
                    self.cipsecphase2gwoutdrops.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWOutEncryptFails"):
                    self.cipsecphase2gwoutencryptfails = value
                    self.cipsecphase2gwoutencryptfails.value_namespace = name_space
                    self.cipsecphase2gwoutencryptfails.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWOutEncrypts"):
                    self.cipsecphase2gwoutencrypts = value
                    self.cipsecphase2gwoutencrypts.value_namespace = name_space
                    self.cipsecphase2gwoutencrypts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWOutOctets"):
                    self.cipsecphase2gwoutoctets = value
                    self.cipsecphase2gwoutoctets.value_namespace = name_space
                    self.cipsecphase2gwoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWOutOctWraps"):
                    self.cipsecphase2gwoutoctwraps = value
                    self.cipsecphase2gwoutoctwraps.value_namespace = name_space
                    self.cipsecphase2gwoutoctwraps.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWOutPkts"):
                    self.cipsecphase2gwoutpkts = value
                    self.cipsecphase2gwoutpkts.value_namespace = name_space
                    self.cipsecphase2gwoutpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWOutUncompOctets"):
                    self.cipsecphase2gwoutuncompoctets = value
                    self.cipsecphase2gwoutuncompoctets.value_namespace = name_space
                    self.cipsecphase2gwoutuncompoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWOutUncompOctWraps"):
                    self.cipsecphase2gwoutuncompoctwraps = value
                    self.cipsecphase2gwoutuncompoctwraps.value_namespace = name_space
                    self.cipsecphase2gwoutuncompoctwraps.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWPreviousTunnels"):
                    self.cipsecphase2gwprevioustunnels = value
                    self.cipsecphase2gwprevioustunnels.value_namespace = name_space
                    self.cipsecphase2gwprevioustunnels.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWProtocolUseFails"):
                    self.cipsecphase2gwprotocolusefails = value
                    self.cipsecphase2gwprotocolusefails.value_namespace = name_space
                    self.cipsecphase2gwprotocolusefails.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecPhase2GWSysCapFails"):
                    self.cipsecphase2gwsyscapfails = value
                    self.cipsecphase2gwsyscapfails.value_namespace = name_space
                    self.cipsecphase2gwsyscapfails.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipsecphase2gwstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipsecphase2gwstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipSecPhase2GWStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipSecPhase2GWStatsEntry"):
                for c in self.cipsecphase2gwstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecFlowMonitorMib.Cipsecphase2Gwstatstable.Cipsecphase2Gwstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipsecphase2gwstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipSecPhase2GWStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciketunnelhisttable(Entity):
        """
        The IPsec Phase\-1 Internet Key Exchange Tunnel
        History Table.  This table is implemented as a 
        sliding window in which only the last n entries 
        are maintained.  The maximum number of entries
         is specified by the cipSecHistTableSize object.
        
        .. attribute:: ciketunnelhistentry
        
        	Each entry contains the attributes associated with a previously active IPsec  Phase\-1 IKE Tunnel
        	**type**\: list of    :py:class:`Ciketunnelhistentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Ciketunnelhisttable.Ciketunnelhistentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CiscoIpsecFlowMonitorMib.Ciketunnelhisttable, self).__init__()

            self.yang_name = "cikeTunnelHistTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

            self.ciketunnelhistentry = YList(self)

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
                        super(CiscoIpsecFlowMonitorMib.Ciketunnelhisttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Ciketunnelhisttable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Ikeauthmethod <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Ikeauthmethod>`
            
            .. attribute:: ciketunhistdiffhellmangrp
            
            	The Diffie Hellman Group used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`Diffhellmangrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Diffhellmangrp>`
            
            .. attribute:: ciketunhistencryptalgo
            
            	The encryption algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`Encryptalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Encryptalgo>`
            
            .. attribute:: ciketunhisthashalgo
            
            	The hash algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`Ikehashalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Ikehashalgo>`
            
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
            	**type**\:   :py:class:`Ikenegomode <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Ikenegomode>`
            
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
            	**type**\:   :py:class:`Ikepeertype <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Ikepeertype>`
            
            .. attribute:: ciketunhistpeerlocalvalue
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\:  str
            
            .. attribute:: ciketunhistpeerremotetype
            
            	The type of remote peer identity.  The remote peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\:   :py:class:`Ikepeertype <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Ikepeertype>`
            
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
            	**type**\:   :py:class:`Ciketunhisttermreason <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Ciketunnelhisttable.Ciketunnelhistentry.Ciketunhisttermreason>`
            
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
                super(CiscoIpsecFlowMonitorMib.Ciketunnelhisttable.Ciketunnelhistentry, self).__init__()

                self.yang_name = "cikeTunnelHistEntry"
                self.yang_parent_name = "cikeTunnelHistTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciketunhistindex",
                                "ciketunhistactiveindex",
                                "ciketunhistactivetime",
                                "ciketunhistauthmethod",
                                "ciketunhistdiffhellmangrp",
                                "ciketunhistencryptalgo",
                                "ciketunhisthashalgo",
                                "ciketunhistindroppkts",
                                "ciketunhistinnotifys",
                                "ciketunhistinoctets",
                                "ciketunhistinp2exchginvalids",
                                "ciketunhistinp2exchgrejects",
                                "ciketunhistinp2exchgs",
                                "ciketunhistinp2sadelrequests",
                                "ciketunhistinpkts",
                                "ciketunhistlifetime",
                                "ciketunhistlocaladdr",
                                "ciketunhistlocalname",
                                "ciketunhistnegomode",
                                "ciketunhistoutdroppkts",
                                "ciketunhistoutnotifys",
                                "ciketunhistoutoctets",
                                "ciketunhistoutp2exchginvalids",
                                "ciketunhistoutp2exchgrejects",
                                "ciketunhistoutp2exchgs",
                                "ciketunhistoutp2sadelrequests",
                                "ciketunhistoutpkts",
                                "ciketunhistpeerintindex",
                                "ciketunhistpeerlocaltype",
                                "ciketunhistpeerlocalvalue",
                                "ciketunhistpeerremotetype",
                                "ciketunhistpeerremotevalue",
                                "ciketunhistremoteaddr",
                                "ciketunhistremotename",
                                "ciketunhiststarttime",
                                "ciketunhisttermreason",
                                "ciketunhisttotalrefreshes",
                                "ciketunhisttotalsas") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecFlowMonitorMib.Ciketunnelhisttable.Ciketunnelhistentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecFlowMonitorMib.Ciketunnelhisttable.Ciketunnelhistentry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.ciketunhistindex.is_set or
                    self.ciketunhistactiveindex.is_set or
                    self.ciketunhistactivetime.is_set or
                    self.ciketunhistauthmethod.is_set or
                    self.ciketunhistdiffhellmangrp.is_set or
                    self.ciketunhistencryptalgo.is_set or
                    self.ciketunhisthashalgo.is_set or
                    self.ciketunhistindroppkts.is_set or
                    self.ciketunhistinnotifys.is_set or
                    self.ciketunhistinoctets.is_set or
                    self.ciketunhistinp2exchginvalids.is_set or
                    self.ciketunhistinp2exchgrejects.is_set or
                    self.ciketunhistinp2exchgs.is_set or
                    self.ciketunhistinp2sadelrequests.is_set or
                    self.ciketunhistinpkts.is_set or
                    self.ciketunhistlifetime.is_set or
                    self.ciketunhistlocaladdr.is_set or
                    self.ciketunhistlocalname.is_set or
                    self.ciketunhistnegomode.is_set or
                    self.ciketunhistoutdroppkts.is_set or
                    self.ciketunhistoutnotifys.is_set or
                    self.ciketunhistoutoctets.is_set or
                    self.ciketunhistoutp2exchginvalids.is_set or
                    self.ciketunhistoutp2exchgrejects.is_set or
                    self.ciketunhistoutp2exchgs.is_set or
                    self.ciketunhistoutp2sadelrequests.is_set or
                    self.ciketunhistoutpkts.is_set or
                    self.ciketunhistpeerintindex.is_set or
                    self.ciketunhistpeerlocaltype.is_set or
                    self.ciketunhistpeerlocalvalue.is_set or
                    self.ciketunhistpeerremotetype.is_set or
                    self.ciketunhistpeerremotevalue.is_set or
                    self.ciketunhistremoteaddr.is_set or
                    self.ciketunhistremotename.is_set or
                    self.ciketunhiststarttime.is_set or
                    self.ciketunhisttermreason.is_set or
                    self.ciketunhisttotalrefreshes.is_set or
                    self.ciketunhisttotalsas.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciketunhistindex.yfilter != YFilter.not_set or
                    self.ciketunhistactiveindex.yfilter != YFilter.not_set or
                    self.ciketunhistactivetime.yfilter != YFilter.not_set or
                    self.ciketunhistauthmethod.yfilter != YFilter.not_set or
                    self.ciketunhistdiffhellmangrp.yfilter != YFilter.not_set or
                    self.ciketunhistencryptalgo.yfilter != YFilter.not_set or
                    self.ciketunhisthashalgo.yfilter != YFilter.not_set or
                    self.ciketunhistindroppkts.yfilter != YFilter.not_set or
                    self.ciketunhistinnotifys.yfilter != YFilter.not_set or
                    self.ciketunhistinoctets.yfilter != YFilter.not_set or
                    self.ciketunhistinp2exchginvalids.yfilter != YFilter.not_set or
                    self.ciketunhistinp2exchgrejects.yfilter != YFilter.not_set or
                    self.ciketunhistinp2exchgs.yfilter != YFilter.not_set or
                    self.ciketunhistinp2sadelrequests.yfilter != YFilter.not_set or
                    self.ciketunhistinpkts.yfilter != YFilter.not_set or
                    self.ciketunhistlifetime.yfilter != YFilter.not_set or
                    self.ciketunhistlocaladdr.yfilter != YFilter.not_set or
                    self.ciketunhistlocalname.yfilter != YFilter.not_set or
                    self.ciketunhistnegomode.yfilter != YFilter.not_set or
                    self.ciketunhistoutdroppkts.yfilter != YFilter.not_set or
                    self.ciketunhistoutnotifys.yfilter != YFilter.not_set or
                    self.ciketunhistoutoctets.yfilter != YFilter.not_set or
                    self.ciketunhistoutp2exchginvalids.yfilter != YFilter.not_set or
                    self.ciketunhistoutp2exchgrejects.yfilter != YFilter.not_set or
                    self.ciketunhistoutp2exchgs.yfilter != YFilter.not_set or
                    self.ciketunhistoutp2sadelrequests.yfilter != YFilter.not_set or
                    self.ciketunhistoutpkts.yfilter != YFilter.not_set or
                    self.ciketunhistpeerintindex.yfilter != YFilter.not_set or
                    self.ciketunhistpeerlocaltype.yfilter != YFilter.not_set or
                    self.ciketunhistpeerlocalvalue.yfilter != YFilter.not_set or
                    self.ciketunhistpeerremotetype.yfilter != YFilter.not_set or
                    self.ciketunhistpeerremotevalue.yfilter != YFilter.not_set or
                    self.ciketunhistremoteaddr.yfilter != YFilter.not_set or
                    self.ciketunhistremotename.yfilter != YFilter.not_set or
                    self.ciketunhiststarttime.yfilter != YFilter.not_set or
                    self.ciketunhisttermreason.yfilter != YFilter.not_set or
                    self.ciketunhisttotalrefreshes.yfilter != YFilter.not_set or
                    self.ciketunhisttotalsas.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cikeTunnelHistEntry" + "[cikeTunHistIndex='" + self.ciketunhistindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikeTunnelHistTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciketunhistindex.is_set or self.ciketunhistindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistindex.get_name_leafdata())
                if (self.ciketunhistactiveindex.is_set or self.ciketunhistactiveindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistactiveindex.get_name_leafdata())
                if (self.ciketunhistactivetime.is_set or self.ciketunhistactivetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistactivetime.get_name_leafdata())
                if (self.ciketunhistauthmethod.is_set or self.ciketunhistauthmethod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistauthmethod.get_name_leafdata())
                if (self.ciketunhistdiffhellmangrp.is_set or self.ciketunhistdiffhellmangrp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistdiffhellmangrp.get_name_leafdata())
                if (self.ciketunhistencryptalgo.is_set or self.ciketunhistencryptalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistencryptalgo.get_name_leafdata())
                if (self.ciketunhisthashalgo.is_set or self.ciketunhisthashalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhisthashalgo.get_name_leafdata())
                if (self.ciketunhistindroppkts.is_set or self.ciketunhistindroppkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistindroppkts.get_name_leafdata())
                if (self.ciketunhistinnotifys.is_set or self.ciketunhistinnotifys.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistinnotifys.get_name_leafdata())
                if (self.ciketunhistinoctets.is_set or self.ciketunhistinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistinoctets.get_name_leafdata())
                if (self.ciketunhistinp2exchginvalids.is_set or self.ciketunhistinp2exchginvalids.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistinp2exchginvalids.get_name_leafdata())
                if (self.ciketunhistinp2exchgrejects.is_set or self.ciketunhistinp2exchgrejects.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistinp2exchgrejects.get_name_leafdata())
                if (self.ciketunhistinp2exchgs.is_set or self.ciketunhistinp2exchgs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistinp2exchgs.get_name_leafdata())
                if (self.ciketunhistinp2sadelrequests.is_set or self.ciketunhistinp2sadelrequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistinp2sadelrequests.get_name_leafdata())
                if (self.ciketunhistinpkts.is_set or self.ciketunhistinpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistinpkts.get_name_leafdata())
                if (self.ciketunhistlifetime.is_set or self.ciketunhistlifetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistlifetime.get_name_leafdata())
                if (self.ciketunhistlocaladdr.is_set or self.ciketunhistlocaladdr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistlocaladdr.get_name_leafdata())
                if (self.ciketunhistlocalname.is_set or self.ciketunhistlocalname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistlocalname.get_name_leafdata())
                if (self.ciketunhistnegomode.is_set or self.ciketunhistnegomode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistnegomode.get_name_leafdata())
                if (self.ciketunhistoutdroppkts.is_set or self.ciketunhistoutdroppkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistoutdroppkts.get_name_leafdata())
                if (self.ciketunhistoutnotifys.is_set or self.ciketunhistoutnotifys.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistoutnotifys.get_name_leafdata())
                if (self.ciketunhistoutoctets.is_set or self.ciketunhistoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistoutoctets.get_name_leafdata())
                if (self.ciketunhistoutp2exchginvalids.is_set or self.ciketunhistoutp2exchginvalids.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistoutp2exchginvalids.get_name_leafdata())
                if (self.ciketunhistoutp2exchgrejects.is_set or self.ciketunhistoutp2exchgrejects.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistoutp2exchgrejects.get_name_leafdata())
                if (self.ciketunhistoutp2exchgs.is_set or self.ciketunhistoutp2exchgs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistoutp2exchgs.get_name_leafdata())
                if (self.ciketunhistoutp2sadelrequests.is_set or self.ciketunhistoutp2sadelrequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistoutp2sadelrequests.get_name_leafdata())
                if (self.ciketunhistoutpkts.is_set or self.ciketunhistoutpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistoutpkts.get_name_leafdata())
                if (self.ciketunhistpeerintindex.is_set or self.ciketunhistpeerintindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistpeerintindex.get_name_leafdata())
                if (self.ciketunhistpeerlocaltype.is_set or self.ciketunhistpeerlocaltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistpeerlocaltype.get_name_leafdata())
                if (self.ciketunhistpeerlocalvalue.is_set or self.ciketunhistpeerlocalvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistpeerlocalvalue.get_name_leafdata())
                if (self.ciketunhistpeerremotetype.is_set or self.ciketunhistpeerremotetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistpeerremotetype.get_name_leafdata())
                if (self.ciketunhistpeerremotevalue.is_set or self.ciketunhistpeerremotevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistpeerremotevalue.get_name_leafdata())
                if (self.ciketunhistremoteaddr.is_set or self.ciketunhistremoteaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistremoteaddr.get_name_leafdata())
                if (self.ciketunhistremotename.is_set or self.ciketunhistremotename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhistremotename.get_name_leafdata())
                if (self.ciketunhiststarttime.is_set or self.ciketunhiststarttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhiststarttime.get_name_leafdata())
                if (self.ciketunhisttermreason.is_set or self.ciketunhisttermreason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhisttermreason.get_name_leafdata())
                if (self.ciketunhisttotalrefreshes.is_set or self.ciketunhisttotalrefreshes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhisttotalrefreshes.get_name_leafdata())
                if (self.ciketunhisttotalsas.is_set or self.ciketunhisttotalsas.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciketunhisttotalsas.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cikeTunHistIndex" or name == "cikeTunHistActiveIndex" or name == "cikeTunHistActiveTime" or name == "cikeTunHistAuthMethod" or name == "cikeTunHistDiffHellmanGrp" or name == "cikeTunHistEncryptAlgo" or name == "cikeTunHistHashAlgo" or name == "cikeTunHistInDropPkts" or name == "cikeTunHistInNotifys" or name == "cikeTunHistInOctets" or name == "cikeTunHistInP2ExchgInvalids" or name == "cikeTunHistInP2ExchgRejects" or name == "cikeTunHistInP2Exchgs" or name == "cikeTunHistInP2SaDelRequests" or name == "cikeTunHistInPkts" or name == "cikeTunHistLifeTime" or name == "cikeTunHistLocalAddr" or name == "cikeTunHistLocalName" or name == "cikeTunHistNegoMode" or name == "cikeTunHistOutDropPkts" or name == "cikeTunHistOutNotifys" or name == "cikeTunHistOutOctets" or name == "cikeTunHistOutP2ExchgInvalids" or name == "cikeTunHistOutP2ExchgRejects" or name == "cikeTunHistOutP2Exchgs" or name == "cikeTunHistOutP2SaDelRequests" or name == "cikeTunHistOutPkts" or name == "cikeTunHistPeerIntIndex" or name == "cikeTunHistPeerLocalType" or name == "cikeTunHistPeerLocalValue" or name == "cikeTunHistPeerRemoteType" or name == "cikeTunHistPeerRemoteValue" or name == "cikeTunHistRemoteAddr" or name == "cikeTunHistRemoteName" or name == "cikeTunHistStartTime" or name == "cikeTunHistTermReason" or name == "cikeTunHistTotalRefreshes" or name == "cikeTunHistTotalSas"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cikeTunHistIndex"):
                    self.ciketunhistindex = value
                    self.ciketunhistindex.value_namespace = name_space
                    self.ciketunhistindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistActiveIndex"):
                    self.ciketunhistactiveindex = value
                    self.ciketunhistactiveindex.value_namespace = name_space
                    self.ciketunhistactiveindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistActiveTime"):
                    self.ciketunhistactivetime = value
                    self.ciketunhistactivetime.value_namespace = name_space
                    self.ciketunhistactivetime.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistAuthMethod"):
                    self.ciketunhistauthmethod = value
                    self.ciketunhistauthmethod.value_namespace = name_space
                    self.ciketunhistauthmethod.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistDiffHellmanGrp"):
                    self.ciketunhistdiffhellmangrp = value
                    self.ciketunhistdiffhellmangrp.value_namespace = name_space
                    self.ciketunhistdiffhellmangrp.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistEncryptAlgo"):
                    self.ciketunhistencryptalgo = value
                    self.ciketunhistencryptalgo.value_namespace = name_space
                    self.ciketunhistencryptalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistHashAlgo"):
                    self.ciketunhisthashalgo = value
                    self.ciketunhisthashalgo.value_namespace = name_space
                    self.ciketunhisthashalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistInDropPkts"):
                    self.ciketunhistindroppkts = value
                    self.ciketunhistindroppkts.value_namespace = name_space
                    self.ciketunhistindroppkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistInNotifys"):
                    self.ciketunhistinnotifys = value
                    self.ciketunhistinnotifys.value_namespace = name_space
                    self.ciketunhistinnotifys.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistInOctets"):
                    self.ciketunhistinoctets = value
                    self.ciketunhistinoctets.value_namespace = name_space
                    self.ciketunhistinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistInP2ExchgInvalids"):
                    self.ciketunhistinp2exchginvalids = value
                    self.ciketunhistinp2exchginvalids.value_namespace = name_space
                    self.ciketunhistinp2exchginvalids.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistInP2ExchgRejects"):
                    self.ciketunhistinp2exchgrejects = value
                    self.ciketunhistinp2exchgrejects.value_namespace = name_space
                    self.ciketunhistinp2exchgrejects.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistInP2Exchgs"):
                    self.ciketunhistinp2exchgs = value
                    self.ciketunhistinp2exchgs.value_namespace = name_space
                    self.ciketunhistinp2exchgs.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistInP2SaDelRequests"):
                    self.ciketunhistinp2sadelrequests = value
                    self.ciketunhistinp2sadelrequests.value_namespace = name_space
                    self.ciketunhistinp2sadelrequests.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistInPkts"):
                    self.ciketunhistinpkts = value
                    self.ciketunhistinpkts.value_namespace = name_space
                    self.ciketunhistinpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistLifeTime"):
                    self.ciketunhistlifetime = value
                    self.ciketunhistlifetime.value_namespace = name_space
                    self.ciketunhistlifetime.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistLocalAddr"):
                    self.ciketunhistlocaladdr = value
                    self.ciketunhistlocaladdr.value_namespace = name_space
                    self.ciketunhistlocaladdr.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistLocalName"):
                    self.ciketunhistlocalname = value
                    self.ciketunhistlocalname.value_namespace = name_space
                    self.ciketunhistlocalname.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistNegoMode"):
                    self.ciketunhistnegomode = value
                    self.ciketunhistnegomode.value_namespace = name_space
                    self.ciketunhistnegomode.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistOutDropPkts"):
                    self.ciketunhistoutdroppkts = value
                    self.ciketunhistoutdroppkts.value_namespace = name_space
                    self.ciketunhistoutdroppkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistOutNotifys"):
                    self.ciketunhistoutnotifys = value
                    self.ciketunhistoutnotifys.value_namespace = name_space
                    self.ciketunhistoutnotifys.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistOutOctets"):
                    self.ciketunhistoutoctets = value
                    self.ciketunhistoutoctets.value_namespace = name_space
                    self.ciketunhistoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistOutP2ExchgInvalids"):
                    self.ciketunhistoutp2exchginvalids = value
                    self.ciketunhistoutp2exchginvalids.value_namespace = name_space
                    self.ciketunhistoutp2exchginvalids.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistOutP2ExchgRejects"):
                    self.ciketunhistoutp2exchgrejects = value
                    self.ciketunhistoutp2exchgrejects.value_namespace = name_space
                    self.ciketunhistoutp2exchgrejects.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistOutP2Exchgs"):
                    self.ciketunhistoutp2exchgs = value
                    self.ciketunhistoutp2exchgs.value_namespace = name_space
                    self.ciketunhistoutp2exchgs.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistOutP2SaDelRequests"):
                    self.ciketunhistoutp2sadelrequests = value
                    self.ciketunhistoutp2sadelrequests.value_namespace = name_space
                    self.ciketunhistoutp2sadelrequests.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistOutPkts"):
                    self.ciketunhistoutpkts = value
                    self.ciketunhistoutpkts.value_namespace = name_space
                    self.ciketunhistoutpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistPeerIntIndex"):
                    self.ciketunhistpeerintindex = value
                    self.ciketunhistpeerintindex.value_namespace = name_space
                    self.ciketunhistpeerintindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistPeerLocalType"):
                    self.ciketunhistpeerlocaltype = value
                    self.ciketunhistpeerlocaltype.value_namespace = name_space
                    self.ciketunhistpeerlocaltype.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistPeerLocalValue"):
                    self.ciketunhistpeerlocalvalue = value
                    self.ciketunhistpeerlocalvalue.value_namespace = name_space
                    self.ciketunhistpeerlocalvalue.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistPeerRemoteType"):
                    self.ciketunhistpeerremotetype = value
                    self.ciketunhistpeerremotetype.value_namespace = name_space
                    self.ciketunhistpeerremotetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistPeerRemoteValue"):
                    self.ciketunhistpeerremotevalue = value
                    self.ciketunhistpeerremotevalue.value_namespace = name_space
                    self.ciketunhistpeerremotevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistRemoteAddr"):
                    self.ciketunhistremoteaddr = value
                    self.ciketunhistremoteaddr.value_namespace = name_space
                    self.ciketunhistremoteaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistRemoteName"):
                    self.ciketunhistremotename = value
                    self.ciketunhistremotename.value_namespace = name_space
                    self.ciketunhistremotename.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistStartTime"):
                    self.ciketunhiststarttime = value
                    self.ciketunhiststarttime.value_namespace = name_space
                    self.ciketunhiststarttime.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistTermReason"):
                    self.ciketunhisttermreason = value
                    self.ciketunhisttermreason.value_namespace = name_space
                    self.ciketunhisttermreason.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistTotalRefreshes"):
                    self.ciketunhisttotalrefreshes = value
                    self.ciketunhisttotalrefreshes.value_namespace = name_space
                    self.ciketunhisttotalrefreshes.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeTunHistTotalSas"):
                    self.ciketunhisttotalsas = value
                    self.ciketunhisttotalsas.value_namespace = name_space
                    self.ciketunhisttotalsas.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciketunnelhistentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciketunnelhistentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cikeTunnelHistTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cikeTunnelHistEntry"):
                for c in self.ciketunnelhistentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecFlowMonitorMib.Ciketunnelhisttable.Ciketunnelhistentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciketunnelhistentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cikeTunnelHistEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cipsectunnelhistentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsectunnelhisttable.Cipsectunnelhistentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CiscoIpsecFlowMonitorMib.Cipsectunnelhisttable, self).__init__()

            self.yang_name = "cipSecTunnelHistTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

            self.cipsectunnelhistentry = YList(self)

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
                        super(CiscoIpsecFlowMonitorMib.Cipsectunnelhisttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Cipsectunnelhisttable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Encapmode <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Encapmode>`
            
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
            	**type**\:   :py:class:`Authalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Authalgo>`
            
            .. attribute:: cipsectunhistinsadecompalgo
            
            	The decompression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Compalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Compalgo>`
            
            .. attribute:: cipsectunhistinsadiffhellmangrp
            
            	The Diffie Hellman Group used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Diffhellmangrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Diffhellmangrp>`
            
            .. attribute:: cipsectunhistinsaencryptalgo
            
            	The encryption algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Encryptalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Encryptalgo>`
            
            .. attribute:: cipsectunhistinsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP)  security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Authalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Authalgo>`
            
            .. attribute:: cipsectunhistkeytype
            
            	The type of key used by the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Keytype <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Keytype>`
            
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
            	**type**\:   :py:class:`Authalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Authalgo>`
            
            .. attribute:: cipsectunhistoutsacompalgo
            
            	The compression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Compalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Compalgo>`
            
            .. attribute:: cipsectunhistoutsadiffhellmangrp
            
            	The Diffie Hellman Group used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Diffhellmangrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Diffhellmangrp>`
            
            .. attribute:: cipsectunhistoutsaencryptalgo
            
            	The encryption algorithm used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Encryptalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Encryptalgo>`
            
            .. attribute:: cipsectunhistoutsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP)  security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`Authalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Authalgo>`
            
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
            	**type**\:   :py:class:`Cipsectunhisttermreason <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsectunnelhisttable.Cipsectunnelhistentry.Cipsectunhisttermreason>`
            
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
                super(CiscoIpsecFlowMonitorMib.Cipsectunnelhisttable.Cipsectunnelhistentry, self).__init__()

                self.yang_name = "cipSecTunnelHistEntry"
                self.yang_parent_name = "cipSecTunnelHistTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipsectunhistindex",
                                "cipsectunhistactiveindex",
                                "cipsectunhistactivetime",
                                "cipsectunhistencapmode",
                                "cipsectunhisthcindecompoctets",
                                "cipsectunhisthcinoctets",
                                "cipsectunhisthcoutoctets",
                                "cipsectunhisthcoutuncompoctets",
                                "cipsectunhistiketunnelindex",
                                "cipsectunhistinauthfails",
                                "cipsectunhistinauths",
                                "cipsectunhistindecompoctets",
                                "cipsectunhistindecompoctwraps",
                                "cipsectunhistindecryptfails",
                                "cipsectunhistindecrypts",
                                "cipsectunhistindroppkts",
                                "cipsectunhistinoctets",
                                "cipsectunhistinoctwraps",
                                "cipsectunhistinpkts",
                                "cipsectunhistinreplaydroppkts",
                                "cipsectunhistinsaahauthalgo",
                                "cipsectunhistinsadecompalgo",
                                "cipsectunhistinsadiffhellmangrp",
                                "cipsectunhistinsaencryptalgo",
                                "cipsectunhistinsaespauthalgo",
                                "cipsectunhistkeytype",
                                "cipsectunhistlifesize",
                                "cipsectunhistlifetime",
                                "cipsectunhistlocaladdr",
                                "cipsectunhistoutauthfails",
                                "cipsectunhistoutauths",
                                "cipsectunhistoutdroppkts",
                                "cipsectunhistoutencryptfails",
                                "cipsectunhistoutencrypts",
                                "cipsectunhistoutoctets",
                                "cipsectunhistoutoctwraps",
                                "cipsectunhistoutpkts",
                                "cipsectunhistoutsaahauthalgo",
                                "cipsectunhistoutsacompalgo",
                                "cipsectunhistoutsadiffhellmangrp",
                                "cipsectunhistoutsaencryptalgo",
                                "cipsectunhistoutsaespauthalgo",
                                "cipsectunhistoutuncompoctets",
                                "cipsectunhistoutuncompoctwraps",
                                "cipsectunhistremoteaddr",
                                "cipsectunhiststarttime",
                                "cipsectunhisttermreason",
                                "cipsectunhisttotalrefreshes",
                                "cipsectunhisttotalsas") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecFlowMonitorMib.Cipsectunnelhisttable.Cipsectunnelhistentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecFlowMonitorMib.Cipsectunnelhisttable.Cipsectunnelhistentry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.cipsectunhistindex.is_set or
                    self.cipsectunhistactiveindex.is_set or
                    self.cipsectunhistactivetime.is_set or
                    self.cipsectunhistencapmode.is_set or
                    self.cipsectunhisthcindecompoctets.is_set or
                    self.cipsectunhisthcinoctets.is_set or
                    self.cipsectunhisthcoutoctets.is_set or
                    self.cipsectunhisthcoutuncompoctets.is_set or
                    self.cipsectunhistiketunnelindex.is_set or
                    self.cipsectunhistinauthfails.is_set or
                    self.cipsectunhistinauths.is_set or
                    self.cipsectunhistindecompoctets.is_set or
                    self.cipsectunhistindecompoctwraps.is_set or
                    self.cipsectunhistindecryptfails.is_set or
                    self.cipsectunhistindecrypts.is_set or
                    self.cipsectunhistindroppkts.is_set or
                    self.cipsectunhistinoctets.is_set or
                    self.cipsectunhistinoctwraps.is_set or
                    self.cipsectunhistinpkts.is_set or
                    self.cipsectunhistinreplaydroppkts.is_set or
                    self.cipsectunhistinsaahauthalgo.is_set or
                    self.cipsectunhistinsadecompalgo.is_set or
                    self.cipsectunhistinsadiffhellmangrp.is_set or
                    self.cipsectunhistinsaencryptalgo.is_set or
                    self.cipsectunhistinsaespauthalgo.is_set or
                    self.cipsectunhistkeytype.is_set or
                    self.cipsectunhistlifesize.is_set or
                    self.cipsectunhistlifetime.is_set or
                    self.cipsectunhistlocaladdr.is_set or
                    self.cipsectunhistoutauthfails.is_set or
                    self.cipsectunhistoutauths.is_set or
                    self.cipsectunhistoutdroppkts.is_set or
                    self.cipsectunhistoutencryptfails.is_set or
                    self.cipsectunhistoutencrypts.is_set or
                    self.cipsectunhistoutoctets.is_set or
                    self.cipsectunhistoutoctwraps.is_set or
                    self.cipsectunhistoutpkts.is_set or
                    self.cipsectunhistoutsaahauthalgo.is_set or
                    self.cipsectunhistoutsacompalgo.is_set or
                    self.cipsectunhistoutsadiffhellmangrp.is_set or
                    self.cipsectunhistoutsaencryptalgo.is_set or
                    self.cipsectunhistoutsaespauthalgo.is_set or
                    self.cipsectunhistoutuncompoctets.is_set or
                    self.cipsectunhistoutuncompoctwraps.is_set or
                    self.cipsectunhistremoteaddr.is_set or
                    self.cipsectunhiststarttime.is_set or
                    self.cipsectunhisttermreason.is_set or
                    self.cipsectunhisttotalrefreshes.is_set or
                    self.cipsectunhisttotalsas.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipsectunhistindex.yfilter != YFilter.not_set or
                    self.cipsectunhistactiveindex.yfilter != YFilter.not_set or
                    self.cipsectunhistactivetime.yfilter != YFilter.not_set or
                    self.cipsectunhistencapmode.yfilter != YFilter.not_set or
                    self.cipsectunhisthcindecompoctets.yfilter != YFilter.not_set or
                    self.cipsectunhisthcinoctets.yfilter != YFilter.not_set or
                    self.cipsectunhisthcoutoctets.yfilter != YFilter.not_set or
                    self.cipsectunhisthcoutuncompoctets.yfilter != YFilter.not_set or
                    self.cipsectunhistiketunnelindex.yfilter != YFilter.not_set or
                    self.cipsectunhistinauthfails.yfilter != YFilter.not_set or
                    self.cipsectunhistinauths.yfilter != YFilter.not_set or
                    self.cipsectunhistindecompoctets.yfilter != YFilter.not_set or
                    self.cipsectunhistindecompoctwraps.yfilter != YFilter.not_set or
                    self.cipsectunhistindecryptfails.yfilter != YFilter.not_set or
                    self.cipsectunhistindecrypts.yfilter != YFilter.not_set or
                    self.cipsectunhistindroppkts.yfilter != YFilter.not_set or
                    self.cipsectunhistinoctets.yfilter != YFilter.not_set or
                    self.cipsectunhistinoctwraps.yfilter != YFilter.not_set or
                    self.cipsectunhistinpkts.yfilter != YFilter.not_set or
                    self.cipsectunhistinreplaydroppkts.yfilter != YFilter.not_set or
                    self.cipsectunhistinsaahauthalgo.yfilter != YFilter.not_set or
                    self.cipsectunhistinsadecompalgo.yfilter != YFilter.not_set or
                    self.cipsectunhistinsadiffhellmangrp.yfilter != YFilter.not_set or
                    self.cipsectunhistinsaencryptalgo.yfilter != YFilter.not_set or
                    self.cipsectunhistinsaespauthalgo.yfilter != YFilter.not_set or
                    self.cipsectunhistkeytype.yfilter != YFilter.not_set or
                    self.cipsectunhistlifesize.yfilter != YFilter.not_set or
                    self.cipsectunhistlifetime.yfilter != YFilter.not_set or
                    self.cipsectunhistlocaladdr.yfilter != YFilter.not_set or
                    self.cipsectunhistoutauthfails.yfilter != YFilter.not_set or
                    self.cipsectunhistoutauths.yfilter != YFilter.not_set or
                    self.cipsectunhistoutdroppkts.yfilter != YFilter.not_set or
                    self.cipsectunhistoutencryptfails.yfilter != YFilter.not_set or
                    self.cipsectunhistoutencrypts.yfilter != YFilter.not_set or
                    self.cipsectunhistoutoctets.yfilter != YFilter.not_set or
                    self.cipsectunhistoutoctwraps.yfilter != YFilter.not_set or
                    self.cipsectunhistoutpkts.yfilter != YFilter.not_set or
                    self.cipsectunhistoutsaahauthalgo.yfilter != YFilter.not_set or
                    self.cipsectunhistoutsacompalgo.yfilter != YFilter.not_set or
                    self.cipsectunhistoutsadiffhellmangrp.yfilter != YFilter.not_set or
                    self.cipsectunhistoutsaencryptalgo.yfilter != YFilter.not_set or
                    self.cipsectunhistoutsaespauthalgo.yfilter != YFilter.not_set or
                    self.cipsectunhistoutuncompoctets.yfilter != YFilter.not_set or
                    self.cipsectunhistoutuncompoctwraps.yfilter != YFilter.not_set or
                    self.cipsectunhistremoteaddr.yfilter != YFilter.not_set or
                    self.cipsectunhiststarttime.yfilter != YFilter.not_set or
                    self.cipsectunhisttermreason.yfilter != YFilter.not_set or
                    self.cipsectunhisttotalrefreshes.yfilter != YFilter.not_set or
                    self.cipsectunhisttotalsas.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipSecTunnelHistEntry" + "[cipSecTunHistIndex='" + self.cipsectunhistindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecTunnelHistTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipsectunhistindex.is_set or self.cipsectunhistindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistindex.get_name_leafdata())
                if (self.cipsectunhistactiveindex.is_set or self.cipsectunhistactiveindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistactiveindex.get_name_leafdata())
                if (self.cipsectunhistactivetime.is_set or self.cipsectunhistactivetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistactivetime.get_name_leafdata())
                if (self.cipsectunhistencapmode.is_set or self.cipsectunhistencapmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistencapmode.get_name_leafdata())
                if (self.cipsectunhisthcindecompoctets.is_set or self.cipsectunhisthcindecompoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhisthcindecompoctets.get_name_leafdata())
                if (self.cipsectunhisthcinoctets.is_set or self.cipsectunhisthcinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhisthcinoctets.get_name_leafdata())
                if (self.cipsectunhisthcoutoctets.is_set or self.cipsectunhisthcoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhisthcoutoctets.get_name_leafdata())
                if (self.cipsectunhisthcoutuncompoctets.is_set or self.cipsectunhisthcoutuncompoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhisthcoutuncompoctets.get_name_leafdata())
                if (self.cipsectunhistiketunnelindex.is_set or self.cipsectunhistiketunnelindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistiketunnelindex.get_name_leafdata())
                if (self.cipsectunhistinauthfails.is_set or self.cipsectunhistinauthfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistinauthfails.get_name_leafdata())
                if (self.cipsectunhistinauths.is_set or self.cipsectunhistinauths.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistinauths.get_name_leafdata())
                if (self.cipsectunhistindecompoctets.is_set or self.cipsectunhistindecompoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistindecompoctets.get_name_leafdata())
                if (self.cipsectunhistindecompoctwraps.is_set or self.cipsectunhistindecompoctwraps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistindecompoctwraps.get_name_leafdata())
                if (self.cipsectunhistindecryptfails.is_set or self.cipsectunhistindecryptfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistindecryptfails.get_name_leafdata())
                if (self.cipsectunhistindecrypts.is_set or self.cipsectunhistindecrypts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistindecrypts.get_name_leafdata())
                if (self.cipsectunhistindroppkts.is_set or self.cipsectunhistindroppkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistindroppkts.get_name_leafdata())
                if (self.cipsectunhistinoctets.is_set or self.cipsectunhistinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistinoctets.get_name_leafdata())
                if (self.cipsectunhistinoctwraps.is_set or self.cipsectunhistinoctwraps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistinoctwraps.get_name_leafdata())
                if (self.cipsectunhistinpkts.is_set or self.cipsectunhistinpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistinpkts.get_name_leafdata())
                if (self.cipsectunhistinreplaydroppkts.is_set or self.cipsectunhistinreplaydroppkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistinreplaydroppkts.get_name_leafdata())
                if (self.cipsectunhistinsaahauthalgo.is_set or self.cipsectunhistinsaahauthalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistinsaahauthalgo.get_name_leafdata())
                if (self.cipsectunhistinsadecompalgo.is_set or self.cipsectunhistinsadecompalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistinsadecompalgo.get_name_leafdata())
                if (self.cipsectunhistinsadiffhellmangrp.is_set or self.cipsectunhistinsadiffhellmangrp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistinsadiffhellmangrp.get_name_leafdata())
                if (self.cipsectunhistinsaencryptalgo.is_set or self.cipsectunhistinsaencryptalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistinsaencryptalgo.get_name_leafdata())
                if (self.cipsectunhistinsaespauthalgo.is_set or self.cipsectunhistinsaespauthalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistinsaespauthalgo.get_name_leafdata())
                if (self.cipsectunhistkeytype.is_set or self.cipsectunhistkeytype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistkeytype.get_name_leafdata())
                if (self.cipsectunhistlifesize.is_set or self.cipsectunhistlifesize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistlifesize.get_name_leafdata())
                if (self.cipsectunhistlifetime.is_set or self.cipsectunhistlifetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistlifetime.get_name_leafdata())
                if (self.cipsectunhistlocaladdr.is_set or self.cipsectunhistlocaladdr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistlocaladdr.get_name_leafdata())
                if (self.cipsectunhistoutauthfails.is_set or self.cipsectunhistoutauthfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistoutauthfails.get_name_leafdata())
                if (self.cipsectunhistoutauths.is_set or self.cipsectunhistoutauths.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistoutauths.get_name_leafdata())
                if (self.cipsectunhistoutdroppkts.is_set or self.cipsectunhistoutdroppkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistoutdroppkts.get_name_leafdata())
                if (self.cipsectunhistoutencryptfails.is_set or self.cipsectunhistoutencryptfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistoutencryptfails.get_name_leafdata())
                if (self.cipsectunhistoutencrypts.is_set or self.cipsectunhistoutencrypts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistoutencrypts.get_name_leafdata())
                if (self.cipsectunhistoutoctets.is_set or self.cipsectunhistoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistoutoctets.get_name_leafdata())
                if (self.cipsectunhistoutoctwraps.is_set or self.cipsectunhistoutoctwraps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistoutoctwraps.get_name_leafdata())
                if (self.cipsectunhistoutpkts.is_set or self.cipsectunhistoutpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistoutpkts.get_name_leafdata())
                if (self.cipsectunhistoutsaahauthalgo.is_set or self.cipsectunhistoutsaahauthalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistoutsaahauthalgo.get_name_leafdata())
                if (self.cipsectunhistoutsacompalgo.is_set or self.cipsectunhistoutsacompalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistoutsacompalgo.get_name_leafdata())
                if (self.cipsectunhistoutsadiffhellmangrp.is_set or self.cipsectunhistoutsadiffhellmangrp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistoutsadiffhellmangrp.get_name_leafdata())
                if (self.cipsectunhistoutsaencryptalgo.is_set or self.cipsectunhistoutsaencryptalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistoutsaencryptalgo.get_name_leafdata())
                if (self.cipsectunhistoutsaespauthalgo.is_set or self.cipsectunhistoutsaespauthalgo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistoutsaespauthalgo.get_name_leafdata())
                if (self.cipsectunhistoutuncompoctets.is_set or self.cipsectunhistoutuncompoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistoutuncompoctets.get_name_leafdata())
                if (self.cipsectunhistoutuncompoctwraps.is_set or self.cipsectunhistoutuncompoctwraps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistoutuncompoctwraps.get_name_leafdata())
                if (self.cipsectunhistremoteaddr.is_set or self.cipsectunhistremoteaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhistremoteaddr.get_name_leafdata())
                if (self.cipsectunhiststarttime.is_set or self.cipsectunhiststarttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhiststarttime.get_name_leafdata())
                if (self.cipsectunhisttermreason.is_set or self.cipsectunhisttermreason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhisttermreason.get_name_leafdata())
                if (self.cipsectunhisttotalrefreshes.is_set or self.cipsectunhisttotalrefreshes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhisttotalrefreshes.get_name_leafdata())
                if (self.cipsectunhisttotalsas.is_set or self.cipsectunhisttotalsas.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsectunhisttotalsas.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipSecTunHistIndex" or name == "cipSecTunHistActiveIndex" or name == "cipSecTunHistActiveTime" or name == "cipSecTunHistEncapMode" or name == "cipSecTunHistHcInDecompOctets" or name == "cipSecTunHistHcInOctets" or name == "cipSecTunHistHcOutOctets" or name == "cipSecTunHistHcOutUncompOctets" or name == "cipSecTunHistIkeTunnelIndex" or name == "cipSecTunHistInAuthFails" or name == "cipSecTunHistInAuths" or name == "cipSecTunHistInDecompOctets" or name == "cipSecTunHistInDecompOctWraps" or name == "cipSecTunHistInDecryptFails" or name == "cipSecTunHistInDecrypts" or name == "cipSecTunHistInDropPkts" or name == "cipSecTunHistInOctets" or name == "cipSecTunHistInOctWraps" or name == "cipSecTunHistInPkts" or name == "cipSecTunHistInReplayDropPkts" or name == "cipSecTunHistInSaAhAuthAlgo" or name == "cipSecTunHistInSaDecompAlgo" or name == "cipSecTunHistInSaDiffHellmanGrp" or name == "cipSecTunHistInSaEncryptAlgo" or name == "cipSecTunHistInSaEspAuthAlgo" or name == "cipSecTunHistKeyType" or name == "cipSecTunHistLifeSize" or name == "cipSecTunHistLifeTime" or name == "cipSecTunHistLocalAddr" or name == "cipSecTunHistOutAuthFails" or name == "cipSecTunHistOutAuths" or name == "cipSecTunHistOutDropPkts" or name == "cipSecTunHistOutEncryptFails" or name == "cipSecTunHistOutEncrypts" or name == "cipSecTunHistOutOctets" or name == "cipSecTunHistOutOctWraps" or name == "cipSecTunHistOutPkts" or name == "cipSecTunHistOutSaAhAuthAlgo" or name == "cipSecTunHistOutSaCompAlgo" or name == "cipSecTunHistOutSaDiffHellmanGrp" or name == "cipSecTunHistOutSaEncryptAlgo" or name == "cipSecTunHistOutSaEspAuthAlgo" or name == "cipSecTunHistOutUncompOctets" or name == "cipSecTunHistOutUncompOctWraps" or name == "cipSecTunHistRemoteAddr" or name == "cipSecTunHistStartTime" or name == "cipSecTunHistTermReason" or name == "cipSecTunHistTotalRefreshes" or name == "cipSecTunHistTotalSas"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipSecTunHistIndex"):
                    self.cipsectunhistindex = value
                    self.cipsectunhistindex.value_namespace = name_space
                    self.cipsectunhistindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistActiveIndex"):
                    self.cipsectunhistactiveindex = value
                    self.cipsectunhistactiveindex.value_namespace = name_space
                    self.cipsectunhistactiveindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistActiveTime"):
                    self.cipsectunhistactivetime = value
                    self.cipsectunhistactivetime.value_namespace = name_space
                    self.cipsectunhistactivetime.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistEncapMode"):
                    self.cipsectunhistencapmode = value
                    self.cipsectunhistencapmode.value_namespace = name_space
                    self.cipsectunhistencapmode.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistHcInDecompOctets"):
                    self.cipsectunhisthcindecompoctets = value
                    self.cipsectunhisthcindecompoctets.value_namespace = name_space
                    self.cipsectunhisthcindecompoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistHcInOctets"):
                    self.cipsectunhisthcinoctets = value
                    self.cipsectunhisthcinoctets.value_namespace = name_space
                    self.cipsectunhisthcinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistHcOutOctets"):
                    self.cipsectunhisthcoutoctets = value
                    self.cipsectunhisthcoutoctets.value_namespace = name_space
                    self.cipsectunhisthcoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistHcOutUncompOctets"):
                    self.cipsectunhisthcoutuncompoctets = value
                    self.cipsectunhisthcoutuncompoctets.value_namespace = name_space
                    self.cipsectunhisthcoutuncompoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistIkeTunnelIndex"):
                    self.cipsectunhistiketunnelindex = value
                    self.cipsectunhistiketunnelindex.value_namespace = name_space
                    self.cipsectunhistiketunnelindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistInAuthFails"):
                    self.cipsectunhistinauthfails = value
                    self.cipsectunhistinauthfails.value_namespace = name_space
                    self.cipsectunhistinauthfails.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistInAuths"):
                    self.cipsectunhistinauths = value
                    self.cipsectunhistinauths.value_namespace = name_space
                    self.cipsectunhistinauths.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistInDecompOctets"):
                    self.cipsectunhistindecompoctets = value
                    self.cipsectunhistindecompoctets.value_namespace = name_space
                    self.cipsectunhistindecompoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistInDecompOctWraps"):
                    self.cipsectunhistindecompoctwraps = value
                    self.cipsectunhistindecompoctwraps.value_namespace = name_space
                    self.cipsectunhistindecompoctwraps.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistInDecryptFails"):
                    self.cipsectunhistindecryptfails = value
                    self.cipsectunhistindecryptfails.value_namespace = name_space
                    self.cipsectunhistindecryptfails.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistInDecrypts"):
                    self.cipsectunhistindecrypts = value
                    self.cipsectunhistindecrypts.value_namespace = name_space
                    self.cipsectunhistindecrypts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistInDropPkts"):
                    self.cipsectunhistindroppkts = value
                    self.cipsectunhistindroppkts.value_namespace = name_space
                    self.cipsectunhistindroppkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistInOctets"):
                    self.cipsectunhistinoctets = value
                    self.cipsectunhistinoctets.value_namespace = name_space
                    self.cipsectunhistinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistInOctWraps"):
                    self.cipsectunhistinoctwraps = value
                    self.cipsectunhistinoctwraps.value_namespace = name_space
                    self.cipsectunhistinoctwraps.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistInPkts"):
                    self.cipsectunhistinpkts = value
                    self.cipsectunhistinpkts.value_namespace = name_space
                    self.cipsectunhistinpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistInReplayDropPkts"):
                    self.cipsectunhistinreplaydroppkts = value
                    self.cipsectunhistinreplaydroppkts.value_namespace = name_space
                    self.cipsectunhistinreplaydroppkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistInSaAhAuthAlgo"):
                    self.cipsectunhistinsaahauthalgo = value
                    self.cipsectunhistinsaahauthalgo.value_namespace = name_space
                    self.cipsectunhistinsaahauthalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistInSaDecompAlgo"):
                    self.cipsectunhistinsadecompalgo = value
                    self.cipsectunhistinsadecompalgo.value_namespace = name_space
                    self.cipsectunhistinsadecompalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistInSaDiffHellmanGrp"):
                    self.cipsectunhistinsadiffhellmangrp = value
                    self.cipsectunhistinsadiffhellmangrp.value_namespace = name_space
                    self.cipsectunhistinsadiffhellmangrp.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistInSaEncryptAlgo"):
                    self.cipsectunhistinsaencryptalgo = value
                    self.cipsectunhistinsaencryptalgo.value_namespace = name_space
                    self.cipsectunhistinsaencryptalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistInSaEspAuthAlgo"):
                    self.cipsectunhistinsaespauthalgo = value
                    self.cipsectunhistinsaespauthalgo.value_namespace = name_space
                    self.cipsectunhistinsaespauthalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistKeyType"):
                    self.cipsectunhistkeytype = value
                    self.cipsectunhistkeytype.value_namespace = name_space
                    self.cipsectunhistkeytype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistLifeSize"):
                    self.cipsectunhistlifesize = value
                    self.cipsectunhistlifesize.value_namespace = name_space
                    self.cipsectunhistlifesize.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistLifeTime"):
                    self.cipsectunhistlifetime = value
                    self.cipsectunhistlifetime.value_namespace = name_space
                    self.cipsectunhistlifetime.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistLocalAddr"):
                    self.cipsectunhistlocaladdr = value
                    self.cipsectunhistlocaladdr.value_namespace = name_space
                    self.cipsectunhistlocaladdr.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistOutAuthFails"):
                    self.cipsectunhistoutauthfails = value
                    self.cipsectunhistoutauthfails.value_namespace = name_space
                    self.cipsectunhistoutauthfails.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistOutAuths"):
                    self.cipsectunhistoutauths = value
                    self.cipsectunhistoutauths.value_namespace = name_space
                    self.cipsectunhistoutauths.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistOutDropPkts"):
                    self.cipsectunhistoutdroppkts = value
                    self.cipsectunhistoutdroppkts.value_namespace = name_space
                    self.cipsectunhistoutdroppkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistOutEncryptFails"):
                    self.cipsectunhistoutencryptfails = value
                    self.cipsectunhistoutencryptfails.value_namespace = name_space
                    self.cipsectunhistoutencryptfails.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistOutEncrypts"):
                    self.cipsectunhistoutencrypts = value
                    self.cipsectunhistoutencrypts.value_namespace = name_space
                    self.cipsectunhistoutencrypts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistOutOctets"):
                    self.cipsectunhistoutoctets = value
                    self.cipsectunhistoutoctets.value_namespace = name_space
                    self.cipsectunhistoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistOutOctWraps"):
                    self.cipsectunhistoutoctwraps = value
                    self.cipsectunhistoutoctwraps.value_namespace = name_space
                    self.cipsectunhistoutoctwraps.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistOutPkts"):
                    self.cipsectunhistoutpkts = value
                    self.cipsectunhistoutpkts.value_namespace = name_space
                    self.cipsectunhistoutpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistOutSaAhAuthAlgo"):
                    self.cipsectunhistoutsaahauthalgo = value
                    self.cipsectunhistoutsaahauthalgo.value_namespace = name_space
                    self.cipsectunhistoutsaahauthalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistOutSaCompAlgo"):
                    self.cipsectunhistoutsacompalgo = value
                    self.cipsectunhistoutsacompalgo.value_namespace = name_space
                    self.cipsectunhistoutsacompalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistOutSaDiffHellmanGrp"):
                    self.cipsectunhistoutsadiffhellmangrp = value
                    self.cipsectunhistoutsadiffhellmangrp.value_namespace = name_space
                    self.cipsectunhistoutsadiffhellmangrp.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistOutSaEncryptAlgo"):
                    self.cipsectunhistoutsaencryptalgo = value
                    self.cipsectunhistoutsaencryptalgo.value_namespace = name_space
                    self.cipsectunhistoutsaencryptalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistOutSaEspAuthAlgo"):
                    self.cipsectunhistoutsaespauthalgo = value
                    self.cipsectunhistoutsaespauthalgo.value_namespace = name_space
                    self.cipsectunhistoutsaespauthalgo.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistOutUncompOctets"):
                    self.cipsectunhistoutuncompoctets = value
                    self.cipsectunhistoutuncompoctets.value_namespace = name_space
                    self.cipsectunhistoutuncompoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistOutUncompOctWraps"):
                    self.cipsectunhistoutuncompoctwraps = value
                    self.cipsectunhistoutuncompoctwraps.value_namespace = name_space
                    self.cipsectunhistoutuncompoctwraps.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistRemoteAddr"):
                    self.cipsectunhistremoteaddr = value
                    self.cipsectunhistremoteaddr.value_namespace = name_space
                    self.cipsectunhistremoteaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistStartTime"):
                    self.cipsectunhiststarttime = value
                    self.cipsectunhiststarttime.value_namespace = name_space
                    self.cipsectunhiststarttime.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistTermReason"):
                    self.cipsectunhisttermreason = value
                    self.cipsectunhisttermreason.value_namespace = name_space
                    self.cipsectunhisttermreason.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistTotalRefreshes"):
                    self.cipsectunhisttotalrefreshes = value
                    self.cipsectunhisttotalrefreshes.value_namespace = name_space
                    self.cipsectunhisttotalrefreshes.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecTunHistTotalSas"):
                    self.cipsectunhisttotalsas = value
                    self.cipsectunhisttotalsas.value_namespace = name_space
                    self.cipsectunhisttotalsas.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipsectunnelhistentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipsectunnelhistentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipSecTunnelHistTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipSecTunnelHistEntry"):
                for c in self.cipsectunnelhistentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecFlowMonitorMib.Cipsectunnelhisttable.Cipsectunnelhistentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipsectunnelhistentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipSecTunnelHistEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cipsecendpthistentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecendpthisttable.Cipsecendpthistentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CiscoIpsecFlowMonitorMib.Cipsecendpthisttable, self).__init__()

            self.yang_name = "cipSecEndPtHistTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

            self.cipsecendpthistentry = YList(self)

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
                        super(CiscoIpsecFlowMonitorMib.Cipsecendpthisttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Cipsecendpthisttable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Endpttype <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Endpttype>`
            
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
            	**type**\:   :py:class:`Endpttype <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Endpttype>`
            
            .. attribute:: cipsecendpthisttunindex
            
            	The index  of the previously active IPsec Phase\-2 Tunnel Table
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                super(CiscoIpsecFlowMonitorMib.Cipsecendpthisttable.Cipsecendpthistentry, self).__init__()

                self.yang_name = "cipSecEndPtHistEntry"
                self.yang_parent_name = "cipSecEndPtHistTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipsecendpthistindex",
                                "cipsecendpthistactiveindex",
                                "cipsecendpthistlocaladdr1",
                                "cipsecendpthistlocaladdr2",
                                "cipsecendpthistlocalname",
                                "cipsecendpthistlocalport",
                                "cipsecendpthistlocalprotocol",
                                "cipsecendpthistlocaltype",
                                "cipsecendpthistremoteaddr1",
                                "cipsecendpthistremoteaddr2",
                                "cipsecendpthistremotename",
                                "cipsecendpthistremoteport",
                                "cipsecendpthistremoteprotocol",
                                "cipsecendpthistremotetype",
                                "cipsecendpthisttunindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecFlowMonitorMib.Cipsecendpthisttable.Cipsecendpthistentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecFlowMonitorMib.Cipsecendpthisttable.Cipsecendpthistentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cipsecendpthistindex.is_set or
                    self.cipsecendpthistactiveindex.is_set or
                    self.cipsecendpthistlocaladdr1.is_set or
                    self.cipsecendpthistlocaladdr2.is_set or
                    self.cipsecendpthistlocalname.is_set or
                    self.cipsecendpthistlocalport.is_set or
                    self.cipsecendpthistlocalprotocol.is_set or
                    self.cipsecendpthistlocaltype.is_set or
                    self.cipsecendpthistremoteaddr1.is_set or
                    self.cipsecendpthistremoteaddr2.is_set or
                    self.cipsecendpthistremotename.is_set or
                    self.cipsecendpthistremoteport.is_set or
                    self.cipsecendpthistremoteprotocol.is_set or
                    self.cipsecendpthistremotetype.is_set or
                    self.cipsecendpthisttunindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipsecendpthistindex.yfilter != YFilter.not_set or
                    self.cipsecendpthistactiveindex.yfilter != YFilter.not_set or
                    self.cipsecendpthistlocaladdr1.yfilter != YFilter.not_set or
                    self.cipsecendpthistlocaladdr2.yfilter != YFilter.not_set or
                    self.cipsecendpthistlocalname.yfilter != YFilter.not_set or
                    self.cipsecendpthistlocalport.yfilter != YFilter.not_set or
                    self.cipsecendpthistlocalprotocol.yfilter != YFilter.not_set or
                    self.cipsecendpthistlocaltype.yfilter != YFilter.not_set or
                    self.cipsecendpthistremoteaddr1.yfilter != YFilter.not_set or
                    self.cipsecendpthistremoteaddr2.yfilter != YFilter.not_set or
                    self.cipsecendpthistremotename.yfilter != YFilter.not_set or
                    self.cipsecendpthistremoteport.yfilter != YFilter.not_set or
                    self.cipsecendpthistremoteprotocol.yfilter != YFilter.not_set or
                    self.cipsecendpthistremotetype.yfilter != YFilter.not_set or
                    self.cipsecendpthisttunindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipSecEndPtHistEntry" + "[cipSecEndPtHistIndex='" + self.cipsecendpthistindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecEndPtHistTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipsecendpthistindex.is_set or self.cipsecendpthistindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendpthistindex.get_name_leafdata())
                if (self.cipsecendpthistactiveindex.is_set or self.cipsecendpthistactiveindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendpthistactiveindex.get_name_leafdata())
                if (self.cipsecendpthistlocaladdr1.is_set or self.cipsecendpthistlocaladdr1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendpthistlocaladdr1.get_name_leafdata())
                if (self.cipsecendpthistlocaladdr2.is_set or self.cipsecendpthistlocaladdr2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendpthistlocaladdr2.get_name_leafdata())
                if (self.cipsecendpthistlocalname.is_set or self.cipsecendpthistlocalname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendpthistlocalname.get_name_leafdata())
                if (self.cipsecendpthistlocalport.is_set or self.cipsecendpthistlocalport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendpthistlocalport.get_name_leafdata())
                if (self.cipsecendpthistlocalprotocol.is_set or self.cipsecendpthistlocalprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendpthistlocalprotocol.get_name_leafdata())
                if (self.cipsecendpthistlocaltype.is_set or self.cipsecendpthistlocaltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendpthistlocaltype.get_name_leafdata())
                if (self.cipsecendpthistremoteaddr1.is_set or self.cipsecendpthistremoteaddr1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendpthistremoteaddr1.get_name_leafdata())
                if (self.cipsecendpthistremoteaddr2.is_set or self.cipsecendpthistremoteaddr2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendpthistremoteaddr2.get_name_leafdata())
                if (self.cipsecendpthistremotename.is_set or self.cipsecendpthistremotename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendpthistremotename.get_name_leafdata())
                if (self.cipsecendpthistremoteport.is_set or self.cipsecendpthistremoteport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendpthistremoteport.get_name_leafdata())
                if (self.cipsecendpthistremoteprotocol.is_set or self.cipsecendpthistremoteprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendpthistremoteprotocol.get_name_leafdata())
                if (self.cipsecendpthistremotetype.is_set or self.cipsecendpthistremotetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendpthistremotetype.get_name_leafdata())
                if (self.cipsecendpthisttunindex.is_set or self.cipsecendpthisttunindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecendpthisttunindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipSecEndPtHistIndex" or name == "cipSecEndPtHistActiveIndex" or name == "cipSecEndPtHistLocalAddr1" or name == "cipSecEndPtHistLocalAddr2" or name == "cipSecEndPtHistLocalName" or name == "cipSecEndPtHistLocalPort" or name == "cipSecEndPtHistLocalProtocol" or name == "cipSecEndPtHistLocalType" or name == "cipSecEndPtHistRemoteAddr1" or name == "cipSecEndPtHistRemoteAddr2" or name == "cipSecEndPtHistRemoteName" or name == "cipSecEndPtHistRemotePort" or name == "cipSecEndPtHistRemoteProtocol" or name == "cipSecEndPtHistRemoteType" or name == "cipSecEndPtHistTunIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipSecEndPtHistIndex"):
                    self.cipsecendpthistindex = value
                    self.cipsecendpthistindex.value_namespace = name_space
                    self.cipsecendpthistindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtHistActiveIndex"):
                    self.cipsecendpthistactiveindex = value
                    self.cipsecendpthistactiveindex.value_namespace = name_space
                    self.cipsecendpthistactiveindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtHistLocalAddr1"):
                    self.cipsecendpthistlocaladdr1 = value
                    self.cipsecendpthistlocaladdr1.value_namespace = name_space
                    self.cipsecendpthistlocaladdr1.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtHistLocalAddr2"):
                    self.cipsecendpthistlocaladdr2 = value
                    self.cipsecendpthistlocaladdr2.value_namespace = name_space
                    self.cipsecendpthistlocaladdr2.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtHistLocalName"):
                    self.cipsecendpthistlocalname = value
                    self.cipsecendpthistlocalname.value_namespace = name_space
                    self.cipsecendpthistlocalname.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtHistLocalPort"):
                    self.cipsecendpthistlocalport = value
                    self.cipsecendpthistlocalport.value_namespace = name_space
                    self.cipsecendpthistlocalport.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtHistLocalProtocol"):
                    self.cipsecendpthistlocalprotocol = value
                    self.cipsecendpthistlocalprotocol.value_namespace = name_space
                    self.cipsecendpthistlocalprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtHistLocalType"):
                    self.cipsecendpthistlocaltype = value
                    self.cipsecendpthistlocaltype.value_namespace = name_space
                    self.cipsecendpthistlocaltype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtHistRemoteAddr1"):
                    self.cipsecendpthistremoteaddr1 = value
                    self.cipsecendpthistremoteaddr1.value_namespace = name_space
                    self.cipsecendpthistremoteaddr1.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtHistRemoteAddr2"):
                    self.cipsecendpthistremoteaddr2 = value
                    self.cipsecendpthistremoteaddr2.value_namespace = name_space
                    self.cipsecendpthistremoteaddr2.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtHistRemoteName"):
                    self.cipsecendpthistremotename = value
                    self.cipsecendpthistremotename.value_namespace = name_space
                    self.cipsecendpthistremotename.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtHistRemotePort"):
                    self.cipsecendpthistremoteport = value
                    self.cipsecendpthistremoteport.value_namespace = name_space
                    self.cipsecendpthistremoteport.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtHistRemoteProtocol"):
                    self.cipsecendpthistremoteprotocol = value
                    self.cipsecendpthistremoteprotocol.value_namespace = name_space
                    self.cipsecendpthistremoteprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtHistRemoteType"):
                    self.cipsecendpthistremotetype = value
                    self.cipsecendpthistremotetype.value_namespace = name_space
                    self.cipsecendpthistremotetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecEndPtHistTunIndex"):
                    self.cipsecendpthisttunindex = value
                    self.cipsecendpthisttunindex.value_namespace = name_space
                    self.cipsecendpthisttunindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipsecendpthistentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipsecendpthistentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipSecEndPtHistTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipSecEndPtHistEntry"):
                for c in self.cipsecendpthistentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecFlowMonitorMib.Cipsecendpthisttable.Cipsecendpthistentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipsecendpthistentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipSecEndPtHistEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cikefailtable(Entity):
        """
        The IPsec Phase\-1 Failure Table.
        This table is implemented as a sliding 
        window in which only the last n entries are 
        maintained.  The maximum number of entries
        is specified by the cipSecFailTableSize object.
        
        .. attribute:: cikefailentry
        
        	Each entry contains the attributes associated with  an IPsec Phase\-1 failure
        	**type**\: list of    :py:class:`Cikefailentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cikefailtable.Cikefailentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CiscoIpsecFlowMonitorMib.Cikefailtable, self).__init__()

            self.yang_name = "cikeFailTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

            self.cikefailentry = YList(self)

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
                        super(CiscoIpsecFlowMonitorMib.Cikefailtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Cikefailtable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Ikepeertype <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Ikepeertype>`
            
            .. attribute:: cikefaillocalvalue
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\:  str
            
            .. attribute:: cikefailreason
            
            	The reason for the failure.  Possible reasons include\: 1 = other 2 = peer delete request was received 3 = contact with peer was lost 4 = local failure occurred 5 = authentication failure 6 = hash validation failure 7 = encryption failure 8 = internal error occurred 9 = system capacity failure 10 = proposal failure 11 = peer's certificate is unavailable 12 = peer's certificate was found invalid 13 = local certificate expired 14 = certificate revoke list (crl) failure 15 = peer encoding error 16 = non\-existent security association 17 = operator requested termination
            	**type**\:   :py:class:`Cikefailreason <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cikefailtable.Cikefailentry.Cikefailreason>`
            
            .. attribute:: cikefailremoteaddr
            
            	The IP address of the remote peer
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cikefailremotetype
            
            	The type of remote peer identity.  The remote peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\:   :py:class:`Ikepeertype <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.Ikepeertype>`
            
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
                super(CiscoIpsecFlowMonitorMib.Cikefailtable.Cikefailentry, self).__init__()

                self.yang_name = "cikeFailEntry"
                self.yang_parent_name = "cikeFailTable"

                self.cikefailindex = YLeaf(YType.int32, "cikeFailIndex")

                self.cikefaillocaladdr = YLeaf(YType.str, "cikeFailLocalAddr")

                self.cikefaillocaltype = YLeaf(YType.enumeration, "cikeFailLocalType")

                self.cikefaillocalvalue = YLeaf(YType.str, "cikeFailLocalValue")

                self.cikefailreason = YLeaf(YType.enumeration, "cikeFailReason")

                self.cikefailremoteaddr = YLeaf(YType.str, "cikeFailRemoteAddr")

                self.cikefailremotetype = YLeaf(YType.enumeration, "cikeFailRemoteType")

                self.cikefailremotevalue = YLeaf(YType.str, "cikeFailRemoteValue")

                self.cikefailtime = YLeaf(YType.uint32, "cikeFailTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cikefailindex",
                                "cikefaillocaladdr",
                                "cikefaillocaltype",
                                "cikefaillocalvalue",
                                "cikefailreason",
                                "cikefailremoteaddr",
                                "cikefailremotetype",
                                "cikefailremotevalue",
                                "cikefailtime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecFlowMonitorMib.Cikefailtable.Cikefailentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecFlowMonitorMib.Cikefailtable.Cikefailentry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.cikefailindex.is_set or
                    self.cikefaillocaladdr.is_set or
                    self.cikefaillocaltype.is_set or
                    self.cikefaillocalvalue.is_set or
                    self.cikefailreason.is_set or
                    self.cikefailremoteaddr.is_set or
                    self.cikefailremotetype.is_set or
                    self.cikefailremotevalue.is_set or
                    self.cikefailtime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cikefailindex.yfilter != YFilter.not_set or
                    self.cikefaillocaladdr.yfilter != YFilter.not_set or
                    self.cikefaillocaltype.yfilter != YFilter.not_set or
                    self.cikefaillocalvalue.yfilter != YFilter.not_set or
                    self.cikefailreason.yfilter != YFilter.not_set or
                    self.cikefailremoteaddr.yfilter != YFilter.not_set or
                    self.cikefailremotetype.yfilter != YFilter.not_set or
                    self.cikefailremotevalue.yfilter != YFilter.not_set or
                    self.cikefailtime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cikeFailEntry" + "[cikeFailIndex='" + self.cikefailindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cikeFailTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cikefailindex.is_set or self.cikefailindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikefailindex.get_name_leafdata())
                if (self.cikefaillocaladdr.is_set or self.cikefaillocaladdr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikefaillocaladdr.get_name_leafdata())
                if (self.cikefaillocaltype.is_set or self.cikefaillocaltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikefaillocaltype.get_name_leafdata())
                if (self.cikefaillocalvalue.is_set or self.cikefaillocalvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikefaillocalvalue.get_name_leafdata())
                if (self.cikefailreason.is_set or self.cikefailreason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikefailreason.get_name_leafdata())
                if (self.cikefailremoteaddr.is_set or self.cikefailremoteaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikefailremoteaddr.get_name_leafdata())
                if (self.cikefailremotetype.is_set or self.cikefailremotetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikefailremotetype.get_name_leafdata())
                if (self.cikefailremotevalue.is_set or self.cikefailremotevalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikefailremotevalue.get_name_leafdata())
                if (self.cikefailtime.is_set or self.cikefailtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cikefailtime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cikeFailIndex" or name == "cikeFailLocalAddr" or name == "cikeFailLocalType" or name == "cikeFailLocalValue" or name == "cikeFailReason" or name == "cikeFailRemoteAddr" or name == "cikeFailRemoteType" or name == "cikeFailRemoteValue" or name == "cikeFailTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cikeFailIndex"):
                    self.cikefailindex = value
                    self.cikefailindex.value_namespace = name_space
                    self.cikefailindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeFailLocalAddr"):
                    self.cikefaillocaladdr = value
                    self.cikefaillocaladdr.value_namespace = name_space
                    self.cikefaillocaladdr.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeFailLocalType"):
                    self.cikefaillocaltype = value
                    self.cikefaillocaltype.value_namespace = name_space
                    self.cikefaillocaltype.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeFailLocalValue"):
                    self.cikefaillocalvalue = value
                    self.cikefaillocalvalue.value_namespace = name_space
                    self.cikefaillocalvalue.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeFailReason"):
                    self.cikefailreason = value
                    self.cikefailreason.value_namespace = name_space
                    self.cikefailreason.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeFailRemoteAddr"):
                    self.cikefailremoteaddr = value
                    self.cikefailremoteaddr.value_namespace = name_space
                    self.cikefailremoteaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeFailRemoteType"):
                    self.cikefailremotetype = value
                    self.cikefailremotetype.value_namespace = name_space
                    self.cikefailremotetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeFailRemoteValue"):
                    self.cikefailremotevalue = value
                    self.cikefailremotevalue.value_namespace = name_space
                    self.cikefailremotevalue.value_namespace_prefix = name_space_prefix
                if(value_path == "cikeFailTime"):
                    self.cikefailtime = value
                    self.cikefailtime.value_namespace = name_space
                    self.cikefailtime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cikefailentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cikefailentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cikeFailTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cikeFailEntry"):
                for c in self.cikefailentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecFlowMonitorMib.Cikefailtable.Cikefailentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cikefailentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cikeFailEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cipsecfailtable(Entity):
        """
        The IPsec Phase\-2 Failure Table.
        This table is implemented as a sliding window 
        in which only the last n entries are maintained.  
        The maximum number of entries
        is specified by the cipSecFailTableSize object.
        
        .. attribute:: cipsecfailentry
        
        	Each entry contains the attributes associated with an IPsec Phase\-1 failure
        	**type**\: list of    :py:class:`Cipsecfailentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecfailtable.Cipsecfailentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            super(CiscoIpsecFlowMonitorMib.Cipsecfailtable, self).__init__()

            self.yang_name = "cipSecFailTable"
            self.yang_parent_name = "CISCO-IPSEC-FLOW-MONITOR-MIB"

            self.cipsecfailentry = YList(self)

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
                        super(CiscoIpsecFlowMonitorMib.Cipsecfailtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecFlowMonitorMib.Cipsecfailtable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Cipsecfailreason <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecfailtable.Cipsecfailentry.Cipsecfailreason>`
            
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
                super(CiscoIpsecFlowMonitorMib.Cipsecfailtable.Cipsecfailentry, self).__init__()

                self.yang_name = "cipSecFailEntry"
                self.yang_parent_name = "cipSecFailTable"

                self.cipsecfailindex = YLeaf(YType.int32, "cipSecFailIndex")

                self.cipsecfailpktdstaddr = YLeaf(YType.str, "cipSecFailPktDstAddr")

                self.cipsecfailpktsrcaddr = YLeaf(YType.str, "cipSecFailPktSrcAddr")

                self.cipsecfailreason = YLeaf(YType.enumeration, "cipSecFailReason")

                self.cipsecfailsaspi = YLeaf(YType.int32, "cipSecFailSaSpi")

                self.cipsecfailtime = YLeaf(YType.uint32, "cipSecFailTime")

                self.cipsecfailtunnelindex = YLeaf(YType.int32, "cipSecFailTunnelIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipsecfailindex",
                                "cipsecfailpktdstaddr",
                                "cipsecfailpktsrcaddr",
                                "cipsecfailreason",
                                "cipsecfailsaspi",
                                "cipsecfailtime",
                                "cipsecfailtunnelindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecFlowMonitorMib.Cipsecfailtable.Cipsecfailentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecFlowMonitorMib.Cipsecfailtable.Cipsecfailentry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.cipsecfailindex.is_set or
                    self.cipsecfailpktdstaddr.is_set or
                    self.cipsecfailpktsrcaddr.is_set or
                    self.cipsecfailreason.is_set or
                    self.cipsecfailsaspi.is_set or
                    self.cipsecfailtime.is_set or
                    self.cipsecfailtunnelindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipsecfailindex.yfilter != YFilter.not_set or
                    self.cipsecfailpktdstaddr.yfilter != YFilter.not_set or
                    self.cipsecfailpktsrcaddr.yfilter != YFilter.not_set or
                    self.cipsecfailreason.yfilter != YFilter.not_set or
                    self.cipsecfailsaspi.yfilter != YFilter.not_set or
                    self.cipsecfailtime.yfilter != YFilter.not_set or
                    self.cipsecfailtunnelindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipSecFailEntry" + "[cipSecFailIndex='" + self.cipsecfailindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/cipSecFailTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipsecfailindex.is_set or self.cipsecfailindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecfailindex.get_name_leafdata())
                if (self.cipsecfailpktdstaddr.is_set or self.cipsecfailpktdstaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecfailpktdstaddr.get_name_leafdata())
                if (self.cipsecfailpktsrcaddr.is_set or self.cipsecfailpktsrcaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecfailpktsrcaddr.get_name_leafdata())
                if (self.cipsecfailreason.is_set or self.cipsecfailreason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecfailreason.get_name_leafdata())
                if (self.cipsecfailsaspi.is_set or self.cipsecfailsaspi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecfailsaspi.get_name_leafdata())
                if (self.cipsecfailtime.is_set or self.cipsecfailtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecfailtime.get_name_leafdata())
                if (self.cipsecfailtunnelindex.is_set or self.cipsecfailtunnelindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsecfailtunnelindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipSecFailIndex" or name == "cipSecFailPktDstAddr" or name == "cipSecFailPktSrcAddr" or name == "cipSecFailReason" or name == "cipSecFailSaSpi" or name == "cipSecFailTime" or name == "cipSecFailTunnelIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipSecFailIndex"):
                    self.cipsecfailindex = value
                    self.cipsecfailindex.value_namespace = name_space
                    self.cipsecfailindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecFailPktDstAddr"):
                    self.cipsecfailpktdstaddr = value
                    self.cipsecfailpktdstaddr.value_namespace = name_space
                    self.cipsecfailpktdstaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecFailPktSrcAddr"):
                    self.cipsecfailpktsrcaddr = value
                    self.cipsecfailpktsrcaddr.value_namespace = name_space
                    self.cipsecfailpktsrcaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecFailReason"):
                    self.cipsecfailreason = value
                    self.cipsecfailreason.value_namespace = name_space
                    self.cipsecfailreason.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecFailSaSpi"):
                    self.cipsecfailsaspi = value
                    self.cipsecfailsaspi.value_namespace = name_space
                    self.cipsecfailsaspi.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecFailTime"):
                    self.cipsecfailtime = value
                    self.cipsecfailtime.value_namespace = name_space
                    self.cipsecfailtime.value_namespace_prefix = name_space_prefix
                if(value_path == "cipSecFailTunnelIndex"):
                    self.cipsecfailtunnelindex = value
                    self.cipsecfailtunnelindex.value_namespace = name_space
                    self.cipsecfailtunnelindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipsecfailentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipsecfailentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipSecFailTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipSecFailEntry"):
                for c in self.cipsecfailentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecFlowMonitorMib.Cipsecfailtable.Cipsecfailentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipsecfailentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipSecFailEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cikefailtable is not None and self.cikefailtable.has_data()) or
            (self.cikeglobalstats is not None and self.cikeglobalstats.has_data()) or
            (self.cikepeercorrtable is not None and self.cikepeercorrtable.has_data()) or
            (self.cikepeertable is not None and self.cikepeertable.has_data()) or
            (self.cikephase1gwstatstable is not None and self.cikephase1gwstatstable.has_data()) or
            (self.ciketunnelhisttable is not None and self.ciketunnelhisttable.has_data()) or
            (self.ciketunneltable is not None and self.ciketunneltable.has_data()) or
            (self.cipsecendpthisttable is not None and self.cipsecendpthisttable.has_data()) or
            (self.cipsecendpttable is not None and self.cipsecendpttable.has_data()) or
            (self.cipsecfailglobalcntl is not None and self.cipsecfailglobalcntl.has_data()) or
            (self.cipsecfailtable is not None and self.cipsecfailtable.has_data()) or
            (self.cipsecglobalstats is not None and self.cipsecglobalstats.has_data()) or
            (self.cipsechistglobalcntl is not None and self.cipsechistglobalcntl.has_data()) or
            (self.cipseclevels is not None and self.cipseclevels.has_data()) or
            (self.cipsecphase2gwstatstable is not None and self.cipsecphase2gwstatstable.has_data()) or
            (self.cipsecspitable is not None and self.cipsecspitable.has_data()) or
            (self.cipsectrapcntl is not None and self.cipsectrapcntl.has_data()) or
            (self.cipsectunnelhisttable is not None and self.cipsectunnelhisttable.has_data()) or
            (self.cipsectunneltable is not None and self.cipsectunneltable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cikefailtable is not None and self.cikefailtable.has_operation()) or
            (self.cikeglobalstats is not None and self.cikeglobalstats.has_operation()) or
            (self.cikepeercorrtable is not None and self.cikepeercorrtable.has_operation()) or
            (self.cikepeertable is not None and self.cikepeertable.has_operation()) or
            (self.cikephase1gwstatstable is not None and self.cikephase1gwstatstable.has_operation()) or
            (self.ciketunnelhisttable is not None and self.ciketunnelhisttable.has_operation()) or
            (self.ciketunneltable is not None and self.ciketunneltable.has_operation()) or
            (self.cipsecendpthisttable is not None and self.cipsecendpthisttable.has_operation()) or
            (self.cipsecendpttable is not None and self.cipsecendpttable.has_operation()) or
            (self.cipsecfailglobalcntl is not None and self.cipsecfailglobalcntl.has_operation()) or
            (self.cipsecfailtable is not None and self.cipsecfailtable.has_operation()) or
            (self.cipsecglobalstats is not None and self.cipsecglobalstats.has_operation()) or
            (self.cipsechistglobalcntl is not None and self.cipsechistglobalcntl.has_operation()) or
            (self.cipseclevels is not None and self.cipseclevels.has_operation()) or
            (self.cipsecphase2gwstatstable is not None and self.cipsecphase2gwstatstable.has_operation()) or
            (self.cipsecspitable is not None and self.cipsecspitable.has_operation()) or
            (self.cipsectrapcntl is not None and self.cipsectrapcntl.has_operation()) or
            (self.cipsectunnelhisttable is not None and self.cipsectunnelhisttable.has_operation()) or
            (self.cipsectunneltable is not None and self.cipsectunneltable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB" + path_buffer

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

        if (child_yang_name == "cikeFailTable"):
            if (self.cikefailtable is None):
                self.cikefailtable = CiscoIpsecFlowMonitorMib.Cikefailtable()
                self.cikefailtable.parent = self
                self._children_name_map["cikefailtable"] = "cikeFailTable"
            return self.cikefailtable

        if (child_yang_name == "cikeGlobalStats"):
            if (self.cikeglobalstats is None):
                self.cikeglobalstats = CiscoIpsecFlowMonitorMib.Cikeglobalstats()
                self.cikeglobalstats.parent = self
                self._children_name_map["cikeglobalstats"] = "cikeGlobalStats"
            return self.cikeglobalstats

        if (child_yang_name == "cikePeerCorrTable"):
            if (self.cikepeercorrtable is None):
                self.cikepeercorrtable = CiscoIpsecFlowMonitorMib.Cikepeercorrtable()
                self.cikepeercorrtable.parent = self
                self._children_name_map["cikepeercorrtable"] = "cikePeerCorrTable"
            return self.cikepeercorrtable

        if (child_yang_name == "cikePeerTable"):
            if (self.cikepeertable is None):
                self.cikepeertable = CiscoIpsecFlowMonitorMib.Cikepeertable()
                self.cikepeertable.parent = self
                self._children_name_map["cikepeertable"] = "cikePeerTable"
            return self.cikepeertable

        if (child_yang_name == "cikePhase1GWStatsTable"):
            if (self.cikephase1gwstatstable is None):
                self.cikephase1gwstatstable = CiscoIpsecFlowMonitorMib.Cikephase1Gwstatstable()
                self.cikephase1gwstatstable.parent = self
                self._children_name_map["cikephase1gwstatstable"] = "cikePhase1GWStatsTable"
            return self.cikephase1gwstatstable

        if (child_yang_name == "cikeTunnelHistTable"):
            if (self.ciketunnelhisttable is None):
                self.ciketunnelhisttable = CiscoIpsecFlowMonitorMib.Ciketunnelhisttable()
                self.ciketunnelhisttable.parent = self
                self._children_name_map["ciketunnelhisttable"] = "cikeTunnelHistTable"
            return self.ciketunnelhisttable

        if (child_yang_name == "cikeTunnelTable"):
            if (self.ciketunneltable is None):
                self.ciketunneltable = CiscoIpsecFlowMonitorMib.Ciketunneltable()
                self.ciketunneltable.parent = self
                self._children_name_map["ciketunneltable"] = "cikeTunnelTable"
            return self.ciketunneltable

        if (child_yang_name == "cipSecEndPtHistTable"):
            if (self.cipsecendpthisttable is None):
                self.cipsecendpthisttable = CiscoIpsecFlowMonitorMib.Cipsecendpthisttable()
                self.cipsecendpthisttable.parent = self
                self._children_name_map["cipsecendpthisttable"] = "cipSecEndPtHistTable"
            return self.cipsecendpthisttable

        if (child_yang_name == "cipSecEndPtTable"):
            if (self.cipsecendpttable is None):
                self.cipsecendpttable = CiscoIpsecFlowMonitorMib.Cipsecendpttable()
                self.cipsecendpttable.parent = self
                self._children_name_map["cipsecendpttable"] = "cipSecEndPtTable"
            return self.cipsecendpttable

        if (child_yang_name == "cipSecFailGlobalCntl"):
            if (self.cipsecfailglobalcntl is None):
                self.cipsecfailglobalcntl = CiscoIpsecFlowMonitorMib.Cipsecfailglobalcntl()
                self.cipsecfailglobalcntl.parent = self
                self._children_name_map["cipsecfailglobalcntl"] = "cipSecFailGlobalCntl"
            return self.cipsecfailglobalcntl

        if (child_yang_name == "cipSecFailTable"):
            if (self.cipsecfailtable is None):
                self.cipsecfailtable = CiscoIpsecFlowMonitorMib.Cipsecfailtable()
                self.cipsecfailtable.parent = self
                self._children_name_map["cipsecfailtable"] = "cipSecFailTable"
            return self.cipsecfailtable

        if (child_yang_name == "cipSecGlobalStats"):
            if (self.cipsecglobalstats is None):
                self.cipsecglobalstats = CiscoIpsecFlowMonitorMib.Cipsecglobalstats()
                self.cipsecglobalstats.parent = self
                self._children_name_map["cipsecglobalstats"] = "cipSecGlobalStats"
            return self.cipsecglobalstats

        if (child_yang_name == "cipSecHistGlobalCntl"):
            if (self.cipsechistglobalcntl is None):
                self.cipsechistglobalcntl = CiscoIpsecFlowMonitorMib.Cipsechistglobalcntl()
                self.cipsechistglobalcntl.parent = self
                self._children_name_map["cipsechistglobalcntl"] = "cipSecHistGlobalCntl"
            return self.cipsechistglobalcntl

        if (child_yang_name == "cipSecLevels"):
            if (self.cipseclevels is None):
                self.cipseclevels = CiscoIpsecFlowMonitorMib.Cipseclevels()
                self.cipseclevels.parent = self
                self._children_name_map["cipseclevels"] = "cipSecLevels"
            return self.cipseclevels

        if (child_yang_name == "cipSecPhase2GWStatsTable"):
            if (self.cipsecphase2gwstatstable is None):
                self.cipsecphase2gwstatstable = CiscoIpsecFlowMonitorMib.Cipsecphase2Gwstatstable()
                self.cipsecphase2gwstatstable.parent = self
                self._children_name_map["cipsecphase2gwstatstable"] = "cipSecPhase2GWStatsTable"
            return self.cipsecphase2gwstatstable

        if (child_yang_name == "cipSecSpiTable"):
            if (self.cipsecspitable is None):
                self.cipsecspitable = CiscoIpsecFlowMonitorMib.Cipsecspitable()
                self.cipsecspitable.parent = self
                self._children_name_map["cipsecspitable"] = "cipSecSpiTable"
            return self.cipsecspitable

        if (child_yang_name == "cipSecTrapCntl"):
            if (self.cipsectrapcntl is None):
                self.cipsectrapcntl = CiscoIpsecFlowMonitorMib.Cipsectrapcntl()
                self.cipsectrapcntl.parent = self
                self._children_name_map["cipsectrapcntl"] = "cipSecTrapCntl"
            return self.cipsectrapcntl

        if (child_yang_name == "cipSecTunnelHistTable"):
            if (self.cipsectunnelhisttable is None):
                self.cipsectunnelhisttable = CiscoIpsecFlowMonitorMib.Cipsectunnelhisttable()
                self.cipsectunnelhisttable.parent = self
                self._children_name_map["cipsectunnelhisttable"] = "cipSecTunnelHistTable"
            return self.cipsectunnelhisttable

        if (child_yang_name == "cipSecTunnelTable"):
            if (self.cipsectunneltable is None):
                self.cipsectunneltable = CiscoIpsecFlowMonitorMib.Cipsectunneltable()
                self.cipsectunneltable.parent = self
                self._children_name_map["cipsectunneltable"] = "cipSecTunnelTable"
            return self.cipsectunneltable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cikeFailTable" or name == "cikeGlobalStats" or name == "cikePeerCorrTable" or name == "cikePeerTable" or name == "cikePhase1GWStatsTable" or name == "cikeTunnelHistTable" or name == "cikeTunnelTable" or name == "cipSecEndPtHistTable" or name == "cipSecEndPtTable" or name == "cipSecFailGlobalCntl" or name == "cipSecFailTable" or name == "cipSecGlobalStats" or name == "cipSecHistGlobalCntl" or name == "cipSecLevels" or name == "cipSecPhase2GWStatsTable" or name == "cipSecSpiTable" or name == "cipSecTrapCntl" or name == "cipSecTunnelHistTable" or name == "cipSecTunnelTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIpsecFlowMonitorMib()
        return self._top_entity

