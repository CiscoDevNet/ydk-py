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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Cryptomapsetbindstatus(Enum):
    """
    Cryptomapsetbindstatus

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


class Cryptomaptype(Enum):
    """
    Cryptomaptype

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


class Ikeidentitytype(Enum):
    """
    Ikeidentitytype

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


class Trapstatus(Enum):
    """
    Trapstatus

    The administrative status for sending a TRAP.

    .. data:: enabled = 1

    .. data:: disabled = 2

    """

    enabled = Enum.YLeaf(1, "enabled")

    disabled = Enum.YLeaf(2, "disabled")



class CiscoIpsecMib(Entity):
    """
    
    
    .. attribute:: cipscryptomapsetiftable
    
    	The table lists the binding of cryptomap sets to the interfaces of the managed entity
    	**type**\:   :py:class:`Cipscryptomapsetiftable <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CiscoIpsecMib.Cipscryptomapsetiftable>`
    
    .. attribute:: cipsdynamiccryptomapsettable
    
    	The table containing the list of all dynamic cryptomaps that use IKE, defined on   the managed entity
    	**type**\:   :py:class:`Cipsdynamiccryptomapsettable <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CiscoIpsecMib.Cipsdynamiccryptomapsettable>`
    
    .. attribute:: cipsipsecglobals
    
    	
    	**type**\:   :py:class:`Cipsipsecglobals <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CiscoIpsecMib.Cipsipsecglobals>`
    
    .. attribute:: cipsipsecstatistics
    
    	
    	**type**\:   :py:class:`Cipsipsecstatistics <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CiscoIpsecMib.Cipsipsecstatistics>`
    
    .. attribute:: cipsisakmpgroup
    
    	
    	**type**\:   :py:class:`Cipsisakmpgroup <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CiscoIpsecMib.Cipsisakmpgroup>`
    
    .. attribute:: cipsisakmppolicytable
    
    	The table containing the list of all ISAKMP policy entries configured by the operator
    	**type**\:   :py:class:`Cipsisakmppolicytable <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CiscoIpsecMib.Cipsisakmppolicytable>`
    
    .. attribute:: cipsstaticcryptomapsettable
    
    	The table containing the list of all cryptomap sets that are fully specified and are not wild\-carded.  The operator may include different types of cryptomaps in such a set \- manual, CET, ISAKMP or dynamic
    	**type**\:   :py:class:`Cipsstaticcryptomapsettable <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CiscoIpsecMib.Cipsstaticcryptomapsettable>`
    
    .. attribute:: cipsstaticcryptomaptable
    
    	The table ilisting the member cryptomaps of the cryptomap sets that are configured on the managed entity
    	**type**\:   :py:class:`Cipsstaticcryptomaptable <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CiscoIpsecMib.Cipsstaticcryptomaptable>`
    
    .. attribute:: cipssyscapacitygroup
    
    	
    	**type**\:   :py:class:`Cipssyscapacitygroup <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CiscoIpsecMib.Cipssyscapacitygroup>`
    
    .. attribute:: cipstrapcntlgroup
    
    	
    	**type**\:   :py:class:`Cipstrapcntlgroup <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CiscoIpsecMib.Cipstrapcntlgroup>`
    
    

    """

    _prefix = 'CISCO-IPSEC-MIB'
    _revision = '2000-08-07'

    def __init__(self):
        super(CiscoIpsecMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IPSEC-MIB"
        self.yang_parent_name = "CISCO-IPSEC-MIB"

        self.cipscryptomapsetiftable = CiscoIpsecMib.Cipscryptomapsetiftable()
        self.cipscryptomapsetiftable.parent = self
        self._children_name_map["cipscryptomapsetiftable"] = "cipsCryptomapSetIfTable"
        self._children_yang_names.add("cipsCryptomapSetIfTable")

        self.cipsdynamiccryptomapsettable = CiscoIpsecMib.Cipsdynamiccryptomapsettable()
        self.cipsdynamiccryptomapsettable.parent = self
        self._children_name_map["cipsdynamiccryptomapsettable"] = "cipsDynamicCryptomapSetTable"
        self._children_yang_names.add("cipsDynamicCryptomapSetTable")

        self.cipsipsecglobals = CiscoIpsecMib.Cipsipsecglobals()
        self.cipsipsecglobals.parent = self
        self._children_name_map["cipsipsecglobals"] = "cipsIPsecGlobals"
        self._children_yang_names.add("cipsIPsecGlobals")

        self.cipsipsecstatistics = CiscoIpsecMib.Cipsipsecstatistics()
        self.cipsipsecstatistics.parent = self
        self._children_name_map["cipsipsecstatistics"] = "cipsIPsecStatistics"
        self._children_yang_names.add("cipsIPsecStatistics")

        self.cipsisakmpgroup = CiscoIpsecMib.Cipsisakmpgroup()
        self.cipsisakmpgroup.parent = self
        self._children_name_map["cipsisakmpgroup"] = "cipsIsakmpGroup"
        self._children_yang_names.add("cipsIsakmpGroup")

        self.cipsisakmppolicytable = CiscoIpsecMib.Cipsisakmppolicytable()
        self.cipsisakmppolicytable.parent = self
        self._children_name_map["cipsisakmppolicytable"] = "cipsIsakmpPolicyTable"
        self._children_yang_names.add("cipsIsakmpPolicyTable")

        self.cipsstaticcryptomapsettable = CiscoIpsecMib.Cipsstaticcryptomapsettable()
        self.cipsstaticcryptomapsettable.parent = self
        self._children_name_map["cipsstaticcryptomapsettable"] = "cipsStaticCryptomapSetTable"
        self._children_yang_names.add("cipsStaticCryptomapSetTable")

        self.cipsstaticcryptomaptable = CiscoIpsecMib.Cipsstaticcryptomaptable()
        self.cipsstaticcryptomaptable.parent = self
        self._children_name_map["cipsstaticcryptomaptable"] = "cipsStaticCryptomapTable"
        self._children_yang_names.add("cipsStaticCryptomapTable")

        self.cipssyscapacitygroup = CiscoIpsecMib.Cipssyscapacitygroup()
        self.cipssyscapacitygroup.parent = self
        self._children_name_map["cipssyscapacitygroup"] = "cipsSysCapacityGroup"
        self._children_yang_names.add("cipsSysCapacityGroup")

        self.cipstrapcntlgroup = CiscoIpsecMib.Cipstrapcntlgroup()
        self.cipstrapcntlgroup.parent = self
        self._children_name_map["cipstrapcntlgroup"] = "cipsTrapCntlGroup"
        self._children_yang_names.add("cipsTrapCntlGroup")


    class Cipsisakmpgroup(Entity):
        """
        
        
        .. attribute:: cipsisakmpenabled
        
        	The value of this object is TRUE if ISAKMP has been enabled on the managed entity. Otherise the value of this object is FALSE
        	**type**\:  bool
        
        .. attribute:: cipsisakmpidentity
        
        	The value of this object is shows the type of identity used by the managed entity in ISAKMP negotiations with another peer
        	**type**\:   :py:class:`Ikeidentitytype <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.Ikeidentitytype>`
        
        .. attribute:: cipsisakmpkeepaliveinterval
        
        	The value of this object is time interval in seconds between successive ISAKMP keepalive heartbeats issued to the peers to which IKE tunnels have been setup
        	**type**\:  int
        
        	**range:** 10..3600
        
        	**units**\: seconds
        
        .. attribute:: cipsnumisakmppolicies
        
        	The value of this object is the number of ISAKMP policies that have been configured on the  managed entity
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CiscoIpsecMib.Cipsisakmpgroup, self).__init__()

            self.yang_name = "cipsIsakmpGroup"
            self.yang_parent_name = "CISCO-IPSEC-MIB"

            self.cipsisakmpenabled = YLeaf(YType.boolean, "cipsIsakmpEnabled")

            self.cipsisakmpidentity = YLeaf(YType.enumeration, "cipsIsakmpIdentity")

            self.cipsisakmpkeepaliveinterval = YLeaf(YType.int32, "cipsIsakmpKeepaliveInterval")

            self.cipsnumisakmppolicies = YLeaf(YType.int32, "cipsNumIsakmpPolicies")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cipsisakmpenabled",
                            "cipsisakmpidentity",
                            "cipsisakmpkeepaliveinterval",
                            "cipsnumisakmppolicies") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpsecMib.Cipsisakmpgroup, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecMib.Cipsisakmpgroup, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cipsisakmpenabled.is_set or
                self.cipsisakmpidentity.is_set or
                self.cipsisakmpkeepaliveinterval.is_set or
                self.cipsnumisakmppolicies.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cipsisakmpenabled.yfilter != YFilter.not_set or
                self.cipsisakmpidentity.yfilter != YFilter.not_set or
                self.cipsisakmpkeepaliveinterval.yfilter != YFilter.not_set or
                self.cipsnumisakmppolicies.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipsIsakmpGroup" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cipsisakmpenabled.is_set or self.cipsisakmpenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsisakmpenabled.get_name_leafdata())
            if (self.cipsisakmpidentity.is_set or self.cipsisakmpidentity.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsisakmpidentity.get_name_leafdata())
            if (self.cipsisakmpkeepaliveinterval.is_set or self.cipsisakmpkeepaliveinterval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsisakmpkeepaliveinterval.get_name_leafdata())
            if (self.cipsnumisakmppolicies.is_set or self.cipsnumisakmppolicies.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsnumisakmppolicies.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipsIsakmpEnabled" or name == "cipsIsakmpIdentity" or name == "cipsIsakmpKeepaliveInterval" or name == "cipsNumIsakmpPolicies"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cipsIsakmpEnabled"):
                self.cipsisakmpenabled = value
                self.cipsisakmpenabled.value_namespace = name_space
                self.cipsisakmpenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "cipsIsakmpIdentity"):
                self.cipsisakmpidentity = value
                self.cipsisakmpidentity.value_namespace = name_space
                self.cipsisakmpidentity.value_namespace_prefix = name_space_prefix
            if(value_path == "cipsIsakmpKeepaliveInterval"):
                self.cipsisakmpkeepaliveinterval = value
                self.cipsisakmpkeepaliveinterval.value_namespace = name_space
                self.cipsisakmpkeepaliveinterval.value_namespace_prefix = name_space_prefix
            if(value_path == "cipsNumIsakmpPolicies"):
                self.cipsnumisakmppolicies = value
                self.cipsnumisakmppolicies.value_namespace = name_space
                self.cipsnumisakmppolicies.value_namespace_prefix = name_space_prefix


    class Cipsipsecglobals(Entity):
        """
        
        
        .. attribute:: cipsnumcetcryptomapsets
        
        	The number of static Cryptomap Sets that have  at least one CET cryptomap element as a member of the set
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**units**\: Integral Units
        
        .. attribute:: cipsnumdynamiccryptomapsets
        
        	The number of dynamic IPSec Policy templates (called 'dynamic cryptomap templates') configured on the managed entity
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**units**\: Integral Units
        
        .. attribute:: cipsnumstaticcryptomapsets
        
        	The number of Cryptomap Sets that are are fully configured. Statically defined cryptomap sets  are ones where the operator has fully specified all the parameters required set up IPSec  Virtual Private Networks (VPNs)
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**units**\: Integral Units
        
        .. attribute:: cipsnumtedcryptomapsets
        
        	The number of static Cryptomap Sets that have  at least one dynamic cryptomap template  bound to them which has the Tunnel Endpoint Discovery (TED) enabled
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**units**\: Integral Units
        
        .. attribute:: cipssalifesize
        
        	The default lifesize in KBytes assigned to an SA  as a global policy (unless overridden in cryptomap  definition)
        	**type**\:  int
        
        	**range:** 2560..536870912
        
        	**units**\: KBytes
        
        .. attribute:: cipssalifetime
        
        	The default lifetime (in seconds) assigned  to an SA as a global policy (maybe overridden  in specific cryptomap definitions)
        	**type**\:  int
        
        	**range:** 120..86400
        
        	**units**\: Seconds
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CiscoIpsecMib.Cipsipsecglobals, self).__init__()

            self.yang_name = "cipsIPsecGlobals"
            self.yang_parent_name = "CISCO-IPSEC-MIB"

            self.cipsnumcetcryptomapsets = YLeaf(YType.uint32, "cipsNumCETCryptomapSets")

            self.cipsnumdynamiccryptomapsets = YLeaf(YType.uint32, "cipsNumDynamicCryptomapSets")

            self.cipsnumstaticcryptomapsets = YLeaf(YType.uint32, "cipsNumStaticCryptomapSets")

            self.cipsnumtedcryptomapsets = YLeaf(YType.uint32, "cipsNumTEDCryptomapSets")

            self.cipssalifesize = YLeaf(YType.uint32, "cipsSALifesize")

            self.cipssalifetime = YLeaf(YType.uint32, "cipsSALifetime")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cipsnumcetcryptomapsets",
                            "cipsnumdynamiccryptomapsets",
                            "cipsnumstaticcryptomapsets",
                            "cipsnumtedcryptomapsets",
                            "cipssalifesize",
                            "cipssalifetime") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpsecMib.Cipsipsecglobals, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecMib.Cipsipsecglobals, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cipsnumcetcryptomapsets.is_set or
                self.cipsnumdynamiccryptomapsets.is_set or
                self.cipsnumstaticcryptomapsets.is_set or
                self.cipsnumtedcryptomapsets.is_set or
                self.cipssalifesize.is_set or
                self.cipssalifetime.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cipsnumcetcryptomapsets.yfilter != YFilter.not_set or
                self.cipsnumdynamiccryptomapsets.yfilter != YFilter.not_set or
                self.cipsnumstaticcryptomapsets.yfilter != YFilter.not_set or
                self.cipsnumtedcryptomapsets.yfilter != YFilter.not_set or
                self.cipssalifesize.yfilter != YFilter.not_set or
                self.cipssalifetime.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipsIPsecGlobals" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cipsnumcetcryptomapsets.is_set or self.cipsnumcetcryptomapsets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsnumcetcryptomapsets.get_name_leafdata())
            if (self.cipsnumdynamiccryptomapsets.is_set or self.cipsnumdynamiccryptomapsets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsnumdynamiccryptomapsets.get_name_leafdata())
            if (self.cipsnumstaticcryptomapsets.is_set or self.cipsnumstaticcryptomapsets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsnumstaticcryptomapsets.get_name_leafdata())
            if (self.cipsnumtedcryptomapsets.is_set or self.cipsnumtedcryptomapsets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsnumtedcryptomapsets.get_name_leafdata())
            if (self.cipssalifesize.is_set or self.cipssalifesize.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipssalifesize.get_name_leafdata())
            if (self.cipssalifetime.is_set or self.cipssalifetime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipssalifetime.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipsNumCETCryptomapSets" or name == "cipsNumDynamicCryptomapSets" or name == "cipsNumStaticCryptomapSets" or name == "cipsNumTEDCryptomapSets" or name == "cipsSALifesize" or name == "cipsSALifetime"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cipsNumCETCryptomapSets"):
                self.cipsnumcetcryptomapsets = value
                self.cipsnumcetcryptomapsets.value_namespace = name_space
                self.cipsnumcetcryptomapsets.value_namespace_prefix = name_space_prefix
            if(value_path == "cipsNumDynamicCryptomapSets"):
                self.cipsnumdynamiccryptomapsets = value
                self.cipsnumdynamiccryptomapsets.value_namespace = name_space
                self.cipsnumdynamiccryptomapsets.value_namespace_prefix = name_space_prefix
            if(value_path == "cipsNumStaticCryptomapSets"):
                self.cipsnumstaticcryptomapsets = value
                self.cipsnumstaticcryptomapsets.value_namespace = name_space
                self.cipsnumstaticcryptomapsets.value_namespace_prefix = name_space_prefix
            if(value_path == "cipsNumTEDCryptomapSets"):
                self.cipsnumtedcryptomapsets = value
                self.cipsnumtedcryptomapsets.value_namespace = name_space
                self.cipsnumtedcryptomapsets.value_namespace_prefix = name_space_prefix
            if(value_path == "cipsSALifesize"):
                self.cipssalifesize = value
                self.cipssalifesize.value_namespace = name_space
                self.cipssalifesize.value_namespace_prefix = name_space_prefix
            if(value_path == "cipsSALifetime"):
                self.cipssalifetime = value
                self.cipssalifetime.value_namespace = name_space
                self.cipssalifetime.value_namespace_prefix = name_space_prefix


    class Cipsipsecstatistics(Entity):
        """
        
        
        .. attribute:: cipsnumtedfailures
        
        	The number of TED probes that were dispatched by  the local entity and that failed to locate crypto  endpoint.  Not affected by any CLI operation
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Integral Units
        
        .. attribute:: cipsnumtedprobesreceived
        
        	The number of TED probes that were received by this  managed entity since bootup. Not affected by any  CLI operation
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Integral Units
        
        .. attribute:: cipsnumtedprobessent
        
        	The number of TED probes that were dispatched by all the dynamic cryptomaps in this managed entity since  bootup. Not affected by any CLI operation
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: Integral Units
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CiscoIpsecMib.Cipsipsecstatistics, self).__init__()

            self.yang_name = "cipsIPsecStatistics"
            self.yang_parent_name = "CISCO-IPSEC-MIB"

            self.cipsnumtedfailures = YLeaf(YType.uint32, "cipsNumTEDFailures")

            self.cipsnumtedprobesreceived = YLeaf(YType.uint32, "cipsNumTEDProbesReceived")

            self.cipsnumtedprobessent = YLeaf(YType.uint32, "cipsNumTEDProbesSent")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cipsnumtedfailures",
                            "cipsnumtedprobesreceived",
                            "cipsnumtedprobessent") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpsecMib.Cipsipsecstatistics, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecMib.Cipsipsecstatistics, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cipsnumtedfailures.is_set or
                self.cipsnumtedprobesreceived.is_set or
                self.cipsnumtedprobessent.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cipsnumtedfailures.yfilter != YFilter.not_set or
                self.cipsnumtedprobesreceived.yfilter != YFilter.not_set or
                self.cipsnumtedprobessent.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipsIPsecStatistics" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cipsnumtedfailures.is_set or self.cipsnumtedfailures.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsnumtedfailures.get_name_leafdata())
            if (self.cipsnumtedprobesreceived.is_set or self.cipsnumtedprobesreceived.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsnumtedprobesreceived.get_name_leafdata())
            if (self.cipsnumtedprobessent.is_set or self.cipsnumtedprobessent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsnumtedprobessent.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipsNumTEDFailures" or name == "cipsNumTEDProbesReceived" or name == "cipsNumTEDProbesSent"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cipsNumTEDFailures"):
                self.cipsnumtedfailures = value
                self.cipsnumtedfailures.value_namespace = name_space
                self.cipsnumtedfailures.value_namespace_prefix = name_space_prefix
            if(value_path == "cipsNumTEDProbesReceived"):
                self.cipsnumtedprobesreceived = value
                self.cipsnumtedprobesreceived.value_namespace = name_space
                self.cipsnumtedprobesreceived.value_namespace_prefix = name_space_prefix
            if(value_path == "cipsNumTEDProbesSent"):
                self.cipsnumtedprobessent = value
                self.cipsnumtedprobessent.value_namespace = name_space
                self.cipsnumtedprobessent.value_namespace_prefix = name_space_prefix


    class Cipssyscapacitygroup(Entity):
        """
        
        
        .. attribute:: cips3descapable
        
        	The value of this object is TRUE if the  managed entity has the hardware nad software  features to support 3DES encryption algorithm.  Not affected by any CLI operation
        	**type**\:  bool
        
        .. attribute:: cipsmaxsas
        
        	The maximum number of IPsec Security Associations that can be established on this managed entity. If no theoretical limit exists, this returns value 0.  Not affected by any CLI operation
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**units**\: Integral Units
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CiscoIpsecMib.Cipssyscapacitygroup, self).__init__()

            self.yang_name = "cipsSysCapacityGroup"
            self.yang_parent_name = "CISCO-IPSEC-MIB"

            self.cips3descapable = YLeaf(YType.boolean, "cips3DesCapable")

            self.cipsmaxsas = YLeaf(YType.int32, "cipsMaxSAs")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cips3descapable",
                            "cipsmaxsas") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpsecMib.Cipssyscapacitygroup, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecMib.Cipssyscapacitygroup, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cips3descapable.is_set or
                self.cipsmaxsas.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cips3descapable.yfilter != YFilter.not_set or
                self.cipsmaxsas.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipsSysCapacityGroup" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cips3descapable.is_set or self.cips3descapable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cips3descapable.get_name_leafdata())
            if (self.cipsmaxsas.is_set or self.cipsmaxsas.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipsmaxsas.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cips3DesCapable" or name == "cipsMaxSAs"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cips3DesCapable"):
                self.cips3descapable = value
                self.cips3descapable.value_namespace = name_space
                self.cips3descapable.value_namespace_prefix = name_space_prefix
            if(value_path == "cipsMaxSAs"):
                self.cipsmaxsas = value
                self.cipsmaxsas.value_namespace = name_space
                self.cipsmaxsas.value_namespace_prefix = name_space_prefix


    class Cipstrapcntlgroup(Entity):
        """
        
        
        .. attribute:: cipscntlcryptomapadded
        
        	This object defines the administrative state of  sending the IOS IPsec Cryptomap Add trap
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.Trapstatus>`
        
        .. attribute:: cipscntlcryptomapdeleted
        
        	This object defines the administrative state of  sending the IOS IPsec Cryptomap Delete trap
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.Trapstatus>`
        
        .. attribute:: cipscntlcryptomapsetattached
        
        	This object defines the administrative state of  sending the IOS IPsec trap that is issued when a cryptomap set is attached to an interface
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.Trapstatus>`
        
        .. attribute:: cipscntlcryptomapsetdetached
        
        	This object defines the administrative state of  sending the IOS IPsec trap that is issued when a cryptomap set is detached from an interface. to which it was earlier bound
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.Trapstatus>`
        
        .. attribute:: cipscntlisakmppolicyadded
        
        	This object defines the administrative state of  sending the IOS IPsec ISAKMP Policy Add trap
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.Trapstatus>`
        
        .. attribute:: cipscntlisakmppolicydeleted
        
        	This object defines the administrative state of  sending the IOS IPsec ISAKMP Policy Delete trap
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.Trapstatus>`
        
        .. attribute:: cipscntltoomanysas
        
        	This object defines the administrative state of  sending the IOS IPsec trap that is issued when the number of SAs crosses the maximum number of SAs that may be supported on the managed entity
        	**type**\:   :py:class:`Trapstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.Trapstatus>`
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CiscoIpsecMib.Cipstrapcntlgroup, self).__init__()

            self.yang_name = "cipsTrapCntlGroup"
            self.yang_parent_name = "CISCO-IPSEC-MIB"

            self.cipscntlcryptomapadded = YLeaf(YType.enumeration, "cipsCntlCryptomapAdded")

            self.cipscntlcryptomapdeleted = YLeaf(YType.enumeration, "cipsCntlCryptomapDeleted")

            self.cipscntlcryptomapsetattached = YLeaf(YType.enumeration, "cipsCntlCryptomapSetAttached")

            self.cipscntlcryptomapsetdetached = YLeaf(YType.enumeration, "cipsCntlCryptomapSetDetached")

            self.cipscntlisakmppolicyadded = YLeaf(YType.enumeration, "cipsCntlIsakmpPolicyAdded")

            self.cipscntlisakmppolicydeleted = YLeaf(YType.enumeration, "cipsCntlIsakmpPolicyDeleted")

            self.cipscntltoomanysas = YLeaf(YType.enumeration, "cipsCntlTooManySAs")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cipscntlcryptomapadded",
                            "cipscntlcryptomapdeleted",
                            "cipscntlcryptomapsetattached",
                            "cipscntlcryptomapsetdetached",
                            "cipscntlisakmppolicyadded",
                            "cipscntlisakmppolicydeleted",
                            "cipscntltoomanysas") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpsecMib.Cipstrapcntlgroup, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecMib.Cipstrapcntlgroup, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cipscntlcryptomapadded.is_set or
                self.cipscntlcryptomapdeleted.is_set or
                self.cipscntlcryptomapsetattached.is_set or
                self.cipscntlcryptomapsetdetached.is_set or
                self.cipscntlisakmppolicyadded.is_set or
                self.cipscntlisakmppolicydeleted.is_set or
                self.cipscntltoomanysas.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cipscntlcryptomapadded.yfilter != YFilter.not_set or
                self.cipscntlcryptomapdeleted.yfilter != YFilter.not_set or
                self.cipscntlcryptomapsetattached.yfilter != YFilter.not_set or
                self.cipscntlcryptomapsetdetached.yfilter != YFilter.not_set or
                self.cipscntlisakmppolicyadded.yfilter != YFilter.not_set or
                self.cipscntlisakmppolicydeleted.yfilter != YFilter.not_set or
                self.cipscntltoomanysas.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipsTrapCntlGroup" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cipscntlcryptomapadded.is_set or self.cipscntlcryptomapadded.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipscntlcryptomapadded.get_name_leafdata())
            if (self.cipscntlcryptomapdeleted.is_set or self.cipscntlcryptomapdeleted.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipscntlcryptomapdeleted.get_name_leafdata())
            if (self.cipscntlcryptomapsetattached.is_set or self.cipscntlcryptomapsetattached.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipscntlcryptomapsetattached.get_name_leafdata())
            if (self.cipscntlcryptomapsetdetached.is_set or self.cipscntlcryptomapsetdetached.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipscntlcryptomapsetdetached.get_name_leafdata())
            if (self.cipscntlisakmppolicyadded.is_set or self.cipscntlisakmppolicyadded.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipscntlisakmppolicyadded.get_name_leafdata())
            if (self.cipscntlisakmppolicydeleted.is_set or self.cipscntlisakmppolicydeleted.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipscntlisakmppolicydeleted.get_name_leafdata())
            if (self.cipscntltoomanysas.is_set or self.cipscntltoomanysas.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cipscntltoomanysas.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipsCntlCryptomapAdded" or name == "cipsCntlCryptomapDeleted" or name == "cipsCntlCryptomapSetAttached" or name == "cipsCntlCryptomapSetDetached" or name == "cipsCntlIsakmpPolicyAdded" or name == "cipsCntlIsakmpPolicyDeleted" or name == "cipsCntlTooManySAs"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cipsCntlCryptomapAdded"):
                self.cipscntlcryptomapadded = value
                self.cipscntlcryptomapadded.value_namespace = name_space
                self.cipscntlcryptomapadded.value_namespace_prefix = name_space_prefix
            if(value_path == "cipsCntlCryptomapDeleted"):
                self.cipscntlcryptomapdeleted = value
                self.cipscntlcryptomapdeleted.value_namespace = name_space
                self.cipscntlcryptomapdeleted.value_namespace_prefix = name_space_prefix
            if(value_path == "cipsCntlCryptomapSetAttached"):
                self.cipscntlcryptomapsetattached = value
                self.cipscntlcryptomapsetattached.value_namespace = name_space
                self.cipscntlcryptomapsetattached.value_namespace_prefix = name_space_prefix
            if(value_path == "cipsCntlCryptomapSetDetached"):
                self.cipscntlcryptomapsetdetached = value
                self.cipscntlcryptomapsetdetached.value_namespace = name_space
                self.cipscntlcryptomapsetdetached.value_namespace_prefix = name_space_prefix
            if(value_path == "cipsCntlIsakmpPolicyAdded"):
                self.cipscntlisakmppolicyadded = value
                self.cipscntlisakmppolicyadded.value_namespace = name_space
                self.cipscntlisakmppolicyadded.value_namespace_prefix = name_space_prefix
            if(value_path == "cipsCntlIsakmpPolicyDeleted"):
                self.cipscntlisakmppolicydeleted = value
                self.cipscntlisakmppolicydeleted.value_namespace = name_space
                self.cipscntlisakmppolicydeleted.value_namespace_prefix = name_space_prefix
            if(value_path == "cipsCntlTooManySAs"):
                self.cipscntltoomanysas = value
                self.cipscntltoomanysas.value_namespace = name_space
                self.cipscntltoomanysas.value_namespace_prefix = name_space_prefix


    class Cipsisakmppolicytable(Entity):
        """
        The table containing the list of all
        ISAKMP policy entries configured by the operator.
        
        .. attribute:: cipsisakmppolicyentry
        
        	Each entry contains the attributes  associated with a single ISAKMP Policy entry
        	**type**\: list of    :py:class:`Cipsisakmppolicyentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CiscoIpsecMib.Cipsisakmppolicytable.Cipsisakmppolicyentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CiscoIpsecMib.Cipsisakmppolicytable, self).__init__()

            self.yang_name = "cipsIsakmpPolicyTable"
            self.yang_parent_name = "CISCO-IPSEC-MIB"

            self.cipsisakmppolicyentry = YList(self)

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
                        super(CiscoIpsecMib.Cipsisakmppolicytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecMib.Cipsisakmppolicytable, self).__setattr__(name, value)


        class Cipsisakmppolicyentry(Entity):
            """
            Each entry contains the attributes 
            associated with a single ISAKMP
            Policy entry.
            
            .. attribute:: cipsisakmppolpriority  <key>
            
            	The priotity of this ISAKMP Policy entry. This is also the index of this table
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cipsisakmppolauth
            
            	The peer authentication mthod specified by this ISAKMP policy specification. If this policy entity is selected for negotiation with a peer, the local entity would authenticate the peer using  the method specified by this object
            	**type**\:   :py:class:`Ikeauthmethod <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.Ikeauthmethod>`
            
            .. attribute:: cipsisakmppolencr
            
            	The encryption transform specified by this  ISAKMP policy specification. The Internet Key Exchange (IKE) tunnels setup using this policy item would use the specified encryption transform to protect the ISAKMP PDUs
            	**type**\:   :py:class:`Encryptalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.Encryptalgo>`
            
            .. attribute:: cipsisakmppolgroup
            
            	This object specifies the Oakley group used  for Diffie Hellman exchange in the Main Mode.  If this policy item is selected to negotiate Main Mode with an IKE peer, the local entity  chooses the group specified by this object to perform Diffie Hellman exchange with the peer
            	**type**\:   :py:class:`Diffhellmangrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.Diffhellmangrp>`
            
            .. attribute:: cipsisakmppolhash
            
            	The hash transform specified by this  ISAKMP policy specification. The IKE tunnels setup using this policy item would use the  specified hash transform to protect the ISAKMP PDUs
            	**type**\:   :py:class:`Ikehashalgo <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.Ikehashalgo>`
            
            .. attribute:: cipsisakmppollifetime
            
            	This object specifies the lifetime in seconds of the IKE tunnels generated using this  policy specification
            	**type**\:  int
            
            	**range:** 60..86400
            
            	**units**\: seconds
            
            

            """

            _prefix = 'CISCO-IPSEC-MIB'
            _revision = '2000-08-07'

            def __init__(self):
                super(CiscoIpsecMib.Cipsisakmppolicytable.Cipsisakmppolicyentry, self).__init__()

                self.yang_name = "cipsIsakmpPolicyEntry"
                self.yang_parent_name = "cipsIsakmpPolicyTable"

                self.cipsisakmppolpriority = YLeaf(YType.int32, "cipsIsakmpPolPriority")

                self.cipsisakmppolauth = YLeaf(YType.enumeration, "cipsIsakmpPolAuth")

                self.cipsisakmppolencr = YLeaf(YType.enumeration, "cipsIsakmpPolEncr")

                self.cipsisakmppolgroup = YLeaf(YType.enumeration, "cipsIsakmpPolGroup")

                self.cipsisakmppolhash = YLeaf(YType.enumeration, "cipsIsakmpPolHash")

                self.cipsisakmppollifetime = YLeaf(YType.int32, "cipsIsakmpPolLifetime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipsisakmppolpriority",
                                "cipsisakmppolauth",
                                "cipsisakmppolencr",
                                "cipsisakmppolgroup",
                                "cipsisakmppolhash",
                                "cipsisakmppollifetime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecMib.Cipsisakmppolicytable.Cipsisakmppolicyentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecMib.Cipsisakmppolicytable.Cipsisakmppolicyentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cipsisakmppolpriority.is_set or
                    self.cipsisakmppolauth.is_set or
                    self.cipsisakmppolencr.is_set or
                    self.cipsisakmppolgroup.is_set or
                    self.cipsisakmppolhash.is_set or
                    self.cipsisakmppollifetime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipsisakmppolpriority.yfilter != YFilter.not_set or
                    self.cipsisakmppolauth.yfilter != YFilter.not_set or
                    self.cipsisakmppolencr.yfilter != YFilter.not_set or
                    self.cipsisakmppolgroup.yfilter != YFilter.not_set or
                    self.cipsisakmppolhash.yfilter != YFilter.not_set or
                    self.cipsisakmppollifetime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipsIsakmpPolicyEntry" + "[cipsIsakmpPolPriority='" + self.cipsisakmppolpriority.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/cipsIsakmpPolicyTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipsisakmppolpriority.is_set or self.cipsisakmppolpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsisakmppolpriority.get_name_leafdata())
                if (self.cipsisakmppolauth.is_set or self.cipsisakmppolauth.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsisakmppolauth.get_name_leafdata())
                if (self.cipsisakmppolencr.is_set or self.cipsisakmppolencr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsisakmppolencr.get_name_leafdata())
                if (self.cipsisakmppolgroup.is_set or self.cipsisakmppolgroup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsisakmppolgroup.get_name_leafdata())
                if (self.cipsisakmppolhash.is_set or self.cipsisakmppolhash.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsisakmppolhash.get_name_leafdata())
                if (self.cipsisakmppollifetime.is_set or self.cipsisakmppollifetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsisakmppollifetime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipsIsakmpPolPriority" or name == "cipsIsakmpPolAuth" or name == "cipsIsakmpPolEncr" or name == "cipsIsakmpPolGroup" or name == "cipsIsakmpPolHash" or name == "cipsIsakmpPolLifetime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipsIsakmpPolPriority"):
                    self.cipsisakmppolpriority = value
                    self.cipsisakmppolpriority.value_namespace = name_space
                    self.cipsisakmppolpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsIsakmpPolAuth"):
                    self.cipsisakmppolauth = value
                    self.cipsisakmppolauth.value_namespace = name_space
                    self.cipsisakmppolauth.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsIsakmpPolEncr"):
                    self.cipsisakmppolencr = value
                    self.cipsisakmppolencr.value_namespace = name_space
                    self.cipsisakmppolencr.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsIsakmpPolGroup"):
                    self.cipsisakmppolgroup = value
                    self.cipsisakmppolgroup.value_namespace = name_space
                    self.cipsisakmppolgroup.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsIsakmpPolHash"):
                    self.cipsisakmppolhash = value
                    self.cipsisakmppolhash.value_namespace = name_space
                    self.cipsisakmppolhash.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsIsakmpPolLifetime"):
                    self.cipsisakmppollifetime = value
                    self.cipsisakmppollifetime.value_namespace = name_space
                    self.cipsisakmppollifetime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipsisakmppolicyentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipsisakmppolicyentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipsIsakmpPolicyTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipsIsakmpPolicyEntry"):
                for c in self.cipsisakmppolicyentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecMib.Cipsisakmppolicytable.Cipsisakmppolicyentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipsisakmppolicyentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipsIsakmpPolicyEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cipsstaticcryptomapsetentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CiscoIpsecMib.Cipsstaticcryptomapsettable.Cipsstaticcryptomapsetentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CiscoIpsecMib.Cipsstaticcryptomapsettable, self).__init__()

            self.yang_name = "cipsStaticCryptomapSetTable"
            self.yang_parent_name = "CISCO-IPSEC-MIB"

            self.cipsstaticcryptomapsetentry = YList(self)

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
                        super(CiscoIpsecMib.Cipsstaticcryptomapsettable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecMib.Cipsstaticcryptomapsettable, self).__setattr__(name, value)


        class Cipsstaticcryptomapsetentry(Entity):
            """
            Each entry contains the attributes 
            associated with a single static 
            cryptomap set.
            
            .. attribute:: cipsstaticcryptomapsetname  <key>
            
            	The index of the static cryptomap table. The value  of the string is the name string assigned by the  operator in defining the cryptomap set
            	**type**\:  str
            
            .. attribute:: cipsstaticcryptomapsetnumcet
            
            	The number of cryptomaps of type 'ipsec\-cisco'  associated with this cryptomap set. Such cryptomap elements implement Cisco Encryption Technology based Virtual Private Networks
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsstaticcryptomapsetnumdisc
            
            	The number of dynamic cryptomap templates linked to this cryptomap set that have Tunnel Endpoint Discovery (TED) enabled
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsstaticcryptomapsetnumdynamic
            
            	The number of dynamic cryptomap templates linked to this cryptomap set
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsstaticcryptomapsetnumisakmp
            
            	The number of cryptomaps associated with this  cryptomap set that use ISAKMP protocol to do key exchange
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsstaticcryptomapsetnummanual
            
            	The number of cryptomaps associated with this  cryptomap set that require the operator to manually setup the keys and SPIs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsstaticcryptomapsetnumsas
            
            	The number of and IPsec Security Associations that are active and were setup using this cryptomap.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsstaticcryptomapsetsize
            
            	The total number of cryptomap entries contained in this cryptomap set. 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IPSEC-MIB'
            _revision = '2000-08-07'

            def __init__(self):
                super(CiscoIpsecMib.Cipsstaticcryptomapsettable.Cipsstaticcryptomapsetentry, self).__init__()

                self.yang_name = "cipsStaticCryptomapSetEntry"
                self.yang_parent_name = "cipsStaticCryptomapSetTable"

                self.cipsstaticcryptomapsetname = YLeaf(YType.str, "cipsStaticCryptomapSetName")

                self.cipsstaticcryptomapsetnumcet = YLeaf(YType.uint32, "cipsStaticCryptomapSetNumCET")

                self.cipsstaticcryptomapsetnumdisc = YLeaf(YType.uint32, "cipsStaticCryptomapSetNumDisc")

                self.cipsstaticcryptomapsetnumdynamic = YLeaf(YType.uint32, "cipsStaticCryptomapSetNumDynamic")

                self.cipsstaticcryptomapsetnumisakmp = YLeaf(YType.uint32, "cipsStaticCryptomapSetNumIsakmp")

                self.cipsstaticcryptomapsetnummanual = YLeaf(YType.uint32, "cipsStaticCryptomapSetNumManual")

                self.cipsstaticcryptomapsetnumsas = YLeaf(YType.uint32, "cipsStaticCryptomapSetNumSAs")

                self.cipsstaticcryptomapsetsize = YLeaf(YType.uint32, "cipsStaticCryptomapSetSize")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipsstaticcryptomapsetname",
                                "cipsstaticcryptomapsetnumcet",
                                "cipsstaticcryptomapsetnumdisc",
                                "cipsstaticcryptomapsetnumdynamic",
                                "cipsstaticcryptomapsetnumisakmp",
                                "cipsstaticcryptomapsetnummanual",
                                "cipsstaticcryptomapsetnumsas",
                                "cipsstaticcryptomapsetsize") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecMib.Cipsstaticcryptomapsettable.Cipsstaticcryptomapsetentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecMib.Cipsstaticcryptomapsettable.Cipsstaticcryptomapsetentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cipsstaticcryptomapsetname.is_set or
                    self.cipsstaticcryptomapsetnumcet.is_set or
                    self.cipsstaticcryptomapsetnumdisc.is_set or
                    self.cipsstaticcryptomapsetnumdynamic.is_set or
                    self.cipsstaticcryptomapsetnumisakmp.is_set or
                    self.cipsstaticcryptomapsetnummanual.is_set or
                    self.cipsstaticcryptomapsetnumsas.is_set or
                    self.cipsstaticcryptomapsetsize.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomapsetname.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomapsetnumcet.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomapsetnumdisc.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomapsetnumdynamic.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomapsetnumisakmp.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomapsetnummanual.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomapsetnumsas.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomapsetsize.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipsStaticCryptomapSetEntry" + "[cipsStaticCryptomapSetName='" + self.cipsstaticcryptomapsetname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/cipsStaticCryptomapSetTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipsstaticcryptomapsetname.is_set or self.cipsstaticcryptomapsetname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomapsetname.get_name_leafdata())
                if (self.cipsstaticcryptomapsetnumcet.is_set or self.cipsstaticcryptomapsetnumcet.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomapsetnumcet.get_name_leafdata())
                if (self.cipsstaticcryptomapsetnumdisc.is_set or self.cipsstaticcryptomapsetnumdisc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomapsetnumdisc.get_name_leafdata())
                if (self.cipsstaticcryptomapsetnumdynamic.is_set or self.cipsstaticcryptomapsetnumdynamic.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomapsetnumdynamic.get_name_leafdata())
                if (self.cipsstaticcryptomapsetnumisakmp.is_set or self.cipsstaticcryptomapsetnumisakmp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomapsetnumisakmp.get_name_leafdata())
                if (self.cipsstaticcryptomapsetnummanual.is_set or self.cipsstaticcryptomapsetnummanual.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomapsetnummanual.get_name_leafdata())
                if (self.cipsstaticcryptomapsetnumsas.is_set or self.cipsstaticcryptomapsetnumsas.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomapsetnumsas.get_name_leafdata())
                if (self.cipsstaticcryptomapsetsize.is_set or self.cipsstaticcryptomapsetsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomapsetsize.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipsStaticCryptomapSetName" or name == "cipsStaticCryptomapSetNumCET" or name == "cipsStaticCryptomapSetNumDisc" or name == "cipsStaticCryptomapSetNumDynamic" or name == "cipsStaticCryptomapSetNumIsakmp" or name == "cipsStaticCryptomapSetNumManual" or name == "cipsStaticCryptomapSetNumSAs" or name == "cipsStaticCryptomapSetSize"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipsStaticCryptomapSetName"):
                    self.cipsstaticcryptomapsetname = value
                    self.cipsstaticcryptomapsetname.value_namespace = name_space
                    self.cipsstaticcryptomapsetname.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsStaticCryptomapSetNumCET"):
                    self.cipsstaticcryptomapsetnumcet = value
                    self.cipsstaticcryptomapsetnumcet.value_namespace = name_space
                    self.cipsstaticcryptomapsetnumcet.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsStaticCryptomapSetNumDisc"):
                    self.cipsstaticcryptomapsetnumdisc = value
                    self.cipsstaticcryptomapsetnumdisc.value_namespace = name_space
                    self.cipsstaticcryptomapsetnumdisc.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsStaticCryptomapSetNumDynamic"):
                    self.cipsstaticcryptomapsetnumdynamic = value
                    self.cipsstaticcryptomapsetnumdynamic.value_namespace = name_space
                    self.cipsstaticcryptomapsetnumdynamic.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsStaticCryptomapSetNumIsakmp"):
                    self.cipsstaticcryptomapsetnumisakmp = value
                    self.cipsstaticcryptomapsetnumisakmp.value_namespace = name_space
                    self.cipsstaticcryptomapsetnumisakmp.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsStaticCryptomapSetNumManual"):
                    self.cipsstaticcryptomapsetnummanual = value
                    self.cipsstaticcryptomapsetnummanual.value_namespace = name_space
                    self.cipsstaticcryptomapsetnummanual.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsStaticCryptomapSetNumSAs"):
                    self.cipsstaticcryptomapsetnumsas = value
                    self.cipsstaticcryptomapsetnumsas.value_namespace = name_space
                    self.cipsstaticcryptomapsetnumsas.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsStaticCryptomapSetSize"):
                    self.cipsstaticcryptomapsetsize = value
                    self.cipsstaticcryptomapsetsize.value_namespace = name_space
                    self.cipsstaticcryptomapsetsize.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipsstaticcryptomapsetentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipsstaticcryptomapsetentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipsStaticCryptomapSetTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipsStaticCryptomapSetEntry"):
                for c in self.cipsstaticcryptomapsetentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecMib.Cipsstaticcryptomapsettable.Cipsstaticcryptomapsetentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipsstaticcryptomapsetentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipsStaticCryptomapSetEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cipsdynamiccryptomapsettable(Entity):
        """
        The table containing the list of all dynamic
        cryptomaps that use IKE, defined on 
         the managed entity.
        
        .. attribute:: cipsdynamiccryptomapsetentry
        
        	Each entry contains the attributes associated with a single dynamic cryptomap template
        	**type**\: list of    :py:class:`Cipsdynamiccryptomapsetentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CiscoIpsecMib.Cipsdynamiccryptomapsettable.Cipsdynamiccryptomapsetentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CiscoIpsecMib.Cipsdynamiccryptomapsettable, self).__init__()

            self.yang_name = "cipsDynamicCryptomapSetTable"
            self.yang_parent_name = "CISCO-IPSEC-MIB"

            self.cipsdynamiccryptomapsetentry = YList(self)

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
                        super(CiscoIpsecMib.Cipsdynamiccryptomapsettable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecMib.Cipsdynamiccryptomapsettable, self).__setattr__(name, value)


        class Cipsdynamiccryptomapsetentry(Entity):
            """
            Each entry contains the attributes associated
            with a single dynamic cryptomap template.
            
            .. attribute:: cipsdynamiccryptomapsetname  <key>
            
            	The index of the dynamic cryptomap table.  The value of the string is the one assigned  by the operator in defining the cryptomap set
            	**type**\:  str
            
            .. attribute:: cipsdynamiccryptomapsetnumassoc
            
            	The number of static cryptomap sets with which this dynamic cryptomap is associated.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsdynamiccryptomapsetsize
            
            	The number of cryptomap entries in this cryptomap
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IPSEC-MIB'
            _revision = '2000-08-07'

            def __init__(self):
                super(CiscoIpsecMib.Cipsdynamiccryptomapsettable.Cipsdynamiccryptomapsetentry, self).__init__()

                self.yang_name = "cipsDynamicCryptomapSetEntry"
                self.yang_parent_name = "cipsDynamicCryptomapSetTable"

                self.cipsdynamiccryptomapsetname = YLeaf(YType.str, "cipsDynamicCryptomapSetName")

                self.cipsdynamiccryptomapsetnumassoc = YLeaf(YType.uint32, "cipsDynamicCryptomapSetNumAssoc")

                self.cipsdynamiccryptomapsetsize = YLeaf(YType.uint32, "cipsDynamicCryptomapSetSize")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipsdynamiccryptomapsetname",
                                "cipsdynamiccryptomapsetnumassoc",
                                "cipsdynamiccryptomapsetsize") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecMib.Cipsdynamiccryptomapsettable.Cipsdynamiccryptomapsetentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecMib.Cipsdynamiccryptomapsettable.Cipsdynamiccryptomapsetentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cipsdynamiccryptomapsetname.is_set or
                    self.cipsdynamiccryptomapsetnumassoc.is_set or
                    self.cipsdynamiccryptomapsetsize.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipsdynamiccryptomapsetname.yfilter != YFilter.not_set or
                    self.cipsdynamiccryptomapsetnumassoc.yfilter != YFilter.not_set or
                    self.cipsdynamiccryptomapsetsize.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipsDynamicCryptomapSetEntry" + "[cipsDynamicCryptomapSetName='" + self.cipsdynamiccryptomapsetname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/cipsDynamicCryptomapSetTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipsdynamiccryptomapsetname.is_set or self.cipsdynamiccryptomapsetname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsdynamiccryptomapsetname.get_name_leafdata())
                if (self.cipsdynamiccryptomapsetnumassoc.is_set or self.cipsdynamiccryptomapsetnumassoc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsdynamiccryptomapsetnumassoc.get_name_leafdata())
                if (self.cipsdynamiccryptomapsetsize.is_set or self.cipsdynamiccryptomapsetsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsdynamiccryptomapsetsize.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipsDynamicCryptomapSetName" or name == "cipsDynamicCryptomapSetNumAssoc" or name == "cipsDynamicCryptomapSetSize"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipsDynamicCryptomapSetName"):
                    self.cipsdynamiccryptomapsetname = value
                    self.cipsdynamiccryptomapsetname.value_namespace = name_space
                    self.cipsdynamiccryptomapsetname.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsDynamicCryptomapSetNumAssoc"):
                    self.cipsdynamiccryptomapsetnumassoc = value
                    self.cipsdynamiccryptomapsetnumassoc.value_namespace = name_space
                    self.cipsdynamiccryptomapsetnumassoc.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsDynamicCryptomapSetSize"):
                    self.cipsdynamiccryptomapsetsize = value
                    self.cipsdynamiccryptomapsetsize.value_namespace = name_space
                    self.cipsdynamiccryptomapsetsize.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipsdynamiccryptomapsetentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipsdynamiccryptomapsetentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipsDynamicCryptomapSetTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipsDynamicCryptomapSetEntry"):
                for c in self.cipsdynamiccryptomapsetentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecMib.Cipsdynamiccryptomapsettable.Cipsdynamiccryptomapsetentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipsdynamiccryptomapsetentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipsDynamicCryptomapSetEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cipsstaticcryptomaptable(Entity):
        """
        The table ilisting the member cryptomaps
        of the cryptomap sets that are configured
        on the managed entity.
        
        .. attribute:: cipsstaticcryptomapentry
        
        	Each entry contains the attributes  associated with a single static  (fully specified) cryptomap entry. This table does not include the members  of dynamic cryptomap sets that may be linked with the parent static cryptomap set
        	**type**\: list of    :py:class:`Cipsstaticcryptomapentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CiscoIpsecMib.Cipsstaticcryptomaptable.Cipsstaticcryptomapentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CiscoIpsecMib.Cipsstaticcryptomaptable, self).__init__()

            self.yang_name = "cipsStaticCryptomapTable"
            self.yang_parent_name = "CISCO-IPSEC-MIB"

            self.cipsstaticcryptomapentry = YList(self)

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
                        super(CiscoIpsecMib.Cipsstaticcryptomaptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecMib.Cipsstaticcryptomaptable, self).__setattr__(name, value)


        class Cipsstaticcryptomapentry(Entity):
            """
            Each entry contains the attributes 
            associated with a single static 
            (fully specified) cryptomap entry.
            This table does not include the members 
            of dynamic cryptomap sets that may be
            linked with the parent static cryptomap set.
            
            .. attribute:: cipsstaticcryptomapsetname  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`cipsstaticcryptomapsetname <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CiscoIpsecMib.Cipsstaticcryptomapsettable.Cipsstaticcryptomapsetentry>`
            
            .. attribute:: cipsstaticcryptomappriority  <key>
            
            	The priority of the cryptomap entry in the  cryptomap set. This is the second index component of this table
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cipsstaticcryptomapdescr
            
            	The description string entered by the operatoir while creating this cryptomap. The string generally identifies a description and the purpose of this policy
            	**type**\:  str
            
            .. attribute:: cipsstaticcryptomaplevelhost
            
            	This object identifies the granularity of the IPSec SAs created using this IPSec policy entry.  If this value is TRUE, distinct SA bundles are created for distinct hosts at the end of the application traffic
            	**type**\:  bool
            
            .. attribute:: cipsstaticcryptomaplifesize
            
            	This object identifies the lifesize (maximum traffic in bytes that may be carried) of the IPSec SAs created using this IPSec policy entry.  If this value is zero, the lifetime assumes the  value specified by the global lifesize parameter
            	**type**\:  int
            
            	**range:** 0..None \| 2560..536870912
            
            .. attribute:: cipsstaticcryptomaplifetime
            
            	This object identifies the lifetime of the IPSec Security Associations (SA) created using this IPSec policy entry. If this value is zero, the lifetime assumes the  value specified by the global lifetime parameter
            	**type**\:  int
            
            	**range:** 0..None \| 120..86400
            
            .. attribute:: cipsstaticcryptomapnumpeers
            
            	The number of peers associated with this cryptomap  entry. The peers other than the one identified by  'cipsStaticCryptomapPeer' are backup peers.   Manual cryptomaps may have only one peer
            	**type**\:  int
            
            	**range:** 0..40
            
            .. attribute:: cipsstaticcryptomappeer
            
            	The IP address of the current peer associated with  this IPSec policy item. Traffic that is protected by this cryptomap is protected by a tunnel that terminates at the device whose IP address is specified by this object
            	**type**\:  str
            
            	**length:** 4 \| 16
            
            .. attribute:: cipsstaticcryptomappfs
            
            	This object identifies if the tunnels instantiated due to this policy item should use Perfect Forward Secrecy  (PFS) and if so, what group of Oakley they should use
            	**type**\:   :py:class:`Diffhellmangrp <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.Diffhellmangrp>`
            
            .. attribute:: cipsstaticcryptomaptype
            
            	The type of the cryptomap entry. This can be an ISAKMP cryptomap, CET or manual. Dynamic cryptomaps are not counted in this table
            	**type**\:   :py:class:`Cryptomaptype <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.Cryptomaptype>`
            
            

            """

            _prefix = 'CISCO-IPSEC-MIB'
            _revision = '2000-08-07'

            def __init__(self):
                super(CiscoIpsecMib.Cipsstaticcryptomaptable.Cipsstaticcryptomapentry, self).__init__()

                self.yang_name = "cipsStaticCryptomapEntry"
                self.yang_parent_name = "cipsStaticCryptomapTable"

                self.cipsstaticcryptomapsetname = YLeaf(YType.str, "cipsStaticCryptomapSetName")

                self.cipsstaticcryptomappriority = YLeaf(YType.int32, "cipsStaticCryptomapPriority")

                self.cipsstaticcryptomapdescr = YLeaf(YType.str, "cipsStaticCryptomapDescr")

                self.cipsstaticcryptomaplevelhost = YLeaf(YType.boolean, "cipsStaticCryptomapLevelHost")

                self.cipsstaticcryptomaplifesize = YLeaf(YType.int32, "cipsStaticCryptomapLifesize")

                self.cipsstaticcryptomaplifetime = YLeaf(YType.int32, "cipsStaticCryptomapLifetime")

                self.cipsstaticcryptomapnumpeers = YLeaf(YType.int32, "cipsStaticCryptomapNumPeers")

                self.cipsstaticcryptomappeer = YLeaf(YType.str, "cipsStaticCryptomapPeer")

                self.cipsstaticcryptomappfs = YLeaf(YType.enumeration, "cipsStaticCryptomapPfs")

                self.cipsstaticcryptomaptype = YLeaf(YType.enumeration, "cipsStaticCryptomapType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipsstaticcryptomapsetname",
                                "cipsstaticcryptomappriority",
                                "cipsstaticcryptomapdescr",
                                "cipsstaticcryptomaplevelhost",
                                "cipsstaticcryptomaplifesize",
                                "cipsstaticcryptomaplifetime",
                                "cipsstaticcryptomapnumpeers",
                                "cipsstaticcryptomappeer",
                                "cipsstaticcryptomappfs",
                                "cipsstaticcryptomaptype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecMib.Cipsstaticcryptomaptable.Cipsstaticcryptomapentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecMib.Cipsstaticcryptomaptable.Cipsstaticcryptomapentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cipsstaticcryptomapsetname.is_set or
                    self.cipsstaticcryptomappriority.is_set or
                    self.cipsstaticcryptomapdescr.is_set or
                    self.cipsstaticcryptomaplevelhost.is_set or
                    self.cipsstaticcryptomaplifesize.is_set or
                    self.cipsstaticcryptomaplifetime.is_set or
                    self.cipsstaticcryptomapnumpeers.is_set or
                    self.cipsstaticcryptomappeer.is_set or
                    self.cipsstaticcryptomappfs.is_set or
                    self.cipsstaticcryptomaptype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomapsetname.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomappriority.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomapdescr.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomaplevelhost.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomaplifesize.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomaplifetime.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomapnumpeers.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomappeer.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomappfs.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomaptype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipsStaticCryptomapEntry" + "[cipsStaticCryptomapSetName='" + self.cipsstaticcryptomapsetname.get() + "']" + "[cipsStaticCryptomapPriority='" + self.cipsstaticcryptomappriority.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/cipsStaticCryptomapTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipsstaticcryptomapsetname.is_set or self.cipsstaticcryptomapsetname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomapsetname.get_name_leafdata())
                if (self.cipsstaticcryptomappriority.is_set or self.cipsstaticcryptomappriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomappriority.get_name_leafdata())
                if (self.cipsstaticcryptomapdescr.is_set or self.cipsstaticcryptomapdescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomapdescr.get_name_leafdata())
                if (self.cipsstaticcryptomaplevelhost.is_set or self.cipsstaticcryptomaplevelhost.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomaplevelhost.get_name_leafdata())
                if (self.cipsstaticcryptomaplifesize.is_set or self.cipsstaticcryptomaplifesize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomaplifesize.get_name_leafdata())
                if (self.cipsstaticcryptomaplifetime.is_set or self.cipsstaticcryptomaplifetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomaplifetime.get_name_leafdata())
                if (self.cipsstaticcryptomapnumpeers.is_set or self.cipsstaticcryptomapnumpeers.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomapnumpeers.get_name_leafdata())
                if (self.cipsstaticcryptomappeer.is_set or self.cipsstaticcryptomappeer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomappeer.get_name_leafdata())
                if (self.cipsstaticcryptomappfs.is_set or self.cipsstaticcryptomappfs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomappfs.get_name_leafdata())
                if (self.cipsstaticcryptomaptype.is_set or self.cipsstaticcryptomaptype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomaptype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipsStaticCryptomapSetName" or name == "cipsStaticCryptomapPriority" or name == "cipsStaticCryptomapDescr" or name == "cipsStaticCryptomapLevelHost" or name == "cipsStaticCryptomapLifesize" or name == "cipsStaticCryptomapLifetime" or name == "cipsStaticCryptomapNumPeers" or name == "cipsStaticCryptomapPeer" or name == "cipsStaticCryptomapPfs" or name == "cipsStaticCryptomapType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipsStaticCryptomapSetName"):
                    self.cipsstaticcryptomapsetname = value
                    self.cipsstaticcryptomapsetname.value_namespace = name_space
                    self.cipsstaticcryptomapsetname.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsStaticCryptomapPriority"):
                    self.cipsstaticcryptomappriority = value
                    self.cipsstaticcryptomappriority.value_namespace = name_space
                    self.cipsstaticcryptomappriority.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsStaticCryptomapDescr"):
                    self.cipsstaticcryptomapdescr = value
                    self.cipsstaticcryptomapdescr.value_namespace = name_space
                    self.cipsstaticcryptomapdescr.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsStaticCryptomapLevelHost"):
                    self.cipsstaticcryptomaplevelhost = value
                    self.cipsstaticcryptomaplevelhost.value_namespace = name_space
                    self.cipsstaticcryptomaplevelhost.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsStaticCryptomapLifesize"):
                    self.cipsstaticcryptomaplifesize = value
                    self.cipsstaticcryptomaplifesize.value_namespace = name_space
                    self.cipsstaticcryptomaplifesize.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsStaticCryptomapLifetime"):
                    self.cipsstaticcryptomaplifetime = value
                    self.cipsstaticcryptomaplifetime.value_namespace = name_space
                    self.cipsstaticcryptomaplifetime.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsStaticCryptomapNumPeers"):
                    self.cipsstaticcryptomapnumpeers = value
                    self.cipsstaticcryptomapnumpeers.value_namespace = name_space
                    self.cipsstaticcryptomapnumpeers.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsStaticCryptomapPeer"):
                    self.cipsstaticcryptomappeer = value
                    self.cipsstaticcryptomappeer.value_namespace = name_space
                    self.cipsstaticcryptomappeer.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsStaticCryptomapPfs"):
                    self.cipsstaticcryptomappfs = value
                    self.cipsstaticcryptomappfs.value_namespace = name_space
                    self.cipsstaticcryptomappfs.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsStaticCryptomapType"):
                    self.cipsstaticcryptomaptype = value
                    self.cipsstaticcryptomaptype.value_namespace = name_space
                    self.cipsstaticcryptomaptype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipsstaticcryptomapentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipsstaticcryptomapentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipsStaticCryptomapTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipsStaticCryptomapEntry"):
                for c in self.cipsstaticcryptomapentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecMib.Cipsstaticcryptomaptable.Cipsstaticcryptomapentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipsstaticcryptomapentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipsStaticCryptomapEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cipscryptomapsetiftable(Entity):
        """
        The table lists the binding of cryptomap sets
        to the interfaces of the managed entity.
        
        .. attribute:: cipscryptomapsetifentry
        
        	Each entry contains the record of the association between an interface and a cryptomap set (static) that is defined on the managed entity.  Note that the cryptomap set identified in  this binding must static. Dynamic cryptomaps cannot be bound to interfaces
        	**type**\: list of    :py:class:`Cipscryptomapsetifentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CiscoIpsecMib.Cipscryptomapsetiftable.Cipscryptomapsetifentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-MIB'
        _revision = '2000-08-07'

        def __init__(self):
            super(CiscoIpsecMib.Cipscryptomapsetiftable, self).__init__()

            self.yang_name = "cipsCryptomapSetIfTable"
            self.yang_parent_name = "CISCO-IPSEC-MIB"

            self.cipscryptomapsetifentry = YList(self)

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
                        super(CiscoIpsecMib.Cipscryptomapsetiftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecMib.Cipscryptomapsetiftable, self).__setattr__(name, value)


        class Cipscryptomapsetifentry(Entity):
            """
            Each entry contains the record of
            the association between an interface
            and a cryptomap set (static) that is defined
            on the managed entity.
            
            Note that the cryptomap set identified in 
            this binding must static. Dynamic cryptomaps cannot
            be bound to interfaces.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cipsstaticcryptomapsetname  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`cipsstaticcryptomapsetname <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.CiscoIpsecMib.Cipsstaticcryptomapsettable.Cipsstaticcryptomapsetentry>`
            
            .. attribute:: cipscryptomapsetifstatus
            
            	This object identifies the status of the binding  of the specified cryptomap set with the specified interface. The value when queried is always 'attached'.  When set to 'detached', the cryptomap set if detached  from the specified interface. The effect of this is same  as the CLI command  	config\-if# no crypto map cryptomapSetName  Setting the value to 'attached' will result in  SNMP General Error
            	**type**\:   :py:class:`Cryptomapsetbindstatus <ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB.Cryptomapsetbindstatus>`
            
            .. attribute:: cipscryptomapsetifvirtual
            
            	The value of this object identifies if the interface to which the cryptomap set is attached is a tunnel (such as a GRE or PPTP tunnel)
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-IPSEC-MIB'
            _revision = '2000-08-07'

            def __init__(self):
                super(CiscoIpsecMib.Cipscryptomapsetiftable.Cipscryptomapsetifentry, self).__init__()

                self.yang_name = "cipsCryptomapSetIfEntry"
                self.yang_parent_name = "cipsCryptomapSetIfTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cipsstaticcryptomapsetname = YLeaf(YType.str, "cipsStaticCryptomapSetName")

                self.cipscryptomapsetifstatus = YLeaf(YType.enumeration, "cipsCryptomapSetIfStatus")

                self.cipscryptomapsetifvirtual = YLeaf(YType.boolean, "cipsCryptomapSetIfVirtual")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "cipsstaticcryptomapsetname",
                                "cipscryptomapsetifstatus",
                                "cipscryptomapsetifvirtual") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecMib.Cipscryptomapsetiftable.Cipscryptomapsetifentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecMib.Cipscryptomapsetiftable.Cipscryptomapsetifentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cipsstaticcryptomapsetname.is_set or
                    self.cipscryptomapsetifstatus.is_set or
                    self.cipscryptomapsetifvirtual.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cipsstaticcryptomapsetname.yfilter != YFilter.not_set or
                    self.cipscryptomapsetifstatus.yfilter != YFilter.not_set or
                    self.cipscryptomapsetifvirtual.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipsCryptomapSetIfEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[cipsStaticCryptomapSetName='" + self.cipsstaticcryptomapsetname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/cipsCryptomapSetIfTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cipsstaticcryptomapsetname.is_set or self.cipsstaticcryptomapsetname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipsstaticcryptomapsetname.get_name_leafdata())
                if (self.cipscryptomapsetifstatus.is_set or self.cipscryptomapsetifstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipscryptomapsetifstatus.get_name_leafdata())
                if (self.cipscryptomapsetifvirtual.is_set or self.cipscryptomapsetifvirtual.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipscryptomapsetifvirtual.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cipsStaticCryptomapSetName" or name == "cipsCryptomapSetIfStatus" or name == "cipsCryptomapSetIfVirtual"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsStaticCryptomapSetName"):
                    self.cipsstaticcryptomapsetname = value
                    self.cipsstaticcryptomapsetname.value_namespace = name_space
                    self.cipsstaticcryptomapsetname.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsCryptomapSetIfStatus"):
                    self.cipscryptomapsetifstatus = value
                    self.cipscryptomapsetifstatus.value_namespace = name_space
                    self.cipscryptomapsetifstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cipsCryptomapSetIfVirtual"):
                    self.cipscryptomapsetifvirtual = value
                    self.cipscryptomapsetifvirtual.value_namespace = name_space
                    self.cipscryptomapsetifvirtual.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipscryptomapsetifentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipscryptomapsetifentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipsCryptomapSetIfTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipsCryptomapSetIfEntry"):
                for c in self.cipscryptomapsetifentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecMib.Cipscryptomapsetiftable.Cipscryptomapsetifentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipscryptomapsetifentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipsCryptomapSetIfEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cipscryptomapsetiftable is not None and self.cipscryptomapsetiftable.has_data()) or
            (self.cipsdynamiccryptomapsettable is not None and self.cipsdynamiccryptomapsettable.has_data()) or
            (self.cipsipsecglobals is not None and self.cipsipsecglobals.has_data()) or
            (self.cipsipsecstatistics is not None and self.cipsipsecstatistics.has_data()) or
            (self.cipsisakmpgroup is not None and self.cipsisakmpgroup.has_data()) or
            (self.cipsisakmppolicytable is not None and self.cipsisakmppolicytable.has_data()) or
            (self.cipsstaticcryptomapsettable is not None and self.cipsstaticcryptomapsettable.has_data()) or
            (self.cipsstaticcryptomaptable is not None and self.cipsstaticcryptomaptable.has_data()) or
            (self.cipssyscapacitygroup is not None and self.cipssyscapacitygroup.has_data()) or
            (self.cipstrapcntlgroup is not None and self.cipstrapcntlgroup.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cipscryptomapsetiftable is not None and self.cipscryptomapsetiftable.has_operation()) or
            (self.cipsdynamiccryptomapsettable is not None and self.cipsdynamiccryptomapsettable.has_operation()) or
            (self.cipsipsecglobals is not None and self.cipsipsecglobals.has_operation()) or
            (self.cipsipsecstatistics is not None and self.cipsipsecstatistics.has_operation()) or
            (self.cipsisakmpgroup is not None and self.cipsisakmpgroup.has_operation()) or
            (self.cipsisakmppolicytable is not None and self.cipsisakmppolicytable.has_operation()) or
            (self.cipsstaticcryptomapsettable is not None and self.cipsstaticcryptomapsettable.has_operation()) or
            (self.cipsstaticcryptomaptable is not None and self.cipsstaticcryptomaptable.has_operation()) or
            (self.cipssyscapacitygroup is not None and self.cipssyscapacitygroup.has_operation()) or
            (self.cipstrapcntlgroup is not None and self.cipstrapcntlgroup.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IPSEC-MIB:CISCO-IPSEC-MIB" + path_buffer

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

        if (child_yang_name == "cipsCryptomapSetIfTable"):
            if (self.cipscryptomapsetiftable is None):
                self.cipscryptomapsetiftable = CiscoIpsecMib.Cipscryptomapsetiftable()
                self.cipscryptomapsetiftable.parent = self
                self._children_name_map["cipscryptomapsetiftable"] = "cipsCryptomapSetIfTable"
            return self.cipscryptomapsetiftable

        if (child_yang_name == "cipsDynamicCryptomapSetTable"):
            if (self.cipsdynamiccryptomapsettable is None):
                self.cipsdynamiccryptomapsettable = CiscoIpsecMib.Cipsdynamiccryptomapsettable()
                self.cipsdynamiccryptomapsettable.parent = self
                self._children_name_map["cipsdynamiccryptomapsettable"] = "cipsDynamicCryptomapSetTable"
            return self.cipsdynamiccryptomapsettable

        if (child_yang_name == "cipsIPsecGlobals"):
            if (self.cipsipsecglobals is None):
                self.cipsipsecglobals = CiscoIpsecMib.Cipsipsecglobals()
                self.cipsipsecglobals.parent = self
                self._children_name_map["cipsipsecglobals"] = "cipsIPsecGlobals"
            return self.cipsipsecglobals

        if (child_yang_name == "cipsIPsecStatistics"):
            if (self.cipsipsecstatistics is None):
                self.cipsipsecstatistics = CiscoIpsecMib.Cipsipsecstatistics()
                self.cipsipsecstatistics.parent = self
                self._children_name_map["cipsipsecstatistics"] = "cipsIPsecStatistics"
            return self.cipsipsecstatistics

        if (child_yang_name == "cipsIsakmpGroup"):
            if (self.cipsisakmpgroup is None):
                self.cipsisakmpgroup = CiscoIpsecMib.Cipsisakmpgroup()
                self.cipsisakmpgroup.parent = self
                self._children_name_map["cipsisakmpgroup"] = "cipsIsakmpGroup"
            return self.cipsisakmpgroup

        if (child_yang_name == "cipsIsakmpPolicyTable"):
            if (self.cipsisakmppolicytable is None):
                self.cipsisakmppolicytable = CiscoIpsecMib.Cipsisakmppolicytable()
                self.cipsisakmppolicytable.parent = self
                self._children_name_map["cipsisakmppolicytable"] = "cipsIsakmpPolicyTable"
            return self.cipsisakmppolicytable

        if (child_yang_name == "cipsStaticCryptomapSetTable"):
            if (self.cipsstaticcryptomapsettable is None):
                self.cipsstaticcryptomapsettable = CiscoIpsecMib.Cipsstaticcryptomapsettable()
                self.cipsstaticcryptomapsettable.parent = self
                self._children_name_map["cipsstaticcryptomapsettable"] = "cipsStaticCryptomapSetTable"
            return self.cipsstaticcryptomapsettable

        if (child_yang_name == "cipsStaticCryptomapTable"):
            if (self.cipsstaticcryptomaptable is None):
                self.cipsstaticcryptomaptable = CiscoIpsecMib.Cipsstaticcryptomaptable()
                self.cipsstaticcryptomaptable.parent = self
                self._children_name_map["cipsstaticcryptomaptable"] = "cipsStaticCryptomapTable"
            return self.cipsstaticcryptomaptable

        if (child_yang_name == "cipsSysCapacityGroup"):
            if (self.cipssyscapacitygroup is None):
                self.cipssyscapacitygroup = CiscoIpsecMib.Cipssyscapacitygroup()
                self.cipssyscapacitygroup.parent = self
                self._children_name_map["cipssyscapacitygroup"] = "cipsSysCapacityGroup"
            return self.cipssyscapacitygroup

        if (child_yang_name == "cipsTrapCntlGroup"):
            if (self.cipstrapcntlgroup is None):
                self.cipstrapcntlgroup = CiscoIpsecMib.Cipstrapcntlgroup()
                self.cipstrapcntlgroup.parent = self
                self._children_name_map["cipstrapcntlgroup"] = "cipsTrapCntlGroup"
            return self.cipstrapcntlgroup

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cipsCryptomapSetIfTable" or name == "cipsDynamicCryptomapSetTable" or name == "cipsIPsecGlobals" or name == "cipsIPsecStatistics" or name == "cipsIsakmpGroup" or name == "cipsIsakmpPolicyTable" or name == "cipsStaticCryptomapSetTable" or name == "cipsStaticCryptomapTable" or name == "cipsSysCapacityGroup" or name == "cipsTrapCntlGroup"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIpsecMib()
        return self._top_entity

