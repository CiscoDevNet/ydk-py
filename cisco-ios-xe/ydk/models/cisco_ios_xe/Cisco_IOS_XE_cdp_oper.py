""" Cisco_IOS_XE_cdp_oper 

This module contains a collection of YANG definitions
for monitoring of Cisco CDP operational information.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CdpAdvVersion(Enum):
    """
    CdpAdvVersion

    CDP advertized version information

    .. data:: cdp_advertised_none = 0

    .. data:: cdp_advertised_v1 = 1

    .. data:: cdp_advertised_v2 = 2

    """

    cdp_advertised_none = Enum.YLeaf(0, "cdp-advertised-none")

    cdp_advertised_v1 = Enum.YLeaf(1, "cdp-advertised-v1")

    cdp_advertised_v2 = Enum.YLeaf(2, "cdp-advertised-v2")


class CdpDuplex(Enum):
    """
    CdpDuplex

    CDP duplex modes

    .. data:: cdp_duplex_unknown = 0

    .. data:: cdp_half_duplex = 1

    .. data:: cdp_full_duplex = 2

    .. data:: cdp_half_duplex_mismatch = 3

    .. data:: cdp_full_duplex_mismatch = 4

    """

    cdp_duplex_unknown = Enum.YLeaf(0, "cdp-duplex-unknown")

    cdp_half_duplex = Enum.YLeaf(1, "cdp-half-duplex")

    cdp_full_duplex = Enum.YLeaf(2, "cdp-full-duplex")

    cdp_half_duplex_mismatch = Enum.YLeaf(3, "cdp-half-duplex-mismatch")

    cdp_full_duplex_mismatch = Enum.YLeaf(4, "cdp-full-duplex-mismatch")


class CdpEnableDisable(Enum):
    """
    CdpEnableDisable

    CDP type enable or disable

    .. data:: cdp_disable = 0

    .. data:: cdp_enable = 1

    """

    cdp_disable = Enum.YLeaf(0, "cdp-disable")

    cdp_enable = Enum.YLeaf(1, "cdp-enable")


class CdpUnidirectionalMode(Enum):
    """
    CdpUnidirectionalMode

    CDP unidirectional modes

    .. data:: cdp_uni_mode_off = 0

    .. data:: cdp_uni_mode_send_only = 1

    .. data:: cdp_uni_mode_recv_only = 2

    .. data:: cdp_uni_mode_unknown = 3

    """

    cdp_uni_mode_off = Enum.YLeaf(0, "cdp-uni-mode-off")

    cdp_uni_mode_send_only = Enum.YLeaf(1, "cdp-uni-mode-send-only")

    cdp_uni_mode_recv_only = Enum.YLeaf(2, "cdp-uni-mode-recv-only")

    cdp_uni_mode_unknown = Enum.YLeaf(3, "cdp-uni-mode-unknown")


class CdpYesNo(Enum):
    """
    CdpYesNo

    CDP type yes or no

    .. data:: cdp_no = 0

    .. data:: cdp_yes = 1

    """

    cdp_no = Enum.YLeaf(0, "cdp-no")

    cdp_yes = Enum.YLeaf(1, "cdp-yes")



class CdpNeighbourDetails(Entity):
    """
    Cisco CDP neighbour operational data
    
    .. attribute:: cdp_neighbour_detail
    
    	List of CDP neighbour details
    	**type**\: list of    :py:class:`CdpNeighbourDetail <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpNeighbourDetails.CdpNeighbourDetail>`
    
    

    """

    _prefix = 'cdp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(CdpNeighbourDetails, self).__init__()
        self._top_entity = None

        self.yang_name = "cdp-neighbour-details"
        self.yang_parent_name = "Cisco-IOS-XE-cdp-oper"

        self.cdp_neighbour_detail = YList(self)

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
                    super(CdpNeighbourDetails, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(CdpNeighbourDetails, self).__setattr__(name, value)


    class CdpNeighbourDetail(Entity):
        """
        List of CDP neighbour details
        
        .. attribute:: device_id  <key>
        
        	Device number of this device, Used as a key in the device list
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: adv_version
        
        	CDP header version of the advertisement that last filled this cache entry
        	**type**\:   :py:class:`CdpAdvVersion <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpAdvVersion>`
        
        .. attribute:: capability
        
        	Identifies the functional capability of the device. The capability types that can be discovered are\: R\-Router T\-Transparent bridge B\-Source\-routing bridge S\-Switch H\-Host I\-device is using IGMP r\-Repeater
        	**type**\:  str
        
        .. attribute:: clns_address
        
        	CLNS address of the device
        	**type**\:  str
        
        .. attribute:: decnet_addr
        
        	DECNET address of the device
        	**type**\:  str
        
        .. attribute:: device_name
        
        	Device name in the form of a character string. By default device ID is either the device's fully\-qualified host name (including the domain name) or the device's hardware serial number in ASCII
        	**type**\:  str
        
        .. attribute:: duplex
        
        	Indicates the duplex configuration of the Cisco Discovery Protocol  broadcast interface. This information is used by network operators to diagnose  connectivity problems between adjacent network devices
        	**type**\:   :py:class:`CdpDuplex <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpDuplex>`
        
        .. attribute:: hello_message
        
        	CDP Protocol Hello message
        	**type**\:   :py:class:`HelloMessage <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpNeighbourDetails.CdpNeighbourDetail.HelloMessage>`
        
        .. attribute:: ip_address
        
        	IPv4 address of the device
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        
        ----
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        
        ----
        .. attribute:: ipv6_address
        
        	IPv6 address of the device
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        
        ----
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        
        ----
        .. attribute:: local_intf_name
        
        	The port or interface on which CDP packets are received
        	**type**\:  str
        
        .. attribute:: mgmt_address
        
        	Device's management addresses
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        
        ----
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        
        ----
        .. attribute:: native_vlan
        
        	Indicates, per interface, the assumed VLAN for untagged packets on the interface. Cisco Discovery Protocol learns the native VLAN for an interface. This field is implemented only for interfaces that support the IEEE 802.1Q protocol Remote port's native VLAN [0..1k/4k]; 0 == not received
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: novell_addr
        
        	Novell address of the device. It has a 4 byte net number followed by 6 bytes of  node information
        	**type**\:  str
        
        .. attribute:: platform_name
        
        	Identifies the platform information of the device. For example, Cisco 4500
        	**type**\:  str
        
        .. attribute:: port_id
        
        	Neighbor device's port or interface on which the CDP packets are multicasted
        	**type**\:  str
        
        .. attribute:: power
        
        	This field shows the power in milliwatts device is using
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: power_available
        
        	This field used to keep inline power
        	**type**\:   :py:class:`PowerAvailable <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpNeighbourDetails.CdpNeighbourDetail.PowerAvailable>`
        
        .. attribute:: power_request
        
        	This field used to keep inline power
        	**type**\:   :py:class:`PowerRequest <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpNeighbourDetails.CdpNeighbourDetail.PowerRequest>`
        
        .. attribute:: second_port_status
        
        	Used to keep PC port status on IP phone
        	**type**\:  str
        
        .. attribute:: spare_pair
        
        	Spare pair PoE TLV is a one octet long. This has following field\: Bit            Function                            value/Meaning 0    4\-pair PoE Supported                           0=No/1=Yes 1    Spare pair Detection/Classification required   0=No/1=Yes 2    PD Spare Pair Desired State                    0=Disabled/1=Enabled 3    PSE Spare Pair Operational State               0=No/1=Yes 4\:7   Reserved 
        	**type**\:   :py:class:`SparePair <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpNeighbourDetails.CdpNeighbourDetail.SparePair>`
        
        .. attribute:: table_id
        
        	Table id of ip routing process
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: unidirectional_mode
        
        	Specifies ports to unidirectionally transmit or receive traffic. Unidirectional Ethernet uses only one strand of fiber for either transmitting or receiving one\-way traffic for the GigaPort, instead of  two strands of fiber for a full\-duplex
        	**type**\:   :py:class:`CdpUnidirectionalMode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpUnidirectionalMode>`
        
        .. attribute:: version
        
        	Version Contains the device software release information
        	**type**\:  str
        
        .. attribute:: vty_mgmt_domain
        
        	Advertises the configured VLAN Trunking Protocol (VTP)\-management\-domain name of the system. This name is used by network operators to verify VTP\-domain configuration in adjacent network nodes
        	**type**\:  str
        
        .. attribute:: vvid
        
        	Appliance VLAN ID \- VLAN on the device used by the appliance, for instance if the appliance is an IP phone, this is the voice VLAN
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: vvid_tag
        
        	Appliance id for appliance vlan Appliance ID \- Type of device attached to port advertised in the appliance TLV
        	**type**\:  int
        
        	**range:** 0..255
        
        

        """

        _prefix = 'cdp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(CdpNeighbourDetails.CdpNeighbourDetail, self).__init__()

            self.yang_name = "cdp-neighbour-detail"
            self.yang_parent_name = "cdp-neighbour-details"

            self.device_id = YLeaf(YType.uint32, "device-id")

            self.adv_version = YLeaf(YType.enumeration, "adv-version")

            self.capability = YLeaf(YType.str, "capability")

            self.clns_address = YLeaf(YType.str, "clns-address")

            self.decnet_addr = YLeaf(YType.str, "decnet-addr")

            self.device_name = YLeaf(YType.str, "device-name")

            self.duplex = YLeaf(YType.enumeration, "duplex")

            self.ip_address = YLeaf(YType.str, "ip-address")

            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

            self.local_intf_name = YLeaf(YType.str, "local-intf-name")

            self.mgmt_address = YLeaf(YType.str, "mgmt-address")

            self.native_vlan = YLeaf(YType.uint16, "native-vlan")

            self.novell_addr = YLeaf(YType.str, "novell-addr")

            self.platform_name = YLeaf(YType.str, "platform-name")

            self.port_id = YLeaf(YType.str, "port-id")

            self.power = YLeaf(YType.uint32, "power")

            self.second_port_status = YLeaf(YType.str, "second-port-status")

            self.table_id = YLeaf(YType.uint16, "table-id")

            self.unidirectional_mode = YLeaf(YType.enumeration, "unidirectional-mode")

            self.version = YLeaf(YType.str, "version")

            self.vty_mgmt_domain = YLeaf(YType.str, "vty-mgmt-domain")

            self.vvid = YLeaf(YType.uint16, "vvid")

            self.vvid_tag = YLeaf(YType.uint8, "vvid-tag")

            self.hello_message = CdpNeighbourDetails.CdpNeighbourDetail.HelloMessage()
            self.hello_message.parent = self
            self._children_name_map["hello_message"] = "hello-message"
            self._children_yang_names.add("hello-message")

            self.power_available = CdpNeighbourDetails.CdpNeighbourDetail.PowerAvailable()
            self.power_available.parent = self
            self._children_name_map["power_available"] = "power-available"
            self._children_yang_names.add("power-available")

            self.power_request = CdpNeighbourDetails.CdpNeighbourDetail.PowerRequest()
            self.power_request.parent = self
            self._children_name_map["power_request"] = "power-request"
            self._children_yang_names.add("power-request")

            self.spare_pair = CdpNeighbourDetails.CdpNeighbourDetail.SparePair()
            self.spare_pair.parent = self
            self._children_name_map["spare_pair"] = "spare-pair"
            self._children_yang_names.add("spare-pair")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("device_id",
                            "adv_version",
                            "capability",
                            "clns_address",
                            "decnet_addr",
                            "device_name",
                            "duplex",
                            "ip_address",
                            "ipv6_address",
                            "local_intf_name",
                            "mgmt_address",
                            "native_vlan",
                            "novell_addr",
                            "platform_name",
                            "port_id",
                            "power",
                            "second_port_status",
                            "table_id",
                            "unidirectional_mode",
                            "version",
                            "vty_mgmt_domain",
                            "vvid",
                            "vvid_tag") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CdpNeighbourDetails.CdpNeighbourDetail, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CdpNeighbourDetails.CdpNeighbourDetail, self).__setattr__(name, value)


        class HelloMessage(Entity):
            """
            CDP Protocol Hello message
            
            .. attribute:: oui
            
            	OUI \- org unique identifier for Cisco is 0x00000C
            	**type**\:  str
            
            .. attribute:: payload_len
            
            	Payload length
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: payload_value
            
            	Payload value \- combination of the device and addresses
            	**type**\:  str
            
            .. attribute:: protocol_id
            
            	Protocol identifier. This is the identifier of the cluster
            	**type**\:  str
            
            

            """

            _prefix = 'cdp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(CdpNeighbourDetails.CdpNeighbourDetail.HelloMessage, self).__init__()

                self.yang_name = "hello-message"
                self.yang_parent_name = "cdp-neighbour-detail"

                self.oui = YLeaf(YType.str, "oui")

                self.payload_len = YLeaf(YType.uint16, "payload-len")

                self.payload_value = YLeaf(YType.str, "payload-value")

                self.protocol_id = YLeaf(YType.str, "protocol-id")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("oui",
                                "payload_len",
                                "payload_value",
                                "protocol_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CdpNeighbourDetails.CdpNeighbourDetail.HelloMessage, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CdpNeighbourDetails.CdpNeighbourDetail.HelloMessage, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.oui.is_set or
                    self.payload_len.is_set or
                    self.payload_value.is_set or
                    self.protocol_id.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.oui.yfilter != YFilter.not_set or
                    self.payload_len.yfilter != YFilter.not_set or
                    self.payload_value.yfilter != YFilter.not_set or
                    self.protocol_id.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "hello-message" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.oui.is_set or self.oui.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.oui.get_name_leafdata())
                if (self.payload_len.is_set or self.payload_len.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.payload_len.get_name_leafdata())
                if (self.payload_value.is_set or self.payload_value.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.payload_value.get_name_leafdata())
                if (self.protocol_id.is_set or self.protocol_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.protocol_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "oui" or name == "payload-len" or name == "payload-value" or name == "protocol-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "oui"):
                    self.oui = value
                    self.oui.value_namespace = name_space
                    self.oui.value_namespace_prefix = name_space_prefix
                if(value_path == "payload-len"):
                    self.payload_len = value
                    self.payload_len.value_namespace = name_space
                    self.payload_len.value_namespace_prefix = name_space_prefix
                if(value_path == "payload-value"):
                    self.payload_value = value
                    self.payload_value.value_namespace = name_space
                    self.payload_value.value_namespace_prefix = name_space_prefix
                if(value_path == "protocol-id"):
                    self.protocol_id = value
                    self.protocol_id.value_namespace = name_space
                    self.protocol_id.value_namespace_prefix = name_space_prefix


        class PowerRequest(Entity):
            """
            This field used to keep inline power
            
            .. attribute:: power_man_id
            
            	This field increments by 1 each time the Available\-Power or Management Power fields change, a power requested TLV is received with a  Request\-ID field which is different from the last received set or when  the port goes down
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: power_request_id
            
            	The last power request ID received echoes the Request\-ID field last received in a power requested TLV. It is 0 if no power requested TLV was received since the port last became active
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: power_request_level
            
            	Power to be transmitted by a powerable device in order to negotiate a suitable power level with the supplier of the network power
            	**type**\:  str
            
            

            """

            _prefix = 'cdp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(CdpNeighbourDetails.CdpNeighbourDetail.PowerRequest, self).__init__()

                self.yang_name = "power-request"
                self.yang_parent_name = "cdp-neighbour-detail"

                self.power_man_id = YLeaf(YType.uint16, "power-man-id")

                self.power_request_id = YLeaf(YType.uint16, "power-request-id")

                self.power_request_level = YLeaf(YType.str, "power-request-level")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("power_man_id",
                                "power_request_id",
                                "power_request_level") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CdpNeighbourDetails.CdpNeighbourDetail.PowerRequest, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CdpNeighbourDetails.CdpNeighbourDetail.PowerRequest, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.power_man_id.is_set or
                    self.power_request_id.is_set or
                    self.power_request_level.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.power_man_id.yfilter != YFilter.not_set or
                    self.power_request_id.yfilter != YFilter.not_set or
                    self.power_request_level.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "power-request" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.power_man_id.is_set or self.power_man_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.power_man_id.get_name_leafdata())
                if (self.power_request_id.is_set or self.power_request_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.power_request_id.get_name_leafdata())
                if (self.power_request_level.is_set or self.power_request_level.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.power_request_level.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "power-man-id" or name == "power-request-id" or name == "power-request-level"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "power-man-id"):
                    self.power_man_id = value
                    self.power_man_id.value_namespace = name_space
                    self.power_man_id.value_namespace_prefix = name_space_prefix
                if(value_path == "power-request-id"):
                    self.power_request_id = value
                    self.power_request_id.value_namespace = name_space
                    self.power_request_id.value_namespace_prefix = name_space_prefix
                if(value_path == "power-request-level"):
                    self.power_request_level = value
                    self.power_request_level.value_namespace = name_space
                    self.power_request_level.value_namespace_prefix = name_space_prefix


        class PowerAvailable(Entity):
            """
            This field used to keep inline power
            
            .. attribute:: power_available
            
            	The amount of power consumed by the specified port in watts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: power_man_id
            
            	This field increments by 1 each time the Available\-Power or Management Power fields change, a power requested TLV is received with a  Request\-ID field which is different from the last received set or when  the port goes down
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: power_man_level
            
            	Management Power Level \-\- The request of the supplier to the powered device for the power consumption TLV. The 200/300 switches always display No Preference since the switch is a power provide
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: power_request_id
            
            	The last power request ID received echoes the Request\-ID field last received in a power requested TLV. It is 0 if no power requested TLV was received since the port last became active
            	**type**\:  int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'cdp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(CdpNeighbourDetails.CdpNeighbourDetail.PowerAvailable, self).__init__()

                self.yang_name = "power-available"
                self.yang_parent_name = "cdp-neighbour-detail"

                self.power_available = YLeaf(YType.uint32, "power-available")

                self.power_man_id = YLeaf(YType.uint16, "power-man-id")

                self.power_man_level = YLeaf(YType.uint32, "power-man-level")

                self.power_request_id = YLeaf(YType.uint16, "power-request-id")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("power_available",
                                "power_man_id",
                                "power_man_level",
                                "power_request_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CdpNeighbourDetails.CdpNeighbourDetail.PowerAvailable, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CdpNeighbourDetails.CdpNeighbourDetail.PowerAvailable, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.power_available.is_set or
                    self.power_man_id.is_set or
                    self.power_man_level.is_set or
                    self.power_request_id.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.power_available.yfilter != YFilter.not_set or
                    self.power_man_id.yfilter != YFilter.not_set or
                    self.power_man_level.yfilter != YFilter.not_set or
                    self.power_request_id.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "power-available" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.power_available.is_set or self.power_available.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.power_available.get_name_leafdata())
                if (self.power_man_id.is_set or self.power_man_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.power_man_id.get_name_leafdata())
                if (self.power_man_level.is_set or self.power_man_level.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.power_man_level.get_name_leafdata())
                if (self.power_request_id.is_set or self.power_request_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.power_request_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "power-available" or name == "power-man-id" or name == "power-man-level" or name == "power-request-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "power-available"):
                    self.power_available = value
                    self.power_available.value_namespace = name_space
                    self.power_available.value_namespace_prefix = name_space_prefix
                if(value_path == "power-man-id"):
                    self.power_man_id = value
                    self.power_man_id.value_namespace = name_space
                    self.power_man_id.value_namespace_prefix = name_space_prefix
                if(value_path == "power-man-level"):
                    self.power_man_level = value
                    self.power_man_level.value_namespace = name_space
                    self.power_man_level.value_namespace_prefix = name_space_prefix
                if(value_path == "power-request-id"):
                    self.power_request_id = value
                    self.power_request_id.value_namespace = name_space
                    self.power_request_id.value_namespace_prefix = name_space_prefix


        class SparePair(Entity):
            """
            Spare pair PoE TLV is a one octet long.
            This has following field\:
            Bit            Function                            value/Meaning
            0    4\-pair PoE Supported                           0=No/1=Yes
            1    Spare pair Detection/Classification required   0=No/1=Yes
            2    PD Spare Pair Desired State                    0=Disabled/1=Enabled
            3    PSE Spare Pair Operational State               0=No/1=Yes
            4\:7   Reserved
            
            
            .. attribute:: spare_pair_detection_required
            
            	Spare pair PoE TLV is a one octet long this field represents Spare pair Detection or Classification is required or not
            	**type**\:   :py:class:`CdpYesNo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpYesNo>`
            
            .. attribute:: spare_pair_pd_config
            
            	Spare pair PoE TLV is a one octet long this field represents Powered Device(PD) Spare Pair Desired State
            	**type**\:   :py:class:`CdpEnableDisable <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpEnableDisable>`
            
            .. attribute:: spare_pair_poe
            
            	Spare pair PoE TLV is a one octet long this field represents 4\-pair PoE Supported or not
            	**type**\:   :py:class:`CdpYesNo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpYesNo>`
            
            .. attribute:: spare_pair_pse_operational
            
            	Spare pair PoE TLV is a one octet long this field represents Power Source Equipment(PSE) Spare Pair Operational State
            	**type**\:   :py:class:`CdpYesNo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpYesNo>`
            
            

            """

            _prefix = 'cdp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(CdpNeighbourDetails.CdpNeighbourDetail.SparePair, self).__init__()

                self.yang_name = "spare-pair"
                self.yang_parent_name = "cdp-neighbour-detail"

                self.spare_pair_detection_required = YLeaf(YType.enumeration, "spare-pair-detection-required")

                self.spare_pair_pd_config = YLeaf(YType.enumeration, "spare-pair-pd-config")

                self.spare_pair_poe = YLeaf(YType.enumeration, "spare-pair-poe")

                self.spare_pair_pse_operational = YLeaf(YType.enumeration, "spare-pair-pse-operational")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("spare_pair_detection_required",
                                "spare_pair_pd_config",
                                "spare_pair_poe",
                                "spare_pair_pse_operational") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CdpNeighbourDetails.CdpNeighbourDetail.SparePair, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CdpNeighbourDetails.CdpNeighbourDetail.SparePair, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.spare_pair_detection_required.is_set or
                    self.spare_pair_pd_config.is_set or
                    self.spare_pair_poe.is_set or
                    self.spare_pair_pse_operational.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.spare_pair_detection_required.yfilter != YFilter.not_set or
                    self.spare_pair_pd_config.yfilter != YFilter.not_set or
                    self.spare_pair_poe.yfilter != YFilter.not_set or
                    self.spare_pair_pse_operational.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "spare-pair" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.spare_pair_detection_required.is_set or self.spare_pair_detection_required.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.spare_pair_detection_required.get_name_leafdata())
                if (self.spare_pair_pd_config.is_set or self.spare_pair_pd_config.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.spare_pair_pd_config.get_name_leafdata())
                if (self.spare_pair_poe.is_set or self.spare_pair_poe.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.spare_pair_poe.get_name_leafdata())
                if (self.spare_pair_pse_operational.is_set or self.spare_pair_pse_operational.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.spare_pair_pse_operational.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "spare-pair-detection-required" or name == "spare-pair-pd-config" or name == "spare-pair-poe" or name == "spare-pair-pse-operational"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "spare-pair-detection-required"):
                    self.spare_pair_detection_required = value
                    self.spare_pair_detection_required.value_namespace = name_space
                    self.spare_pair_detection_required.value_namespace_prefix = name_space_prefix
                if(value_path == "spare-pair-pd-config"):
                    self.spare_pair_pd_config = value
                    self.spare_pair_pd_config.value_namespace = name_space
                    self.spare_pair_pd_config.value_namespace_prefix = name_space_prefix
                if(value_path == "spare-pair-poe"):
                    self.spare_pair_poe = value
                    self.spare_pair_poe.value_namespace = name_space
                    self.spare_pair_poe.value_namespace_prefix = name_space_prefix
                if(value_path == "spare-pair-pse-operational"):
                    self.spare_pair_pse_operational = value
                    self.spare_pair_pse_operational.value_namespace = name_space
                    self.spare_pair_pse_operational.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.device_id.is_set or
                self.adv_version.is_set or
                self.capability.is_set or
                self.clns_address.is_set or
                self.decnet_addr.is_set or
                self.device_name.is_set or
                self.duplex.is_set or
                self.ip_address.is_set or
                self.ipv6_address.is_set or
                self.local_intf_name.is_set or
                self.mgmt_address.is_set or
                self.native_vlan.is_set or
                self.novell_addr.is_set or
                self.platform_name.is_set or
                self.port_id.is_set or
                self.power.is_set or
                self.second_port_status.is_set or
                self.table_id.is_set or
                self.unidirectional_mode.is_set or
                self.version.is_set or
                self.vty_mgmt_domain.is_set or
                self.vvid.is_set or
                self.vvid_tag.is_set or
                (self.hello_message is not None and self.hello_message.has_data()) or
                (self.power_available is not None and self.power_available.has_data()) or
                (self.power_request is not None and self.power_request.has_data()) or
                (self.spare_pair is not None and self.spare_pair.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.device_id.yfilter != YFilter.not_set or
                self.adv_version.yfilter != YFilter.not_set or
                self.capability.yfilter != YFilter.not_set or
                self.clns_address.yfilter != YFilter.not_set or
                self.decnet_addr.yfilter != YFilter.not_set or
                self.device_name.yfilter != YFilter.not_set or
                self.duplex.yfilter != YFilter.not_set or
                self.ip_address.yfilter != YFilter.not_set or
                self.ipv6_address.yfilter != YFilter.not_set or
                self.local_intf_name.yfilter != YFilter.not_set or
                self.mgmt_address.yfilter != YFilter.not_set or
                self.native_vlan.yfilter != YFilter.not_set or
                self.novell_addr.yfilter != YFilter.not_set or
                self.platform_name.yfilter != YFilter.not_set or
                self.port_id.yfilter != YFilter.not_set or
                self.power.yfilter != YFilter.not_set or
                self.second_port_status.yfilter != YFilter.not_set or
                self.table_id.yfilter != YFilter.not_set or
                self.unidirectional_mode.yfilter != YFilter.not_set or
                self.version.yfilter != YFilter.not_set or
                self.vty_mgmt_domain.yfilter != YFilter.not_set or
                self.vvid.yfilter != YFilter.not_set or
                self.vvid_tag.yfilter != YFilter.not_set or
                (self.hello_message is not None and self.hello_message.has_operation()) or
                (self.power_available is not None and self.power_available.has_operation()) or
                (self.power_request is not None and self.power_request.has_operation()) or
                (self.spare_pair is not None and self.spare_pair.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cdp-neighbour-detail" + "[device-id='" + self.device_id.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-cdp-oper:cdp-neighbour-details/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.device_id.is_set or self.device_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.device_id.get_name_leafdata())
            if (self.adv_version.is_set or self.adv_version.yfilter != YFilter.not_set):
                leaf_name_data.append(self.adv_version.get_name_leafdata())
            if (self.capability.is_set or self.capability.yfilter != YFilter.not_set):
                leaf_name_data.append(self.capability.get_name_leafdata())
            if (self.clns_address.is_set or self.clns_address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.clns_address.get_name_leafdata())
            if (self.decnet_addr.is_set or self.decnet_addr.yfilter != YFilter.not_set):
                leaf_name_data.append(self.decnet_addr.get_name_leafdata())
            if (self.device_name.is_set or self.device_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.device_name.get_name_leafdata())
            if (self.duplex.is_set or self.duplex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.duplex.get_name_leafdata())
            if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ip_address.get_name_leafdata())
            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_address.get_name_leafdata())
            if (self.local_intf_name.is_set or self.local_intf_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.local_intf_name.get_name_leafdata())
            if (self.mgmt_address.is_set or self.mgmt_address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mgmt_address.get_name_leafdata())
            if (self.native_vlan.is_set or self.native_vlan.yfilter != YFilter.not_set):
                leaf_name_data.append(self.native_vlan.get_name_leafdata())
            if (self.novell_addr.is_set or self.novell_addr.yfilter != YFilter.not_set):
                leaf_name_data.append(self.novell_addr.get_name_leafdata())
            if (self.platform_name.is_set or self.platform_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.platform_name.get_name_leafdata())
            if (self.port_id.is_set or self.port_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.port_id.get_name_leafdata())
            if (self.power.is_set or self.power.yfilter != YFilter.not_set):
                leaf_name_data.append(self.power.get_name_leafdata())
            if (self.second_port_status.is_set or self.second_port_status.yfilter != YFilter.not_set):
                leaf_name_data.append(self.second_port_status.get_name_leafdata())
            if (self.table_id.is_set or self.table_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.table_id.get_name_leafdata())
            if (self.unidirectional_mode.is_set or self.unidirectional_mode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.unidirectional_mode.get_name_leafdata())
            if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                leaf_name_data.append(self.version.get_name_leafdata())
            if (self.vty_mgmt_domain.is_set or self.vty_mgmt_domain.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vty_mgmt_domain.get_name_leafdata())
            if (self.vvid.is_set or self.vvid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vvid.get_name_leafdata())
            if (self.vvid_tag.is_set or self.vvid_tag.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vvid_tag.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "hello-message"):
                if (self.hello_message is None):
                    self.hello_message = CdpNeighbourDetails.CdpNeighbourDetail.HelloMessage()
                    self.hello_message.parent = self
                    self._children_name_map["hello_message"] = "hello-message"
                return self.hello_message

            if (child_yang_name == "power-available"):
                if (self.power_available is None):
                    self.power_available = CdpNeighbourDetails.CdpNeighbourDetail.PowerAvailable()
                    self.power_available.parent = self
                    self._children_name_map["power_available"] = "power-available"
                return self.power_available

            if (child_yang_name == "power-request"):
                if (self.power_request is None):
                    self.power_request = CdpNeighbourDetails.CdpNeighbourDetail.PowerRequest()
                    self.power_request.parent = self
                    self._children_name_map["power_request"] = "power-request"
                return self.power_request

            if (child_yang_name == "spare-pair"):
                if (self.spare_pair is None):
                    self.spare_pair = CdpNeighbourDetails.CdpNeighbourDetail.SparePair()
                    self.spare_pair.parent = self
                    self._children_name_map["spare_pair"] = "spare-pair"
                return self.spare_pair

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "hello-message" or name == "power-available" or name == "power-request" or name == "spare-pair" or name == "device-id" or name == "adv-version" or name == "capability" or name == "clns-address" or name == "decnet-addr" or name == "device-name" or name == "duplex" or name == "ip-address" or name == "ipv6-address" or name == "local-intf-name" or name == "mgmt-address" or name == "native-vlan" or name == "novell-addr" or name == "platform-name" or name == "port-id" or name == "power" or name == "second-port-status" or name == "table-id" or name == "unidirectional-mode" or name == "version" or name == "vty-mgmt-domain" or name == "vvid" or name == "vvid-tag"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "device-id"):
                self.device_id = value
                self.device_id.value_namespace = name_space
                self.device_id.value_namespace_prefix = name_space_prefix
            if(value_path == "adv-version"):
                self.adv_version = value
                self.adv_version.value_namespace = name_space
                self.adv_version.value_namespace_prefix = name_space_prefix
            if(value_path == "capability"):
                self.capability = value
                self.capability.value_namespace = name_space
                self.capability.value_namespace_prefix = name_space_prefix
            if(value_path == "clns-address"):
                self.clns_address = value
                self.clns_address.value_namespace = name_space
                self.clns_address.value_namespace_prefix = name_space_prefix
            if(value_path == "decnet-addr"):
                self.decnet_addr = value
                self.decnet_addr.value_namespace = name_space
                self.decnet_addr.value_namespace_prefix = name_space_prefix
            if(value_path == "device-name"):
                self.device_name = value
                self.device_name.value_namespace = name_space
                self.device_name.value_namespace_prefix = name_space_prefix
            if(value_path == "duplex"):
                self.duplex = value
                self.duplex.value_namespace = name_space
                self.duplex.value_namespace_prefix = name_space_prefix
            if(value_path == "ip-address"):
                self.ip_address = value
                self.ip_address.value_namespace = name_space
                self.ip_address.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-address"):
                self.ipv6_address = value
                self.ipv6_address.value_namespace = name_space
                self.ipv6_address.value_namespace_prefix = name_space_prefix
            if(value_path == "local-intf-name"):
                self.local_intf_name = value
                self.local_intf_name.value_namespace = name_space
                self.local_intf_name.value_namespace_prefix = name_space_prefix
            if(value_path == "mgmt-address"):
                self.mgmt_address = value
                self.mgmt_address.value_namespace = name_space
                self.mgmt_address.value_namespace_prefix = name_space_prefix
            if(value_path == "native-vlan"):
                self.native_vlan = value
                self.native_vlan.value_namespace = name_space
                self.native_vlan.value_namespace_prefix = name_space_prefix
            if(value_path == "novell-addr"):
                self.novell_addr = value
                self.novell_addr.value_namespace = name_space
                self.novell_addr.value_namespace_prefix = name_space_prefix
            if(value_path == "platform-name"):
                self.platform_name = value
                self.platform_name.value_namespace = name_space
                self.platform_name.value_namespace_prefix = name_space_prefix
            if(value_path == "port-id"):
                self.port_id = value
                self.port_id.value_namespace = name_space
                self.port_id.value_namespace_prefix = name_space_prefix
            if(value_path == "power"):
                self.power = value
                self.power.value_namespace = name_space
                self.power.value_namespace_prefix = name_space_prefix
            if(value_path == "second-port-status"):
                self.second_port_status = value
                self.second_port_status.value_namespace = name_space
                self.second_port_status.value_namespace_prefix = name_space_prefix
            if(value_path == "table-id"):
                self.table_id = value
                self.table_id.value_namespace = name_space
                self.table_id.value_namespace_prefix = name_space_prefix
            if(value_path == "unidirectional-mode"):
                self.unidirectional_mode = value
                self.unidirectional_mode.value_namespace = name_space
                self.unidirectional_mode.value_namespace_prefix = name_space_prefix
            if(value_path == "version"):
                self.version = value
                self.version.value_namespace = name_space
                self.version.value_namespace_prefix = name_space_prefix
            if(value_path == "vty-mgmt-domain"):
                self.vty_mgmt_domain = value
                self.vty_mgmt_domain.value_namespace = name_space
                self.vty_mgmt_domain.value_namespace_prefix = name_space_prefix
            if(value_path == "vvid"):
                self.vvid = value
                self.vvid.value_namespace = name_space
                self.vvid.value_namespace_prefix = name_space_prefix
            if(value_path == "vvid-tag"):
                self.vvid_tag = value
                self.vvid_tag.value_namespace = name_space
                self.vvid_tag.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.cdp_neighbour_detail:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.cdp_neighbour_detail:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-cdp-oper:cdp-neighbour-details" + path_buffer

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

        if (child_yang_name == "cdp-neighbour-detail"):
            for c in self.cdp_neighbour_detail:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = CdpNeighbourDetails.CdpNeighbourDetail()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.cdp_neighbour_detail.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cdp-neighbour-detail"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CdpNeighbourDetails()
        return self._top_entity

