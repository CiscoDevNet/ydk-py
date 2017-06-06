""" Cisco_IOS_XR_ip_rip_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-rip package configuration.

This module contains definitions
for the following management objects\:
  rip\: RIP configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BgpRedistRouteEnum(Enum):
    """
    BgpRedistRouteEnum

    Bgp redist route

    .. data:: all = 0

    	All routes

    .. data:: internal = 512

    	Internal routes only

    .. data:: external = 1024

    	External routes only

    .. data:: local = 2048

    	Local routes only

    """

    all = 0

    internal = 512

    external = 1024

    local = 2048


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
        return meta._meta_table['BgpRedistRouteEnum']


class DefaultInformationOptionEnum(Enum):
    """
    DefaultInformationOptionEnum

    Default information option

    .. data:: always = 0

    	Always

    .. data:: policy = 1

    	Use route-policy

    """

    always = 0

    policy = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
        return meta._meta_table['DefaultInformationOptionEnum']


class DefaultRedistRouteEnum(Enum):
    """
    DefaultRedistRouteEnum

    Default redist route

    .. data:: all = 0

    	All routes

    """

    all = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
        return meta._meta_table['DefaultRedistRouteEnum']


class IsisRedistRouteEnum(Enum):
    """
    IsisRedistRouteEnum

    Isis redist route

    .. data:: level1 = 1

    	Level-1 routes only

    .. data:: level2 = 2

    	Level-1 routes only

    .. data:: level1_and2 = 3

    	Level-1 and level-2 routes

    """

    level1 = 1

    level2 = 2

    level1_and2 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
        return meta._meta_table['IsisRedistRouteEnum']


class RipAuthModeEnum(Enum):
    """
    RipAuthModeEnum

    Rip auth mode

    .. data:: text = 2

    	Text mode

    .. data:: md5 = 3

    	MD5 mode

    """

    text = 2

    md5 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
        return meta._meta_table['RipAuthModeEnum']


class RipExtCommunityEnum(Enum):
    """
    RipExtCommunityEnum

    Rip ext community

    .. data:: as_ = 0

    	AS:nn format

    .. data:: ipv4_address = 1

    	IPV4Address:nn format

    .. data:: four_byte_as = 2

    	4-byte ASN format

    """

    as_ = 0

    ipv4_address = 1

    four_byte_as = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
        return meta._meta_table['RipExtCommunityEnum']



class Rip(object):
    """
    RIP configuration
    
    .. attribute:: default_vrf
    
    	RIP configuration for Default VRF
    	**type**\:   :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf>`
    
    .. attribute:: vrfs
    
    	VRF related RIP configuration
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs>`
    
    

    """

    _prefix = 'ip-rip-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.default_vrf = Rip.DefaultVrf()
        self.default_vrf.parent = self
        self.vrfs = Rip.Vrfs()
        self.vrfs.parent = self


    class DefaultVrf(object):
        """
        RIP configuration for Default VRF
        
        .. attribute:: auto_summary
        
        	Enable automatic network number summarization
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: broadcast_for_v2
        
        	Send RIP v2 output packets to broadcast address
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: default_information
        
        	Controls default information origination
        	**type**\:   :py:class:`DefaultInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.DefaultInformation>`
        
        	**presence node**\: True
        
        .. attribute:: default_metric
        
        	Default metric of redistributed routes
        	**type**\:  int
        
        	**range:** 0..16
        
        .. attribute:: distance
        
        	Administrative distance
        	**type**\:  int
        
        	**range:** 0..255
        
        	**default value**\: 120
        
        .. attribute:: enable
        
        	Starts RIP configuration for Default VRF
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: interfaces
        
        	Table of RIP interfaces
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces>`
        
        .. attribute:: ip_distances
        
        	Table of IP specific administrative distances
        	**type**\:   :py:class:`IpDistances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.IpDistances>`
        
        .. attribute:: maximum_paths
        
        	Maximum number of paths allowed per route
        	**type**\:  int
        
        	**range:** 1..128
        
        	**default value**\: 4
        
        .. attribute:: neighbors
        
        	Configure RIP Neighbors
        	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Neighbors>`
        
        .. attribute:: nsf
        
        	Enable Cisco Non Stop Forwarding
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: output_delay
        
        	Inter\-packet delay for RIP updates
        	**type**\:  int
        
        	**range:** 8..50
        
        	**units**\: millisecond
        
        .. attribute:: policy_in
        
        	Route Policy for inbbound routing updates
        	**type**\:  str
        
        .. attribute:: policy_out
        
        	Route Policy for outbound routing updates
        	**type**\:  str
        
        .. attribute:: redistribution
        
        	Redistribute information from another routing protocol
        	**type**\:   :py:class:`Redistribution <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution>`
        
        .. attribute:: timers
        
        	Various routing timers
        	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Timers>`
        
        .. attribute:: validate_source_disable
        
        	Disable validation of source address of routing updates
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ip-rip-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.auto_summary = None
            self.broadcast_for_v2 = None
            self.default_information = None
            self.default_metric = None
            self.distance = None
            self.enable = None
            self.interfaces = Rip.DefaultVrf.Interfaces()
            self.interfaces.parent = self
            self.ip_distances = Rip.DefaultVrf.IpDistances()
            self.ip_distances.parent = self
            self.maximum_paths = None
            self.neighbors = Rip.DefaultVrf.Neighbors()
            self.neighbors.parent = self
            self.nsf = None
            self.output_delay = None
            self.policy_in = None
            self.policy_out = None
            self.redistribution = Rip.DefaultVrf.Redistribution()
            self.redistribution.parent = self
            self.timers = Rip.DefaultVrf.Timers()
            self.timers.parent = self
            self.validate_source_disable = None


        class DefaultInformation(object):
            """
            Controls default information origination
            
            .. attribute:: option
            
            	Origination option
            	**type**\:   :py:class:`DefaultInformationOptionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultInformationOptionEnum>`
            
            	**mandatory**\: True
            
            .. attribute:: route_policy_name
            
            	Route policy name
            	**type**\:  str
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self._is_presence = True
                self.option = None
                self.route_policy_name = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:default-information'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self._is_presence:
                    return True
                if self.option is not None:
                    return True

                if self.route_policy_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                return meta._meta_table['Rip.DefaultVrf.DefaultInformation']['meta_info']


        class Redistribution(object):
            """
            Redistribute information from another routing
            protocol
            
            .. attribute:: bgps
            
            	Redistribute BGP routes
            	**type**\:   :py:class:`Bgps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Bgps>`
            
            .. attribute:: connected
            
            	Redistribute connected routes
            	**type**\:   :py:class:`Connected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Connected>`
            
            	**presence node**\: True
            
            .. attribute:: eigrp_s
            
            	Redistribute EIGRP routes
            	**type**\:   :py:class:`EigrpS <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.EigrpS>`
            
            .. attribute:: isises
            
            	Redistribute IS\-IS routes
            	**type**\:   :py:class:`Isises <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Isises>`
            
            .. attribute:: ospfs
            
            	Redistribute OSPF routes
            	**type**\:   :py:class:`Ospfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Ospfs>`
            
            .. attribute:: static
            
            	Redistribute static routes
            	**type**\:   :py:class:`Static <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Static>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bgps = Rip.DefaultVrf.Redistribution.Bgps()
                self.bgps.parent = self
                self.connected = None
                self.eigrp_s = Rip.DefaultVrf.Redistribution.EigrpS()
                self.eigrp_s.parent = self
                self.isises = Rip.DefaultVrf.Redistribution.Isises()
                self.isises.parent = self
                self.ospfs = Rip.DefaultVrf.Redistribution.Ospfs()
                self.ospfs.parent = self
                self.static = None


            class Connected(object):
                """
                Redistribute connected routes
                
                .. attribute:: route_policy_name
                
                	Route Policy name
                	**type**\:  str
                
                .. attribute:: route_type
                
                	Route type
                	**type**\:   :py:class:`DefaultRedistRouteEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRouteEnum>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.route_policy_name = None
                    self.route_type = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:redistribution/Cisco-IOS-XR-ip-rip-cfg:connected'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.route_policy_name is not None:
                        return True

                    if self.route_type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                    return meta._meta_table['Rip.DefaultVrf.Redistribution.Connected']['meta_info']


            class Bgps(object):
                """
                Redistribute BGP routes
                
                .. attribute:: bgp
                
                	Autonomous system number
                	**type**\: list of    :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Bgps.Bgp>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bgp = YList()
                    self.bgp.parent = self
                    self.bgp.name = 'bgp'


                class Bgp(object):
                    """
                    Autonomous system number
                    
                    .. attribute:: asnxx  <key>
                    
                    	Higher 16 bits of 4\-byte BGP AS number
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: asnyy  <key>
                    
                    	2\-byte or 4\-byte BGP AS number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: policy
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    .. attribute:: type
                    
                    	Route type
                    	**type**\:   :py:class:`BgpRedistRouteEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.BgpRedistRouteEnum>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.asnxx = None
                        self.asnyy = None
                        self.policy = None
                        self.type = None

                    @property
                    def _common_path(self):
                        if self.asnxx is None:
                            raise YPYModelError('Key property asnxx is None')
                        if self.asnyy is None:
                            raise YPYModelError('Key property asnyy is None')

                        return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:redistribution/Cisco-IOS-XR-ip-rip-cfg:bgps/Cisco-IOS-XR-ip-rip-cfg:bgp[Cisco-IOS-XR-ip-rip-cfg:asnxx = ' + str(self.asnxx) + '][Cisco-IOS-XR-ip-rip-cfg:asnyy = ' + str(self.asnyy) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.asnxx is not None:
                            return True

                        if self.asnyy is not None:
                            return True

                        if self.policy is not None:
                            return True

                        if self.type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                        return meta._meta_table['Rip.DefaultVrf.Redistribution.Bgps.Bgp']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:redistribution/Cisco-IOS-XR-ip-rip-cfg:bgps'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.bgp is not None:
                        for child_ref in self.bgp:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                    return meta._meta_table['Rip.DefaultVrf.Redistribution.Bgps']['meta_info']


            class Isises(object):
                """
                Redistribute IS\-IS routes
                
                .. attribute:: isis
                
                	Redistribute IS\-IS routes
                	**type**\: list of    :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Isises.Isis>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.isis = YList()
                    self.isis.parent = self
                    self.isis.name = 'isis'


                class Isis(object):
                    """
                    Redistribute IS\-IS routes
                    
                    .. attribute:: isis_name  <key>
                    
                    	IS\-IS instance name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    .. attribute:: route_type
                    
                    	Route type
                    	**type**\:   :py:class:`IsisRedistRouteEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.IsisRedistRouteEnum>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.isis_name = None
                        self.route_policy_name = None
                        self.route_type = None

                    @property
                    def _common_path(self):
                        if self.isis_name is None:
                            raise YPYModelError('Key property isis_name is None')

                        return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:redistribution/Cisco-IOS-XR-ip-rip-cfg:isises/Cisco-IOS-XR-ip-rip-cfg:isis[Cisco-IOS-XR-ip-rip-cfg:isis-name = ' + str(self.isis_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.isis_name is not None:
                            return True

                        if self.route_policy_name is not None:
                            return True

                        if self.route_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                        return meta._meta_table['Rip.DefaultVrf.Redistribution.Isises.Isis']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:redistribution/Cisco-IOS-XR-ip-rip-cfg:isises'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.isis is not None:
                        for child_ref in self.isis:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                    return meta._meta_table['Rip.DefaultVrf.Redistribution.Isises']['meta_info']


            class EigrpS(object):
                """
                Redistribute EIGRP routes
                
                .. attribute:: eigrp
                
                	Redistribute EIGRP routes
                	**type**\: list of    :py:class:`Eigrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.EigrpS.Eigrp>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.eigrp = YList()
                    self.eigrp.parent = self
                    self.eigrp.name = 'eigrp'


                class Eigrp(object):
                    """
                    Redistribute EIGRP routes
                    
                    .. attribute:: as_  <key>
                    
                    	Autonomous system number
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    .. attribute:: route_type
                    
                    	Route type
                    	**type**\:   :py:class:`DefaultRedistRouteEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRouteEnum>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.as_ = None
                        self.route_policy_name = None
                        self.route_type = None

                    @property
                    def _common_path(self):
                        if self.as_ is None:
                            raise YPYModelError('Key property as_ is None')

                        return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:redistribution/Cisco-IOS-XR-ip-rip-cfg:eigrp-s/Cisco-IOS-XR-ip-rip-cfg:eigrp[Cisco-IOS-XR-ip-rip-cfg:as = ' + str(self.as_) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.as_ is not None:
                            return True

                        if self.route_policy_name is not None:
                            return True

                        if self.route_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                        return meta._meta_table['Rip.DefaultVrf.Redistribution.EigrpS.Eigrp']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:redistribution/Cisco-IOS-XR-ip-rip-cfg:eigrp-s'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.eigrp is not None:
                        for child_ref in self.eigrp:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                    return meta._meta_table['Rip.DefaultVrf.Redistribution.EigrpS']['meta_info']


            class Static(object):
                """
                Redistribute static routes
                
                .. attribute:: route_policy_name
                
                	Route Policy name
                	**type**\:  str
                
                .. attribute:: route_type
                
                	Route type
                	**type**\:   :py:class:`DefaultRedistRouteEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRouteEnum>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.route_policy_name = None
                    self.route_type = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:redistribution/Cisco-IOS-XR-ip-rip-cfg:static'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.route_policy_name is not None:
                        return True

                    if self.route_type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                    return meta._meta_table['Rip.DefaultVrf.Redistribution.Static']['meta_info']


            class Ospfs(object):
                """
                Redistribute OSPF routes
                
                .. attribute:: ospf
                
                	Redistribute OSPF routes
                	**type**\: list of    :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Redistribution.Ospfs.Ospf>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ospf = YList()
                    self.ospf.parent = self
                    self.ospf.name = 'ospf'


                class Ospf(object):
                    """
                    Redistribute OSPF routes
                    
                    .. attribute:: ospf_name  <key>
                    
                    	Process ID for the OSPF instance
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: external
                    
                    	External routes
                    	**type**\:  bool
                    
                    .. attribute:: external_type
                    
                    	External route type
                    	**type**\:  int
                    
                    	**range:** 0..2
                    
                    .. attribute:: internal
                    
                    	Internal routes
                    	**type**\:  bool
                    
                    .. attribute:: nssa_external
                    
                    	NSSA External routes
                    	**type**\:  bool
                    
                    .. attribute:: nssa_external_type
                    
                    	NSSA External route type
                    	**type**\:  int
                    
                    	**range:** 0..2
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ospf_name = None
                        self.external = None
                        self.external_type = None
                        self.internal = None
                        self.nssa_external = None
                        self.nssa_external_type = None
                        self.route_policy_name = None

                    @property
                    def _common_path(self):
                        if self.ospf_name is None:
                            raise YPYModelError('Key property ospf_name is None')

                        return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:redistribution/Cisco-IOS-XR-ip-rip-cfg:ospfs/Cisco-IOS-XR-ip-rip-cfg:ospf[Cisco-IOS-XR-ip-rip-cfg:ospf-name = ' + str(self.ospf_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ospf_name is not None:
                            return True

                        if self.external is not None:
                            return True

                        if self.external_type is not None:
                            return True

                        if self.internal is not None:
                            return True

                        if self.nssa_external is not None:
                            return True

                        if self.nssa_external_type is not None:
                            return True

                        if self.route_policy_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                        return meta._meta_table['Rip.DefaultVrf.Redistribution.Ospfs.Ospf']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:redistribution/Cisco-IOS-XR-ip-rip-cfg:ospfs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ospf is not None:
                        for child_ref in self.ospf:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                    return meta._meta_table['Rip.DefaultVrf.Redistribution.Ospfs']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:redistribution'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.bgps is not None and self.bgps._has_data():
                    return True

                if self.connected is not None and self.connected._has_data():
                    return True

                if self.eigrp_s is not None and self.eigrp_s._has_data():
                    return True

                if self.isises is not None and self.isises._has_data():
                    return True

                if self.ospfs is not None and self.ospfs._has_data():
                    return True

                if self.static is not None and self.static._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                return meta._meta_table['Rip.DefaultVrf.Redistribution']['meta_info']


        class IpDistances(object):
            """
            Table of IP specific administrative distances
            
            .. attribute:: ip_distance
            
            	IP specific administrative distance
            	**type**\: list of    :py:class:`IpDistance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.IpDistances.IpDistance>`
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ip_distance = YList()
                self.ip_distance.parent = self
                self.ip_distance.name = 'ip_distance'


            class IpDistance(object):
                """
                IP specific administrative distance
                
                .. attribute:: address  <key>
                
                	IP Source address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: netmask  <key>
                
                	IP address mask
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: distance
                
                	Administrative distance
                	**type**\:  int
                
                	**range:** 0..255
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.netmask = None
                    self.distance = None

                @property
                def _common_path(self):
                    if self.address is None:
                        raise YPYModelError('Key property address is None')
                    if self.netmask is None:
                        raise YPYModelError('Key property netmask is None')

                    return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:ip-distances/Cisco-IOS-XR-ip-rip-cfg:ip-distance[Cisco-IOS-XR-ip-rip-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-ip-rip-cfg:netmask = ' + str(self.netmask) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.address is not None:
                        return True

                    if self.netmask is not None:
                        return True

                    if self.distance is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                    return meta._meta_table['Rip.DefaultVrf.IpDistances.IpDistance']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:ip-distances'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ip_distance is not None:
                    for child_ref in self.ip_distance:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                return meta._meta_table['Rip.DefaultVrf.IpDistances']['meta_info']


        class Interfaces(object):
            """
            Table of RIP interfaces
            
            .. attribute:: interface
            
            	RIP interface name
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface>`
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
                """
                RIP interface name
                
                .. attribute:: interface_name  <key>
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: accept_metric_zero
                
                	Accept RIP updates with metric 0
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: authentication
                
                	Authentication keychain and mode
                	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface.Authentication>`
                
                	**presence node**\: True
                
                .. attribute:: broadcast_for_v2
                
                	Send RIP v2 output packets to broadcast address
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: enable
                
                	Starts RIP interface configuration
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: passive
                
                	Suppress routing updates on this interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: poison_reverse
                
                	Enable poison reverse
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: policy_in
                
                	Route Policy for inbound routing updates
                	**type**\:  str
                
                .. attribute:: policy_out
                
                	Route Policy for outbound routing updates
                	**type**\:  str
                
                .. attribute:: receive_version
                
                	RIP versions supported for receiving advertisements
                	**type**\:   :py:class:`ReceiveVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion>`
                
                .. attribute:: send_version
                
                	RIP versions supported for sending advertisements
                	**type**\:   :py:class:`SendVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface.SendVersion>`
                
                .. attribute:: site_of_origin
                
                	SOO community for prefixes learned over this interface
                	**type**\:   :py:class:`SiteOfOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin>`
                
                .. attribute:: split_horizon_disable
                
                	Disable split horizon
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.accept_metric_zero = None
                    self.authentication = None
                    self.broadcast_for_v2 = None
                    self.enable = None
                    self.passive = None
                    self.poison_reverse = None
                    self.policy_in = None
                    self.policy_out = None
                    self.receive_version = Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion()
                    self.receive_version.parent = self
                    self.send_version = Rip.DefaultVrf.Interfaces.Interface.SendVersion()
                    self.send_version.parent = self
                    self.site_of_origin = Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin()
                    self.site_of_origin.parent = self
                    self.split_horizon_disable = None


                class Authentication(object):
                    """
                    Authentication keychain and mode
                    
                    .. attribute:: keychain
                    
                    	Name of keychain
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: mode
                    
                    	Authentication mode
                    	**type**\:   :py:class:`RipAuthModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.RipAuthModeEnum>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.keychain = None
                        self.mode = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:authentication'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.keychain is not None:
                            return True

                        if self.mode is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                        return meta._meta_table['Rip.DefaultVrf.Interfaces.Interface.Authentication']['meta_info']


                class SiteOfOrigin(object):
                    """
                    SOO community for prefixes learned over this
                    interface
                    
                    .. attribute:: address
                    
                    	IPV4 address for IPV4Address\:nn format
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: address_index
                    
                    	16bit value for IPV4Address\:nn format
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: as_index
                    
                    	AS Number Index
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: as_xx
                    
                    	AS Number for AS\:nn format
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: as_yy
                    
                    	32 bit value for AS\:nn format
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: type
                    
                    	Extended community type
                    	**type**\:   :py:class:`RipExtCommunityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.RipExtCommunityEnum>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.address_index = None
                        self.as_index = None
                        self.as_xx = None
                        self.as_yy = None
                        self.type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:site-of-origin'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.address is not None:
                            return True

                        if self.address_index is not None:
                            return True

                        if self.as_index is not None:
                            return True

                        if self.as_xx is not None:
                            return True

                        if self.as_yy is not None:
                            return True

                        if self.type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                        return meta._meta_table['Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin']['meta_info']


                class ReceiveVersion(object):
                    """
                    RIP versions supported for receiving
                    advertisements
                    
                    .. attribute:: version1
                    
                    	Support RIP version 1
                    	**type**\:  bool
                    
                    .. attribute:: version2
                    
                    	Support RIP version 2
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.version1 = None
                        self.version2 = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:receive-version'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.version1 is not None:
                            return True

                        if self.version2 is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                        return meta._meta_table['Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion']['meta_info']


                class SendVersion(object):
                    """
                    RIP versions supported for sending
                    advertisements
                    
                    .. attribute:: version1
                    
                    	Support RIP version 1
                    	**type**\:  bool
                    
                    .. attribute:: version2
                    
                    	Support RIP version 2
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.version1 = None
                        self.version2 = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:send-version'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.version1 is not None:
                            return True

                        if self.version2 is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                        return meta._meta_table['Rip.DefaultVrf.Interfaces.Interface.SendVersion']['meta_info']

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:interfaces/Cisco-IOS-XR-ip-rip-cfg:interface[Cisco-IOS-XR-ip-rip-cfg:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.accept_metric_zero is not None:
                        return True

                    if self.authentication is not None and self.authentication._has_data():
                        return True

                    if self.broadcast_for_v2 is not None:
                        return True

                    if self.enable is not None:
                        return True

                    if self.passive is not None:
                        return True

                    if self.poison_reverse is not None:
                        return True

                    if self.policy_in is not None:
                        return True

                    if self.policy_out is not None:
                        return True

                    if self.receive_version is not None and self.receive_version._has_data():
                        return True

                    if self.send_version is not None and self.send_version._has_data():
                        return True

                    if self.site_of_origin is not None and self.site_of_origin._has_data():
                        return True

                    if self.split_horizon_disable is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                    return meta._meta_table['Rip.DefaultVrf.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:interfaces'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                return meta._meta_table['Rip.DefaultVrf.Interfaces']['meta_info']


        class Neighbors(object):
            """
            Configure RIP Neighbors
            
            .. attribute:: neighbor
            
            	Neighbor address
            	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.DefaultVrf.Neighbors.Neighbor>`
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.neighbor = YList()
                self.neighbor.parent = self
                self.neighbor.name = 'neighbor'


            class Neighbor(object):
                """
                Neighbor address
                
                .. attribute:: neighbor_address  <key>
                
                	IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.neighbor_address = None

                @property
                def _common_path(self):
                    if self.neighbor_address is None:
                        raise YPYModelError('Key property neighbor_address is None')

                    return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:neighbors/Cisco-IOS-XR-ip-rip-cfg:neighbor[Cisco-IOS-XR-ip-rip-cfg:neighbor-address = ' + str(self.neighbor_address) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.neighbor_address is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                    return meta._meta_table['Rip.DefaultVrf.Neighbors.Neighbor']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:neighbors'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.neighbor is not None:
                    for child_ref in self.neighbor:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                return meta._meta_table['Rip.DefaultVrf.Neighbors']['meta_info']


        class Timers(object):
            """
            Various routing timers
            
            .. attribute:: flush_timer
            
            	Flush
            	**type**\:  int
            
            	**range:** 16..250000
            
            	**default value**\: 240
            
            .. attribute:: holddown_timer
            
            	Holddown
            	**type**\:  int
            
            	**range:** 15..200000
            
            	**default value**\: 180
            
            .. attribute:: invalid_timer
            
            	Invalid
            	**type**\:  int
            
            	**range:** 15..200000
            
            	**default value**\: 180
            
            .. attribute:: update_timer
            
            	Interval between updates
            	**type**\:  int
            
            	**range:** 5..50000
            
            	**default value**\: 30
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.flush_timer = None
                self.holddown_timer = None
                self.invalid_timer = None
                self.update_timer = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf/Cisco-IOS-XR-ip-rip-cfg:timers'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.flush_timer is not None:
                    return True

                if self.holddown_timer is not None:
                    return True

                if self.invalid_timer is not None:
                    return True

                if self.update_timer is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                return meta._meta_table['Rip.DefaultVrf.Timers']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:default-vrf'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.auto_summary is not None:
                return True

            if self.broadcast_for_v2 is not None:
                return True

            if self.default_information is not None and self.default_information._has_data():
                return True

            if self.default_metric is not None:
                return True

            if self.distance is not None:
                return True

            if self.enable is not None:
                return True

            if self.interfaces is not None and self.interfaces._has_data():
                return True

            if self.ip_distances is not None and self.ip_distances._has_data():
                return True

            if self.maximum_paths is not None:
                return True

            if self.neighbors is not None and self.neighbors._has_data():
                return True

            if self.nsf is not None:
                return True

            if self.output_delay is not None:
                return True

            if self.policy_in is not None:
                return True

            if self.policy_out is not None:
                return True

            if self.redistribution is not None and self.redistribution._has_data():
                return True

            if self.timers is not None and self.timers._has_data():
                return True

            if self.validate_source_disable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
            return meta._meta_table['Rip.DefaultVrf']['meta_info']


    class Vrfs(object):
        """
        VRF related RIP configuration
        
        .. attribute:: vrf
        
        	RIP configuration for a particular VRF
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ip-rip-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
            """
            RIP configuration for a particular VRF
            
            .. attribute:: vrf_name  <key>
            
            	VRF Name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: auto_summary
            
            	Enable automatic network number summarization
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: broadcast_for_v2
            
            	Send RIP v2 output packets to broadcast address
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: default_information
            
            	Controls default information origination
            	**type**\:   :py:class:`DefaultInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.DefaultInformation>`
            
            	**presence node**\: True
            
            .. attribute:: default_metric
            
            	Default metric of redistributed routes
            	**type**\:  int
            
            	**range:** 0..16
            
            .. attribute:: distance
            
            	Administrative distance
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 120
            
            .. attribute:: enable
            
            	Starts RIP configuration for a particular VRF
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: interfaces
            
            	Table of RIP interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces>`
            
            .. attribute:: ip_distances
            
            	Table of IP specific administrative distances
            	**type**\:   :py:class:`IpDistances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.IpDistances>`
            
            .. attribute:: maximum_paths
            
            	Maximum number of paths allowed per route
            	**type**\:  int
            
            	**range:** 1..128
            
            	**default value**\: 4
            
            .. attribute:: neighbors
            
            	Configure RIP Neighbors
            	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Neighbors>`
            
            .. attribute:: nsf
            
            	Enable Cisco Non Stop Forwarding
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: output_delay
            
            	Inter\-packet delay for RIP updates
            	**type**\:  int
            
            	**range:** 8..50
            
            	**units**\: millisecond
            
            .. attribute:: policy_in
            
            	Route Policy for inbbound routing updates
            	**type**\:  str
            
            .. attribute:: policy_out
            
            	Route Policy for outbound routing updates
            	**type**\:  str
            
            .. attribute:: redistribution
            
            	Redistribute information from another routing protocol
            	**type**\:   :py:class:`Redistribution <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution>`
            
            .. attribute:: timers
            
            	Various routing timers
            	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Timers>`
            
            .. attribute:: validate_source_disable
            
            	Disable validation of source address of routing updates
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-rip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.auto_summary = None
                self.broadcast_for_v2 = None
                self.default_information = None
                self.default_metric = None
                self.distance = None
                self.enable = None
                self.interfaces = Rip.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self
                self.ip_distances = Rip.Vrfs.Vrf.IpDistances()
                self.ip_distances.parent = self
                self.maximum_paths = None
                self.neighbors = Rip.Vrfs.Vrf.Neighbors()
                self.neighbors.parent = self
                self.nsf = None
                self.output_delay = None
                self.policy_in = None
                self.policy_out = None
                self.redistribution = Rip.Vrfs.Vrf.Redistribution()
                self.redistribution.parent = self
                self.timers = Rip.Vrfs.Vrf.Timers()
                self.timers.parent = self
                self.validate_source_disable = None


            class DefaultInformation(object):
                """
                Controls default information origination
                
                .. attribute:: option
                
                	Origination option
                	**type**\:   :py:class:`DefaultInformationOptionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultInformationOptionEnum>`
                
                	**mandatory**\: True
                
                .. attribute:: route_policy_name
                
                	Route policy name
                	**type**\:  str
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.option = None
                    self.route_policy_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:default-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.option is not None:
                        return True

                    if self.route_policy_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                    return meta._meta_table['Rip.Vrfs.Vrf.DefaultInformation']['meta_info']


            class Redistribution(object):
                """
                Redistribute information from another routing
                protocol
                
                .. attribute:: bgps
                
                	Redistribute BGP routes
                	**type**\:   :py:class:`Bgps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Bgps>`
                
                .. attribute:: connected
                
                	Redistribute connected routes
                	**type**\:   :py:class:`Connected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Connected>`
                
                	**presence node**\: True
                
                .. attribute:: eigrp_s
                
                	Redistribute EIGRP routes
                	**type**\:   :py:class:`EigrpS <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.EigrpS>`
                
                .. attribute:: isises
                
                	Redistribute IS\-IS routes
                	**type**\:   :py:class:`Isises <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Isises>`
                
                .. attribute:: ospfs
                
                	Redistribute OSPF routes
                	**type**\:   :py:class:`Ospfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Ospfs>`
                
                .. attribute:: static
                
                	Redistribute static routes
                	**type**\:   :py:class:`Static <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Static>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bgps = Rip.Vrfs.Vrf.Redistribution.Bgps()
                    self.bgps.parent = self
                    self.connected = None
                    self.eigrp_s = Rip.Vrfs.Vrf.Redistribution.EigrpS()
                    self.eigrp_s.parent = self
                    self.isises = Rip.Vrfs.Vrf.Redistribution.Isises()
                    self.isises.parent = self
                    self.ospfs = Rip.Vrfs.Vrf.Redistribution.Ospfs()
                    self.ospfs.parent = self
                    self.static = None


                class Connected(object):
                    """
                    Redistribute connected routes
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    .. attribute:: route_type
                    
                    	Route type
                    	**type**\:   :py:class:`DefaultRedistRouteEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRouteEnum>`
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.route_policy_name = None
                        self.route_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:connected'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.route_policy_name is not None:
                            return True

                        if self.route_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                        return meta._meta_table['Rip.Vrfs.Vrf.Redistribution.Connected']['meta_info']


                class Bgps(object):
                    """
                    Redistribute BGP routes
                    
                    .. attribute:: bgp
                    
                    	Autonomous system number
                    	**type**\: list of    :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.bgp = YList()
                        self.bgp.parent = self
                        self.bgp.name = 'bgp'


                    class Bgp(object):
                        """
                        Autonomous system number
                        
                        .. attribute:: asnxx  <key>
                        
                        	Higher 16 bits of 4\-byte BGP AS number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: asnyy  <key>
                        
                        	2\-byte or 4\-byte BGP AS number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: policy
                        
                        	Route Policy name
                        	**type**\:  str
                        
                        .. attribute:: type
                        
                        	Route type
                        	**type**\:   :py:class:`BgpRedistRouteEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.BgpRedistRouteEnum>`
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.asnxx = None
                            self.asnyy = None
                            self.policy = None
                            self.type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.asnxx is None:
                                raise YPYModelError('Key property asnxx is None')
                            if self.asnyy is None:
                                raise YPYModelError('Key property asnyy is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:bgp[Cisco-IOS-XR-ip-rip-cfg:asnxx = ' + str(self.asnxx) + '][Cisco-IOS-XR-ip-rip-cfg:asnyy = ' + str(self.asnyy) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.asnxx is not None:
                                return True

                            if self.asnyy is not None:
                                return True

                            if self.policy is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                            return meta._meta_table['Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:bgps'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.bgp is not None:
                            for child_ref in self.bgp:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                        return meta._meta_table['Rip.Vrfs.Vrf.Redistribution.Bgps']['meta_info']


                class Isises(object):
                    """
                    Redistribute IS\-IS routes
                    
                    .. attribute:: isis
                    
                    	Redistribute IS\-IS routes
                    	**type**\: list of    :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Isises.Isis>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.isis = YList()
                        self.isis.parent = self
                        self.isis.name = 'isis'


                    class Isis(object):
                        """
                        Redistribute IS\-IS routes
                        
                        .. attribute:: isis_name  <key>
                        
                        	IS\-IS instance name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: route_policy_name
                        
                        	Route Policy name
                        	**type**\:  str
                        
                        .. attribute:: route_type
                        
                        	Route type
                        	**type**\:   :py:class:`IsisRedistRouteEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.IsisRedistRouteEnum>`
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.isis_name = None
                            self.route_policy_name = None
                            self.route_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.isis_name is None:
                                raise YPYModelError('Key property isis_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:isis[Cisco-IOS-XR-ip-rip-cfg:isis-name = ' + str(self.isis_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.isis_name is not None:
                                return True

                            if self.route_policy_name is not None:
                                return True

                            if self.route_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                            return meta._meta_table['Rip.Vrfs.Vrf.Redistribution.Isises.Isis']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:isises'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.isis is not None:
                            for child_ref in self.isis:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                        return meta._meta_table['Rip.Vrfs.Vrf.Redistribution.Isises']['meta_info']


                class EigrpS(object):
                    """
                    Redistribute EIGRP routes
                    
                    .. attribute:: eigrp
                    
                    	Redistribute EIGRP routes
                    	**type**\: list of    :py:class:`Eigrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.eigrp = YList()
                        self.eigrp.parent = self
                        self.eigrp.name = 'eigrp'


                    class Eigrp(object):
                        """
                        Redistribute EIGRP routes
                        
                        .. attribute:: as_  <key>
                        
                        	Autonomous system number
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: route_policy_name
                        
                        	Route Policy name
                        	**type**\:  str
                        
                        .. attribute:: route_type
                        
                        	Route type
                        	**type**\:   :py:class:`DefaultRedistRouteEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRouteEnum>`
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.as_ = None
                            self.route_policy_name = None
                            self.route_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.as_ is None:
                                raise YPYModelError('Key property as_ is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:eigrp[Cisco-IOS-XR-ip-rip-cfg:as = ' + str(self.as_) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.as_ is not None:
                                return True

                            if self.route_policy_name is not None:
                                return True

                            if self.route_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                            return meta._meta_table['Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:eigrp-s'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.eigrp is not None:
                            for child_ref in self.eigrp:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                        return meta._meta_table['Rip.Vrfs.Vrf.Redistribution.EigrpS']['meta_info']


                class Static(object):
                    """
                    Redistribute static routes
                    
                    .. attribute:: route_policy_name
                    
                    	Route Policy name
                    	**type**\:  str
                    
                    .. attribute:: route_type
                    
                    	Route type
                    	**type**\:   :py:class:`DefaultRedistRouteEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.DefaultRedistRouteEnum>`
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.route_policy_name = None
                        self.route_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:static'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.route_policy_name is not None:
                            return True

                        if self.route_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                        return meta._meta_table['Rip.Vrfs.Vrf.Redistribution.Static']['meta_info']


                class Ospfs(object):
                    """
                    Redistribute OSPF routes
                    
                    .. attribute:: ospf
                    
                    	Redistribute OSPF routes
                    	**type**\: list of    :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ospf = YList()
                        self.ospf.parent = self
                        self.ospf.name = 'ospf'


                    class Ospf(object):
                        """
                        Redistribute OSPF routes
                        
                        .. attribute:: ospf_name  <key>
                        
                        	Process ID for the OSPF instance
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: external
                        
                        	External routes
                        	**type**\:  bool
                        
                        .. attribute:: external_type
                        
                        	External route type
                        	**type**\:  int
                        
                        	**range:** 0..2
                        
                        .. attribute:: internal
                        
                        	Internal routes
                        	**type**\:  bool
                        
                        .. attribute:: nssa_external
                        
                        	NSSA External routes
                        	**type**\:  bool
                        
                        .. attribute:: nssa_external_type
                        
                        	NSSA External route type
                        	**type**\:  int
                        
                        	**range:** 0..2
                        
                        .. attribute:: route_policy_name
                        
                        	Route Policy name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ospf_name = None
                            self.external = None
                            self.external_type = None
                            self.internal = None
                            self.nssa_external = None
                            self.nssa_external_type = None
                            self.route_policy_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ospf_name is None:
                                raise YPYModelError('Key property ospf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:ospf[Cisco-IOS-XR-ip-rip-cfg:ospf-name = ' + str(self.ospf_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.ospf_name is not None:
                                return True

                            if self.external is not None:
                                return True

                            if self.external_type is not None:
                                return True

                            if self.internal is not None:
                                return True

                            if self.nssa_external is not None:
                                return True

                            if self.nssa_external_type is not None:
                                return True

                            if self.route_policy_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                            return meta._meta_table['Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:ospfs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ospf is not None:
                            for child_ref in self.ospf:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                        return meta._meta_table['Rip.Vrfs.Vrf.Redistribution.Ospfs']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:redistribution'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.bgps is not None and self.bgps._has_data():
                        return True

                    if self.connected is not None and self.connected._has_data():
                        return True

                    if self.eigrp_s is not None and self.eigrp_s._has_data():
                        return True

                    if self.isises is not None and self.isises._has_data():
                        return True

                    if self.ospfs is not None and self.ospfs._has_data():
                        return True

                    if self.static is not None and self.static._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                    return meta._meta_table['Rip.Vrfs.Vrf.Redistribution']['meta_info']


            class IpDistances(object):
                """
                Table of IP specific administrative distances
                
                .. attribute:: ip_distance
                
                	IP specific administrative distance
                	**type**\: list of    :py:class:`IpDistance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.IpDistances.IpDistance>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ip_distance = YList()
                    self.ip_distance.parent = self
                    self.ip_distance.name = 'ip_distance'


                class IpDistance(object):
                    """
                    IP specific administrative distance
                    
                    .. attribute:: address  <key>
                    
                    	IP Source address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: netmask  <key>
                    
                    	IP address mask
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: distance
                    
                    	Administrative distance
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.netmask = None
                        self.distance = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')
                        if self.netmask is None:
                            raise YPYModelError('Key property netmask is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:ip-distance[Cisco-IOS-XR-ip-rip-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-ip-rip-cfg:netmask = ' + str(self.netmask) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.address is not None:
                            return True

                        if self.netmask is not None:
                            return True

                        if self.distance is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                        return meta._meta_table['Rip.Vrfs.Vrf.IpDistances.IpDistance']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:ip-distances'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ip_distance is not None:
                        for child_ref in self.ip_distance:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                    return meta._meta_table['Rip.Vrfs.Vrf.IpDistances']['meta_info']


            class Interfaces(object):
                """
                Table of RIP interfaces
                
                .. attribute:: interface
                
                	RIP interface name
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    RIP interface name
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: accept_metric_zero
                    
                    	Accept RIP updates with metric 0
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: authentication
                    
                    	Authentication keychain and mode
                    	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface.Authentication>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: broadcast_for_v2
                    
                    	Send RIP v2 output packets to broadcast address
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: enable
                    
                    	Starts RIP interface configuration
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: passive
                    
                    	Suppress routing updates on this interface
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: poison_reverse
                    
                    	Enable poison reverse
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: policy_in
                    
                    	Route Policy for inbound routing updates
                    	**type**\:  str
                    
                    .. attribute:: policy_out
                    
                    	Route Policy for outbound routing updates
                    	**type**\:  str
                    
                    .. attribute:: receive_version
                    
                    	RIP versions supported for receiving advertisements
                    	**type**\:   :py:class:`ReceiveVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion>`
                    
                    .. attribute:: send_version
                    
                    	RIP versions supported for sending advertisements
                    	**type**\:   :py:class:`SendVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion>`
                    
                    .. attribute:: site_of_origin
                    
                    	SOO community for prefixes learned over this interface
                    	**type**\:   :py:class:`SiteOfOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin>`
                    
                    .. attribute:: split_horizon_disable
                    
                    	Disable split horizon
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.accept_metric_zero = None
                        self.authentication = None
                        self.broadcast_for_v2 = None
                        self.enable = None
                        self.passive = None
                        self.poison_reverse = None
                        self.policy_in = None
                        self.policy_out = None
                        self.receive_version = Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion()
                        self.receive_version.parent = self
                        self.send_version = Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion()
                        self.send_version.parent = self
                        self.site_of_origin = Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin()
                        self.site_of_origin.parent = self
                        self.split_horizon_disable = None


                    class Authentication(object):
                        """
                        Authentication keychain and mode
                        
                        .. attribute:: keychain
                        
                        	Name of keychain
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: mode
                        
                        	Authentication mode
                        	**type**\:   :py:class:`RipAuthModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.RipAuthModeEnum>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.keychain = None
                            self.mode = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:authentication'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.keychain is not None:
                                return True

                            if self.mode is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                            return meta._meta_table['Rip.Vrfs.Vrf.Interfaces.Interface.Authentication']['meta_info']


                    class SiteOfOrigin(object):
                        """
                        SOO community for prefixes learned over this
                        interface
                        
                        .. attribute:: address
                        
                        	IPV4 address for IPV4Address\:nn format
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: address_index
                        
                        	16bit value for IPV4Address\:nn format
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: as_index
                        
                        	AS Number Index
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: as_xx
                        
                        	AS Number for AS\:nn format
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: as_yy
                        
                        	32 bit value for AS\:nn format
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Extended community type
                        	**type**\:   :py:class:`RipExtCommunityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.RipExtCommunityEnum>`
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address = None
                            self.address_index = None
                            self.as_index = None
                            self.as_xx = None
                            self.as_yy = None
                            self.type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:site-of-origin'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.address is not None:
                                return True

                            if self.address_index is not None:
                                return True

                            if self.as_index is not None:
                                return True

                            if self.as_xx is not None:
                                return True

                            if self.as_yy is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                            return meta._meta_table['Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin']['meta_info']


                    class ReceiveVersion(object):
                        """
                        RIP versions supported for receiving
                        advertisements
                        
                        .. attribute:: version1
                        
                        	Support RIP version 1
                        	**type**\:  bool
                        
                        .. attribute:: version2
                        
                        	Support RIP version 2
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.version1 = None
                            self.version2 = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:receive-version'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.version1 is not None:
                                return True

                            if self.version2 is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                            return meta._meta_table['Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion']['meta_info']


                    class SendVersion(object):
                        """
                        RIP versions supported for sending
                        advertisements
                        
                        .. attribute:: version1
                        
                        	Support RIP version 1
                        	**type**\:  bool
                        
                        .. attribute:: version2
                        
                        	Support RIP version 2
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        

                        """

                        _prefix = 'ip-rip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.version1 = None
                            self.version2 = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:send-version'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.version1 is not None:
                                return True

                            if self.version2 is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                            return meta._meta_table['Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:interface[Cisco-IOS-XR-ip-rip-cfg:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.accept_metric_zero is not None:
                            return True

                        if self.authentication is not None and self.authentication._has_data():
                            return True

                        if self.broadcast_for_v2 is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.passive is not None:
                            return True

                        if self.poison_reverse is not None:
                            return True

                        if self.policy_in is not None:
                            return True

                        if self.policy_out is not None:
                            return True

                        if self.receive_version is not None and self.receive_version._has_data():
                            return True

                        if self.send_version is not None and self.send_version._has_data():
                            return True

                        if self.site_of_origin is not None and self.site_of_origin._has_data():
                            return True

                        if self.split_horizon_disable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                        return meta._meta_table['Rip.Vrfs.Vrf.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:interfaces'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                    return meta._meta_table['Rip.Vrfs.Vrf.Interfaces']['meta_info']


            class Neighbors(object):
                """
                Configure RIP Neighbors
                
                .. attribute:: neighbor
                
                	Neighbor address
                	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg.Rip.Vrfs.Vrf.Neighbors.Neighbor>`
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.neighbor = YList()
                    self.neighbor.parent = self
                    self.neighbor.name = 'neighbor'


                class Neighbor(object):
                    """
                    Neighbor address
                    
                    .. attribute:: neighbor_address  <key>
                    
                    	IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-rip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.neighbor_address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.neighbor_address is None:
                            raise YPYModelError('Key property neighbor_address is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:neighbor[Cisco-IOS-XR-ip-rip-cfg:neighbor-address = ' + str(self.neighbor_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.neighbor_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                        return meta._meta_table['Rip.Vrfs.Vrf.Neighbors.Neighbor']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:neighbors'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.neighbor is not None:
                        for child_ref in self.neighbor:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                    return meta._meta_table['Rip.Vrfs.Vrf.Neighbors']['meta_info']


            class Timers(object):
                """
                Various routing timers
                
                .. attribute:: flush_timer
                
                	Flush
                	**type**\:  int
                
                	**range:** 16..250000
                
                	**default value**\: 240
                
                .. attribute:: holddown_timer
                
                	Holddown
                	**type**\:  int
                
                	**range:** 15..200000
                
                	**default value**\: 180
                
                .. attribute:: invalid_timer
                
                	Invalid
                	**type**\:  int
                
                	**range:** 15..200000
                
                	**default value**\: 180
                
                .. attribute:: update_timer
                
                	Interval between updates
                	**type**\:  int
                
                	**range:** 5..50000
                
                	**default value**\: 30
                
                

                """

                _prefix = 'ip-rip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.flush_timer = None
                    self.holddown_timer = None
                    self.invalid_timer = None
                    self.update_timer = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-rip-cfg:timers'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.flush_timer is not None:
                        return True

                    if self.holddown_timer is not None:
                        return True

                    if self.invalid_timer is not None:
                        return True

                    if self.update_timer is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                    return meta._meta_table['Rip.Vrfs.Vrf.Timers']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:vrfs/Cisco-IOS-XR-ip-rip-cfg:vrf[Cisco-IOS-XR-ip-rip-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.auto_summary is not None:
                    return True

                if self.broadcast_for_v2 is not None:
                    return True

                if self.default_information is not None and self.default_information._has_data():
                    return True

                if self.default_metric is not None:
                    return True

                if self.distance is not None:
                    return True

                if self.enable is not None:
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.ip_distances is not None and self.ip_distances._has_data():
                    return True

                if self.maximum_paths is not None:
                    return True

                if self.neighbors is not None and self.neighbors._has_data():
                    return True

                if self.nsf is not None:
                    return True

                if self.output_delay is not None:
                    return True

                if self.policy_in is not None:
                    return True

                if self.policy_out is not None:
                    return True

                if self.redistribution is not None and self.redistribution._has_data():
                    return True

                if self.timers is not None and self.timers._has_data():
                    return True

                if self.validate_source_disable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
                return meta._meta_table['Rip.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-rip-cfg:rip/Cisco-IOS-XR-ip-rip-cfg:vrfs'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
            return meta._meta_table['Rip.Vrfs']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-rip-cfg:rip'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.default_vrf is not None and self.default_vrf._has_data():
            return True

        if self.vrfs is not None and self.vrfs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rip_cfg as meta
        return meta._meta_table['Rip']['meta_info']


