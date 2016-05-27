""" Cisco_IOS_XR_ip_bfd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-bfd package configuration.

This module contains definitions
for the following management objects\:
  bfd\: BFD Configuration

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class BfdBundleCoexistenceBobBlbEnum(Enum):
    """
    BfdBundleCoexistenceBobBlbEnum

    Bfd bundle coexistence bob blb

    .. data:: INHERITED = 1

    	Inherited coexistence mode

    .. data:: LOGICAL = 2

    	Logical coexistence mode

    """

    INHERITED = 1

    LOGICAL = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_bfd_cfg as meta
        return meta._meta_table['BfdBundleCoexistenceBobBlbEnum']


class BfdEchoStartupValidateEnum(Enum):
    """
    BfdEchoStartupValidateEnum

    Bfd echo startup validate

    .. data:: OFF = 0

    	Disable echo startup validation

    .. data:: ON = 1

    	Enable echo startup validation

    .. data:: FORCE = 2

    	Force echo startup validation

    """

    OFF = 0

    ON = 1

    FORCE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_bfd_cfg as meta
        return meta._meta_table['BfdEchoStartupValidateEnum']


class BfdIfEchoUsageEnum(Enum):
    """
    BfdIfEchoUsageEnum

    Bfd if echo usage

    .. data:: ENABLE = 0

    	Enable echo

    .. data:: DISABLE = 1

    	Disable echo

    """

    ENABLE = 0

    DISABLE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_bfd_cfg as meta
        return meta._meta_table['BfdIfEchoUsageEnum']


class BfdIfIpv6ChecksumUsageEnum(Enum):
    """
    BfdIfIpv6ChecksumUsageEnum

    Bfd if ipv6 checksum usage

    .. data:: DISABLE = 0

    	Disable IPv6 checksum

    .. data:: ENABLE = 1

    	Enable IPv6 checksum

    """

    DISABLE = 0

    ENABLE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_bfd_cfg as meta
        return meta._meta_table['BfdIfIpv6ChecksumUsageEnum']



class Bfd(object):
    """
    BFD Configuration
    
    .. attribute:: flap_damp
    
    	Flapping class container
    	**type**\: :py:class:`FlapDamp <ydk.models.ip.Cisco_IOS_XR_ip_bfd_cfg.Bfd.FlapDamp>`
    
    .. attribute:: echo_latency
    
    	BFD echo latency feature class container
    	**type**\: :py:class:`EchoLatency <ydk.models.ip.Cisco_IOS_XR_ip_bfd_cfg.Bfd.EchoLatency>`
    
    .. attribute:: echo_startup
    
    	BFD echo startup feature class container
    	**type**\: :py:class:`EchoStartup <ydk.models.ip.Cisco_IOS_XR_ip_bfd_cfg.Bfd.EchoStartup>`
    
    .. attribute:: interfaces
    
    	Interface configuration
    	**type**\: :py:class:`Interfaces <ydk.models.ip.Cisco_IOS_XR_ip_bfd_cfg.Bfd.Interfaces>`
    
    .. attribute:: multi_path_includes
    
    	Multipath Include configuration
    	**type**\: :py:class:`MultiPathIncludes <ydk.models.ip.Cisco_IOS_XR_ip_bfd_cfg.Bfd.MultiPathIncludes>`
    
    .. attribute:: bundle
    
    	Configuration related to BFD over Bundle
    	**type**\: :py:class:`Bundle <ydk.models.ip.Cisco_IOS_XR_ip_bfd_cfg.Bfd.Bundle>`
    
    .. attribute:: global_echo_usage
    
    	Echo configuration
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: ipv6_checksum_disable
    
    	To disable IPv6 checksum configuration
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: global_echo_min_interval
    
    	Configure echo min\-interval for bundle interface
    	**type**\: int
    
    	**range:** 15..2000
    
    .. attribute:: ttl_drop_threshold
    
    	Multihop TTL Drop Threshold
    	**type**\: int
    
    	**range:** 0..254
    
    .. attribute:: single_hop_trap
    
    	Single hop trap configuration
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: global_ipv4_echo_source
    
    	IPv4 echo source address configuration
    	**type**\: one of the below types:
    
    	**type**\: str
    
    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
    
    
    ----
    	**type**\: str
    
    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
    
    
    ----
    

    """

    _prefix = 'ip-bfd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.flap_damp = Bfd.FlapDamp()
        self.flap_damp.parent = self
        self.echo_latency = Bfd.EchoLatency()
        self.echo_latency.parent = self
        self.echo_startup = Bfd.EchoStartup()
        self.echo_startup.parent = self
        self.interfaces = Bfd.Interfaces()
        self.interfaces.parent = self
        self.multi_path_includes = Bfd.MultiPathIncludes()
        self.multi_path_includes.parent = self
        self.bundle = Bfd.Bundle()
        self.bundle.parent = self
        self.global_echo_usage = None
        self.ipv6_checksum_disable = None
        self.global_echo_min_interval = None
        self.ttl_drop_threshold = None
        self.single_hop_trap = None
        self.global_ipv4_echo_source = None


    class FlapDamp(object):
        """
        Flapping class container
        
        .. attribute:: bundle_member
        
        	Bundle per member feature class container
        	**type**\: :py:class:`BundleMember <ydk.models.ip.Cisco_IOS_XR_ip_bfd_cfg.Bfd.FlapDamp.BundleMember>`
        
        .. attribute:: extensions
        
        	Extensions to the BFD dampening feature
        	**type**\: :py:class:`Extensions <ydk.models.ip.Cisco_IOS_XR_ip_bfd_cfg.Bfd.FlapDamp.Extensions>`
        
        .. attribute:: threshold
        
        	Stability threshold to enable dampening
        	**type**\: int
        
        	**range:** 60000..3600000
        
        .. attribute:: initial_delay
        
        	Initial delay before bringing up session
        	**type**\: int
        
        	**range:** 1..3600000
        
        .. attribute:: maximum_delay
        
        	Maximum delay before bringing up session
        	**type**\: int
        
        	**range:** 1..3600000
        
        .. attribute:: secondary_delay
        
        	Secondary delay before bringing up session
        	**type**\: int
        
        	**range:** 1..3600000
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.bundle_member = Bfd.FlapDamp.BundleMember()
            self.bundle_member.parent = self
            self.extensions = Bfd.FlapDamp.Extensions()
            self.extensions.parent = self
            self.threshold = None
            self.initial_delay = None
            self.maximum_delay = None
            self.secondary_delay = None


        class BundleMember(object):
            """
            Bundle per member feature class container
            
            .. attribute:: initial_delay
            
            	Initial delay before bringing up session
            	**type**\: int
            
            	**range:** 1..518400000
            
            .. attribute:: maximum_delay
            
            	Maximum delay before bringing up session
            	**type**\: int
            
            	**range:** 1..518400000
            
            .. attribute:: secondary_delay
            
            	Secondary delay before bringing up session
            	**type**\: int
            
            	**range:** 1..518400000
            
            .. attribute:: l3_only_mode
            
            	Apply immediate dampening and only when failure is L3 specific
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.initial_delay = None
                self.maximum_delay = None
                self.secondary_delay = None
                self.l3_only_mode = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-bfd-cfg:bfd/Cisco-IOS-XR-ip-bfd-cfg:flap-damp/Cisco-IOS-XR-ip-bfd-cfg:bundle-member'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.initial_delay is not None:
                    return True

                if self.maximum_delay is not None:
                    return True

                if self.secondary_delay is not None:
                    return True

                if self.l3_only_mode is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_bfd_cfg as meta
                return meta._meta_table['Bfd.FlapDamp.BundleMember']['meta_info']


        class Extensions(object):
            """
            Extensions to the BFD dampening feature
            
            .. attribute:: down_monitor
            
            	If set, DOWN state monitoring mode is enabled
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.down_monitor = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-bfd-cfg:bfd/Cisco-IOS-XR-ip-bfd-cfg:flap-damp/Cisco-IOS-XR-ip-bfd-cfg:extensions'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.down_monitor is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_bfd_cfg as meta
                return meta._meta_table['Bfd.FlapDamp.Extensions']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-bfd-cfg:bfd/Cisco-IOS-XR-ip-bfd-cfg:flap-damp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.bundle_member is not None and self.bundle_member._has_data():
                return True

            if self.extensions is not None and self.extensions._has_data():
                return True

            if self.threshold is not None:
                return True

            if self.initial_delay is not None:
                return True

            if self.maximum_delay is not None:
                return True

            if self.secondary_delay is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_bfd_cfg as meta
            return meta._meta_table['Bfd.FlapDamp']['meta_info']


    class EchoLatency(object):
        """
        BFD echo latency feature class container
        
        .. attribute:: detect
        
        	BFD echo latency detection
        	**type**\: :py:class:`Detect <ydk.models.ip.Cisco_IOS_XR_ip_bfd_cfg.Bfd.EchoLatency.Detect>`
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.detect = Bfd.EchoLatency.Detect()
            self.detect.parent = self


        class Detect(object):
            """
            BFD echo latency detection
            
            .. attribute:: latency_detect_enabled
            
            	If set, echo latency detect is enabled
            	**type**\: bool
            
            .. attribute:: latency_detect_percentage
            
            	Echo latency detect percentage
            	**type**\: int
            
            	**range:** 100..250
            
            .. attribute:: latency_detect_count
            
            	Echo latency detect count
            	**type**\: int
            
            	**range:** 1..10
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.latency_detect_enabled = None
                self.latency_detect_percentage = None
                self.latency_detect_count = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-bfd-cfg:bfd/Cisco-IOS-XR-ip-bfd-cfg:echo-latency/Cisco-IOS-XR-ip-bfd-cfg:detect'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.latency_detect_enabled is not None:
                    return True

                if self.latency_detect_percentage is not None:
                    return True

                if self.latency_detect_count is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_bfd_cfg as meta
                return meta._meta_table['Bfd.EchoLatency.Detect']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-bfd-cfg:bfd/Cisco-IOS-XR-ip-bfd-cfg:echo-latency'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.detect is not None and self.detect._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_bfd_cfg as meta
            return meta._meta_table['Bfd.EchoLatency']['meta_info']


    class EchoStartup(object):
        """
        BFD echo startup feature class container
        
        .. attribute:: validate
        
        	BFD echo validation prior to session bringup
        	**type**\: :py:class:`BfdEchoStartupValidateEnum <ydk.models.ip.Cisco_IOS_XR_ip_bfd_cfg.BfdEchoStartupValidateEnum>`
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.validate = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-bfd-cfg:bfd/Cisco-IOS-XR-ip-bfd-cfg:echo-startup'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.validate is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_bfd_cfg as meta
            return meta._meta_table['Bfd.EchoStartup']['meta_info']


    class Interfaces(object):
        """
        Interface configuration
        
        .. attribute:: interface
        
        	Single interface configuration
        	**type**\: list of :py:class:`Interface <ydk.models.ip.Cisco_IOS_XR_ip_bfd_cfg.Bfd.Interfaces.Interface>`
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            Single interface configuration
            
            .. attribute:: interface_name  <key>
            
            	Interface Name
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: interface_echo_usage
            
            	Echo usage for this interface
            	**type**\: :py:class:`BfdIfEchoUsageEnum <ydk.models.ip.Cisco_IOS_XR_ip_bfd_cfg.BfdIfEchoUsageEnum>`
            
            .. attribute:: ipv6_checksum
            
            	IPv6 checksum usage for this interface \- Interface config will always take precedence over global config
            	**type**\: :py:class:`BfdIfIpv6ChecksumUsageEnum <ydk.models.ip.Cisco_IOS_XR_ip_bfd_cfg.BfdIfIpv6ChecksumUsageEnum>`
            
            .. attribute:: interface_ipv4_echo_source
            
            	Interface IPv4 echo source address configuration
            	**type**\: one of the below types:
            
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\: str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.interface_echo_usage = None
                self.ipv6_checksum = None
                self.interface_ipv4_echo_source = None

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYDataValidationError('Key property interface_name is None')

                return '/Cisco-IOS-XR-ip-bfd-cfg:bfd/Cisco-IOS-XR-ip-bfd-cfg:interfaces/Cisco-IOS-XR-ip-bfd-cfg:interface[Cisco-IOS-XR-ip-bfd-cfg:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.interface_name is not None:
                    return True

                if self.interface_echo_usage is not None:
                    return True

                if self.ipv6_checksum is not None:
                    return True

                if self.interface_ipv4_echo_source is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_bfd_cfg as meta
                return meta._meta_table['Bfd.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-bfd-cfg:bfd/Cisco-IOS-XR-ip-bfd-cfg:interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.interface is not None:
                for child_ref in self.interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_bfd_cfg as meta
            return meta._meta_table['Bfd.Interfaces']['meta_info']


    class MultiPathIncludes(object):
        """
        Multipath Include configuration
        
        .. attribute:: multi_path_include
        
        	Location configuration
        	**type**\: list of :py:class:`MultiPathInclude <ydk.models.ip.Cisco_IOS_XR_ip_bfd_cfg.Bfd.MultiPathIncludes.MultiPathInclude>`
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.multi_path_include = YList()
            self.multi_path_include.parent = self
            self.multi_path_include.name = 'multi_path_include'


        class MultiPathInclude(object):
            """
            Location configuration
            
            .. attribute:: location  <key>
            
            	Location
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.location = None

            @property
            def _common_path(self):
                if self.location is None:
                    raise YPYDataValidationError('Key property location is None')

                return '/Cisco-IOS-XR-ip-bfd-cfg:bfd/Cisco-IOS-XR-ip-bfd-cfg:multi-path-includes/Cisco-IOS-XR-ip-bfd-cfg:multi-path-include[Cisco-IOS-XR-ip-bfd-cfg:location = ' + str(self.location) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.location is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_bfd_cfg as meta
                return meta._meta_table['Bfd.MultiPathIncludes.MultiPathInclude']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-bfd-cfg:bfd/Cisco-IOS-XR-ip-bfd-cfg:multi-path-includes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.multi_path_include is not None:
                for child_ref in self.multi_path_include:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_bfd_cfg as meta
            return meta._meta_table['Bfd.MultiPathIncludes']['meta_info']


    class Bundle(object):
        """
        Configuration related to BFD over Bundle
        
        .. attribute:: coexistence
        
        	Coexistence mode for BFD on bundle feature
        	**type**\: :py:class:`Coexistence <ydk.models.ip.Cisco_IOS_XR_ip_bfd_cfg.Bfd.Bundle.Coexistence>`
        
        

        """

        _prefix = 'ip-bfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.coexistence = Bfd.Bundle.Coexistence()
            self.coexistence.parent = self


        class Coexistence(object):
            """
            Coexistence mode for BFD on bundle feature
            
            .. attribute:: bob_blb
            
            	Coexistence mode for BoB and BLB feature
            	**type**\: :py:class:`BfdBundleCoexistenceBobBlbEnum <ydk.models.ip.Cisco_IOS_XR_ip_bfd_cfg.BfdBundleCoexistenceBobBlbEnum>`
            
            

            """

            _prefix = 'ip-bfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bob_blb = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-bfd-cfg:bfd/Cisco-IOS-XR-ip-bfd-cfg:bundle/Cisco-IOS-XR-ip-bfd-cfg:coexistence'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.bob_blb is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_bfd_cfg as meta
                return meta._meta_table['Bfd.Bundle.Coexistence']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-bfd-cfg:bfd/Cisco-IOS-XR-ip-bfd-cfg:bundle'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.coexistence is not None and self.coexistence._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_bfd_cfg as meta
            return meta._meta_table['Bfd.Bundle']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-bfd-cfg:bfd'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.flap_damp is not None and self.flap_damp._has_data():
            return True

        if self.echo_latency is not None and self.echo_latency._has_data():
            return True

        if self.echo_startup is not None and self.echo_startup._has_data():
            return True

        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.multi_path_includes is not None and self.multi_path_includes._has_data():
            return True

        if self.bundle is not None and self.bundle._has_data():
            return True

        if self.global_echo_usage is not None:
            return True

        if self.ipv6_checksum_disable is not None:
            return True

        if self.global_echo_min_interval is not None:
            return True

        if self.ttl_drop_threshold is not None:
            return True

        if self.single_hop_trap is not None:
            return True

        if self.global_ipv4_echo_source is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_bfd_cfg as meta
        return meta._meta_table['Bfd']['meta_info']


