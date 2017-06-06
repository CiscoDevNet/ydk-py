""" Cisco_IOS_XR_tunnel_nve_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-nve package operational data.

This module contains definitions
for the following management objects\:
  nve\: NVE operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Nve(object):
    """
    NVE operational data
    
    .. attribute:: interfaces
    
    	Table for NVE interface attributes
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper.Nve.Interfaces>`
    
    .. attribute:: vnis
    
    	Table for VNIs
    	**type**\:   :py:class:`Vnis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper.Nve.Vnis>`
    
    

    """

    _prefix = 'tunnel-nve-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.interfaces = Nve.Interfaces()
        self.interfaces.parent = self
        self.vnis = Nve.Vnis()
        self.vnis.parent = self


    class Vnis(object):
        """
        Table for VNIs
        
        .. attribute:: vni
        
        	The attributes for a particular VNI
        	**type**\: list of    :py:class:`Vni <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper.Nve.Vnis.Vni>`
        
        

        """

        _prefix = 'tunnel-nve-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.vni = YList()
            self.vni.parent = self
            self.vni.name = 'vni'


        class Vni(object):
            """
            The attributes for a particular VNI
            
            .. attribute:: vni  <key>
            
            	VNI ID
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: bvi_ifh
            
            	BVI Interface Handle
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bvi_mac
            
            	BVI MAC address
            	**type**\:  str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: bvi_state
            
            	BVI Interface Oper State
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: flags
            
            	Flags
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_name
            
            	NVE Interface name
            	**type**\:  str
            
            .. attribute:: ipv4_tbl_id
            
            	IPv4 Table ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6_tbl_id
            
            	IPv6 Table ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mcast_flags
            
            	McastFlags
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mcast_ipv4_address
            
            	MCAST IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: state
            
            	State
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: topo_id
            
            	L2RIB Topology ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: topo_name
            
            	L2RIB Topology Name
            	**type**\:  str
            
            	**length:** 0..50
            
            .. attribute:: topo_valid
            
            	TOPO ID valid flag
            	**type**\:  bool
            
            .. attribute:: udp_port
            
            	UDP Port
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vni_max
            
            	VNI Max in Range
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vni_min
            
            	VNI Min in Range
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vni_xr
            
            	VNI Number
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_id
            
            	L3 VRF ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_name
            
            	L3 VRF Name
            	**type**\:  str
            
            .. attribute:: vrf_vni
            
            	VRF VNI
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-nve-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vni = None
                self.bvi_ifh = None
                self.bvi_mac = None
                self.bvi_state = None
                self.flags = None
                self.interface_name = None
                self.ipv4_tbl_id = None
                self.ipv6_tbl_id = None
                self.mcast_flags = None
                self.mcast_ipv4_address = None
                self.state = None
                self.topo_id = None
                self.topo_name = None
                self.topo_valid = None
                self.udp_port = None
                self.vni_max = None
                self.vni_min = None
                self.vni_xr = None
                self.vrf_id = None
                self.vrf_name = None
                self.vrf_vni = None

            @property
            def _common_path(self):
                if self.vni is None:
                    raise YPYModelError('Key property vni is None')

                return '/Cisco-IOS-XR-tunnel-nve-oper:nve/Cisco-IOS-XR-tunnel-nve-oper:vnis/Cisco-IOS-XR-tunnel-nve-oper:vni[Cisco-IOS-XR-tunnel-nve-oper:vni = ' + str(self.vni) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.vni is not None:
                    return True

                if self.bvi_ifh is not None:
                    return True

                if self.bvi_mac is not None:
                    return True

                if self.bvi_state is not None:
                    return True

                if self.flags is not None:
                    return True

                if self.interface_name is not None:
                    return True

                if self.ipv4_tbl_id is not None:
                    return True

                if self.ipv6_tbl_id is not None:
                    return True

                if self.mcast_flags is not None:
                    return True

                if self.mcast_ipv4_address is not None:
                    return True

                if self.state is not None:
                    return True

                if self.topo_id is not None:
                    return True

                if self.topo_name is not None:
                    return True

                if self.topo_valid is not None:
                    return True

                if self.udp_port is not None:
                    return True

                if self.vni_max is not None:
                    return True

                if self.vni_min is not None:
                    return True

                if self.vni_xr is not None:
                    return True

                if self.vrf_id is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                if self.vrf_vni is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_nve_oper as meta
                return meta._meta_table['Nve.Vnis.Vni']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-nve-oper:nve/Cisco-IOS-XR-tunnel-nve-oper:vnis'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vni is not None:
                for child_ref in self.vni:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_nve_oper as meta
            return meta._meta_table['Nve.Vnis']['meta_info']


    class Interfaces(object):
        """
        Table for NVE interface attributes
        
        .. attribute:: interface
        
        	The attributes for a particular interface
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper.Nve.Interfaces.Interface>`
        
        

        """

        _prefix = 'tunnel-nve-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            The attributes for a particular interface
            
            .. attribute:: interface_name  <key>
            
            	Interface Name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: admin_state
            
            	Admin State
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: any_cast_source_interface_name
            
            	Anycast Source Interface name
            	**type**\:  str
            
            .. attribute:: any_cast_source_ipv4_address
            
            	Anycast Source IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: any_cast_source_state
            
            	Anycast Source Interface State
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: encap
            
            	Encap
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: flags
            
            	Flags
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: if_handle
            
            	NVE IfHandle
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: interface_name_xr
            
            	Interface name
            	**type**\:  str
            
            .. attribute:: source_interface_name
            
            	Source Interface name
            	**type**\:  str
            
            .. attribute:: source_ipv4_address
            
            	Source IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: source_state
            
            	Source Intf State
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: state
            
            	State
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: sync_mcast_flags
            
            	Sync McastFlags
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sync_mcast_ipv4_address
            
            	MCAST sync group IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: udp_port
            
            	UDP Port
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-nve-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.admin_state = None
                self.any_cast_source_interface_name = None
                self.any_cast_source_ipv4_address = None
                self.any_cast_source_state = None
                self.encap = None
                self.flags = None
                self.if_handle = None
                self.interface_name_xr = None
                self.source_interface_name = None
                self.source_ipv4_address = None
                self.source_state = None
                self.state = None
                self.sync_mcast_flags = None
                self.sync_mcast_ipv4_address = None
                self.udp_port = None

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-tunnel-nve-oper:nve/Cisco-IOS-XR-tunnel-nve-oper:interfaces/Cisco-IOS-XR-tunnel-nve-oper:interface[Cisco-IOS-XR-tunnel-nve-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.admin_state is not None:
                    return True

                if self.any_cast_source_interface_name is not None:
                    return True

                if self.any_cast_source_ipv4_address is not None:
                    return True

                if self.any_cast_source_state is not None:
                    return True

                if self.encap is not None:
                    return True

                if self.flags is not None:
                    return True

                if self.if_handle is not None:
                    return True

                if self.interface_name_xr is not None:
                    return True

                if self.source_interface_name is not None:
                    return True

                if self.source_ipv4_address is not None:
                    return True

                if self.source_state is not None:
                    return True

                if self.state is not None:
                    return True

                if self.sync_mcast_flags is not None:
                    return True

                if self.sync_mcast_ipv4_address is not None:
                    return True

                if self.udp_port is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_nve_oper as meta
                return meta._meta_table['Nve.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-nve-oper:nve/Cisco-IOS-XR-tunnel-nve-oper:interfaces'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_nve_oper as meta
            return meta._meta_table['Nve.Interfaces']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-tunnel-nve-oper:nve'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.vnis is not None and self.vnis._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_nve_oper as meta
        return meta._meta_table['Nve']['meta_info']


