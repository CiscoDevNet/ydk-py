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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoIpsecPolicyMapMib(object):
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
        self.ikepolmaptable = CiscoIpsecPolicyMapMib.Ikepolmaptable()
        self.ikepolmaptable.parent = self
        self.ipsecpolmaptable = CiscoIpsecPolicyMapMib.Ipsecpolmaptable()
        self.ipsecpolmaptable.parent = self


    class Ikepolmaptable(object):
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
            self.parent = None
            self.ikepolmapentry = YList()
            self.ikepolmapentry.parent = self
            self.ikepolmapentry.name = 'ikepolmapentry'


        class Ikepolmapentry(object):
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
                self.parent = None
                self.ikepolmaptunindex = None
                self.ikepolmappolicynum = None

            @property
            def _common_path(self):
                if self.ikepolmaptunindex is None:
                    raise YPYModelError('Key property ikepolmaptunindex is None')

                return '/CISCO-IPSEC-POLICY-MAP-MIB:CISCO-IPSEC-POLICY-MAP-MIB/CISCO-IPSEC-POLICY-MAP-MIB:ikePolMapTable/CISCO-IPSEC-POLICY-MAP-MIB:ikePolMapEntry[CISCO-IPSEC-POLICY-MAP-MIB:ikePolMapTunIndex = ' + str(self.ikepolmaptunindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ikepolmaptunindex is not None:
                    return True

                if self.ikepolmappolicynum is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_POLICY_MAP_MIB as meta
                return meta._meta_table['CiscoIpsecPolicyMapMib.Ikepolmaptable.Ikepolmapentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-POLICY-MAP-MIB:CISCO-IPSEC-POLICY-MAP-MIB/CISCO-IPSEC-POLICY-MAP-MIB:ikePolMapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ikepolmapentry is not None:
                for child_ref in self.ikepolmapentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_POLICY_MAP_MIB as meta
            return meta._meta_table['CiscoIpsecPolicyMapMib.Ikepolmaptable']['meta_info']


    class Ipsecpolmaptable(object):
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
            self.parent = None
            self.ipsecpolmapentry = YList()
            self.ipsecpolmapentry.parent = self
            self.ipsecpolmapentry.name = 'ipsecpolmapentry'


        class Ipsecpolmapentry(object):
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
                self.parent = None
                self.ipsecpolmaptunindex = None
                self.ipsecpolmapacestring = None
                self.ipsecpolmapaclstring = None
                self.ipsecpolmapcryptomapname = None
                self.ipsecpolmapcryptomapnum = None

            @property
            def _common_path(self):
                if self.ipsecpolmaptunindex is None:
                    raise YPYModelError('Key property ipsecpolmaptunindex is None')

                return '/CISCO-IPSEC-POLICY-MAP-MIB:CISCO-IPSEC-POLICY-MAP-MIB/CISCO-IPSEC-POLICY-MAP-MIB:ipSecPolMapTable/CISCO-IPSEC-POLICY-MAP-MIB:ipSecPolMapEntry[CISCO-IPSEC-POLICY-MAP-MIB:ipSecPolMapTunIndex = ' + str(self.ipsecpolmaptunindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipsecpolmaptunindex is not None:
                    return True

                if self.ipsecpolmapacestring is not None:
                    return True

                if self.ipsecpolmapaclstring is not None:
                    return True

                if self.ipsecpolmapcryptomapname is not None:
                    return True

                if self.ipsecpolmapcryptomapnum is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_POLICY_MAP_MIB as meta
                return meta._meta_table['CiscoIpsecPolicyMapMib.Ipsecpolmaptable.Ipsecpolmapentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-POLICY-MAP-MIB:CISCO-IPSEC-POLICY-MAP-MIB/CISCO-IPSEC-POLICY-MAP-MIB:ipSecPolMapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipsecpolmapentry is not None:
                for child_ref in self.ipsecpolmapentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_POLICY_MAP_MIB as meta
            return meta._meta_table['CiscoIpsecPolicyMapMib.Ipsecpolmaptable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IPSEC-POLICY-MAP-MIB:CISCO-IPSEC-POLICY-MAP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ikepolmaptable is not None and self.ikepolmaptable._has_data():
            return True

        if self.ipsecpolmaptable is not None and self.ipsecpolmaptable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IPSEC_POLICY_MAP_MIB as meta
        return meta._meta_table['CiscoIpsecPolicyMapMib']['meta_info']


