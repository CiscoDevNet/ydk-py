""" Cisco_IOS_XR_mpls_vpn_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-vpn package operational data.

This module contains definitions
for the following management objects\:
  l3vpn\: L3VPN operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class MplsVpnAfiEnum(Enum):
    """
    MplsVpnAfiEnum

    Layer 3 VPN Address Family Type

    .. data:: ipv4 = 1

    	VRF IPv4 address family

    .. data:: ipv6 = 2

    	VRF IPv6 address family

    """

    ipv4 = 1

    ipv6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_vpn_oper as meta
        return meta._meta_table['MplsVpnAfiEnum']


class MplsVpnRtEnum(Enum):
    """
    MplsVpnRtEnum

    Layer 3 VPN Route Target Type

    .. data:: import_ = 1

    	VRF Route Target Type Import

    .. data:: export = 2

    	VRF Route Target Type Export

    .. data:: both = 3

    	VRF Route Target Type Import and Export

    """

    import_ = 1

    export = 2

    both = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_vpn_oper as meta
        return meta._meta_table['MplsVpnRtEnum']


class MplsVpnSafiEnum(Enum):
    """
    MplsVpnSafiEnum

    Layer 3 VPN Sub\-Address Family Type

    .. data:: unicast = 1

    	VRF Unicast sub-address family

    .. data:: multicast = 2

    	VRF Multicast sub-address family

    .. data:: flowspec = 133

    	VRF Flowspec sub-address family

    """

    unicast = 1

    multicast = 2

    flowspec = 133


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_vpn_oper as meta
        return meta._meta_table['MplsVpnSafiEnum']



class L3Vpn(object):
    """
    L3VPN operational data
    
    .. attribute:: invalid_vrfs
    
    	Invalid VRF Table (VRFs that are forward referenced)
    	**type**\:   :py:class:`InvalidVrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.InvalidVrfs>`
    
    .. attribute:: vrfs
    
    	VRF Table
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.Vrfs>`
    
    

    """

    _prefix = 'mpls-vpn-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.invalid_vrfs = L3Vpn.InvalidVrfs()
        self.invalid_vrfs.parent = self
        self.vrfs = L3Vpn.Vrfs()
        self.vrfs.parent = self


    class InvalidVrfs(object):
        """
        Invalid VRF Table (VRFs that are forward
        referenced)
        
        .. attribute:: invalid_vrf
        
        	Invalid VRF (VRF that is forward referenced)
        	**type**\: list of    :py:class:`InvalidVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.InvalidVrfs.InvalidVrf>`
        
        

        """

        _prefix = 'mpls-vpn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.invalid_vrf = YList()
            self.invalid_vrf.parent = self
            self.invalid_vrf.name = 'invalid_vrf'


        class InvalidVrf(object):
            """
            Invalid VRF (VRF that is forward referenced)
            
            .. attribute:: vrf_name  <key>
            
            	The Name for an invalid VRF
            	**type**\:  str
            
            .. attribute:: af
            
            	AF/SAF information
            	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.InvalidVrfs.InvalidVrf.Af>`
            
            .. attribute:: interface
            
            	Interfaces in VRF
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.InvalidVrfs.InvalidVrf.Interface>`
            
            .. attribute:: is_big_vrf
            
            	VRF mode information
            	**type**\:  bool
            
            .. attribute:: route_distinguisher
            
            	Route Distinguisher
            	**type**\:  str
            
            .. attribute:: vrf_description
            
            	VRF Description
            	**type**\:  str
            
            .. attribute:: vrf_name_xr
            
            	VRF Name
            	**type**\:  str
            
            

            """

            _prefix = 'mpls-vpn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.af = YList()
                self.af.parent = self
                self.af.name = 'af'
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'
                self.is_big_vrf = None
                self.route_distinguisher = None
                self.vrf_description = None
                self.vrf_name_xr = None


            class Interface(object):
                """
                Interfaces in VRF
                
                .. attribute:: interface_name
                
                	Interface Name
                	**type**\:  str
                
                

                """

                _prefix = 'mpls-vpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-vpn-oper:interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_vpn_oper as meta
                    return meta._meta_table['L3Vpn.InvalidVrfs.InvalidVrf.Interface']['meta_info']


            class Af(object):
                """
                AF/SAF information
                
                .. attribute:: af_name
                
                	AF name
                	**type**\:   :py:class:`MplsVpnAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnAfiEnum>`
                
                .. attribute:: export_route_policy
                
                	Export Route Policy
                	**type**\:  str
                
                .. attribute:: import_route_policy
                
                	Import Route Policy
                	**type**\:  str
                
                .. attribute:: route_target
                
                	Route Targets
                	**type**\: list of    :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.InvalidVrfs.InvalidVrf.Af.RouteTarget>`
                
                .. attribute:: saf_name
                
                	SAF name
                	**type**\:   :py:class:`MplsVpnSafiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnSafiEnum>`
                
                

                """

                _prefix = 'mpls-vpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.af_name = None
                    self.export_route_policy = None
                    self.import_route_policy = None
                    self.route_target = YList()
                    self.route_target.parent = self
                    self.route_target.name = 'route_target'
                    self.saf_name = None


                class RouteTarget(object):
                    """
                    Route Targets
                    
                    .. attribute:: af_name
                    
                    	AF name
                    	**type**\:   :py:class:`MplsVpnAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnAfiEnum>`
                    
                    .. attribute:: route_target_type
                    
                    	Route Target Type
                    	**type**\:   :py:class:`MplsVpnRtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnRtEnum>`
                    
                    .. attribute:: route_target_value
                    
                    	Route Target Value
                    	**type**\:  str
                    
                    .. attribute:: saf_name
                    
                    	SAF name
                    	**type**\:   :py:class:`MplsVpnSafiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnSafiEnum>`
                    
                    

                    """

                    _prefix = 'mpls-vpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.af_name = None
                        self.route_target_type = None
                        self.route_target_value = None
                        self.saf_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-vpn-oper:route-target'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.af_name is not None:
                            return True

                        if self.route_target_type is not None:
                            return True

                        if self.route_target_value is not None:
                            return True

                        if self.saf_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_vpn_oper as meta
                        return meta._meta_table['L3Vpn.InvalidVrfs.InvalidVrf.Af.RouteTarget']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-vpn-oper:af'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.af_name is not None:
                        return True

                    if self.export_route_policy is not None:
                        return True

                    if self.import_route_policy is not None:
                        return True

                    if self.route_target is not None:
                        for child_ref in self.route_target:
                            if child_ref._has_data():
                                return True

                    if self.saf_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_vpn_oper as meta
                    return meta._meta_table['L3Vpn.InvalidVrfs.InvalidVrf.Af']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-mpls-vpn-oper:l3vpn/Cisco-IOS-XR-mpls-vpn-oper:invalid-vrfs/Cisco-IOS-XR-mpls-vpn-oper:invalid-vrf[Cisco-IOS-XR-mpls-vpn-oper:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.af is not None:
                    for child_ref in self.af:
                        if child_ref._has_data():
                            return True

                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                if self.is_big_vrf is not None:
                    return True

                if self.route_distinguisher is not None:
                    return True

                if self.vrf_description is not None:
                    return True

                if self.vrf_name_xr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_vpn_oper as meta
                return meta._meta_table['L3Vpn.InvalidVrfs.InvalidVrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-vpn-oper:l3vpn/Cisco-IOS-XR-mpls-vpn-oper:invalid-vrfs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.invalid_vrf is not None:
                for child_ref in self.invalid_vrf:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_vpn_oper as meta
            return meta._meta_table['L3Vpn.InvalidVrfs']['meta_info']


    class Vrfs(object):
        """
        VRF Table
        
        .. attribute:: vrf
        
        	VRF
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.Vrfs.Vrf>`
        
        

        """

        _prefix = 'mpls-vpn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
            """
            VRF
            
            .. attribute:: vrf_name  <key>
            
            	The Name for a VRF
            	**type**\:  str
            
            .. attribute:: af
            
            	AF/SAF information
            	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.Vrfs.Vrf.Af>`
            
            .. attribute:: interface
            
            	Interfaces in VRF
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.Vrfs.Vrf.Interface>`
            
            .. attribute:: is_big_vrf
            
            	VRF mode information
            	**type**\:  bool
            
            .. attribute:: route_distinguisher
            
            	Route Distinguisher
            	**type**\:  str
            
            .. attribute:: vrf_description
            
            	VRF Description
            	**type**\:  str
            
            .. attribute:: vrf_name_xr
            
            	VRF Name
            	**type**\:  str
            
            

            """

            _prefix = 'mpls-vpn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.af = YList()
                self.af.parent = self
                self.af.name = 'af'
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'
                self.is_big_vrf = None
                self.route_distinguisher = None
                self.vrf_description = None
                self.vrf_name_xr = None


            class Interface(object):
                """
                Interfaces in VRF
                
                .. attribute:: interface_name
                
                	Interface Name
                	**type**\:  str
                
                

                """

                _prefix = 'mpls-vpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-vpn-oper:interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_vpn_oper as meta
                    return meta._meta_table['L3Vpn.Vrfs.Vrf.Interface']['meta_info']


            class Af(object):
                """
                AF/SAF information
                
                .. attribute:: af_name
                
                	AF name
                	**type**\:   :py:class:`MplsVpnAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnAfiEnum>`
                
                .. attribute:: export_route_policy
                
                	Export Route Policy
                	**type**\:  str
                
                .. attribute:: import_route_policy
                
                	Import Route Policy
                	**type**\:  str
                
                .. attribute:: route_target
                
                	Route Targets
                	**type**\: list of    :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.Vrfs.Vrf.Af.RouteTarget>`
                
                .. attribute:: saf_name
                
                	SAF name
                	**type**\:   :py:class:`MplsVpnSafiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnSafiEnum>`
                
                

                """

                _prefix = 'mpls-vpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.af_name = None
                    self.export_route_policy = None
                    self.import_route_policy = None
                    self.route_target = YList()
                    self.route_target.parent = self
                    self.route_target.name = 'route_target'
                    self.saf_name = None


                class RouteTarget(object):
                    """
                    Route Targets
                    
                    .. attribute:: af_name
                    
                    	AF name
                    	**type**\:   :py:class:`MplsVpnAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnAfiEnum>`
                    
                    .. attribute:: route_target_type
                    
                    	Route Target Type
                    	**type**\:   :py:class:`MplsVpnRtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnRtEnum>`
                    
                    .. attribute:: route_target_value
                    
                    	Route Target Value
                    	**type**\:  str
                    
                    .. attribute:: saf_name
                    
                    	SAF name
                    	**type**\:   :py:class:`MplsVpnSafiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnSafiEnum>`
                    
                    

                    """

                    _prefix = 'mpls-vpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.af_name = None
                        self.route_target_type = None
                        self.route_target_value = None
                        self.saf_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-vpn-oper:route-target'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.af_name is not None:
                            return True

                        if self.route_target_type is not None:
                            return True

                        if self.route_target_value is not None:
                            return True

                        if self.saf_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_vpn_oper as meta
                        return meta._meta_table['L3Vpn.Vrfs.Vrf.Af.RouteTarget']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-vpn-oper:af'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.af_name is not None:
                        return True

                    if self.export_route_policy is not None:
                        return True

                    if self.import_route_policy is not None:
                        return True

                    if self.route_target is not None:
                        for child_ref in self.route_target:
                            if child_ref._has_data():
                                return True

                    if self.saf_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_vpn_oper as meta
                    return meta._meta_table['L3Vpn.Vrfs.Vrf.Af']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-mpls-vpn-oper:l3vpn/Cisco-IOS-XR-mpls-vpn-oper:vrfs/Cisco-IOS-XR-mpls-vpn-oper:vrf[Cisco-IOS-XR-mpls-vpn-oper:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.af is not None:
                    for child_ref in self.af:
                        if child_ref._has_data():
                            return True

                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                if self.is_big_vrf is not None:
                    return True

                if self.route_distinguisher is not None:
                    return True

                if self.vrf_description is not None:
                    return True

                if self.vrf_name_xr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_vpn_oper as meta
                return meta._meta_table['L3Vpn.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-vpn-oper:l3vpn/Cisco-IOS-XR-mpls-vpn-oper:vrfs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vrf is not None:
                for child_ref in self.vrf:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_vpn_oper as meta
            return meta._meta_table['L3Vpn.Vrfs']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-mpls-vpn-oper:l3vpn'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.invalid_vrfs is not None and self.invalid_vrfs._has_data():
            return True

        if self.vrfs is not None and self.vrfs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_vpn_oper as meta
        return meta._meta_table['L3Vpn']['meta_info']


