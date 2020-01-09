""" Cisco_IOS_XR_ipv4_arp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-arp package operational data.

This module contains definitions
for the following management objects\:
  arp\-gmp\: ARP\-GMP global operational data
  arp\: arp

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ArpGmpBagEncap(Enum):
    """
    ArpGmpBagEncap (Enum Class)

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

    none = Enum.YLeaf(0, "none")

    arpa = Enum.YLeaf(1, "arpa")

    snap = Enum.YLeaf(2, "snap")

    ieee802_1q = Enum.YLeaf(3, "ieee802-1q")

    srp = Enum.YLeaf(4, "srp")

    srpa = Enum.YLeaf(5, "srpa")

    srpb = Enum.YLeaf(6, "srpb")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['ArpGmpBagEncap']


class ArpGmpBagEntry(Enum):
    """
    ArpGmpBagEntry (Enum Class)

    ARP Entry type

    .. data:: null = 0

    	No state

    .. data:: static = 1

    	Static

    .. data:: alias = 2

    	Alias

    """

    null = Enum.YLeaf(0, "null")

    static = Enum.YLeaf(1, "static")

    alias = Enum.YLeaf(2, "alias")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['ArpGmpBagEntry']


class ArpIssuPhase(Enum):
    """
    ArpIssuPhase (Enum Class)

    Arp issu phase

    .. data:: phase_not_started = 0

    	An ISSU event has not started

    .. data:: phase_load = 1

    	ISSU Load Phase

    .. data:: phase_run = 2

    	ISSU Run Phase

    .. data:: phase_completed = 3

    	An ISSU event has completed successfully

    .. data:: phase_aborted = 4

    	An ISSU event has aborted

    """

    phase_not_started = Enum.YLeaf(0, "phase-not-started")

    phase_load = Enum.YLeaf(1, "phase-load")

    phase_run = Enum.YLeaf(2, "phase-run")

    phase_completed = Enum.YLeaf(3, "phase-completed")

    phase_aborted = Enum.YLeaf(4, "phase-aborted")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['ArpIssuPhase']


class ArpIssuRole(Enum):
    """
    ArpIssuRole (Enum Class)

    Arp issu role

    .. data:: role_primary = 0

    	Primary role

    .. data:: role_secondary = 1

    	Secondary role

    """

    role_primary = Enum.YLeaf(0, "role-primary")

    role_secondary = Enum.YLeaf(1, "role-secondary")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['ArpIssuRole']


class ArpIssuVersion(Enum):
    """
    ArpIssuVersion (Enum Class)

    Arp issu version

    .. data:: version1 = 0

    	Version 1

    .. data:: version2 = 1

    	Version 2

    """

    version1 = Enum.YLeaf(0, "version1")

    version2 = Enum.YLeaf(1, "version2")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['ArpIssuVersion']


class ArpResolutionHistoryStatus(Enum):
    """
    ArpResolutionHistoryStatus (Enum Class)

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

    .. data:: status_dropped_unsolicited_pak = 22

    	Learning unsolicited ARP packets is disabled on

    	this Interface

    .. data:: status_drop_adjacency_added = 23

    	Adding drop adjacency entry for the address

    """

    status_none = Enum.YLeaf(0, "status-none")

    status_resolution_request = Enum.YLeaf(1, "status-resolution-request")

    status_resolved_reply = Enum.YLeaf(2, "status-resolved-reply")

    status_resolved_grat_arp = Enum.YLeaf(3, "status-resolved-grat-arp")

    status_resolved_request = Enum.YLeaf(4, "status-resolved-request")

    status_resolved_lc_sync = Enum.YLeaf(5, "status-resolved-lc-sync")

    status_resolved_lc_sync_purge_delay = Enum.YLeaf(6, "status-resolved-lc-sync-purge-delay")

    status_resolved_client = Enum.YLeaf(7, "status-resolved-client")

    status_removed_client = Enum.YLeaf(8, "status-removed-client")

    status_already_resolved = Enum.YLeaf(9, "status-already-resolved")

    status_failed = Enum.YLeaf(10, "status-failed")

    status_dropped_interface_down = Enum.YLeaf(11, "status-dropped-interface-down")

    status_dropped_broadcast_disabled = Enum.YLeaf(12, "status-dropped-broadcast-disabled")

    status_dropped_interface_unavailable = Enum.YLeaf(13, "status-dropped-interface-unavailable")

    status_dropped_bad_subnet = Enum.YLeaf(14, "status-dropped-bad-subnet")

    status_dropped_dynamic_learning_disabled = Enum.YLeaf(15, "status-dropped-dynamic-learning-disabled")

    status_dropped_out_of_subnet_disabled = Enum.YLeaf(16, "status-dropped-out-of-subnet-disabled")

    status_removed_client_sweep = Enum.YLeaf(17, "status-removed-client-sweep")

    status_added_client = Enum.YLeaf(18, "status-added-client")

    status_added_v1 = Enum.YLeaf(19, "status-added-v1")

    status_removed_v1 = Enum.YLeaf(20, "status-removed-v1")

    status_resolved_peer_sync = Enum.YLeaf(21, "status-resolved-peer-sync")

    status_dropped_unsolicited_pak = Enum.YLeaf(22, "status-dropped-unsolicited-pak")

    status_drop_adjacency_added = Enum.YLeaf(23, "status-drop-adjacency-added")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['ArpResolutionHistoryStatus']


class IpArpBagEncap(Enum):
    """
    IpArpBagEncap (Enum Class)

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

    none = Enum.YLeaf(0, "none")

    arpa = Enum.YLeaf(1, "arpa")

    snap = Enum.YLeaf(2, "snap")

    ieee802_1q = Enum.YLeaf(3, "ieee802-1q")

    srp = Enum.YLeaf(4, "srp")

    srpa = Enum.YLeaf(5, "srpa")

    srpb = Enum.YLeaf(6, "srpb")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['IpArpBagEncap']


class IpArpBagFlags(Enum):
    """
    IpArpBagFlags (Enum Class)

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

    flag_none = Enum.YLeaf(0, "flag-none")

    flag_dynamic = Enum.YLeaf(1, "flag-dynamic")

    flag_evpn_sync = Enum.YLeaf(2, "flag-evpn-sync")

    flag_max = Enum.YLeaf(3, "flag-max")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['IpArpBagFlags']


class IpArpBagMedia(Enum):
    """
    IpArpBagMedia (Enum Class)

    ARP media type

    .. data:: media_arpa = 0

    	ARPA

    .. data:: media_srp = 1

    	SRP

    .. data:: media_unknown = 2

    	Unknown

    """

    media_arpa = Enum.YLeaf(0, "media-arpa")

    media_srp = Enum.YLeaf(1, "media-srp")

    media_unknown = Enum.YLeaf(2, "media-unknown")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['IpArpBagMedia']


class IpArpBagState(Enum):
    """
    IpArpBagState (Enum Class)

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

    .. data:: state_drop_adj = 16

    	Drop adjacency

    .. data:: state_stale = 17

    	Stale

    .. data:: state_max = 18

    	Maximum state number

    """

    state_none = Enum.YLeaf(0, "state-none")

    state_interface = Enum.YLeaf(1, "state-interface")

    state_standby = Enum.YLeaf(2, "state-standby")

    state_static = Enum.YLeaf(3, "state-static")

    state_alias = Enum.YLeaf(4, "state-alias")

    state_mobile = Enum.YLeaf(5, "state-mobile")

    state_incomplete = Enum.YLeaf(6, "state-incomplete")

    state_deleted = Enum.YLeaf(7, "state-deleted")

    state_dynamic = Enum.YLeaf(8, "state-dynamic")

    state_probe = Enum.YLeaf(9, "state-probe")

    state_purge_delayed = Enum.YLeaf(10, "state-purge-delayed")

    state_dhcp = Enum.YLeaf(11, "state-dhcp")

    state_vxlan = Enum.YLeaf(12, "state-vxlan")

    state_evpn_sync = Enum.YLeaf(13, "state-evpn-sync")

    state_sat = Enum.YLeaf(14, "state-sat")

    state_r_sync = Enum.YLeaf(15, "state-r-sync")

    state_drop_adj = Enum.YLeaf(16, "state-drop-adj")

    state_stale = Enum.YLeaf(17, "state-stale")

    state_max = Enum.YLeaf(18, "state-max")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['IpArpBagState']



class ArpGmp(_Entity_):
    """
    ARP\-GMP global operational data
    
    .. attribute:: vrf_infos
    
    	Table of VRF related ARP\-GMP operational data
    	**type**\:  :py:class:`VrfInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.VrfInfos>`
    
    	**config**\: False
    
    .. attribute:: vrfs
    
    	Table of per VRF ARP\-GMP operational data
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ipv4-arp-oper'
    _revision = '2017-05-01'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(ArpGmp, self).__init__()
        self._top_entity = None

        self.yang_name = "arp-gmp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-arp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrf-infos", ("vrf_infos", ArpGmp.VrfInfos)), ("vrfs", ("vrfs", ArpGmp.Vrfs))])
        self._leafs = OrderedDict()

        self.vrf_infos = ArpGmp.VrfInfos()
        self.vrf_infos.parent = self
        self._children_name_map["vrf_infos"] = "vrf-infos"

        self.vrfs = ArpGmp.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-arp-oper:arp-gmp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ArpGmp, [], name, value)


    class VrfInfos(_Entity_):
        """
        Table of VRF related ARP\-GMP operational data
        
        .. attribute:: vrf_info
        
        	VRF related ARP\-GMP operational data
        	**type**\: list of  		 :py:class:`VrfInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.VrfInfos.VrfInfo>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ipv4-arp-oper'
        _revision = '2017-05-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ArpGmp.VrfInfos, self).__init__()

            self.yang_name = "vrf-infos"
            self.yang_parent_name = "arp-gmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf-info", ("vrf_info", ArpGmp.VrfInfos.VrfInfo))])
            self._leafs = OrderedDict()

            self.vrf_info = YList(self)
            self._segment_path = lambda: "vrf-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-arp-oper:arp-gmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ArpGmp.VrfInfos, [], name, value)


        class VrfInfo(_Entity_):
            """
            VRF related ARP\-GMP operational data
            
            .. attribute:: vrf_name  (key)
            
            	VRF name for the default VRF use 'default'
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            	**config**\: False
            
            .. attribute:: vrf_name_xr
            
            	VRF Name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: vrf_id_number
            
            	VRF ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: table_id
            
            	IPv4 unicast table ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rsi_handle
            
            	RSI registration handle
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rsi_handle_high
            
            	RSI registration handle (top 32\-bits)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'ipv4-arp-oper'
            _revision = '2017-05-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ArpGmp.VrfInfos.VrfInfo, self).__init__()

                self.yang_name = "vrf-info"
                self.yang_parent_name = "vrf-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('vrf_name_xr', (YLeaf(YType.str, 'vrf-name-xr'), ['str'])),
                    ('vrf_id_number', (YLeaf(YType.uint32, 'vrf-id-number'), ['int'])),
                    ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                    ('rsi_handle', (YLeaf(YType.uint32, 'rsi-handle'), ['int'])),
                    ('rsi_handle_high', (YLeaf(YType.uint32, 'rsi-handle-high'), ['int'])),
                ])
                self.vrf_name = None
                self.vrf_name_xr = None
                self.vrf_id_number = None
                self.table_id = None
                self.rsi_handle = None
                self.rsi_handle_high = None
                self._segment_path = lambda: "vrf-info" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-arp-oper:arp-gmp/vrf-infos/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ArpGmp.VrfInfos.VrfInfo, ['vrf_name', 'vrf_name_xr', 'vrf_id_number', 'table_id', 'rsi_handle', 'rsi_handle_high'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                return meta._meta_table['ArpGmp.VrfInfos.VrfInfo']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
            return meta._meta_table['ArpGmp.VrfInfos']['meta_info']


    class Vrfs(_Entity_):
        """
        Table of per VRF ARP\-GMP operational data
        
        .. attribute:: vrf
        
        	Per VRF ARP\-GMP operational data
        	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ipv4-arp-oper'
        _revision = '2017-05-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ArpGmp.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "arp-gmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf", ("vrf", ArpGmp.Vrfs.Vrf))])
            self._leafs = OrderedDict()

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-arp-oper:arp-gmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ArpGmp.Vrfs, [], name, value)


        class Vrf(_Entity_):
            """
            Per VRF ARP\-GMP operational data
            
            .. attribute:: vrf_name  (key)
            
            	VRF name for the default VRF use 'default'
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            	**config**\: False
            
            .. attribute:: configured_ip_addresses
            
            	Table of ARP\-GMP configured IP addresses information
            	**type**\:  :py:class:`ConfiguredIpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses>`
            
            	**config**\: False
            
            .. attribute:: routes
            
            	Table of ARP GMP route information
            	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf.Routes>`
            
            	**config**\: False
            
            .. attribute:: interface_configured_ips
            
            	Table of ARP GMP interface and associated configured IP data
            	**type**\:  :py:class:`InterfaceConfiguredIps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ipv4-arp-oper'
            _revision = '2017-05-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ArpGmp.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("configured-ip-addresses", ("configured_ip_addresses", ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses)), ("routes", ("routes", ArpGmp.Vrfs.Vrf.Routes)), ("interface-configured-ips", ("interface_configured_ips", ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.vrf_name = None

                self.configured_ip_addresses = ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses()
                self.configured_ip_addresses.parent = self
                self._children_name_map["configured_ip_addresses"] = "configured-ip-addresses"

                self.routes = ArpGmp.Vrfs.Vrf.Routes()
                self.routes.parent = self
                self._children_name_map["routes"] = "routes"

                self.interface_configured_ips = ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps()
                self.interface_configured_ips.parent = self
                self._children_name_map["interface_configured_ips"] = "interface-configured-ips"
                self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-arp-oper:arp-gmp/vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ArpGmp.Vrfs.Vrf, ['vrf_name'], name, value)


            class ConfiguredIpAddresses(_Entity_):
                """
                Table of ARP\-GMP configured IP addresses
                information
                
                .. attribute:: configured_ip_address
                
                	ARP\-GMP configured IP address information
                	**type**\: list of  		 :py:class:`ConfiguredIpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses.ConfiguredIpAddress>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses, self).__init__()

                    self.yang_name = "configured-ip-addresses"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("configured-ip-address", ("configured_ip_address", ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses.ConfiguredIpAddress))])
                    self._leafs = OrderedDict()

                    self.configured_ip_address = YList(self)
                    self._segment_path = lambda: "configured-ip-addresses"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses, [], name, value)


                class ConfiguredIpAddress(_Entity_):
                    """
                    ARP\-GMP configured IP address information
                    
                    .. attribute:: address  (key)
                    
                    	Configured ARP\-GMP IP
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: ip_address
                    
                    	IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: hardware_address
                    
                    	Hardware address 
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    	**config**\: False
                    
                    .. attribute:: encapsulation_type
                    
                    	Encap type
                    	**type**\:  :py:class:`ArpGmpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmpBagEncap>`
                    
                    	**config**\: False
                    
                    .. attribute:: entry_type
                    
                    	Entry type static/alias
                    	**type**\:  :py:class:`ArpGmpBagEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmpBagEntry>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses.ConfiguredIpAddress, self).__init__()

                        self.yang_name = "configured-ip-address"
                        self.yang_parent_name = "configured-ip-addresses"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                            ('hardware_address', (YLeaf(YType.str, 'hardware-address'), ['str'])),
                            ('encapsulation_type', (YLeaf(YType.enumeration, 'encapsulation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmpBagEncap', '')])),
                            ('entry_type', (YLeaf(YType.enumeration, 'entry-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmpBagEntry', '')])),
                        ])
                        self.address = None
                        self.ip_address = None
                        self.hardware_address = None
                        self.encapsulation_type = None
                        self.entry_type = None
                        self._segment_path = lambda: "configured-ip-address" + "[address='" + str(self.address) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses.ConfiguredIpAddress, ['address', 'ip_address', 'hardware_address', 'encapsulation_type', 'entry_type'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                        return meta._meta_table['ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses.ConfiguredIpAddress']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses']['meta_info']


            class Routes(_Entity_):
                """
                Table of ARP GMP route information
                
                .. attribute:: route
                
                	ARP GMP route information
                	**type**\: list of  		 :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf.Routes.Route>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ArpGmp.Vrfs.Vrf.Routes, self).__init__()

                    self.yang_name = "routes"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("route", ("route", ArpGmp.Vrfs.Vrf.Routes.Route))])
                    self._leafs = OrderedDict()

                    self.route = YList(self)
                    self._segment_path = lambda: "routes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ArpGmp.Vrfs.Vrf.Routes, [], name, value)


                class Route(_Entity_):
                    """
                    ARP GMP route information
                    
                    .. attribute:: address
                    
                    	IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length
                    	**type**\: int
                    
                    	**range:** 0..32
                    
                    	**config**\: False
                    
                    .. attribute:: ip_address
                    
                    	IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: prefix_length_xr
                    
                    	IP address length
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface name (first element of InterfaceNames array)
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: interface_name
                    
                    	Interface names
                    	**type**\: list of str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(ArpGmp.Vrfs.Vrf.Routes.Route, self).__init__()

                        self.yang_name = "route"
                        self.yang_parent_name = "routes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                            ('prefix_length_xr', (YLeaf(YType.uint8, 'prefix-length-xr'), ['int'])),
                            ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                            ('interface_name', (YLeafList(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.address = None
                        self.prefix_length = None
                        self.ip_address = None
                        self.prefix_length_xr = None
                        self.interface_name_xr = None
                        self.interface_name = []
                        self._segment_path = lambda: "route"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ArpGmp.Vrfs.Vrf.Routes.Route, ['address', 'prefix_length', 'ip_address', 'prefix_length_xr', 'interface_name_xr', 'interface_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                        return meta._meta_table['ArpGmp.Vrfs.Vrf.Routes.Route']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['ArpGmp.Vrfs.Vrf.Routes']['meta_info']


            class InterfaceConfiguredIps(_Entity_):
                """
                Table of ARP GMP interface and associated
                configured IP data
                
                .. attribute:: interface_configured_ip
                
                	ARP GMP interface and associated configured IP data
                	**type**\: list of  		 :py:class:`InterfaceConfiguredIp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps, self).__init__()

                    self.yang_name = "interface-configured-ips"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-configured-ip", ("interface_configured_ip", ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp))])
                    self._leafs = OrderedDict()

                    self.interface_configured_ip = YList(self)
                    self._segment_path = lambda: "interface-configured-ips"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps, [], name, value)


                class InterfaceConfiguredIp(_Entity_):
                    """
                    ARP GMP interface and associated configured
                    IP data
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: address
                    
                    	Configured ARP\-GMP IP
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: associated_configuration_entry
                    
                    	Associated configuration entry
                    	**type**\:  :py:class:`AssociatedConfigurationEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry>`
                    
                    	**config**\: False
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: reference_count
                    
                    	Route reference count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp, self).__init__()

                        self.yang_name = "interface-configured-ip"
                        self.yang_parent_name = "interface-configured-ips"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("associated-configuration-entry", ("associated_configuration_entry", ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                            ('reference_count', (YLeaf(YType.uint32, 'reference-count'), ['int'])),
                        ])
                        self.interface_name = None
                        self.address = None
                        self.interface_name_xr = None
                        self.reference_count = None

                        self.associated_configuration_entry = ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry()
                        self.associated_configuration_entry.parent = self
                        self._children_name_map["associated_configuration_entry"] = "associated-configuration-entry"
                        self._segment_path = lambda: "interface-configured-ip"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp, ['interface_name', 'address', 'interface_name_xr', 'reference_count'], name, value)


                    class AssociatedConfigurationEntry(_Entity_):
                        """
                        Associated configuration entry
                        
                        .. attribute:: ip_address
                        
                        	IP address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: hardware_address
                        
                        	Hardware address 
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        	**config**\: False
                        
                        .. attribute:: encapsulation_type
                        
                        	Encap type
                        	**type**\:  :py:class:`ArpGmpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmpBagEncap>`
                        
                        	**config**\: False
                        
                        .. attribute:: entry_type
                        
                        	Entry type static/alias
                        	**type**\:  :py:class:`ArpGmpBagEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmpBagEntry>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv4-arp-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry, self).__init__()

                            self.yang_name = "associated-configuration-entry"
                            self.yang_parent_name = "interface-configured-ip"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                ('hardware_address', (YLeaf(YType.str, 'hardware-address'), ['str'])),
                                ('encapsulation_type', (YLeaf(YType.enumeration, 'encapsulation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmpBagEncap', '')])),
                                ('entry_type', (YLeaf(YType.enumeration, 'entry-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmpBagEntry', '')])),
                            ])
                            self.ip_address = None
                            self.hardware_address = None
                            self.encapsulation_type = None
                            self.entry_type = None
                            self._segment_path = lambda: "associated-configuration-entry"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry, ['ip_address', 'hardware_address', 'encapsulation_type', 'entry_type'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                            return meta._meta_table['ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                        return meta._meta_table['ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                return meta._meta_table['ArpGmp.Vrfs.Vrf']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
            return meta._meta_table['ArpGmp.Vrfs']['meta_info']

    def clone_ptr(self):
        self._top_entity = ArpGmp()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['ArpGmp']['meta_info']


class Arp(_Entity_):
    """
    arp
    
    .. attribute:: nodes
    
    	Table of per\-node ARP operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ipv4-arp-oper'
    _revision = '2017-05-01'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Arp, self).__init__()
        self._top_entity = None

        self.yang_name = "arp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-arp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Arp.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Arp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-arp-oper:arp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Arp, [], name, value)


    class Nodes(_Entity_):
        """
        Table of per\-node ARP operational data
        
        .. attribute:: node
        
        	Per\-node ARP operational data
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ipv4-arp-oper'
        _revision = '2017-05-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Arp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "arp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Arp.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-arp-oper:arp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Arp.Nodes, [], name, value)


        class Node(_Entity_):
            """
            Per\-node ARP operational data
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: resolution_history_dynamic
            
            	Per node dynamically\-resolved ARP resolution history data
            	**type**\:  :py:class:`ResolutionHistoryDynamic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.ResolutionHistoryDynamic>`
            
            	**config**\: False
            
            .. attribute:: arp_status_info
            
            	Per node ARP status information
            	**type**\:  :py:class:`ArpStatusInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.ArpStatusInfo>`
            
            	**config**\: False
            
            .. attribute:: traffic_vrfs
            
            	ARP Traffic information per VRF
            	**type**\:  :py:class:`TrafficVrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.TrafficVrfs>`
            
            	**config**\: False
            
            .. attribute:: traffic_node
            
            	Per node ARP Traffic data
            	**type**\:  :py:class:`TrafficNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.TrafficNode>`
            
            	**config**\: False
            
            .. attribute:: resolution_history_client
            
            	Per node client\-installed ARP resolution history data
            	**type**\:  :py:class:`ResolutionHistoryClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.ResolutionHistoryClient>`
            
            	**config**\: False
            
            .. attribute:: entries
            
            	Table of ARP entries
            	**type**\:  :py:class:`Entries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.Entries>`
            
            	**config**\: False
            
            .. attribute:: traffic_interfaces
            
            	ARP Traffic information per interface
            	**type**\:  :py:class:`TrafficInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.TrafficInterfaces>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ipv4-arp-oper'
            _revision = '2017-05-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Arp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("resolution-history-dynamic", ("resolution_history_dynamic", Arp.Nodes.Node.ResolutionHistoryDynamic)), ("arp-status-info", ("arp_status_info", Arp.Nodes.Node.ArpStatusInfo)), ("traffic-vrfs", ("traffic_vrfs", Arp.Nodes.Node.TrafficVrfs)), ("traffic-node", ("traffic_node", Arp.Nodes.Node.TrafficNode)), ("resolution-history-client", ("resolution_history_client", Arp.Nodes.Node.ResolutionHistoryClient)), ("entries", ("entries", Arp.Nodes.Node.Entries)), ("traffic-interfaces", ("traffic_interfaces", Arp.Nodes.Node.TrafficInterfaces))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.resolution_history_dynamic = Arp.Nodes.Node.ResolutionHistoryDynamic()
                self.resolution_history_dynamic.parent = self
                self._children_name_map["resolution_history_dynamic"] = "resolution-history-dynamic"

                self.arp_status_info = Arp.Nodes.Node.ArpStatusInfo()
                self.arp_status_info.parent = self
                self._children_name_map["arp_status_info"] = "arp-status-info"

                self.traffic_vrfs = Arp.Nodes.Node.TrafficVrfs()
                self.traffic_vrfs.parent = self
                self._children_name_map["traffic_vrfs"] = "traffic-vrfs"

                self.traffic_node = Arp.Nodes.Node.TrafficNode()
                self.traffic_node.parent = self
                self._children_name_map["traffic_node"] = "traffic-node"

                self.resolution_history_client = Arp.Nodes.Node.ResolutionHistoryClient()
                self.resolution_history_client.parent = self
                self._children_name_map["resolution_history_client"] = "resolution-history-client"

                self.entries = Arp.Nodes.Node.Entries()
                self.entries.parent = self
                self._children_name_map["entries"] = "entries"

                self.traffic_interfaces = Arp.Nodes.Node.TrafficInterfaces()
                self.traffic_interfaces.parent = self
                self._children_name_map["traffic_interfaces"] = "traffic-interfaces"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-arp-oper:arp/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Arp.Nodes.Node, ['node_name'], name, value)


            class ResolutionHistoryDynamic(_Entity_):
                """
                Per node dynamically\-resolved ARP resolution
                history data
                
                .. attribute:: arp_entry
                
                	Resolution history array
                	**type**\: list of  		 :py:class:`ArpEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.ResolutionHistoryDynamic.ArpEntry>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Arp.Nodes.Node.ResolutionHistoryDynamic, self).__init__()

                    self.yang_name = "resolution-history-dynamic"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("arp-entry", ("arp_entry", Arp.Nodes.Node.ResolutionHistoryDynamic.ArpEntry))])
                    self._leafs = OrderedDict()

                    self.arp_entry = YList(self)
                    self._segment_path = lambda: "resolution-history-dynamic"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Arp.Nodes.Node.ResolutionHistoryDynamic, [], name, value)


                class ArpEntry(_Entity_):
                    """
                    Resolution history array
                    
                    .. attribute:: nsec_timestamp
                    
                    	Timestamp for entry in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC, January 1, 1970
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: idb_interface_name
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: mac_address
                    
                    	MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    	**config**\: False
                    
                    .. attribute:: status
                    
                    	Resolution status
                    	**type**\:  :py:class:`ArpResolutionHistoryStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpResolutionHistoryStatus>`
                    
                    	**config**\: False
                    
                    .. attribute:: client_id
                    
                    	Resolving Client ID
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: entry_state
                    
                    	ARP entry state
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: resolution_request_count
                    
                    	Resolution Request count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Arp.Nodes.Node.ResolutionHistoryDynamic.ArpEntry, self).__init__()

                        self.yang_name = "arp-entry"
                        self.yang_parent_name = "resolution-history-dynamic"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('nsec_timestamp', (YLeaf(YType.uint64, 'nsec-timestamp'), ['int'])),
                            ('idb_interface_name', (YLeaf(YType.str, 'idb-interface-name'), ['str'])),
                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper', 'ArpResolutionHistoryStatus', '')])),
                            ('client_id', (YLeaf(YType.int32, 'client-id'), ['int'])),
                            ('entry_state', (YLeaf(YType.int32, 'entry-state'), ['int'])),
                            ('resolution_request_count', (YLeaf(YType.uint32, 'resolution-request-count'), ['int'])),
                        ])
                        self.nsec_timestamp = None
                        self.idb_interface_name = None
                        self.ipv4_address = None
                        self.mac_address = None
                        self.status = None
                        self.client_id = None
                        self.entry_state = None
                        self.resolution_request_count = None
                        self._segment_path = lambda: "arp-entry"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Arp.Nodes.Node.ResolutionHistoryDynamic.ArpEntry, ['nsec_timestamp', 'idb_interface_name', 'ipv4_address', 'mac_address', 'status', 'client_id', 'entry_state', 'resolution_request_count'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                        return meta._meta_table['Arp.Nodes.Node.ResolutionHistoryDynamic.ArpEntry']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['Arp.Nodes.Node.ResolutionHistoryDynamic']['meta_info']


            class ArpStatusInfo(_Entity_):
                """
                Per node ARP status information
                
                .. attribute:: process_start_time
                
                	Timestamp for the process start time in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC , January 1, 1970
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: nanosecond
                
                .. attribute:: issu_sync_complete_time
                
                	Timestamp for the ISSU sync complete in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC , January 1, 1970
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: nanosecond
                
                .. attribute:: issu_ready_time
                
                	Timestamp for the ISSU ready declaration in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC , January 1, 1970
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: nanosecond
                
                .. attribute:: big_bang_time
                
                	Timestamp for the Big Bang notification time in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC , January 1, 1970
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: nanosecond
                
                .. attribute:: primary_role_time
                
                	Timestamp for the change to Primary role notification time in nanoseconds since Epoch, i .e. since 00\:00\:00 UTC, January 1, 1970
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: nanosecond
                
                .. attribute:: role
                
                	The current role of the ARP process
                	**type**\:  :py:class:`ArpIssuRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpIssuRole>`
                
                	**config**\: False
                
                .. attribute:: phase
                
                	The current ISSU phase of the ARP process
                	**type**\:  :py:class:`ArpIssuPhase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpIssuPhase>`
                
                	**config**\: False
                
                .. attribute:: version
                
                	The current version of the ARP process in the context of an ISSU
                	**type**\:  :py:class:`ArpIssuVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpIssuVersion>`
                
                	**config**\: False
                
                .. attribute:: dynamic_entries_recovered_count
                
                	The number of entries that have been recovered during ISSU V1 and V2 synchronisation
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: non_operational_entries_count
                
                	The number of entries that are currently non\-operational in the shadow database
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: interface_handle_translation_failure_count
                
                	The number of interface handle translation failures that occurred during the ISSU V1 and V2 synchronisation
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: issu_ready_issu_mgr_connection
                
                	Whether or not ARP is currently connected to ISSU Manager during the ISSU Load Phase
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: issu_ready_im
                
                	Whether or not ARP is in sync with IM during the ISSU Load Phase
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: issu_ready_dagr_rib
                
                	Whether or not the ARP DAGR system is in sync with the RIB during the ISSU Load Phase
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: issu_ready_entries_replicate
                
                	Whether or not ARP has received all replicated entries during the ISSU Load Phase
                	**type**\: bool
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Arp.Nodes.Node.ArpStatusInfo, self).__init__()

                    self.yang_name = "arp-status-info"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('process_start_time', (YLeaf(YType.uint64, 'process-start-time'), ['int'])),
                        ('issu_sync_complete_time', (YLeaf(YType.uint64, 'issu-sync-complete-time'), ['int'])),
                        ('issu_ready_time', (YLeaf(YType.uint64, 'issu-ready-time'), ['int'])),
                        ('big_bang_time', (YLeaf(YType.uint64, 'big-bang-time'), ['int'])),
                        ('primary_role_time', (YLeaf(YType.uint64, 'primary-role-time'), ['int'])),
                        ('role', (YLeaf(YType.enumeration, 'role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper', 'ArpIssuRole', '')])),
                        ('phase', (YLeaf(YType.enumeration, 'phase'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper', 'ArpIssuPhase', '')])),
                        ('version', (YLeaf(YType.enumeration, 'version'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper', 'ArpIssuVersion', '')])),
                        ('dynamic_entries_recovered_count', (YLeaf(YType.uint32, 'dynamic-entries-recovered-count'), ['int'])),
                        ('non_operational_entries_count', (YLeaf(YType.uint32, 'non-operational-entries-count'), ['int'])),
                        ('interface_handle_translation_failure_count', (YLeaf(YType.uint32, 'interface-handle-translation-failure-count'), ['int'])),
                        ('issu_ready_issu_mgr_connection', (YLeaf(YType.boolean, 'issu-ready-issu-mgr-connection'), ['bool'])),
                        ('issu_ready_im', (YLeaf(YType.boolean, 'issu-ready-im'), ['bool'])),
                        ('issu_ready_dagr_rib', (YLeaf(YType.boolean, 'issu-ready-dagr-rib'), ['bool'])),
                        ('issu_ready_entries_replicate', (YLeaf(YType.boolean, 'issu-ready-entries-replicate'), ['bool'])),
                    ])
                    self.process_start_time = None
                    self.issu_sync_complete_time = None
                    self.issu_ready_time = None
                    self.big_bang_time = None
                    self.primary_role_time = None
                    self.role = None
                    self.phase = None
                    self.version = None
                    self.dynamic_entries_recovered_count = None
                    self.non_operational_entries_count = None
                    self.interface_handle_translation_failure_count = None
                    self.issu_ready_issu_mgr_connection = None
                    self.issu_ready_im = None
                    self.issu_ready_dagr_rib = None
                    self.issu_ready_entries_replicate = None
                    self._segment_path = lambda: "arp-status-info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Arp.Nodes.Node.ArpStatusInfo, ['process_start_time', 'issu_sync_complete_time', 'issu_ready_time', 'big_bang_time', 'primary_role_time', 'role', 'phase', 'version', 'dynamic_entries_recovered_count', 'non_operational_entries_count', 'interface_handle_translation_failure_count', 'issu_ready_issu_mgr_connection', 'issu_ready_im', 'issu_ready_dagr_rib', 'issu_ready_entries_replicate'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['Arp.Nodes.Node.ArpStatusInfo']['meta_info']


            class TrafficVrfs(_Entity_):
                """
                ARP Traffic information per VRF
                
                .. attribute:: traffic_vrf
                
                	Per VRF traffic data
                	**type**\: list of  		 :py:class:`TrafficVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.TrafficVrfs.TrafficVrf>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Arp.Nodes.Node.TrafficVrfs, self).__init__()

                    self.yang_name = "traffic-vrfs"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("traffic-vrf", ("traffic_vrf", Arp.Nodes.Node.TrafficVrfs.TrafficVrf))])
                    self._leafs = OrderedDict()

                    self.traffic_vrf = YList(self)
                    self._segment_path = lambda: "traffic-vrfs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Arp.Nodes.Node.TrafficVrfs, [], name, value)


                class TrafficVrf(_Entity_):
                    """
                    Per VRF traffic data
                    
                    .. attribute:: vrf_name  (key)
                    
                    	VRF name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: requests_received
                    
                    	Total ARP requests received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: replies_received
                    
                    	Total ARP replies received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: requests_sent
                    
                    	Total ARP requests sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: replies_sent
                    
                    	Total ARP replies sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: proxy_replies_sent
                    
                    	Total Proxy ARP replies sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: subscr_requests_received
                    
                    	Total ARP requests received over subscriber interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: subscr_replies_sent
                    
                    	Total ARP replies sent over subscriber interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: subscr_replies_gratg_sent
                    
                    	Total ARP grat replies sent over subscriber interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: local_proxy_replies_sent
                    
                    	Total Local Proxy ARP replies sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: gratuitous_replies_sent
                    
                    	Total Gratuituous ARP replies sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: resolution_requests_received
                    
                    	Total ARP resolution requests received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: resolution_replies_received
                    
                    	Total ARP resolution replies received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: resolution_requests_dropped
                    
                    	total ARP resolution requests dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: out_of_memory_errors
                    
                    	Total errors for out of memory
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: no_buffer_errors
                    
                    	Total errors for no buffer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: total_entries
                    
                    	Total ARP entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dynamic_entries
                    
                    	Total dynamic entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: static_entries
                    
                    	Total static entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: alias_entries
                    
                    	Total alias entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: interface_entries
                    
                    	Total interface entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: standby_entries
                    
                    	Total standby entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dhcp_entries
                    
                    	Total DHCP entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: vxlan_entries
                    
                    	Total VXLAN entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: drop_adjacency_entries
                    
                    	Total drop adjacency entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ip_packets_dropped_node
                    
                    	Total ip packets droped on this node
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: arp_packet_node_out_of_subnet
                    
                    	Total ARP packets on node due to out of subnet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ip_packets_dropped_interface
                    
                    	Total ip packets droped on this interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: arp_packet_interface_out_of_subnet
                    
                    	Total arp packets on interface due to out of subnet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: arp_packet_unsolicited_packet
                    
                    	Total unsolicited arp packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: idb_structures
                    
                    	Total idb structures on this node
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Arp.Nodes.Node.TrafficVrfs.TrafficVrf, self).__init__()

                        self.yang_name = "traffic-vrf"
                        self.yang_parent_name = "traffic-vrfs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['vrf_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('requests_received', (YLeaf(YType.uint32, 'requests-received'), ['int'])),
                            ('replies_received', (YLeaf(YType.uint32, 'replies-received'), ['int'])),
                            ('requests_sent', (YLeaf(YType.uint32, 'requests-sent'), ['int'])),
                            ('replies_sent', (YLeaf(YType.uint32, 'replies-sent'), ['int'])),
                            ('proxy_replies_sent', (YLeaf(YType.uint32, 'proxy-replies-sent'), ['int'])),
                            ('subscr_requests_received', (YLeaf(YType.uint32, 'subscr-requests-received'), ['int'])),
                            ('subscr_replies_sent', (YLeaf(YType.uint32, 'subscr-replies-sent'), ['int'])),
                            ('subscr_replies_gratg_sent', (YLeaf(YType.uint32, 'subscr-replies-gratg-sent'), ['int'])),
                            ('local_proxy_replies_sent', (YLeaf(YType.uint32, 'local-proxy-replies-sent'), ['int'])),
                            ('gratuitous_replies_sent', (YLeaf(YType.uint32, 'gratuitous-replies-sent'), ['int'])),
                            ('resolution_requests_received', (YLeaf(YType.uint32, 'resolution-requests-received'), ['int'])),
                            ('resolution_replies_received', (YLeaf(YType.uint32, 'resolution-replies-received'), ['int'])),
                            ('resolution_requests_dropped', (YLeaf(YType.uint32, 'resolution-requests-dropped'), ['int'])),
                            ('out_of_memory_errors', (YLeaf(YType.uint32, 'out-of-memory-errors'), ['int'])),
                            ('no_buffer_errors', (YLeaf(YType.uint32, 'no-buffer-errors'), ['int'])),
                            ('total_entries', (YLeaf(YType.uint32, 'total-entries'), ['int'])),
                            ('dynamic_entries', (YLeaf(YType.uint32, 'dynamic-entries'), ['int'])),
                            ('static_entries', (YLeaf(YType.uint32, 'static-entries'), ['int'])),
                            ('alias_entries', (YLeaf(YType.uint32, 'alias-entries'), ['int'])),
                            ('interface_entries', (YLeaf(YType.uint32, 'interface-entries'), ['int'])),
                            ('standby_entries', (YLeaf(YType.uint32, 'standby-entries'), ['int'])),
                            ('dhcp_entries', (YLeaf(YType.uint32, 'dhcp-entries'), ['int'])),
                            ('vxlan_entries', (YLeaf(YType.uint32, 'vxlan-entries'), ['int'])),
                            ('drop_adjacency_entries', (YLeaf(YType.uint32, 'drop-adjacency-entries'), ['int'])),
                            ('ip_packets_dropped_node', (YLeaf(YType.uint32, 'ip-packets-dropped-node'), ['int'])),
                            ('arp_packet_node_out_of_subnet', (YLeaf(YType.uint32, 'arp-packet-node-out-of-subnet'), ['int'])),
                            ('ip_packets_dropped_interface', (YLeaf(YType.uint32, 'ip-packets-dropped-interface'), ['int'])),
                            ('arp_packet_interface_out_of_subnet', (YLeaf(YType.uint32, 'arp-packet-interface-out-of-subnet'), ['int'])),
                            ('arp_packet_unsolicited_packet', (YLeaf(YType.uint32, 'arp-packet-unsolicited-packet'), ['int'])),
                            ('idb_structures', (YLeaf(YType.uint32, 'idb-structures'), ['int'])),
                        ])
                        self.vrf_name = None
                        self.requests_received = None
                        self.replies_received = None
                        self.requests_sent = None
                        self.replies_sent = None
                        self.proxy_replies_sent = None
                        self.subscr_requests_received = None
                        self.subscr_replies_sent = None
                        self.subscr_replies_gratg_sent = None
                        self.local_proxy_replies_sent = None
                        self.gratuitous_replies_sent = None
                        self.resolution_requests_received = None
                        self.resolution_replies_received = None
                        self.resolution_requests_dropped = None
                        self.out_of_memory_errors = None
                        self.no_buffer_errors = None
                        self.total_entries = None
                        self.dynamic_entries = None
                        self.static_entries = None
                        self.alias_entries = None
                        self.interface_entries = None
                        self.standby_entries = None
                        self.dhcp_entries = None
                        self.vxlan_entries = None
                        self.drop_adjacency_entries = None
                        self.ip_packets_dropped_node = None
                        self.arp_packet_node_out_of_subnet = None
                        self.ip_packets_dropped_interface = None
                        self.arp_packet_interface_out_of_subnet = None
                        self.arp_packet_unsolicited_packet = None
                        self.idb_structures = None
                        self._segment_path = lambda: "traffic-vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Arp.Nodes.Node.TrafficVrfs.TrafficVrf, ['vrf_name', 'requests_received', 'replies_received', 'requests_sent', 'replies_sent', 'proxy_replies_sent', 'subscr_requests_received', 'subscr_replies_sent', 'subscr_replies_gratg_sent', 'local_proxy_replies_sent', 'gratuitous_replies_sent', 'resolution_requests_received', 'resolution_replies_received', 'resolution_requests_dropped', 'out_of_memory_errors', 'no_buffer_errors', 'total_entries', 'dynamic_entries', 'static_entries', 'alias_entries', 'interface_entries', 'standby_entries', 'dhcp_entries', 'vxlan_entries', 'drop_adjacency_entries', 'ip_packets_dropped_node', 'arp_packet_node_out_of_subnet', 'ip_packets_dropped_interface', 'arp_packet_interface_out_of_subnet', 'arp_packet_unsolicited_packet', 'idb_structures'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                        return meta._meta_table['Arp.Nodes.Node.TrafficVrfs.TrafficVrf']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['Arp.Nodes.Node.TrafficVrfs']['meta_info']


            class TrafficNode(_Entity_):
                """
                Per node ARP Traffic data
                
                .. attribute:: requests_received
                
                	Total ARP requests received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: replies_received
                
                	Total ARP replies received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: requests_sent
                
                	Total ARP requests sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: replies_sent
                
                	Total ARP replies sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: proxy_replies_sent
                
                	Total Proxy ARP replies sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: subscr_requests_received
                
                	Total ARP requests received over subscriber interface
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: subscr_replies_sent
                
                	Total ARP replies sent over subscriber interface
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: subscr_replies_gratg_sent
                
                	Total ARP grat replies sent over subscriber interface
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: local_proxy_replies_sent
                
                	Total Local Proxy ARP replies sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: gratuitous_replies_sent
                
                	Total Gratuituous ARP replies sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: resolution_requests_received
                
                	Total ARP resolution requests received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: resolution_replies_received
                
                	Total ARP resolution replies received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: resolution_requests_dropped
                
                	total ARP resolution requests dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: out_of_memory_errors
                
                	Total errors for out of memory
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: no_buffer_errors
                
                	Total errors for no buffer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: total_entries
                
                	Total ARP entries in the cache
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: dynamic_entries
                
                	Total dynamic entries in the cache
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: static_entries
                
                	Total static entries in the cache
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: alias_entries
                
                	Total alias entries in the cache
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: interface_entries
                
                	Total interface entries in the cache
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: standby_entries
                
                	Total standby entries in the cache
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: dhcp_entries
                
                	Total DHCP entries in the cache
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: vxlan_entries
                
                	Total VXLAN entries in the cache
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: drop_adjacency_entries
                
                	Total drop adjacency entries in the cache
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: ip_packets_dropped_node
                
                	Total ip packets droped on this node
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: arp_packet_node_out_of_subnet
                
                	Total ARP packets on node due to out of subnet
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: ip_packets_dropped_interface
                
                	Total ip packets droped on this interface
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: arp_packet_interface_out_of_subnet
                
                	Total arp packets on interface due to out of subnet
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: arp_packet_unsolicited_packet
                
                	Total unsolicited arp packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: idb_structures
                
                	Total idb structures on this node
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Arp.Nodes.Node.TrafficNode, self).__init__()

                    self.yang_name = "traffic-node"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('requests_received', (YLeaf(YType.uint32, 'requests-received'), ['int'])),
                        ('replies_received', (YLeaf(YType.uint32, 'replies-received'), ['int'])),
                        ('requests_sent', (YLeaf(YType.uint32, 'requests-sent'), ['int'])),
                        ('replies_sent', (YLeaf(YType.uint32, 'replies-sent'), ['int'])),
                        ('proxy_replies_sent', (YLeaf(YType.uint32, 'proxy-replies-sent'), ['int'])),
                        ('subscr_requests_received', (YLeaf(YType.uint32, 'subscr-requests-received'), ['int'])),
                        ('subscr_replies_sent', (YLeaf(YType.uint32, 'subscr-replies-sent'), ['int'])),
                        ('subscr_replies_gratg_sent', (YLeaf(YType.uint32, 'subscr-replies-gratg-sent'), ['int'])),
                        ('local_proxy_replies_sent', (YLeaf(YType.uint32, 'local-proxy-replies-sent'), ['int'])),
                        ('gratuitous_replies_sent', (YLeaf(YType.uint32, 'gratuitous-replies-sent'), ['int'])),
                        ('resolution_requests_received', (YLeaf(YType.uint32, 'resolution-requests-received'), ['int'])),
                        ('resolution_replies_received', (YLeaf(YType.uint32, 'resolution-replies-received'), ['int'])),
                        ('resolution_requests_dropped', (YLeaf(YType.uint32, 'resolution-requests-dropped'), ['int'])),
                        ('out_of_memory_errors', (YLeaf(YType.uint32, 'out-of-memory-errors'), ['int'])),
                        ('no_buffer_errors', (YLeaf(YType.uint32, 'no-buffer-errors'), ['int'])),
                        ('total_entries', (YLeaf(YType.uint32, 'total-entries'), ['int'])),
                        ('dynamic_entries', (YLeaf(YType.uint32, 'dynamic-entries'), ['int'])),
                        ('static_entries', (YLeaf(YType.uint32, 'static-entries'), ['int'])),
                        ('alias_entries', (YLeaf(YType.uint32, 'alias-entries'), ['int'])),
                        ('interface_entries', (YLeaf(YType.uint32, 'interface-entries'), ['int'])),
                        ('standby_entries', (YLeaf(YType.uint32, 'standby-entries'), ['int'])),
                        ('dhcp_entries', (YLeaf(YType.uint32, 'dhcp-entries'), ['int'])),
                        ('vxlan_entries', (YLeaf(YType.uint32, 'vxlan-entries'), ['int'])),
                        ('drop_adjacency_entries', (YLeaf(YType.uint32, 'drop-adjacency-entries'), ['int'])),
                        ('ip_packets_dropped_node', (YLeaf(YType.uint32, 'ip-packets-dropped-node'), ['int'])),
                        ('arp_packet_node_out_of_subnet', (YLeaf(YType.uint32, 'arp-packet-node-out-of-subnet'), ['int'])),
                        ('ip_packets_dropped_interface', (YLeaf(YType.uint32, 'ip-packets-dropped-interface'), ['int'])),
                        ('arp_packet_interface_out_of_subnet', (YLeaf(YType.uint32, 'arp-packet-interface-out-of-subnet'), ['int'])),
                        ('arp_packet_unsolicited_packet', (YLeaf(YType.uint32, 'arp-packet-unsolicited-packet'), ['int'])),
                        ('idb_structures', (YLeaf(YType.uint32, 'idb-structures'), ['int'])),
                    ])
                    self.requests_received = None
                    self.replies_received = None
                    self.requests_sent = None
                    self.replies_sent = None
                    self.proxy_replies_sent = None
                    self.subscr_requests_received = None
                    self.subscr_replies_sent = None
                    self.subscr_replies_gratg_sent = None
                    self.local_proxy_replies_sent = None
                    self.gratuitous_replies_sent = None
                    self.resolution_requests_received = None
                    self.resolution_replies_received = None
                    self.resolution_requests_dropped = None
                    self.out_of_memory_errors = None
                    self.no_buffer_errors = None
                    self.total_entries = None
                    self.dynamic_entries = None
                    self.static_entries = None
                    self.alias_entries = None
                    self.interface_entries = None
                    self.standby_entries = None
                    self.dhcp_entries = None
                    self.vxlan_entries = None
                    self.drop_adjacency_entries = None
                    self.ip_packets_dropped_node = None
                    self.arp_packet_node_out_of_subnet = None
                    self.ip_packets_dropped_interface = None
                    self.arp_packet_interface_out_of_subnet = None
                    self.arp_packet_unsolicited_packet = None
                    self.idb_structures = None
                    self._segment_path = lambda: "traffic-node"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Arp.Nodes.Node.TrafficNode, ['requests_received', 'replies_received', 'requests_sent', 'replies_sent', 'proxy_replies_sent', 'subscr_requests_received', 'subscr_replies_sent', 'subscr_replies_gratg_sent', 'local_proxy_replies_sent', 'gratuitous_replies_sent', 'resolution_requests_received', 'resolution_replies_received', 'resolution_requests_dropped', 'out_of_memory_errors', 'no_buffer_errors', 'total_entries', 'dynamic_entries', 'static_entries', 'alias_entries', 'interface_entries', 'standby_entries', 'dhcp_entries', 'vxlan_entries', 'drop_adjacency_entries', 'ip_packets_dropped_node', 'arp_packet_node_out_of_subnet', 'ip_packets_dropped_interface', 'arp_packet_interface_out_of_subnet', 'arp_packet_unsolicited_packet', 'idb_structures'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['Arp.Nodes.Node.TrafficNode']['meta_info']


            class ResolutionHistoryClient(_Entity_):
                """
                Per node client\-installed ARP resolution
                history data
                
                .. attribute:: arp_entry
                
                	Resolution history array
                	**type**\: list of  		 :py:class:`ArpEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.ResolutionHistoryClient.ArpEntry>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Arp.Nodes.Node.ResolutionHistoryClient, self).__init__()

                    self.yang_name = "resolution-history-client"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("arp-entry", ("arp_entry", Arp.Nodes.Node.ResolutionHistoryClient.ArpEntry))])
                    self._leafs = OrderedDict()

                    self.arp_entry = YList(self)
                    self._segment_path = lambda: "resolution-history-client"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Arp.Nodes.Node.ResolutionHistoryClient, [], name, value)


                class ArpEntry(_Entity_):
                    """
                    Resolution history array
                    
                    .. attribute:: nsec_timestamp
                    
                    	Timestamp for entry in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC, January 1, 1970
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: idb_interface_name
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: mac_address
                    
                    	MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    	**config**\: False
                    
                    .. attribute:: status
                    
                    	Resolution status
                    	**type**\:  :py:class:`ArpResolutionHistoryStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpResolutionHistoryStatus>`
                    
                    	**config**\: False
                    
                    .. attribute:: client_id
                    
                    	Resolving Client ID
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: entry_state
                    
                    	ARP entry state
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: resolution_request_count
                    
                    	Resolution Request count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Arp.Nodes.Node.ResolutionHistoryClient.ArpEntry, self).__init__()

                        self.yang_name = "arp-entry"
                        self.yang_parent_name = "resolution-history-client"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('nsec_timestamp', (YLeaf(YType.uint64, 'nsec-timestamp'), ['int'])),
                            ('idb_interface_name', (YLeaf(YType.str, 'idb-interface-name'), ['str'])),
                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper', 'ArpResolutionHistoryStatus', '')])),
                            ('client_id', (YLeaf(YType.int32, 'client-id'), ['int'])),
                            ('entry_state', (YLeaf(YType.int32, 'entry-state'), ['int'])),
                            ('resolution_request_count', (YLeaf(YType.uint32, 'resolution-request-count'), ['int'])),
                        ])
                        self.nsec_timestamp = None
                        self.idb_interface_name = None
                        self.ipv4_address = None
                        self.mac_address = None
                        self.status = None
                        self.client_id = None
                        self.entry_state = None
                        self.resolution_request_count = None
                        self._segment_path = lambda: "arp-entry"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Arp.Nodes.Node.ResolutionHistoryClient.ArpEntry, ['nsec_timestamp', 'idb_interface_name', 'ipv4_address', 'mac_address', 'status', 'client_id', 'entry_state', 'resolution_request_count'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                        return meta._meta_table['Arp.Nodes.Node.ResolutionHistoryClient.ArpEntry']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['Arp.Nodes.Node.ResolutionHistoryClient']['meta_info']


            class Entries(_Entity_):
                """
                Table of ARP entries
                
                .. attribute:: entry
                
                	ARP entry
                	**type**\: list of  		 :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.Entries.Entry>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Arp.Nodes.Node.Entries, self).__init__()

                    self.yang_name = "entries"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("entry", ("entry", Arp.Nodes.Node.Entries.Entry))])
                    self._leafs = OrderedDict()

                    self.entry = YList(self)
                    self._segment_path = lambda: "entries"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Arp.Nodes.Node.Entries, [], name, value)


                class Entry(_Entity_):
                    """
                    ARP entry
                    
                    .. attribute:: address  (key)
                    
                    	IP Address of ARP entry
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: media_type
                    
                    	Media type for this entry
                    	**type**\:  :py:class:`IpArpBagMedia <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.IpArpBagMedia>`
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	State of this entry
                    	**type**\:  :py:class:`IpArpBagState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.IpArpBagState>`
                    
                    	**config**\: False
                    
                    .. attribute:: flag
                    
                    	Flags of this entry
                    	**type**\:  :py:class:`IpArpBagFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.IpArpBagFlags>`
                    
                    	**config**\: False
                    
                    .. attribute:: age
                    
                    	Age of this entry
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: encapsulation_type
                    
                    	Source encapsulation type
                    	**type**\:  :py:class:`IpArpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.IpArpBagEncap>`
                    
                    	**config**\: False
                    
                    .. attribute:: hardware_length
                    
                    	Source hardware length
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: hardware_address
                    
                    	Hardware address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Arp.Nodes.Node.Entries.Entry, self).__init__()

                        self.yang_name = "entry"
                        self.yang_parent_name = "entries"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['address','interface_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('media_type', (YLeaf(YType.enumeration, 'media-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper', 'IpArpBagMedia', '')])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper', 'IpArpBagState', '')])),
                            ('flag', (YLeaf(YType.enumeration, 'flag'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper', 'IpArpBagFlags', '')])),
                            ('age', (YLeaf(YType.uint64, 'age'), ['int'])),
                            ('encapsulation_type', (YLeaf(YType.enumeration, 'encapsulation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper', 'IpArpBagEncap', '')])),
                            ('hardware_length', (YLeaf(YType.uint8, 'hardware-length'), ['int'])),
                            ('hardware_address', (YLeaf(YType.str, 'hardware-address'), ['str'])),
                        ])
                        self.address = None
                        self.interface_name = None
                        self.media_type = None
                        self.state = None
                        self.flag = None
                        self.age = None
                        self.encapsulation_type = None
                        self.hardware_length = None
                        self.hardware_address = None
                        self._segment_path = lambda: "entry" + "[address='" + str(self.address) + "']" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Arp.Nodes.Node.Entries.Entry, ['address', 'interface_name', 'media_type', 'state', 'flag', 'age', 'encapsulation_type', 'hardware_length', 'hardware_address'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                        return meta._meta_table['Arp.Nodes.Node.Entries.Entry']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['Arp.Nodes.Node.Entries']['meta_info']


            class TrafficInterfaces(_Entity_):
                """
                ARP Traffic information per interface
                
                .. attribute:: traffic_interface
                
                	Per interface traffic data
                	**type**\: list of  		 :py:class:`TrafficInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.TrafficInterfaces.TrafficInterface>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Arp.Nodes.Node.TrafficInterfaces, self).__init__()

                    self.yang_name = "traffic-interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("traffic-interface", ("traffic_interface", Arp.Nodes.Node.TrafficInterfaces.TrafficInterface))])
                    self._leafs = OrderedDict()

                    self.traffic_interface = YList(self)
                    self._segment_path = lambda: "traffic-interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Arp.Nodes.Node.TrafficInterfaces, [], name, value)


                class TrafficInterface(_Entity_):
                    """
                    Per interface traffic data
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: requests_received
                    
                    	Total ARP requests received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: replies_received
                    
                    	Total ARP replies received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: requests_sent
                    
                    	Total ARP requests sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: replies_sent
                    
                    	Total ARP replies sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: proxy_replies_sent
                    
                    	Total Proxy ARP replies sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: subscr_requests_received
                    
                    	Total ARP requests received over subscriber interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: subscr_replies_sent
                    
                    	Total ARP replies sent over subscriber interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: subscr_replies_gratg_sent
                    
                    	Total ARP grat replies sent over subscriber interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: local_proxy_replies_sent
                    
                    	Total Local Proxy ARP replies sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: gratuitous_replies_sent
                    
                    	Total Gratuituous ARP replies sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: resolution_requests_received
                    
                    	Total ARP resolution requests received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: resolution_replies_received
                    
                    	Total ARP resolution replies received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: resolution_requests_dropped
                    
                    	total ARP resolution requests dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: out_of_memory_errors
                    
                    	Total errors for out of memory
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: no_buffer_errors
                    
                    	Total errors for no buffer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: total_entries
                    
                    	Total ARP entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dynamic_entries
                    
                    	Total dynamic entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: static_entries
                    
                    	Total static entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: alias_entries
                    
                    	Total alias entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: interface_entries
                    
                    	Total interface entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: standby_entries
                    
                    	Total standby entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dhcp_entries
                    
                    	Total DHCP entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: vxlan_entries
                    
                    	Total VXLAN entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: drop_adjacency_entries
                    
                    	Total drop adjacency entries in the cache
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ip_packets_dropped_node
                    
                    	Total ip packets droped on this node
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: arp_packet_node_out_of_subnet
                    
                    	Total ARP packets on node due to out of subnet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ip_packets_dropped_interface
                    
                    	Total ip packets droped on this interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: arp_packet_interface_out_of_subnet
                    
                    	Total arp packets on interface due to out of subnet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: arp_packet_unsolicited_packet
                    
                    	Total unsolicited arp packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: idb_structures
                    
                    	Total idb structures on this node
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Arp.Nodes.Node.TrafficInterfaces.TrafficInterface, self).__init__()

                        self.yang_name = "traffic-interface"
                        self.yang_parent_name = "traffic-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('requests_received', (YLeaf(YType.uint32, 'requests-received'), ['int'])),
                            ('replies_received', (YLeaf(YType.uint32, 'replies-received'), ['int'])),
                            ('requests_sent', (YLeaf(YType.uint32, 'requests-sent'), ['int'])),
                            ('replies_sent', (YLeaf(YType.uint32, 'replies-sent'), ['int'])),
                            ('proxy_replies_sent', (YLeaf(YType.uint32, 'proxy-replies-sent'), ['int'])),
                            ('subscr_requests_received', (YLeaf(YType.uint32, 'subscr-requests-received'), ['int'])),
                            ('subscr_replies_sent', (YLeaf(YType.uint32, 'subscr-replies-sent'), ['int'])),
                            ('subscr_replies_gratg_sent', (YLeaf(YType.uint32, 'subscr-replies-gratg-sent'), ['int'])),
                            ('local_proxy_replies_sent', (YLeaf(YType.uint32, 'local-proxy-replies-sent'), ['int'])),
                            ('gratuitous_replies_sent', (YLeaf(YType.uint32, 'gratuitous-replies-sent'), ['int'])),
                            ('resolution_requests_received', (YLeaf(YType.uint32, 'resolution-requests-received'), ['int'])),
                            ('resolution_replies_received', (YLeaf(YType.uint32, 'resolution-replies-received'), ['int'])),
                            ('resolution_requests_dropped', (YLeaf(YType.uint32, 'resolution-requests-dropped'), ['int'])),
                            ('out_of_memory_errors', (YLeaf(YType.uint32, 'out-of-memory-errors'), ['int'])),
                            ('no_buffer_errors', (YLeaf(YType.uint32, 'no-buffer-errors'), ['int'])),
                            ('total_entries', (YLeaf(YType.uint32, 'total-entries'), ['int'])),
                            ('dynamic_entries', (YLeaf(YType.uint32, 'dynamic-entries'), ['int'])),
                            ('static_entries', (YLeaf(YType.uint32, 'static-entries'), ['int'])),
                            ('alias_entries', (YLeaf(YType.uint32, 'alias-entries'), ['int'])),
                            ('interface_entries', (YLeaf(YType.uint32, 'interface-entries'), ['int'])),
                            ('standby_entries', (YLeaf(YType.uint32, 'standby-entries'), ['int'])),
                            ('dhcp_entries', (YLeaf(YType.uint32, 'dhcp-entries'), ['int'])),
                            ('vxlan_entries', (YLeaf(YType.uint32, 'vxlan-entries'), ['int'])),
                            ('drop_adjacency_entries', (YLeaf(YType.uint32, 'drop-adjacency-entries'), ['int'])),
                            ('ip_packets_dropped_node', (YLeaf(YType.uint32, 'ip-packets-dropped-node'), ['int'])),
                            ('arp_packet_node_out_of_subnet', (YLeaf(YType.uint32, 'arp-packet-node-out-of-subnet'), ['int'])),
                            ('ip_packets_dropped_interface', (YLeaf(YType.uint32, 'ip-packets-dropped-interface'), ['int'])),
                            ('arp_packet_interface_out_of_subnet', (YLeaf(YType.uint32, 'arp-packet-interface-out-of-subnet'), ['int'])),
                            ('arp_packet_unsolicited_packet', (YLeaf(YType.uint32, 'arp-packet-unsolicited-packet'), ['int'])),
                            ('idb_structures', (YLeaf(YType.uint32, 'idb-structures'), ['int'])),
                        ])
                        self.interface_name = None
                        self.requests_received = None
                        self.replies_received = None
                        self.requests_sent = None
                        self.replies_sent = None
                        self.proxy_replies_sent = None
                        self.subscr_requests_received = None
                        self.subscr_replies_sent = None
                        self.subscr_replies_gratg_sent = None
                        self.local_proxy_replies_sent = None
                        self.gratuitous_replies_sent = None
                        self.resolution_requests_received = None
                        self.resolution_replies_received = None
                        self.resolution_requests_dropped = None
                        self.out_of_memory_errors = None
                        self.no_buffer_errors = None
                        self.total_entries = None
                        self.dynamic_entries = None
                        self.static_entries = None
                        self.alias_entries = None
                        self.interface_entries = None
                        self.standby_entries = None
                        self.dhcp_entries = None
                        self.vxlan_entries = None
                        self.drop_adjacency_entries = None
                        self.ip_packets_dropped_node = None
                        self.arp_packet_node_out_of_subnet = None
                        self.ip_packets_dropped_interface = None
                        self.arp_packet_interface_out_of_subnet = None
                        self.arp_packet_unsolicited_packet = None
                        self.idb_structures = None
                        self._segment_path = lambda: "traffic-interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Arp.Nodes.Node.TrafficInterfaces.TrafficInterface, ['interface_name', 'requests_received', 'replies_received', 'requests_sent', 'replies_sent', 'proxy_replies_sent', 'subscr_requests_received', 'subscr_replies_sent', 'subscr_replies_gratg_sent', 'local_proxy_replies_sent', 'gratuitous_replies_sent', 'resolution_requests_received', 'resolution_replies_received', 'resolution_requests_dropped', 'out_of_memory_errors', 'no_buffer_errors', 'total_entries', 'dynamic_entries', 'static_entries', 'alias_entries', 'interface_entries', 'standby_entries', 'dhcp_entries', 'vxlan_entries', 'drop_adjacency_entries', 'ip_packets_dropped_node', 'arp_packet_node_out_of_subnet', 'ip_packets_dropped_interface', 'arp_packet_interface_out_of_subnet', 'arp_packet_unsolicited_packet', 'idb_structures'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                        return meta._meta_table['Arp.Nodes.Node.TrafficInterfaces.TrafficInterface']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                    return meta._meta_table['Arp.Nodes.Node.TrafficInterfaces']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
                return meta._meta_table['Arp.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
            return meta._meta_table['Arp.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = Arp()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_arp_oper as meta
        return meta._meta_table['Arp']['meta_info']


