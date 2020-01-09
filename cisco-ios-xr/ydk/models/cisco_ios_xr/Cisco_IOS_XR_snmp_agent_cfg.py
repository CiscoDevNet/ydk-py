""" Cisco_IOS_XR_snmp_agent_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR snmp\-agent package configuration.

This module contains definitions
for the following management objects\:
  snmp\: The heirarchy point for all the SNMP configurations
  mib\: mib

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class GroupSnmpVersion(Enum):
    """
    GroupSnmpVersion (Enum Class)

    Group snmp version

    .. data:: v1 = 0

    	SNMP version 1

    .. data:: v2c = 1

    	SNMP version 2

    .. data:: v3 = 2

    	SNMP version 3

    """

    v1 = Enum.YLeaf(0, "v1")

    v2c = Enum.YLeaf(1, "v2c")

    v3 = Enum.YLeaf(2, "v3")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['GroupSnmpVersion']


class SnmpAccessLevel(Enum):
    """
    SnmpAccessLevel (Enum Class)

    Snmp access level

    .. data:: read_only = 0

    	Read Only Access for a community string

    .. data:: read_write = 1

    	Read Write Access for a community string

    """

    read_only = Enum.YLeaf(0, "read-only")

    read_write = Enum.YLeaf(1, "read-write")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpAccessLevel']


class SnmpBulkstatFileFormat(Enum):
    """
    SnmpBulkstatFileFormat (Enum Class)

    Snmp bulkstat file format

    .. data:: schema_ascii = 1

    	Tranfer file in schema Ascii format

    .. data:: bulk_ascii = 2

    	Tranfer file in Bulk Ascii format

    .. data:: bulk_binary = 3

    	Tranfer file in Bulk binary format

    """

    schema_ascii = Enum.YLeaf(1, "schema-ascii")

    bulk_ascii = Enum.YLeaf(2, "bulk-ascii")

    bulk_binary = Enum.YLeaf(3, "bulk-binary")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpBulkstatFileFormat']


class SnmpBulkstatSchema(Enum):
    """
    SnmpBulkstatSchema (Enum Class)

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

    exact_interface = Enum.YLeaf(1, "exact-interface")

    exact_oid = Enum.YLeaf(2, "exact-oid")

    wild_interface = Enum.YLeaf(3, "wild-interface")

    wild_oid = Enum.YLeaf(4, "wild-oid")

    range_oid = Enum.YLeaf(5, "range-oid")

    repeat_oid = Enum.YLeaf(6, "repeat-oid")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpBulkstatSchema']


class SnmpContext(Enum):
    """
    SnmpContext (Enum Class)

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

    vrf = Enum.YLeaf(1, "vrf")

    bridge = Enum.YLeaf(4, "bridge")

    ospf = Enum.YLeaf(5, "ospf")

    ospfv3 = Enum.YLeaf(6, "ospfv3")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpContext']


class SnmpDscpValue(Enum):
    """
    SnmpDscpValue (Enum Class)

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

    default = Enum.YLeaf(0, "default")

    af11 = Enum.YLeaf(10, "af11")

    af12 = Enum.YLeaf(12, "af12")

    af13 = Enum.YLeaf(14, "af13")

    af21 = Enum.YLeaf(18, "af21")

    af22 = Enum.YLeaf(20, "af22")

    af23 = Enum.YLeaf(22, "af23")

    af31 = Enum.YLeaf(26, "af31")

    af32 = Enum.YLeaf(28, "af32")

    af33 = Enum.YLeaf(30, "af33")

    af41 = Enum.YLeaf(34, "af41")

    af42 = Enum.YLeaf(36, "af42")

    af43 = Enum.YLeaf(38, "af43")

    ef = Enum.YLeaf(46, "ef")

    cs1 = Enum.YLeaf(8, "cs1")

    cs2 = Enum.YLeaf(16, "cs2")

    cs3 = Enum.YLeaf(24, "cs3")

    cs4 = Enum.YLeaf(32, "cs4")

    cs5 = Enum.YLeaf(40, "cs5")

    cs6 = Enum.YLeaf(48, "cs6")

    cs7 = Enum.YLeaf(56, "cs7")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpDscpValue']


class SnmpHashAlgorithm(Enum):
    """
    SnmpHashAlgorithm (Enum Class)

    Snmp hash algorithm

    .. data:: none = 0

    	No authentication required

    .. data:: md5 = 1

    	Standard Message Digest algorithm

    .. data:: sha = 2

    	SHA algorithm

    """

    none = Enum.YLeaf(0, "none")

    md5 = Enum.YLeaf(1, "md5")

    sha = Enum.YLeaf(2, "sha")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpHashAlgorithm']


class SnmpMibViewInclusion(Enum):
    """
    SnmpMibViewInclusion (Enum Class)

    Snmp mib view inclusion

    .. data:: included = 1

    	MIB View to be included

    .. data:: excluded = 2

    	MIB View to be excluded

    """

    included = Enum.YLeaf(1, "included")

    excluded = Enum.YLeaf(2, "excluded")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpMibViewInclusion']


class SnmpOwnerAccess(Enum):
    """
    SnmpOwnerAccess (Enum Class)

    Snmp owner access

    .. data:: sdr_owner = 0

    	Secure Domain Router Owner permissions

    .. data:: system_owner = 1

    	System owner permissions

    """

    sdr_owner = Enum.YLeaf(0, "sdr-owner")

    system_owner = Enum.YLeaf(1, "system-owner")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpOwnerAccess']


class SnmpPrecedenceValue1(Enum):
    """
    SnmpPrecedenceValue1 (Enum Class)

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

    routine = Enum.YLeaf(0, "routine")

    priority = Enum.YLeaf(1, "priority")

    immediate = Enum.YLeaf(2, "immediate")

    flash = Enum.YLeaf(3, "flash")

    flash_override = Enum.YLeaf(4, "flash-override")

    critical = Enum.YLeaf(5, "critical")

    internet = Enum.YLeaf(6, "internet")

    network = Enum.YLeaf(7, "network")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpPrecedenceValue1']


class SnmpPrivAlgorithm(Enum):
    """
    SnmpPrivAlgorithm (Enum Class)

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

    none = Enum.YLeaf(0, "none")

    des = Enum.YLeaf(1, "des")

    Y_3des = Enum.YLeaf(2, "3des")

    aes128 = Enum.YLeaf(3, "aes128")

    aes192 = Enum.YLeaf(4, "aes192")

    aes256 = Enum.YLeaf(5, "aes256")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpPrivAlgorithm']


class SnmpSecurityModel(Enum):
    """
    SnmpSecurityModel (Enum Class)

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

    no_authentication = Enum.YLeaf(0, "no-authentication")

    authentication = Enum.YLeaf(1, "authentication")

    privacy = Enum.YLeaf(2, "privacy")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpSecurityModel']


class SnmpTos(Enum):
    """
    SnmpTos (Enum Class)

    Snmp tos

    .. data:: precedence = 0

    	SNMP TOS type Precedence

    .. data:: dscp = 1

    	SNMP TOS type DSCP

    """

    precedence = Enum.YLeaf(0, "precedence")

    dscp = Enum.YLeaf(1, "dscp")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['SnmpTos']


class Snmpacl(Enum):
    """
    Snmpacl (Enum Class)

    Snmpacl

    .. data:: ipv4 = 1

    	Ipv4 Access-list

    .. data:: ipv6 = 2

    	Ipv6 Access-list

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['Snmpacl']


class UserSnmpVersion(Enum):
    """
    UserSnmpVersion (Enum Class)

    User snmp version

    .. data:: v1 = 1

    	SNMP version 1

    .. data:: v2c = 2

    	SNMP version 2

    .. data:: v3 = 3

    	SNMP version 3

    """

    v1 = Enum.YLeaf(1, "v1")

    v2c = Enum.YLeaf(2, "v2c")

    v3 = Enum.YLeaf(3, "v3")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['UserSnmpVersion']



class Snmp(_Entity_):
    """
    The heirarchy point for all the SNMP
    configurations
    
    .. attribute:: encrypted_community_maps
    
    	Container class to hold clear/encrypted communitie maps
    	**type**\:  :py:class:`EncryptedCommunityMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.EncryptedCommunityMaps>`
    
    .. attribute:: views
    
    	Class to configure a SNMPv2 MIB view
    	**type**\:  :py:class:`Views <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Views>`
    
    .. attribute:: logging
    
    	SNMP logging
    	**type**\:  :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Logging>`
    
    .. attribute:: administration
    
    	Container class for SNMP administration
    	**type**\:  :py:class:`Administration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Administration>`
    
    .. attribute:: agent
    
    	The heirarchy point for SNMP Agent configurations
    	**type**\:  :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Agent>`
    
    .. attribute:: trap
    
    	Class to hold trap configurations
    	**type**\:  :py:class:`Trap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Trap>`
    
    .. attribute:: drop_packet
    
    	SNMP packet drop config
    	**type**\:  :py:class:`DropPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.DropPacket>`
    
    .. attribute:: ipv6
    
    	SNMP TOS bit for outgoing packets
    	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Ipv6>`
    
    .. attribute:: ipv4
    
    	SNMP TOS bit for outgoing packets
    	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Ipv4>`
    
    .. attribute:: system
    
    	container to hold system information
    	**type**\:  :py:class:`System <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.System>`
    
    .. attribute:: target
    
    	SNMP target configurations
    	**type**\:  :py:class:`Target <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target>`
    
    .. attribute:: notification
    
    	Enable SNMP notifications
    	**type**\:  :py:class:`Notification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification>`
    
    .. attribute:: correlator
    
    	Configure properties of the trap correlator
    	**type**\:  :py:class:`Correlator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator>`
    
    .. attribute:: bulk_stats
    
    	SNMP bulk stats configuration commands
    	**type**\:  :py:class:`BulkStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats>`
    
    .. attribute:: default_community_maps
    
    	Container class to hold unencrpted community map
    	**type**\:  :py:class:`DefaultCommunityMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.DefaultCommunityMaps>`
    
    .. attribute:: overload_control
    
    	Set overload control params for handling incoming messages
    	**type**\:  :py:class:`OverloadControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.OverloadControl>`
    
    	**presence node**\: True
    
    .. attribute:: timeouts
    
    	SNMP timeouts
    	**type**\:  :py:class:`Timeouts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Timeouts>`
    
    .. attribute:: users
    
    	Define a user who can access the SNMP engine
    	**type**\:  :py:class:`Users <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Users>`
    
    .. attribute:: vrfs
    
    	SNMP VRF configuration commands
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs>`
    
    .. attribute:: groups
    
    	Define a User Security Model group
    	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Groups>`
    
    .. attribute:: inform_retries
    
    	Number of times to retry an Inform request (default 3)
    	**type**\: int
    
    	**range:** 0..100
    
    .. attribute:: trap_port
    
    	Change the source port of all traps
    	**type**\: int
    
    	**range:** 1024..65535
    
    .. attribute:: oid_poll_stats
    
    	Enable Poll OID statistics
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: trap_source
    
    	Assign an interface for the source address of all traps
    	**type**\: str
    
    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
    
    .. attribute:: vrf_authentication_trap_disable
    
    	Disable authentication traps for packets on a vrf
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: inform_timeout
    
    	Timeout value in seconds for Inform request (default 15 sec)
    	**type**\: int
    
    	**range:** 1..42949671
    
    	**units**\: second
    
    .. attribute:: trap_source_ipv6
    
    	Assign an interface for the source IPV6 address of all traps
    	**type**\: str
    
    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
    
    .. attribute:: packet_size
    
    	Largest SNMP packet size
    	**type**\: int
    
    	**range:** 484..65500
    
    .. attribute:: throttle_time
    
    	Throttle time for incoming queue (default 0 msec)
    	**type**\: int
    
    	**range:** 50..1000
    
    .. attribute:: trap_source_ipv4
    
    	Assign an interface for the source address of all traps
    	**type**\: str
    
    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
    
    .. attribute:: inform_pending
    
    	Max nmber of informs to hold in queue, (default 25)
    	**type**\: int
    
    	**range:** 0..4294967295
    
    .. attribute:: trap_hosts
    
    	Specify hosts to receive SNMP notifications
    	**type**\:  :py:class:`TrapHosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts>`
    
    .. attribute:: contexts
    
    	List of Context Names
    	**type**\:  :py:class:`Contexts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Contexts>`
    
    .. attribute:: context_mappings
    
    	List of context names
    	**type**\:  :py:class:`ContextMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.ContextMappings>`
    
    

    """

    _prefix = 'snmp-agent-cfg'
    _revision = '2018-06-27'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Snmp, self).__init__()
        self._top_entity = None

        self.yang_name = "snmp"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-agent-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("encrypted-community-maps", ("encrypted_community_maps", Snmp.EncryptedCommunityMaps)), ("views", ("views", Snmp.Views)), ("logging", ("logging", Snmp.Logging)), ("administration", ("administration", Snmp.Administration)), ("agent", ("agent", Snmp.Agent)), ("trap", ("trap", Snmp.Trap)), ("drop-packet", ("drop_packet", Snmp.DropPacket)), ("ipv6", ("ipv6", Snmp.Ipv6)), ("ipv4", ("ipv4", Snmp.Ipv4)), ("system", ("system", Snmp.System)), ("target", ("target", Snmp.Target)), ("notification", ("notification", Snmp.Notification)), ("correlator", ("correlator", Snmp.Correlator)), ("bulk-stats", ("bulk_stats", Snmp.BulkStats)), ("default-community-maps", ("default_community_maps", Snmp.DefaultCommunityMaps)), ("overload-control", ("overload_control", Snmp.OverloadControl)), ("timeouts", ("timeouts", Snmp.Timeouts)), ("users", ("users", Snmp.Users)), ("vrfs", ("vrfs", Snmp.Vrfs)), ("groups", ("groups", Snmp.Groups)), ("trap-hosts", ("trap_hosts", Snmp.TrapHosts)), ("contexts", ("contexts", Snmp.Contexts)), ("context-mappings", ("context_mappings", Snmp.ContextMappings))])
        self._leafs = OrderedDict([
            ('inform_retries', (YLeaf(YType.uint32, 'inform-retries'), ['int'])),
            ('trap_port', (YLeaf(YType.uint32, 'trap-port'), ['int'])),
            ('oid_poll_stats', (YLeaf(YType.empty, 'oid-poll-stats'), ['Empty'])),
            ('trap_source', (YLeaf(YType.str, 'trap-source'), ['str'])),
            ('vrf_authentication_trap_disable', (YLeaf(YType.empty, 'vrf-authentication-trap-disable'), ['Empty'])),
            ('inform_timeout', (YLeaf(YType.uint32, 'inform-timeout'), ['int'])),
            ('trap_source_ipv6', (YLeaf(YType.str, 'trap-source-ipv6'), ['str'])),
            ('packet_size', (YLeaf(YType.uint32, 'packet-size'), ['int'])),
            ('throttle_time', (YLeaf(YType.uint32, 'throttle-time'), ['int'])),
            ('trap_source_ipv4', (YLeaf(YType.str, 'trap-source-ipv4'), ['str'])),
            ('inform_pending', (YLeaf(YType.uint32, 'inform-pending'), ['int'])),
        ])
        self.inform_retries = None
        self.trap_port = None
        self.oid_poll_stats = None
        self.trap_source = None
        self.vrf_authentication_trap_disable = None
        self.inform_timeout = None
        self.trap_source_ipv6 = None
        self.packet_size = None
        self.throttle_time = None
        self.trap_source_ipv4 = None
        self.inform_pending = None

        self.encrypted_community_maps = Snmp.EncryptedCommunityMaps()
        self.encrypted_community_maps.parent = self
        self._children_name_map["encrypted_community_maps"] = "encrypted-community-maps"

        self.views = Snmp.Views()
        self.views.parent = self
        self._children_name_map["views"] = "views"

        self.logging = Snmp.Logging()
        self.logging.parent = self
        self._children_name_map["logging"] = "logging"

        self.administration = Snmp.Administration()
        self.administration.parent = self
        self._children_name_map["administration"] = "administration"

        self.agent = Snmp.Agent()
        self.agent.parent = self
        self._children_name_map["agent"] = "agent"

        self.trap = Snmp.Trap()
        self.trap.parent = self
        self._children_name_map["trap"] = "trap"

        self.drop_packet = Snmp.DropPacket()
        self.drop_packet.parent = self
        self._children_name_map["drop_packet"] = "drop-packet"

        self.ipv6 = Snmp.Ipv6()
        self.ipv6.parent = self
        self._children_name_map["ipv6"] = "ipv6"

        self.ipv4 = Snmp.Ipv4()
        self.ipv4.parent = self
        self._children_name_map["ipv4"] = "ipv4"

        self.system = Snmp.System()
        self.system.parent = self
        self._children_name_map["system"] = "system"

        self.target = Snmp.Target()
        self.target.parent = self
        self._children_name_map["target"] = "target"

        self.notification = Snmp.Notification()
        self.notification.parent = self
        self._children_name_map["notification"] = "notification"

        self.correlator = Snmp.Correlator()
        self.correlator.parent = self
        self._children_name_map["correlator"] = "correlator"

        self.bulk_stats = Snmp.BulkStats()
        self.bulk_stats.parent = self
        self._children_name_map["bulk_stats"] = "bulk-stats"

        self.default_community_maps = Snmp.DefaultCommunityMaps()
        self.default_community_maps.parent = self
        self._children_name_map["default_community_maps"] = "default-community-maps"

        self.overload_control = None
        self._children_name_map["overload_control"] = "overload-control"

        self.timeouts = Snmp.Timeouts()
        self.timeouts.parent = self
        self._children_name_map["timeouts"] = "timeouts"

        self.users = Snmp.Users()
        self.users.parent = self
        self._children_name_map["users"] = "users"

        self.vrfs = Snmp.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"

        self.groups = Snmp.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"

        self.trap_hosts = Snmp.TrapHosts()
        self.trap_hosts.parent = self
        self._children_name_map["trap_hosts"] = "trap-hosts"

        self.contexts = Snmp.Contexts()
        self.contexts.parent = self
        self._children_name_map["contexts"] = "contexts"

        self.context_mappings = Snmp.ContextMappings()
        self.context_mappings.parent = self
        self._children_name_map["context_mappings"] = "context-mappings"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Snmp, ['inform_retries', 'trap_port', 'oid_poll_stats', 'trap_source', 'vrf_authentication_trap_disable', 'inform_timeout', 'trap_source_ipv6', 'packet_size', 'throttle_time', 'trap_source_ipv4', 'inform_pending'], name, value)


    class EncryptedCommunityMaps(_Entity_):
        """
        Container class to hold clear/encrypted
        communitie maps
        
        .. attribute:: encrypted_community_map
        
        	Clear/encrypted SNMP community map
        	**type**\: list of  		 :py:class:`EncryptedCommunityMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.EncryptedCommunityMaps.EncryptedCommunityMap>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.EncryptedCommunityMaps, self).__init__()

            self.yang_name = "encrypted-community-maps"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("encrypted-community-map", ("encrypted_community_map", Snmp.EncryptedCommunityMaps.EncryptedCommunityMap))])
            self._leafs = OrderedDict()

            self.encrypted_community_map = YList(self)
            self._segment_path = lambda: "encrypted-community-maps"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.EncryptedCommunityMaps, [], name, value)


        class EncryptedCommunityMap(_Entity_):
            """
            Clear/encrypted SNMP community map
            
            .. attribute:: community_name  (key)
            
            	SNMP community map
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: context
            
            	SNMP Context Name 
            	**type**\: str
            
            .. attribute:: security
            
            	SNMP Security Name 
            	**type**\: str
            
            .. attribute:: target_list
            
            	target list name 
            	**type**\: str
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.EncryptedCommunityMaps.EncryptedCommunityMap, self).__init__()

                self.yang_name = "encrypted-community-map"
                self.yang_parent_name = "encrypted-community-maps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['community_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('community_name', (YLeaf(YType.str, 'community-name'), ['str'])),
                    ('context', (YLeaf(YType.str, 'context'), ['str'])),
                    ('security', (YLeaf(YType.str, 'security'), ['str'])),
                    ('target_list', (YLeaf(YType.str, 'target-list'), ['str'])),
                ])
                self.community_name = None
                self.context = None
                self.security = None
                self.target_list = None
                self._segment_path = lambda: "encrypted-community-map" + "[community-name='" + str(self.community_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/encrypted-community-maps/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.EncryptedCommunityMaps.EncryptedCommunityMap, ['community_name', 'context', 'security', 'target_list'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.EncryptedCommunityMaps.EncryptedCommunityMap']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.EncryptedCommunityMaps']['meta_info']


    class Views(_Entity_):
        """
        Class to configure a SNMPv2 MIB view
        
        .. attribute:: view
        
        	Name of the view
        	**type**\: list of  		 :py:class:`View <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Views.View>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Views, self).__init__()

            self.yang_name = "views"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("view", ("view", Snmp.Views.View))])
            self._leafs = OrderedDict()

            self.view = YList(self)
            self._segment_path = lambda: "views"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Views, [], name, value)


        class View(_Entity_):
            """
            Name of the view
            
            .. attribute:: view_name  (key)
            
            	Name of the view
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: family  (key)
            
            	MIB view family name
            	**type**\: str
            
            .. attribute:: view_inclusion
            
            	MIB view to be included or excluded
            	**type**\:  :py:class:`SnmpMibViewInclusion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpMibViewInclusion>`
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Views.View, self).__init__()

                self.yang_name = "view"
                self.yang_parent_name = "views"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['view_name','family']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('view_name', (YLeaf(YType.str, 'view-name'), ['str'])),
                    ('family', (YLeaf(YType.str, 'family'), ['str'])),
                    ('view_inclusion', (YLeaf(YType.enumeration, 'view-inclusion'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpMibViewInclusion', '')])),
                ])
                self.view_name = None
                self.family = None
                self.view_inclusion = None
                self._segment_path = lambda: "view" + "[view-name='" + str(self.view_name) + "']" + "[family='" + str(self.family) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/views/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Views.View, ['view_name', 'family', 'view_inclusion'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Views.View']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Views']['meta_info']


    class Logging(_Entity_):
        """
        SNMP logging
        
        .. attribute:: threshold
        
        	SNMP logging threshold
        	**type**\:  :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Logging.Threshold>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Logging, self).__init__()

            self.yang_name = "logging"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("threshold", ("threshold", Snmp.Logging.Threshold))])
            self._leafs = OrderedDict()

            self.threshold = Snmp.Logging.Threshold()
            self.threshold.parent = self
            self._children_name_map["threshold"] = "threshold"
            self._segment_path = lambda: "logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Logging, [], name, value)


        class Threshold(_Entity_):
            """
            SNMP logging threshold
            
            .. attribute:: oid_processing
            
            	SNMP logging threshold for OID processing
            	**type**\: int
            
            	**range:** 0..20000
            
            	**default value**\: 500
            
            .. attribute:: pdu_processing
            
            	SNMP logging threshold for PDU processing
            	**type**\: int
            
            	**range:** 0..20000
            
            	**default value**\: 20000
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Logging.Threshold, self).__init__()

                self.yang_name = "threshold"
                self.yang_parent_name = "logging"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('oid_processing', (YLeaf(YType.uint32, 'oid-processing'), ['int'])),
                    ('pdu_processing', (YLeaf(YType.uint32, 'pdu-processing'), ['int'])),
                ])
                self.oid_processing = None
                self.pdu_processing = None
                self._segment_path = lambda: "threshold"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/logging/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Logging.Threshold, ['oid_processing', 'pdu_processing'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Logging.Threshold']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Logging']['meta_info']


    class Administration(_Entity_):
        """
        Container class for SNMP administration
        
        .. attribute:: default_communities
        
        	Container class to hold unencrpted communities
        	**type**\:  :py:class:`DefaultCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Administration.DefaultCommunities>`
        
        .. attribute:: encrypted_communities
        
        	Container class to hold clear/encrypted communities
        	**type**\:  :py:class:`EncryptedCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Administration.EncryptedCommunities>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Administration, self).__init__()

            self.yang_name = "administration"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("default-communities", ("default_communities", Snmp.Administration.DefaultCommunities)), ("encrypted-communities", ("encrypted_communities", Snmp.Administration.EncryptedCommunities))])
            self._leafs = OrderedDict()

            self.default_communities = Snmp.Administration.DefaultCommunities()
            self.default_communities.parent = self
            self._children_name_map["default_communities"] = "default-communities"

            self.encrypted_communities = Snmp.Administration.EncryptedCommunities()
            self.encrypted_communities.parent = self
            self._children_name_map["encrypted_communities"] = "encrypted-communities"
            self._segment_path = lambda: "administration"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Administration, [], name, value)


        class DefaultCommunities(_Entity_):
            """
            Container class to hold unencrpted communities
            
            .. attribute:: default_community
            
            	Unencrpted SNMP community string and access priviledges
            	**type**\: list of  		 :py:class:`DefaultCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Administration.DefaultCommunities.DefaultCommunity>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Administration.DefaultCommunities, self).__init__()

                self.yang_name = "default-communities"
                self.yang_parent_name = "administration"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("default-community", ("default_community", Snmp.Administration.DefaultCommunities.DefaultCommunity))])
                self._leafs = OrderedDict()

                self.default_community = YList(self)
                self._segment_path = lambda: "default-communities"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/administration/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Administration.DefaultCommunities, [], name, value)


            class DefaultCommunity(_Entity_):
                """
                Unencrpted SNMP community string and access
                priviledges
                
                .. attribute:: community_name  (key)
                
                	SNMP community string
                	**type**\: str
                
                	**length:** 1..128
                
                .. attribute:: priviledge
                
                	Read/Write Access
                	**type**\:  :py:class:`SnmpAccessLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpAccessLevel>`
                
                .. attribute:: view_name
                
                	MIB view to which the community has access
                	**type**\: str
                
                .. attribute:: v4acl_type
                
                	Access\-list type
                	**type**\:  :py:class:`Snmpacl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmpacl>`
                
                .. attribute:: v4_access_list
                
                	Ipv4 Access\-list name
                	**type**\: str
                
                .. attribute:: v6acl_type
                
                	Access\-list type
                	**type**\:  :py:class:`Snmpacl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmpacl>`
                
                .. attribute:: v6_access_list
                
                	Ipv6 Access\-list name
                	**type**\: str
                
                .. attribute:: owner
                
                	Logical Router or System owner access
                	**type**\:  :py:class:`SnmpOwnerAccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpOwnerAccess>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2018-06-27'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Administration.DefaultCommunities.DefaultCommunity, self).__init__()

                    self.yang_name = "default-community"
                    self.yang_parent_name = "default-communities"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['community_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('community_name', (YLeaf(YType.str, 'community-name'), ['str'])),
                        ('priviledge', (YLeaf(YType.enumeration, 'priviledge'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpAccessLevel', '')])),
                        ('view_name', (YLeaf(YType.str, 'view-name'), ['str'])),
                        ('v4acl_type', (YLeaf(YType.enumeration, 'v4acl-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmpacl', '')])),
                        ('v4_access_list', (YLeaf(YType.str, 'v4-access-list'), ['str'])),
                        ('v6acl_type', (YLeaf(YType.enumeration, 'v6acl-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmpacl', '')])),
                        ('v6_access_list', (YLeaf(YType.str, 'v6-access-list'), ['str'])),
                        ('owner', (YLeaf(YType.enumeration, 'owner'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpOwnerAccess', '')])),
                    ])
                    self.community_name = None
                    self.priviledge = None
                    self.view_name = None
                    self.v4acl_type = None
                    self.v4_access_list = None
                    self.v6acl_type = None
                    self.v6_access_list = None
                    self.owner = None
                    self._segment_path = lambda: "default-community" + "[community-name='" + str(self.community_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/administration/default-communities/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Administration.DefaultCommunities.DefaultCommunity, ['community_name', 'priviledge', 'view_name', 'v4acl_type', 'v4_access_list', 'v6acl_type', 'v6_access_list', 'owner'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Administration.DefaultCommunities.DefaultCommunity']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Administration.DefaultCommunities']['meta_info']


        class EncryptedCommunities(_Entity_):
            """
            Container class to hold clear/encrypted
            communities
            
            .. attribute:: encrypted_community
            
            	Clear/encrypted SNMP community string and access priviledges
            	**type**\: list of  		 :py:class:`EncryptedCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Administration.EncryptedCommunities.EncryptedCommunity>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Administration.EncryptedCommunities, self).__init__()

                self.yang_name = "encrypted-communities"
                self.yang_parent_name = "administration"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("encrypted-community", ("encrypted_community", Snmp.Administration.EncryptedCommunities.EncryptedCommunity))])
                self._leafs = OrderedDict()

                self.encrypted_community = YList(self)
                self._segment_path = lambda: "encrypted-communities"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/administration/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Administration.EncryptedCommunities, [], name, value)


            class EncryptedCommunity(_Entity_):
                """
                Clear/encrypted SNMP community string and
                access priviledges
                
                .. attribute:: community_name  (key)
                
                	SNMP community string
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: priviledge
                
                	Read/Write Access
                	**type**\:  :py:class:`SnmpAccessLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpAccessLevel>`
                
                .. attribute:: view_name
                
                	MIB view to which the community has access
                	**type**\: str
                
                .. attribute:: v4acl_type
                
                	Access\-list type
                	**type**\:  :py:class:`Snmpacl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmpacl>`
                
                .. attribute:: v4_access_list
                
                	Ipv4 Access\-list name
                	**type**\: str
                
                .. attribute:: v6acl_type
                
                	Access\-list type
                	**type**\:  :py:class:`Snmpacl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmpacl>`
                
                .. attribute:: v6_access_list
                
                	Ipv6 Access\-list name
                	**type**\: str
                
                .. attribute:: owner
                
                	Logical Router or System owner access
                	**type**\:  :py:class:`SnmpOwnerAccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpOwnerAccess>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2018-06-27'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Administration.EncryptedCommunities.EncryptedCommunity, self).__init__()

                    self.yang_name = "encrypted-community"
                    self.yang_parent_name = "encrypted-communities"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['community_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('community_name', (YLeaf(YType.str, 'community-name'), ['str'])),
                        ('priviledge', (YLeaf(YType.enumeration, 'priviledge'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpAccessLevel', '')])),
                        ('view_name', (YLeaf(YType.str, 'view-name'), ['str'])),
                        ('v4acl_type', (YLeaf(YType.enumeration, 'v4acl-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmpacl', '')])),
                        ('v4_access_list', (YLeaf(YType.str, 'v4-access-list'), ['str'])),
                        ('v6acl_type', (YLeaf(YType.enumeration, 'v6acl-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmpacl', '')])),
                        ('v6_access_list', (YLeaf(YType.str, 'v6-access-list'), ['str'])),
                        ('owner', (YLeaf(YType.enumeration, 'owner'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpOwnerAccess', '')])),
                    ])
                    self.community_name = None
                    self.priviledge = None
                    self.view_name = None
                    self.v4acl_type = None
                    self.v4_access_list = None
                    self.v6acl_type = None
                    self.v6_access_list = None
                    self.owner = None
                    self._segment_path = lambda: "encrypted-community" + "[community-name='" + str(self.community_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/administration/encrypted-communities/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Administration.EncryptedCommunities.EncryptedCommunity, ['community_name', 'priviledge', 'view_name', 'v4acl_type', 'v4_access_list', 'v6acl_type', 'v6_access_list', 'owner'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Administration.EncryptedCommunities.EncryptedCommunity']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Administration.EncryptedCommunities']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Administration']['meta_info']


    class Agent(_Entity_):
        """
        The heirarchy point for SNMP Agent
        configurations
        
        .. attribute:: engine_id
        
        	SNMPv3 engineID
        	**type**\:  :py:class:`EngineId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Agent.EngineId>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Agent, self).__init__()

            self.yang_name = "agent"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("engine-id", ("engine_id", Snmp.Agent.EngineId))])
            self._leafs = OrderedDict()

            self.engine_id = Snmp.Agent.EngineId()
            self.engine_id.parent = self
            self._children_name_map["engine_id"] = "engine-id"
            self._segment_path = lambda: "agent"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Agent, [], name, value)


        class EngineId(_Entity_):
            """
            SNMPv3 engineID
            
            .. attribute:: remotes
            
            	SNMPv3 remote SNMP Entity
            	**type**\:  :py:class:`Remotes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Agent.EngineId.Remotes>`
            
            .. attribute:: local
            
            	engineID of the local agent
            	**type**\: str
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Agent.EngineId, self).__init__()

                self.yang_name = "engine-id"
                self.yang_parent_name = "agent"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("remotes", ("remotes", Snmp.Agent.EngineId.Remotes))])
                self._leafs = OrderedDict([
                    ('local', (YLeaf(YType.str, 'local'), ['str'])),
                ])
                self.local = None

                self.remotes = Snmp.Agent.EngineId.Remotes()
                self.remotes.parent = self
                self._children_name_map["remotes"] = "remotes"
                self._segment_path = lambda: "engine-id"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/agent/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Agent.EngineId, ['local'], name, value)


            class Remotes(_Entity_):
                """
                SNMPv3 remote SNMP Entity
                
                .. attribute:: remote
                
                	engineID of the remote agent
                	**type**\: list of  		 :py:class:`Remote <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Agent.EngineId.Remotes.Remote>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2018-06-27'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Agent.EngineId.Remotes, self).__init__()

                    self.yang_name = "remotes"
                    self.yang_parent_name = "engine-id"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("remote", ("remote", Snmp.Agent.EngineId.Remotes.Remote))])
                    self._leafs = OrderedDict()

                    self.remote = YList(self)
                    self._segment_path = lambda: "remotes"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/agent/engine-id/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Agent.EngineId.Remotes, [], name, value)


                class Remote(_Entity_):
                    """
                    engineID of the remote agent
                    
                    .. attribute:: remote_address  (key)
                    
                    	IP address of remote SNMP entity
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: remote_engine_id
                    
                    	engine ID octet string
                    	**type**\: str
                    
                    .. attribute:: port
                    
                    	UDP port number
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Agent.EngineId.Remotes.Remote, self).__init__()

                        self.yang_name = "remote"
                        self.yang_parent_name = "remotes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['remote_address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('remote_address', (YLeaf(YType.str, 'remote-address'), ['str','str'])),
                            ('remote_engine_id', (YLeaf(YType.str, 'remote-engine-id'), ['str'])),
                            ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                        ])
                        self.remote_address = None
                        self.remote_engine_id = None
                        self.port = None
                        self._segment_path = lambda: "remote" + "[remote-address='" + str(self.remote_address) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/agent/engine-id/remotes/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Agent.EngineId.Remotes.Remote, ['remote_address', 'remote_engine_id', 'port'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Agent.EngineId.Remotes.Remote']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Agent.EngineId.Remotes']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Agent.EngineId']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Agent']['meta_info']


    class Trap(_Entity_):
        """
        Class to hold trap configurations
        
        .. attribute:: timeout
        
        	Timeout for TRAP message retransmissions
        	**type**\: int
        
        	**range:** 1..1000
        
        .. attribute:: throttle_time
        
        	Set throttle time for handling traps
        	**type**\: int
        
        	**range:** 10..500
        
        	**units**\: millisecond
        
        .. attribute:: queue_length
        
        	Message queue length for each TRAP host
        	**type**\: int
        
        	**range:** 1..5000
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Trap, self).__init__()

            self.yang_name = "trap"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                ('throttle_time', (YLeaf(YType.uint32, 'throttle-time'), ['int'])),
                ('queue_length', (YLeaf(YType.uint32, 'queue-length'), ['int'])),
            ])
            self.timeout = None
            self.throttle_time = None
            self.queue_length = None
            self._segment_path = lambda: "trap"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Trap, ['timeout', 'throttle_time', 'queue_length'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Trap']['meta_info']


    class DropPacket(_Entity_):
        """
        SNMP packet drop config
        
        .. attribute:: unknown_user
        
        	Enable drop unknown user name
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.DropPacket, self).__init__()

            self.yang_name = "drop-packet"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('unknown_user', (YLeaf(YType.empty, 'unknown-user'), ['Empty'])),
            ])
            self.unknown_user = None
            self._segment_path = lambda: "drop-packet"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.DropPacket, ['unknown_user'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.DropPacket']['meta_info']


    class Ipv6(_Entity_):
        """
        SNMP TOS bit for outgoing packets
        
        .. attribute:: tos
        
        	Type of TOS
        	**type**\:  :py:class:`Tos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Ipv6.Tos>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Ipv6, self).__init__()

            self.yang_name = "ipv6"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tos", ("tos", Snmp.Ipv6.Tos))])
            self._leafs = OrderedDict()

            self.tos = Snmp.Ipv6.Tos()
            self.tos.parent = self
            self._children_name_map["tos"] = "tos"
            self._segment_path = lambda: "ipv6"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Ipv6, [], name, value)


        class Tos(_Entity_):
            """
            Type of TOS
            
            .. attribute:: type
            
            	SNMP TOS type DSCP or Precedence
            	**type**\:  :py:class:`SnmpTos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpTos>`
            
            .. attribute:: precedence
            
            	SNMP Precedence value
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`SnmpPrecedenceValue1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpPrecedenceValue1>`
            
            		**type**\: int
            
            			**range:** 0..7
            
            .. attribute:: dscp
            
            	SNMP DSCP value
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`SnmpDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpDscpValue>`
            
            		**type**\: int
            
            			**range:** 0..63
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Ipv6.Tos, self).__init__()

                self.yang_name = "tos"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpTos', '')])),
                    ('precedence', (YLeaf(YType.str, 'precedence'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpPrecedenceValue1', ''),'int'])),
                    ('dscp', (YLeaf(YType.str, 'dscp'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpDscpValue', ''),'int'])),
                ])
                self.type = None
                self.precedence = None
                self.dscp = None
                self._segment_path = lambda: "tos"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/ipv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Ipv6.Tos, ['type', 'precedence', 'dscp'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Ipv6.Tos']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Ipv6']['meta_info']


    class Ipv4(_Entity_):
        """
        SNMP TOS bit for outgoing packets
        
        .. attribute:: tos
        
        	Type of TOS
        	**type**\:  :py:class:`Tos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Ipv4.Tos>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Ipv4, self).__init__()

            self.yang_name = "ipv4"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tos", ("tos", Snmp.Ipv4.Tos))])
            self._leafs = OrderedDict()

            self.tos = Snmp.Ipv4.Tos()
            self.tos.parent = self
            self._children_name_map["tos"] = "tos"
            self._segment_path = lambda: "ipv4"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Ipv4, [], name, value)


        class Tos(_Entity_):
            """
            Type of TOS
            
            .. attribute:: type
            
            	SNMP TOS type DSCP or Precedence
            	**type**\:  :py:class:`SnmpTos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpTos>`
            
            .. attribute:: precedence
            
            	SNMP Precedence value
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`SnmpPrecedenceValue1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpPrecedenceValue1>`
            
            		**type**\: int
            
            			**range:** 0..7
            
            .. attribute:: dscp
            
            	SNMP DSCP value
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`SnmpDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpDscpValue>`
            
            		**type**\: int
            
            			**range:** 0..63
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Ipv4.Tos, self).__init__()

                self.yang_name = "tos"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpTos', '')])),
                    ('precedence', (YLeaf(YType.str, 'precedence'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpPrecedenceValue1', ''),'int'])),
                    ('dscp', (YLeaf(YType.str, 'dscp'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpDscpValue', ''),'int'])),
                ])
                self.type = None
                self.precedence = None
                self.dscp = None
                self._segment_path = lambda: "tos"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/ipv4/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Ipv4.Tos, ['type', 'precedence', 'dscp'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Ipv4.Tos']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Ipv4']['meta_info']


    class System(_Entity_):
        """
        container to hold system information
        
        .. attribute:: chassis_id
        
        	String to uniquely identify this chassis
        	**type**\: str
        
        	**length:** 1..255
        
        .. attribute:: location
        
        	The physical location of this node
        	**type**\: str
        
        	**length:** 1..255
        
        .. attribute:: contact
        
        	identification of the contact person for this managed node
        	**type**\: str
        
        	**length:** 1..255
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.System, self).__init__()

            self.yang_name = "system"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('chassis_id', (YLeaf(YType.str, 'chassis-id'), ['str'])),
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ('contact', (YLeaf(YType.str, 'contact'), ['str'])),
            ])
            self.chassis_id = None
            self.location = None
            self.contact = None
            self._segment_path = lambda: "system"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.System, ['chassis_id', 'location', 'contact'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.System']['meta_info']


    class Target(_Entity_):
        """
        SNMP target configurations
        
        .. attribute:: targets
        
        	List of targets
        	**type**\:  :py:class:`Targets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Target, self).__init__()

            self.yang_name = "target"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("targets", ("targets", Snmp.Target.Targets))])
            self._leafs = OrderedDict()

            self.targets = Snmp.Target.Targets()
            self.targets.parent = self
            self._children_name_map["targets"] = "targets"
            self._segment_path = lambda: "target"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Target, [], name, value)


        class Targets(_Entity_):
            """
            List of targets
            
            .. attribute:: target
            
            	Name of the target list
            	**type**\: list of  		 :py:class:`Target_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets.Target_>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Target.Targets, self).__init__()

                self.yang_name = "targets"
                self.yang_parent_name = "target"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("target", ("target", Snmp.Target.Targets.Target_))])
                self._leafs = OrderedDict()

                self.target = YList(self)
                self._segment_path = lambda: "targets"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/target/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Target.Targets, [], name, value)


            class Target_(_Entity_):
                """
                Name of the target list
                
                .. attribute:: target_list_name  (key)
                
                	Name of the target list
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: vrf_names
                
                	List of VRF Name for a target list
                	**type**\:  :py:class:`VrfNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets.Target_.VrfNames>`
                
                .. attribute:: target_addresses
                
                	SNMP Target address configurations
                	**type**\:  :py:class:`TargetAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets.Target_.TargetAddresses>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2018-06-27'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Target.Targets.Target_, self).__init__()

                    self.yang_name = "target"
                    self.yang_parent_name = "targets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['target_list_name']
                    self._child_classes = OrderedDict([("vrf-names", ("vrf_names", Snmp.Target.Targets.Target_.VrfNames)), ("target-addresses", ("target_addresses", Snmp.Target.Targets.Target_.TargetAddresses))])
                    self._leafs = OrderedDict([
                        ('target_list_name', (YLeaf(YType.str, 'target-list-name'), ['str'])),
                    ])
                    self.target_list_name = None

                    self.vrf_names = Snmp.Target.Targets.Target_.VrfNames()
                    self.vrf_names.parent = self
                    self._children_name_map["vrf_names"] = "vrf-names"

                    self.target_addresses = Snmp.Target.Targets.Target_.TargetAddresses()
                    self.target_addresses.parent = self
                    self._children_name_map["target_addresses"] = "target-addresses"
                    self._segment_path = lambda: "target" + "[target-list-name='" + str(self.target_list_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/target/targets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Target.Targets.Target_, ['target_list_name'], name, value)


                class VrfNames(_Entity_):
                    """
                    List of VRF Name for a target list
                    
                    .. attribute:: vrf_name
                    
                    	VRF name of the target
                    	**type**\: list of  		 :py:class:`VrfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets.Target_.VrfNames.VrfName>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Target.Targets.Target_.VrfNames, self).__init__()

                        self.yang_name = "vrf-names"
                        self.yang_parent_name = "target"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("vrf-name", ("vrf_name", Snmp.Target.Targets.Target_.VrfNames.VrfName))])
                        self._leafs = OrderedDict()

                        self.vrf_name = YList(self)
                        self._segment_path = lambda: "vrf-names"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Target.Targets.Target_.VrfNames, [], name, value)


                    class VrfName(_Entity_):
                        """
                        VRF name of the target
                        
                        .. attribute:: name  (key)
                        
                        	VRF Name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2018-06-27'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.Target.Targets.Target_.VrfNames.VrfName, self).__init__()

                            self.yang_name = "vrf-name"
                            self.yang_parent_name = "vrf-names"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ])
                            self.name = None
                            self._segment_path = lambda: "vrf-name" + "[name='" + str(self.name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Target.Targets.Target_.VrfNames.VrfName, ['name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Target.Targets.Target_.VrfNames.VrfName']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Target.Targets.Target_.VrfNames']['meta_info']


                class TargetAddresses(_Entity_):
                    """
                    SNMP Target address configurations
                    
                    .. attribute:: target_address
                    
                    	IP Address to be configured for the Target
                    	**type**\: list of  		 :py:class:`TargetAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets.Target_.TargetAddresses.TargetAddress>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Target.Targets.Target_.TargetAddresses, self).__init__()

                        self.yang_name = "target-addresses"
                        self.yang_parent_name = "target"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("target-address", ("target_address", Snmp.Target.Targets.Target_.TargetAddresses.TargetAddress))])
                        self._leafs = OrderedDict()

                        self.target_address = YList(self)
                        self._segment_path = lambda: "target-addresses"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Target.Targets.Target_.TargetAddresses, [], name, value)


                    class TargetAddress(_Entity_):
                        """
                        IP Address to be configured for the Target
                        
                        .. attribute:: ip_address  (key)
                        
                        	IPv4/Ipv6 address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2018-06-27'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.Target.Targets.Target_.TargetAddresses.TargetAddress, self).__init__()

                            self.yang_name = "target-address"
                            self.yang_parent_name = "target-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['ip_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                            ])
                            self.ip_address = None
                            self._segment_path = lambda: "target-address" + "[ip-address='" + str(self.ip_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Target.Targets.Target_.TargetAddresses.TargetAddress, ['ip_address'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Target.Targets.Target_.TargetAddresses.TargetAddress']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Target.Targets.Target_.TargetAddresses']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Target.Targets.Target_']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Target.Targets']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Target']['meta_info']


    class Notification(_Entity_):
        """
        Enable SNMP notifications
        
        .. attribute:: snmp
        
        	SNMP notification configuration
        	**type**\:  :py:class:`Snmp_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Snmp_>`
        
        .. attribute:: selective_vrf_download
        
        	CISCO\-SELECTIVE\-VRF\-DOWNLOAD\-MIB notification configuration
        	**type**\:  :py:class:`SelectiveVrfDownload <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.SelectiveVrfDownload>`
        
        .. attribute:: vpls
        
        	CISCO\-IETF\-VPLS\-GENERIC\-MIB notification configuration
        	**type**\:  :py:class:`Vpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Vpls>`
        
        .. attribute:: l2vpn
        
        	CISCO\-IETF\-PW\-MIB notification configuration
        	**type**\:  :py:class:`L2vpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.L2vpn>`
        
        .. attribute:: entity_
        
        	Enable ENTITY\-MIB notifications
        	**type**\:  :py:class:`Entity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Entity>`
        
        .. attribute:: bridge
        
        	BRIDGE\-MIB notification configuration
        	**type**\:  :py:class:`Bridge <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Bridge>`
        
        .. attribute:: rf
        
        	CISCO\-RF\-MIB notification configuration
        	**type**\:  :py:class:`Rf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Rf>`
        
        .. attribute:: ntp
        
        	CISCO\-NTP\-MIB notification configuration
        	**type**\:  :py:class:`Ntp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ntp>`
        
        .. attribute:: otn
        
        	CISCO\-OTN\-IF\-MIB notification configuration
        	**type**\:  :py:class:`Otn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Otn>`
        
        .. attribute:: addresspool_mib
        
        	Enable SNMP daps traps
        	**type**\:  :py:class:`AddresspoolMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.AddresspoolMib>`
        
        .. attribute:: system
        
        	CISCO\-SYSTEM\-MIB notification configuration
        	**type**\:  :py:class:`System <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.System>`
        
        .. attribute:: rsvp
        
        	Enable RSVP\-MIB notifications
        	**type**\:  :py:class:`Rsvp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Rsvp>`
        
        .. attribute:: sensor
        
        	CISCO\-ENTITY\-SENSOR\-MIB notification configuration
        	**type**\:  :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Sensor>`
        
        .. attribute:: mpls_ldp
        
        	MPLS\-LDP\-STD\-MIB notification configuration
        	**type**\:  :py:class:`MplsLdp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.MplsLdp>`
        
        .. attribute:: subscriber_mib
        
        	Subscriber notification commands
        	**type**\:  :py:class:`SubscriberMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.SubscriberMib>`
        
        .. attribute:: flash
        
        	CISCO\-FLASH\-MIB notification configuration
        	**type**\:  :py:class:`Flash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Flash>`
        
        .. attribute:: config_copy
        
        	CISCO\-CONFIG\-COPY\-MIB notification configuration
        	**type**\:  :py:class:`ConfigCopy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.ConfigCopy>`
        
        .. attribute:: hsrp
        
        	CISCO\-HSRP\-MIB notification configuration
        	**type**\:  :py:class:`Hsrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Hsrp>`
        
        .. attribute:: entity_redundancy
        
        	CISCO\-ENTITY\-REDUNDANCY\-MIB notification configuration
        	**type**\:  :py:class:`EntityRedundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.EntityRedundancy>`
        
        .. attribute:: isis
        
        	Enable ISIS\-MIB notifications
        	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Isis>`
        
        .. attribute:: vrrp
        
        	VRRP\-MIB notification configuration
        	**type**\:  :py:class:`Vrrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Vrrp>`
        
        .. attribute:: ip_sec
        
        	Enable CISCO\-IPSEC\-FLOW\-MONITOR\-MIB notifications
        	**type**\:  :py:class:`IpSec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.IpSec>`
        
        .. attribute:: isakmp
        
        	Enable CISCO\-IPSEC\-FLOW\-MONITOR\-MIB notifications
        	**type**\:  :py:class:`Isakmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Isakmp>`
        
        .. attribute:: cisco_entity_ext
        
        	Enable CISCO\-ENTITY\-EXT\-MIB notifications
        	**type**\:  :py:class:`CiscoEntityExt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.CiscoEntityExt>`
        
        .. attribute:: ospf
        
        	OSPF\-MIB notification configuration
        	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ospf>`
        
        .. attribute:: cfm
        
        	802.1ag Connectivity Fault Management MIB notification configuration
        	**type**\:  :py:class:`Cfm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Cfm>`
        
        .. attribute:: l2tun
        
        	Enable SNMP l2tun traps
        	**type**\:  :py:class:`L2tun <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.L2tun>`
        
        .. attribute:: bgp
        
        	BGP4\-MIB and CISCO\-BGP4\-MIB notification configuration
        	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Bgp>`
        
        .. attribute:: entity_state
        
        	ENTITY\-STATE\-MIB notification configuration
        	**type**\:  :py:class:`EntityState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.EntityState>`
        
        .. attribute:: frequency_synchronization
        
        	Frequency Synchronization trap configuration
        	**type**\:  :py:class:`FrequencySynchronization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.FrequencySynchronization>`
        
        .. attribute:: mpls_te_p2mp
        
        	CISCO\-MPLS\-TE\-P2MP\-STD\-MIB notification configuration
        	**type**\:  :py:class:`MplsTeP2mp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.MplsTeP2mp>`
        
        .. attribute:: mpls_te
        
        	MPLS\-TE\-STD\-MIB notification configuration
        	**type**\:  :py:class:`MplsTe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.MplsTe>`
        
        .. attribute:: mpls_frr
        
        	CISCO\-IETF\-FRR\-MIB notification configuration
        	**type**\:  :py:class:`MplsFrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.MplsFrr>`
        
        .. attribute:: oam
        
        	802.3 OAM MIB notification configuration
        	**type**\:  :py:class:`Oam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Oam>`
        
        .. attribute:: mpls_l3vpn
        
        	MPLS\-L3VPN\-STD\-MIB notification configuration
        	**type**\:  :py:class:`MplsL3vpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.MplsL3vpn>`
        
        .. attribute:: config_man
        
        	CISCO\-CONFIG\-MAN\-MIB notification configurations
        	**type**\:  :py:class:`ConfigMan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.ConfigMan>`
        
        .. attribute:: diametermib
        
        	Enable SNMP diameter traps
        	**type**\:  :py:class:`Diametermib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Diametermib>`
        
        .. attribute:: fru_control
        
        	CISCO\-ENTITY\-FRU\-CONTROL\-MIB notification configuration
        	**type**\:  :py:class:`FruControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.FruControl>`
        
        .. attribute:: syslog
        
        	CISCO\-SYSLOG\-MIB notification configuration
        	**type**\:  :py:class:`Syslog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Syslog>`
        
        .. attribute:: ipsla
        
        	Enable SNMP RTTMON\-MIB IPSLA traps
        	**type**\: bool
        
        .. attribute:: bfd
        
        	CISCO\-IETF\-BFD\-MIB notification configuration
        	**type**\:  :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Bfd>`
        
        .. attribute:: optical_ots
        
        	CISCO\-OPTICAL\-OTS\-MIB notification configuration
        	**type**\:  :py:class:`OpticalOts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.OpticalOts>`
        
        .. attribute:: optical
        
        	CISCO\-OPTICAL\-MIB notification configuration
        	**type**\:  :py:class:`Optical <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Optical>`
        
        .. attribute:: ospfv3
        
        	OSPFv3\-MIB notification configuration
        	**type**\:  :py:class:`Ospfv3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ospfv3>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Notification, self).__init__()

            self.yang_name = "notification"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("snmp", ("snmp", Snmp.Notification.Snmp_)), ("Cisco-IOS-XR-infra-rsi-cfg:selective-vrf-download", ("selective_vrf_download", Snmp.Notification.SelectiveVrfDownload)), ("Cisco-IOS-XR-l2vpn-cfg:vpls", ("vpls", Snmp.Notification.Vpls)), ("Cisco-IOS-XR-l2vpn-cfg:l2vpn", ("l2vpn", Snmp.Notification.L2vpn)), ("Cisco-IOS-XR-snmp-entitymib-cfg:entity", ("entity_", Snmp.Notification.Entity)), ("Cisco-IOS-XR-snmp-bridgemib-cfg:bridge", ("bridge", Snmp.Notification.Bridge)), ("Cisco-IOS-XR-snmp-mib-rfmib-cfg:rf", ("rf", Snmp.Notification.Rf)), ("Cisco-IOS-XR-ip-ntp-cfg:ntp", ("ntp", Snmp.Notification.Ntp)), ("Cisco-IOS-XR-otnifmib-cfg:otn", ("otn", Snmp.Notification.Otn)), ("Cisco-IOS-XR-ip-daps-mib-cfg:addresspool-mib", ("addresspool_mib", Snmp.Notification.AddresspoolMib)), ("Cisco-IOS-XR-infra-systemmib-cfg:system", ("system", Snmp.Notification.System)), ("Cisco-IOS-XR-ip-rsvp-cfg:rsvp", ("rsvp", Snmp.Notification.Rsvp)), ("Cisco-IOS-XR-snmp-ciscosensormib-cfg:sensor", ("sensor", Snmp.Notification.Sensor)), ("Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp", ("mpls_ldp", Snmp.Notification.MplsLdp)), ("Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber-mib", ("subscriber_mib", Snmp.Notification.SubscriberMib)), ("Cisco-IOS-XR-flashmib-cfg:flash", ("flash", Snmp.Notification.Flash)), ("Cisco-IOS-XR-infra-confcopymib-cfg:config-copy", ("config_copy", Snmp.Notification.ConfigCopy)), ("Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp", ("hsrp", Snmp.Notification.Hsrp)), ("Cisco-IOS-XR-infra-ceredundancymib-cfg:entity-redundancy", ("entity_redundancy", Snmp.Notification.EntityRedundancy)), ("Cisco-IOS-XR-clns-isis-cfg:isis", ("isis", Snmp.Notification.Isis)), ("Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp", ("vrrp", Snmp.Notification.Vrrp)), ("Cisco-IOS-XR-crypto-mibs-ipsecflowmon-cfg:ip-sec", ("ip_sec", Snmp.Notification.IpSec)), ("Cisco-IOS-XR-crypto-mibs-ipsecflowmon-cfg:isakmp", ("isakmp", Snmp.Notification.Isakmp)), ("Cisco-IOS-XR-snmp-entityextmib-cfg:cisco-entity-ext", ("cisco_entity_ext", Snmp.Notification.CiscoEntityExt)), ("Cisco-IOS-XR-ipv4-ospf-cfg:ospf", ("ospf", Snmp.Notification.Ospf)), ("Cisco-IOS-XR-ethernet-cfm-cfg:cfm", ("cfm", Snmp.Notification.Cfm)), ("Cisco-IOS-XR-tunnel-l2tun-proto-mibs-cfg:l2tun", ("l2tun", Snmp.Notification.L2tun)), ("Cisco-IOS-XR-ipv4-bgp-cfg:bgp", ("bgp", Snmp.Notification.Bgp)), ("Cisco-IOS-XR-snmp-entstatemib-cfg:entity-state", ("entity_state", Snmp.Notification.EntityState)), ("Cisco-IOS-XR-freqsync-cfg:frequency-synchronization", ("frequency_synchronization", Snmp.Notification.FrequencySynchronization)), ("Cisco-IOS-XR-mpls-te-cfg:mpls-te-p2mp", ("mpls_te_p2mp", Snmp.Notification.MplsTeP2mp)), ("Cisco-IOS-XR-mpls-te-cfg:mpls-te", ("mpls_te", Snmp.Notification.MplsTe)), ("Cisco-IOS-XR-mpls-te-cfg:mpls-frr", ("mpls_frr", Snmp.Notification.MplsFrr)), ("Cisco-IOS-XR-ethernet-link-oam-cfg:oam", ("oam", Snmp.Notification.Oam)), ("Cisco-IOS-XR-mpls-vpn-cfg:mpls-l3vpn", ("mpls_l3vpn", Snmp.Notification.MplsL3vpn)), ("Cisco-IOS-XR-config-mibs-cfg:config-man", ("config_man", Snmp.Notification.ConfigMan)), ("Cisco-IOS-XR-aaa-diameter-base-mib-cfg:diametermib", ("diametermib", Snmp.Notification.Diametermib)), ("Cisco-IOS-XR-snmp-frucontrolmib-cfg:fru-control", ("fru_control", Snmp.Notification.FruControl)), ("Cisco-IOS-XR-snmp-syslogmib-cfg:syslog", ("syslog", Snmp.Notification.Syslog)), ("Cisco-IOS-XR-ip-bfd-cfg:bfd", ("bfd", Snmp.Notification.Bfd)), ("Cisco-IOS-XR-opticalotsmib-cfg:optical-ots", ("optical_ots", Snmp.Notification.OpticalOts)), ("Cisco-IOS-XR-opticalmib-cfg:optical", ("optical", Snmp.Notification.Optical)), ("Cisco-IOS-XR-ipv6-ospfv3-cfg:ospfv3", ("ospfv3", Snmp.Notification.Ospfv3))])
            self._leafs = OrderedDict([
                ('ipsla', (YLeaf(YType.boolean, 'Cisco-IOS-XR-man-ipsla-cfg:ipsla'), ['bool'])),
            ])
            self.ipsla = None

            self.snmp = Snmp.Notification.Snmp_()
            self.snmp.parent = self
            self._children_name_map["snmp"] = "snmp"

            self.selective_vrf_download = Snmp.Notification.SelectiveVrfDownload()
            self.selective_vrf_download.parent = self
            self._children_name_map["selective_vrf_download"] = "Cisco-IOS-XR-infra-rsi-cfg:selective-vrf-download"

            self.vpls = Snmp.Notification.Vpls()
            self.vpls.parent = self
            self._children_name_map["vpls"] = "Cisco-IOS-XR-l2vpn-cfg:vpls"

            self.l2vpn = Snmp.Notification.L2vpn()
            self.l2vpn.parent = self
            self._children_name_map["l2vpn"] = "Cisco-IOS-XR-l2vpn-cfg:l2vpn"

            self.entity_ = Snmp.Notification.Entity()
            self.entity_.parent = self
            self._children_name_map["entity_"] = "Cisco-IOS-XR-snmp-entitymib-cfg:entity"

            self.bridge = Snmp.Notification.Bridge()
            self.bridge.parent = self
            self._children_name_map["bridge"] = "Cisco-IOS-XR-snmp-bridgemib-cfg:bridge"

            self.rf = Snmp.Notification.Rf()
            self.rf.parent = self
            self._children_name_map["rf"] = "Cisco-IOS-XR-snmp-mib-rfmib-cfg:rf"

            self.ntp = Snmp.Notification.Ntp()
            self.ntp.parent = self
            self._children_name_map["ntp"] = "Cisco-IOS-XR-ip-ntp-cfg:ntp"

            self.otn = Snmp.Notification.Otn()
            self.otn.parent = self
            self._children_name_map["otn"] = "Cisco-IOS-XR-otnifmib-cfg:otn"

            self.addresspool_mib = Snmp.Notification.AddresspoolMib()
            self.addresspool_mib.parent = self
            self._children_name_map["addresspool_mib"] = "Cisco-IOS-XR-ip-daps-mib-cfg:addresspool-mib"

            self.system = Snmp.Notification.System()
            self.system.parent = self
            self._children_name_map["system"] = "Cisco-IOS-XR-infra-systemmib-cfg:system"

            self.rsvp = Snmp.Notification.Rsvp()
            self.rsvp.parent = self
            self._children_name_map["rsvp"] = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp"

            self.sensor = Snmp.Notification.Sensor()
            self.sensor.parent = self
            self._children_name_map["sensor"] = "Cisco-IOS-XR-snmp-ciscosensormib-cfg:sensor"

            self.mpls_ldp = Snmp.Notification.MplsLdp()
            self.mpls_ldp.parent = self
            self._children_name_map["mpls_ldp"] = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp"

            self.subscriber_mib = Snmp.Notification.SubscriberMib()
            self.subscriber_mib.parent = self
            self._children_name_map["subscriber_mib"] = "Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber-mib"

            self.flash = Snmp.Notification.Flash()
            self.flash.parent = self
            self._children_name_map["flash"] = "Cisco-IOS-XR-flashmib-cfg:flash"

            self.config_copy = Snmp.Notification.ConfigCopy()
            self.config_copy.parent = self
            self._children_name_map["config_copy"] = "Cisco-IOS-XR-infra-confcopymib-cfg:config-copy"

            self.hsrp = Snmp.Notification.Hsrp()
            self.hsrp.parent = self
            self._children_name_map["hsrp"] = "Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp"

            self.entity_redundancy = Snmp.Notification.EntityRedundancy()
            self.entity_redundancy.parent = self
            self._children_name_map["entity_redundancy"] = "Cisco-IOS-XR-infra-ceredundancymib-cfg:entity-redundancy"

            self.isis = Snmp.Notification.Isis()
            self.isis.parent = self
            self._children_name_map["isis"] = "Cisco-IOS-XR-clns-isis-cfg:isis"

            self.vrrp = Snmp.Notification.Vrrp()
            self.vrrp.parent = self
            self._children_name_map["vrrp"] = "Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp"

            self.ip_sec = Snmp.Notification.IpSec()
            self.ip_sec.parent = self
            self._children_name_map["ip_sec"] = "Cisco-IOS-XR-crypto-mibs-ipsecflowmon-cfg:ip-sec"

            self.isakmp = Snmp.Notification.Isakmp()
            self.isakmp.parent = self
            self._children_name_map["isakmp"] = "Cisco-IOS-XR-crypto-mibs-ipsecflowmon-cfg:isakmp"

            self.cisco_entity_ext = Snmp.Notification.CiscoEntityExt()
            self.cisco_entity_ext.parent = self
            self._children_name_map["cisco_entity_ext"] = "Cisco-IOS-XR-snmp-entityextmib-cfg:cisco-entity-ext"

            self.ospf = Snmp.Notification.Ospf()
            self.ospf.parent = self
            self._children_name_map["ospf"] = "Cisco-IOS-XR-ipv4-ospf-cfg:ospf"

            self.cfm = Snmp.Notification.Cfm()
            self.cfm.parent = self
            self._children_name_map["cfm"] = "Cisco-IOS-XR-ethernet-cfm-cfg:cfm"

            self.l2tun = Snmp.Notification.L2tun()
            self.l2tun.parent = self
            self._children_name_map["l2tun"] = "Cisco-IOS-XR-tunnel-l2tun-proto-mibs-cfg:l2tun"

            self.bgp = Snmp.Notification.Bgp()
            self.bgp.parent = self
            self._children_name_map["bgp"] = "Cisco-IOS-XR-ipv4-bgp-cfg:bgp"

            self.entity_state = Snmp.Notification.EntityState()
            self.entity_state.parent = self
            self._children_name_map["entity_state"] = "Cisco-IOS-XR-snmp-entstatemib-cfg:entity-state"

            self.frequency_synchronization = Snmp.Notification.FrequencySynchronization()
            self.frequency_synchronization.parent = self
            self._children_name_map["frequency_synchronization"] = "Cisco-IOS-XR-freqsync-cfg:frequency-synchronization"

            self.mpls_te_p2mp = Snmp.Notification.MplsTeP2mp()
            self.mpls_te_p2mp.parent = self
            self._children_name_map["mpls_te_p2mp"] = "Cisco-IOS-XR-mpls-te-cfg:mpls-te-p2mp"

            self.mpls_te = Snmp.Notification.MplsTe()
            self.mpls_te.parent = self
            self._children_name_map["mpls_te"] = "Cisco-IOS-XR-mpls-te-cfg:mpls-te"

            self.mpls_frr = Snmp.Notification.MplsFrr()
            self.mpls_frr.parent = self
            self._children_name_map["mpls_frr"] = "Cisco-IOS-XR-mpls-te-cfg:mpls-frr"

            self.oam = Snmp.Notification.Oam()
            self.oam.parent = self
            self._children_name_map["oam"] = "Cisco-IOS-XR-ethernet-link-oam-cfg:oam"

            self.mpls_l3vpn = Snmp.Notification.MplsL3vpn()
            self.mpls_l3vpn.parent = self
            self._children_name_map["mpls_l3vpn"] = "Cisco-IOS-XR-mpls-vpn-cfg:mpls-l3vpn"

            self.config_man = Snmp.Notification.ConfigMan()
            self.config_man.parent = self
            self._children_name_map["config_man"] = "Cisco-IOS-XR-config-mibs-cfg:config-man"

            self.diametermib = Snmp.Notification.Diametermib()
            self.diametermib.parent = self
            self._children_name_map["diametermib"] = "Cisco-IOS-XR-aaa-diameter-base-mib-cfg:diametermib"

            self.fru_control = Snmp.Notification.FruControl()
            self.fru_control.parent = self
            self._children_name_map["fru_control"] = "Cisco-IOS-XR-snmp-frucontrolmib-cfg:fru-control"

            self.syslog = Snmp.Notification.Syslog()
            self.syslog.parent = self
            self._children_name_map["syslog"] = "Cisco-IOS-XR-snmp-syslogmib-cfg:syslog"

            self.bfd = Snmp.Notification.Bfd()
            self.bfd.parent = self
            self._children_name_map["bfd"] = "Cisco-IOS-XR-ip-bfd-cfg:bfd"

            self.optical_ots = Snmp.Notification.OpticalOts()
            self.optical_ots.parent = self
            self._children_name_map["optical_ots"] = "Cisco-IOS-XR-opticalotsmib-cfg:optical-ots"

            self.optical = Snmp.Notification.Optical()
            self.optical.parent = self
            self._children_name_map["optical"] = "Cisco-IOS-XR-opticalmib-cfg:optical"

            self.ospfv3 = Snmp.Notification.Ospfv3()
            self.ospfv3.parent = self
            self._children_name_map["ospfv3"] = "Cisco-IOS-XR-ipv6-ospfv3-cfg:ospfv3"
            self._segment_path = lambda: "notification"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Notification, ['ipsla'], name, value)


        class Snmp_(_Entity_):
            """
            SNMP notification configuration
            
            .. attribute:: authentication
            
            	Enable authentication notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: cold_start
            
            	Enable cold start notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: warm_start
            
            	Enable warm start notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable
            
            	Enable SNMP notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: link_down
            
            	Enable link down notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: link_up
            
            	Enable link up notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Snmp_, self).__init__()

                self.yang_name = "snmp"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('authentication', (YLeaf(YType.empty, 'authentication'), ['Empty'])),
                    ('cold_start', (YLeaf(YType.empty, 'cold-start'), ['Empty'])),
                    ('warm_start', (YLeaf(YType.empty, 'warm-start'), ['Empty'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ('link_down', (YLeaf(YType.empty, 'Cisco-IOS-XR-snmp-ifmib-cfg:link-down'), ['Empty'])),
                    ('link_up', (YLeaf(YType.empty, 'Cisco-IOS-XR-snmp-ifmib-cfg:link-up'), ['Empty'])),
                ])
                self.authentication = None
                self.cold_start = None
                self.warm_start = None
                self.enable = None
                self.link_down = None
                self.link_up = None
                self._segment_path = lambda: "snmp"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Snmp_, ['authentication', 'cold_start', 'warm_start', 'enable', 'link_down', 'link_up'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Snmp_']['meta_info']


        class SelectiveVrfDownload(_Entity_):
            """
            CISCO\-SELECTIVE\-VRF\-DOWNLOAD\-MIB notification
            configuration
            
            .. attribute:: role_change
            
            	Enable csvdEntityRoleChangeNotification notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2018-06-15'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.SelectiveVrfDownload, self).__init__()

                self.yang_name = "selective-vrf-download"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('role_change', (YLeaf(YType.empty, 'role-change'), ['Empty'])),
                ])
                self.role_change = None
                self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:selective-vrf-download"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.SelectiveVrfDownload, ['role_change'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.SelectiveVrfDownload']['meta_info']


        class Vpls(_Entity_):
            """
            CISCO\-IETF\-VPLS\-GENERIC\-MIB notification
            configuration
            
            .. attribute:: full_clear
            
            	Enable cvplsFwdFullAlarmCleared notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: status
            
            	Enable cvplsStatusChanged notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable
            
            	Enable CISCO\-IETF\-VPLS\-GENERIC\-MIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: full_raise
            
            	Enable cvplsFwdFullAlarmRaised notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2018-06-15'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Vpls, self).__init__()

                self.yang_name = "vpls"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('full_clear', (YLeaf(YType.empty, 'full-clear'), ['Empty'])),
                    ('status', (YLeaf(YType.empty, 'status'), ['Empty'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ('full_raise', (YLeaf(YType.empty, 'full-raise'), ['Empty'])),
                ])
                self.full_clear = None
                self.status = None
                self.enable = None
                self.full_raise = None
                self._segment_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:vpls"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Vpls, ['full_clear', 'status', 'enable', 'full_raise'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Vpls']['meta_info']


        class L2vpn(_Entity_):
            """
            CISCO\-IETF\-PW\-MIB notification configuration
            
            .. attribute:: cisco
            
            	Enable Cisco format including extra varbinds
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable
            
            	Enable CISCO\-IETF\-PW\-MIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: vc_down
            
            	Enable cpwVcDown notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: vc_up
            
            	Enable cpwVcUp notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2018-06-15'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.L2vpn, self).__init__()

                self.yang_name = "l2vpn"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cisco', (YLeaf(YType.empty, 'cisco'), ['Empty'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ('vc_down', (YLeaf(YType.empty, 'vc-down'), ['Empty'])),
                    ('vc_up', (YLeaf(YType.empty, 'vc-up'), ['Empty'])),
                ])
                self.cisco = None
                self.enable = None
                self.vc_down = None
                self.vc_up = None
                self._segment_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.L2vpn, ['cisco', 'enable', 'vc_down', 'vc_up'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.L2vpn']['meta_info']


        class Entity(_Entity_):
            """
            Enable ENTITY\-MIB notifications
            
            .. attribute:: enable
            
            	Enable entityMIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-entitymib-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Entity, self).__init__()

                self.yang_name = "entity"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-snmp-entitymib-cfg:entity"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Entity, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Entity']['meta_info']


        class Bridge(_Entity_):
            """
            BRIDGE\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable dot1dBridge notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-bridgemib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Bridge, self).__init__()

                self.yang_name = "bridge"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-snmp-bridgemib-cfg:bridge"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Bridge, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Bridge']['meta_info']


        class Rf(_Entity_):
            """
            CISCO\-RF\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable ciscoRFMIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-mib-rfmib-cfg'
            _revision = '2016-05-13'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Rf, self).__init__()

                self.yang_name = "rf"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-snmp-mib-rfmib-cfg:rf"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Rf, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Rf']['meta_info']


        class Ntp(_Entity_):
            """
            CISCO\-NTP\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable ciscoNtpMIB notification configuration
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Ntp, self).__init__()

                self.yang_name = "ntp"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Ntp, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Ntp']['meta_info']


        class Otn(_Entity_):
            """
            CISCO\-OTN\-IF\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable ciscoOtnIfMIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'otnifmib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Otn, self).__init__()

                self.yang_name = "otn"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-otnifmib-cfg:otn"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Otn, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Otn']['meta_info']


        class AddresspoolMib(_Entity_):
            """
            Enable SNMP daps traps
            
            .. attribute:: high
            
            	Enable SNMP Address Pool High Threshold trap
            	**type**\: bool
            
            .. attribute:: low
            
            	Enable SNMP Address Pool Low Threshold trap
            	**type**\: bool
            
            

            """

            _prefix = 'ip-daps-mib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.AddresspoolMib, self).__init__()

                self.yang_name = "addresspool-mib"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('high', (YLeaf(YType.boolean, 'high'), ['bool'])),
                    ('low', (YLeaf(YType.boolean, 'low'), ['bool'])),
                ])
                self.high = None
                self.low = None
                self._segment_path = lambda: "Cisco-IOS-XR-ip-daps-mib-cfg:addresspool-mib"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.AddresspoolMib, ['high', 'low'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.AddresspoolMib']['meta_info']


        class System(_Entity_):
            """
            CISCO\-SYSTEM\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable ciscoSystemMIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-systemmib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.System, self).__init__()

                self.yang_name = "system"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-infra-systemmib-cfg:system"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.System, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.System']['meta_info']


        class Rsvp(_Entity_):
            """
            Enable RSVP\-MIB notifications
            
            .. attribute:: lost_flow
            
            	Enable lostFlow notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: new_flow
            
            	Enable newFlow notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable
            
            	Enable all RSVP notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2019-09-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Rsvp, self).__init__()

                self.yang_name = "rsvp"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lost_flow', (YLeaf(YType.empty, 'lost-flow'), ['Empty'])),
                    ('new_flow', (YLeaf(YType.empty, 'new-flow'), ['Empty'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.lost_flow = None
                self.new_flow = None
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Rsvp, ['lost_flow', 'new_flow', 'enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Rsvp']['meta_info']


        class Sensor(_Entity_):
            """
            CISCO\-ENTITY\-SENSOR\-MIB notification
            configuration
            
            .. attribute:: enable
            
            	Enable entitySensorMIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-ciscosensormib-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Sensor, self).__init__()

                self.yang_name = "sensor"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-snmp-ciscosensormib-cfg:sensor"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Sensor, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Sensor']['meta_info']


        class MplsLdp(_Entity_):
            """
            MPLS\-LDP\-STD\-MIB notification configuration
            
            .. attribute:: session_up
            
            	Enable mplsLdpSessionUp notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: init_session_threshold_exceeded
            
            	Enable mplsLdpInitSessionThresholdExceeded notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: session_down
            
            	Enable mplsLdpSessionDown notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2018-06-15'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.MplsLdp, self).__init__()

                self.yang_name = "mpls-ldp"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('session_up', (YLeaf(YType.empty, 'session-up'), ['Empty'])),
                    ('init_session_threshold_exceeded', (YLeaf(YType.empty, 'init-session-threshold-exceeded'), ['Empty'])),
                    ('session_down', (YLeaf(YType.empty, 'session-down'), ['Empty'])),
                ])
                self.session_up = None
                self.init_session_threshold_exceeded = None
                self.session_down = None
                self._segment_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.MplsLdp, ['session_up', 'init_session_threshold_exceeded', 'session_down'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.MplsLdp']['meta_info']


        class SubscriberMib(_Entity_):
            """
            Subscriber notification commands
            
            .. attribute:: session_aggregate
            
            	Session aggregation
            	**type**\:  :py:class:`SessionAggregate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.SubscriberMib.SessionAggregate>`
            
            

            """

            _prefix = 'subscriber-session-mon-mibs-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.SubscriberMib, self).__init__()

                self.yang_name = "subscriber-mib"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("session-aggregate", ("session_aggregate", Snmp.Notification.SubscriberMib.SessionAggregate))])
                self._leafs = OrderedDict()

                self.session_aggregate = Snmp.Notification.SubscriberMib.SessionAggregate()
                self.session_aggregate.parent = self
                self._children_name_map["session_aggregate"] = "session-aggregate"
                self._segment_path = lambda: "Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber-mib"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.SubscriberMib, [], name, value)


            class SessionAggregate(_Entity_):
                """
                Session aggregation
                
                .. attribute:: node
                
                	Subscriber notification at node level
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: access_interface
                
                	Subscriber notification at access interface level
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'subscriber-session-mon-mibs-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Notification.SubscriberMib.SessionAggregate, self).__init__()

                    self.yang_name = "session-aggregate"
                    self.yang_parent_name = "subscriber-mib"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('node', (YLeaf(YType.empty, 'node'), ['Empty'])),
                        ('access_interface', (YLeaf(YType.empty, 'access-interface'), ['Empty'])),
                    ])
                    self.node = None
                    self.access_interface = None
                    self._segment_path = lambda: "session-aggregate"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber-mib/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.SubscriberMib.SessionAggregate, ['node', 'access_interface'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.SubscriberMib.SessionAggregate']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.SubscriberMib']['meta_info']


        class Flash(_Entity_):
            """
            CISCO\-FLASH\-MIB notification configuration
            
            .. attribute:: insertion
            
            	Enable ciscoFlashDeviceInsertedNotif notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: removal
            
            	Enable ciscoFlashDeviceRemovedNotif notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'flashmib-cfg'
            _revision = '2015-12-15'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Flash, self).__init__()

                self.yang_name = "flash"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('insertion', (YLeaf(YType.empty, 'insertion'), ['Empty'])),
                    ('removal', (YLeaf(YType.empty, 'removal'), ['Empty'])),
                ])
                self.insertion = None
                self.removal = None
                self._segment_path = lambda: "Cisco-IOS-XR-flashmib-cfg:flash"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Flash, ['insertion', 'removal'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Flash']['meta_info']


        class ConfigCopy(_Entity_):
            """
            CISCO\-CONFIG\-COPY\-MIB notification configuration
            
            .. attribute:: completion
            
            	Enable ccCopyCompletion notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-confcopymib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.ConfigCopy, self).__init__()

                self.yang_name = "config-copy"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('completion', (YLeaf(YType.empty, 'completion'), ['Empty'])),
                ])
                self.completion = None
                self._segment_path = lambda: "Cisco-IOS-XR-infra-confcopymib-cfg:config-copy"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.ConfigCopy, ['completion'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.ConfigCopy']['meta_info']


        class Hsrp(_Entity_):
            """
            CISCO\-HSRP\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable CISCO\-HSRP\-MIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ipv4-hsrp-cfg'
            _revision = '2017-11-05'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Hsrp, self).__init__()

                self.yang_name = "hsrp"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Hsrp, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Hsrp']['meta_info']


        class EntityRedundancy(_Entity_):
            """
            CISCO\-ENTITY\-REDUNDANCY\-MIB notification
            configuration
            
            .. attribute:: switchover
            
            	Enable switchover notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable
            
            	Enable CISCO\-ENTITY\-REDUNDANCY\-MIB notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: status
            
            	Enable status change notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-ceredundancymib-cfg'
            _revision = '2015-01-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.EntityRedundancy, self).__init__()

                self.yang_name = "entity-redundancy"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('switchover', (YLeaf(YType.empty, 'switchover'), ['Empty'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ('status', (YLeaf(YType.empty, 'status'), ['Empty'])),
                ])
                self.switchover = None
                self.enable = None
                self.status = None
                self._segment_path = lambda: "Cisco-IOS-XR-infra-ceredundancymib-cfg:entity-redundancy"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.EntityRedundancy, ['switchover', 'enable', 'status'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.EntityRedundancy']['meta_info']


        class Isis(_Entity_):
            """
            Enable ISIS\-MIB notifications
            
            .. attribute:: database_overflow
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibDatabaseOverFlowBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibDatabaseOverFlowBoolean>`
            
            	**default value**\: false
            
            .. attribute:: manual_address_drops
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibManualAddressDropsBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibManualAddressDropsBoolean>`
            
            	**default value**\: false
            
            .. attribute:: corrupted_lsp_detected
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibCorruptedLspDetectedBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibCorruptedLspDetectedBoolean>`
            
            	**default value**\: false
            
            .. attribute:: attempt_to_exceed_max_sequence
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibAttemptToExceedMaxSequenceBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAttemptToExceedMaxSequenceBoolean>`
            
            	**default value**\: false
            
            .. attribute:: id_length_mismatch
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibIdLengthMismatchBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibIdLengthMismatchBoolean>`
            
            	**default value**\: false
            
            .. attribute:: max_area_address_mismatch
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibMaxAreaAddressMismatchBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibMaxAreaAddressMismatchBoolean>`
            
            	**default value**\: false
            
            .. attribute:: own_lsp_purge
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibOwnLspPurgeBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibOwnLspPurgeBoolean>`
            
            	**default value**\: false
            
            .. attribute:: sequence_number_skip
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibSequenceNumberSkipBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibSequenceNumberSkipBoolean>`
            
            	**default value**\: false
            
            .. attribute:: authentication_type_failure
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibAuthenticationTypeFailureBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAuthenticationTypeFailureBoolean>`
            
            	**default value**\: false
            
            .. attribute:: authentication_failure
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibAuthenticationFailureBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAuthenticationFailureBoolean>`
            
            	**default value**\: false
            
            .. attribute:: version_skew
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibVersionSkewBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibVersionSkewBoolean>`
            
            	**default value**\: false
            
            .. attribute:: area_mismatch
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibAreaMismatchBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAreaMismatchBoolean>`
            
            	**default value**\: false
            
            .. attribute:: rejected_adjacency
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibRejectedAdjacencyBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibRejectedAdjacencyBoolean>`
            
            	**default value**\: false
            
            .. attribute:: lsp_too_large_to_propagate
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibLspTooLargeToPropagateBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibLspTooLargeToPropagateBoolean>`
            
            	**default value**\: false
            
            .. attribute:: originated_lsp_buffer_size_mismatch
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibOriginatedLspBufferSizeMismatchBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibOriginatedLspBufferSizeMismatchBoolean>`
            
            	**default value**\: false
            
            .. attribute:: protocols_supported_mismatch
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibProtocolsSupportedMismatchBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibProtocolsSupportedMismatchBoolean>`
            
            	**default value**\: false
            
            .. attribute:: adjacency_change
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibAdjacencyChangeBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAdjacencyChangeBoolean>`
            
            	**default value**\: false
            
            .. attribute:: lsp_error_detected
            
            	Enable or disable
            	**type**\:  :py:class:`IsisMibLspErrorDetectedBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibLspErrorDetectedBoolean>`
            
            	**default value**\: false
            
            .. attribute:: all
            
            	Enable all isisMIB notifications
            	**type**\:  :py:class:`IsisMibAllBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAllBoolean>`
            
            	**default value**\: false
            
            

            """

            _prefix = 'clns-isis-cfg'
            _revision = '2019-03-15'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Isis, self).__init__()

                self.yang_name = "isis"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('database_overflow', (YLeaf(YType.enumeration, 'database-overflow'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibDatabaseOverFlowBoolean', '')])),
                    ('manual_address_drops', (YLeaf(YType.enumeration, 'manual-address-drops'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibManualAddressDropsBoolean', '')])),
                    ('corrupted_lsp_detected', (YLeaf(YType.enumeration, 'corrupted-lsp-detected'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibCorruptedLspDetectedBoolean', '')])),
                    ('attempt_to_exceed_max_sequence', (YLeaf(YType.enumeration, 'attempt-to-exceed-max-sequence'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAttemptToExceedMaxSequenceBoolean', '')])),
                    ('id_length_mismatch', (YLeaf(YType.enumeration, 'id-length-mismatch'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibIdLengthMismatchBoolean', '')])),
                    ('max_area_address_mismatch', (YLeaf(YType.enumeration, 'max-area-address-mismatch'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibMaxAreaAddressMismatchBoolean', '')])),
                    ('own_lsp_purge', (YLeaf(YType.enumeration, 'own-lsp-purge'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibOwnLspPurgeBoolean', '')])),
                    ('sequence_number_skip', (YLeaf(YType.enumeration, 'sequence-number-skip'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibSequenceNumberSkipBoolean', '')])),
                    ('authentication_type_failure', (YLeaf(YType.enumeration, 'authentication-type-failure'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAuthenticationTypeFailureBoolean', '')])),
                    ('authentication_failure', (YLeaf(YType.enumeration, 'authentication-failure'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAuthenticationFailureBoolean', '')])),
                    ('version_skew', (YLeaf(YType.enumeration, 'version-skew'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibVersionSkewBoolean', '')])),
                    ('area_mismatch', (YLeaf(YType.enumeration, 'area-mismatch'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAreaMismatchBoolean', '')])),
                    ('rejected_adjacency', (YLeaf(YType.enumeration, 'rejected-adjacency'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibRejectedAdjacencyBoolean', '')])),
                    ('lsp_too_large_to_propagate', (YLeaf(YType.enumeration, 'lsp-too-large-to-propagate'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibLspTooLargeToPropagateBoolean', '')])),
                    ('originated_lsp_buffer_size_mismatch', (YLeaf(YType.enumeration, 'originated-lsp-buffer-size-mismatch'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibOriginatedLspBufferSizeMismatchBoolean', '')])),
                    ('protocols_supported_mismatch', (YLeaf(YType.enumeration, 'protocols-supported-mismatch'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibProtocolsSupportedMismatchBoolean', '')])),
                    ('adjacency_change', (YLeaf(YType.enumeration, 'adjacency-change'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAdjacencyChangeBoolean', '')])),
                    ('lsp_error_detected', (YLeaf(YType.enumeration, 'lsp-error-detected'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibLspErrorDetectedBoolean', '')])),
                    ('all', (YLeaf(YType.enumeration, 'all'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAllBoolean', '')])),
                ])
                self.database_overflow = None
                self.manual_address_drops = None
                self.corrupted_lsp_detected = None
                self.attempt_to_exceed_max_sequence = None
                self.id_length_mismatch = None
                self.max_area_address_mismatch = None
                self.own_lsp_purge = None
                self.sequence_number_skip = None
                self.authentication_type_failure = None
                self.authentication_failure = None
                self.version_skew = None
                self.area_mismatch = None
                self.rejected_adjacency = None
                self.lsp_too_large_to_propagate = None
                self.originated_lsp_buffer_size_mismatch = None
                self.protocols_supported_mismatch = None
                self.adjacency_change = None
                self.lsp_error_detected = None
                self.all = None
                self._segment_path = lambda: "Cisco-IOS-XR-clns-isis-cfg:isis"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Isis, ['database_overflow', 'manual_address_drops', 'corrupted_lsp_detected', 'attempt_to_exceed_max_sequence', 'id_length_mismatch', 'max_area_address_mismatch', 'own_lsp_purge', 'sequence_number_skip', 'authentication_type_failure', 'authentication_failure', 'version_skew', 'area_mismatch', 'rejected_adjacency', 'lsp_too_large_to_propagate', 'originated_lsp_buffer_size_mismatch', 'protocols_supported_mismatch', 'adjacency_change', 'lsp_error_detected', 'all'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Isis']['meta_info']


        class Vrrp(_Entity_):
            """
            VRRP\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable VRRP\-MIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ipv4-vrrp-cfg'
            _revision = '2018-05-19'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Vrrp, self).__init__()

                self.yang_name = "vrrp"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Vrrp, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Vrrp']['meta_info']


        class IpSec(_Entity_):
            """
            Enable CISCO\-IPSEC\-FLOW\-MONITOR\-MIB
            notifications
            
            .. attribute:: tunnel_stop
            
            	Enable cipSecTunnelStop notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: tunnel_start
            
            	Enable cipSecTunnelStart notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'crypto-mibs-ipsecflowmon-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.IpSec, self).__init__()

                self.yang_name = "ip-sec"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tunnel_stop', (YLeaf(YType.empty, 'tunnel-stop'), ['Empty'])),
                    ('tunnel_start', (YLeaf(YType.empty, 'tunnel-start'), ['Empty'])),
                ])
                self.tunnel_stop = None
                self.tunnel_start = None
                self._segment_path = lambda: "Cisco-IOS-XR-crypto-mibs-ipsecflowmon-cfg:ip-sec"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.IpSec, ['tunnel_stop', 'tunnel_start'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.IpSec']['meta_info']


        class Isakmp(_Entity_):
            """
            Enable CISCO\-IPSEC\-FLOW\-MONITOR\-MIB
            notifications
            
            .. attribute:: tunnel_stop
            
            	Enable cikeTunnelStop notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: tunnel_start
            
            	Enable cikeTunnelStart notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'crypto-mibs-ipsecflowmon-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Isakmp, self).__init__()

                self.yang_name = "isakmp"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tunnel_stop', (YLeaf(YType.empty, 'tunnel-stop'), ['Empty'])),
                    ('tunnel_start', (YLeaf(YType.empty, 'tunnel-start'), ['Empty'])),
                ])
                self.tunnel_stop = None
                self.tunnel_start = None
                self._segment_path = lambda: "Cisco-IOS-XR-crypto-mibs-ipsecflowmon-cfg:isakmp"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Isakmp, ['tunnel_stop', 'tunnel_start'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Isakmp']['meta_info']


        class CiscoEntityExt(_Entity_):
            """
            Enable CISCO\-ENTITY\-EXT\-MIB notifications
            
            .. attribute:: enable
            
            	Enable CISCO\-ENTITY\-EXT\-MIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-entityextmib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.CiscoEntityExt, self).__init__()

                self.yang_name = "cisco-entity-ext"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-snmp-entityextmib-cfg:cisco-entity-ext"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.CiscoEntityExt, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.CiscoEntityExt']['meta_info']


        class Ospf(_Entity_):
            """
            OSPF\-MIB notification configuration
            
            .. attribute:: lsa
            
            	SNMP notifications related to LSAs
            	**type**\:  :py:class:`Lsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ospf.Lsa>`
            
            .. attribute:: state_change
            
            	SNMP notifications for OSPF state change
            	**type**\:  :py:class:`StateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ospf.StateChange>`
            
            .. attribute:: retransmit
            
            	SNMP notifications for packet retransmissions
            	**type**\:  :py:class:`Retransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ospf.Retransmit>`
            
            .. attribute:: error
            
            	SNMP notifications for OSPF errors
            	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ospf.Error>`
            
            

            """

            _prefix = 'ipv4-ospf-cfg'
            _revision = '2018-05-14'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Ospf, self).__init__()

                self.yang_name = "ospf"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("lsa", ("lsa", Snmp.Notification.Ospf.Lsa)), ("state-change", ("state_change", Snmp.Notification.Ospf.StateChange)), ("retransmit", ("retransmit", Snmp.Notification.Ospf.Retransmit)), ("error", ("error", Snmp.Notification.Ospf.Error))])
                self._leafs = OrderedDict()

                self.lsa = Snmp.Notification.Ospf.Lsa()
                self.lsa.parent = self
                self._children_name_map["lsa"] = "lsa"

                self.state_change = Snmp.Notification.Ospf.StateChange()
                self.state_change.parent = self
                self._children_name_map["state_change"] = "state-change"

                self.retransmit = Snmp.Notification.Ospf.Retransmit()
                self.retransmit.parent = self
                self._children_name_map["retransmit"] = "retransmit"

                self.error = Snmp.Notification.Ospf.Error()
                self.error.parent = self
                self._children_name_map["error"] = "error"
                self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ospf-cfg:ospf"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Ospf, [], name, value)


            class Lsa(_Entity_):
                """
                SNMP notifications related to LSAs
                
                .. attribute:: max_age_lsa
                
                	Enable ospfMaxAgeLsa notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: originate_lsa
                
                	Enable ospfOriginateLsa notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv4-ospf-cfg'
                _revision = '2018-05-14'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Notification.Ospf.Lsa, self).__init__()

                    self.yang_name = "lsa"
                    self.yang_parent_name = "ospf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('max_age_lsa', (YLeaf(YType.empty, 'max-age-lsa'), ['Empty'])),
                        ('originate_lsa', (YLeaf(YType.empty, 'originate-lsa'), ['Empty'])),
                    ])
                    self.max_age_lsa = None
                    self.originate_lsa = None
                    self._segment_path = lambda: "lsa"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-ipv4-ospf-cfg:ospf/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.Ospf.Lsa, ['max_age_lsa', 'originate_lsa'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.Ospf.Lsa']['meta_info']


            class StateChange(_Entity_):
                """
                SNMP notifications for OSPF state change
                
                .. attribute:: interface
                
                	Enable ospfIfStateChange notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_interface
                
                	Enable ospfVirtIfStateChange notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_neighbor
                
                	Enable ospfVirtNbrStateChange notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: neighbor
                
                	Enable ospfNbrStateChange notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv4-ospf-cfg'
                _revision = '2018-05-14'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Notification.Ospf.StateChange, self).__init__()

                    self.yang_name = "state-change"
                    self.yang_parent_name = "ospf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface', (YLeaf(YType.empty, 'interface'), ['Empty'])),
                        ('virtual_interface', (YLeaf(YType.empty, 'virtual-interface'), ['Empty'])),
                        ('virtual_neighbor', (YLeaf(YType.empty, 'virtual-neighbor'), ['Empty'])),
                        ('neighbor', (YLeaf(YType.empty, 'neighbor'), ['Empty'])),
                    ])
                    self.interface = None
                    self.virtual_interface = None
                    self.virtual_neighbor = None
                    self.neighbor = None
                    self._segment_path = lambda: "state-change"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-ipv4-ospf-cfg:ospf/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.Ospf.StateChange, ['interface', 'virtual_interface', 'virtual_neighbor', 'neighbor'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.Ospf.StateChange']['meta_info']


            class Retransmit(_Entity_):
                """
                SNMP notifications for packet retransmissions
                
                .. attribute:: virtual_packet
                
                	Enable ospfVirtIfTxRetransmit notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: packet
                
                	Enable ospfTxRetransmit notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv4-ospf-cfg'
                _revision = '2018-05-14'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Notification.Ospf.Retransmit, self).__init__()

                    self.yang_name = "retransmit"
                    self.yang_parent_name = "ospf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('virtual_packet', (YLeaf(YType.empty, 'virtual-packet'), ['Empty'])),
                        ('packet', (YLeaf(YType.empty, 'packet'), ['Empty'])),
                    ])
                    self.virtual_packet = None
                    self.packet = None
                    self._segment_path = lambda: "retransmit"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-ipv4-ospf-cfg:ospf/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.Ospf.Retransmit, ['virtual_packet', 'packet'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.Ospf.Retransmit']['meta_info']


            class Error(_Entity_):
                """
                SNMP notifications for OSPF errors
                
                .. attribute:: config_error
                
                	Enable ospfIfConfigError notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: authentication_failure
                
                	Enable ospfIfAuthFailure notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_config_error
                
                	Enable ospfVirtIfConfigError notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_authentication_failure
                
                	Enable ospfVirtIfAuthFailure notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: bad_packet
                
                	Enable ospfIfRxBadPacket notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_bad_packet
                
                	Enable ospfVirtIfRxBadPacket notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv4-ospf-cfg'
                _revision = '2018-05-14'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Notification.Ospf.Error, self).__init__()

                    self.yang_name = "error"
                    self.yang_parent_name = "ospf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('config_error', (YLeaf(YType.empty, 'config-error'), ['Empty'])),
                        ('authentication_failure', (YLeaf(YType.empty, 'authentication-failure'), ['Empty'])),
                        ('virtual_config_error', (YLeaf(YType.empty, 'virtual-config-error'), ['Empty'])),
                        ('virtual_authentication_failure', (YLeaf(YType.empty, 'virtual-authentication-failure'), ['Empty'])),
                        ('bad_packet', (YLeaf(YType.empty, 'bad-packet'), ['Empty'])),
                        ('virtual_bad_packet', (YLeaf(YType.empty, 'virtual-bad-packet'), ['Empty'])),
                    ])
                    self.config_error = None
                    self.authentication_failure = None
                    self.virtual_config_error = None
                    self.virtual_authentication_failure = None
                    self.bad_packet = None
                    self.virtual_bad_packet = None
                    self._segment_path = lambda: "error"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-ipv4-ospf-cfg:ospf/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.Ospf.Error, ['config_error', 'authentication_failure', 'virtual_config_error', 'virtual_authentication_failure', 'bad_packet', 'virtual_bad_packet'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.Ospf.Error']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Ospf']['meta_info']


        class Cfm(_Entity_):
            """
            802.1ag Connectivity Fault Management MIB
            notification configuration
            
            .. attribute:: enable
            
            	Enable 802.1ag Connectivity Fault Management MIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ethernet-cfm-cfg'
            _revision = '2018-07-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Cfm, self).__init__()

                self.yang_name = "cfm"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-ethernet-cfm-cfg:cfm"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Cfm, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Cfm']['meta_info']


        class L2tun(_Entity_):
            """
            Enable SNMP l2tun traps
            
            .. attribute:: tunnel_up
            
            	Enable L2TUN tunnel UP traps
            	**type**\: bool
            
            .. attribute:: tunnel_down
            
            	Enable L2TUN tunnel DOWN traps
            	**type**\: bool
            
            .. attribute:: pseudowire_status
            
            	Enable traps for L2TPv3 PW status
            	**type**\: bool
            
            .. attribute:: sessions
            
            	Enable L2TUN sessions traps
            	**type**\: bool
            
            

            """

            _prefix = 'tunnel-l2tun-proto-mibs-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.L2tun, self).__init__()

                self.yang_name = "l2tun"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tunnel_up', (YLeaf(YType.boolean, 'tunnel-up'), ['bool'])),
                    ('tunnel_down', (YLeaf(YType.boolean, 'tunnel-down'), ['bool'])),
                    ('pseudowire_status', (YLeaf(YType.boolean, 'pseudowire-status'), ['bool'])),
                    ('sessions', (YLeaf(YType.boolean, 'sessions'), ['bool'])),
                ])
                self.tunnel_up = None
                self.tunnel_down = None
                self.pseudowire_status = None
                self.sessions = None
                self._segment_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-proto-mibs-cfg:l2tun"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.L2tun, ['tunnel_up', 'tunnel_down', 'pseudowire_status', 'sessions'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.L2tun']['meta_info']


        class Bgp(_Entity_):
            """
            BGP4\-MIB and CISCO\-BGP4\-MIB notification
            configuration
            
            .. attribute:: bgp4mib
            
            	Enable BGP4\-MIB and CISCO\-BGP4\-MIB IPv4\-only notifications\: bgpEstablishedNotification, bgpBackwardTransNotification, cbgpFsmStateChange, cbgpBackwardTransition, cbgpPrefixThresholdExceeded, cbgpPrefixThresholdClear
            	**type**\:  :py:class:`Bgp4mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Bgp.Bgp4mib>`
            
            .. attribute:: cisco_bgp4mib
            
            	Enable CISCO\-BGP4\-MIB v2 notifications\: cbgpPeer2EstablishedNotification, cbgpPeer2BackwardTransNotification, cbgpPeer2FsmStateChange, cbgpPeer2BackwardTransition, cbgpPeer2PrefixThresholdExceeded, cbgpPeer2PrefixThresholdClear
            	**type**\:  :py:class:`CiscoBgp4mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Bgp.CiscoBgp4mib>`
            
            

            """

            _prefix = 'ipv4-bgp-cfg'
            _revision = '2018-06-15'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Bgp, self).__init__()

                self.yang_name = "bgp"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("bgp4mib", ("bgp4mib", Snmp.Notification.Bgp.Bgp4mib)), ("cisco-bgp4mib", ("cisco_bgp4mib", Snmp.Notification.Bgp.CiscoBgp4mib))])
                self._leafs = OrderedDict()

                self.bgp4mib = Snmp.Notification.Bgp.Bgp4mib()
                self.bgp4mib.parent = self
                self._children_name_map["bgp4mib"] = "bgp4mib"

                self.cisco_bgp4mib = Snmp.Notification.Bgp.CiscoBgp4mib()
                self.cisco_bgp4mib.parent = self
                self._children_name_map["cisco_bgp4mib"] = "cisco-bgp4mib"
                self._segment_path = lambda: "Cisco-IOS-XR-ipv4-bgp-cfg:bgp"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Bgp, [], name, value)


            class Bgp4mib(_Entity_):
                """
                Enable BGP4\-MIB and CISCO\-BGP4\-MIB IPv4\-only
                notifications\: bgpEstablishedNotification,
                bgpBackwardTransNotification,
                cbgpFsmStateChange, cbgpBackwardTransition,
                cbgpPrefixThresholdExceeded,
                cbgpPrefixThresholdClear.
                
                .. attribute:: enable
                
                	Enable BGP4\-MIB and CISCO\-BGP4\-MIB IPv4\-only notifications
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: up_down
                
                	Enable BGP4\-MIB and CISCO\-BGP4\-MIB IPv4\-only up/down notifications
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv4-bgp-cfg'
                _revision = '2018-06-15'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Notification.Bgp.Bgp4mib, self).__init__()

                    self.yang_name = "bgp4mib"
                    self.yang_parent_name = "bgp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ('up_down', (YLeaf(YType.empty, 'up-down'), ['Empty'])),
                    ])
                    self.enable = None
                    self.up_down = None
                    self._segment_path = lambda: "bgp4mib"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-ipv4-bgp-cfg:bgp/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.Bgp.Bgp4mib, ['enable', 'up_down'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.Bgp.Bgp4mib']['meta_info']


            class CiscoBgp4mib(_Entity_):
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
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: up_down
                
                	Enable CISCO\-BGP4\-MIB v2 up/down notifications
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv4-bgp-cfg'
                _revision = '2018-06-15'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Notification.Bgp.CiscoBgp4mib, self).__init__()

                    self.yang_name = "cisco-bgp4mib"
                    self.yang_parent_name = "bgp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ('up_down', (YLeaf(YType.empty, 'up-down'), ['Empty'])),
                    ])
                    self.enable = None
                    self.up_down = None
                    self._segment_path = lambda: "cisco-bgp4mib"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-ipv4-bgp-cfg:bgp/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.Bgp.CiscoBgp4mib, ['enable', 'up_down'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.Bgp.CiscoBgp4mib']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Bgp']['meta_info']


        class EntityState(_Entity_):
            """
            ENTITY\-STATE\-MIB notification configuration
            
            .. attribute:: switchover
            
            	Enable ceStateExtStandbySwitchover notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: oper_status
            
            	Enable entStateOperEnable and entStateOperDisable notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-entstatemib-cfg'
            _revision = '2015-07-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.EntityState, self).__init__()

                self.yang_name = "entity-state"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('switchover', (YLeaf(YType.empty, 'switchover'), ['Empty'])),
                    ('oper_status', (YLeaf(YType.empty, 'oper-status'), ['Empty'])),
                ])
                self.switchover = None
                self.oper_status = None
                self._segment_path = lambda: "Cisco-IOS-XR-snmp-entstatemib-cfg:entity-state"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.EntityState, ['switchover', 'oper_status'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.EntityState']['meta_info']


        class FrequencySynchronization(_Entity_):
            """
            Frequency Synchronization trap configuration
            
            .. attribute:: enable
            
            	Enable Frequency Synchronization traps
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'freqsync-cfg'
            _revision = '2017-09-30'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.FrequencySynchronization, self).__init__()

                self.yang_name = "frequency-synchronization"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-freqsync-cfg:frequency-synchronization"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.FrequencySynchronization, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.FrequencySynchronization']['meta_info']


        class MplsTeP2mp(_Entity_):
            """
            CISCO\-MPLS\-TE\-P2MP\-STD\-MIB notification
            configuration
            
            .. attribute:: up
            
            	Enable cmplsTeP2mpTunnelDestUp notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: down
            
            	Enable cmplsTeP2mpTunnelDestDown notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2019-10-16'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.MplsTeP2mp, self).__init__()

                self.yang_name = "mpls-te-p2mp"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('up', (YLeaf(YType.empty, 'up'), ['Empty'])),
                    ('down', (YLeaf(YType.empty, 'down'), ['Empty'])),
                ])
                self.up = None
                self.down = None
                self._segment_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te-p2mp"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.MplsTeP2mp, ['up', 'down'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.MplsTeP2mp']['meta_info']


        class MplsTe(_Entity_):
            """
            MPLS\-TE\-STD\-MIB notification configuration
            
            .. attribute:: cisco_extension
            
            	CISCO\-MPLS\-TE\-STD\-EXT\-MIB notification configuration
            	**type**\:  :py:class:`CiscoExtension <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.MplsTe.CiscoExtension>`
            
            .. attribute:: cisco
            
            	Enable MPLS TE tunnel Cisco format (default IETF) notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: up
            
            	Enable mplsTunnelUp notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: reoptimize
            
            	Enable mplsTunnelReoptimized notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: reroute
            
            	Enable mplsTunnelRerouted notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: down
            
            	Enable mplsTunnelDown notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2019-10-16'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.MplsTe, self).__init__()

                self.yang_name = "mpls-te"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("cisco-extension", ("cisco_extension", Snmp.Notification.MplsTe.CiscoExtension))])
                self._leafs = OrderedDict([
                    ('cisco', (YLeaf(YType.empty, 'cisco'), ['Empty'])),
                    ('up', (YLeaf(YType.empty, 'up'), ['Empty'])),
                    ('reoptimize', (YLeaf(YType.empty, 'reoptimize'), ['Empty'])),
                    ('reroute', (YLeaf(YType.empty, 'reroute'), ['Empty'])),
                    ('down', (YLeaf(YType.empty, 'down'), ['Empty'])),
                ])
                self.cisco = None
                self.up = None
                self.reoptimize = None
                self.reroute = None
                self.down = None

                self.cisco_extension = Snmp.Notification.MplsTe.CiscoExtension()
                self.cisco_extension.parent = self
                self._children_name_map["cisco_extension"] = "cisco-extension"
                self._segment_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.MplsTe, ['cisco', 'up', 'reoptimize', 'reroute', 'down'], name, value)


            class CiscoExtension(_Entity_):
                """
                CISCO\-MPLS\-TE\-STD\-EXT\-MIB notification
                configuration
                
                .. attribute:: preempt
                
                	Enable cmplsTunnelPreempt notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: insufficient_bandwidth
                
                	Enable cmplsTunnelInsuffBW notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: re_route_pending_clear
                
                	Enable cmplsTunnelReRoutePendingClear notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: bringup_fail
                
                	Enable cmplsTunnelBringupFail notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: re_route_pending
                
                	Enable cmplsTunnelReRoutePending notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2019-10-16'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Notification.MplsTe.CiscoExtension, self).__init__()

                    self.yang_name = "cisco-extension"
                    self.yang_parent_name = "mpls-te"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('preempt', (YLeaf(YType.empty, 'preempt'), ['Empty'])),
                        ('insufficient_bandwidth', (YLeaf(YType.empty, 'insufficient-bandwidth'), ['Empty'])),
                        ('re_route_pending_clear', (YLeaf(YType.empty, 're-route-pending-clear'), ['Empty'])),
                        ('bringup_fail', (YLeaf(YType.empty, 'bringup-fail'), ['Empty'])),
                        ('re_route_pending', (YLeaf(YType.empty, 're-route-pending'), ['Empty'])),
                    ])
                    self.preempt = None
                    self.insufficient_bandwidth = None
                    self.re_route_pending_clear = None
                    self.bringup_fail = None
                    self.re_route_pending = None
                    self._segment_path = lambda: "cisco-extension"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-mpls-te-cfg:mpls-te/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.MplsTe.CiscoExtension, ['preempt', 'insufficient_bandwidth', 're_route_pending_clear', 'bringup_fail', 're_route_pending'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.MplsTe.CiscoExtension']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.MplsTe']['meta_info']


        class MplsFrr(_Entity_):
            """
            CISCO\-IETF\-FRR\-MIB notification configuration
            
            .. attribute:: unprotected
            
            	Enable cmplsFrrUnProtected notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable
            
            	Enable cmplsFrrMIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: protected
            
            	Enable cmplsFrrProtected notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2019-10-16'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.MplsFrr, self).__init__()

                self.yang_name = "mpls-frr"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('unprotected', (YLeaf(YType.empty, 'unprotected'), ['Empty'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ('protected', (YLeaf(YType.empty, 'protected'), ['Empty'])),
                ])
                self.unprotected = None
                self.enable = None
                self.protected = None
                self._segment_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-frr"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.MplsFrr, ['unprotected', 'enable', 'protected'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.MplsFrr']['meta_info']


        class Oam(_Entity_):
            """
            802.3 OAM MIB notification configuration
            
            .. attribute:: enable
            
            	Enable 802.3 OAM MIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ethernet-link-oam-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Oam, self).__init__()

                self.yang_name = "oam"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-ethernet-link-oam-cfg:oam"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Oam, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Oam']['meta_info']


        class MplsL3vpn(_Entity_):
            """
            MPLS\-L3VPN\-STD\-MIB notification configuration
            
            .. attribute:: max_threshold_reissue_notification_time
            
            	Time interval (secs) for re\-issuing max\-threshold notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: max_threshold_exceeded
            
            	Enable mplsL3VpnVrfNumVrfRouteMaxThreshExceeded notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: max_threshold_cleared
            
            	Enable mplsL3VpnNumVrfRouteMaxThreshCleared notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: mid_threshold_exceeded
            
            	Enable mplsL3VpnVrfRouteMidThreshExceeded notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable
            
            	Enable mplsL3VpnMIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: vrf_down
            
            	Enable mplsL3VpnVrfDown notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: vrf_up
            
            	Enable mplsL3VpnVrfUp notification
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-vpn-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.MplsL3vpn, self).__init__()

                self.yang_name = "mpls-l3vpn"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('max_threshold_reissue_notification_time', (YLeaf(YType.uint32, 'max-threshold-reissue-notification-time'), ['int'])),
                    ('max_threshold_exceeded', (YLeaf(YType.empty, 'max-threshold-exceeded'), ['Empty'])),
                    ('max_threshold_cleared', (YLeaf(YType.empty, 'max-threshold-cleared'), ['Empty'])),
                    ('mid_threshold_exceeded', (YLeaf(YType.empty, 'mid-threshold-exceeded'), ['Empty'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ('vrf_down', (YLeaf(YType.empty, 'vrf-down'), ['Empty'])),
                    ('vrf_up', (YLeaf(YType.empty, 'vrf-up'), ['Empty'])),
                ])
                self.max_threshold_reissue_notification_time = None
                self.max_threshold_exceeded = None
                self.max_threshold_cleared = None
                self.mid_threshold_exceeded = None
                self.enable = None
                self.vrf_down = None
                self.vrf_up = None
                self._segment_path = lambda: "Cisco-IOS-XR-mpls-vpn-cfg:mpls-l3vpn"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.MplsL3vpn, ['max_threshold_reissue_notification_time', 'max_threshold_exceeded', 'max_threshold_cleared', 'mid_threshold_exceeded', 'enable', 'vrf_down', 'vrf_up'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.MplsL3vpn']['meta_info']


        class ConfigMan(_Entity_):
            """
            CISCO\-CONFIG\-MAN\-MIB notification configurations
            
            .. attribute:: enable
            
            	Enable ciscoConfigManMIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'config-mibs-cfg'
            _revision = '2015-09-29'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.ConfigMan, self).__init__()

                self.yang_name = "config-man"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-config-mibs-cfg:config-man"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.ConfigMan, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.ConfigMan']['meta_info']


        class Diametermib(_Entity_):
            """
            Enable SNMP diameter traps
            
            .. attribute:: protocolerror
            
            	Enable SNMP diameter protocol error notification
            	**type**\: bool
            
            .. attribute:: permanentfail
            
            	Enable SNMP diameter permanent failure notification
            	**type**\: bool
            
            .. attribute:: peerdown
            
            	Enable SNMP diameter peer connection down notification
            	**type**\: bool
            
            .. attribute:: peerup
            
            	Enable SNMP diameter peer connection up notification
            	**type**\: bool
            
            .. attribute:: transientfail
            
            	Enable SNMP diameter transient failure notification
            	**type**\: bool
            
            

            """

            _prefix = 'aaa-diameter-base-mib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Diametermib, self).__init__()

                self.yang_name = "diametermib"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('protocolerror', (YLeaf(YType.boolean, 'protocolerror'), ['bool'])),
                    ('permanentfail', (YLeaf(YType.boolean, 'permanentfail'), ['bool'])),
                    ('peerdown', (YLeaf(YType.boolean, 'peerdown'), ['bool'])),
                    ('peerup', (YLeaf(YType.boolean, 'peerup'), ['bool'])),
                    ('transientfail', (YLeaf(YType.boolean, 'transientfail'), ['bool'])),
                ])
                self.protocolerror = None
                self.permanentfail = None
                self.peerdown = None
                self.peerup = None
                self.transientfail = None
                self._segment_path = lambda: "Cisco-IOS-XR-aaa-diameter-base-mib-cfg:diametermib"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Diametermib, ['protocolerror', 'permanentfail', 'peerdown', 'peerup', 'transientfail'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Diametermib']['meta_info']


        class FruControl(_Entity_):
            """
            CISCO\-ENTITY\-FRU\-CONTROL\-MIB notification
            configuration
            
            .. attribute:: enable
            
            	Enable ciscoEntityFRUControlMIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-frucontrolmib-cfg'
            _revision = '2015-01-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.FruControl, self).__init__()

                self.yang_name = "fru-control"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-snmp-frucontrolmib-cfg:fru-control"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.FruControl, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.FruControl']['meta_info']


        class Syslog(_Entity_):
            """
            CISCO\-SYSLOG\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable ciscoSyslogMIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-syslogmib-cfg'
            _revision = '2015-12-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Syslog, self).__init__()

                self.yang_name = "syslog"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-snmp-syslogmib-cfg:syslog"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Syslog, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Syslog']['meta_info']


        class Bfd(_Entity_):
            """
            CISCO\-IETF\-BFD\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable CISCO\-IETF\-BFD\-MIB notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Bfd, self).__init__()

                self.yang_name = "bfd"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-ip-bfd-cfg:bfd"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Bfd, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Bfd']['meta_info']


        class OpticalOts(_Entity_):
            """
            CISCO\-OPTICAL\-OTS\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable OpticalOtsmib notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'opticalotsmib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.OpticalOts, self).__init__()

                self.yang_name = "optical-ots"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-opticalotsmib-cfg:optical-ots"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.OpticalOts, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.OpticalOts']['meta_info']


        class Optical(_Entity_):
            """
            CISCO\-OPTICAL\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable Opticalmib notifications
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'opticalmib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Optical, self).__init__()

                self.yang_name = "optical"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "Cisco-IOS-XR-opticalmib-cfg:optical"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Optical, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Optical']['meta_info']


        class Ospfv3(_Entity_):
            """
            OSPFv3\-MIB notification configuration
            
            .. attribute:: error
            
            	SNMP notifications for OSPF errors
            	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ospfv3.Error>`
            
            .. attribute:: state_change
            
            	SNMP notifications for OSPF state change
            	**type**\:  :py:class:`StateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Ospfv3.StateChange>`
            
            

            """

            _prefix = 'ipv6-ospfv3-cfg'
            _revision = '2018-05-14'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Notification.Ospfv3, self).__init__()

                self.yang_name = "ospfv3"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("error", ("error", Snmp.Notification.Ospfv3.Error)), ("state-change", ("state_change", Snmp.Notification.Ospfv3.StateChange))])
                self._leafs = OrderedDict()

                self.error = Snmp.Notification.Ospfv3.Error()
                self.error.parent = self
                self._children_name_map["error"] = "error"

                self.state_change = Snmp.Notification.Ospfv3.StateChange()
                self.state_change.parent = self
                self._children_name_map["state_change"] = "state-change"
                self._segment_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-cfg:ospfv3"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Ospfv3, [], name, value)


            class Error(_Entity_):
                """
                SNMP notifications for OSPF errors
                
                .. attribute:: config_error
                
                	Enable ospfv3IfConfigError notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: bad_packet
                
                	Enable ospfv3IfRxBadPacket notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_bad_packet
                
                	Enable ospfv3VirtIfRxBadPacket notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_config_error
                
                	Enable ospfv3VirtIfConfigError notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv6-ospfv3-cfg'
                _revision = '2018-05-14'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Notification.Ospfv3.Error, self).__init__()

                    self.yang_name = "error"
                    self.yang_parent_name = "ospfv3"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('config_error', (YLeaf(YType.empty, 'config-error'), ['Empty'])),
                        ('bad_packet', (YLeaf(YType.empty, 'bad-packet'), ['Empty'])),
                        ('virtual_bad_packet', (YLeaf(YType.empty, 'virtual-bad-packet'), ['Empty'])),
                        ('virtual_config_error', (YLeaf(YType.empty, 'virtual-config-error'), ['Empty'])),
                    ])
                    self.config_error = None
                    self.bad_packet = None
                    self.virtual_bad_packet = None
                    self.virtual_config_error = None
                    self._segment_path = lambda: "error"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-ipv6-ospfv3-cfg:ospfv3/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.Ospfv3.Error, ['config_error', 'bad_packet', 'virtual_bad_packet', 'virtual_config_error'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.Ospfv3.Error']['meta_info']


            class StateChange(_Entity_):
                """
                SNMP notifications for OSPF state change
                
                .. attribute:: restart_virtual_helper
                
                	Enable ospfv3VirtNbrRestartHelperStatusChange notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: nssa_translator
                
                	Enable ospfv3NssaTranslatorStatusChange notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: interface
                
                	Enable ospfv3IfStateChange notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: restart
                
                	Enable ospfv3RestartStatusChange notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: neighbor
                
                	Enable ospfv3NbrStateChange notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_interface
                
                	Enable ospfv3VirtIfStateChange notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: restart_helper
                
                	Enable ospfv3NbrRestartHelperStatusChange notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: virtual_neighbor
                
                	Enable ospfv3VirtNbrStateChange notification
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv6-ospfv3-cfg'
                _revision = '2018-05-14'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Notification.Ospfv3.StateChange, self).__init__()

                    self.yang_name = "state-change"
                    self.yang_parent_name = "ospfv3"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('restart_virtual_helper', (YLeaf(YType.empty, 'restart-virtual-helper'), ['Empty'])),
                        ('nssa_translator', (YLeaf(YType.empty, 'nssa-translator'), ['Empty'])),
                        ('interface', (YLeaf(YType.empty, 'interface'), ['Empty'])),
                        ('restart', (YLeaf(YType.empty, 'restart'), ['Empty'])),
                        ('neighbor', (YLeaf(YType.empty, 'neighbor'), ['Empty'])),
                        ('virtual_interface', (YLeaf(YType.empty, 'virtual-interface'), ['Empty'])),
                        ('restart_helper', (YLeaf(YType.empty, 'restart-helper'), ['Empty'])),
                        ('virtual_neighbor', (YLeaf(YType.empty, 'virtual-neighbor'), ['Empty'])),
                    ])
                    self.restart_virtual_helper = None
                    self.nssa_translator = None
                    self.interface = None
                    self.restart = None
                    self.neighbor = None
                    self.virtual_interface = None
                    self.restart_helper = None
                    self.virtual_neighbor = None
                    self._segment_path = lambda: "state-change"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-ipv6-ospfv3-cfg:ospfv3/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.Ospfv3.StateChange, ['restart_virtual_helper', 'nssa_translator', 'interface', 'restart', 'neighbor', 'virtual_interface', 'restart_helper', 'virtual_neighbor'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Notification.Ospfv3.StateChange']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Notification.Ospfv3']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Notification']['meta_info']


    class Correlator(_Entity_):
        """
        Configure properties of the trap correlator
        
        .. attribute:: rules
        
        	Table of configured rules
        	**type**\:  :py:class:`Rules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules>`
        
        .. attribute:: rule_sets
        
        	Table of configured rulesets
        	**type**\:  :py:class:`RuleSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.RuleSets>`
        
        .. attribute:: buffer_size
        
        	Configure size of the correlator buffer
        	**type**\: int
        
        	**range:** 1024..52428800
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Correlator, self).__init__()

            self.yang_name = "correlator"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rules", ("rules", Snmp.Correlator.Rules)), ("rule-sets", ("rule_sets", Snmp.Correlator.RuleSets))])
            self._leafs = OrderedDict([
                ('buffer_size', (YLeaf(YType.uint32, 'buffer-size'), ['int'])),
            ])
            self.buffer_size = None

            self.rules = Snmp.Correlator.Rules()
            self.rules.parent = self
            self._children_name_map["rules"] = "rules"

            self.rule_sets = Snmp.Correlator.RuleSets()
            self.rule_sets.parent = self
            self._children_name_map["rule_sets"] = "rule-sets"
            self._segment_path = lambda: "correlator"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Correlator, ['buffer_size'], name, value)


        class Rules(_Entity_):
            """
            Table of configured rules
            
            .. attribute:: rule
            
            	Rule name
            	**type**\: list of  		 :py:class:`Rule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Correlator.Rules, self).__init__()

                self.yang_name = "rules"
                self.yang_parent_name = "correlator"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rule", ("rule", Snmp.Correlator.Rules.Rule))])
                self._leafs = OrderedDict()

                self.rule = YList(self)
                self._segment_path = lambda: "rules"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/correlator/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Correlator.Rules, [], name, value)


            class Rule(_Entity_):
                """
                Rule name
                
                .. attribute:: name  (key)
                
                	Rule name
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: root_causes
                
                	Table of configured rootcause (only one entry allowed)
                	**type**\:  :py:class:`RootCauses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.RootCauses>`
                
                .. attribute:: non_root_causes
                
                	Table of configured non\-rootcause
                	**type**\:  :py:class:`NonRootCauses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonRootCauses>`
                
                .. attribute:: timeout
                
                	Timeout (time to wait for active correlation) in milliseconds
                	**type**\: int
                
                	**range:** 1..600000
                
                	**units**\: millisecond
                
                .. attribute:: applied_to
                
                	Applied to the Rule or Ruleset
                	**type**\:  :py:class:`AppliedTo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.AppliedTo>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2018-06-27'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Correlator.Rules.Rule, self).__init__()

                    self.yang_name = "rule"
                    self.yang_parent_name = "rules"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("root-causes", ("root_causes", Snmp.Correlator.Rules.Rule.RootCauses)), ("non-root-causes", ("non_root_causes", Snmp.Correlator.Rules.Rule.NonRootCauses)), ("applied-to", ("applied_to", Snmp.Correlator.Rules.Rule.AppliedTo))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                    ])
                    self.name = None
                    self.timeout = None

                    self.root_causes = Snmp.Correlator.Rules.Rule.RootCauses()
                    self.root_causes.parent = self
                    self._children_name_map["root_causes"] = "root-causes"

                    self.non_root_causes = Snmp.Correlator.Rules.Rule.NonRootCauses()
                    self.non_root_causes.parent = self
                    self._children_name_map["non_root_causes"] = "non-root-causes"

                    self.applied_to = Snmp.Correlator.Rules.Rule.AppliedTo()
                    self.applied_to.parent = self
                    self._children_name_map["applied_to"] = "applied-to"
                    self._segment_path = lambda: "rule" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/correlator/rules/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Correlator.Rules.Rule, ['name', 'timeout'], name, value)


                class RootCauses(_Entity_):
                    """
                    Table of configured rootcause (only one entry
                    allowed)
                    
                    .. attribute:: root_cause
                    
                    	The rootcause \- maximum of one can be configured per rule
                    	**type**\: list of  		 :py:class:`RootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.RootCauses.RootCause>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Correlator.Rules.Rule.RootCauses, self).__init__()

                        self.yang_name = "root-causes"
                        self.yang_parent_name = "rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("root-cause", ("root_cause", Snmp.Correlator.Rules.Rule.RootCauses.RootCause))])
                        self._leafs = OrderedDict()

                        self.root_cause = YList(self)
                        self._segment_path = lambda: "root-causes"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Correlator.Rules.Rule.RootCauses, [], name, value)


                    class RootCause(_Entity_):
                        """
                        The rootcause \- maximum of one can be
                        configured per rule
                        
                        .. attribute:: oid  (key)
                        
                        	OID of rootcause trap (dotted decimal)
                        	**type**\: str
                        
                        .. attribute:: created
                        
                        	Create rootcause
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: var_binds
                        
                        	Varbinds to match
                        	**type**\:  :py:class:`VarBinds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2018-06-27'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.Correlator.Rules.Rule.RootCauses.RootCause, self).__init__()

                            self.yang_name = "root-cause"
                            self.yang_parent_name = "root-causes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['oid']
                            self._child_classes = OrderedDict([("var-binds", ("var_binds", Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds))])
                            self._leafs = OrderedDict([
                                ('oid', (YLeaf(YType.str, 'oid'), ['str'])),
                                ('created', (YLeaf(YType.empty, 'created'), ['Empty'])),
                            ])
                            self.oid = None
                            self.created = None

                            self.var_binds = Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds()
                            self.var_binds.parent = self
                            self._children_name_map["var_binds"] = "var-binds"
                            self._segment_path = lambda: "root-cause" + "[oid='" + str(self.oid) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Correlator.Rules.Rule.RootCauses.RootCause, ['oid', 'created'], name, value)


                        class VarBinds(_Entity_):
                            """
                            Varbinds to match
                            
                            .. attribute:: var_bind
                            
                            	Varbind match conditions
                            	**type**\: list of  		 :py:class:`VarBind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind>`
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2018-06-27'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds, self).__init__()

                                self.yang_name = "var-binds"
                                self.yang_parent_name = "root-cause"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("var-bind", ("var_bind", Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind))])
                                self._leafs = OrderedDict()

                                self.var_bind = YList(self)
                                self._segment_path = lambda: "var-binds"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds, [], name, value)


                            class VarBind(_Entity_):
                                """
                                Varbind match conditions
                                
                                .. attribute:: oid  (key)
                                
                                	OID of varbind (dotted decimal)
                                	**type**\: str
                                
                                .. attribute:: match
                                
                                	VarBind match conditions
                                	**type**\:  :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind.Match>`
                                
                                

                                """

                                _prefix = 'snmp-agent-cfg'
                                _revision = '2018-06-27'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind, self).__init__()

                                    self.yang_name = "var-bind"
                                    self.yang_parent_name = "var-binds"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['oid']
                                    self._child_classes = OrderedDict([("match", ("match", Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind.Match))])
                                    self._leafs = OrderedDict([
                                        ('oid', (YLeaf(YType.str, 'oid'), ['str'])),
                                    ])
                                    self.oid = None

                                    self.match = Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind.Match()
                                    self.match.parent = self
                                    self._children_name_map["match"] = "match"
                                    self._segment_path = lambda: "var-bind" + "[oid='" + str(self.oid) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind, ['oid'], name, value)


                                class Match(_Entity_):
                                    """
                                    VarBind match conditions
                                    
                                    .. attribute:: value
                                    
                                    	Regular Expression to match value
                                    	**type**\: str
                                    
                                    .. attribute:: index
                                    
                                    	Regular Expression to match index
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'snmp-agent-cfg'
                                    _revision = '2018-06-27'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind.Match, self).__init__()

                                        self.yang_name = "match"
                                        self.yang_parent_name = "var-bind"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('value', (YLeaf(YType.str, 'value'), ['str'])),
                                            ('index', (YLeaf(YType.str, 'index'), ['str'])),
                                        ])
                                        self.value = None
                                        self.index = None
                                        self._segment_path = lambda: "match"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind.Match, ['value', 'index'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                        return meta._meta_table['Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind.Match']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                    return meta._meta_table['Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds.VarBind']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Snmp.Correlator.Rules.Rule.RootCauses.RootCause.VarBinds']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Correlator.Rules.Rule.RootCauses.RootCause']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Correlator.Rules.Rule.RootCauses']['meta_info']


                class NonRootCauses(_Entity_):
                    """
                    Table of configured non\-rootcause
                    
                    .. attribute:: non_root_cause
                    
                    	A non\-rootcause
                    	**type**\: list of  		 :py:class:`NonRootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Correlator.Rules.Rule.NonRootCauses, self).__init__()

                        self.yang_name = "non-root-causes"
                        self.yang_parent_name = "rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("non-root-cause", ("non_root_cause", Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause))])
                        self._leafs = OrderedDict()

                        self.non_root_cause = YList(self)
                        self._segment_path = lambda: "non-root-causes"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Correlator.Rules.Rule.NonRootCauses, [], name, value)


                    class NonRootCause(_Entity_):
                        """
                        A non\-rootcause
                        
                        .. attribute:: oid  (key)
                        
                        	OID of nonrootcause trap (dotted decimal)
                        	**type**\: str
                        
                        .. attribute:: created
                        
                        	Create nonrootcause
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: var_binds
                        
                        	Varbinds to match
                        	**type**\:  :py:class:`VarBinds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2018-06-27'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause, self).__init__()

                            self.yang_name = "non-root-cause"
                            self.yang_parent_name = "non-root-causes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['oid']
                            self._child_classes = OrderedDict([("var-binds", ("var_binds", Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds))])
                            self._leafs = OrderedDict([
                                ('oid', (YLeaf(YType.str, 'oid'), ['str'])),
                                ('created', (YLeaf(YType.empty, 'created'), ['Empty'])),
                            ])
                            self.oid = None
                            self.created = None

                            self.var_binds = Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds()
                            self.var_binds.parent = self
                            self._children_name_map["var_binds"] = "var-binds"
                            self._segment_path = lambda: "non-root-cause" + "[oid='" + str(self.oid) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause, ['oid', 'created'], name, value)


                        class VarBinds(_Entity_):
                            """
                            Varbinds to match
                            
                            .. attribute:: var_bind
                            
                            	Varbind match conditions
                            	**type**\: list of  		 :py:class:`VarBind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind>`
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2018-06-27'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds, self).__init__()

                                self.yang_name = "var-binds"
                                self.yang_parent_name = "non-root-cause"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("var-bind", ("var_bind", Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind))])
                                self._leafs = OrderedDict()

                                self.var_bind = YList(self)
                                self._segment_path = lambda: "var-binds"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds, [], name, value)


                            class VarBind(_Entity_):
                                """
                                Varbind match conditions
                                
                                .. attribute:: oid  (key)
                                
                                	OID of varbind (dotted decimal)
                                	**type**\: str
                                
                                .. attribute:: match
                                
                                	VarBind match conditions
                                	**type**\:  :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind.Match>`
                                
                                

                                """

                                _prefix = 'snmp-agent-cfg'
                                _revision = '2018-06-27'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind, self).__init__()

                                    self.yang_name = "var-bind"
                                    self.yang_parent_name = "var-binds"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['oid']
                                    self._child_classes = OrderedDict([("match", ("match", Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind.Match))])
                                    self._leafs = OrderedDict([
                                        ('oid', (YLeaf(YType.str, 'oid'), ['str'])),
                                    ])
                                    self.oid = None

                                    self.match = Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind.Match()
                                    self.match.parent = self
                                    self._children_name_map["match"] = "match"
                                    self._segment_path = lambda: "var-bind" + "[oid='" + str(self.oid) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind, ['oid'], name, value)


                                class Match(_Entity_):
                                    """
                                    VarBind match conditions
                                    
                                    .. attribute:: value
                                    
                                    	Regular Expression to match value
                                    	**type**\: str
                                    
                                    .. attribute:: index
                                    
                                    	Regular Expression to match index
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'snmp-agent-cfg'
                                    _revision = '2018-06-27'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind.Match, self).__init__()

                                        self.yang_name = "match"
                                        self.yang_parent_name = "var-bind"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('value', (YLeaf(YType.str, 'value'), ['str'])),
                                            ('index', (YLeaf(YType.str, 'index'), ['str'])),
                                        ])
                                        self.value = None
                                        self.index = None
                                        self._segment_path = lambda: "match"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind.Match, ['value', 'index'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                        return meta._meta_table['Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind.Match']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                    return meta._meta_table['Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds.VarBind']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause.VarBinds']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Correlator.Rules.Rule.NonRootCauses.NonRootCause']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Correlator.Rules.Rule.NonRootCauses']['meta_info']


                class AppliedTo(_Entity_):
                    """
                    Applied to the Rule or Ruleset
                    
                    .. attribute:: hosts
                    
                    	Table of configured hosts to apply rules to
                    	**type**\:  :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.AppliedTo.Hosts>`
                    
                    .. attribute:: all
                    
                    	Apply to all of the device
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Correlator.Rules.Rule.AppliedTo, self).__init__()

                        self.yang_name = "applied-to"
                        self.yang_parent_name = "rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("hosts", ("hosts", Snmp.Correlator.Rules.Rule.AppliedTo.Hosts))])
                        self._leafs = OrderedDict([
                            ('all', (YLeaf(YType.empty, 'all'), ['Empty'])),
                        ])
                        self.all = None

                        self.hosts = Snmp.Correlator.Rules.Rule.AppliedTo.Hosts()
                        self.hosts.parent = self
                        self._children_name_map["hosts"] = "hosts"
                        self._segment_path = lambda: "applied-to"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Correlator.Rules.Rule.AppliedTo, ['all'], name, value)


                    class Hosts(_Entity_):
                        """
                        Table of configured hosts to apply rules to
                        
                        .. attribute:: host
                        
                        	A destination host
                        	**type**\: list of  		 :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2018-06-27'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.Correlator.Rules.Rule.AppliedTo.Hosts, self).__init__()

                            self.yang_name = "hosts"
                            self.yang_parent_name = "applied-to"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("host", ("host", Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host))])
                            self._leafs = OrderedDict()

                            self.host = YList(self)
                            self._segment_path = lambda: "hosts"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Correlator.Rules.Rule.AppliedTo.Hosts, [], name, value)


                        class Host(_Entity_):
                            """
                            A destination host
                            
                            .. attribute:: ip_address  (key)
                            
                            	IP address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: port  (key)
                            
                            	Port (specify 162 for default)
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2018-06-27'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host, self).__init__()

                                self.yang_name = "host"
                                self.yang_parent_name = "hosts"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['ip_address','port']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                                    ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                                ])
                                self.ip_address = None
                                self.port = None
                                self._segment_path = lambda: "host" + "[ip-address='" + str(self.ip_address) + "']" + "[port='" + str(self.port) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host, ['ip_address', 'port'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Correlator.Rules.Rule.AppliedTo.Hosts']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Correlator.Rules.Rule.AppliedTo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Correlator.Rules.Rule']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Correlator.Rules']['meta_info']


        class RuleSets(_Entity_):
            """
            Table of configured rulesets
            
            .. attribute:: rule_set
            
            	Ruleset name
            	**type**\: list of  		 :py:class:`RuleSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.RuleSets.RuleSet>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Correlator.RuleSets, self).__init__()

                self.yang_name = "rule-sets"
                self.yang_parent_name = "correlator"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rule-set", ("rule_set", Snmp.Correlator.RuleSets.RuleSet))])
                self._leafs = OrderedDict()

                self.rule_set = YList(self)
                self._segment_path = lambda: "rule-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/correlator/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Correlator.RuleSets, [], name, value)


            class RuleSet(_Entity_):
                """
                Ruleset name
                
                .. attribute:: name  (key)
                
                	Ruleset name
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: rulenames
                
                	Table of configured rulenames
                	**type**\:  :py:class:`Rulenames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.RuleSets.RuleSet.Rulenames>`
                
                .. attribute:: applied_to
                
                	Applied to the Rule or Ruleset
                	**type**\:  :py:class:`AppliedTo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.RuleSets.RuleSet.AppliedTo>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2018-06-27'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Correlator.RuleSets.RuleSet, self).__init__()

                    self.yang_name = "rule-set"
                    self.yang_parent_name = "rule-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("rulenames", ("rulenames", Snmp.Correlator.RuleSets.RuleSet.Rulenames)), ("applied-to", ("applied_to", Snmp.Correlator.RuleSets.RuleSet.AppliedTo))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.rulenames = Snmp.Correlator.RuleSets.RuleSet.Rulenames()
                    self.rulenames.parent = self
                    self._children_name_map["rulenames"] = "rulenames"

                    self.applied_to = Snmp.Correlator.RuleSets.RuleSet.AppliedTo()
                    self.applied_to.parent = self
                    self._children_name_map["applied_to"] = "applied-to"
                    self._segment_path = lambda: "rule-set" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/correlator/rule-sets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Correlator.RuleSets.RuleSet, ['name'], name, value)


                class Rulenames(_Entity_):
                    """
                    Table of configured rulenames
                    
                    .. attribute:: rulename
                    
                    	A rulename
                    	**type**\: list of  		 :py:class:`Rulename <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Correlator.RuleSets.RuleSet.Rulenames, self).__init__()

                        self.yang_name = "rulenames"
                        self.yang_parent_name = "rule-set"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("rulename", ("rulename", Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename))])
                        self._leafs = OrderedDict()

                        self.rulename = YList(self)
                        self._segment_path = lambda: "rulenames"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Correlator.RuleSets.RuleSet.Rulenames, [], name, value)


                    class Rulename(_Entity_):
                        """
                        A rulename
                        
                        .. attribute:: rulename  (key)
                        
                        	Rule name
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2018-06-27'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename, self).__init__()

                            self.yang_name = "rulename"
                            self.yang_parent_name = "rulenames"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['rulename']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rulename', (YLeaf(YType.str, 'rulename'), ['str'])),
                            ])
                            self.rulename = None
                            self._segment_path = lambda: "rulename" + "[rulename='" + str(self.rulename) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename, ['rulename'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Correlator.RuleSets.RuleSet.Rulenames']['meta_info']


                class AppliedTo(_Entity_):
                    """
                    Applied to the Rule or Ruleset
                    
                    .. attribute:: hosts
                    
                    	Table of configured hosts to apply rules to
                    	**type**\:  :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts>`
                    
                    .. attribute:: all
                    
                    	Apply to all of the device
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Correlator.RuleSets.RuleSet.AppliedTo, self).__init__()

                        self.yang_name = "applied-to"
                        self.yang_parent_name = "rule-set"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("hosts", ("hosts", Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts))])
                        self._leafs = OrderedDict([
                            ('all', (YLeaf(YType.empty, 'all'), ['Empty'])),
                        ])
                        self.all = None

                        self.hosts = Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts()
                        self.hosts.parent = self
                        self._children_name_map["hosts"] = "hosts"
                        self._segment_path = lambda: "applied-to"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Correlator.RuleSets.RuleSet.AppliedTo, ['all'], name, value)


                    class Hosts(_Entity_):
                        """
                        Table of configured hosts to apply rules to
                        
                        .. attribute:: host
                        
                        	A destination host
                        	**type**\: list of  		 :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2018-06-27'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts, self).__init__()

                            self.yang_name = "hosts"
                            self.yang_parent_name = "applied-to"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("host", ("host", Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host))])
                            self._leafs = OrderedDict()

                            self.host = YList(self)
                            self._segment_path = lambda: "hosts"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts, [], name, value)


                        class Host(_Entity_):
                            """
                            A destination host
                            
                            .. attribute:: ip_address  (key)
                            
                            	IP address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: port  (key)
                            
                            	Port (specify 162 for default)
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2018-06-27'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host, self).__init__()

                                self.yang_name = "host"
                                self.yang_parent_name = "hosts"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['ip_address','port']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                                    ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                                ])
                                self.ip_address = None
                                self.port = None
                                self._segment_path = lambda: "host" + "[ip-address='" + str(self.ip_address) + "']" + "[port='" + str(self.port) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host, ['ip_address', 'port'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Correlator.RuleSets.RuleSet.AppliedTo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Correlator.RuleSets.RuleSet']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Correlator.RuleSets']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Correlator']['meta_info']


    class BulkStats(_Entity_):
        """
        SNMP bulk stats configuration commands
        
        .. attribute:: schemas
        
        	Configure schema definition
        	**type**\:  :py:class:`Schemas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Schemas>`
        
        .. attribute:: objects
        
        	Configure an Object List 
        	**type**\:  :py:class:`Objects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Objects>`
        
        .. attribute:: transfers
        
        	Periodicity for the transfer of bulk data in minutes
        	**type**\:  :py:class:`Transfers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Transfers>`
        
        .. attribute:: memory
        
        	per process memory limit in kilo bytes
        	**type**\: int
        
        	**range:** 100..200000
        
        	**units**\: kilobyte
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.BulkStats, self).__init__()

            self.yang_name = "bulk-stats"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("schemas", ("schemas", Snmp.BulkStats.Schemas)), ("objects", ("objects", Snmp.BulkStats.Objects)), ("transfers", ("transfers", Snmp.BulkStats.Transfers))])
            self._leafs = OrderedDict([
                ('memory', (YLeaf(YType.uint32, 'memory'), ['int'])),
            ])
            self.memory = None

            self.schemas = Snmp.BulkStats.Schemas()
            self.schemas.parent = self
            self._children_name_map["schemas"] = "schemas"

            self.objects = Snmp.BulkStats.Objects()
            self.objects.parent = self
            self._children_name_map["objects"] = "objects"

            self.transfers = Snmp.BulkStats.Transfers()
            self.transfers.parent = self
            self._children_name_map["transfers"] = "transfers"
            self._segment_path = lambda: "bulk-stats"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.BulkStats, ['memory'], name, value)


        class Schemas(_Entity_):
            """
            Configure schema definition
            
            .. attribute:: schema
            
            	The name of the Schema
            	**type**\: list of  		 :py:class:`Schema <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Schemas.Schema>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.BulkStats.Schemas, self).__init__()

                self.yang_name = "schemas"
                self.yang_parent_name = "bulk-stats"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("schema", ("schema", Snmp.BulkStats.Schemas.Schema))])
                self._leafs = OrderedDict()

                self.schema = YList(self)
                self._segment_path = lambda: "schemas"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/bulk-stats/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.BulkStats.Schemas, [], name, value)


            class Schema(_Entity_):
                """
                The name of the Schema
                
                .. attribute:: schema_name  (key)
                
                	The name of the schema
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: instance
                
                	Object instance information
                	**type**\:  :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Schemas.Schema.Instance>`
                
                	**presence node**\: True
                
                .. attribute:: type
                
                	Configure schema name
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: schema_object_list
                
                	Name of an object List
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: poll_interval
                
                	Periodicity for polling of objects in this schema in minutes
                	**type**\: int
                
                	**range:** 1..20000
                
                	**units**\: minute
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2018-06-27'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.BulkStats.Schemas.Schema, self).__init__()

                    self.yang_name = "schema"
                    self.yang_parent_name = "schemas"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['schema_name']
                    self._child_classes = OrderedDict([("instance", ("instance", Snmp.BulkStats.Schemas.Schema.Instance))])
                    self._leafs = OrderedDict([
                        ('schema_name', (YLeaf(YType.str, 'schema-name'), ['str'])),
                        ('type', (YLeaf(YType.empty, 'type'), ['Empty'])),
                        ('schema_object_list', (YLeaf(YType.str, 'schema-object-list'), ['str'])),
                        ('poll_interval', (YLeaf(YType.uint32, 'poll-interval'), ['int'])),
                    ])
                    self.schema_name = None
                    self.type = None
                    self.schema_object_list = None
                    self.poll_interval = None

                    self.instance = None
                    self._children_name_map["instance"] = "instance"
                    self._segment_path = lambda: "schema" + "[schema-name='" + str(self.schema_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/bulk-stats/schemas/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.BulkStats.Schemas.Schema, ['schema_name', 'type', 'schema_object_list', 'poll_interval'], name, value)


                class Instance(_Entity_):
                    """
                    Object instance information
                    
                    .. attribute:: type
                    
                    	Type of the instance
                    	**type**\:  :py:class:`SnmpBulkstatSchema <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpBulkstatSchema>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: instance
                    
                    	Instance of the schema
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: start
                    
                    	Start Instance OID for repetition
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: end
                    
                    	End Instance OID for repetition
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: max
                    
                    	Max value of Instance repetition
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: sub_interface
                    
                    	Include all the subinterface
                    	**type**\: bool
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.BulkStats.Schemas.Schema.Instance, self).__init__()

                        self.yang_name = "instance"
                        self.yang_parent_name = "schema"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpBulkstatSchema', '')])),
                            ('instance', (YLeaf(YType.str, 'instance'), ['str'])),
                            ('start', (YLeaf(YType.str, 'start'), ['str'])),
                            ('end', (YLeaf(YType.str, 'end'), ['str'])),
                            ('max', (YLeaf(YType.uint32, 'max'), ['int'])),
                            ('sub_interface', (YLeaf(YType.boolean, 'sub-interface'), ['bool'])),
                        ])
                        self.type = None
                        self.instance = None
                        self.start = None
                        self.end = None
                        self.max = None
                        self.sub_interface = None
                        self._segment_path = lambda: "instance"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.BulkStats.Schemas.Schema.Instance, ['type', 'instance', 'start', 'end', 'max', 'sub_interface'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.BulkStats.Schemas.Schema.Instance']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.BulkStats.Schemas.Schema']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.BulkStats.Schemas']['meta_info']


        class Objects(_Entity_):
            """
            Configure an Object List 
            
            .. attribute:: object
            
            	Name of the object List
            	**type**\: list of  		 :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Objects.Object>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.BulkStats.Objects, self).__init__()

                self.yang_name = "objects"
                self.yang_parent_name = "bulk-stats"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("object", ("object", Snmp.BulkStats.Objects.Object))])
                self._leafs = OrderedDict()

                self.object = YList(self)
                self._segment_path = lambda: "objects"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/bulk-stats/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.BulkStats.Objects, [], name, value)


            class Object(_Entity_):
                """
                Name of the object List
                
                .. attribute:: object_list_name  (key)
                
                	Name of the object List
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: objects
                
                	Configure an object List
                	**type**\:  :py:class:`Objects_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Objects.Object.Objects_>`
                
                .. attribute:: type
                
                	Configure object list name
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2018-06-27'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.BulkStats.Objects.Object, self).__init__()

                    self.yang_name = "object"
                    self.yang_parent_name = "objects"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['object_list_name']
                    self._child_classes = OrderedDict([("objects", ("objects", Snmp.BulkStats.Objects.Object.Objects_))])
                    self._leafs = OrderedDict([
                        ('object_list_name', (YLeaf(YType.str, 'object-list-name'), ['str'])),
                        ('type', (YLeaf(YType.empty, 'type'), ['Empty'])),
                    ])
                    self.object_list_name = None
                    self.type = None

                    self.objects = Snmp.BulkStats.Objects.Object.Objects_()
                    self.objects.parent = self
                    self._children_name_map["objects"] = "objects"
                    self._segment_path = lambda: "object" + "[object-list-name='" + str(self.object_list_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/bulk-stats/objects/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.BulkStats.Objects.Object, ['object_list_name', 'type'], name, value)


                class Objects_(_Entity_):
                    """
                    Configure an object List
                    
                    .. attribute:: object
                    
                    	Object name or OID
                    	**type**\: list of  		 :py:class:`Object_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Objects.Object.Objects_.Object_>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.BulkStats.Objects.Object.Objects_, self).__init__()

                        self.yang_name = "objects"
                        self.yang_parent_name = "object"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("object", ("object", Snmp.BulkStats.Objects.Object.Objects_.Object_))])
                        self._leafs = OrderedDict()

                        self.object = YList(self)
                        self._segment_path = lambda: "objects"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.BulkStats.Objects.Object.Objects_, [], name, value)


                    class Object_(_Entity_):
                        """
                        Object name or OID
                        
                        .. attribute:: oid  (key)
                        
                        	Object name or OID 
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2018-06-27'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.BulkStats.Objects.Object.Objects_.Object_, self).__init__()

                            self.yang_name = "object"
                            self.yang_parent_name = "objects"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['oid']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('oid', (YLeaf(YType.str, 'oid'), ['str'])),
                            ])
                            self.oid = None
                            self._segment_path = lambda: "object" + "[oid='" + str(self.oid) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.BulkStats.Objects.Object.Objects_.Object_, ['oid'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.BulkStats.Objects.Object.Objects_.Object_']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.BulkStats.Objects.Object.Objects_']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.BulkStats.Objects.Object']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.BulkStats.Objects']['meta_info']


        class Transfers(_Entity_):
            """
            Periodicity for the transfer of bulk data in
            minutes
            
            .. attribute:: transfer
            
            	Name of bulk transfer
            	**type**\: list of  		 :py:class:`Transfer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Transfers.Transfer>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.BulkStats.Transfers, self).__init__()

                self.yang_name = "transfers"
                self.yang_parent_name = "bulk-stats"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("transfer", ("transfer", Snmp.BulkStats.Transfers.Transfer))])
                self._leafs = OrderedDict()

                self.transfer = YList(self)
                self._segment_path = lambda: "transfers"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/bulk-stats/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.BulkStats.Transfers, [], name, value)


            class Transfer(_Entity_):
                """
                Name of bulk transfer
                
                .. attribute:: transfer_name  (key)
                
                	Name of bulk transfer
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: transfer_schemas
                
                	Schema that contains objects to be collected
                	**type**\:  :py:class:`TransferSchemas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Transfers.Transfer.TransferSchemas>`
                
                .. attribute:: secondary
                
                	FTP or rcp or TFTP can be used for file transfer
                	**type**\: str
                
                .. attribute:: type
                
                	Configure transfer list name
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: buffer_size
                
                	Bulkstat data file maximum size in bytes
                	**type**\: int
                
                	**range:** 1024..2147483647
                
                	**units**\: byte
                
                .. attribute:: retain
                
                	Retention period in minutes
                	**type**\: int
                
                	**range:** 0..20000
                
                	**units**\: minute
                
                .. attribute:: format
                
                	Format of the bulk data file
                	**type**\:  :py:class:`SnmpBulkstatFileFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpBulkstatFileFormat>`
                
                .. attribute:: retry
                
                	Number of transmission retries
                	**type**\: int
                
                	**range:** 0..100
                
                .. attribute:: enable
                
                	Start Data Collection for this Configuration
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: primary
                
                	FTP or rcp or TFTP can be used for file transfer
                	**type**\: str
                
                .. attribute:: interval
                
                	Periodicity for the transfer of bulk data in minutes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: minute
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2018-06-27'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.BulkStats.Transfers.Transfer, self).__init__()

                    self.yang_name = "transfer"
                    self.yang_parent_name = "transfers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['transfer_name']
                    self._child_classes = OrderedDict([("transfer-schemas", ("transfer_schemas", Snmp.BulkStats.Transfers.Transfer.TransferSchemas))])
                    self._leafs = OrderedDict([
                        ('transfer_name', (YLeaf(YType.str, 'transfer-name'), ['str'])),
                        ('secondary', (YLeaf(YType.str, 'secondary'), ['str'])),
                        ('type', (YLeaf(YType.empty, 'type'), ['Empty'])),
                        ('buffer_size', (YLeaf(YType.uint32, 'buffer-size'), ['int'])),
                        ('retain', (YLeaf(YType.uint32, 'retain'), ['int'])),
                        ('format', (YLeaf(YType.enumeration, 'format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpBulkstatFileFormat', '')])),
                        ('retry', (YLeaf(YType.uint32, 'retry'), ['int'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ('primary', (YLeaf(YType.str, 'primary'), ['str'])),
                        ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                    ])
                    self.transfer_name = None
                    self.secondary = None
                    self.type = None
                    self.buffer_size = None
                    self.retain = None
                    self.format = None
                    self.retry = None
                    self.enable = None
                    self.primary = None
                    self.interval = None

                    self.transfer_schemas = Snmp.BulkStats.Transfers.Transfer.TransferSchemas()
                    self.transfer_schemas.parent = self
                    self._children_name_map["transfer_schemas"] = "transfer-schemas"
                    self._segment_path = lambda: "transfer" + "[transfer-name='" + str(self.transfer_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/bulk-stats/transfers/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.BulkStats.Transfers.Transfer, ['transfer_name', 'secondary', 'type', 'buffer_size', 'retain', 'format', 'retry', 'enable', 'primary', 'interval'], name, value)


                class TransferSchemas(_Entity_):
                    """
                    Schema that contains objects to be collected
                    
                    .. attribute:: transfer_schema
                    
                    	Schema that contains objects to be collected
                    	**type**\: list of  		 :py:class:`TransferSchema <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.BulkStats.Transfers.Transfer.TransferSchemas, self).__init__()

                        self.yang_name = "transfer-schemas"
                        self.yang_parent_name = "transfer"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("transfer-schema", ("transfer_schema", Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema))])
                        self._leafs = OrderedDict()

                        self.transfer_schema = YList(self)
                        self._segment_path = lambda: "transfer-schemas"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.BulkStats.Transfers.Transfer.TransferSchemas, [], name, value)


                    class TransferSchema(_Entity_):
                        """
                        Schema that contains objects to be collected
                        
                        .. attribute:: schema_name  (key)
                        
                        	Schema that contains objects to be collected
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2018-06-27'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema, self).__init__()

                            self.yang_name = "transfer-schema"
                            self.yang_parent_name = "transfer-schemas"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['schema_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('schema_name', (YLeaf(YType.str, 'schema-name'), ['str'])),
                            ])
                            self.schema_name = None
                            self._segment_path = lambda: "transfer-schema" + "[schema-name='" + str(self.schema_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema, ['schema_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.BulkStats.Transfers.Transfer.TransferSchemas']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.BulkStats.Transfers.Transfer']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.BulkStats.Transfers']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.BulkStats']['meta_info']


    class DefaultCommunityMaps(_Entity_):
        """
        Container class to hold unencrpted community map
        
        .. attribute:: default_community_map
        
        	Unencrpted SNMP community map name 
        	**type**\: list of  		 :py:class:`DefaultCommunityMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.DefaultCommunityMaps.DefaultCommunityMap>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.DefaultCommunityMaps, self).__init__()

            self.yang_name = "default-community-maps"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("default-community-map", ("default_community_map", Snmp.DefaultCommunityMaps.DefaultCommunityMap))])
            self._leafs = OrderedDict()

            self.default_community_map = YList(self)
            self._segment_path = lambda: "default-community-maps"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.DefaultCommunityMaps, [], name, value)


        class DefaultCommunityMap(_Entity_):
            """
            Unencrpted SNMP community map name 
            
            .. attribute:: community_name  (key)
            
            	SNMP community map
            	**type**\: str
            
            	**length:** 1..128
            
            .. attribute:: context
            
            	SNMP Context Name 
            	**type**\: str
            
            .. attribute:: security
            
            	SNMP Security Name 
            	**type**\: str
            
            .. attribute:: target_list
            
            	target list name 
            	**type**\: str
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.DefaultCommunityMaps.DefaultCommunityMap, self).__init__()

                self.yang_name = "default-community-map"
                self.yang_parent_name = "default-community-maps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['community_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('community_name', (YLeaf(YType.str, 'community-name'), ['str'])),
                    ('context', (YLeaf(YType.str, 'context'), ['str'])),
                    ('security', (YLeaf(YType.str, 'security'), ['str'])),
                    ('target_list', (YLeaf(YType.str, 'target-list'), ['str'])),
                ])
                self.community_name = None
                self.context = None
                self.security = None
                self.target_list = None
                self._segment_path = lambda: "default-community-map" + "[community-name='" + str(self.community_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/default-community-maps/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.DefaultCommunityMaps.DefaultCommunityMap, ['community_name', 'context', 'security', 'target_list'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.DefaultCommunityMaps.DefaultCommunityMap']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.DefaultCommunityMaps']['meta_info']


    class OverloadControl(_Entity_):
        """
        Set overload control params for handling
        incoming messages
        
        .. attribute:: drop_time
        
        	Drop time in seconds for incoming queue (default 1 sec)
        	**type**\: int
        
        	**range:** 0..300
        
        	**mandatory**\: True
        
        	**units**\: second
        
        .. attribute:: throttle_rate
        
        	Throttle time in milliseconds for incoming queue (default 500 msec)
        	**type**\: int
        
        	**range:** 0..1000
        
        	**mandatory**\: True
        
        	**units**\: millisecond
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.OverloadControl, self).__init__()

            self.yang_name = "overload-control"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('drop_time', (YLeaf(YType.uint32, 'drop-time'), ['int'])),
                ('throttle_rate', (YLeaf(YType.uint32, 'throttle-rate'), ['int'])),
            ])
            self.drop_time = None
            self.throttle_rate = None
            self._segment_path = lambda: "overload-control"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.OverloadControl, ['drop_time', 'throttle_rate'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.OverloadControl']['meta_info']


    class Timeouts(_Entity_):
        """
        SNMP timeouts
        
        .. attribute:: duplicates
        
        	Duplicate request feature timeout
        	**type**\: int
        
        	**range:** 0..20
        
        	**units**\: second
        
        	**default value**\: 1
        
        .. attribute:: in_qdrop
        
        	incoming queue drop feature timeout
        	**type**\: int
        
        	**range:** 0..20
        
        	**units**\: second
        
        	**default value**\: 10
        
        .. attribute:: threshold
        
        	Threshold request feature timeout
        	**type**\: int
        
        	**range:** 0..100000
        
        	**units**\: second
        
        	**default value**\: 50000
        
        .. attribute:: subagent
        
        	Sub\-Agent Request timeout
        	**type**\: int
        
        	**range:** 1..20
        
        	**units**\: second
        
        	**default value**\: 10
        
        .. attribute:: pdu_stats
        
        	SNMP pdu statistics timeout
        	**type**\: int
        
        	**range:** 1..10
        
        	**units**\: second
        
        	**default value**\: 2
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Timeouts, self).__init__()

            self.yang_name = "timeouts"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('duplicates', (YLeaf(YType.uint32, 'duplicates'), ['int'])),
                ('in_qdrop', (YLeaf(YType.uint32, 'in-qdrop'), ['int'])),
                ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                ('subagent', (YLeaf(YType.uint32, 'subagent'), ['int'])),
                ('pdu_stats', (YLeaf(YType.uint32, 'pdu-stats'), ['int'])),
            ])
            self.duplicates = None
            self.in_qdrop = None
            self.threshold = None
            self.subagent = None
            self.pdu_stats = None
            self._segment_path = lambda: "timeouts"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Timeouts, ['duplicates', 'in_qdrop', 'threshold', 'subagent', 'pdu_stats'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Timeouts']['meta_info']


    class Users(_Entity_):
        """
        Define a user who can access the SNMP engine
        
        .. attribute:: user
        
        	Name of the user
        	**type**\: list of  		 :py:class:`User <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Users.User>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Users, self).__init__()

            self.yang_name = "users"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("user", ("user", Snmp.Users.User))])
            self._leafs = OrderedDict()

            self.user = YList(self)
            self._segment_path = lambda: "users"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Users, [], name, value)


        class User(_Entity_):
            """
            Name of the user
            
            .. attribute:: user_name  (key)
            
            	Name of the user
            	**type**\: str
            
            .. attribute:: group_name
            
            	Group to which the user belongs
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: version
            
            	SNMP version to be used. v1,v2c or v3
            	**type**\:  :py:class:`UserSnmpVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.UserSnmpVersion>`
            
            	**mandatory**\: True
            
            .. attribute:: authentication_password_configured
            
            	Flag to indicate that authentication password is configred for version 3
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: algorithm
            
            	The algorithm used md5 or sha
            	**type**\:  :py:class:`SnmpHashAlgorithm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpHashAlgorithm>`
            
            .. attribute:: authentication_password
            
            	The authentication password
            	**type**\: str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: privacy_password_configured
            
            	Flag to indicate that the privacy password is configured for version 3
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: priv_algorithm
            
            	The algorithm used des56 or aes128 or aes192or aes256 or 3des
            	**type**\:  :py:class:`SnmpPrivAlgorithm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpPrivAlgorithm>`
            
            .. attribute:: privacy_password
            
            	The privacy password
            	**type**\: str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: v4acl_type
            
            	Access\-list type
            	**type**\:  :py:class:`Snmpacl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmpacl>`
            
            .. attribute:: v4_access_list
            
            	Ipv4 Access\-list name
            	**type**\: str
            
            .. attribute:: v6acl_type
            
            	Access\-list type
            	**type**\:  :py:class:`Snmpacl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmpacl>`
            
            .. attribute:: v6_access_list
            
            	Ipv6 Access\-list name
            	**type**\: str
            
            .. attribute:: owner
            
            	The system access either SDROwner or SystemOwner
            	**type**\:  :py:class:`SnmpOwnerAccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpOwnerAccess>`
            
            .. attribute:: remote_address
            
            	IP address of remote SNMP entity
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: port
            
            	UDP port number
            	**type**\: int
            
            	**range:** 1..65535
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Users.User, self).__init__()

                self.yang_name = "user"
                self.yang_parent_name = "users"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['user_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('user_name', (YLeaf(YType.str, 'user-name'), ['str'])),
                    ('group_name', (YLeaf(YType.str, 'group-name'), ['str'])),
                    ('version', (YLeaf(YType.enumeration, 'version'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'UserSnmpVersion', '')])),
                    ('authentication_password_configured', (YLeaf(YType.empty, 'authentication-password-configured'), ['Empty'])),
                    ('algorithm', (YLeaf(YType.enumeration, 'algorithm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpHashAlgorithm', '')])),
                    ('authentication_password', (YLeaf(YType.str, 'authentication-password'), ['str'])),
                    ('privacy_password_configured', (YLeaf(YType.empty, 'privacy-password-configured'), ['Empty'])),
                    ('priv_algorithm', (YLeaf(YType.enumeration, 'priv-algorithm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpPrivAlgorithm', '')])),
                    ('privacy_password', (YLeaf(YType.str, 'privacy-password'), ['str'])),
                    ('v4acl_type', (YLeaf(YType.enumeration, 'v4acl-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmpacl', '')])),
                    ('v4_access_list', (YLeaf(YType.str, 'v4-access-list'), ['str'])),
                    ('v6acl_type', (YLeaf(YType.enumeration, 'v6acl-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmpacl', '')])),
                    ('v6_access_list', (YLeaf(YType.str, 'v6-access-list'), ['str'])),
                    ('owner', (YLeaf(YType.enumeration, 'owner'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpOwnerAccess', '')])),
                    ('remote_address', (YLeaf(YType.str, 'remote-address'), ['str','str'])),
                    ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                ])
                self.user_name = None
                self.group_name = None
                self.version = None
                self.authentication_password_configured = None
                self.algorithm = None
                self.authentication_password = None
                self.privacy_password_configured = None
                self.priv_algorithm = None
                self.privacy_password = None
                self.v4acl_type = None
                self.v4_access_list = None
                self.v6acl_type = None
                self.v6_access_list = None
                self.owner = None
                self.remote_address = None
                self.port = None
                self._segment_path = lambda: "user" + "[user-name='" + str(self.user_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/users/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Users.User, ['user_name', 'group_name', 'version', 'authentication_password_configured', 'algorithm', 'authentication_password', 'privacy_password_configured', 'priv_algorithm', 'privacy_password', 'v4acl_type', 'v4_access_list', 'v6acl_type', 'v6_access_list', 'owner', 'remote_address', 'port'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Users.User']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Users']['meta_info']


    class Vrfs(_Entity_):
        """
        SNMP VRF configuration commands
        
        .. attribute:: vrf
        
        	VRF name
        	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf", ("vrf", Snmp.Vrfs.Vrf))])
            self._leafs = OrderedDict()

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Vrfs, [], name, value)


        class Vrf(_Entity_):
            """
            VRF name
            
            .. attribute:: name  (key)
            
            	VRF name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: trap_hosts
            
            	Specify hosts to receive SNMP notifications
            	**type**\:  :py:class:`TrapHosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts>`
            
            .. attribute:: contexts
            
            	List of Context Names
            	**type**\:  :py:class:`Contexts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.Contexts>`
            
            .. attribute:: context_mappings
            
            	List of context names
            	**type**\:  :py:class:`ContextMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.ContextMappings>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("trap-hosts", ("trap_hosts", Snmp.Vrfs.Vrf.TrapHosts)), ("contexts", ("contexts", Snmp.Vrfs.Vrf.Contexts)), ("context-mappings", ("context_mappings", Snmp.Vrfs.Vrf.ContextMappings))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None

                self.trap_hosts = Snmp.Vrfs.Vrf.TrapHosts()
                self.trap_hosts.parent = self
                self._children_name_map["trap_hosts"] = "trap-hosts"

                self.contexts = Snmp.Vrfs.Vrf.Contexts()
                self.contexts.parent = self
                self._children_name_map["contexts"] = "contexts"

                self.context_mappings = Snmp.Vrfs.Vrf.ContextMappings()
                self.context_mappings.parent = self
                self._children_name_map["context_mappings"] = "context-mappings"
                self._segment_path = lambda: "vrf" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Vrfs.Vrf, ['name'], name, value)


            class TrapHosts(_Entity_):
                """
                Specify hosts to receive SNMP notifications
                
                .. attribute:: trap_host
                
                	Specify hosts to receive SNMP notifications
                	**type**\: list of  		 :py:class:`TrapHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2018-06-27'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Vrfs.Vrf.TrapHosts, self).__init__()

                    self.yang_name = "trap-hosts"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("trap-host", ("trap_host", Snmp.Vrfs.Vrf.TrapHosts.TrapHost))])
                    self._leafs = OrderedDict()

                    self.trap_host = YList(self)
                    self._segment_path = lambda: "trap-hosts"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts, [], name, value)


                class TrapHost(_Entity_):
                    """
                    Specify hosts to receive SNMP notifications
                    
                    .. attribute:: ip_address  (key)
                    
                    	IP address of SNMP notification host
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: encrypted_user_communities
                    
                    	Container class for defining Clear/encrypt communities for a trap host
                    	**type**\:  :py:class:`EncryptedUserCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities>`
                    
                    .. attribute:: inform_host
                    
                    	Container class for defining notification type for a Inform host
                    	**type**\:  :py:class:`InformHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost>`
                    
                    .. attribute:: default_user_communities
                    
                    	Container class for defining communities for a trap host
                    	**type**\:  :py:class:`DefaultUserCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost, self).__init__()

                        self.yang_name = "trap-host"
                        self.yang_parent_name = "trap-hosts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['ip_address']
                        self._child_classes = OrderedDict([("encrypted-user-communities", ("encrypted_user_communities", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities)), ("inform-host", ("inform_host", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost)), ("default-user-communities", ("default_user_communities", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities))])
                        self._leafs = OrderedDict([
                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                        ])
                        self.ip_address = None

                        self.encrypted_user_communities = Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities()
                        self.encrypted_user_communities.parent = self
                        self._children_name_map["encrypted_user_communities"] = "encrypted-user-communities"

                        self.inform_host = Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost()
                        self.inform_host.parent = self
                        self._children_name_map["inform_host"] = "inform-host"

                        self.default_user_communities = Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities()
                        self.default_user_communities.parent = self
                        self._children_name_map["default_user_communities"] = "default-user-communities"
                        self._segment_path = lambda: "trap-host" + "[ip-address='" + str(self.ip_address) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost, ['ip_address'], name, value)


                    class EncryptedUserCommunities(_Entity_):
                        """
                        Container class for defining Clear/encrypt
                        communities for a trap host
                        
                        .. attribute:: encrypted_user_community
                        
                        	Clear/Encrypt Community name associated with a trap host
                        	**type**\: list of  		 :py:class:`EncryptedUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2018-06-27'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities, self).__init__()

                            self.yang_name = "encrypted-user-communities"
                            self.yang_parent_name = "trap-host"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("encrypted-user-community", ("encrypted_user_community", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity))])
                            self._leafs = OrderedDict()

                            self.encrypted_user_community = YList(self)
                            self._segment_path = lambda: "encrypted-user-communities"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities, [], name, value)


                        class EncryptedUserCommunity(_Entity_):
                            """
                            Clear/Encrypt Community name associated with
                            a trap host
                            
                            .. attribute:: community_name  (key)
                            
                            	SNMPv1/v2c community string or SNMPv3 user
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: port
                            
                            	UDP port number
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            	**default value**\: 162
                            
                            .. attribute:: version
                            
                            	SNMP Version to be used 1/2c/3
                            	**type**\: str
                            
                            	**default value**\: 1
                            
                            .. attribute:: security_level
                            
                            	Security level to be used noauth/auth/priv
                            	**type**\:  :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
                            
                            .. attribute:: basic_trap_types
                            
                            	Number to signify the feature traps that needs to be setBasicTrapTypes is used for all traps except copy\-completeSet this value to an integer corresponding to the trapBGP 8192, CONFIG 4096,SYSLOG 131072,SNMP\_TRAP 1COPY\_COMPLETE\_TRAP 64To provide a combination of trap Add the respective numbersValue must be set to 0 for all traps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 0
                            
                            .. attribute:: advanced_trap_types1
                            
                            	Number to signify the feature traps that needs to be setUse this for providing copy\-complete trapValue must be set to 0 if not used
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 0
                            
                            .. attribute:: advanced_trap_types2
                            
                            	Number to signify the feature traps that needs to be setvalue should always to set as 0
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 0
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2018-06-27'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity, self).__init__()

                                self.yang_name = "encrypted-user-community"
                                self.yang_parent_name = "encrypted-user-communities"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['community_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('community_name', (YLeaf(YType.str, 'community-name'), ['str'])),
                                    ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                                    ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                    ('security_level', (YLeaf(YType.enumeration, 'security-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel', '')])),
                                    ('basic_trap_types', (YLeaf(YType.uint32, 'basic-trap-types'), ['int'])),
                                    ('advanced_trap_types1', (YLeaf(YType.uint32, 'advanced-trap-types1'), ['int'])),
                                    ('advanced_trap_types2', (YLeaf(YType.uint32, 'advanced-trap-types2'), ['int'])),
                                ])
                                self.community_name = None
                                self.port = None
                                self.version = None
                                self.security_level = None
                                self.basic_trap_types = None
                                self.advanced_trap_types1 = None
                                self.advanced_trap_types2 = None
                                self._segment_path = lambda: "encrypted-user-community" + "[community-name='" + str(self.community_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity, ['community_name', 'port', 'version', 'security_level', 'basic_trap_types', 'advanced_trap_types1', 'advanced_trap_types2'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities']['meta_info']


                    class InformHost(_Entity_):
                        """
                        Container class for defining notification type
                        for a Inform host
                        
                        .. attribute:: inform_user_communities
                        
                        	Container class for defining communities for a inform host
                        	**type**\:  :py:class:`InformUserCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities>`
                        
                        .. attribute:: inform_encrypted_user_communities
                        
                        	Container class for defining Clear/encrypt communities for a inform host
                        	**type**\:  :py:class:`InformEncryptedUserCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2018-06-27'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost, self).__init__()

                            self.yang_name = "inform-host"
                            self.yang_parent_name = "trap-host"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("inform-user-communities", ("inform_user_communities", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities)), ("inform-encrypted-user-communities", ("inform_encrypted_user_communities", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities))])
                            self._leafs = OrderedDict()

                            self.inform_user_communities = Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities()
                            self.inform_user_communities.parent = self
                            self._children_name_map["inform_user_communities"] = "inform-user-communities"

                            self.inform_encrypted_user_communities = Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities()
                            self.inform_encrypted_user_communities.parent = self
                            self._children_name_map["inform_encrypted_user_communities"] = "inform-encrypted-user-communities"
                            self._segment_path = lambda: "inform-host"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost, [], name, value)


                        class InformUserCommunities(_Entity_):
                            """
                            Container class for defining communities for
                            a inform host
                            
                            .. attribute:: inform_user_community
                            
                            	Unencrpted Community name associated with a inform host
                            	**type**\: list of  		 :py:class:`InformUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity>`
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2018-06-27'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities, self).__init__()

                                self.yang_name = "inform-user-communities"
                                self.yang_parent_name = "inform-host"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("inform-user-community", ("inform_user_community", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity))])
                                self._leafs = OrderedDict()

                                self.inform_user_community = YList(self)
                                self._segment_path = lambda: "inform-user-communities"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities, [], name, value)


                            class InformUserCommunity(_Entity_):
                                """
                                Unencrpted Community name associated with a
                                inform host
                                
                                .. attribute:: community_name  (key)
                                
                                	SNMPv2c community string or SNMPv3 user
                                	**type**\: str
                                
                                	**length:** 1..128
                                
                                .. attribute:: port
                                
                                	UDP port number
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**default value**\: 162
                                
                                .. attribute:: version
                                
                                	SNMP Version to be used 2c/3
                                	**type**\: str
                                
                                	**default value**\: 2c
                                
                                .. attribute:: security_level
                                
                                	Security level to be used noauth/auth/priv
                                	**type**\:  :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
                                
                                .. attribute:: basic_trap_types
                                
                                	Number to signify the feature traps that needs to be setBasicTrapTypes is used for all traps except copy\-completeSet this value to an integer corresponding to the trapBGP 8192, CONFIG 4096,SYSLOG 131072 ,SNMP\_TRAP 1COPY\_COMPLETE\_TRAP 64To provide a combination of trap Add the respective numbersValue must be set to 0 for all traps
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**default value**\: 0
                                
                                .. attribute:: advanced_trap_types1
                                
                                	Number to signify the feature traps that needs to be setUse this for providing copy\-complete trapValue must be set to 0 if not used
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**default value**\: 0
                                
                                .. attribute:: advanced_trap_types2
                                
                                	Number to signify the feature traps that needs to be setvalue should always to set as 0
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**default value**\: 0
                                
                                

                                """

                                _prefix = 'snmp-agent-cfg'
                                _revision = '2018-06-27'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity, self).__init__()

                                    self.yang_name = "inform-user-community"
                                    self.yang_parent_name = "inform-user-communities"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['community_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('community_name', (YLeaf(YType.str, 'community-name'), ['str'])),
                                        ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                                        ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                        ('security_level', (YLeaf(YType.enumeration, 'security-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel', '')])),
                                        ('basic_trap_types', (YLeaf(YType.uint32, 'basic-trap-types'), ['int'])),
                                        ('advanced_trap_types1', (YLeaf(YType.uint32, 'advanced-trap-types1'), ['int'])),
                                        ('advanced_trap_types2', (YLeaf(YType.uint32, 'advanced-trap-types2'), ['int'])),
                                    ])
                                    self.community_name = None
                                    self.port = None
                                    self.version = None
                                    self.security_level = None
                                    self.basic_trap_types = None
                                    self.advanced_trap_types1 = None
                                    self.advanced_trap_types2 = None
                                    self._segment_path = lambda: "inform-user-community" + "[community-name='" + str(self.community_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity, ['community_name', 'port', 'version', 'security_level', 'basic_trap_types', 'advanced_trap_types1', 'advanced_trap_types2'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                    return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities']['meta_info']


                        class InformEncryptedUserCommunities(_Entity_):
                            """
                            Container class for defining Clear/encrypt
                            communities for a inform host
                            
                            .. attribute:: inform_encrypted_user_community
                            
                            	Clear/Encrypt Community name associated with a inform host
                            	**type**\: list of  		 :py:class:`InformEncryptedUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity>`
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2018-06-27'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities, self).__init__()

                                self.yang_name = "inform-encrypted-user-communities"
                                self.yang_parent_name = "inform-host"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("inform-encrypted-user-community", ("inform_encrypted_user_community", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity))])
                                self._leafs = OrderedDict()

                                self.inform_encrypted_user_community = YList(self)
                                self._segment_path = lambda: "inform-encrypted-user-communities"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities, [], name, value)


                            class InformEncryptedUserCommunity(_Entity_):
                                """
                                Clear/Encrypt Community name associated with
                                a inform host
                                
                                .. attribute:: community_name  (key)
                                
                                	SNMPv2c community string or SNMPv3 user
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: port
                                
                                	UDP port number
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**default value**\: 162
                                
                                .. attribute:: version
                                
                                	SNMP Version to be used 2c/3
                                	**type**\: str
                                
                                	**default value**\: 2c
                                
                                .. attribute:: security_level
                                
                                	Security level to be used noauth/auth/priv
                                	**type**\:  :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
                                
                                .. attribute:: basic_trap_types
                                
                                	Number to signify the feature traps that needs to be setBasicTrapTypes is used for all traps except copy\-completeSet this value to an integer corresponding to the trapBGP 8192, CONFIG 4096,SYSLOG 131072 ,SNMP\_TRAP 1COPY\_COMPLETE\_TRAP 64To provide a combination of trap Add the respective numbersValue must be set to 0 for all traps
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**default value**\: 0
                                
                                .. attribute:: advanced_trap_types1
                                
                                	Number to signify the feature traps that needs to be setUse this for providing copy\-complete trapValue must be set to 0 if not used
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**default value**\: 0
                                
                                .. attribute:: advanced_trap_types2
                                
                                	Number to signify the feature traps that needs to be setvalue should always to set as 0
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**default value**\: 0
                                
                                

                                """

                                _prefix = 'snmp-agent-cfg'
                                _revision = '2018-06-27'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity, self).__init__()

                                    self.yang_name = "inform-encrypted-user-community"
                                    self.yang_parent_name = "inform-encrypted-user-communities"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['community_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('community_name', (YLeaf(YType.str, 'community-name'), ['str'])),
                                        ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                                        ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                        ('security_level', (YLeaf(YType.enumeration, 'security-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel', '')])),
                                        ('basic_trap_types', (YLeaf(YType.uint32, 'basic-trap-types'), ['int'])),
                                        ('advanced_trap_types1', (YLeaf(YType.uint32, 'advanced-trap-types1'), ['int'])),
                                        ('advanced_trap_types2', (YLeaf(YType.uint32, 'advanced-trap-types2'), ['int'])),
                                    ])
                                    self.community_name = None
                                    self.port = None
                                    self.version = None
                                    self.security_level = None
                                    self.basic_trap_types = None
                                    self.advanced_trap_types1 = None
                                    self.advanced_trap_types2 = None
                                    self._segment_path = lambda: "inform-encrypted-user-community" + "[community-name='" + str(self.community_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity, ['community_name', 'port', 'version', 'security_level', 'basic_trap_types', 'advanced_trap_types1', 'advanced_trap_types2'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                    return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost']['meta_info']


                    class DefaultUserCommunities(_Entity_):
                        """
                        Container class for defining communities for a
                        trap host
                        
                        .. attribute:: default_user_community
                        
                        	Unencrpted Community name associated with a trap host
                        	**type**\: list of  		 :py:class:`DefaultUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2018-06-27'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities, self).__init__()

                            self.yang_name = "default-user-communities"
                            self.yang_parent_name = "trap-host"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("default-user-community", ("default_user_community", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity))])
                            self._leafs = OrderedDict()

                            self.default_user_community = YList(self)
                            self._segment_path = lambda: "default-user-communities"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities, [], name, value)


                        class DefaultUserCommunity(_Entity_):
                            """
                            Unencrpted Community name associated with a
                            trap host
                            
                            .. attribute:: community_name  (key)
                            
                            	SNMPv1/v2c community string or SNMPv3 user
                            	**type**\: str
                            
                            	**length:** 1..128
                            
                            .. attribute:: port
                            
                            	UDP port number
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            	**default value**\: 162
                            
                            .. attribute:: version
                            
                            	SNMP Version to be used 1/2c/3
                            	**type**\: str
                            
                            	**default value**\: 1
                            
                            .. attribute:: security_level
                            
                            	Security level to be used noauth/auth/priv
                            	**type**\:  :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
                            
                            .. attribute:: basic_trap_types
                            
                            	Number to signify the feature traps that needs to be setBasicTrapTypes is used for all traps except copy\-completeSet this value to an integer corresponding to the trapBGP 8192, CONFIG 4096,SYSLOG 131072,SNMP\_TRAP 1COPY\_COMPLETE\_TRAP 64To provide a combination of trap Add the respective numbersValue must be set to 0 for all traps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 0
                            
                            .. attribute:: advanced_trap_types1
                            
                            	Number to signify the feature traps that needs to be setUse this for providing copy\-complete trapValue must be set to 0 if not used
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 0
                            
                            .. attribute:: advanced_trap_types2
                            
                            	Number to signify the feature traps that needs to be setvalue should always to set as 0
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 0
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2018-06-27'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity, self).__init__()

                                self.yang_name = "default-user-community"
                                self.yang_parent_name = "default-user-communities"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['community_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('community_name', (YLeaf(YType.str, 'community-name'), ['str'])),
                                    ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                                    ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                    ('security_level', (YLeaf(YType.enumeration, 'security-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel', '')])),
                                    ('basic_trap_types', (YLeaf(YType.uint32, 'basic-trap-types'), ['int'])),
                                    ('advanced_trap_types1', (YLeaf(YType.uint32, 'advanced-trap-types1'), ['int'])),
                                    ('advanced_trap_types2', (YLeaf(YType.uint32, 'advanced-trap-types2'), ['int'])),
                                ])
                                self.community_name = None
                                self.port = None
                                self.version = None
                                self.security_level = None
                                self.basic_trap_types = None
                                self.advanced_trap_types1 = None
                                self.advanced_trap_types2 = None
                                self._segment_path = lambda: "default-user-community" + "[community-name='" + str(self.community_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity, ['community_name', 'port', 'version', 'security_level', 'basic_trap_types', 'advanced_trap_types1', 'advanced_trap_types2'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Vrfs.Vrf.TrapHosts']['meta_info']


            class Contexts(_Entity_):
                """
                List of Context Names
                
                .. attribute:: context
                
                	Context Name
                	**type**\: list of  		 :py:class:`Context <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.Contexts.Context>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2018-06-27'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Vrfs.Vrf.Contexts, self).__init__()

                    self.yang_name = "contexts"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("context", ("context", Snmp.Vrfs.Vrf.Contexts.Context))])
                    self._leafs = OrderedDict()

                    self.context = YList(self)
                    self._segment_path = lambda: "contexts"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Vrfs.Vrf.Contexts, [], name, value)


                class Context(_Entity_):
                    """
                    Context Name
                    
                    .. attribute:: context_name  (key)
                    
                    	Context Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Vrfs.Vrf.Contexts.Context, self).__init__()

                        self.yang_name = "context"
                        self.yang_parent_name = "contexts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['context_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('context_name', (YLeaf(YType.str, 'context-name'), ['str'])),
                        ])
                        self.context_name = None
                        self._segment_path = lambda: "context" + "[context-name='" + str(self.context_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Vrfs.Vrf.Contexts.Context, ['context_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Vrfs.Vrf.Contexts.Context']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Vrfs.Vrf.Contexts']['meta_info']


            class ContextMappings(_Entity_):
                """
                List of context names
                
                .. attribute:: context_mapping
                
                	Context mapping name
                	**type**\: list of  		 :py:class:`ContextMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.ContextMappings.ContextMapping>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2018-06-27'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.Vrfs.Vrf.ContextMappings, self).__init__()

                    self.yang_name = "context-mappings"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("context-mapping", ("context_mapping", Snmp.Vrfs.Vrf.ContextMappings.ContextMapping))])
                    self._leafs = OrderedDict()

                    self.context_mapping = YList(self)
                    self._segment_path = lambda: "context-mappings"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Vrfs.Vrf.ContextMappings, [], name, value)


                class ContextMapping(_Entity_):
                    """
                    Context mapping name
                    
                    .. attribute:: context_mapping_name  (key)
                    
                    	Context mapping name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: context
                    
                    	SNMP context feature type
                    	**type**\:  :py:class:`SnmpContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpContext>`
                    
                    .. attribute:: instance_name
                    
                    	OSPF protocol instance
                    	**type**\: str
                    
                    .. attribute:: vrf_name
                    
                    	VRF name associated with the context
                    	**type**\: str
                    
                    .. attribute:: topology_name
                    
                    	Topology name associated with the context
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.Vrfs.Vrf.ContextMappings.ContextMapping, self).__init__()

                        self.yang_name = "context-mapping"
                        self.yang_parent_name = "context-mappings"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['context_mapping_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('context_mapping_name', (YLeaf(YType.str, 'context-mapping-name'), ['str'])),
                            ('context', (YLeaf(YType.enumeration, 'context'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpContext', '')])),
                            ('instance_name', (YLeaf(YType.str, 'instance-name'), ['str'])),
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('topology_name', (YLeaf(YType.str, 'topology-name'), ['str'])),
                        ])
                        self.context_mapping_name = None
                        self.context = None
                        self.instance_name = None
                        self.vrf_name = None
                        self.topology_name = None
                        self._segment_path = lambda: "context-mapping" + "[context-mapping-name='" + str(self.context_mapping_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Vrfs.Vrf.ContextMappings.ContextMapping, ['context_mapping_name', 'context', 'instance_name', 'vrf_name', 'topology_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.Vrfs.Vrf.ContextMappings.ContextMapping']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.Vrfs.Vrf.ContextMappings']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Vrfs.Vrf']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Vrfs']['meta_info']


    class Groups(_Entity_):
        """
        Define a User Security Model group
        
        .. attribute:: group
        
        	Name of the group
        	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Groups.Group>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("group", ("group", Snmp.Groups.Group))])
            self._leafs = OrderedDict()

            self.group = YList(self)
            self._segment_path = lambda: "groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Groups, [], name, value)


        class Group(_Entity_):
            """
            Name of the group
            
            .. attribute:: name  (key)
            
            	Name of the group
            	**type**\: str
            
            	**length:** 1..128
            
            .. attribute:: snmp_version
            
            	snmp version
            	**type**\:  :py:class:`GroupSnmpVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.GroupSnmpVersion>`
            
            	**mandatory**\: True
            
            .. attribute:: security_model
            
            	security model like auth/noAuth/Priv applicable for v3
            	**type**\:  :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
            
            .. attribute:: notify_view
            
            	notify view name
            	**type**\: str
            
            .. attribute:: read_view
            
            	read view name
            	**type**\: str
            
            .. attribute:: write_view
            
            	write view name
            	**type**\: str
            
            .. attribute:: v4acl_type
            
            	Access\-list type
            	**type**\:  :py:class:`Snmpacl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmpacl>`
            
            .. attribute:: v4_access_list
            
            	Ipv4 Access\-list name
            	**type**\: str
            
            .. attribute:: v6acl_type
            
            	Access\-list type
            	**type**\:  :py:class:`Snmpacl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmpacl>`
            
            .. attribute:: v6_access_list
            
            	Ipv6 Access\-list name
            	**type**\: str
            
            .. attribute:: context_name
            
            	Context name
            	**type**\: str
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Groups.Group, self).__init__()

                self.yang_name = "group"
                self.yang_parent_name = "groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('snmp_version', (YLeaf(YType.enumeration, 'snmp-version'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'GroupSnmpVersion', '')])),
                    ('security_model', (YLeaf(YType.enumeration, 'security-model'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel', '')])),
                    ('notify_view', (YLeaf(YType.str, 'notify-view'), ['str'])),
                    ('read_view', (YLeaf(YType.str, 'read-view'), ['str'])),
                    ('write_view', (YLeaf(YType.str, 'write-view'), ['str'])),
                    ('v4acl_type', (YLeaf(YType.enumeration, 'v4acl-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmpacl', '')])),
                    ('v4_access_list', (YLeaf(YType.str, 'v4-access-list'), ['str'])),
                    ('v6acl_type', (YLeaf(YType.enumeration, 'v6acl-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmpacl', '')])),
                    ('v6_access_list', (YLeaf(YType.str, 'v6-access-list'), ['str'])),
                    ('context_name', (YLeaf(YType.str, 'context-name'), ['str'])),
                ])
                self.name = None
                self.snmp_version = None
                self.security_model = None
                self.notify_view = None
                self.read_view = None
                self.write_view = None
                self.v4acl_type = None
                self.v4_access_list = None
                self.v6acl_type = None
                self.v6_access_list = None
                self.context_name = None
                self._segment_path = lambda: "group" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/groups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Groups.Group, ['name', 'snmp_version', 'security_model', 'notify_view', 'read_view', 'write_view', 'v4acl_type', 'v4_access_list', 'v6acl_type', 'v6_access_list', 'context_name'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Groups.Group']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Groups']['meta_info']


    class TrapHosts(_Entity_):
        """
        Specify hosts to receive SNMP notifications
        
        .. attribute:: trap_host
        
        	Specify hosts to receive SNMP notifications
        	**type**\: list of  		 :py:class:`TrapHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.TrapHosts, self).__init__()

            self.yang_name = "trap-hosts"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("trap-host", ("trap_host", Snmp.TrapHosts.TrapHost))])
            self._leafs = OrderedDict()

            self.trap_host = YList(self)
            self._segment_path = lambda: "trap-hosts"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.TrapHosts, [], name, value)


        class TrapHost(_Entity_):
            """
            Specify hosts to receive SNMP notifications
            
            .. attribute:: ip_address  (key)
            
            	IP address of SNMP notification host
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: encrypted_user_communities
            
            	Container class for defining Clear/encrypt communities for a trap host
            	**type**\:  :py:class:`EncryptedUserCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.EncryptedUserCommunities>`
            
            .. attribute:: inform_host
            
            	Container class for defining notification type for a Inform host
            	**type**\:  :py:class:`InformHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.InformHost>`
            
            .. attribute:: default_user_communities
            
            	Container class for defining communities for a trap host
            	**type**\:  :py:class:`DefaultUserCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.DefaultUserCommunities>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.TrapHosts.TrapHost, self).__init__()

                self.yang_name = "trap-host"
                self.yang_parent_name = "trap-hosts"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ip_address']
                self._child_classes = OrderedDict([("encrypted-user-communities", ("encrypted_user_communities", Snmp.TrapHosts.TrapHost.EncryptedUserCommunities)), ("inform-host", ("inform_host", Snmp.TrapHosts.TrapHost.InformHost)), ("default-user-communities", ("default_user_communities", Snmp.TrapHosts.TrapHost.DefaultUserCommunities))])
                self._leafs = OrderedDict([
                    ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                ])
                self.ip_address = None

                self.encrypted_user_communities = Snmp.TrapHosts.TrapHost.EncryptedUserCommunities()
                self.encrypted_user_communities.parent = self
                self._children_name_map["encrypted_user_communities"] = "encrypted-user-communities"

                self.inform_host = Snmp.TrapHosts.TrapHost.InformHost()
                self.inform_host.parent = self
                self._children_name_map["inform_host"] = "inform-host"

                self.default_user_communities = Snmp.TrapHosts.TrapHost.DefaultUserCommunities()
                self.default_user_communities.parent = self
                self._children_name_map["default_user_communities"] = "default-user-communities"
                self._segment_path = lambda: "trap-host" + "[ip-address='" + str(self.ip_address) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/trap-hosts/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.TrapHosts.TrapHost, ['ip_address'], name, value)


            class EncryptedUserCommunities(_Entity_):
                """
                Container class for defining Clear/encrypt
                communities for a trap host
                
                .. attribute:: encrypted_user_community
                
                	Clear/Encrypt Community name associated with a trap host
                	**type**\: list of  		 :py:class:`EncryptedUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2018-06-27'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.TrapHosts.TrapHost.EncryptedUserCommunities, self).__init__()

                    self.yang_name = "encrypted-user-communities"
                    self.yang_parent_name = "trap-host"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("encrypted-user-community", ("encrypted_user_community", Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity))])
                    self._leafs = OrderedDict()

                    self.encrypted_user_community = YList(self)
                    self._segment_path = lambda: "encrypted-user-communities"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.TrapHosts.TrapHost.EncryptedUserCommunities, [], name, value)


                class EncryptedUserCommunity(_Entity_):
                    """
                    Clear/Encrypt Community name associated with
                    a trap host
                    
                    .. attribute:: community_name  (key)
                    
                    	SNMPv1/v2c community string or SNMPv3 user
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: port
                    
                    	UDP port number
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**default value**\: 162
                    
                    .. attribute:: version
                    
                    	SNMP Version to be used 1/2c/3
                    	**type**\: str
                    
                    	**default value**\: 1
                    
                    .. attribute:: security_level
                    
                    	Security level to be used noauth/auth/priv
                    	**type**\:  :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
                    
                    .. attribute:: basic_trap_types
                    
                    	Number to signify the feature traps that needs to be setBasicTrapTypes is used for all traps except copy\-completeSet this value to an integer corresponding to the trapBGP 8192, CONFIG 4096,SYSLOG 131072,SNMP\_TRAP 1COPY\_COMPLETE\_TRAP 64To provide a combination of trap Add the respective numbersValue must be set to 0 for all traps
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 0
                    
                    .. attribute:: advanced_trap_types1
                    
                    	Number to signify the feature traps that needs to be setUse this for providing copy\-complete trapValue must be set to 0 if not used
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 0
                    
                    .. attribute:: advanced_trap_types2
                    
                    	Number to signify the feature traps that needs to be setvalue should always to set as 0
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 0
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity, self).__init__()

                        self.yang_name = "encrypted-user-community"
                        self.yang_parent_name = "encrypted-user-communities"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['community_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('community_name', (YLeaf(YType.str, 'community-name'), ['str'])),
                            ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                            ('version', (YLeaf(YType.str, 'version'), ['str'])),
                            ('security_level', (YLeaf(YType.enumeration, 'security-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel', '')])),
                            ('basic_trap_types', (YLeaf(YType.uint32, 'basic-trap-types'), ['int'])),
                            ('advanced_trap_types1', (YLeaf(YType.uint32, 'advanced-trap-types1'), ['int'])),
                            ('advanced_trap_types2', (YLeaf(YType.uint32, 'advanced-trap-types2'), ['int'])),
                        ])
                        self.community_name = None
                        self.port = None
                        self.version = None
                        self.security_level = None
                        self.basic_trap_types = None
                        self.advanced_trap_types1 = None
                        self.advanced_trap_types2 = None
                        self._segment_path = lambda: "encrypted-user-community" + "[community-name='" + str(self.community_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity, ['community_name', 'port', 'version', 'security_level', 'basic_trap_types', 'advanced_trap_types1', 'advanced_trap_types2'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.TrapHosts.TrapHost.EncryptedUserCommunities']['meta_info']


            class InformHost(_Entity_):
                """
                Container class for defining notification type
                for a Inform host
                
                .. attribute:: inform_user_communities
                
                	Container class for defining communities for a inform host
                	**type**\:  :py:class:`InformUserCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities>`
                
                .. attribute:: inform_encrypted_user_communities
                
                	Container class for defining Clear/encrypt communities for a inform host
                	**type**\:  :py:class:`InformEncryptedUserCommunities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2018-06-27'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.TrapHosts.TrapHost.InformHost, self).__init__()

                    self.yang_name = "inform-host"
                    self.yang_parent_name = "trap-host"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("inform-user-communities", ("inform_user_communities", Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities)), ("inform-encrypted-user-communities", ("inform_encrypted_user_communities", Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities))])
                    self._leafs = OrderedDict()

                    self.inform_user_communities = Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities()
                    self.inform_user_communities.parent = self
                    self._children_name_map["inform_user_communities"] = "inform-user-communities"

                    self.inform_encrypted_user_communities = Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities()
                    self.inform_encrypted_user_communities.parent = self
                    self._children_name_map["inform_encrypted_user_communities"] = "inform-encrypted-user-communities"
                    self._segment_path = lambda: "inform-host"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.TrapHosts.TrapHost.InformHost, [], name, value)


                class InformUserCommunities(_Entity_):
                    """
                    Container class for defining communities for
                    a inform host
                    
                    .. attribute:: inform_user_community
                    
                    	Unencrpted Community name associated with a inform host
                    	**type**\: list of  		 :py:class:`InformUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities, self).__init__()

                        self.yang_name = "inform-user-communities"
                        self.yang_parent_name = "inform-host"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("inform-user-community", ("inform_user_community", Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity))])
                        self._leafs = OrderedDict()

                        self.inform_user_community = YList(self)
                        self._segment_path = lambda: "inform-user-communities"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities, [], name, value)


                    class InformUserCommunity(_Entity_):
                        """
                        Unencrpted Community name associated with a
                        inform host
                        
                        .. attribute:: community_name  (key)
                        
                        	SNMPv2c community string or SNMPv3 user
                        	**type**\: str
                        
                        	**length:** 1..128
                        
                        .. attribute:: port
                        
                        	UDP port number
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        	**default value**\: 162
                        
                        .. attribute:: version
                        
                        	SNMP Version to be used 2c/3
                        	**type**\: str
                        
                        	**default value**\: 2c
                        
                        .. attribute:: security_level
                        
                        	Security level to be used noauth/auth/priv
                        	**type**\:  :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
                        
                        .. attribute:: basic_trap_types
                        
                        	Number to signify the feature traps that needs to be setBasicTrapTypes is used for all traps except copy\-completeSet this value to an integer corresponding to the trapBGP 8192, CONFIG 4096,SYSLOG 131072 ,SNMP\_TRAP 1COPY\_COMPLETE\_TRAP 64To provide a combination of trap Add the respective numbersValue must be set to 0 for all traps
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: advanced_trap_types1
                        
                        	Number to signify the feature traps that needs to be setUse this for providing copy\-complete trapValue must be set to 0 if not used
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: advanced_trap_types2
                        
                        	Number to signify the feature traps that needs to be setvalue should always to set as 0
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2018-06-27'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity, self).__init__()

                            self.yang_name = "inform-user-community"
                            self.yang_parent_name = "inform-user-communities"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['community_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('community_name', (YLeaf(YType.str, 'community-name'), ['str'])),
                                ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('security_level', (YLeaf(YType.enumeration, 'security-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel', '')])),
                                ('basic_trap_types', (YLeaf(YType.uint32, 'basic-trap-types'), ['int'])),
                                ('advanced_trap_types1', (YLeaf(YType.uint32, 'advanced-trap-types1'), ['int'])),
                                ('advanced_trap_types2', (YLeaf(YType.uint32, 'advanced-trap-types2'), ['int'])),
                            ])
                            self.community_name = None
                            self.port = None
                            self.version = None
                            self.security_level = None
                            self.basic_trap_types = None
                            self.advanced_trap_types1 = None
                            self.advanced_trap_types2 = None
                            self._segment_path = lambda: "inform-user-community" + "[community-name='" + str(self.community_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity, ['community_name', 'port', 'version', 'security_level', 'basic_trap_types', 'advanced_trap_types1', 'advanced_trap_types2'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities']['meta_info']


                class InformEncryptedUserCommunities(_Entity_):
                    """
                    Container class for defining Clear/encrypt
                    communities for a inform host
                    
                    .. attribute:: inform_encrypted_user_community
                    
                    	Clear/Encrypt Community name associated with a inform host
                    	**type**\: list of  		 :py:class:`InformEncryptedUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities, self).__init__()

                        self.yang_name = "inform-encrypted-user-communities"
                        self.yang_parent_name = "inform-host"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("inform-encrypted-user-community", ("inform_encrypted_user_community", Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity))])
                        self._leafs = OrderedDict()

                        self.inform_encrypted_user_community = YList(self)
                        self._segment_path = lambda: "inform-encrypted-user-communities"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities, [], name, value)


                    class InformEncryptedUserCommunity(_Entity_):
                        """
                        Clear/Encrypt Community name associated with
                        a inform host
                        
                        .. attribute:: community_name  (key)
                        
                        	SNMPv2c community string or SNMPv3 user
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: port
                        
                        	UDP port number
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        	**default value**\: 162
                        
                        .. attribute:: version
                        
                        	SNMP Version to be used 2c/3
                        	**type**\: str
                        
                        	**default value**\: 2c
                        
                        .. attribute:: security_level
                        
                        	Security level to be used noauth/auth/priv
                        	**type**\:  :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
                        
                        .. attribute:: basic_trap_types
                        
                        	Number to signify the feature traps that needs to be setBasicTrapTypes is used for all traps except copy\-completeSet this value to an integer corresponding to the trapBGP 8192, CONFIG 4096,SYSLOG 131072 ,SNMP\_TRAP 1COPY\_COMPLETE\_TRAP 64To provide a combination of trap Add the respective numbersValue must be set to 0 for all traps
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: advanced_trap_types1
                        
                        	Number to signify the feature traps that needs to be setUse this for providing copy\-complete trapValue must be set to 0 if not used
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: advanced_trap_types2
                        
                        	Number to signify the feature traps that needs to be setvalue should always to set as 0
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2018-06-27'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity, self).__init__()

                            self.yang_name = "inform-encrypted-user-community"
                            self.yang_parent_name = "inform-encrypted-user-communities"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['community_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('community_name', (YLeaf(YType.str, 'community-name'), ['str'])),
                                ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                                ('security_level', (YLeaf(YType.enumeration, 'security-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel', '')])),
                                ('basic_trap_types', (YLeaf(YType.uint32, 'basic-trap-types'), ['int'])),
                                ('advanced_trap_types1', (YLeaf(YType.uint32, 'advanced-trap-types1'), ['int'])),
                                ('advanced_trap_types2', (YLeaf(YType.uint32, 'advanced-trap-types2'), ['int'])),
                            ])
                            self.community_name = None
                            self.port = None
                            self.version = None
                            self.security_level = None
                            self.basic_trap_types = None
                            self.advanced_trap_types1 = None
                            self.advanced_trap_types2 = None
                            self._segment_path = lambda: "inform-encrypted-user-community" + "[community-name='" + str(self.community_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity, ['community_name', 'port', 'version', 'security_level', 'basic_trap_types', 'advanced_trap_types1', 'advanced_trap_types2'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.TrapHosts.TrapHost.InformHost']['meta_info']


            class DefaultUserCommunities(_Entity_):
                """
                Container class for defining communities for a
                trap host
                
                .. attribute:: default_user_community
                
                	Unencrpted Community name associated with a trap host
                	**type**\: list of  		 :py:class:`DefaultUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2018-06-27'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Snmp.TrapHosts.TrapHost.DefaultUserCommunities, self).__init__()

                    self.yang_name = "default-user-communities"
                    self.yang_parent_name = "trap-host"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("default-user-community", ("default_user_community", Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity))])
                    self._leafs = OrderedDict()

                    self.default_user_community = YList(self)
                    self._segment_path = lambda: "default-user-communities"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.TrapHosts.TrapHost.DefaultUserCommunities, [], name, value)


                class DefaultUserCommunity(_Entity_):
                    """
                    Unencrpted Community name associated with a
                    trap host
                    
                    .. attribute:: community_name  (key)
                    
                    	SNMPv1/v2c community string or SNMPv3 user
                    	**type**\: str
                    
                    	**length:** 1..128
                    
                    .. attribute:: port
                    
                    	UDP port number
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**default value**\: 162
                    
                    .. attribute:: version
                    
                    	SNMP Version to be used 1/2c/3
                    	**type**\: str
                    
                    	**default value**\: 1
                    
                    .. attribute:: security_level
                    
                    	Security level to be used noauth/auth/priv
                    	**type**\:  :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
                    
                    .. attribute:: basic_trap_types
                    
                    	Number to signify the feature traps that needs to be setBasicTrapTypes is used for all traps except copy\-completeSet this value to an integer corresponding to the trapBGP 8192, CONFIG 4096,SYSLOG 131072,SNMP\_TRAP 1COPY\_COMPLETE\_TRAP 64To provide a combination of trap Add the respective numbersValue must be set to 0 for all traps
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 0
                    
                    .. attribute:: advanced_trap_types1
                    
                    	Number to signify the feature traps that needs to be setUse this for providing copy\-complete trapValue must be set to 0 if not used
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 0
                    
                    .. attribute:: advanced_trap_types2
                    
                    	Number to signify the feature traps that needs to be setvalue should always to set as 0
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 0
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2018-06-27'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity, self).__init__()

                        self.yang_name = "default-user-community"
                        self.yang_parent_name = "default-user-communities"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['community_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('community_name', (YLeaf(YType.str, 'community-name'), ['str'])),
                            ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                            ('version', (YLeaf(YType.str, 'version'), ['str'])),
                            ('security_level', (YLeaf(YType.enumeration, 'security-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModel', '')])),
                            ('basic_trap_types', (YLeaf(YType.uint32, 'basic-trap-types'), ['int'])),
                            ('advanced_trap_types1', (YLeaf(YType.uint32, 'advanced-trap-types1'), ['int'])),
                            ('advanced_trap_types2', (YLeaf(YType.uint32, 'advanced-trap-types2'), ['int'])),
                        ])
                        self.community_name = None
                        self.port = None
                        self.version = None
                        self.security_level = None
                        self.basic_trap_types = None
                        self.advanced_trap_types1 = None
                        self.advanced_trap_types2 = None
                        self._segment_path = lambda: "default-user-community" + "[community-name='" + str(self.community_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity, ['community_name', 'port', 'version', 'security_level', 'basic_trap_types', 'advanced_trap_types1', 'advanced_trap_types2'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Snmp.TrapHosts.TrapHost.DefaultUserCommunities']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.TrapHosts.TrapHost']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.TrapHosts']['meta_info']


    class Contexts(_Entity_):
        """
        List of Context Names
        
        .. attribute:: context
        
        	Context Name
        	**type**\: list of  		 :py:class:`Context <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Contexts.Context>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.Contexts, self).__init__()

            self.yang_name = "contexts"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("context", ("context", Snmp.Contexts.Context))])
            self._leafs = OrderedDict()

            self.context = YList(self)
            self._segment_path = lambda: "contexts"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Contexts, [], name, value)


        class Context(_Entity_):
            """
            Context Name
            
            .. attribute:: context_name  (key)
            
            	Context Name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.Contexts.Context, self).__init__()

                self.yang_name = "context"
                self.yang_parent_name = "contexts"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['context_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('context_name', (YLeaf(YType.str, 'context-name'), ['str'])),
                ])
                self.context_name = None
                self._segment_path = lambda: "context" + "[context-name='" + str(self.context_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/contexts/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Contexts.Context, ['context_name'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.Contexts.Context']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.Contexts']['meta_info']


    class ContextMappings(_Entity_):
        """
        List of context names
        
        .. attribute:: context_mapping
        
        	Context mapping name
        	**type**\: list of  		 :py:class:`ContextMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.ContextMappings.ContextMapping>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2018-06-27'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Snmp.ContextMappings, self).__init__()

            self.yang_name = "context-mappings"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("context-mapping", ("context_mapping", Snmp.ContextMappings.ContextMapping))])
            self._leafs = OrderedDict()

            self.context_mapping = YList(self)
            self._segment_path = lambda: "context-mappings"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.ContextMappings, [], name, value)


        class ContextMapping(_Entity_):
            """
            Context mapping name
            
            .. attribute:: context_mapping_name  (key)
            
            	Context mapping name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: context
            
            	SNMP context feature type
            	**type**\:  :py:class:`SnmpContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpContext>`
            
            .. attribute:: instance_name
            
            	OSPF protocol instance
            	**type**\: str
            
            .. attribute:: vrf_name
            
            	VRF name associated with the context
            	**type**\: str
            
            .. attribute:: topology_name
            
            	Topology name associated with the context
            	**type**\: str
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2018-06-27'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Snmp.ContextMappings.ContextMapping, self).__init__()

                self.yang_name = "context-mapping"
                self.yang_parent_name = "context-mappings"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['context_mapping_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('context_mapping_name', (YLeaf(YType.str, 'context-mapping-name'), ['str'])),
                    ('context', (YLeaf(YType.enumeration, 'context'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpContext', '')])),
                    ('instance_name', (YLeaf(YType.str, 'instance-name'), ['str'])),
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('topology_name', (YLeaf(YType.str, 'topology-name'), ['str'])),
                ])
                self.context_mapping_name = None
                self.context = None
                self.instance_name = None
                self.vrf_name = None
                self.topology_name = None
                self._segment_path = lambda: "context-mapping" + "[context-mapping-name='" + str(self.context_mapping_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/context-mappings/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.ContextMappings.ContextMapping, ['context_mapping_name', 'context', 'instance_name', 'vrf_name', 'topology_name'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Snmp.ContextMappings.ContextMapping']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Snmp.ContextMappings']['meta_info']

    def clone_ptr(self):
        self._top_entity = Snmp()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['Snmp']['meta_info']


class Mib(_Entity_):
    """
    mib
    
    .. attribute:: notification_log_mib
    
    	Notification log MIB configuration
    	**type**\:  :py:class:`NotificationLogMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.NotificationLogMib>`
    
    .. attribute:: entity_mib
    
    	Entity MIB
    	**type**\:  :py:class:`EntityMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.EntityMib>`
    
    .. attribute:: interface_mib
    
    	Interface MIB configuration
    	**type**\:  :py:class:`InterfaceMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.InterfaceMib>`
    
    .. attribute:: sensor_mib_cache
    
    	Get cached Sesnsor MIB statistics
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: subscriber
    
    	Subscriber threshold commands
    	**type**\:  :py:class:`Subscriber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber>`
    
    .. attribute:: cb_qosmib
    
    	CBQoSMIB configuration
    	**type**\:  :py:class:`CbQosmib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.CbQosmib>`
    
    .. attribute:: mpls_te_mib
    
    	MPLS TE MIB configuration
    	**type**\:  :py:class:`MplsTeMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.MplsTeMib>`
    
    .. attribute:: mpls_p2mp_mib
    
    	MPLS P2MP MIB configuration
    	**type**\:  :py:class:`MplsP2mpMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.MplsP2mpMib>`
    
    .. attribute:: mpls_te_ext_std_mib
    
    	MPLS TE EXT STD MIB configuration
    	**type**\:  :py:class:`MplsTeExtStdMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.MplsTeExtStdMib>`
    
    .. attribute:: mpls_te_ext_mib
    
    	MPLS TE EXT MIB configuration
    	**type**\:  :py:class:`MplsTeExtMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.MplsTeExtMib>`
    
    .. attribute:: mpls_frr_mib
    
    	FRR MIB configuration
    	**type**\:  :py:class:`MplsFrrMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.MplsFrrMib>`
    
    

    """

    _prefix = 'snmp-agent-cfg'
    _revision = '2018-06-27'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Mib, self).__init__()
        self._top_entity = None

        self.yang_name = "mib"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-agent-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("Cisco-IOS-XR-infra-notification-log-mib-cfg:notification-log-mib", ("notification_log_mib", Mib.NotificationLogMib)), ("Cisco-IOS-XR-snmp-entitymib-cfg:entity-mib", ("entity_mib", Mib.EntityMib)), ("Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib", ("interface_mib", Mib.InterfaceMib)), ("Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber", ("subscriber", Mib.Subscriber)), ("Cisco-IOS-XR-qos-mibs-cfg:cb-qosmib", ("cb_qosmib", Mib.CbQosmib)), ("Cisco-IOS-XR-mpls-te-cfg:mpls-te-mib", ("mpls_te_mib", Mib.MplsTeMib)), ("Cisco-IOS-XR-mpls-te-cfg:mpls-p2mp-mib", ("mpls_p2mp_mib", Mib.MplsP2mpMib)), ("Cisco-IOS-XR-mpls-te-cfg:mpls-te-ext-std-mib", ("mpls_te_ext_std_mib", Mib.MplsTeExtStdMib)), ("Cisco-IOS-XR-mpls-te-cfg:mpls-te-ext-mib", ("mpls_te_ext_mib", Mib.MplsTeExtMib)), ("Cisco-IOS-XR-mpls-te-cfg:mpls-frr-mib", ("mpls_frr_mib", Mib.MplsFrrMib))])
        self._leafs = OrderedDict([
            ('sensor_mib_cache', (YLeaf(YType.empty, 'Cisco-IOS-XR-snmp-ciscosensormib-cfg:sensor-mib-cache'), ['Empty'])),
        ])
        self.sensor_mib_cache = None

        self.notification_log_mib = Mib.NotificationLogMib()
        self.notification_log_mib.parent = self
        self._children_name_map["notification_log_mib"] = "Cisco-IOS-XR-infra-notification-log-mib-cfg:notification-log-mib"

        self.entity_mib = Mib.EntityMib()
        self.entity_mib.parent = self
        self._children_name_map["entity_mib"] = "Cisco-IOS-XR-snmp-entitymib-cfg:entity-mib"

        self.interface_mib = Mib.InterfaceMib()
        self.interface_mib.parent = self
        self._children_name_map["interface_mib"] = "Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib"

        self.subscriber = Mib.Subscriber()
        self.subscriber.parent = self
        self._children_name_map["subscriber"] = "Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber"

        self.cb_qosmib = Mib.CbQosmib()
        self.cb_qosmib.parent = self
        self._children_name_map["cb_qosmib"] = "Cisco-IOS-XR-qos-mibs-cfg:cb-qosmib"

        self.mpls_te_mib = Mib.MplsTeMib()
        self.mpls_te_mib.parent = self
        self._children_name_map["mpls_te_mib"] = "Cisco-IOS-XR-mpls-te-cfg:mpls-te-mib"

        self.mpls_p2mp_mib = Mib.MplsP2mpMib()
        self.mpls_p2mp_mib.parent = self
        self._children_name_map["mpls_p2mp_mib"] = "Cisco-IOS-XR-mpls-te-cfg:mpls-p2mp-mib"

        self.mpls_te_ext_std_mib = Mib.MplsTeExtStdMib()
        self.mpls_te_ext_std_mib.parent = self
        self._children_name_map["mpls_te_ext_std_mib"] = "Cisco-IOS-XR-mpls-te-cfg:mpls-te-ext-std-mib"

        self.mpls_te_ext_mib = Mib.MplsTeExtMib()
        self.mpls_te_ext_mib.parent = self
        self._children_name_map["mpls_te_ext_mib"] = "Cisco-IOS-XR-mpls-te-cfg:mpls-te-ext-mib"

        self.mpls_frr_mib = Mib.MplsFrrMib()
        self.mpls_frr_mib.parent = self
        self._children_name_map["mpls_frr_mib"] = "Cisco-IOS-XR-mpls-te-cfg:mpls-frr-mib"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Mib, ['sensor_mib_cache'], name, value)


    class NotificationLogMib(_Entity_):
        """
        Notification log MIB configuration
        
        .. attribute:: global_age_out
        
        	GlobalAgeOut is the minutes associated with the mib
        	**type**\: int
        
        	**range:** 1..4294967295
        
        	**units**\: minute
        
        .. attribute:: disable
        
        	Disable, to disable the logging in default log
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: default
        
        	To create a default log
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: global_size
        
        	GlobalSize, max number of notifications that can be logged in all logs
        	**type**\: int
        
        	**range:** 1..15000
        
        .. attribute:: default_size
        
        	The max number of notifications that this log (default) can hold
        	**type**\: int
        
        	**range:** 1..15000
        
        

        """

        _prefix = 'infra-notification-log-mib-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Mib.NotificationLogMib, self).__init__()

            self.yang_name = "notification-log-mib"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('global_age_out', (YLeaf(YType.uint32, 'global-age-out'), ['int'])),
                ('disable', (YLeaf(YType.empty, 'disable'), ['Empty'])),
                ('default', (YLeaf(YType.empty, 'default'), ['Empty'])),
                ('global_size', (YLeaf(YType.uint32, 'global-size'), ['int'])),
                ('default_size', (YLeaf(YType.uint32, 'default-size'), ['int'])),
            ])
            self.global_age_out = None
            self.disable = None
            self.default = None
            self.global_size = None
            self.default_size = None
            self._segment_path = lambda: "Cisco-IOS-XR-infra-notification-log-mib-cfg:notification-log-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.NotificationLogMib, ['global_age_out', 'disable', 'default', 'global_size', 'default_size'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.NotificationLogMib']['meta_info']


    class EntityMib(_Entity_):
        """
        Entity MIB
        
        .. attribute:: entity_index_persistence
        
        	Enable entPhysicalIndex persistence
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'snmp-entitymib-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Mib.EntityMib, self).__init__()

            self.yang_name = "entity-mib"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('entity_index_persistence', (YLeaf(YType.empty, 'entity-index-persistence'), ['Empty'])),
            ])
            self.entity_index_persistence = None
            self._segment_path = lambda: "Cisco-IOS-XR-snmp-entitymib-cfg:entity-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.EntityMib, ['entity_index_persistence'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.EntityMib']['meta_info']


    class InterfaceMib(_Entity_):
        """
        Interface MIB configuration
        
        .. attribute:: interfaces
        
        	Enter the SNMP interface configuration commands
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.InterfaceMib.Interfaces>`
        
        .. attribute:: notification
        
        	MIB notification configuration
        	**type**\:  :py:class:`Notification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.InterfaceMib.Notification>`
        
        .. attribute:: subsets
        
        	Add configuration for an interface subset
        	**type**\:  :py:class:`Subsets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.InterfaceMib.Subsets>`
        
        .. attribute:: internal_cache
        
        	Get cached interface statistics
        	**type**\: int
        
        	**range:** 0..60
        
        	**default value**\: 15
        
        .. attribute:: interface_alias_long
        
        	Enable support for ifAlias values longer than 64 characters
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: ip_subscriber
        
        	Enable IP subscriber interfaces in IFMIB
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: interface_index_persistence
        
        	Enable ifindex persistence
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: statistics_cache
        
        	Enable cached interface statistics
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'snmp-ifmib-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Mib.InterfaceMib, self).__init__()

            self.yang_name = "interface-mib"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interfaces", ("interfaces", Mib.InterfaceMib.Interfaces)), ("notification", ("notification", Mib.InterfaceMib.Notification)), ("subsets", ("subsets", Mib.InterfaceMib.Subsets))])
            self._leafs = OrderedDict([
                ('internal_cache', (YLeaf(YType.uint32, 'internal-cache'), ['int'])),
                ('interface_alias_long', (YLeaf(YType.empty, 'interface-alias-long'), ['Empty'])),
                ('ip_subscriber', (YLeaf(YType.empty, 'ip-subscriber'), ['Empty'])),
                ('interface_index_persistence', (YLeaf(YType.empty, 'interface-index-persistence'), ['Empty'])),
                ('statistics_cache', (YLeaf(YType.empty, 'statistics-cache'), ['Empty'])),
            ])
            self.internal_cache = None
            self.interface_alias_long = None
            self.ip_subscriber = None
            self.interface_index_persistence = None
            self.statistics_cache = None

            self.interfaces = Mib.InterfaceMib.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"

            self.notification = Mib.InterfaceMib.Notification()
            self.notification.parent = self
            self._children_name_map["notification"] = "notification"

            self.subsets = Mib.InterfaceMib.Subsets()
            self.subsets.parent = self
            self._children_name_map["subsets"] = "subsets"
            self._segment_path = lambda: "Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.InterfaceMib, ['internal_cache', 'interface_alias_long', 'ip_subscriber', 'interface_index_persistence', 'statistics_cache'], name, value)


        class Interfaces(_Entity_):
            """
            Enter the SNMP interface configuration commands
            
            .. attribute:: interface
            
            	Interface to configure
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.InterfaceMib.Interfaces.Interface>`
            
            

            """

            _prefix = 'snmp-ifmib-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mib.InterfaceMib.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "interface-mib"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface", ("interface", Mib.InterfaceMib.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mib.InterfaceMib.Interfaces, [], name, value)


            class Interface(_Entity_):
                """
                Interface to configure
                
                .. attribute:: interface_name  (key)
                
                	The name of the interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: link_up_down
                
                	Enable or disable LinkUpDown notification
                	**type**\: bool
                
                .. attribute:: index_persistence
                
                	Enable or disable index persistence
                	**type**\: bool
                
                

                """

                _prefix = 'snmp-ifmib-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mib.InterfaceMib.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('link_up_down', (YLeaf(YType.boolean, 'link-up-down'), ['bool'])),
                        ('index_persistence', (YLeaf(YType.boolean, 'index-persistence'), ['bool'])),
                    ])
                    self.interface_name = None
                    self.link_up_down = None
                    self.index_persistence = None
                    self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib/interfaces/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mib.InterfaceMib.Interfaces.Interface, ['interface_name', 'link_up_down', 'index_persistence'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Mib.InterfaceMib.Interfaces.Interface']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Mib.InterfaceMib.Interfaces']['meta_info']


        class Notification(_Entity_):
            """
            MIB notification configuration
            
            .. attribute:: link_ietf
            
            	Set the varbind of linkupdown trap to the RFC specified varbinds (default cisco)
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-ifmib-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mib.InterfaceMib.Notification, self).__init__()

                self.yang_name = "notification"
                self.yang_parent_name = "interface-mib"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('link_ietf', (YLeaf(YType.empty, 'link-ietf'), ['Empty'])),
                ])
                self.link_ietf = None
                self._segment_path = lambda: "notification"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mib.InterfaceMib.Notification, ['link_ietf'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Mib.InterfaceMib.Notification']['meta_info']


        class Subsets(_Entity_):
            """
            Add configuration for an interface subset
            
            .. attribute:: subset
            
            	Subset priorityID to group ifNames based on Regular Expression
            	**type**\: list of  		 :py:class:`Subset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.InterfaceMib.Subsets.Subset>`
            
            

            """

            _prefix = 'snmp-ifmib-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mib.InterfaceMib.Subsets, self).__init__()

                self.yang_name = "subsets"
                self.yang_parent_name = "interface-mib"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("subset", ("subset", Mib.InterfaceMib.Subsets.Subset))])
                self._leafs = OrderedDict()

                self.subset = YList(self)
                self._segment_path = lambda: "subsets"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mib.InterfaceMib.Subsets, [], name, value)


            class Subset(_Entity_):
                """
                Subset priorityID to group ifNames based on
                Regular Expression
                
                .. attribute:: subset_id  (key)
                
                	The interface subset PriorityID
                	**type**\: int
                
                	**range:** 1..255
                
                .. attribute:: link_up_down
                
                	SNMP linkUp and linkDown notifications
                	**type**\:  :py:class:`LinkUpDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.InterfaceMib.Subsets.Subset.LinkUpDown>`
                
                

                """

                _prefix = 'snmp-ifmib-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mib.InterfaceMib.Subsets.Subset, self).__init__()

                    self.yang_name = "subset"
                    self.yang_parent_name = "subsets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['subset_id']
                    self._child_classes = OrderedDict([("link-up-down", ("link_up_down", Mib.InterfaceMib.Subsets.Subset.LinkUpDown))])
                    self._leafs = OrderedDict([
                        ('subset_id', (YLeaf(YType.uint32, 'subset-id'), ['int'])),
                    ])
                    self.subset_id = None

                    self.link_up_down = Mib.InterfaceMib.Subsets.Subset.LinkUpDown()
                    self.link_up_down.parent = self
                    self._children_name_map["link_up_down"] = "link-up-down"
                    self._segment_path = lambda: "subset" + "[subset-id='" + str(self.subset_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib/subsets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mib.InterfaceMib.Subsets.Subset, ['subset_id'], name, value)


                class LinkUpDown(_Entity_):
                    """
                    SNMP linkUp and linkDown notifications
                    
                    .. attribute:: enable
                    
                    	Enable or disable linkupdown notification
                    	**type**\: bool
                    
                    .. attribute:: regular_expression
                    
                    	Regular expression to match ifName
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'snmp-ifmib-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mib.InterfaceMib.Subsets.Subset.LinkUpDown, self).__init__()

                        self.yang_name = "link-up-down"
                        self.yang_parent_name = "subset"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                            ('regular_expression', (YLeaf(YType.str, 'regular-expression'), ['str'])),
                        ])
                        self.enable = None
                        self.regular_expression = None
                        self._segment_path = lambda: "link-up-down"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mib.InterfaceMib.Subsets.Subset.LinkUpDown, ['enable', 'regular_expression'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Mib.InterfaceMib.Subsets.Subset.LinkUpDown']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Mib.InterfaceMib.Subsets.Subset']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Mib.InterfaceMib.Subsets']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.InterfaceMib']['meta_info']


    class Subscriber(_Entity_):
        """
        Subscriber threshold commands
        
        .. attribute:: threshold
        
        	Subscriber threshold commands
        	**type**\:  :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold>`
        
        

        """

        _prefix = 'subscriber-session-mon-mibs-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Mib.Subscriber, self).__init__()

            self.yang_name = "subscriber"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("threshold", ("threshold", Mib.Subscriber.Threshold))])
            self._leafs = OrderedDict()

            self.threshold = Mib.Subscriber.Threshold()
            self.threshold.parent = self
            self._children_name_map["threshold"] = "threshold"
            self._segment_path = lambda: "Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.Subscriber, [], name, value)


        class Threshold(_Entity_):
            """
            Subscriber threshold commands
            
            .. attribute:: delta
            
            	Delta loss keyword
            	**type**\:  :py:class:`Delta <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta>`
            
            .. attribute:: access_interface_sub
            
            	Access interface for regular expression
            	**type**\:  :py:class:`AccessInterfaceSub <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.AccessInterfaceSub>`
            
            .. attribute:: falling
            
            	Falling threshold
            	**type**\:  :py:class:`Falling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Falling>`
            
            .. attribute:: rising
            
            	Rising threshold
            	**type**\:  :py:class:`Rising <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Rising>`
            
            

            """

            _prefix = 'subscriber-session-mon-mibs-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mib.Subscriber.Threshold, self).__init__()

                self.yang_name = "threshold"
                self.yang_parent_name = "subscriber"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("delta", ("delta", Mib.Subscriber.Threshold.Delta)), ("access-interface-sub", ("access_interface_sub", Mib.Subscriber.Threshold.AccessInterfaceSub)), ("falling", ("falling", Mib.Subscriber.Threshold.Falling)), ("rising", ("rising", Mib.Subscriber.Threshold.Rising))])
                self._leafs = OrderedDict()

                self.delta = Mib.Subscriber.Threshold.Delta()
                self.delta.parent = self
                self._children_name_map["delta"] = "delta"

                self.access_interface_sub = Mib.Subscriber.Threshold.AccessInterfaceSub()
                self.access_interface_sub.parent = self
                self._children_name_map["access_interface_sub"] = "access-interface-sub"

                self.falling = Mib.Subscriber.Threshold.Falling()
                self.falling.parent = self
                self._children_name_map["falling"] = "falling"

                self.rising = Mib.Subscriber.Threshold.Rising()
                self.rising.parent = self
                self._children_name_map["rising"] = "rising"
                self._segment_path = lambda: "threshold"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mib.Subscriber.Threshold, [], name, value)


            class Delta(_Entity_):
                """
                Delta loss keyword
                
                .. attribute:: evaluation
                
                	Evaluation keyword
                	**type**\:  :py:class:`Evaluation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Evaluation>`
                
                .. attribute:: percent
                
                	Delta loss percent
                	**type**\:  :py:class:`Percent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Percent>`
                
                

                """

                _prefix = 'subscriber-session-mon-mibs-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mib.Subscriber.Threshold.Delta, self).__init__()

                    self.yang_name = "delta"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("evaluation", ("evaluation", Mib.Subscriber.Threshold.Delta.Evaluation)), ("percent", ("percent", Mib.Subscriber.Threshold.Delta.Percent))])
                    self._leafs = OrderedDict()

                    self.evaluation = Mib.Subscriber.Threshold.Delta.Evaluation()
                    self.evaluation.parent = self
                    self._children_name_map["evaluation"] = "evaluation"

                    self.percent = Mib.Subscriber.Threshold.Delta.Percent()
                    self.percent.parent = self
                    self._children_name_map["percent"] = "percent"
                    self._segment_path = lambda: "delta"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mib.Subscriber.Threshold.Delta, [], name, value)


                class Evaluation(_Entity_):
                    """
                    Evaluation keyword
                    
                    .. attribute:: access_interfaces
                    
                    	Table of AccessInterface
                    	**type**\:  :py:class:`AccessInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces>`
                    
                    .. attribute:: nodes
                    
                    	Table of Node
                    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Evaluation.Nodes>`
                    
                    

                    """

                    _prefix = 'subscriber-session-mon-mibs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mib.Subscriber.Threshold.Delta.Evaluation, self).__init__()

                        self.yang_name = "evaluation"
                        self.yang_parent_name = "delta"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("access-interfaces", ("access_interfaces", Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces)), ("nodes", ("nodes", Mib.Subscriber.Threshold.Delta.Evaluation.Nodes))])
                        self._leafs = OrderedDict()

                        self.access_interfaces = Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces()
                        self.access_interfaces.parent = self
                        self._children_name_map["access_interfaces"] = "access-interfaces"

                        self.nodes = Mib.Subscriber.Threshold.Delta.Evaluation.Nodes()
                        self.nodes.parent = self
                        self._children_name_map["nodes"] = "nodes"
                        self._segment_path = lambda: "evaluation"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mib.Subscriber.Threshold.Delta.Evaluation, [], name, value)


                    class AccessInterfaces(_Entity_):
                        """
                        Table of AccessInterface
                        
                        .. attribute:: access_interface
                        
                        	Access interface
                        	**type**\: list of  		 :py:class:`AccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces.AccessInterface>`
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces, self).__init__()

                            self.yang_name = "access-interfaces"
                            self.yang_parent_name = "evaluation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("access-interface", ("access_interface", Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces.AccessInterface))])
                            self._leafs = OrderedDict()

                            self.access_interface = YList(self)
                            self._segment_path = lambda: "access-interfaces"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/evaluation/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces, [], name, value)


                        class AccessInterface(_Entity_):
                            """
                            Access interface
                            
                            .. attribute:: interface_name  (key)
                            
                            	Interface name
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: session_count
                            
                            	Session count
                            	**type**\: int
                            
                            	**range:** 1..4294967294
                            
                            .. attribute:: interval
                            
                            	Interval value in multiples of 10
                            	**type**\: int
                            
                            	**range:** 30..3600
                            
                            

                            """

                            _prefix = 'subscriber-session-mon-mibs-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces.AccessInterface, self).__init__()

                                self.yang_name = "access-interface"
                                self.yang_parent_name = "access-interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = ['interface_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('session_count', (YLeaf(YType.uint32, 'session-count'), ['int'])),
                                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                ])
                                self.interface_name = None
                                self.session_count = None
                                self.interval = None
                                self._segment_path = lambda: "access-interface" + "[interface-name='" + str(self.interface_name) + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/evaluation/access-interfaces/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces.AccessInterface, ['interface_name', 'session_count', 'interval'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces.AccessInterface']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces']['meta_info']


                    class Nodes(_Entity_):
                        """
                        Table of Node
                        
                        .. attribute:: node
                        
                        	Rising node level
                        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Evaluation.Nodes.Node>`
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mib.Subscriber.Threshold.Delta.Evaluation.Nodes, self).__init__()

                            self.yang_name = "nodes"
                            self.yang_parent_name = "evaluation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("node", ("node", Mib.Subscriber.Threshold.Delta.Evaluation.Nodes.Node))])
                            self._leafs = OrderedDict()

                            self.node = YList(self)
                            self._segment_path = lambda: "nodes"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/evaluation/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.Delta.Evaluation.Nodes, [], name, value)


                        class Node(_Entity_):
                            """
                            Rising node level
                            
                            .. attribute:: node_name  (key)
                            
                            	location
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: session_count
                            
                            	Session count
                            	**type**\: int
                            
                            	**range:** 1..4294967294
                            
                            .. attribute:: interval
                            
                            	interval value in multiples of 10
                            	**type**\: int
                            
                            	**range:** 30..3600
                            
                            

                            """

                            _prefix = 'subscriber-session-mon-mibs-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mib.Subscriber.Threshold.Delta.Evaluation.Nodes.Node, self).__init__()

                                self.yang_name = "node"
                                self.yang_parent_name = "nodes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = ['node_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                                    ('session_count', (YLeaf(YType.uint32, 'session-count'), ['int'])),
                                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                ])
                                self.node_name = None
                                self.session_count = None
                                self.interval = None
                                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/evaluation/nodes/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mib.Subscriber.Threshold.Delta.Evaluation.Nodes.Node, ['node_name', 'session_count', 'interval'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Mib.Subscriber.Threshold.Delta.Evaluation.Nodes.Node']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Mib.Subscriber.Threshold.Delta.Evaluation.Nodes']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Mib.Subscriber.Threshold.Delta.Evaluation']['meta_info']


                class Percent(_Entity_):
                    """
                    Delta loss percent
                    
                    .. attribute:: access_interfaces
                    
                    	Table of AccessInterface
                    	**type**\:  :py:class:`AccessInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces>`
                    
                    .. attribute:: nodes
                    
                    	Table of Node
                    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Percent.Nodes>`
                    
                    

                    """

                    _prefix = 'subscriber-session-mon-mibs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mib.Subscriber.Threshold.Delta.Percent, self).__init__()

                        self.yang_name = "percent"
                        self.yang_parent_name = "delta"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("access-interfaces", ("access_interfaces", Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces)), ("nodes", ("nodes", Mib.Subscriber.Threshold.Delta.Percent.Nodes))])
                        self._leafs = OrderedDict()

                        self.access_interfaces = Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces()
                        self.access_interfaces.parent = self
                        self._children_name_map["access_interfaces"] = "access-interfaces"

                        self.nodes = Mib.Subscriber.Threshold.Delta.Percent.Nodes()
                        self.nodes.parent = self
                        self._children_name_map["nodes"] = "nodes"
                        self._segment_path = lambda: "percent"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mib.Subscriber.Threshold.Delta.Percent, [], name, value)


                    class AccessInterfaces(_Entity_):
                        """
                        Table of AccessInterface
                        
                        .. attribute:: access_interface
                        
                        	Access interface
                        	**type**\: list of  		 :py:class:`AccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces.AccessInterface>`
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces, self).__init__()

                            self.yang_name = "access-interfaces"
                            self.yang_parent_name = "percent"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("access-interface", ("access_interface", Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces.AccessInterface))])
                            self._leafs = OrderedDict()

                            self.access_interface = YList(self)
                            self._segment_path = lambda: "access-interfaces"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/percent/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces, [], name, value)


                        class AccessInterface(_Entity_):
                            """
                            Access interface
                            
                            .. attribute:: interface_name  (key)
                            
                            	Interface name
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: session_count
                            
                            	Session count
                            	**type**\: int
                            
                            	**range:** 1..4294967294
                            
                            .. attribute:: interval
                            
                            	Interval value in multiples of 10
                            	**type**\: int
                            
                            	**range:** 30..3600
                            
                            

                            """

                            _prefix = 'subscriber-session-mon-mibs-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces.AccessInterface, self).__init__()

                                self.yang_name = "access-interface"
                                self.yang_parent_name = "access-interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = ['interface_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('session_count', (YLeaf(YType.uint32, 'session-count'), ['int'])),
                                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                ])
                                self.interface_name = None
                                self.session_count = None
                                self.interval = None
                                self._segment_path = lambda: "access-interface" + "[interface-name='" + str(self.interface_name) + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/percent/access-interfaces/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces.AccessInterface, ['interface_name', 'session_count', 'interval'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces.AccessInterface']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces']['meta_info']


                    class Nodes(_Entity_):
                        """
                        Table of Node
                        
                        .. attribute:: node
                        
                        	Rising node level
                        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Percent.Nodes.Node>`
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mib.Subscriber.Threshold.Delta.Percent.Nodes, self).__init__()

                            self.yang_name = "nodes"
                            self.yang_parent_name = "percent"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("node", ("node", Mib.Subscriber.Threshold.Delta.Percent.Nodes.Node))])
                            self._leafs = OrderedDict()

                            self.node = YList(self)
                            self._segment_path = lambda: "nodes"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/percent/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.Delta.Percent.Nodes, [], name, value)


                        class Node(_Entity_):
                            """
                            Rising node level
                            
                            .. attribute:: node_name  (key)
                            
                            	location
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: session_count
                            
                            	Session count
                            	**type**\: int
                            
                            	**range:** 1..4294967294
                            
                            .. attribute:: interval
                            
                            	interval value in multiples of 10
                            	**type**\: int
                            
                            	**range:** 30..3600
                            
                            

                            """

                            _prefix = 'subscriber-session-mon-mibs-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mib.Subscriber.Threshold.Delta.Percent.Nodes.Node, self).__init__()

                                self.yang_name = "node"
                                self.yang_parent_name = "nodes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = ['node_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                                    ('session_count', (YLeaf(YType.uint32, 'session-count'), ['int'])),
                                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                ])
                                self.node_name = None
                                self.session_count = None
                                self.interval = None
                                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/percent/nodes/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mib.Subscriber.Threshold.Delta.Percent.Nodes.Node, ['node_name', 'session_count', 'interval'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Mib.Subscriber.Threshold.Delta.Percent.Nodes.Node']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Mib.Subscriber.Threshold.Delta.Percent.Nodes']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Mib.Subscriber.Threshold.Delta.Percent']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Mib.Subscriber.Threshold.Delta']['meta_info']


            class AccessInterfaceSub(_Entity_):
                """
                Access interface for regular expression
                
                .. attribute:: subsets
                
                	Table of Subset
                	**type**\:  :py:class:`Subsets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets>`
                
                

                """

                _prefix = 'subscriber-session-mon-mibs-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mib.Subscriber.Threshold.AccessInterfaceSub, self).__init__()

                    self.yang_name = "access-interface-sub"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("subsets", ("subsets", Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets))])
                    self._leafs = OrderedDict()

                    self.subsets = Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets()
                    self.subsets.parent = self
                    self._children_name_map["subsets"] = "subsets"
                    self._segment_path = lambda: "access-interface-sub"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mib.Subscriber.Threshold.AccessInterfaceSub, [], name, value)


                class Subsets(_Entity_):
                    """
                    Table of Subset
                    
                    .. attribute:: subset
                    
                    	Subset command
                    	**type**\: list of  		 :py:class:`Subset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset>`
                    
                    

                    """

                    _prefix = 'subscriber-session-mon-mibs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets, self).__init__()

                        self.yang_name = "subsets"
                        self.yang_parent_name = "access-interface-sub"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("subset", ("subset", Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset))])
                        self._leafs = OrderedDict()

                        self.subset = YList(self)
                        self._segment_path = lambda: "subsets"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/access-interface-sub/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets, [], name, value)


                    class Subset(_Entity_):
                        """
                        Subset command
                        
                        .. attribute:: subset_id  (key)
                        
                        	Subset number
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        .. attribute:: regular_expression
                        
                        	Regular expression
                        	**type**\:  :py:class:`RegularExpression <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression>`
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset, self).__init__()

                            self.yang_name = "subset"
                            self.yang_parent_name = "subsets"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['subset_id']
                            self._child_classes = OrderedDict([("regular-expression", ("regular_expression", Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression))])
                            self._leafs = OrderedDict([
                                ('subset_id', (YLeaf(YType.uint32, 'subset-id'), ['int'])),
                            ])
                            self.subset_id = None

                            self.regular_expression = Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression()
                            self.regular_expression.parent = self
                            self._children_name_map["regular_expression"] = "regular-expression"
                            self._segment_path = lambda: "subset" + "[subset-id='" + str(self.subset_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/access-interface-sub/subsets/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset, ['subset_id'], name, value)


                        class RegularExpression(_Entity_):
                            """
                            Regular expression
                            
                            .. attribute:: notification
                            
                            	Notification keyword
                            	**type**\:  :py:class:`Notification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification>`
                            
                            

                            """

                            _prefix = 'subscriber-session-mon-mibs-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression, self).__init__()

                                self.yang_name = "regular-expression"
                                self.yang_parent_name = "subset"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("notification", ("notification", Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification))])
                                self._leafs = OrderedDict()

                                self.notification = Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification()
                                self.notification.parent = self
                                self._children_name_map["notification"] = "notification"
                                self._segment_path = lambda: "regular-expression"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression, [], name, value)


                            class Notification(_Entity_):
                                """
                                Notification keyword
                                
                                .. attribute:: rising_falling
                                
                                	Rising\-falling threshold
                                	**type**\:  :py:class:`RisingFalling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification.RisingFalling>`
                                
                                

                                """

                                _prefix = 'subscriber-session-mon-mibs-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification, self).__init__()

                                    self.yang_name = "notification"
                                    self.yang_parent_name = "regular-expression"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("rising-falling", ("rising_falling", Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification.RisingFalling))])
                                    self._leafs = OrderedDict()

                                    self.rising_falling = Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification.RisingFalling()
                                    self.rising_falling.parent = self
                                    self._children_name_map["rising_falling"] = "rising-falling"
                                    self._segment_path = lambda: "notification"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification, [], name, value)


                                class RisingFalling(_Entity_):
                                    """
                                    Rising\-falling threshold
                                    
                                    .. attribute:: disable
                                    
                                    	Disable the notifications on access interfaces
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'subscriber-session-mon-mibs-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification.RisingFalling, self).__init__()

                                        self.yang_name = "rising-falling"
                                        self.yang_parent_name = "notification"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('disable', (YLeaf(YType.str, 'disable'), ['str'])),
                                        ])
                                        self.disable = None
                                        self._segment_path = lambda: "rising-falling"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification.RisingFalling, ['disable'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                        return meta._meta_table['Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification.RisingFalling']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                    return meta._meta_table['Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                                return meta._meta_table['Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Mib.Subscriber.Threshold.AccessInterfaceSub']['meta_info']


            class Falling(_Entity_):
                """
                Falling threshold
                
                .. attribute:: access_interfaces
                
                	Table of AccessInterface
                	**type**\:  :py:class:`AccessInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Falling.AccessInterfaces>`
                
                .. attribute:: nodes
                
                	Table of Node
                	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Falling.Nodes>`
                
                

                """

                _prefix = 'subscriber-session-mon-mibs-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mib.Subscriber.Threshold.Falling, self).__init__()

                    self.yang_name = "falling"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("access-interfaces", ("access_interfaces", Mib.Subscriber.Threshold.Falling.AccessInterfaces)), ("nodes", ("nodes", Mib.Subscriber.Threshold.Falling.Nodes))])
                    self._leafs = OrderedDict()

                    self.access_interfaces = Mib.Subscriber.Threshold.Falling.AccessInterfaces()
                    self.access_interfaces.parent = self
                    self._children_name_map["access_interfaces"] = "access-interfaces"

                    self.nodes = Mib.Subscriber.Threshold.Falling.Nodes()
                    self.nodes.parent = self
                    self._children_name_map["nodes"] = "nodes"
                    self._segment_path = lambda: "falling"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mib.Subscriber.Threshold.Falling, [], name, value)


                class AccessInterfaces(_Entity_):
                    """
                    Table of AccessInterface
                    
                    .. attribute:: access_interface
                    
                    	Access interface
                    	**type**\: list of  		 :py:class:`AccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Falling.AccessInterfaces.AccessInterface>`
                    
                    

                    """

                    _prefix = 'subscriber-session-mon-mibs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mib.Subscriber.Threshold.Falling.AccessInterfaces, self).__init__()

                        self.yang_name = "access-interfaces"
                        self.yang_parent_name = "falling"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("access-interface", ("access_interface", Mib.Subscriber.Threshold.Falling.AccessInterfaces.AccessInterface))])
                        self._leafs = OrderedDict()

                        self.access_interface = YList(self)
                        self._segment_path = lambda: "access-interfaces"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/falling/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mib.Subscriber.Threshold.Falling.AccessInterfaces, [], name, value)


                    class AccessInterface(_Entity_):
                        """
                        Access interface
                        
                        .. attribute:: interface_name  (key)
                        
                        	Interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: session_count
                        
                        	Session count
                        	**type**\: int
                        
                        	**range:** 1..4294967294
                        
                        .. attribute:: interval
                        
                        	Interval value in multiples of 10
                        	**type**\: int
                        
                        	**range:** 30..3600
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mib.Subscriber.Threshold.Falling.AccessInterfaces.AccessInterface, self).__init__()

                            self.yang_name = "access-interface"
                            self.yang_parent_name = "access-interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['interface_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('session_count', (YLeaf(YType.uint32, 'session-count'), ['int'])),
                                ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                            ])
                            self.interface_name = None
                            self.session_count = None
                            self.interval = None
                            self._segment_path = lambda: "access-interface" + "[interface-name='" + str(self.interface_name) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/falling/access-interfaces/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.Falling.AccessInterfaces.AccessInterface, ['interface_name', 'session_count', 'interval'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Mib.Subscriber.Threshold.Falling.AccessInterfaces.AccessInterface']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Mib.Subscriber.Threshold.Falling.AccessInterfaces']['meta_info']


                class Nodes(_Entity_):
                    """
                    Table of Node
                    
                    .. attribute:: node
                    
                    	Rising node level
                    	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Falling.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'subscriber-session-mon-mibs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mib.Subscriber.Threshold.Falling.Nodes, self).__init__()

                        self.yang_name = "nodes"
                        self.yang_parent_name = "falling"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node", ("node", Mib.Subscriber.Threshold.Falling.Nodes.Node))])
                        self._leafs = OrderedDict()

                        self.node = YList(self)
                        self._segment_path = lambda: "nodes"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/falling/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mib.Subscriber.Threshold.Falling.Nodes, [], name, value)


                    class Node(_Entity_):
                        """
                        Rising node level
                        
                        .. attribute:: node_name  (key)
                        
                        	location
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: session_count
                        
                        	Session count
                        	**type**\: int
                        
                        	**range:** 1..4294967294
                        
                        .. attribute:: interval
                        
                        	interval value in multiples of 10
                        	**type**\: int
                        
                        	**range:** 30..3600
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mib.Subscriber.Threshold.Falling.Nodes.Node, self).__init__()

                            self.yang_name = "node"
                            self.yang_parent_name = "nodes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['node_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                                ('session_count', (YLeaf(YType.uint32, 'session-count'), ['int'])),
                                ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                            ])
                            self.node_name = None
                            self.session_count = None
                            self.interval = None
                            self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/falling/nodes/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.Falling.Nodes.Node, ['node_name', 'session_count', 'interval'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Mib.Subscriber.Threshold.Falling.Nodes.Node']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Mib.Subscriber.Threshold.Falling.Nodes']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Mib.Subscriber.Threshold.Falling']['meta_info']


            class Rising(_Entity_):
                """
                Rising threshold
                
                .. attribute:: access_interfaces
                
                	Table of AccessInterface
                	**type**\:  :py:class:`AccessInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Rising.AccessInterfaces>`
                
                .. attribute:: nodes
                
                	Table of Node
                	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Rising.Nodes>`
                
                

                """

                _prefix = 'subscriber-session-mon-mibs-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mib.Subscriber.Threshold.Rising, self).__init__()

                    self.yang_name = "rising"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("access-interfaces", ("access_interfaces", Mib.Subscriber.Threshold.Rising.AccessInterfaces)), ("nodes", ("nodes", Mib.Subscriber.Threshold.Rising.Nodes))])
                    self._leafs = OrderedDict()

                    self.access_interfaces = Mib.Subscriber.Threshold.Rising.AccessInterfaces()
                    self.access_interfaces.parent = self
                    self._children_name_map["access_interfaces"] = "access-interfaces"

                    self.nodes = Mib.Subscriber.Threshold.Rising.Nodes()
                    self.nodes.parent = self
                    self._children_name_map["nodes"] = "nodes"
                    self._segment_path = lambda: "rising"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mib.Subscriber.Threshold.Rising, [], name, value)


                class AccessInterfaces(_Entity_):
                    """
                    Table of AccessInterface
                    
                    .. attribute:: access_interface
                    
                    	Access interface
                    	**type**\: list of  		 :py:class:`AccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Rising.AccessInterfaces.AccessInterface>`
                    
                    

                    """

                    _prefix = 'subscriber-session-mon-mibs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mib.Subscriber.Threshold.Rising.AccessInterfaces, self).__init__()

                        self.yang_name = "access-interfaces"
                        self.yang_parent_name = "rising"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("access-interface", ("access_interface", Mib.Subscriber.Threshold.Rising.AccessInterfaces.AccessInterface))])
                        self._leafs = OrderedDict()

                        self.access_interface = YList(self)
                        self._segment_path = lambda: "access-interfaces"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/rising/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mib.Subscriber.Threshold.Rising.AccessInterfaces, [], name, value)


                    class AccessInterface(_Entity_):
                        """
                        Access interface
                        
                        .. attribute:: interface_name  (key)
                        
                        	Interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: session_count
                        
                        	Session count
                        	**type**\: int
                        
                        	**range:** 1..4294967294
                        
                        .. attribute:: interval
                        
                        	Interval value in multiples of 10
                        	**type**\: int
                        
                        	**range:** 30..3600
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mib.Subscriber.Threshold.Rising.AccessInterfaces.AccessInterface, self).__init__()

                            self.yang_name = "access-interface"
                            self.yang_parent_name = "access-interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['interface_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('session_count', (YLeaf(YType.uint32, 'session-count'), ['int'])),
                                ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                            ])
                            self.interface_name = None
                            self.session_count = None
                            self.interval = None
                            self._segment_path = lambda: "access-interface" + "[interface-name='" + str(self.interface_name) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/rising/access-interfaces/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.Rising.AccessInterfaces.AccessInterface, ['interface_name', 'session_count', 'interval'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Mib.Subscriber.Threshold.Rising.AccessInterfaces.AccessInterface']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Mib.Subscriber.Threshold.Rising.AccessInterfaces']['meta_info']


                class Nodes(_Entity_):
                    """
                    Table of Node
                    
                    .. attribute:: node
                    
                    	Rising node level
                    	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Rising.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'subscriber-session-mon-mibs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mib.Subscriber.Threshold.Rising.Nodes, self).__init__()

                        self.yang_name = "nodes"
                        self.yang_parent_name = "rising"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node", ("node", Mib.Subscriber.Threshold.Rising.Nodes.Node))])
                        self._leafs = OrderedDict()

                        self.node = YList(self)
                        self._segment_path = lambda: "nodes"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/rising/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mib.Subscriber.Threshold.Rising.Nodes, [], name, value)


                    class Node(_Entity_):
                        """
                        Rising node level
                        
                        .. attribute:: node_name  (key)
                        
                        	location
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: session_count
                        
                        	Session count
                        	**type**\: int
                        
                        	**range:** 1..4294967294
                        
                        .. attribute:: interval
                        
                        	interval value in multiples of 10
                        	**type**\: int
                        
                        	**range:** 30..3600
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mib.Subscriber.Threshold.Rising.Nodes.Node, self).__init__()

                            self.yang_name = "node"
                            self.yang_parent_name = "nodes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['node_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                                ('session_count', (YLeaf(YType.uint32, 'session-count'), ['int'])),
                                ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                            ])
                            self.node_name = None
                            self.session_count = None
                            self.interval = None
                            self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/rising/nodes/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.Rising.Nodes.Node, ['node_name', 'session_count', 'interval'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                            return meta._meta_table['Mib.Subscriber.Threshold.Rising.Nodes.Node']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                        return meta._meta_table['Mib.Subscriber.Threshold.Rising.Nodes']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                    return meta._meta_table['Mib.Subscriber.Threshold.Rising']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Mib.Subscriber.Threshold']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.Subscriber']['meta_info']


    class CbQosmib(_Entity_):
        """
        CBQoSMIB configuration
        
        .. attribute:: cache
        
        	CBQoSMIB statistics data caching
        	**type**\:  :py:class:`Cache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.CbQosmib.Cache>`
        
        .. attribute:: member_interface_stats
        
        	Enable bundle member interface statistics retrieval
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: persist
        
        	Persist CBQoSMIB config, service\-policy and object indices
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'qos-mibs-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Mib.CbQosmib, self).__init__()

            self.yang_name = "cb-qosmib"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cache", ("cache", Mib.CbQosmib.Cache))])
            self._leafs = OrderedDict([
                ('member_interface_stats', (YLeaf(YType.empty, 'member-interface-stats'), ['Empty'])),
                ('persist', (YLeaf(YType.empty, 'persist'), ['Empty'])),
            ])
            self.member_interface_stats = None
            self.persist = None

            self.cache = Mib.CbQosmib.Cache()
            self.cache.parent = self
            self._children_name_map["cache"] = "cache"
            self._segment_path = lambda: "Cisco-IOS-XR-qos-mibs-cfg:cb-qosmib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.CbQosmib, ['member_interface_stats', 'persist'], name, value)


        class Cache(_Entity_):
            """
            CBQoSMIB statistics data caching
            
            .. attribute:: enable
            
            	Enable CBQoSMIB statistics data caching
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: refresh_time
            
            	Cache refresh time in seconds
            	**type**\: int
            
            	**range:** 5..60
            
            	**units**\: second
            
            .. attribute:: service_policy_count
            
            	Maximum number of service policies to cache the statistics for
            	**type**\: int
            
            	**range:** 1..5000
            
            

            """

            _prefix = 'qos-mibs-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mib.CbQosmib.Cache, self).__init__()

                self.yang_name = "cache"
                self.yang_parent_name = "cb-qosmib"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ('refresh_time', (YLeaf(YType.uint32, 'refresh-time'), ['int'])),
                    ('service_policy_count', (YLeaf(YType.uint32, 'service-policy-count'), ['int'])),
                ])
                self.enable = None
                self.refresh_time = None
                self.service_policy_count = None
                self._segment_path = lambda: "cache"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-qos-mibs-cfg:cb-qosmib/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mib.CbQosmib.Cache, ['enable', 'refresh_time', 'service_policy_count'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
                return meta._meta_table['Mib.CbQosmib.Cache']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.CbQosmib']['meta_info']


    class MplsTeMib(_Entity_):
        """
        MPLS TE MIB configuration
        
        .. attribute:: cache_garbage_collect_timer
        
        	Configure the cache garbage collector time for the mib
        	**type**\: int
        
        	**range:** 0..3600
        
        	**units**\: second
        
        	**default value**\: 1800
        
        .. attribute:: cache_timer
        
        	Configure the cache time for the mib
        	**type**\: int
        
        	**range:** 0..600
        
        	**units**\: second
        
        	**default value**\: 60
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2019-10-16'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Mib.MplsTeMib, self).__init__()

            self.yang_name = "mpls-te-mib"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cache_garbage_collect_timer', (YLeaf(YType.uint32, 'cache-garbage-collect-timer'), ['int'])),
                ('cache_timer', (YLeaf(YType.uint32, 'cache-timer'), ['int'])),
            ])
            self.cache_garbage_collect_timer = None
            self.cache_timer = None
            self._segment_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.MplsTeMib, ['cache_garbage_collect_timer', 'cache_timer'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.MplsTeMib']['meta_info']


    class MplsP2mpMib(_Entity_):
        """
        MPLS P2MP MIB configuration
        
        .. attribute:: cache_timer
        
        	Configure the cache time for the mib
        	**type**\: int
        
        	**range:** 0..600
        
        	**units**\: second
        
        	**default value**\: 60
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2019-10-16'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Mib.MplsP2mpMib, self).__init__()

            self.yang_name = "mpls-p2mp-mib"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cache_timer', (YLeaf(YType.uint32, 'cache-timer'), ['int'])),
            ])
            self.cache_timer = None
            self._segment_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-p2mp-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.MplsP2mpMib, ['cache_timer'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.MplsP2mpMib']['meta_info']


    class MplsTeExtStdMib(_Entity_):
        """
        MPLS TE EXT STD MIB configuration
        
        .. attribute:: cache_timer
        
        	Configure the cache time for the mib
        	**type**\: int
        
        	**range:** 0..600
        
        	**units**\: second
        
        	**default value**\: 60
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2019-10-16'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Mib.MplsTeExtStdMib, self).__init__()

            self.yang_name = "mpls-te-ext-std-mib"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cache_timer', (YLeaf(YType.uint32, 'cache-timer'), ['int'])),
            ])
            self.cache_timer = None
            self._segment_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te-ext-std-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.MplsTeExtStdMib, ['cache_timer'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.MplsTeExtStdMib']['meta_info']


    class MplsTeExtMib(_Entity_):
        """
        MPLS TE EXT MIB configuration
        
        .. attribute:: cache_timer
        
        	Configure the cache time for the mib
        	**type**\: int
        
        	**range:** 0..600
        
        	**units**\: second
        
        	**default value**\: 60
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2019-10-16'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Mib.MplsTeExtMib, self).__init__()

            self.yang_name = "mpls-te-ext-mib"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cache_timer', (YLeaf(YType.uint32, 'cache-timer'), ['int'])),
            ])
            self.cache_timer = None
            self._segment_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te-ext-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.MplsTeExtMib, ['cache_timer'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.MplsTeExtMib']['meta_info']


    class MplsFrrMib(_Entity_):
        """
        FRR MIB configuration
        
        .. attribute:: cache_timer
        
        	Configure the cache time for the mib
        	**type**\: int
        
        	**range:** 0..600
        
        	**units**\: second
        
        	**default value**\: 60
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2019-10-16'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Mib.MplsFrrMib, self).__init__()

            self.yang_name = "mpls-frr-mib"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cache_timer', (YLeaf(YType.uint32, 'cache-timer'), ['int'])),
            ])
            self.cache_timer = None
            self._segment_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-frr-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.MplsFrrMib, ['cache_timer'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
            return meta._meta_table['Mib.MplsFrrMib']['meta_info']

    def clone_ptr(self):
        self._top_entity = Mib()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_agent_cfg as meta
        return meta._meta_table['Mib']['meta_info']


