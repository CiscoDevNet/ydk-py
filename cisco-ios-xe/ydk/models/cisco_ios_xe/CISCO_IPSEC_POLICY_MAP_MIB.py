""" CISCO_IPSEC_POLICY_MAP_MIB 

The MIB module maps the IPSec
entities created dynamically to the policy entities
that caused them. This is an appendix to the
IPSEC\-MONITOR\-MIB that has been proposed to
IETF for monitoring IPSec based Virtual Private 
Networks.

Overview of Cisco IPsec Policy Map MIB

MIB description

There are two components to this MIB\:  
  #1 a table that maps an IPSec Phase\-1 
     tunnel to the Internet Security Association 
     and Key Exchange (ISAKMP) Policy 
     
  and 

  #2 a table that maps an IPSec Phase\-2 
     tunnel to the corresponding IPSec Policy
     element \- called 'cryptomaps' \- in IOS 
     (Internet Operating System)

The first mappin (also called Internet Key Exchange
 or IKE mapping) yields, given the index of
the IKE tunnel in the ikeTunnelTable
(IPSEC\-MONITOR\-MIB), the ISAKMP policy definition
defined using the CLI on the managed entity.

The IPSec mapping yields, given the index
of the IPSec tunnel in the ipSecTunnelTable
(IPSEC\-MONITOR\-MIB), the IPSec transform and
the cryptomap definition that gave rise to
this tunnel.

In implementation and usage, this MIB cannot
exist independent of the IPSEC\-MONITOR\-MIB. 

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOIPSECPOLICYMAPMIB(Entity):
    """
    
    
    .. attribute:: ikepolmaptable
    
    	The IPSec Phase\-1 Internet Key Exchange Tunnel to Policy Mapping Table. There is one entry in this table for each active IPSec Phase\-1 Tunnel
    	**type**\:  :py:class:`Ikepolmaptable <ydk.models.cisco_ios_xe.CISCO_IPSEC_POLICY_MAP_MIB.CISCOIPSECPOLICYMAPMIB.Ikepolmaptable>`
    
    .. attribute:: ipsecpolmaptable
    
    	The IPSec Phase\-2 Tunnel to Policy Mapping Table. There is one entry in this table for each active IPSec Phase\-2 Tunnel
    	**type**\:  :py:class:`Ipsecpolmaptable <ydk.models.cisco_ios_xe.CISCO_IPSEC_POLICY_MAP_MIB.CISCOIPSECPOLICYMAPMIB.Ipsecpolmaptable>`
    
    

    """

    _prefix = 'CISCO-IPSEC-POLICY-MAP-MIB'
    _revision = '2000-08-17'

    def __init__(self):
        super(CISCOIPSECPOLICYMAPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IPSEC-POLICY-MAP-MIB"
        self.yang_parent_name = "CISCO-IPSEC-POLICY-MAP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ikePolMapTable", ("ikepolmaptable", CISCOIPSECPOLICYMAPMIB.Ikepolmaptable)), ("ipSecPolMapTable", ("ipsecpolmaptable", CISCOIPSECPOLICYMAPMIB.Ipsecpolmaptable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ikepolmaptable = CISCOIPSECPOLICYMAPMIB.Ikepolmaptable()
        self.ikepolmaptable.parent = self
        self._children_name_map["ikepolmaptable"] = "ikePolMapTable"
        self._children_yang_names.add("ikePolMapTable")

        self.ipsecpolmaptable = CISCOIPSECPOLICYMAPMIB.Ipsecpolmaptable()
        self.ipsecpolmaptable.parent = self
        self._children_name_map["ipsecpolmaptable"] = "ipSecPolMapTable"
        self._children_yang_names.add("ipSecPolMapTable")
        self._segment_path = lambda: "CISCO-IPSEC-POLICY-MAP-MIB:CISCO-IPSEC-POLICY-MAP-MIB"


    class Ikepolmaptable(Entity):
        """
        The IPSec Phase\-1 Internet Key Exchange Tunnel
        to Policy Mapping Table. There is one entry in
        this table for each active IPSec Phase\-1
        Tunnel.
        
        .. attribute:: ikepolmapentry
        
        	Each entry contains the attributes associated with mapping an active IPSec Phase\-1 IKE Tunnel to it's configured Policy definition
        	**type**\: list of  		 :py:class:`Ikepolmapentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_POLICY_MAP_MIB.CISCOIPSECPOLICYMAPMIB.Ikepolmaptable.Ikepolmapentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-POLICY-MAP-MIB'
        _revision = '2000-08-17'

        def __init__(self):
            super(CISCOIPSECPOLICYMAPMIB.Ikepolmaptable, self).__init__()

            self.yang_name = "ikePolMapTable"
            self.yang_parent_name = "CISCO-IPSEC-POLICY-MAP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ikePolMapEntry", ("ikepolmapentry", CISCOIPSECPOLICYMAPMIB.Ikepolmaptable.Ikepolmapentry))])
            self._leafs = OrderedDict()

            self.ikepolmapentry = YList(self)
            self._segment_path = lambda: "ikePolMapTable"
            self._absolute_path = lambda: "CISCO-IPSEC-POLICY-MAP-MIB:CISCO-IPSEC-POLICY-MAP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECPOLICYMAPMIB.Ikepolmaptable, [], name, value)


        class Ikepolmapentry(Entity):
            """
            Each entry contains the attributes associated
            with mapping an active IPSec Phase\-1 IKE Tunnel
            to it's configured Policy definition.
            
            .. attribute:: ikepolmaptunindex  (key)
            
            	The index of the IPSec Phase\-1 Tunnel to Policy Map Table.  The value of the index is the number used to represent this IPSec Phase\-1 Tunnel in the IPSec MIB (ikeTunIndex in the ikeTunnelTable)
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ikepolmappolicynum
            
            	The number of the locally defined ISAKMP policy used to establish the IPSec IKE Phase\-1 Tunnel. This is the number which was used on the crypto command. For example, if the configuration command was\:   ==>  crypto isakmp policy 15  then the value of this object would be 15. If ISAKMP was not used to establish this tunnel, then the value of this object will be zero
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'CISCO-IPSEC-POLICY-MAP-MIB'
            _revision = '2000-08-17'

            def __init__(self):
                super(CISCOIPSECPOLICYMAPMIB.Ikepolmaptable.Ikepolmapentry, self).__init__()

                self.yang_name = "ikePolMapEntry"
                self.yang_parent_name = "ikePolMapTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ikepolmaptunindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ikepolmaptunindex', YLeaf(YType.int32, 'ikePolMapTunIndex')),
                    ('ikepolmappolicynum', YLeaf(YType.int32, 'ikePolMapPolicyNum')),
                ])
                self.ikepolmaptunindex = None
                self.ikepolmappolicynum = None
                self._segment_path = lambda: "ikePolMapEntry" + "[ikePolMapTunIndex='" + str(self.ikepolmaptunindex) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-POLICY-MAP-MIB:CISCO-IPSEC-POLICY-MAP-MIB/ikePolMapTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECPOLICYMAPMIB.Ikepolmaptable.Ikepolmapentry, ['ikepolmaptunindex', 'ikepolmappolicynum'], name, value)


    class Ipsecpolmaptable(Entity):
        """
        The IPSec Phase\-2 Tunnel to Policy Mapping Table.
        There is one entry in this table for each active
        IPSec Phase\-2 Tunnel.
        
        .. attribute:: ipsecpolmapentry
        
        	Each entry contains the attributes associated with mapping an active IPSec Phase\-2 Tunnel to its configured Policy definition
        	**type**\: list of  		 :py:class:`Ipsecpolmapentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_POLICY_MAP_MIB.CISCOIPSECPOLICYMAPMIB.Ipsecpolmaptable.Ipsecpolmapentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-POLICY-MAP-MIB'
        _revision = '2000-08-17'

        def __init__(self):
            super(CISCOIPSECPOLICYMAPMIB.Ipsecpolmaptable, self).__init__()

            self.yang_name = "ipSecPolMapTable"
            self.yang_parent_name = "CISCO-IPSEC-POLICY-MAP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipSecPolMapEntry", ("ipsecpolmapentry", CISCOIPSECPOLICYMAPMIB.Ipsecpolmaptable.Ipsecpolmapentry))])
            self._leafs = OrderedDict()

            self.ipsecpolmapentry = YList(self)
            self._segment_path = lambda: "ipSecPolMapTable"
            self._absolute_path = lambda: "CISCO-IPSEC-POLICY-MAP-MIB:CISCO-IPSEC-POLICY-MAP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSECPOLICYMAPMIB.Ipsecpolmaptable, [], name, value)


        class Ipsecpolmapentry(Entity):
            """
            Each entry contains the attributes associated
            with mapping an active IPSec Phase\-2 Tunnel
            to its configured Policy definition.
            
            .. attribute:: ipsecpolmaptunindex  (key)
            
            	The index of the IPSec Phase\-2 Tunnel to Policy Map Table. The value of the index is the number used to represent this IPSec Phase\-2 Tunnel in the IPSec MIB (ipSecTunIndex in the ipSecTunnelTable)
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipsecpolmapcryptomapname
            
            	The value of this object should be the name of  the IPSec Policy (cryptomap) as assigned by the  operator while configuring the policy of  the IPSec traffic.  For instance, on an IOS router, the if the command entered to configure the IPSec policy was   ==>  crypto map ftpPolicy 10 ipsec\-isakmp  then the value of this object would be 'ftpPolicy'
            	**type**\: str
            
            .. attribute:: ipsecpolmapcryptomapnum
            
            	The value of this object should be the priority of the IPSec Policy (cryptomap) assigned by the  operator while configuring the policy of  this IPSec tunnel.  For instance, on an IOS router, the if the command entered to configure the IPSec policy was   ==>  crypto map ftpPolicy 10 ipsec\-isakmp  then the value of this object would be 10
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipsecpolmapaclstring
            
            	The value of this object is the number or the name of the access control string (ACL)  that caused this IPSec tunnel to be established.   The ACL that causes an IPSec tunnel  to be established is referenced by the   cryptomap of the tunnel.   The ACL identifies the traffic that requires  protection as defined by the policy.   For instance, the ACL that requires FTP  traffic between local subnet 172.16.14.0 and a  remote subnet 172.16.16.0 to be protected  is defined as   ==>access\-list 101 permit tcp 172.16.14.0 0.0.0.255                   172.16.16.0 0.0.0.255 eq ftp   When this command causes an IPSec tunnel to be   established, the object 'ipSecPolMapAclString'   assumes the string value '101'.   If the ACL is a named list such as   ==> ip access\-list standard myAcl        permit 172.16.16.8 0.0.0.0   then the value of this MIB element corresponding to    IPSec tunnel that was created by this ACL would   be 'myAcl'
            	**type**\: str
            
            .. attribute:: ipsecpolmapacestring
            
            	The value of this object is the access control  entry (ACE) within the ACL that caused this IPSec  tunnel to be established.   For instance, if an ACL defines access for two traffic streams (FTP and SNMP) as follows\:  access\-list 101 permit tcp 172.16.14.0 0.0.0.255                  172.16.16.0 0.0.0.255 eq ftp access\-list 101 permit udp 172.16.14.0 0.0.0.255                  host 172.16.16.1 eq 161   When associated with an IPSec policy, the second element of the ACL gives rise to an IPSec tunnel in the wake of SNMP traffic. The value of the object 'ipSecPolMapAceString' for the IPSec tunnel would be then the string 'access\-list 101 permit udp 172.16.14.0 0.0.0.255                  host 172.16.16.1 eq 161'
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-IPSEC-POLICY-MAP-MIB'
            _revision = '2000-08-17'

            def __init__(self):
                super(CISCOIPSECPOLICYMAPMIB.Ipsecpolmaptable.Ipsecpolmapentry, self).__init__()

                self.yang_name = "ipSecPolMapEntry"
                self.yang_parent_name = "ipSecPolMapTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipsecpolmaptunindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipsecpolmaptunindex', YLeaf(YType.int32, 'ipSecPolMapTunIndex')),
                    ('ipsecpolmapcryptomapname', YLeaf(YType.str, 'ipSecPolMapCryptoMapName')),
                    ('ipsecpolmapcryptomapnum', YLeaf(YType.int32, 'ipSecPolMapCryptoMapNum')),
                    ('ipsecpolmapaclstring', YLeaf(YType.str, 'ipSecPolMapAclString')),
                    ('ipsecpolmapacestring', YLeaf(YType.str, 'ipSecPolMapAceString')),
                ])
                self.ipsecpolmaptunindex = None
                self.ipsecpolmapcryptomapname = None
                self.ipsecpolmapcryptomapnum = None
                self.ipsecpolmapaclstring = None
                self.ipsecpolmapacestring = None
                self._segment_path = lambda: "ipSecPolMapEntry" + "[ipSecPolMapTunIndex='" + str(self.ipsecpolmaptunindex) + "']"
                self._absolute_path = lambda: "CISCO-IPSEC-POLICY-MAP-MIB:CISCO-IPSEC-POLICY-MAP-MIB/ipSecPolMapTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSECPOLICYMAPMIB.Ipsecpolmaptable.Ipsecpolmapentry, ['ipsecpolmaptunindex', 'ipsecpolmapcryptomapname', 'ipsecpolmapcryptomapnum', 'ipsecpolmapaclstring', 'ipsecpolmapacestring'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOIPSECPOLICYMAPMIB()
        return self._top_entity

