""" Cisco_IOS_XR_lib_mpp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-mpp package operational data.

This module contains definitions
for the following management objects\:
  management\-plane\-protection\: Management Plane Protection (MPP)
    operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class MppAllowEnum(Enum):
    """
    MppAllowEnum

    MPP protocol types

    .. data:: ssh = 0

    	SSH protocol

    .. data:: telnet = 1

    	TELNET protocol

    .. data:: snmp = 2

    	SNMP protocol

    .. data:: tftp = 3

    	TFTP protocol

    .. data:: http = 4

    	HTTP protocol

    .. data:: xr_xml = 5

    	XML

    .. data:: netconf = 6

    	NETCONF protocol

    .. data:: all = 7

    	All

    """

    ssh = 0

    telnet = 1

    snmp = 2

    tftp = 3

    http = 4

    xr_xml = 5

    netconf = 6

    all = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_mpp_oper as meta
        return meta._meta_table['MppAllowEnum']



class MppAfIdBaseIdentity(object):
    """
    Base identity for Mpp\-af\-id
    
    

    """

    _prefix = 'Cisco-IOS-XR-lib-mpp-oper'
    _revision = '2015-01-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_mpp_oper as meta
        return meta._meta_table['MppAfIdBaseIdentity']['meta_info']


class ManagementPlaneProtection(object):
    """
    Management Plane Protection (MPP) operational
    data
    
    .. attribute:: inband
    
    	Management Plane Protection (MPP) inband interface data
    	**type**\:   :py:class:`Inband <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband>`
    
    .. attribute:: outband
    
    	Management Plane Protection (MPP) outband interface data
    	**type**\:   :py:class:`Outband <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband>`
    
    

    """

    _prefix = 'lib-mpp-oper'
    _revision = '2015-01-07'

    def __init__(self):
        self.inband = ManagementPlaneProtection.Inband()
        self.inband.parent = self
        self.outband = ManagementPlaneProtection.Outband()
        self.outband.parent = self


    class Outband(object):
        """
        Management Plane Protection (MPP) outband
        interface data
        
        .. attribute:: interfaces
        
        	List of inband/outband interfaces
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Interfaces>`
        
        .. attribute:: vrf
        
        	Outband VRF information
        	**type**\:   :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Vrf>`
        
        

        """

        _prefix = 'lib-mpp-oper'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.interfaces = ManagementPlaneProtection.Outband.Interfaces()
            self.interfaces.parent = self
            self.vrf = ManagementPlaneProtection.Outband.Vrf()
            self.vrf.parent = self


        class Vrf(object):
            """
            Outband VRF information
            
            .. attribute:: vrf_name
            
            	Outband VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'lib-mpp-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.vrf_name = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/Cisco-IOS-XR-lib-mpp-oper:outband/Cisco-IOS-XR-lib-mpp-oper:vrf'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_mpp_oper as meta
                return meta._meta_table['ManagementPlaneProtection.Outband.Vrf']['meta_info']


        class Interfaces(object):
            """
            List of inband/outband interfaces
            
            .. attribute:: interface
            
            	MPP interface information
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Interfaces.Interface>`
            
            

            """

            _prefix = 'lib-mpp-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
                """
                MPP interface information
                
                .. attribute:: interface_name  <key>
                
                	Interface name, specify 'all' for all interfaces
                	**type**\:  str
                
                .. attribute:: protocol
                
                	MPP Interface protocols
                	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol>`
                
                

                """

                _prefix = 'lib-mpp-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.protocol = YList()
                    self.protocol.parent = self
                    self.protocol.name = 'protocol'


                class Protocol(object):
                    """
                    MPP Interface protocols
                    
                    .. attribute:: allow
                    
                    	MPP allow
                    	**type**\:   :py:class:`MppAllowEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.MppAllowEnum>`
                    
                    .. attribute:: is_all_peers_allowed
                    
                    	If TRUE, all peers are allowed
                    	**type**\:  bool
                    
                    .. attribute:: peer_address
                    
                    	List of peer addresses
                    	**type**\: list of    :py:class:`PeerAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress>`
                    
                    

                    """

                    _prefix = 'lib-mpp-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.allow = None
                        self.is_all_peers_allowed = None
                        self.peer_address = YList()
                        self.peer_address.parent = self
                        self.peer_address.name = 'peer_address'


                    class PeerAddress(object):
                        """
                        List of peer addresses
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`MppAfIdBaseIdentity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.MppAfIdBaseIdentity>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'lib-mpp-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            self.parent = None
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-lib-mpp-oper:peer-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.ipv4_address is not None:
                                return True

                            if self.ipv6_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_mpp_oper as meta
                            return meta._meta_table['ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-lib-mpp-oper:protocol'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.allow is not None:
                            return True

                        if self.is_all_peers_allowed is not None:
                            return True

                        if self.peer_address is not None:
                            for child_ref in self.peer_address:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_mpp_oper as meta
                        return meta._meta_table['ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol']['meta_info']

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/Cisco-IOS-XR-lib-mpp-oper:outband/Cisco-IOS-XR-lib-mpp-oper:interfaces/Cisco-IOS-XR-lib-mpp-oper:interface[Cisco-IOS-XR-lib-mpp-oper:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.protocol is not None:
                        for child_ref in self.protocol:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_mpp_oper as meta
                    return meta._meta_table['ManagementPlaneProtection.Outband.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/Cisco-IOS-XR-lib-mpp-oper:outband/Cisco-IOS-XR-lib-mpp-oper:interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_mpp_oper as meta
                return meta._meta_table['ManagementPlaneProtection.Outband.Interfaces']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/Cisco-IOS-XR-lib-mpp-oper:outband'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interfaces is not None and self.interfaces._has_data():
                return True

            if self.vrf is not None and self.vrf._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_mpp_oper as meta
            return meta._meta_table['ManagementPlaneProtection.Outband']['meta_info']


    class Inband(object):
        """
        Management Plane Protection (MPP) inband
        interface data
        
        .. attribute:: interfaces
        
        	List of inband/outband interfaces
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband.Interfaces>`
        
        

        """

        _prefix = 'lib-mpp-oper'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.interfaces = ManagementPlaneProtection.Inband.Interfaces()
            self.interfaces.parent = self


        class Interfaces(object):
            """
            List of inband/outband interfaces
            
            .. attribute:: interface
            
            	MPP interface information
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband.Interfaces.Interface>`
            
            

            """

            _prefix = 'lib-mpp-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
                """
                MPP interface information
                
                .. attribute:: interface_name  <key>
                
                	Interface name, specify 'all' for all interfaces
                	**type**\:  str
                
                .. attribute:: protocol
                
                	MPP Interface protocols
                	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol>`
                
                

                """

                _prefix = 'lib-mpp-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.protocol = YList()
                    self.protocol.parent = self
                    self.protocol.name = 'protocol'


                class Protocol(object):
                    """
                    MPP Interface protocols
                    
                    .. attribute:: allow
                    
                    	MPP allow
                    	**type**\:   :py:class:`MppAllowEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.MppAllowEnum>`
                    
                    .. attribute:: is_all_peers_allowed
                    
                    	If TRUE, all peers are allowed
                    	**type**\:  bool
                    
                    .. attribute:: peer_address
                    
                    	List of peer addresses
                    	**type**\: list of    :py:class:`PeerAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress>`
                    
                    

                    """

                    _prefix = 'lib-mpp-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.allow = None
                        self.is_all_peers_allowed = None
                        self.peer_address = YList()
                        self.peer_address.parent = self
                        self.peer_address.name = 'peer_address'


                    class PeerAddress(object):
                        """
                        List of peer addresses
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`MppAfIdBaseIdentity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.MppAfIdBaseIdentity>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'lib-mpp-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            self.parent = None
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-lib-mpp-oper:peer-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.ipv4_address is not None:
                                return True

                            if self.ipv6_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_mpp_oper as meta
                            return meta._meta_table['ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-lib-mpp-oper:protocol'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.allow is not None:
                            return True

                        if self.is_all_peers_allowed is not None:
                            return True

                        if self.peer_address is not None:
                            for child_ref in self.peer_address:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_mpp_oper as meta
                        return meta._meta_table['ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol']['meta_info']

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/Cisco-IOS-XR-lib-mpp-oper:inband/Cisco-IOS-XR-lib-mpp-oper:interfaces/Cisco-IOS-XR-lib-mpp-oper:interface[Cisco-IOS-XR-lib-mpp-oper:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.protocol is not None:
                        for child_ref in self.protocol:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_mpp_oper as meta
                    return meta._meta_table['ManagementPlaneProtection.Inband.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/Cisco-IOS-XR-lib-mpp-oper:inband/Cisco-IOS-XR-lib-mpp-oper:interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_mpp_oper as meta
                return meta._meta_table['ManagementPlaneProtection.Inband.Interfaces']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/Cisco-IOS-XR-lib-mpp-oper:inband'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interfaces is not None and self.interfaces._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_mpp_oper as meta
            return meta._meta_table['ManagementPlaneProtection.Inband']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-lib-mpp-oper:management-plane-protection'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.inband is not None and self.inband._has_data():
            return True

        if self.outband is not None and self.outband._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_mpp_oper as meta
        return meta._meta_table['ManagementPlaneProtection']['meta_info']


class Ipv4Identity(MppAfIdBaseIdentity):
    """
    IPv4 address family
    
    

    """

    _prefix = 'Cisco-IOS-XR-lib-mpp-oper'
    _revision = '2015-01-07'

    def __init__(self):
        MppAfIdBaseIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_mpp_oper as meta
        return meta._meta_table['Ipv4Identity']['meta_info']


class Ipv6Identity(MppAfIdBaseIdentity):
    """
    IPv6 address family
    
    

    """

    _prefix = 'Cisco-IOS-XR-lib-mpp-oper'
    _revision = '2015-01-07'

    def __init__(self):
        MppAfIdBaseIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_mpp_oper as meta
        return meta._meta_table['Ipv6Identity']['meta_info']


