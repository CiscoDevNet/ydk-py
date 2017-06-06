""" Cisco_IOS_XR_ipv4_arp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-arp package operational data.

This module contains definitions
for the following management objects\:
  arp\-gmp\: ARP\-GMP global operational data
  arp\: arp

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class ArpGmpBagEncapEnum(Enum):
    """
    ArpGmpBagEncapEnum

    ARP encapsulation

    .. data:: none = 0

    	No encapsulation

    .. data:: arpa = 1

    	ARPA

    .. data:: snap = 2

    	SNAP

    .. data:: ieee802_1q = 3

    	802 1Q

    .. data:: srp = 4

    	SRP

    .. data:: srpa = 5

    	SRPA

    .. data:: srpb = 6

    	SRPB

    """

    none = 0

    arpa = 1

    snap = 2

    ieee802_1q = 3

    srp = 4

    srpa = 5

    srpb = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['ArpGmpBagEncapEnum']


class ArpGmpBagEntryEnum(Enum):
    """
    ArpGmpBagEntryEnum

    ARP Entry type

    .. data:: null = 0

    	No state

    .. data:: static = 1

    	Static

    .. data:: alias = 2

    	Alias

    """

    null = 0

    static = 1

    alias = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['ArpGmpBagEntryEnum']


class ArpResolutionHistoryStatusEnum(Enum):
    """
    ArpResolutionHistoryStatusEnum

    Arp resolution history status

    .. data:: status_none = 0

    	No Status

    .. data:: status_resolution_request = 1

    	Resolution Request Received

    .. data:: status_resolved_reply = 2

    	Resolved with ARP reply

    .. data:: status_resolved_grat_arp = 3

    	Resolved with Grat ARP

    .. data:: status_resolved_request = 4

    	Resolved with ARP Request

    .. data:: status_resolved_lc_sync = 5

    	Resolved via a Linecard sync

    .. data:: status_resolved_lc_sync_purge_delay = 6

    	Resolved via a Linecard sync while purge

    	delayed

    .. data:: status_resolved_client = 7

    	Resolved from an ARP API client

    .. data:: status_removed_client = 8

    	Removed by an ARP API client

    .. data:: status_already_resolved = 9

    	Already Resolved

    .. data:: status_failed = 10

    	Resolution Failed

    .. data:: status_dropped_interface_down = 11

    	Dropped because the Interface was down

    .. data:: status_dropped_broadcast_disabled = 12

    	Dropped because the Interface was broadcast

    	disabled

    .. data:: status_dropped_interface_unavailable = 13

    	Dropped because the Interface was unavailable

    	to arp

    .. data:: status_dropped_bad_subnet = 14

    	The requested IP address didn't belong to the

    	subnet

    .. data:: status_dropped_dynamic_learning_disabled = 15

    	Dynamic learning of ARP entries is disabled on

    	the interface

    .. data:: status_dropped_out_of_subnet_disabled = 16

    	Out of Subnet address learning is disabled on

    	the interface

    .. data:: status_removed_client_sweep = 17

    	Removed by an ARP API client during a resync

    .. data:: status_added_client = 18

    	Added by an ARP API client

    .. data:: status_added_v1 = 19

    	Added by replication from ARP V1 during ISSU

    .. data:: status_removed_v1 = 20

    	Removed by replication from ARP V1 during ISSU

    .. data:: status_resolved_peer_sync = 21

    	Resolved via a Peer Router sync

    """

    status_none = 0

    status_resolution_request = 1

    status_resolved_reply = 2

    status_resolved_grat_arp = 3

    status_resolved_request = 4

    status_resolved_lc_sync = 5

    status_resolved_lc_sync_purge_delay = 6

    status_resolved_client = 7

    status_removed_client = 8

    status_already_resolved = 9

    status_failed = 10

    status_dropped_interface_down = 11

    status_dropped_broadcast_disabled = 12

    status_dropped_interface_unavailable = 13

    status_dropped_bad_subnet = 14

    status_dropped_dynamic_learning_disabled = 15

    status_dropped_out_of_subnet_disabled = 16

    status_removed_client_sweep = 17

    status_added_client = 18

    status_added_v1 = 19

    status_removed_v1 = 20

    status_resolved_peer_sync = 21


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['ArpResolutionHistoryStatusEnum']


class IpArpBagEncapEnum(Enum):
    """
    IpArpBagEncapEnum

    ARP encapsulation

    .. data:: none = 0

    	No encapsulation

    .. data:: arpa = 1

    	ARPA

    .. data:: snap = 2

    	SNAP

    .. data:: ieee802_1q = 3

    	802 1Q

    .. data:: srp = 4

    	SRP

    .. data:: srpa = 5

    	SRPA

    .. data:: srpb = 6

    	SRPB

    """

    none = 0

    arpa = 1

    snap = 2

    ieee802_1q = 3

    srp = 4

    srpa = 5

    srpb = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['IpArpBagEncapEnum']


class IpArpBagFlagsEnum(Enum):
    """
    IpArpBagFlagsEnum

    ARP flags

    .. data:: flag_none = 0

    	No Flag

    .. data:: flag_dynamic = 1

    	Dynamic learnt entry

    .. data:: flag_evpn_sync = 2

    	EVPN Synced entry

    .. data:: flag_max = 3

    	Maximum Flag number

    """

    flag_none = 0

    flag_dynamic = 1

    flag_evpn_sync = 2

    flag_max = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['IpArpBagFlagsEnum']


class IpArpBagMediaEnum(Enum):
    """
    IpArpBagMediaEnum

    ARP media type

    .. data:: media_arpa = 0

    	ARPA

    .. data:: media_srp = 1

    	SRP

    .. data:: media_unknown = 2

    	Unknown

    """

    media_arpa = 0

    media_srp = 1

    media_unknown = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['IpArpBagMediaEnum']


class IpArpBagStateEnum(Enum):
    """
    IpArpBagStateEnum

    ARP state

    .. data:: state_none = 0

    	No state

    .. data:: state_interface = 1

    	Interface

    .. data:: state_standby = 2

    	Standby

    .. data:: state_static = 3

    	Static

    .. data:: state_alias = 4

    	Alias

    .. data:: state_mobile = 5

    	Mobile

    .. data:: state_incomplete = 6

    	Incomplete

    .. data:: state_deleted = 7

    	Deleted

    .. data:: state_dynamic = 8

    	Dynamic

    .. data:: state_probe = 9

    	Probe

    .. data:: state_purge_delayed = 10

    	Purge delayed

    .. data:: state_dhcp = 11

    	DHCP installed

    .. data:: state_vxlan = 12

    	VXLAN installed

    .. data:: state_evpn_sync = 13

    	EVPN-SYNC installed

    .. data:: state_sat = 14

    	Satellite installed

    .. data:: state_r_sync = 15

    	Geo-redundancy sync'ed

    .. data:: state_max = 16

    	Maximum state number

    """

    state_none = 0

    state_interface = 1

    state_standby = 2

    state_static = 3

    state_alias = 4

    state_mobile = 5

    state_incomplete = 6

    state_deleted = 7

    state_dynamic = 8

    state_probe = 9

    state_purge_delayed = 10

    state_dhcp = 11

    state_vxlan = 12

    state_evpn_sync = 13

    state_sat = 14

    state_r_sync = 15

    state_max = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['IpArpBagStateEnum']



class ArpGmp(object):
    """
    ARP\-GMP global operational data
    
    .. attribute:: vrf_infos
    
    	Table of VRF related ARP\-GMP operational data
    	**type**\:   :py:class:`VrfInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.VrfInfos>`
    
    .. attribute:: vrfs
    
    	Table of per VRF ARP\-GMP operational data
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs>`
    
    

    """

    _prefix = 'ipv4-arp-oper'
    _revision = '2016-12-19'

    def __init__(self):
        self.vrf_infos = ArpGmp.VrfInfos()
        self.vrf_infos.parent = self
        self.vrfs = ArpGmp.Vrfs()
        self.vrfs.parent = self


    class VrfInfos(object):
        """
        Table of VRF related ARP\-GMP operational data
        
        .. attribute:: vrf_info
        
        	VRF related ARP\-GMP operational data
        	**type**\: list of    :py:class:`VrfInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.VrfInfos.VrfInfo>`
        
        

        """

        _prefix = 'ipv4-arp-oper'
        _revision = '2016-12-19'

        def __init__(self):
            self.parent = None
            self.vrf_info = YList()
            self.vrf_info.parent = self
            self.vrf_info.name = 'vrf_info'


        class VrfInfo(object):
            """
            VRF related ARP\-GMP operational data
            
            .. attribute:: vrf_name  <key>
            
            	VRF name for the default VRF use 'default'
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: rsi_handle
            
            	RSI registration handle
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsi_handle_high
            
            	RSI registration handle (top 32\-bits)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: table_id
            
            	IPv4 unicast table ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_id_number
            
            	VRF ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_name_xr
            
            	VRF Name
            	**type**\:  str
            
            

            """

            _prefix = 'ipv4-arp-oper'
            _revision = '2016-12-19'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.rsi_handle = None
                self.rsi_handle_high = None
                self.table_id = None
                self.vrf_id_number = None
                self.vrf_name_xr = None

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ipv4-arp-oper:arp-gmp/Cisco-IOS-XR-ipv4-arp-oper:vrf-infos/Cisco-IOS-XR-ipv4-arp-oper:vrf-info[Cisco-IOS-XR-ipv4-arp-oper:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.rsi_handle is not None:
                    return True

                if self.rsi_handle_high is not None:
                    return True

                if self.table_id is not None:
                    return True

                if self.vrf_id_number is not None:
                    return True

                if self.vrf_name_xr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                return meta._meta_table['ArpGmp.VrfInfos.VrfInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-arp-oper:arp-gmp/Cisco-IOS-XR-ipv4-arp-oper:vrf-infos'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vrf_info is not None:
                for child_ref in self.vrf_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
            return meta._meta_table['ArpGmp.VrfInfos']['meta_info']


    class Vrfs(object):
        """
        Table of per VRF ARP\-GMP operational data
        
        .. attribute:: vrf
        
        	Per VRF ARP\-GMP operational data
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-arp-oper'
        _revision = '2016-12-19'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
            """
            Per VRF ARP\-GMP operational data
            
            .. attribute:: vrf_name  <key>
            
            	VRF name for the default VRF use 'default'
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: configured_ip_addresses
            
            	Table of ARP\-GMP configured IP addresses information
            	**type**\:   :py:class:`ConfiguredIpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses>`
            
            .. attribute:: interface_configured_ips
            
            	Table of ARP GMP interface and associated configured IP data
            	**type**\:   :py:class:`InterfaceConfiguredIps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps>`
            
            .. attribute:: routes
            
            	Table of ARP GMP route information
            	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf.Routes>`
            
            

            """

            _prefix = 'ipv4-arp-oper'
            _revision = '2016-12-19'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.configured_ip_addresses = ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses()
                self.configured_ip_addresses.parent = self
                self.interface_configured_ips = ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps()
                self.interface_configured_ips.parent = self
                self.routes = ArpGmp.Vrfs.Vrf.Routes()
                self.routes.parent = self


            class ConfiguredIpAddresses(object):
                """
                Table of ARP\-GMP configured IP addresses
                information
                
                .. attribute:: configured_ip_address
                
                	ARP\-GMP configured IP address information
                	**type**\: list of    :py:class:`ConfiguredIpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses.ConfiguredIpAddress>`
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.configured_ip_address = YList()
                    self.configured_ip_address.parent = self
                    self.configured_ip_address.name = 'configured_ip_address'


                class ConfiguredIpAddress(object):
                    """
                    ARP\-GMP configured IP address information
                    
                    .. attribute:: address  <key>
                    
                    	Configured ARP\-GMP IP
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: encapsulation_type
                    
                    	Encap type
                    	**type**\:   :py:class:`ArpGmpBagEncapEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmpBagEncapEnum>`
                    
                    .. attribute:: entry_type
                    
                    	Entry type static/alias
                    	**type**\:   :py:class:`ArpGmpBagEntryEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmpBagEntryEnum>`
                    
                    .. attribute:: hardware_address
                    
                    	Hardware address 
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: ip_address
                    
                    	IP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2016-12-19'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.encapsulation_type = None
                        self.entry_type = None
                        self.hardware_address = None
                        self.ip_address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:configured-ip-address[Cisco-IOS-XR-ipv4-arp-oper:address = ' + str(self.address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.address is not None:
                            return True

                        if self.encapsulation_type is not None:
                            return True

                        if self.entry_type is not None:
                            return True

                        if self.hardware_address is not None:
                            return True

                        if self.ip_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                        return meta._meta_table['ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses.ConfiguredIpAddress']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:configured-ip-addresses'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.configured_ip_address is not None:
                        for child_ref in self.configured_ip_address:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses']['meta_info']


            class Routes(object):
                """
                Table of ARP GMP route information
                
                .. attribute:: route
                
                	ARP GMP route information
                	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf.Routes.Route>`
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.route = YList()
                    self.route.parent = self
                    self.route.name = 'route'


                class Route(object):
                    """
                    ARP GMP route information
                    
                    .. attribute:: address
                    
                    	IP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: interface_name
                    
                    	Interface names
                    	**type**\:  list of str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface name (first element of InterfaceNames array)
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: ip_address
                    
                    	IP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length
                    	**type**\:  int
                    
                    	**range:** 0..32
                    
                    .. attribute:: prefix_length_xr
                    
                    	IP address length
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2016-12-19'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.interface_name = YLeafList()
                        self.interface_name.parent = self
                        self.interface_name.name = 'interface_name'
                        self.interface_name_xr = None
                        self.ip_address = None
                        self.prefix_length = None
                        self.prefix_length_xr = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:route'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.address is not None:
                            return True

                        if self.interface_name is not None:
                            for child in self.interface_name:
                                if child is not None:
                                    return True

                        if self.interface_name_xr is not None:
                            return True

                        if self.ip_address is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.prefix_length_xr is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                        return meta._meta_table['ArpGmp.Vrfs.Vrf.Routes.Route']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:routes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.route is not None:
                        for child_ref in self.route:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['ArpGmp.Vrfs.Vrf.Routes']['meta_info']


            class InterfaceConfiguredIps(object):
                """
                Table of ARP GMP interface and associated
                configured IP data
                
                .. attribute:: interface_configured_ip
                
                	ARP GMP interface and associated configured IP data
                	**type**\: list of    :py:class:`InterfaceConfiguredIp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp>`
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.interface_configured_ip = YList()
                    self.interface_configured_ip.parent = self
                    self.interface_configured_ip.name = 'interface_configured_ip'


                class InterfaceConfiguredIp(object):
                    """
                    ARP GMP interface and associated configured
                    IP data
                    
                    .. attribute:: address
                    
                    	Configured ARP\-GMP IP
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: associated_configuration_entry
                    
                    	Associated configuration entry
                    	**type**\:   :py:class:`AssociatedConfigurationEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry>`
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: reference_count
                    
                    	Route reference count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2016-12-19'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.associated_configuration_entry = ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry()
                        self.associated_configuration_entry.parent = self
                        self.interface_name = None
                        self.interface_name_xr = None
                        self.reference_count = None


                    class AssociatedConfigurationEntry(object):
                        """
                        Associated configuration entry
                        
                        .. attribute:: encapsulation_type
                        
                        	Encap type
                        	**type**\:   :py:class:`ArpGmpBagEncapEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmpBagEncapEnum>`
                        
                        .. attribute:: entry_type
                        
                        	Entry type static/alias
                        	**type**\:   :py:class:`ArpGmpBagEntryEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmpBagEntryEnum>`
                        
                        .. attribute:: hardware_address
                        
                        	Hardware address 
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: ip_address
                        
                        	IP address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv4-arp-oper'
                        _revision = '2016-12-19'

                        def __init__(self):
                            self.parent = None
                            self.encapsulation_type = None
                            self.entry_type = None
                            self.hardware_address = None
                            self.ip_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:associated-configuration-entry'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.encapsulation_type is not None:
                                return True

                            if self.entry_type is not None:
                                return True

                            if self.hardware_address is not None:
                                return True

                            if self.ip_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                            return meta._meta_table['ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:interface-configured-ip'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.address is not None:
                            return True

                        if self.associated_configuration_entry is not None and self.associated_configuration_entry._has_data():
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.interface_name_xr is not None:
                            return True

                        if self.reference_count is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                        return meta._meta_table['ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:interface-configured-ips'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_configured_ip is not None:
                        for child_ref in self.interface_configured_ip:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ipv4-arp-oper:arp-gmp/Cisco-IOS-XR-ipv4-arp-oper:vrfs/Cisco-IOS-XR-ipv4-arp-oper:vrf[Cisco-IOS-XR-ipv4-arp-oper:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.configured_ip_addresses is not None and self.configured_ip_addresses._has_data():
                    return True

                if self.interface_configured_ips is not None and self.interface_configured_ips._has_data():
                    return True

                if self.routes is not None and self.routes._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                return meta._meta_table['ArpGmp.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-arp-oper:arp-gmp/Cisco-IOS-XR-ipv4-arp-oper:vrfs'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
            return meta._meta_table['ArpGmp.Vrfs']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-arp-oper:arp-gmp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.vrf_infos is not None and self.vrf_infos._has_data():
            return True

        if self.vrfs is not None and self.vrfs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['ArpGmp']['meta_info']


class Arp(object):
    """
    arp
    
    .. attribute:: nodes
    
    	Table of per\-node ARP operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes>`
    
    

    """

    _prefix = 'ipv4-arp-oper'
    _revision = '2016-12-19'

    def __init__(self):
        self.nodes = Arp.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Table of per\-node ARP operational data
        
        .. attribute:: node
        
        	Per\-node ARP operational data
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node>`
        
        

        """

        _prefix = 'ipv4-arp-oper'
        _revision = '2016-12-19'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Per\-node ARP operational data
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: entries
            
            	Table of ARP entries
            	**type**\:   :py:class:`Entries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.Entries>`
            
            .. attribute:: resolution_history_client
            
            	Per node client\-installed ARP resolution history data
            	**type**\:   :py:class:`ResolutionHistoryClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.ResolutionHistoryClient>`
            
            .. attribute:: resolution_history_dynamic
            
            	Per node dynamically\-resolved ARP resolution history data
            	**type**\:   :py:class:`ResolutionHistoryDynamic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.ResolutionHistoryDynamic>`
            
            .. attribute:: traffic_interfaces
            
            	ARP Traffic information per interface
            	**type**\:   :py:class:`TrafficInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.TrafficInterfaces>`
            
            .. attribute:: traffic_node
            
            	Per node ARP Traffic data
            	**type**\:   :py:class:`TrafficNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.TrafficNode>`
            
            .. attribute:: traffic_vrfs
            
            	ARP Traffic information per VRF
            	**type**\:   :py:class:`TrafficVrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.TrafficVrfs>`
            
            

            """

            _prefix = 'ipv4-arp-oper'
            _revision = '2016-12-19'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.entries = Arp.Nodes.Node.Entries()
                self.entries.parent = self
                self.resolution_history_client = Arp.Nodes.Node.ResolutionHistoryClient()
                self.resolution_history_client.parent = self
                self.resolution_history_dynamic = Arp.Nodes.Node.ResolutionHistoryDynamic()
                self.resolution_history_dynamic.parent = self
                self.traffic_interfaces = Arp.Nodes.Node.TrafficInterfaces()
                self.traffic_interfaces.parent = self
                self.traffic_node = Arp.Nodes.Node.TrafficNode()
                self.traffic_node.parent = self
                self.traffic_vrfs = Arp.Nodes.Node.TrafficVrfs()
                self.traffic_vrfs.parent = self


            class ResolutionHistoryDynamic(object):
                """
                Per node dynamically\-resolved ARP resolution
                history data
                
                .. attribute:: arp_entry
                
                	Resolution history array
                	**type**\: list of    :py:class:`ArpEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.ResolutionHistoryDynamic.ArpEntry>`
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.arp_entry = YList()
                    self.arp_entry.parent = self
                    self.arp_entry.name = 'arp_entry'


                class ArpEntry(object):
                    """
                    Resolution history array
                    
                    .. attribute:: client_id
                    
                    	Resolving Client ID
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: entry_state
                    
                    	ARP entry state
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: idb_interface_name
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: mac_address
                    
                    	MAC address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: nsec_timestamp
                    
                    	Timestamp for entry in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC, January 1, 1970
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: resolution_request_count
                    
                    	Resolution Request count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: status
                    
                    	Resolution status
                    	**type**\:   :py:class:`ArpResolutionHistoryStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpResolutionHistoryStatusEnum>`
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2016-12-19'

                    def __init__(self):
                        self.parent = None
                        self.client_id = None
                        self.entry_state = None
                        self.idb_interface_name = None
                        self.ipv4_address = None
                        self.mac_address = None
                        self.nsec_timestamp = None
                        self.resolution_request_count = None
                        self.status = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:arp-entry'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.client_id is not None:
                            return True

                        if self.entry_state is not None:
                            return True

                        if self.idb_interface_name is not None:
                            return True

                        if self.ipv4_address is not None:
                            return True

                        if self.mac_address is not None:
                            return True

                        if self.nsec_timestamp is not None:
                            return True

                        if self.resolution_request_count is not None:
                            return True

                        if self.status is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                        return meta._meta_table['Arp.Nodes.Node.ResolutionHistoryDynamic.ArpEntry']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:resolution-history-dynamic'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.arp_entry is not None:
                        for child_ref in self.arp_entry:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['Arp.Nodes.Node.ResolutionHistoryDynamic']['meta_info']


            class TrafficVrfs(object):
                """
                ARP Traffic information per VRF
                
                .. attribute:: traffic_vrf
                
                	Per VRF traffic data
                	**type**\: list of    :py:class:`TrafficVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.TrafficVrfs.TrafficVrf>`
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.traffic_vrf = YList()
                    self.traffic_vrf.parent = self
                    self.traffic_vrf.name = 'traffic_vrf'


                class TrafficVrf(object):
                    """
                    Per VRF traffic data
                    
                    .. attribute:: vrf_name  <key>
                    
                    	VRF name
                    	**type**\:  str
                    
                    .. attribute:: alias_entries
                    
                    	Total alias entries in the cache
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: arp_packet_interface_out_of_subnet
                    
                    	Total arp packets on interface due to out of subnet
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: arp_packet_node_out_of_subnet
                    
                    	Total ARP packets on node due to out of subnet
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dhcp_entries
                    
                    	Total DHCP entries in the cache
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dynamic_entries
                    
                    	Total dynamic entries in the cache
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: gratuitous_replies_sent
                    
                    	Total Gratuituous ARP replies sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: idb_structures
                    
                    	Total idb structures on this node
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_entries
                    
                    	Total interface entries in the cache
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ip_packets_dropped_interface
                    
                    	Total ip packets droped on this interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ip_packets_dropped_node
                    
                    	Total ip packets droped on this node
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_proxy_replies_sent
                    
                    	Total Local Proxy ARP replies sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_buffer_errors
                    
                    	Total errors for no buffer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: out_of_memory_errors
                    
                    	Total errors for out of memory
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: proxy_replies_sent
                    
                    	Total Proxy ARP replies sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: replies_received
                    
                    	Total ARP replies received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: replies_sent
                    
                    	Total ARP replies sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: requests_received
                    
                    	Total ARP requests received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: requests_sent
                    
                    	Total ARP requests sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resolution_replies_received
                    
                    	Total ARP resolution replies received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resolution_requests_dropped
                    
                    	total ARP resolution requests dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resolution_requests_received
                    
                    	Total ARP resolution requests received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: standby_entries
                    
                    	Total standby entries in the cache
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: static_entries
                    
                    	Total static entries in the cache
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subscr_replies_gratg_sent
                    
                    	Total ARP grat replies sent over subscriber interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subscr_replies_sent
                    
                    	Total ARP replies sent over subscriber interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subscr_requests_received
                    
                    	Total ARP requests received over subscriber interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_entries
                    
                    	Total ARP entries in the cache
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vxlan_entries
                    
                    	Total VXLAN entries in the cache
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2016-12-19'

                    def __init__(self):
                        self.parent = None
                        self.vrf_name = None
                        self.alias_entries = None
                        self.arp_packet_interface_out_of_subnet = None
                        self.arp_packet_node_out_of_subnet = None
                        self.dhcp_entries = None
                        self.dynamic_entries = None
                        self.gratuitous_replies_sent = None
                        self.idb_structures = None
                        self.interface_entries = None
                        self.ip_packets_dropped_interface = None
                        self.ip_packets_dropped_node = None
                        self.local_proxy_replies_sent = None
                        self.no_buffer_errors = None
                        self.out_of_memory_errors = None
                        self.proxy_replies_sent = None
                        self.replies_received = None
                        self.replies_sent = None
                        self.requests_received = None
                        self.requests_sent = None
                        self.resolution_replies_received = None
                        self.resolution_requests_dropped = None
                        self.resolution_requests_received = None
                        self.standby_entries = None
                        self.static_entries = None
                        self.subscr_replies_gratg_sent = None
                        self.subscr_replies_sent = None
                        self.subscr_requests_received = None
                        self.total_entries = None
                        self.vxlan_entries = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.vrf_name is None:
                            raise YPYModelError('Key property vrf_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:traffic-vrf[Cisco-IOS-XR-ipv4-arp-oper:vrf-name = ' + str(self.vrf_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.vrf_name is not None:
                            return True

                        if self.alias_entries is not None:
                            return True

                        if self.arp_packet_interface_out_of_subnet is not None:
                            return True

                        if self.arp_packet_node_out_of_subnet is not None:
                            return True

                        if self.dhcp_entries is not None:
                            return True

                        if self.dynamic_entries is not None:
                            return True

                        if self.gratuitous_replies_sent is not None:
                            return True

                        if self.idb_structures is not None:
                            return True

                        if self.interface_entries is not None:
                            return True

                        if self.ip_packets_dropped_interface is not None:
                            return True

                        if self.ip_packets_dropped_node is not None:
                            return True

                        if self.local_proxy_replies_sent is not None:
                            return True

                        if self.no_buffer_errors is not None:
                            return True

                        if self.out_of_memory_errors is not None:
                            return True

                        if self.proxy_replies_sent is not None:
                            return True

                        if self.replies_received is not None:
                            return True

                        if self.replies_sent is not None:
                            return True

                        if self.requests_received is not None:
                            return True

                        if self.requests_sent is not None:
                            return True

                        if self.resolution_replies_received is not None:
                            return True

                        if self.resolution_requests_dropped is not None:
                            return True

                        if self.resolution_requests_received is not None:
                            return True

                        if self.standby_entries is not None:
                            return True

                        if self.static_entries is not None:
                            return True

                        if self.subscr_replies_gratg_sent is not None:
                            return True

                        if self.subscr_replies_sent is not None:
                            return True

                        if self.subscr_requests_received is not None:
                            return True

                        if self.total_entries is not None:
                            return True

                        if self.vxlan_entries is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                        return meta._meta_table['Arp.Nodes.Node.TrafficVrfs.TrafficVrf']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:traffic-vrfs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.traffic_vrf is not None:
                        for child_ref in self.traffic_vrf:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['Arp.Nodes.Node.TrafficVrfs']['meta_info']


            class TrafficNode(object):
                """
                Per node ARP Traffic data
                
                .. attribute:: alias_entries
                
                	Total alias entries in the cache
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: arp_packet_interface_out_of_subnet
                
                	Total arp packets on interface due to out of subnet
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: arp_packet_node_out_of_subnet
                
                	Total ARP packets on node due to out of subnet
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dhcp_entries
                
                	Total DHCP entries in the cache
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dynamic_entries
                
                	Total dynamic entries in the cache
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: gratuitous_replies_sent
                
                	Total Gratuituous ARP replies sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: idb_structures
                
                	Total idb structures on this node
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_entries
                
                	Total interface entries in the cache
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ip_packets_dropped_interface
                
                	Total ip packets droped on this interface
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ip_packets_dropped_node
                
                	Total ip packets droped on this node
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_proxy_replies_sent
                
                	Total Local Proxy ARP replies sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: no_buffer_errors
                
                	Total errors for no buffer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_memory_errors
                
                	Total errors for out of memory
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: proxy_replies_sent
                
                	Total Proxy ARP replies sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: replies_received
                
                	Total ARP replies received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: replies_sent
                
                	Total ARP replies sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: requests_received
                
                	Total ARP requests received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: requests_sent
                
                	Total ARP requests sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: resolution_replies_received
                
                	Total ARP resolution replies received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: resolution_requests_dropped
                
                	total ARP resolution requests dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: resolution_requests_received
                
                	Total ARP resolution requests received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: standby_entries
                
                	Total standby entries in the cache
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: static_entries
                
                	Total static entries in the cache
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: subscr_replies_gratg_sent
                
                	Total ARP grat replies sent over subscriber interface
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: subscr_replies_sent
                
                	Total ARP replies sent over subscriber interface
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: subscr_requests_received
                
                	Total ARP requests received over subscriber interface
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_entries
                
                	Total ARP entries in the cache
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vxlan_entries
                
                	Total VXLAN entries in the cache
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.alias_entries = None
                    self.arp_packet_interface_out_of_subnet = None
                    self.arp_packet_node_out_of_subnet = None
                    self.dhcp_entries = None
                    self.dynamic_entries = None
                    self.gratuitous_replies_sent = None
                    self.idb_structures = None
                    self.interface_entries = None
                    self.ip_packets_dropped_interface = None
                    self.ip_packets_dropped_node = None
                    self.local_proxy_replies_sent = None
                    self.no_buffer_errors = None
                    self.out_of_memory_errors = None
                    self.proxy_replies_sent = None
                    self.replies_received = None
                    self.replies_sent = None
                    self.requests_received = None
                    self.requests_sent = None
                    self.resolution_replies_received = None
                    self.resolution_requests_dropped = None
                    self.resolution_requests_received = None
                    self.standby_entries = None
                    self.static_entries = None
                    self.subscr_replies_gratg_sent = None
                    self.subscr_replies_sent = None
                    self.subscr_requests_received = None
                    self.total_entries = None
                    self.vxlan_entries = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:traffic-node'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.alias_entries is not None:
                        return True

                    if self.arp_packet_interface_out_of_subnet is not None:
                        return True

                    if self.arp_packet_node_out_of_subnet is not None:
                        return True

                    if self.dhcp_entries is not None:
                        return True

                    if self.dynamic_entries is not None:
                        return True

                    if self.gratuitous_replies_sent is not None:
                        return True

                    if self.idb_structures is not None:
                        return True

                    if self.interface_entries is not None:
                        return True

                    if self.ip_packets_dropped_interface is not None:
                        return True

                    if self.ip_packets_dropped_node is not None:
                        return True

                    if self.local_proxy_replies_sent is not None:
                        return True

                    if self.no_buffer_errors is not None:
                        return True

                    if self.out_of_memory_errors is not None:
                        return True

                    if self.proxy_replies_sent is not None:
                        return True

                    if self.replies_received is not None:
                        return True

                    if self.replies_sent is not None:
                        return True

                    if self.requests_received is not None:
                        return True

                    if self.requests_sent is not None:
                        return True

                    if self.resolution_replies_received is not None:
                        return True

                    if self.resolution_requests_dropped is not None:
                        return True

                    if self.resolution_requests_received is not None:
                        return True

                    if self.standby_entries is not None:
                        return True

                    if self.static_entries is not None:
                        return True

                    if self.subscr_replies_gratg_sent is not None:
                        return True

                    if self.subscr_replies_sent is not None:
                        return True

                    if self.subscr_requests_received is not None:
                        return True

                    if self.total_entries is not None:
                        return True

                    if self.vxlan_entries is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['Arp.Nodes.Node.TrafficNode']['meta_info']


            class ResolutionHistoryClient(object):
                """
                Per node client\-installed ARP resolution
                history data
                
                .. attribute:: arp_entry
                
                	Resolution history array
                	**type**\: list of    :py:class:`ArpEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.ResolutionHistoryClient.ArpEntry>`
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.arp_entry = YList()
                    self.arp_entry.parent = self
                    self.arp_entry.name = 'arp_entry'


                class ArpEntry(object):
                    """
                    Resolution history array
                    
                    .. attribute:: client_id
                    
                    	Resolving Client ID
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: entry_state
                    
                    	ARP entry state
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: idb_interface_name
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: mac_address
                    
                    	MAC address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: nsec_timestamp
                    
                    	Timestamp for entry in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC, January 1, 1970
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: resolution_request_count
                    
                    	Resolution Request count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: status
                    
                    	Resolution status
                    	**type**\:   :py:class:`ArpResolutionHistoryStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpResolutionHistoryStatusEnum>`
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2016-12-19'

                    def __init__(self):
                        self.parent = None
                        self.client_id = None
                        self.entry_state = None
                        self.idb_interface_name = None
                        self.ipv4_address = None
                        self.mac_address = None
                        self.nsec_timestamp = None
                        self.resolution_request_count = None
                        self.status = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:arp-entry'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.client_id is not None:
                            return True

                        if self.entry_state is not None:
                            return True

                        if self.idb_interface_name is not None:
                            return True

                        if self.ipv4_address is not None:
                            return True

                        if self.mac_address is not None:
                            return True

                        if self.nsec_timestamp is not None:
                            return True

                        if self.resolution_request_count is not None:
                            return True

                        if self.status is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                        return meta._meta_table['Arp.Nodes.Node.ResolutionHistoryClient.ArpEntry']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:resolution-history-client'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.arp_entry is not None:
                        for child_ref in self.arp_entry:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['Arp.Nodes.Node.ResolutionHistoryClient']['meta_info']


            class Entries(object):
                """
                Table of ARP entries
                
                .. attribute:: entry
                
                	ARP entry
                	**type**\: list of    :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.Entries.Entry>`
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.entry = YList()
                    self.entry.parent = self
                    self.entry.name = 'entry'


                class Entry(object):
                    """
                    ARP entry
                    
                    .. attribute:: address  <key>
                    
                    	IP Address of ARP entry
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: age
                    
                    	Age of this entry
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: encapsulation_type
                    
                    	Source encapsulation type
                    	**type**\:   :py:class:`IpArpBagEncapEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.IpArpBagEncapEnum>`
                    
                    .. attribute:: flag
                    
                    	Flags of this entry
                    	**type**\:   :py:class:`IpArpBagFlagsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.IpArpBagFlagsEnum>`
                    
                    .. attribute:: hardware_address
                    
                    	Hardware address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: hardware_length
                    
                    	Source hardware length
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: media_type
                    
                    	Media type for this entry
                    	**type**\:   :py:class:`IpArpBagMediaEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.IpArpBagMediaEnum>`
                    
                    .. attribute:: state
                    
                    	State of this entry
                    	**type**\:   :py:class:`IpArpBagStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.IpArpBagStateEnum>`
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2016-12-19'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.interface_name = None
                        self.age = None
                        self.encapsulation_type = None
                        self.flag = None
                        self.hardware_address = None
                        self.hardware_length = None
                        self.media_type = None
                        self.state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:entry[Cisco-IOS-XR-ipv4-arp-oper:address = ' + str(self.address) + '][Cisco-IOS-XR-ipv4-arp-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.address is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.age is not None:
                            return True

                        if self.encapsulation_type is not None:
                            return True

                        if self.flag is not None:
                            return True

                        if self.hardware_address is not None:
                            return True

                        if self.hardware_length is not None:
                            return True

                        if self.media_type is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                        return meta._meta_table['Arp.Nodes.Node.Entries.Entry']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:entries'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.entry is not None:
                        for child_ref in self.entry:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['Arp.Nodes.Node.Entries']['meta_info']


            class TrafficInterfaces(object):
                """
                ARP Traffic information per interface
                
                .. attribute:: traffic_interface
                
                	Per interface traffic data
                	**type**\: list of    :py:class:`TrafficInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.TrafficInterfaces.TrafficInterface>`
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.traffic_interface = YList()
                    self.traffic_interface.parent = self
                    self.traffic_interface.name = 'traffic_interface'


                class TrafficInterface(object):
                    """
                    Per interface traffic data
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: alias_entries
                    
                    	Total alias entries in the cache
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: arp_packet_interface_out_of_subnet
                    
                    	Total arp packets on interface due to out of subnet
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: arp_packet_node_out_of_subnet
                    
                    	Total ARP packets on node due to out of subnet
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dhcp_entries
                    
                    	Total DHCP entries in the cache
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dynamic_entries
                    
                    	Total dynamic entries in the cache
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: gratuitous_replies_sent
                    
                    	Total Gratuituous ARP replies sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: idb_structures
                    
                    	Total idb structures on this node
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_entries
                    
                    	Total interface entries in the cache
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ip_packets_dropped_interface
                    
                    	Total ip packets droped on this interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ip_packets_dropped_node
                    
                    	Total ip packets droped on this node
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_proxy_replies_sent
                    
                    	Total Local Proxy ARP replies sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_buffer_errors
                    
                    	Total errors for no buffer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: out_of_memory_errors
                    
                    	Total errors for out of memory
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: proxy_replies_sent
                    
                    	Total Proxy ARP replies sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: replies_received
                    
                    	Total ARP replies received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: replies_sent
                    
                    	Total ARP replies sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: requests_received
                    
                    	Total ARP requests received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: requests_sent
                    
                    	Total ARP requests sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resolution_replies_received
                    
                    	Total ARP resolution replies received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resolution_requests_dropped
                    
                    	total ARP resolution requests dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resolution_requests_received
                    
                    	Total ARP resolution requests received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: standby_entries
                    
                    	Total standby entries in the cache
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: static_entries
                    
                    	Total static entries in the cache
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subscr_replies_gratg_sent
                    
                    	Total ARP grat replies sent over subscriber interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subscr_replies_sent
                    
                    	Total ARP replies sent over subscriber interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subscr_requests_received
                    
                    	Total ARP requests received over subscriber interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_entries
                    
                    	Total ARP entries in the cache
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vxlan_entries
                    
                    	Total VXLAN entries in the cache
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2016-12-19'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.alias_entries = None
                        self.arp_packet_interface_out_of_subnet = None
                        self.arp_packet_node_out_of_subnet = None
                        self.dhcp_entries = None
                        self.dynamic_entries = None
                        self.gratuitous_replies_sent = None
                        self.idb_structures = None
                        self.interface_entries = None
                        self.ip_packets_dropped_interface = None
                        self.ip_packets_dropped_node = None
                        self.local_proxy_replies_sent = None
                        self.no_buffer_errors = None
                        self.out_of_memory_errors = None
                        self.proxy_replies_sent = None
                        self.replies_received = None
                        self.replies_sent = None
                        self.requests_received = None
                        self.requests_sent = None
                        self.resolution_replies_received = None
                        self.resolution_requests_dropped = None
                        self.resolution_requests_received = None
                        self.standby_entries = None
                        self.static_entries = None
                        self.subscr_replies_gratg_sent = None
                        self.subscr_replies_sent = None
                        self.subscr_requests_received = None
                        self.total_entries = None
                        self.vxlan_entries = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:traffic-interface[Cisco-IOS-XR-ipv4-arp-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.alias_entries is not None:
                            return True

                        if self.arp_packet_interface_out_of_subnet is not None:
                            return True

                        if self.arp_packet_node_out_of_subnet is not None:
                            return True

                        if self.dhcp_entries is not None:
                            return True

                        if self.dynamic_entries is not None:
                            return True

                        if self.gratuitous_replies_sent is not None:
                            return True

                        if self.idb_structures is not None:
                            return True

                        if self.interface_entries is not None:
                            return True

                        if self.ip_packets_dropped_interface is not None:
                            return True

                        if self.ip_packets_dropped_node is not None:
                            return True

                        if self.local_proxy_replies_sent is not None:
                            return True

                        if self.no_buffer_errors is not None:
                            return True

                        if self.out_of_memory_errors is not None:
                            return True

                        if self.proxy_replies_sent is not None:
                            return True

                        if self.replies_received is not None:
                            return True

                        if self.replies_sent is not None:
                            return True

                        if self.requests_received is not None:
                            return True

                        if self.requests_sent is not None:
                            return True

                        if self.resolution_replies_received is not None:
                            return True

                        if self.resolution_requests_dropped is not None:
                            return True

                        if self.resolution_requests_received is not None:
                            return True

                        if self.standby_entries is not None:
                            return True

                        if self.static_entries is not None:
                            return True

                        if self.subscr_replies_gratg_sent is not None:
                            return True

                        if self.subscr_replies_sent is not None:
                            return True

                        if self.subscr_requests_received is not None:
                            return True

                        if self.total_entries is not None:
                            return True

                        if self.vxlan_entries is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                        return meta._meta_table['Arp.Nodes.Node.TrafficInterfaces.TrafficInterface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-oper:traffic-interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.traffic_interface is not None:
                        for child_ref in self.traffic_interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['Arp.Nodes.Node.TrafficInterfaces']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ipv4-arp-oper:arp/Cisco-IOS-XR-ipv4-arp-oper:nodes/Cisco-IOS-XR-ipv4-arp-oper:node[Cisco-IOS-XR-ipv4-arp-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.entries is not None and self.entries._has_data():
                    return True

                if self.resolution_history_client is not None and self.resolution_history_client._has_data():
                    return True

                if self.resolution_history_dynamic is not None and self.resolution_history_dynamic._has_data():
                    return True

                if self.traffic_interfaces is not None and self.traffic_interfaces._has_data():
                    return True

                if self.traffic_node is not None and self.traffic_node._has_data():
                    return True

                if self.traffic_vrfs is not None and self.traffic_vrfs._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                return meta._meta_table['Arp.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-arp-oper:arp/Cisco-IOS-XR-ipv4-arp-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
            return meta._meta_table['Arp.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-arp-oper:arp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['Arp']['meta_info']


