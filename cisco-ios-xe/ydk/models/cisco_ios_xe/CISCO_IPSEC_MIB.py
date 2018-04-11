""" CISCO_IPSEC_MIB 

The MIB module for modeling Cisco\-specific 
IPsec attributes

Overview of Cisco IPsec MIB

MIB description

This MIB models the Cisco implementation\-specific 
attributes of a Cisco entity that implements IPsec. 
This MIB is complementary to the standard IPsec MIB 
proposed jointly by Tivoli and Cisco.

The ciscoIPsec MIB provides the operational information 
on Cisco's IPsec tunnelling implementation.  
The following entities are managed\:
1) ISAKMP Group\:
a) ISAKMP global parameters
b) ISAKMP Policy Table

2) IPSec Group\:
a) IPSec Global Parameters
b) IPSec Global Traffic Parameters
c) Cryptomap Group
\- Cryptomap Set Table
\- Cryptomap Table
\- CryptomapSet Binding Table

3) System Capacity & Capability Group\:
a) Capacity Parameters
b) Capability Parameters

4) Trap Control Group
5) Notifications Group

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CryptomapSetBindStatus(Enum):
    """
    CryptomapSetBindStatus (Enum Class)

    The status of the binding of a cryptomap set 

    to the specified interface. The value qhen queried

    is always 'attached'. When set to 'detached', the 

    cryptomap set if detached from the specified interface.

    Setting the value to 'attached' will result in 

    SNMP General Error.

    .. data:: unknown = 0

    .. data:: attached = 1

    .. data:: detached = 2

    """

    unknown = Enum.YLeaf(0, "unknown")

    attached = Enum.YLeaf(1, "attached")

    detached = Enum.YLeaf(2, "detached")


class CryptomapType(Enum):
    """
    CryptomapType (Enum Class)

    The type of a cryptomap entry. Cryptomap 

    is a unit of IOS IPSec policy specification.

    .. data:: cryptomapTypeNONE = 0

    .. data:: cryptomapTypeMANUAL = 1

    .. data:: cryptomapTypeISAKMP = 2

    .. data:: cryptomapTypeCET = 3

    .. data:: cryptomapTypeDYNAMIC = 4

    .. data:: cryptomapTypeDYNAMICDISCOVERY = 5

    """

    cryptomapTypeNONE = Enum.YLeaf(0, "cryptomapTypeNONE")

    cryptomapTypeMANUAL = Enum.YLeaf(1, "cryptomapTypeMANUAL")

    cryptomapTypeISAKMP = Enum.YLeaf(2, "cryptomapTypeISAKMP")

    cryptomapTypeCET = Enum.YLeaf(3, "cryptomapTypeCET")

    cryptomapTypeDYNAMIC = Enum.YLeaf(4, "cryptomapTypeDYNAMIC")

    cryptomapTypeDYNAMICDISCOVERY = Enum.YLeaf(5, "cryptomapTypeDYNAMICDISCOVERY")


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


class IkeIdentityType(Enum):
    """
    IkeIdentityType (Enum Class)

    The type of identity used by the local entity to

    identity itself to the peer with which it performs

    IPSec Main Mode negotiations. This type decides the

    content of the Identification payload in the

    	Main Mode of IPSec tunnel setup.

    .. data:: isakmpIdTypeUNKNOWN = 0

    .. data:: isakmpIdTypeADDRESS = 1

    .. data:: isakmpIdTypeHOSTNAME = 2

    """

    isakmpIdTypeUNKNOWN = Enum.YLeaf(0, "isakmpIdTypeUNKNOWN")

    isakmpIdTypeADDRESS = Enum.YLeaf(1, "isakmpIdTypeADDRESS")

    isakmpIdTypeHOSTNAME = Enum.YLeaf(2, "isakmpIdTypeHOSTNAME")


class TrapStatus(Enum):
    """
    TrapStatus (Enum Class)

    The administrative status for sending a TRAP.

    .. data:: enabled = 1

    .. data:: disabled = 2

    """

    enabled = Enum.YLeaf(1, "enabled")

    disabled = Enum.YLeaf(2, "disabled")



class CISCOIPSECMIB(Entity):
    """
    
    
    .. attribute:: cipsisakmpgroup
    
    	
    	**type**\:  :py:class:`Cipsisakmpgroup <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CISCOIPSECMIB.Cipsisakmpgroup>`
    
    .. attribute:: cipsipsecglobals
    
    	
    	**type**\:  :py:class:`Cipsipsecglobals <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CISCOIPSECMIB.Cipsipsecglobals>`
    
    .. attribute:: cipsipsecstatistics
    
    	
    	**type**\:  :py:class:`Cipsipsecstatistics <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CISCOIPSECMIB.Cipsipsecstatistics>`
    
    .. attribute:: cipssyscapacitygroup
    
    	
    	**type**\:  :py:class:`Cipssyscapacitygroup <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CISCOIPSECMIB.Cipssyscapacitygroup>`
    
    .. attribute:: cipstrapcntlgroup
    
    	
    	**type**\:  :py:class:`Cipstrapcntlgroup <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CISCOIPSECMIB.Cipstrapcntlgroup>`
    
    .. attribute:: cipsisakmppolicytable
    
    	The table containing the list of all ISAKMP policy entries configured by the operator
    	**type**\:  :py:class:`Cipsisakmppolicytable <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CISCOIPSECMIB.Cipsisakmppolicytable>`
    
    .. attribute:: cipsstaticcryptomapsettable
    
    	The table containing the list of all cryptomap sets that are fully specified and are not wild\-carded.  The operator may include different types of cryptomaps in such a set \- manual, CET, ISAKMP or dynamic
    	**type**\:  :py:class:`Cipsstaticcryptomapsettable <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CISCOIPSECMIB.Cipsstaticcryptomapsettable>`
    
    .. attribute:: cipsdynamiccryptomapsettable
    
    	The table containing the list of all dynamic cryptomaps that use IKE, defined on   the managed entity
    	**type**\:  :py:class:`Cipsdynamiccryptomapsettable <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CISCOIPSECMIB.Cipsdynamiccryptomapsettable>`
    
    .. attribute:: cipsstaticcryptomaptable
    
    	The table ilisting the member cryptomaps of the cryptomap sets that are configured on the managed entity
    	**type**\:  :py:class:`Cipsstaticcryptomaptable <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CISCOIPSECMIB.Cipsstaticcryptomaptable>`
    
    .. attribute:: cipscryptomapsetiftable
    
    	The table lists the binding of cryptomap sets to the interfaces of the managed entity
    	**type**\:  :py:class:`Cipscryptomapsetiftable <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CISCOIPSECMIB.Cipscryptomapsetiftable>`
    
    

    """

    _prefix = 'CISCO-IPSEC-MIB'
    _revision = '2000-08-07'

    def __init__(self):
        super(CISCOIPSECMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IPSEC-MIB"
        self.yang_parent_name = "CISCO-IPSEC-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cipsIsakmpGroup", ("cipsisakmpgroup", CISCOIPSECMIB.Cipsisakmpgroup)), ("cipsIPsecGlobals", ("cipsipsecglobals", CISCOIPSECMIB.Cipsipsecglobals)), ("cipsIPsecStatistics", ("cipsipsecstatistics", CISCOIPSECMIB.Cipsipsecstatistics)), ("cipsSysCapacityGroup", ("cipssyscapacitygroup", CISCOIPSECMIB.Cipssyscapacitygroup)), ("cipsTrapCntlGroup", ("cipstrapcntlgroup", CISCOIPSECMIB.Cipstrapcntlgroup)), ("cipsIsakmpPolicyTable", ("cipsisakmppolicytable", CISCOIPSECMIB.Cipsisakmppolicytable)), ("cipsStaticCryptomapSetTable", ("cipsstaticcryptomapsettable", CISCOIPSECMIB.Cipsstaticcryptomapsettable)), ("cipsDynamicCryptomapSetTable", ("cipsdynamiccryptomapsettable", CISCOIPSECMIB.Cipsdynamiccryptomapsettable)), ("cipsStaticCryptomapTable", ("cipsstaticcryptomaptable", CISCOIPSECMIB.Cipsstaticcryptomaptable)), ("cipsCryptomapSetIfTable", ("cipscryptomapsetiftable", CISCOIPSECMIB.Cipscryptomapsetiftable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cipsisakmpgroup = CISCOIPSECMIB.Cipsisakmpgroup()
        self.cipsisakmpgroup.parent = self
        self._children_name_map["cipsisakmpgroup"] = "cipsIsakmpGroup"
        self._children_yang_names.add("cipsIsakmpGroup")

        self.cipsipsecglobals = CISCOIPSECMIB.Cipsipsecglobals()
        self.cipsipsecglobals.parent = self
        self._children_name_map["cipsipsecglobals"] = "cipsIPsecGlobals"
        self._children_yang_names.add("cipsIPsecGlobals")

        self.cipsipsecstatistics = CISCOIPSECMIB.Cipsipsecstatistics()
        self.cipsipsecstatistics.parent = self
        self._children_name_map["cipsipsecstatistics"] = "cipsIPsecStatistics"
        self._children_yang_names.add("cipsIPsecStatistics")

        self.cipssyscapacitygroup = CISCOIPSECMIB.Cipssyscapacitygroup()
        self.cipssyscapacitygroup.parent = self
        self._children_name_map["cipssyscapacitygroup"] = "cipsSysCapacityGroup"
        self._children_yang_names.add("cipsSysCapacityGroup")

        self.cipstrapcntlgroup = CISCOIPSECMIB.Cipstrapcntlgroup()
        self.cipstrapcntlgroup.parent = self
        self._children_name_map["cipstrapcntlgroup"] = "cipsTrapCntlGroup"
        self._children_yang_names.add("cipsTrapCntlGroup")

        self.cipsisakmppolicytable = CISCOIPSECMIB.Cipsisakmppolicytable()
        self.cipsisakmppolicytable.parent = self
        self._children_name_map["cipsisakmppolicytable"] = "cipsIsakmpPolicyTable"
        self._children_yang_names.add("cipsIsakmpPolicyTable")

        self.cipsstaticcryptomapsettable = CISCOIPSECMIB.Cipsstaticcryptomapsettable()
        self.cipsstaticcryptomapsettable.parent = self
        self._children_name_map["cipsstaticcryptomapsettable"] = "cipsStaticCryptomapSetTable"
        self._children_yang_names.add("cipsStaticCryptomapSetTable")

        self.cipsdynamiccryptomapsettable = CISCOIPSECMIB.Cipsdynamiccryptomapsettable()
        self.cipsdynamiccryptomapsettable.parent = self
        self._children_name_map["cipsdynamiccryptomapsettable"] = "cipsDynamicCryptomapSetTable"
        self._children_yang_names.add("cipsDynamicCryptomapSetTable")

        self.cipsstaticcryptomaptable = CISCOIPSECMIB.Cipsstaticcryptomaptable()
        self.cipsstaticcryptomaptable.parent = self
        self._children_name_map["cipsstaticcryptomaptable"] = "cipsStaticCryptomapTable"
        self._children_yang_names.add("cipsStaticCryptomapTable")

        self.cipscryptomapsetiftable = CISCOIPSECMIB.Cipscryptomapsetiftable()
        self.cipscryptomapsetiftable.parent = self
        self._children_name_map["cipscryptomapsetiftable"] = "cipsCryptomapSetIfTable"
        self._children_yang_names.add("cipsCryptomapSetIfTable")
        self._segment_path = lambda: "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB"


    class Cipsisakmpgroup(Entity):
        """
        
        
        .. attribute:: cipsisakmpenabled
        
        	The value of this object is TRUE if ISAKMP has been enabled on the managed entity. Otherise the value of this object is FALSE
        	**type**\: bool
        
        .. attribute:: cipsisakmpidentity
        
        	The value of this object is shows the type of identity used by the managed entity in ISAKMP negotiations with another peer
        	**type**\:  :py:class:`IkeIdentityType <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.IkeIdentityType>`
        
        .. attribute:: cipsisakmpkeepaliveinterval
        
        	The value of this object is time interval in seconds between successive ISAKMP keepalive heartbeats issued to the peers to which IKE tunnels have been setup
        	**type**\: int
        
        	**range:** 10..3600
        
        	**units**\: seconds
        
        .. attribute:: cipsnumisakmppolicies
        
        	The value of this object is the number of ISAKMP policies that have been configured on the  managed entity
        	**type**\: int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CISCOIPSECMIB.Cipsisakmpgroup, self).__init__()

            self.yang_name = "cipsIsakmpGroup"
            self.yang_parent_name = "CISCO-IPSEC-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cipsisakmpenabled', YLeaf(YType.boolean, 'cipsIsakmpEnabled')),
                ('cipsisakmpidentity', YLeaf(YType.enumeration, 'cipsIsakmpIdentity')),
                ('cipsisakmpkeepaliveinterval', YLeaf(YType.int32, 'cipsIsakmpKeepaliveInterval')),
                ('cipsnumisakmppolicies', YLeaf(YType.int32, 'cipsNumIsakmpPolicies')),
            ])
            self.cipsisakmpenabled = None
            self.cipsisakmpidentity = None
            self.cipsisakmpkeepaliveinterval = None
            self.cipsnumisakmppolicies = None
            self._segment_path = lambda: "cipsIsakmpGroup"
            self._absolute_path = lambda: "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECMIB.Cipsisakmpgroup, ['cipsisakmpenabled', 'cipsisakmpidentity', 'cipsisakmpkeepaliveinterval', 'cipsnumisakmppolicies'], name, value)


    class Cipsipsecglobals(Entity):
        """
        
        
        .. attribute:: cipssalifetime
        
        	The default lifetime (in seconds) assigned  to an SA as a global policy (maybe overridden  in specific cryptomap definitions)
        	**type**\: int
        
        	**range:** 120..86400
        
        	**units**\: Seconds
        
        .. attribute:: cipssalifesize
        
        	The default lifesize in KBytes assigned to an SA  as a global policy (unless overridden in cryptomap  definition)
        	**type**\: int
        
        	**range:** 2560..536870912
        
        	**units**\: KBytes
        
        .. attribute:: cipsnumstaticcryptomapsets
        
        	The number of Cryptomap Sets that are are fully configured. Statically defined cryptomap sets  are ones where the operator has fully specified all the parameters required set up IPSec  Virtual Private Networks (VPNs)
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**units**\: Integral Units
        
        .. attribute:: cipsnumcetcryptomapsets
        
        	The number of static Cryptomap Sets that have  at least one CET cryptomap element as a member of the set
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**units**\: Integral Units
        
        .. attribute:: cipsnumdynamiccryptomapsets
        
        	The number of dynamic IPSec Policy templates (called 'dynamic cryptomap templates') configured on the managed entity
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**units**\: Integral Units
        
        .. attribute:: cipsnumtedcryptomapsets
        
        	The number of static Cryptomap Sets that have  at least one dynamic cryptomap template  bound to them which has the Tunnel Endpoint Discovery (TED) enabled
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**units**\: Integral Units
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CISCOIPSECMIB.Cipsipsecglobals, self).__init__()

            self.yang_name = "cipsIPsecGlobals"
            self.yang_parent_name = "CISCO-IPSEC-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cipssalifetime', YLeaf(YType.uint32, 'cipsSALifetime')),
                ('cipssalifesize', YLeaf(YType.uint32, 'cipsSALifesize')),
                ('cipsnumstaticcryptomapsets', YLeaf(YType.uint32, 'cipsNumStaticCryptomapSets')),
                ('cipsnumcetcryptomapsets', YLeaf(YType.uint32, 'cipsNumCETCryptomapSets')),
                ('cipsnumdynamiccryptomapsets', YLeaf(YType.uint32, 'cipsNumDynamicCryptomapSets')),
                ('cipsnumtedcryptomapsets', YLeaf(YType.uint32, 'cipsNumTEDCryptomapSets')),
            ])
            self.cipssalifetime = None
            self.cipssalifesize = None
            self.cipsnumstaticcryptomapsets = None
            self.cipsnumcetcryptomapsets = None
            self.cipsnumdynamiccryptomapsets = None
            self.cipsnumtedcryptomapsets = None
            self._segment_path = lambda: "cipsIPsecGlobals"
            self._absolute_path = lambda: "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECMIB.Cipsipsecglobals, ['cipssalifetime', 'cipssalifesize', 'cipsnumstaticcryptomapsets', 'cipsnumcetcryptomapsets', 'cipsnumdynamiccryptomapsets', 'cipsnumtedcryptomapsets'], name, value)


    class Cipsipsecstatistics(Entity):
        """
        
        
        .. attribute:: cipsnumtedprobesreceived
        
        	The number of TED probes that were received by this  managed entity since bootup. Not affected by any  CLI operation
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Integral Units
        
        .. attribute:: cipsnumtedprobessent
        
        	The number of TED probes that were dispatched by all the dynamic cryptomaps in this managed entity since  bootup. Not affected by any CLI operation
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Integral Units
        
        .. attribute:: cipsnumtedfailures
        
        	The number of TED probes that were dispatched by  the local entity and that failed to locate crypto  endpoint.  Not affected by any CLI operation
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: Integral Units
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CISCOIPSECMIB.Cipsipsecstatistics, self).__init__()

            self.yang_name = "cipsIPsecStatistics"
            self.yang_parent_name = "CISCO-IPSEC-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cipsnumtedprobesreceived', YLeaf(YType.uint32, 'cipsNumTEDProbesReceived')),
                ('cipsnumtedprobessent', YLeaf(YType.uint32, 'cipsNumTEDProbesSent')),
                ('cipsnumtedfailures', YLeaf(YType.uint32, 'cipsNumTEDFailures')),
            ])
            self.cipsnumtedprobesreceived = None
            self.cipsnumtedprobessent = None
            self.cipsnumtedfailures = None
            self._segment_path = lambda: "cipsIPsecStatistics"
            self._absolute_path = lambda: "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECMIB.Cipsipsecstatistics, ['cipsnumtedprobesreceived', 'cipsnumtedprobessent', 'cipsnumtedfailures'], name, value)


    class Cipssyscapacitygroup(Entity):
        """
        
        
        .. attribute:: cipsmaxsas
        
        	The maximum number of IPsec Security Associations that can be established on this managed entity. If no theoretical limit exists, this returns value 0.  Not affected by any CLI operation
        	**type**\: int
        
        	**range:** 0..65535
        
        	**units**\: Integral Units
        
        .. attribute:: cips3descapable
        
        	The value of this object is TRUE if the  managed entity has the hardware nad software  features to support 3DES encryption algorithm.  Not affected by any CLI operation
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CISCOIPSECMIB.Cipssyscapacitygroup, self).__init__()

            self.yang_name = "cipsSysCapacityGroup"
            self.yang_parent_name = "CISCO-IPSEC-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cipsmaxsas', YLeaf(YType.int32, 'cipsMaxSAs')),
                ('cips3descapable', YLeaf(YType.boolean, 'cips3DesCapable')),
            ])
            self.cipsmaxsas = None
            self.cips3descapable = None
            self._segment_path = lambda: "cipsSysCapacityGroup"
            self._absolute_path = lambda: "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECMIB.Cipssyscapacitygroup, ['cipsmaxsas', 'cips3descapable'], name, value)


    class Cipstrapcntlgroup(Entity):
        """
        
        
        .. attribute:: cipscntlisakmppolicyadded
        
        	This object defines the administrative state of  sending the IOS IPsec ISAKMP Policy Add trap
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.TrapStatus>`
        
        .. attribute:: cipscntlisakmppolicydeleted
        
        	This object defines the administrative state of  sending the IOS IPsec ISAKMP Policy Delete trap
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.TrapStatus>`
        
        .. attribute:: cipscntlcryptomapadded
        
        	This object defines the administrative state of  sending the IOS IPsec Cryptomap Add trap
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.TrapStatus>`
        
        .. attribute:: cipscntlcryptomapdeleted
        
        	This object defines the administrative state of  sending the IOS IPsec Cryptomap Delete trap
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.TrapStatus>`
        
        .. attribute:: cipscntlcryptomapsetattached
        
        	This object defines the administrative state of  sending the IOS IPsec trap that is issued when a cryptomap set is attached to an interface
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.TrapStatus>`
        
        .. attribute:: cipscntlcryptomapsetdetached
        
        	This object defines the administrative state of  sending the IOS IPsec trap that is issued when a cryptomap set is detached from an interface. to which it was earlier bound
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.TrapStatus>`
        
        .. attribute:: cipscntltoomanysas
        
        	This object defines the administrative state of  sending the IOS IPsec trap that is issued when the number of SAs crosses the maximum number of SAs that may be supported on the managed entity
        	**type**\:  :py:class:`TrapStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.TrapStatus>`
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CISCOIPSECMIB.Cipstrapcntlgroup, self).__init__()

            self.yang_name = "cipsTrapCntlGroup"
            self.yang_parent_name = "CISCO-IPSEC-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cipscntlisakmppolicyadded', YLeaf(YType.enumeration, 'cipsCntlIsakmpPolicyAdded')),
                ('cipscntlisakmppolicydeleted', YLeaf(YType.enumeration, 'cipsCntlIsakmpPolicyDeleted')),
                ('cipscntlcryptomapadded', YLeaf(YType.enumeration, 'cipsCntlCryptomapAdded')),
                ('cipscntlcryptomapdeleted', YLeaf(YType.enumeration, 'cipsCntlCryptomapDeleted')),
                ('cipscntlcryptomapsetattached', YLeaf(YType.enumeration, 'cipsCntlCryptomapSetAttached')),
                ('cipscntlcryptomapsetdetached', YLeaf(YType.enumeration, 'cipsCntlCryptomapSetDetached')),
                ('cipscntltoomanysas', YLeaf(YType.enumeration, 'cipsCntlTooManySAs')),
            ])
            self.cipscntlisakmppolicyadded = None
            self.cipscntlisakmppolicydeleted = None
            self.cipscntlcryptomapadded = None
            self.cipscntlcryptomapdeleted = None
            self.cipscntlcryptomapsetattached = None
            self.cipscntlcryptomapsetdetached = None
            self.cipscntltoomanysas = None
            self._segment_path = lambda: "cipsTrapCntlGroup"
            self._absolute_path = lambda: "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECMIB.Cipstrapcntlgroup, ['cipscntlisakmppolicyadded', 'cipscntlisakmppolicydeleted', 'cipscntlcryptomapadded', 'cipscntlcryptomapdeleted', 'cipscntlcryptomapsetattached', 'cipscntlcryptomapsetdetached', 'cipscntltoomanysas'], name, value)


    class Cipsisakmppolicytable(Entity):
        """
        The table containing the list of all
        ISAKMP policy entries configured by the operator.
        
        .. attribute:: cipsisakmppolicyentry
        
        	Each entry contains the attributes  associated with a single ISAKMP Policy entry
        	**type**\: list of  		 :py:class:`Cipsisakmppolicyentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CISCOIPSECMIB.Cipsisakmppolicytable.Cipsisakmppolicyentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CISCOIPSECMIB.Cipsisakmppolicytable, self).__init__()

            self.yang_name = "cipsIsakmpPolicyTable"
            self.yang_parent_name = "CISCO-IPSEC-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipsIsakmpPolicyEntry", ("cipsisakmppolicyentry", CISCOIPSECMIB.Cipsisakmppolicytable.Cipsisakmppolicyentry))])
            self._leafs = OrderedDict()

            self.cipsisakmppolicyentry = YList(self)
            self._segment_path = lambda: "cipsIsakmpPolicyTable"
            self._absolute_path = lambda: "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECMIB.Cipsisakmppolicytable, [], name, value)


        class Cipsisakmppolicyentry(Entity):
            """
            Each entry contains the attributes 
            associated with a single ISAKMP
            Policy entry.
            
            .. attribute:: cipsisakmppolpriority  (key)
            
            	The priotity of this ISAKMP Policy entry. This is also the index of this table
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cipsisakmppolencr
            
            	The encryption transform specified by this  ISAKMP policy specification. The Internet Key Exchange (IKE) tunnels setup using this policy item would use the specified encryption transform to protect the ISAKMP PDUs
            	**type**\:  :py:class:`EncryptAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.EncryptAlgo>`
            
            .. attribute:: cipsisakmppolhash
            
            	The hash transform specified by this  ISAKMP policy specification. The IKE tunnels setup using this policy item would use the  specified hash transform to protect the ISAKMP PDUs
            	**type**\:  :py:class:`IkeHashAlgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.IkeHashAlgo>`
            
            .. attribute:: cipsisakmppolauth
            
            	The peer authentication mthod specified by this ISAKMP policy specification. If this policy entity is selected for negotiation with a peer, the local entity would authenticate the peer using  the method specified by this object
            	**type**\:  :py:class:`IkeAuthMethod <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.IkeAuthMethod>`
            
            .. attribute:: cipsisakmppolgroup
            
            	This object specifies the Oakley group used  for Diffie Hellman exchange in the Main Mode.  If this policy item is selected to negotiate Main Mode with an IKE peer, the local entity  chooses the group specified by this object to perform Diffie Hellman exchange with the peer
            	**type**\:  :py:class:`DiffHellmanGrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.DiffHellmanGrp>`
            
            .. attribute:: cipsisakmppollifetime
            
            	This object specifies the lifetime in seconds of the IKE tunnels generated using this  policy specification
            	**type**\: int
            
            	**range:** 60..86400
            
            	**units**\: seconds
            
            

            """

            _prefix = 'CISCO-IPSEC-MIB'
            _revision = '2000-08-07'

            def __init__(self):
                super(CISCOIPSECMIB.Cipsisakmppolicytable.Cipsisakmppolicyentry, self).__init__()

                self.yang_name = "cipsIsakmpPolicyEntry"
                self.yang_parent_name = "cipsIsakmpPolicyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipsisakmppolpriority']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipsisakmppolpriority', YLeaf(YType.int32, 'cipsIsakmpPolPriority')),
                    ('cipsisakmppolencr', YLeaf(YType.enumeration, 'cipsIsakmpPolEncr')),
                    ('cipsisakmppolhash', YLeaf(YType.enumeration, 'cipsIsakmpPolHash')),
                    ('cipsisakmppolauth', YLeaf(YType.enumeration, 'cipsIsakmpPolAuth')),
                    ('cipsisakmppolgroup', YLeaf(YType.enumeration, 'cipsIsakmpPolGroup')),
                    ('cipsisakmppollifetime', YLeaf(YType.int32, 'cipsIsakmpPolLifetime')),
                ])
                self.cipsisakmppolpriority = None
                self.cipsisakmppolencr = None
                self.cipsisakmppolhash = None
                self.cipsisakmppolauth = None
                self.cipsisakmppolgroup = None
                self.cipsisakmppollifetime = None
                self._segment_path = lambda: "cipsIsakmpPolicyEntry" + "[cipsIsakmpPolPriority='" + str(self.cipsisakmppolpriority) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/cipsIsakmpPolicyTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECMIB.Cipsisakmppolicytable.Cipsisakmppolicyentry, ['cipsisakmppolpriority', 'cipsisakmppolencr', 'cipsisakmppolhash', 'cipsisakmppolauth', 'cipsisakmppolgroup', 'cipsisakmppollifetime'], name, value)


    class Cipsstaticcryptomapsettable(Entity):
        """
        The table containing the list of all
        cryptomap sets that are fully specified
        and are not wild\-carded.
        
        The operator may include different types of
        cryptomaps in such a set \- manual, CET,
        ISAKMP or dynamic.
        
        .. attribute:: cipsstaticcryptomapsetentry
        
        	Each entry contains the attributes  associated with a single static  cryptomap set
        	**type**\: list of  		 :py:class:`Cipsstaticcryptomapsetentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CISCOIPSECMIB.Cipsstaticcryptomapsettable.Cipsstaticcryptomapsetentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CISCOIPSECMIB.Cipsstaticcryptomapsettable, self).__init__()

            self.yang_name = "cipsStaticCryptomapSetTable"
            self.yang_parent_name = "CISCO-IPSEC-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipsStaticCryptomapSetEntry", ("cipsstaticcryptomapsetentry", CISCOIPSECMIB.Cipsstaticcryptomapsettable.Cipsstaticcryptomapsetentry))])
            self._leafs = OrderedDict()

            self.cipsstaticcryptomapsetentry = YList(self)
            self._segment_path = lambda: "cipsStaticCryptomapSetTable"
            self._absolute_path = lambda: "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECMIB.Cipsstaticcryptomapsettable, [], name, value)


        class Cipsstaticcryptomapsetentry(Entity):
            """
            Each entry contains the attributes 
            associated with a single static 
            cryptomap set.
            
            .. attribute:: cipsstaticcryptomapsetname  (key)
            
            	The index of the static cryptomap table. The value  of the string is the name string assigned by the  operator in defining the cryptomap set
            	**type**\: str
            
            .. attribute:: cipsstaticcryptomapsetsize
            
            	The total number of cryptomap entries contained in this cryptomap set. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsstaticcryptomapsetnumisakmp
            
            	The number of cryptomaps associated with this  cryptomap set that use ISAKMP protocol to do key exchange
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsstaticcryptomapsetnummanual
            
            	The number of cryptomaps associated with this  cryptomap set that require the operator to manually setup the keys and SPIs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsstaticcryptomapsetnumcet
            
            	The number of cryptomaps of type 'ipsec\-cisco'  associated with this cryptomap set. Such cryptomap elements implement Cisco Encryption Technology based Virtual Private Networks
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsstaticcryptomapsetnumdynamic
            
            	The number of dynamic cryptomap templates linked to this cryptomap set
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsstaticcryptomapsetnumdisc
            
            	The number of dynamic cryptomap templates linked to this cryptomap set that have Tunnel Endpoint Discovery (TED) enabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsstaticcryptomapsetnumsas
            
            	The number of and IPsec Security Associations that are active and were setup using this cryptomap.  
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IPSEC-MIB'
            _revision = '2000-08-07'

            def __init__(self):
                super(CISCOIPSECMIB.Cipsstaticcryptomapsettable.Cipsstaticcryptomapsetentry, self).__init__()

                self.yang_name = "cipsStaticCryptomapSetEntry"
                self.yang_parent_name = "cipsStaticCryptomapSetTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipsstaticcryptomapsetname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipsstaticcryptomapsetname', YLeaf(YType.str, 'cipsStaticCryptomapSetName')),
                    ('cipsstaticcryptomapsetsize', YLeaf(YType.uint32, 'cipsStaticCryptomapSetSize')),
                    ('cipsstaticcryptomapsetnumisakmp', YLeaf(YType.uint32, 'cipsStaticCryptomapSetNumIsakmp')),
                    ('cipsstaticcryptomapsetnummanual', YLeaf(YType.uint32, 'cipsStaticCryptomapSetNumManual')),
                    ('cipsstaticcryptomapsetnumcet', YLeaf(YType.uint32, 'cipsStaticCryptomapSetNumCET')),
                    ('cipsstaticcryptomapsetnumdynamic', YLeaf(YType.uint32, 'cipsStaticCryptomapSetNumDynamic')),
                    ('cipsstaticcryptomapsetnumdisc', YLeaf(YType.uint32, 'cipsStaticCryptomapSetNumDisc')),
                    ('cipsstaticcryptomapsetnumsas', YLeaf(YType.uint32, 'cipsStaticCryptomapSetNumSAs')),
                ])
                self.cipsstaticcryptomapsetname = None
                self.cipsstaticcryptomapsetsize = None
                self.cipsstaticcryptomapsetnumisakmp = None
                self.cipsstaticcryptomapsetnummanual = None
                self.cipsstaticcryptomapsetnumcet = None
                self.cipsstaticcryptomapsetnumdynamic = None
                self.cipsstaticcryptomapsetnumdisc = None
                self.cipsstaticcryptomapsetnumsas = None
                self._segment_path = lambda: "cipsStaticCryptomapSetEntry" + "[cipsStaticCryptomapSetName='" + str(self.cipsstaticcryptomapsetname) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/cipsStaticCryptomapSetTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECMIB.Cipsstaticcryptomapsettable.Cipsstaticcryptomapsetentry, ['cipsstaticcryptomapsetname', 'cipsstaticcryptomapsetsize', 'cipsstaticcryptomapsetnumisakmp', 'cipsstaticcryptomapsetnummanual', 'cipsstaticcryptomapsetnumcet', 'cipsstaticcryptomapsetnumdynamic', 'cipsstaticcryptomapsetnumdisc', 'cipsstaticcryptomapsetnumsas'], name, value)


    class Cipsdynamiccryptomapsettable(Entity):
        """
        The table containing the list of all dynamic
        cryptomaps that use IKE, defined on 
         the managed entity.
        
        .. attribute:: cipsdynamiccryptomapsetentry
        
        	Each entry contains the attributes associated with a single dynamic cryptomap template
        	**type**\: list of  		 :py:class:`Cipsdynamiccryptomapsetentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CISCOIPSECMIB.Cipsdynamiccryptomapsettable.Cipsdynamiccryptomapsetentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CISCOIPSECMIB.Cipsdynamiccryptomapsettable, self).__init__()

            self.yang_name = "cipsDynamicCryptomapSetTable"
            self.yang_parent_name = "CISCO-IPSEC-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipsDynamicCryptomapSetEntry", ("cipsdynamiccryptomapsetentry", CISCOIPSECMIB.Cipsdynamiccryptomapsettable.Cipsdynamiccryptomapsetentry))])
            self._leafs = OrderedDict()

            self.cipsdynamiccryptomapsetentry = YList(self)
            self._segment_path = lambda: "cipsDynamicCryptomapSetTable"
            self._absolute_path = lambda: "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECMIB.Cipsdynamiccryptomapsettable, [], name, value)


        class Cipsdynamiccryptomapsetentry(Entity):
            """
            Each entry contains the attributes associated
            with a single dynamic cryptomap template.
            
            .. attribute:: cipsdynamiccryptomapsetname  (key)
            
            	The index of the dynamic cryptomap table.  The value of the string is the one assigned  by the operator in defining the cryptomap set
            	**type**\: str
            
            .. attribute:: cipsdynamiccryptomapsetsize
            
            	The number of cryptomap entries in this cryptomap
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsdynamiccryptomapsetnumassoc
            
            	The number of static cryptomap sets with which this dynamic cryptomap is associated.  
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IPSEC-MIB'
            _revision = '2000-08-07'

            def __init__(self):
                super(CISCOIPSECMIB.Cipsdynamiccryptomapsettable.Cipsdynamiccryptomapsetentry, self).__init__()

                self.yang_name = "cipsDynamicCryptomapSetEntry"
                self.yang_parent_name = "cipsDynamicCryptomapSetTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipsdynamiccryptomapsetname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipsdynamiccryptomapsetname', YLeaf(YType.str, 'cipsDynamicCryptomapSetName')),
                    ('cipsdynamiccryptomapsetsize', YLeaf(YType.uint32, 'cipsDynamicCryptomapSetSize')),
                    ('cipsdynamiccryptomapsetnumassoc', YLeaf(YType.uint32, 'cipsDynamicCryptomapSetNumAssoc')),
                ])
                self.cipsdynamiccryptomapsetname = None
                self.cipsdynamiccryptomapsetsize = None
                self.cipsdynamiccryptomapsetnumassoc = None
                self._segment_path = lambda: "cipsDynamicCryptomapSetEntry" + "[cipsDynamicCryptomapSetName='" + str(self.cipsdynamiccryptomapsetname) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/cipsDynamicCryptomapSetTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECMIB.Cipsdynamiccryptomapsettable.Cipsdynamiccryptomapsetentry, ['cipsdynamiccryptomapsetname', 'cipsdynamiccryptomapsetsize', 'cipsdynamiccryptomapsetnumassoc'], name, value)


    class Cipsstaticcryptomaptable(Entity):
        """
        The table ilisting the member cryptomaps
        of the cryptomap sets that are configured
        on the managed entity.
        
        .. attribute:: cipsstaticcryptomapentry
        
        	Each entry contains the attributes  associated with a single static  (fully specified) cryptomap entry. This table does not include the members  of dynamic cryptomap sets that may be linked with the parent static cryptomap set
        	**type**\: list of  		 :py:class:`Cipsstaticcryptomapentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CISCOIPSECMIB.Cipsstaticcryptomaptable.Cipsstaticcryptomapentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CISCOIPSECMIB.Cipsstaticcryptomaptable, self).__init__()

            self.yang_name = "cipsStaticCryptomapTable"
            self.yang_parent_name = "CISCO-IPSEC-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipsStaticCryptomapEntry", ("cipsstaticcryptomapentry", CISCOIPSECMIB.Cipsstaticcryptomaptable.Cipsstaticcryptomapentry))])
            self._leafs = OrderedDict()

            self.cipsstaticcryptomapentry = YList(self)
            self._segment_path = lambda: "cipsStaticCryptomapTable"
            self._absolute_path = lambda: "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECMIB.Cipsstaticcryptomaptable, [], name, value)


        class Cipsstaticcryptomapentry(Entity):
            """
            Each entry contains the attributes 
            associated with a single static 
            (fully specified) cryptomap entry.
            This table does not include the members 
            of dynamic cryptomap sets that may be
            linked with the parent static cryptomap set.
            
            .. attribute:: cipsstaticcryptomapsetname  (key)
            
            	
            	**type**\: str
            
            	**refers to**\:  :py:class:`cipsstaticcryptomapsetname <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CISCOIPSECMIB.Cipsstaticcryptomapsettable.Cipsstaticcryptomapsetentry>`
            
            .. attribute:: cipsstaticcryptomappriority  (key)
            
            	The priority of the cryptomap entry in the  cryptomap set. This is the second index component of this table
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cipsstaticcryptomaptype
            
            	The type of the cryptomap entry. This can be an ISAKMP cryptomap, CET or manual. Dynamic cryptomaps are not counted in this table
            	**type**\:  :py:class:`CryptomapType <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CryptomapType>`
            
            .. attribute:: cipsstaticcryptomapdescr
            
            	The description string entered by the operatoir while creating this cryptomap. The string generally identifies a description and the purpose of this policy
            	**type**\: str
            
            .. attribute:: cipsstaticcryptomappeer
            
            	The IP address of the current peer associated with  this IPSec policy item. Traffic that is protected by this cryptomap is protected by a tunnel that terminates at the device whose IP address is specified by this object
            	**type**\: str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsstaticcryptomapnumpeers
            
            	The number of peers associated with this cryptomap  entry. The peers other than the one identified by  'cipsStaticCryptomapPeer' are backup peers.   Manual cryptomaps may have only one peer
            	**type**\: int
            
            	**range:** 0..40
            
            .. attribute:: cipsstaticcryptomappfs
            
            	This object identifies if the tunnels instantiated due to this policy item should use Perfect Forward Secrecy  (PFS) and if so, what group of Oakley they should use
            	**type**\:  :py:class:`DiffHellmanGrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.DiffHellmanGrp>`
            
            .. attribute:: cipsstaticcryptomaplifetime
            
            	This object identifies the lifetime of the IPSec Security Associations (SA) created using this IPSec policy entry. If this value is zero, the lifetime assumes the  value specified by the global lifetime parameter
            	**type**\: int
            
            	**range:** 0..None \| 120..86400
            
            .. attribute:: cipsstaticcryptomaplifesize
            
            	This object identifies the lifesize (maximum traffic in bytes that may be carried) of the IPSec SAs created using this IPSec policy entry.  If this value is zero, the lifetime assumes the  value specified by the global lifesize parameter
            	**type**\: int
            
            	**range:** 0..None \| 2560..536870912
            
            .. attribute:: cipsstaticcryptomaplevelhost
            
            	This object identifies the granularity of the IPSec SAs created using this IPSec policy entry.  If this value is TRUE, distinct SA bundles are created for distinct hosts at the end of the application traffic
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-IPSEC-MIB'
            _revision = '2000-08-07'

            def __init__(self):
                super(CISCOIPSECMIB.Cipsstaticcryptomaptable.Cipsstaticcryptomapentry, self).__init__()

                self.yang_name = "cipsStaticCryptomapEntry"
                self.yang_parent_name = "cipsStaticCryptomapTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipsstaticcryptomapsetname','cipsstaticcryptomappriority']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipsstaticcryptomapsetname', YLeaf(YType.str, 'cipsStaticCryptomapSetName')),
                    ('cipsstaticcryptomappriority', YLeaf(YType.int32, 'cipsStaticCryptomapPriority')),
                    ('cipsstaticcryptomaptype', YLeaf(YType.enumeration, 'cipsStaticCryptomapType')),
                    ('cipsstaticcryptomapdescr', YLeaf(YType.str, 'cipsStaticCryptomapDescr')),
                    ('cipsstaticcryptomappeer', YLeaf(YType.str, 'cipsStaticCryptomapPeer')),
                    ('cipsstaticcryptomapnumpeers', YLeaf(YType.int32, 'cipsStaticCryptomapNumPeers')),
                    ('cipsstaticcryptomappfs', YLeaf(YType.enumeration, 'cipsStaticCryptomapPfs')),
                    ('cipsstaticcryptomaplifetime', YLeaf(YType.int32, 'cipsStaticCryptomapLifetime')),
                    ('cipsstaticcryptomaplifesize', YLeaf(YType.int32, 'cipsStaticCryptomapLifesize')),
                    ('cipsstaticcryptomaplevelhost', YLeaf(YType.boolean, 'cipsStaticCryptomapLevelHost')),
                ])
                self.cipsstaticcryptomapsetname = None
                self.cipsstaticcryptomappriority = None
                self.cipsstaticcryptomaptype = None
                self.cipsstaticcryptomapdescr = None
                self.cipsstaticcryptomappeer = None
                self.cipsstaticcryptomapnumpeers = None
                self.cipsstaticcryptomappfs = None
                self.cipsstaticcryptomaplifetime = None
                self.cipsstaticcryptomaplifesize = None
                self.cipsstaticcryptomaplevelhost = None
                self._segment_path = lambda: "cipsStaticCryptomapEntry" + "[cipsStaticCryptomapSetName='" + str(self.cipsstaticcryptomapsetname) + "']" + "[cipsStaticCryptomapPriority='" + str(self.cipsstaticcryptomappriority) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/cipsStaticCryptomapTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECMIB.Cipsstaticcryptomaptable.Cipsstaticcryptomapentry, ['cipsstaticcryptomapsetname', 'cipsstaticcryptomappriority', 'cipsstaticcryptomaptype', 'cipsstaticcryptomapdescr', 'cipsstaticcryptomappeer', 'cipsstaticcryptomapnumpeers', 'cipsstaticcryptomappfs', 'cipsstaticcryptomaplifetime', 'cipsstaticcryptomaplifesize', 'cipsstaticcryptomaplevelhost'], name, value)


    class Cipscryptomapsetiftable(Entity):
        """
        The table lists the binding of cryptomap sets
        to the interfaces of the managed entity.
        
        .. attribute:: cipscryptomapsetifentry
        
        	Each entry contains the record of the association between an interface and a cryptomap set (static) that is defined on the managed entity.  Note that the cryptomap set identified in  this binding must static. Dynamic cryptomaps cannot be bound to interfaces
        	**type**\: list of  		 :py:class:`Cipscryptomapsetifentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CISCOIPSECMIB.Cipscryptomapsetiftable.Cipscryptomapsetifentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CISCOIPSECMIB.Cipscryptomapsetiftable, self).__init__()

            self.yang_name = "cipsCryptomapSetIfTable"
            self.yang_parent_name = "CISCO-IPSEC-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipsCryptomapSetIfEntry", ("cipscryptomapsetifentry", CISCOIPSECMIB.Cipscryptomapsetiftable.Cipscryptomapsetifentry))])
            self._leafs = OrderedDict()

            self.cipscryptomapsetifentry = YList(self)
            self._segment_path = lambda: "cipsCryptomapSetIfTable"
            self._absolute_path = lambda: "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECMIB.Cipscryptomapsetiftable, [], name, value)


        class Cipscryptomapsetifentry(Entity):
            """
            Each entry contains the record of
            the association between an interface
            and a cryptomap set (static) that is defined
            on the managed entity.
            
            Note that the cryptomap set identified in 
            this binding must static. Dynamic cryptomaps cannot
            be bound to interfaces.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cipsstaticcryptomapsetname  (key)
            
            	
            	**type**\: str
            
            	**refers to**\:  :py:class:`cipsstaticcryptomapsetname <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CISCOIPSECMIB.Cipsstaticcryptomapsettable.Cipsstaticcryptomapsetentry>`
            
            .. attribute:: cipscryptomapsetifvirtual
            
            	The value of this object identifies if the interface to which the cryptomap set is attached is a tunnel (such as a GRE or PPTP tunnel)
            	**type**\: bool
            
            .. attribute:: cipscryptomapsetifstatus
            
            	This object identifies the status of the binding  of the specified cryptomap set with the specified interface. The value when queried is always 'attached'.  When set to 'detached', the cryptomap set if detached  from the specified interface. The effect of this is same  as the CLI command  	config\-if# no crypto map cryptomapSetName  Setting the value to 'attached' will result in  SNMP General Error
            	**type**\:  :py:class:`CryptomapSetBindStatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CryptomapSetBindStatus>`
            
            

            """

            _prefix = 'CISCO-IPSEC-MIB'
            _revision = '2000-08-07'

            def __init__(self):
                super(CISCOIPSECMIB.Cipscryptomapsetiftable.Cipscryptomapsetifentry, self).__init__()

                self.yang_name = "cipsCryptomapSetIfEntry"
                self.yang_parent_name = "cipsCryptomapSetIfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','cipsstaticcryptomapsetname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cipsstaticcryptomapsetname', YLeaf(YType.str, 'cipsStaticCryptomapSetName')),
                    ('cipscryptomapsetifvirtual', YLeaf(YType.boolean, 'cipsCryptomapSetIfVirtual')),
                    ('cipscryptomapsetifstatus', YLeaf(YType.enumeration, 'cipsCryptomapSetIfStatus')),
                ])
                self.ifindex = None
                self.cipsstaticcryptomapsetname = None
                self.cipscryptomapsetifvirtual = None
                self.cipscryptomapsetifstatus = None
                self._segment_path = lambda: "cipsCryptomapSetIfEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[cipsStaticCryptomapSetName='" + str(self.cipsstaticcryptomapsetname) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/cipsCryptomapSetIfTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECMIB.Cipscryptomapsetiftable.Cipscryptomapsetifentry, ['ifindex', 'cipsstaticcryptomapsetname', 'cipscryptomapsetifvirtual', 'cipscryptomapsetifstatus'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOIPSECMIB()
        return self._top_entity

