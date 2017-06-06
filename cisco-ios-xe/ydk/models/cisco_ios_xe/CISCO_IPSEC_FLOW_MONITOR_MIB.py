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

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AuthalgoEnum(Enum):
    """
    AuthalgoEnum

    The authentication algorithm used by a

    security association of an IPsec Phase\-2 Tunnel.

    .. data:: none = 1

    .. data:: hmacMd5 = 2

    .. data:: hmacSha = 3

    """

    none = 1

    hmacMd5 = 2

    hmacSha = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['AuthalgoEnum']


class CompalgoEnum(Enum):
    """
    CompalgoEnum

    The compression algorithm used by a

    security association of an IPsec Phase\-2 Tunnel.

    .. data:: none = 1

    .. data:: ldf = 2

    """

    none = 1

    ldf = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['CompalgoEnum']


class DiffhellmangrpEnum(Enum):
    """
    DiffhellmangrpEnum

    The Diffie Hellman Group used in negotiations.

    .. data:: none = 1

    .. data:: dhGroup1 = 2

    .. data:: dhGroup2 = 3

    """

    none = 1

    dhGroup1 = 2

    dhGroup2 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['DiffhellmangrpEnum']


class EncapmodeEnum(Enum):
    """
    EncapmodeEnum

    The encapsulation mode used by an IPsec Phase\-2

    Tunnel.

    .. data:: tunnel = 1

    .. data:: transport = 2

    """

    tunnel = 1

    transport = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['EncapmodeEnum']


class EncryptalgoEnum(Enum):
    """
    EncryptalgoEnum

    The encryption algorithm used in negotiations.

    .. data:: none = 1

    .. data:: des = 2

    .. data:: des3 = 3

    """

    none = 1

    des = 2

    des3 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['EncryptalgoEnum']


class EndpttypeEnum(Enum):
    """
    EndpttypeEnum

    The type of identity use to specify an IPsec End Point.

    .. data:: singleIpAddr = 1

    .. data:: ipAddrRange = 2

    .. data:: ipSubnet = 3

    """

    singleIpAddr = 1

    ipAddrRange = 2

    ipSubnet = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['EndpttypeEnum']


class IkeauthmethodEnum(Enum):
    """
    IkeauthmethodEnum

    The authentication method used in IPsec Phase\-1 IKE

    negotiations.

    .. data:: none = 1

    .. data:: preSharedKey = 2

    .. data:: rsaSig = 3

    .. data:: rsaEncrypt = 4

    .. data:: revPublicKey = 5

    """

    none = 1

    preSharedKey = 2

    rsaSig = 3

    rsaEncrypt = 4

    revPublicKey = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['IkeauthmethodEnum']


class IkehashalgoEnum(Enum):
    """
    IkehashalgoEnum

    The hash algorithm used in IPsec Phase\-1

    IKE negotiations.

    .. data:: none = 1

    .. data:: md5 = 2

    .. data:: sha = 3

    """

    none = 1

    md5 = 2

    sha = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['IkehashalgoEnum']


class IkenegomodeEnum(Enum):
    """
    IkenegomodeEnum

    The IPsec Phase\-1 IKE negotiation mode.

    .. data:: main = 1

    .. data:: aggressive = 2

    """

    main = 1

    aggressive = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['IkenegomodeEnum']


class IkepeertypeEnum(Enum):
    """
    IkepeertypeEnum

    The type of IPsec Phase\-1 IKE peer identity.

    The IKE peer may be identified by\:

     1. an IP address, or

     2. a host name.

    .. data:: ipAddrPeer = 1

    .. data:: namePeer = 2

    """

    ipAddrPeer = 1

    namePeer = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['IkepeertypeEnum']


class KeytypeEnum(Enum):
    """
    KeytypeEnum

    The type of key used by an IPsec Phase\-2 Tunnel.

    .. data:: ike = 1

    .. data:: manual = 2

    """

    ike = 1

    manual = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['KeytypeEnum']


class TrapstatusEnum(Enum):
    """
    TrapstatusEnum

    The administrative status for sending a TRAP.

    .. data:: enabled = 1

    .. data:: disabled = 2

    """

    enabled = 1

    disabled = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['TrapstatusEnum']


class TunnelstatusEnum(Enum):
    """
    TunnelstatusEnum

    The status of a Tunnel.  Objects of this type may

    be used to bring the tunnel down by setting

    value of this object to destroy(2).  Objects of this

    type cannot be used to create a Tunnel.

    .. data:: active = 1

    .. data:: destroy = 2

    """

    active = 1

    destroy = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['TunnelstatusEnum']



class CiscoIpsecFlowMonitorMib(object):
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
        self.cikefailtable = CiscoIpsecFlowMonitorMib.Cikefailtable()
        self.cikefailtable.parent = self
        self.cikeglobalstats = CiscoIpsecFlowMonitorMib.Cikeglobalstats()
        self.cikeglobalstats.parent = self
        self.cikepeercorrtable = CiscoIpsecFlowMonitorMib.Cikepeercorrtable()
        self.cikepeercorrtable.parent = self
        self.cikepeertable = CiscoIpsecFlowMonitorMib.Cikepeertable()
        self.cikepeertable.parent = self
        self.cikephase1gwstatstable = CiscoIpsecFlowMonitorMib.Cikephase1Gwstatstable()
        self.cikephase1gwstatstable.parent = self
        self.ciketunnelhisttable = CiscoIpsecFlowMonitorMib.Ciketunnelhisttable()
        self.ciketunnelhisttable.parent = self
        self.ciketunneltable = CiscoIpsecFlowMonitorMib.Ciketunneltable()
        self.ciketunneltable.parent = self
        self.cipsecendpthisttable = CiscoIpsecFlowMonitorMib.Cipsecendpthisttable()
        self.cipsecendpthisttable.parent = self
        self.cipsecendpttable = CiscoIpsecFlowMonitorMib.Cipsecendpttable()
        self.cipsecendpttable.parent = self
        self.cipsecfailglobalcntl = CiscoIpsecFlowMonitorMib.Cipsecfailglobalcntl()
        self.cipsecfailglobalcntl.parent = self
        self.cipsecfailtable = CiscoIpsecFlowMonitorMib.Cipsecfailtable()
        self.cipsecfailtable.parent = self
        self.cipsecglobalstats = CiscoIpsecFlowMonitorMib.Cipsecglobalstats()
        self.cipsecglobalstats.parent = self
        self.cipsechistglobalcntl = CiscoIpsecFlowMonitorMib.Cipsechistglobalcntl()
        self.cipsechistglobalcntl.parent = self
        self.cipseclevels = CiscoIpsecFlowMonitorMib.Cipseclevels()
        self.cipseclevels.parent = self
        self.cipsecphase2gwstatstable = CiscoIpsecFlowMonitorMib.Cipsecphase2Gwstatstable()
        self.cipsecphase2gwstatstable.parent = self
        self.cipsecspitable = CiscoIpsecFlowMonitorMib.Cipsecspitable()
        self.cipsecspitable.parent = self
        self.cipsectrapcntl = CiscoIpsecFlowMonitorMib.Cipsectrapcntl()
        self.cipsectrapcntl.parent = self
        self.cipsectunnelhisttable = CiscoIpsecFlowMonitorMib.Cipsectunnelhisttable()
        self.cipsectunnelhisttable.parent = self
        self.cipsectunneltable = CiscoIpsecFlowMonitorMib.Cipsectunneltable()
        self.cipsectunneltable.parent = self


    class Cipseclevels(object):
        """
        
        
        .. attribute:: cipsecmiblevel
        
        	The level of the IPsec MIB
        	**type**\:  int
        
        	**range:** 1..4096
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
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
            if self.cipsecmiblevel is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipseclevels']['meta_info']


    class Cikeglobalstats(object):
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

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Cikeglobalstats']['meta_info']


    class Cipsecglobalstats(object):
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

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsecglobalstats']['meta_info']


    class Cipsechistglobalcntl(object):
        """
        
        
        .. attribute:: cipsechistcheckpoint
        
        	The current state of check point processing.  This object will return ready when the agent is  ready to create on\-demand history entries for  active IPsec Tunnels or checkPoint when the  agent is currently creating on\-demand history  entries for active IPsec Tunnels.  By setting this value to checkPoint, the agent  will create\: a) an entry in the IPsec Phase\-1 Tunnel History     for each active IPsec Phase\-1 Tunnel and b) an entry in the IPsec Phase\-2 Tunnel History     Table and an entry in the IPsec Phase\-2     Tunnel EndPoint History Table    for each active IPsec Phase\-2 Tunnel
        	**type**\:   :py:class:`CipsechistcheckpointEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsechistglobalcntl.CipsechistcheckpointEnum>`
        
        .. attribute:: cipsechisttablesize
        
        	The window size of the IPsec Phase\-1 and Phase\-2 History Tables.  The IPsec Phase\-1 and Phase\-2 History Tables are implemented as a sliding window in which only the last n entries are maintained.  This object is used specify the number of entries which will be  maintained in the IPsec Phase\-1 and  Phase\-2 History Tables.  An implementation may choose suitable minimum and  maximum values for this element based on the local  policy and available resources. If an SNMP SET request  specifies a value outside this window for this element,  a BAD VALUE may be returned
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
        _revision = '2007-10-24'

        def __init__(self):
            self.parent = None
            self.cipsechistcheckpoint = None
            self.cipsechisttablesize = None

        class CipsechistcheckpointEnum(Enum):
            """
            CipsechistcheckpointEnum

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

            ready = 1

            checkPoint = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsechistglobalcntl.CipsechistcheckpointEnum']


        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecHistGlobalCntl'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cipsechistcheckpoint is not None:
                return True

            if self.cipsechisttablesize is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsechistglobalcntl']['meta_info']


    class Cipsecfailglobalcntl(object):
        """
        
        
        .. attribute:: cipsecfailtablesize
        
        	The window size of the IPsec Phase\-1 and Phase\-2 Failure Tables.  The IPsec Phase\-1 and Phase\-2 Failure Tables are implemented as a sliding window in which only the last n entries are maintained.  This object is used specify the number of entries which will be  maintained in the IPsec Phase\-1 and Phase\-2 Failure  Tables.  An implementation may choose suitable minimum and  maximum values for this element based on the local  policy and available resources. If an SNMP SET request  specifies a value outside this window for this element,  a BAD VALUE may be returned
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
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
            if self.cipsecfailtablesize is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsecfailglobalcntl']['meta_info']


    class Cipsectrapcntl(object):
        """
        
        
        .. attribute:: cipsectrapcntlikecertcrlfailure
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 Certificate/CRL Failure TRAP
        	**type**\:   :py:class:`TrapstatusEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapstatusEnum>`
        
        .. attribute:: cipsectrapcntlikenosa
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 No Security Association TRAP
        	**type**\:   :py:class:`TrapstatusEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapstatusEnum>`
        
        .. attribute:: cipsectrapcntlikeprotocolfail
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 Protocol Failure TRAP
        	**type**\:   :py:class:`TrapstatusEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapstatusEnum>`
        
        .. attribute:: cipsectrapcntlikesysfailure
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 System Failure TRAP
        	**type**\:   :py:class:`TrapstatusEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapstatusEnum>`
        
        .. attribute:: cipsectrapcntliketunnelstart
        
        	This object defines the administrative state of sending the IPsec IKE Phase\-1 Tunnel Start TRAP
        	**type**\:   :py:class:`TrapstatusEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapstatusEnum>`
        
        .. attribute:: cipsectrapcntliketunnelstop
        
        	This object defines the administrative state of sending the  IPsec IKE Phase\-1 Tunnel Stop TRAP
        	**type**\:   :py:class:`TrapstatusEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapstatusEnum>`
        
        .. attribute:: cipsectrapcntlipsecearlytunterm
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Early Tunnel Termination TRAP
        	**type**\:   :py:class:`TrapstatusEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapstatusEnum>`
        
        .. attribute:: cipsectrapcntlipsecnosa
        
        	This object defines the administrative state of sending the IPsec  Phase\-2  No Security Association TRAP
        	**type**\:   :py:class:`TrapstatusEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapstatusEnum>`
        
        .. attribute:: cipsectrapcntlipsecprotocolfail
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Protocol Failure TRAP
        	**type**\:   :py:class:`TrapstatusEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapstatusEnum>`
        
        .. attribute:: cipsectrapcntlipsecsetupfailure
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Set Up Failure TRAP
        	**type**\:   :py:class:`TrapstatusEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapstatusEnum>`
        
        .. attribute:: cipsectrapcntlipsecsysfailure
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 System Failure TRAP
        	**type**\:   :py:class:`TrapstatusEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapstatusEnum>`
        
        .. attribute:: cipsectrapcntlipsectunnelstart
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Tunnel Start TRAP
        	**type**\:   :py:class:`TrapstatusEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapstatusEnum>`
        
        .. attribute:: cipsectrapcntlipsectunnelstop
        
        	This object defines the administrative state of sending the IPsec  Phase\-2 Tunnel Stop TRAP
        	**type**\:   :py:class:`TrapstatusEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TrapstatusEnum>`
        
        

        """

        _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
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

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsectrapcntl']['meta_info']


    class Cikepeertable(object):
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
            self.parent = None
            self.cikepeerentry = YList()
            self.cikepeerentry.parent = self
            self.cikepeerentry.name = 'cikepeerentry'


        class Cikepeerentry(object):
            """
            Each entry contains the attributes associated
            with an IPsec Phase\-1 IKE peer association.
            
            .. attribute:: cikepeerlocaltype  <key>
            
            	The type of local peer identity.  The local peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\:   :py:class:`IkepeertypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkepeertypeEnum>`
            
            .. attribute:: cikepeerlocalvalue  <key>
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\:  str
            
            .. attribute:: cikepeerremotetype  <key>
            
            	The type of remote peer identity.  The remote peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\:   :py:class:`IkepeertypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkepeertypeEnum>`
            
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
                self.parent = None
                self.cikepeerlocaltype = None
                self.cikepeerlocalvalue = None
                self.cikepeerremotetype = None
                self.cikepeerremotevalue = None
                self.cikepeerintindex = None
                self.cikepeeractivetime = None
                self.cikepeeractivetunnelindex = None
                self.cikepeerlocaladdr = None
                self.cikepeerremoteaddr = None

            @property
            def _common_path(self):
                if self.cikepeerlocaltype is None:
                    raise YPYModelError('Key property cikepeerlocaltype is None')
                if self.cikepeerlocalvalue is None:
                    raise YPYModelError('Key property cikepeerlocalvalue is None')
                if self.cikepeerremotetype is None:
                    raise YPYModelError('Key property cikepeerremotetype is None')
                if self.cikepeerremotevalue is None:
                    raise YPYModelError('Key property cikepeerremotevalue is None')
                if self.cikepeerintindex is None:
                    raise YPYModelError('Key property cikepeerintindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerLocalType = ' + str(self.cikepeerlocaltype) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerLocalValue = ' + str(self.cikepeerlocalvalue) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerRemoteType = ' + str(self.cikepeerremotetype) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerRemoteValue = ' + str(self.cikepeerremotevalue) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerIntIndex = ' + str(self.cikepeerintindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cikepeerlocaltype is not None:
                    return True

                if self.cikepeerlocalvalue is not None:
                    return True

                if self.cikepeerremotetype is not None:
                    return True

                if self.cikepeerremotevalue is not None:
                    return True

                if self.cikepeerintindex is not None:
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CiscoIpsecFlowMonitorMib.Cikepeertable.Cikepeerentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cikepeerentry is not None:
                for child_ref in self.cikepeerentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Cikepeertable']['meta_info']


    class Ciketunneltable(object):
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
            self.parent = None
            self.ciketunnelentry = YList()
            self.ciketunnelentry.parent = self
            self.ciketunnelentry.name = 'ciketunnelentry'


        class Ciketunnelentry(object):
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
            	**type**\:   :py:class:`IkeauthmethodEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeauthmethodEnum>`
            
            .. attribute:: ciketundiffhellmangrp
            
            	The Diffie Hellman Group used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`DiffhellmangrpEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffhellmangrpEnum>`
            
            .. attribute:: ciketunencryptalgo
            
            	The encryption algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`EncryptalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptalgoEnum>`
            
            .. attribute:: ciketunhashalgo
            
            	The hash algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`IkehashalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkehashalgoEnum>`
            
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
            	**type**\:   :py:class:`IkepeertypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkepeertypeEnum>`
            
            .. attribute:: ciketunlocalvalue
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\:  str
            
            .. attribute:: ciketunnegomode
            
            	The negotiation mode of the IPsec Phase\-1 IKE Tunnel
            	**type**\:   :py:class:`IkenegomodeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkenegomodeEnum>`
            
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
            	**type**\:   :py:class:`IkepeertypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkepeertypeEnum>`
            
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
            	**type**\:   :py:class:`TunnelstatusEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TunnelstatusEnum>`
            
            .. attribute:: ciketuntotalrefreshes
            
            	The total number of security associations refreshes performed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: QM Exchanges
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
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
                    raise YPYModelError('Key property ciketunindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeTunnelTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeTunnelEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cikeTunIndex = ' + str(self.ciketunindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CiscoIpsecFlowMonitorMib.Ciketunneltable.Ciketunnelentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeTunnelTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ciketunnelentry is not None:
                for child_ref in self.ciketunnelentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Ciketunneltable']['meta_info']


    class Cikepeercorrtable(object):
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
            self.parent = None
            self.cikepeercorrentry = YList()
            self.cikepeercorrentry.parent = self
            self.cikepeercorrentry.name = 'cikepeercorrentry'


        class Cikepeercorrentry(object):
            """
            Each entry contains the attributes of an
            IPsec Phase\-1 IKE Peer Association to IPsec
            Phase\-2 Tunnel Correlation.
            
            .. attribute:: cikepeercorrlocaltype  <key>
            
            	The type of local peer identity. The local peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\:   :py:class:`IkepeertypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkepeertypeEnum>`
            
            .. attribute:: cikepeercorrlocalvalue  <key>
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\:  str
            
            .. attribute:: cikepeercorrremotetype  <key>
            
            	The type of remote peer identity. The remote peer may be identified by\: 1. an IP address, or 2. a host name
            	**type**\:   :py:class:`IkepeertypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkepeertypeEnum>`
            
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
                self.parent = None
                self.cikepeercorrlocaltype = None
                self.cikepeercorrlocalvalue = None
                self.cikepeercorrremotetype = None
                self.cikepeercorrremotevalue = None
                self.cikepeercorrintindex = None
                self.cikepeercorrseqnum = None
                self.cikepeercorripsectunindex = None

            @property
            def _common_path(self):
                if self.cikepeercorrlocaltype is None:
                    raise YPYModelError('Key property cikepeercorrlocaltype is None')
                if self.cikepeercorrlocalvalue is None:
                    raise YPYModelError('Key property cikepeercorrlocalvalue is None')
                if self.cikepeercorrremotetype is None:
                    raise YPYModelError('Key property cikepeercorrremotetype is None')
                if self.cikepeercorrremotevalue is None:
                    raise YPYModelError('Key property cikepeercorrremotevalue is None')
                if self.cikepeercorrintindex is None:
                    raise YPYModelError('Key property cikepeercorrintindex is None')
                if self.cikepeercorrseqnum is None:
                    raise YPYModelError('Key property cikepeercorrseqnum is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrLocalType = ' + str(self.cikepeercorrlocaltype) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrLocalValue = ' + str(self.cikepeercorrlocalvalue) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrRemoteType = ' + str(self.cikepeercorrremotetype) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrRemoteValue = ' + str(self.cikepeercorrremotevalue) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrIntIndex = ' + str(self.cikepeercorrintindex) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrSeqNum = ' + str(self.cikepeercorrseqnum) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cikepeercorrlocaltype is not None:
                    return True

                if self.cikepeercorrlocalvalue is not None:
                    return True

                if self.cikepeercorrremotetype is not None:
                    return True

                if self.cikepeercorrremotevalue is not None:
                    return True

                if self.cikepeercorrintindex is not None:
                    return True

                if self.cikepeercorrseqnum is not None:
                    return True

                if self.cikepeercorripsectunindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CiscoIpsecFlowMonitorMib.Cikepeercorrtable.Cikepeercorrentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePeerCorrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cikepeercorrentry is not None:
                for child_ref in self.cikepeercorrentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Cikepeercorrtable']['meta_info']


    class Cikephase1Gwstatstable(object):
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
            self.parent = None
            self.cikephase1gwstatsentry = YList()
            self.cikephase1gwstatsentry.parent = self
            self.cikephase1gwstatsentry.name = 'cikephase1gwstatsentry'


        class Cikephase1Gwstatsentry(object):
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
                    raise YPYModelError('Key property cmgwindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePhase1GWStatsTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePhase1GWStatsEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cmgwIndex = ' + str(self.cmgwindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CiscoIpsecFlowMonitorMib.Cikephase1Gwstatstable.Cikephase1Gwstatsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikePhase1GWStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cikephase1gwstatsentry is not None:
                for child_ref in self.cikephase1gwstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Cikephase1Gwstatstable']['meta_info']


    class Cipsectunneltable(object):
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
            self.parent = None
            self.cipsectunnelentry = YList()
            self.cipsectunnelentry.parent = self
            self.cipsectunnelentry.name = 'cipsectunnelentry'


        class Cipsectunnelentry(object):
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
            	**type**\:   :py:class:`EncapmodeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncapmodeEnum>`
            
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
            	**type**\:   :py:class:`AuthalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthalgoEnum>`
            
            .. attribute:: cipsectuninsadecompalgo
            
            	The decompression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`CompalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CompalgoEnum>`
            
            .. attribute:: cipsectuninsadiffhellmangrp
            
            	The Diffie Hellman Group used by the inbound security association of the  IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`DiffhellmangrpEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffhellmangrpEnum>`
            
            .. attribute:: cipsectuninsaencryptalgo
            
            	The encryption algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`EncryptalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptalgoEnum>`
            
            .. attribute:: cipsectuninsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP) security  association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`AuthalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthalgoEnum>`
            
            .. attribute:: cipsectunkeytype
            
            	The type of key used by the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`KeytypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.KeytypeEnum>`
            
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
            	**type**\:   :py:class:`AuthalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthalgoEnum>`
            
            .. attribute:: cipsectunoutsacompalgo
            
            	The compression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`CompalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CompalgoEnum>`
            
            .. attribute:: cipsectunoutsadiffhellmangrp
            
            	The Diffie Hellman Group used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`DiffhellmangrpEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffhellmangrpEnum>`
            
            .. attribute:: cipsectunoutsaencryptalgo
            
            	The encryption algorithm used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`EncryptalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptalgoEnum>`
            
            .. attribute:: cipsectunoutsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP)  security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`AuthalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthalgoEnum>`
            
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
            	**type**\:   :py:class:`TunnelstatusEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.TunnelstatusEnum>`
            
            .. attribute:: cipsectuntotalrefreshes
            
            	The total number of security association refreshes performed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: QM Exchanges
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
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
                    raise YPYModelError('Key property cipsectunindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunnelTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunnelEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunIndex = ' + str(self.cipsectunindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsectunneltable.Cipsectunnelentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunnelTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cipsectunnelentry is not None:
                for child_ref in self.cipsectunnelentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsectunneltable']['meta_info']


    class Cipsecendpttable(object):
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
            self.parent = None
            self.cipsecendptentry = YList()
            self.cipsecendptentry.parent = self
            self.cipsecendptentry.name = 'cipsecendptentry'


        class Cipsecendptentry(object):
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
            	**type**\:   :py:class:`EndpttypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EndpttypeEnum>`
            
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
            	**type**\:   :py:class:`EndpttypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EndpttypeEnum>`
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                self.parent = None
                self.cipsectunindex = None
                self.cipsecendptindex = None
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
                if self.cipsectunindex is None:
                    raise YPYModelError('Key property cipsectunindex is None')
                if self.cipsecendptindex is None:
                    raise YPYModelError('Key property cipsecendptindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecEndPtTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecEndPtEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunIndex = ' + str(self.cipsectunindex) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecEndPtIndex = ' + str(self.cipsecendptindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cipsectunindex is not None:
                    return True

                if self.cipsecendptindex is not None:
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsecendpttable.Cipsecendptentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecEndPtTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cipsecendptentry is not None:
                for child_ref in self.cipsecendptentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsecendpttable']['meta_info']


    class Cipsecspitable(object):
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
            self.parent = None
            self.cipsecspientry = YList()
            self.cipsecspientry.parent = self
            self.cipsecspientry.name = 'cipsecspientry'


        class Cipsecspientry(object):
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
            	**type**\:   :py:class:`CipsecspidirectionEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecspitable.Cipsecspientry.CipsecspidirectionEnum>`
            
            .. attribute:: cipsecspiprotocol
            
            	The protocol of the SPI
            	**type**\:   :py:class:`CipsecspiprotocolEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecspitable.Cipsecspientry.CipsecspiprotocolEnum>`
            
            .. attribute:: cipsecspistatus
            
            	The status of the SPI
            	**type**\:   :py:class:`CipsecspistatusEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecspitable.Cipsecspientry.CipsecspistatusEnum>`
            
            .. attribute:: cipsecspivalue
            
            	The value of the SPI
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
            _revision = '2007-10-24'

            def __init__(self):
                self.parent = None
                self.cipsectunindex = None
                self.cipsecspiindex = None
                self.cipsecspidirection = None
                self.cipsecspiprotocol = None
                self.cipsecspistatus = None
                self.cipsecspivalue = None

            class CipsecspidirectionEnum(Enum):
                """
                CipsecspidirectionEnum

                The direction of the SPI.

                .. data:: in_ = 1

                .. data:: out = 2

                """

                in_ = 1

                out = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                    return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsecspitable.Cipsecspientry.CipsecspidirectionEnum']


            class CipsecspiprotocolEnum(Enum):
                """
                CipsecspiprotocolEnum

                The protocol of the SPI.

                .. data:: ah = 1

                .. data:: esp = 2

                .. data:: ipcomp = 3

                """

                ah = 1

                esp = 2

                ipcomp = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                    return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsecspitable.Cipsecspientry.CipsecspiprotocolEnum']


            class CipsecspistatusEnum(Enum):
                """
                CipsecspistatusEnum

                The status of the SPI.

                .. data:: active = 1

                .. data:: expiring = 2

                """

                active = 1

                expiring = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                    return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsecspitable.Cipsecspientry.CipsecspistatusEnum']


            @property
            def _common_path(self):
                if self.cipsectunindex is None:
                    raise YPYModelError('Key property cipsectunindex is None')
                if self.cipsecspiindex is None:
                    raise YPYModelError('Key property cipsecspiindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecSpiTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecSpiEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunIndex = ' + str(self.cipsectunindex) + '][CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecSpiIndex = ' + str(self.cipsecspiindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cipsectunindex is not None:
                    return True

                if self.cipsecspiindex is not None:
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsecspitable.Cipsecspientry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecSpiTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cipsecspientry is not None:
                for child_ref in self.cipsecspientry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsecspitable']['meta_info']


    class Cipsecphase2Gwstatstable(object):
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
            self.parent = None
            self.cipsecphase2gwstatsentry = YList()
            self.cipsecphase2gwstatsentry.parent = self
            self.cipsecphase2gwstatsentry.name = 'cipsecphase2gwstatsentry'


        class Cipsecphase2Gwstatsentry(object):
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
                    raise YPYModelError('Key property cmgwindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecPhase2GWStatsTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecPhase2GWStatsEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cmgwIndex = ' + str(self.cmgwindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsecphase2Gwstatstable.Cipsecphase2Gwstatsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecPhase2GWStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cipsecphase2gwstatsentry is not None:
                for child_ref in self.cipsecphase2gwstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsecphase2Gwstatstable']['meta_info']


    class Ciketunnelhisttable(object):
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
            self.parent = None
            self.ciketunnelhistentry = YList()
            self.ciketunnelhistentry.parent = self
            self.ciketunnelhistentry.name = 'ciketunnelhistentry'


        class Ciketunnelhistentry(object):
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
            	**type**\:   :py:class:`IkeauthmethodEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkeauthmethodEnum>`
            
            .. attribute:: ciketunhistdiffhellmangrp
            
            	The Diffie Hellman Group used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`DiffhellmangrpEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffhellmangrpEnum>`
            
            .. attribute:: ciketunhistencryptalgo
            
            	The encryption algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`EncryptalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptalgoEnum>`
            
            .. attribute:: ciketunhisthashalgo
            
            	The hash algorithm used in IPsec Phase\-1 IKE negotiations
            	**type**\:   :py:class:`IkehashalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkehashalgoEnum>`
            
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
            	**type**\:   :py:class:`IkenegomodeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkenegomodeEnum>`
            
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
            	**type**\:   :py:class:`IkepeertypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkepeertypeEnum>`
            
            .. attribute:: ciketunhistpeerlocalvalue
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\:  str
            
            .. attribute:: ciketunhistpeerremotetype
            
            	The type of remote peer identity.  The remote peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\:   :py:class:`IkepeertypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkepeertypeEnum>`
            
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
            	**type**\:   :py:class:`CiketunhisttermreasonEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Ciketunnelhisttable.Ciketunnelhistentry.CiketunhisttermreasonEnum>`
            
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

            class CiketunhisttermreasonEnum(Enum):
                """
                CiketunhisttermreasonEnum

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

                other = 1

                normal = 2

                operRequest = 3

                peerDelRequest = 4

                peerLost = 5

                localFailure = 6

                checkPointReg = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                    return meta._meta_table['CiscoIpsecFlowMonitorMib.Ciketunnelhisttable.Ciketunnelhistentry.CiketunhisttermreasonEnum']


            @property
            def _common_path(self):
                if self.ciketunhistindex is None:
                    raise YPYModelError('Key property ciketunhistindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeTunnelHistTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeTunnelHistEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cikeTunHistIndex = ' + str(self.ciketunhistindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CiscoIpsecFlowMonitorMib.Ciketunnelhisttable.Ciketunnelhistentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeTunnelHistTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ciketunnelhistentry is not None:
                for child_ref in self.ciketunnelhistentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Ciketunnelhisttable']['meta_info']


    class Cipsectunnelhisttable(object):
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
            self.parent = None
            self.cipsectunnelhistentry = YList()
            self.cipsectunnelhistentry.parent = self
            self.cipsectunnelhistentry.name = 'cipsectunnelhistentry'


        class Cipsectunnelhistentry(object):
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
            	**type**\:   :py:class:`EncapmodeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncapmodeEnum>`
            
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
            	**type**\:   :py:class:`AuthalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthalgoEnum>`
            
            .. attribute:: cipsectunhistinsadecompalgo
            
            	The decompression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`CompalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CompalgoEnum>`
            
            .. attribute:: cipsectunhistinsadiffhellmangrp
            
            	The Diffie Hellman Group used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`DiffhellmangrpEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffhellmangrpEnum>`
            
            .. attribute:: cipsectunhistinsaencryptalgo
            
            	The encryption algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`EncryptalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptalgoEnum>`
            
            .. attribute:: cipsectunhistinsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP)  security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`AuthalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthalgoEnum>`
            
            .. attribute:: cipsectunhistkeytype
            
            	The type of key used by the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`KeytypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.KeytypeEnum>`
            
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
            	**type**\:   :py:class:`AuthalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthalgoEnum>`
            
            .. attribute:: cipsectunhistoutsacompalgo
            
            	The compression algorithm used by the inbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`CompalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CompalgoEnum>`
            
            .. attribute:: cipsectunhistoutsadiffhellmangrp
            
            	The Diffie Hellman Group used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`DiffhellmangrpEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.DiffhellmangrpEnum>`
            
            .. attribute:: cipsectunhistoutsaencryptalgo
            
            	The encryption algorithm used by the outbound security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`EncryptalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EncryptalgoEnum>`
            
            .. attribute:: cipsectunhistoutsaespauthalgo
            
            	The authentication algorithm used by the inbound encapsulation security protocol (ESP)  security association of the IPsec Phase\-2 Tunnel
            	**type**\:   :py:class:`AuthalgoEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.AuthalgoEnum>`
            
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
            	**type**\:   :py:class:`CipsectunhisttermreasonEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsectunnelhisttable.Cipsectunnelhistentry.CipsectunhisttermreasonEnum>`
            
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

            class CipsectunhisttermreasonEnum(Enum):
                """
                CipsectunhisttermreasonEnum

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

                other = 1

                normal = 2

                operRequest = 3

                peerDelRequest = 4

                peerLost = 5

                seqNumRollOver = 6

                checkPointReq = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                    return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsectunnelhisttable.Cipsectunnelhistentry.CipsectunhisttermreasonEnum']


            @property
            def _common_path(self):
                if self.cipsectunhistindex is None:
                    raise YPYModelError('Key property cipsectunhistindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunnelHistTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunnelHistEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunHistIndex = ' + str(self.cipsectunhistindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsectunnelhisttable.Cipsectunnelhistentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecTunnelHistTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cipsectunnelhistentry is not None:
                for child_ref in self.cipsectunnelhistentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsectunnelhisttable']['meta_info']


    class Cipsecendpthisttable(object):
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
            self.parent = None
            self.cipsecendpthistentry = YList()
            self.cipsecendpthistentry.parent = self
            self.cipsecendpthistentry.name = 'cipsecendpthistentry'


        class Cipsecendpthistentry(object):
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
            	**type**\:   :py:class:`EndpttypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EndpttypeEnum>`
            
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
            	**type**\:   :py:class:`EndpttypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.EndpttypeEnum>`
            
            .. attribute:: cipsecendpthisttunindex
            
            	The index  of the previously active IPsec Phase\-2 Tunnel Table
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'CISCO-IPSEC-FLOW-MONITOR-MIB'
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
                    raise YPYModelError('Key property cipsecendpthistindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecEndPtHistTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecEndPtHistEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecEndPtHistIndex = ' + str(self.cipsecendpthistindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsecendpthisttable.Cipsecendpthistentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecEndPtHistTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cipsecendpthistentry is not None:
                for child_ref in self.cipsecendpthistentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsecendpthisttable']['meta_info']


    class Cikefailtable(object):
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
            self.parent = None
            self.cikefailentry = YList()
            self.cikefailentry.parent = self
            self.cikefailentry.name = 'cikefailentry'


        class Cikefailentry(object):
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
            	**type**\:   :py:class:`IkepeertypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkepeertypeEnum>`
            
            .. attribute:: cikefaillocalvalue
            
            	The value of the local peer identity.  If the local peer type is an IP Address, then this is the IP Address used to identify the local peer.  If the local peer type is a host name, then this is the host name used to identify the local peer
            	**type**\:  str
            
            .. attribute:: cikefailreason
            
            	The reason for the failure.  Possible reasons include\: 1 = other 2 = peer delete request was received 3 = contact with peer was lost 4 = local failure occurred 5 = authentication failure 6 = hash validation failure 7 = encryption failure 8 = internal error occurred 9 = system capacity failure 10 = proposal failure 11 = peer's certificate is unavailable 12 = peer's certificate was found invalid 13 = local certificate expired 14 = certificate revoke list (crl) failure 15 = peer encoding error 16 = non\-existent security association 17 = operator requested termination
            	**type**\:   :py:class:`CikefailreasonEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cikefailtable.Cikefailentry.CikefailreasonEnum>`
            
            .. attribute:: cikefailremoteaddr
            
            	The IP address of the remote peer
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cikefailremotetype
            
            	The type of remote peer identity.  The remote peer may be identified by\:  1. an IP address, or  2. a host name
            	**type**\:   :py:class:`IkepeertypeEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.IkepeertypeEnum>`
            
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

            class CikefailreasonEnum(Enum):
                """
                CikefailreasonEnum

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

                other = 1

                peerDelRequest = 2

                peerLost = 3

                localFailure = 4

                authFailure = 5

                hashValidation = 6

                encryptFailure = 7

                internalError = 8

                sysCapExceeded = 9

                proposalFailure = 10

                peerCertUnavailable = 11

                peerCertNotValid = 12

                localCertExpired = 13

                crlFailure = 14

                peerEncodingError = 15

                nonExistentSa = 16

                operRequest = 17


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                    return meta._meta_table['CiscoIpsecFlowMonitorMib.Cikefailtable.Cikefailentry.CikefailreasonEnum']


            @property
            def _common_path(self):
                if self.cikefailindex is None:
                    raise YPYModelError('Key property cikefailindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeFailTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeFailEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cikeFailIndex = ' + str(self.cikefailindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CiscoIpsecFlowMonitorMib.Cikefailtable.Cikefailentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cikeFailTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cikefailentry is not None:
                for child_ref in self.cikefailentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Cikefailtable']['meta_info']


    class Cipsecfailtable(object):
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
            self.parent = None
            self.cipsecfailentry = YList()
            self.cipsecfailentry.parent = self
            self.cipsecfailentry.name = 'cipsecfailentry'


        class Cipsecfailentry(object):
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
            	**type**\:   :py:class:`CipsecfailreasonEnum <ydk.models.cisco_ios_xe.CISCO_IPSEC_FLOW_MONITOR_MIB.CiscoIpsecFlowMonitorMib.Cipsecfailtable.Cipsecfailentry.CipsecfailreasonEnum>`
            
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
                self.parent = None
                self.cipsecfailindex = None
                self.cipsecfailpktdstaddr = None
                self.cipsecfailpktsrcaddr = None
                self.cipsecfailreason = None
                self.cipsecfailsaspi = None
                self.cipsecfailtime = None
                self.cipsecfailtunnelindex = None

            class CipsecfailreasonEnum(Enum):
                """
                CipsecfailreasonEnum

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

                other = 1

                internalError = 2

                peerEncodingError = 3

                proposalFailure = 4

                protocolUseFail = 5

                nonExistentSa = 6

                decryptFailure = 7

                encryptFailure = 8

                inAuthFailure = 9

                outAuthFailure = 10

                compression = 11

                sysCapExceeded = 12

                peerDelRequest = 13

                peerLost = 14

                seqNumRollOver = 15

                operRequest = 16


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                    return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsecfailtable.Cipsecfailentry.CipsecfailreasonEnum']


            @property
            def _common_path(self):
                if self.cipsecfailindex is None:
                    raise YPYModelError('Key property cipsecfailindex is None')

                return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecFailTable/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecFailEntry[CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecFailIndex = ' + str(self.cipsecfailindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
                return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsecfailtable.Cipsecfailentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB/CISCO-IPSEC-FLOW-MONITOR-MIB:cipSecFailTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cipsecfailentry is not None:
                for child_ref in self.cipsecfailentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
            return meta._meta_table['CiscoIpsecFlowMonitorMib.Cipsecfailtable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IPSEC-FLOW-MONITOR-MIB:CISCO-IPSEC-FLOW-MONITOR-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cikefailtable is not None and self.cikefailtable._has_data():
            return True

        if self.cikeglobalstats is not None and self.cikeglobalstats._has_data():
            return True

        if self.cikepeercorrtable is not None and self.cikepeercorrtable._has_data():
            return True

        if self.cikepeertable is not None and self.cikepeertable._has_data():
            return True

        if self.cikephase1gwstatstable is not None and self.cikephase1gwstatstable._has_data():
            return True

        if self.ciketunnelhisttable is not None and self.ciketunnelhisttable._has_data():
            return True

        if self.ciketunneltable is not None and self.ciketunneltable._has_data():
            return True

        if self.cipsecendpthisttable is not None and self.cipsecendpthisttable._has_data():
            return True

        if self.cipsecendpttable is not None and self.cipsecendpttable._has_data():
            return True

        if self.cipsecfailglobalcntl is not None and self.cipsecfailglobalcntl._has_data():
            return True

        if self.cipsecfailtable is not None and self.cipsecfailtable._has_data():
            return True

        if self.cipsecglobalstats is not None and self.cipsecglobalstats._has_data():
            return True

        if self.cipsechistglobalcntl is not None and self.cipsechistglobalcntl._has_data():
            return True

        if self.cipseclevels is not None and self.cipseclevels._has_data():
            return True

        if self.cipsecphase2gwstatstable is not None and self.cipsecphase2gwstatstable._has_data():
            return True

        if self.cipsecspitable is not None and self.cipsecspitable._has_data():
            return True

        if self.cipsectrapcntl is not None and self.cipsectrapcntl._has_data():
            return True

        if self.cipsectunnelhisttable is not None and self.cipsectunnelhisttable._has_data():
            return True

        if self.cipsectunneltable is not None and self.cipsectunneltable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_FLOW_MONITOR_MIB as meta
        return meta._meta_table['CiscoIpsecFlowMonitorMib']['meta_info']


