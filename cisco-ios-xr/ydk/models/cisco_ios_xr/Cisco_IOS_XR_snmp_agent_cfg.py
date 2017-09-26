""" Cisco_IOS_XR_snmp_agent_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR snmp\-agent package configuration.

This module contains definitions
for the following management objects\:
  snmp\: The heirarchy point for all the SNMP configurations
  mib\: mib

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class GroupSnmpVersion(Enum):
    """
    GroupSnmpVersion

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


class SnmpAccessLevel(Enum):
    """
    SnmpAccessLevel

    Snmp access level

    .. data:: read_only = 0

    	Read Only Access for a community string

    .. data:: read_write = 1

    	Read Write Access for a community string

    """

    read_only = Enum.YLeaf(0, "read-only")

    read_write = Enum.YLeaf(1, "read-write")


class SnmpBulkstatFileFormat(Enum):
    """
    SnmpBulkstatFileFormat

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


class SnmpBulkstatSchema(Enum):
    """
    SnmpBulkstatSchema

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


class SnmpContext(Enum):
    """
    SnmpContext

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


class SnmpDscpValue(Enum):
    """
    SnmpDscpValue

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


class SnmpHashAlgorithm(Enum):
    """
    SnmpHashAlgorithm

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


class SnmpMibViewInclusion(Enum):
    """
    SnmpMibViewInclusion

    Snmp mib view inclusion

    .. data:: included = 1

    	MIB View to be included

    .. data:: excluded = 2

    	MIB View to be excluded

    """

    included = Enum.YLeaf(1, "included")

    excluded = Enum.YLeaf(2, "excluded")


class SnmpOwnerAccess(Enum):
    """
    SnmpOwnerAccess

    Snmp owner access

    .. data:: sdr_owner = 0

    	Secure Domain Router Owner permissions

    .. data:: system_owner = 1

    	System owner permissions

    """

    sdr_owner = Enum.YLeaf(0, "sdr-owner")

    system_owner = Enum.YLeaf(1, "system-owner")


class SnmpPrecedenceValue1(Enum):
    """
    SnmpPrecedenceValue1

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


class SnmpPrivAlgorithm(Enum):
    """
    SnmpPrivAlgorithm

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


class SnmpSecurityModel(Enum):
    """
    SnmpSecurityModel

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


class SnmpTos(Enum):
    """
    SnmpTos

    Snmp tos

    .. data:: precedence = 0

    	SNMP TOS type Precedence

    .. data:: dscp = 1

    	SNMP TOS type DSCP

    """

    precedence = Enum.YLeaf(0, "precedence")

    dscp = Enum.YLeaf(1, "dscp")


class Snmpacl(Enum):
    """
    Snmpacl

    Snmpacl

    .. data:: ipv4 = 1

    	Ipv4 Access-list

    .. data:: ipv6 = 2

    	Ipv6 Access-list

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


class UserSnmpVersion(Enum):
    """
    UserSnmpVersion

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



class Mib(Entity):
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
    
    .. attribute:: subscriber
    
    	Subscriber threshold commands
    	**type**\:   :py:class:`Subscriber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber>`
    
    

    """

    _prefix = 'snmp-agent-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(Mib, self).__init__()
        self._top_entity = None

        self.yang_name = "mib"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-agent-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"cb-qosmib" : ("cb_qosmib", Mib.CbQosmib), "entity-mib" : ("entity_mib", Mib.EntityMib), "interface-mib" : ("interface_mib", Mib.InterfaceMib), "mpls-frr-mib" : ("mpls_frr_mib", Mib.MplsFrrMib), "mpls-p2mp-mib" : ("mpls_p2mp_mib", Mib.MplsP2MpMib), "mpls-te-ext-mib" : ("mpls_te_ext_mib", Mib.MplsTeExtMib), "mpls-te-ext-std-mib" : ("mpls_te_ext_std_mib", Mib.MplsTeExtStdMib), "mpls-te-mib" : ("mpls_te_mib", Mib.MplsTeMib), "subscriber" : ("subscriber", Mib.Subscriber)}
        self._child_list_classes = {}

        self.sensor_mib_cache = YLeaf(YType.empty, "Cisco-IOS-XR-snmp-ciscosensormib-cfg:sensor-mib-cache")

        self.cb_qosmib = Mib.CbQosmib()
        self.cb_qosmib.parent = self
        self._children_name_map["cb_qosmib"] = "cb-qosmib"
        self._children_yang_names.add("cb-qosmib")

        self.entity_mib = Mib.EntityMib()
        self.entity_mib.parent = self
        self._children_name_map["entity_mib"] = "entity-mib"
        self._children_yang_names.add("entity-mib")

        self.interface_mib = Mib.InterfaceMib()
        self.interface_mib.parent = self
        self._children_name_map["interface_mib"] = "interface-mib"
        self._children_yang_names.add("interface-mib")

        self.mpls_frr_mib = Mib.MplsFrrMib()
        self.mpls_frr_mib.parent = self
        self._children_name_map["mpls_frr_mib"] = "mpls-frr-mib"
        self._children_yang_names.add("mpls-frr-mib")

        self.mpls_p2mp_mib = Mib.MplsP2MpMib()
        self.mpls_p2mp_mib.parent = self
        self._children_name_map["mpls_p2mp_mib"] = "mpls-p2mp-mib"
        self._children_yang_names.add("mpls-p2mp-mib")

        self.mpls_te_ext_mib = Mib.MplsTeExtMib()
        self.mpls_te_ext_mib.parent = self
        self._children_name_map["mpls_te_ext_mib"] = "mpls-te-ext-mib"
        self._children_yang_names.add("mpls-te-ext-mib")

        self.mpls_te_ext_std_mib = Mib.MplsTeExtStdMib()
        self.mpls_te_ext_std_mib.parent = self
        self._children_name_map["mpls_te_ext_std_mib"] = "mpls-te-ext-std-mib"
        self._children_yang_names.add("mpls-te-ext-std-mib")

        self.mpls_te_mib = Mib.MplsTeMib()
        self.mpls_te_mib.parent = self
        self._children_name_map["mpls_te_mib"] = "mpls-te-mib"
        self._children_yang_names.add("mpls-te-mib")

        self.subscriber = Mib.Subscriber()
        self.subscriber.parent = self
        self._children_name_map["subscriber"] = "subscriber"
        self._children_yang_names.add("subscriber")
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib"

    def __setattr__(self, name, value):
        self._perform_setattr(Mib, ['sensor_mib_cache'], name, value)


    class CbQosmib(Entity):
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
        _revision = '2017-05-01'

        def __init__(self):
            super(Mib.CbQosmib, self).__init__()

            self.yang_name = "cb-qosmib"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"cache" : ("cache", Mib.CbQosmib.Cache)}
            self._child_list_classes = {}

            self.member_interface_stats = YLeaf(YType.empty, "member-interface-stats")

            self.persist = YLeaf(YType.empty, "persist")

            self.cache = Mib.CbQosmib.Cache()
            self.cache.parent = self
            self._children_name_map["cache"] = "cache"
            self._children_yang_names.add("cache")
            self._segment_path = lambda: "Cisco-IOS-XR-qos-mibs-cfg:cb-qosmib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.CbQosmib, ['member_interface_stats', 'persist'], name, value)


        class Cache(Entity):
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
            _revision = '2017-05-01'

            def __init__(self):
                super(Mib.CbQosmib.Cache, self).__init__()

                self.yang_name = "cache"
                self.yang_parent_name = "cb-qosmib"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")

                self.refresh_time = YLeaf(YType.uint32, "refresh-time")

                self.service_policy_count = YLeaf(YType.uint32, "service-policy-count")
                self._segment_path = lambda: "cache"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-qos-mibs-cfg:cb-qosmib/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mib.CbQosmib.Cache, ['enable', 'refresh_time', 'service_policy_count'], name, value)


    class EntityMib(Entity):
        """
        Entity MIB
        
        .. attribute:: entity_index_persistence
        
        	Enable entPhysicalIndex persistence
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'snmp-entitymib-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Mib.EntityMib, self).__init__()

            self.yang_name = "entity-mib"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.entity_index_persistence = YLeaf(YType.empty, "entity-index-persistence")
            self._segment_path = lambda: "Cisco-IOS-XR-snmp-entitymib-cfg:entity-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.EntityMib, ['entity_index_persistence'], name, value)


    class InterfaceMib(Entity):
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
        _revision = '2017-05-01'

        def __init__(self):
            super(Mib.InterfaceMib, self).__init__()

            self.yang_name = "interface-mib"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"interfaces" : ("interfaces", Mib.InterfaceMib.Interfaces), "notification" : ("notification", Mib.InterfaceMib.Notification), "subsets" : ("subsets", Mib.InterfaceMib.Subsets)}
            self._child_list_classes = {}

            self.interface_alias_long = YLeaf(YType.empty, "interface-alias-long")

            self.interface_index_persistence = YLeaf(YType.empty, "interface-index-persistence")

            self.internal_cache = YLeaf(YType.uint32, "internal-cache")

            self.ip_subscriber = YLeaf(YType.empty, "ip-subscriber")

            self.statistics_cache = YLeaf(YType.empty, "statistics-cache")

            self.interfaces = Mib.InterfaceMib.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.notification = Mib.InterfaceMib.Notification()
            self.notification.parent = self
            self._children_name_map["notification"] = "notification"
            self._children_yang_names.add("notification")

            self.subsets = Mib.InterfaceMib.Subsets()
            self.subsets.parent = self
            self._children_name_map["subsets"] = "subsets"
            self._children_yang_names.add("subsets")
            self._segment_path = lambda: "Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.InterfaceMib, ['interface_alias_long', 'interface_index_persistence', 'internal_cache', 'ip_subscriber', 'statistics_cache'], name, value)


        class Interfaces(Entity):
            """
            Enter the SNMP interface configuration commands
            
            .. attribute:: interface
            
            	Interface to configure
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.InterfaceMib.Interfaces.Interface>`
            
            

            """

            _prefix = 'snmp-ifmib-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Mib.InterfaceMib.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "interface-mib"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"interface" : ("interface", Mib.InterfaceMib.Interfaces.Interface)}

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mib.InterfaceMib.Interfaces, [], name, value)


            class Interface(Entity):
                """
                Interface to configure
                
                .. attribute:: interface_name  <key>
                
                	The name of the interface
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: index_persistence
                
                	Enable or disable index persistence
                	**type**\:  bool
                
                .. attribute:: link_up_down
                
                	Enable or disable LinkUpDown notification
                	**type**\:  bool
                
                

                """

                _prefix = 'snmp-ifmib-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Mib.InterfaceMib.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.index_persistence = YLeaf(YType.boolean, "index-persistence")

                    self.link_up_down = YLeaf(YType.boolean, "link-up-down")
                    self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib/interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mib.InterfaceMib.Interfaces.Interface, ['interface_name', 'index_persistence', 'link_up_down'], name, value)


        class Notification(Entity):
            """
            MIB notification configuration
            
            .. attribute:: link_ietf
            
            	Set the varbind of linkupdown trap to the RFC specified varbinds (default cisco)
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-ifmib-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Mib.InterfaceMib.Notification, self).__init__()

                self.yang_name = "notification"
                self.yang_parent_name = "interface-mib"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.link_ietf = YLeaf(YType.empty, "link-ietf")
                self._segment_path = lambda: "notification"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mib.InterfaceMib.Notification, ['link_ietf'], name, value)


        class Subsets(Entity):
            """
            Add configuration for an interface subset
            
            .. attribute:: subset
            
            	Subset priorityID to group ifNames based on Regular Expression
            	**type**\: list of    :py:class:`Subset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.InterfaceMib.Subsets.Subset>`
            
            

            """

            _prefix = 'snmp-ifmib-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Mib.InterfaceMib.Subsets, self).__init__()

                self.yang_name = "subsets"
                self.yang_parent_name = "interface-mib"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"subset" : ("subset", Mib.InterfaceMib.Subsets.Subset)}

                self.subset = YList(self)
                self._segment_path = lambda: "subsets"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mib.InterfaceMib.Subsets, [], name, value)


            class Subset(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(Mib.InterfaceMib.Subsets.Subset, self).__init__()

                    self.yang_name = "subset"
                    self.yang_parent_name = "subsets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"link-up-down" : ("link_up_down", Mib.InterfaceMib.Subsets.Subset.LinkUpDown)}
                    self._child_list_classes = {}

                    self.subset_id = YLeaf(YType.uint32, "subset-id")

                    self.link_up_down = Mib.InterfaceMib.Subsets.Subset.LinkUpDown()
                    self.link_up_down.parent = self
                    self._children_name_map["link_up_down"] = "link-up-down"
                    self._children_yang_names.add("link-up-down")
                    self._segment_path = lambda: "subset" + "[subset-id='" + self.subset_id.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-snmp-ifmib-cfg:interface-mib/subsets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mib.InterfaceMib.Subsets.Subset, ['subset_id'], name, value)


                class LinkUpDown(Entity):
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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Mib.InterfaceMib.Subsets.Subset.LinkUpDown, self).__init__()

                        self.yang_name = "link-up-down"
                        self.yang_parent_name = "subset"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.enable = YLeaf(YType.boolean, "enable")

                        self.regular_expression = YLeaf(YType.str, "regular-expression")
                        self._segment_path = lambda: "link-up-down"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mib.InterfaceMib.Subsets.Subset.LinkUpDown, ['enable', 'regular_expression'], name, value)


    class MplsFrrMib(Entity):
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
        _revision = '2017-05-01'

        def __init__(self):
            super(Mib.MplsFrrMib, self).__init__()

            self.yang_name = "mpls-frr-mib"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.cache_timer = YLeaf(YType.uint32, "cache-timer")
            self._segment_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-frr-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.MplsFrrMib, ['cache_timer'], name, value)


    class MplsP2MpMib(Entity):
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
        _revision = '2017-05-01'

        def __init__(self):
            super(Mib.MplsP2MpMib, self).__init__()

            self.yang_name = "mpls-p2mp-mib"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.cache_timer = YLeaf(YType.uint32, "cache-timer")
            self._segment_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-p2mp-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.MplsP2MpMib, ['cache_timer'], name, value)


    class MplsTeExtMib(Entity):
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
        _revision = '2017-05-01'

        def __init__(self):
            super(Mib.MplsTeExtMib, self).__init__()

            self.yang_name = "mpls-te-ext-mib"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.cache_timer = YLeaf(YType.uint32, "cache-timer")
            self._segment_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te-ext-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.MplsTeExtMib, ['cache_timer'], name, value)


    class MplsTeExtStdMib(Entity):
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
        _revision = '2017-05-01'

        def __init__(self):
            super(Mib.MplsTeExtStdMib, self).__init__()

            self.yang_name = "mpls-te-ext-std-mib"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.cache_timer = YLeaf(YType.uint32, "cache-timer")
            self._segment_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te-ext-std-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.MplsTeExtStdMib, ['cache_timer'], name, value)


    class MplsTeMib(Entity):
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
        _revision = '2017-05-01'

        def __init__(self):
            super(Mib.MplsTeMib, self).__init__()

            self.yang_name = "mpls-te-mib"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.cache_garbage_collect_timer = YLeaf(YType.uint32, "cache-garbage-collect-timer")

            self.cache_timer = YLeaf(YType.uint32, "cache-timer")
            self._segment_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te-mib"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Mib.MplsTeMib, ['cache_garbage_collect_timer', 'cache_timer'], name, value)


    class Subscriber(Entity):
        """
        Subscriber threshold commands
        
        .. attribute:: threshold
        
        	Subscriber threshold commands
        	**type**\:   :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold>`
        
        

        """

        _prefix = 'subscriber-session-mon-mibs-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Mib.Subscriber, self).__init__()

            self.yang_name = "subscriber"
            self.yang_parent_name = "mib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"threshold" : ("threshold", Mib.Subscriber.Threshold)}
            self._child_list_classes = {}

            self.threshold = Mib.Subscriber.Threshold()
            self.threshold.parent = self
            self._children_name_map["threshold"] = "threshold"
            self._children_yang_names.add("threshold")
            self._segment_path = lambda: "Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/%s" % self._segment_path()


        class Threshold(Entity):
            """
            Subscriber threshold commands
            
            .. attribute:: access_interface_sub
            
            	Access interface for regular expression
            	**type**\:   :py:class:`AccessInterfaceSub <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.AccessInterfaceSub>`
            
            .. attribute:: delta
            
            	Delta loss keyword
            	**type**\:   :py:class:`Delta <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta>`
            
            .. attribute:: falling
            
            	Falling threshold
            	**type**\:   :py:class:`Falling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Falling>`
            
            .. attribute:: rising
            
            	Rising threshold
            	**type**\:   :py:class:`Rising <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Rising>`
            
            

            """

            _prefix = 'subscriber-session-mon-mibs-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Mib.Subscriber.Threshold, self).__init__()

                self.yang_name = "threshold"
                self.yang_parent_name = "subscriber"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"access-interface-sub" : ("access_interface_sub", Mib.Subscriber.Threshold.AccessInterfaceSub), "delta" : ("delta", Mib.Subscriber.Threshold.Delta), "falling" : ("falling", Mib.Subscriber.Threshold.Falling), "rising" : ("rising", Mib.Subscriber.Threshold.Rising)}
                self._child_list_classes = {}

                self.access_interface_sub = Mib.Subscriber.Threshold.AccessInterfaceSub()
                self.access_interface_sub.parent = self
                self._children_name_map["access_interface_sub"] = "access-interface-sub"
                self._children_yang_names.add("access-interface-sub")

                self.delta = Mib.Subscriber.Threshold.Delta()
                self.delta.parent = self
                self._children_name_map["delta"] = "delta"
                self._children_yang_names.add("delta")

                self.falling = Mib.Subscriber.Threshold.Falling()
                self.falling.parent = self
                self._children_name_map["falling"] = "falling"
                self._children_yang_names.add("falling")

                self.rising = Mib.Subscriber.Threshold.Rising()
                self.rising.parent = self
                self._children_name_map["rising"] = "rising"
                self._children_yang_names.add("rising")
                self._segment_path = lambda: "threshold"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/%s" % self._segment_path()


            class AccessInterfaceSub(Entity):
                """
                Access interface for regular expression
                
                .. attribute:: subsets
                
                	Table of Subset
                	**type**\:   :py:class:`Subsets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets>`
                
                

                """

                _prefix = 'subscriber-session-mon-mibs-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Mib.Subscriber.Threshold.AccessInterfaceSub, self).__init__()

                    self.yang_name = "access-interface-sub"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"subsets" : ("subsets", Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets)}
                    self._child_list_classes = {}

                    self.subsets = Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets()
                    self.subsets.parent = self
                    self._children_name_map["subsets"] = "subsets"
                    self._children_yang_names.add("subsets")
                    self._segment_path = lambda: "access-interface-sub"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/%s" % self._segment_path()


                class Subsets(Entity):
                    """
                    Table of Subset
                    
                    .. attribute:: subset
                    
                    	Subset command
                    	**type**\: list of    :py:class:`Subset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset>`
                    
                    

                    """

                    _prefix = 'subscriber-session-mon-mibs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets, self).__init__()

                        self.yang_name = "subsets"
                        self.yang_parent_name = "access-interface-sub"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {"subset" : ("subset", Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset)}

                        self.subset = YList(self)
                        self._segment_path = lambda: "subsets"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/access-interface-sub/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets, [], name, value)


                    class Subset(Entity):
                        """
                        Subset command
                        
                        .. attribute:: subset_id  <key>
                        
                        	Subset number
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        .. attribute:: regular_expression
                        
                        	Regular expression
                        	**type**\:   :py:class:`RegularExpression <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression>`
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset, self).__init__()

                            self.yang_name = "subset"
                            self.yang_parent_name = "subsets"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {"regular-expression" : ("regular_expression", Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression)}
                            self._child_list_classes = {}

                            self.subset_id = YLeaf(YType.uint32, "subset-id")

                            self.regular_expression = Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression()
                            self.regular_expression.parent = self
                            self._children_name_map["regular_expression"] = "regular-expression"
                            self._children_yang_names.add("regular-expression")
                            self._segment_path = lambda: "subset" + "[subset-id='" + self.subset_id.get() + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/access-interface-sub/subsets/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset, ['subset_id'], name, value)


                        class RegularExpression(Entity):
                            """
                            Regular expression
                            
                            .. attribute:: notification
                            
                            	Notification keyword
                            	**type**\:   :py:class:`Notification <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification>`
                            
                            

                            """

                            _prefix = 'subscriber-session-mon-mibs-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression, self).__init__()

                                self.yang_name = "regular-expression"
                                self.yang_parent_name = "subset"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"notification" : ("notification", Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification)}
                                self._child_list_classes = {}

                                self.notification = Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification()
                                self.notification.parent = self
                                self._children_name_map["notification"] = "notification"
                                self._children_yang_names.add("notification")
                                self._segment_path = lambda: "regular-expression"


                            class Notification(Entity):
                                """
                                Notification keyword
                                
                                .. attribute:: rising_falling
                                
                                	Rising\-falling threshold
                                	**type**\:   :py:class:`RisingFalling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification.RisingFalling>`
                                
                                

                                """

                                _prefix = 'subscriber-session-mon-mibs-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification, self).__init__()

                                    self.yang_name = "notification"
                                    self.yang_parent_name = "regular-expression"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"rising-falling" : ("rising_falling", Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification.RisingFalling)}
                                    self._child_list_classes = {}

                                    self.rising_falling = Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification.RisingFalling()
                                    self.rising_falling.parent = self
                                    self._children_name_map["rising_falling"] = "rising-falling"
                                    self._children_yang_names.add("rising-falling")
                                    self._segment_path = lambda: "notification"


                                class RisingFalling(Entity):
                                    """
                                    Rising\-falling threshold
                                    
                                    .. attribute:: disable
                                    
                                    	Disable the notifications on access interfaces
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'subscriber-session-mon-mibs-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification.RisingFalling, self).__init__()

                                        self.yang_name = "rising-falling"
                                        self.yang_parent_name = "notification"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.disable = YLeaf(YType.str, "disable")
                                        self._segment_path = lambda: "rising-falling"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mib.Subscriber.Threshold.AccessInterfaceSub.Subsets.Subset.RegularExpression.Notification.RisingFalling, ['disable'], name, value)


            class Delta(Entity):
                """
                Delta loss keyword
                
                .. attribute:: evaluation
                
                	Evaluation keyword
                	**type**\:   :py:class:`Evaluation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Evaluation>`
                
                .. attribute:: percent
                
                	Delta loss percent
                	**type**\:   :py:class:`Percent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Percent>`
                
                

                """

                _prefix = 'subscriber-session-mon-mibs-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Mib.Subscriber.Threshold.Delta, self).__init__()

                    self.yang_name = "delta"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"evaluation" : ("evaluation", Mib.Subscriber.Threshold.Delta.Evaluation), "percent" : ("percent", Mib.Subscriber.Threshold.Delta.Percent)}
                    self._child_list_classes = {}

                    self.evaluation = Mib.Subscriber.Threshold.Delta.Evaluation()
                    self.evaluation.parent = self
                    self._children_name_map["evaluation"] = "evaluation"
                    self._children_yang_names.add("evaluation")

                    self.percent = Mib.Subscriber.Threshold.Delta.Percent()
                    self.percent.parent = self
                    self._children_name_map["percent"] = "percent"
                    self._children_yang_names.add("percent")
                    self._segment_path = lambda: "delta"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/%s" % self._segment_path()


                class Evaluation(Entity):
                    """
                    Evaluation keyword
                    
                    .. attribute:: access_interfaces
                    
                    	Table of AccessInterface
                    	**type**\:   :py:class:`AccessInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces>`
                    
                    .. attribute:: nodes
                    
                    	Table of Node
                    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Evaluation.Nodes>`
                    
                    

                    """

                    _prefix = 'subscriber-session-mon-mibs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Mib.Subscriber.Threshold.Delta.Evaluation, self).__init__()

                        self.yang_name = "evaluation"
                        self.yang_parent_name = "delta"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"access-interfaces" : ("access_interfaces", Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces), "nodes" : ("nodes", Mib.Subscriber.Threshold.Delta.Evaluation.Nodes)}
                        self._child_list_classes = {}

                        self.access_interfaces = Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces()
                        self.access_interfaces.parent = self
                        self._children_name_map["access_interfaces"] = "access-interfaces"
                        self._children_yang_names.add("access-interfaces")

                        self.nodes = Mib.Subscriber.Threshold.Delta.Evaluation.Nodes()
                        self.nodes.parent = self
                        self._children_name_map["nodes"] = "nodes"
                        self._children_yang_names.add("nodes")
                        self._segment_path = lambda: "evaluation"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/%s" % self._segment_path()


                    class AccessInterfaces(Entity):
                        """
                        Table of AccessInterface
                        
                        .. attribute:: access_interface
                        
                        	Access interface
                        	**type**\: list of    :py:class:`AccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces.AccessInterface>`
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces, self).__init__()

                            self.yang_name = "access-interfaces"
                            self.yang_parent_name = "evaluation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {"access-interface" : ("access_interface", Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces.AccessInterface)}

                            self.access_interface = YList(self)
                            self._segment_path = lambda: "access-interfaces"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/evaluation/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces, [], name, value)


                        class AccessInterface(Entity):
                            """
                            Access interface
                            
                            .. attribute:: interface_name  <key>
                            
                            	Interface name
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: interval
                            
                            	Interval value in multiples of 10
                            	**type**\:  int
                            
                            	**range:** 30..3600
                            
                            .. attribute:: session_count
                            
                            	Session count
                            	**type**\:  int
                            
                            	**range:** 1..4294967294
                            
                            

                            """

                            _prefix = 'subscriber-session-mon-mibs-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces.AccessInterface, self).__init__()

                                self.yang_name = "access-interface"
                                self.yang_parent_name = "access-interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.interval = YLeaf(YType.uint32, "interval")

                                self.session_count = YLeaf(YType.uint32, "session-count")
                                self._segment_path = lambda: "access-interface" + "[interface-name='" + self.interface_name.get() + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/evaluation/access-interfaces/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mib.Subscriber.Threshold.Delta.Evaluation.AccessInterfaces.AccessInterface, ['interface_name', 'interval', 'session_count'], name, value)


                    class Nodes(Entity):
                        """
                        Table of Node
                        
                        .. attribute:: node
                        
                        	Rising node level
                        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Evaluation.Nodes.Node>`
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mib.Subscriber.Threshold.Delta.Evaluation.Nodes, self).__init__()

                            self.yang_name = "nodes"
                            self.yang_parent_name = "evaluation"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {"node" : ("node", Mib.Subscriber.Threshold.Delta.Evaluation.Nodes.Node)}

                            self.node = YList(self)
                            self._segment_path = lambda: "nodes"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/evaluation/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.Delta.Evaluation.Nodes, [], name, value)


                        class Node(Entity):
                            """
                            Rising node level
                            
                            .. attribute:: node_name  <key>
                            
                            	location
                            	**type**\:  str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: interval
                            
                            	interval value in multiples of 10
                            	**type**\:  int
                            
                            	**range:** 30..3600
                            
                            .. attribute:: session_count
                            
                            	Session count
                            	**type**\:  int
                            
                            	**range:** 1..4294967294
                            
                            

                            """

                            _prefix = 'subscriber-session-mon-mibs-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Mib.Subscriber.Threshold.Delta.Evaluation.Nodes.Node, self).__init__()

                                self.yang_name = "node"
                                self.yang_parent_name = "nodes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.node_name = YLeaf(YType.str, "node-name")

                                self.interval = YLeaf(YType.uint32, "interval")

                                self.session_count = YLeaf(YType.uint32, "session-count")
                                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/evaluation/nodes/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mib.Subscriber.Threshold.Delta.Evaluation.Nodes.Node, ['node_name', 'interval', 'session_count'], name, value)


                class Percent(Entity):
                    """
                    Delta loss percent
                    
                    .. attribute:: access_interfaces
                    
                    	Table of AccessInterface
                    	**type**\:   :py:class:`AccessInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces>`
                    
                    .. attribute:: nodes
                    
                    	Table of Node
                    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Percent.Nodes>`
                    
                    

                    """

                    _prefix = 'subscriber-session-mon-mibs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Mib.Subscriber.Threshold.Delta.Percent, self).__init__()

                        self.yang_name = "percent"
                        self.yang_parent_name = "delta"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"access-interfaces" : ("access_interfaces", Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces), "nodes" : ("nodes", Mib.Subscriber.Threshold.Delta.Percent.Nodes)}
                        self._child_list_classes = {}

                        self.access_interfaces = Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces()
                        self.access_interfaces.parent = self
                        self._children_name_map["access_interfaces"] = "access-interfaces"
                        self._children_yang_names.add("access-interfaces")

                        self.nodes = Mib.Subscriber.Threshold.Delta.Percent.Nodes()
                        self.nodes.parent = self
                        self._children_name_map["nodes"] = "nodes"
                        self._children_yang_names.add("nodes")
                        self._segment_path = lambda: "percent"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/%s" % self._segment_path()


                    class AccessInterfaces(Entity):
                        """
                        Table of AccessInterface
                        
                        .. attribute:: access_interface
                        
                        	Access interface
                        	**type**\: list of    :py:class:`AccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces.AccessInterface>`
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces, self).__init__()

                            self.yang_name = "access-interfaces"
                            self.yang_parent_name = "percent"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {"access-interface" : ("access_interface", Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces.AccessInterface)}

                            self.access_interface = YList(self)
                            self._segment_path = lambda: "access-interfaces"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/percent/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces, [], name, value)


                        class AccessInterface(Entity):
                            """
                            Access interface
                            
                            .. attribute:: interface_name  <key>
                            
                            	Interface name
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: interval
                            
                            	Interval value in multiples of 10
                            	**type**\:  int
                            
                            	**range:** 30..3600
                            
                            .. attribute:: session_count
                            
                            	Session count
                            	**type**\:  int
                            
                            	**range:** 1..4294967294
                            
                            

                            """

                            _prefix = 'subscriber-session-mon-mibs-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces.AccessInterface, self).__init__()

                                self.yang_name = "access-interface"
                                self.yang_parent_name = "access-interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.interval = YLeaf(YType.uint32, "interval")

                                self.session_count = YLeaf(YType.uint32, "session-count")
                                self._segment_path = lambda: "access-interface" + "[interface-name='" + self.interface_name.get() + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/percent/access-interfaces/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mib.Subscriber.Threshold.Delta.Percent.AccessInterfaces.AccessInterface, ['interface_name', 'interval', 'session_count'], name, value)


                    class Nodes(Entity):
                        """
                        Table of Node
                        
                        .. attribute:: node
                        
                        	Rising node level
                        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Delta.Percent.Nodes.Node>`
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mib.Subscriber.Threshold.Delta.Percent.Nodes, self).__init__()

                            self.yang_name = "nodes"
                            self.yang_parent_name = "percent"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {"node" : ("node", Mib.Subscriber.Threshold.Delta.Percent.Nodes.Node)}

                            self.node = YList(self)
                            self._segment_path = lambda: "nodes"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/percent/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.Delta.Percent.Nodes, [], name, value)


                        class Node(Entity):
                            """
                            Rising node level
                            
                            .. attribute:: node_name  <key>
                            
                            	location
                            	**type**\:  str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: interval
                            
                            	interval value in multiples of 10
                            	**type**\:  int
                            
                            	**range:** 30..3600
                            
                            .. attribute:: session_count
                            
                            	Session count
                            	**type**\:  int
                            
                            	**range:** 1..4294967294
                            
                            

                            """

                            _prefix = 'subscriber-session-mon-mibs-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Mib.Subscriber.Threshold.Delta.Percent.Nodes.Node, self).__init__()

                                self.yang_name = "node"
                                self.yang_parent_name = "nodes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.node_name = YLeaf(YType.str, "node-name")

                                self.interval = YLeaf(YType.uint32, "interval")

                                self.session_count = YLeaf(YType.uint32, "session-count")
                                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/delta/percent/nodes/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mib.Subscriber.Threshold.Delta.Percent.Nodes.Node, ['node_name', 'interval', 'session_count'], name, value)


            class Falling(Entity):
                """
                Falling threshold
                
                .. attribute:: access_interfaces
                
                	Table of AccessInterface
                	**type**\:   :py:class:`AccessInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Falling.AccessInterfaces>`
                
                .. attribute:: nodes
                
                	Table of Node
                	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Falling.Nodes>`
                
                

                """

                _prefix = 'subscriber-session-mon-mibs-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Mib.Subscriber.Threshold.Falling, self).__init__()

                    self.yang_name = "falling"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"access-interfaces" : ("access_interfaces", Mib.Subscriber.Threshold.Falling.AccessInterfaces), "nodes" : ("nodes", Mib.Subscriber.Threshold.Falling.Nodes)}
                    self._child_list_classes = {}

                    self.access_interfaces = Mib.Subscriber.Threshold.Falling.AccessInterfaces()
                    self.access_interfaces.parent = self
                    self._children_name_map["access_interfaces"] = "access-interfaces"
                    self._children_yang_names.add("access-interfaces")

                    self.nodes = Mib.Subscriber.Threshold.Falling.Nodes()
                    self.nodes.parent = self
                    self._children_name_map["nodes"] = "nodes"
                    self._children_yang_names.add("nodes")
                    self._segment_path = lambda: "falling"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/%s" % self._segment_path()


                class AccessInterfaces(Entity):
                    """
                    Table of AccessInterface
                    
                    .. attribute:: access_interface
                    
                    	Access interface
                    	**type**\: list of    :py:class:`AccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Falling.AccessInterfaces.AccessInterface>`
                    
                    

                    """

                    _prefix = 'subscriber-session-mon-mibs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Mib.Subscriber.Threshold.Falling.AccessInterfaces, self).__init__()

                        self.yang_name = "access-interfaces"
                        self.yang_parent_name = "falling"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {"access-interface" : ("access_interface", Mib.Subscriber.Threshold.Falling.AccessInterfaces.AccessInterface)}

                        self.access_interface = YList(self)
                        self._segment_path = lambda: "access-interfaces"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/falling/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mib.Subscriber.Threshold.Falling.AccessInterfaces, [], name, value)


                    class AccessInterface(Entity):
                        """
                        Access interface
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface name
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: interval
                        
                        	Interval value in multiples of 10
                        	**type**\:  int
                        
                        	**range:** 30..3600
                        
                        .. attribute:: session_count
                        
                        	Session count
                        	**type**\:  int
                        
                        	**range:** 1..4294967294
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mib.Subscriber.Threshold.Falling.AccessInterfaces.AccessInterface, self).__init__()

                            self.yang_name = "access-interface"
                            self.yang_parent_name = "access-interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.interval = YLeaf(YType.uint32, "interval")

                            self.session_count = YLeaf(YType.uint32, "session-count")
                            self._segment_path = lambda: "access-interface" + "[interface-name='" + self.interface_name.get() + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/falling/access-interfaces/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.Falling.AccessInterfaces.AccessInterface, ['interface_name', 'interval', 'session_count'], name, value)


                class Nodes(Entity):
                    """
                    Table of Node
                    
                    .. attribute:: node
                    
                    	Rising node level
                    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Falling.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'subscriber-session-mon-mibs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Mib.Subscriber.Threshold.Falling.Nodes, self).__init__()

                        self.yang_name = "nodes"
                        self.yang_parent_name = "falling"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {"node" : ("node", Mib.Subscriber.Threshold.Falling.Nodes.Node)}

                        self.node = YList(self)
                        self._segment_path = lambda: "nodes"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/falling/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mib.Subscriber.Threshold.Falling.Nodes, [], name, value)


                    class Node(Entity):
                        """
                        Rising node level
                        
                        .. attribute:: node_name  <key>
                        
                        	location
                        	**type**\:  str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: interval
                        
                        	interval value in multiples of 10
                        	**type**\:  int
                        
                        	**range:** 30..3600
                        
                        .. attribute:: session_count
                        
                        	Session count
                        	**type**\:  int
                        
                        	**range:** 1..4294967294
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mib.Subscriber.Threshold.Falling.Nodes.Node, self).__init__()

                            self.yang_name = "node"
                            self.yang_parent_name = "nodes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.node_name = YLeaf(YType.str, "node-name")

                            self.interval = YLeaf(YType.uint32, "interval")

                            self.session_count = YLeaf(YType.uint32, "session-count")
                            self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/falling/nodes/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.Falling.Nodes.Node, ['node_name', 'interval', 'session_count'], name, value)


            class Rising(Entity):
                """
                Rising threshold
                
                .. attribute:: access_interfaces
                
                	Table of AccessInterface
                	**type**\:   :py:class:`AccessInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Rising.AccessInterfaces>`
                
                .. attribute:: nodes
                
                	Table of Node
                	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Rising.Nodes>`
                
                

                """

                _prefix = 'subscriber-session-mon-mibs-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Mib.Subscriber.Threshold.Rising, self).__init__()

                    self.yang_name = "rising"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"access-interfaces" : ("access_interfaces", Mib.Subscriber.Threshold.Rising.AccessInterfaces), "nodes" : ("nodes", Mib.Subscriber.Threshold.Rising.Nodes)}
                    self._child_list_classes = {}

                    self.access_interfaces = Mib.Subscriber.Threshold.Rising.AccessInterfaces()
                    self.access_interfaces.parent = self
                    self._children_name_map["access_interfaces"] = "access-interfaces"
                    self._children_yang_names.add("access-interfaces")

                    self.nodes = Mib.Subscriber.Threshold.Rising.Nodes()
                    self.nodes.parent = self
                    self._children_name_map["nodes"] = "nodes"
                    self._children_yang_names.add("nodes")
                    self._segment_path = lambda: "rising"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/%s" % self._segment_path()


                class AccessInterfaces(Entity):
                    """
                    Table of AccessInterface
                    
                    .. attribute:: access_interface
                    
                    	Access interface
                    	**type**\: list of    :py:class:`AccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Rising.AccessInterfaces.AccessInterface>`
                    
                    

                    """

                    _prefix = 'subscriber-session-mon-mibs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Mib.Subscriber.Threshold.Rising.AccessInterfaces, self).__init__()

                        self.yang_name = "access-interfaces"
                        self.yang_parent_name = "rising"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {"access-interface" : ("access_interface", Mib.Subscriber.Threshold.Rising.AccessInterfaces.AccessInterface)}

                        self.access_interface = YList(self)
                        self._segment_path = lambda: "access-interfaces"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/rising/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mib.Subscriber.Threshold.Rising.AccessInterfaces, [], name, value)


                    class AccessInterface(Entity):
                        """
                        Access interface
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface name
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: interval
                        
                        	Interval value in multiples of 10
                        	**type**\:  int
                        
                        	**range:** 30..3600
                        
                        .. attribute:: session_count
                        
                        	Session count
                        	**type**\:  int
                        
                        	**range:** 1..4294967294
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mib.Subscriber.Threshold.Rising.AccessInterfaces.AccessInterface, self).__init__()

                            self.yang_name = "access-interface"
                            self.yang_parent_name = "access-interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.interval = YLeaf(YType.uint32, "interval")

                            self.session_count = YLeaf(YType.uint32, "session-count")
                            self._segment_path = lambda: "access-interface" + "[interface-name='" + self.interface_name.get() + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/rising/access-interfaces/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.Rising.AccessInterfaces.AccessInterface, ['interface_name', 'interval', 'session_count'], name, value)


                class Nodes(Entity):
                    """
                    Table of Node
                    
                    .. attribute:: node
                    
                    	Rising node level
                    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Mib.Subscriber.Threshold.Rising.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'subscriber-session-mon-mibs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Mib.Subscriber.Threshold.Rising.Nodes, self).__init__()

                        self.yang_name = "nodes"
                        self.yang_parent_name = "rising"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {"node" : ("node", Mib.Subscriber.Threshold.Rising.Nodes.Node)}

                        self.node = YList(self)
                        self._segment_path = lambda: "nodes"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/rising/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mib.Subscriber.Threshold.Rising.Nodes, [], name, value)


                    class Node(Entity):
                        """
                        Rising node level
                        
                        .. attribute:: node_name  <key>
                        
                        	location
                        	**type**\:  str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: interval
                        
                        	interval value in multiples of 10
                        	**type**\:  int
                        
                        	**range:** 30..3600
                        
                        .. attribute:: session_count
                        
                        	Session count
                        	**type**\:  int
                        
                        	**range:** 1..4294967294
                        
                        

                        """

                        _prefix = 'subscriber-session-mon-mibs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mib.Subscriber.Threshold.Rising.Nodes.Node, self).__init__()

                            self.yang_name = "node"
                            self.yang_parent_name = "nodes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.node_name = YLeaf(YType.str, "node-name")

                            self.interval = YLeaf(YType.uint32, "interval")

                            self.session_count = YLeaf(YType.uint32, "session-count")
                            self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:mib/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber/threshold/rising/nodes/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mib.Subscriber.Threshold.Rising.Nodes.Node, ['node_name', 'interval', 'session_count'], name, value)

    def clone_ptr(self):
        self._top_entity = Mib()
        return self._top_entity

class Snmp(Entity):
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
    
    	**pattern:** [a\-zA\-Z0\-9./\-]+
    
    .. attribute:: trap_source_ipv4
    
    	Assign an interface for the source address of all traps
    	**type**\:  str
    
    	**pattern:** [a\-zA\-Z0\-9./\-]+
    
    .. attribute:: trap_source_ipv6
    
    	Assign an interface for the source IPV6 address of all traps
    	**type**\:  str
    
    	**pattern:** [a\-zA\-Z0\-9./\-]+
    
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
    _revision = '2017-05-01'

    def __init__(self):
        super(Snmp, self).__init__()
        self._top_entity = None

        self.yang_name = "snmp"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-agent-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"administration" : ("administration", Snmp.Administration), "agent" : ("agent", Snmp.Agent), "bulk-stats" : ("bulk_stats", Snmp.BulkStats), "context-mappings" : ("context_mappings", Snmp.ContextMappings), "contexts" : ("contexts", Snmp.Contexts), "correlator" : ("correlator", Snmp.Correlator), "default-community-maps" : ("default_community_maps", Snmp.DefaultCommunityMaps), "encrypted-community-maps" : ("encrypted_community_maps", Snmp.EncryptedCommunityMaps), "groups" : ("groups", Snmp.Groups), "ipv4" : ("ipv4", Snmp.Ipv4), "ipv6" : ("ipv6", Snmp.Ipv6), "logging" : ("logging", Snmp.Logging), "notification" : ("notification", Snmp.Notification), "overload-control" : ("overload_control", Snmp.OverloadControl), "system" : ("system", Snmp.System), "target" : ("target", Snmp.Target), "timeouts" : ("timeouts", Snmp.Timeouts), "trap" : ("trap", Snmp.Trap), "trap-hosts" : ("trap_hosts", Snmp.TrapHosts), "users" : ("users", Snmp.Users), "views" : ("views", Snmp.Views), "vrfs" : ("vrfs", Snmp.Vrfs)}
        self._child_list_classes = {}

        self.inform_pending = YLeaf(YType.uint32, "inform-pending")

        self.inform_retries = YLeaf(YType.uint32, "inform-retries")

        self.inform_timeout = YLeaf(YType.uint32, "inform-timeout")

        self.oid_poll_stats = YLeaf(YType.empty, "oid-poll-stats")

        self.packet_size = YLeaf(YType.uint32, "packet-size")

        self.throttle_time = YLeaf(YType.uint32, "throttle-time")

        self.trap_port = YLeaf(YType.uint32, "trap-port")

        self.trap_source = YLeaf(YType.str, "trap-source")

        self.trap_source_ipv4 = YLeaf(YType.str, "trap-source-ipv4")

        self.trap_source_ipv6 = YLeaf(YType.str, "trap-source-ipv6")

        self.vrf_authentication_trap_disable = YLeaf(YType.empty, "vrf-authentication-trap-disable")

        self.administration = Snmp.Administration()
        self.administration.parent = self
        self._children_name_map["administration"] = "administration"
        self._children_yang_names.add("administration")

        self.agent = Snmp.Agent()
        self.agent.parent = self
        self._children_name_map["agent"] = "agent"
        self._children_yang_names.add("agent")

        self.bulk_stats = Snmp.BulkStats()
        self.bulk_stats.parent = self
        self._children_name_map["bulk_stats"] = "bulk-stats"
        self._children_yang_names.add("bulk-stats")

        self.context_mappings = Snmp.ContextMappings()
        self.context_mappings.parent = self
        self._children_name_map["context_mappings"] = "context-mappings"
        self._children_yang_names.add("context-mappings")

        self.contexts = Snmp.Contexts()
        self.contexts.parent = self
        self._children_name_map["contexts"] = "contexts"
        self._children_yang_names.add("contexts")

        self.correlator = Snmp.Correlator()
        self.correlator.parent = self
        self._children_name_map["correlator"] = "correlator"
        self._children_yang_names.add("correlator")

        self.default_community_maps = Snmp.DefaultCommunityMaps()
        self.default_community_maps.parent = self
        self._children_name_map["default_community_maps"] = "default-community-maps"
        self._children_yang_names.add("default-community-maps")

        self.encrypted_community_maps = Snmp.EncryptedCommunityMaps()
        self.encrypted_community_maps.parent = self
        self._children_name_map["encrypted_community_maps"] = "encrypted-community-maps"
        self._children_yang_names.add("encrypted-community-maps")

        self.groups = Snmp.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"
        self._children_yang_names.add("groups")

        self.ipv4 = Snmp.Ipv4()
        self.ipv4.parent = self
        self._children_name_map["ipv4"] = "ipv4"
        self._children_yang_names.add("ipv4")

        self.ipv6 = Snmp.Ipv6()
        self.ipv6.parent = self
        self._children_name_map["ipv6"] = "ipv6"
        self._children_yang_names.add("ipv6")

        self.logging = Snmp.Logging()
        self.logging.parent = self
        self._children_name_map["logging"] = "logging"
        self._children_yang_names.add("logging")

        self.notification = Snmp.Notification()
        self.notification.parent = self
        self._children_name_map["notification"] = "notification"
        self._children_yang_names.add("notification")

        self.overload_control = None
        self._children_name_map["overload_control"] = "overload-control"
        self._children_yang_names.add("overload-control")

        self.system = Snmp.System()
        self.system.parent = self
        self._children_name_map["system"] = "system"
        self._children_yang_names.add("system")

        self.target = Snmp.Target()
        self.target.parent = self
        self._children_name_map["target"] = "target"
        self._children_yang_names.add("target")

        self.timeouts = Snmp.Timeouts()
        self.timeouts.parent = self
        self._children_name_map["timeouts"] = "timeouts"
        self._children_yang_names.add("timeouts")

        self.trap = Snmp.Trap()
        self.trap.parent = self
        self._children_name_map["trap"] = "trap"
        self._children_yang_names.add("trap")

        self.trap_hosts = Snmp.TrapHosts()
        self.trap_hosts.parent = self
        self._children_name_map["trap_hosts"] = "trap-hosts"
        self._children_yang_names.add("trap-hosts")

        self.users = Snmp.Users()
        self.users.parent = self
        self._children_name_map["users"] = "users"
        self._children_yang_names.add("users")

        self.views = Snmp.Views()
        self.views.parent = self
        self._children_name_map["views"] = "views"
        self._children_yang_names.add("views")

        self.vrfs = Snmp.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp"

    def __setattr__(self, name, value):
        self._perform_setattr(Snmp, ['inform_pending', 'inform_retries', 'inform_timeout', 'oid_poll_stats', 'packet_size', 'throttle_time', 'trap_port', 'trap_source', 'trap_source_ipv4', 'trap_source_ipv6', 'vrf_authentication_trap_disable'], name, value)


    class Administration(Entity):
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
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.Administration, self).__init__()

            self.yang_name = "administration"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"default-communities" : ("default_communities", Snmp.Administration.DefaultCommunities), "encrypted-communities" : ("encrypted_communities", Snmp.Administration.EncryptedCommunities)}
            self._child_list_classes = {}

            self.default_communities = Snmp.Administration.DefaultCommunities()
            self.default_communities.parent = self
            self._children_name_map["default_communities"] = "default-communities"
            self._children_yang_names.add("default-communities")

            self.encrypted_communities = Snmp.Administration.EncryptedCommunities()
            self.encrypted_communities.parent = self
            self._children_name_map["encrypted_communities"] = "encrypted-communities"
            self._children_yang_names.add("encrypted-communities")
            self._segment_path = lambda: "administration"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()


        class DefaultCommunities(Entity):
            """
            Container class to hold unencrpted communities
            
            .. attribute:: default_community
            
            	Unencrpted SNMP community string and access priviledges
            	**type**\: list of    :py:class:`DefaultCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Administration.DefaultCommunities.DefaultCommunity>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Administration.DefaultCommunities, self).__init__()

                self.yang_name = "default-communities"
                self.yang_parent_name = "administration"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"default-community" : ("default_community", Snmp.Administration.DefaultCommunities.DefaultCommunity)}

                self.default_community = YList(self)
                self._segment_path = lambda: "default-communities"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/administration/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Administration.DefaultCommunities, [], name, value)


            class DefaultCommunity(Entity):
                """
                Unencrpted SNMP community string and access
                priviledges
                
                .. attribute:: community_name  <key>
                
                	SNMP community string
                	**type**\:  str
                
                	**length:** 1..128
                
                .. attribute:: owner
                
                	Logical Router or System owner access
                	**type**\:   :py:class:`SnmpOwnerAccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpOwnerAccess>`
                
                .. attribute:: priviledge
                
                	Read/Write Access
                	**type**\:   :py:class:`SnmpAccessLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpAccessLevel>`
                
                .. attribute:: v4_access_list
                
                	Ipv4 Access\-list name
                	**type**\:  str
                
                .. attribute:: v4acl_type
                
                	Access\-list type
                	**type**\:   :py:class:`Snmpacl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmpacl>`
                
                .. attribute:: v6_access_list
                
                	Ipv6 Access\-list name
                	**type**\:  str
                
                .. attribute:: v6acl_type
                
                	Access\-list type
                	**type**\:   :py:class:`Snmpacl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmpacl>`
                
                .. attribute:: view_name
                
                	MIB view to which the community has access
                	**type**\:  str
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Snmp.Administration.DefaultCommunities.DefaultCommunity, self).__init__()

                    self.yang_name = "default-community"
                    self.yang_parent_name = "default-communities"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.community_name = YLeaf(YType.str, "community-name")

                    self.owner = YLeaf(YType.enumeration, "owner")

                    self.priviledge = YLeaf(YType.enumeration, "priviledge")

                    self.v4_access_list = YLeaf(YType.str, "v4-access-list")

                    self.v4acl_type = YLeaf(YType.enumeration, "v4acl-type")

                    self.v6_access_list = YLeaf(YType.str, "v6-access-list")

                    self.v6acl_type = YLeaf(YType.enumeration, "v6acl-type")

                    self.view_name = YLeaf(YType.str, "view-name")
                    self._segment_path = lambda: "default-community" + "[community-name='" + self.community_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/administration/default-communities/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Administration.DefaultCommunities.DefaultCommunity, ['community_name', 'owner', 'priviledge', 'v4_access_list', 'v4acl_type', 'v6_access_list', 'v6acl_type', 'view_name'], name, value)


        class EncryptedCommunities(Entity):
            """
            Container class to hold clear/encrypted
            communities
            
            .. attribute:: encrypted_community
            
            	Clear/encrypted SNMP community string and access priviledges
            	**type**\: list of    :py:class:`EncryptedCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Administration.EncryptedCommunities.EncryptedCommunity>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Administration.EncryptedCommunities, self).__init__()

                self.yang_name = "encrypted-communities"
                self.yang_parent_name = "administration"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"encrypted-community" : ("encrypted_community", Snmp.Administration.EncryptedCommunities.EncryptedCommunity)}

                self.encrypted_community = YList(self)
                self._segment_path = lambda: "encrypted-communities"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/administration/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Administration.EncryptedCommunities, [], name, value)


            class EncryptedCommunity(Entity):
                """
                Clear/encrypted SNMP community string and
                access priviledges
                
                .. attribute:: community_name  <key>
                
                	SNMP community string
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: owner
                
                	Logical Router or System owner access
                	**type**\:   :py:class:`SnmpOwnerAccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpOwnerAccess>`
                
                .. attribute:: priviledge
                
                	Read/Write Access
                	**type**\:   :py:class:`SnmpAccessLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpAccessLevel>`
                
                .. attribute:: v4_access_list
                
                	Ipv4 Access\-list name
                	**type**\:  str
                
                .. attribute:: v4acl_type
                
                	Access\-list type
                	**type**\:   :py:class:`Snmpacl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmpacl>`
                
                .. attribute:: v6_access_list
                
                	Ipv6 Access\-list name
                	**type**\:  str
                
                .. attribute:: v6acl_type
                
                	Access\-list type
                	**type**\:   :py:class:`Snmpacl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmpacl>`
                
                .. attribute:: view_name
                
                	MIB view to which the community has access
                	**type**\:  str
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Snmp.Administration.EncryptedCommunities.EncryptedCommunity, self).__init__()

                    self.yang_name = "encrypted-community"
                    self.yang_parent_name = "encrypted-communities"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.community_name = YLeaf(YType.str, "community-name")

                    self.owner = YLeaf(YType.enumeration, "owner")

                    self.priviledge = YLeaf(YType.enumeration, "priviledge")

                    self.v4_access_list = YLeaf(YType.str, "v4-access-list")

                    self.v4acl_type = YLeaf(YType.enumeration, "v4acl-type")

                    self.v6_access_list = YLeaf(YType.str, "v6-access-list")

                    self.v6acl_type = YLeaf(YType.enumeration, "v6acl-type")

                    self.view_name = YLeaf(YType.str, "view-name")
                    self._segment_path = lambda: "encrypted-community" + "[community-name='" + self.community_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/administration/encrypted-communities/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Administration.EncryptedCommunities.EncryptedCommunity, ['community_name', 'owner', 'priviledge', 'v4_access_list', 'v4acl_type', 'v6_access_list', 'v6acl_type', 'view_name'], name, value)


    class Agent(Entity):
        """
        The heirarchy point for SNMP Agent
        configurations
        
        .. attribute:: engine_id
        
        	SNMPv3 engineID
        	**type**\:   :py:class:`EngineId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Agent.EngineId>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.Agent, self).__init__()

            self.yang_name = "agent"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"engine-id" : ("engine_id", Snmp.Agent.EngineId)}
            self._child_list_classes = {}

            self.engine_id = Snmp.Agent.EngineId()
            self.engine_id.parent = self
            self._children_name_map["engine_id"] = "engine-id"
            self._children_yang_names.add("engine-id")
            self._segment_path = lambda: "agent"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()


        class EngineId(Entity):
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
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Agent.EngineId, self).__init__()

                self.yang_name = "engine-id"
                self.yang_parent_name = "agent"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"remotes" : ("remotes", Snmp.Agent.EngineId.Remotes)}
                self._child_list_classes = {}

                self.local = YLeaf(YType.str, "local")

                self.remotes = Snmp.Agent.EngineId.Remotes()
                self.remotes.parent = self
                self._children_name_map["remotes"] = "remotes"
                self._children_yang_names.add("remotes")
                self._segment_path = lambda: "engine-id"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/agent/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Agent.EngineId, ['local'], name, value)


            class Remotes(Entity):
                """
                SNMPv3 remote SNMP Entity
                
                .. attribute:: remote
                
                	engineID of the remote agent
                	**type**\: list of    :py:class:`Remote <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Agent.EngineId.Remotes.Remote>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Snmp.Agent.EngineId.Remotes, self).__init__()

                    self.yang_name = "remotes"
                    self.yang_parent_name = "engine-id"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"remote" : ("remote", Snmp.Agent.EngineId.Remotes.Remote)}

                    self.remote = YList(self)
                    self._segment_path = lambda: "remotes"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/agent/engine-id/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Agent.EngineId.Remotes, [], name, value)


                class Remote(Entity):
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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Snmp.Agent.EngineId.Remotes.Remote, self).__init__()

                        self.yang_name = "remote"
                        self.yang_parent_name = "remotes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.remote_address = YLeaf(YType.str, "remote-address")

                        self.port = YLeaf(YType.uint16, "port")

                        self.remote_engine_id = YLeaf(YType.str, "remote-engine-id")
                        self._segment_path = lambda: "remote" + "[remote-address='" + self.remote_address.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/agent/engine-id/remotes/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Agent.EngineId.Remotes.Remote, ['remote_address', 'port', 'remote_engine_id'], name, value)


    class BulkStats(Entity):
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
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.BulkStats, self).__init__()

            self.yang_name = "bulk-stats"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"objects" : ("objects", Snmp.BulkStats.Objects), "schemas" : ("schemas", Snmp.BulkStats.Schemas), "transfers" : ("transfers", Snmp.BulkStats.Transfers)}
            self._child_list_classes = {}

            self.memory = YLeaf(YType.uint32, "memory")

            self.objects = Snmp.BulkStats.Objects()
            self.objects.parent = self
            self._children_name_map["objects"] = "objects"
            self._children_yang_names.add("objects")

            self.schemas = Snmp.BulkStats.Schemas()
            self.schemas.parent = self
            self._children_name_map["schemas"] = "schemas"
            self._children_yang_names.add("schemas")

            self.transfers = Snmp.BulkStats.Transfers()
            self.transfers.parent = self
            self._children_name_map["transfers"] = "transfers"
            self._children_yang_names.add("transfers")
            self._segment_path = lambda: "bulk-stats"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.BulkStats, ['memory'], name, value)


        class Objects(Entity):
            """
            Configure an Object List 
            
            .. attribute:: object
            
            	Name of the object List
            	**type**\: list of    :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Objects.Object>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.BulkStats.Objects, self).__init__()

                self.yang_name = "objects"
                self.yang_parent_name = "bulk-stats"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"object" : ("object", Snmp.BulkStats.Objects.Object)}

                self.object = YList(self)
                self._segment_path = lambda: "objects"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/bulk-stats/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.BulkStats.Objects, [], name, value)


            class Object(Entity):
                """
                Name of the object List
                
                .. attribute:: object_list_name  <key>
                
                	Name of the object List
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: objects
                
                	Configure an object List
                	**type**\:   :py:class:`Objects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Objects.Object.Objects>`
                
                .. attribute:: type
                
                	Configure object list name
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Snmp.BulkStats.Objects.Object, self).__init__()

                    self.yang_name = "object"
                    self.yang_parent_name = "objects"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"objects" : ("objects", Snmp.BulkStats.Objects.Object.Objects)}
                    self._child_list_classes = {}

                    self.object_list_name = YLeaf(YType.str, "object-list-name")

                    self.type = YLeaf(YType.empty, "type")

                    self.objects = Snmp.BulkStats.Objects.Object.Objects()
                    self.objects.parent = self
                    self._children_name_map["objects"] = "objects"
                    self._children_yang_names.add("objects")
                    self._segment_path = lambda: "object" + "[object-list-name='" + self.object_list_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/bulk-stats/objects/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.BulkStats.Objects.Object, ['object_list_name', 'type'], name, value)


                class Objects(Entity):
                    """
                    Configure an object List
                    
                    .. attribute:: object
                    
                    	Object name or OID
                    	**type**\: list of    :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Objects.Object.Objects.Object>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Snmp.BulkStats.Objects.Object.Objects, self).__init__()

                        self.yang_name = "objects"
                        self.yang_parent_name = "object"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"object" : ("object", Snmp.BulkStats.Objects.Object.Objects.Object)}

                        self.object = YList(self)
                        self._segment_path = lambda: "objects"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.BulkStats.Objects.Object.Objects, [], name, value)


                    class Object(Entity):
                        """
                        Object name or OID
                        
                        .. attribute:: oid  <key>
                        
                        	Object name or OID 
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Snmp.BulkStats.Objects.Object.Objects.Object, self).__init__()

                            self.yang_name = "object"
                            self.yang_parent_name = "objects"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.oid = YLeaf(YType.str, "oid")
                            self._segment_path = lambda: "object" + "[oid='" + self.oid.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.BulkStats.Objects.Object.Objects.Object, ['oid'], name, value)


        class Schemas(Entity):
            """
            Configure schema definition
            
            .. attribute:: schema
            
            	The name of the Schema
            	**type**\: list of    :py:class:`Schema <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Schemas.Schema>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.BulkStats.Schemas, self).__init__()

                self.yang_name = "schemas"
                self.yang_parent_name = "bulk-stats"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"schema" : ("schema", Snmp.BulkStats.Schemas.Schema)}

                self.schema = YList(self)
                self._segment_path = lambda: "schemas"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/bulk-stats/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.BulkStats.Schemas, [], name, value)


            class Schema(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(Snmp.BulkStats.Schemas.Schema, self).__init__()

                    self.yang_name = "schema"
                    self.yang_parent_name = "schemas"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"instance" : ("instance", Snmp.BulkStats.Schemas.Schema.Instance)}
                    self._child_list_classes = {}

                    self.schema_name = YLeaf(YType.str, "schema-name")

                    self.poll_interval = YLeaf(YType.uint32, "poll-interval")

                    self.schema_object_list = YLeaf(YType.str, "schema-object-list")

                    self.type = YLeaf(YType.empty, "type")

                    self.instance = None
                    self._children_name_map["instance"] = "instance"
                    self._children_yang_names.add("instance")
                    self._segment_path = lambda: "schema" + "[schema-name='" + self.schema_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/bulk-stats/schemas/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.BulkStats.Schemas.Schema, ['schema_name', 'poll_interval', 'schema_object_list', 'type'], name, value)


                class Instance(Entity):
                    """
                    Object instance information
                    
                    .. attribute:: end
                    
                    	End Instance OID for repetition
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: instance
                    
                    	Instance of the schema
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                    	**type**\:   :py:class:`SnmpBulkstatSchema <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpBulkstatSchema>`
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Snmp.BulkStats.Schemas.Schema.Instance, self).__init__()

                        self.yang_name = "instance"
                        self.yang_parent_name = "schema"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.end = YLeaf(YType.str, "end")

                        self.instance = YLeaf(YType.str, "instance")

                        self.max = YLeaf(YType.int32, "max")

                        self.start = YLeaf(YType.str, "start")

                        self.sub_interface = YLeaf(YType.boolean, "sub-interface")

                        self.type = YLeaf(YType.enumeration, "type")
                        self._segment_path = lambda: "instance"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.BulkStats.Schemas.Schema.Instance, ['end', 'instance', 'max', 'start', 'sub_interface', 'type'], name, value)


        class Transfers(Entity):
            """
            Periodicity for the transfer of bulk data in
            minutes
            
            .. attribute:: transfer
            
            	Name of bulk transfer
            	**type**\: list of    :py:class:`Transfer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Transfers.Transfer>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.BulkStats.Transfers, self).__init__()

                self.yang_name = "transfers"
                self.yang_parent_name = "bulk-stats"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"transfer" : ("transfer", Snmp.BulkStats.Transfers.Transfer)}

                self.transfer = YList(self)
                self._segment_path = lambda: "transfers"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/bulk-stats/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.BulkStats.Transfers, [], name, value)


            class Transfer(Entity):
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
                	**type**\:   :py:class:`SnmpBulkstatFileFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpBulkstatFileFormat>`
                
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(Snmp.BulkStats.Transfers.Transfer, self).__init__()

                    self.yang_name = "transfer"
                    self.yang_parent_name = "transfers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"transfer-schemas" : ("transfer_schemas", Snmp.BulkStats.Transfers.Transfer.TransferSchemas)}
                    self._child_list_classes = {}

                    self.transfer_name = YLeaf(YType.str, "transfer-name")

                    self.buffer_size = YLeaf(YType.uint32, "buffer-size")

                    self.enable = YLeaf(YType.empty, "enable")

                    self.format = YLeaf(YType.enumeration, "format")

                    self.interval = YLeaf(YType.int32, "interval")

                    self.primary = YLeaf(YType.str, "primary")

                    self.retain = YLeaf(YType.uint32, "retain")

                    self.retry = YLeaf(YType.uint32, "retry")

                    self.secondary = YLeaf(YType.str, "secondary")

                    self.type = YLeaf(YType.empty, "type")

                    self.transfer_schemas = Snmp.BulkStats.Transfers.Transfer.TransferSchemas()
                    self.transfer_schemas.parent = self
                    self._children_name_map["transfer_schemas"] = "transfer-schemas"
                    self._children_yang_names.add("transfer-schemas")
                    self._segment_path = lambda: "transfer" + "[transfer-name='" + self.transfer_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/bulk-stats/transfers/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.BulkStats.Transfers.Transfer, ['transfer_name', 'buffer_size', 'enable', 'format', 'interval', 'primary', 'retain', 'retry', 'secondary', 'type'], name, value)


                class TransferSchemas(Entity):
                    """
                    Schema that contains objects to be collected
                    
                    .. attribute:: transfer_schema
                    
                    	Schema that contains objects to be collected
                    	**type**\: list of    :py:class:`TransferSchema <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Snmp.BulkStats.Transfers.Transfer.TransferSchemas, self).__init__()

                        self.yang_name = "transfer-schemas"
                        self.yang_parent_name = "transfer"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"transfer-schema" : ("transfer_schema", Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema)}

                        self.transfer_schema = YList(self)
                        self._segment_path = lambda: "transfer-schemas"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.BulkStats.Transfers.Transfer.TransferSchemas, [], name, value)


                    class TransferSchema(Entity):
                        """
                        Schema that contains objects to be collected
                        
                        .. attribute:: schema_name  <key>
                        
                        	Schema that contains objects to be collected
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema, self).__init__()

                            self.yang_name = "transfer-schema"
                            self.yang_parent_name = "transfer-schemas"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.schema_name = YLeaf(YType.str, "schema-name")
                            self._segment_path = lambda: "transfer-schema" + "[schema-name='" + self.schema_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema, ['schema_name'], name, value)


    class ContextMappings(Entity):
        """
        List of context names
        
        .. attribute:: context_mapping
        
        	Context mapping name
        	**type**\: list of    :py:class:`ContextMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.ContextMappings.ContextMapping>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.ContextMappings, self).__init__()

            self.yang_name = "context-mappings"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"context-mapping" : ("context_mapping", Snmp.ContextMappings.ContextMapping)}

            self.context_mapping = YList(self)
            self._segment_path = lambda: "context-mappings"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.ContextMappings, [], name, value)


        class ContextMapping(Entity):
            """
            Context mapping name
            
            .. attribute:: context_mapping_name  <key>
            
            	Context mapping name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: context
            
            	SNMP context feature type
            	**type**\:   :py:class:`SnmpContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpContext>`
            
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
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.ContextMappings.ContextMapping, self).__init__()

                self.yang_name = "context-mapping"
                self.yang_parent_name = "context-mappings"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.context_mapping_name = YLeaf(YType.str, "context-mapping-name")

                self.context = YLeaf(YType.enumeration, "context")

                self.instance_name = YLeaf(YType.str, "instance-name")

                self.topology_name = YLeaf(YType.str, "topology-name")

                self.vrf_name = YLeaf(YType.str, "vrf-name")
                self._segment_path = lambda: "context-mapping" + "[context-mapping-name='" + self.context_mapping_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/context-mappings/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.ContextMappings.ContextMapping, ['context_mapping_name', 'context', 'instance_name', 'topology_name', 'vrf_name'], name, value)


    class Contexts(Entity):
        """
        List of Context Names
        
        .. attribute:: context
        
        	Context Name
        	**type**\: list of    :py:class:`Context <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Contexts.Context>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.Contexts, self).__init__()

            self.yang_name = "contexts"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"context" : ("context", Snmp.Contexts.Context)}

            self.context = YList(self)
            self._segment_path = lambda: "contexts"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Contexts, [], name, value)


        class Context(Entity):
            """
            Context Name
            
            .. attribute:: context_name  <key>
            
            	Context Name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Contexts.Context, self).__init__()

                self.yang_name = "context"
                self.yang_parent_name = "contexts"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.context_name = YLeaf(YType.str, "context-name")
                self._segment_path = lambda: "context" + "[context-name='" + self.context_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/contexts/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Contexts.Context, ['context_name'], name, value)


    class Correlator(Entity):
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
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.Correlator, self).__init__()

            self.yang_name = "correlator"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"rule-sets" : ("rule_sets", Snmp.Correlator.RuleSets), "rules" : ("rules", Snmp.Correlator.Rules)}
            self._child_list_classes = {}

            self.buffer_size = YLeaf(YType.uint32, "buffer-size")

            self.rule_sets = Snmp.Correlator.RuleSets()
            self.rule_sets.parent = self
            self._children_name_map["rule_sets"] = "rule-sets"
            self._children_yang_names.add("rule-sets")

            self.rules = Snmp.Correlator.Rules()
            self.rules.parent = self
            self._children_name_map["rules"] = "rules"
            self._children_yang_names.add("rules")
            self._segment_path = lambda: "correlator"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Correlator, ['buffer_size'], name, value)


        class RuleSets(Entity):
            """
            Table of configured rulesets
            
            .. attribute:: rule_set
            
            	Ruleset name
            	**type**\: list of    :py:class:`RuleSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.RuleSets.RuleSet>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Correlator.RuleSets, self).__init__()

                self.yang_name = "rule-sets"
                self.yang_parent_name = "correlator"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"rule-set" : ("rule_set", Snmp.Correlator.RuleSets.RuleSet)}

                self.rule_set = YList(self)
                self._segment_path = lambda: "rule-sets"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/correlator/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Correlator.RuleSets, [], name, value)


            class RuleSet(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(Snmp.Correlator.RuleSets.RuleSet, self).__init__()

                    self.yang_name = "rule-set"
                    self.yang_parent_name = "rule-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"applied-to" : ("applied_to", Snmp.Correlator.RuleSets.RuleSet.AppliedTo), "rulenames" : ("rulenames", Snmp.Correlator.RuleSets.RuleSet.Rulenames)}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.applied_to = Snmp.Correlator.RuleSets.RuleSet.AppliedTo()
                    self.applied_to.parent = self
                    self._children_name_map["applied_to"] = "applied-to"
                    self._children_yang_names.add("applied-to")

                    self.rulenames = Snmp.Correlator.RuleSets.RuleSet.Rulenames()
                    self.rulenames.parent = self
                    self._children_name_map["rulenames"] = "rulenames"
                    self._children_yang_names.add("rulenames")
                    self._segment_path = lambda: "rule-set" + "[name='" + self.name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/correlator/rule-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Correlator.RuleSets.RuleSet, ['name'], name, value)


                class AppliedTo(Entity):
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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Snmp.Correlator.RuleSets.RuleSet.AppliedTo, self).__init__()

                        self.yang_name = "applied-to"
                        self.yang_parent_name = "rule-set"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"hosts" : ("hosts", Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts)}
                        self._child_list_classes = {}

                        self.all = YLeaf(YType.empty, "all")

                        self.hosts = Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts()
                        self.hosts.parent = self
                        self._children_name_map["hosts"] = "hosts"
                        self._children_yang_names.add("hosts")
                        self._segment_path = lambda: "applied-to"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Correlator.RuleSets.RuleSet.AppliedTo, ['all'], name, value)


                    class Hosts(Entity):
                        """
                        Table of configured hosts to apply rules to
                        
                        .. attribute:: host
                        
                        	A destination host
                        	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts, self).__init__()

                            self.yang_name = "hosts"
                            self.yang_parent_name = "applied-to"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"host" : ("host", Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host)}

                            self.host = YList(self)
                            self._segment_path = lambda: "hosts"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts, [], name, value)


                        class Host(Entity):
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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host, self).__init__()

                                self.yang_name = "host"
                                self.yang_parent_name = "hosts"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ip_address = YLeaf(YType.str, "ip-address")

                                self.port = YLeaf(YType.uint16, "port")
                                self._segment_path = lambda: "host" + "[ip-address='" + self.ip_address.get() + "']" + "[port='" + self.port.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host, ['ip_address', 'port'], name, value)


                class Rulenames(Entity):
                    """
                    Table of configured rulenames
                    
                    .. attribute:: rulename
                    
                    	A rulename
                    	**type**\: list of    :py:class:`Rulename <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Snmp.Correlator.RuleSets.RuleSet.Rulenames, self).__init__()

                        self.yang_name = "rulenames"
                        self.yang_parent_name = "rule-set"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"rulename" : ("rulename", Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename)}

                        self.rulename = YList(self)
                        self._segment_path = lambda: "rulenames"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Correlator.RuleSets.RuleSet.Rulenames, [], name, value)


                    class Rulename(Entity):
                        """
                        A rulename
                        
                        .. attribute:: rulename  <key>
                        
                        	Rule name
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename, self).__init__()

                            self.yang_name = "rulename"
                            self.yang_parent_name = "rulenames"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.rulename = YLeaf(YType.str, "rulename")
                            self._segment_path = lambda: "rulename" + "[rulename='" + self.rulename.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename, ['rulename'], name, value)


        class Rules(Entity):
            """
            Table of configured rules
            
            .. attribute:: rule
            
            	Rule name
            	**type**\: list of    :py:class:`Rule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Correlator.Rules, self).__init__()

                self.yang_name = "rules"
                self.yang_parent_name = "correlator"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"rule" : ("rule", Snmp.Correlator.Rules.Rule)}

                self.rule = YList(self)
                self._segment_path = lambda: "rules"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/correlator/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Correlator.Rules, [], name, value)


            class Rule(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(Snmp.Correlator.Rules.Rule, self).__init__()

                    self.yang_name = "rule"
                    self.yang_parent_name = "rules"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"applied-to" : ("applied_to", Snmp.Correlator.Rules.Rule.AppliedTo), "non-stateful" : ("non_stateful", Snmp.Correlator.Rules.Rule.NonStateful)}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.applied_to = Snmp.Correlator.Rules.Rule.AppliedTo()
                    self.applied_to.parent = self
                    self._children_name_map["applied_to"] = "applied-to"
                    self._children_yang_names.add("applied-to")

                    self.non_stateful = None
                    self._children_name_map["non_stateful"] = "non-stateful"
                    self._children_yang_names.add("non-stateful")
                    self._segment_path = lambda: "rule" + "[name='" + self.name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/correlator/rules/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Correlator.Rules.Rule, ['name'], name, value)


                class AppliedTo(Entity):
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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Snmp.Correlator.Rules.Rule.AppliedTo, self).__init__()

                        self.yang_name = "applied-to"
                        self.yang_parent_name = "rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"hosts" : ("hosts", Snmp.Correlator.Rules.Rule.AppliedTo.Hosts)}
                        self._child_list_classes = {}

                        self.all = YLeaf(YType.empty, "all")

                        self.hosts = Snmp.Correlator.Rules.Rule.AppliedTo.Hosts()
                        self.hosts.parent = self
                        self._children_name_map["hosts"] = "hosts"
                        self._children_yang_names.add("hosts")
                        self._segment_path = lambda: "applied-to"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Correlator.Rules.Rule.AppliedTo, ['all'], name, value)


                    class Hosts(Entity):
                        """
                        Table of configured hosts to apply rules to
                        
                        .. attribute:: host
                        
                        	A destination host
                        	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Snmp.Correlator.Rules.Rule.AppliedTo.Hosts, self).__init__()

                            self.yang_name = "hosts"
                            self.yang_parent_name = "applied-to"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"host" : ("host", Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host)}

                            self.host = YList(self)
                            self._segment_path = lambda: "hosts"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Correlator.Rules.Rule.AppliedTo.Hosts, [], name, value)


                        class Host(Entity):
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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host, self).__init__()

                                self.yang_name = "host"
                                self.yang_parent_name = "hosts"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ip_address = YLeaf(YType.str, "ip-address")

                                self.port = YLeaf(YType.uint16, "port")
                                self._segment_path = lambda: "host" + "[ip-address='" + self.ip_address.get() + "']" + "[port='" + self.port.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host, ['ip_address', 'port'], name, value)


                class NonStateful(Entity):
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
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Snmp.Correlator.Rules.Rule.NonStateful, self).__init__()

                        self.yang_name = "non-stateful"
                        self.yang_parent_name = "rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"non-root-causes" : ("non_root_causes", Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses), "root-causes" : ("root_causes", Snmp.Correlator.Rules.Rule.NonStateful.RootCauses)}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.timeout = YLeaf(YType.uint32, "timeout")

                        self.non_root_causes = Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses()
                        self.non_root_causes.parent = self
                        self._children_name_map["non_root_causes"] = "non-root-causes"
                        self._children_yang_names.add("non-root-causes")

                        self.root_causes = Snmp.Correlator.Rules.Rule.NonStateful.RootCauses()
                        self.root_causes.parent = self
                        self._children_name_map["root_causes"] = "root-causes"
                        self._children_yang_names.add("root-causes")
                        self._segment_path = lambda: "non-stateful"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Correlator.Rules.Rule.NonStateful, ['timeout'], name, value)


                    class NonRootCauses(Entity):
                        """
                        Table of configured non\-rootcause
                        
                        .. attribute:: non_root_cause
                        
                        	A non\-rootcause
                        	**type**\: list of    :py:class:`NonRootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses, self).__init__()

                            self.yang_name = "non-root-causes"
                            self.yang_parent_name = "non-stateful"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"non-root-cause" : ("non_root_cause", Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause)}

                            self.non_root_cause = YList(self)
                            self._segment_path = lambda: "non-root-causes"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses, [], name, value)


                        class NonRootCause(Entity):
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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause, self).__init__()

                                self.yang_name = "non-root-cause"
                                self.yang_parent_name = "non-root-causes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"var-binds" : ("var_binds", Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds)}
                                self._child_list_classes = {}

                                self.oid = YLeaf(YType.str, "oid")

                                self.created = YLeaf(YType.empty, "created")

                                self.var_binds = Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds()
                                self.var_binds.parent = self
                                self._children_name_map["var_binds"] = "var-binds"
                                self._children_yang_names.add("var-binds")
                                self._segment_path = lambda: "non-root-cause" + "[oid='" + self.oid.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause, ['oid', 'created'], name, value)


                            class VarBinds(Entity):
                                """
                                Varbinds to match
                                
                                .. attribute:: var_bind
                                
                                	Varbind match conditions
                                	**type**\: list of    :py:class:`VarBind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind>`
                                
                                

                                """

                                _prefix = 'snmp-agent-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds, self).__init__()

                                    self.yang_name = "var-binds"
                                    self.yang_parent_name = "non-root-cause"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"var-bind" : ("var_bind", Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind)}

                                    self.var_bind = YList(self)
                                    self._segment_path = lambda: "var-binds"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds, [], name, value)


                                class VarBind(Entity):
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
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind, self).__init__()

                                        self.yang_name = "var-bind"
                                        self.yang_parent_name = "var-binds"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"match" : ("match", Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind.Match)}
                                        self._child_list_classes = {}

                                        self.oid = YLeaf(YType.str, "oid")

                                        self.match = Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind.Match()
                                        self.match.parent = self
                                        self._children_name_map["match"] = "match"
                                        self._children_yang_names.add("match")
                                        self._segment_path = lambda: "var-bind" + "[oid='" + self.oid.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind, ['oid'], name, value)


                                    class Match(Entity):
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
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind.Match, self).__init__()

                                            self.yang_name = "match"
                                            self.yang_parent_name = "var-bind"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.index = YLeaf(YType.str, "index")

                                            self.value = YLeaf(YType.str, "value")
                                            self._segment_path = lambda: "match"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind.Match, ['index', 'value'], name, value)


                    class RootCauses(Entity):
                        """
                        Table of configured rootcause (only one
                        entry allowed)
                        
                        .. attribute:: root_cause
                        
                        	The rootcause \- maximum of one can be configured per rule
                        	**type**\: list of    :py:class:`RootCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Snmp.Correlator.Rules.Rule.NonStateful.RootCauses, self).__init__()

                            self.yang_name = "root-causes"
                            self.yang_parent_name = "non-stateful"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"root-cause" : ("root_cause", Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause)}

                            self.root_cause = YList(self)
                            self._segment_path = lambda: "root-causes"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Correlator.Rules.Rule.NonStateful.RootCauses, [], name, value)


                        class RootCause(Entity):
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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause, self).__init__()

                                self.yang_name = "root-cause"
                                self.yang_parent_name = "root-causes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"var-binds" : ("var_binds", Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds)}
                                self._child_list_classes = {}

                                self.oid = YLeaf(YType.str, "oid")

                                self.created = YLeaf(YType.empty, "created")

                                self.var_binds = Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds()
                                self.var_binds.parent = self
                                self._children_name_map["var_binds"] = "var-binds"
                                self._children_yang_names.add("var-binds")
                                self._segment_path = lambda: "root-cause" + "[oid='" + self.oid.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause, ['oid', 'created'], name, value)


                            class VarBinds(Entity):
                                """
                                Varbinds to match
                                
                                .. attribute:: var_bind
                                
                                	Varbind match conditions
                                	**type**\: list of    :py:class:`VarBind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind>`
                                
                                

                                """

                                _prefix = 'snmp-agent-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds, self).__init__()

                                    self.yang_name = "var-binds"
                                    self.yang_parent_name = "root-cause"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"var-bind" : ("var_bind", Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind)}

                                    self.var_bind = YList(self)
                                    self._segment_path = lambda: "var-binds"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds, [], name, value)


                                class VarBind(Entity):
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
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind, self).__init__()

                                        self.yang_name = "var-bind"
                                        self.yang_parent_name = "var-binds"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"match" : ("match", Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind.Match)}
                                        self._child_list_classes = {}

                                        self.oid = YLeaf(YType.str, "oid")

                                        self.match = Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind.Match()
                                        self.match.parent = self
                                        self._children_name_map["match"] = "match"
                                        self._children_yang_names.add("match")
                                        self._segment_path = lambda: "var-bind" + "[oid='" + self.oid.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind, ['oid'], name, value)


                                    class Match(Entity):
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
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind.Match, self).__init__()

                                            self.yang_name = "match"
                                            self.yang_parent_name = "var-bind"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.index = YLeaf(YType.str, "index")

                                            self.value = YLeaf(YType.str, "value")
                                            self._segment_path = lambda: "match"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind.Match, ['index', 'value'], name, value)


    class DefaultCommunityMaps(Entity):
        """
        Container class to hold unencrpted community map
        
        .. attribute:: default_community_map
        
        	Unencrpted SNMP community map name 
        	**type**\: list of    :py:class:`DefaultCommunityMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.DefaultCommunityMaps.DefaultCommunityMap>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.DefaultCommunityMaps, self).__init__()

            self.yang_name = "default-community-maps"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"default-community-map" : ("default_community_map", Snmp.DefaultCommunityMaps.DefaultCommunityMap)}

            self.default_community_map = YList(self)
            self._segment_path = lambda: "default-community-maps"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.DefaultCommunityMaps, [], name, value)


        class DefaultCommunityMap(Entity):
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
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.DefaultCommunityMaps.DefaultCommunityMap, self).__init__()

                self.yang_name = "default-community-map"
                self.yang_parent_name = "default-community-maps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.community_name = YLeaf(YType.str, "community-name")

                self.context = YLeaf(YType.str, "context")

                self.security = YLeaf(YType.str, "security")

                self.target_list = YLeaf(YType.str, "target-list")
                self._segment_path = lambda: "default-community-map" + "[community-name='" + self.community_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/default-community-maps/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.DefaultCommunityMaps.DefaultCommunityMap, ['community_name', 'context', 'security', 'target_list'], name, value)


    class EncryptedCommunityMaps(Entity):
        """
        Container class to hold clear/encrypted
        communitie maps
        
        .. attribute:: encrypted_community_map
        
        	Clear/encrypted SNMP community map
        	**type**\: list of    :py:class:`EncryptedCommunityMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.EncryptedCommunityMaps.EncryptedCommunityMap>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.EncryptedCommunityMaps, self).__init__()

            self.yang_name = "encrypted-community-maps"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"encrypted-community-map" : ("encrypted_community_map", Snmp.EncryptedCommunityMaps.EncryptedCommunityMap)}

            self.encrypted_community_map = YList(self)
            self._segment_path = lambda: "encrypted-community-maps"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.EncryptedCommunityMaps, [], name, value)


        class EncryptedCommunityMap(Entity):
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
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.EncryptedCommunityMaps.EncryptedCommunityMap, self).__init__()

                self.yang_name = "encrypted-community-map"
                self.yang_parent_name = "encrypted-community-maps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.community_name = YLeaf(YType.str, "community-name")

                self.context = YLeaf(YType.str, "context")

                self.security = YLeaf(YType.str, "security")

                self.target_list = YLeaf(YType.str, "target-list")
                self._segment_path = lambda: "encrypted-community-map" + "[community-name='" + self.community_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/encrypted-community-maps/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.EncryptedCommunityMaps.EncryptedCommunityMap, ['community_name', 'context', 'security', 'target_list'], name, value)


    class Groups(Entity):
        """
        Define a User Security Model group
        
        .. attribute:: group
        
        	Name of the group
        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Groups.Group>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"group" : ("group", Snmp.Groups.Group)}

            self.group = YList(self)
            self._segment_path = lambda: "groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Groups, [], name, value)


        class Group(Entity):
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
            	**type**\:   :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
            
            .. attribute:: snmp_version
            
            	snmp version
            	**type**\:   :py:class:`GroupSnmpVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.GroupSnmpVersion>`
            
            	**mandatory**\: True
            
            .. attribute:: v4_access_list
            
            	Ipv4 Access\-list name
            	**type**\:  str
            
            .. attribute:: v4acl_type
            
            	Access\-list type
            	**type**\:   :py:class:`Snmpacl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmpacl>`
            
            .. attribute:: v6_access_list
            
            	Ipv6 Access\-list name
            	**type**\:  str
            
            .. attribute:: v6acl_type
            
            	Access\-list type
            	**type**\:   :py:class:`Snmpacl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmpacl>`
            
            .. attribute:: write_view
            
            	write view name
            	**type**\:  str
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Groups.Group, self).__init__()

                self.yang_name = "group"
                self.yang_parent_name = "groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.context_name = YLeaf(YType.str, "context-name")

                self.notify_view = YLeaf(YType.str, "notify-view")

                self.read_view = YLeaf(YType.str, "read-view")

                self.security_model = YLeaf(YType.enumeration, "security-model")

                self.snmp_version = YLeaf(YType.enumeration, "snmp-version")

                self.v4_access_list = YLeaf(YType.str, "v4-access-list")

                self.v4acl_type = YLeaf(YType.enumeration, "v4acl-type")

                self.v6_access_list = YLeaf(YType.str, "v6-access-list")

                self.v6acl_type = YLeaf(YType.enumeration, "v6acl-type")

                self.write_view = YLeaf(YType.str, "write-view")
                self._segment_path = lambda: "group" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/groups/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Groups.Group, ['name', 'context_name', 'notify_view', 'read_view', 'security_model', 'snmp_version', 'v4_access_list', 'v4acl_type', 'v6_access_list', 'v6acl_type', 'write_view'], name, value)


    class Ipv4(Entity):
        """
        SNMP TOS bit for outgoing packets
        
        .. attribute:: tos
        
        	Type of TOS
        	**type**\:   :py:class:`Tos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Ipv4.Tos>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.Ipv4, self).__init__()

            self.yang_name = "ipv4"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"tos" : ("tos", Snmp.Ipv4.Tos)}
            self._child_list_classes = {}

            self.tos = Snmp.Ipv4.Tos()
            self.tos.parent = self
            self._children_name_map["tos"] = "tos"
            self._children_yang_names.add("tos")
            self._segment_path = lambda: "ipv4"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()


        class Tos(Entity):
            """
            Type of TOS
            
            .. attribute:: dscp
            
            	SNMP DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`SnmpDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpDscpValue>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: precedence
            
            	SNMP Precedence value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`SnmpPrecedenceValue1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpPrecedenceValue1>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: type
            
            	SNMP TOS type DSCP or Precedence
            	**type**\:   :py:class:`SnmpTos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpTos>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Ipv4.Tos, self).__init__()

                self.yang_name = "tos"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.dscp = YLeaf(YType.str, "dscp")

                self.precedence = YLeaf(YType.str, "precedence")

                self.type = YLeaf(YType.enumeration, "type")
                self._segment_path = lambda: "tos"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/ipv4/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Ipv4.Tos, ['dscp', 'precedence', 'type'], name, value)


    class Ipv6(Entity):
        """
        SNMP TOS bit for outgoing packets
        
        .. attribute:: tos
        
        	Type of TOS
        	**type**\:   :py:class:`Tos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Ipv6.Tos>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.Ipv6, self).__init__()

            self.yang_name = "ipv6"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"tos" : ("tos", Snmp.Ipv6.Tos)}
            self._child_list_classes = {}

            self.tos = Snmp.Ipv6.Tos()
            self.tos.parent = self
            self._children_name_map["tos"] = "tos"
            self._children_yang_names.add("tos")
            self._segment_path = lambda: "ipv6"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()


        class Tos(Entity):
            """
            Type of TOS
            
            .. attribute:: dscp
            
            	SNMP DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`SnmpDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpDscpValue>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            .. attribute:: precedence
            
            	SNMP Precedence value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`SnmpPrecedenceValue1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpPrecedenceValue1>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..7
            
            
            ----
            .. attribute:: type
            
            	SNMP TOS type DSCP or Precedence
            	**type**\:   :py:class:`SnmpTos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpTos>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Ipv6.Tos, self).__init__()

                self.yang_name = "tos"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.dscp = YLeaf(YType.str, "dscp")

                self.precedence = YLeaf(YType.str, "precedence")

                self.type = YLeaf(YType.enumeration, "type")
                self._segment_path = lambda: "tos"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/ipv6/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Ipv6.Tos, ['dscp', 'precedence', 'type'], name, value)


    class Logging(Entity):
        """
        SNMP logging
        
        .. attribute:: threshold
        
        	SNMP logging threshold
        	**type**\:   :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Logging.Threshold>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.Logging, self).__init__()

            self.yang_name = "logging"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"threshold" : ("threshold", Snmp.Logging.Threshold)}
            self._child_list_classes = {}

            self.threshold = Snmp.Logging.Threshold()
            self.threshold.parent = self
            self._children_name_map["threshold"] = "threshold"
            self._children_yang_names.add("threshold")
            self._segment_path = lambda: "logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()


        class Threshold(Entity):
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
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Logging.Threshold, self).__init__()

                self.yang_name = "threshold"
                self.yang_parent_name = "logging"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.oid_processing = YLeaf(YType.uint32, "oid-processing")

                self.pdu_processing = YLeaf(YType.uint32, "pdu-processing")
                self._segment_path = lambda: "threshold"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/logging/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Logging.Threshold, ['oid_processing', 'pdu_processing'], name, value)


    class Notification(Entity):
        """
        Enable SNMP notifications
        
        .. attribute:: addresspool_mib
        
        	Enable SNMP daps traps
        	**type**\:   :py:class:`AddresspoolMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.AddresspoolMib>`
        
        .. attribute:: bfd
        
        	CISCO\-IETF\-BFD\-MIB notification configuration
        	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Bfd>`
        
        .. attribute:: bgp
        
        	BGP4\-MIB and CISCO\-BGP4\-MIB notification configuration
        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Bgp>`
        
        .. attribute:: bridge
        
        	BRIDGE\-MIB notification configuration
        	**type**\:   :py:class:`Bridge <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Bridge>`
        
        .. attribute:: cfm
        
        	802.1ag Connectivity Fault Management MIB notification configuration
        	**type**\:   :py:class:`Cfm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Cfm>`
        
        .. attribute:: cisco_ios_xr_freqsync_cfg_frequency_synchronization
        
        	Frequency Synchronization trap configuration
        	**type**\:   :py:class:`CiscoIOSXRFreqsyncCfgFrequencySynchronization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.CiscoIOSXRFreqsyncCfgFrequencySynchronization>`
        
        .. attribute:: cisco_ios_xr_ncs4k_freqsync_cfg_frequency_synchronization
        
        	Frequency Synchronization trap configuration
        	**type**\:   :py:class:`CiscoIOSXRNcs4KFreqsyncCfgFrequencySynchronization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.CiscoIOSXRNcs4KFreqsyncCfgFrequencySynchronization>`
        
        .. attribute:: config_copy
        
        	CISCO\-CONFIG\-COPY\-MIB notification configuration
        	**type**\:   :py:class:`ConfigCopy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.ConfigCopy>`
        
        .. attribute:: config_man
        
        	CISCO\-CONFIG\-MAN\-MIB notification configurations
        	**type**\:   :py:class:`ConfigMan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.ConfigMan>`
        
        .. attribute:: diametermib
        
        	Enable SNMP diameter traps
        	**type**\:   :py:class:`Diametermib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Diametermib>`
        
        .. attribute:: entity_
        
        	Enable ENTITY\-MIB notifications
        	**type**\:   :py:class:`Entity_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Entity_>`
        
        .. attribute:: entity_redundancy
        
        	CISCO\-ENTITY\-REDUNDANCY\-MIB notification configuration
        	**type**\:   :py:class:`EntityRedundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.EntityRedundancy>`
        
        .. attribute:: entity_state
        
        	ENTITY\-STATE\-MIB notification configuration
        	**type**\:   :py:class:`EntityState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.EntityState>`
        
        .. attribute:: fabric_crs
        
        	CISCO\-FABRIC\-HFR\-MIB notification configuration
        	**type**\:   :py:class:`FabricCrs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.FabricCrs>`
        
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
        
        .. attribute:: l2tun
        
        	Enable SNMP l2tun traps
        	**type**\:   :py:class:`L2Tun <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.L2Tun>`
        
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
        
        .. attribute:: optical
        
        	CISCO\-OPTICAL\-MIB notification configuration
        	**type**\:   :py:class:`Optical <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Optical>`
        
        .. attribute:: optical_ots
        
        	CISCO\-OPTICAL\-OTS\-MIB notification configuration
        	**type**\:   :py:class:`OpticalOts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.OpticalOts>`
        
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
        	**type**\:   :py:class:`Snmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.Snmp>`
        
        .. attribute:: subscriber_mib
        
        	Subscriber notification commands
        	**type**\:   :py:class:`SubscriberMib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.SubscriberMib>`
        
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
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.Notification, self).__init__()

            self.yang_name = "notification"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"addresspool-mib" : ("addresspool_mib", Snmp.Notification.AddresspoolMib), "bfd" : ("bfd", Snmp.Notification.Bfd), "bgp" : ("bgp", Snmp.Notification.Bgp), "bridge" : ("bridge", Snmp.Notification.Bridge), "cfm" : ("cfm", Snmp.Notification.Cfm), "Cisco-IOS-XR-freqsync-cfg_frequency-synchronization" : ("cisco_ios_xr_freqsync_cfg_frequency_synchronization", Snmp.Notification.CiscoIOSXRFreqsyncCfgFrequencySynchronization), "Cisco-IOS-XR-ncs4k-freqsync-cfg_frequency-synchronization" : ("cisco_ios_xr_ncs4k_freqsync_cfg_frequency_synchronization", Snmp.Notification.CiscoIOSXRNcs4KFreqsyncCfgFrequencySynchronization), "config-copy" : ("config_copy", Snmp.Notification.ConfigCopy), "config-man" : ("config_man", Snmp.Notification.ConfigMan), "diametermib" : ("diametermib", Snmp.Notification.Diametermib), "entity" : ("entity_", Snmp.Notification.Entity_), "entity-redundancy" : ("entity_redundancy", Snmp.Notification.EntityRedundancy), "entity-state" : ("entity_state", Snmp.Notification.EntityState), "fabric-crs" : ("fabric_crs", Snmp.Notification.FabricCrs), "flash" : ("flash", Snmp.Notification.Flash), "fru-control" : ("fru_control", Snmp.Notification.FruControl), "hsrp" : ("hsrp", Snmp.Notification.Hsrp), "isis" : ("isis", Snmp.Notification.Isis), "l2tun" : ("l2tun", Snmp.Notification.L2Tun), "l2vpn" : ("l2vpn", Snmp.Notification.L2Vpn), "mpls-frr" : ("mpls_frr", Snmp.Notification.MplsFrr), "mpls-l3vpn" : ("mpls_l3vpn", Snmp.Notification.MplsL3Vpn), "mpls-ldp" : ("mpls_ldp", Snmp.Notification.MplsLdp), "mpls-te" : ("mpls_te", Snmp.Notification.MplsTe), "mpls-te-p2mp" : ("mpls_te_p2mp", Snmp.Notification.MplsTeP2Mp), "ntp" : ("ntp", Snmp.Notification.Ntp), "oam" : ("oam", Snmp.Notification.Oam), "optical" : ("optical", Snmp.Notification.Optical), "optical-ots" : ("optical_ots", Snmp.Notification.OpticalOts), "ospf" : ("ospf", Snmp.Notification.Ospf), "ospfv3" : ("ospfv3", Snmp.Notification.Ospfv3), "otn" : ("otn", Snmp.Notification.Otn), "rf" : ("rf", Snmp.Notification.Rf), "rsvp" : ("rsvp", Snmp.Notification.Rsvp), "selective-vrf-download" : ("selective_vrf_download", Snmp.Notification.SelectiveVrfDownload), "sensor" : ("sensor", Snmp.Notification.Sensor), "snmp" : ("snmp", Snmp.Notification.Snmp), "subscriber-mib" : ("subscriber_mib", Snmp.Notification.SubscriberMib), "syslog" : ("syslog", Snmp.Notification.Syslog), "system" : ("system", Snmp.Notification.System), "vpls" : ("vpls", Snmp.Notification.Vpls), "vrrp" : ("vrrp", Snmp.Notification.Vrrp)}
            self._child_list_classes = {}

            self.addresspool_mib = Snmp.Notification.AddresspoolMib()
            self.addresspool_mib.parent = self
            self._children_name_map["addresspool_mib"] = "addresspool-mib"
            self._children_yang_names.add("addresspool-mib")

            self.bfd = Snmp.Notification.Bfd()
            self.bfd.parent = self
            self._children_name_map["bfd"] = "bfd"
            self._children_yang_names.add("bfd")

            self.bgp = Snmp.Notification.Bgp()
            self.bgp.parent = self
            self._children_name_map["bgp"] = "bgp"
            self._children_yang_names.add("bgp")

            self.bridge = Snmp.Notification.Bridge()
            self.bridge.parent = self
            self._children_name_map["bridge"] = "bridge"
            self._children_yang_names.add("bridge")

            self.cfm = Snmp.Notification.Cfm()
            self.cfm.parent = self
            self._children_name_map["cfm"] = "cfm"
            self._children_yang_names.add("cfm")

            self.cisco_ios_xr_freqsync_cfg_frequency_synchronization = Snmp.Notification.CiscoIOSXRFreqsyncCfgFrequencySynchronization()
            self.cisco_ios_xr_freqsync_cfg_frequency_synchronization.parent = self
            self._children_name_map["cisco_ios_xr_freqsync_cfg_frequency_synchronization"] = "Cisco-IOS-XR-freqsync-cfg_frequency-synchronization"
            self._children_yang_names.add("Cisco-IOS-XR-freqsync-cfg_frequency-synchronization")

            self.cisco_ios_xr_ncs4k_freqsync_cfg_frequency_synchronization = Snmp.Notification.CiscoIOSXRNcs4KFreqsyncCfgFrequencySynchronization()
            self.cisco_ios_xr_ncs4k_freqsync_cfg_frequency_synchronization.parent = self
            self._children_name_map["cisco_ios_xr_ncs4k_freqsync_cfg_frequency_synchronization"] = "Cisco-IOS-XR-ncs4k-freqsync-cfg_frequency-synchronization"
            self._children_yang_names.add("Cisco-IOS-XR-ncs4k-freqsync-cfg_frequency-synchronization")

            self.config_copy = Snmp.Notification.ConfigCopy()
            self.config_copy.parent = self
            self._children_name_map["config_copy"] = "config-copy"
            self._children_yang_names.add("config-copy")

            self.config_man = Snmp.Notification.ConfigMan()
            self.config_man.parent = self
            self._children_name_map["config_man"] = "config-man"
            self._children_yang_names.add("config-man")

            self.diametermib = Snmp.Notification.Diametermib()
            self.diametermib.parent = self
            self._children_name_map["diametermib"] = "diametermib"
            self._children_yang_names.add("diametermib")

            self.entity_ = Snmp.Notification.Entity_()
            self.entity_.parent = self
            self._children_name_map["entity_"] = "entity"
            self._children_yang_names.add("entity")

            self.entity_redundancy = Snmp.Notification.EntityRedundancy()
            self.entity_redundancy.parent = self
            self._children_name_map["entity_redundancy"] = "entity-redundancy"
            self._children_yang_names.add("entity-redundancy")

            self.entity_state = Snmp.Notification.EntityState()
            self.entity_state.parent = self
            self._children_name_map["entity_state"] = "entity-state"
            self._children_yang_names.add("entity-state")

            self.fabric_crs = Snmp.Notification.FabricCrs()
            self.fabric_crs.parent = self
            self._children_name_map["fabric_crs"] = "fabric-crs"
            self._children_yang_names.add("fabric-crs")

            self.flash = Snmp.Notification.Flash()
            self.flash.parent = self
            self._children_name_map["flash"] = "flash"
            self._children_yang_names.add("flash")

            self.fru_control = Snmp.Notification.FruControl()
            self.fru_control.parent = self
            self._children_name_map["fru_control"] = "fru-control"
            self._children_yang_names.add("fru-control")

            self.hsrp = Snmp.Notification.Hsrp()
            self.hsrp.parent = self
            self._children_name_map["hsrp"] = "hsrp"
            self._children_yang_names.add("hsrp")

            self.isis = Snmp.Notification.Isis()
            self.isis.parent = self
            self._children_name_map["isis"] = "isis"
            self._children_yang_names.add("isis")

            self.l2tun = Snmp.Notification.L2Tun()
            self.l2tun.parent = self
            self._children_name_map["l2tun"] = "l2tun"
            self._children_yang_names.add("l2tun")

            self.l2vpn = Snmp.Notification.L2Vpn()
            self.l2vpn.parent = self
            self._children_name_map["l2vpn"] = "l2vpn"
            self._children_yang_names.add("l2vpn")

            self.mpls_frr = Snmp.Notification.MplsFrr()
            self.mpls_frr.parent = self
            self._children_name_map["mpls_frr"] = "mpls-frr"
            self._children_yang_names.add("mpls-frr")

            self.mpls_l3vpn = Snmp.Notification.MplsL3Vpn()
            self.mpls_l3vpn.parent = self
            self._children_name_map["mpls_l3vpn"] = "mpls-l3vpn"
            self._children_yang_names.add("mpls-l3vpn")

            self.mpls_ldp = Snmp.Notification.MplsLdp()
            self.mpls_ldp.parent = self
            self._children_name_map["mpls_ldp"] = "mpls-ldp"
            self._children_yang_names.add("mpls-ldp")

            self.mpls_te = Snmp.Notification.MplsTe()
            self.mpls_te.parent = self
            self._children_name_map["mpls_te"] = "mpls-te"
            self._children_yang_names.add("mpls-te")

            self.mpls_te_p2mp = Snmp.Notification.MplsTeP2Mp()
            self.mpls_te_p2mp.parent = self
            self._children_name_map["mpls_te_p2mp"] = "mpls-te-p2mp"
            self._children_yang_names.add("mpls-te-p2mp")

            self.ntp = Snmp.Notification.Ntp()
            self.ntp.parent = self
            self._children_name_map["ntp"] = "ntp"
            self._children_yang_names.add("ntp")

            self.oam = Snmp.Notification.Oam()
            self.oam.parent = self
            self._children_name_map["oam"] = "oam"
            self._children_yang_names.add("oam")

            self.optical = Snmp.Notification.Optical()
            self.optical.parent = self
            self._children_name_map["optical"] = "optical"
            self._children_yang_names.add("optical")

            self.optical_ots = Snmp.Notification.OpticalOts()
            self.optical_ots.parent = self
            self._children_name_map["optical_ots"] = "optical-ots"
            self._children_yang_names.add("optical-ots")

            self.ospf = Snmp.Notification.Ospf()
            self.ospf.parent = self
            self._children_name_map["ospf"] = "ospf"
            self._children_yang_names.add("ospf")

            self.ospfv3 = Snmp.Notification.Ospfv3()
            self.ospfv3.parent = self
            self._children_name_map["ospfv3"] = "ospfv3"
            self._children_yang_names.add("ospfv3")

            self.otn = Snmp.Notification.Otn()
            self.otn.parent = self
            self._children_name_map["otn"] = "otn"
            self._children_yang_names.add("otn")

            self.rf = Snmp.Notification.Rf()
            self.rf.parent = self
            self._children_name_map["rf"] = "rf"
            self._children_yang_names.add("rf")

            self.rsvp = Snmp.Notification.Rsvp()
            self.rsvp.parent = self
            self._children_name_map["rsvp"] = "rsvp"
            self._children_yang_names.add("rsvp")

            self.selective_vrf_download = Snmp.Notification.SelectiveVrfDownload()
            self.selective_vrf_download.parent = self
            self._children_name_map["selective_vrf_download"] = "selective-vrf-download"
            self._children_yang_names.add("selective-vrf-download")

            self.sensor = Snmp.Notification.Sensor()
            self.sensor.parent = self
            self._children_name_map["sensor"] = "sensor"
            self._children_yang_names.add("sensor")

            self.snmp = Snmp.Notification.Snmp()
            self.snmp.parent = self
            self._children_name_map["snmp"] = "snmp"
            self._children_yang_names.add("snmp")

            self.subscriber_mib = Snmp.Notification.SubscriberMib()
            self.subscriber_mib.parent = self
            self._children_name_map["subscriber_mib"] = "subscriber-mib"
            self._children_yang_names.add("subscriber-mib")

            self.syslog = Snmp.Notification.Syslog()
            self.syslog.parent = self
            self._children_name_map["syslog"] = "syslog"
            self._children_yang_names.add("syslog")

            self.system = Snmp.Notification.System()
            self.system.parent = self
            self._children_name_map["system"] = "system"
            self._children_yang_names.add("system")

            self.vpls = Snmp.Notification.Vpls()
            self.vpls.parent = self
            self._children_name_map["vpls"] = "vpls"
            self._children_yang_names.add("vpls")

            self.vrrp = Snmp.Notification.Vrrp()
            self.vrrp.parent = self
            self._children_name_map["vrrp"] = "vrrp"
            self._children_yang_names.add("vrrp")
            self._segment_path = lambda: "notification"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()


        class AddresspoolMib(Entity):
            """
            Enable SNMP daps traps
            
            .. attribute:: high
            
            	Enable SNMP Address Pool High Threshold trap
            	**type**\:  bool
            
            .. attribute:: low
            
            	Enable SNMP Address Pool Low Threshold trap
            	**type**\:  bool
            
            

            """

            _prefix = 'ip-daps-mib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Snmp.Notification.AddresspoolMib, self).__init__()

                self.yang_name = "addresspool-mib"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.high = YLeaf(YType.boolean, "high")

                self.low = YLeaf(YType.boolean, "low")
                self._segment_path = lambda: "Cisco-IOS-XR-ip-daps-mib-cfg:addresspool-mib"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.AddresspoolMib, ['high', 'low'], name, value)


        class Bfd(Entity):
            """
            CISCO\-IETF\-BFD\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable CISCO\-IETF\-BFD\-MIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Snmp.Notification.Bfd, self).__init__()

                self.yang_name = "bfd"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-ip-bfd-cfg:bfd"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Bfd, ['enable'], name, value)


        class Bgp(Entity):
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
            _revision = '2017-06-26'

            def __init__(self):
                super(Snmp.Notification.Bgp, self).__init__()

                self.yang_name = "bgp"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"bgp4mib" : ("bgp4mib", Snmp.Notification.Bgp.Bgp4Mib), "cisco-bgp4mib" : ("cisco_bgp4mib", Snmp.Notification.Bgp.CiscoBgp4Mib)}
                self._child_list_classes = {}

                self.bgp4mib = Snmp.Notification.Bgp.Bgp4Mib()
                self.bgp4mib.parent = self
                self._children_name_map["bgp4mib"] = "bgp4mib"
                self._children_yang_names.add("bgp4mib")

                self.cisco_bgp4mib = Snmp.Notification.Bgp.CiscoBgp4Mib()
                self.cisco_bgp4mib.parent = self
                self._children_name_map["cisco_bgp4mib"] = "cisco-bgp4mib"
                self._children_yang_names.add("cisco-bgp4mib")
                self._segment_path = lambda: "Cisco-IOS-XR-ipv4-bgp-cfg:bgp"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()


            class Bgp4Mib(Entity):
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
                _revision = '2017-06-26'

                def __init__(self):
                    super(Snmp.Notification.Bgp.Bgp4Mib, self).__init__()

                    self.yang_name = "bgp4mib"
                    self.yang_parent_name = "bgp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.enable = YLeaf(YType.empty, "enable")

                    self.up_down = YLeaf(YType.empty, "up-down")
                    self._segment_path = lambda: "bgp4mib"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-ipv4-bgp-cfg:bgp/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.Bgp.Bgp4Mib, ['enable', 'up_down'], name, value)


            class CiscoBgp4Mib(Entity):
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
                _revision = '2017-06-26'

                def __init__(self):
                    super(Snmp.Notification.Bgp.CiscoBgp4Mib, self).__init__()

                    self.yang_name = "cisco-bgp4mib"
                    self.yang_parent_name = "bgp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.enable = YLeaf(YType.empty, "enable")

                    self.up_down = YLeaf(YType.empty, "up-down")
                    self._segment_path = lambda: "cisco-bgp4mib"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-ipv4-bgp-cfg:bgp/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.Bgp.CiscoBgp4Mib, ['enable', 'up_down'], name, value)


        class Bridge(Entity):
            """
            BRIDGE\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable dot1dBridge notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-bridgemib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Snmp.Notification.Bridge, self).__init__()

                self.yang_name = "bridge"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-snmp-bridgemib-cfg:bridge"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Bridge, ['enable'], name, value)


        class Cfm(Entity):
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
                super(Snmp.Notification.Cfm, self).__init__()

                self.yang_name = "cfm"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-ethernet-cfm-cfg:cfm"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Cfm, ['enable'], name, value)


        class CiscoIOSXRFreqsyncCfgFrequencySynchronization(Entity):
            """
            Frequency Synchronization trap configuration
            
            .. attribute:: enable
            
            	Enable Frequency Synchronization traps
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'freqsync-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Snmp.Notification.CiscoIOSXRFreqsyncCfgFrequencySynchronization, self).__init__()

                self.yang_name = "Cisco-IOS-XR-freqsync-cfg_frequency-synchronization"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-freqsync-cfg:Cisco-IOS-XR-freqsync-cfg_frequency-synchronization"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.CiscoIOSXRFreqsyncCfgFrequencySynchronization, ['enable'], name, value)


        class CiscoIOSXRNcs4KFreqsyncCfgFrequencySynchronization(Entity):
            """
            Frequency Synchronization trap configuration
            
            .. attribute:: enable
            
            	Enable Frequency Synchronization traps
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ncs4k-freqsync-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Snmp.Notification.CiscoIOSXRNcs4KFreqsyncCfgFrequencySynchronization, self).__init__()

                self.yang_name = "Cisco-IOS-XR-ncs4k-freqsync-cfg_frequency-synchronization"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-ncs4k-freqsync-cfg:Cisco-IOS-XR-ncs4k-freqsync-cfg_frequency-synchronization"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.CiscoIOSXRNcs4KFreqsyncCfgFrequencySynchronization, ['enable'], name, value)


        class ConfigCopy(Entity):
            """
            CISCO\-CONFIG\-COPY\-MIB notification configuration
            
            .. attribute:: completion
            
            	Enable ccCopyCompletion notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-confcopymib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Snmp.Notification.ConfigCopy, self).__init__()

                self.yang_name = "config-copy"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.completion = YLeaf(YType.empty, "completion")
                self._segment_path = lambda: "Cisco-IOS-XR-infra-confcopymib-cfg:config-copy"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.ConfigCopy, ['completion'], name, value)


        class ConfigMan(Entity):
            """
            CISCO\-CONFIG\-MAN\-MIB notification configurations
            
            .. attribute:: enable
            
            	Enable ciscoConfigManMIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'config-mibs-cfg'
            _revision = '2015-09-29'

            def __init__(self):
                super(Snmp.Notification.ConfigMan, self).__init__()

                self.yang_name = "config-man"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-config-mibs-cfg:config-man"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.ConfigMan, ['enable'], name, value)


        class Diametermib(Entity):
            """
            Enable SNMP diameter traps
            
            .. attribute:: peerdown
            
            	Enable SNMP diameter peer connection down notification
            	**type**\:  bool
            
            .. attribute:: peerup
            
            	Enable SNMP diameter peer connection up notification
            	**type**\:  bool
            
            .. attribute:: permanentfail
            
            	Enable SNMP diameter permanent failure notification
            	**type**\:  bool
            
            .. attribute:: protocolerror
            
            	Enable SNMP diameter protocol error notification
            	**type**\:  bool
            
            .. attribute:: transientfail
            
            	Enable SNMP diameter transient failure notification
            	**type**\:  bool
            
            

            """

            _prefix = 'aaa-diameter-base-mib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Snmp.Notification.Diametermib, self).__init__()

                self.yang_name = "diametermib"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.peerdown = YLeaf(YType.boolean, "peerdown")

                self.peerup = YLeaf(YType.boolean, "peerup")

                self.permanentfail = YLeaf(YType.boolean, "permanentfail")

                self.protocolerror = YLeaf(YType.boolean, "protocolerror")

                self.transientfail = YLeaf(YType.boolean, "transientfail")
                self._segment_path = lambda: "Cisco-IOS-XR-aaa-diameter-base-mib-cfg:diametermib"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Diametermib, ['peerdown', 'peerup', 'permanentfail', 'protocolerror', 'transientfail'], name, value)


        class EntityRedundancy(Entity):
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
                super(Snmp.Notification.EntityRedundancy, self).__init__()

                self.yang_name = "entity-redundancy"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")

                self.status = YLeaf(YType.empty, "status")

                self.switchover = YLeaf(YType.empty, "switchover")
                self._segment_path = lambda: "Cisco-IOS-XR-infra-ceredundancymib-cfg:entity-redundancy"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.EntityRedundancy, ['enable', 'status', 'switchover'], name, value)


        class EntityState(Entity):
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
                super(Snmp.Notification.EntityState, self).__init__()

                self.yang_name = "entity-state"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.oper_status = YLeaf(YType.empty, "oper-status")

                self.switchover = YLeaf(YType.empty, "switchover")
                self._segment_path = lambda: "Cisco-IOS-XR-snmp-entstatemib-cfg:entity-state"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.EntityState, ['oper_status', 'switchover'], name, value)


        class Entity_(Entity):
            """
            Enable ENTITY\-MIB notifications
            
            .. attribute:: enable
            
            	Enable entityMIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-entitymib-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Notification.Entity_, self).__init__()

                self.yang_name = "entity"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-snmp-entitymib-cfg:entity"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Entity_, ['enable'], name, value)


        class FabricCrs(Entity):
            """
            CISCO\-FABRIC\-HFR\-MIB notification configuration
            
            .. attribute:: bundle_downed_link
            
            	Enable cfhBundleDownedLinkNotification notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: bundle_state
            
            	Enable cfhBundleStateNotification notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: plane_state
            
            	Enable cfhPlaneStateNotification notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'fabhfr-mib-cfg'
            _revision = '2017-05-31'

            def __init__(self):
                super(Snmp.Notification.FabricCrs, self).__init__()

                self.yang_name = "fabric-crs"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.bundle_downed_link = YLeaf(YType.empty, "bundle-downed-link")

                self.bundle_state = YLeaf(YType.empty, "bundle-state")

                self.plane_state = YLeaf(YType.empty, "plane-state")
                self._segment_path = lambda: "Cisco-IOS-XR-fabhfr-mib-cfg:fabric-crs"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.FabricCrs, ['bundle_downed_link', 'bundle_state', 'plane_state'], name, value)


        class Flash(Entity):
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
                super(Snmp.Notification.Flash, self).__init__()

                self.yang_name = "flash"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.insertion = YLeaf(YType.empty, "insertion")

                self.removal = YLeaf(YType.empty, "removal")
                self._segment_path = lambda: "Cisco-IOS-XR-flashmib-cfg:flash"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Flash, ['insertion', 'removal'], name, value)


        class FruControl(Entity):
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
                super(Snmp.Notification.FruControl, self).__init__()

                self.yang_name = "fru-control"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-snmp-frucontrolmib-cfg:fru-control"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.FruControl, ['enable'], name, value)


        class Hsrp(Entity):
            """
            CISCO\-HSRP\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable CISCO\-HSRP\-MIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ipv4-hsrp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Notification.Hsrp, self).__init__()

                self.yang_name = "hsrp"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Hsrp, ['enable'], name, value)


        class Isis(Entity):
            """
            Enable ISIS\-MIB notifications
            
            .. attribute:: adjacency_change
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibAdjacencyChangeBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAdjacencyChangeBoolean>`
            
            	**default value**\: false
            
            .. attribute:: all
            
            	Enable all isisMIB notifications
            	**type**\:   :py:class:`IsisMibAllBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAllBoolean>`
            
            	**default value**\: false
            
            .. attribute:: area_mismatch
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibAreaMismatchBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAreaMismatchBoolean>`
            
            	**default value**\: false
            
            .. attribute:: attempt_to_exceed_max_sequence
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibAttemptToExceedMaxSequenceBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAttemptToExceedMaxSequenceBoolean>`
            
            	**default value**\: false
            
            .. attribute:: authentication_failure
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibAuthenticationFailureBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAuthenticationFailureBoolean>`
            
            	**default value**\: false
            
            .. attribute:: authentication_type_failure
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibAuthenticationTypeFailureBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibAuthenticationTypeFailureBoolean>`
            
            	**default value**\: false
            
            .. attribute:: corrupted_lsp_detected
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibCorruptedLspDetectedBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibCorruptedLspDetectedBoolean>`
            
            	**default value**\: false
            
            .. attribute:: database_overflow
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibDatabaseOverFlowBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibDatabaseOverFlowBoolean>`
            
            	**default value**\: false
            
            .. attribute:: id_length_mismatch
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibIdLengthMismatchBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibIdLengthMismatchBoolean>`
            
            	**default value**\: false
            
            .. attribute:: lsp_error_detected
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibLspErrorDetectedBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibLspErrorDetectedBoolean>`
            
            	**default value**\: false
            
            .. attribute:: lsp_too_large_to_propagate
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibLspTooLargeToPropagateBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibLspTooLargeToPropagateBoolean>`
            
            	**default value**\: false
            
            .. attribute:: manual_address_drops
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibManualAddressDropsBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibManualAddressDropsBoolean>`
            
            	**default value**\: false
            
            .. attribute:: max_area_address_mismatch
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibMaxAreaAddressMismatchBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibMaxAreaAddressMismatchBoolean>`
            
            	**default value**\: false
            
            .. attribute:: originated_lsp_buffer_size_mismatch
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibOriginatedLspBufferSizeMismatchBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibOriginatedLspBufferSizeMismatchBoolean>`
            
            	**default value**\: false
            
            .. attribute:: own_lsp_purge
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibOwnLspPurgeBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibOwnLspPurgeBoolean>`
            
            	**default value**\: false
            
            .. attribute:: protocols_supported_mismatch
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibProtocolsSupportedMismatchBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibProtocolsSupportedMismatchBoolean>`
            
            	**default value**\: false
            
            .. attribute:: rejected_adjacency
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibRejectedAdjacencyBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibRejectedAdjacencyBoolean>`
            
            	**default value**\: false
            
            .. attribute:: sequence_number_skip
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibSequenceNumberSkipBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibSequenceNumberSkipBoolean>`
            
            	**default value**\: false
            
            .. attribute:: version_skew
            
            	Enable or disable
            	**type**\:   :py:class:`IsisMibVersionSkewBoolean <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMibVersionSkewBoolean>`
            
            	**default value**\: false
            
            

            """

            _prefix = 'clns-isis-cfg'
            _revision = '2017-06-02'

            def __init__(self):
                super(Snmp.Notification.Isis, self).__init__()

                self.yang_name = "isis"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.adjacency_change = YLeaf(YType.enumeration, "adjacency-change")

                self.all = YLeaf(YType.enumeration, "all")

                self.area_mismatch = YLeaf(YType.enumeration, "area-mismatch")

                self.attempt_to_exceed_max_sequence = YLeaf(YType.enumeration, "attempt-to-exceed-max-sequence")

                self.authentication_failure = YLeaf(YType.enumeration, "authentication-failure")

                self.authentication_type_failure = YLeaf(YType.enumeration, "authentication-type-failure")

                self.corrupted_lsp_detected = YLeaf(YType.enumeration, "corrupted-lsp-detected")

                self.database_overflow = YLeaf(YType.enumeration, "database-overflow")

                self.id_length_mismatch = YLeaf(YType.enumeration, "id-length-mismatch")

                self.lsp_error_detected = YLeaf(YType.enumeration, "lsp-error-detected")

                self.lsp_too_large_to_propagate = YLeaf(YType.enumeration, "lsp-too-large-to-propagate")

                self.manual_address_drops = YLeaf(YType.enumeration, "manual-address-drops")

                self.max_area_address_mismatch = YLeaf(YType.enumeration, "max-area-address-mismatch")

                self.originated_lsp_buffer_size_mismatch = YLeaf(YType.enumeration, "originated-lsp-buffer-size-mismatch")

                self.own_lsp_purge = YLeaf(YType.enumeration, "own-lsp-purge")

                self.protocols_supported_mismatch = YLeaf(YType.enumeration, "protocols-supported-mismatch")

                self.rejected_adjacency = YLeaf(YType.enumeration, "rejected-adjacency")

                self.sequence_number_skip = YLeaf(YType.enumeration, "sequence-number-skip")

                self.version_skew = YLeaf(YType.enumeration, "version-skew")
                self._segment_path = lambda: "Cisco-IOS-XR-clns-isis-cfg:isis"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Isis, ['adjacency_change', 'all', 'area_mismatch', 'attempt_to_exceed_max_sequence', 'authentication_failure', 'authentication_type_failure', 'corrupted_lsp_detected', 'database_overflow', 'id_length_mismatch', 'lsp_error_detected', 'lsp_too_large_to_propagate', 'manual_address_drops', 'max_area_address_mismatch', 'originated_lsp_buffer_size_mismatch', 'own_lsp_purge', 'protocols_supported_mismatch', 'rejected_adjacency', 'sequence_number_skip', 'version_skew'], name, value)


        class L2Tun(Entity):
            """
            Enable SNMP l2tun traps
            
            .. attribute:: pseudowire_status
            
            	Enable traps for L2TPv3 PW status
            	**type**\:  bool
            
            .. attribute:: sessions
            
            	Enable L2TUN sessions traps
            	**type**\:  bool
            
            .. attribute:: tunnel_down
            
            	Enable L2TUN tunnel DOWN traps
            	**type**\:  bool
            
            .. attribute:: tunnel_up
            
            	Enable L2TUN tunnel UP traps
            	**type**\:  bool
            
            

            """

            _prefix = 'tunnel-l2tun-proto-mibs-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Snmp.Notification.L2Tun, self).__init__()

                self.yang_name = "l2tun"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.pseudowire_status = YLeaf(YType.boolean, "pseudowire-status")

                self.sessions = YLeaf(YType.boolean, "sessions")

                self.tunnel_down = YLeaf(YType.boolean, "tunnel-down")

                self.tunnel_up = YLeaf(YType.boolean, "tunnel-up")
                self._segment_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-proto-mibs-cfg:l2tun"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.L2Tun, ['pseudowire_status', 'sessions', 'tunnel_down', 'tunnel_up'], name, value)


        class L2Vpn(Entity):
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
            _revision = '2017-06-26'

            def __init__(self):
                super(Snmp.Notification.L2Vpn, self).__init__()

                self.yang_name = "l2vpn"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cisco = YLeaf(YType.empty, "cisco")

                self.enable = YLeaf(YType.empty, "enable")

                self.vc_down = YLeaf(YType.empty, "vc-down")

                self.vc_up = YLeaf(YType.empty, "vc-up")
                self._segment_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:l2vpn"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.L2Vpn, ['cisco', 'enable', 'vc_down', 'vc_up'], name, value)


        class MplsFrr(Entity):
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
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Notification.MplsFrr, self).__init__()

                self.yang_name = "mpls-frr"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")

                self.protected = YLeaf(YType.empty, "protected")

                self.unprotected = YLeaf(YType.empty, "unprotected")
                self._segment_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-frr"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.MplsFrr, ['enable', 'protected', 'unprotected'], name, value)


        class MplsL3Vpn(Entity):
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
                super(Snmp.Notification.MplsL3Vpn, self).__init__()

                self.yang_name = "mpls-l3vpn"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")

                self.max_threshold_cleared = YLeaf(YType.empty, "max-threshold-cleared")

                self.max_threshold_exceeded = YLeaf(YType.empty, "max-threshold-exceeded")

                self.max_threshold_reissue_notification_time = YLeaf(YType.int32, "max-threshold-reissue-notification-time")

                self.mid_threshold_exceeded = YLeaf(YType.empty, "mid-threshold-exceeded")

                self.vrf_down = YLeaf(YType.empty, "vrf-down")

                self.vrf_up = YLeaf(YType.empty, "vrf-up")
                self._segment_path = lambda: "Cisco-IOS-XR-mpls-vpn-cfg:mpls-l3vpn"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.MplsL3Vpn, ['enable', 'max_threshold_cleared', 'max_threshold_exceeded', 'max_threshold_reissue_notification_time', 'mid_threshold_exceeded', 'vrf_down', 'vrf_up'], name, value)


        class MplsLdp(Entity):
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
            _revision = '2017-06-26'

            def __init__(self):
                super(Snmp.Notification.MplsLdp, self).__init__()

                self.yang_name = "mpls-ldp"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.init_session_threshold_exceeded = YLeaf(YType.empty, "init-session-threshold-exceeded")

                self.session_down = YLeaf(YType.empty, "session-down")

                self.session_up = YLeaf(YType.empty, "session-up")
                self._segment_path = lambda: "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.MplsLdp, ['init_session_threshold_exceeded', 'session_down', 'session_up'], name, value)


        class MplsTe(Entity):
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
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Notification.MplsTe, self).__init__()

                self.yang_name = "mpls-te"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"cisco-extension" : ("cisco_extension", Snmp.Notification.MplsTe.CiscoExtension)}
                self._child_list_classes = {}

                self.cisco = YLeaf(YType.empty, "cisco")

                self.down = YLeaf(YType.empty, "down")

                self.reoptimize = YLeaf(YType.empty, "reoptimize")

                self.reroute = YLeaf(YType.empty, "reroute")

                self.up = YLeaf(YType.empty, "up")

                self.cisco_extension = Snmp.Notification.MplsTe.CiscoExtension()
                self.cisco_extension.parent = self
                self._children_name_map["cisco_extension"] = "cisco-extension"
                self._children_yang_names.add("cisco-extension")
                self._segment_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.MplsTe, ['cisco', 'down', 'reoptimize', 'reroute', 'up'], name, value)


            class CiscoExtension(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(Snmp.Notification.MplsTe.CiscoExtension, self).__init__()

                    self.yang_name = "cisco-extension"
                    self.yang_parent_name = "mpls-te"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bringup_fail = YLeaf(YType.empty, "bringup-fail")

                    self.insufficient_bandwidth = YLeaf(YType.empty, "insufficient-bandwidth")

                    self.preempt = YLeaf(YType.empty, "preempt")

                    self.re_route_pending = YLeaf(YType.empty, "re-route-pending")

                    self.re_route_pending_clear = YLeaf(YType.empty, "re-route-pending-clear")
                    self._segment_path = lambda: "cisco-extension"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-mpls-te-cfg:mpls-te/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.MplsTe.CiscoExtension, ['bringup_fail', 'insufficient_bandwidth', 'preempt', 're_route_pending', 're_route_pending_clear'], name, value)


        class MplsTeP2Mp(Entity):
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
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Notification.MplsTeP2Mp, self).__init__()

                self.yang_name = "mpls-te-p2mp"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.down = YLeaf(YType.empty, "down")

                self.up = YLeaf(YType.empty, "up")
                self._segment_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te-p2mp"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.MplsTeP2Mp, ['down', 'up'], name, value)


        class Ntp(Entity):
            """
            CISCO\-NTP\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable ciscoNtpMIB notification configuration
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Notification.Ntp, self).__init__()

                self.yang_name = "ntp"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Ntp, ['enable'], name, value)


        class Oam(Entity):
            """
            802.3 OAM MIB notification configuration
            
            .. attribute:: enable
            
            	Enable 802.3 OAM MIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ethernet-link-oam-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Snmp.Notification.Oam, self).__init__()

                self.yang_name = "oam"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-ethernet-link-oam-cfg:oam"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Oam, ['enable'], name, value)


        class Optical(Entity):
            """
            CISCO\-OPTICAL\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable Opticalmib notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'opticalmib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Snmp.Notification.Optical, self).__init__()

                self.yang_name = "optical"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-opticalmib-cfg:optical"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Optical, ['enable'], name, value)


        class OpticalOts(Entity):
            """
            CISCO\-OPTICAL\-OTS\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable OpticalOtsmib notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'opticalotsmib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Snmp.Notification.OpticalOts, self).__init__()

                self.yang_name = "optical-ots"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-opticalotsmib-cfg:optical-ots"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.OpticalOts, ['enable'], name, value)


        class Ospf(Entity):
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
            _revision = '2017-07-14'

            def __init__(self):
                super(Snmp.Notification.Ospf, self).__init__()

                self.yang_name = "ospf"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"error" : ("error", Snmp.Notification.Ospf.Error), "lsa" : ("lsa", Snmp.Notification.Ospf.Lsa), "retransmit" : ("retransmit", Snmp.Notification.Ospf.Retransmit), "state-change" : ("state_change", Snmp.Notification.Ospf.StateChange)}
                self._child_list_classes = {}

                self.error = Snmp.Notification.Ospf.Error()
                self.error.parent = self
                self._children_name_map["error"] = "error"
                self._children_yang_names.add("error")

                self.lsa = Snmp.Notification.Ospf.Lsa()
                self.lsa.parent = self
                self._children_name_map["lsa"] = "lsa"
                self._children_yang_names.add("lsa")

                self.retransmit = Snmp.Notification.Ospf.Retransmit()
                self.retransmit.parent = self
                self._children_name_map["retransmit"] = "retransmit"
                self._children_yang_names.add("retransmit")

                self.state_change = Snmp.Notification.Ospf.StateChange()
                self.state_change.parent = self
                self._children_name_map["state_change"] = "state-change"
                self._children_yang_names.add("state-change")
                self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ospf-cfg:ospf"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()


            class Error(Entity):
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
                _revision = '2017-07-14'

                def __init__(self):
                    super(Snmp.Notification.Ospf.Error, self).__init__()

                    self.yang_name = "error"
                    self.yang_parent_name = "ospf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.authentication_failure = YLeaf(YType.empty, "authentication-failure")

                    self.bad_packet = YLeaf(YType.empty, "bad-packet")

                    self.config_error = YLeaf(YType.empty, "config-error")

                    self.virtual_authentication_failure = YLeaf(YType.empty, "virtual-authentication-failure")

                    self.virtual_bad_packet = YLeaf(YType.empty, "virtual-bad-packet")

                    self.virtual_config_error = YLeaf(YType.empty, "virtual-config-error")
                    self._segment_path = lambda: "error"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-ipv4-ospf-cfg:ospf/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.Ospf.Error, ['authentication_failure', 'bad_packet', 'config_error', 'virtual_authentication_failure', 'virtual_bad_packet', 'virtual_config_error'], name, value)


            class Lsa(Entity):
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
                _revision = '2017-07-14'

                def __init__(self):
                    super(Snmp.Notification.Ospf.Lsa, self).__init__()

                    self.yang_name = "lsa"
                    self.yang_parent_name = "ospf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.max_age_lsa = YLeaf(YType.empty, "max-age-lsa")

                    self.originate_lsa = YLeaf(YType.empty, "originate-lsa")
                    self._segment_path = lambda: "lsa"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-ipv4-ospf-cfg:ospf/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.Ospf.Lsa, ['max_age_lsa', 'originate_lsa'], name, value)


            class Retransmit(Entity):
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
                _revision = '2017-07-14'

                def __init__(self):
                    super(Snmp.Notification.Ospf.Retransmit, self).__init__()

                    self.yang_name = "retransmit"
                    self.yang_parent_name = "ospf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.packet = YLeaf(YType.empty, "packet")

                    self.virtual_packet = YLeaf(YType.empty, "virtual-packet")
                    self._segment_path = lambda: "retransmit"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-ipv4-ospf-cfg:ospf/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.Ospf.Retransmit, ['packet', 'virtual_packet'], name, value)


            class StateChange(Entity):
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
                _revision = '2017-07-14'

                def __init__(self):
                    super(Snmp.Notification.Ospf.StateChange, self).__init__()

                    self.yang_name = "state-change"
                    self.yang_parent_name = "ospf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interface = YLeaf(YType.empty, "interface")

                    self.neighbor = YLeaf(YType.empty, "neighbor")

                    self.virtual_interface = YLeaf(YType.empty, "virtual-interface")

                    self.virtual_neighbor = YLeaf(YType.empty, "virtual-neighbor")
                    self._segment_path = lambda: "state-change"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-ipv4-ospf-cfg:ospf/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.Ospf.StateChange, ['interface', 'neighbor', 'virtual_interface', 'virtual_neighbor'], name, value)


        class Ospfv3(Entity):
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
            _revision = '2017-07-14'

            def __init__(self):
                super(Snmp.Notification.Ospfv3, self).__init__()

                self.yang_name = "ospfv3"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"error" : ("error", Snmp.Notification.Ospfv3.Error), "state-change" : ("state_change", Snmp.Notification.Ospfv3.StateChange)}
                self._child_list_classes = {}

                self.error = Snmp.Notification.Ospfv3.Error()
                self.error.parent = self
                self._children_name_map["error"] = "error"
                self._children_yang_names.add("error")

                self.state_change = Snmp.Notification.Ospfv3.StateChange()
                self.state_change.parent = self
                self._children_name_map["state_change"] = "state-change"
                self._children_yang_names.add("state-change")
                self._segment_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-cfg:ospfv3"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()


            class Error(Entity):
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
                _revision = '2017-07-14'

                def __init__(self):
                    super(Snmp.Notification.Ospfv3.Error, self).__init__()

                    self.yang_name = "error"
                    self.yang_parent_name = "ospfv3"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bad_packet = YLeaf(YType.empty, "bad-packet")

                    self.config_error = YLeaf(YType.empty, "config-error")

                    self.virtual_bad_packet = YLeaf(YType.empty, "virtual-bad-packet")

                    self.virtual_config_error = YLeaf(YType.empty, "virtual-config-error")
                    self._segment_path = lambda: "error"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-ipv6-ospfv3-cfg:ospfv3/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.Ospfv3.Error, ['bad_packet', 'config_error', 'virtual_bad_packet', 'virtual_config_error'], name, value)


            class StateChange(Entity):
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
                _revision = '2017-07-14'

                def __init__(self):
                    super(Snmp.Notification.Ospfv3.StateChange, self).__init__()

                    self.yang_name = "state-change"
                    self.yang_parent_name = "ospfv3"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interface = YLeaf(YType.empty, "interface")

                    self.neighbor = YLeaf(YType.empty, "neighbor")

                    self.nssa_translator = YLeaf(YType.empty, "nssa-translator")

                    self.restart = YLeaf(YType.empty, "restart")

                    self.restart_helper = YLeaf(YType.empty, "restart-helper")

                    self.restart_virtual_helper = YLeaf(YType.empty, "restart-virtual-helper")

                    self.virtual_interface = YLeaf(YType.empty, "virtual-interface")

                    self.virtual_neighbor = YLeaf(YType.empty, "virtual-neighbor")
                    self._segment_path = lambda: "state-change"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-ipv6-ospfv3-cfg:ospfv3/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.Ospfv3.StateChange, ['interface', 'neighbor', 'nssa_translator', 'restart', 'restart_helper', 'restart_virtual_helper', 'virtual_interface', 'virtual_neighbor'], name, value)


        class Otn(Entity):
            """
            CISCO\-OTN\-IF\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable ciscoOtnIfMIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'otnifmib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Snmp.Notification.Otn, self).__init__()

                self.yang_name = "otn"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-otnifmib-cfg:otn"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Otn, ['enable'], name, value)


        class Rf(Entity):
            """
            CISCO\-RF\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable ciscoRFMIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-mib-rfmib-cfg'
            _revision = '2016-05-13'

            def __init__(self):
                super(Snmp.Notification.Rf, self).__init__()

                self.yang_name = "rf"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-snmp-mib-rfmib-cfg:rf"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Rf, ['enable'], name, value)


        class Rsvp(Entity):
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
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Notification.Rsvp, self).__init__()

                self.yang_name = "rsvp"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")

                self.lost_flow = YLeaf(YType.empty, "lost-flow")

                self.new_flow = YLeaf(YType.empty, "new-flow")
                self._segment_path = lambda: "Cisco-IOS-XR-ip-rsvp-cfg:rsvp"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Rsvp, ['enable', 'lost_flow', 'new_flow'], name, value)


        class SelectiveVrfDownload(Entity):
            """
            CISCO\-SELECTIVE\-VRF\-DOWNLOAD\-MIB notification
            configuration
            
            .. attribute:: role_change
            
            	Enable csvdEntityRoleChangeNotification notification
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Notification.SelectiveVrfDownload, self).__init__()

                self.yang_name = "selective-vrf-download"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.role_change = YLeaf(YType.empty, "role-change")
                self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:selective-vrf-download"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.SelectiveVrfDownload, ['role_change'], name, value)


        class Sensor(Entity):
            """
            CISCO\-ENTITY\-SENSOR\-MIB notification
            configuration
            
            .. attribute:: enable
            
            	Enable entitySensorMIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-ciscosensormib-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Notification.Sensor, self).__init__()

                self.yang_name = "sensor"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-snmp-ciscosensormib-cfg:sensor"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Sensor, ['enable'], name, value)


        class Snmp(Entity):
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
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Notification.Snmp, self).__init__()

                self.yang_name = "snmp"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.authentication = YLeaf(YType.empty, "authentication")

                self.cold_start = YLeaf(YType.empty, "cold-start")

                self.enable = YLeaf(YType.empty, "enable")

                self.link_down = YLeaf(YType.empty, "Cisco-IOS-XR-snmp-ifmib-cfg:link-down")

                self.link_up = YLeaf(YType.empty, "Cisco-IOS-XR-snmp-ifmib-cfg:link-up")

                self.warm_start = YLeaf(YType.empty, "warm-start")
                self._segment_path = lambda: "snmp"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Snmp, ['authentication', 'cold_start', 'enable', 'link_down', 'link_up', 'warm_start'], name, value)


        class SubscriberMib(Entity):
            """
            Subscriber notification commands
            
            .. attribute:: session_aggregate
            
            	Session aggregation
            	**type**\:   :py:class:`SessionAggregate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Notification.SubscriberMib.SessionAggregate>`
            
            

            """

            _prefix = 'subscriber-session-mon-mibs-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Snmp.Notification.SubscriberMib, self).__init__()

                self.yang_name = "subscriber-mib"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"session-aggregate" : ("session_aggregate", Snmp.Notification.SubscriberMib.SessionAggregate)}
                self._child_list_classes = {}

                self.session_aggregate = Snmp.Notification.SubscriberMib.SessionAggregate()
                self.session_aggregate.parent = self
                self._children_name_map["session_aggregate"] = "session-aggregate"
                self._children_yang_names.add("session-aggregate")
                self._segment_path = lambda: "Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber-mib"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()


            class SessionAggregate(Entity):
                """
                Session aggregation
                
                .. attribute:: access_interface
                
                	Subscriber notification at access interface level
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: node
                
                	Subscriber notification at node level
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'subscriber-session-mon-mibs-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Snmp.Notification.SubscriberMib.SessionAggregate, self).__init__()

                    self.yang_name = "session-aggregate"
                    self.yang_parent_name = "subscriber-mib"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.access_interface = YLeaf(YType.empty, "access-interface")

                    self.node = YLeaf(YType.empty, "node")
                    self._segment_path = lambda: "session-aggregate"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/Cisco-IOS-XR-subscriber-session-mon-mibs-cfg:subscriber-mib/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Notification.SubscriberMib.SessionAggregate, ['access_interface', 'node'], name, value)


        class Syslog(Entity):
            """
            CISCO\-SYSLOG\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable ciscoSyslogMIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'snmp-syslogmib-cfg'
            _revision = '2015-12-01'

            def __init__(self):
                super(Snmp.Notification.Syslog, self).__init__()

                self.yang_name = "syslog"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-snmp-syslogmib-cfg:syslog"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Syslog, ['enable'], name, value)


        class System(Entity):
            """
            CISCO\-SYSTEM\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable ciscoSystemMIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-systemmib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Snmp.Notification.System, self).__init__()

                self.yang_name = "system"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-infra-systemmib-cfg:system"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.System, ['enable'], name, value)


        class Vpls(Entity):
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
            _revision = '2017-06-26'

            def __init__(self):
                super(Snmp.Notification.Vpls, self).__init__()

                self.yang_name = "vpls"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")

                self.full_clear = YLeaf(YType.empty, "full-clear")

                self.full_raise = YLeaf(YType.empty, "full-raise")

                self.status = YLeaf(YType.empty, "status")
                self._segment_path = lambda: "Cisco-IOS-XR-l2vpn-cfg:vpls"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Vpls, ['enable', 'full_clear', 'full_raise', 'status'], name, value)


        class Vrrp(Entity):
            """
            VRRP\-MIB notification configuration
            
            .. attribute:: enable
            
            	Enable VRRP\-MIB notifications
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ipv4-vrrp-cfg'
            _revision = '2017-05-19'

            def __init__(self):
                super(Snmp.Notification.Vrrp, self).__init__()

                self.yang_name = "vrrp"
                self.yang_parent_name = "notification"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.enable = YLeaf(YType.empty, "enable")
                self._segment_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/notification/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Notification.Vrrp, ['enable'], name, value)


    class OverloadControl(Entity):
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
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.OverloadControl, self).__init__()

            self.yang_name = "overload-control"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.drop_time = YLeaf(YType.uint32, "drop-time")

            self.throttle_rate = YLeaf(YType.uint32, "throttle-rate")
            self._segment_path = lambda: "overload-control"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.OverloadControl, ['drop_time', 'throttle_rate'], name, value)


    class System(Entity):
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
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.System, self).__init__()

            self.yang_name = "system"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.chassis_id = YLeaf(YType.str, "chassis-id")

            self.contact = YLeaf(YType.str, "contact")

            self.location = YLeaf(YType.str, "location")
            self._segment_path = lambda: "system"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.System, ['chassis_id', 'contact', 'location'], name, value)


    class Target(Entity):
        """
        SNMP target configurations
        
        .. attribute:: targets
        
        	List of targets
        	**type**\:   :py:class:`Targets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.Target, self).__init__()

            self.yang_name = "target"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"targets" : ("targets", Snmp.Target.Targets)}
            self._child_list_classes = {}

            self.targets = Snmp.Target.Targets()
            self.targets.parent = self
            self._children_name_map["targets"] = "targets"
            self._children_yang_names.add("targets")
            self._segment_path = lambda: "target"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()


        class Targets(Entity):
            """
            List of targets
            
            .. attribute:: target
            
            	Name of the target list
            	**type**\: list of    :py:class:`Target <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets.Target>`
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Target.Targets, self).__init__()

                self.yang_name = "targets"
                self.yang_parent_name = "target"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"target" : ("target", Snmp.Target.Targets.Target)}

                self.target = YList(self)
                self._segment_path = lambda: "targets"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/target/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Target.Targets, [], name, value)


            class Target(Entity):
                """
                Name of the target list
                
                .. attribute:: target_list_name  <key>
                
                	Name of the target list
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: target_addresses
                
                	SNMP Target address configurations
                	**type**\:   :py:class:`TargetAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets.Target.TargetAddresses>`
                
                .. attribute:: vrf_names
                
                	List of VRF Name for a target list
                	**type**\:   :py:class:`VrfNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets.Target.VrfNames>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Snmp.Target.Targets.Target, self).__init__()

                    self.yang_name = "target"
                    self.yang_parent_name = "targets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"target-addresses" : ("target_addresses", Snmp.Target.Targets.Target.TargetAddresses), "vrf-names" : ("vrf_names", Snmp.Target.Targets.Target.VrfNames)}
                    self._child_list_classes = {}

                    self.target_list_name = YLeaf(YType.str, "target-list-name")

                    self.target_addresses = Snmp.Target.Targets.Target.TargetAddresses()
                    self.target_addresses.parent = self
                    self._children_name_map["target_addresses"] = "target-addresses"
                    self._children_yang_names.add("target-addresses")

                    self.vrf_names = Snmp.Target.Targets.Target.VrfNames()
                    self.vrf_names.parent = self
                    self._children_name_map["vrf_names"] = "vrf-names"
                    self._children_yang_names.add("vrf-names")
                    self._segment_path = lambda: "target" + "[target-list-name='" + self.target_list_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/target/targets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Target.Targets.Target, ['target_list_name'], name, value)


                class TargetAddresses(Entity):
                    """
                    SNMP Target address configurations
                    
                    .. attribute:: target_address
                    
                    	IP Address to be configured for the Target
                    	**type**\: list of    :py:class:`TargetAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets.Target.TargetAddresses.TargetAddress>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Snmp.Target.Targets.Target.TargetAddresses, self).__init__()

                        self.yang_name = "target-addresses"
                        self.yang_parent_name = "target"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"target-address" : ("target_address", Snmp.Target.Targets.Target.TargetAddresses.TargetAddress)}

                        self.target_address = YList(self)
                        self._segment_path = lambda: "target-addresses"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Target.Targets.Target.TargetAddresses, [], name, value)


                    class TargetAddress(Entity):
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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Snmp.Target.Targets.Target.TargetAddresses.TargetAddress, self).__init__()

                            self.yang_name = "target-address"
                            self.yang_parent_name = "target-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ip_address = YLeaf(YType.str, "ip-address")
                            self._segment_path = lambda: "target-address" + "[ip-address='" + self.ip_address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Target.Targets.Target.TargetAddresses.TargetAddress, ['ip_address'], name, value)


                class VrfNames(Entity):
                    """
                    List of VRF Name for a target list
                    
                    .. attribute:: vrf_name
                    
                    	VRF name of the target
                    	**type**\: list of    :py:class:`VrfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Target.Targets.Target.VrfNames.VrfName>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Snmp.Target.Targets.Target.VrfNames, self).__init__()

                        self.yang_name = "vrf-names"
                        self.yang_parent_name = "target"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"vrf-name" : ("vrf_name", Snmp.Target.Targets.Target.VrfNames.VrfName)}

                        self.vrf_name = YList(self)
                        self._segment_path = lambda: "vrf-names"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Target.Targets.Target.VrfNames, [], name, value)


                    class VrfName(Entity):
                        """
                        VRF name of the target
                        
                        .. attribute:: name  <key>
                        
                        	VRF Name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Snmp.Target.Targets.Target.VrfNames.VrfName, self).__init__()

                            self.yang_name = "vrf-name"
                            self.yang_parent_name = "vrf-names"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.name = YLeaf(YType.str, "name")
                            self._segment_path = lambda: "vrf-name" + "[name='" + self.name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Target.Targets.Target.VrfNames.VrfName, ['name'], name, value)


    class Timeouts(Entity):
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
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.Timeouts, self).__init__()

            self.yang_name = "timeouts"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.duplicates = YLeaf(YType.uint32, "duplicates")

            self.in_qdrop = YLeaf(YType.uint32, "in-qdrop")

            self.pdu_stats = YLeaf(YType.uint32, "pdu-stats")

            self.subagent = YLeaf(YType.uint32, "subagent")
            self._segment_path = lambda: "timeouts"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Timeouts, ['duplicates', 'in_qdrop', 'pdu_stats', 'subagent'], name, value)


    class Trap(Entity):
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
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.Trap, self).__init__()

            self.yang_name = "trap"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.queue_length = YLeaf(YType.uint32, "queue-length")

            self.throttle_time = YLeaf(YType.uint32, "throttle-time")

            self.timeout = YLeaf(YType.uint32, "timeout")
            self._segment_path = lambda: "trap"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Trap, ['queue_length', 'throttle_time', 'timeout'], name, value)


    class TrapHosts(Entity):
        """
        Specify hosts to receive SNMP notifications
        
        .. attribute:: trap_host
        
        	Specify hosts to receive SNMP notifications
        	**type**\: list of    :py:class:`TrapHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.TrapHosts, self).__init__()

            self.yang_name = "trap-hosts"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"trap-host" : ("trap_host", Snmp.TrapHosts.TrapHost)}

            self.trap_host = YList(self)
            self._segment_path = lambda: "trap-hosts"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.TrapHosts, [], name, value)


        class TrapHost(Entity):
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
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.TrapHosts.TrapHost, self).__init__()

                self.yang_name = "trap-host"
                self.yang_parent_name = "trap-hosts"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"default-user-communities" : ("default_user_communities", Snmp.TrapHosts.TrapHost.DefaultUserCommunities), "encrypted-user-communities" : ("encrypted_user_communities", Snmp.TrapHosts.TrapHost.EncryptedUserCommunities), "inform-host" : ("inform_host", Snmp.TrapHosts.TrapHost.InformHost)}
                self._child_list_classes = {}

                self.ip_address = YLeaf(YType.str, "ip-address")

                self.default_user_communities = Snmp.TrapHosts.TrapHost.DefaultUserCommunities()
                self.default_user_communities.parent = self
                self._children_name_map["default_user_communities"] = "default-user-communities"
                self._children_yang_names.add("default-user-communities")

                self.encrypted_user_communities = Snmp.TrapHosts.TrapHost.EncryptedUserCommunities()
                self.encrypted_user_communities.parent = self
                self._children_name_map["encrypted_user_communities"] = "encrypted-user-communities"
                self._children_yang_names.add("encrypted-user-communities")

                self.inform_host = Snmp.TrapHosts.TrapHost.InformHost()
                self.inform_host.parent = self
                self._children_name_map["inform_host"] = "inform-host"
                self._children_yang_names.add("inform-host")
                self._segment_path = lambda: "trap-host" + "[ip-address='" + self.ip_address.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/trap-hosts/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.TrapHosts.TrapHost, ['ip_address'], name, value)


            class DefaultUserCommunities(Entity):
                """
                Container class for defining communities for a
                trap host
                
                .. attribute:: default_user_community
                
                	Unencrpted Community name associated with a trap host
                	**type**\: list of    :py:class:`DefaultUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Snmp.TrapHosts.TrapHost.DefaultUserCommunities, self).__init__()

                    self.yang_name = "default-user-communities"
                    self.yang_parent_name = "trap-host"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"default-user-community" : ("default_user_community", Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity)}

                    self.default_user_community = YList(self)
                    self._segment_path = lambda: "default-user-communities"

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.TrapHosts.TrapHost.DefaultUserCommunities, [], name, value)


                class DefaultUserCommunity(Entity):
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
                    	**type**\:   :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
                    
                    .. attribute:: version
                    
                    	SNMP Version to be used v1/v2c/v3
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity, self).__init__()

                        self.yang_name = "default-user-community"
                        self.yang_parent_name = "default-user-communities"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.community_name = YLeaf(YType.str, "community-name")

                        self.advanced_trap_types1 = YLeaf(YType.int32, "advanced-trap-types1")

                        self.advanced_trap_types2 = YLeaf(YType.int32, "advanced-trap-types2")

                        self.basic_trap_types = YLeaf(YType.int32, "basic-trap-types")

                        self.port = YLeaf(YType.uint16, "port")

                        self.security_level = YLeaf(YType.enumeration, "security-level")

                        self.version = YLeaf(YType.str, "version")
                        self._segment_path = lambda: "default-user-community" + "[community-name='" + self.community_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity, ['community_name', 'advanced_trap_types1', 'advanced_trap_types2', 'basic_trap_types', 'port', 'security_level', 'version'], name, value)


            class EncryptedUserCommunities(Entity):
                """
                Container class for defining Clear/encrypt
                communities for a trap host
                
                .. attribute:: encrypted_user_community
                
                	Clear/Encrypt Community name associated with a trap host
                	**type**\: list of    :py:class:`EncryptedUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Snmp.TrapHosts.TrapHost.EncryptedUserCommunities, self).__init__()

                    self.yang_name = "encrypted-user-communities"
                    self.yang_parent_name = "trap-host"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"encrypted-user-community" : ("encrypted_user_community", Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity)}

                    self.encrypted_user_community = YList(self)
                    self._segment_path = lambda: "encrypted-user-communities"

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.TrapHosts.TrapHost.EncryptedUserCommunities, [], name, value)


                class EncryptedUserCommunity(Entity):
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
                    	**type**\:   :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
                    
                    .. attribute:: version
                    
                    	SNMP Version to be used v1/v2c/v3
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity, self).__init__()

                        self.yang_name = "encrypted-user-community"
                        self.yang_parent_name = "encrypted-user-communities"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.community_name = YLeaf(YType.str, "community-name")

                        self.advanced_trap_types1 = YLeaf(YType.int32, "advanced-trap-types1")

                        self.advanced_trap_types2 = YLeaf(YType.int32, "advanced-trap-types2")

                        self.basic_trap_types = YLeaf(YType.int32, "basic-trap-types")

                        self.port = YLeaf(YType.uint16, "port")

                        self.security_level = YLeaf(YType.enumeration, "security-level")

                        self.version = YLeaf(YType.str, "version")
                        self._segment_path = lambda: "encrypted-user-community" + "[community-name='" + self.community_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity, ['community_name', 'advanced_trap_types1', 'advanced_trap_types2', 'basic_trap_types', 'port', 'security_level', 'version'], name, value)


            class InformHost(Entity):
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(Snmp.TrapHosts.TrapHost.InformHost, self).__init__()

                    self.yang_name = "inform-host"
                    self.yang_parent_name = "trap-host"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"inform-encrypted-user-communities" : ("inform_encrypted_user_communities", Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities), "inform-user-communities" : ("inform_user_communities", Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities)}
                    self._child_list_classes = {}

                    self.inform_encrypted_user_communities = Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities()
                    self.inform_encrypted_user_communities.parent = self
                    self._children_name_map["inform_encrypted_user_communities"] = "inform-encrypted-user-communities"
                    self._children_yang_names.add("inform-encrypted-user-communities")

                    self.inform_user_communities = Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities()
                    self.inform_user_communities.parent = self
                    self._children_name_map["inform_user_communities"] = "inform-user-communities"
                    self._children_yang_names.add("inform-user-communities")
                    self._segment_path = lambda: "inform-host"


                class InformEncryptedUserCommunities(Entity):
                    """
                    Container class for defining Clear/encrypt
                    communities for a inform host
                    
                    .. attribute:: inform_encrypted_user_community
                    
                    	Clear/Encrypt Community name associated with a inform host
                    	**type**\: list of    :py:class:`InformEncryptedUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities, self).__init__()

                        self.yang_name = "inform-encrypted-user-communities"
                        self.yang_parent_name = "inform-host"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"inform-encrypted-user-community" : ("inform_encrypted_user_community", Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity)}

                        self.inform_encrypted_user_community = YList(self)
                        self._segment_path = lambda: "inform-encrypted-user-communities"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities, [], name, value)


                    class InformEncryptedUserCommunity(Entity):
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
                        	**type**\:   :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
                        
                        .. attribute:: version
                        
                        	SNMP Version to be used v2c/v3
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity, self).__init__()

                            self.yang_name = "inform-encrypted-user-community"
                            self.yang_parent_name = "inform-encrypted-user-communities"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.community_name = YLeaf(YType.str, "community-name")

                            self.advanced_trap_types1 = YLeaf(YType.int32, "advanced-trap-types1")

                            self.advanced_trap_types2 = YLeaf(YType.int32, "advanced-trap-types2")

                            self.basic_trap_types = YLeaf(YType.int32, "basic-trap-types")

                            self.port = YLeaf(YType.uint16, "port")

                            self.security_level = YLeaf(YType.enumeration, "security-level")

                            self.version = YLeaf(YType.str, "version")
                            self._segment_path = lambda: "inform-encrypted-user-community" + "[community-name='" + self.community_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity, ['community_name', 'advanced_trap_types1', 'advanced_trap_types2', 'basic_trap_types', 'port', 'security_level', 'version'], name, value)


                class InformUserCommunities(Entity):
                    """
                    Container class for defining communities for
                    a inform host
                    
                    .. attribute:: inform_user_community
                    
                    	Unencrpted Community name associated with a inform host
                    	**type**\: list of    :py:class:`InformUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity>`
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities, self).__init__()

                        self.yang_name = "inform-user-communities"
                        self.yang_parent_name = "inform-host"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"inform-user-community" : ("inform_user_community", Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity)}

                        self.inform_user_community = YList(self)
                        self._segment_path = lambda: "inform-user-communities"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities, [], name, value)


                    class InformUserCommunity(Entity):
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
                        	**type**\:   :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
                        
                        .. attribute:: version
                        
                        	SNMP Version to be used v2c/v3
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity, self).__init__()

                            self.yang_name = "inform-user-community"
                            self.yang_parent_name = "inform-user-communities"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.community_name = YLeaf(YType.str, "community-name")

                            self.advanced_trap_types1 = YLeaf(YType.int32, "advanced-trap-types1")

                            self.advanced_trap_types2 = YLeaf(YType.int32, "advanced-trap-types2")

                            self.basic_trap_types = YLeaf(YType.int32, "basic-trap-types")

                            self.port = YLeaf(YType.uint16, "port")

                            self.security_level = YLeaf(YType.enumeration, "security-level")

                            self.version = YLeaf(YType.str, "version")
                            self._segment_path = lambda: "inform-user-community" + "[community-name='" + self.community_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity, ['community_name', 'advanced_trap_types1', 'advanced_trap_types2', 'basic_trap_types', 'port', 'security_level', 'version'], name, value)


    class Users(Entity):
        """
        Define a user who can access the SNMP engine
        
        .. attribute:: user
        
        	Name of the user
        	**type**\: list of    :py:class:`User <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Users.User>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.Users, self).__init__()

            self.yang_name = "users"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"user" : ("user", Snmp.Users.User)}

            self.user = YList(self)
            self._segment_path = lambda: "users"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Users, [], name, value)


        class User(Entity):
            """
            Name of the user
            
            .. attribute:: user_name  <key>
            
            	Name of the user
            	**type**\:  str
            
            .. attribute:: algorithm
            
            	The algorithm used md5 or sha
            	**type**\:   :py:class:`SnmpHashAlgorithm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpHashAlgorithm>`
            
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
            	**type**\:   :py:class:`SnmpOwnerAccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpOwnerAccess>`
            
            .. attribute:: port
            
            	UDP port number
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: priv_algorithm
            
            	The algorithm used des56 or aes128 or aes192or aes256 or 3des
            	**type**\:   :py:class:`SnmpPrivAlgorithm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpPrivAlgorithm>`
            
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
            	**type**\:   :py:class:`Snmpacl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmpacl>`
            
            .. attribute:: v6_access_list
            
            	Ipv6 Access\-list name
            	**type**\:  str
            
            .. attribute:: v6acl_type
            
            	Access\-list type
            	**type**\:   :py:class:`Snmpacl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmpacl>`
            
            .. attribute:: version
            
            	SNMP version to be used. v1,v2c or v3
            	**type**\:   :py:class:`UserSnmpVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.UserSnmpVersion>`
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Users.User, self).__init__()

                self.yang_name = "user"
                self.yang_parent_name = "users"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.user_name = YLeaf(YType.str, "user-name")

                self.algorithm = YLeaf(YType.enumeration, "algorithm")

                self.authentication_password = YLeaf(YType.str, "authentication-password")

                self.authentication_password_configured = YLeaf(YType.empty, "authentication-password-configured")

                self.group_name = YLeaf(YType.str, "group-name")

                self.owner = YLeaf(YType.enumeration, "owner")

                self.port = YLeaf(YType.uint16, "port")

                self.priv_algorithm = YLeaf(YType.enumeration, "priv-algorithm")

                self.privacy_password = YLeaf(YType.str, "privacy-password")

                self.privacy_password_configured = YLeaf(YType.empty, "privacy-password-configured")

                self.remote_address = YLeaf(YType.str, "remote-address")

                self.v4_access_list = YLeaf(YType.str, "v4-access-list")

                self.v4acl_type = YLeaf(YType.enumeration, "v4acl-type")

                self.v6_access_list = YLeaf(YType.str, "v6-access-list")

                self.v6acl_type = YLeaf(YType.enumeration, "v6acl-type")

                self.version = YLeaf(YType.enumeration, "version")
                self._segment_path = lambda: "user" + "[user-name='" + self.user_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/users/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Users.User, ['user_name', 'algorithm', 'authentication_password', 'authentication_password_configured', 'group_name', 'owner', 'port', 'priv_algorithm', 'privacy_password', 'privacy_password_configured', 'remote_address', 'v4_access_list', 'v4acl_type', 'v6_access_list', 'v6acl_type', 'version'], name, value)


    class Views(Entity):
        """
        Class to configure a SNMPv2 MIB view
        
        .. attribute:: view
        
        	Name of the view
        	**type**\: list of    :py:class:`View <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Views.View>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.Views, self).__init__()

            self.yang_name = "views"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"view" : ("view", Snmp.Views.View)}

            self.view = YList(self)
            self._segment_path = lambda: "views"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Views, [], name, value)


        class View(Entity):
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
            	**type**\:   :py:class:`SnmpMibViewInclusion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpMibViewInclusion>`
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'snmp-agent-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Views.View, self).__init__()

                self.yang_name = "view"
                self.yang_parent_name = "views"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.view_name = YLeaf(YType.str, "view-name")

                self.family = YLeaf(YType.str, "family")

                self.view_inclusion = YLeaf(YType.enumeration, "view-inclusion")
                self._segment_path = lambda: "view" + "[view-name='" + self.view_name.get() + "']" + "[family='" + self.family.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/views/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Views.View, ['view_name', 'family', 'view_inclusion'], name, value)


    class Vrfs(Entity):
        """
        SNMP VRF configuration commands
        
        .. attribute:: vrf
        
        	VRF name
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf>`
        
        

        """

        _prefix = 'snmp-agent-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Snmp.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "snmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"vrf" : ("vrf", Snmp.Vrfs.Vrf)}

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Snmp.Vrfs, [], name, value)


        class Vrf(Entity):
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
            _revision = '2017-05-01'

            def __init__(self):
                super(Snmp.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"context-mappings" : ("context_mappings", Snmp.Vrfs.Vrf.ContextMappings), "contexts" : ("contexts", Snmp.Vrfs.Vrf.Contexts), "trap-hosts" : ("trap_hosts", Snmp.Vrfs.Vrf.TrapHosts)}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.context_mappings = Snmp.Vrfs.Vrf.ContextMappings()
                self.context_mappings.parent = self
                self._children_name_map["context_mappings"] = "context-mappings"
                self._children_yang_names.add("context-mappings")

                self.contexts = Snmp.Vrfs.Vrf.Contexts()
                self.contexts.parent = self
                self._children_name_map["contexts"] = "contexts"
                self._children_yang_names.add("contexts")

                self.trap_hosts = Snmp.Vrfs.Vrf.TrapHosts()
                self.trap_hosts.parent = self
                self._children_name_map["trap_hosts"] = "trap-hosts"
                self._children_yang_names.add("trap-hosts")
                self._segment_path = lambda: "vrf" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-snmp-agent-cfg:snmp/vrfs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Snmp.Vrfs.Vrf, ['name'], name, value)


            class ContextMappings(Entity):
                """
                List of context names
                
                .. attribute:: context_mapping
                
                	Context mapping name
                	**type**\: list of    :py:class:`ContextMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.ContextMappings.ContextMapping>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Snmp.Vrfs.Vrf.ContextMappings, self).__init__()

                    self.yang_name = "context-mappings"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"context-mapping" : ("context_mapping", Snmp.Vrfs.Vrf.ContextMappings.ContextMapping)}

                    self.context_mapping = YList(self)
                    self._segment_path = lambda: "context-mappings"

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Vrfs.Vrf.ContextMappings, [], name, value)


                class ContextMapping(Entity):
                    """
                    Context mapping name
                    
                    .. attribute:: context_mapping_name  <key>
                    
                    	Context mapping name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: context
                    
                    	SNMP context feature type
                    	**type**\:   :py:class:`SnmpContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpContext>`
                    
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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Snmp.Vrfs.Vrf.ContextMappings.ContextMapping, self).__init__()

                        self.yang_name = "context-mapping"
                        self.yang_parent_name = "context-mappings"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.context_mapping_name = YLeaf(YType.str, "context-mapping-name")

                        self.context = YLeaf(YType.enumeration, "context")

                        self.instance_name = YLeaf(YType.str, "instance-name")

                        self.topology_name = YLeaf(YType.str, "topology-name")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")
                        self._segment_path = lambda: "context-mapping" + "[context-mapping-name='" + self.context_mapping_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Vrfs.Vrf.ContextMappings.ContextMapping, ['context_mapping_name', 'context', 'instance_name', 'topology_name', 'vrf_name'], name, value)


            class Contexts(Entity):
                """
                List of Context Names
                
                .. attribute:: context
                
                	Context Name
                	**type**\: list of    :py:class:`Context <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.Contexts.Context>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Snmp.Vrfs.Vrf.Contexts, self).__init__()

                    self.yang_name = "contexts"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"context" : ("context", Snmp.Vrfs.Vrf.Contexts.Context)}

                    self.context = YList(self)
                    self._segment_path = lambda: "contexts"

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Vrfs.Vrf.Contexts, [], name, value)


                class Context(Entity):
                    """
                    Context Name
                    
                    .. attribute:: context_name  <key>
                    
                    	Context Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'snmp-agent-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Snmp.Vrfs.Vrf.Contexts.Context, self).__init__()

                        self.yang_name = "context"
                        self.yang_parent_name = "contexts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.context_name = YLeaf(YType.str, "context-name")
                        self._segment_path = lambda: "context" + "[context-name='" + self.context_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Vrfs.Vrf.Contexts.Context, ['context_name'], name, value)


            class TrapHosts(Entity):
                """
                Specify hosts to receive SNMP notifications
                
                .. attribute:: trap_host
                
                	Specify hosts to receive SNMP notifications
                	**type**\: list of    :py:class:`TrapHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost>`
                
                

                """

                _prefix = 'snmp-agent-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Snmp.Vrfs.Vrf.TrapHosts, self).__init__()

                    self.yang_name = "trap-hosts"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"trap-host" : ("trap_host", Snmp.Vrfs.Vrf.TrapHosts.TrapHost)}

                    self.trap_host = YList(self)
                    self._segment_path = lambda: "trap-hosts"

                def __setattr__(self, name, value):
                    self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts, [], name, value)


                class TrapHost(Entity):
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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost, self).__init__()

                        self.yang_name = "trap-host"
                        self.yang_parent_name = "trap-hosts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"default-user-communities" : ("default_user_communities", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities), "encrypted-user-communities" : ("encrypted_user_communities", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities), "inform-host" : ("inform_host", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost)}
                        self._child_list_classes = {}

                        self.ip_address = YLeaf(YType.str, "ip-address")

                        self.default_user_communities = Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities()
                        self.default_user_communities.parent = self
                        self._children_name_map["default_user_communities"] = "default-user-communities"
                        self._children_yang_names.add("default-user-communities")

                        self.encrypted_user_communities = Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities()
                        self.encrypted_user_communities.parent = self
                        self._children_name_map["encrypted_user_communities"] = "encrypted-user-communities"
                        self._children_yang_names.add("encrypted-user-communities")

                        self.inform_host = Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost()
                        self.inform_host.parent = self
                        self._children_name_map["inform_host"] = "inform-host"
                        self._children_yang_names.add("inform-host")
                        self._segment_path = lambda: "trap-host" + "[ip-address='" + self.ip_address.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost, ['ip_address'], name, value)


                    class DefaultUserCommunities(Entity):
                        """
                        Container class for defining communities for a
                        trap host
                        
                        .. attribute:: default_user_community
                        
                        	Unencrpted Community name associated with a trap host
                        	**type**\: list of    :py:class:`DefaultUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities, self).__init__()

                            self.yang_name = "default-user-communities"
                            self.yang_parent_name = "trap-host"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"default-user-community" : ("default_user_community", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity)}

                            self.default_user_community = YList(self)
                            self._segment_path = lambda: "default-user-communities"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities, [], name, value)


                        class DefaultUserCommunity(Entity):
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
                            	**type**\:   :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
                            
                            .. attribute:: version
                            
                            	SNMP Version to be used v1/v2c/v3
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity, self).__init__()

                                self.yang_name = "default-user-community"
                                self.yang_parent_name = "default-user-communities"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.community_name = YLeaf(YType.str, "community-name")

                                self.advanced_trap_types1 = YLeaf(YType.int32, "advanced-trap-types1")

                                self.advanced_trap_types2 = YLeaf(YType.int32, "advanced-trap-types2")

                                self.basic_trap_types = YLeaf(YType.int32, "basic-trap-types")

                                self.port = YLeaf(YType.uint16, "port")

                                self.security_level = YLeaf(YType.enumeration, "security-level")

                                self.version = YLeaf(YType.str, "version")
                                self._segment_path = lambda: "default-user-community" + "[community-name='" + self.community_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity, ['community_name', 'advanced_trap_types1', 'advanced_trap_types2', 'basic_trap_types', 'port', 'security_level', 'version'], name, value)


                    class EncryptedUserCommunities(Entity):
                        """
                        Container class for defining Clear/encrypt
                        communities for a trap host
                        
                        .. attribute:: encrypted_user_community
                        
                        	Clear/Encrypt Community name associated with a trap host
                        	**type**\: list of    :py:class:`EncryptedUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity>`
                        
                        

                        """

                        _prefix = 'snmp-agent-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities, self).__init__()

                            self.yang_name = "encrypted-user-communities"
                            self.yang_parent_name = "trap-host"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"encrypted-user-community" : ("encrypted_user_community", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity)}

                            self.encrypted_user_community = YList(self)
                            self._segment_path = lambda: "encrypted-user-communities"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities, [], name, value)


                        class EncryptedUserCommunity(Entity):
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
                            	**type**\:   :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
                            
                            .. attribute:: version
                            
                            	SNMP Version to be used v1/v2c/v3
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity, self).__init__()

                                self.yang_name = "encrypted-user-community"
                                self.yang_parent_name = "encrypted-user-communities"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.community_name = YLeaf(YType.str, "community-name")

                                self.advanced_trap_types1 = YLeaf(YType.int32, "advanced-trap-types1")

                                self.advanced_trap_types2 = YLeaf(YType.int32, "advanced-trap-types2")

                                self.basic_trap_types = YLeaf(YType.int32, "basic-trap-types")

                                self.port = YLeaf(YType.uint16, "port")

                                self.security_level = YLeaf(YType.enumeration, "security-level")

                                self.version = YLeaf(YType.str, "version")
                                self._segment_path = lambda: "encrypted-user-community" + "[community-name='" + self.community_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity, ['community_name', 'advanced_trap_types1', 'advanced_trap_types2', 'basic_trap_types', 'port', 'security_level', 'version'], name, value)


                    class InformHost(Entity):
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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost, self).__init__()

                            self.yang_name = "inform-host"
                            self.yang_parent_name = "trap-host"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"inform-encrypted-user-communities" : ("inform_encrypted_user_communities", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities), "inform-user-communities" : ("inform_user_communities", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities)}
                            self._child_list_classes = {}

                            self.inform_encrypted_user_communities = Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities()
                            self.inform_encrypted_user_communities.parent = self
                            self._children_name_map["inform_encrypted_user_communities"] = "inform-encrypted-user-communities"
                            self._children_yang_names.add("inform-encrypted-user-communities")

                            self.inform_user_communities = Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities()
                            self.inform_user_communities.parent = self
                            self._children_name_map["inform_user_communities"] = "inform-user-communities"
                            self._children_yang_names.add("inform-user-communities")
                            self._segment_path = lambda: "inform-host"


                        class InformEncryptedUserCommunities(Entity):
                            """
                            Container class for defining Clear/encrypt
                            communities for a inform host
                            
                            .. attribute:: inform_encrypted_user_community
                            
                            	Clear/Encrypt Community name associated with a inform host
                            	**type**\: list of    :py:class:`InformEncryptedUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity>`
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities, self).__init__()

                                self.yang_name = "inform-encrypted-user-communities"
                                self.yang_parent_name = "inform-host"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"inform-encrypted-user-community" : ("inform_encrypted_user_community", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity)}

                                self.inform_encrypted_user_community = YList(self)
                                self._segment_path = lambda: "inform-encrypted-user-communities"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities, [], name, value)


                            class InformEncryptedUserCommunity(Entity):
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
                                	**type**\:   :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
                                
                                .. attribute:: version
                                
                                	SNMP Version to be used v2c/v3
                                	**type**\:  str
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'snmp-agent-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity, self).__init__()

                                    self.yang_name = "inform-encrypted-user-community"
                                    self.yang_parent_name = "inform-encrypted-user-communities"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.community_name = YLeaf(YType.str, "community-name")

                                    self.advanced_trap_types1 = YLeaf(YType.int32, "advanced-trap-types1")

                                    self.advanced_trap_types2 = YLeaf(YType.int32, "advanced-trap-types2")

                                    self.basic_trap_types = YLeaf(YType.int32, "basic-trap-types")

                                    self.port = YLeaf(YType.uint16, "port")

                                    self.security_level = YLeaf(YType.enumeration, "security-level")

                                    self.version = YLeaf(YType.str, "version")
                                    self._segment_path = lambda: "inform-encrypted-user-community" + "[community-name='" + self.community_name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity, ['community_name', 'advanced_trap_types1', 'advanced_trap_types2', 'basic_trap_types', 'port', 'security_level', 'version'], name, value)


                        class InformUserCommunities(Entity):
                            """
                            Container class for defining communities for
                            a inform host
                            
                            .. attribute:: inform_user_community
                            
                            	Unencrpted Community name associated with a inform host
                            	**type**\: list of    :py:class:`InformUserCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity>`
                            
                            

                            """

                            _prefix = 'snmp-agent-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities, self).__init__()

                                self.yang_name = "inform-user-communities"
                                self.yang_parent_name = "inform-host"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"inform-user-community" : ("inform_user_community", Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity)}

                                self.inform_user_community = YList(self)
                                self._segment_path = lambda: "inform-user-communities"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities, [], name, value)


                            class InformUserCommunity(Entity):
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
                                	**type**\:   :py:class:`SnmpSecurityModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg.SnmpSecurityModel>`
                                
                                .. attribute:: version
                                
                                	SNMP Version to be used v2c/v3
                                	**type**\:  str
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'snmp-agent-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity, self).__init__()

                                    self.yang_name = "inform-user-community"
                                    self.yang_parent_name = "inform-user-communities"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.community_name = YLeaf(YType.str, "community-name")

                                    self.advanced_trap_types1 = YLeaf(YType.int32, "advanced-trap-types1")

                                    self.advanced_trap_types2 = YLeaf(YType.int32, "advanced-trap-types2")

                                    self.basic_trap_types = YLeaf(YType.int32, "basic-trap-types")

                                    self.port = YLeaf(YType.uint16, "port")

                                    self.security_level = YLeaf(YType.enumeration, "security-level")

                                    self.version = YLeaf(YType.str, "version")
                                    self._segment_path = lambda: "inform-user-community" + "[community-name='" + self.community_name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity, ['community_name', 'advanced_trap_types1', 'advanced_trap_types2', 'basic_trap_types', 'port', 'security_level', 'version'], name, value)

    def clone_ptr(self):
        self._top_entity = Snmp()
        return self._top_entity

