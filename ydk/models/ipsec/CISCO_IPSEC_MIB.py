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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CryptomapSetBindStatus_Enum(Enum):
    """
    CryptomapSetBindStatus_Enum

    The status of the binding of a cryptomap set 
    to the specified interface. The value qhen queried
    is always 'attached'. When set to 'detached', the 
    cryptomap set if detached from the specified interface.
    Setting the value to 'attached' will result in 
    SNMP General Error.

    """

    UNKNOWN = 0

    ATTACHED = 1

    DETACHED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
        return meta._meta_table['CryptomapSetBindStatus_Enum']


class CryptomapType_Enum(Enum):
    """
    CryptomapType_Enum

    The type of a cryptomap entry. Cryptomap 
    is a unit of IOS IPSec policy specification.

    """

    CRYPTOMAPTYPENONE = 0

    CRYPTOMAPTYPEMANUAL = 1

    CRYPTOMAPTYPEISAKMP = 2

    CRYPTOMAPTYPECET = 3

    CRYPTOMAPTYPEDYNAMIC = 4

    CRYPTOMAPTYPEDYNAMICDISCOVERY = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
        return meta._meta_table['CryptomapType_Enum']


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
        from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
        return meta._meta_table['DiffHellmanGrp_Enum']


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
        from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
        return meta._meta_table['EncryptAlgo_Enum']


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
        from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
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
        from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
        return meta._meta_table['IkeHashAlgo_Enum']


class IkeIdentityType_Enum(Enum):
    """
    IkeIdentityType_Enum

    The type of identity used by the local entity to
    identity itself to the peer with which it performs
    IPSec Main Mode negotiations. This type decides the
    content of the Identification payload in the
    	Main Mode of IPSec tunnel setup.

    """

    ISAKMPIDTYPEUNKNOWN = 0

    ISAKMPIDTYPEADDRESS = 1

    ISAKMPIDTYPEHOSTNAME = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
        return meta._meta_table['IkeIdentityType_Enum']


class TrapStatus_Enum(Enum):
    """
    TrapStatus_Enum

    The administrative status for sending a TRAP.

    """

    ENABLED = 1

    DISABLED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
        return meta._meta_table['TrapStatus_Enum']



class CISCOIPSECMIB(object):
    """
    
    
    .. attribute:: cipscryptomapsetiftable
    
    	The table lists the binding of cryptomap sets to the interfaces of the managed entity
    	**type**\: :py:class:`CipsCryptomapSetIfTable <ydk.models.ipsec.CISCO_IPSEC_MIB.CISCOIPSECMIB.CipsCryptomapSetIfTable>`
    
    .. attribute:: cipsdynamiccryptomapsettable
    
    	The table containing the list of all dynamic cryptomaps that use IKE, defined on   the managed entity
    	**type**\: :py:class:`CipsDynamicCryptomapSetTable <ydk.models.ipsec.CISCO_IPSEC_MIB.CISCOIPSECMIB.CipsDynamicCryptomapSetTable>`
    
    .. attribute:: cipsipsecglobals
    
    	
    	**type**\: :py:class:`CipsIPsecGlobals <ydk.models.ipsec.CISCO_IPSEC_MIB.CISCOIPSECMIB.CipsIPsecGlobals>`
    
    .. attribute:: cipsipsecstatistics
    
    	
    	**type**\: :py:class:`CipsIPsecStatistics <ydk.models.ipsec.CISCO_IPSEC_MIB.CISCOIPSECMIB.CipsIPsecStatistics>`
    
    .. attribute:: cipsisakmpgroup
    
    	
    	**type**\: :py:class:`CipsIsakmpGroup <ydk.models.ipsec.CISCO_IPSEC_MIB.CISCOIPSECMIB.CipsIsakmpGroup>`
    
    .. attribute:: cipsisakmppolicytable
    
    	The table containing the list of all ISAKMP policy entries configured by the operator
    	**type**\: :py:class:`CipsIsakmpPolicyTable <ydk.models.ipsec.CISCO_IPSEC_MIB.CISCOIPSECMIB.CipsIsakmpPolicyTable>`
    
    .. attribute:: cipsstaticcryptomapsettable
    
    	The table containing the list of all cryptomap sets that are fully specified and are not wild\-carded.  The operator may include different types of cryptomaps in such a set \- manual, CET, ISAKMP or dynamic
    	**type**\: :py:class:`CipsStaticCryptomapSetTable <ydk.models.ipsec.CISCO_IPSEC_MIB.CISCOIPSECMIB.CipsStaticCryptomapSetTable>`
    
    .. attribute:: cipsstaticcryptomaptable
    
    	The table ilisting the member cryptomaps of the cryptomap sets that are configured on the managed entity
    	**type**\: :py:class:`CipsStaticCryptomapTable <ydk.models.ipsec.CISCO_IPSEC_MIB.CISCOIPSECMIB.CipsStaticCryptomapTable>`
    
    .. attribute:: cipssyscapacitygroup
    
    	
    	**type**\: :py:class:`CipsSysCapacityGroup <ydk.models.ipsec.CISCO_IPSEC_MIB.CISCOIPSECMIB.CipsSysCapacityGroup>`
    
    .. attribute:: cipstrapcntlgroup
    
    	
    	**type**\: :py:class:`CipsTrapCntlGroup <ydk.models.ipsec.CISCO_IPSEC_MIB.CISCOIPSECMIB.CipsTrapCntlGroup>`
    
    

    """

    _prefix = 'cisco-ipsec'
    _revision = '2000-08-07'

    def __init__(self):
        self.cipscryptomapsetiftable = CISCOIPSECMIB.CipsCryptomapSetIfTable()
        self.cipscryptomapsetiftable.parent = self
        self.cipsdynamiccryptomapsettable = CISCOIPSECMIB.CipsDynamicCryptomapSetTable()
        self.cipsdynamiccryptomapsettable.parent = self
        self.cipsipsecglobals = CISCOIPSECMIB.CipsIPsecGlobals()
        self.cipsipsecglobals.parent = self
        self.cipsipsecstatistics = CISCOIPSECMIB.CipsIPsecStatistics()
        self.cipsipsecstatistics.parent = self
        self.cipsisakmpgroup = CISCOIPSECMIB.CipsIsakmpGroup()
        self.cipsisakmpgroup.parent = self
        self.cipsisakmppolicytable = CISCOIPSECMIB.CipsIsakmpPolicyTable()
        self.cipsisakmppolicytable.parent = self
        self.cipsstaticcryptomapsettable = CISCOIPSECMIB.CipsStaticCryptomapSetTable()
        self.cipsstaticcryptomapsettable.parent = self
        self.cipsstaticcryptomaptable = CISCOIPSECMIB.CipsStaticCryptomapTable()
        self.cipsstaticcryptomaptable.parent = self
        self.cipssyscapacitygroup = CISCOIPSECMIB.CipsSysCapacityGroup()
        self.cipssyscapacitygroup.parent = self
        self.cipstrapcntlgroup = CISCOIPSECMIB.CipsTrapCntlGroup()
        self.cipstrapcntlgroup.parent = self


    class CipsCryptomapSetIfTable(object):
        """
        The table lists the binding of cryptomap sets
        to the interfaces of the managed entity.
        
        .. attribute:: cipscryptomapsetifentry
        
        	Each entry contains the record of the association between an interface and a cryptomap set (static) that is defined on the managed entity.  Note that the cryptomap set identified in  this binding must static. Dynamic cryptomaps cannot be bound to interfaces
        	**type**\: list of :py:class:`CipsCryptomapSetIfEntry <ydk.models.ipsec.CISCO_IPSEC_MIB.CISCOIPSECMIB.CipsCryptomapSetIfTable.CipsCryptomapSetIfEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2000-08-07'

        def __init__(self):
            self.parent = None
            self.cipscryptomapsetifentry = YList()
            self.cipscryptomapsetifentry.parent = self
            self.cipscryptomapsetifentry.name = 'cipscryptomapsetifentry'


        class CipsCryptomapSetIfEntry(object):
            """
            Each entry contains the record of
            the association between an interface
            and a cryptomap set (static) that is defined
            on the managed entity.
            
            Note that the cryptomap set identified in 
            this binding must static. Dynamic cryptomaps cannot
            be bound to interfaces.
            
            .. attribute:: cipsstaticcryptomapsetname
            
            	
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipscryptomapsetifstatus
            
            	This object identifies the status of the binding  of the specified cryptomap set with the specified interface. The value when queried is always 'attached'.  When set to 'detached', the cryptomap set if detached  from the specified interface. The effect of this is same  as the CLI command  	config\-if# no crypto map cryptomapSetName  Setting the value to 'attached' will result in  SNMP General Error
            	**type**\: :py:class:`CryptomapSetBindStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_MIB.CryptomapSetBindStatus_Enum>`
            
            .. attribute:: cipscryptomapsetifvirtual
            
            	The value of this object identifies if the interface to which the cryptomap set is attached is a tunnel (such as a GRE or PPTP tunnel)
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2000-08-07'

            def __init__(self):
                self.parent = None
                self.cipsstaticcryptomapsetname = None
                self.ifindex = None
                self.cipscryptomapsetifstatus = None
                self.cipscryptomapsetifvirtual = None

            @property
            def _common_path(self):
                if self.cipsstaticcryptomapsetname is None:
                    raise YPYDataValidationError('Key property cipsstaticcryptomapsetname is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/CISCO-IPSEC-MIB:cipsCryptomapSetIfTable/CISCO-IPSEC-MIB:cipsCryptomapSetIfEntry[CISCO-IPSEC-MIB:cipsStaticCryptomapSetName = ' + str(self.cipsstaticcryptomapsetname) + '][CISCO-IPSEC-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cipsstaticcryptomapsetname is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.cipscryptomapsetifstatus is not None:
                    return True

                if self.cipscryptomapsetifvirtual is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
                return meta._meta_table['CISCOIPSECMIB.CipsCryptomapSetIfTable.CipsCryptomapSetIfEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/CISCO-IPSEC-MIB:cipsCryptomapSetIfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipscryptomapsetifentry is not None:
                for child_ref in self.cipscryptomapsetifentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
            return meta._meta_table['CISCOIPSECMIB.CipsCryptomapSetIfTable']['meta_info']


    class CipsDynamicCryptomapSetTable(object):
        """
        The table containing the list of all dynamic
        cryptomaps that use IKE, defined on 
         the managed entity.
        
        .. attribute:: cipsdynamiccryptomapsetentry
        
        	Each entry contains the attributes associated with a single dynamic cryptomap template
        	**type**\: list of :py:class:`CipsDynamicCryptomapSetEntry <ydk.models.ipsec.CISCO_IPSEC_MIB.CISCOIPSECMIB.CipsDynamicCryptomapSetTable.CipsDynamicCryptomapSetEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2000-08-07'

        def __init__(self):
            self.parent = None
            self.cipsdynamiccryptomapsetentry = YList()
            self.cipsdynamiccryptomapsetentry.parent = self
            self.cipsdynamiccryptomapsetentry.name = 'cipsdynamiccryptomapsetentry'


        class CipsDynamicCryptomapSetEntry(object):
            """
            Each entry contains the attributes associated
            with a single dynamic cryptomap template.
            
            .. attribute:: cipsdynamiccryptomapsetname
            
            	The index of the dynamic cryptomap table.  The value of the string is the one assigned  by the operator in defining the cryptomap set
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cipsdynamiccryptomapsetnumassoc
            
            	The number of static cryptomap sets with which this dynamic cryptomap is associated.  
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsdynamiccryptomapsetsize
            
            	The number of cryptomap entries in this cryptomap
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2000-08-07'

            def __init__(self):
                self.parent = None
                self.cipsdynamiccryptomapsetname = None
                self.cipsdynamiccryptomapsetnumassoc = None
                self.cipsdynamiccryptomapsetsize = None

            @property
            def _common_path(self):
                if self.cipsdynamiccryptomapsetname is None:
                    raise YPYDataValidationError('Key property cipsdynamiccryptomapsetname is None')

                return '/CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/CISCO-IPSEC-MIB:cipsDynamicCryptomapSetTable/CISCO-IPSEC-MIB:cipsDynamicCryptomapSetEntry[CISCO-IPSEC-MIB:cipsDynamicCryptomapSetName = ' + str(self.cipsdynamiccryptomapsetname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cipsdynamiccryptomapsetname is not None:
                    return True

                if self.cipsdynamiccryptomapsetnumassoc is not None:
                    return True

                if self.cipsdynamiccryptomapsetsize is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
                return meta._meta_table['CISCOIPSECMIB.CipsDynamicCryptomapSetTable.CipsDynamicCryptomapSetEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/CISCO-IPSEC-MIB:cipsDynamicCryptomapSetTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsdynamiccryptomapsetentry is not None:
                for child_ref in self.cipsdynamiccryptomapsetentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
            return meta._meta_table['CISCOIPSECMIB.CipsDynamicCryptomapSetTable']['meta_info']


    class CipsIPsecGlobals(object):
        """
        
        
        .. attribute:: cipsnumcetcryptomapsets
        
        	The number of static Cryptomap Sets that have  at least one CET cryptomap element as a member of the set
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: cipsnumdynamiccryptomapsets
        
        	The number of dynamic IPSec Policy templates (called 'dynamic cryptomap templates') configured on the managed entity
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: cipsnumstaticcryptomapsets
        
        	The number of Cryptomap Sets that are are fully configured. Statically defined cryptomap sets  are ones where the operator has fully specified all the parameters required set up IPSec  Virtual Private Networks (VPNs)
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: cipsnumtedcryptomapsets
        
        	The number of static Cryptomap Sets that have  at least one dynamic cryptomap template  bound to them which has the Tunnel Endpoint Discovery (TED) enabled
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: cipssalifesize
        
        	The default lifesize in KBytes assigned to an SA  as a global policy (unless overridden in cryptomap  definition)
        	**type**\: int
        
        	**range:** 2560..536870912
        
        .. attribute:: cipssalifetime
        
        	The default lifetime (in seconds) assigned  to an SA as a global policy (maybe overridden  in specific cryptomap definitions)
        	**type**\: int
        
        	**range:** 120..86400
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2000-08-07'

        def __init__(self):
            self.parent = None
            self.cipsnumcetcryptomapsets = None
            self.cipsnumdynamiccryptomapsets = None
            self.cipsnumstaticcryptomapsets = None
            self.cipsnumtedcryptomapsets = None
            self.cipssalifesize = None
            self.cipssalifetime = None

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/CISCO-IPSEC-MIB:cipsIPsecGlobals'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsnumcetcryptomapsets is not None:
                return True

            if self.cipsnumdynamiccryptomapsets is not None:
                return True

            if self.cipsnumstaticcryptomapsets is not None:
                return True

            if self.cipsnumtedcryptomapsets is not None:
                return True

            if self.cipssalifesize is not None:
                return True

            if self.cipssalifetime is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
            return meta._meta_table['CISCOIPSECMIB.CipsIPsecGlobals']['meta_info']


    class CipsIPsecStatistics(object):
        """
        
        
        .. attribute:: cipsnumtedfailures
        
        	The number of TED probes that were dispatched by  the local entity and that failed to locate crypto  endpoint.  Not affected by any CLI operation
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsnumtedprobesreceived
        
        	The number of TED probes that were received by this  managed entity since bootup. Not affected by any  CLI operation
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cipsnumtedprobessent
        
        	The number of TED probes that were dispatched by all the dynamic cryptomaps in this managed entity since  bootup. Not affected by any CLI operation
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2000-08-07'

        def __init__(self):
            self.parent = None
            self.cipsnumtedfailures = None
            self.cipsnumtedprobesreceived = None
            self.cipsnumtedprobessent = None

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/CISCO-IPSEC-MIB:cipsIPsecStatistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsnumtedfailures is not None:
                return True

            if self.cipsnumtedprobesreceived is not None:
                return True

            if self.cipsnumtedprobessent is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
            return meta._meta_table['CISCOIPSECMIB.CipsIPsecStatistics']['meta_info']


    class CipsIsakmpGroup(object):
        """
        
        
        .. attribute:: cipsisakmpenabled
        
        	The value of this object is TRUE if ISAKMP has been enabled on the managed entity. Otherise the value of this object is FALSE
        	**type**\: bool
        
        .. attribute:: cipsisakmpidentity
        
        	The value of this object is shows the type of identity used by the managed entity in ISAKMP negotiations with another peer
        	**type**\: :py:class:`IkeIdentityType_Enum <ydk.models.ipsec.CISCO_IPSEC_MIB.IkeIdentityType_Enum>`
        
        .. attribute:: cipsisakmpkeepaliveinterval
        
        	The value of this object is time interval in seconds between successive ISAKMP keepalive heartbeats issued to the peers to which IKE tunnels have been setup
        	**type**\: int
        
        	**range:** 10..3600
        
        .. attribute:: cipsnumisakmppolicies
        
        	The value of this object is the number of ISAKMP policies that have been configured on the  managed entity
        	**type**\: int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2000-08-07'

        def __init__(self):
            self.parent = None
            self.cipsisakmpenabled = None
            self.cipsisakmpidentity = None
            self.cipsisakmpkeepaliveinterval = None
            self.cipsnumisakmppolicies = None

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/CISCO-IPSEC-MIB:cipsIsakmpGroup'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsisakmpenabled is not None:
                return True

            if self.cipsisakmpidentity is not None:
                return True

            if self.cipsisakmpkeepaliveinterval is not None:
                return True

            if self.cipsnumisakmppolicies is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
            return meta._meta_table['CISCOIPSECMIB.CipsIsakmpGroup']['meta_info']


    class CipsIsakmpPolicyTable(object):
        """
        The table containing the list of all
        ISAKMP policy entries configured by the operator.
        
        .. attribute:: cipsisakmppolicyentry
        
        	Each entry contains the attributes  associated with a single ISAKMP Policy entry
        	**type**\: list of :py:class:`CipsIsakmpPolicyEntry <ydk.models.ipsec.CISCO_IPSEC_MIB.CISCOIPSECMIB.CipsIsakmpPolicyTable.CipsIsakmpPolicyEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2000-08-07'

        def __init__(self):
            self.parent = None
            self.cipsisakmppolicyentry = YList()
            self.cipsisakmppolicyentry.parent = self
            self.cipsisakmppolicyentry.name = 'cipsisakmppolicyentry'


        class CipsIsakmpPolicyEntry(object):
            """
            Each entry contains the attributes 
            associated with a single ISAKMP
            Policy entry.
            
            .. attribute:: cipsisakmppolpriority
            
            	The priotity of this ISAKMP Policy entry. This is also the index of this table
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cipsisakmppolauth
            
            	The peer authentication mthod specified by this ISAKMP policy specification. If this policy entity is selected for negotiation with a peer, the local entity would authenticate the peer using  the method specified by this object
            	**type**\: :py:class:`IkeAuthMethod_Enum <ydk.models.ipsec.CISCO_IPSEC_MIB.IkeAuthMethod_Enum>`
            
            .. attribute:: cipsisakmppolencr
            
            	The encryption transform specified by this  ISAKMP policy specification. The Internet Key Exchange (IKE) tunnels setup using this policy item would use the specified encryption transform to protect the ISAKMP PDUs
            	**type**\: :py:class:`EncryptAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_MIB.EncryptAlgo_Enum>`
            
            .. attribute:: cipsisakmppolgroup
            
            	This object specifies the Oakley group used  for Diffie Hellman exchange in the Main Mode.  If this policy item is selected to negotiate Main Mode with an IKE peer, the local entity  chooses the group specified by this object to perform Diffie Hellman exchange with the peer
            	**type**\: :py:class:`DiffHellmanGrp_Enum <ydk.models.ipsec.CISCO_IPSEC_MIB.DiffHellmanGrp_Enum>`
            
            .. attribute:: cipsisakmppolhash
            
            	The hash transform specified by this  ISAKMP policy specification. The IKE tunnels setup using this policy item would use the  specified hash transform to protect the ISAKMP PDUs
            	**type**\: :py:class:`IkeHashAlgo_Enum <ydk.models.ipsec.CISCO_IPSEC_MIB.IkeHashAlgo_Enum>`
            
            .. attribute:: cipsisakmppollifetime
            
            	This object specifies the lifetime in seconds of the IKE tunnels generated using this  policy specification
            	**type**\: int
            
            	**range:** 60..86400
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2000-08-07'

            def __init__(self):
                self.parent = None
                self.cipsisakmppolpriority = None
                self.cipsisakmppolauth = None
                self.cipsisakmppolencr = None
                self.cipsisakmppolgroup = None
                self.cipsisakmppolhash = None
                self.cipsisakmppollifetime = None

            @property
            def _common_path(self):
                if self.cipsisakmppolpriority is None:
                    raise YPYDataValidationError('Key property cipsisakmppolpriority is None')

                return '/CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/CISCO-IPSEC-MIB:cipsIsakmpPolicyTable/CISCO-IPSEC-MIB:cipsIsakmpPolicyEntry[CISCO-IPSEC-MIB:cipsIsakmpPolPriority = ' + str(self.cipsisakmppolpriority) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cipsisakmppolpriority is not None:
                    return True

                if self.cipsisakmppolauth is not None:
                    return True

                if self.cipsisakmppolencr is not None:
                    return True

                if self.cipsisakmppolgroup is not None:
                    return True

                if self.cipsisakmppolhash is not None:
                    return True

                if self.cipsisakmppollifetime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
                return meta._meta_table['CISCOIPSECMIB.CipsIsakmpPolicyTable.CipsIsakmpPolicyEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/CISCO-IPSEC-MIB:cipsIsakmpPolicyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsisakmppolicyentry is not None:
                for child_ref in self.cipsisakmppolicyentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
            return meta._meta_table['CISCOIPSECMIB.CipsIsakmpPolicyTable']['meta_info']


    class CipsStaticCryptomapSetTable(object):
        """
        The table containing the list of all
        cryptomap sets that are fully specified
        and are not wild\-carded.
        
        The operator may include different types of
        cryptomaps in such a set \- manual, CET,
        ISAKMP or dynamic.
        
        .. attribute:: cipsstaticcryptomapsetentry
        
        	Each entry contains the attributes  associated with a single static  cryptomap set
        	**type**\: list of :py:class:`CipsStaticCryptomapSetEntry <ydk.models.ipsec.CISCO_IPSEC_MIB.CISCOIPSECMIB.CipsStaticCryptomapSetTable.CipsStaticCryptomapSetEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2000-08-07'

        def __init__(self):
            self.parent = None
            self.cipsstaticcryptomapsetentry = YList()
            self.cipsstaticcryptomapsetentry.parent = self
            self.cipsstaticcryptomapsetentry.name = 'cipsstaticcryptomapsetentry'


        class CipsStaticCryptomapSetEntry(object):
            """
            Each entry contains the attributes 
            associated with a single static 
            cryptomap set.
            
            .. attribute:: cipsstaticcryptomapsetname
            
            	The index of the static cryptomap table. The value  of the string is the name string assigned by the  operator in defining the cryptomap set
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cipsstaticcryptomapsetnumcet
            
            	The number of cryptomaps of type 'ipsec\-cisco'  associated with this cryptomap set. Such cryptomap elements implement Cisco Encryption Technology based Virtual Private Networks
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsstaticcryptomapsetnumdisc
            
            	The number of dynamic cryptomap templates linked to this cryptomap set that have Tunnel Endpoint Discovery (TED) enabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsstaticcryptomapsetnumdynamic
            
            	The number of dynamic cryptomap templates linked to this cryptomap set
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
            
            .. attribute:: cipsstaticcryptomapsetnumsas
            
            	The number of and IPsec Security Associations that are active and were setup using this cryptomap.  
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipsstaticcryptomapsetsize
            
            	The total number of cryptomap entries contained in this cryptomap set. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2000-08-07'

            def __init__(self):
                self.parent = None
                self.cipsstaticcryptomapsetname = None
                self.cipsstaticcryptomapsetnumcet = None
                self.cipsstaticcryptomapsetnumdisc = None
                self.cipsstaticcryptomapsetnumdynamic = None
                self.cipsstaticcryptomapsetnumisakmp = None
                self.cipsstaticcryptomapsetnummanual = None
                self.cipsstaticcryptomapsetnumsas = None
                self.cipsstaticcryptomapsetsize = None

            @property
            def _common_path(self):
                if self.cipsstaticcryptomapsetname is None:
                    raise YPYDataValidationError('Key property cipsstaticcryptomapsetname is None')

                return '/CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/CISCO-IPSEC-MIB:cipsStaticCryptomapSetTable/CISCO-IPSEC-MIB:cipsStaticCryptomapSetEntry[CISCO-IPSEC-MIB:cipsStaticCryptomapSetName = ' + str(self.cipsstaticcryptomapsetname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cipsstaticcryptomapsetname is not None:
                    return True

                if self.cipsstaticcryptomapsetnumcet is not None:
                    return True

                if self.cipsstaticcryptomapsetnumdisc is not None:
                    return True

                if self.cipsstaticcryptomapsetnumdynamic is not None:
                    return True

                if self.cipsstaticcryptomapsetnumisakmp is not None:
                    return True

                if self.cipsstaticcryptomapsetnummanual is not None:
                    return True

                if self.cipsstaticcryptomapsetnumsas is not None:
                    return True

                if self.cipsstaticcryptomapsetsize is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
                return meta._meta_table['CISCOIPSECMIB.CipsStaticCryptomapSetTable.CipsStaticCryptomapSetEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/CISCO-IPSEC-MIB:cipsStaticCryptomapSetTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsstaticcryptomapsetentry is not None:
                for child_ref in self.cipsstaticcryptomapsetentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
            return meta._meta_table['CISCOIPSECMIB.CipsStaticCryptomapSetTable']['meta_info']


    class CipsStaticCryptomapTable(object):
        """
        The table ilisting the member cryptomaps
        of the cryptomap sets that are configured
        on the managed entity.
        
        .. attribute:: cipsstaticcryptomapentry
        
        	Each entry contains the attributes  associated with a single static  (fully specified) cryptomap entry. This table does not include the members  of dynamic cryptomap sets that may be linked with the parent static cryptomap set
        	**type**\: list of :py:class:`CipsStaticCryptomapEntry <ydk.models.ipsec.CISCO_IPSEC_MIB.CISCOIPSECMIB.CipsStaticCryptomapTable.CipsStaticCryptomapEntry>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2000-08-07'

        def __init__(self):
            self.parent = None
            self.cipsstaticcryptomapentry = YList()
            self.cipsstaticcryptomapentry.parent = self
            self.cipsstaticcryptomapentry.name = 'cipsstaticcryptomapentry'


        class CipsStaticCryptomapEntry(object):
            """
            Each entry contains the attributes 
            associated with a single static 
            (fully specified) cryptomap entry.
            This table does not include the members 
            of dynamic cryptomap sets that may be
            linked with the parent static cryptomap set.
            
            .. attribute:: cipsstaticcryptomappriority
            
            	The priority of the cryptomap entry in the  cryptomap set. This is the second index component of this table
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cipsstaticcryptomapsetname
            
            	
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cipsstaticcryptomapdescr
            
            	The description string entered by the operatoir while creating this cryptomap. The string generally identifies a description and the purpose of this policy
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cipsstaticcryptomaplevelhost
            
            	This object identifies the granularity of the IPSec SAs created using this IPSec policy entry.  If this value is TRUE, distinct SA bundles are created for distinct hosts at the end of the application traffic
            	**type**\: bool
            
            .. attribute:: cipsstaticcryptomaplifesize
            
            	This object identifies the lifesize (maximum traffic in bytes that may be carried) of the IPSec SAs created using this IPSec policy entry.  If this value is zero, the lifetime assumes the  value specified by the global lifesize parameter
            	**type**\: int
            
            	**range:** 0 \| 2560..536870912
            
            .. attribute:: cipsstaticcryptomaplifetime
            
            	This object identifies the lifetime of the IPSec Security Associations (SA) created using this IPSec policy entry. If this value is zero, the lifetime assumes the  value specified by the global lifetime parameter
            	**type**\: int
            
            	**range:** 0 \| 120..86400
            
            .. attribute:: cipsstaticcryptomapnumpeers
            
            	The number of peers associated with this cryptomap  entry. The peers other than the one identified by  'cipsStaticCryptomapPeer' are backup peers.   Manual cryptomaps may have only one peer
            	**type**\: int
            
            	**range:** 0..40
            
            .. attribute:: cipsstaticcryptomappeer
            
            	The IP address of the current peer associated with  this IPSec policy item. Traffic that is protected by this cryptomap is protected by a tunnel that terminates at the device whose IP address is specified by this object
            	**type**\: str
            
            	**range:** 4 \| 16
            
            .. attribute:: cipsstaticcryptomappfs
            
            	This object identifies if the tunnels instantiated due to this policy item should use Perfect Forward Secrecy  (PFS) and if so, what group of Oakley they should use
            	**type**\: :py:class:`DiffHellmanGrp_Enum <ydk.models.ipsec.CISCO_IPSEC_MIB.DiffHellmanGrp_Enum>`
            
            .. attribute:: cipsstaticcryptomaptype
            
            	The type of the cryptomap entry. This can be an ISAKMP cryptomap, CET or manual. Dynamic cryptomaps are not counted in this table
            	**type**\: :py:class:`CryptomapType_Enum <ydk.models.ipsec.CISCO_IPSEC_MIB.CryptomapType_Enum>`
            
            

            """

            _prefix = 'cisco-ipsec'
            _revision = '2000-08-07'

            def __init__(self):
                self.parent = None
                self.cipsstaticcryptomappriority = None
                self.cipsstaticcryptomapsetname = None
                self.cipsstaticcryptomapdescr = None
                self.cipsstaticcryptomaplevelhost = None
                self.cipsstaticcryptomaplifesize = None
                self.cipsstaticcryptomaplifetime = None
                self.cipsstaticcryptomapnumpeers = None
                self.cipsstaticcryptomappeer = None
                self.cipsstaticcryptomappfs = None
                self.cipsstaticcryptomaptype = None

            @property
            def _common_path(self):
                if self.cipsstaticcryptomappriority is None:
                    raise YPYDataValidationError('Key property cipsstaticcryptomappriority is None')
                if self.cipsstaticcryptomapsetname is None:
                    raise YPYDataValidationError('Key property cipsstaticcryptomapsetname is None')

                return '/CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/CISCO-IPSEC-MIB:cipsStaticCryptomapTable/CISCO-IPSEC-MIB:cipsStaticCryptomapEntry[CISCO-IPSEC-MIB:cipsStaticCryptomapPriority = ' + str(self.cipsstaticcryptomappriority) + '][CISCO-IPSEC-MIB:cipsStaticCryptomapSetName = ' + str(self.cipsstaticcryptomapsetname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cipsstaticcryptomappriority is not None:
                    return True

                if self.cipsstaticcryptomapsetname is not None:
                    return True

                if self.cipsstaticcryptomapdescr is not None:
                    return True

                if self.cipsstaticcryptomaplevelhost is not None:
                    return True

                if self.cipsstaticcryptomaplifesize is not None:
                    return True

                if self.cipsstaticcryptomaplifetime is not None:
                    return True

                if self.cipsstaticcryptomapnumpeers is not None:
                    return True

                if self.cipsstaticcryptomappeer is not None:
                    return True

                if self.cipsstaticcryptomappfs is not None:
                    return True

                if self.cipsstaticcryptomaptype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
                return meta._meta_table['CISCOIPSECMIB.CipsStaticCryptomapTable.CipsStaticCryptomapEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/CISCO-IPSEC-MIB:cipsStaticCryptomapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipsstaticcryptomapentry is not None:
                for child_ref in self.cipsstaticcryptomapentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
            return meta._meta_table['CISCOIPSECMIB.CipsStaticCryptomapTable']['meta_info']


    class CipsSysCapacityGroup(object):
        """
        
        
        .. attribute:: cips3descapable
        
        	The value of this object is TRUE if the  managed entity has the hardware nad software  features to support 3DES encryption algorithm.  Not affected by any CLI operation
        	**type**\: bool
        
        .. attribute:: cipsmaxsas
        
        	The maximum number of IPsec Security Associations that can be established on this managed entity. If no theoretical limit exists, this returns value 0.  Not affected by any CLI operation
        	**type**\: int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2000-08-07'

        def __init__(self):
            self.parent = None
            self.cips3descapable = None
            self.cipsmaxsas = None

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/CISCO-IPSEC-MIB:cipsSysCapacityGroup'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cips3descapable is not None:
                return True

            if self.cipsmaxsas is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
            return meta._meta_table['CISCOIPSECMIB.CipsSysCapacityGroup']['meta_info']


    class CipsTrapCntlGroup(object):
        """
        
        
        .. attribute:: cipscntlcryptomapadded
        
        	This object defines the administrative state of  sending the IOS IPsec Cryptomap Add trap
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipscntlcryptomapdeleted
        
        	This object defines the administrative state of  sending the IOS IPsec Cryptomap Delete trap
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipscntlcryptomapsetattached
        
        	This object defines the administrative state of  sending the IOS IPsec trap that is issued when a cryptomap set is attached to an interface
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipscntlcryptomapsetdetached
        
        	This object defines the administrative state of  sending the IOS IPsec trap that is issued when a cryptomap set is detached from an interface. to which it was earlier bound
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipscntlisakmppolicyadded
        
        	This object defines the administrative state of  sending the IOS IPsec ISAKMP Policy Add trap
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipscntlisakmppolicydeleted
        
        	This object defines the administrative state of  sending the IOS IPsec ISAKMP Policy Delete trap
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_MIB.TrapStatus_Enum>`
        
        .. attribute:: cipscntltoomanysas
        
        	This object defines the administrative state of  sending the IOS IPsec trap that is issued when the number of SAs crosses the maximum number of SAs that may be supported on the managed entity
        	**type**\: :py:class:`TrapStatus_Enum <ydk.models.ipsec.CISCO_IPSEC_MIB.TrapStatus_Enum>`
        
        

        """

        _prefix = 'cisco-ipsec'
        _revision = '2000-08-07'

        def __init__(self):
            self.parent = None
            self.cipscntlcryptomapadded = None
            self.cipscntlcryptomapdeleted = None
            self.cipscntlcryptomapsetattached = None
            self.cipscntlcryptomapsetdetached = None
            self.cipscntlisakmppolicyadded = None
            self.cipscntlisakmppolicydeleted = None
            self.cipscntltoomanysas = None

        @property
        def _common_path(self):

            return '/CISCO-IPSEC-MIB:CISCO-IPSEC-MIB/CISCO-IPSEC-MIB:cipsTrapCntlGroup'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cipscntlcryptomapadded is not None:
                return True

            if self.cipscntlcryptomapdeleted is not None:
                return True

            if self.cipscntlcryptomapsetattached is not None:
                return True

            if self.cipscntlcryptomapsetdetached is not None:
                return True

            if self.cipscntlisakmppolicyadded is not None:
                return True

            if self.cipscntlisakmppolicydeleted is not None:
                return True

            if self.cipscntltoomanysas is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
            return meta._meta_table['CISCOIPSECMIB.CipsTrapCntlGroup']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IPSEC-MIB:CISCO-IPSEC-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cipscryptomapsetiftable is not None and self.cipscryptomapsetiftable._has_data():
            return True

        if self.cipscryptomapsetiftable is not None and self.cipscryptomapsetiftable.is_presence():
            return True

        if self.cipsdynamiccryptomapsettable is not None and self.cipsdynamiccryptomapsettable._has_data():
            return True

        if self.cipsdynamiccryptomapsettable is not None and self.cipsdynamiccryptomapsettable.is_presence():
            return True

        if self.cipsipsecglobals is not None and self.cipsipsecglobals._has_data():
            return True

        if self.cipsipsecglobals is not None and self.cipsipsecglobals.is_presence():
            return True

        if self.cipsipsecstatistics is not None and self.cipsipsecstatistics._has_data():
            return True

        if self.cipsipsecstatistics is not None and self.cipsipsecstatistics.is_presence():
            return True

        if self.cipsisakmpgroup is not None and self.cipsisakmpgroup._has_data():
            return True

        if self.cipsisakmpgroup is not None and self.cipsisakmpgroup.is_presence():
            return True

        if self.cipsisakmppolicytable is not None and self.cipsisakmppolicytable._has_data():
            return True

        if self.cipsisakmppolicytable is not None and self.cipsisakmppolicytable.is_presence():
            return True

        if self.cipsstaticcryptomapsettable is not None and self.cipsstaticcryptomapsettable._has_data():
            return True

        if self.cipsstaticcryptomapsettable is not None and self.cipsstaticcryptomapsettable.is_presence():
            return True

        if self.cipsstaticcryptomaptable is not None and self.cipsstaticcryptomaptable._has_data():
            return True

        if self.cipsstaticcryptomaptable is not None and self.cipsstaticcryptomaptable.is_presence():
            return True

        if self.cipssyscapacitygroup is not None and self.cipssyscapacitygroup._has_data():
            return True

        if self.cipssyscapacitygroup is not None and self.cipssyscapacitygroup.is_presence():
            return True

        if self.cipstrapcntlgroup is not None and self.cipstrapcntlgroup._has_data():
            return True

        if self.cipstrapcntlgroup is not None and self.cipstrapcntlgroup.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ipsec._meta import _CISCO_IPSEC_MIB as meta
        return meta._meta_table['CISCOIPSECMIB']['meta_info']


