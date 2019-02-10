""" Cisco_IOS_XE_cdp_oper 

This module contains a collection of YANG definitions
for monitoring of Cisco CDP operational information.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CdpAdvVersion(Enum):
    """
    CdpAdvVersion (Enum Class)

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
    CdpDuplex (Enum Class)

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
    CdpEnableDisable (Enum Class)

    CDP type enable or disable

    .. data:: cdp_disable = 0

    .. data:: cdp_enable = 1

    """

    cdp_disable = Enum.YLeaf(0, "cdp-disable")

    cdp_enable = Enum.YLeaf(1, "cdp-enable")


class CdpUnidirectionalMode(Enum):
    """
    CdpUnidirectionalMode (Enum Class)

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
    CdpYesNo (Enum Class)

    CDP type yes or no

    .. data:: cdp_no = 0

    .. data:: cdp_yes = 1

    """

    cdp_no = Enum.YLeaf(0, "cdp-no")

    cdp_yes = Enum.YLeaf(1, "cdp-yes")



class CdpNeighborDetails(Entity):
    """
    Cisco CDP neighbor operational data
    
    .. attribute:: cdp_neighbor_detail
    
    	List of CDP neighbor details
    	**type**\: list of  		 :py:class:`CdpNeighborDetail <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpNeighborDetails.CdpNeighborDetail>`
    
    	**config**\: False
    
    

    """

    _prefix = 'cdp-ios-xe-oper'
    _revision = '2017-09-21'

    def __init__(self):
        super(CdpNeighborDetails, self).__init__()
        self._top_entity = None

        self.yang_name = "cdp-neighbor-details"
        self.yang_parent_name = "Cisco-IOS-XE-cdp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cdp-neighbor-detail", ("cdp_neighbor_detail", CdpNeighborDetails.CdpNeighborDetail))])
        self._leafs = OrderedDict()

        self.cdp_neighbor_detail = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-cdp-oper:cdp-neighbor-details"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CdpNeighborDetails, [], name, value)


    class CdpNeighborDetail(Entity):
        """
        List of CDP neighbor details
        
        .. attribute:: device_id  (key)
        
        	Device number of this device, Used as a key in the device list
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: device_name
        
        	Device name in the form of a character string. By default device ID is either the device's fully\-qualified host name (including the domain name) or the device's hardware serial number in ASCII
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: local_intf_name
        
        	The port or interface on which CDP packets are received
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: port_id
        
        	Neighbor device's port or interface on which the CDP packets are multicasted
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: capability
        
        	Identifies the functional capability of the device. The capability types that can be discovered are\: R\-Router T\-Transparent bridge B\-Source\-routing bridge S\-Switch H\-Host I\-device is using IGMP r\-Repeater
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: platform_name
        
        	Identifies the platform information of the device. For example, Cisco 4500
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: version
        
        	Version Contains the device software release information
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: duplex
        
        	Indicates the duplex configuration of the Cisco Discovery Protocol  broadcast interface. This information is used by network operators to diagnose  connectivity problems between adjacent network devices
        	**type**\:  :py:class:`CdpDuplex <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpDuplex>`
        
        	**config**\: False
        
        .. attribute:: adv_version
        
        	CDP header version of the advertisement that last filled this cache entry
        	**type**\:  :py:class:`CdpAdvVersion <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpAdvVersion>`
        
        	**config**\: False
        
        .. attribute:: hello_message
        
        	CDP Protocol Hello message
        	**type**\:  :py:class:`HelloMessage <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpNeighborDetails.CdpNeighborDetail.HelloMessage>`
        
        	**config**\: False
        
        .. attribute:: vty_mgmt_domain
        
        	Advertises the configured VLAN Trunking Protocol (VTP)\-management\-domain name of the system. This name is used by network operators to verify VTP\-domain configuration in adjacent network nodes
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: native_vlan
        
        	Indicates, per interface, the assumed VLAN for untagged packets on the interface. Cisco Discovery Protocol learns the native VLAN for an interface. This field is implemented only for interfaces that support the IEEE 802.1Q protocol Remote port's native VLAN [0..1k/4k]; 0 == not received
        	**type**\: int
        
        	**range:** 0..65535
        
        	**config**\: False
        
        .. attribute:: vvid_tag
        
        	Appliance id for appliance vlan Appliance ID \- Type of device attached to port advertised in the appliance TLV
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        .. attribute:: vvid
        
        	Appliance VLAN ID \- VLAN on the device used by the appliance, for instance if the appliance is an IP phone, this is the voice VLAN
        	**type**\: int
        
        	**range:** 0..65535
        
        	**config**\: False
        
        .. attribute:: power
        
        	This field shows the power in milliwatts device is using
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: power_request
        
        	This field used to keep inline power
        	**type**\:  :py:class:`PowerRequest <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpNeighborDetails.CdpNeighborDetail.PowerRequest>`
        
        	**config**\: False
        
        .. attribute:: power_available
        
        	This field used to keep inline power
        	**type**\:  :py:class:`PowerAvailable <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpNeighborDetails.CdpNeighborDetail.PowerAvailable>`
        
        	**config**\: False
        
        .. attribute:: unidirectional_mode
        
        	Specifies ports to unidirectionally transmit or receive traffic. Unidirectional Ethernet uses only one strand of fiber for either transmitting or receiving one\-way traffic for the GigaPort, instead of  two strands of fiber for a full\-duplex
        	**type**\:  :py:class:`CdpUnidirectionalMode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpUnidirectionalMode>`
        
        	**config**\: False
        
        .. attribute:: spare_pair
        
        	Spare pair PoE TLV is a one octet long. This has following field\: Bit            Function                            value/Meaning 0    4\-pair PoE Supported                           0=No/1=Yes 1    Spare pair Detection/Classification required   0=No/1=Yes 2    PD Spare Pair Desired State                    0=Disabled/1=Enabled 3    PSE Spare Pair Operational State               0=No/1=Yes 4\:7   Reserved 
        	**type**\:  :py:class:`SparePair <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpNeighborDetails.CdpNeighborDetail.SparePair>`
        
        	**config**\: False
        
        .. attribute:: mgmt_address
        
        	Device's management addresses
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        	**config**\: False
        
        .. attribute:: ip_address
        
        	IPv4 address of the device
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        	**config**\: False
        
        .. attribute:: ipv6_address
        
        	IPv6 address of the device
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        	**config**\: False
        
        .. attribute:: clns_address
        
        	CLNS address of the device
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: decnet_addr
        
        	DECNET address of the device
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: novell_addr
        
        	Novell address of the device. It has a 4 byte net number followed by 6 bytes of  node information
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: second_port_status
        
        	Used to keep PC port status on IP phone
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: table_id
        
        	Table id of ip routing process
        	**type**\: int
        
        	**range:** 0..65535
        
        	**config**\: False
        
        

        """

        _prefix = 'cdp-ios-xe-oper'
        _revision = '2017-09-21'

        def __init__(self):
            super(CdpNeighborDetails.CdpNeighborDetail, self).__init__()

            self.yang_name = "cdp-neighbor-detail"
            self.yang_parent_name = "cdp-neighbor-details"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['device_id']
            self._child_classes = OrderedDict([("hello-message", ("hello_message", CdpNeighborDetails.CdpNeighborDetail.HelloMessage)), ("power-request", ("power_request", CdpNeighborDetails.CdpNeighborDetail.PowerRequest)), ("power-available", ("power_available", CdpNeighborDetails.CdpNeighborDetail.PowerAvailable)), ("spare-pair", ("spare_pair", CdpNeighborDetails.CdpNeighborDetail.SparePair))])
            self._leafs = OrderedDict([
                ('device_id', (YLeaf(YType.uint32, 'device-id'), ['int'])),
                ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                ('local_intf_name', (YLeaf(YType.str, 'local-intf-name'), ['str'])),
                ('port_id', (YLeaf(YType.str, 'port-id'), ['str'])),
                ('capability', (YLeaf(YType.str, 'capability'), ['str'])),
                ('platform_name', (YLeaf(YType.str, 'platform-name'), ['str'])),
                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                ('duplex', (YLeaf(YType.enumeration, 'duplex'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper', 'CdpDuplex', '')])),
                ('adv_version', (YLeaf(YType.enumeration, 'adv-version'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper', 'CdpAdvVersion', '')])),
                ('vty_mgmt_domain', (YLeaf(YType.str, 'vty-mgmt-domain'), ['str'])),
                ('native_vlan', (YLeaf(YType.uint16, 'native-vlan'), ['int'])),
                ('vvid_tag', (YLeaf(YType.uint8, 'vvid-tag'), ['int'])),
                ('vvid', (YLeaf(YType.uint16, 'vvid'), ['int'])),
                ('power', (YLeaf(YType.uint32, 'power'), ['int'])),
                ('unidirectional_mode', (YLeaf(YType.enumeration, 'unidirectional-mode'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper', 'CdpUnidirectionalMode', '')])),
                ('mgmt_address', (YLeaf(YType.str, 'mgmt-address'), ['str','str'])),
                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str','str'])),
                ('clns_address', (YLeaf(YType.str, 'clns-address'), ['str'])),
                ('decnet_addr', (YLeaf(YType.str, 'decnet-addr'), ['str'])),
                ('novell_addr', (YLeaf(YType.str, 'novell-addr'), ['str'])),
                ('second_port_status', (YLeaf(YType.str, 'second-port-status'), ['str'])),
                ('table_id', (YLeaf(YType.uint16, 'table-id'), ['int'])),
            ])
            self.device_id = None
            self.device_name = None
            self.local_intf_name = None
            self.port_id = None
            self.capability = None
            self.platform_name = None
            self.version = None
            self.duplex = None
            self.adv_version = None
            self.vty_mgmt_domain = None
            self.native_vlan = None
            self.vvid_tag = None
            self.vvid = None
            self.power = None
            self.unidirectional_mode = None
            self.mgmt_address = None
            self.ip_address = None
            self.ipv6_address = None
            self.clns_address = None
            self.decnet_addr = None
            self.novell_addr = None
            self.second_port_status = None
            self.table_id = None

            self.hello_message = CdpNeighborDetails.CdpNeighborDetail.HelloMessage()
            self.hello_message.parent = self
            self._children_name_map["hello_message"] = "hello-message"

            self.power_request = CdpNeighborDetails.CdpNeighborDetail.PowerRequest()
            self.power_request.parent = self
            self._children_name_map["power_request"] = "power-request"

            self.power_available = CdpNeighborDetails.CdpNeighborDetail.PowerAvailable()
            self.power_available.parent = self
            self._children_name_map["power_available"] = "power-available"

            self.spare_pair = CdpNeighborDetails.CdpNeighborDetail.SparePair()
            self.spare_pair.parent = self
            self._children_name_map["spare_pair"] = "spare-pair"
            self._segment_path = lambda: "cdp-neighbor-detail" + "[device-id='" + str(self.device_id) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-cdp-oper:cdp-neighbor-details/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CdpNeighborDetails.CdpNeighborDetail, ['device_id', 'device_name', 'local_intf_name', 'port_id', 'capability', 'platform_name', 'version', 'duplex', 'adv_version', 'vty_mgmt_domain', 'native_vlan', 'vvid_tag', 'vvid', 'power', 'unidirectional_mode', 'mgmt_address', 'ip_address', 'ipv6_address', 'clns_address', 'decnet_addr', 'novell_addr', 'second_port_status', 'table_id'], name, value)


        class HelloMessage(Entity):
            """
            CDP Protocol Hello message
            
            .. attribute:: oui
            
            	OUI \- org unique identifier for Cisco is 0x00000C
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: protocol_id
            
            	Protocol identifier. This is the identifier of the cluster
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: payload_value
            
            	Payload value \- combination of the device and addresses
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: payload_len
            
            	Payload length
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            

            """

            _prefix = 'cdp-ios-xe-oper'
            _revision = '2017-09-21'

            def __init__(self):
                super(CdpNeighborDetails.CdpNeighborDetail.HelloMessage, self).__init__()

                self.yang_name = "hello-message"
                self.yang_parent_name = "cdp-neighbor-detail"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('oui', (YLeaf(YType.str, 'oui'), ['str'])),
                    ('protocol_id', (YLeaf(YType.str, 'protocol-id'), ['str'])),
                    ('payload_value', (YLeaf(YType.str, 'payload-value'), ['str'])),
                    ('payload_len', (YLeaf(YType.uint16, 'payload-len'), ['int'])),
                ])
                self.oui = None
                self.protocol_id = None
                self.payload_value = None
                self.payload_len = None
                self._segment_path = lambda: "hello-message"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CdpNeighborDetails.CdpNeighborDetail.HelloMessage, ['oui', 'protocol_id', 'payload_value', 'payload_len'], name, value)



        class PowerRequest(Entity):
            """
            This field used to keep inline power
            
            .. attribute:: power_request_id
            
            	The last power request ID received echoes the Request\-ID field last received in a power requested TLV. It is 0 if no power requested TLV was received since the port last became active
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: power_man_id
            
            	This field increments by 1 each time the Available\-Power or Management Power fields change, a power requested TLV is received with a  Request\-ID field which is different from the last received set or when  the port goes down
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: power_request_level
            
            	Power to be transmitted by a powerable device in order to negotiate a suitable power level with the supplier of the network power
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'cdp-ios-xe-oper'
            _revision = '2017-09-21'

            def __init__(self):
                super(CdpNeighborDetails.CdpNeighborDetail.PowerRequest, self).__init__()

                self.yang_name = "power-request"
                self.yang_parent_name = "cdp-neighbor-detail"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('power_request_id', (YLeaf(YType.uint16, 'power-request-id'), ['int'])),
                    ('power_man_id', (YLeaf(YType.uint16, 'power-man-id'), ['int'])),
                    ('power_request_level', (YLeaf(YType.str, 'power-request-level'), ['str'])),
                ])
                self.power_request_id = None
                self.power_man_id = None
                self.power_request_level = None
                self._segment_path = lambda: "power-request"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CdpNeighborDetails.CdpNeighborDetail.PowerRequest, ['power_request_id', 'power_man_id', 'power_request_level'], name, value)



        class PowerAvailable(Entity):
            """
            This field used to keep inline power
            
            .. attribute:: power_request_id
            
            	The last power request ID received echoes the Request\-ID field last received in a power requested TLV. It is 0 if no power requested TLV was received since the port last became active
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: power_man_id
            
            	This field increments by 1 each time the Available\-Power or Management Power fields change, a power requested TLV is received with a  Request\-ID field which is different from the last received set or when  the port goes down
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: power_available
            
            	The amount of power consumed by the specified port in watts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: power_man_level
            
            	Management Power Level \-\- The request of the supplier to the powered device for the power consumption TLV. The 200/300 switches always display No Preference since the switch is a power provide
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'cdp-ios-xe-oper'
            _revision = '2017-09-21'

            def __init__(self):
                super(CdpNeighborDetails.CdpNeighborDetail.PowerAvailable, self).__init__()

                self.yang_name = "power-available"
                self.yang_parent_name = "cdp-neighbor-detail"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('power_request_id', (YLeaf(YType.uint16, 'power-request-id'), ['int'])),
                    ('power_man_id', (YLeaf(YType.uint16, 'power-man-id'), ['int'])),
                    ('power_available', (YLeaf(YType.uint32, 'power-available'), ['int'])),
                    ('power_man_level', (YLeaf(YType.uint32, 'power-man-level'), ['int'])),
                ])
                self.power_request_id = None
                self.power_man_id = None
                self.power_available = None
                self.power_man_level = None
                self._segment_path = lambda: "power-available"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CdpNeighborDetails.CdpNeighborDetail.PowerAvailable, ['power_request_id', 'power_man_id', 'power_available', 'power_man_level'], name, value)



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
            
            
            .. attribute:: spare_pair_poe
            
            	Spare pair PoE TLV is a one octet long this field represents 4\-pair PoE Supported or not
            	**type**\:  :py:class:`CdpYesNo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpYesNo>`
            
            	**config**\: False
            
            .. attribute:: spare_pair_detection_required
            
            	Spare pair PoE TLV is a one octet long this field represents Spare pair Detection or Classification is required or not
            	**type**\:  :py:class:`CdpYesNo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpYesNo>`
            
            	**config**\: False
            
            .. attribute:: spare_pair_pd_config
            
            	Spare pair PoE TLV is a one octet long this field represents Powered Device(PD) Spare Pair Desired State
            	**type**\:  :py:class:`CdpEnableDisable <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpEnableDisable>`
            
            	**config**\: False
            
            .. attribute:: spare_pair_pse_operational
            
            	Spare pair PoE TLV is a one octet long this field represents Power Source Equipment(PSE) Spare Pair Operational State
            	**type**\:  :py:class:`CdpYesNo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper.CdpYesNo>`
            
            	**config**\: False
            
            

            """

            _prefix = 'cdp-ios-xe-oper'
            _revision = '2017-09-21'

            def __init__(self):
                super(CdpNeighborDetails.CdpNeighborDetail.SparePair, self).__init__()

                self.yang_name = "spare-pair"
                self.yang_parent_name = "cdp-neighbor-detail"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('spare_pair_poe', (YLeaf(YType.enumeration, 'spare-pair-poe'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper', 'CdpYesNo', '')])),
                    ('spare_pair_detection_required', (YLeaf(YType.enumeration, 'spare-pair-detection-required'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper', 'CdpYesNo', '')])),
                    ('spare_pair_pd_config', (YLeaf(YType.enumeration, 'spare-pair-pd-config'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper', 'CdpEnableDisable', '')])),
                    ('spare_pair_pse_operational', (YLeaf(YType.enumeration, 'spare-pair-pse-operational'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_cdp_oper', 'CdpYesNo', '')])),
                ])
                self.spare_pair_poe = None
                self.spare_pair_detection_required = None
                self.spare_pair_pd_config = None
                self.spare_pair_pse_operational = None
                self._segment_path = lambda: "spare-pair"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CdpNeighborDetails.CdpNeighborDetail.SparePair, ['spare_pair_poe', 'spare_pair_detection_required', 'spare_pair_pd_config', 'spare_pair_pse_operational'], name, value)



    def clone_ptr(self):
        self._top_entity = CdpNeighborDetails()
        return self._top_entity



