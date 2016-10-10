""" Cisco_IOS_XR_ipv4_dhcpd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-dhcpd package configuration.

This module contains definitions
for the following management objects\:
  ipv4\-dhcpd\: DHCP IPV4 configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class Ipv4DhcpdBroadcastFlagPolicyEnum(Enum):
    """
    Ipv4DhcpdBroadcastFlagPolicyEnum

    Ipv4dhcpd broadcast flag policy

    .. data:: IGNORE = 0

    	Ignore

    .. data:: CHECK = 1

    	check

    .. data:: UNICAST_ALWAYS = 2

    	Unicast always

    """

    IGNORE = 0

    CHECK = 1

    UNICAST_ALWAYS = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Ipv4DhcpdBroadcastFlagPolicyEnum']


class Ipv4DhcpdFmtEnum(Enum):
    """
    Ipv4DhcpdFmtEnum

    Ipv4dhcpd fmt

    .. data:: NO_FORMAT = 0

    	Not a Format String

    .. data:: FORMAT = 1

    	Format String

    """

    NO_FORMAT = 0

    FORMAT = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Ipv4DhcpdFmtEnum']


class Ipv4DhcpdFmtSpecifierEnum(Enum):
    """
    Ipv4DhcpdFmtSpecifierEnum

    Ipv4dhcpd fmt specifier

    .. data:: PHYSICAL_CHASSIS = 1

    	Physical chassis

    .. data:: PHYSICAL_SLOT = 2

    	Physical slot

    .. data:: PHYSICAL_SUB_SLOT = 3

    	Physical sub-slot

    .. data:: PHYSICAL_PORT = 4

    	Physical port

    .. data:: PHYSICAL_SUB_PORT = 5

    	Physical sub-port

    .. data:: INNER_VLAN_ID = 6

    	Inner VLAN ID

    .. data:: OUTER_VLAN_ID = 7

    	Outer VLAN ID

    .. data:: L2_INTERFACE = 8

    	L2 Interface

    """

    PHYSICAL_CHASSIS = 1

    PHYSICAL_SLOT = 2

    PHYSICAL_SUB_SLOT = 3

    PHYSICAL_PORT = 4

    PHYSICAL_SUB_PORT = 5

    INNER_VLAN_ID = 6

    OUTER_VLAN_ID = 7

    L2_INTERFACE = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Ipv4DhcpdFmtSpecifierEnum']


class Ipv4DhcpdGiaddrPolicyEnum(Enum):
    """
    Ipv4DhcpdGiaddrPolicyEnum

    Ipv4dhcpd giaddr policy

    .. data:: KEEP = 0

    	Keep

    .. data:: REPLACE = 1

    	Replace

    .. data:: DROP = 2

    	Drop

    """

    KEEP = 0

    REPLACE = 1

    DROP = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Ipv4DhcpdGiaddrPolicyEnum']


class Ipv4DhcpdModeEnum(Enum):
    """
    Ipv4DhcpdModeEnum

    Ipv4dhcpd mode

    .. data:: BASE = 0

    	Base

    .. data:: RELAY = 1

    	Relay

    .. data:: SNOOP = 2

    	Snoop

    .. data:: SERVER = 3

    	Server

    .. data:: PROXY = 4

    	Proxy

    .. data:: BASE2 = 5

    	Base2

    """

    BASE = 0

    RELAY = 1

    SNOOP = 2

    SERVER = 3

    PROXY = 4

    BASE2 = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Ipv4DhcpdModeEnum']


class Ipv4DhcpdRelayInfoOptionPolicyEnum(Enum):
    """
    Ipv4DhcpdRelayInfoOptionPolicyEnum

    Ipv4dhcpd relay info option policy

    .. data:: REPLACE = 0

    	Replace

    .. data:: KEEP = 1

    	Keep

    .. data:: DROP = 2

    	Drop

    .. data:: ENCAPSULATE = 3

    	Encapsulate

    """

    REPLACE = 0

    KEEP = 1

    DROP = 2

    ENCAPSULATE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Ipv4DhcpdRelayInfoOptionPolicyEnum']


class Ipv4DhcpdRelayInfoOptionvpnModeEnum(Enum):
    """
    Ipv4DhcpdRelayInfoOptionvpnModeEnum

    Ipv4dhcpd relay info optionvpn mode

    .. data:: RFC = 0

    	RFC

    .. data:: CISCO = 1

    	Cisco

    """

    RFC = 0

    CISCO = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Ipv4DhcpdRelayInfoOptionvpnModeEnum']



class Ipv4Dhcpd(object):
    """
    DHCP IPV4 configuration
    
    .. attribute:: allow_client_id_change
    
    	For BNG session, allow client id change for a client MAC
    	**type**\:  :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: database
    
    	Enable DHCP binding database storage to file system
    	**type**\:  :py:class:`Database <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Database>`
    
    .. attribute:: duplicate_mac_allowed
    
    	Allow Duplicate MAC Address
    	**type**\:  :py:class:`DuplicateMacAllowed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.DuplicateMacAllowed>`
    
    .. attribute:: enable
    
    	DHCP IPV4 configuration
    	**type**\:  :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: interfaces
    
    	DHCP IPV4 Interface Table
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces>`
    
    .. attribute:: profiles
    
    	DHCP IPV4 Profile Table
    	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles>`
    
    .. attribute:: rate_limit
    
    	Rate limit ingress packets
    	**type**\:  :py:class:`RateLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.RateLimit>`
    
    .. attribute:: vrfs
    
    	VRF Table
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Vrfs>`
    
    

    """

    _prefix = 'ipv4-dhcpd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.allow_client_id_change = None
        self.database = Ipv4Dhcpd.Database()
        self.database.parent = self
        self.duplicate_mac_allowed = None
        self.enable = None
        self.interfaces = Ipv4Dhcpd.Interfaces()
        self.interfaces.parent = self
        self.profiles = Ipv4Dhcpd.Profiles()
        self.profiles.parent = self
        self.rate_limit = Ipv4Dhcpd.RateLimit()
        self.rate_limit.parent = self
        self.vrfs = Ipv4Dhcpd.Vrfs()
        self.vrfs.parent = self


    class Vrfs(object):
        """
        VRF Table
        
        .. attribute:: vrf
        
        	VRF table
        	**type**\: list of  :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
            """
            VRF table
            
            .. attribute:: vrf_name  <key>
            
            	VRF Name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: profile
            
            	Profile name and mode
            	**type**\:  :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Vrfs.Vrf.Profile>`
            
            

            """

            _prefix = 'ipv4-dhcpd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.profile = None


            class Profile(object):
                """
                Profile name and mode
                
                .. attribute:: mode
                
                	Dhcp mode
                	**type**\:  :py:class:`Ipv4DhcpdModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdModeEnum>`
                
                	**mandatory**\: True
                
                .. attribute:: vrf_profile_name
                
                	Profile name
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.mode = None
                    self.vrf_profile_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:profile'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self._is_presence:
                        return True
                    if self.mode is not None:
                        return True

                    if self.vrf_profile_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                    return meta._meta_table['Ipv4Dhcpd.Vrfs.Vrf.Profile']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-cfg:vrfs/Cisco-IOS-XR-ipv4-dhcpd-cfg:vrf[Cisco-IOS-XR-ipv4-dhcpd-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.vrf_name is not None:
                    return True

                if self.profile is not None and self.profile._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                return meta._meta_table['Ipv4Dhcpd.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-cfg:vrfs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.vrf is not None:
                for child_ref in self.vrf:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
            return meta._meta_table['Ipv4Dhcpd.Vrfs']['meta_info']


    class Profiles(object):
        """
        DHCP IPV4 Profile Table
        
        .. attribute:: profile
        
        	DHCP IPV4 Profile
        	**type**\: list of  :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile>`
        
        

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.profile = YList()
            self.profile.parent = self
            self.profile.name = 'profile'


        class Profile(object):
            """
            DHCP IPV4 Profile
            
            .. attribute:: profile_name  <key>
            
            	Profile Name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: modes
            
            	DHCP IPV4 Profile modes
            	**type**\:  :py:class:`Modes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes>`
            
            

            """

            _prefix = 'ipv4-dhcpd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.profile_name = None
                self.modes = Ipv4Dhcpd.Profiles.Profile.Modes()
                self.modes.parent = self


            class Modes(object):
                """
                DHCP IPV4 Profile modes
                
                .. attribute:: mode
                
                	DHCP IPV4 Profile mode
                	**type**\: list of  :py:class:`Mode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode>`
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.mode = YList()
                    self.mode.parent = self
                    self.mode.name = 'mode'


                class Mode(object):
                    """
                    DHCP IPV4 Profile mode
                    
                    .. attribute:: mode  <key>
                    
                    	DHCP IPV4 Profile mode
                    	**type**\:  :py:class:`Ipv4DhcpdModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdModeEnum>`
                    
                    .. attribute:: enable
                    
                    	Enable the DHCP IPV4 Profile mode
                    	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: relay
                    
                    	DHCP Relay profile
                    	**type**\:  :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay>`
                    
                    .. attribute:: server
                    
                    	DHCP Server profile
                    	**type**\:  :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mode = None
                        self.enable = None
                        self.relay = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay()
                        self.relay.parent = self
                        self.server = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server()
                        self.server.parent = self


                    class Server(object):
                        """
                        DHCP Server profile
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:server'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                            return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info']


                    class Relay(object):
                        """
                        DHCP Relay profile
                        
                        .. attribute:: broadcast_policy
                        
                        	Broadcast Flag policy
                        	**type**\:  :py:class:`BroadcastPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy>`
                        
                        .. attribute:: gi_addr_policy
                        
                        	GIADDR policy
                        	**type**\:  :py:class:`GiAddrPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy>`
                        
                        .. attribute:: relay_information_option
                        
                        	Relay agent information option
                        	**type**\:  :py:class:`RelayInformationOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption>`
                        
                        .. attribute:: vrfs
                        
                        	VRF Helper Addresses
                        	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.broadcast_policy = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy()
                            self.broadcast_policy.parent = self
                            self.gi_addr_policy = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy()
                            self.gi_addr_policy.parent = self
                            self.relay_information_option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption()
                            self.relay_information_option.parent = self
                            self.vrfs = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs()
                            self.vrfs.parent = self


                        class GiAddrPolicy(object):
                            """
                            GIADDR policy
                            
                            .. attribute:: policy
                            
                            	GIADDR policy
                            	**type**\:  :py:class:`Ipv4DhcpdGiaddrPolicyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdGiaddrPolicyEnum>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.policy = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:gi-addr-policy'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.policy is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy']['meta_info']


                        class Vrfs(object):
                            """
                            VRF Helper Addresses
                            
                            .. attribute:: vrf
                            
                            	VRF Name
                            	**type**\: list of  :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.vrf = YList()
                                self.vrf.parent = self
                                self.vrf.name = 'vrf'


                            class Vrf(object):
                                """
                                VRF Name
                                
                                .. attribute:: vrf_name  <key>
                                
                                	VRF Name
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: helper_addresses
                                
                                	Helper Addresses
                                	**type**\:  :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.vrf_name = None
                                    self.helper_addresses = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses()
                                    self.helper_addresses.parent = self


                                class HelperAddresses(object):
                                    """
                                    Helper Addresses
                                    
                                    .. attribute:: helper_address
                                    
                                    	Helper Address
                                    	**type**\: list of  :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.helper_address = YList()
                                        self.helper_address.parent = self
                                        self.helper_address.name = 'helper_address'


                                    class HelperAddress(object):
                                        """
                                        Helper Address
                                        
                                        .. attribute:: ip_address  <key>
                                        
                                        	IPV4 Address
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: enable
                                        
                                        	Enable helper \- deprecated
                                        	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                                        
                                        .. attribute:: gateway_address
                                        
                                        	GatewayAddress
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.ip_address = None
                                            self.enable = None
                                            self.gateway_address = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.ip_address is None:
                                                raise YPYModelError('Key property ip_address is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:helper-address[Cisco-IOS-XR-ipv4-dhcpd-cfg:ip-address = ' + str(self.ip_address) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.ip_address is not None:
                                                return True

                                            if self.enable is not None:
                                                return True

                                            if self.gateway_address is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                            return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:helper-addresses'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.helper_address is not None:
                                            for child_ref in self.helper_address:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.vrf_name is None:
                                        raise YPYModelError('Key property vrf_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:vrf[Cisco-IOS-XR-ipv4-dhcpd-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.vrf_name is not None:
                                        return True

                                    if self.helper_addresses is not None and self.helper_addresses._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:vrfs'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.vrf is not None:
                                    for child_ref in self.vrf:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs']['meta_info']


                        class RelayInformationOption(object):
                            """
                            Relay agent information option
                            
                            .. attribute:: allow_untrusted
                            
                            	Forward untrusted packets
                            	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: check
                            
                            	Check Relay Agent Information Option in server reply
                            	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: insert
                            
                            	Insert Relay Agent Information circuit ID and remote ID suboptions in client requests
                            	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: policy
                            
                            	Relay information option policy
                            	**type**\:  :py:class:`Ipv4DhcpdRelayInfoOptionPolicyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdRelayInfoOptionPolicyEnum>`
                            
                            .. attribute:: subscriber_id
                            
                            	Subscriber ID
                            	**type**\:  str
                            
                            .. attribute:: vpn
                            
                            	Insert VPN options
                            	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: vpn_mode
                            
                            	VPN Mode
                            	**type**\:  :py:class:`Ipv4DhcpdRelayInfoOptionvpnModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdRelayInfoOptionvpnModeEnum>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.allow_untrusted = None
                                self.check = None
                                self.insert = None
                                self.policy = None
                                self.subscriber_id = None
                                self.vpn = None
                                self.vpn_mode = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:relay-information-option'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.allow_untrusted is not None:
                                    return True

                                if self.check is not None:
                                    return True

                                if self.insert is not None:
                                    return True

                                if self.policy is not None:
                                    return True

                                if self.subscriber_id is not None:
                                    return True

                                if self.vpn is not None:
                                    return True

                                if self.vpn_mode is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption']['meta_info']


                        class BroadcastPolicy(object):
                            """
                            Broadcast Flag policy
                            
                            .. attribute:: policy
                            
                            	Broadcast flag policy
                            	**type**\:  :py:class:`Ipv4DhcpdBroadcastFlagPolicyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdBroadcastFlagPolicyEnum>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.policy = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:broadcast-policy'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.policy is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:relay'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.broadcast_policy is not None and self.broadcast_policy._has_data():
                                return True

                            if self.gi_addr_policy is not None and self.gi_addr_policy._has_data():
                                return True

                            if self.relay_information_option is not None and self.relay_information_option._has_data():
                                return True

                            if self.vrfs is not None and self.vrfs._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                            return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.mode is None:
                            raise YPYModelError('Key property mode is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:mode[Cisco-IOS-XR-ipv4-dhcpd-cfg:mode = ' + str(self.mode) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.mode is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.relay is not None and self.relay._has_data():
                            return True

                        if self.server is not None and self.server._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:modes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.mode is not None:
                        for child_ref in self.mode:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes']['meta_info']

            @property
            def _common_path(self):
                if self.profile_name is None:
                    raise YPYModelError('Key property profile_name is None')

                return '/Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-cfg:profiles/Cisco-IOS-XR-ipv4-dhcpd-cfg:profile[Cisco-IOS-XR-ipv4-dhcpd-cfg:profile-name = ' + str(self.profile_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.profile_name is not None:
                    return True

                if self.modes is not None and self.modes._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-cfg:profiles'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.profile is not None:
                for child_ref in self.profile:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
            return meta._meta_table['Ipv4Dhcpd.Profiles']['meta_info']


    class Database(object):
        """
        Enable DHCP binding database storage to file
        system
        
        .. attribute:: full_write_interval
        
        	Full file write interval (default 10 minutes)
        	**type**\:  int
        
        	**range:** 1..1440
        
        .. attribute:: incremental_write_interval
        
        	Incremental file write interval (default 1 minutes)
        	**type**\:  int
        
        	**range:** 1..1440
        
        .. attribute:: proxy
        
        	Enable DHCP proxy binding database storage to file system
        	**type**\:  :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: server
        
        	Enable DHCP server binding database storage to file system
        	**type**\:  :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: snoop
        
        	Enable DHCP snoop binding database storage to file system
        	**type**\:  :py:class:`Empty <ydk.types.Empty>`
        
        

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.full_write_interval = None
            self.incremental_write_interval = None
            self.proxy = None
            self.server = None
            self.snoop = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-cfg:database'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.full_write_interval is not None:
                return True

            if self.incremental_write_interval is not None:
                return True

            if self.proxy is not None:
                return True

            if self.server is not None:
                return True

            if self.snoop is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
            return meta._meta_table['Ipv4Dhcpd.Database']['meta_info']


    class Interfaces(object):
        """
        DHCP IPV4 Interface Table
        
        .. attribute:: interface
        
        	DHCP IPV4 Interface
        	**type**\: list of  :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            DHCP IPV4 Interface
            
            .. attribute:: interface_name  <key>
            
            	Interface Name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: base_interface
            
            	DHCP IPv4 Base profile information
            	**type**\:  :py:class:`BaseInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.BaseInterface>`
            
            .. attribute:: none
            
            	DHCP IPV4 disabled
            	**type**\:  :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: profile
            
            	Profile name and mode
            	**type**\:  :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.Profile>`
            
            .. attribute:: proxy_interface
            
            	DHCP IPv4 proxy information
            	**type**\:  :py:class:`ProxyInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.ProxyInterface>`
            
            .. attribute:: relay_interface
            
            	DHCP IPv4 relay information
            	**type**\:  :py:class:`RelayInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.RelayInterface>`
            
            .. attribute:: server_interface
            
            	DHCP IPv4 Server information
            	**type**\:  :py:class:`ServerInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.ServerInterface>`
            
            .. attribute:: snoop_interface
            
            	DHCP IPv4 snoop information
            	**type**\:  :py:class:`SnoopInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.SnoopInterface>`
            
            

            """

            _prefix = 'ipv4-dhcpd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.base_interface = Ipv4Dhcpd.Interfaces.Interface.BaseInterface()
                self.base_interface.parent = self
                self.none = None
                self.profile = None
                self.proxy_interface = Ipv4Dhcpd.Interfaces.Interface.ProxyInterface()
                self.proxy_interface.parent = self
                self.relay_interface = Ipv4Dhcpd.Interfaces.Interface.RelayInterface()
                self.relay_interface.parent = self
                self.server_interface = Ipv4Dhcpd.Interfaces.Interface.ServerInterface()
                self.server_interface.parent = self
                self.snoop_interface = Ipv4Dhcpd.Interfaces.Interface.SnoopInterface()
                self.snoop_interface.parent = self


            class ProxyInterface(object):
                """
                DHCP IPv4 proxy information
                
                .. attribute:: dhcp_circuit_id
                
                	Circuit ID value
                	**type**\:  :py:class:`DhcpCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId>`
                
                .. attribute:: profile
                
                	Interface profile name
                	**type**\:  str
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.dhcp_circuit_id = None
                    self.profile = None


                class DhcpCircuitId(object):
                    """
                    Circuit ID value
                    
                    .. attribute:: argument1
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:  :py:class:`Ipv4DhcpdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtEnum>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.argument1 = None
                        self.argument10 = None
                        self.argument11 = None
                        self.argument12 = None
                        self.argument13 = None
                        self.argument14 = None
                        self.argument15 = None
                        self.argument16 = None
                        self.argument2 = None
                        self.argument3 = None
                        self.argument4 = None
                        self.argument5 = None
                        self.argument6 = None
                        self.argument7 = None
                        self.argument8 = None
                        self.argument9 = None
                        self.circuit_id = None
                        self.format = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:dhcp-circuit-id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self._is_presence:
                            return True
                        if self.argument1 is not None:
                            return True

                        if self.argument10 is not None:
                            return True

                        if self.argument11 is not None:
                            return True

                        if self.argument12 is not None:
                            return True

                        if self.argument13 is not None:
                            return True

                        if self.argument14 is not None:
                            return True

                        if self.argument15 is not None:
                            return True

                        if self.argument16 is not None:
                            return True

                        if self.argument2 is not None:
                            return True

                        if self.argument3 is not None:
                            return True

                        if self.argument4 is not None:
                            return True

                        if self.argument5 is not None:
                            return True

                        if self.argument6 is not None:
                            return True

                        if self.argument7 is not None:
                            return True

                        if self.argument8 is not None:
                            return True

                        if self.argument9 is not None:
                            return True

                        if self.circuit_id is not None:
                            return True

                        if self.format is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                        return meta._meta_table['Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:proxy-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.dhcp_circuit_id is not None and self.dhcp_circuit_id._has_data():
                        return True

                    if self.profile is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                    return meta._meta_table['Ipv4Dhcpd.Interfaces.Interface.ProxyInterface']['meta_info']


            class BaseInterface(object):
                """
                DHCP IPv4 Base profile information
                
                .. attribute:: profile
                
                	Interface profile name
                	**type**\:  str
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.profile = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:base-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.profile is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                    return meta._meta_table['Ipv4Dhcpd.Interfaces.Interface.BaseInterface']['meta_info']


            class RelayInterface(object):
                """
                DHCP IPv4 relay information
                
                .. attribute:: relay_dhcp_circuit_id
                
                	Circuit ID value
                	**type**\:  :py:class:`RelayDhcpCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId>`
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.relay_dhcp_circuit_id = None


                class RelayDhcpCircuitId(object):
                    """
                    Circuit ID value
                    
                    .. attribute:: argument1
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:  :py:class:`Ipv4DhcpdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtEnum>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.argument1 = None
                        self.argument10 = None
                        self.argument11 = None
                        self.argument12 = None
                        self.argument13 = None
                        self.argument14 = None
                        self.argument15 = None
                        self.argument16 = None
                        self.argument2 = None
                        self.argument3 = None
                        self.argument4 = None
                        self.argument5 = None
                        self.argument6 = None
                        self.argument7 = None
                        self.argument8 = None
                        self.argument9 = None
                        self.circuit_id = None
                        self.format = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:relay-dhcp-circuit-id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self._is_presence:
                            return True
                        if self.argument1 is not None:
                            return True

                        if self.argument10 is not None:
                            return True

                        if self.argument11 is not None:
                            return True

                        if self.argument12 is not None:
                            return True

                        if self.argument13 is not None:
                            return True

                        if self.argument14 is not None:
                            return True

                        if self.argument15 is not None:
                            return True

                        if self.argument16 is not None:
                            return True

                        if self.argument2 is not None:
                            return True

                        if self.argument3 is not None:
                            return True

                        if self.argument4 is not None:
                            return True

                        if self.argument5 is not None:
                            return True

                        if self.argument6 is not None:
                            return True

                        if self.argument7 is not None:
                            return True

                        if self.argument8 is not None:
                            return True

                        if self.argument9 is not None:
                            return True

                        if self.circuit_id is not None:
                            return True

                        if self.format is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                        return meta._meta_table['Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:relay-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.relay_dhcp_circuit_id is not None and self.relay_dhcp_circuit_id._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                    return meta._meta_table['Ipv4Dhcpd.Interfaces.Interface.RelayInterface']['meta_info']


            class Profile(object):
                """
                Profile name and mode
                
                .. attribute:: mode
                
                	DHCP mode
                	**type**\:  :py:class:`Ipv4DhcpdModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdModeEnum>`
                
                	**mandatory**\: True
                
                .. attribute:: profile_name
                
                	Profile name
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.mode = None
                    self.profile_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:profile'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self._is_presence:
                        return True
                    if self.mode is not None:
                        return True

                    if self.profile_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                    return meta._meta_table['Ipv4Dhcpd.Interfaces.Interface.Profile']['meta_info']


            class ServerInterface(object):
                """
                DHCP IPv4 Server information
                
                .. attribute:: profile
                
                	Interface profile name
                	**type**\:  str
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.profile = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:server-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.profile is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                    return meta._meta_table['Ipv4Dhcpd.Interfaces.Interface.ServerInterface']['meta_info']


            class SnoopInterface(object):
                """
                DHCP IPv4 snoop information
                
                .. attribute:: snoop_circuit_id
                
                	Configure circuit ID for snoop 1. Hex 2. ASCII
                	**type**\:  :py:class:`SnoopCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId>`
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.snoop_circuit_id = Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId()
                    self.snoop_circuit_id.parent = self


                class SnoopCircuitId(object):
                    """
                    Configure circuit ID for snoop 1. Hex 2.
                    ASCII
                    
                    .. attribute:: circuit_id_value
                    
                    	Enter circuit\-id value
                    	**type**\:  str
                    
                    .. attribute:: format_type
                    
                    	Format type, 1. Hex 2. ASCII
                    	**type**\:  int
                    
                    	**range:** 1..2
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.circuit_id_value = None
                        self.format_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:snoop-circuit-id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.circuit_id_value is not None:
                            return True

                        if self.format_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                        return meta._meta_table['Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:snoop-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.snoop_circuit_id is not None and self.snoop_circuit_id._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                    return meta._meta_table['Ipv4Dhcpd.Interfaces.Interface.SnoopInterface']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-cfg:interfaces/Cisco-IOS-XR-ipv4-dhcpd-cfg:interface[Cisco-IOS-XR-ipv4-dhcpd-cfg:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.interface_name is not None:
                    return True

                if self.base_interface is not None and self.base_interface._has_data():
                    return True

                if self.none is not None:
                    return True

                if self.profile is not None and self.profile._has_data():
                    return True

                if self.proxy_interface is not None and self.proxy_interface._has_data():
                    return True

                if self.relay_interface is not None and self.relay_interface._has_data():
                    return True

                if self.server_interface is not None and self.server_interface._has_data():
                    return True

                if self.snoop_interface is not None and self.snoop_interface._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                return meta._meta_table['Ipv4Dhcpd.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-cfg:interfaces'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
            return meta._meta_table['Ipv4Dhcpd.Interfaces']['meta_info']


    class DuplicateMacAllowed(object):
        """
        Allow Duplicate MAC Address
        
        .. attribute:: duplicate_mac
        
        	Duplicate mac is allowed
        	**type**\:  :py:class:`Empty <ydk.types.Empty>`
        
        	**mandatory**\: True
        
        .. attribute:: exclude_vlan
        
        	Exclude vlan
        	**type**\:  :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.duplicate_mac = None
            self.exclude_vlan = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-cfg:duplicate-mac-allowed'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self._is_presence:
                return True
            if self.duplicate_mac is not None:
                return True

            if self.exclude_vlan is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
            return meta._meta_table['Ipv4Dhcpd.DuplicateMacAllowed']['meta_info']


    class RateLimit(object):
        """
        Rate limit ingress packets
        
        .. attribute:: num_discover
        
        	Max DISCOVER packets per rate\-limiter period (default 100)
        	**type**\:  int
        
        	**range:** 0..1000
        
        .. attribute:: num_period
        
        	Rate limiter period in msec (default\: 200 msec)
        	**type**\:  int
        
        	**range:** 1..1000
        
        

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.num_discover = None
            self.num_period = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-cfg:rate-limit'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.num_discover is not None:
                return True

            if self.num_period is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
            return meta._meta_table['Ipv4Dhcpd.RateLimit']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.allow_client_id_change is not None:
            return True

        if self.database is not None and self.database._has_data():
            return True

        if self.duplicate_mac_allowed is not None and self.duplicate_mac_allowed._has_data():
            return True

        if self.enable is not None:
            return True

        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.profiles is not None and self.profiles._has_data():
            return True

        if self.rate_limit is not None and self.rate_limit._has_data():
            return True

        if self.vrfs is not None and self.vrfs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Ipv4Dhcpd']['meta_info']


