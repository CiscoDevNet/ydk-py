""" Cisco_IOS_XR_snmp_agent_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR snmp\-agent package configuration.

This module contains definitions
for the following management objects\:
  snmp\: The heirarchy point for all the SNMP configurations
  mib\: mib

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class GroupSnmpVersionEnum(Enum):
    """
    GroupSnmpVersionEnum

    Group snmp version

    .. data:: v1 = 0

    	SNMP version 1

    .. data:: v2c = 1

    	SNMP version 2

    .. data:: v3 = 2

    	SNMP version 3

    """

    v1 = 0

    v2c = 1

    v3 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['GroupSnmpVersionEnum']


class SnmpAccessLevelEnum(Enum):
    """
    SnmpAccessLevelEnum

    Snmp access level

    .. data:: read_only = 0

    	Read Only Access for a community string

    .. data:: read_write = 1

    	Read Write Access for a community string

    """

    read_only = 0

    read_write = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpAccessLevelEnum']


class SnmpBulkstatFileFormatEnum(Enum):
    """
    SnmpBulkstatFileFormatEnum

    Snmp bulkstat file format

    .. data:: schema_ascii = 1

    	Tranfer file in schema Ascii format

    .. data:: bulk_ascii = 2

    	Tranfer file in Bulk Ascii format

    .. data:: bulk_binary = 3

    	Tranfer file in Bulk binary format

    """

    schema_ascii = 1

    bulk_ascii = 2

    bulk_binary = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpBulkstatFileFormatEnum']


class SnmpBulkstatSchemaEnum(Enum):
    """
    SnmpBulkstatSchemaEnum

    Snmp bulkstat schema

    .. data:: exact_interface = 1

    	Exact Interface

    .. data:: exact_oid = 2

    	Exact OID

    .. data:: wild_interface = 3

    	Wild Interface

    .. data:: wild_oid = 4

    	Wild OID

    .. data:: range_oid = 5

    	Range of OID

    .. data:: repeat_oid = 6

    	Repeated the instance

    """

    exact_interface = 1

    exact_oid = 2

    wild_interface = 3

    wild_oid = 4

    range_oid = 5

    repeat_oid = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpBulkstatSchemaEnum']


class SnmpContextEnum(Enum):
    """
    SnmpContextEnum

    Snmp context

    .. data:: vrf = 1

    	VRF feature

    .. data:: bridge = 4

    	BRIDGE feature

    .. data:: ospf = 5

    	OSPF feature

    .. data:: ospfv3 = 6

    	OSPFv3 feature

    """

    vrf = 1

    bridge = 4

    ospf = 5

    ospfv3 = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpContextEnum']


class SnmpDscpValueEnum(Enum):
    """
    SnmpDscpValueEnum

    Snmp dscp value

    .. data:: default = 0

    	Applicable to DSCP: bits 000000

    .. data:: af11 = 10

    	Applicable to DSCP: bits 001010

    .. data:: af12 = 12

    	Applicable to DSCP: bits 001100

    .. data:: af13 = 14

    	Applicable to DSCP: bits 001110

    .. data:: af21 = 18

    	Applicable to DSCP: bits 010010

    .. data:: af22 = 20

    	Applicable to DSCP: bits 010100

    .. data:: af23 = 22

    	Applicable to DSCP: bits 010110

    .. data:: af31 = 26

    	Applicable to DSCP: bits 011010

    .. data:: af32 = 28

    	Applicable to DSCP: bits 011100

    .. data:: af33 = 30

    	Applicable to DSCP: bits 011110

    .. data:: af41 = 34

    	Applicable to DSCP: bits 100010

    .. data:: af42 = 36

    	Applicable to DSCP: bits 100100

    .. data:: af43 = 38

    	Applicable to DSCP: bits 100110

    .. data:: ef = 46

    	Applicable to DSCP: bits 101110

    .. data:: cs1 = 8

    	Applicable to DSCP: bits 001000

    .. data:: cs2 = 16

    	Applicable to DSCP: bits 010000

    .. data:: cs3 = 24

    	Applicable to DSCP: bits 011000

    .. data:: cs4 = 32

    	Applicable to DSCP: bits 100000

    .. data:: cs5 = 40

    	Applicable to DSCP: bits 101000

    .. data:: cs6 = 48

    	Applicable to DSCP: bits 110000

    .. data:: cs7 = 56

    	Applicable to DSCP: bits 111000

    """

    default = 0

    af11 = 10

    af12 = 12

    af13 = 14

    af21 = 18

    af22 = 20

    af23 = 22

    af31 = 26

    af32 = 28

    af33 = 30

    af41 = 34

    af42 = 36

    af43 = 38

    ef = 46

    cs1 = 8

    cs2 = 16

    cs3 = 24

    cs4 = 32

    cs5 = 40

    cs6 = 48

    cs7 = 56


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpDscpValueEnum']


class SnmpHashAlgorithmEnum(Enum):
    """
    SnmpHashAlgorithmEnum

    Snmp hash algorithm

    .. data:: none = 0

    	No authentication required

    .. data:: md5 = 1

    	Standard Message Digest algorithm

    .. data:: sha = 2

    	SHA algorithm

    """

    none = 0

    md5 = 1

    sha = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpHashAlgorithmEnum']


class SnmpMibViewInclusionEnum(Enum):
    """
    SnmpMibViewInclusionEnum

    Snmp mib view inclusion

    .. data:: included = 1

    	MIB View to be included

    .. data:: excluded = 2

    	MIB View to be excluded

    """

    included = 1

    excluded = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpMibViewInclusionEnum']


class SnmpOwnerAccessEnum(Enum):
    """
    SnmpOwnerAccessEnum

    Snmp owner access

    .. data:: sdr_owner = 0

    	Secure Domain Router Owner permissions

    .. data:: system_owner = 1

    	System owner permissions

    """

    sdr_owner = 0

    system_owner = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpOwnerAccessEnum']


class SnmpPrecedenceValue1Enum(Enum):
    """
    SnmpPrecedenceValue1Enum

    Snmp precedence value1

    .. data:: routine = 0

    	Applicable to Precedence: value 0

    .. data:: priority = 1

    	Applicable to Precedence: value 1

    .. data:: immediate = 2

    	Applicable to Precedence: value 2

    .. data:: flash = 3

    	Applicable to Precedence: value 3

    .. data:: flash_override = 4

    	Applicable to Precedence: value 4

    .. data:: critical = 5

    	Applicable to Precedence: value 5

    .. data:: internet = 6

    	Applicable to Precedence: value 6

    .. data:: network = 7

    	Applicable to Precedence: value 7

    """

    routine = 0

    priority = 1

    immediate = 2

    flash = 3

    flash_override = 4

    critical = 5

    internet = 6

    network = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpPrecedenceValue1Enum']


class SnmpPrivAlgorithmEnum(Enum):
    """
    SnmpPrivAlgorithmEnum

    Snmp priv algorithm

    .. data:: none = 0

    	No Privacy

    .. data:: des = 1

    	Des algorithm

    .. data:: Y_3des = 2

    	3des algorithm

    .. data:: aes128 = 3

    	aes128 algorithm

    .. data:: aes192 = 4

    	aes192 algorithm

    .. data:: aes256 = 5

    	aes256 algorithm

    """

    none = 0

    des = 1

    Y_3des = 2

    aes128 = 3

    aes192 = 4

    aes256 = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpPrivAlgorithmEnum']


class SnmpSecurityModelEnum(Enum):
    """
    SnmpSecurityModelEnum

    Snmp security model

    .. data:: no_authentication = 0

    	No Authentication required

    .. data:: authentication = 1

    	Authentication password alone required for

    	access

    .. data:: privacy = 2

    	Authentication and privacy password required

    	for access

    """

    no_authentication = 0

    authentication = 1

    privacy = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpSecurityModelEnum']


class SnmpTosEnum(Enum):
    """
    SnmpTosEnum

    Snmp tos

    .. data:: precedence = 0

    	SNMP TOS type Precedence

    .. data:: dscp = 1

    	SNMP TOS type DSCP

    """

    precedence = 0

    dscp = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpTosEnum']


class SnmpaclEnum(Enum):
    """
    SnmpaclEnum

    Snmpacl

    .. data:: ipv4 = 1

    	Ipv4 Access-list

    .. data:: ipv6 = 2

    	Ipv6 Access-list

    """

    ipv4 = 1

    ipv6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpaclEnum']


class UserSnmpVersionEnum(Enum):
    """
    UserSnmpVersionEnum

    User snmp version

    .. data:: v1 = 1

    	SNMP version 1

    .. data:: v2c = 2

    	SNMP version 2

    .. data:: v3 = 3

    	SNMP version 3

    """

    v1 = 1

    v2c = 2

    v3 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['UserSnmpVersionEnum']



class Snmp(object):
    """
    The heirarchy point for all the SNMP
    configurations
    
    .. attribute:: administration
    
    	Container class for SNMP administration
    	**type**\:   :py:class:`Administration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Administration>`
    
    .. attribute:: agent
    
    	The heirarchy point for SNMP Agent configurations
    	**type**\:   :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Agent>`
    
    .. attribute:: bulk_stats
    
    	SNMP bulk stats configuration commands
    	**type**\:   :py:class:`BulkStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats>`
    
    .. attribute:: context_mappings
    
    	List of context names
    	**type**\:   :py:class:`ContextMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.ContextMappings>`
    
    .. attribute:: contexts
    
    	List of Context Names
    	**type**\:   :py:class:`Contexts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Contexts>`
    
    .. attribute:: correlator
    
    	Configure properties of the trap correlator
    	**type**\:   :py:class:`Correlator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator>`
    
    .. attribute:: default_community_maps
    
    	Container class to hold unencrpted community map
    	**type**\:   :py:class:`DefaultCommunityMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.DefaultCommunityMaps>`
    
    .. attribute:: encrypted_community_maps
    
    	Container class to hold clear/encrypted communitie maps
    	**type**\:   :py:class:`EncryptedCommunityMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.EncryptedCommunityMaps>`
    
    .. attribute:: groups
    
    	Define a User Security Model group
    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Groups>`
    
    .. attribute:: inform_pending
    
    	Max nmber of informs to hold in queue, (default 25)
    	**type**\:  int
    
    	**range:** 0..4294967295
    
    .. attribute:: inform_retries
    
    	Number of times to retry an Inform request (default 3)
    	**type**\:  int
    
    	**range:** 0..100
    
    .. attribute:: inform_timeout
    
    	Timeout value in seconds for Inform request (default 15 sec)
    	**type**\:  int
    
    	**range:** 1..42949671
    
    	**units**\: second
    
    .. attribute:: ipv4
    
    	SNMP TOS bit for outgoing packets
    	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Ipv4>`
    
    .. attribute:: ipv6
    
    	SNMP TOS bit for outgoing packets
    	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Ipv6>`
    
    .. attribute:: logging
    
    	SNMP logging
    	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Logging>`
    
    .. attribute:: notification
    
    	Enable SNMP notifications
    	**type**\:   :py:class:`Notification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification>`
    
    .. attribute:: oid_poll_stats
    
    	Enable Poll OID statistics
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: overload_control
    
    	Set overload control params for handling incoming messages
    	**type**\:   :py:class:`OverloadControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.OverloadControl>`
    
    	**presence node**\: True
    
    .. attribute:: packet_size
    
    	Largest SNMP packet size
    	**type**\:  int
    
    	**range:** 484..65500
    
    .. attribute:: system
    
    	container to hold system information
    	**type**\:   :py:class:`System <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.System>`
    
    .. attribute:: target
    
    	SNMP target configurations
    	**type**\:   :py:class:`Target <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target>`
    
    .. attribute:: throttle_time
    
    	Throttle time for incoming queue (default 0 msec)
    	**type**\:  int
    
    	**range:** 50..1000
    
    .. attribute:: timeouts
    
    	SNMP timeouts
    	**type**\:   :py:class:`Timeouts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Timeouts>`
    
    .. attribute:: trap
    
    	Class to hold trap configurations
    	**type**\:   :py:class:`Trap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Trap>`
    
    .. attribute:: trap_hosts
    
    	Specify hosts to receive SNMP notifications
    	**type**\:   :py:class:`TrapHosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts>`
    
    .. attribute:: trap_port
    
    	Change the source port of all traps
    	**type**\:  int
    
    	**range:** 1024..65535
    
    .. attribute:: trap_source
    
    	Assign an interface for the source address of all traps
    	**type**\:  str
    
    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
    
    .. attribute:: trap_source_ipv4
    
    	Assign an interface for the source address of all traps
    	**type**\:  str
    
    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
    
    .. attribute:: trap_source_ipv6
    
    	Assign an interface for the source IPV6 address of all traps
    	**type**\:  str
    
    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
    
    .. attribute:: users
    
    	Define a user who can access the SNMP engine
    	**type**\:   :py:class:`Users <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Users>`
    
    .. attribute:: views
    
    	Class to configure a SNMPv2 MIB view
    	**type**\:   :py:class:`Views <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Views>`
    
    .. attribute:: vrf_authentication_trap_disable
    
    	Disable authentication traps for packets on a vrf
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: vrfs
    
    	SNMP VRF configuration commands
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs>`
    
    

    """

    _prefix = 'snmp-agent-cfg'
    _revision = '2015-10-27'

    def __init__(self):
        self.administration = Snmp.Administration()
        self.administration.parent = self
        self.agent = Snmp.Agent()
        self.agent.parent = self
        self.bulk_stats = Snmp.BulkStats()
        self.bulk_stats.parent = self
        self.context_mappings = Snmp.ContextMappings()
        self.context_mappings.parent = self
        self.contexts = Snmp.Contexts()
        self.contexts.parent = self
        self.correlator = Snmp.Correlator()
        self.correlator.parent = self
        self.default_community_maps = Snmp.DefaultCommunityMaps()
        self.default_community_maps.parent = self
        self.encrypted_community_maps = Snmp.EncryptedCommunityMaps()
        self.encrypted_community_maps.parent = self
        self.groups = Snmp.Groups()
        self.groups.parent = self
        self.inform_pending = None
        self.inform_retries = None
        self.inform_timeout = None
        self.ipv4 = Snmp.Ipv4()
        self.ipv4.parent = self
        self.ipv6 = Snmp.Ipv6()
        self.ipv6.parent = self
        self.logging = Snmp.Logging()
        self.logging.parent = self
        self.notification = Snmp.Notification()
        self.notification.parent = self
        self.oid_poll_stats = None
        self.overload_control = None
        self.packet_size = None
        self.system = Snmp.System()
        self.system.parent = self
        self.target = Snmp.Target()
        self.target.parent = self
        self.throttle_time = None
        self.timeouts = Snmp.Timeouts()
        self.timeouts.parent = self
        self.trap = Snmp.Trap()
        self.trap.parent = self
        self.trap_hosts = Snmp.TrapHosts()
        self.trap_hosts.parent = self
        self.trap_port = None
        self.trap_source = None
        self.trap_source_ipv4 = None
        self.trap_source_ipv6 = None
        self.users = Snmp.Users()
        self.users.parent = self
        self.views = Snmp.Views()
        self.views.parent = self
        self.vrf_authentication_trap_disable = None
        self.vrfs = Snmp.Vrfs()
        self.vrfs.parent = self


    class EncryptedCommunityMaps(object):
        """
        Container class to hold clear/encrypted
        communitie maps
        
        .. attribute:: encrypted_community_map
        
        	Clear/encrypted SNMP community map
        	**type**\: list of    :py:class:`EncryptedCommunityMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.EncryptedCommunityMaps.EncryptedCommunityMap>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.encrypted_community_map = YList()
            self.encrypted_community_map.parent = self
            self.encrypted_community_map.name = 'encrypted_community_map'


        class EncryptedCommunityMap(object):
            """
            Clear/encrypted SNMP community map
            
            .. attribute:: community_name  <key>
            
            	SNMP community map
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: context
            
            	SNMP Context Name 
            	**type**\:  str
            
            .. attribute:: security
            
            	SNMP Security Name 
            	**type**\:  str
            
            .. attribute:: target_list
            
            	target list name 
            	**type**\:  str
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.community_name = None
                self.context = None
                self.security = None
                self.target_list = None

            @property
            def _common_path(self):
                if self.community_name is None:
                    raise YPYModelError('Key property community_name is None')

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:encrypted-community-maps/Cisco-IOS-XR-snmp-agent-cfg:encrypted-community-map[Cisco-IOS-XR-snmp-agent-cfg:community-name = ' + str(self.community_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.community_name is not None:
                    return True

                if self.context is not None:
                    return True

                if self.security is not None:
                    return True

                if self.target_list is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.EncryptedCommunityMaps.EncryptedCommunityMap']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:encrypted-community-maps'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.encrypted_community_map is not None:
                for child_ref in self.encrypted_community_map:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.EncryptedCommunityMaps']['meta_info']


    class Views(object):
        """
        Class to configure a SNMPv2 MIB view
        
        .. attribute:: view
        
        	Name of the view
        	**type**\: list of    :py:class:`View <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Views.View>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.view = YList()
            self.view.parent = self
            self.view.name = 'view'


        class View(object):
            """
            Name of the view
            
            .. attribute:: view_name  <key>
            
            	Name of the view
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: family  <key>
            
            	MIB view family name
            	**type**\:  str
            
            .. attribute:: view_inclusion
            
            	MIB view to be included or excluded
            	**type**\:   :py:class:`SnmpMibViewInclusionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpMibViewInclusionEnum>`
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.view_name = None
                self.family = None
                self.view_inclusion = None

            @property
            def _common_path(self):
                if self.view_name is None:
                    raise YPYModelError('Key property view_name is None')
                if self.family is None:
                    raise YPYModelError('Key property family is None')

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:views/Cisco-IOS-XR-snmp-agent-cfg:view[Cisco-IOS-XR-snmp-agent-cfg:view-name = ' + str(self.view_name) + '][Cisco-IOS-XR-snmp-agent-cfg:family = ' + str(self.family) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.view_name is not None:
                    return True

                if self.family is not None:
                    return True

                if self.view_inclusion is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Views.View']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:views'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.view is not None:
                for child_ref in self.view:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Views']['meta_info']


    class Logging(object):
        """
        SNMP logging
        
        .. attribute:: threshold
        
        	SNMP logging threshold
        	**type**\:   :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Logging.Threshold>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.threshold = Snmp.Logging.Threshold()
            self.threshold.parent = self


        class Threshold(object):
            """
            SNMP logging threshold
            
            .. attribute:: oid_processing
            
            	SNMP logging threshold for OID processing
            	**type**\:  int
            
            	**range:** 0..20000
            
            	**default value**\: 500
            
            .. attribute:: pdu_processing
            
            	SNMP logging threshold for PDU processing
            	**type**\:  int
            
            	**range:** 0..20000
            
            	**default value**\: 20000
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.oid_processing = None
                self.pdu_processing = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:logging/Cisco-IOS-XR-snmp-agent-cfg:threshold'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.oid_processing is not None:
                    return True

                if self.pdu_processing is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Logging.Threshold']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:logging'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.threshold is not None and self.threshold._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Logging']['meta_info']


    class Administration(object):
        """
        Container class for SNMP administration
        
        .. attribute:: default_communities
        
        	Container class to hold unencrpted communities
        	**type**\:   :py:class:`DefaultCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Administration.DefaultCommunities>`
        
        .. attribute:: encrypted_communities
        
        	Container class to hold clear/encrypted communities
        	**type**\:   :py:class:`EncryptedCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Administration.EncryptedCommunities>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.default_communities = Snmp.Administration.DefaultCommunities()
            self.default_communities.parent = self
            self.encrypted_communities = Snmp.Administration.EncryptedCommunities()
            self.encrypted_communities.parent = self


        class DefaultCommunities(object):
            """
            Container class to hold unencrpted communities
            
            .. attribute:: default_community
            
            	Unencrpted SNMP community string and access priviledges
            	**type**\: list of    :py:class:`DefaultCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Administration.DefaultCommunities.DefaultCommunity>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.default_community = YList()
                self.default_community.parent = self
                self.default_community.name = 'default_community'


            class DefaultCommunity(object):
                """
                Unencrpted SNMP community string and access
                priviledges
                
                .. attribute:: community_name  <key>
                
                	SNMP community string
                	**type**\:  str
                
                	**length:** 1..128
                
                .. attribute:: owner
                
                	Logical Router or System owner access
                	**type**\:   :py:class:`SnmpOwnerAccessEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpOwnerAccessEnum>`
                
                .. attribute:: priviledge
                
                	Read/Write Access
                	**type**\:   :py:class:`SnmpAccessLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpAccessLevelEnum>`
                
                .. attribute:: v4_access_list
                
                	Ipv4 Access\-list name
                	**type**\:  str
                
                .. attribute:: v4acl_type
                
                	Access\-list type
                	**type**\:   :py:class:`SnmpaclEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpaclEnum>`
                
                .. attribute:: v6_access_list
                
                	Ipv6 Access\-list name
                	**type**\:  str
                
                .. attribute:: v6acl_type
                
                	Access\-list type
                	**type**\:   :py:class:`SnmpaclEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpaclEnum>`
                
                .. attribute:: view_name
                
                	MIB view to which the community has access
                	**type**\:  str
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2015-10-27'

                def __init__(self):
                    self.parent = None
                    self.community_name = None
                    self.owner = None
                    self.priviledge = None
                    self.v4_access_list = None
                    self.v4acl_type = None
                    self.v6_access_list = None
                    self.v6acl_type = None
                    self.view_name = None

                @property
                def _common_path(self):
                    if self.community_name is None:
                        raise YPYModelError('Key property community_name is None')

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:administration/Cisco-IOS-XR-snmp-agent-cfg:default-communities/Cisco-IOS-XR-snmp-agent-cfg:default-community[Cisco-IOS-XR-snmp-agent-cfg:community-name = ' + str(self.community_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.community_name is not None:
                        return True

                    if self.owner is not None:
                        return True

                    if self.priviledge is not None:
                        return True

                    if self.v4_access_list is not None:
                        return True

                    if self.v4acl_type is not None:
                        return True

                    if self.v6_access_list is not None:
                        return True

                    if self.v6acl_type is not None:
                        return True

                    if self.view_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Administration.DefaultCommunities.DefaultCommunity']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:administration/Cisco-IOS-XR-snmp-agent-cfg:default-communities'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.default_community is not None:
                    for child_ref in self.default_community:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Administration.DefaultCommunities']['meta_info']


        class EncryptedCommunities(object):
            """
            Container class to hold clear/encrypted
            communities
            
            .. attribute:: encrypted_community
            
            	Clear/encrypted SNMP community string and access priviledges
            	**type**\: list of    :py:class:`EncryptedCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Administration.EncryptedCommunities.EncryptedCommunity>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.encrypted_community = YList()
                self.encrypted_community.parent = self
                self.encrypted_community.name = 'encrypted_community'


            class EncryptedCommunity(object):
                """
                Clear/encrypted SNMP community string and
                access priviledges
                
                .. attribute:: community_name  <key>
                
                	SNMP community string
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: owner
                
                	Logical Router or System owner access
                	**type**\:   :py:class:`SnmpOwnerAccessEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpOwnerAccessEnum>`
                
                .. attribute:: priviledge
                
                	Read/Write Access
                	**type**\:   :py:class:`SnmpAccessLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpAccessLevelEnum>`
                
                .. attribute:: v4_access_list
                
                	Ipv4 Access\-list name
                	**type**\:  str
                
                .. attribute:: v4acl_type
                
                	Access\-list type
                	**type**\:   :py:class:`SnmpaclEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpaclEnum>`
                
                .. attribute:: v6_access_list
                
                	Ipv6 Access\-list name
                	**type**\:  str
                
                .. attribute:: v6acl_type
                
                	Access\-list type
                	**type**\:   :py:class:`SnmpaclEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpaclEnum>`
                
                .. attribute:: view_name
                
                	MIB view to which the community has access
                	**type**\:  str
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2015-10-27'

                def __init__(self):
                    self.parent = None
                    self.community_name = None
                    self.owner = None
                    self.priviledge = None
                    self.v4_access_list = None
                    self.v4acl_type = None
                    self.v6_access_list = None
                    self.v6acl_type = None
                    self.view_name = None

                @property
                def _common_path(self):
                    if self.community_name is None:
                        raise YPYModelError('Key property community_name is None')

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:administration/Cisco-IOS-XR-snmp-agent-cfg:encrypted-communities/Cisco-IOS-XR-snmp-agent-cfg:encrypted-community[Cisco-IOS-XR-snmp-agent-cfg:community-name = ' + str(self.community_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.community_name is not None:
                        return True

                    if self.owner is not None:
                        return True

                    if self.priviledge is not None:
                        return True

                    if self.v4_access_list is not None:
                        return True

                    if self.v4acl_type is not None:
                        return True

                    if self.v6_access_list is not None:
                        return True

                    if self.v6acl_type is not None:
                        return True

                    if self.view_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Administration.EncryptedCommunities.EncryptedCommunity']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:administration/Cisco-IOS-XR-snmp-agent-cfg:encrypted-communities'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.encrypted_community is not None:
                    for child_ref in self.encrypted_community:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Administration.EncryptedCommunities']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:administration'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.default_communities is not None and self.default_communities._has_data():
                return True

            if self.encrypted_communities is not None and self.encrypted_communities._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Administration']['meta_info']


    class Agent(object):
        """
        The heirarchy point for SNMP Agent
        configurations
        
        .. attribute:: engine_id
        
        	SNMPv3 engineID
        	**type**\:   :py:class:`EngineId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Agent.EngineId>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.engine_id = Snmp.Agent.EngineId()
            self.engine_id.parent = self


        class EngineId(object):
            """
            SNMPv3 engineID
            
            .. attribute:: local
            
            	engineID of the local agent
            	**type**\:  str
            
            .. attribute:: remotes
            
            	SNMPv3 remote SNMP Entity
            	**type**\:   :py:class:`Remotes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Agent.EngineId.Remotes>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.local = None
                self.remotes = Snmp.Agent.EngineId.Remotes()
                self.remotes.parent = self


            class Remotes(object):
                """
                SNMPv3 remote SNMP Entity
                
                .. attribute:: remote
                
                	engineID of the remote agent
                	**type**\: list of    :py:class:`Remote <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Agent.EngineId.Remotes.Remote>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2015-10-27'

                def __init__(self):
                    self.parent = None
                    self.remote = YList()
                    self.remote.parent = self
                    self.remote.name = 'remote'


                class Remote(object):
                    """
                    engineID of the remote agent
                    
                    .. attribute:: remote_address  <key>
                    
                    	IP address of remote SNMP entity
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: port
                    
                    	UDP port number
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: remote_engine_id
                    
                    	engine ID octet string
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2015-10-27'

                    def __init__(self):
                        self.parent = None
                        self.remote_address = None
                        self.port = None
                        self.remote_engine_id = None

                    @property
                    def _common_path(self):
                        if self.remote_address is None:
                            raise YPYModelError('Key property remote_address is None')

                        return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:agent/Cisco-IOS-XR-snmp-agent-cfg:engine-id/Cisco-IOS-XR-snmp-agent-cfg:remotes/Cisco-IOS-XR-snmp-agent-cfg:remote[Cisco-IOS-XR-snmp-agent-cfg:remote-address = ' + str(self.remote_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.remote_address is not None:
                            return True

                        if self.port is not None:
                            return True

                        if self.remote_engine_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Agent.EngineId.Remotes.Remote']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:agent/Cisco-IOS-XR-snmp-agent-cfg:engine-id/Cisco-IOS-XR-snmp-agent-cfg:remotes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.remote is not None:
                        for child_ref in self.remote:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Agent.EngineId.Remotes']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:agent/Cisco-IOS-XR-snmp-agent-cfg:engine-id'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.local is not None:
                    return True

                if self.remotes is not None and self.remotes._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Agent.EngineId']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:agent'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.engine_id is not None and self.engine_id._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Agent']['meta_info']


    class Trap(object):
        """
        Class to hold trap configurations
        
        .. attribute:: queue_length
        
        	Message queue length for each TRAP host
        	**type**\:  int
        
        	**range:** 1..5000
        
        .. attribute:: throttle_time
        
        	Set throttle time for handling traps
        	**type**\:  int
        
        	**range:** 10..500
        
        	**units**\: millisecond
        
        .. attribute:: timeout
        
        	Timeout for TRAP message retransmissions
        	**type**\:  int
        
        	**range:** 1..1000
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.queue_length = None
            self.throttle_time = None
            self.timeout = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:trap'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.queue_length is not None:
                return True

            if self.throttle_time is not None:
                return True

            if self.timeout is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Trap']['meta_info']


    class Ipv6(object):
        """
        SNMP TOS bit for outgoing packets
        
        .. attribute:: tos
        
        	Type of TOS
        	**type**\:   :py:class:`Tos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Ipv6.Tos>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.tos = Snmp.Ipv6.Tos()
            self.tos.parent = self


        class Tos(object):
            """
            Type of TOS
            
            .. attribute:: dscp
            
            	SNMP DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`SnmpDscpValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpDscpValueEnum>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: precedence
            
            	SNMP Precedence value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`SnmpPrecedenceValue1Enum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpPrecedenceValue1Enum>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: type
            
            	SNMP TOS type DSCP or Precedence
            	**type**\:   :py:class:`SnmpTosEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpTosEnum>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.dscp = None
                self.precedence = None
                self.type = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:ipv6/Cisco-IOS-XR-snmp-agent-cfg:tos'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.dscp is not None:
                    return True

                if self.precedence is not None:
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Ipv6.Tos']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:ipv6'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.tos is not None and self.tos._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Ipv6']['meta_info']


    class Ipv4(object):
        """
        SNMP TOS bit for outgoing packets
        
        .. attribute:: tos
        
        	Type of TOS
        	**type**\:   :py:class:`Tos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Ipv4.Tos>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.tos = Snmp.Ipv4.Tos()
            self.tos.parent = self


        class Tos(object):
            """
            Type of TOS
            
            .. attribute:: dscp
            
            	SNMP DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`SnmpDscpValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpDscpValueEnum>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: precedence
            
            	SNMP Precedence value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`SnmpPrecedenceValue1Enum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpPrecedenceValue1Enum>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: type
            
            	SNMP TOS type DSCP or Precedence
            	**type**\:   :py:class:`SnmpTosEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpTosEnum>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.dscp = None
                self.precedence = None
                self.type = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:ipv4/Cisco-IOS-XR-snmp-agent-cfg:tos'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.dscp is not None:
                    return True

                if self.precedence is not None:
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Ipv4.Tos']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:ipv4'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.tos is not None and self.tos._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Ipv4']['meta_info']


    class System(object):
        """
        container to hold system information
        
        .. attribute:: chassis_id
        
        	String to uniquely identify this chassis
        	**type**\:  str
        
        	**length:** 1..255
        
        .. attribute:: contact
        
        	identification of the contact person for this managed node
        	**type**\:  str
        
        	**length:** 1..255
        
        .. attribute:: location
        
        	The physical location of this node
        	**type**\:  str
        
        	**length:** 1..255
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.chassis_id = None
            self.contact = None
            self.location = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:system'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.chassis_id is not None:
                return True

            if self.contact is not None:
                return True

            if self.location is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.System']['meta_info']


    class Target(object):
        """
        SNMP target configurations
        
        .. attribute:: targets
        
        	List of targets
        	**type**\:   :py:class:`Targets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.targets = Snmp.Target.Targets()
            self.targets.parent = self


        class Targets(object):
            """
            List of targets
            
            .. attribute:: target
            
            	Name of the target list
            	**type**\: list of    :py:class:`Target_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets.Target_>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.target = YList()
                self.target.parent = self
                self.target.name = 'target'


            class Target_(object):
                """
                Name of the target list
                
                .. attribute:: target_list_name  <key>
                
                	Name of the target list
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: target_addresses
                
                	SNMP Target address configurations
                	**type**\:   :py:class:`TargetAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets.Target_.TargetAddresses>`
                
                .. attribute:: vrf_names
                
                	List of VRF Name for a target list
                	**type**\:   :py:class:`VrfNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets.Target_.VrfNames>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2015-10-27'

                def __init__(self):
                    self.parent = None
                    self.target_list_name = None
                    self.target_addresses = Snmp.Target.Targets.Target_.TargetAddresses()
                    self.target_addresses.parent = self
                    self.vrf_names = Snmp.Target.Targets.Target_.VrfNames()
                    self.vrf_names.parent = self


                class VrfNames(object):
                    """
                    List of VRF Name for a target list
                    
                    .. attribute:: vrf_name
                    
                    	VRF name of the target
                    	**type**\: list of    :py:class:`VrfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets.Target_.VrfNames.VrfName>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2015-10-27'

                    def __init__(self):
                        self.parent = None
                        self.vrf_name = YList()
                        self.vrf_name.parent = self
                        self.vrf_name.name = 'vrf_name'


                    class VrfName(object):
                        """
                        VRF name of the target
                        
                        .. attribute:: name  <key>
                        
                        	VRF Name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2015-10-27'

                        def __init__(self):
                            self.parent = None
                            self.name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYModelError('Key property name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:vrf-name[Cisco-IOS-XR-snmp-agent-cfg:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Target.Targets.Target_.VrfNames.VrfName']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:vrf-names'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.vrf_name is not None:
                            for child_ref in self.vrf_name:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Target.Targets.Target_.VrfNames']['meta_info']


                class TargetAddresses(object):
                    """
                    SNMP Target address configurations
                    
                    .. attribute:: target_address
                    
                    	IP Address to be configured for the Target
                    	**type**\: list of    :py:class:`TargetAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets.Target_.TargetAddresses.TargetAddress>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2015-10-27'

                    def __init__(self):
                        self.parent = None
                        self.target_address = YList()
                        self.target_address.parent = self
                        self.target_address.name = 'target_address'


                    class TargetAddress(object):
                        """
                        IP Address to be configured for the Target
                        
                        .. attribute:: ip_address  <key>
                        
                        	IPv4/Ipv6 address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2015-10-27'

                        def __init__(self):
                            self.parent = None
                            self.ip_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ip_address is None:
                                raise YPYModelError('Key property ip_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:target-address[Cisco-IOS-XR-snmp-agent-cfg:ip-address = ' + str(self.ip_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.ip_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Target.Targets.Target_.TargetAddresses.TargetAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:target-addresses'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.target_address is not None:
                            for child_ref in self.target_address:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Target.Targets.Target_.TargetAddresses']['meta_info']

                @property
                def _common_path(self):
                    if self.target_list_name is None:
                        raise YPYModelError('Key property target_list_name is None')

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:target/Cisco-IOS-XR-snmp-agent-cfg:targets/Cisco-IOS-XR-snmp-agent-cfg:target[Cisco-IOS-XR-snmp-agent-cfg:target-list-name = ' + str(self.target_list_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.target_list_name is not None:
                        return True

                    if self.target_addresses is not None and self.target_addresses._has_data():
                        return True

                    if self.vrf_names is not None and self.vrf_names._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Target.Targets.Target_']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:target/Cisco-IOS-XR-snmp-agent-cfg:targets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.target is not None:
                    for child_ref in self.target:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Target.Targets']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:target'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.targets is not None and self.targets._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Target']['meta_info']


    class Notification(object):
        """
        Enable SNMP notifications
        
        .. attribute:: bfd
        
        	CISCO\-IETF\-BFD\-MIB notification configuration
        	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Bfd>`
        
        .. attribute:: bgp
        
        	BGP4\-MIB and CISCO\-BGP4\-MIB notification configuration
        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Bgp>`
        
        .. attribute:: cfm
        
        	802.1ag Connectivity Fault Management MIB notification configuration
        	**type**\:   :py:class:`Cfm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Cfm>`
        
        .. attribute:: config_copy
        
        	CISCO\-CONFIG\-COPY\-MIB notification configuration
        	**type**\:   :py:class:`ConfigCopy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.ConfigCopy>`
        
        .. attribute:: config_man
        
        	CISCO\-CONFIG\-MAN\-MIB notification configurations
        	**type**\:   :py:class:`ConfigMan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.ConfigMan>`
        
        .. attribute:: entity
        
        	Enable ENTITY\-MIB notifications
        	**type**\:   :py:class:`Entity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Entity>`
        
        .. attribute:: entity_redundancy
        
        	CISCO\-ENTITY\-REDUNDANCY\-MIB notification configuration
        	**type**\:   :py:class:`EntityRedundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.EntityRedundancy>`
        
        .. attribute:: entity_state
        
        	ENTITY\-STATE\-MIB notification configuration
        	**type**\:   :py:class:`EntityState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.EntityState>`
        
        .. attribute:: flash
        
        	CISCO\-FLASH\-MIB notification configuration
        	**type**\:   :py:class:`Flash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Flash>`
        
        .. attribute:: fru_control
        
        	CISCO\-ENTITY\-FRU\-CONTROL\-MIB notification configuration
        	**type**\:   :py:class:`FruControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.FruControl>`
        
        .. attribute:: hsrp
        
        	CISCO\-HSRP\-MIB notification configuration
        	**type**\:   :py:class:`Hsrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Hsrp>`
        
        .. attribute:: isis
        
        	Enable ISIS\-MIB notifications
        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Isis>`
        
        .. attribute:: l2vpn
        
        	CISCO\-IETF\-PW\-MIB notification configuration
        	**type**\:   :py:class:`L2Vpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.L2Vpn>`
        
        .. attribute:: mpls_frr
        
        	CISCO\-IETF\-FRR\-MIB notification configuration
        	**type**\:   :py:class:`MplsFrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.MplsFrr>`
        
        .. attribute:: mpls_l3vpn
        
        	MPLS\-L3VPN\-STD\-MIB notification configuration
        	**type**\:   :py:class:`MplsL3Vpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.MplsL3Vpn>`
        
        .. attribute:: mpls_ldp
        
        	MPLS\-LDP\-STD\-MIB notification configuration
        	**type**\:   :py:class:`MplsLdp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.MplsLdp>`
        
        .. attribute:: mpls_te
        
        	MPLS\-TE\-STD\-MIB notification configuration
        	**type**\:   :py:class:`MplsTe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.MplsTe>`
        
        .. attribute:: mpls_te_p2mp
        
        	CISCO\-MPLS\-TE\-P2MP\-STD\-MIB notification configuration
        	**type**\:   :py:class:`MplsTeP2Mp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.MplsTeP2Mp>`
        
        .. attribute:: ntp
        
        	CISCO\-NTP\-MIB notification configuration
        	**type**\:   :py:class:`Ntp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ntp>`
        
        .. attribute:: oam
        
        	802.3 OAM MIB notification configuration
        	**type**\:   :py:class:`Oam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Oam>`
        
        .. attribute:: ospf
        
        	OSPF\-MIB notification configuration
        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ospf>`
        
        .. attribute:: ospfv3
        
        	OSPFv3\-MIB notification configuration
        	**type**\:   :py:class:`Ospfv3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ospfv3>`
        
        .. attribute:: otn
        
        	CISCO\-OTN\-IF\-MIB notification configuration
        	**type**\:   :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Otn>`
        
        .. attribute:: rf
        
        	CISCO\-RF\-MIB notification configuration
        	**type**\:   :py:class:`Rf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Rf>`
        
        .. attribute:: rsvp
        
        	Enable RSVP\-MIB notifications
        	**type**\:   :py:class:`Rsvp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Rsvp>`
        
        .. attribute:: selective_vrf_download
        
        	CISCO\-SELECTIVE\-VRF\-DOWNLOAD\-MIB notification configuration
        	**type**\:   :py:class:`SelectiveVrfDownload <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.SelectiveVrfDownload>`
        
        .. attribute:: sensor
        
        	CISCO\-ENTITY\-SENSOR\-MIB notification configuration
        	**type**\:   :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Sensor>`
        
        .. attribute:: snmp
        
        	SNMP notification configuration
        	**type**\:   :py:class:`Snmp_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Snmp_>`
        
        .. attribute:: syslog
        
        	CISCO\-SYSLOG\-MIB notification configuration
        	**type**\:   :py:class:`Syslog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Syslog>`
        
        .. attribute:: system
        
        	CISCO\-SYSTEM\-MIB notification configuration
        	**type**\:   :py:class:`System <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.System>`
        
        .. attribute:: vpls
        
        	CISCO\-IETF\-VPLS\-GENERIC\-MIB notification configuration
        	**type**\:   :py:class:`Vpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Vpls>`
        
        .. attribute:: vrrp
        
        	VRRP\-MIB notification configuration
        	**type**\:   :py:class:`Vrrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Vrrp>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.bfd = Snmp.Notification.Bfd()
            self.bfd.parent = self
            self.bgp = Snmp.Notification.Bgp()
            self.bgp.parent = self
            self.cfm = Snmp.Notification.Cfm()
            self.cfm.parent = self
            self.config_copy = Snmp.Notification.ConfigCopy()
            self.config_copy.parent = self
            self.config_man = Snmp.Notification.ConfigMan()
            self.config_man.parent = self
            self.entity = Snmp.Notification.Entity()
            self.entity.parent = self
            self.entity_redundancy = Snmp.Notification.EntityRedundancy()
            self.entity_redundancy.parent = self
            self.entity_state = Snmp.Notification.EntityState()
            self.entity_state.parent = self
            self.flash = Snmp.Notification.Flash()
            self.flash.parent = self
            self.fru_control = Snmp.Notification.FruControl()
            self.fru_control.parent = self
            self.hsrp = Snmp.Notification.Hsrp()
            self.hsrp.parent = self
            self.isis = Snmp.Notification.Isis()
            self.isis.parent = self
            self.l2vpn = Snmp.Notification.L2Vpn()
            self.l2vpn.parent = self
            self.mpls_frr = Snmp.Notification.MplsFrr()
            self.mpls_frr.parent = self
            self.mpls_l3vpn = Snmp.Notification.MplsL3Vpn()
            self.mpls_l3vpn.parent = self
            self.mpls_ldp = Snmp.Notification.MplsLdp()
            self.mpls_ldp.parent = self
            self.mpls_te = Snmp.Notification.MplsTe()
            self.mpls_te.parent = self
            self.mpls_te_p2mp = Snmp.Notification.MplsTeP2Mp()
            self.mpls_te_p2mp.parent = self
            self.ntp = Snmp.Notification.Ntp()
            self.ntp.parent = self
            self.oam = Snmp.Notification.Oam()
            self.oam.parent = self
            self.ospf = Snmp.Notification.Ospf()
            self.ospf.parent = self
            self.ospfv3 = Snmp.Notification.Ospfv3()
            self.ospfv3.parent = self
            self.otn = Snmp.Notification.Otn()
            self.otn.parent = self
            self.rf = Snmp.Notification.Rf()
            self.rf.parent = self
            self.rsvp = Snmp.Notification.Rsvp()
            self.rsvp.parent = self
            self.selective_vrf_download = Snmp.Notification.SelectiveVrfDownload()
            self.selective_vrf_download.parent = self
            self.sensor = Snmp.Notification.Sensor()
            self.sensor.parent = self
            self.snmp = Snmp.Notification.Snmp_()
            self.snmp.parent = self
            self.syslog = Snmp.Notification.Syslog()
            self.syslog.parent = self
            self.system = Snmp.Notification.System()
            self.system.parent = self
            self.vpls = Snmp.Notification.Vpls()
            self.vpls.parent = self
            self.vrrp = Snmp.Notification.Vrrp()
            self.vrrp.parent = self


        class Snmp_(object):
            """
            SNMP notification configuration
            
            .. attribute:: authentication
            
            	Enable authentication notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: cold_start
            
            	Enable cold start notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable
            
            	Enable SNMP notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: link_down
            
            	Enable link down notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: link_up
            
            	Enable link up notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: warm_start
            
            	Enable warm start notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.authentication = None
                self.cold_start = None
                self.enable = None
                self.link_down = None
                self.link_up = None
                self.warm_start = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-snmp-agent-cfg:snmp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.authentication is not None:
                    return True

                if self.cold_start is not None:
                    return True

                if self.enable is not None:
                    return True

                if self.link_down is not None:
                    return True

                if self.link_up is not None:
                    return True

                if self.warm_start is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Snmp_']['meta_info']


        class Vpls(object):
            """
            CISCO\-IETF\-VPLS\-GENERIC\-MIB notification
            configuration
            
            .. attribute:: enable
            
            	Enable CISCO\-IETF\-VPLS\-GENERIC\-MIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: full_clear
            
            	Enable cvplsFwdFullAlarmCleared notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: full_raise
            
            	Enable cvplsFwdFullAlarmRaised notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: status
            
            	Enable cvplsStatusChanged notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.full_clear = None
                self.full_raise = None
                self.status = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-l2vpn-cfg:vpls'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.full_clear is not None:
                    return True

                if self.full_raise is not None:
                    return True

                if self.status is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Vpls']['meta_info']


        class L2Vpn(object):
            """
            CISCO\-IETF\-PW\-MIB notification configuration
            
            .. attribute:: cisco
            
            	Enable Cisco format including extra varbinds
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable
            
            	Enable CISCO\-IETF\-PW\-MIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: vc_down
            
            	Enable cpwVcDown notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: vc_up
            
            	Enable cpwVcUp notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.cisco = None
                self.enable = None
                self.vc_down = None
                self.vc_up = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-l2vpn-cfg:l2vpn'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.cisco is not None:
                    return True

                if self.enable is not None:
                    return True

                if self.vc_down is not None:
                    return True

                if self.vc_up is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.L2Vpn']['meta_info']


        class Isis(object):
            """
            Enable ISIS\-MIB notifications
            
            .. attribute:: adjacency_change
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibAdjacencyChangeBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAdjacencyChangeBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: all
            
            	Enable all isisMIB notifications
            	**type**\:   :py:class:`IsisMibAllBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAllBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: area_mismatch
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibAreaMismatchBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAreaMismatchBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: attempt_to_exceed_max_sequence
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibAttemptToExceedMaxSequenceBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAttemptToExceedMaxSequenceBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: authentication_failure
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibAuthenticationFailureBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAuthenticationFailureBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: authentication_type_failure
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibAuthenticationTypeFailureBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAuthenticationTypeFailureBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: corrupted_lsp_detected
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibCorruptedLspDetectedBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibCorruptedLspDetectedBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: database_overflow
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibDatabaseOverFlowBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibDatabaseOverFlowBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: id_length_mismatch
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibIdLengthMismatchBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibIdLengthMismatchBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: lsp_error_detected
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibLspErrorDetectedBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibLspErrorDetectedBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: lsp_too_large_to_propagate
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibLspTooLargeToPropagateBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibLspTooLargeToPropagateBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: manual_address_drops
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibManualAddressDropsBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibManualAddressDropsBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: max_area_address_mismatch
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibMaxAreaAddressMismatchBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibMaxAreaAddressMismatchBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: originated_lsp_buffer_size_mismatch
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibOriginatedLspBufferSizeMismatchBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibOriginatedLspBufferSizeMismatchBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: own_lsp_purge
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibOwnLspPurgeBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibOwnLspPurgeBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: protocols_supported_mismatch
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibProtocolsSupportedMismatchBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibProtocolsSupportedMismatchBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: rejected_adjacency
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibRejectedAdjacencyBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibRejectedAdjacencyBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: sequence_number_skip
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibSequenceNumberSkipBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibSequenceNumberSkipBooleanEnum>`
            
            	**default value**\: false
            
            .. attribute:: version_skew
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibVersionSkewBooleanEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibVersionSkewBooleanEnum>`
            
            	**default value**\: false
            
            

            """

            _prefix = 'clns-isis-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.adjacency_change = None
                self.all = None
                self.area_mismatch = None
                self.attempt_to_exceed_max_sequence = None
                self.authentication_failure = None
                self.authentication_type_failure = None
                self.corrupted_lsp_detected = None
                self.database_overflow = None
                self.id_length_mismatch = None
                self.lsp_error_detected = None
                self.lsp_too_large_to_propagate = None
                self.manual_address_drops = None
                self.max_area_address_mismatch = None
                self.originated_lsp_buffer_size_mismatch = None
                self.own_lsp_purge = None
                self.protocols_supported_mismatch = None
                self.rejected_adjacency = None
                self.sequence_number_skip = None
                self.version_skew = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-clns-isis-cfg:isis'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.adjacency_change is not None:
                    return True

                if self.all is not None:
                    return True

                if self.area_mismatch is not None:
                    return True

                if self.attempt_to_exceed_max_sequence is not None:
                    return True

                if self.authentication_failure is not None:
                    return True

                if self.authentication_type_failure is not None:
                    return True

                if self.corrupted_lsp_detected is not None:
                    return True

                if self.database_overflow is not None:
                    return True

                if self.id_length_mismatch is not None:
                    return True

                if self.lsp_error_detected is not None:
                    return True

                if self.lsp_too_large_to_propagate is not None:
                    return True

                if self.manual_address_drops is not None:
                    return True

                if self.max_area_address_mismatch is not None:
                    return True

                if self.originated_lsp_buffer_size_mismatch is not None:
                    return True

                if self.own_lsp_purge is not None:
                    return True

                if self.protocols_supported_mismatch is not None:
                    return True

                if self.rejected_adjacency is not None:
                    return True

                if self.sequence_number_skip is not None:
                    return True

                if self.version_skew is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Isis']['meta_info']


        class ConfigMan(object):
            """
            CISCO\-CONFIG\-MAN\-MIB notification configurations
            
            .. attribute:: enable
            
            	Enable ciscoConfigManMIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'config-mibs-cfg'
            _revision = '2015-09-29'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-config-mibs-cfg:config-man'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.ConfigMan']['meta_info']


        class Cfm(object):
            """
            802.1ag Connectivity Fault Management MIB
            notification configuration
            
            .. attribute:: enable
            
            	Enable 802.1ag Connectivity Fault Management MIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ethernet-cfm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ethernet-cfm-cfg:cfm'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Cfm']['meta_info']


        class Oam(object):
            """
            802.3 OAM MIB notification configuration
            
            .. attribute:: enable
            
            	Enable 802.3 OAM MIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ethernet-link-oam-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ethernet-link-oam-cfg:oam'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Oam']['meta_info']


        class Flash(object):
            """
            CISCO\-FLASH\-MIB notification configuration
            
            .. attribute:: insertion
            
            	Enable ciscoFlashDeviceInsertedNotif notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: removal
            
            	Enable ciscoFlashDeviceRemovedNotif notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'flashmib-cfg'
            _revision = '2015-12-15'

            def __init__(self):
                self.parent = None
                self.insertion = None
                self.removal = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-flashmib-cfg:flash'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.insertion is not None:
                    return True

                if self.removal is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Flash']['meta_info']


        class EntityRedundancy(object):
            """
            CISCO\-ENTITY\-REDUNDANCY\-MIB notification
            configuration
            
            .. attribute:: enable
            
            	Enable CISCO\-ENTITY\-REDUNDANCY\-MIB notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: status
            
            	Enable status change notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: switchover
            
            	Enable switchover notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-ceredundancymib-cfg'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.status = None
                self.switchover = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-infra-ceredundancymib-cfg:entity-redundancy'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.status is not None:
                    return True

                if self.switchover is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.EntityRedundancy']['meta_info']


        class ConfigCopy(object):
            """
            CISCO\-CONFIG\-COPY\-MIB notification configuration
            
            .. attribute:: completion
            
            	Enable ccCopyCompletion notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-confcopymib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.completion = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-infra-confcopymib-cfg:config-copy'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.completion is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.ConfigCopy']['meta_info']


        class SelectiveVrfDownload(object):
            """
            CISCO\-SELECTIVE\-VRF\-DOWNLOAD\-MIB notification
            configuration
            
            .. attribute:: role_change
            
            	Enable csvdEntityRoleChangeNotification notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2016-12-19'

            def __init__(self):
                self.parent = None
                self.role_change = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-infra-rsi-cfg:selective-vrf-download'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.role_change is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.SelectiveVrfDownload']['meta_info']


        class System(object):
            """
            CISCO\-SYSTEM\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable ciscoSystemMIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-systemmib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-infra-systemmib-cfg:system'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.System']['meta_info']


        class Bfd(object):
            """
            CISCO\-IETF\-BFD\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable CISCO\-IETF\-BFD\-MIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ip-bfd-cfg:bfd'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Bfd']['meta_info']


        class Ntp(object):
            """
            CISCO\-NTP\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable ciscoNtpMIB notification configuration
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ip-ntp-cfg:ntp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Ntp']['meta_info']


        class Rsvp(object):
            """
            Enable RSVP\-MIB notifications
            
            .. attribute:: enable
            
            	Enable all RSVP notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: lost_flow
            
            	Enable lostFlow notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: new_flow
            
            	Enable newFlow notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.lost_flow = None
                self.new_flow = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ip-rsvp-cfg:rsvp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.lost_flow is not None:
                    return True

                if self.new_flow is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Rsvp']['meta_info']


        class Bgp(object):
            """
            BGP4\-MIB and CISCO\-BGP4\-MIB notification
            configuration
            
            .. attribute:: bgp4mib
            
            	Enable BGP4\-MIB and CISCO\-BGP4\-MIB IPv4\-only notifications\: bgpEstablishedNotification, bgpBackwardTransNotification, cbgpFsmStateChange, cbgpBackwardTransition, cbgpPrefixThresholdExceeded, cbgpPrefixThresholdClear
            	**type**\:   :py:class:`Bgp4Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Bgp.Bgp4Mib>`
            
            .. attribute:: cisco_bgp4mib
            
            	Enable CISCO\-BGP4\-MIB v2 notifications\: cbgpPeer2EstablishedNotification, cbgpPeer2BackwardTransNotification, cbgpPeer2FsmStateChange, cbgpPeer2BackwardTransition, cbgpPeer2PrefixThresholdExceeded, cbgpPeer2PrefixThresholdClear
            	**type**\:   :py:class:`CiscoBgp4Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Bgp.CiscoBgp4Mib>`
            
            

            """

            _prefix = 'ipv4-bgp-cfg'
            _revision = '2015-08-27'

            def __init__(self):
                self.parent = None
                self.bgp4mib = Snmp.Notification.Bgp.Bgp4Mib()
                self.bgp4mib.parent = self
                self.cisco_bgp4mib = Snmp.Notification.Bgp.CiscoBgp4Mib()
                self.cisco_bgp4mib.parent = self


            class Bgp4Mib(object):
                """
                Enable BGP4\-MIB and CISCO\-BGP4\-MIB IPv4\-only
                notifications\: bgpEstablishedNotification,
                bgpBackwardTransNotification,
                cbgpFsmStateChange, cbgpBackwardTransition,
                cbgpPrefixThresholdExceeded,
                cbgpPrefixThresholdClear.
                
                .. attribute:: enable
                
                	Enable BGP4\-MIB and CISCO\-BGP4\-MIB IPv4\-only notifications
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: up_down
                
                	Enable BGP4\-MIB and CISCO\-BGP4\-MIB IPv4\-only up/down notifications
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv4-bgp-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.enable = None
                    self.up_down = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ipv4-bgp-cfg:bgp/Cisco-IOS-XR-ipv4-bgp-cfg:bgp4mib'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.enable is not None:
                        return True

                    if self.up_down is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.Bgp.Bgp4Mib']['meta_info']


            class CiscoBgp4Mib(object):
                """
                Enable CISCO\-BGP4\-MIB v2 notifications\:
                cbgpPeer2EstablishedNotification,
                cbgpPeer2BackwardTransNotification,
                cbgpPeer2FsmStateChange,
                cbgpPeer2BackwardTransition,
                cbgpPeer2PrefixThresholdExceeded,
                cbgpPeer2PrefixThresholdClear.
                
                .. attribute:: enable
                
                	Enable CISCO\-BGP4\-MIB v2 notifications
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: up_down
                
                	Enable CISCO\-BGP4\-MIB v2 up/down notifications
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv4-bgp-cfg'
                _revision = '2015-08-27'

                def __init__(self):
                    self.parent = None
                    self.enable = None
                    self.up_down = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ipv4-bgp-cfg:bgp/Cisco-IOS-XR-ipv4-bgp-cfg:cisco-bgp4mib'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.enable is not None:
                        return True

                    if self.up_down is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.Bgp.CiscoBgp4Mib']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ipv4-bgp-cfg:bgp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.bgp4mib is not None and self.bgp4mib._has_data():
                    return True

                if self.cisco_bgp4mib is not None and self.cisco_bgp4mib._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Bgp']['meta_info']


        class Hsrp(object):
            """
            CISCO\-HSRP\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable CISCO\-HSRP\-MIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ipv4-hsrp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Hsrp']['meta_info']


        class Ospf(object):
            """
            OSPF\-MIB notification configuration
            
            .. attribute:: error
            
            	SNMP notifications for OSPF errors
            	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ospf.Error>`
            
            .. attribute:: lsa
            
            	SNMP notifications related to LSAs
            	**type**\:   :py:class:`Lsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ospf.Lsa>`
            
            .. attribute:: retransmit
            
            	SNMP notifications for packet retransmissions
            	**type**\:   :py:class:`Retransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ospf.Retransmit>`
            
            .. attribute:: state_change
            
            	SNMP notifications for OSPF state change
            	**type**\:   :py:class:`StateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ospf.StateChange>`
            
            

            """

            _prefix = 'ipv4-ospf-cfg'
            _revision = '2017-01-02'

            def __init__(self):
                self.parent = None
                self.error = Snmp.Notification.Ospf.Error()
                self.error.parent = self
                self.lsa = Snmp.Notification.Ospf.Lsa()
                self.lsa.parent = self
                self.retransmit = Snmp.Notification.Ospf.Retransmit()
                self.retransmit.parent = self
                self.state_change = Snmp.Notification.Ospf.StateChange()
                self.state_change.parent = self


            class Lsa(object):
                """
                SNMP notifications related to LSAs
                
                .. attribute:: max_age_lsa
                
                	Enable ospfMaxAgeLsa notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: originate_lsa
                
                	Enable ospfOriginateLsa notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv4-ospf-cfg'
                _revision = '2017-01-02'

                def __init__(self):
                    self.parent = None
                    self.max_age_lsa = None
                    self.originate_lsa = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ipv4-ospf-cfg:ospf/Cisco-IOS-XR-ipv4-ospf-cfg:lsa'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.max_age_lsa is not None:
                        return True

                    if self.originate_lsa is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.Ospf.Lsa']['meta_info']


            class StateChange(object):
                """
                SNMP notifications for OSPF state change
                
                .. attribute:: interface
                
                	Enable ospfIfStateChange notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: neighbor
                
                	Enable ospfNbrStateChange notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_interface
                
                	Enable ospfVirtIfStateChange notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_neighbor
                
                	Enable ospfVirtNbrStateChange notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv4-ospf-cfg'
                _revision = '2017-01-02'

                def __init__(self):
                    self.parent = None
                    self.interface = None
                    self.neighbor = None
                    self.virtual_interface = None
                    self.virtual_neighbor = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ipv4-ospf-cfg:ospf/Cisco-IOS-XR-ipv4-ospf-cfg:state-change'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface is not None:
                        return True

                    if self.neighbor is not None:
                        return True

                    if self.virtual_interface is not None:
                        return True

                    if self.virtual_neighbor is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.Ospf.StateChange']['meta_info']


            class Retransmit(object):
                """
                SNMP notifications for packet retransmissions
                
                .. attribute:: packet
                
                	Enable ospfTxRetransmit notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_packet
                
                	Enable ospfVirtIfTxRetransmit notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv4-ospf-cfg'
                _revision = '2017-01-02'

                def __init__(self):
                    self.parent = None
                    self.packet = None
                    self.virtual_packet = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ipv4-ospf-cfg:ospf/Cisco-IOS-XR-ipv4-ospf-cfg:retransmit'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.packet is not None:
                        return True

                    if self.virtual_packet is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.Ospf.Retransmit']['meta_info']


            class Error(object):
                """
                SNMP notifications for OSPF errors
                
                .. attribute:: authentication_failure
                
                	Enable ospfIfAuthFailure notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: bad_packet
                
                	Enable ospfIfRxBadPacket notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: config_error
                
                	Enable ospfIfConfigError notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_authentication_failure
                
                	Enable ospfVirtIfAuthFailure notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_bad_packet
                
                	Enable ospfVirtIfRxBadPacket notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_config_error
                
                	Enable ospfVirtIfConfigError notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv4-ospf-cfg'
                _revision = '2017-01-02'

                def __init__(self):
                    self.parent = None
                    self.authentication_failure = None
                    self.bad_packet = None
                    self.config_error = None
                    self.virtual_authentication_failure = None
                    self.virtual_bad_packet = None
                    self.virtual_config_error = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ipv4-ospf-cfg:ospf/Cisco-IOS-XR-ipv4-ospf-cfg:error'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.authentication_failure is not None:
                        return True

                    if self.bad_packet is not None:
                        return True

                    if self.config_error is not None:
                        return True

                    if self.virtual_authentication_failure is not None:
                        return True

                    if self.virtual_bad_packet is not None:
                        return True

                    if self.virtual_config_error is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.Ospf.Error']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ipv4-ospf-cfg:ospf'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.error is not None and self.error._has_data():
                    return True

                if self.lsa is not None and self.lsa._has_data():
                    return True

                if self.retransmit is not None and self.retransmit._has_data():
                    return True

                if self.state_change is not None and self.state_change._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Ospf']['meta_info']


        class Vrrp(object):
            """
            VRRP\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable VRRP\-MIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ipv4-vrrp-cfg'
            _revision = '2016-12-16'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Vrrp']['meta_info']


        class Ospfv3(object):
            """
            OSPFv3\-MIB notification configuration
            
            .. attribute:: error
            
            	SNMP notifications for OSPF errors
            	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ospfv3.Error>`
            
            .. attribute:: state_change
            
            	SNMP notifications for OSPF state change
            	**type**\:   :py:class:`StateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ospfv3.StateChange>`
            
            

            """

            _prefix = 'ipv6-ospfv3-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.error = Snmp.Notification.Ospfv3.Error()
                self.error.parent = self
                self.state_change = Snmp.Notification.Ospfv3.StateChange()
                self.state_change.parent = self


            class Error(object):
                """
                SNMP notifications for OSPF errors
                
                .. attribute:: bad_packet
                
                	Enable ospfv3IfRxBadPacket notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: config_error
                
                	Enable ospfv3IfConfigError notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_bad_packet
                
                	Enable ospfv3VirtIfRxBadPacket notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_config_error
                
                	Enable ospfv3VirtIfConfigError notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv6-ospfv3-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bad_packet = None
                    self.config_error = None
                    self.virtual_bad_packet = None
                    self.virtual_config_error = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ipv6-ospfv3-cfg:ospfv3/Cisco-IOS-XR-ipv6-ospfv3-cfg:error'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.bad_packet is not None:
                        return True

                    if self.config_error is not None:
                        return True

                    if self.virtual_bad_packet is not None:
                        return True

                    if self.virtual_config_error is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.Ospfv3.Error']['meta_info']


            class StateChange(object):
                """
                SNMP notifications for OSPF state change
                
                .. attribute:: interface
                
                	Enable ospfv3IfStateChange notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: neighbor
                
                	Enable ospfv3NbrStateChange notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: nssa_translator
                
                	Enable ospfv3NssaTranslatorStatusChange notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: restart
                
                	Enable ospfv3RestartStatusChange notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: restart_helper
                
                	Enable ospfv3NbrRestartHelperStatusChange notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: restart_virtual_helper
                
                	Enable ospfv3VirtNbrRestartHelperStatusChange notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_interface
                
                	Enable ospfv3VirtIfStateChange notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_neighbor
                
                	Enable ospfv3VirtNbrStateChange notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv6-ospfv3-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = None
                    self.neighbor = None
                    self.nssa_translator = None
                    self.restart = None
                    self.restart_helper = None
                    self.restart_virtual_helper = None
                    self.virtual_interface = None
                    self.virtual_neighbor = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ipv6-ospfv3-cfg:ospfv3/Cisco-IOS-XR-ipv6-ospfv3-cfg:state-change'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface is not None:
                        return True

                    if self.neighbor is not None:
                        return True

                    if self.nssa_translator is not None:
                        return True

                    if self.restart is not None:
                        return True

                    if self.restart_helper is not None:
                        return True

                    if self.restart_virtual_helper is not None:
                        return True

                    if self.virtual_interface is not None:
                        return True

                    if self.virtual_neighbor is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.Ospfv3.StateChange']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-ipv6-ospfv3-cfg:ospfv3'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.error is not None and self.error._has_data():
                    return True

                if self.state_change is not None and self.state_change._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Ospfv3']['meta_info']


        class MplsLdp(object):
            """
            MPLS\-LDP\-STD\-MIB notification configuration
            
            .. attribute:: init_session_threshold_exceeded
            
            	Enable mplsLdpInitSessionThresholdExceeded notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: session_down
            
            	Enable mplsLdpSessionDown notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: session_up
            
            	Enable mplsLdpSessionUp notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.init_session_threshold_exceeded = None
                self.session_down = None
                self.session_up = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.init_session_threshold_exceeded is not None:
                    return True

                if self.session_down is not None:
                    return True

                if self.session_up is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.MplsLdp']['meta_info']


        class MplsTeP2Mp(object):
            """
            CISCO\-MPLS\-TE\-P2MP\-STD\-MIB notification
            configuration
            
            .. attribute:: down
            
            	Enable cmplsTeP2mpTunnelDestDown notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: up
            
            	Enable cmplsTeP2mpTunnelDestUp notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.down = None
                self.up = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-mpls-te-cfg:mpls-te-p2mp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.down is not None:
                    return True

                if self.up is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.MplsTeP2Mp']['meta_info']


        class MplsTe(object):
            """
            MPLS\-TE\-STD\-MIB notification configuration
            
            .. attribute:: cisco
            
            	Enable MPLS TE tunnel Cisco format (default IETF) notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: cisco_extension
            
            	CISCO\-MPLS\-TE\-STD\-EXT\-MIB notification configuration
            	**type**\:   :py:class:`CiscoExtension <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.MplsTe.CiscoExtension>`
            
            .. attribute:: down
            
            	Enable mplsTunnelDown notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: reoptimize
            
            	Enable mplsTunnelReoptimized notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: reroute
            
            	Enable mplsTunnelRerouted notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: up
            
            	Enable mplsTunnelUp notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.cisco = None
                self.cisco_extension = Snmp.Notification.MplsTe.CiscoExtension()
                self.cisco_extension.parent = self
                self.down = None
                self.reoptimize = None
                self.reroute = None
                self.up = None


            class CiscoExtension(object):
                """
                CISCO\-MPLS\-TE\-STD\-EXT\-MIB notification
                configuration
                
                .. attribute:: bringup_fail
                
                	Enable cmplsTunnelBringupFail notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: insufficient_bandwidth
                
                	Enable cmplsTunnelInsuffBW notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: preempt
                
                	Enable cmplsTunnelPreempt notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: re_route_pending
                
                	Enable cmplsTunnelReRoutePending notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: re_route_pending_clear
                
                	Enable cmplsTunnelReRoutePendingClear notification
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bringup_fail = None
                    self.insufficient_bandwidth = None
                    self.preempt = None
                    self.re_route_pending = None
                    self.re_route_pending_clear = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:cisco-extension'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.bringup_fail is not None:
                        return True

                    if self.insufficient_bandwidth is not None:
                        return True

                    if self.preempt is not None:
                        return True

                    if self.re_route_pending is not None:
                        return True

                    if self.re_route_pending_clear is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.MplsTe.CiscoExtension']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-mpls-te-cfg:mpls-te'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.cisco is not None:
                    return True

                if self.cisco_extension is not None and self.cisco_extension._has_data():
                    return True

                if self.down is not None:
                    return True

                if self.reoptimize is not None:
                    return True

                if self.reroute is not None:
                    return True

                if self.up is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.MplsTe']['meta_info']


        class MplsFrr(object):
            """
            CISCO\-IETF\-FRR\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable cmplsFrrMIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: protected
            
            	Enable cmplsFrrProtected notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: unprotected
            
            	Enable cmplsFrrUnProtected notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.protected = None
                self.unprotected = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-mpls-te-cfg:mpls-frr'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.protected is not None:
                    return True

                if self.unprotected is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.MplsFrr']['meta_info']


        class MplsL3Vpn(object):
            """
            MPLS\-L3VPN\-STD\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable mplsL3VpnMIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: max_threshold_cleared
            
            	Enable mplsL3VpnNumVrfRouteMaxThreshCleared notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: max_threshold_exceeded
            
            	Enable mplsL3VpnVrfNumVrfRouteMaxThreshExceeded notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: max_threshold_reissue_notification_time
            
            	Time interval (secs) for re\-issuing max\-threshold notification
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: second
            
            .. attribute:: mid_threshold_exceeded
            
            	Enable mplsL3VpnVrfRouteMidThreshExceeded notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: vrf_down
            
            	Enable mplsL3VpnVrfDown notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: vrf_up
            
            	Enable mplsL3VpnVrfUp notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.max_threshold_cleared = None
                self.max_threshold_exceeded = None
                self.max_threshold_reissue_notification_time = None
                self.mid_threshold_exceeded = None
                self.vrf_down = None
                self.vrf_up = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-mpls-vpn-cfg:mpls-l3vpn'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.max_threshold_cleared is not None:
                    return True

                if self.max_threshold_exceeded is not None:
                    return True

                if self.max_threshold_reissue_notification_time is not None:
                    return True

                if self.mid_threshold_exceeded is not None:
                    return True

                if self.vrf_down is not None:
                    return True

                if self.vrf_up is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.MplsL3Vpn']['meta_info']


        class Otn(object):
            """
            CISCO\-OTN\-IF\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable ciscoOtnIfMIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'otnifmib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-otnifmib-cfg:otn'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Otn']['meta_info']


        class Sensor(object):
            """
            CISCO\-ENTITY\-SENSOR\-MIB notification
            configuration
            
            .. attribute:: enable
            
            	Enable entitySensorMIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-ciscosensormib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-snmp-ciscosensormib-cfg:sensor'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Sensor']['meta_info']


        class Entity(object):
            """
            Enable ENTITY\-MIB notifications
            
            .. attribute:: enable
            
            	Enable entityMIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-entitymib-cfg'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-snmp-entitymib-cfg:entity'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Entity']['meta_info']


        class EntityState(object):
            """
            ENTITY\-STATE\-MIB notification configuration
            
            .. attribute:: oper_status
            
            	Enable entStateOperEnable and entStateOperDisable notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: switchover
            
            	Enable ceStateExtStandbySwitchover notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-entstatemib-cfg'
            _revision = '2015-07-27'

            def __init__(self):
                self.parent = None
                self.oper_status = None
                self.switchover = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-snmp-entstatemib-cfg:entity-state'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.oper_status is not None:
                    return True

                if self.switchover is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.EntityState']['meta_info']


        class FruControl(object):
            """
            CISCO\-ENTITY\-FRU\-CONTROL\-MIB notification
            configuration
            
            .. attribute:: enable
            
            	Enable ciscoEntityFRUControlMIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-frucontrolmib-cfg'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-snmp-frucontrolmib-cfg:fru-control'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.FruControl']['meta_info']


        class Rf(object):
            """
            CISCO\-RF\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable ciscoRFMIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-mib-rfmib-cfg'
            _revision = '2016-05-13'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-snmp-mib-rfmib-cfg:rf'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Rf']['meta_info']


        class Syslog(object):
            """
            CISCO\-SYSLOG\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable ciscoSyslogMIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-syslogmib-cfg'
            _revision = '2015-12-01'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification/Cisco-IOS-XR-snmp-syslogmib-cfg:syslog'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Syslog']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:notification'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.bfd is not None and self.bfd._has_data():
                return True

            if self.bgp is not None and self.bgp._has_data():
                return True

            if self.cfm is not None and self.cfm._has_data():
                return True

            if self.config_copy is not None and self.config_copy._has_data():
                return True

            if self.config_man is not None and self.config_man._has_data():
                return True

            if self.entity is not None and self.entity._has_data():
                return True

            if self.entity_redundancy is not None and self.entity_redundancy._has_data():
                return True

            if self.entity_state is not None and self.entity_state._has_data():
                return True

            if self.flash is not None and self.flash._has_data():
                return True

            if self.fru_control is not None and self.fru_control._has_data():
                return True

            if self.hsrp is not None and self.hsrp._has_data():
                return True

            if self.isis is not None and self.isis._has_data():
                return True

            if self.l2vpn is not None and self.l2vpn._has_data():
                return True

            if self.mpls_frr is not None and self.mpls_frr._has_data():
                return True

            if self.mpls_l3vpn is not None and self.mpls_l3vpn._has_data():
                return True

            if self.mpls_ldp is not None and self.mpls_ldp._has_data():
                return True

            if self.mpls_te is not None and self.mpls_te._has_data():
                return True

            if self.mpls_te_p2mp is not None and self.mpls_te_p2mp._has_data():
                return True

            if self.ntp is not None and self.ntp._has_data():
                return True

            if self.oam is not None and self.oam._has_data():
                return True

            if self.ospf is not None and self.ospf._has_data():
                return True

            if self.ospfv3 is not None and self.ospfv3._has_data():
                return True

            if self.otn is not None and self.otn._has_data():
                return True

            if self.rf is not None and self.rf._has_data():
                return True

            if self.rsvp is not None and self.rsvp._has_data():
                return True

            if self.selective_vrf_download is not None and self.selective_vrf_download._has_data():
                return True

            if self.sensor is not None and self.sensor._has_data():
                return True

            if self.snmp is not None and self.snmp._has_data():
                return True

            if self.syslog is not None and self.syslog._has_data():
                return True

            if self.system is not None and self.system._has_data():
                return True

            if self.vpls is not None and self.vpls._has_data():
                return True

            if self.vrrp is not None and self.vrrp._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Notification']['meta_info']


    class Correlator(object):
        """
        Configure properties of the trap correlator
        
        .. attribute:: buffer_size
        
        	Configure size of the correlator buffer
        	**type**\:  int
        
        	**range:** 1024..52428800
        
        .. attribute:: rule_sets
        
        	Table of configured rulesets
        	**type**\:   :py:class:`RuleSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.RuleSets>`
        
        .. attribute:: rules
        
        	Table of configured rules
        	**type**\:   :py:class:`Rules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.buffer_size = None
            self.rule_sets = Snmp.Correlator.RuleSets()
            self.rule_sets.parent = self
            self.rules = Snmp.Correlator.Rules()
            self.rules.parent = self


        class Rules(object):
            """
            Table of configured rules
            
            .. attribute:: rule
            
            	Rule name
            	**type**\: list of    :py:class:`Rule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.rule = YList()
                self.rule.parent = self
                self.rule.name = 'rule'


            class Rule(object):
                """
                Rule name
                
                .. attribute:: name  <key>
                
                	Rule name
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: applied_to
                
                	Applied to the Rule or Ruleset
                	**type**\:   :py:class:`AppliedTo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.AppliedTo>`
                
                .. attribute:: non_stateful
                
                	The Non\-Stateful Rule Type
                	**type**\:   :py:class:`NonStateful <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonStateful>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2015-10-27'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.applied_to = Snmp.Correlator.Rules.Rule.AppliedTo()
                    self.applied_to.parent = self
                    self.non_stateful = None


                class NonStateful(object):
                    """
                    The Non\-Stateful Rule Type
                    
                    .. attribute:: non_root_causes
                    
                    	Table of configured non\-rootcause
                    	**type**\:   :py:class:`NonRootCauses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses>`
                    
                    .. attribute:: root_causes
                    
                    	Table of configured rootcause (only one entry allowed)
                    	**type**\:   :py:class:`RootCauses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonStateful.RootCauses>`
                    
                    .. attribute:: timeout
                    
                    	Timeout (time to wait for active correlation) in milliseconds
                    	**type**\:  int
                    
                    	**range:** 1..600000
                    
                    	**units**\: millisecond
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2015-10-27'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.non_root_causes = Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses()
                        self.non_root_causes.parent = self
                        self.root_causes = Snmp.Correlator.Rules.Rule.NonStateful.RootCauses()
                        self.root_causes.parent = self
                        self.timeout = None


                    class RootCauses(object):
                        """
                        Table of configured rootcause (only one
                        entry allowed)
                        
                        .. attribute:: root_cause
                        
                        	The rootcause \- maximum of one can be configured per rule
                        	**type**\: list of    :py:class:`RootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2015-10-27'

                        def __init__(self):
                            self.parent = None
                            self.root_cause = YList()
                            self.root_cause.parent = self
                            self.root_cause.name = 'root_cause'


                        class RootCause(object):
                            """
                            The rootcause \- maximum of one can be
                            configured per rule
                            
                            .. attribute:: oid  <key>
                            
                            	OID of rootcause trap (dotted decimal)
                            	**type**\:  str
                            
                            .. attribute:: created
                            
                            	Create rootcause
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: var_binds
                            
                            	Varbinds to match
                            	**type**\:   :py:class:`VarBinds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds>`
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2015-10-27'

                            def __init__(self):
                                self.parent = None
                                self.oid = None
                                self.created = None
                                self.var_binds = Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds()
                                self.var_binds.parent = self


                            class VarBinds(object):
                                """
                                Varbinds to match
                                
                                .. attribute:: var_bind
                                
                                	Varbind match conditions
                                	**type**\: list of    :py:class:`VarBind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind>`
                                
                                

                                """

                                _prefix = 'snmp-agent-cfg'
                                _revision = '2015-10-27'

                                def __init__(self):
                                    self.parent = None
                                    self.var_bind = YList()
                                    self.var_bind.parent = self
                                    self.var_bind.name = 'var_bind'


                                class VarBind(object):
                                    """
                                    Varbind match conditions
                                    
                                    .. attribute:: oid  <key>
                                    
                                    	OID of varbind (dotted decimal)
                                    	**type**\:  str
                                    
                                    .. attribute:: match
                                    
                                    	VarBind match conditions
                                    	**type**\:   :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind.Match>`
                                    
                                    

                                    """

                                    _prefix = 'snmp-agent-cfg'
                                    _revision = '2015-10-27'

                                    def __init__(self):
                                        self.parent = None
                                        self.oid = None
                                        self.match = Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind.Match()
                                        self.match.parent = self


                                    class Match(object):
                                        """
                                        VarBind match conditions
                                        
                                        .. attribute:: index
                                        
                                        	Regular Expression to match index
                                        	**type**\:  str
                                        
                                        .. attribute:: value
                                        
                                        	Regular Expression to match value
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'snmp-agent-cfg'
                                        _revision = '2015-10-27'

                                        def __init__(self):
                                            self.parent = None
                                            self.index = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:match'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.index is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                            return meta._meta_table['Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind.Match']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.oid is None:
                                            raise YPYModelError('Key property oid is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:var-bind[Cisco-IOS-XR-snmp-agent-cfg:oid = ' + str(self.oid) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.oid is not None:
                                            return True

                                        if self.match is not None and self.match._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                        return meta._meta_table['Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:var-binds'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.var_bind is not None:
                                        for child_ref in self.var_bind:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                    return meta._meta_table['Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.oid is None:
                                    raise YPYModelError('Key property oid is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:root-cause[Cisco-IOS-XR-snmp-agent-cfg:oid = ' + str(self.oid) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.oid is not None:
                                    return True

                                if self.created is not None:
                                    return True

                                if self.var_binds is not None and self.var_binds._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:root-causes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.root_cause is not None:
                                for child_ref in self.root_cause:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Correlator.Rules.Rule.NonStateful.RootCauses']['meta_info']


                    class NonRootCauses(object):
                        """
                        Table of configured non\-rootcause
                        
                        .. attribute:: non_root_cause
                        
                        	A non\-rootcause
                        	**type**\: list of    :py:class:`NonRootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2015-10-27'

                        def __init__(self):
                            self.parent = None
                            self.non_root_cause = YList()
                            self.non_root_cause.parent = self
                            self.non_root_cause.name = 'non_root_cause'


                        class NonRootCause(object):
                            """
                            A non\-rootcause
                            
                            .. attribute:: oid  <key>
                            
                            	OID of nonrootcause trap (dotted decimal)
                            	**type**\:  str
                            
                            .. attribute:: created
                            
                            	Create nonrootcause
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: var_binds
                            
                            	Varbinds to match
                            	**type**\:   :py:class:`VarBinds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds>`
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2015-10-27'

                            def __init__(self):
                                self.parent = None
                                self.oid = None
                                self.created = None
                                self.var_binds = Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds()
                                self.var_binds.parent = self


                            class VarBinds(object):
                                """
                                Varbinds to match
                                
                                .. attribute:: var_bind
                                
                                	Varbind match conditions
                                	**type**\: list of    :py:class:`VarBind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind>`
                                
                                

                                """

                                _prefix = 'snmp-agent-cfg'
                                _revision = '2015-10-27'

                                def __init__(self):
                                    self.parent = None
                                    self.var_bind = YList()
                                    self.var_bind.parent = self
                                    self.var_bind.name = 'var_bind'


                                class VarBind(object):
                                    """
                                    Varbind match conditions
                                    
                                    .. attribute:: oid  <key>
                                    
                                    	OID of varbind (dotted decimal)
                                    	**type**\:  str
                                    
                                    .. attribute:: match
                                    
                                    	VarBind match conditions
                                    	**type**\:   :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind.Match>`
                                    
                                    

                                    """

                                    _prefix = 'snmp-agent-cfg'
                                    _revision = '2015-10-27'

                                    def __init__(self):
                                        self.parent = None
                                        self.oid = None
                                        self.match = Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind.Match()
                                        self.match.parent = self


                                    class Match(object):
                                        """
                                        VarBind match conditions
                                        
                                        .. attribute:: index
                                        
                                        	Regular Expression to match index
                                        	**type**\:  str
                                        
                                        .. attribute:: value
                                        
                                        	Regular Expression to match value
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'snmp-agent-cfg'
                                        _revision = '2015-10-27'

                                        def __init__(self):
                                            self.parent = None
                                            self.index = None
                                            self.value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:match'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.index is not None:
                                                return True

                                            if self.value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                            return meta._meta_table['Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind.Match']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.oid is None:
                                            raise YPYModelError('Key property oid is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:var-bind[Cisco-IOS-XR-snmp-agent-cfg:oid = ' + str(self.oid) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.oid is not None:
                                            return True

                                        if self.match is not None and self.match._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                        return meta._meta_table['Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:var-binds'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.var_bind is not None:
                                        for child_ref in self.var_bind:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                    return meta._meta_table['Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.oid is None:
                                    raise YPYModelError('Key property oid is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:non-root-cause[Cisco-IOS-XR-snmp-agent-cfg:oid = ' + str(self.oid) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.oid is not None:
                                    return True

                                if self.created is not None:
                                    return True

                                if self.var_binds is not None and self.var_binds._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:non-root-causes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.non_root_cause is not None:
                                for child_ref in self.non_root_cause:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:non-stateful'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.non_root_causes is not None and self.non_root_causes._has_data():
                            return True

                        if self.root_causes is not None and self.root_causes._has_data():
                            return True

                        if self.timeout is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Correlator.Rules.Rule.NonStateful']['meta_info']


                class AppliedTo(object):
                    """
                    Applied to the Rule or Ruleset
                    
                    .. attribute:: all
                    
                    	Apply to all of the device
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: hosts
                    
                    	Table of configured hosts to apply rules to
                    	**type**\:   :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.AppliedTo.Hosts>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2015-10-27'

                    def __init__(self):
                        self.parent = None
                        self.all = None
                        self.hosts = Snmp.Correlator.Rules.Rule.AppliedTo.Hosts()
                        self.hosts.parent = self


                    class Hosts(object):
                        """
                        Table of configured hosts to apply rules to
                        
                        .. attribute:: host
                        
                        	A destination host
                        	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2015-10-27'

                        def __init__(self):
                            self.parent = None
                            self.host = YList()
                            self.host.parent = self
                            self.host.name = 'host'


                        class Host(object):
                            """
                            A destination host
                            
                            .. attribute:: ip_address  <key>
                            
                            	IP address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: port  <key>
                            
                            	Port (specify 162 for default)
                            	**type**\:  int
                            
                            	**range:** 1..65535
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2015-10-27'

                            def __init__(self):
                                self.parent = None
                                self.ip_address = None
                                self.port = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.ip_address is None:
                                    raise YPYModelError('Key property ip_address is None')
                                if self.port is None:
                                    raise YPYModelError('Key property port is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:host[Cisco-IOS-XR-snmp-agent-cfg:ip-address = ' + str(self.ip_address) + '][Cisco-IOS-XR-snmp-agent-cfg:port = ' + str(self.port) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.ip_address is not None:
                                    return True

                                if self.port is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:hosts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.host is not None:
                                for child_ref in self.host:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Correlator.Rules.Rule.AppliedTo.Hosts']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:applied-to'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.all is not None:
                            return True

                        if self.hosts is not None and self.hosts._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Correlator.Rules.Rule.AppliedTo']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:correlator/Cisco-IOS-XR-snmp-agent-cfg:rules/Cisco-IOS-XR-snmp-agent-cfg:rule[Cisco-IOS-XR-snmp-agent-cfg:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.applied_to is not None and self.applied_to._has_data():
                        return True

                    if self.non_stateful is not None and self.non_stateful._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Correlator.Rules.Rule']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:correlator/Cisco-IOS-XR-snmp-agent-cfg:rules'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.rule is not None:
                    for child_ref in self.rule:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Correlator.Rules']['meta_info']


        class RuleSets(object):
            """
            Table of configured rulesets
            
            .. attribute:: rule_set
            
            	Ruleset name
            	**type**\: list of    :py:class:`RuleSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.RuleSets.RuleSet>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.rule_set = YList()
                self.rule_set.parent = self
                self.rule_set.name = 'rule_set'


            class RuleSet(object):
                """
                Ruleset name
                
                .. attribute:: name  <key>
                
                	Ruleset name
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: applied_to
                
                	Applied to the Rule or Ruleset
                	**type**\:   :py:class:`AppliedTo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.RuleSets.RuleSet.AppliedTo>`
                
                .. attribute:: rulenames
                
                	Table of configured rulenames
                	**type**\:   :py:class:`Rulenames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.RuleSets.RuleSet.Rulenames>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2015-10-27'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.applied_to = Snmp.Correlator.RuleSets.RuleSet.AppliedTo()
                    self.applied_to.parent = self
                    self.rulenames = Snmp.Correlator.RuleSets.RuleSet.Rulenames()
                    self.rulenames.parent = self


                class Rulenames(object):
                    """
                    Table of configured rulenames
                    
                    .. attribute:: rulename
                    
                    	A rulename
                    	**type**\: list of    :py:class:`Rulename <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2015-10-27'

                    def __init__(self):
                        self.parent = None
                        self.rulename = YList()
                        self.rulename.parent = self
                        self.rulename.name = 'rulename'


                    class Rulename(object):
                        """
                        A rulename
                        
                        .. attribute:: rulename  <key>
                        
                        	Rule name
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2015-10-27'

                        def __init__(self):
                            self.parent = None
                            self.rulename = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.rulename is None:
                                raise YPYModelError('Key property rulename is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:rulename[Cisco-IOS-XR-snmp-agent-cfg:rulename = ' + str(self.rulename) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.rulename is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:rulenames'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.rulename is not None:
                            for child_ref in self.rulename:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Correlator.RuleSets.RuleSet.Rulenames']['meta_info']


                class AppliedTo(object):
                    """
                    Applied to the Rule or Ruleset
                    
                    .. attribute:: all
                    
                    	Apply to all of the device
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: hosts
                    
                    	Table of configured hosts to apply rules to
                    	**type**\:   :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2015-10-27'

                    def __init__(self):
                        self.parent = None
                        self.all = None
                        self.hosts = Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts()
                        self.hosts.parent = self


                    class Hosts(object):
                        """
                        Table of configured hosts to apply rules to
                        
                        .. attribute:: host
                        
                        	A destination host
                        	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2015-10-27'

                        def __init__(self):
                            self.parent = None
                            self.host = YList()
                            self.host.parent = self
                            self.host.name = 'host'


                        class Host(object):
                            """
                            A destination host
                            
                            .. attribute:: ip_address  <key>
                            
                            	IP address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: port  <key>
                            
                            	Port (specify 162 for default)
                            	**type**\:  int
                            
                            	**range:** 1..65535
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2015-10-27'

                            def __init__(self):
                                self.parent = None
                                self.ip_address = None
                                self.port = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.ip_address is None:
                                    raise YPYModelError('Key property ip_address is None')
                                if self.port is None:
                                    raise YPYModelError('Key property port is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:host[Cisco-IOS-XR-snmp-agent-cfg:ip-address = ' + str(self.ip_address) + '][Cisco-IOS-XR-snmp-agent-cfg:port = ' + str(self.port) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.ip_address is not None:
                                    return True

                                if self.port is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:hosts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.host is not None:
                                for child_ref in self.host:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:applied-to'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.all is not None:
                            return True

                        if self.hosts is not None and self.hosts._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Correlator.RuleSets.RuleSet.AppliedTo']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:correlator/Cisco-IOS-XR-snmp-agent-cfg:rule-sets/Cisco-IOS-XR-snmp-agent-cfg:rule-set[Cisco-IOS-XR-snmp-agent-cfg:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.applied_to is not None and self.applied_to._has_data():
                        return True

                    if self.rulenames is not None and self.rulenames._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Correlator.RuleSets.RuleSet']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:correlator/Cisco-IOS-XR-snmp-agent-cfg:rule-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.rule_set is not None:
                    for child_ref in self.rule_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Correlator.RuleSets']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:correlator'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.buffer_size is not None:
                return True

            if self.rule_sets is not None and self.rule_sets._has_data():
                return True

            if self.rules is not None and self.rules._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Correlator']['meta_info']


    class BulkStats(object):
        """
        SNMP bulk stats configuration commands
        
        .. attribute:: memory
        
        	per process memory limit in kilo bytes
        	**type**\:  int
        
        	**range:** 100..200000
        
        	**units**\: kilobyte
        
        .. attribute:: objects
        
        	Configure an Object List 
        	**type**\:   :py:class:`Objects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Objects>`
        
        .. attribute:: schemas
        
        	Configure schema definition
        	**type**\:   :py:class:`Schemas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Schemas>`
        
        .. attribute:: transfers
        
        	Periodicity for the transfer of bulk data in minutes
        	**type**\:   :py:class:`Transfers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Transfers>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.memory = None
            self.objects = Snmp.BulkStats.Objects()
            self.objects.parent = self
            self.schemas = Snmp.BulkStats.Schemas()
            self.schemas.parent = self
            self.transfers = Snmp.BulkStats.Transfers()
            self.transfers.parent = self


        class Schemas(object):
            """
            Configure schema definition
            
            .. attribute:: schema
            
            	The name of the Schema
            	**type**\: list of    :py:class:`Schema <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Schemas.Schema>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.schema = YList()
                self.schema.parent = self
                self.schema.name = 'schema'


            class Schema(object):
                """
                The name of the Schema
                
                .. attribute:: schema_name  <key>
                
                	The name of the schema
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: instance
                
                	Object instance information
                	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Schemas.Schema.Instance>`
                
                	**presence node**\: True
                
                .. attribute:: poll_interval
                
                	Periodicity for polling of objects in this schema in minutes
                	**type**\:  int
                
                	**range:** 1..20000
                
                	**units**\: minute
                
                .. attribute:: schema_object_list
                
                	Name of an object List
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: type
                
                	Configure schema name
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2015-10-27'

                def __init__(self):
                    self.parent = None
                    self.schema_name = None
                    self.instance = None
                    self.poll_interval = None
                    self.schema_object_list = None
                    self.type = None


                class Instance(object):
                    """
                    Object instance information
                    
                    .. attribute:: end
                    
                    	End Instance OID for repetition
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: instance
                    
                    	Instance of the schema
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: max
                    
                    	Max value of Instance repetition
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**mandatory**\: True
                    
                    .. attribute:: start
                    
                    	Start Instance OID for repetition
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: sub_interface
                    
                    	Include all the subinterface
                    	**type**\:  bool
                    
                    	**mandatory**\: True
                    
                    .. attribute:: type
                    
                    	Type of the instance
                    	**type**\:   :py:class:`SnmpBulkstatSchemaEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpBulkstatSchemaEnum>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2015-10-27'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.end = None
                        self.instance = None
                        self.max = None
                        self.start = None
                        self.sub_interface = None
                        self.type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:instance'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.end is not None:
                            return True

                        if self.instance is not None:
                            return True

                        if self.max is not None:
                            return True

                        if self.start is not None:
                            return True

                        if self.sub_interface is not None:
                            return True

                        if self.type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.BulkStats.Schemas.Schema.Instance']['meta_info']

                @property
                def _common_path(self):
                    if self.schema_name is None:
                        raise YPYModelError('Key property schema_name is None')

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:bulk-stats/Cisco-IOS-XR-snmp-agent-cfg:schemas/Cisco-IOS-XR-snmp-agent-cfg:schema[Cisco-IOS-XR-snmp-agent-cfg:schema-name = ' + str(self.schema_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.schema_name is not None:
                        return True

                    if self.instance is not None and self.instance._has_data():
                        return True

                    if self.poll_interval is not None:
                        return True

                    if self.schema_object_list is not None:
                        return True

                    if self.type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.BulkStats.Schemas.Schema']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:bulk-stats/Cisco-IOS-XR-snmp-agent-cfg:schemas'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.schema is not None:
                    for child_ref in self.schema:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.BulkStats.Schemas']['meta_info']


        class Objects(object):
            """
            Configure an Object List 
            
            .. attribute:: object
            
            	Name of the object List
            	**type**\: list of    :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Objects.Object>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.object = YList()
                self.object.parent = self
                self.object.name = 'object'


            class Object(object):
                """
                Name of the object List
                
                .. attribute:: object_list_name  <key>
                
                	Name of the object List
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: objects
                
                	Configure an object List
                	**type**\:   :py:class:`Objects_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Objects.Object.Objects_>`
                
                .. attribute:: type
                
                	Configure object list name
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2015-10-27'

                def __init__(self):
                    self.parent = None
                    self.object_list_name = None
                    self.objects = Snmp.BulkStats.Objects.Object.Objects_()
                    self.objects.parent = self
                    self.type = None


                class Objects_(object):
                    """
                    Configure an object List
                    
                    .. attribute:: object
                    
                    	Object name or OID
                    	**type**\: list of    :py:class:`Object_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Objects.Object.Objects_.Object_>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2015-10-27'

                    def __init__(self):
                        self.parent = None
                        self.object = YList()
                        self.object.parent = self
                        self.object.name = 'object'


                    class Object_(object):
                        """
                        Object name or OID
                        
                        .. attribute:: oid  <key>
                        
                        	Object name or OID 
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2015-10-27'

                        def __init__(self):
                            self.parent = None
                            self.oid = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.oid is None:
                                raise YPYModelError('Key property oid is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:object[Cisco-IOS-XR-snmp-agent-cfg:oid = ' + str(self.oid) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.oid is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.BulkStats.Objects.Object.Objects_.Object_']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:objects'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.object is not None:
                            for child_ref in self.object:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.BulkStats.Objects.Object.Objects_']['meta_info']

                @property
                def _common_path(self):
                    if self.object_list_name is None:
                        raise YPYModelError('Key property object_list_name is None')

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:bulk-stats/Cisco-IOS-XR-snmp-agent-cfg:objects/Cisco-IOS-XR-snmp-agent-cfg:object[Cisco-IOS-XR-snmp-agent-cfg:object-list-name = ' + str(self.object_list_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.object_list_name is not None:
                        return True

                    if self.objects is not None and self.objects._has_data():
                        return True

                    if self.type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.BulkStats.Objects.Object']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:bulk-stats/Cisco-IOS-XR-snmp-agent-cfg:objects'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.object is not None:
                    for child_ref in self.object:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.BulkStats.Objects']['meta_info']


        class Transfers(object):
            """
            Periodicity for the transfer of bulk data in
            minutes
            
            .. attribute:: transfer
            
            	Name of bulk transfer
            	**type**\: list of    :py:class:`Transfer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Transfers.Transfer>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.transfer = YList()
                self.transfer.parent = self
                self.transfer.name = 'transfer'


            class Transfer(object):
                """
                Name of bulk transfer
                
                .. attribute:: transfer_name  <key>
                
                	Name of bulk transfer
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: buffer_size
                
                	Bulkstat data file maximum size in bytes
                	**type**\:  int
                
                	**range:** 1024..2147483647
                
                	**units**\: byte
                
                .. attribute:: enable
                
                	Start Data Collection for this Configuration
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: format
                
                	Format of the bulk data file
                	**type**\:   :py:class:`SnmpBulkstatFileFormatEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpBulkstatFileFormatEnum>`
                
                .. attribute:: interval
                
                	Periodicity for the transfer of bulk data in minutes
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: minute
                
                .. attribute:: primary
                
                	FTP or rcp or TFTP can be used for file transfer
                	**type**\:  str
                
                .. attribute:: retain
                
                	Retention period in minutes
                	**type**\:  int
                
                	**range:** 0..20000
                
                	**units**\: minute
                
                .. attribute:: retry
                
                	Number of transmission retries
                	**type**\:  int
                
                	**range:** 0..100
                
                .. attribute:: secondary
                
                	FTP or rcp or TFTP can be used for file transfer
                	**type**\:  str
                
                .. attribute:: transfer_schemas
                
                	Schema that contains objects to be collected
                	**type**\:   :py:class:`TransferSchemas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Transfers.Transfer.TransferSchemas>`
                
                .. attribute:: type
                
                	Configure transfer list name
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2015-10-27'

                def __init__(self):
                    self.parent = None
                    self.transfer_name = None
                    self.buffer_size = None
                    self.enable = None
                    self.format = None
                    self.interval = None
                    self.primary = None
                    self.retain = None
                    self.retry = None
                    self.secondary = None
                    self.transfer_schemas = Snmp.BulkStats.Transfers.Transfer.TransferSchemas()
                    self.transfer_schemas.parent = self
                    self.type = None


                class TransferSchemas(object):
                    """
                    Schema that contains objects to be collected
                    
                    .. attribute:: transfer_schema
                    
                    	Schema that contains objects to be collected
                    	**type**\: list of    :py:class:`TransferSchema <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2015-10-27'

                    def __init__(self):
                        self.parent = None
                        self.transfer_schema = YList()
                        self.transfer_schema.parent = self
                        self.transfer_schema.name = 'transfer_schema'


                    class TransferSchema(object):
                        """
                        Schema that contains objects to be collected
                        
                        .. attribute:: schema_name  <key>
                        
                        	Schema that contains objects to be collected
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2015-10-27'

                        def __init__(self):
                            self.parent = None
                            self.schema_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.schema_name is None:
                                raise YPYModelError('Key property schema_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:transfer-schema[Cisco-IOS-XR-snmp-agent-cfg:schema-name = ' + str(self.schema_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.schema_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:transfer-schemas'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.transfer_schema is not None:
                            for child_ref in self.transfer_schema:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.BulkStats.Transfers.Transfer.TransferSchemas']['meta_info']

                @property
                def _common_path(self):
                    if self.transfer_name is None:
                        raise YPYModelError('Key property transfer_name is None')

                    return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:bulk-stats/Cisco-IOS-XR-snmp-agent-cfg:transfers/Cisco-IOS-XR-snmp-agent-cfg:transfer[Cisco-IOS-XR-snmp-agent-cfg:transfer-name = ' + str(self.transfer_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.transfer_name is not None:
                        return True

                    if self.buffer_size is not None:
                        return True

                    if self.enable is not None:
                        return True

                    if self.format is not None:
                        return True

                    if self.interval is not None:
                        return True

                    if self.primary is not None:
                        return True

                    if self.retain is not None:
                        return True

                    if self.retry is not None:
                        return True

                    if self.secondary is not None:
                        return True

                    if self.transfer_schemas is not None and self.transfer_schemas._has_data():
                        return True

                    if self.type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.BulkStats.Transfers.Transfer']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:bulk-stats/Cisco-IOS-XR-snmp-agent-cfg:transfers'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.transfer is not None:
                    for child_ref in self.transfer:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.BulkStats.Transfers']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:bulk-stats'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.memory is not None:
                return True

            if self.objects is not None and self.objects._has_data():
                return True

            if self.schemas is not None and self.schemas._has_data():
                return True

            if self.transfers is not None and self.transfers._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.BulkStats']['meta_info']


    class DefaultCommunityMaps(object):
        """
        Container class to hold unencrpted community map
        
        .. attribute:: default_community_map
        
        	Unencrpted SNMP community map name 
        	**type**\: list of    :py:class:`DefaultCommunityMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.DefaultCommunityMaps.DefaultCommunityMap>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.default_community_map = YList()
            self.default_community_map.parent = self
            self.default_community_map.name = 'default_community_map'


        class DefaultCommunityMap(object):
            """
            Unencrpted SNMP community map name 
            
            .. attribute:: community_name  <key>
            
            	SNMP community map
            	**type**\:  str
            
            	**length:** 1..128
            
            .. attribute:: context
            
            	SNMP Context Name 
            	**type**\:  str
            
            .. attribute:: security
            
            	SNMP Security Name 
            	**type**\:  str
            
            .. attribute:: target_list
            
            	target list name 
            	**type**\:  str
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.community_name = None
                self.context = None
                self.security = None
                self.target_list = None

            @property
            def _common_path(self):
                if self.community_name is None:
                    raise YPYModelError('Key property community_name is None')

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:default-community-maps/Cisco-IOS-XR-snmp-agent-cfg:default-community-map[Cisco-IOS-XR-snmp-agent-cfg:community-name = ' + str(self.community_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.community_name is not None:
                    return True

                if self.context is not None:
                    return True

                if self.security is not None:
                    return True

                if self.target_list is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.DefaultCommunityMaps.DefaultCommunityMap']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:default-community-maps'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.default_community_map is not None:
                for child_ref in self.default_community_map:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.DefaultCommunityMaps']['meta_info']


    class OverloadControl(object):
        """
        Set overload control params for handling
        incoming messages
        
        .. attribute:: drop_time
        
        	Drop time in seconds for incoming queue (default 1 sec)
        	**type**\:  int
        
        	**range:** 0..300
        
        	**mandatory**\: True
        
        	**units**\: second
        
        .. attribute:: throttle_rate
        
        	Throttle time in milliseconds for incoming queue (default 500 msec)
        	**type**\:  int
        
        	**range:** 0..1000
        
        	**mandatory**\: True
        
        	**units**\: millisecond
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.drop_time = None
            self.throttle_rate = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:overload-control'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.drop_time is not None:
                return True

            if self.throttle_rate is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.OverloadControl']['meta_info']


    class Timeouts(object):
        """
        SNMP timeouts
        
        .. attribute:: duplicates
        
        	Duplicate request feature timeout
        	**type**\:  int
        
        	**range:** 0..20
        
        	**units**\: second
        
        	**default value**\: 1
        
        .. attribute:: in_qdrop
        
        	incoming queue drop feature timeout
        	**type**\:  int
        
        	**range:** 0..20
        
        	**units**\: second
        
        	**default value**\: 10
        
        .. attribute:: pdu_stats
        
        	SNMP pdu statistics timeout
        	**type**\:  int
        
        	**range:** 1..10
        
        	**units**\: second
        
        	**default value**\: 2
        
        .. attribute:: subagent
        
        	Sub\-Agent Request timeout
        	**type**\:  int
        
        	**range:** 1..20
        
        	**units**\: second
        
        	**default value**\: 10
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.duplicates = None
            self.in_qdrop = None
            self.pdu_stats = None
            self.subagent = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:timeouts'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.duplicates is not None:
                return True

            if self.in_qdrop is not None:
                return True

            if self.pdu_stats is not None:
                return True

            if self.subagent is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Timeouts']['meta_info']


    class Users(object):
        """
        Define a user who can access the SNMP engine
        
        .. attribute:: user
        
        	Name of the user
        	**type**\: list of    :py:class:`User <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Users.User>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.user = YList()
            self.user.parent = self
            self.user.name = 'user'


        class User(object):
            """
            Name of the user
            
            .. attribute:: user_name  <key>
            
            	Name of the user
            	**type**\:  str
            
            .. attribute:: algorithm
            
            	The algorithm used md5 or sha
            	**type**\:   :py:class:`SnmpHashAlgorithmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpHashAlgorithmEnum>`
            
            .. attribute:: authentication_password
            
            	The authentication password
            	**type**\:  str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: authentication_password_configured
            
            	Flag to indicate that authentication password is configred for version 3
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: group_name
            
            	Group to which the user belongs
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: owner
            
            	The system access either SDROwner or SystemOwner
            	**type**\:   :py:class:`SnmpOwnerAccessEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpOwnerAccessEnum>`
            
            .. attribute:: port
            
            	UDP port number
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: priv_algorithm
            
            	The algorithm used des56 or aes128 or aes192or aes256 or 3des
            	**type**\:   :py:class:`SnmpPrivAlgorithmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpPrivAlgorithmEnum>`
            
            .. attribute:: privacy_password
            
            	The privacy password
            	**type**\:  str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: privacy_password_configured
            
            	Flag to indicate that the privacy password is configured for version 3
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: remote_address
            
            	IP address of remote SNMP entity
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: v4_access_list
            
            	Ipv4 Access\-list name
            	**type**\:  str
            
            .. attribute:: v4acl_type
            
            	Access\-list type
            	**type**\:   :py:class:`SnmpaclEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpaclEnum>`
            
            .. attribute:: v6_access_list
            
            	Ipv6 Access\-list name
            	**type**\:  str
            
            .. attribute:: v6acl_type
            
            	Access\-list type
            	**type**\:   :py:class:`SnmpaclEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpaclEnum>`
            
            .. attribute:: version
            
            	SNMP version to be used. v1,v2c or v3
            	**type**\:   :py:class:`UserSnmpVersionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.UserSnmpVersionEnum>`
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.user_name = None
                self.algorithm = None
                self.authentication_password = None
                self.authentication_password_configured = None
                self.group_name = None
                self.owner = None
                self.port = None
                self.priv_algorithm = None
                self.privacy_password = None
                self.privacy_password_configured = None
                self.remote_address = None
                self.v4_access_list = None
                self.v4acl_type = None
                self.v6_access_list = None
                self.v6acl_type = None
                self.version = None

            @property
            def _common_path(self):
                if self.user_name is None:
                    raise YPYModelError('Key property user_name is None')

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:users/Cisco-IOS-XR-snmp-agent-cfg:user[Cisco-IOS-XR-snmp-agent-cfg:user-name = ' + str(self.user_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.user_name is not None:
                    return True

                if self.algorithm is not None:
                    return True

                if self.authentication_password is not None:
                    return True

                if self.authentication_password_configured is not None:
                    return True

                if self.group_name is not None:
                    return True

                if self.owner is not None:
                    return True

                if self.port is not None:
                    return True

                if self.priv_algorithm is not None:
                    return True

                if self.privacy_password is not None:
                    return True

                if self.privacy_password_configured is not None:
                    return True

                if self.remote_address is not None:
                    return True

                if self.v4_access_list is not None:
                    return True

                if self.v4acl_type is not None:
                    return True

                if self.v6_access_list is not None:
                    return True

                if self.v6acl_type is not None:
                    return True

                if self.version is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Users.User']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:users'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.user is not None:
                for child_ref in self.user:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Users']['meta_info']


    class Vrfs(object):
        """
        SNMP VRF configuration commands
        
        .. attribute:: vrf
        
        	VRF name
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
            """
            VRF name
            
            .. attribute:: name  <key>
            
            	VRF name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: context_mappings
            
            	List of context names
            	**type**\:   :py:class:`ContextMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.ContextMappings>`
            
            .. attribute:: contexts
            
            	List of Context Names
            	**type**\:   :py:class:`Contexts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.Contexts>`
            
            .. attribute:: trap_hosts
            
            	Specify hosts to receive SNMP notifications
            	**type**\:   :py:class:`TrapHosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.name = None
                self.context_mappings = Snmp.Vrfs.Vrf.ContextMappings()
                self.context_mappings.parent = self
                self.contexts = Snmp.Vrfs.Vrf.Contexts()
                self.contexts.parent = self
                self.trap_hosts = Snmp.Vrfs.Vrf.TrapHosts()
                self.trap_hosts.parent = self


            class TrapHosts(object):
                """
                Specify hosts to receive SNMP notifications
                
                .. attribute:: trap_host
                
                	Specify hosts to receive SNMP notifications
                	**type**\: list of    :py:class:`TrapHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2015-10-27'

                def __init__(self):
                    self.parent = None
                    self.trap_host = YList()
                    self.trap_host.parent = self
                    self.trap_host.name = 'trap_host'


                class TrapHost(object):
                    """
                    Specify hosts to receive SNMP notifications
                    
                    .. attribute:: ip_address  <key>
                    
                    	IP address of SNMP notification host
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: default_user_communities
                    
                    	Container class for defining communities for a trap host
                    	**type**\:   :py:class:`DefaultUserCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities>`
                    
                    .. attribute:: encrypted_user_communities
                    
                    	Container class for defining Clear/encrypt communities for a trap host
                    	**type**\:   :py:class:`EncryptedUserCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities>`
                    
                    .. attribute:: inform_host
                    
                    	Container class for defining notification type for a Inform host
                    	**type**\:   :py:class:`InformHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2015-10-27'

                    def __init__(self):
                        self.parent = None
                        self.ip_address = None
                        self.default_user_communities = Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities()
                        self.default_user_communities.parent = self
                        self.encrypted_user_communities = Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities()
                        self.encrypted_user_communities.parent = self
                        self.inform_host = Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost()
                        self.inform_host.parent = self


                    class EncryptedUserCommunities(object):
                        """
                        Container class for defining Clear/encrypt
                        communities for a trap host
                        
                        .. attribute:: encrypted_user_community
                        
                        	Clear/Encrypt Community name associated with a trap host
                        	**type**\: list of    :py:class:`EncryptedUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2015-10-27'

                        def __init__(self):
                            self.parent = None
                            self.encrypted_user_community = YList()
                            self.encrypted_user_community.parent = self
                            self.encrypted_user_community.name = 'encrypted_user_community'


                        class EncryptedUserCommunity(object):
                            """
                            Clear/Encrypt Community name associated with
                            a trap host
                            
                            .. attribute:: community_name  <key>
                            
                            	SNMPv1/v2c community string or SNMPv3 user
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: advanced_trap_types1
                            
                            	Number to signify the feature traps that needs to be setUse this for providing copy\-complete trapValue must be set to 0 if not used
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**mandatory**\: True
                            
                            .. attribute:: advanced_trap_types2
                            
                            	Number to signify the feature traps that needs to be setvalue should always to set as 0
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**mandatory**\: True
                            
                            .. attribute:: basic_trap_types
                            
                            	Number to signify the feature traps that needs to be setBasicTrapTypes is used for all traps except copy\-completeSet this value to an integer corresponding to the trapBGP 8192, CONFIG 4096,SYSLOG 131072,SNMP\_TRAP 1COPY\_COMPLETE\_TRAP 64To provide a combination of trap Add the respective numbersValue must be set to 0 for all traps
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**mandatory**\: True
                            
                            .. attribute:: port
                            
                            	UDP port number
                            	**type**\:  int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: security_level
                            
                            	Security level to be used noauth/auth/priv
                            	**type**\:   :py:class:`SnmpSecurityModelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModelEnum>`
                            
                            .. attribute:: version
                            
                            	SNMP Version to be used v1/v2c/v3
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2015-10-27'

                            def __init__(self):
                                self.parent = None
                                self.community_name = None
                                self.advanced_trap_types1 = None
                                self.advanced_trap_types2 = None
                                self.basic_trap_types = None
                                self.port = None
                                self.security_level = None
                                self.version = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.community_name is None:
                                    raise YPYModelError('Key property community_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:encrypted-user-community[Cisco-IOS-XR-snmp-agent-cfg:community-name = ' + str(self.community_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.community_name is not None:
                                    return True

                                if self.advanced_trap_types1 is not None:
                                    return True

                                if self.advanced_trap_types2 is not None:
                                    return True

                                if self.basic_trap_types is not None:
                                    return True

                                if self.port is not None:
                                    return True

                                if self.security_level is not None:
                                    return True

                                if self.version is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:encrypted-user-communities'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.encrypted_user_community is not None:
                                for child_ref in self.encrypted_user_community:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities']['meta_info']


                    class InformHost(object):
                        """
                        Container class for defining notification type
                        for a Inform host
                        
                        .. attribute:: inform_encrypted_user_communities
                        
                        	Container class for defining Clear/encrypt communities for a inform host
                        	**type**\:   :py:class:`InformEncryptedUserCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities>`
                        
                        .. attribute:: inform_user_communities
                        
                        	Container class for defining communities for a inform host
                        	**type**\:   :py:class:`InformUserCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2015-10-27'

                        def __init__(self):
                            self.parent = None
                            self.inform_encrypted_user_communities = Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities()
                            self.inform_encrypted_user_communities.parent = self
                            self.inform_user_communities = Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities()
                            self.inform_user_communities.parent = self


                        class InformUserCommunities(object):
                            """
                            Container class for defining communities for
                            a inform host
                            
                            .. attribute:: inform_user_community
                            
                            	Unencrpted Community name associated with a inform host
                            	**type**\: list of    :py:class:`InformUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity>`
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2015-10-27'

                            def __init__(self):
                                self.parent = None
                                self.inform_user_community = YList()
                                self.inform_user_community.parent = self
                                self.inform_user_community.name = 'inform_user_community'


                            class InformUserCommunity(object):
                                """
                                Unencrpted Community name associated with a
                                inform host
                                
                                .. attribute:: community_name  <key>
                                
                                	SNMPv2c community string or SNMPv3 user
                                	**type**\:  str
                                
                                	**length:** 1..128
                                
                                .. attribute:: advanced_trap_types1
                                
                                	Number to signify the feature traps that needs to be setUse this for providing copy\-complete trapValue must be set to 0 if not used
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**mandatory**\: True
                                
                                .. attribute:: advanced_trap_types2
                                
                                	Number to signify the feature traps that needs to be setvalue should always to set as 0
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**mandatory**\: True
                                
                                .. attribute:: basic_trap_types
                                
                                	Number to signify the feature traps that needs to be setBasicTrapTypes is used for all traps except copy\-completeSet this value to an integer corresponding to the trapBGP 8192, CONFIG 4096,SYSLOG 131072 ,SNMP\_TRAP 1COPY\_COMPLETE\_TRAP 64To provide a combination of trap Add the respective numbersValue must be set to 0 for all traps
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**mandatory**\: True
                                
                                .. attribute:: port
                                
                                	UDP port number
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                .. attribute:: security_level
                                
                                	Security level to be used noauth/auth/priv
                                	**type**\:   :py:class:`SnmpSecurityModelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModelEnum>`
                                
                                .. attribute:: version
                                
                                	SNMP Version to be used v2c/v3
                                	**type**\:  str
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'snmp-agent-cfg'
                                _revision = '2015-10-27'

                                def __init__(self):
                                    self.parent = None
                                    self.community_name = None
                                    self.advanced_trap_types1 = None
                                    self.advanced_trap_types2 = None
                                    self.basic_trap_types = None
                                    self.port = None
                                    self.security_level = None
                                    self.version = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.community_name is None:
                                        raise YPYModelError('Key property community_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:inform-user-community[Cisco-IOS-XR-snmp-agent-cfg:community-name = ' + str(self.community_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.community_name is not None:
                                        return True

                                    if self.advanced_trap_types1 is not None:
                                        return True

                                    if self.advanced_trap_types2 is not None:
                                        return True

                                    if self.basic_trap_types is not None:
                                        return True

                                    if self.port is not None:
                                        return True

                                    if self.security_level is not None:
                                        return True

                                    if self.version is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                    return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:inform-user-communities'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.inform_user_community is not None:
                                    for child_ref in self.inform_user_community:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities']['meta_info']


                        class InformEncryptedUserCommunities(object):
                            """
                            Container class for defining Clear/encrypt
                            communities for a inform host
                            
                            .. attribute:: inform_encrypted_user_community
                            
                            	Clear/Encrypt Community name associated with a inform host
                            	**type**\: list of    :py:class:`InformEncryptedUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity>`
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2015-10-27'

                            def __init__(self):
                                self.parent = None
                                self.inform_encrypted_user_community = YList()
                                self.inform_encrypted_user_community.parent = self
                                self.inform_encrypted_user_community.name = 'inform_encrypted_user_community'


                            class InformEncryptedUserCommunity(object):
                                """
                                Clear/Encrypt Community name associated with
                                a inform host
                                
                                .. attribute:: community_name  <key>
                                
                                	SNMPv2c community string or SNMPv3 user
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: advanced_trap_types1
                                
                                	Number to signify the feature traps that needs to be setUse this for providing copy\-complete trapValue must be set to 0 if not used
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**mandatory**\: True
                                
                                .. attribute:: advanced_trap_types2
                                
                                	Number to signify the feature traps that needs to be setvalue should always to set as 0
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**mandatory**\: True
                                
                                .. attribute:: basic_trap_types
                                
                                	Number to signify the feature traps that needs to be setBasicTrapTypes is used for all traps except copy\-completeSet this value to an integer corresponding to the trapBGP 8192, CONFIG 4096,SYSLOG 131072 ,SNMP\_TRAP 1COPY\_COMPLETE\_TRAP 64To provide a combination of trap Add the respective numbersValue must be set to 0 for all traps
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**mandatory**\: True
                                
                                .. attribute:: port
                                
                                	UDP port number
                                	**type**\:  int
                                
                                	**range:** 1..65535
                                
                                .. attribute:: security_level
                                
                                	Security level to be used noauth/auth/priv
                                	**type**\:   :py:class:`SnmpSecurityModelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModelEnum>`
                                
                                .. attribute:: version
                                
                                	SNMP Version to be used v2c/v3
                                	**type**\:  str
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'snmp-agent-cfg'
                                _revision = '2015-10-27'

                                def __init__(self):
                                    self.parent = None
                                    self.community_name = None
                                    self.advanced_trap_types1 = None
                                    self.advanced_trap_types2 = None
                                    self.basic_trap_types = None
                                    self.port = None
                                    self.security_level = None
                                    self.version = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.community_name is None:
                                        raise YPYModelError('Key property community_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:inform-encrypted-user-community[Cisco-IOS-XR-snmp-agent-cfg:community-name = ' + str(self.community_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.community_name is not None:
                                        return True

                                    if self.advanced_trap_types1 is not None:
                                        return True

                                    if self.advanced_trap_types2 is not None:
                                        return True

                                    if self.basic_trap_types is not None:
                                        return True

                                    if self.port is not None:
                                        return True

                                    if self.security_level is not None:
                                        return True

                                    if self.version is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                    return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:inform-encrypted-user-communities'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.inform_encrypted_user_community is not None:
                                    for child_ref in self.inform_encrypted_user_community:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:inform-host'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.inform_encrypted_user_communities is not None and self.inform_encrypted_user_communities._has_data():
                                return True

                            if self.inform_user_communities is not None and self.inform_user_communities._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost']['meta_info']


                    class DefaultUserCommunities(object):
                        """
                        Container class for defining communities for a
                        trap host
                        
                        .. attribute:: default_user_community
                        
                        	Unencrpted Community name associated with a trap host
                        	**type**\: list of    :py:class:`DefaultUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2015-10-27'

                        def __init__(self):
                            self.parent = None
                            self.default_user_community = YList()
                            self.default_user_community.parent = self
                            self.default_user_community.name = 'default_user_community'


                        class DefaultUserCommunity(object):
                            """
                            Unencrpted Community name associated with a
                            trap host
                            
                            .. attribute:: community_name  <key>
                            
                            	SNMPv1/v2c community string or SNMPv3 user
                            	**type**\:  str
                            
                            	**length:** 1..128
                            
                            .. attribute:: advanced_trap_types1
                            
                            	Number to signify the feature traps that needs to be setUse this for providing copy\-complete trapValue must be set to 0 if not used
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**mandatory**\: True
                            
                            .. attribute:: advanced_trap_types2
                            
                            	Number to signify the feature traps that needs to be setvalue should always to set as 0
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**mandatory**\: True
                            
                            .. attribute:: basic_trap_types
                            
                            	Number to signify the feature traps that needs to be setBasicTrapTypes is used for all traps except copy\-completeSet this value to an integer corresponding to the trapBGP 8192, CONFIG 4096,SYSLOG 131072,SNMP\_TRAP 1COPY\_COMPLETE\_TRAP 64To provide a combination of trap Add the respective numbersValue must be set to 0 for all traps
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**mandatory**\: True
                            
                            .. attribute:: port
                            
                            	UDP port number
                            	**type**\:  int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: security_level
                            
                            	Security level to be used noauth/auth/priv
                            	**type**\:   :py:class:`SnmpSecurityModelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModelEnum>`
                            
                            .. attribute:: version
                            
                            	SNMP Version to be used v1/v2c/v3
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2015-10-27'

                            def __init__(self):
                                self.parent = None
                                self.community_name = None
                                self.advanced_trap_types1 = None
                                self.advanced_trap_types2 = None
                                self.basic_trap_types = None
                                self.port = None
                                self.security_level = None
                                self.version = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.community_name is None:
                                    raise YPYModelError('Key property community_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:default-user-community[Cisco-IOS-XR-snmp-agent-cfg:community-name = ' + str(self.community_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.community_name is not None:
                                    return True

                                if self.advanced_trap_types1 is not None:
                                    return True

                                if self.advanced_trap_types2 is not None:
                                    return True

                                if self.basic_trap_types is not None:
                                    return True

                                if self.port is not None:
                                    return True

                                if self.security_level is not None:
                                    return True

                                if self.version is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:default-user-communities'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.default_user_community is not None:
                                for child_ref in self.default_user_community:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.ip_address is None:
                            raise YPYModelError('Key property ip_address is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:trap-host[Cisco-IOS-XR-snmp-agent-cfg:ip-address = ' + str(self.ip_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ip_address is not None:
                            return True

                        if self.default_user_communities is not None and self.default_user_communities._has_data():
                            return True

                        if self.encrypted_user_communities is not None and self.encrypted_user_communities._has_data():
                            return True

                        if self.inform_host is not None and self.inform_host._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:trap-hosts'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.trap_host is not None:
                        for child_ref in self.trap_host:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts']['meta_info']


            class Contexts(object):
                """
                List of Context Names
                
                .. attribute:: context
                
                	Context Name
                	**type**\: list of    :py:class:`Context <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.Contexts.Context>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2015-10-27'

                def __init__(self):
                    self.parent = None
                    self.context = YList()
                    self.context.parent = self
                    self.context.name = 'context'


                class Context(object):
                    """
                    Context Name
                    
                    .. attribute:: context_name  <key>
                    
                    	Context Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2015-10-27'

                    def __init__(self):
                        self.parent = None
                        self.context_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.context_name is None:
                            raise YPYModelError('Key property context_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:context[Cisco-IOS-XR-snmp-agent-cfg:context-name = ' + str(self.context_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.context_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Vrfs.Vrf.Contexts.Context']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:contexts'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.context is not None:
                        for child_ref in self.context:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Vrfs.Vrf.Contexts']['meta_info']


            class ContextMappings(object):
                """
                List of context names
                
                .. attribute:: context_mapping
                
                	Context mapping name
                	**type**\: list of    :py:class:`ContextMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.ContextMappings.ContextMapping>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2015-10-27'

                def __init__(self):
                    self.parent = None
                    self.context_mapping = YList()
                    self.context_mapping.parent = self
                    self.context_mapping.name = 'context_mapping'


                class ContextMapping(object):
                    """
                    Context mapping name
                    
                    .. attribute:: context_mapping_name  <key>
                    
                    	Context mapping name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: context
                    
                    	SNMP context feature type
                    	**type**\:   :py:class:`SnmpContextEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpContextEnum>`
                    
                    .. attribute:: instance_name
                    
                    	OSPF protocol instance
                    	**type**\:  str
                    
                    .. attribute:: topology_name
                    
                    	Topology name associated with the context
                    	**type**\:  str
                    
                    .. attribute:: vrf_name
                    
                    	VRF name associated with the context
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2015-10-27'

                    def __init__(self):
                        self.parent = None
                        self.context_mapping_name = None
                        self.context = None
                        self.instance_name = None
                        self.topology_name = None
                        self.vrf_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.context_mapping_name is None:
                            raise YPYModelError('Key property context_mapping_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:context-mapping[Cisco-IOS-XR-snmp-agent-cfg:context-mapping-name = ' + str(self.context_mapping_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.context_mapping_name is not None:
                            return True

                        if self.context is not None:
                            return True

                        if self.instance_name is not None:
                            return True

                        if self.topology_name is not None:
                            return True

                        if self.vrf_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Vrfs.Vrf.ContextMappings.ContextMapping']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:context-mappings'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.context_mapping is not None:
                        for child_ref in self.context_mapping:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Vrfs.Vrf.ContextMappings']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:vrfs/Cisco-IOS-XR-snmp-agent-cfg:vrf[Cisco-IOS-XR-snmp-agent-cfg:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.context_mappings is not None and self.context_mappings._has_data():
                    return True

                if self.contexts is not None and self.contexts._has_data():
                    return True

                if self.trap_hosts is not None and self.trap_hosts._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:vrfs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.vrf is not None:
                for child_ref in self.vrf:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Vrfs']['meta_info']


    class Groups(object):
        """
        Define a User Security Model group
        
        .. attribute:: group
        
        	Name of the group
        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Groups.Group>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.group = YList()
            self.group.parent = self
            self.group.name = 'group'


        class Group(object):
            """
            Name of the group
            
            .. attribute:: name  <key>
            
            	Name of the group
            	**type**\:  str
            
            	**length:** 1..128
            
            .. attribute:: context_name
            
            	Context name
            	**type**\:  str
            
            .. attribute:: notify_view
            
            	notify view name
            	**type**\:  str
            
            .. attribute:: read_view
            
            	read view name
            	**type**\:  str
            
            .. attribute:: security_model
            
            	security model like auth/noAuth/Priv applicable for v3
            	**type**\:   :py:class:`SnmpSecurityModelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModelEnum>`
            
            .. attribute:: snmp_version
            
            	snmp version
            	**type**\:   :py:class:`GroupSnmpVersionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.GroupSnmpVersionEnum>`
            
            	**mandatory**\: True
            
            .. attribute:: v4_access_list
            
            	Ipv4 Access\-list name
            	**type**\:  str
            
            .. attribute:: v4acl_type
            
            	Access\-list type
            	**type**\:   :py:class:`SnmpaclEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpaclEnum>`
            
            .. attribute:: v6_access_list
            
            	Ipv6 Access\-list name
            	**type**\:  str
            
            .. attribute:: v6acl_type
            
            	Access\-list type
            	**type**\:   :py:class:`SnmpaclEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpaclEnum>`
            
            .. attribute:: write_view
            
            	write view name
            	**type**\:  str
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.name = None
                self.context_name = None
                self.notify_view = None
                self.read_view = None
                self.security_model = None
                self.snmp_version = None
                self.v4_access_list = None
                self.v4acl_type = None
                self.v6_access_list = None
                self.v6acl_type = None
                self.write_view = None

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:groups/Cisco-IOS-XR-snmp-agent-cfg:group[Cisco-IOS-XR-snmp-agent-cfg:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.context_name is not None:
                    return True

                if self.notify_view is not None:
                    return True

                if self.read_view is not None:
                    return True

                if self.security_model is not None:
                    return True

                if self.snmp_version is not None:
                    return True

                if self.v4_access_list is not None:
                    return True

                if self.v4acl_type is not None:
                    return True

                if self.v6_access_list is not None:
                    return True

                if self.v6acl_type is not None:
                    return True

                if self.write_view is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Groups.Group']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:groups'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.group is not None:
                for child_ref in self.group:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Groups']['meta_info']


    class TrapHosts(object):
        """
        Specify hosts to receive SNMP notifications
        
        .. attribute:: trap_host
        
        	Specify hosts to receive SNMP notifications
        	**type**\: list of    :py:class:`TrapHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.trap_host = YList()
            self.trap_host.parent = self
            self.trap_host.name = 'trap_host'


        class TrapHost(object):
            """
            Specify hosts to receive SNMP notifications
            
            .. attribute:: ip_address  <key>
            
            	IP address of SNMP notification host
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: default_user_communities
            
            	Container class for defining communities for a trap host
            	**type**\:   :py:class:`DefaultUserCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.DefaultUserCommunities>`
            
            .. attribute:: encrypted_user_communities
            
            	Container class for defining Clear/encrypt communities for a trap host
            	**type**\:   :py:class:`EncryptedUserCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.EncryptedUserCommunities>`
            
            .. attribute:: inform_host
            
            	Container class for defining notification type for a Inform host
            	**type**\:   :py:class:`InformHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.InformHost>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.ip_address = None
                self.default_user_communities = Snmp.TrapHosts.TrapHost.DefaultUserCommunities()
                self.default_user_communities.parent = self
                self.encrypted_user_communities = Snmp.TrapHosts.TrapHost.EncryptedUserCommunities()
                self.encrypted_user_communities.parent = self
                self.inform_host = Snmp.TrapHosts.TrapHost.InformHost()
                self.inform_host.parent = self


            class EncryptedUserCommunities(object):
                """
                Container class for defining Clear/encrypt
                communities for a trap host
                
                .. attribute:: encrypted_user_community
                
                	Clear/Encrypt Community name associated with a trap host
                	**type**\: list of    :py:class:`EncryptedUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2015-10-27'

                def __init__(self):
                    self.parent = None
                    self.encrypted_user_community = YList()
                    self.encrypted_user_community.parent = self
                    self.encrypted_user_community.name = 'encrypted_user_community'


                class EncryptedUserCommunity(object):
                    """
                    Clear/Encrypt Community name associated with
                    a trap host
                    
                    .. attribute:: community_name  <key>
                    
                    	SNMPv1/v2c community string or SNMPv3 user
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: advanced_trap_types1
                    
                    	Number to signify the feature traps that needs to be setUse this for providing copy\-complete trapValue must be set to 0 if not used
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**mandatory**\: True
                    
                    .. attribute:: advanced_trap_types2
                    
                    	Number to signify the feature traps that needs to be setvalue should always to set as 0
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**mandatory**\: True
                    
                    .. attribute:: basic_trap_types
                    
                    	Number to signify the feature traps that needs to be setBasicTrapTypes is used for all traps except copy\-completeSet this value to an integer corresponding to the trapBGP 8192, CONFIG 4096,SYSLOG 131072,SNMP\_TRAP 1COPY\_COMPLETE\_TRAP 64To provide a combination of trap Add the respective numbersValue must be set to 0 for all traps
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**mandatory**\: True
                    
                    .. attribute:: port
                    
                    	UDP port number
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: security_level
                    
                    	Security level to be used noauth/auth/priv
                    	**type**\:   :py:class:`SnmpSecurityModelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModelEnum>`
                    
                    .. attribute:: version
                    
                    	SNMP Version to be used v1/v2c/v3
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2015-10-27'

                    def __init__(self):
                        self.parent = None
                        self.community_name = None
                        self.advanced_trap_types1 = None
                        self.advanced_trap_types2 = None
                        self.basic_trap_types = None
                        self.port = None
                        self.security_level = None
                        self.version = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.community_name is None:
                            raise YPYModelError('Key property community_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:encrypted-user-community[Cisco-IOS-XR-snmp-agent-cfg:community-name = ' + str(self.community_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.community_name is not None:
                            return True

                        if self.advanced_trap_types1 is not None:
                            return True

                        if self.advanced_trap_types2 is not None:
                            return True

                        if self.basic_trap_types is not None:
                            return True

                        if self.port is not None:
                            return True

                        if self.security_level is not None:
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:encrypted-user-communities'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.encrypted_user_community is not None:
                        for child_ref in self.encrypted_user_community:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.TrapHosts.TrapHost.EncryptedUserCommunities']['meta_info']


            class InformHost(object):
                """
                Container class for defining notification type
                for a Inform host
                
                .. attribute:: inform_encrypted_user_communities
                
                	Container class for defining Clear/encrypt communities for a inform host
                	**type**\:   :py:class:`InformEncryptedUserCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities>`
                
                .. attribute:: inform_user_communities
                
                	Container class for defining communities for a inform host
                	**type**\:   :py:class:`InformUserCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2015-10-27'

                def __init__(self):
                    self.parent = None
                    self.inform_encrypted_user_communities = Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities()
                    self.inform_encrypted_user_communities.parent = self
                    self.inform_user_communities = Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities()
                    self.inform_user_communities.parent = self


                class InformUserCommunities(object):
                    """
                    Container class for defining communities for
                    a inform host
                    
                    .. attribute:: inform_user_community
                    
                    	Unencrpted Community name associated with a inform host
                    	**type**\: list of    :py:class:`InformUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2015-10-27'

                    def __init__(self):
                        self.parent = None
                        self.inform_user_community = YList()
                        self.inform_user_community.parent = self
                        self.inform_user_community.name = 'inform_user_community'


                    class InformUserCommunity(object):
                        """
                        Unencrpted Community name associated with a
                        inform host
                        
                        .. attribute:: community_name  <key>
                        
                        	SNMPv2c community string or SNMPv3 user
                        	**type**\:  str
                        
                        	**length:** 1..128
                        
                        .. attribute:: advanced_trap_types1
                        
                        	Number to signify the feature traps that needs to be setUse this for providing copy\-complete trapValue must be set to 0 if not used
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**mandatory**\: True
                        
                        .. attribute:: advanced_trap_types2
                        
                        	Number to signify the feature traps that needs to be setvalue should always to set as 0
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**mandatory**\: True
                        
                        .. attribute:: basic_trap_types
                        
                        	Number to signify the feature traps that needs to be setBasicTrapTypes is used for all traps except copy\-completeSet this value to an integer corresponding to the trapBGP 8192, CONFIG 4096,SYSLOG 131072 ,SNMP\_TRAP 1COPY\_COMPLETE\_TRAP 64To provide a combination of trap Add the respective numbersValue must be set to 0 for all traps
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**mandatory**\: True
                        
                        .. attribute:: port
                        
                        	UDP port number
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: security_level
                        
                        	Security level to be used noauth/auth/priv
                        	**type**\:   :py:class:`SnmpSecurityModelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModelEnum>`
                        
                        .. attribute:: version
                        
                        	SNMP Version to be used v2c/v3
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2015-10-27'

                        def __init__(self):
                            self.parent = None
                            self.community_name = None
                            self.advanced_trap_types1 = None
                            self.advanced_trap_types2 = None
                            self.basic_trap_types = None
                            self.port = None
                            self.security_level = None
                            self.version = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.community_name is None:
                                raise YPYModelError('Key property community_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:inform-user-community[Cisco-IOS-XR-snmp-agent-cfg:community-name = ' + str(self.community_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.community_name is not None:
                                return True

                            if self.advanced_trap_types1 is not None:
                                return True

                            if self.advanced_trap_types2 is not None:
                                return True

                            if self.basic_trap_types is not None:
                                return True

                            if self.port is not None:
                                return True

                            if self.security_level is not None:
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:inform-user-communities'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.inform_user_community is not None:
                            for child_ref in self.inform_user_community:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities']['meta_info']


                class InformEncryptedUserCommunities(object):
                    """
                    Container class for defining Clear/encrypt
                    communities for a inform host
                    
                    .. attribute:: inform_encrypted_user_community
                    
                    	Clear/Encrypt Community name associated with a inform host
                    	**type**\: list of    :py:class:`InformEncryptedUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2015-10-27'

                    def __init__(self):
                        self.parent = None
                        self.inform_encrypted_user_community = YList()
                        self.inform_encrypted_user_community.parent = self
                        self.inform_encrypted_user_community.name = 'inform_encrypted_user_community'


                    class InformEncryptedUserCommunity(object):
                        """
                        Clear/Encrypt Community name associated with
                        a inform host
                        
                        .. attribute:: community_name  <key>
                        
                        	SNMPv2c community string or SNMPv3 user
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: advanced_trap_types1
                        
                        	Number to signify the feature traps that needs to be setUse this for providing copy\-complete trapValue must be set to 0 if not used
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**mandatory**\: True
                        
                        .. attribute:: advanced_trap_types2
                        
                        	Number to signify the feature traps that needs to be setvalue should always to set as 0
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**mandatory**\: True
                        
                        .. attribute:: basic_trap_types
                        
                        	Number to signify the feature traps that needs to be setBasicTrapTypes is used for all traps except copy\-completeSet this value to an integer corresponding to the trapBGP 8192, CONFIG 4096,SYSLOG 131072 ,SNMP\_TRAP 1COPY\_COMPLETE\_TRAP 64To provide a combination of trap Add the respective numbersValue must be set to 0 for all traps
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**mandatory**\: True
                        
                        .. attribute:: port
                        
                        	UDP port number
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: security_level
                        
                        	Security level to be used noauth/auth/priv
                        	**type**\:   :py:class:`SnmpSecurityModelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModelEnum>`
                        
                        .. attribute:: version
                        
                        	SNMP Version to be used v2c/v3
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2015-10-27'

                        def __init__(self):
                            self.parent = None
                            self.community_name = None
                            self.advanced_trap_types1 = None
                            self.advanced_trap_types2 = None
                            self.basic_trap_types = None
                            self.port = None
                            self.security_level = None
                            self.version = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.community_name is None:
                                raise YPYModelError('Key property community_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:inform-encrypted-user-community[Cisco-IOS-XR-snmp-agent-cfg:community-name = ' + str(self.community_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.community_name is not None:
                                return True

                            if self.advanced_trap_types1 is not None:
                                return True

                            if self.advanced_trap_types2 is not None:
                                return True

                            if self.basic_trap_types is not None:
                                return True

                            if self.port is not None:
                                return True

                            if self.security_level is not None:
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:inform-encrypted-user-communities'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.inform_encrypted_user_community is not None:
                            for child_ref in self.inform_encrypted_user_community:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:inform-host'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.inform_encrypted_user_communities is not None and self.inform_encrypted_user_communities._has_data():
                        return True

                    if self.inform_user_communities is not None and self.inform_user_communities._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.TrapHosts.TrapHost.InformHost']['meta_info']


            class DefaultUserCommunities(object):
                """
                Container class for defining communities for a
                trap host
                
                .. attribute:: default_user_community
                
                	Unencrpted Community name associated with a trap host
                	**type**\: list of    :py:class:`DefaultUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2015-10-27'

                def __init__(self):
                    self.parent = None
                    self.default_user_community = YList()
                    self.default_user_community.parent = self
                    self.default_user_community.name = 'default_user_community'


                class DefaultUserCommunity(object):
                    """
                    Unencrpted Community name associated with a
                    trap host
                    
                    .. attribute:: community_name  <key>
                    
                    	SNMPv1/v2c community string or SNMPv3 user
                    	**type**\:  str
                    
                    	**length:** 1..128
                    
                    .. attribute:: advanced_trap_types1
                    
                    	Number to signify the feature traps that needs to be setUse this for providing copy\-complete trapValue must be set to 0 if not used
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**mandatory**\: True
                    
                    .. attribute:: advanced_trap_types2
                    
                    	Number to signify the feature traps that needs to be setvalue should always to set as 0
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**mandatory**\: True
                    
                    .. attribute:: basic_trap_types
                    
                    	Number to signify the feature traps that needs to be setBasicTrapTypes is used for all traps except copy\-completeSet this value to an integer corresponding to the trapBGP 8192, CONFIG 4096,SYSLOG 131072,SNMP\_TRAP 1COPY\_COMPLETE\_TRAP 64To provide a combination of trap Add the respective numbersValue must be set to 0 for all traps
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**mandatory**\: True
                    
                    .. attribute:: port
                    
                    	UDP port number
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: security_level
                    
                    	Security level to be used noauth/auth/priv
                    	**type**\:   :py:class:`SnmpSecurityModelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModelEnum>`
                    
                    .. attribute:: version
                    
                    	SNMP Version to be used v1/v2c/v3
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2015-10-27'

                    def __init__(self):
                        self.parent = None
                        self.community_name = None
                        self.advanced_trap_types1 = None
                        self.advanced_trap_types2 = None
                        self.basic_trap_types = None
                        self.port = None
                        self.security_level = None
                        self.version = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.community_name is None:
                            raise YPYModelError('Key property community_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:default-user-community[Cisco-IOS-XR-snmp-agent-cfg:community-name = ' + str(self.community_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.community_name is not None:
                            return True

                        if self.advanced_trap_types1 is not None:
                            return True

                        if self.advanced_trap_types2 is not None:
                            return True

                        if self.basic_trap_types is not None:
                            return True

                        if self.port is not None:
                            return True

                        if self.security_level is not None:
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-snmp-agent-cfg:default-user-communities'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.default_user_community is not None:
                        for child_ref in self.default_user_community:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.TrapHosts.TrapHost.DefaultUserCommunities']['meta_info']

            @property
            def _common_path(self):
                if self.ip_address is None:
                    raise YPYModelError('Key property ip_address is None')

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:trap-hosts/Cisco-IOS-XR-snmp-agent-cfg:trap-host[Cisco-IOS-XR-snmp-agent-cfg:ip-address = ' + str(self.ip_address) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ip_address is not None:
                    return True

                if self.default_user_communities is not None and self.default_user_communities._has_data():
                    return True

                if self.encrypted_user_communities is not None and self.encrypted_user_communities._has_data():
                    return True

                if self.inform_host is not None and self.inform_host._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.TrapHosts.TrapHost']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:trap-hosts'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.trap_host is not None:
                for child_ref in self.trap_host:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.TrapHosts']['meta_info']


    class Contexts(object):
        """
        List of Context Names
        
        .. attribute:: context
        
        	Context Name
        	**type**\: list of    :py:class:`Context <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Contexts.Context>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.context = YList()
            self.context.parent = self
            self.context.name = 'context'


        class Context(object):
            """
            Context Name
            
            .. attribute:: context_name  <key>
            
            	Context Name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.context_name = None

            @property
            def _common_path(self):
                if self.context_name is None:
                    raise YPYModelError('Key property context_name is None')

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:contexts/Cisco-IOS-XR-snmp-agent-cfg:context[Cisco-IOS-XR-snmp-agent-cfg:context-name = ' + str(self.context_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.context_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Contexts.Context']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:contexts'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.context is not None:
                for child_ref in self.context:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Contexts']['meta_info']


    class ContextMappings(object):
        """
        List of context names
        
        .. attribute:: context_mapping
        
        	Context mapping name
        	**type**\: list of    :py:class:`ContextMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.ContextMappings.ContextMapping>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2015-10-27'

        def __init__(self):
            self.parent = None
            self.context_mapping = YList()
            self.context_mapping.parent = self
            self.context_mapping.name = 'context_mapping'


        class ContextMapping(object):
            """
            Context mapping name
            
            .. attribute:: context_mapping_name  <key>
            
            	Context mapping name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: context
            
            	SNMP context feature type
            	**type**\:   :py:class:`SnmpContextEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpContextEnum>`
            
            .. attribute:: instance_name
            
            	OSPF protocol instance
            	**type**\:  str
            
            .. attribute:: topology_name
            
            	Topology name associated with the context
            	**type**\:  str
            
            .. attribute:: vrf_name
            
            	VRF name associated with the context
            	**type**\:  str
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2015-10-27'

            def __init__(self):
                self.parent = None
                self.context_mapping_name = None
                self.context = None
                self.instance_name = None
                self.topology_name = None
                self.vrf_name = None

            @property
            def _common_path(self):
                if self.context_mapping_name is None:
                    raise YPYModelError('Key property context_mapping_name is None')

                return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:context-mappings/Cisco-IOS-XR-snmp-agent-cfg:context-mapping[Cisco-IOS-XR-snmp-agent-cfg:context-mapping-name = ' + str(self.context_mapping_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.context_mapping_name is not None:
                    return True

                if self.context is not None:
                    return True

                if self.instance_name is not None:
                    return True

                if self.topology_name is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.ContextMappings.ContextMapping']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:snmp/Cisco-IOS-XR-snmp-agent-cfg:context-mappings'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.context_mapping is not None:
                for child_ref in self.context_mapping:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.ContextMappings']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-agent-cfg:snmp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.administration is not None and self.administration._has_data():
            return True

        if self.agent is not None and self.agent._has_data():
            return True

        if self.bulk_stats is not None and self.bulk_stats._has_data():
            return True

        if self.context_mappings is not None and self.context_mappings._has_data():
            return True

        if self.contexts is not None and self.contexts._has_data():
            return True

        if self.correlator is not None and self.correlator._has_data():
            return True

        if self.default_community_maps is not None and self.default_community_maps._has_data():
            return True

        if self.encrypted_community_maps is not None and self.encrypted_community_maps._has_data():
            return True

        if self.groups is not None and self.groups._has_data():
            return True

        if self.inform_pending is not None:
            return True

        if self.inform_retries is not None:
            return True

        if self.inform_timeout is not None:
            return True

        if self.ipv4 is not None and self.ipv4._has_data():
            return True

        if self.ipv6 is not None and self.ipv6._has_data():
            return True

        if self.logging is not None and self.logging._has_data():
            return True

        if self.notification is not None and self.notification._has_data():
            return True

        if self.oid_poll_stats is not None:
            return True

        if self.overload_control is not None and self.overload_control._has_data():
            return True

        if self.packet_size is not None:
            return True

        if self.system is not None and self.system._has_data():
            return True

        if self.target is not None and self.target._has_data():
            return True

        if self.throttle_time is not None:
            return True

        if self.timeouts is not None and self.timeouts._has_data():
            return True

        if self.trap is not None and self.trap._has_data():
            return True

        if self.trap_hosts is not None and self.trap_hosts._has_data():
            return True

        if self.trap_port is not None:
            return True

        if self.trap_source is not None:
            return True

        if self.trap_source_ipv4 is not None:
            return True

        if self.trap_source_ipv6 is not None:
            return True

        if self.users is not None and self.users._has_data():
            return True

        if self.views is not None and self.views._has_data():
            return True

        if self.vrf_authentication_trap_disable is not None:
            return True

        if self.vrfs is not None and self.vrfs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['Snmp']['meta_info']


class Mib(object):
    """
    mib
    
    .. attribute:: cb_qosmib
    
    	CBQoSMIB configuration
    	**type**\:   :py:class:`CbQosmib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.CbQosmib>`
    
    .. attribute:: entity_mib
    
    	Entity MIB
    	**type**\:   :py:class:`EntityMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.EntityMib>`
    
    .. attribute:: interface_mib
    
    	Interface MIB configuration
    	**type**\:   :py:class:`InterfaceMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.InterfaceMib>`
    
    .. attribute:: mpls_frr_mib
    
    	FRR MIB configuration
    	**type**\:   :py:class:`MplsFrrMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.MplsFrrMib>`
    
    .. attribute:: mpls_p2mp_mib
    
    	MPLS P2MP MIB configuration
    	**type**\:   :py:class:`MplsP2MpMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.MplsP2MpMib>`
    
    .. attribute:: mpls_te_ext_mib
    
    	MPLS TE EXT MIB configuration
    	**type**\:   :py:class:`MplsTeExtMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.MplsTeExtMib>`
    
    .. attribute:: mpls_te_ext_std_mib
    
    	MPLS TE EXT STD MIB configuration
    	**type**\:   :py:class:`MplsTeExtStdMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.MplsTeExtStdMib>`
    
    .. attribute:: mpls_te_mib
    
    	MPLS TE MIB configuration
    	**type**\:   :py:class:`MplsTeMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.MplsTeMib>`
    
    .. attribute:: sensor_mib_cache
    
    	Get cached Sesnsor MIB statistics
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'snmp-agent-cfg'
    _revision = '2015-10-27'

    def __init__(self):
        self.cb_qosmib = Mib.CbQosmib()
        self.cb_qosmib.parent = self
        self.entity_mib = Mib.EntityMib()
        self.entity_mib.parent = self
        self.interface_mib = Mib.InterfaceMib()
        self.interface_mib.parent = self
        self.mpls_frr_mib = Mib.MplsFrrMib()
        self.mpls_frr_mib.parent = self
        self.mpls_p2mp_mib = Mib.MplsP2MpMib()
        self.mpls_p2mp_mib.parent = self
        self.mpls_te_ext_mib = Mib.MplsTeExtMib()
        self.mpls_te_ext_mib.parent = self
        self.mpls_te_ext_std_mib = Mib.MplsTeExtStdMib()
        self.mpls_te_ext_std_mib.parent = self
        self.mpls_te_mib = Mib.MplsTeMib()
        self.mpls_te_mib.parent = self
        self.sensor_mib_cache = None


    class MplsTeMib(object):
        """
        MPLS TE MIB configuration
        
        .. attribute:: cache_garbage_collect_timer
        
        	Configure the cache garbage collector time for the mib
        	**type**\:  int
        
        	**range:** 0..3600
        
        	**units**\: second
        
        	**default value**\: 1800
        
        .. attribute:: cache_timer
        
        	Configure the cache time for the mib
        	**type**\:  int
        
        	**range:** 0..600
        
        	**units**\: second
        
        	**default value**\: 60
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.cache_garbage_collect_timer = None
            self.cache_timer = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-mpls-te-cfg:mpls-te-mib'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.cache_garbage_collect_timer is not None:
                return True

            if self.cache_timer is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.MplsTeMib']['meta_info']


    class MplsP2MpMib(object):
        """
        MPLS P2MP MIB configuration
        
        .. attribute:: cache_timer
        
        	Configure the cache time for the mib
        	**type**\:  int
        
        	**range:** 0..600
        
        	**units**\: second
        
        	**default value**\: 60
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.cache_timer = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-mpls-te-cfg:mpls-p2mp-mib'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.cache_timer is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.MplsP2MpMib']['meta_info']


    class MplsTeExtStdMib(object):
        """
        MPLS TE EXT STD MIB configuration
        
        .. attribute:: cache_timer
        
        	Configure the cache time for the mib
        	**type**\:  int
        
        	**range:** 0..600
        
        	**units**\: second
        
        	**default value**\: 60
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.cache_timer = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-mpls-te-cfg:mpls-te-ext-std-mib'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.cache_timer is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.MplsTeExtStdMib']['meta_info']


    class MplsTeExtMib(object):
        """
        MPLS TE EXT MIB configuration
        
        .. attribute:: cache_timer
        
        	Configure the cache time for the mib
        	**type**\:  int
        
        	**range:** 0..600
        
        	**units**\: second
        
        	**default value**\: 60
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.cache_timer = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-mpls-te-cfg:mpls-te-ext-mib'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.cache_timer is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.MplsTeExtMib']['meta_info']


    class MplsFrrMib(object):
        """
        FRR MIB configuration
        
        .. attribute:: cache_timer
        
        	Configure the cache time for the mib
        	**type**\:  int
        
        	**range:** 0..600
        
        	**units**\: second
        
        	**default value**\: 60
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.cache_timer = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-mpls-te-cfg:mpls-frr-mib'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.cache_timer is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.MplsFrrMib']['meta_info']


    class CbQosmib(object):
        """
        CBQoSMIB configuration
        
        .. attribute:: cache
        
        	CBQoSMIB statistics data caching
        	**type**\:   :py:class:`Cache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.CbQosmib.Cache>`
        
        .. attribute:: member_interface_stats
        
        	Enable bundle member interface statistics retrieval
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: persist
        
        	Persist CBQoSMIB config, service\-policy and object indices
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'qos-mibs-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.cache = Mib.CbQosmib.Cache()
            self.cache.parent = self
            self.member_interface_stats = None
            self.persist = None


        class Cache(object):
            """
            CBQoSMIB statistics data caching
            
            .. attribute:: enable
            
            	Enable CBQoSMIB statistics data caching
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: refresh_time
            
            	Cache refresh time in seconds
            	**type**\:  int
            
            	**range:** 5..60
            
            	**units**\: second
            
            .. attribute:: service_policy_count
            
            	Maximum number of service policies to cache the statistics for
            	**type**\:  int
            
            	**range:** 1..5000
            
            

            """

            _prefix = 'qos-mibs-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.refresh_time = None
                self.service_policy_count = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-qos-mibs-cfg:cb-qosmib/Cisco-IOS-XR-qos-mibs-cfg:cache'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.refresh_time is not None:
                    return True

                if self.service_policy_count is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Mib.CbQosmib.Cache']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-qos-mibs-cfg:cb-qosmib'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.cache is not None and self.cache._has_data():
                return True

            if self.member_interface_stats is not None:
                return True

            if self.persist is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.CbQosmib']['meta_info']


    class EntityMib(object):
        """
        Entity MIB
        
        .. attribute:: entity_index_persistence
        
        	Enable entPhysicalIndex persistence
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'snmp-entitymib-cfg'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.entity_index_persistence = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-snmp-entitymib-cfg:entity-mib'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.entity_index_persistence is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.EntityMib']['meta_info']


    class InterfaceMib(object):
        """
        Interface MIB configuration
        
        .. attribute:: interface_alias_long
        
        	Enable support for ifAlias values longer than 64 characters
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: interface_index_persistence
        
        	Enable ifindex persistence
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: interfaces
        
        	Enter the SNMP interface configuration commands
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.InterfaceMib.Interfaces>`
        
        .. attribute:: internal_cache
        
        	Get cached interface statistics
        	**type**\:  int
        
        	**range:** 0..60
        
        	**default value**\: 15
        
        .. attribute:: ip_subscriber
        
        	Enable IP subscriber interfaces in IFMIB
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: notification
        
        	MIB notification configuration
        	**type**\:   :py:class:`Notification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.InterfaceMib.Notification>`
        
        .. attribute:: statistics_cache
        
        	Enable cached interface statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: subsets
        
        	Add configuration for an interface subset
        	**type**\:   :py:class:`Subsets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.InterfaceMib.Subsets>`
        
        

        """

        _prefix = 'snmp-ifmib-cfg'
        _revision = '2015-05-14'

        def __init__(self):
            self.parent = None
            self.interface_alias_long = None
            self.interface_index_persistence = None
            self.interfaces = Mib.InterfaceMib.Interfaces()
            self.interfaces.parent = self
            self.internal_cache = None
            self.ip_subscriber = None
            self.notification = Mib.InterfaceMib.Notification()
            self.notification.parent = self
            self.statistics_cache = None
            self.subsets = Mib.InterfaceMib.Subsets()
            self.subsets.parent = self


        class Interfaces(object):
            """
            Enter the SNMP interface configuration commands
            
            .. attribute:: interface
            
            	Interface to configure
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.InterfaceMib.Interfaces.Interface>`
            
            

            """

            _prefix = 'snmp-ifmib-cfg'
            _revision = '2015-05-14'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
                """
                Interface to configure
                
                .. attribute:: interface_name  <key>
                
                	The name of the interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: index_persistence
                
                	Enable or disable index persistence
                	**type**\:  bool
                
                .. attribute:: link_up_down
                
                	Enable or disable LinkUpDown notification
                	**type**\:  bool
                
                

                """

                _prefix = 'snmp-ifmib-cfg'
                _revision = '2015-05-14'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.index_persistence = None
                    self.link_up_down = None

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib/Cisco-IOS-XR-snmp-ifmib-cfg:interfaces/Cisco-IOS-XR-snmp-ifmib-cfg:interface[Cisco-IOS-XR-snmp-ifmib-cfg:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.index_persistence is not None:
                        return True

                    if self.link_up_down is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Mib.InterfaceMib.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib/Cisco-IOS-XR-snmp-ifmib-cfg:interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Mib.InterfaceMib.Interfaces']['meta_info']


        class Notification(object):
            """
            MIB notification configuration
            
            .. attribute:: link_ietf
            
            	Set the varbind of linkupdown trap to the RFC specified varbinds (default cisco)
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-ifmib-cfg'
            _revision = '2015-05-14'

            def __init__(self):
                self.parent = None
                self.link_ietf = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib/Cisco-IOS-XR-snmp-ifmib-cfg:notification'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.link_ietf is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Mib.InterfaceMib.Notification']['meta_info']


        class Subsets(object):
            """
            Add configuration for an interface subset
            
            .. attribute:: subset
            
            	Subset priorityID to group ifNames based on Regular Expression
            	**type**\: list of    :py:class:`Subset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.InterfaceMib.Subsets.Subset>`
            
            

            """

            _prefix = 'snmp-ifmib-cfg'
            _revision = '2015-05-14'

            def __init__(self):
                self.parent = None
                self.subset = YList()
                self.subset.parent = self
                self.subset.name = 'subset'


            class Subset(object):
                """
                Subset priorityID to group ifNames based on
                Regular Expression
                
                .. attribute:: subset_id  <key>
                
                	The interface subset PriorityID
                	**type**\:  int
                
                	**range:** 1..255
                
                .. attribute:: link_up_down
                
                	SNMP linkUp and linkDown notifications
                	**type**\:   :py:class:`LinkUpDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.InterfaceMib.Subsets.Subset.LinkUpDown>`
                
                

                """

                _prefix = 'snmp-ifmib-cfg'
                _revision = '2015-05-14'

                def __init__(self):
                    self.parent = None
                    self.subset_id = None
                    self.link_up_down = Mib.InterfaceMib.Subsets.Subset.LinkUpDown()
                    self.link_up_down.parent = self


                class LinkUpDown(object):
                    """
                    SNMP linkUp and linkDown notifications
                    
                    .. attribute:: enable
                    
                    	Enable or disable linkupdown notification
                    	**type**\:  bool
                    
                    .. attribute:: regular_expression
                    
                    	Regular expression to match ifName
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'snmp-ifmib-cfg'
                    _revision = '2015-05-14'

                    def __init__(self):
                        self.parent = None
                        self.enable = None
                        self.regular_expression = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-snmp-ifmib-cfg:link-up-down'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.enable is not None:
                            return True

                        if self.regular_expression is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Mib.InterfaceMib.Subsets.Subset.LinkUpDown']['meta_info']

                @property
                def _common_path(self):
                    if self.subset_id is None:
                        raise YPYModelError('Key property subset_id is None')

                    return '/Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib/Cisco-IOS-XR-snmp-ifmib-cfg:subsets/Cisco-IOS-XR-snmp-ifmib-cfg:subset[Cisco-IOS-XR-snmp-ifmib-cfg:subset-id = ' + str(self.subset_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.subset_id is not None:
                        return True

                    if self.link_up_down is not None and self.link_up_down._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Mib.InterfaceMib.Subsets.Subset']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib/Cisco-IOS-XR-snmp-ifmib-cfg:subsets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.subset is not None:
                    for child_ref in self.subset:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Mib.InterfaceMib.Subsets']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.interface_alias_long is not None:
                return True

            if self.interface_index_persistence is not None:
                return True

            if self.interfaces is not None and self.interfaces._has_data():
                return True

            if self.internal_cache is not None:
                return True

            if self.ip_subscriber is not None:
                return True

            if self.notification is not None and self.notification._has_data():
                return True

            if self.statistics_cache is not None:
                return True

            if self.subsets is not None and self.subsets._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.InterfaceMib']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-agent-cfg:mib'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.cb_qosmib is not None and self.cb_qosmib._has_data():
            return True

        if self.entity_mib is not None and self.entity_mib._has_data():
            return True

        if self.interface_mib is not None and self.interface_mib._has_data():
            return True

        if self.mpls_frr_mib is not None and self.mpls_frr_mib._has_data():
            return True

        if self.mpls_p2mp_mib is not None and self.mpls_p2mp_mib._has_data():
            return True

        if self.mpls_te_ext_mib is not None and self.mpls_te_ext_mib._has_data():
            return True

        if self.mpls_te_ext_std_mib is not None and self.mpls_te_ext_std_mib._has_data():
            return True

        if self.mpls_te_mib is not None and self.mpls_te_mib._has_data():
            return True

        if self.sensor_mib_cache is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['Mib']['meta_info']


