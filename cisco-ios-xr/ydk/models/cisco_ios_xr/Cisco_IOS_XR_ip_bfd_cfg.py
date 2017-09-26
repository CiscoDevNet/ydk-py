""" Cisco_IOS_XR_ip_bfd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-bfd package configuration.

This module contains definitions
for the following management objects\:
  bfd\: BFD Configuration

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BfdBundleCoexistenceBobBlb(Enum):
    """
    BfdBundleCoexistenceBobBlb

    Bfd bundle coexistence bob blb

    .. data:: inherited = 1

    	Inherited coexistence mode

    .. data:: logical = 2

    	Logical coexistence mode

    """

    inherited = Enum.YLeaf(1, "inherited")

    logical = Enum.YLeaf(2, "logical")


class BfdEchoStartupValidate(Enum):
    """
    BfdEchoStartupValidate

    Bfd echo startup validate

    .. data:: off = 0

    	Disable echo startup validation

    .. data:: on = 1

    	Enable echo startup validation

    .. data:: force = 2

    	Force echo startup validation

    """

    off = Enum.YLeaf(0, "off")

    on = Enum.YLeaf(1, "on")

    force = Enum.YLeaf(2, "force")


class BfdIfEchoUsage(Enum):
    """
    BfdIfEchoUsage

    Bfd if echo usage

    .. data:: enable = 0

    	Enable echo

    .. data:: disable = 1

    	Disable echo

    """

    enable = Enum.YLeaf(0, "enable")

    disable = Enum.YLeaf(1, "disable")


class BfdIfIpv6ChecksumUsage(Enum):
    """
    BfdIfIpv6ChecksumUsage

    Bfd if ipv6 checksum usage

    .. data:: disable = 0

    	Disable IPv6 checksum

    .. data:: enable = 1

    	Enable IPv6 checksum

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")



class Bfd(Entity):
    """
    BFD Configuration
    
    .. attribute:: bundle
    
    	Configuration related to BFD over Bundle
    	**type**\:   :py:class:`Bundle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.Bundle>`
    
    .. attribute:: echo_latency
    
    	BFD echo latency feature class container
    	**type**\:   :py:class:`EchoLatency <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.EchoLatency>`
    
    .. attribute:: echo_startup
    
    	BFD echo startup feature class container
    	**type**\:   :py:class:`EchoStartup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.EchoStartup>`
    
    .. attribute:: flap_damp
    
    	Flapping class container
    	**type**\:   :py:class:`FlapDamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.FlapDamp>`
    
    .. attribute:: global_echo_min_interval
    
    	Configure echo min\-interval for bundle interface
    	**type**\:  int
    
    	**range:** 15..2000
    
    	**units**\: millisecond
    
    	**default value**\: 15
    
    .. attribute:: global_echo_usage
    
    	Echo configuration
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: global_ipv4_echo_source
    
    	IPv4 echo source address configuration
    	**type**\: one of the below types:
    
    	**type**\:  str
    
    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
    
    
    ----
    	**type**\:  str
    
    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
    
    
    ----
    .. attribute:: interfaces
    
    	Interface configuration
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.Interfaces>`
    
    .. attribute:: ipv6_checksum_disable
    
    	To disable IPv6 checksum configuration
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: multi_path_includes
    
    	Multipath Include configuration
    	**type**\:   :py:class:`MultiPathIncludes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.MultiPathIncludes>`
    
    .. attribute:: single_hop_trap
    
    	Single hop trap configuration
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: ttl_drop_threshold
    
    	Multihop TTL Drop Threshold
    	**type**\:  int
    
    	**range:** 0..254
    
    

    """

    _prefix = 'ip-bfd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Bfd, self).__init__()
        self._top_entity = None

        self.yang_name = "bfd"
        self.yang_parent_name = "Cisco-IOS-XR-ip-bfd-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"bundle" : ("bundle", Bfd.Bundle), "echo-latency" : ("echo_latency", Bfd.EchoLatency), "echo-startup" : ("echo_startup", Bfd.EchoStartup), "flap-damp" : ("flap_damp", Bfd.FlapDamp), "interfaces" : ("interfaces", Bfd.Interfaces), "multi-path-includes" : ("multi_path_includes", Bfd.MultiPathIncludes)}
        self._child_list_classes = {}

        self.global_echo_min_interval = YLeaf(YType.uint32, "global-echo-min-interval")

        self.global_echo_usage = YLeaf(YType.empty, "global-echo-usage")

        self.global_ipv4_echo_source = YLeaf(YType.str, "global-ipv4-echo-source")

        self.ipv6_checksum_disable = YLeaf(YType.empty, "ipv6-checksum-disable")

        self.single_hop_trap = YLeaf(YType.empty, "single-hop-trap")

        self.ttl_drop_threshold = YLeaf(YType.uint32, "ttl-drop-threshold")

        self.bundle = Bfd.Bundle()
        self.bundle.parent = self
        self._children_name_map["bundle"] = "bundle"
        self._children_yang_names.add("bundle")

        self.echo_latency = Bfd.EchoLatency()
        self.echo_latency.parent = self
        self._children_name_map["echo_latency"] = "echo-latency"
        self._children_yang_names.add("echo-latency")

        self.echo_startup = Bfd.EchoStartup()
        self.echo_startup.parent = self
        self._children_name_map["echo_startup"] = "echo-startup"
        self._children_yang_names.add("echo-startup")

        self.flap_damp = Bfd.FlapDamp()
        self.flap_damp.parent = self
        self._children_name_map["flap_damp"] = "flap-damp"
        self._children_yang_names.add("flap-damp")

        self.interfaces = Bfd.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.multi_path_includes = Bfd.MultiPathIncludes()
        self.multi_path_includes.parent = self
        self._children_name_map["multi_path_includes"] = "multi-path-includes"
        self._children_yang_names.add("multi-path-includes")
        self._segment_path = lambda: "Cisco-IOS-XR-ip-bfd-cfg:bfd"

    def __setattr__(self, name, value):
        self._perform_setattr(Bfd, ['global_echo_min_interval', 'global_echo_usage', 'global_ipv4_echo_source', 'ipv6_checksum_disable', 'single_hop_trap', 'ttl_drop_threshold'], name, value)


    class Bundle(Entity):
        """
        Configuration related to BFD over Bundle
        
        .. attribute:: coexistence
        
        	Coexistence mode for BFD on bundle feature
        	**type**\:   :py:class:`Coexistence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.Bundle.Coexistence>`
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Bfd.Bundle, self).__init__()

            self.yang_name = "bundle"
            self.yang_parent_name = "bfd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"coexistence" : ("coexistence", Bfd.Bundle.Coexistence)}
            self._child_list_classes = {}

            self.coexistence = Bfd.Bundle.Coexistence()
            self.coexistence.parent = self
            self._children_name_map["coexistence"] = "coexistence"
            self._children_yang_names.add("coexistence")
            self._segment_path = lambda: "bundle"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-bfd-cfg:bfd/%s" % self._segment_path()


        class Coexistence(Entity):
            """
            Coexistence mode for BFD on bundle feature
            
            .. attribute:: bob_blb
            
            	Coexistence mode for BoB and BLB feature
            	**type**\:   :py:class:`BfdBundleCoexistenceBobBlb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.BfdBundleCoexistenceBobBlb>`
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Bfd.Bundle.Coexistence, self).__init__()

                self.yang_name = "coexistence"
                self.yang_parent_name = "bundle"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.bob_blb = YLeaf(YType.enumeration, "bob-blb")
                self._segment_path = lambda: "coexistence"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-bfd-cfg:bfd/bundle/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Bfd.Bundle.Coexistence, ['bob_blb'], name, value)


    class EchoLatency(Entity):
        """
        BFD echo latency feature class container
        
        .. attribute:: detect
        
        	BFD echo latency detection
        	**type**\:   :py:class:`Detect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.EchoLatency.Detect>`
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Bfd.EchoLatency, self).__init__()

            self.yang_name = "echo-latency"
            self.yang_parent_name = "bfd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"detect" : ("detect", Bfd.EchoLatency.Detect)}
            self._child_list_classes = {}

            self.detect = Bfd.EchoLatency.Detect()
            self.detect.parent = self
            self._children_name_map["detect"] = "detect"
            self._children_yang_names.add("detect")
            self._segment_path = lambda: "echo-latency"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-bfd-cfg:bfd/%s" % self._segment_path()


        class Detect(Entity):
            """
            BFD echo latency detection
            
            .. attribute:: latency_detect_count
            
            	Echo latency detect count
            	**type**\:  int
            
            	**range:** 1..10
            
            	**default value**\: 1
            
            .. attribute:: latency_detect_enabled
            
            	If set, echo latency detect is enabled
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: latency_detect_percentage
            
            	Echo latency detect percentage
            	**type**\:  int
            
            	**range:** 100..250
            
            	**units**\: percentage
            
            	**default value**\: 100
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Bfd.EchoLatency.Detect, self).__init__()

                self.yang_name = "detect"
                self.yang_parent_name = "echo-latency"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.latency_detect_count = YLeaf(YType.uint32, "latency-detect-count")

                self.latency_detect_enabled = YLeaf(YType.boolean, "latency-detect-enabled")

                self.latency_detect_percentage = YLeaf(YType.uint32, "latency-detect-percentage")
                self._segment_path = lambda: "detect"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-bfd-cfg:bfd/echo-latency/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Bfd.EchoLatency.Detect, ['latency_detect_count', 'latency_detect_enabled', 'latency_detect_percentage'], name, value)


    class EchoStartup(Entity):
        """
        BFD echo startup feature class container
        
        .. attribute:: validate
        
        	BFD echo validation prior to session bringup
        	**type**\:   :py:class:`BfdEchoStartupValidate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.BfdEchoStartupValidate>`
        
        	**default value**\: off
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Bfd.EchoStartup, self).__init__()

            self.yang_name = "echo-startup"
            self.yang_parent_name = "bfd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.validate = YLeaf(YType.enumeration, "validate")
            self._segment_path = lambda: "echo-startup"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-bfd-cfg:bfd/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Bfd.EchoStartup, ['validate'], name, value)


    class FlapDamp(Entity):
        """
        Flapping class container
        
        .. attribute:: bundle_member
        
        	Bundle per member feature class container
        	**type**\:   :py:class:`BundleMember <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.FlapDamp.BundleMember>`
        
        .. attribute:: dampen_disable
        
        	Dampening Enable/Disable
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: extensions
        
        	Extensions to the BFD dampening feature
        	**type**\:   :py:class:`Extensions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.FlapDamp.Extensions>`
        
        .. attribute:: initial_delay
        
        	Initial delay before bringing up session
        	**type**\:  int
        
        	**range:** 1..3600000
        
        	**units**\: millisecond
        
        	**default value**\: 2000
        
        .. attribute:: maximum_delay
        
        	Maximum delay before bringing up session
        	**type**\:  int
        
        	**range:** 1..3600000
        
        	**units**\: millisecond
        
        	**default value**\: 120000
        
        .. attribute:: secondary_delay
        
        	Secondary delay before bringing up session
        	**type**\:  int
        
        	**range:** 1..3600000
        
        	**units**\: millisecond
        
        	**default value**\: 5000
        
        .. attribute:: threshold
        
        	Stability threshold to enable dampening
        	**type**\:  int
        
        	**range:** 60000..3600000
        
        	**units**\: millisecond
        
        	**default value**\: 120000
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Bfd.FlapDamp, self).__init__()

            self.yang_name = "flap-damp"
            self.yang_parent_name = "bfd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"bundle-member" : ("bundle_member", Bfd.FlapDamp.BundleMember), "extensions" : ("extensions", Bfd.FlapDamp.Extensions)}
            self._child_list_classes = {}

            self.dampen_disable = YLeaf(YType.empty, "dampen-disable")

            self.initial_delay = YLeaf(YType.uint32, "initial-delay")

            self.maximum_delay = YLeaf(YType.uint32, "maximum-delay")

            self.secondary_delay = YLeaf(YType.uint32, "secondary-delay")

            self.threshold = YLeaf(YType.uint32, "threshold")

            self.bundle_member = Bfd.FlapDamp.BundleMember()
            self.bundle_member.parent = self
            self._children_name_map["bundle_member"] = "bundle-member"
            self._children_yang_names.add("bundle-member")

            self.extensions = Bfd.FlapDamp.Extensions()
            self.extensions.parent = self
            self._children_name_map["extensions"] = "extensions"
            self._children_yang_names.add("extensions")
            self._segment_path = lambda: "flap-damp"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-bfd-cfg:bfd/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Bfd.FlapDamp, ['dampen_disable', 'initial_delay', 'maximum_delay', 'secondary_delay', 'threshold'], name, value)


        class BundleMember(Entity):
            """
            Bundle per member feature class container
            
            .. attribute:: initial_delay
            
            	Initial delay before bringing up session
            	**type**\:  int
            
            	**range:** 1..518400000
            
            	**units**\: millisecond
            
            	**default value**\: 16000
            
            .. attribute:: l3_only_mode
            
            	Apply immediate dampening and only when failure is L3 specific
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: maximum_delay
            
            	Maximum delay before bringing up session
            	**type**\:  int
            
            	**range:** 1..518400000
            
            	**units**\: millisecond
            
            	**default value**\: 600000
            
            .. attribute:: secondary_delay
            
            	Secondary delay before bringing up session
            	**type**\:  int
            
            	**range:** 1..518400000
            
            	**units**\: millisecond
            
            	**default value**\: 20000
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Bfd.FlapDamp.BundleMember, self).__init__()

                self.yang_name = "bundle-member"
                self.yang_parent_name = "flap-damp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.initial_delay = YLeaf(YType.uint32, "initial-delay")

                self.l3_only_mode = YLeaf(YType.empty, "l3-only-mode")

                self.maximum_delay = YLeaf(YType.uint32, "maximum-delay")

                self.secondary_delay = YLeaf(YType.uint32, "secondary-delay")
                self._segment_path = lambda: "bundle-member"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-bfd-cfg:bfd/flap-damp/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Bfd.FlapDamp.BundleMember, ['initial_delay', 'l3_only_mode', 'maximum_delay', 'secondary_delay'], name, value)


        class Extensions(Entity):
            """
            Extensions to the BFD dampening feature
            
            .. attribute:: down_monitor
            
            	If set, DOWN state monitoring mode is enabled
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Bfd.FlapDamp.Extensions, self).__init__()

                self.yang_name = "extensions"
                self.yang_parent_name = "flap-damp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.down_monitor = YLeaf(YType.empty, "down-monitor")
                self._segment_path = lambda: "extensions"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-bfd-cfg:bfd/flap-damp/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Bfd.FlapDamp.Extensions, ['down_monitor'], name, value)


    class Interfaces(Entity):
        """
        Interface configuration
        
        .. attribute:: interface
        
        	Single interface configuration
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.Interfaces.Interface>`
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Bfd.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "bfd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", Bfd.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-bfd-cfg:bfd/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Bfd.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Single interface configuration
            
            .. attribute:: interface_name  <key>
            
            	Interface Name
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: interface_echo_usage
            
            	Echo usage for this interface
            	**type**\:   :py:class:`BfdIfEchoUsage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.BfdIfEchoUsage>`
            
            	**default value**\: enable
            
            .. attribute:: interface_ipv4_echo_source
            
            	Interface IPv4 echo source address configuration
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: ipv6_checksum
            
            	IPv6 checksum usage for this interface \- Interface config will always take precedence over global config
            	**type**\:   :py:class:`BfdIfIpv6ChecksumUsage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.BfdIfIpv6ChecksumUsage>`
            
            	**default value**\: enable
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Bfd.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.interface_echo_usage = YLeaf(YType.enumeration, "interface-echo-usage")

                self.interface_ipv4_echo_source = YLeaf(YType.str, "interface-ipv4-echo-source")

                self.ipv6_checksum = YLeaf(YType.enumeration, "ipv6-checksum")
                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-bfd-cfg:bfd/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Bfd.Interfaces.Interface, ['interface_name', 'interface_echo_usage', 'interface_ipv4_echo_source', 'ipv6_checksum'], name, value)


    class MultiPathIncludes(Entity):
        """
        Multipath Include configuration
        
        .. attribute:: multi_path_include
        
        	Location configuration
        	**type**\: list of    :py:class:`MultiPathInclude <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_bfd_cfg.Bfd.MultiPathIncludes.MultiPathInclude>`
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Bfd.MultiPathIncludes, self).__init__()

            self.yang_name = "multi-path-includes"
            self.yang_parent_name = "bfd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"multi-path-include" : ("multi_path_include", Bfd.MultiPathIncludes.MultiPathInclude)}

            self.multi_path_include = YList(self)
            self._segment_path = lambda: "multi-path-includes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-bfd-cfg:bfd/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Bfd.MultiPathIncludes, [], name, value)


        class MultiPathInclude(Entity):
            """
            Location configuration
            
            .. attribute:: location  <key>
            
            	Location
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Bfd.MultiPathIncludes.MultiPathInclude, self).__init__()

                self.yang_name = "multi-path-include"
                self.yang_parent_name = "multi-path-includes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.location = YLeaf(YType.str, "location")
                self._segment_path = lambda: "multi-path-include" + "[location='" + self.location.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-bfd-cfg:bfd/multi-path-includes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Bfd.MultiPathIncludes.MultiPathInclude, ['location'], name, value)

    def clone_ptr(self):
        self._top_entity = Bfd()
        return self._top_entity

