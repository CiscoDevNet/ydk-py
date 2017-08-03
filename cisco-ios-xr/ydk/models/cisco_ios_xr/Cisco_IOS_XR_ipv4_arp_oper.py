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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class ArpGmpBagEncap(Enum):
    """
    ArpGmpBagEncap

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


class ArpGmpBagEntry(Enum):
    """
    ArpGmpBagEntry

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


class ArpResolutionHistoryStatus(Enum):
    """
    ArpResolutionHistoryStatus

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


class IpArpBagEncap(Enum):
    """
    IpArpBagEncap

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


class IpArpBagFlags(Enum):
    """
    IpArpBagFlags

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


class IpArpBagMedia(Enum):
    """
    IpArpBagMedia

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


class IpArpBagState(Enum):
    """
    IpArpBagState

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

    state_max = Enum.YLeaf(16, "state-max")



class ArpGmp(Entity):
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
        super(ArpGmp, self).__init__()
        self._top_entity = None

        self.yang_name = "arp-gmp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-arp-oper"

        self.vrf_infos = ArpGmp.VrfInfos()
        self.vrf_infos.parent = self
        self._children_name_map["vrf_infos"] = "vrf-infos"
        self._children_yang_names.add("vrf-infos")

        self.vrfs = ArpGmp.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")


    class VrfInfos(Entity):
        """
        Table of VRF related ARP\-GMP operational data
        
        .. attribute:: vrf_info
        
        	VRF related ARP\-GMP operational data
        	**type**\: list of    :py:class:`VrfInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.VrfInfos.VrfInfo>`
        
        

        """

        _prefix = 'ipv4-arp-oper'
        _revision = '2016-12-19'

        def __init__(self):
            super(ArpGmp.VrfInfos, self).__init__()

            self.yang_name = "vrf-infos"
            self.yang_parent_name = "arp-gmp"

            self.vrf_info = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ArpGmp.VrfInfos, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ArpGmp.VrfInfos, self).__setattr__(name, value)


        class VrfInfo(Entity):
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
                super(ArpGmp.VrfInfos.VrfInfo, self).__init__()

                self.yang_name = "vrf-info"
                self.yang_parent_name = "vrf-infos"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.rsi_handle = YLeaf(YType.uint32, "rsi-handle")

                self.rsi_handle_high = YLeaf(YType.uint32, "rsi-handle-high")

                self.table_id = YLeaf(YType.uint32, "table-id")

                self.vrf_id_number = YLeaf(YType.uint32, "vrf-id-number")

                self.vrf_name_xr = YLeaf(YType.str, "vrf-name-xr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name",
                                "rsi_handle",
                                "rsi_handle_high",
                                "table_id",
                                "vrf_id_number",
                                "vrf_name_xr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ArpGmp.VrfInfos.VrfInfo, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ArpGmp.VrfInfos.VrfInfo, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    self.rsi_handle.is_set or
                    self.rsi_handle_high.is_set or
                    self.table_id.is_set or
                    self.vrf_id_number.is_set or
                    self.vrf_name_xr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.rsi_handle.yfilter != YFilter.not_set or
                    self.rsi_handle_high.yfilter != YFilter.not_set or
                    self.table_id.yfilter != YFilter.not_set or
                    self.vrf_id_number.yfilter != YFilter.not_set or
                    self.vrf_name_xr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf-info" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-arp-oper:arp-gmp/vrf-infos/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.rsi_handle.is_set or self.rsi_handle.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsi_handle.get_name_leafdata())
                if (self.rsi_handle_high.is_set or self.rsi_handle_high.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsi_handle_high.get_name_leafdata())
                if (self.table_id.is_set or self.table_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.table_id.get_name_leafdata())
                if (self.vrf_id_number.is_set or self.vrf_id_number.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_id_number.get_name_leafdata())
                if (self.vrf_name_xr.is_set or self.vrf_name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name_xr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "vrf-name" or name == "rsi-handle" or name == "rsi-handle-high" or name == "table-id" or name == "vrf-id-number" or name == "vrf-name-xr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "rsi-handle"):
                    self.rsi_handle = value
                    self.rsi_handle.value_namespace = name_space
                    self.rsi_handle.value_namespace_prefix = name_space_prefix
                if(value_path == "rsi-handle-high"):
                    self.rsi_handle_high = value
                    self.rsi_handle_high.value_namespace = name_space
                    self.rsi_handle_high.value_namespace_prefix = name_space_prefix
                if(value_path == "table-id"):
                    self.table_id = value
                    self.table_id.value_namespace = name_space
                    self.table_id.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-id-number"):
                    self.vrf_id_number = value
                    self.vrf_id_number.value_namespace = name_space
                    self.vrf_id_number.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name-xr"):
                    self.vrf_name_xr = value
                    self.vrf_name_xr.value_namespace = name_space
                    self.vrf_name_xr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vrf_info:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vrf_info:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vrf-infos" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-arp-oper:arp-gmp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vrf-info"):
                for c in self.vrf_info:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ArpGmp.VrfInfos.VrfInfo()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vrf_info.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vrf-info"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Vrfs(Entity):
        """
        Table of per VRF ARP\-GMP operational data
        
        .. attribute:: vrf
        
        	Per VRF ARP\-GMP operational data
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-arp-oper'
        _revision = '2016-12-19'

        def __init__(self):
            super(ArpGmp.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "arp-gmp"

            self.vrf = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ArpGmp.Vrfs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ArpGmp.Vrfs, self).__setattr__(name, value)


        class Vrf(Entity):
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
                super(ArpGmp.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.configured_ip_addresses = ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses()
                self.configured_ip_addresses.parent = self
                self._children_name_map["configured_ip_addresses"] = "configured-ip-addresses"
                self._children_yang_names.add("configured-ip-addresses")

                self.interface_configured_ips = ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps()
                self.interface_configured_ips.parent = self
                self._children_name_map["interface_configured_ips"] = "interface-configured-ips"
                self._children_yang_names.add("interface-configured-ips")

                self.routes = ArpGmp.Vrfs.Vrf.Routes()
                self.routes.parent = self
                self._children_name_map["routes"] = "routes"
                self._children_yang_names.add("routes")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ArpGmp.Vrfs.Vrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ArpGmp.Vrfs.Vrf, self).__setattr__(name, value)


            class ConfiguredIpAddresses(Entity):
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
                    super(ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses, self).__init__()

                    self.yang_name = "configured-ip-addresses"
                    self.yang_parent_name = "vrf"

                    self.configured_ip_address = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses, self).__setattr__(name, value)


                class ConfiguredIpAddress(Entity):
                    """
                    ARP\-GMP configured IP address information
                    
                    .. attribute:: address  <key>
                    
                    	Configured ARP\-GMP IP
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: encapsulation_type
                    
                    	Encap type
                    	**type**\:   :py:class:`ArpGmpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmpBagEncap>`
                    
                    .. attribute:: entry_type
                    
                    	Entry type static/alias
                    	**type**\:   :py:class:`ArpGmpBagEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmpBagEntry>`
                    
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
                        super(ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses.ConfiguredIpAddress, self).__init__()

                        self.yang_name = "configured-ip-address"
                        self.yang_parent_name = "configured-ip-addresses"

                        self.address = YLeaf(YType.str, "address")

                        self.encapsulation_type = YLeaf(YType.enumeration, "encapsulation-type")

                        self.entry_type = YLeaf(YType.enumeration, "entry-type")

                        self.hardware_address = YLeaf(YType.str, "hardware-address")

                        self.ip_address = YLeaf(YType.str, "ip-address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address",
                                        "encapsulation_type",
                                        "entry_type",
                                        "hardware_address",
                                        "ip_address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses.ConfiguredIpAddress, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses.ConfiguredIpAddress, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.address.is_set or
                            self.encapsulation_type.is_set or
                            self.entry_type.is_set or
                            self.hardware_address.is_set or
                            self.ip_address.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.encapsulation_type.yfilter != YFilter.not_set or
                            self.entry_type.yfilter != YFilter.not_set or
                            self.hardware_address.yfilter != YFilter.not_set or
                            self.ip_address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "configured-ip-address" + "[address='" + self.address.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())
                        if (self.encapsulation_type.is_set or self.encapsulation_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.encapsulation_type.get_name_leafdata())
                        if (self.entry_type.is_set or self.entry_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.entry_type.get_name_leafdata())
                        if (self.hardware_address.is_set or self.hardware_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hardware_address.get_name_leafdata())
                        if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "encapsulation-type" or name == "entry-type" or name == "hardware-address" or name == "ip-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "encapsulation-type"):
                            self.encapsulation_type = value
                            self.encapsulation_type.value_namespace = name_space
                            self.encapsulation_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "entry-type"):
                            self.entry_type = value
                            self.entry_type.value_namespace = name_space
                            self.entry_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "hardware-address"):
                            self.hardware_address = value
                            self.hardware_address.value_namespace = name_space
                            self.hardware_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "ip-address"):
                            self.ip_address = value
                            self.ip_address.value_namespace = name_space
                            self.ip_address.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.configured_ip_address:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.configured_ip_address:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "configured-ip-addresses" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "configured-ip-address"):
                        for c in self.configured_ip_address:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses.ConfiguredIpAddress()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.configured_ip_address.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "configured-ip-address"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Routes(Entity):
                """
                Table of ARP GMP route information
                
                .. attribute:: route
                
                	ARP GMP route information
                	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmp.Vrfs.Vrf.Routes.Route>`
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2016-12-19'

                def __init__(self):
                    super(ArpGmp.Vrfs.Vrf.Routes, self).__init__()

                    self.yang_name = "routes"
                    self.yang_parent_name = "vrf"

                    self.route = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ArpGmp.Vrfs.Vrf.Routes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ArpGmp.Vrfs.Vrf.Routes, self).__setattr__(name, value)


                class Route(Entity):
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
                        super(ArpGmp.Vrfs.Vrf.Routes.Route, self).__init__()

                        self.yang_name = "route"
                        self.yang_parent_name = "routes"

                        self.address = YLeaf(YType.str, "address")

                        self.interface_name = YLeafList(YType.str, "interface-name")

                        self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                        self.ip_address = YLeaf(YType.str, "ip-address")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.prefix_length_xr = YLeaf(YType.uint8, "prefix-length-xr")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address",
                                        "interface_name",
                                        "interface_name_xr",
                                        "ip_address",
                                        "prefix_length",
                                        "prefix_length_xr") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ArpGmp.Vrfs.Vrf.Routes.Route, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ArpGmp.Vrfs.Vrf.Routes.Route, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.interface_name.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return (
                            self.address.is_set or
                            self.interface_name_xr.is_set or
                            self.ip_address.is_set or
                            self.prefix_length.is_set or
                            self.prefix_length_xr.is_set)

                    def has_operation(self):
                        for leaf in self.interface_name.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.interface_name_xr.yfilter != YFilter.not_set or
                            self.ip_address.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set or
                            self.prefix_length_xr.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "route" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())
                        if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name_xr.get_name_leafdata())
                        if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_address.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                        if (self.prefix_length_xr.is_set or self.prefix_length_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length_xr.get_name_leafdata())

                        leaf_name_data.extend(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "interface-name" or name == "interface-name-xr" or name == "ip-address" or name == "prefix-length" or name == "prefix-length-xr"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name.append(value)
                        if(value_path == "interface-name-xr"):
                            self.interface_name_xr = value
                            self.interface_name_xr.value_namespace = name_space
                            self.interface_name_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "ip-address"):
                            self.ip_address = value
                            self.ip_address.value_namespace = name_space
                            self.ip_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length-xr"):
                            self.prefix_length_xr = value
                            self.prefix_length_xr.value_namespace = name_space
                            self.prefix_length_xr.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.route:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.route:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "routes" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "route"):
                        for c in self.route:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ArpGmp.Vrfs.Vrf.Routes.Route()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.route.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "route"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class InterfaceConfiguredIps(Entity):
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
                    super(ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps, self).__init__()

                    self.yang_name = "interface-configured-ips"
                    self.yang_parent_name = "vrf"

                    self.interface_configured_ip = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps, self).__setattr__(name, value)


                class InterfaceConfiguredIp(Entity):
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
                        super(ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp, self).__init__()

                        self.yang_name = "interface-configured-ip"
                        self.yang_parent_name = "interface-configured-ips"

                        self.address = YLeaf(YType.str, "address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                        self.reference_count = YLeaf(YType.uint32, "reference-count")

                        self.associated_configuration_entry = ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry()
                        self.associated_configuration_entry.parent = self
                        self._children_name_map["associated_configuration_entry"] = "associated-configuration-entry"
                        self._children_yang_names.add("associated-configuration-entry")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address",
                                        "interface_name",
                                        "interface_name_xr",
                                        "reference_count") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp, self).__setattr__(name, value)


                    class AssociatedConfigurationEntry(Entity):
                        """
                        Associated configuration entry
                        
                        .. attribute:: encapsulation_type
                        
                        	Encap type
                        	**type**\:   :py:class:`ArpGmpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmpBagEncap>`
                        
                        .. attribute:: entry_type
                        
                        	Entry type static/alias
                        	**type**\:   :py:class:`ArpGmpBagEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpGmpBagEntry>`
                        
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
                            super(ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry, self).__init__()

                            self.yang_name = "associated-configuration-entry"
                            self.yang_parent_name = "interface-configured-ip"

                            self.encapsulation_type = YLeaf(YType.enumeration, "encapsulation-type")

                            self.entry_type = YLeaf(YType.enumeration, "entry-type")

                            self.hardware_address = YLeaf(YType.str, "hardware-address")

                            self.ip_address = YLeaf(YType.str, "ip-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("encapsulation_type",
                                            "entry_type",
                                            "hardware_address",
                                            "ip_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.encapsulation_type.is_set or
                                self.entry_type.is_set or
                                self.hardware_address.is_set or
                                self.ip_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.encapsulation_type.yfilter != YFilter.not_set or
                                self.entry_type.yfilter != YFilter.not_set or
                                self.hardware_address.yfilter != YFilter.not_set or
                                self.ip_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "associated-configuration-entry" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.encapsulation_type.is_set or self.encapsulation_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.encapsulation_type.get_name_leafdata())
                            if (self.entry_type.is_set or self.entry_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.entry_type.get_name_leafdata())
                            if (self.hardware_address.is_set or self.hardware_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hardware_address.get_name_leafdata())
                            if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "encapsulation-type" or name == "entry-type" or name == "hardware-address" or name == "ip-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "encapsulation-type"):
                                self.encapsulation_type = value
                                self.encapsulation_type.value_namespace = name_space
                                self.encapsulation_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "entry-type"):
                                self.entry_type = value
                                self.entry_type.value_namespace = name_space
                                self.entry_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "hardware-address"):
                                self.hardware_address = value
                                self.hardware_address.value_namespace = name_space
                                self.hardware_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-address"):
                                self.ip_address = value
                                self.ip_address.value_namespace = name_space
                                self.ip_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.address.is_set or
                            self.interface_name.is_set or
                            self.interface_name_xr.is_set or
                            self.reference_count.is_set or
                            (self.associated_configuration_entry is not None and self.associated_configuration_entry.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.interface_name_xr.yfilter != YFilter.not_set or
                            self.reference_count.yfilter != YFilter.not_set or
                            (self.associated_configuration_entry is not None and self.associated_configuration_entry.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-configured-ip" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name_xr.get_name_leafdata())
                        if (self.reference_count.is_set or self.reference_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reference_count.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "associated-configuration-entry"):
                            if (self.associated_configuration_entry is None):
                                self.associated_configuration_entry = ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry()
                                self.associated_configuration_entry.parent = self
                                self._children_name_map["associated_configuration_entry"] = "associated-configuration-entry"
                            return self.associated_configuration_entry

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "associated-configuration-entry" or name == "address" or name == "interface-name" or name == "interface-name-xr" or name == "reference-count"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name-xr"):
                            self.interface_name_xr = value
                            self.interface_name_xr.value_namespace = name_space
                            self.interface_name_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "reference-count"):
                            self.reference_count = value
                            self.reference_count.value_namespace = name_space
                            self.reference_count.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface_configured_ip:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface_configured_ip:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface-configured-ips" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interface-configured-ip"):
                        for c in self.interface_configured_ip:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface_configured_ip.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-configured-ip"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    (self.configured_ip_addresses is not None and self.configured_ip_addresses.has_data()) or
                    (self.interface_configured_ips is not None and self.interface_configured_ips.has_data()) or
                    (self.routes is not None and self.routes.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    (self.configured_ip_addresses is not None and self.configured_ip_addresses.has_operation()) or
                    (self.interface_configured_ips is not None and self.interface_configured_ips.has_operation()) or
                    (self.routes is not None and self.routes.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-arp-oper:arp-gmp/vrfs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "configured-ip-addresses"):
                    if (self.configured_ip_addresses is None):
                        self.configured_ip_addresses = ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses()
                        self.configured_ip_addresses.parent = self
                        self._children_name_map["configured_ip_addresses"] = "configured-ip-addresses"
                    return self.configured_ip_addresses

                if (child_yang_name == "interface-configured-ips"):
                    if (self.interface_configured_ips is None):
                        self.interface_configured_ips = ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps()
                        self.interface_configured_ips.parent = self
                        self._children_name_map["interface_configured_ips"] = "interface-configured-ips"
                    return self.interface_configured_ips

                if (child_yang_name == "routes"):
                    if (self.routes is None):
                        self.routes = ArpGmp.Vrfs.Vrf.Routes()
                        self.routes.parent = self
                        self._children_name_map["routes"] = "routes"
                    return self.routes

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "configured-ip-addresses" or name == "interface-configured-ips" or name == "routes" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vrf:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vrf:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vrfs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-arp-oper:arp-gmp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vrf"):
                for c in self.vrf:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ArpGmp.Vrfs.Vrf()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vrf.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vrf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.vrf_infos is not None and self.vrf_infos.has_data()) or
            (self.vrfs is not None and self.vrfs.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.vrf_infos is not None and self.vrf_infos.has_operation()) or
            (self.vrfs is not None and self.vrfs.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-arp-oper:arp-gmp" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "vrf-infos"):
            if (self.vrf_infos is None):
                self.vrf_infos = ArpGmp.VrfInfos()
                self.vrf_infos.parent = self
                self._children_name_map["vrf_infos"] = "vrf-infos"
            return self.vrf_infos

        if (child_yang_name == "vrfs"):
            if (self.vrfs is None):
                self.vrfs = ArpGmp.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
            return self.vrfs

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "vrf-infos" or name == "vrfs"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ArpGmp()
        return self._top_entity

class Arp(Entity):
    """
    arp
    
    .. attribute:: nodes
    
    	Table of per\-node ARP operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes>`
    
    

    """

    _prefix = 'ipv4-arp-oper'
    _revision = '2016-12-19'

    def __init__(self):
        super(Arp, self).__init__()
        self._top_entity = None

        self.yang_name = "arp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-arp-oper"

        self.nodes = Arp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Table of per\-node ARP operational data
        
        .. attribute:: node
        
        	Per\-node ARP operational data
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node>`
        
        

        """

        _prefix = 'ipv4-arp-oper'
        _revision = '2016-12-19'

        def __init__(self):
            super(Arp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "arp"

            self.node = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Arp.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Arp.Nodes, self).__setattr__(name, value)


        class Node(Entity):
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
                super(Arp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.entries = Arp.Nodes.Node.Entries()
                self.entries.parent = self
                self._children_name_map["entries"] = "entries"
                self._children_yang_names.add("entries")

                self.resolution_history_client = Arp.Nodes.Node.ResolutionHistoryClient()
                self.resolution_history_client.parent = self
                self._children_name_map["resolution_history_client"] = "resolution-history-client"
                self._children_yang_names.add("resolution-history-client")

                self.resolution_history_dynamic = Arp.Nodes.Node.ResolutionHistoryDynamic()
                self.resolution_history_dynamic.parent = self
                self._children_name_map["resolution_history_dynamic"] = "resolution-history-dynamic"
                self._children_yang_names.add("resolution-history-dynamic")

                self.traffic_interfaces = Arp.Nodes.Node.TrafficInterfaces()
                self.traffic_interfaces.parent = self
                self._children_name_map["traffic_interfaces"] = "traffic-interfaces"
                self._children_yang_names.add("traffic-interfaces")

                self.traffic_node = Arp.Nodes.Node.TrafficNode()
                self.traffic_node.parent = self
                self._children_name_map["traffic_node"] = "traffic-node"
                self._children_yang_names.add("traffic-node")

                self.traffic_vrfs = Arp.Nodes.Node.TrafficVrfs()
                self.traffic_vrfs.parent = self
                self._children_name_map["traffic_vrfs"] = "traffic-vrfs"
                self._children_yang_names.add("traffic-vrfs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Arp.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Arp.Nodes.Node, self).__setattr__(name, value)


            class ResolutionHistoryDynamic(Entity):
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
                    super(Arp.Nodes.Node.ResolutionHistoryDynamic, self).__init__()

                    self.yang_name = "resolution-history-dynamic"
                    self.yang_parent_name = "node"

                    self.arp_entry = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Arp.Nodes.Node.ResolutionHistoryDynamic, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Arp.Nodes.Node.ResolutionHistoryDynamic, self).__setattr__(name, value)


                class ArpEntry(Entity):
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
                    	**type**\:   :py:class:`ArpResolutionHistoryStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpResolutionHistoryStatus>`
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(Arp.Nodes.Node.ResolutionHistoryDynamic.ArpEntry, self).__init__()

                        self.yang_name = "arp-entry"
                        self.yang_parent_name = "resolution-history-dynamic"

                        self.client_id = YLeaf(YType.int32, "client-id")

                        self.entry_state = YLeaf(YType.int32, "entry-state")

                        self.idb_interface_name = YLeaf(YType.str, "idb-interface-name")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.mac_address = YLeaf(YType.str, "mac-address")

                        self.nsec_timestamp = YLeaf(YType.uint64, "nsec-timestamp")

                        self.resolution_request_count = YLeaf(YType.uint32, "resolution-request-count")

                        self.status = YLeaf(YType.enumeration, "status")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("client_id",
                                        "entry_state",
                                        "idb_interface_name",
                                        "ipv4_address",
                                        "mac_address",
                                        "nsec_timestamp",
                                        "resolution_request_count",
                                        "status") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Arp.Nodes.Node.ResolutionHistoryDynamic.ArpEntry, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Arp.Nodes.Node.ResolutionHistoryDynamic.ArpEntry, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.client_id.is_set or
                            self.entry_state.is_set or
                            self.idb_interface_name.is_set or
                            self.ipv4_address.is_set or
                            self.mac_address.is_set or
                            self.nsec_timestamp.is_set or
                            self.resolution_request_count.is_set or
                            self.status.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.client_id.yfilter != YFilter.not_set or
                            self.entry_state.yfilter != YFilter.not_set or
                            self.idb_interface_name.yfilter != YFilter.not_set or
                            self.ipv4_address.yfilter != YFilter.not_set or
                            self.mac_address.yfilter != YFilter.not_set or
                            self.nsec_timestamp.yfilter != YFilter.not_set or
                            self.resolution_request_count.yfilter != YFilter.not_set or
                            self.status.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "arp-entry" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.client_id.is_set or self.client_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.client_id.get_name_leafdata())
                        if (self.entry_state.is_set or self.entry_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.entry_state.get_name_leafdata())
                        if (self.idb_interface_name.is_set or self.idb_interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.idb_interface_name.get_name_leafdata())
                        if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                        if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mac_address.get_name_leafdata())
                        if (self.nsec_timestamp.is_set or self.nsec_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nsec_timestamp.get_name_leafdata())
                        if (self.resolution_request_count.is_set or self.resolution_request_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resolution_request_count.get_name_leafdata())
                        if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.status.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "client-id" or name == "entry-state" or name == "idb-interface-name" or name == "ipv4-address" or name == "mac-address" or name == "nsec-timestamp" or name == "resolution-request-count" or name == "status"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "client-id"):
                            self.client_id = value
                            self.client_id.value_namespace = name_space
                            self.client_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "entry-state"):
                            self.entry_state = value
                            self.entry_state.value_namespace = name_space
                            self.entry_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "idb-interface-name"):
                            self.idb_interface_name = value
                            self.idb_interface_name.value_namespace = name_space
                            self.idb_interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4-address"):
                            self.ipv4_address = value
                            self.ipv4_address.value_namespace = name_space
                            self.ipv4_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "mac-address"):
                            self.mac_address = value
                            self.mac_address.value_namespace = name_space
                            self.mac_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "nsec-timestamp"):
                            self.nsec_timestamp = value
                            self.nsec_timestamp.value_namespace = name_space
                            self.nsec_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "resolution-request-count"):
                            self.resolution_request_count = value
                            self.resolution_request_count.value_namespace = name_space
                            self.resolution_request_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "status"):
                            self.status = value
                            self.status.value_namespace = name_space
                            self.status.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.arp_entry:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.arp_entry:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "resolution-history-dynamic" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "arp-entry"):
                        for c in self.arp_entry:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Arp.Nodes.Node.ResolutionHistoryDynamic.ArpEntry()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.arp_entry.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "arp-entry"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class TrafficVrfs(Entity):
                """
                ARP Traffic information per VRF
                
                .. attribute:: traffic_vrf
                
                	Per VRF traffic data
                	**type**\: list of    :py:class:`TrafficVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.TrafficVrfs.TrafficVrf>`
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2016-12-19'

                def __init__(self):
                    super(Arp.Nodes.Node.TrafficVrfs, self).__init__()

                    self.yang_name = "traffic-vrfs"
                    self.yang_parent_name = "node"

                    self.traffic_vrf = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Arp.Nodes.Node.TrafficVrfs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Arp.Nodes.Node.TrafficVrfs, self).__setattr__(name, value)


                class TrafficVrf(Entity):
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
                        super(Arp.Nodes.Node.TrafficVrfs.TrafficVrf, self).__init__()

                        self.yang_name = "traffic-vrf"
                        self.yang_parent_name = "traffic-vrfs"

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.alias_entries = YLeaf(YType.uint32, "alias-entries")

                        self.arp_packet_interface_out_of_subnet = YLeaf(YType.uint32, "arp-packet-interface-out-of-subnet")

                        self.arp_packet_node_out_of_subnet = YLeaf(YType.uint32, "arp-packet-node-out-of-subnet")

                        self.dhcp_entries = YLeaf(YType.uint32, "dhcp-entries")

                        self.dynamic_entries = YLeaf(YType.uint32, "dynamic-entries")

                        self.gratuitous_replies_sent = YLeaf(YType.uint32, "gratuitous-replies-sent")

                        self.idb_structures = YLeaf(YType.uint32, "idb-structures")

                        self.interface_entries = YLeaf(YType.uint32, "interface-entries")

                        self.ip_packets_dropped_interface = YLeaf(YType.uint32, "ip-packets-dropped-interface")

                        self.ip_packets_dropped_node = YLeaf(YType.uint32, "ip-packets-dropped-node")

                        self.local_proxy_replies_sent = YLeaf(YType.uint32, "local-proxy-replies-sent")

                        self.no_buffer_errors = YLeaf(YType.uint32, "no-buffer-errors")

                        self.out_of_memory_errors = YLeaf(YType.uint32, "out-of-memory-errors")

                        self.proxy_replies_sent = YLeaf(YType.uint32, "proxy-replies-sent")

                        self.replies_received = YLeaf(YType.uint32, "replies-received")

                        self.replies_sent = YLeaf(YType.uint32, "replies-sent")

                        self.requests_received = YLeaf(YType.uint32, "requests-received")

                        self.requests_sent = YLeaf(YType.uint32, "requests-sent")

                        self.resolution_replies_received = YLeaf(YType.uint32, "resolution-replies-received")

                        self.resolution_requests_dropped = YLeaf(YType.uint32, "resolution-requests-dropped")

                        self.resolution_requests_received = YLeaf(YType.uint32, "resolution-requests-received")

                        self.standby_entries = YLeaf(YType.uint32, "standby-entries")

                        self.static_entries = YLeaf(YType.uint32, "static-entries")

                        self.subscr_replies_gratg_sent = YLeaf(YType.uint32, "subscr-replies-gratg-sent")

                        self.subscr_replies_sent = YLeaf(YType.uint32, "subscr-replies-sent")

                        self.subscr_requests_received = YLeaf(YType.uint32, "subscr-requests-received")

                        self.total_entries = YLeaf(YType.uint32, "total-entries")

                        self.vxlan_entries = YLeaf(YType.uint32, "vxlan-entries")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("vrf_name",
                                        "alias_entries",
                                        "arp_packet_interface_out_of_subnet",
                                        "arp_packet_node_out_of_subnet",
                                        "dhcp_entries",
                                        "dynamic_entries",
                                        "gratuitous_replies_sent",
                                        "idb_structures",
                                        "interface_entries",
                                        "ip_packets_dropped_interface",
                                        "ip_packets_dropped_node",
                                        "local_proxy_replies_sent",
                                        "no_buffer_errors",
                                        "out_of_memory_errors",
                                        "proxy_replies_sent",
                                        "replies_received",
                                        "replies_sent",
                                        "requests_received",
                                        "requests_sent",
                                        "resolution_replies_received",
                                        "resolution_requests_dropped",
                                        "resolution_requests_received",
                                        "standby_entries",
                                        "static_entries",
                                        "subscr_replies_gratg_sent",
                                        "subscr_replies_sent",
                                        "subscr_requests_received",
                                        "total_entries",
                                        "vxlan_entries") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Arp.Nodes.Node.TrafficVrfs.TrafficVrf, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Arp.Nodes.Node.TrafficVrfs.TrafficVrf, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.vrf_name.is_set or
                            self.alias_entries.is_set or
                            self.arp_packet_interface_out_of_subnet.is_set or
                            self.arp_packet_node_out_of_subnet.is_set or
                            self.dhcp_entries.is_set or
                            self.dynamic_entries.is_set or
                            self.gratuitous_replies_sent.is_set or
                            self.idb_structures.is_set or
                            self.interface_entries.is_set or
                            self.ip_packets_dropped_interface.is_set or
                            self.ip_packets_dropped_node.is_set or
                            self.local_proxy_replies_sent.is_set or
                            self.no_buffer_errors.is_set or
                            self.out_of_memory_errors.is_set or
                            self.proxy_replies_sent.is_set or
                            self.replies_received.is_set or
                            self.replies_sent.is_set or
                            self.requests_received.is_set or
                            self.requests_sent.is_set or
                            self.resolution_replies_received.is_set or
                            self.resolution_requests_dropped.is_set or
                            self.resolution_requests_received.is_set or
                            self.standby_entries.is_set or
                            self.static_entries.is_set or
                            self.subscr_replies_gratg_sent.is_set or
                            self.subscr_replies_sent.is_set or
                            self.subscr_requests_received.is_set or
                            self.total_entries.is_set or
                            self.vxlan_entries.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set or
                            self.alias_entries.yfilter != YFilter.not_set or
                            self.arp_packet_interface_out_of_subnet.yfilter != YFilter.not_set or
                            self.arp_packet_node_out_of_subnet.yfilter != YFilter.not_set or
                            self.dhcp_entries.yfilter != YFilter.not_set or
                            self.dynamic_entries.yfilter != YFilter.not_set or
                            self.gratuitous_replies_sent.yfilter != YFilter.not_set or
                            self.idb_structures.yfilter != YFilter.not_set or
                            self.interface_entries.yfilter != YFilter.not_set or
                            self.ip_packets_dropped_interface.yfilter != YFilter.not_set or
                            self.ip_packets_dropped_node.yfilter != YFilter.not_set or
                            self.local_proxy_replies_sent.yfilter != YFilter.not_set or
                            self.no_buffer_errors.yfilter != YFilter.not_set or
                            self.out_of_memory_errors.yfilter != YFilter.not_set or
                            self.proxy_replies_sent.yfilter != YFilter.not_set or
                            self.replies_received.yfilter != YFilter.not_set or
                            self.replies_sent.yfilter != YFilter.not_set or
                            self.requests_received.yfilter != YFilter.not_set or
                            self.requests_sent.yfilter != YFilter.not_set or
                            self.resolution_replies_received.yfilter != YFilter.not_set or
                            self.resolution_requests_dropped.yfilter != YFilter.not_set or
                            self.resolution_requests_received.yfilter != YFilter.not_set or
                            self.standby_entries.yfilter != YFilter.not_set or
                            self.static_entries.yfilter != YFilter.not_set or
                            self.subscr_replies_gratg_sent.yfilter != YFilter.not_set or
                            self.subscr_replies_sent.yfilter != YFilter.not_set or
                            self.subscr_requests_received.yfilter != YFilter.not_set or
                            self.total_entries.yfilter != YFilter.not_set or
                            self.vxlan_entries.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "traffic-vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())
                        if (self.alias_entries.is_set or self.alias_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.alias_entries.get_name_leafdata())
                        if (self.arp_packet_interface_out_of_subnet.is_set or self.arp_packet_interface_out_of_subnet.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.arp_packet_interface_out_of_subnet.get_name_leafdata())
                        if (self.arp_packet_node_out_of_subnet.is_set or self.arp_packet_node_out_of_subnet.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.arp_packet_node_out_of_subnet.get_name_leafdata())
                        if (self.dhcp_entries.is_set or self.dhcp_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dhcp_entries.get_name_leafdata())
                        if (self.dynamic_entries.is_set or self.dynamic_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dynamic_entries.get_name_leafdata())
                        if (self.gratuitous_replies_sent.is_set or self.gratuitous_replies_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.gratuitous_replies_sent.get_name_leafdata())
                        if (self.idb_structures.is_set or self.idb_structures.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.idb_structures.get_name_leafdata())
                        if (self.interface_entries.is_set or self.interface_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_entries.get_name_leafdata())
                        if (self.ip_packets_dropped_interface.is_set or self.ip_packets_dropped_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_packets_dropped_interface.get_name_leafdata())
                        if (self.ip_packets_dropped_node.is_set or self.ip_packets_dropped_node.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_packets_dropped_node.get_name_leafdata())
                        if (self.local_proxy_replies_sent.is_set or self.local_proxy_replies_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_proxy_replies_sent.get_name_leafdata())
                        if (self.no_buffer_errors.is_set or self.no_buffer_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.no_buffer_errors.get_name_leafdata())
                        if (self.out_of_memory_errors.is_set or self.out_of_memory_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.out_of_memory_errors.get_name_leafdata())
                        if (self.proxy_replies_sent.is_set or self.proxy_replies_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.proxy_replies_sent.get_name_leafdata())
                        if (self.replies_received.is_set or self.replies_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.replies_received.get_name_leafdata())
                        if (self.replies_sent.is_set or self.replies_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.replies_sent.get_name_leafdata())
                        if (self.requests_received.is_set or self.requests_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.requests_received.get_name_leafdata())
                        if (self.requests_sent.is_set or self.requests_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.requests_sent.get_name_leafdata())
                        if (self.resolution_replies_received.is_set or self.resolution_replies_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resolution_replies_received.get_name_leafdata())
                        if (self.resolution_requests_dropped.is_set or self.resolution_requests_dropped.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resolution_requests_dropped.get_name_leafdata())
                        if (self.resolution_requests_received.is_set or self.resolution_requests_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resolution_requests_received.get_name_leafdata())
                        if (self.standby_entries.is_set or self.standby_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.standby_entries.get_name_leafdata())
                        if (self.static_entries.is_set or self.static_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.static_entries.get_name_leafdata())
                        if (self.subscr_replies_gratg_sent.is_set or self.subscr_replies_gratg_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subscr_replies_gratg_sent.get_name_leafdata())
                        if (self.subscr_replies_sent.is_set or self.subscr_replies_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subscr_replies_sent.get_name_leafdata())
                        if (self.subscr_requests_received.is_set or self.subscr_requests_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subscr_requests_received.get_name_leafdata())
                        if (self.total_entries.is_set or self.total_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_entries.get_name_leafdata())
                        if (self.vxlan_entries.is_set or self.vxlan_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vxlan_entries.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "vrf-name" or name == "alias-entries" or name == "arp-packet-interface-out-of-subnet" or name == "arp-packet-node-out-of-subnet" or name == "dhcp-entries" or name == "dynamic-entries" or name == "gratuitous-replies-sent" or name == "idb-structures" or name == "interface-entries" or name == "ip-packets-dropped-interface" or name == "ip-packets-dropped-node" or name == "local-proxy-replies-sent" or name == "no-buffer-errors" or name == "out-of-memory-errors" or name == "proxy-replies-sent" or name == "replies-received" or name == "replies-sent" or name == "requests-received" or name == "requests-sent" or name == "resolution-replies-received" or name == "resolution-requests-dropped" or name == "resolution-requests-received" or name == "standby-entries" or name == "static-entries" or name == "subscr-replies-gratg-sent" or name == "subscr-replies-sent" or name == "subscr-requests-received" or name == "total-entries" or name == "vxlan-entries"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "alias-entries"):
                            self.alias_entries = value
                            self.alias_entries.value_namespace = name_space
                            self.alias_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "arp-packet-interface-out-of-subnet"):
                            self.arp_packet_interface_out_of_subnet = value
                            self.arp_packet_interface_out_of_subnet.value_namespace = name_space
                            self.arp_packet_interface_out_of_subnet.value_namespace_prefix = name_space_prefix
                        if(value_path == "arp-packet-node-out-of-subnet"):
                            self.arp_packet_node_out_of_subnet = value
                            self.arp_packet_node_out_of_subnet.value_namespace = name_space
                            self.arp_packet_node_out_of_subnet.value_namespace_prefix = name_space_prefix
                        if(value_path == "dhcp-entries"):
                            self.dhcp_entries = value
                            self.dhcp_entries.value_namespace = name_space
                            self.dhcp_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "dynamic-entries"):
                            self.dynamic_entries = value
                            self.dynamic_entries.value_namespace = name_space
                            self.dynamic_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "gratuitous-replies-sent"):
                            self.gratuitous_replies_sent = value
                            self.gratuitous_replies_sent.value_namespace = name_space
                            self.gratuitous_replies_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "idb-structures"):
                            self.idb_structures = value
                            self.idb_structures.value_namespace = name_space
                            self.idb_structures.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-entries"):
                            self.interface_entries = value
                            self.interface_entries.value_namespace = name_space
                            self.interface_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "ip-packets-dropped-interface"):
                            self.ip_packets_dropped_interface = value
                            self.ip_packets_dropped_interface.value_namespace = name_space
                            self.ip_packets_dropped_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "ip-packets-dropped-node"):
                            self.ip_packets_dropped_node = value
                            self.ip_packets_dropped_node.value_namespace = name_space
                            self.ip_packets_dropped_node.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-proxy-replies-sent"):
                            self.local_proxy_replies_sent = value
                            self.local_proxy_replies_sent.value_namespace = name_space
                            self.local_proxy_replies_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "no-buffer-errors"):
                            self.no_buffer_errors = value
                            self.no_buffer_errors.value_namespace = name_space
                            self.no_buffer_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "out-of-memory-errors"):
                            self.out_of_memory_errors = value
                            self.out_of_memory_errors.value_namespace = name_space
                            self.out_of_memory_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "proxy-replies-sent"):
                            self.proxy_replies_sent = value
                            self.proxy_replies_sent.value_namespace = name_space
                            self.proxy_replies_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "replies-received"):
                            self.replies_received = value
                            self.replies_received.value_namespace = name_space
                            self.replies_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "replies-sent"):
                            self.replies_sent = value
                            self.replies_sent.value_namespace = name_space
                            self.replies_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "requests-received"):
                            self.requests_received = value
                            self.requests_received.value_namespace = name_space
                            self.requests_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "requests-sent"):
                            self.requests_sent = value
                            self.requests_sent.value_namespace = name_space
                            self.requests_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "resolution-replies-received"):
                            self.resolution_replies_received = value
                            self.resolution_replies_received.value_namespace = name_space
                            self.resolution_replies_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "resolution-requests-dropped"):
                            self.resolution_requests_dropped = value
                            self.resolution_requests_dropped.value_namespace = name_space
                            self.resolution_requests_dropped.value_namespace_prefix = name_space_prefix
                        if(value_path == "resolution-requests-received"):
                            self.resolution_requests_received = value
                            self.resolution_requests_received.value_namespace = name_space
                            self.resolution_requests_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "standby-entries"):
                            self.standby_entries = value
                            self.standby_entries.value_namespace = name_space
                            self.standby_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "static-entries"):
                            self.static_entries = value
                            self.static_entries.value_namespace = name_space
                            self.static_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "subscr-replies-gratg-sent"):
                            self.subscr_replies_gratg_sent = value
                            self.subscr_replies_gratg_sent.value_namespace = name_space
                            self.subscr_replies_gratg_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "subscr-replies-sent"):
                            self.subscr_replies_sent = value
                            self.subscr_replies_sent.value_namespace = name_space
                            self.subscr_replies_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "subscr-requests-received"):
                            self.subscr_requests_received = value
                            self.subscr_requests_received.value_namespace = name_space
                            self.subscr_requests_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-entries"):
                            self.total_entries = value
                            self.total_entries.value_namespace = name_space
                            self.total_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "vxlan-entries"):
                            self.vxlan_entries = value
                            self.vxlan_entries.value_namespace = name_space
                            self.vxlan_entries.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.traffic_vrf:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.traffic_vrf:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "traffic-vrfs" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "traffic-vrf"):
                        for c in self.traffic_vrf:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Arp.Nodes.Node.TrafficVrfs.TrafficVrf()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.traffic_vrf.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "traffic-vrf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class TrafficNode(Entity):
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
                    super(Arp.Nodes.Node.TrafficNode, self).__init__()

                    self.yang_name = "traffic-node"
                    self.yang_parent_name = "node"

                    self.alias_entries = YLeaf(YType.uint32, "alias-entries")

                    self.arp_packet_interface_out_of_subnet = YLeaf(YType.uint32, "arp-packet-interface-out-of-subnet")

                    self.arp_packet_node_out_of_subnet = YLeaf(YType.uint32, "arp-packet-node-out-of-subnet")

                    self.dhcp_entries = YLeaf(YType.uint32, "dhcp-entries")

                    self.dynamic_entries = YLeaf(YType.uint32, "dynamic-entries")

                    self.gratuitous_replies_sent = YLeaf(YType.uint32, "gratuitous-replies-sent")

                    self.idb_structures = YLeaf(YType.uint32, "idb-structures")

                    self.interface_entries = YLeaf(YType.uint32, "interface-entries")

                    self.ip_packets_dropped_interface = YLeaf(YType.uint32, "ip-packets-dropped-interface")

                    self.ip_packets_dropped_node = YLeaf(YType.uint32, "ip-packets-dropped-node")

                    self.local_proxy_replies_sent = YLeaf(YType.uint32, "local-proxy-replies-sent")

                    self.no_buffer_errors = YLeaf(YType.uint32, "no-buffer-errors")

                    self.out_of_memory_errors = YLeaf(YType.uint32, "out-of-memory-errors")

                    self.proxy_replies_sent = YLeaf(YType.uint32, "proxy-replies-sent")

                    self.replies_received = YLeaf(YType.uint32, "replies-received")

                    self.replies_sent = YLeaf(YType.uint32, "replies-sent")

                    self.requests_received = YLeaf(YType.uint32, "requests-received")

                    self.requests_sent = YLeaf(YType.uint32, "requests-sent")

                    self.resolution_replies_received = YLeaf(YType.uint32, "resolution-replies-received")

                    self.resolution_requests_dropped = YLeaf(YType.uint32, "resolution-requests-dropped")

                    self.resolution_requests_received = YLeaf(YType.uint32, "resolution-requests-received")

                    self.standby_entries = YLeaf(YType.uint32, "standby-entries")

                    self.static_entries = YLeaf(YType.uint32, "static-entries")

                    self.subscr_replies_gratg_sent = YLeaf(YType.uint32, "subscr-replies-gratg-sent")

                    self.subscr_replies_sent = YLeaf(YType.uint32, "subscr-replies-sent")

                    self.subscr_requests_received = YLeaf(YType.uint32, "subscr-requests-received")

                    self.total_entries = YLeaf(YType.uint32, "total-entries")

                    self.vxlan_entries = YLeaf(YType.uint32, "vxlan-entries")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("alias_entries",
                                    "arp_packet_interface_out_of_subnet",
                                    "arp_packet_node_out_of_subnet",
                                    "dhcp_entries",
                                    "dynamic_entries",
                                    "gratuitous_replies_sent",
                                    "idb_structures",
                                    "interface_entries",
                                    "ip_packets_dropped_interface",
                                    "ip_packets_dropped_node",
                                    "local_proxy_replies_sent",
                                    "no_buffer_errors",
                                    "out_of_memory_errors",
                                    "proxy_replies_sent",
                                    "replies_received",
                                    "replies_sent",
                                    "requests_received",
                                    "requests_sent",
                                    "resolution_replies_received",
                                    "resolution_requests_dropped",
                                    "resolution_requests_received",
                                    "standby_entries",
                                    "static_entries",
                                    "subscr_replies_gratg_sent",
                                    "subscr_replies_sent",
                                    "subscr_requests_received",
                                    "total_entries",
                                    "vxlan_entries") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Arp.Nodes.Node.TrafficNode, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Arp.Nodes.Node.TrafficNode, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.alias_entries.is_set or
                        self.arp_packet_interface_out_of_subnet.is_set or
                        self.arp_packet_node_out_of_subnet.is_set or
                        self.dhcp_entries.is_set or
                        self.dynamic_entries.is_set or
                        self.gratuitous_replies_sent.is_set or
                        self.idb_structures.is_set or
                        self.interface_entries.is_set or
                        self.ip_packets_dropped_interface.is_set or
                        self.ip_packets_dropped_node.is_set or
                        self.local_proxy_replies_sent.is_set or
                        self.no_buffer_errors.is_set or
                        self.out_of_memory_errors.is_set or
                        self.proxy_replies_sent.is_set or
                        self.replies_received.is_set or
                        self.replies_sent.is_set or
                        self.requests_received.is_set or
                        self.requests_sent.is_set or
                        self.resolution_replies_received.is_set or
                        self.resolution_requests_dropped.is_set or
                        self.resolution_requests_received.is_set or
                        self.standby_entries.is_set or
                        self.static_entries.is_set or
                        self.subscr_replies_gratg_sent.is_set or
                        self.subscr_replies_sent.is_set or
                        self.subscr_requests_received.is_set or
                        self.total_entries.is_set or
                        self.vxlan_entries.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.alias_entries.yfilter != YFilter.not_set or
                        self.arp_packet_interface_out_of_subnet.yfilter != YFilter.not_set or
                        self.arp_packet_node_out_of_subnet.yfilter != YFilter.not_set or
                        self.dhcp_entries.yfilter != YFilter.not_set or
                        self.dynamic_entries.yfilter != YFilter.not_set or
                        self.gratuitous_replies_sent.yfilter != YFilter.not_set or
                        self.idb_structures.yfilter != YFilter.not_set or
                        self.interface_entries.yfilter != YFilter.not_set or
                        self.ip_packets_dropped_interface.yfilter != YFilter.not_set or
                        self.ip_packets_dropped_node.yfilter != YFilter.not_set or
                        self.local_proxy_replies_sent.yfilter != YFilter.not_set or
                        self.no_buffer_errors.yfilter != YFilter.not_set or
                        self.out_of_memory_errors.yfilter != YFilter.not_set or
                        self.proxy_replies_sent.yfilter != YFilter.not_set or
                        self.replies_received.yfilter != YFilter.not_set or
                        self.replies_sent.yfilter != YFilter.not_set or
                        self.requests_received.yfilter != YFilter.not_set or
                        self.requests_sent.yfilter != YFilter.not_set or
                        self.resolution_replies_received.yfilter != YFilter.not_set or
                        self.resolution_requests_dropped.yfilter != YFilter.not_set or
                        self.resolution_requests_received.yfilter != YFilter.not_set or
                        self.standby_entries.yfilter != YFilter.not_set or
                        self.static_entries.yfilter != YFilter.not_set or
                        self.subscr_replies_gratg_sent.yfilter != YFilter.not_set or
                        self.subscr_replies_sent.yfilter != YFilter.not_set or
                        self.subscr_requests_received.yfilter != YFilter.not_set or
                        self.total_entries.yfilter != YFilter.not_set or
                        self.vxlan_entries.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "traffic-node" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.alias_entries.is_set or self.alias_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.alias_entries.get_name_leafdata())
                    if (self.arp_packet_interface_out_of_subnet.is_set or self.arp_packet_interface_out_of_subnet.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.arp_packet_interface_out_of_subnet.get_name_leafdata())
                    if (self.arp_packet_node_out_of_subnet.is_set or self.arp_packet_node_out_of_subnet.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.arp_packet_node_out_of_subnet.get_name_leafdata())
                    if (self.dhcp_entries.is_set or self.dhcp_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dhcp_entries.get_name_leafdata())
                    if (self.dynamic_entries.is_set or self.dynamic_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dynamic_entries.get_name_leafdata())
                    if (self.gratuitous_replies_sent.is_set or self.gratuitous_replies_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.gratuitous_replies_sent.get_name_leafdata())
                    if (self.idb_structures.is_set or self.idb_structures.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.idb_structures.get_name_leafdata())
                    if (self.interface_entries.is_set or self.interface_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_entries.get_name_leafdata())
                    if (self.ip_packets_dropped_interface.is_set or self.ip_packets_dropped_interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip_packets_dropped_interface.get_name_leafdata())
                    if (self.ip_packets_dropped_node.is_set or self.ip_packets_dropped_node.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip_packets_dropped_node.get_name_leafdata())
                    if (self.local_proxy_replies_sent.is_set or self.local_proxy_replies_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.local_proxy_replies_sent.get_name_leafdata())
                    if (self.no_buffer_errors.is_set or self.no_buffer_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.no_buffer_errors.get_name_leafdata())
                    if (self.out_of_memory_errors.is_set or self.out_of_memory_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_of_memory_errors.get_name_leafdata())
                    if (self.proxy_replies_sent.is_set or self.proxy_replies_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.proxy_replies_sent.get_name_leafdata())
                    if (self.replies_received.is_set or self.replies_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.replies_received.get_name_leafdata())
                    if (self.replies_sent.is_set or self.replies_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.replies_sent.get_name_leafdata())
                    if (self.requests_received.is_set or self.requests_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.requests_received.get_name_leafdata())
                    if (self.requests_sent.is_set or self.requests_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.requests_sent.get_name_leafdata())
                    if (self.resolution_replies_received.is_set or self.resolution_replies_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.resolution_replies_received.get_name_leafdata())
                    if (self.resolution_requests_dropped.is_set or self.resolution_requests_dropped.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.resolution_requests_dropped.get_name_leafdata())
                    if (self.resolution_requests_received.is_set or self.resolution_requests_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.resolution_requests_received.get_name_leafdata())
                    if (self.standby_entries.is_set or self.standby_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_entries.get_name_leafdata())
                    if (self.static_entries.is_set or self.static_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.static_entries.get_name_leafdata())
                    if (self.subscr_replies_gratg_sent.is_set or self.subscr_replies_gratg_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.subscr_replies_gratg_sent.get_name_leafdata())
                    if (self.subscr_replies_sent.is_set or self.subscr_replies_sent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.subscr_replies_sent.get_name_leafdata())
                    if (self.subscr_requests_received.is_set or self.subscr_requests_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.subscr_requests_received.get_name_leafdata())
                    if (self.total_entries.is_set or self.total_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_entries.get_name_leafdata())
                    if (self.vxlan_entries.is_set or self.vxlan_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vxlan_entries.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "alias-entries" or name == "arp-packet-interface-out-of-subnet" or name == "arp-packet-node-out-of-subnet" or name == "dhcp-entries" or name == "dynamic-entries" or name == "gratuitous-replies-sent" or name == "idb-structures" or name == "interface-entries" or name == "ip-packets-dropped-interface" or name == "ip-packets-dropped-node" or name == "local-proxy-replies-sent" or name == "no-buffer-errors" or name == "out-of-memory-errors" or name == "proxy-replies-sent" or name == "replies-received" or name == "replies-sent" or name == "requests-received" or name == "requests-sent" or name == "resolution-replies-received" or name == "resolution-requests-dropped" or name == "resolution-requests-received" or name == "standby-entries" or name == "static-entries" or name == "subscr-replies-gratg-sent" or name == "subscr-replies-sent" or name == "subscr-requests-received" or name == "total-entries" or name == "vxlan-entries"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "alias-entries"):
                        self.alias_entries = value
                        self.alias_entries.value_namespace = name_space
                        self.alias_entries.value_namespace_prefix = name_space_prefix
                    if(value_path == "arp-packet-interface-out-of-subnet"):
                        self.arp_packet_interface_out_of_subnet = value
                        self.arp_packet_interface_out_of_subnet.value_namespace = name_space
                        self.arp_packet_interface_out_of_subnet.value_namespace_prefix = name_space_prefix
                    if(value_path == "arp-packet-node-out-of-subnet"):
                        self.arp_packet_node_out_of_subnet = value
                        self.arp_packet_node_out_of_subnet.value_namespace = name_space
                        self.arp_packet_node_out_of_subnet.value_namespace_prefix = name_space_prefix
                    if(value_path == "dhcp-entries"):
                        self.dhcp_entries = value
                        self.dhcp_entries.value_namespace = name_space
                        self.dhcp_entries.value_namespace_prefix = name_space_prefix
                    if(value_path == "dynamic-entries"):
                        self.dynamic_entries = value
                        self.dynamic_entries.value_namespace = name_space
                        self.dynamic_entries.value_namespace_prefix = name_space_prefix
                    if(value_path == "gratuitous-replies-sent"):
                        self.gratuitous_replies_sent = value
                        self.gratuitous_replies_sent.value_namespace = name_space
                        self.gratuitous_replies_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "idb-structures"):
                        self.idb_structures = value
                        self.idb_structures.value_namespace = name_space
                        self.idb_structures.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-entries"):
                        self.interface_entries = value
                        self.interface_entries.value_namespace = name_space
                        self.interface_entries.value_namespace_prefix = name_space_prefix
                    if(value_path == "ip-packets-dropped-interface"):
                        self.ip_packets_dropped_interface = value
                        self.ip_packets_dropped_interface.value_namespace = name_space
                        self.ip_packets_dropped_interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "ip-packets-dropped-node"):
                        self.ip_packets_dropped_node = value
                        self.ip_packets_dropped_node.value_namespace = name_space
                        self.ip_packets_dropped_node.value_namespace_prefix = name_space_prefix
                    if(value_path == "local-proxy-replies-sent"):
                        self.local_proxy_replies_sent = value
                        self.local_proxy_replies_sent.value_namespace = name_space
                        self.local_proxy_replies_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "no-buffer-errors"):
                        self.no_buffer_errors = value
                        self.no_buffer_errors.value_namespace = name_space
                        self.no_buffer_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-of-memory-errors"):
                        self.out_of_memory_errors = value
                        self.out_of_memory_errors.value_namespace = name_space
                        self.out_of_memory_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "proxy-replies-sent"):
                        self.proxy_replies_sent = value
                        self.proxy_replies_sent.value_namespace = name_space
                        self.proxy_replies_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "replies-received"):
                        self.replies_received = value
                        self.replies_received.value_namespace = name_space
                        self.replies_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "replies-sent"):
                        self.replies_sent = value
                        self.replies_sent.value_namespace = name_space
                        self.replies_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "requests-received"):
                        self.requests_received = value
                        self.requests_received.value_namespace = name_space
                        self.requests_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "requests-sent"):
                        self.requests_sent = value
                        self.requests_sent.value_namespace = name_space
                        self.requests_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "resolution-replies-received"):
                        self.resolution_replies_received = value
                        self.resolution_replies_received.value_namespace = name_space
                        self.resolution_replies_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "resolution-requests-dropped"):
                        self.resolution_requests_dropped = value
                        self.resolution_requests_dropped.value_namespace = name_space
                        self.resolution_requests_dropped.value_namespace_prefix = name_space_prefix
                    if(value_path == "resolution-requests-received"):
                        self.resolution_requests_received = value
                        self.resolution_requests_received.value_namespace = name_space
                        self.resolution_requests_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-entries"):
                        self.standby_entries = value
                        self.standby_entries.value_namespace = name_space
                        self.standby_entries.value_namespace_prefix = name_space_prefix
                    if(value_path == "static-entries"):
                        self.static_entries = value
                        self.static_entries.value_namespace = name_space
                        self.static_entries.value_namespace_prefix = name_space_prefix
                    if(value_path == "subscr-replies-gratg-sent"):
                        self.subscr_replies_gratg_sent = value
                        self.subscr_replies_gratg_sent.value_namespace = name_space
                        self.subscr_replies_gratg_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "subscr-replies-sent"):
                        self.subscr_replies_sent = value
                        self.subscr_replies_sent.value_namespace = name_space
                        self.subscr_replies_sent.value_namespace_prefix = name_space_prefix
                    if(value_path == "subscr-requests-received"):
                        self.subscr_requests_received = value
                        self.subscr_requests_received.value_namespace = name_space
                        self.subscr_requests_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-entries"):
                        self.total_entries = value
                        self.total_entries.value_namespace = name_space
                        self.total_entries.value_namespace_prefix = name_space_prefix
                    if(value_path == "vxlan-entries"):
                        self.vxlan_entries = value
                        self.vxlan_entries.value_namespace = name_space
                        self.vxlan_entries.value_namespace_prefix = name_space_prefix


            class ResolutionHistoryClient(Entity):
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
                    super(Arp.Nodes.Node.ResolutionHistoryClient, self).__init__()

                    self.yang_name = "resolution-history-client"
                    self.yang_parent_name = "node"

                    self.arp_entry = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Arp.Nodes.Node.ResolutionHistoryClient, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Arp.Nodes.Node.ResolutionHistoryClient, self).__setattr__(name, value)


                class ArpEntry(Entity):
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
                    	**type**\:   :py:class:`ArpResolutionHistoryStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.ArpResolutionHistoryStatus>`
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(Arp.Nodes.Node.ResolutionHistoryClient.ArpEntry, self).__init__()

                        self.yang_name = "arp-entry"
                        self.yang_parent_name = "resolution-history-client"

                        self.client_id = YLeaf(YType.int32, "client-id")

                        self.entry_state = YLeaf(YType.int32, "entry-state")

                        self.idb_interface_name = YLeaf(YType.str, "idb-interface-name")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.mac_address = YLeaf(YType.str, "mac-address")

                        self.nsec_timestamp = YLeaf(YType.uint64, "nsec-timestamp")

                        self.resolution_request_count = YLeaf(YType.uint32, "resolution-request-count")

                        self.status = YLeaf(YType.enumeration, "status")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("client_id",
                                        "entry_state",
                                        "idb_interface_name",
                                        "ipv4_address",
                                        "mac_address",
                                        "nsec_timestamp",
                                        "resolution_request_count",
                                        "status") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Arp.Nodes.Node.ResolutionHistoryClient.ArpEntry, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Arp.Nodes.Node.ResolutionHistoryClient.ArpEntry, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.client_id.is_set or
                            self.entry_state.is_set or
                            self.idb_interface_name.is_set or
                            self.ipv4_address.is_set or
                            self.mac_address.is_set or
                            self.nsec_timestamp.is_set or
                            self.resolution_request_count.is_set or
                            self.status.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.client_id.yfilter != YFilter.not_set or
                            self.entry_state.yfilter != YFilter.not_set or
                            self.idb_interface_name.yfilter != YFilter.not_set or
                            self.ipv4_address.yfilter != YFilter.not_set or
                            self.mac_address.yfilter != YFilter.not_set or
                            self.nsec_timestamp.yfilter != YFilter.not_set or
                            self.resolution_request_count.yfilter != YFilter.not_set or
                            self.status.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "arp-entry" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.client_id.is_set or self.client_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.client_id.get_name_leafdata())
                        if (self.entry_state.is_set or self.entry_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.entry_state.get_name_leafdata())
                        if (self.idb_interface_name.is_set or self.idb_interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.idb_interface_name.get_name_leafdata())
                        if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                        if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mac_address.get_name_leafdata())
                        if (self.nsec_timestamp.is_set or self.nsec_timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nsec_timestamp.get_name_leafdata())
                        if (self.resolution_request_count.is_set or self.resolution_request_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resolution_request_count.get_name_leafdata())
                        if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.status.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "client-id" or name == "entry-state" or name == "idb-interface-name" or name == "ipv4-address" or name == "mac-address" or name == "nsec-timestamp" or name == "resolution-request-count" or name == "status"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "client-id"):
                            self.client_id = value
                            self.client_id.value_namespace = name_space
                            self.client_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "entry-state"):
                            self.entry_state = value
                            self.entry_state.value_namespace = name_space
                            self.entry_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "idb-interface-name"):
                            self.idb_interface_name = value
                            self.idb_interface_name.value_namespace = name_space
                            self.idb_interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4-address"):
                            self.ipv4_address = value
                            self.ipv4_address.value_namespace = name_space
                            self.ipv4_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "mac-address"):
                            self.mac_address = value
                            self.mac_address.value_namespace = name_space
                            self.mac_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "nsec-timestamp"):
                            self.nsec_timestamp = value
                            self.nsec_timestamp.value_namespace = name_space
                            self.nsec_timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "resolution-request-count"):
                            self.resolution_request_count = value
                            self.resolution_request_count.value_namespace = name_space
                            self.resolution_request_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "status"):
                            self.status = value
                            self.status.value_namespace = name_space
                            self.status.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.arp_entry:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.arp_entry:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "resolution-history-client" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "arp-entry"):
                        for c in self.arp_entry:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Arp.Nodes.Node.ResolutionHistoryClient.ArpEntry()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.arp_entry.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "arp-entry"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Entries(Entity):
                """
                Table of ARP entries
                
                .. attribute:: entry
                
                	ARP entry
                	**type**\: list of    :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.Entries.Entry>`
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2016-12-19'

                def __init__(self):
                    super(Arp.Nodes.Node.Entries, self).__init__()

                    self.yang_name = "entries"
                    self.yang_parent_name = "node"

                    self.entry = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Arp.Nodes.Node.Entries, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Arp.Nodes.Node.Entries, self).__setattr__(name, value)


                class Entry(Entity):
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
                    	**type**\:   :py:class:`IpArpBagEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.IpArpBagEncap>`
                    
                    .. attribute:: flag
                    
                    	Flags of this entry
                    	**type**\:   :py:class:`IpArpBagFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.IpArpBagFlags>`
                    
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
                    	**type**\:   :py:class:`IpArpBagMedia <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.IpArpBagMedia>`
                    
                    .. attribute:: state
                    
                    	State of this entry
                    	**type**\:   :py:class:`IpArpBagState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.IpArpBagState>`
                    
                    

                    """

                    _prefix = 'ipv4-arp-oper'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(Arp.Nodes.Node.Entries.Entry, self).__init__()

                        self.yang_name = "entry"
                        self.yang_parent_name = "entries"

                        self.address = YLeaf(YType.str, "address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.age = YLeaf(YType.uint64, "age")

                        self.encapsulation_type = YLeaf(YType.enumeration, "encapsulation-type")

                        self.flag = YLeaf(YType.enumeration, "flag")

                        self.hardware_address = YLeaf(YType.str, "hardware-address")

                        self.hardware_length = YLeaf(YType.uint8, "hardware-length")

                        self.media_type = YLeaf(YType.enumeration, "media-type")

                        self.state = YLeaf(YType.enumeration, "state")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address",
                                        "interface_name",
                                        "age",
                                        "encapsulation_type",
                                        "flag",
                                        "hardware_address",
                                        "hardware_length",
                                        "media_type",
                                        "state") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Arp.Nodes.Node.Entries.Entry, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Arp.Nodes.Node.Entries.Entry, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.address.is_set or
                            self.interface_name.is_set or
                            self.age.is_set or
                            self.encapsulation_type.is_set or
                            self.flag.is_set or
                            self.hardware_address.is_set or
                            self.hardware_length.is_set or
                            self.media_type.is_set or
                            self.state.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.age.yfilter != YFilter.not_set or
                            self.encapsulation_type.yfilter != YFilter.not_set or
                            self.flag.yfilter != YFilter.not_set or
                            self.hardware_address.yfilter != YFilter.not_set or
                            self.hardware_length.yfilter != YFilter.not_set or
                            self.media_type.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "entry" + "[address='" + self.address.get() + "']" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.age.is_set or self.age.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.age.get_name_leafdata())
                        if (self.encapsulation_type.is_set or self.encapsulation_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.encapsulation_type.get_name_leafdata())
                        if (self.flag.is_set or self.flag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flag.get_name_leafdata())
                        if (self.hardware_address.is_set or self.hardware_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hardware_address.get_name_leafdata())
                        if (self.hardware_length.is_set or self.hardware_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hardware_length.get_name_leafdata())
                        if (self.media_type.is_set or self.media_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.media_type.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "interface-name" or name == "age" or name == "encapsulation-type" or name == "flag" or name == "hardware-address" or name == "hardware-length" or name == "media-type" or name == "state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "age"):
                            self.age = value
                            self.age.value_namespace = name_space
                            self.age.value_namespace_prefix = name_space_prefix
                        if(value_path == "encapsulation-type"):
                            self.encapsulation_type = value
                            self.encapsulation_type.value_namespace = name_space
                            self.encapsulation_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "flag"):
                            self.flag = value
                            self.flag.value_namespace = name_space
                            self.flag.value_namespace_prefix = name_space_prefix
                        if(value_path == "hardware-address"):
                            self.hardware_address = value
                            self.hardware_address.value_namespace = name_space
                            self.hardware_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "hardware-length"):
                            self.hardware_length = value
                            self.hardware_length.value_namespace = name_space
                            self.hardware_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "media-type"):
                            self.media_type = value
                            self.media_type.value_namespace = name_space
                            self.media_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.entry:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.entry:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "entries" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "entry"):
                        for c in self.entry:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Arp.Nodes.Node.Entries.Entry()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.entry.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "entry"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class TrafficInterfaces(Entity):
                """
                ARP Traffic information per interface
                
                .. attribute:: traffic_interface
                
                	Per interface traffic data
                	**type**\: list of    :py:class:`TrafficInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_oper.Arp.Nodes.Node.TrafficInterfaces.TrafficInterface>`
                
                

                """

                _prefix = 'ipv4-arp-oper'
                _revision = '2016-12-19'

                def __init__(self):
                    super(Arp.Nodes.Node.TrafficInterfaces, self).__init__()

                    self.yang_name = "traffic-interfaces"
                    self.yang_parent_name = "node"

                    self.traffic_interface = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Arp.Nodes.Node.TrafficInterfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Arp.Nodes.Node.TrafficInterfaces, self).__setattr__(name, value)


                class TrafficInterface(Entity):
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
                        super(Arp.Nodes.Node.TrafficInterfaces.TrafficInterface, self).__init__()

                        self.yang_name = "traffic-interface"
                        self.yang_parent_name = "traffic-interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.alias_entries = YLeaf(YType.uint32, "alias-entries")

                        self.arp_packet_interface_out_of_subnet = YLeaf(YType.uint32, "arp-packet-interface-out-of-subnet")

                        self.arp_packet_node_out_of_subnet = YLeaf(YType.uint32, "arp-packet-node-out-of-subnet")

                        self.dhcp_entries = YLeaf(YType.uint32, "dhcp-entries")

                        self.dynamic_entries = YLeaf(YType.uint32, "dynamic-entries")

                        self.gratuitous_replies_sent = YLeaf(YType.uint32, "gratuitous-replies-sent")

                        self.idb_structures = YLeaf(YType.uint32, "idb-structures")

                        self.interface_entries = YLeaf(YType.uint32, "interface-entries")

                        self.ip_packets_dropped_interface = YLeaf(YType.uint32, "ip-packets-dropped-interface")

                        self.ip_packets_dropped_node = YLeaf(YType.uint32, "ip-packets-dropped-node")

                        self.local_proxy_replies_sent = YLeaf(YType.uint32, "local-proxy-replies-sent")

                        self.no_buffer_errors = YLeaf(YType.uint32, "no-buffer-errors")

                        self.out_of_memory_errors = YLeaf(YType.uint32, "out-of-memory-errors")

                        self.proxy_replies_sent = YLeaf(YType.uint32, "proxy-replies-sent")

                        self.replies_received = YLeaf(YType.uint32, "replies-received")

                        self.replies_sent = YLeaf(YType.uint32, "replies-sent")

                        self.requests_received = YLeaf(YType.uint32, "requests-received")

                        self.requests_sent = YLeaf(YType.uint32, "requests-sent")

                        self.resolution_replies_received = YLeaf(YType.uint32, "resolution-replies-received")

                        self.resolution_requests_dropped = YLeaf(YType.uint32, "resolution-requests-dropped")

                        self.resolution_requests_received = YLeaf(YType.uint32, "resolution-requests-received")

                        self.standby_entries = YLeaf(YType.uint32, "standby-entries")

                        self.static_entries = YLeaf(YType.uint32, "static-entries")

                        self.subscr_replies_gratg_sent = YLeaf(YType.uint32, "subscr-replies-gratg-sent")

                        self.subscr_replies_sent = YLeaf(YType.uint32, "subscr-replies-sent")

                        self.subscr_requests_received = YLeaf(YType.uint32, "subscr-requests-received")

                        self.total_entries = YLeaf(YType.uint32, "total-entries")

                        self.vxlan_entries = YLeaf(YType.uint32, "vxlan-entries")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name",
                                        "alias_entries",
                                        "arp_packet_interface_out_of_subnet",
                                        "arp_packet_node_out_of_subnet",
                                        "dhcp_entries",
                                        "dynamic_entries",
                                        "gratuitous_replies_sent",
                                        "idb_structures",
                                        "interface_entries",
                                        "ip_packets_dropped_interface",
                                        "ip_packets_dropped_node",
                                        "local_proxy_replies_sent",
                                        "no_buffer_errors",
                                        "out_of_memory_errors",
                                        "proxy_replies_sent",
                                        "replies_received",
                                        "replies_sent",
                                        "requests_received",
                                        "requests_sent",
                                        "resolution_replies_received",
                                        "resolution_requests_dropped",
                                        "resolution_requests_received",
                                        "standby_entries",
                                        "static_entries",
                                        "subscr_replies_gratg_sent",
                                        "subscr_replies_sent",
                                        "subscr_requests_received",
                                        "total_entries",
                                        "vxlan_entries") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Arp.Nodes.Node.TrafficInterfaces.TrafficInterface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Arp.Nodes.Node.TrafficInterfaces.TrafficInterface, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.alias_entries.is_set or
                            self.arp_packet_interface_out_of_subnet.is_set or
                            self.arp_packet_node_out_of_subnet.is_set or
                            self.dhcp_entries.is_set or
                            self.dynamic_entries.is_set or
                            self.gratuitous_replies_sent.is_set or
                            self.idb_structures.is_set or
                            self.interface_entries.is_set or
                            self.ip_packets_dropped_interface.is_set or
                            self.ip_packets_dropped_node.is_set or
                            self.local_proxy_replies_sent.is_set or
                            self.no_buffer_errors.is_set or
                            self.out_of_memory_errors.is_set or
                            self.proxy_replies_sent.is_set or
                            self.replies_received.is_set or
                            self.replies_sent.is_set or
                            self.requests_received.is_set or
                            self.requests_sent.is_set or
                            self.resolution_replies_received.is_set or
                            self.resolution_requests_dropped.is_set or
                            self.resolution_requests_received.is_set or
                            self.standby_entries.is_set or
                            self.static_entries.is_set or
                            self.subscr_replies_gratg_sent.is_set or
                            self.subscr_replies_sent.is_set or
                            self.subscr_requests_received.is_set or
                            self.total_entries.is_set or
                            self.vxlan_entries.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.alias_entries.yfilter != YFilter.not_set or
                            self.arp_packet_interface_out_of_subnet.yfilter != YFilter.not_set or
                            self.arp_packet_node_out_of_subnet.yfilter != YFilter.not_set or
                            self.dhcp_entries.yfilter != YFilter.not_set or
                            self.dynamic_entries.yfilter != YFilter.not_set or
                            self.gratuitous_replies_sent.yfilter != YFilter.not_set or
                            self.idb_structures.yfilter != YFilter.not_set or
                            self.interface_entries.yfilter != YFilter.not_set or
                            self.ip_packets_dropped_interface.yfilter != YFilter.not_set or
                            self.ip_packets_dropped_node.yfilter != YFilter.not_set or
                            self.local_proxy_replies_sent.yfilter != YFilter.not_set or
                            self.no_buffer_errors.yfilter != YFilter.not_set or
                            self.out_of_memory_errors.yfilter != YFilter.not_set or
                            self.proxy_replies_sent.yfilter != YFilter.not_set or
                            self.replies_received.yfilter != YFilter.not_set or
                            self.replies_sent.yfilter != YFilter.not_set or
                            self.requests_received.yfilter != YFilter.not_set or
                            self.requests_sent.yfilter != YFilter.not_set or
                            self.resolution_replies_received.yfilter != YFilter.not_set or
                            self.resolution_requests_dropped.yfilter != YFilter.not_set or
                            self.resolution_requests_received.yfilter != YFilter.not_set or
                            self.standby_entries.yfilter != YFilter.not_set or
                            self.static_entries.yfilter != YFilter.not_set or
                            self.subscr_replies_gratg_sent.yfilter != YFilter.not_set or
                            self.subscr_replies_sent.yfilter != YFilter.not_set or
                            self.subscr_requests_received.yfilter != YFilter.not_set or
                            self.total_entries.yfilter != YFilter.not_set or
                            self.vxlan_entries.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "traffic-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.alias_entries.is_set or self.alias_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.alias_entries.get_name_leafdata())
                        if (self.arp_packet_interface_out_of_subnet.is_set or self.arp_packet_interface_out_of_subnet.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.arp_packet_interface_out_of_subnet.get_name_leafdata())
                        if (self.arp_packet_node_out_of_subnet.is_set or self.arp_packet_node_out_of_subnet.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.arp_packet_node_out_of_subnet.get_name_leafdata())
                        if (self.dhcp_entries.is_set or self.dhcp_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dhcp_entries.get_name_leafdata())
                        if (self.dynamic_entries.is_set or self.dynamic_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dynamic_entries.get_name_leafdata())
                        if (self.gratuitous_replies_sent.is_set or self.gratuitous_replies_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.gratuitous_replies_sent.get_name_leafdata())
                        if (self.idb_structures.is_set or self.idb_structures.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.idb_structures.get_name_leafdata())
                        if (self.interface_entries.is_set or self.interface_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_entries.get_name_leafdata())
                        if (self.ip_packets_dropped_interface.is_set or self.ip_packets_dropped_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_packets_dropped_interface.get_name_leafdata())
                        if (self.ip_packets_dropped_node.is_set or self.ip_packets_dropped_node.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_packets_dropped_node.get_name_leafdata())
                        if (self.local_proxy_replies_sent.is_set or self.local_proxy_replies_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_proxy_replies_sent.get_name_leafdata())
                        if (self.no_buffer_errors.is_set or self.no_buffer_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.no_buffer_errors.get_name_leafdata())
                        if (self.out_of_memory_errors.is_set or self.out_of_memory_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.out_of_memory_errors.get_name_leafdata())
                        if (self.proxy_replies_sent.is_set or self.proxy_replies_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.proxy_replies_sent.get_name_leafdata())
                        if (self.replies_received.is_set or self.replies_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.replies_received.get_name_leafdata())
                        if (self.replies_sent.is_set or self.replies_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.replies_sent.get_name_leafdata())
                        if (self.requests_received.is_set or self.requests_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.requests_received.get_name_leafdata())
                        if (self.requests_sent.is_set or self.requests_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.requests_sent.get_name_leafdata())
                        if (self.resolution_replies_received.is_set or self.resolution_replies_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resolution_replies_received.get_name_leafdata())
                        if (self.resolution_requests_dropped.is_set or self.resolution_requests_dropped.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resolution_requests_dropped.get_name_leafdata())
                        if (self.resolution_requests_received.is_set or self.resolution_requests_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resolution_requests_received.get_name_leafdata())
                        if (self.standby_entries.is_set or self.standby_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.standby_entries.get_name_leafdata())
                        if (self.static_entries.is_set or self.static_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.static_entries.get_name_leafdata())
                        if (self.subscr_replies_gratg_sent.is_set or self.subscr_replies_gratg_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subscr_replies_gratg_sent.get_name_leafdata())
                        if (self.subscr_replies_sent.is_set or self.subscr_replies_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subscr_replies_sent.get_name_leafdata())
                        if (self.subscr_requests_received.is_set or self.subscr_requests_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subscr_requests_received.get_name_leafdata())
                        if (self.total_entries.is_set or self.total_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_entries.get_name_leafdata())
                        if (self.vxlan_entries.is_set or self.vxlan_entries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vxlan_entries.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name" or name == "alias-entries" or name == "arp-packet-interface-out-of-subnet" or name == "arp-packet-node-out-of-subnet" or name == "dhcp-entries" or name == "dynamic-entries" or name == "gratuitous-replies-sent" or name == "idb-structures" or name == "interface-entries" or name == "ip-packets-dropped-interface" or name == "ip-packets-dropped-node" or name == "local-proxy-replies-sent" or name == "no-buffer-errors" or name == "out-of-memory-errors" or name == "proxy-replies-sent" or name == "replies-received" or name == "replies-sent" or name == "requests-received" or name == "requests-sent" or name == "resolution-replies-received" or name == "resolution-requests-dropped" or name == "resolution-requests-received" or name == "standby-entries" or name == "static-entries" or name == "subscr-replies-gratg-sent" or name == "subscr-replies-sent" or name == "subscr-requests-received" or name == "total-entries" or name == "vxlan-entries"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "alias-entries"):
                            self.alias_entries = value
                            self.alias_entries.value_namespace = name_space
                            self.alias_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "arp-packet-interface-out-of-subnet"):
                            self.arp_packet_interface_out_of_subnet = value
                            self.arp_packet_interface_out_of_subnet.value_namespace = name_space
                            self.arp_packet_interface_out_of_subnet.value_namespace_prefix = name_space_prefix
                        if(value_path == "arp-packet-node-out-of-subnet"):
                            self.arp_packet_node_out_of_subnet = value
                            self.arp_packet_node_out_of_subnet.value_namespace = name_space
                            self.arp_packet_node_out_of_subnet.value_namespace_prefix = name_space_prefix
                        if(value_path == "dhcp-entries"):
                            self.dhcp_entries = value
                            self.dhcp_entries.value_namespace = name_space
                            self.dhcp_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "dynamic-entries"):
                            self.dynamic_entries = value
                            self.dynamic_entries.value_namespace = name_space
                            self.dynamic_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "gratuitous-replies-sent"):
                            self.gratuitous_replies_sent = value
                            self.gratuitous_replies_sent.value_namespace = name_space
                            self.gratuitous_replies_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "idb-structures"):
                            self.idb_structures = value
                            self.idb_structures.value_namespace = name_space
                            self.idb_structures.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-entries"):
                            self.interface_entries = value
                            self.interface_entries.value_namespace = name_space
                            self.interface_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "ip-packets-dropped-interface"):
                            self.ip_packets_dropped_interface = value
                            self.ip_packets_dropped_interface.value_namespace = name_space
                            self.ip_packets_dropped_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "ip-packets-dropped-node"):
                            self.ip_packets_dropped_node = value
                            self.ip_packets_dropped_node.value_namespace = name_space
                            self.ip_packets_dropped_node.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-proxy-replies-sent"):
                            self.local_proxy_replies_sent = value
                            self.local_proxy_replies_sent.value_namespace = name_space
                            self.local_proxy_replies_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "no-buffer-errors"):
                            self.no_buffer_errors = value
                            self.no_buffer_errors.value_namespace = name_space
                            self.no_buffer_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "out-of-memory-errors"):
                            self.out_of_memory_errors = value
                            self.out_of_memory_errors.value_namespace = name_space
                            self.out_of_memory_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "proxy-replies-sent"):
                            self.proxy_replies_sent = value
                            self.proxy_replies_sent.value_namespace = name_space
                            self.proxy_replies_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "replies-received"):
                            self.replies_received = value
                            self.replies_received.value_namespace = name_space
                            self.replies_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "replies-sent"):
                            self.replies_sent = value
                            self.replies_sent.value_namespace = name_space
                            self.replies_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "requests-received"):
                            self.requests_received = value
                            self.requests_received.value_namespace = name_space
                            self.requests_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "requests-sent"):
                            self.requests_sent = value
                            self.requests_sent.value_namespace = name_space
                            self.requests_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "resolution-replies-received"):
                            self.resolution_replies_received = value
                            self.resolution_replies_received.value_namespace = name_space
                            self.resolution_replies_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "resolution-requests-dropped"):
                            self.resolution_requests_dropped = value
                            self.resolution_requests_dropped.value_namespace = name_space
                            self.resolution_requests_dropped.value_namespace_prefix = name_space_prefix
                        if(value_path == "resolution-requests-received"):
                            self.resolution_requests_received = value
                            self.resolution_requests_received.value_namespace = name_space
                            self.resolution_requests_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "standby-entries"):
                            self.standby_entries = value
                            self.standby_entries.value_namespace = name_space
                            self.standby_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "static-entries"):
                            self.static_entries = value
                            self.static_entries.value_namespace = name_space
                            self.static_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "subscr-replies-gratg-sent"):
                            self.subscr_replies_gratg_sent = value
                            self.subscr_replies_gratg_sent.value_namespace = name_space
                            self.subscr_replies_gratg_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "subscr-replies-sent"):
                            self.subscr_replies_sent = value
                            self.subscr_replies_sent.value_namespace = name_space
                            self.subscr_replies_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "subscr-requests-received"):
                            self.subscr_requests_received = value
                            self.subscr_requests_received.value_namespace = name_space
                            self.subscr_requests_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-entries"):
                            self.total_entries = value
                            self.total_entries.value_namespace = name_space
                            self.total_entries.value_namespace_prefix = name_space_prefix
                        if(value_path == "vxlan-entries"):
                            self.vxlan_entries = value
                            self.vxlan_entries.value_namespace = name_space
                            self.vxlan_entries.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.traffic_interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.traffic_interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "traffic-interfaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "traffic-interface"):
                        for c in self.traffic_interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Arp.Nodes.Node.TrafficInterfaces.TrafficInterface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.traffic_interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "traffic-interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.entries is not None and self.entries.has_data()) or
                    (self.resolution_history_client is not None and self.resolution_history_client.has_data()) or
                    (self.resolution_history_dynamic is not None and self.resolution_history_dynamic.has_data()) or
                    (self.traffic_interfaces is not None and self.traffic_interfaces.has_data()) or
                    (self.traffic_node is not None and self.traffic_node.has_data()) or
                    (self.traffic_vrfs is not None and self.traffic_vrfs.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.entries is not None and self.entries.has_operation()) or
                    (self.resolution_history_client is not None and self.resolution_history_client.has_operation()) or
                    (self.resolution_history_dynamic is not None and self.resolution_history_dynamic.has_operation()) or
                    (self.traffic_interfaces is not None and self.traffic_interfaces.has_operation()) or
                    (self.traffic_node is not None and self.traffic_node.has_operation()) or
                    (self.traffic_vrfs is not None and self.traffic_vrfs.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-arp-oper:arp/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "entries"):
                    if (self.entries is None):
                        self.entries = Arp.Nodes.Node.Entries()
                        self.entries.parent = self
                        self._children_name_map["entries"] = "entries"
                    return self.entries

                if (child_yang_name == "resolution-history-client"):
                    if (self.resolution_history_client is None):
                        self.resolution_history_client = Arp.Nodes.Node.ResolutionHistoryClient()
                        self.resolution_history_client.parent = self
                        self._children_name_map["resolution_history_client"] = "resolution-history-client"
                    return self.resolution_history_client

                if (child_yang_name == "resolution-history-dynamic"):
                    if (self.resolution_history_dynamic is None):
                        self.resolution_history_dynamic = Arp.Nodes.Node.ResolutionHistoryDynamic()
                        self.resolution_history_dynamic.parent = self
                        self._children_name_map["resolution_history_dynamic"] = "resolution-history-dynamic"
                    return self.resolution_history_dynamic

                if (child_yang_name == "traffic-interfaces"):
                    if (self.traffic_interfaces is None):
                        self.traffic_interfaces = Arp.Nodes.Node.TrafficInterfaces()
                        self.traffic_interfaces.parent = self
                        self._children_name_map["traffic_interfaces"] = "traffic-interfaces"
                    return self.traffic_interfaces

                if (child_yang_name == "traffic-node"):
                    if (self.traffic_node is None):
                        self.traffic_node = Arp.Nodes.Node.TrafficNode()
                        self.traffic_node.parent = self
                        self._children_name_map["traffic_node"] = "traffic-node"
                    return self.traffic_node

                if (child_yang_name == "traffic-vrfs"):
                    if (self.traffic_vrfs is None):
                        self.traffic_vrfs = Arp.Nodes.Node.TrafficVrfs()
                        self.traffic_vrfs.parent = self
                        self._children_name_map["traffic_vrfs"] = "traffic-vrfs"
                    return self.traffic_vrfs

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entries" or name == "resolution-history-client" or name == "resolution-history-dynamic" or name == "traffic-interfaces" or name == "traffic-node" or name == "traffic-vrfs" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-arp-oper:arp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Arp.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-arp-oper:arp" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = Arp.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Arp()
        return self._top_entity

