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



class BaseActionEnum(Enum):
    """
    BaseActionEnum

    Base action

    .. data:: allow = 0

    	Allow vendor specific DHCP Discover

    .. data:: drop = 1

    	Drop vendor specific DHCP Discover

    """

    allow = 0

    drop = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['BaseActionEnum']


class Dhcpv4LimitLease1Enum(Enum):
    """
    Dhcpv4LimitLease1Enum

    Dhcpv4 limit lease1

    .. data:: interface = 1

    	Interface

    .. data:: circuit_id = 2

    	Circuit ID

    .. data:: remote_id = 3

    	Remote ID

    .. data:: circuit_id_remote_id = 4

    	Circuit ID Remote ID

    """

    interface = 1

    circuit_id = 2

    remote_id = 3

    circuit_id_remote_id = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Dhcpv4LimitLease1Enum']


class Dhcpv4MatchOptionEnum(Enum):
    """
    Dhcpv4MatchOptionEnum

    Dhcpv4 match option

    .. data:: Y_60__FWD_SLASH__60 = 60

    	Vendor class ID

    .. data:: Y_77__FWD_SLASH__77 = 77

    	77 User class

    .. data:: Y_124__FWD_SLASH__124 = 124

    	Vendor identifying class

    .. data:: Y_125__FWD_SLASH__125 = 125

    	Vendor specific information

    """

    Y_60__FWD_SLASH__60 = 60

    Y_77__FWD_SLASH__77 = 77

    Y_124__FWD_SLASH__124 = 124

    Y_125__FWD_SLASH__125 = 125


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Dhcpv4MatchOptionEnum']


class Ipv4DhcpdBroadcastFlagPolicyEnum(Enum):
    """
    Ipv4DhcpdBroadcastFlagPolicyEnum

    Ipv4dhcpd broadcast flag policy

    .. data:: ignore = 0

    	Ignore

    .. data:: check = 1

    	check

    .. data:: unicast_always = 2

    	Unicast always

    """

    ignore = 0

    check = 1

    unicast_always = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Ipv4DhcpdBroadcastFlagPolicyEnum']


class Ipv4DhcpdFmtEnum(Enum):
    """
    Ipv4DhcpdFmtEnum

    Ipv4dhcpd fmt

    .. data:: no_format = 0

    	Not a Format String

    .. data:: format = 1

    	Format String

    """

    no_format = 0

    format = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Ipv4DhcpdFmtEnum']


class Ipv4DhcpdFmtSpecifierEnum(Enum):
    """
    Ipv4DhcpdFmtSpecifierEnum

    Ipv4dhcpd fmt specifier

    .. data:: physical_chassis = 1

    	Physical chassis

    .. data:: physical_slot = 2

    	Physical slot

    .. data:: physical_sub_slot = 3

    	Physical sub-slot

    .. data:: physical_port = 4

    	Physical port

    .. data:: physical_sub_port = 5

    	Physical sub-port

    .. data:: inner_vlan_id = 6

    	Inner VLAN ID

    .. data:: outer_vlan_id = 7

    	Outer VLAN ID

    .. data:: l2_interface = 8

    	L2 Interface

    """

    physical_chassis = 1

    physical_slot = 2

    physical_sub_slot = 3

    physical_port = 4

    physical_sub_port = 5

    inner_vlan_id = 6

    outer_vlan_id = 7

    l2_interface = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Ipv4DhcpdFmtSpecifierEnum']


class Ipv4DhcpdGiaddrPolicyEnum(Enum):
    """
    Ipv4DhcpdGiaddrPolicyEnum

    Ipv4dhcpd giaddr policy

    .. data:: keep = 0

    	Keep

    .. data:: replace = 1

    	Replace

    .. data:: drop = 2

    	Drop

    """

    keep = 0

    replace = 1

    drop = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Ipv4DhcpdGiaddrPolicyEnum']


class Ipv4DhcpdLayerEnum(Enum):
    """
    Ipv4DhcpdLayerEnum

    Ipv4dhcpd layer

    .. data:: layer2 = 2

    	Layer2

    .. data:: layer3 = 3

    	Layer3

    """

    layer2 = 2

    layer3 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Ipv4DhcpdLayerEnum']


class Ipv4DhcpdModeEnum(Enum):
    """
    Ipv4DhcpdModeEnum

    Ipv4dhcpd mode

    .. data:: base = 0

    	Base

    .. data:: relay = 1

    	Relay

    .. data:: snoop = 2

    	Snoop

    .. data:: server = 3

    	Server

    .. data:: proxy = 4

    	Proxy

    .. data:: base2 = 5

    	Base2

    """

    base = 0

    relay = 1

    snoop = 2

    server = 3

    proxy = 4

    base2 = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Ipv4DhcpdModeEnum']


class Ipv4DhcpdRelayInfoOptionAuthenticateEnum(Enum):
    """
    Ipv4DhcpdRelayInfoOptionAuthenticateEnum

    Ipv4dhcpd relay info option authenticate

    .. data:: received = 0

    	Received

    .. data:: inserted = 1

    	Inserted

    """

    received = 0

    inserted = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Ipv4DhcpdRelayInfoOptionAuthenticateEnum']


class Ipv4DhcpdRelayInfoOptionPolicyEnum(Enum):
    """
    Ipv4DhcpdRelayInfoOptionPolicyEnum

    Ipv4dhcpd relay info option policy

    .. data:: replace = 0

    	Replace

    .. data:: keep = 1

    	Keep

    .. data:: drop = 2

    	Drop

    .. data:: encapsulate = 3

    	Encapsulate

    """

    replace = 0

    keep = 1

    drop = 2

    encapsulate = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Ipv4DhcpdRelayInfoOptionPolicyEnum']


class Ipv4DhcpdRelayInfoOptionvpnModeEnum(Enum):
    """
    Ipv4DhcpdRelayInfoOptionvpnModeEnum

    Ipv4dhcpd relay info optionvpn mode

    .. data:: rfc = 0

    	RFC

    .. data:: cisco = 1

    	Cisco

    """

    rfc = 0

    cisco = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['Ipv4DhcpdRelayInfoOptionvpnModeEnum']


class LeaseLimitValueEnum(Enum):
    """
    LeaseLimitValueEnum

    Lease limit value

    .. data:: per_interface = 1

    	Insert the limit lease type interface

    .. data:: per_circuit_id = 2

    	Insert the limit lease type circuit-id

    .. data:: per_remote_id = 3

    	Insert the limit lease type remote-id

    """

    per_interface = 1

    per_circuit_id = 2

    per_remote_id = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['LeaseLimitValueEnum']


class MatchactionEnum(Enum):
    """
    MatchactionEnum

    Matchaction

    .. data:: allow = 0

    	Allow DHCP Discover

    .. data:: drop = 1

    	Drop DHCP Discover

    """

    allow = 0

    drop = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['MatchactionEnum']


class MatchoptionEnum(Enum):
    """
    MatchoptionEnum

    Matchoption

    .. data:: circuitid = 1

    	Match circuit id of option 82 Relay-agent

    	specific class

    .. data:: remoteid = 2

    	Match remote id of option 82 Relay-agent

    	specific class

    .. data:: Y_60 = 60

    	Match option 60 vendor class id

    .. data:: Y_77 = 77

    	Match option 77 user class

    .. data:: Y_124 = 124

    	Match option 124 vendor-identifying vendor

    	class

    .. data:: Y_125 = 125

    	Match option 125 vendor-indentifying

    	vendor-specific info

    """

    circuitid = 1

    remoteid = 2

    Y_60 = 60

    Y_77 = 77

    Y_124 = 124

    Y_125 = 125


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['MatchoptionEnum']


class PolicyEnum(Enum):
    """
    PolicyEnum

    Policy

    .. data:: ignore = 0

    	Ignore the broadcast policy

    .. data:: check = 1

    	Check for broadcast flag

    .. data:: unicastalways = 2

    	Always Unicast the reply

    """

    ignore = 0

    check = 1

    unicastalways = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['PolicyEnum']


class ProxyActionEnum(Enum):
    """
    ProxyActionEnum

    Proxy action

    .. data:: allow = 0

    	Allow vendor specific DHCP Discover

    .. data:: drop = 1

    	Drop vendor specific DHCP Discover

    """

    allow = 0

    drop = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
        return meta._meta_table['ProxyActionEnum']



class Ipv4Dhcpd(object):
    """
    DHCP IPV4 configuration
    
    .. attribute:: allow_client_id_change
    
    	For BNG session, allow client id change for a client MAC
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: database
    
    	Enable DHCP binding database storage to file system
    	**type**\:   :py:class:`Database <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Database>`
    
    .. attribute:: duplicate_mac_allowed
    
    	Allow Duplicate MAC Address
    	**type**\:   :py:class:`DuplicateMacAllowed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.DuplicateMacAllowed>`
    
    	**presence node**\: True
    
    .. attribute:: enable
    
    	DHCP IPV4 configuration
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: inner_cos
    
    	Configure inner cos values for dhcp packets
    	**type**\:  int
    
    	**range:** 0..7
    
    .. attribute:: interfaces
    
    	DHCP IPV4 Interface Table
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces>`
    
    .. attribute:: outer_cos
    
    	Configure outer cos values for dhcp packets
    	**type**\:  int
    
    	**range:** 0..7
    
    .. attribute:: profiles
    
    	DHCP IPV4 Profile Table
    	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles>`
    
    .. attribute:: rate_limit
    
    	Rate limit ingress packets
    	**type**\:   :py:class:`RateLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.RateLimit>`
    
    .. attribute:: vrfs
    
    	VRF Table
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Vrfs>`
    
    

    """

    _prefix = 'ipv4-dhcpd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.allow_client_id_change = None
        self.database = Ipv4Dhcpd.Database()
        self.database.parent = self
        self.duplicate_mac_allowed = None
        self.enable = None
        self.inner_cos = None
        self.interfaces = Ipv4Dhcpd.Interfaces()
        self.interfaces.parent = self
        self.outer_cos = None
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
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Vrfs.Vrf>`
        
        

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
            	**type**\:   :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Vrfs.Vrf.Profile>`
            
            	**presence node**\: True
            
            

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
                	**type**\:   :py:class:`Ipv4DhcpdModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdModeEnum>`
                
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
        	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile>`
        
        

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
            	**type**\:   :py:class:`Modes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes>`
            
            

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
                	**type**\: list of    :py:class:`Mode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode>`
                
                

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
                    	**type**\:   :py:class:`Ipv4DhcpdModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdModeEnum>`
                    
                    .. attribute:: base
                    
                    	DHCP Base Profile
                    	**type**\:   :py:class:`Base <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base>`
                    
                    .. attribute:: enable
                    
                    	Enable the DHCP IPV4 Profile mode
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: proxy
                    
                    	DHCP proxy profile
                    	**type**\:   :py:class:`Proxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy>`
                    
                    .. attribute:: relay
                    
                    	DHCP Relay profile
                    	**type**\:   :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay>`
                    
                    .. attribute:: server
                    
                    	DHCP Server profile
                    	**type**\:   :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server>`
                    
                    .. attribute:: snoop
                    
                    	DHCP Snoop profile
                    	**type**\:   :py:class:`Snoop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mode = None
                        self.base = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base()
                        self.base.parent = self
                        self.enable = None
                        self.proxy = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy()
                        self.proxy.parent = self
                        self.relay = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay()
                        self.relay.parent = self
                        self.server = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server()
                        self.server.parent = self
                        self.snoop = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop()
                        self.snoop.parent = self


                    class Snoop(object):
                        """
                        DHCP Snoop profile
                        
                        .. attribute:: relay_information_option
                        
                        	DHCP Snoop profile
                        	**type**\:   :py:class:`RelayInformationOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption>`
                        
                        .. attribute:: trusted
                        
                        	Trusted sources
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.relay_information_option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption()
                            self.relay_information_option.parent = self
                            self.trusted = None


                        class RelayInformationOption(object):
                            """
                            DHCP Snoop profile
                            
                            .. attribute:: allow_untrusted
                            
                            	Forward untrusted packets
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: insert
                            
                            	Insert Relay Agent Information circuit ID and remote ID suboptions in client request
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: policy
                            
                            	Relay information option policy
                            	**type**\:   :py:class:`Ipv4DhcpdRelayInfoOptionPolicyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdRelayInfoOptionPolicyEnum>`
                            
                            .. attribute:: remote_id
                            
                            	Enter remote\-id value
                            	**type**\:   :py:class:`RemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.allow_untrusted = None
                                self.insert = None
                                self.policy = None
                                self.remote_id = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId()
                                self.remote_id.parent = self


                            class RemoteId(object):
                                """
                                Enter remote\-id value
                                
                                .. attribute:: format_type
                                
                                	Format type, 1. Hex 2. ASCII
                                	**type**\:  int
                                
                                	**range:** 1..2
                                
                                .. attribute:: remote_id_value
                                
                                	Enter remote\-id value
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.format_type = None
                                    self.remote_id_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:remote-id'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.format_type is not None:
                                        return True

                                    if self.remote_id_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:relay-information-option'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.allow_untrusted is not None:
                                    return True

                                if self.insert is not None:
                                    return True

                                if self.policy is not None:
                                    return True

                                if self.remote_id is not None and self.remote_id._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:snoop'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.relay_information_option is not None and self.relay_information_option._has_data():
                                return True

                            if self.trusted is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                            return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop']['meta_info']


                    class Base(object):
                        """
                        DHCP Base Profile
                        
                        .. attribute:: base_match
                        
                        	Insert match keyword
                        	**type**\:   :py:class:`BaseMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch>`
                        
                        .. attribute:: base_relay_opt
                        
                        	Insert Relay Agent Information circuit ID and remote ID suboptions in client request
                        	**type**\:   :py:class:`BaseRelayOpt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt>`
                        
                        .. attribute:: default_profile
                        
                        	Enable the default profile
                        	**type**\:   :py:class:`DefaultProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile>`
                        
                        .. attribute:: enable
                        
                        	Enable the DHCP IPv4 Base Profile
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: match
                        
                        	Insert match keyword
                        	**type**\:   :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.base_match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch()
                            self.base_match.parent = self
                            self.base_relay_opt = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt()
                            self.base_relay_opt.parent = self
                            self.default_profile = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile()
                            self.default_profile.parent = self
                            self.enable = None
                            self.match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match()
                            self.match.parent = self


                        class DefaultProfile(object):
                            """
                            Enable the default profile
                            
                            .. attribute:: profile_mode
                            
                            	none
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: profile_name
                            
                            	Profile name
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.profile_mode = None
                                self.profile_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:default-profile'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.profile_mode is not None:
                                    return True

                                if self.profile_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile']['meta_info']


                        class Match(object):
                            """
                            Insert match keyword
                            
                            .. attribute:: def_options
                            
                            	Table of Option
                            	**type**\:   :py:class:`DefOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions>`
                            
                            .. attribute:: option_filters
                            
                            	Table of Option
                            	**type**\:   :py:class:`OptionFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.def_options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions()
                                self.def_options.parent = self
                                self.option_filters = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters()
                                self.option_filters.parent = self


                            class OptionFilters(object):
                                """
                                Table of Option
                                
                                .. attribute:: option_filter
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`OptionFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.option_filter = YList()
                                    self.option_filter.parent = self
                                    self.option_filter.name = 'option_filter'


                                class OptionFilter(object):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: matchoption  <key>
                                    
                                    	Match option 60
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: pattern  <key>
                                    
                                    	Enter hex pattern string
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: format  <key>
                                    
                                    	Set constant integer
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: option_action
                                    
                                    	Vendor action
                                    	**type**\:   :py:class:`BaseActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.BaseActionEnum>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.matchoption = None
                                        self.pattern = None
                                        self.format = None
                                        self.option_action = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.matchoption is None:
                                            raise YPYModelError('Key property matchoption is None')
                                        if self.pattern is None:
                                            raise YPYModelError('Key property pattern is None')
                                        if self.format is None:
                                            raise YPYModelError('Key property format is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:option-filter[Cisco-IOS-XR-ipv4-dhcpd-cfg:matchoption = ' + str(self.matchoption) + '][Cisco-IOS-XR-ipv4-dhcpd-cfg:pattern = ' + str(self.pattern) + '][Cisco-IOS-XR-ipv4-dhcpd-cfg:format = ' + str(self.format) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.matchoption is not None:
                                            return True

                                        if self.pattern is not None:
                                            return True

                                        if self.format is not None:
                                            return True

                                        if self.option_action is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:option-filters'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.option_filter is not None:
                                        for child_ref in self.option_filter:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters']['meta_info']


                            class DefOptions(object):
                                """
                                Table of Option
                                
                                .. attribute:: def_option
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`DefOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.def_option = YList()
                                    self.def_option.parent = self
                                    self.def_option.name = 'def_option'


                                class DefOption(object):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: def_matchoption  <key>
                                    
                                    	Match option 60
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: def_matchaction
                                    
                                    	Vendor action
                                    	**type**\:   :py:class:`BaseActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.BaseActionEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.def_matchoption = None
                                        self.def_matchaction = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.def_matchoption is None:
                                            raise YPYModelError('Key property def_matchoption is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:def-option[Cisco-IOS-XR-ipv4-dhcpd-cfg:def-matchoption = ' + str(self.def_matchoption) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.def_matchoption is not None:
                                            return True

                                        if self.def_matchaction is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:def-options'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.def_option is not None:
                                        for child_ref in self.def_option:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:match'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.def_options is not None and self.def_options._has_data():
                                    return True

                                if self.option_filters is not None and self.option_filters._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match']['meta_info']


                        class BaseRelayOpt(object):
                            """
                            Insert Relay Agent Information circuit ID
                            and remote ID suboptions in client request
                            
                            .. attribute:: authenticate
                            
                            	Specify Relay Agent Information Option authenticate
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: remote_id
                            
                            	Enter remote\-id value
                            	**type**\:  str
                            
                            	**length:** 1..256
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.authenticate = None
                                self.remote_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:base-relay-opt'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.authenticate is not None:
                                    return True

                                if self.remote_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt']['meta_info']


                        class BaseMatch(object):
                            """
                            Insert match keyword
                            
                            .. attribute:: options
                            
                            	Specify match option
                            	**type**\:   :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options()
                                self.options.parent = self


                            class Options(object):
                                """
                                Specify match option
                                
                                .. attribute:: option
                                
                                	none
                                	**type**\: list of    :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.option = YList()
                                    self.option.parent = self
                                    self.option.name = 'option'


                                class Option(object):
                                    """
                                    none
                                    
                                    .. attribute:: opt60  <key>
                                    
                                    	none
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: opt60_hex_str  <key>
                                    
                                    	Enter hex pattern string
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: format  <key>
                                    
                                    	Set constant integer
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: option_profile
                                    
                                    	Enter a profile
                                    	**type**\:   :py:class:`OptionProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.opt60 = None
                                        self.opt60_hex_str = None
                                        self.format = None
                                        self.option_profile = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile()
                                        self.option_profile.parent = self


                                    class OptionProfile(object):
                                        """
                                        Enter a profile
                                        
                                        .. attribute:: profile_mode
                                        
                                        	none
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: profile_name
                                        
                                        	Profile name
                                        	**type**\:  str
                                        
                                        	**length:** 1..64
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.profile_mode = None
                                            self.profile_name = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:option-profile'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.profile_mode is not None:
                                                return True

                                            if self.profile_name is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                            return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.opt60 is None:
                                            raise YPYModelError('Key property opt60 is None')
                                        if self.opt60_hex_str is None:
                                            raise YPYModelError('Key property opt60_hex_str is None')
                                        if self.format is None:
                                            raise YPYModelError('Key property format is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:option[Cisco-IOS-XR-ipv4-dhcpd-cfg:opt60 = ' + str(self.opt60) + '][Cisco-IOS-XR-ipv4-dhcpd-cfg:opt60-hex-str = ' + str(self.opt60_hex_str) + '][Cisco-IOS-XR-ipv4-dhcpd-cfg:format = ' + str(self.format) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.opt60 is not None:
                                            return True

                                        if self.opt60_hex_str is not None:
                                            return True

                                        if self.format is not None:
                                            return True

                                        if self.option_profile is not None and self.option_profile._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:options'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.option is not None:
                                        for child_ref in self.option:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:base-match'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.options is not None and self.options._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:base'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.base_match is not None and self.base_match._has_data():
                                return True

                            if self.base_relay_opt is not None and self.base_relay_opt._has_data():
                                return True

                            if self.default_profile is not None and self.default_profile._has_data():
                                return True

                            if self.enable is not None:
                                return True

                            if self.match is not None and self.match._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                            return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base']['meta_info']


                    class Server(object):
                        """
                        DHCP Server profile
                        
                        .. attribute:: aaa
                        
                        	Enable aaa dhcp option force\-insert
                        	**type**\:   :py:class:`Aaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa>`
                        
                        .. attribute:: boot_filename
                        
                        	Boot Filename
                        	**type**\:  str
                        
                        	**length:** 1..128
                        
                        .. attribute:: broadcast_flag
                        
                        	None
                        	**type**\:   :py:class:`BroadcastFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag>`
                        
                        .. attribute:: classes
                        
                        	Table of Class
                        	**type**\:   :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes>`
                        
                        .. attribute:: default_routers
                        
                        	default routers
                        	**type**\:   :py:class:`DefaultRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters>`
                        
                        .. attribute:: dns_servers
                        
                        	DNS servers
                        	**type**\:   :py:class:`DnsServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers>`
                        
                        .. attribute:: domain_name
                        
                        	Domain name
                        	**type**\:  str
                        
                        	**length:** 1..256
                        
                        .. attribute:: infinite_lease
                        
                        	Infinite lease
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: lease
                        
                        	lease
                        	**type**\:   :py:class:`Lease <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease>`
                        
                        .. attribute:: lease_limit
                        
                        	Specify limit lease
                        	**type**\:   :py:class:`LeaseLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit>`
                        
                        .. attribute:: match
                        
                        	Insert match keyword
                        	**type**\:   :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match>`
                        
                        .. attribute:: net_bios_name_servers
                        
                        	NetBIOS name servers
                        	**type**\:   :py:class:`NetBiosNameServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers>`
                        
                        .. attribute:: netbios_node_type
                        
                        	NetBIOS node type
                        	**type**\:   :py:class:`NetbiosNodeType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType>`
                        
                        .. attribute:: next_server
                        
                        	Configure the tftp\-server IP to be used by the client
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: option_codes
                        
                        	Table of OptionCode
                        	**type**\:   :py:class:`OptionCodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes>`
                        
                        .. attribute:: pool
                        
                        	Specify the Pool name
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: relay
                        
                        	Specify Relay Agent Information Option configuration
                        	**type**\:   :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay>`
                        
                        .. attribute:: requested_ip_address
                        
                        	Validate Requested IP Address
                        	**type**\:   :py:class:`RequestedIpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress>`
                        
                        .. attribute:: secure_arp
                        
                        	Enable Secure Arp
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: server_allow_move
                        
                        	Allow dhcp subscriber move
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: server_id_check
                        
                        	Validate server ID check
                        	**type**\:   :py:class:`ServerIdCheck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck>`
                        
                        .. attribute:: session
                        
                        	Change sessions configuration
                        	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session>`
                        
                        .. attribute:: subnet_mask
                        
                        	Configure Subnet Mask
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.aaa = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa()
                            self.aaa.parent = self
                            self.boot_filename = None
                            self.broadcast_flag = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag()
                            self.broadcast_flag.parent = self
                            self.classes = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes()
                            self.classes.parent = self
                            self.default_routers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters()
                            self.default_routers.parent = self
                            self.dns_servers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers()
                            self.dns_servers.parent = self
                            self.domain_name = None
                            self.infinite_lease = None
                            self.lease = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease()
                            self.lease.parent = self
                            self.lease_limit = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit()
                            self.lease_limit.parent = self
                            self.match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match()
                            self.match.parent = self
                            self.net_bios_name_servers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers()
                            self.net_bios_name_servers.parent = self
                            self.netbios_node_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType()
                            self.netbios_node_type.parent = self
                            self.next_server = None
                            self.option_codes = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes()
                            self.option_codes.parent = self
                            self.pool = None
                            self.relay = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay()
                            self.relay.parent = self
                            self.requested_ip_address = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress()
                            self.requested_ip_address.parent = self
                            self.secure_arp = None
                            self.server_allow_move = None
                            self.server_id_check = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck()
                            self.server_id_check.parent = self
                            self.session = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session()
                            self.session.parent = self
                            self.subnet_mask = None


                        class ServerIdCheck(object):
                            """
                            Validate server ID check
                            
                            .. attribute:: check
                            
                            	specify server\-id\-check disable
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.check = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:server-id-check'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.check is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck']['meta_info']


                        class LeaseLimit(object):
                            """
                            Specify limit lease
                            
                            .. attribute:: lease_limit_value
                            
                            	Configure Lease limit value
                            	**type**\:   :py:class:`LeaseLimitValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.LeaseLimitValueEnum>`
                            
                            .. attribute:: range
                            
                            	Value of limit lease count in Decimal
                            	**type**\:  int
                            
                            	**range:** 1..240000
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.lease_limit_value = None
                                self.range = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:lease-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.lease_limit_value is not None:
                                    return True

                                if self.range is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit']['meta_info']


                        class RequestedIpAddress(object):
                            """
                            Validate Requested IP Address
                            
                            .. attribute:: check
                            
                            	specify requested\-ip\-address\-check disable
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.check = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:requested-ip-address'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.check is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress']['meta_info']


                        class DefaultRouters(object):
                            """
                            default routers
                            
                            .. attribute:: default_router
                            
                            	Router's IP address
                            	**type**\:  list of str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.default_router = YLeafList()
                                self.default_router.parent = self
                                self.default_router.name = 'default_router'

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:default-routers'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.default_router is not None:
                                    for child in self.default_router:
                                        if child is not None:
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters']['meta_info']


                        class NetBiosNameServers(object):
                            """
                            NetBIOS name servers
                            
                            .. attribute:: net_bios_name_server
                            
                            	NetBIOSNameServer's IP address
                            	**type**\:  list of str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.net_bios_name_server = YLeafList()
                                self.net_bios_name_server.parent = self
                                self.net_bios_name_server.name = 'net_bios_name_server'

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:net-bios-name-servers'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.net_bios_name_server is not None:
                                    for child in self.net_bios_name_server:
                                        if child is not None:
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers']['meta_info']


                        class Match(object):
                            """
                            Insert match keyword
                            
                            .. attribute:: option_defaults
                            
                            	Table of OptionDefault
                            	**type**\:   :py:class:`OptionDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults>`
                            
                            .. attribute:: options
                            
                            	Table of Option
                            	**type**\:   :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.option_defaults = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults()
                                self.option_defaults.parent = self
                                self.options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options()
                                self.options.parent = self


                            class OptionDefaults(object):
                                """
                                Table of OptionDefault
                                
                                .. attribute:: option_default
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`OptionDefault <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.option_default = YList()
                                    self.option_default.parent = self
                                    self.option_default.name = 'option_default'


                                class OptionDefault(object):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: matchoption  <key>
                                    
                                    	Match option 60
                                    	**type**\:   :py:class:`MatchoptionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.MatchoptionEnum>`
                                    
                                    .. attribute:: matchaction
                                    
                                    	Vendor action
                                    	**type**\:   :py:class:`MatchactionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.MatchactionEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.matchoption = None
                                        self.matchaction = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.matchoption is None:
                                            raise YPYModelError('Key property matchoption is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:option-default[Cisco-IOS-XR-ipv4-dhcpd-cfg:matchoption = ' + str(self.matchoption) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.matchoption is not None:
                                            return True

                                        if self.matchaction is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:option-defaults'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.option_default is not None:
                                        for child_ref in self.option_default:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults']['meta_info']


                            class Options(object):
                                """
                                Table of Option
                                
                                .. attribute:: option
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.option = YList()
                                    self.option.parent = self
                                    self.option.name = 'option'


                                class Option(object):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: matchoption  <key>
                                    
                                    	Match option 60
                                    	**type**\:   :py:class:`MatchoptionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.MatchoptionEnum>`
                                    
                                    .. attribute:: pattern  <key>
                                    
                                    	Enter hex pattern string
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: format  <key>
                                    
                                    	Set constant integer
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: matchaction
                                    
                                    	Vendor action
                                    	**type**\:   :py:class:`MatchactionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.MatchactionEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.matchoption = None
                                        self.pattern = None
                                        self.format = None
                                        self.matchaction = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.matchoption is None:
                                            raise YPYModelError('Key property matchoption is None')
                                        if self.pattern is None:
                                            raise YPYModelError('Key property pattern is None')
                                        if self.format is None:
                                            raise YPYModelError('Key property format is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:option[Cisco-IOS-XR-ipv4-dhcpd-cfg:matchoption = ' + str(self.matchoption) + '][Cisco-IOS-XR-ipv4-dhcpd-cfg:pattern = ' + str(self.pattern) + '][Cisco-IOS-XR-ipv4-dhcpd-cfg:format = ' + str(self.format) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.matchoption is not None:
                                            return True

                                        if self.pattern is not None:
                                            return True

                                        if self.format is not None:
                                            return True

                                        if self.matchaction is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:options'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.option is not None:
                                        for child_ref in self.option:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:match'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.option_defaults is not None and self.option_defaults._has_data():
                                    return True

                                if self.options is not None and self.options._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match']['meta_info']


                        class BroadcastFlag(object):
                            """
                            None
                            
                            .. attribute:: policy
                            
                            	Specify broadcast flag policy
                            	**type**\:   :py:class:`PolicyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.PolicyEnum>`
                            
                            

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

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:broadcast-flag'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.policy is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag']['meta_info']


                        class Session(object):
                            """
                            Change sessions configuration
                            
                            .. attribute:: throttle_type
                            
                            	Throttle DHCP sessions based on MAC address
                            	**type**\:   :py:class:`ThrottleType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.throttle_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType()
                                self.throttle_type.parent = self


                            class ThrottleType(object):
                                """
                                Throttle DHCP sessions based on MAC
                                address
                                
                                .. attribute:: mac_throttle
                                
                                	Throttle DHCP sessions from any one MAC address
                                	**type**\:   :py:class:`MacThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.mac_throttle = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle()
                                    self.mac_throttle.parent = self


                                class MacThrottle(object):
                                    """
                                    Throttle DHCP sessions from any one MAC
                                    address
                                    
                                    .. attribute:: num_block
                                    
                                    	Throttle blocking period (in secs)
                                    	**type**\:  int
                                    
                                    	**range:** 1..100
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: num_discover
                                    
                                    	Number of discovers at which to throttle
                                    	**type**\:  int
                                    
                                    	**range:** 1..65535
                                    
                                    .. attribute:: num_request
                                    
                                    	Throttle request period (in secs)
                                    	**type**\:  int
                                    
                                    	**range:** 1..100
                                    
                                    	**units**\: second
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_block = None
                                        self.num_discover = None
                                        self.num_request = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:mac-throttle'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.num_block is not None:
                                            return True

                                        if self.num_discover is not None:
                                            return True

                                        if self.num_request is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:throttle-type'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.mac_throttle is not None and self.mac_throttle._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:session'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.throttle_type is not None and self.throttle_type._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session']['meta_info']


                        class Classes(object):
                            """
                            Table of Class
                            
                            .. attribute:: class_
                            
                            	Create or enter server profile class
                            	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.class_ = YList()
                                self.class_.parent = self
                                self.class_.name = 'class_'


                            class Class_(object):
                                """
                                Create or enter server profile class
                                
                                .. attribute:: class_name  <key>
                                
                                	class name
                                	**type**\:  str
                                
                                	**length:** 1..128
                                
                                .. attribute:: boot_filename
                                
                                	Boot Filename
                                	**type**\:  str
                                
                                	**length:** 1..128
                                
                                .. attribute:: class_match
                                
                                	Insert match keyword
                                	**type**\:   :py:class:`ClassMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch>`
                                
                                .. attribute:: default_routers
                                
                                	default routers
                                	**type**\:   :py:class:`DefaultRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DefaultRouters>`
                                
                                .. attribute:: dns_servers
                                
                                	DNS servers
                                	**type**\:   :py:class:`DnsServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DnsServers>`
                                
                                .. attribute:: domain_name
                                
                                	Domain name
                                	**type**\:  str
                                
                                	**length:** 1..256
                                
                                .. attribute:: enable
                                
                                	Enable Create or enter server profile class. Deletion of this object also causes deletion of all associated objects under Class
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: infinite_lease
                                
                                	Infinite lease
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: lease
                                
                                	lease
                                	**type**\:   :py:class:`Lease <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.Lease>`
                                
                                .. attribute:: net_bios_name_servers
                                
                                	NetBIOS name servers
                                	**type**\:   :py:class:`NetBiosNameServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetBiosNameServers>`
                                
                                .. attribute:: netbios_node_type
                                
                                	NetBIOS node type
                                	**type**\:   :py:class:`NetbiosNodeType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetbiosNodeType>`
                                
                                .. attribute:: next_server
                                
                                	Configure the tftp\-server IP to be used by the client
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: option_codes
                                
                                	Table of OptionCode
                                	**type**\:   :py:class:`OptionCodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes>`
                                
                                .. attribute:: pool
                                
                                	Specify the pool
                                	**type**\:  str
                                
                                .. attribute:: subnet_mask
                                
                                	Configure Subnet Mask
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.class_name = None
                                    self.boot_filename = None
                                    self.class_match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch()
                                    self.class_match.parent = self
                                    self.default_routers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DefaultRouters()
                                    self.default_routers.parent = self
                                    self.dns_servers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DnsServers()
                                    self.dns_servers.parent = self
                                    self.domain_name = None
                                    self.enable = None
                                    self.infinite_lease = None
                                    self.lease = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.Lease()
                                    self.lease.parent = self
                                    self.net_bios_name_servers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetBiosNameServers()
                                    self.net_bios_name_servers.parent = self
                                    self.netbios_node_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetbiosNodeType()
                                    self.netbios_node_type.parent = self
                                    self.next_server = None
                                    self.option_codes = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes()
                                    self.option_codes.parent = self
                                    self.pool = None
                                    self.subnet_mask = None


                                class DefaultRouters(object):
                                    """
                                    default routers
                                    
                                    .. attribute:: default_router
                                    
                                    	Router's IP address
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.default_router = YLeafList()
                                        self.default_router.parent = self
                                        self.default_router.name = 'default_router'

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:default-routers'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.default_router is not None:
                                            for child in self.default_router:
                                                if child is not None:
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DefaultRouters']['meta_info']


                                class NetBiosNameServers(object):
                                    """
                                    NetBIOS name servers
                                    
                                    .. attribute:: net_bios_name_server
                                    
                                    	NetBIOSNameServer's IP address
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.net_bios_name_server = YLeafList()
                                        self.net_bios_name_server.parent = self
                                        self.net_bios_name_server.name = 'net_bios_name_server'

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:net-bios-name-servers'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.net_bios_name_server is not None:
                                            for child in self.net_bios_name_server:
                                                if child is not None:
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetBiosNameServers']['meta_info']


                                class ClassMatch(object):
                                    """
                                    Insert match keyword
                                    
                                    .. attribute:: class_options
                                    
                                    	Table of Class\-Option
                                    	**type**\:   :py:class:`ClassOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions>`
                                    
                                    .. attribute:: l2_interface
                                    
                                    	Specify match l2\-interface
                                    	**type**\:  str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    .. attribute:: vrf
                                    
                                    	Specify match VRF
                                    	**type**\:  str
                                    
                                    	**length:** 1..32
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.class_options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions()
                                        self.class_options.parent = self
                                        self.l2_interface = None
                                        self.vrf = None


                                    class ClassOptions(object):
                                        """
                                        Table of Class\-Option
                                        
                                        .. attribute:: class_option
                                        
                                        	Specify match option
                                        	**type**\: list of    :py:class:`ClassOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions.ClassOption>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.class_option = YList()
                                            self.class_option.parent = self
                                            self.class_option.name = 'class_option'


                                        class ClassOption(object):
                                            """
                                            Specify match option
                                            
                                            .. attribute:: matchoption  <key>
                                            
                                            	Match options
                                            	**type**\:   :py:class:`MatchoptionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.MatchoptionEnum>`
                                            
                                            .. attribute:: bit_mask
                                            
                                            	Enter bit mask pattern string
                                            	**type**\:  str
                                            
                                            	**length:** 1..64
                                            
                                            .. attribute:: pattern
                                            
                                            	Enter hex pattern string
                                            	**type**\:  str
                                            
                                            	**length:** 1..64
                                            
                                            

                                            """

                                            _prefix = 'ipv4-dhcpd-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.matchoption = None
                                                self.bit_mask = None
                                                self.pattern = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.matchoption is None:
                                                    raise YPYModelError('Key property matchoption is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:class-option[Cisco-IOS-XR-ipv4-dhcpd-cfg:matchoption = ' + str(self.matchoption) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.matchoption is not None:
                                                    return True

                                                if self.bit_mask is not None:
                                                    return True

                                                if self.pattern is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions.ClassOption']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:class-options'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.class_option is not None:
                                                for child_ref in self.class_option:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                            return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:class-match'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.class_options is not None and self.class_options._has_data():
                                            return True

                                        if self.l2_interface is not None:
                                            return True

                                        if self.vrf is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch']['meta_info']


                                class Lease(object):
                                    """
                                    lease
                                    
                                    .. attribute:: days
                                    
                                    	Days
                                    	**type**\:  int
                                    
                                    	**range:** 0..365
                                    
                                    	**units**\: day
                                    
                                    .. attribute:: hours
                                    
                                    	Hours
                                    	**type**\:  int
                                    
                                    	**range:** 0..23
                                    
                                    	**units**\: hour
                                    
                                    .. attribute:: infinite
                                    
                                    	Set string
                                    	**type**\:  str
                                    
                                    .. attribute:: minutes
                                    
                                    	Minutes
                                    	**type**\:  int
                                    
                                    	**range:** 0..59
                                    
                                    	**units**\: minute
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.days = None
                                        self.hours = None
                                        self.infinite = None
                                        self.minutes = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:lease'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.days is not None:
                                            return True

                                        if self.hours is not None:
                                            return True

                                        if self.infinite is not None:
                                            return True

                                        if self.minutes is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.Lease']['meta_info']


                                class NetbiosNodeType(object):
                                    """
                                    NetBIOS node type
                                    
                                    .. attribute:: broadcast_node
                                    
                                    	Set string
                                    	**type**\:  str
                                    
                                    .. attribute:: hexadecimal
                                    
                                    	Hexadecimal number
                                    	**type**\:  str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                                    
                                    .. attribute:: hybrid_node
                                    
                                    	Set string
                                    	**type**\:  str
                                    
                                    .. attribute:: mixed_node
                                    
                                    	Set string
                                    	**type**\:  str
                                    
                                    .. attribute:: peer_to_peer_node
                                    
                                    	Set string
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.broadcast_node = None
                                        self.hexadecimal = None
                                        self.hybrid_node = None
                                        self.mixed_node = None
                                        self.peer_to_peer_node = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:netbios-node-type'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.broadcast_node is not None:
                                            return True

                                        if self.hexadecimal is not None:
                                            return True

                                        if self.hybrid_node is not None:
                                            return True

                                        if self.mixed_node is not None:
                                            return True

                                        if self.peer_to_peer_node is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetbiosNodeType']['meta_info']


                                class DnsServers(object):
                                    """
                                    DNS servers
                                    
                                    .. attribute:: dns_server
                                    
                                    	DNS Server's IP address
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.dns_server = YLeafList()
                                        self.dns_server.parent = self
                                        self.dns_server.name = 'dns_server'

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:dns-servers'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.dns_server is not None:
                                            for child in self.dns_server:
                                                if child is not None:
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DnsServers']['meta_info']


                                class OptionCodes(object):
                                    """
                                    Table of OptionCode
                                    
                                    .. attribute:: option_code
                                    
                                    	DHCP option code
                                    	**type**\: list of    :py:class:`OptionCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes.OptionCode>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.option_code = YList()
                                        self.option_code.parent = self
                                        self.option_code.name = 'option_code'


                                    class OptionCode(object):
                                        """
                                        DHCP option code
                                        
                                        .. attribute:: option_code  <key>
                                        
                                        	DHCP option code
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: ascii_string
                                        
                                        	ASCII string
                                        	**type**\:  str
                                        
                                        .. attribute:: force_insert
                                        
                                        	Set constant integer
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: hex_string
                                        
                                        	Hexadecimal string
                                        	**type**\:  str
                                        
                                        .. attribute:: ip_address
                                        
                                        	Server's IP address
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.option_code = None
                                            self.ascii_string = None
                                            self.force_insert = None
                                            self.hex_string = None
                                            self.ip_address = YLeafList()
                                            self.ip_address.parent = self
                                            self.ip_address.name = 'ip_address'

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.option_code is None:
                                                raise YPYModelError('Key property option_code is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:option-code[Cisco-IOS-XR-ipv4-dhcpd-cfg:option-code = ' + str(self.option_code) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.option_code is not None:
                                                return True

                                            if self.ascii_string is not None:
                                                return True

                                            if self.force_insert is not None:
                                                return True

                                            if self.hex_string is not None:
                                                return True

                                            if self.ip_address is not None:
                                                for child in self.ip_address:
                                                    if child is not None:
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                            return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes.OptionCode']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:option-codes'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.option_code is not None:
                                            for child_ref in self.option_code:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.class_name is None:
                                        raise YPYModelError('Key property class_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:class[Cisco-IOS-XR-ipv4-dhcpd-cfg:class-name = ' + str(self.class_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.class_name is not None:
                                        return True

                                    if self.boot_filename is not None:
                                        return True

                                    if self.class_match is not None and self.class_match._has_data():
                                        return True

                                    if self.default_routers is not None and self.default_routers._has_data():
                                        return True

                                    if self.dns_servers is not None and self.dns_servers._has_data():
                                        return True

                                    if self.domain_name is not None:
                                        return True

                                    if self.enable is not None:
                                        return True

                                    if self.infinite_lease is not None:
                                        return True

                                    if self.lease is not None and self.lease._has_data():
                                        return True

                                    if self.net_bios_name_servers is not None and self.net_bios_name_servers._has_data():
                                        return True

                                    if self.netbios_node_type is not None and self.netbios_node_type._has_data():
                                        return True

                                    if self.next_server is not None:
                                        return True

                                    if self.option_codes is not None and self.option_codes._has_data():
                                        return True

                                    if self.pool is not None:
                                        return True

                                    if self.subnet_mask is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:classes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.class_ is not None:
                                    for child_ref in self.class_:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes']['meta_info']


                        class Relay(object):
                            """
                            Specify Relay Agent Information Option
                            configuration
                            
                            .. attribute:: authenticate
                            
                            	Specify Relay Agent Information Option authenticate
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.authenticate = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:relay'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.authenticate is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay']['meta_info']


                        class Lease(object):
                            """
                            lease
                            
                            .. attribute:: days
                            
                            	Days
                            	**type**\:  int
                            
                            	**range:** 0..365
                            
                            	**units**\: day
                            
                            .. attribute:: hours
                            
                            	Hours
                            	**type**\:  int
                            
                            	**range:** 0..23
                            
                            	**units**\: hour
                            
                            .. attribute:: infinite
                            
                            	Set string
                            	**type**\:  str
                            
                            .. attribute:: minutes
                            
                            	Minutes
                            	**type**\:  int
                            
                            	**range:** 0..59
                            
                            	**units**\: minute
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.days = None
                                self.hours = None
                                self.infinite = None
                                self.minutes = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:lease'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.days is not None:
                                    return True

                                if self.hours is not None:
                                    return True

                                if self.infinite is not None:
                                    return True

                                if self.minutes is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease']['meta_info']


                        class NetbiosNodeType(object):
                            """
                            NetBIOS node type
                            
                            .. attribute:: broadcast_node
                            
                            	Set string
                            	**type**\:  str
                            
                            .. attribute:: hexadecimal
                            
                            	Hexadecimal number
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: hybrid_node
                            
                            	Set string
                            	**type**\:  str
                            
                            .. attribute:: mixed_node
                            
                            	Set string
                            	**type**\:  str
                            
                            .. attribute:: peer_to_peer_node
                            
                            	Set string
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.broadcast_node = None
                                self.hexadecimal = None
                                self.hybrid_node = None
                                self.mixed_node = None
                                self.peer_to_peer_node = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:netbios-node-type'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.broadcast_node is not None:
                                    return True

                                if self.hexadecimal is not None:
                                    return True

                                if self.hybrid_node is not None:
                                    return True

                                if self.mixed_node is not None:
                                    return True

                                if self.peer_to_peer_node is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType']['meta_info']


                        class Aaa(object):
                            """
                            Enable aaa dhcp option force\-insert
                            
                            .. attribute:: dhcp_option
                            
                            	Enable aaa dhcp option force\-insert
                            	**type**\:   :py:class:`DhcpOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa.DhcpOption>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.dhcp_option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa.DhcpOption()
                                self.dhcp_option.parent = self


                            class DhcpOption(object):
                                """
                                Enable aaa dhcp option force\-insert
                                
                                .. attribute:: force_insert
                                
                                	Enable aaa dhcp option force\-insert
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.force_insert = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:dhcp-option'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.force_insert is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa.DhcpOption']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:aaa'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.dhcp_option is not None and self.dhcp_option._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa']['meta_info']


                        class DnsServers(object):
                            """
                            DNS servers
                            
                            .. attribute:: dns_server
                            
                            	DNS Server's IP address
                            	**type**\:  list of str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.dns_server = YLeafList()
                                self.dns_server.parent = self
                                self.dns_server.name = 'dns_server'

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:dns-servers'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.dns_server is not None:
                                    for child in self.dns_server:
                                        if child is not None:
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers']['meta_info']


                        class OptionCodes(object):
                            """
                            Table of OptionCode
                            
                            .. attribute:: option_code
                            
                            	DHCP option code
                            	**type**\: list of    :py:class:`OptionCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.option_code = YList()
                                self.option_code.parent = self
                                self.option_code.name = 'option_code'


                            class OptionCode(object):
                                """
                                DHCP option code
                                
                                .. attribute:: option_code  <key>
                                
                                	DHCP option code
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: ascii_string
                                
                                	ASCII string
                                	**type**\:  str
                                
                                .. attribute:: force_insert
                                
                                	Set constant integer
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: hex_string
                                
                                	Hexadecimal string
                                	**type**\:  str
                                
                                .. attribute:: ip_address
                                
                                	Server's IP address
                                	**type**\:  list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.option_code = None
                                    self.ascii_string = None
                                    self.force_insert = None
                                    self.hex_string = None
                                    self.ip_address = YLeafList()
                                    self.ip_address.parent = self
                                    self.ip_address.name = 'ip_address'

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.option_code is None:
                                        raise YPYModelError('Key property option_code is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:option-code[Cisco-IOS-XR-ipv4-dhcpd-cfg:option-code = ' + str(self.option_code) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.option_code is not None:
                                        return True

                                    if self.ascii_string is not None:
                                        return True

                                    if self.force_insert is not None:
                                        return True

                                    if self.hex_string is not None:
                                        return True

                                    if self.ip_address is not None:
                                        for child in self.ip_address:
                                            if child is not None:
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:option-codes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.option_code is not None:
                                    for child_ref in self.option_code:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:server'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.aaa is not None and self.aaa._has_data():
                                return True

                            if self.boot_filename is not None:
                                return True

                            if self.broadcast_flag is not None and self.broadcast_flag._has_data():
                                return True

                            if self.classes is not None and self.classes._has_data():
                                return True

                            if self.default_routers is not None and self.default_routers._has_data():
                                return True

                            if self.dns_servers is not None and self.dns_servers._has_data():
                                return True

                            if self.domain_name is not None:
                                return True

                            if self.infinite_lease is not None:
                                return True

                            if self.lease is not None and self.lease._has_data():
                                return True

                            if self.lease_limit is not None and self.lease_limit._has_data():
                                return True

                            if self.match is not None and self.match._has_data():
                                return True

                            if self.net_bios_name_servers is not None and self.net_bios_name_servers._has_data():
                                return True

                            if self.netbios_node_type is not None and self.netbios_node_type._has_data():
                                return True

                            if self.next_server is not None:
                                return True

                            if self.option_codes is not None and self.option_codes._has_data():
                                return True

                            if self.pool is not None:
                                return True

                            if self.relay is not None and self.relay._has_data():
                                return True

                            if self.requested_ip_address is not None and self.requested_ip_address._has_data():
                                return True

                            if self.secure_arp is not None:
                                return True

                            if self.server_allow_move is not None:
                                return True

                            if self.server_id_check is not None and self.server_id_check._has_data():
                                return True

                            if self.session is not None and self.session._has_data():
                                return True

                            if self.subnet_mask is not None:
                                return True

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
                        	**type**\:   :py:class:`BroadcastPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy>`
                        
                        .. attribute:: gi_addr_policy
                        
                        	GIADDR policy
                        	**type**\:   :py:class:`GiAddrPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy>`
                        
                        .. attribute:: relay_information_option
                        
                        	Relay agent information option
                        	**type**\:   :py:class:`RelayInformationOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption>`
                        
                        .. attribute:: vrfs
                        
                        	VRF Helper Addresses
                        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs>`
                        
                        

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
                            	**type**\:   :py:class:`Ipv4DhcpdGiaddrPolicyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdGiaddrPolicyEnum>`
                            
                            

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
                            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf>`
                            
                            

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
                                	**type**\:   :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses>`
                                
                                

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
                                    	**type**\: list of    :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                                    
                                    

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
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
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
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: check
                            
                            	Check Relay Agent Information Option in server reply
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: insert
                            
                            	Insert Relay Agent Information circuit ID and remote ID suboptions in client requests
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: policy
                            
                            	Relay information option policy
                            	**type**\:   :py:class:`Ipv4DhcpdRelayInfoOptionPolicyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdRelayInfoOptionPolicyEnum>`
                            
                            .. attribute:: subscriber_id
                            
                            	Subscriber ID
                            	**type**\:  str
                            
                            .. attribute:: vpn
                            
                            	Insert VPN options
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: vpn_mode
                            
                            	VPN Mode
                            	**type**\:   :py:class:`Ipv4DhcpdRelayInfoOptionvpnModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdRelayInfoOptionvpnModeEnum>`
                            
                            

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
                            	**type**\:   :py:class:`Ipv4DhcpdBroadcastFlagPolicyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdBroadcastFlagPolicyEnum>`
                            
                            

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


                    class Proxy(object):
                        """
                        DHCP proxy profile
                        
                        .. attribute:: broadcast_flag
                        
                        	Specify broadcast flag
                        	**type**\:   :py:class:`BroadcastFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag>`
                        
                        .. attribute:: classes
                        
                        	DHCP class table
                        	**type**\:   :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes>`
                        
                        .. attribute:: enable
                        
                        	DHCP IPV4 profile mode enable
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: lease_proxy
                        
                        	DHCPv4 lease proxy
                        	**type**\:   :py:class:`LeaseProxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy>`
                        
                        .. attribute:: limit_lease
                        
                        	Proxy limit lease
                        	**type**\:   :py:class:`LimitLease <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: match
                        
                        	Insert match keyword
                        	**type**\:   :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match>`
                        
                        .. attribute:: proxy_allow_move
                        
                        	Allow dhcp subscriber move
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: relay_information
                        
                        	Relay agent information option
                        	**type**\:   :py:class:`RelayInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation>`
                        
                        .. attribute:: secure_arp
                        
                        	DHCP IPV4 profile proxy secure\-arp enable
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: sessions
                        
                        	Change sessions configuration
                        	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions>`
                        
                        .. attribute:: vrfs
                        
                        	List of VRFs
                        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.broadcast_flag = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag()
                            self.broadcast_flag.parent = self
                            self.classes = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes()
                            self.classes.parent = self
                            self.enable = None
                            self.lease_proxy = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy()
                            self.lease_proxy.parent = self
                            self.limit_lease = None
                            self.match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match()
                            self.match.parent = self
                            self.proxy_allow_move = None
                            self.relay_information = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation()
                            self.relay_information.parent = self
                            self.secure_arp = None
                            self.sessions = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions()
                            self.sessions.parent = self
                            self.vrfs = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs()
                            self.vrfs.parent = self


                        class Classes(object):
                            """
                            DHCP class table
                            
                            .. attribute:: class_
                            
                            	DHCP class
                            	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.class_ = YList()
                                self.class_.parent = self
                                self.class_.name = 'class_'


                            class Class_(object):
                                """
                                DHCP class
                                
                                .. attribute:: class_name  <key>
                                
                                	Class name
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: enable
                                
                                	Enable the DHCP IPV4 proxy class
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: match
                                
                                	Match option
                                	**type**\:   :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match>`
                                
                                .. attribute:: vrfs
                                
                                	List of VRFs
                                	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.class_name = None
                                    self.enable = None
                                    self.match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match()
                                    self.match.parent = self
                                    self.vrfs = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs()
                                    self.vrfs.parent = self


                                class Match(object):
                                    """
                                    Match option
                                    
                                    .. attribute:: option
                                    
                                    	Match option
                                    	**type**\:   :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match.Option>`
                                    
                                    .. attribute:: vrf
                                    
                                    	Match VRF name
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match.Option()
                                        self.option.parent = self
                                        self.vrf = None


                                    class Option(object):
                                        """
                                        Match option
                                        
                                        .. attribute:: bit_mask
                                        
                                        	Bit mask pattern
                                        	**type**\:  str
                                        
                                        .. attribute:: option_type
                                        
                                        	Match option
                                        	**type**\:   :py:class:`Dhcpv4MatchOptionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Dhcpv4MatchOptionEnum>`
                                        
                                        .. attribute:: pattern
                                        
                                        	Hex pattern string
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.bit_mask = None
                                            self.option_type = None
                                            self.pattern = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:option'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.bit_mask is not None:
                                                return True

                                            if self.option_type is not None:
                                                return True

                                            if self.pattern is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                            return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match.Option']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:match'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.option is not None and self.option._has_data():
                                            return True

                                        if self.vrf is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match']['meta_info']


                                class Vrfs(object):
                                    """
                                    List of VRFs
                                    
                                    .. attribute:: vrf
                                    
                                    	VRF name
                                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf>`
                                    
                                    

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
                                        VRF name
                                        
                                        .. attribute:: vrf_name  <key>
                                        
                                        	VRF name
                                        	**type**\:  str
                                        
                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                        
                                        .. attribute:: helper_addresses
                                        
                                        	Helper addresses
                                        	**type**\:   :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.vrf_name = None
                                            self.helper_addresses = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses()
                                            self.helper_addresses.parent = self


                                        class HelperAddresses(object):
                                            """
                                            Helper addresses
                                            
                                            .. attribute:: helper_address
                                            
                                            	Helper address
                                            	**type**\: list of    :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                                            
                                            

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
                                                Helper address
                                                
                                                .. attribute:: server_address  <key>
                                                
                                                	IPv4 address
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: gateway_address
                                                
                                                	Gateway address
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                	**mandatory**\: True
                                                
                                                

                                                """

                                                _prefix = 'ipv4-dhcpd-cfg'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.server_address = None
                                                    self.gateway_address = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                                    if self.server_address is None:
                                                        raise YPYModelError('Key property server_address is None')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:helper-address[Cisco-IOS-XR-ipv4-dhcpd-cfg:server-address = ' + str(self.server_address) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return True

                                                def _has_data(self):
                                                    if self.server_address is not None:
                                                        return True

                                                    if self.gateway_address is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses.HelperAddress']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:helper-addresses'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.helper_address is not None:
                                                    for child_ref in self.helper_address:
                                                        if child_ref._has_data():
                                                            return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses']['meta_info']

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
                                            if self.vrf_name is not None:
                                                return True

                                            if self.helper_addresses is not None and self.helper_addresses._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                            return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:vrfs'

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
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.class_name is None:
                                        raise YPYModelError('Key property class_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:class[Cisco-IOS-XR-ipv4-dhcpd-cfg:class-name = ' + str(self.class_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.class_name is not None:
                                        return True

                                    if self.enable is not None:
                                        return True

                                    if self.match is not None and self.match._has_data():
                                        return True

                                    if self.vrfs is not None and self.vrfs._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:classes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.class_ is not None:
                                    for child_ref in self.class_:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes']['meta_info']


                        class RelayInformation(object):
                            """
                            Relay agent information option
                            
                            .. attribute:: allow_untrusted
                            
                            	Forward untrusted packets
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: authenticate
                            
                            	Relay information option authenticate
                            	**type**\:   :py:class:`Ipv4DhcpdRelayInfoOptionAuthenticateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdRelayInfoOptionAuthenticateEnum>`
                            
                            .. attribute:: check
                            
                            	Check relay agent information option in server reply
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: circuit_id
                            
                            	Insert Circuit\-id sub\-option
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: option
                            
                            	Insert relay rgent information circuit ID and remote ID suboptions in client requests
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: policy
                            
                            	Relay information option policy
                            	**type**\:   :py:class:`Ipv4DhcpdRelayInfoOptionPolicyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdRelayInfoOptionPolicyEnum>`
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\:  str
                            
                            .. attribute:: remote_id_suppress
                            
                            	Suppress Remote ID
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: remote_id_xr
                            
                            	Insert Remote\-id sub\-option
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: vpn
                            
                            	Insert VPN options
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: vpn_mode
                            
                            	VPN Mode
                            	**type**\:   :py:class:`Ipv4DhcpdRelayInfoOptionvpnModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdRelayInfoOptionvpnModeEnum>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.allow_untrusted = None
                                self.authenticate = None
                                self.check = None
                                self.circuit_id = None
                                self.option = None
                                self.policy = None
                                self.remote_id = None
                                self.remote_id_suppress = None
                                self.remote_id_xr = None
                                self.vpn = None
                                self.vpn_mode = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:relay-information'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.allow_untrusted is not None:
                                    return True

                                if self.authenticate is not None:
                                    return True

                                if self.check is not None:
                                    return True

                                if self.circuit_id is not None:
                                    return True

                                if self.option is not None:
                                    return True

                                if self.policy is not None:
                                    return True

                                if self.remote_id is not None:
                                    return True

                                if self.remote_id_suppress is not None:
                                    return True

                                if self.remote_id_xr is not None:
                                    return True

                                if self.vpn is not None:
                                    return True

                                if self.vpn_mode is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation']['meta_info']


                        class Vrfs(object):
                            """
                            List of VRFs
                            
                            .. attribute:: vrf
                            
                            	VRF name
                            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf>`
                            
                            

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
                                VRF name
                                
                                .. attribute:: vrf_name  <key>
                                
                                	VRF name
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: helper_addresses
                                
                                	Helper addresses
                                	**type**\:   :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.vrf_name = None
                                    self.helper_addresses = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses()
                                    self.helper_addresses.parent = self


                                class HelperAddresses(object):
                                    """
                                    Helper addresses
                                    
                                    .. attribute:: helper_address
                                    
                                    	Helper address
                                    	**type**\: list of    :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                                    
                                    

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
                                        Helper address
                                        
                                        .. attribute:: server_address  <key>
                                        
                                        	IPv4 address
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: gateway_address
                                        
                                        	Gateway address
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.server_address = None
                                            self.gateway_address = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.server_address is None:
                                                raise YPYModelError('Key property server_address is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:helper-address[Cisco-IOS-XR-ipv4-dhcpd-cfg:server-address = ' + str(self.server_address) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.server_address is not None:
                                                return True

                                            if self.gateway_address is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                            return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:helper-addresses'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.helper_address is not None:
                                            for child_ref in self.helper_address:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses']['meta_info']

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
                                    if self.vrf_name is not None:
                                        return True

                                    if self.helper_addresses is not None and self.helper_addresses._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:vrfs'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs']['meta_info']


                        class Sessions(object):
                            """
                            Change sessions configuration
                            
                            .. attribute:: proxy_throttle_type
                            
                            	Throttle DHCP sessions based on MAC address
                            	**type**\:   :py:class:`ProxyThrottleType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.proxy_throttle_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType()
                                self.proxy_throttle_type.parent = self


                            class ProxyThrottleType(object):
                                """
                                Throttle DHCP sessions based on MAC
                                address
                                
                                .. attribute:: proxy_mac_throttle
                                
                                	Throttle DHCP sessions from any one MAC address
                                	**type**\:   :py:class:`ProxyMacThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.proxy_mac_throttle = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle()
                                    self.proxy_mac_throttle.parent = self


                                class ProxyMacThrottle(object):
                                    """
                                    Throttle DHCP sessions from any one MAC
                                    address
                                    
                                    .. attribute:: num_block
                                    
                                    	Throttle blocking period (in secs)
                                    	**type**\:  int
                                    
                                    	**range:** 1..100
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: num_discover
                                    
                                    	Number of discovers at which to throttle
                                    	**type**\:  int
                                    
                                    	**range:** 1..65535
                                    
                                    .. attribute:: num_request
                                    
                                    	Throttle request period (in secs)
                                    	**type**\:  int
                                    
                                    	**range:** 1..100
                                    
                                    	**units**\: second
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.num_block = None
                                        self.num_discover = None
                                        self.num_request = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:proxy-mac-throttle'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.num_block is not None:
                                            return True

                                        if self.num_discover is not None:
                                            return True

                                        if self.num_request is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:proxy-throttle-type'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.proxy_mac_throttle is not None and self.proxy_mac_throttle._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:sessions'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.proxy_throttle_type is not None and self.proxy_throttle_type._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions']['meta_info']


                        class LimitLease(object):
                            """
                            Proxy limit lease
                            
                            .. attribute:: limit_lease_count
                            
                            	Limit lease count
                            	**type**\:  int
                            
                            	**range:** 1..240000
                            
                            	**mandatory**\: True
                            
                            .. attribute:: limit_type
                            
                            	Lease limit type
                            	**type**\:   :py:class:`Dhcpv4LimitLease1Enum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Dhcpv4LimitLease1Enum>`
                            
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
                                self.limit_lease_count = None
                                self.limit_type = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:limit-lease'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self._is_presence:
                                    return True
                                if self.limit_lease_count is not None:
                                    return True

                                if self.limit_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease']['meta_info']


                        class LeaseProxy(object):
                            """
                            DHCPv4 lease proxy
                            
                            .. attribute:: client_lease_time
                            
                            	Specify client lease proxy time
                            	**type**\:  int
                            
                            	**range:** 300..4294967295
                            
                            .. attribute:: set_server_options
                            
                            	Set DHCP server sent options in lease proxy generating ACK
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.client_lease_time = None
                                self.set_server_options = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:lease-proxy'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.client_lease_time is not None:
                                    return True

                                if self.set_server_options is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy']['meta_info']


                        class BroadcastFlag(object):
                            """
                            Specify broadcast flag
                            
                            .. attribute:: policy
                            
                            	Broadcast flag policy
                            	**type**\:   :py:class:`Ipv4DhcpdBroadcastFlagPolicyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdBroadcastFlagPolicyEnum>`
                            
                            

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

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:broadcast-flag'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.policy is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag']['meta_info']


                        class Match(object):
                            """
                            Insert match keyword
                            
                            .. attribute:: def_options
                            
                            	Table of Option
                            	**type**\:   :py:class:`DefOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions>`
                            
                            .. attribute:: option_filters
                            
                            	Table of Option
                            	**type**\:   :py:class:`OptionFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.def_options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions()
                                self.def_options.parent = self
                                self.option_filters = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters()
                                self.option_filters.parent = self


                            class DefOptions(object):
                                """
                                Table of Option
                                
                                .. attribute:: def_option
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`DefOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.def_option = YList()
                                    self.def_option.parent = self
                                    self.def_option.name = 'def_option'


                                class DefOption(object):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: def_matchoption  <key>
                                    
                                    	Match option 60
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: def_matchaction
                                    
                                    	Vendor action
                                    	**type**\:   :py:class:`ProxyActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.ProxyActionEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.def_matchoption = None
                                        self.def_matchaction = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.def_matchoption is None:
                                            raise YPYModelError('Key property def_matchoption is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:def-option[Cisco-IOS-XR-ipv4-dhcpd-cfg:def-matchoption = ' + str(self.def_matchoption) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.def_matchoption is not None:
                                            return True

                                        if self.def_matchaction is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:def-options'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.def_option is not None:
                                        for child_ref in self.def_option:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions']['meta_info']


                            class OptionFilters(object):
                                """
                                Table of Option
                                
                                .. attribute:: option_filter
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`OptionFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.option_filter = YList()
                                    self.option_filter.parent = self
                                    self.option_filter.name = 'option_filter'


                                class OptionFilter(object):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: matchoption  <key>
                                    
                                    	Match option 60
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: pattern  <key>
                                    
                                    	Enter hex pattern string
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: format  <key>
                                    
                                    	Set constant integer
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: matchaction
                                    
                                    	Vendor action
                                    	**type**\:   :py:class:`ProxyActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.ProxyActionEnum>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.matchoption = None
                                        self.pattern = None
                                        self.format = None
                                        self.matchaction = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.matchoption is None:
                                            raise YPYModelError('Key property matchoption is None')
                                        if self.pattern is None:
                                            raise YPYModelError('Key property pattern is None')
                                        if self.format is None:
                                            raise YPYModelError('Key property format is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:option-filter[Cisco-IOS-XR-ipv4-dhcpd-cfg:matchoption = ' + str(self.matchoption) + '][Cisco-IOS-XR-ipv4-dhcpd-cfg:pattern = ' + str(self.pattern) + '][Cisco-IOS-XR-ipv4-dhcpd-cfg:format = ' + str(self.format) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.matchoption is not None:
                                            return True

                                        if self.pattern is not None:
                                            return True

                                        if self.format is not None:
                                            return True

                                        if self.matchaction is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                        return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:option-filters'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.option_filter is not None:
                                        for child_ref in self.option_filter:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                    return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:match'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.def_options is not None and self.def_options._has_data():
                                    return True

                                if self.option_filters is not None and self.option_filters._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                                return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:proxy'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.broadcast_flag is not None and self.broadcast_flag._has_data():
                                return True

                            if self.classes is not None and self.classes._has_data():
                                return True

                            if self.enable is not None:
                                return True

                            if self.lease_proxy is not None and self.lease_proxy._has_data():
                                return True

                            if self.limit_lease is not None and self.limit_lease._has_data():
                                return True

                            if self.match is not None and self.match._has_data():
                                return True

                            if self.proxy_allow_move is not None:
                                return True

                            if self.relay_information is not None and self.relay_information._has_data():
                                return True

                            if self.secure_arp is not None:
                                return True

                            if self.sessions is not None and self.sessions._has_data():
                                return True

                            if self.vrfs is not None and self.vrfs._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                            return meta._meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy']['meta_info']

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
                        if self.mode is not None:
                            return True

                        if self.base is not None and self.base._has_data():
                            return True

                        if self.enable is not None:
                            return True

                        if self.proxy is not None and self.proxy._has_data():
                            return True

                        if self.relay is not None and self.relay._has_data():
                            return True

                        if self.server is not None and self.server._has_data():
                            return True

                        if self.snoop is not None and self.snoop._has_data():
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
        
        	**default value**\: 10
        
        .. attribute:: incremental_write_interval
        
        	Incremental file write interval (default 1 minutes)
        	**type**\:  int
        
        	**range:** 1..1440
        
        	**default value**\: 1
        
        .. attribute:: proxy
        
        	Enable DHCP proxy binding database storage to file system
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: server
        
        	Enable DHCP server binding database storage to file system
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: snoop
        
        	Enable DHCP snoop binding database storage to file system
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

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
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface>`
        
        

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
            	**type**\:   :py:class:`BaseInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.BaseInterface>`
            
            .. attribute:: none
            
            	DHCP IPV4 disabled
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: profile
            
            	Profile name and mode
            	**type**\:   :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.Profile>`
            
            	**presence node**\: True
            
            .. attribute:: proxy_interface
            
            	DHCP IPv4 proxy information
            	**type**\:   :py:class:`ProxyInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.ProxyInterface>`
            
            .. attribute:: relay_interface
            
            	DHCP IPv4 relay information
            	**type**\:   :py:class:`RelayInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.RelayInterface>`
            
            .. attribute:: server_interface
            
            	DHCP IPv4 Server information
            	**type**\:   :py:class:`ServerInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.ServerInterface>`
            
            .. attribute:: snoop_interface
            
            	DHCP IPv4 snoop information
            	**type**\:   :py:class:`SnoopInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.SnoopInterface>`
            
            .. attribute:: static_mode
            
            	Static Table Entries containing MAC address to IP address bindings
            	**type**\:   :py:class:`StaticMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.StaticMode>`
            
            

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
                self.static_mode = Ipv4Dhcpd.Interfaces.Interface.StaticMode()
                self.static_mode.parent = self


            class ProxyInterface(object):
                """
                DHCP IPv4 proxy information
                
                .. attribute:: dhcp_circuit_id
                
                	Circuit ID value
                	**type**\:   :py:class:`DhcpCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId>`
                
                	**presence node**\: True
                
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
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:   :py:class:`Ipv4DhcpdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtEnum>`
                    
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
                
                .. attribute:: base_dhcp_circuit_id
                
                	Circuit ID value
                	**type**\:   :py:class:`BaseDhcpCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId>`
                
                	**presence node**\: True
                
                .. attribute:: profile
                
                	Interface profile name
                	**type**\:  str
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.base_dhcp_circuit_id = None
                    self.profile = None


                class BaseDhcpCircuitId(object):
                    """
                    Circuit ID value
                    
                    .. attribute:: argument1
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:   :py:class:`Ipv4DhcpdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtEnum>`
                    
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

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:base-dhcp-circuit-id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
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
                        return meta._meta_table['Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:base-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.base_dhcp_circuit_id is not None and self.base_dhcp_circuit_id._has_data():
                        return True

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
                	**type**\:   :py:class:`RelayDhcpCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId>`
                
                	**presence node**\: True
                
                

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
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:   :py:class:`Ipv4DhcpdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtEnum>`
                    
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
                    if self.relay_dhcp_circuit_id is not None and self.relay_dhcp_circuit_id._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                    return meta._meta_table['Ipv4Dhcpd.Interfaces.Interface.RelayInterface']['meta_info']


            class StaticMode(object):
                """
                Static Table Entries containing MAC address to
                IP address bindings
                
                .. attribute:: statics
                
                	Static Table Entries containing MAC address to IP address bindings
                	**type**\:   :py:class:`Statics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics>`
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.statics = Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics()
                    self.statics.parent = self


                class Statics(object):
                    """
                    Static Table Entries containing MAC address
                    to IP address bindings
                    
                    .. attribute:: static
                    
                    	DHCP static binding of Mac address to IP address
                    	**type**\: list of    :py:class:`Static <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.static = YList()
                        self.static.parent = self
                        self.static.name = 'static'


                    class Static(object):
                        """
                        DHCP static binding of Mac address to IP
                        address
                        
                        .. attribute:: mac_address  <key>
                        
                        	MACAddress
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: client_id  <key>
                        
                        	Client Id
                        	**type**\:  int
                        
                        	**range:** 1..4294967295
                        
                        .. attribute:: layer  <key>
                        
                        	DHCP IPV4 Static layer
                        	**type**\:   :py:class:`Ipv4DhcpdLayerEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdLayerEnum>`
                        
                        .. attribute:: static_address
                        
                        	IP address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.mac_address = None
                            self.client_id = None
                            self.layer = None
                            self.static_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.mac_address is None:
                                raise YPYModelError('Key property mac_address is None')
                            if self.client_id is None:
                                raise YPYModelError('Key property client_id is None')
                            if self.layer is None:
                                raise YPYModelError('Key property layer is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:static[Cisco-IOS-XR-ipv4-dhcpd-cfg:mac-address = ' + str(self.mac_address) + '][Cisco-IOS-XR-ipv4-dhcpd-cfg:client-id = ' + str(self.client_id) + '][Cisco-IOS-XR-ipv4-dhcpd-cfg:layer = ' + str(self.layer) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.mac_address is not None:
                                return True

                            if self.client_id is not None:
                                return True

                            if self.layer is not None:
                                return True

                            if self.static_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                            return meta._meta_table['Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:statics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.static is not None:
                            for child_ref in self.static:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                        return meta._meta_table['Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:static-mode'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.statics is not None and self.statics._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_cfg as meta
                    return meta._meta_table['Ipv4Dhcpd.Interfaces.Interface.StaticMode']['meta_info']


            class Profile(object):
                """
                Profile name and mode
                
                .. attribute:: mode
                
                	DHCP mode
                	**type**\:   :py:class:`Ipv4DhcpdModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdModeEnum>`
                
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
                
                .. attribute:: server_dhcp_circuit_id
                
                	Circuit ID value
                	**type**\:   :py:class:`ServerDhcpCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.profile = None
                    self.server_dhcp_circuit_id = None


                class ServerDhcpCircuitId(object):
                    """
                    Circuit ID value
                    
                    .. attribute:: argument1
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifierEnum>`
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:   :py:class:`Ipv4DhcpdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtEnum>`
                    
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

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:server-dhcp-circuit-id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
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
                        return meta._meta_table['Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-cfg:server-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.profile is not None:
                        return True

                    if self.server_dhcp_circuit_id is not None and self.server_dhcp_circuit_id._has_data():
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
                	**type**\:   :py:class:`SnoopCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId>`
                
                

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

                if self.static_mode is not None and self.static_mode._has_data():
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
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        .. attribute:: exclude_vlan
        
        	Exclude vlan
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
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
        
        	**default value**\: 100
        
        .. attribute:: num_period
        
        	Rate limiter period in msec (default\: 200 msec)
        	**type**\:  int
        
        	**range:** 1..1000
        
        	**default value**\: 200
        
        

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
        if self.allow_client_id_change is not None:
            return True

        if self.database is not None and self.database._has_data():
            return True

        if self.duplicate_mac_allowed is not None and self.duplicate_mac_allowed._has_data():
            return True

        if self.enable is not None:
            return True

        if self.inner_cos is not None:
            return True

        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.outer_cos is not None:
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


