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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIpsecPolicyMapMib(Entity):
    """
    
    
    .. attribute:: ikepolmaptable
    
    	The IPSec Phase\-1 Internet Key Exchange Tunnel to Policy Mapping Table. There is one entry in this table for each active IPSec Phase\-1 Tunnel
    	**type**\:   :py:class:`Ikepolmaptable <ydk.models.cisco_ios_xe.CISCO_IPSEC_POLICY_MAP_MIB.CiscoIpsecPolicyMapMib.Ikepolmaptable>`
    
    .. attribute:: ipsecpolmaptable
    
    	The IPSec Phase\-2 Tunnel to Policy Mapping Table. There is one entry in this table for each active IPSec Phase\-2 Tunnel
    	**type**\:   :py:class:`Ipsecpolmaptable <ydk.models.cisco_ios_xe.CISCO_IPSEC_POLICY_MAP_MIB.CiscoIpsecPolicyMapMib.Ipsecpolmaptable>`
    
    

    """

    _prefix = 'CISCO-IPSEC-POLICY-MAP-MIB'
    _revision = '2000-08-17'

    def __init__(self):
        super(CiscoIpsecPolicyMapMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IPSEC-POLICY-MAP-MIB"
        self.yang_parent_name = "CISCO-IPSEC-POLICY-MAP-MIB"

        self.ikepolmaptable = CiscoIpsecPolicyMapMib.Ikepolmaptable()
        self.ikepolmaptable.parent = self
        self._children_name_map["ikepolmaptable"] = "ikePolMapTable"
        self._children_yang_names.add("ikePolMapTable")

        self.ipsecpolmaptable = CiscoIpsecPolicyMapMib.Ipsecpolmaptable()
        self.ipsecpolmaptable.parent = self
        self._children_name_map["ipsecpolmaptable"] = "ipSecPolMapTable"
        self._children_yang_names.add("ipSecPolMapTable")


    class Ikepolmaptable(Entity):
        """
        The IPSec Phase\-1 Internet Key Exchange Tunnel
        to Policy Mapping Table. There is one entry in
        this table for each active IPSec Phase\-1
        Tunnel.
        
        .. attribute:: ikepolmapentry
        
        	Each entry contains the attributes associated with mapping an active IPSec Phase\-1 IKE Tunnel to it's configured Policy definition
        	**type**\: list of    :py:class:`Ikepolmapentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_POLICY_MAP_MIB.CiscoIpsecPolicyMapMib.Ikepolmaptable.Ikepolmapentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-POLICY-MAP-MIB'
        _revision = '2000-08-17'

        def __init__(self):
            super(CiscoIpsecPolicyMapMib.Ikepolmaptable, self).__init__()

            self.yang_name = "ikePolMapTable"
            self.yang_parent_name = "CISCO-IPSEC-POLICY-MAP-MIB"

            self.ikepolmapentry = YList(self)

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
                        super(CiscoIpsecPolicyMapMib.Ikepolmaptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecPolicyMapMib.Ikepolmaptable, self).__setattr__(name, value)


        class Ikepolmapentry(Entity):
            """
            Each entry contains the attributes associated
            with mapping an active IPSec Phase\-1 IKE Tunnel
            to it's configured Policy definition.
            
            .. attribute:: ikepolmaptunindex  <key>
            
            	The index of the IPSec Phase\-1 Tunnel to Policy Map Table.  The value of the index is the number used to represent this IPSec Phase\-1 Tunnel in the IPSec MIB (ikeTunIndex in the ikeTunnelTable)
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ikepolmappolicynum
            
            	The number of the locally defined ISAKMP policy used to establish the IPSec IKE Phase\-1 Tunnel. This is the number which was used on the crypto command. For example, if the configuration command was\:   ==>  crypto isakmp policy 15  then the value of this object would be 15. If ISAKMP was not used to establish this tunnel, then the value of this object will be zero
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'CISCO-IPSEC-POLICY-MAP-MIB'
            _revision = '2000-08-17'

            def __init__(self):
                super(CiscoIpsecPolicyMapMib.Ikepolmaptable.Ikepolmapentry, self).__init__()

                self.yang_name = "ikePolMapEntry"
                self.yang_parent_name = "ikePolMapTable"

                self.ikepolmaptunindex = YLeaf(YType.int32, "ikePolMapTunIndex")

                self.ikepolmappolicynum = YLeaf(YType.int32, "ikePolMapPolicyNum")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ikepolmaptunindex",
                                "ikepolmappolicynum") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecPolicyMapMib.Ikepolmaptable.Ikepolmapentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecPolicyMapMib.Ikepolmaptable.Ikepolmapentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ikepolmaptunindex.is_set or
                    self.ikepolmappolicynum.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ikepolmaptunindex.yfilter != YFilter.not_set or
                    self.ikepolmappolicynum.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ikePolMapEntry" + "[ikePolMapTunIndex='" + self.ikepolmaptunindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-POLICY-MAP-MIB:CISCO-IPSEC-POLICY-MAP-MIB/ikePolMapTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ikepolmaptunindex.is_set or self.ikepolmaptunindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ikepolmaptunindex.get_name_leafdata())
                if (self.ikepolmappolicynum.is_set or self.ikepolmappolicynum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ikepolmappolicynum.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ikePolMapTunIndex" or name == "ikePolMapPolicyNum"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ikePolMapTunIndex"):
                    self.ikepolmaptunindex = value
                    self.ikepolmaptunindex.value_namespace = name_space
                    self.ikepolmaptunindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ikePolMapPolicyNum"):
                    self.ikepolmappolicynum = value
                    self.ikepolmappolicynum.value_namespace = name_space
                    self.ikepolmappolicynum.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ikepolmapentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ikepolmapentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ikePolMapTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-POLICY-MAP-MIB:CISCO-IPSEC-POLICY-MAP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ikePolMapEntry"):
                for c in self.ikepolmapentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecPolicyMapMib.Ikepolmaptable.Ikepolmapentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ikepolmapentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ikePolMapEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ipsecpolmaptable(Entity):
        """
        The IPSec Phase\-2 Tunnel to Policy Mapping Table.
        There is one entry in this table for each active
        IPSec Phase\-2 Tunnel.
        
        .. attribute:: ipsecpolmapentry
        
        	Each entry contains the attributes associated with mapping an active IPSec Phase\-2 Tunnel to its configured Policy definition
        	**type**\: list of    :py:class:`Ipsecpolmapentry <ydk.models.cisco_ios_xe.CISCO_IPSEC_POLICY_MAP_MIB.CiscoIpsecPolicyMapMib.Ipsecpolmaptable.Ipsecpolmapentry>`
        
        

        """

        _prefix = 'CISCO-IPSEC-POLICY-MAP-MIB'
        _revision = '2000-08-17'

        def __init__(self):
            super(CiscoIpsecPolicyMapMib.Ipsecpolmaptable, self).__init__()

            self.yang_name = "ipSecPolMapTable"
            self.yang_parent_name = "CISCO-IPSEC-POLICY-MAP-MIB"

            self.ipsecpolmapentry = YList(self)

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
                        super(CiscoIpsecPolicyMapMib.Ipsecpolmaptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpsecPolicyMapMib.Ipsecpolmaptable, self).__setattr__(name, value)


        class Ipsecpolmapentry(Entity):
            """
            Each entry contains the attributes associated
            with mapping an active IPSec Phase\-2 Tunnel
            to its configured Policy definition.
            
            .. attribute:: ipsecpolmaptunindex  <key>
            
            	The index of the IPSec Phase\-2 Tunnel to Policy Map Table. The value of the index is the number used to represent this IPSec Phase\-2 Tunnel in the IPSec MIB (ipSecTunIndex in the ipSecTunnelTable)
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipsecpolmapacestring
            
            	The value of this object is the access control  entry (ACE) within the ACL that caused this IPSec  tunnel to be established.   For instance, if an ACL defines access for two traffic streams (FTP and SNMP) as follows\:  access\-list 101 permit tcp 172.16.14.0 0.0.0.255                  172.16.16.0 0.0.0.255 eq ftp access\-list 101 permit udp 172.16.14.0 0.0.0.255                  host 172.16.16.1 eq 161   When associated with an IPSec policy, the second element of the ACL gives rise to an IPSec tunnel in the wake of SNMP traffic. The value of the object 'ipSecPolMapAceString' for the IPSec tunnel would be then the string 'access\-list 101 permit udp 172.16.14.0 0.0.0.255                  host 172.16.16.1 eq 161'
            	**type**\:  str
            
            .. attribute:: ipsecpolmapaclstring
            
            	The value of this object is the number or the name of the access control string (ACL)  that caused this IPSec tunnel to be established.   The ACL that causes an IPSec tunnel  to be established is referenced by the   cryptomap of the tunnel.   The ACL identifies the traffic that requires  protection as defined by the policy.   For instance, the ACL that requires FTP  traffic between local subnet 172.16.14.0 and a  remote subnet 172.16.16.0 to be protected  is defined as   ==>access\-list 101 permit tcp 172.16.14.0 0.0.0.255                   172.16.16.0 0.0.0.255 eq ftp   When this command causes an IPSec tunnel to be   established, the object 'ipSecPolMapAclString'   assumes the string value '101'.   If the ACL is a named list such as   ==> ip access\-list standard myAcl        permit 172.16.16.8 0.0.0.0   then the value of this MIB element corresponding to    IPSec tunnel that was created by this ACL would   be 'myAcl'
            	**type**\:  str
            
            .. attribute:: ipsecpolmapcryptomapname
            
            	The value of this object should be the name of  the IPSec Policy (cryptomap) as assigned by the  operator while configuring the policy of  the IPSec traffic.  For instance, on an IOS router, the if the command entered to configure the IPSec policy was   ==>  crypto map ftpPolicy 10 ipsec\-isakmp  then the value of this object would be 'ftpPolicy'
            	**type**\:  str
            
            .. attribute:: ipsecpolmapcryptomapnum
            
            	The value of this object should be the priority of the IPSec Policy (cryptomap) assigned by the  operator while configuring the policy of  this IPSec tunnel.  For instance, on an IOS router, the if the command entered to configure the IPSec policy was   ==>  crypto map ftpPolicy 10 ipsec\-isakmp  then the value of this object would be 10
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'CISCO-IPSEC-POLICY-MAP-MIB'
            _revision = '2000-08-17'

            def __init__(self):
                super(CiscoIpsecPolicyMapMib.Ipsecpolmaptable.Ipsecpolmapentry, self).__init__()

                self.yang_name = "ipSecPolMapEntry"
                self.yang_parent_name = "ipSecPolMapTable"

                self.ipsecpolmaptunindex = YLeaf(YType.int32, "ipSecPolMapTunIndex")

                self.ipsecpolmapacestring = YLeaf(YType.str, "ipSecPolMapAceString")

                self.ipsecpolmapaclstring = YLeaf(YType.str, "ipSecPolMapAclString")

                self.ipsecpolmapcryptomapname = YLeaf(YType.str, "ipSecPolMapCryptoMapName")

                self.ipsecpolmapcryptomapnum = YLeaf(YType.int32, "ipSecPolMapCryptoMapNum")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipsecpolmaptunindex",
                                "ipsecpolmapacestring",
                                "ipsecpolmapaclstring",
                                "ipsecpolmapcryptomapname",
                                "ipsecpolmapcryptomapnum") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpsecPolicyMapMib.Ipsecpolmaptable.Ipsecpolmapentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpsecPolicyMapMib.Ipsecpolmaptable.Ipsecpolmapentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ipsecpolmaptunindex.is_set or
                    self.ipsecpolmapacestring.is_set or
                    self.ipsecpolmapaclstring.is_set or
                    self.ipsecpolmapcryptomapname.is_set or
                    self.ipsecpolmapcryptomapnum.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipsecpolmaptunindex.yfilter != YFilter.not_set or
                    self.ipsecpolmapacestring.yfilter != YFilter.not_set or
                    self.ipsecpolmapaclstring.yfilter != YFilter.not_set or
                    self.ipsecpolmapcryptomapname.yfilter != YFilter.not_set or
                    self.ipsecpolmapcryptomapnum.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipSecPolMapEntry" + "[ipSecPolMapTunIndex='" + self.ipsecpolmaptunindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSEC-POLICY-MAP-MIB:CISCO-IPSEC-POLICY-MAP-MIB/ipSecPolMapTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipsecpolmaptunindex.is_set or self.ipsecpolmaptunindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsecpolmaptunindex.get_name_leafdata())
                if (self.ipsecpolmapacestring.is_set or self.ipsecpolmapacestring.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsecpolmapacestring.get_name_leafdata())
                if (self.ipsecpolmapaclstring.is_set or self.ipsecpolmapaclstring.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsecpolmapaclstring.get_name_leafdata())
                if (self.ipsecpolmapcryptomapname.is_set or self.ipsecpolmapcryptomapname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsecpolmapcryptomapname.get_name_leafdata())
                if (self.ipsecpolmapcryptomapnum.is_set or self.ipsecpolmapcryptomapnum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsecpolmapcryptomapnum.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipSecPolMapTunIndex" or name == "ipSecPolMapAceString" or name == "ipSecPolMapAclString" or name == "ipSecPolMapCryptoMapName" or name == "ipSecPolMapCryptoMapNum"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipSecPolMapTunIndex"):
                    self.ipsecpolmaptunindex = value
                    self.ipsecpolmaptunindex.value_namespace = name_space
                    self.ipsecpolmaptunindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSecPolMapAceString"):
                    self.ipsecpolmapacestring = value
                    self.ipsecpolmapacestring.value_namespace = name_space
                    self.ipsecpolmapacestring.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSecPolMapAclString"):
                    self.ipsecpolmapaclstring = value
                    self.ipsecpolmapaclstring.value_namespace = name_space
                    self.ipsecpolmapaclstring.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSecPolMapCryptoMapName"):
                    self.ipsecpolmapcryptomapname = value
                    self.ipsecpolmapcryptomapname.value_namespace = name_space
                    self.ipsecpolmapcryptomapname.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSecPolMapCryptoMapNum"):
                    self.ipsecpolmapcryptomapnum = value
                    self.ipsecpolmapcryptomapnum.value_namespace = name_space
                    self.ipsecpolmapcryptomapnum.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipsecpolmapentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipsecpolmapentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipSecPolMapTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSEC-POLICY-MAP-MIB:CISCO-IPSEC-POLICY-MAP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipSecPolMapEntry"):
                for c in self.ipsecpolmapentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpsecPolicyMapMib.Ipsecpolmaptable.Ipsecpolmapentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipsecpolmapentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipSecPolMapEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ikepolmaptable is not None and self.ikepolmaptable.has_data()) or
            (self.ipsecpolmaptable is not None and self.ipsecpolmaptable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ikepolmaptable is not None and self.ikepolmaptable.has_operation()) or
            (self.ipsecpolmaptable is not None and self.ipsecpolmaptable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IPSEC-POLICY-MAP-MIB:CISCO-IPSEC-POLICY-MAP-MIB" + path_buffer

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

        if (child_yang_name == "ikePolMapTable"):
            if (self.ikepolmaptable is None):
                self.ikepolmaptable = CiscoIpsecPolicyMapMib.Ikepolmaptable()
                self.ikepolmaptable.parent = self
                self._children_name_map["ikepolmaptable"] = "ikePolMapTable"
            return self.ikepolmaptable

        if (child_yang_name == "ipSecPolMapTable"):
            if (self.ipsecpolmaptable is None):
                self.ipsecpolmaptable = CiscoIpsecPolicyMapMib.Ipsecpolmaptable()
                self.ipsecpolmaptable.parent = self
                self._children_name_map["ipsecpolmaptable"] = "ipSecPolMapTable"
            return self.ipsecpolmaptable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ikePolMapTable" or name == "ipSecPolMapTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIpsecPolicyMapMib()
        return self._top_entity

