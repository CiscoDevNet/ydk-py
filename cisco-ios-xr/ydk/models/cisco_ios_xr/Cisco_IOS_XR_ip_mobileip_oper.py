""" Cisco_IOS_XR_ip_mobileip_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-mobileip package operational data.

This module contains definitions
for the following management objects\:
  pmipv6\: Proxy Mobile IPv6

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Pmipv6Addr(Enum):
    """
    Pmipv6Addr

    Address Types

    .. data:: none = 0

    	None

    .. data:: ipv4 = 1

    	IPV4 Address

    .. data:: ipv6 = 2

    	IPV6 Address

    .. data:: pmipv6_addr_ipv4_ipv6 = 3

    	Both IPV4 and IPV6 Address

    """

    none = Enum.YLeaf(0, "none")

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")

    pmipv6_addr_ipv4_ipv6 = Enum.YLeaf(3, "pmipv6-addr-ipv4-ipv6")


class Pmipv6Encap(Enum):
    """
    Pmipv6Encap

    ENCAP Types

    .. data:: none = 0

    	None

    .. data:: ipv6 = 1

    	IPV6 Tunnel

    .. data:: ipv6_ipv4 = 2

    	IPV6 in IPV4 Tunnel

    .. data:: ipv6_udp = 3

    	IPV6 in IPV4 UDP Tunnel

    .. data:: gre_ipv4 = 4

    	GRE IPV4 Tunnel

    .. data:: gre_ipv6 = 5

    	GRE IPV6 Tunnel

    .. data:: gre = 6

    	GRE Tunnel

    .. data:: mgre_ipv4 = 7

    	MGRE IPV4 Tunnel

    .. data:: mgre_ipv6 = 8

    	MGRE IPV6 Tunnel

    .. data:: mip_udp = 9

    	MIP UDP Tunnel

    .. data:: mip_mudp = 10

    	MIP MUDP Tunnel

    .. data:: max = 11

    	MAX Encap Type

    """

    none = Enum.YLeaf(0, "none")

    ipv6 = Enum.YLeaf(1, "ipv6")

    ipv6_ipv4 = Enum.YLeaf(2, "ipv6-ipv4")

    ipv6_udp = Enum.YLeaf(3, "ipv6-udp")

    gre_ipv4 = Enum.YLeaf(4, "gre-ipv4")

    gre_ipv6 = Enum.YLeaf(5, "gre-ipv6")

    gre = Enum.YLeaf(6, "gre")

    mgre_ipv4 = Enum.YLeaf(7, "mgre-ipv4")

    mgre_ipv6 = Enum.YLeaf(8, "mgre-ipv6")

    mip_udp = Enum.YLeaf(9, "mip-udp")

    mip_mudp = Enum.YLeaf(10, "mip-mudp")

    max = Enum.YLeaf(11, "max")


class Pmipv6Role(Enum):
    """
    Pmipv6Role

    PMIPV6 Role Types

    .. data:: wlan = 0

    	WLAN

    .. data:: gpp = 1

    	3GPP

    .. data:: lte = 2

    	LTE

    .. data:: wi_max = 3

    	WiMAX

    .. data:: gma = 4

    	3GMA

    .. data:: rmax = 5

    	MAX Role

    """

    wlan = Enum.YLeaf(0, "wlan")

    gpp = Enum.YLeaf(1, "gpp")

    lte = Enum.YLeaf(2, "lte")

    wi_max = Enum.YLeaf(3, "wi-max")

    gma = Enum.YLeaf(4, "gma")

    rmax = Enum.YLeaf(5, "rmax")



class Pmipv6(Entity):
    """
    Proxy Mobile IPv6
    
    .. attribute:: lma
    
    	None
    	**type**\:   :py:class:`Lma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma>`
    
    

    """

    _prefix = 'ip-mobileip-oper'
    _revision = '2016-03-10'

    def __init__(self):
        super(Pmipv6, self).__init__()
        self._top_entity = None

        self.yang_name = "pmipv6"
        self.yang_parent_name = "Cisco-IOS-XR-ip-mobileip-oper"

        self.lma = Pmipv6.Lma()
        self.lma.parent = self
        self._children_name_map["lma"] = "lma"
        self._children_yang_names.add("lma")


    class Lma(Entity):
        """
        None
        
        .. attribute:: bindings
        
        	Table of Binding
        	**type**\:   :py:class:`Bindings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Bindings>`
        
        .. attribute:: config_variables
        
        	Global Configuration Variables
        	**type**\:   :py:class:`ConfigVariables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables>`
        
        .. attribute:: heartbeats
        
        	Table of Heartbeat
        	**type**\:   :py:class:`Heartbeats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Heartbeats>`
        
        .. attribute:: statistics
        
        	None
        	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics>`
        
        

        """

        _prefix = 'ip-mobileip-oper'
        _revision = '2016-03-10'

        def __init__(self):
            super(Pmipv6.Lma, self).__init__()

            self.yang_name = "lma"
            self.yang_parent_name = "pmipv6"

            self.bindings = Pmipv6.Lma.Bindings()
            self.bindings.parent = self
            self._children_name_map["bindings"] = "bindings"
            self._children_yang_names.add("bindings")

            self.config_variables = Pmipv6.Lma.ConfigVariables()
            self.config_variables.parent = self
            self._children_name_map["config_variables"] = "config-variables"
            self._children_yang_names.add("config-variables")

            self.heartbeats = Pmipv6.Lma.Heartbeats()
            self.heartbeats.parent = self
            self._children_name_map["heartbeats"] = "heartbeats"
            self._children_yang_names.add("heartbeats")

            self.statistics = Pmipv6.Lma.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"
            self._children_yang_names.add("statistics")


        class Statistics(Entity):
            """
            None
            
            .. attribute:: customer_statistics
            
            	Table of CustomerStatistics
            	**type**\:   :py:class:`CustomerStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics>`
            
            .. attribute:: global_
            
            	Global Statistics
            	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_>`
            
            .. attribute:: mag_statistics
            
            	Table of MAGStatistics
            	**type**\:   :py:class:`MagStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics>`
            
            

            """

            _prefix = 'ip-mobileip-oper'
            _revision = '2016-03-10'

            def __init__(self):
                super(Pmipv6.Lma.Statistics, self).__init__()

                self.yang_name = "statistics"
                self.yang_parent_name = "lma"

                self.customer_statistics = Pmipv6.Lma.Statistics.CustomerStatistics()
                self.customer_statistics.parent = self
                self._children_name_map["customer_statistics"] = "customer-statistics"
                self._children_yang_names.add("customer-statistics")

                self.global_ = Pmipv6.Lma.Statistics.Global_()
                self.global_.parent = self
                self._children_name_map["global_"] = "global"
                self._children_yang_names.add("global")

                self.mag_statistics = Pmipv6.Lma.Statistics.MagStatistics()
                self.mag_statistics.parent = self
                self._children_name_map["mag_statistics"] = "mag-statistics"
                self._children_yang_names.add("mag-statistics")


            class CustomerStatistics(Entity):
                """
                Table of CustomerStatistics
                
                .. attribute:: customer_statistic
                
                	Customer statistics
                	**type**\: list of    :py:class:`CustomerStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic>`
                
                

                """

                _prefix = 'ip-mobileip-oper'
                _revision = '2016-03-10'

                def __init__(self):
                    super(Pmipv6.Lma.Statistics.CustomerStatistics, self).__init__()

                    self.yang_name = "customer-statistics"
                    self.yang_parent_name = "statistics"

                    self.customer_statistic = YList(self)

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
                                super(Pmipv6.Lma.Statistics.CustomerStatistics, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Pmipv6.Lma.Statistics.CustomerStatistics, self).__setattr__(name, value)


                class CustomerStatistic(Entity):
                    """
                    Customer statistics
                    
                    .. attribute:: customer_name  <key>
                    
                    	Customer Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: accounting_statistics
                    
                    	LMA Accounting Statistics
                    	**type**\:   :py:class:`AccountingStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.AccountingStatistics>`
                    
                    .. attribute:: bce_count
                    
                    	Count of Bindings
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: handoff_count
                    
                    	Count of Handoffs
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv4_mnp_count
                    
                    	Count of IPv4 Mobile Node Prefixes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv6_mnp_count
                    
                    	Count of IPv6 Mobile Node Prefixes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lma_identifier
                    
                    	LMA Identifier
                    	**type**\:  str
                    
                    .. attribute:: protocol_statistics
                    
                    	LMA Protocol Statistics
                    	**type**\:   :py:class:`ProtocolStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics>`
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic, self).__init__()

                        self.yang_name = "customer-statistic"
                        self.yang_parent_name = "customer-statistics"

                        self.customer_name = YLeaf(YType.str, "customer-name")

                        self.bce_count = YLeaf(YType.uint32, "bce-count")

                        self.handoff_count = YLeaf(YType.uint32, "handoff-count")

                        self.ipv4_mnp_count = YLeaf(YType.uint32, "ipv4-mnp-count")

                        self.ipv6_mnp_count = YLeaf(YType.uint32, "ipv6-mnp-count")

                        self.lma_identifier = YLeaf(YType.str, "lma-identifier")

                        self.accounting_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.AccountingStatistics()
                        self.accounting_statistics.parent = self
                        self._children_name_map["accounting_statistics"] = "accounting-statistics"
                        self._children_yang_names.add("accounting-statistics")

                        self.protocol_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics()
                        self.protocol_statistics.parent = self
                        self._children_name_map["protocol_statistics"] = "protocol-statistics"
                        self._children_yang_names.add("protocol-statistics")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("customer_name",
                                        "bce_count",
                                        "handoff_count",
                                        "ipv4_mnp_count",
                                        "ipv6_mnp_count",
                                        "lma_identifier") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic, self).__setattr__(name, value)


                    class ProtocolStatistics(Entity):
                        """
                        LMA Protocol Statistics
                        
                        .. attribute:: pba_send_statistics
                        
                        	PBA Send Statistics
                        	**type**\:   :py:class:`PbaSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbaSendStatistics>`
                        
                        .. attribute:: pbra_receive_statistics
                        
                        	PBRA Receive Statistics
                        	**type**\:   :py:class:`PbraReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraReceiveStatistics>`
                        
                        .. attribute:: pbra_send_statistics
                        
                        	PBRA Send Statistics
                        	**type**\:   :py:class:`PbraSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraSendStatistics>`
                        
                        .. attribute:: pbri_receive_statistics
                        
                        	PBRI Receive Statistics
                        	**type**\:   :py:class:`PbriReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriReceiveStatistics>`
                        
                        .. attribute:: pbri_send_statistics
                        
                        	PBRI Send Statistics
                        	**type**\:   :py:class:`PbriSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriSendStatistics>`
                        
                        .. attribute:: pbu_receive_statistics
                        
                        	PBU Receive Statistics
                        	**type**\:   :py:class:`PbuReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbuReceiveStatistics>`
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics, self).__init__()

                            self.yang_name = "protocol-statistics"
                            self.yang_parent_name = "customer-statistic"

                            self.pba_send_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbaSendStatistics()
                            self.pba_send_statistics.parent = self
                            self._children_name_map["pba_send_statistics"] = "pba-send-statistics"
                            self._children_yang_names.add("pba-send-statistics")

                            self.pbra_receive_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraReceiveStatistics()
                            self.pbra_receive_statistics.parent = self
                            self._children_name_map["pbra_receive_statistics"] = "pbra-receive-statistics"
                            self._children_yang_names.add("pbra-receive-statistics")

                            self.pbra_send_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraSendStatistics()
                            self.pbra_send_statistics.parent = self
                            self._children_name_map["pbra_send_statistics"] = "pbra-send-statistics"
                            self._children_yang_names.add("pbra-send-statistics")

                            self.pbri_receive_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriReceiveStatistics()
                            self.pbri_receive_statistics.parent = self
                            self._children_name_map["pbri_receive_statistics"] = "pbri-receive-statistics"
                            self._children_yang_names.add("pbri-receive-statistics")

                            self.pbri_send_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriSendStatistics()
                            self.pbri_send_statistics.parent = self
                            self._children_name_map["pbri_send_statistics"] = "pbri-send-statistics"
                            self._children_yang_names.add("pbri-send-statistics")

                            self.pbu_receive_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbuReceiveStatistics()
                            self.pbu_receive_statistics.parent = self
                            self._children_name_map["pbu_receive_statistics"] = "pbu-receive-statistics"
                            self._children_yang_names.add("pbu-receive-statistics")


                        class PbuReceiveStatistics(Entity):
                            """
                            PBU Receive Statistics
                            
                            .. attribute:: pbu_count
                            
                            	Count of PBUs
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbu_drop_count
                            
                            	Count of PBUs Dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbuReceiveStatistics, self).__init__()

                                self.yang_name = "pbu-receive-statistics"
                                self.yang_parent_name = "protocol-statistics"

                                self.pbu_count = YLeaf(YType.uint64, "pbu-count")

                                self.pbu_drop_count = YLeaf(YType.uint32, "pbu-drop-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("pbu_count",
                                                "pbu_drop_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbuReceiveStatistics, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbuReceiveStatistics, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.pbu_count.is_set or
                                    self.pbu_drop_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.pbu_count.yfilter != YFilter.not_set or
                                    self.pbu_drop_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pbu-receive-statistics" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.pbu_count.is_set or self.pbu_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbu_count.get_name_leafdata())
                                if (self.pbu_drop_count.is_set or self.pbu_drop_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbu_drop_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "pbu-count" or name == "pbu-drop-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "pbu-count"):
                                    self.pbu_count = value
                                    self.pbu_count.value_namespace = name_space
                                    self.pbu_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbu-drop-count"):
                                    self.pbu_drop_count = value
                                    self.pbu_drop_count.value_namespace = name_space
                                    self.pbu_drop_count.value_namespace_prefix = name_space_prefix


                        class PbaSendStatistics(Entity):
                            """
                            PBA Send Statistics
                            
                            .. attribute:: accepted_count
                            
                            	Count of Status Code \- Binding Update accepted
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: admin_failure_count
                            
                            	Count of Status Code \- Administratively prohibited
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_failure_count
                            
                            	Count of Status Code \- Auth Fail
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bad_sequence_failure_count
                            
                            	Count of Status Code \- Sequence number out of window
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: gre_key_opt_required_count
                            
                            	Count of Status Code \- GRE Key option is required
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: home_reg_failure_count
                            
                            	Count of Status Code \- Home registration not supported
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: home_subnet_failure_count
                            
                            	Count of Status Code \- Not home subnet
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: missing_access_tech_type_opt_count
                            
                            	Count of Status Code \- Missing ATT option
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: missing_hi_opt_count
                            
                            	Count of Status Code \- Missing Handoff Indicator
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: missing_hnp_opt_count
                            
                            	Count of Status Code \- Missing Home Network Prefix option
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: missing_mn_id_opt_count
                            
                            	Count of Status Code \- Missing MN identifier option
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: multiple_ipv4_ho_a_not_supported_count
                            
                            	Count of Status Code \- Multiple IPv4 HoA not supported
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_hnp_count
                            
                            	Count of Status Code \- Not authorized for HNP
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_ipv4_hoa_count
                            
                            	Count of Status Code \- Not authorized for IPv4 HoA
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_ipv4_mobility_count
                            
                            	Count of Status Code \- Not authorized for IPv4 mobility
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_ipv6_mobility_count
                            
                            	Count of Status Code \- Not authorized for IPv6 mobility
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_proxy_reg_count
                            
                            	Count of Status Code \- MAG not auth.for proxyreg
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: not_lma_for_this_mn_count
                            
                            	Count of Status Code \- Not LMA for this Mobile Node
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pba_count
                            
                            	Count of PBAs
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pba_drop_count
                            
                            	Count of PBAs dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: proxy_reg_not_enabled_count
                            
                            	Count of Status Code \- Proxy Registration not enabled
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: received_hnps_do_not_match_bce_hnps_count
                            
                            	Count of Status Code \- Recevied HNPs do not match with BCE
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: reg_type_failure_count
                            
                            	Count of Status Code \- Registration type change
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: resource_failure_count
                            
                            	Count of Status Code \- Insufficient resources
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: timestamp_lower_than_previous_accepted_count
                            
                            	Count of Status Code \- Timestamp lower than previous accepted
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: timestamp_mismatch_count
                            
                            	Count of Status Code \- Invalid timestamp value
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_count
                            
                            	Count of Status Code \- Last BA status code sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unspecified_failure_count
                            
                            	Count of Status Code \- Reason unspecified
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbaSendStatistics, self).__init__()

                                self.yang_name = "pba-send-statistics"
                                self.yang_parent_name = "protocol-statistics"

                                self.accepted_count = YLeaf(YType.uint32, "accepted-count")

                                self.admin_failure_count = YLeaf(YType.uint32, "admin-failure-count")

                                self.authen_failure_count = YLeaf(YType.uint32, "authen-failure-count")

                                self.bad_sequence_failure_count = YLeaf(YType.uint32, "bad-sequence-failure-count")

                                self.gre_key_opt_required_count = YLeaf(YType.uint32, "gre-key-opt-required-count")

                                self.home_reg_failure_count = YLeaf(YType.uint32, "home-reg-failure-count")

                                self.home_subnet_failure_count = YLeaf(YType.uint32, "home-subnet-failure-count")

                                self.missing_access_tech_type_opt_count = YLeaf(YType.uint32, "missing-access-tech-type-opt-count")

                                self.missing_hi_opt_count = YLeaf(YType.uint32, "missing-hi-opt-count")

                                self.missing_hnp_opt_count = YLeaf(YType.uint32, "missing-hnp-opt-count")

                                self.missing_mn_id_opt_count = YLeaf(YType.uint32, "missing-mn-id-opt-count")

                                self.multiple_ipv4_ho_a_not_supported_count = YLeaf(YType.uint32, "multiple-ipv4-ho-a-not-supported-count")

                                self.no_author_for_hnp_count = YLeaf(YType.uint32, "no-author-for-hnp-count")

                                self.no_author_for_ipv4_hoa_count = YLeaf(YType.uint32, "no-author-for-ipv4-hoa-count")

                                self.no_author_for_ipv4_mobility_count = YLeaf(YType.uint32, "no-author-for-ipv4-mobility-count")

                                self.no_author_for_ipv6_mobility_count = YLeaf(YType.uint32, "no-author-for-ipv6-mobility-count")

                                self.no_author_for_proxy_reg_count = YLeaf(YType.uint32, "no-author-for-proxy-reg-count")

                                self.not_lma_for_this_mn_count = YLeaf(YType.uint32, "not-lma-for-this-mn-count")

                                self.pba_count = YLeaf(YType.uint64, "pba-count")

                                self.pba_drop_count = YLeaf(YType.uint32, "pba-drop-count")

                                self.proxy_reg_not_enabled_count = YLeaf(YType.uint32, "proxy-reg-not-enabled-count")

                                self.received_hnps_do_not_match_bce_hnps_count = YLeaf(YType.uint32, "received-hnps-do-not-match-bce-hnps-count")

                                self.reg_type_failure_count = YLeaf(YType.uint32, "reg-type-failure-count")

                                self.resource_failure_count = YLeaf(YType.uint32, "resource-failure-count")

                                self.timestamp_lower_than_previous_accepted_count = YLeaf(YType.uint32, "timestamp-lower-than-previous-accepted-count")

                                self.timestamp_mismatch_count = YLeaf(YType.uint32, "timestamp-mismatch-count")

                                self.unknown_count = YLeaf(YType.uint32, "unknown-count")

                                self.unspecified_failure_count = YLeaf(YType.uint32, "unspecified-failure-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("accepted_count",
                                                "admin_failure_count",
                                                "authen_failure_count",
                                                "bad_sequence_failure_count",
                                                "gre_key_opt_required_count",
                                                "home_reg_failure_count",
                                                "home_subnet_failure_count",
                                                "missing_access_tech_type_opt_count",
                                                "missing_hi_opt_count",
                                                "missing_hnp_opt_count",
                                                "missing_mn_id_opt_count",
                                                "multiple_ipv4_ho_a_not_supported_count",
                                                "no_author_for_hnp_count",
                                                "no_author_for_ipv4_hoa_count",
                                                "no_author_for_ipv4_mobility_count",
                                                "no_author_for_ipv6_mobility_count",
                                                "no_author_for_proxy_reg_count",
                                                "not_lma_for_this_mn_count",
                                                "pba_count",
                                                "pba_drop_count",
                                                "proxy_reg_not_enabled_count",
                                                "received_hnps_do_not_match_bce_hnps_count",
                                                "reg_type_failure_count",
                                                "resource_failure_count",
                                                "timestamp_lower_than_previous_accepted_count",
                                                "timestamp_mismatch_count",
                                                "unknown_count",
                                                "unspecified_failure_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbaSendStatistics, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbaSendStatistics, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.accepted_count.is_set or
                                    self.admin_failure_count.is_set or
                                    self.authen_failure_count.is_set or
                                    self.bad_sequence_failure_count.is_set or
                                    self.gre_key_opt_required_count.is_set or
                                    self.home_reg_failure_count.is_set or
                                    self.home_subnet_failure_count.is_set or
                                    self.missing_access_tech_type_opt_count.is_set or
                                    self.missing_hi_opt_count.is_set or
                                    self.missing_hnp_opt_count.is_set or
                                    self.missing_mn_id_opt_count.is_set or
                                    self.multiple_ipv4_ho_a_not_supported_count.is_set or
                                    self.no_author_for_hnp_count.is_set or
                                    self.no_author_for_ipv4_hoa_count.is_set or
                                    self.no_author_for_ipv4_mobility_count.is_set or
                                    self.no_author_for_ipv6_mobility_count.is_set or
                                    self.no_author_for_proxy_reg_count.is_set or
                                    self.not_lma_for_this_mn_count.is_set or
                                    self.pba_count.is_set or
                                    self.pba_drop_count.is_set or
                                    self.proxy_reg_not_enabled_count.is_set or
                                    self.received_hnps_do_not_match_bce_hnps_count.is_set or
                                    self.reg_type_failure_count.is_set or
                                    self.resource_failure_count.is_set or
                                    self.timestamp_lower_than_previous_accepted_count.is_set or
                                    self.timestamp_mismatch_count.is_set or
                                    self.unknown_count.is_set or
                                    self.unspecified_failure_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.accepted_count.yfilter != YFilter.not_set or
                                    self.admin_failure_count.yfilter != YFilter.not_set or
                                    self.authen_failure_count.yfilter != YFilter.not_set or
                                    self.bad_sequence_failure_count.yfilter != YFilter.not_set or
                                    self.gre_key_opt_required_count.yfilter != YFilter.not_set or
                                    self.home_reg_failure_count.yfilter != YFilter.not_set or
                                    self.home_subnet_failure_count.yfilter != YFilter.not_set or
                                    self.missing_access_tech_type_opt_count.yfilter != YFilter.not_set or
                                    self.missing_hi_opt_count.yfilter != YFilter.not_set or
                                    self.missing_hnp_opt_count.yfilter != YFilter.not_set or
                                    self.missing_mn_id_opt_count.yfilter != YFilter.not_set or
                                    self.multiple_ipv4_ho_a_not_supported_count.yfilter != YFilter.not_set or
                                    self.no_author_for_hnp_count.yfilter != YFilter.not_set or
                                    self.no_author_for_ipv4_hoa_count.yfilter != YFilter.not_set or
                                    self.no_author_for_ipv4_mobility_count.yfilter != YFilter.not_set or
                                    self.no_author_for_ipv6_mobility_count.yfilter != YFilter.not_set or
                                    self.no_author_for_proxy_reg_count.yfilter != YFilter.not_set or
                                    self.not_lma_for_this_mn_count.yfilter != YFilter.not_set or
                                    self.pba_count.yfilter != YFilter.not_set or
                                    self.pba_drop_count.yfilter != YFilter.not_set or
                                    self.proxy_reg_not_enabled_count.yfilter != YFilter.not_set or
                                    self.received_hnps_do_not_match_bce_hnps_count.yfilter != YFilter.not_set or
                                    self.reg_type_failure_count.yfilter != YFilter.not_set or
                                    self.resource_failure_count.yfilter != YFilter.not_set or
                                    self.timestamp_lower_than_previous_accepted_count.yfilter != YFilter.not_set or
                                    self.timestamp_mismatch_count.yfilter != YFilter.not_set or
                                    self.unknown_count.yfilter != YFilter.not_set or
                                    self.unspecified_failure_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pba-send-statistics" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.accepted_count.is_set or self.accepted_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.accepted_count.get_name_leafdata())
                                if (self.admin_failure_count.is_set or self.admin_failure_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.admin_failure_count.get_name_leafdata())
                                if (self.authen_failure_count.is_set or self.authen_failure_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.authen_failure_count.get_name_leafdata())
                                if (self.bad_sequence_failure_count.is_set or self.bad_sequence_failure_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bad_sequence_failure_count.get_name_leafdata())
                                if (self.gre_key_opt_required_count.is_set or self.gre_key_opt_required_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.gre_key_opt_required_count.get_name_leafdata())
                                if (self.home_reg_failure_count.is_set or self.home_reg_failure_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.home_reg_failure_count.get_name_leafdata())
                                if (self.home_subnet_failure_count.is_set or self.home_subnet_failure_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.home_subnet_failure_count.get_name_leafdata())
                                if (self.missing_access_tech_type_opt_count.is_set or self.missing_access_tech_type_opt_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.missing_access_tech_type_opt_count.get_name_leafdata())
                                if (self.missing_hi_opt_count.is_set or self.missing_hi_opt_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.missing_hi_opt_count.get_name_leafdata())
                                if (self.missing_hnp_opt_count.is_set or self.missing_hnp_opt_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.missing_hnp_opt_count.get_name_leafdata())
                                if (self.missing_mn_id_opt_count.is_set or self.missing_mn_id_opt_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.missing_mn_id_opt_count.get_name_leafdata())
                                if (self.multiple_ipv4_ho_a_not_supported_count.is_set or self.multiple_ipv4_ho_a_not_supported_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.multiple_ipv4_ho_a_not_supported_count.get_name_leafdata())
                                if (self.no_author_for_hnp_count.is_set or self.no_author_for_hnp_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_author_for_hnp_count.get_name_leafdata())
                                if (self.no_author_for_ipv4_hoa_count.is_set or self.no_author_for_ipv4_hoa_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_author_for_ipv4_hoa_count.get_name_leafdata())
                                if (self.no_author_for_ipv4_mobility_count.is_set or self.no_author_for_ipv4_mobility_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_author_for_ipv4_mobility_count.get_name_leafdata())
                                if (self.no_author_for_ipv6_mobility_count.is_set or self.no_author_for_ipv6_mobility_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_author_for_ipv6_mobility_count.get_name_leafdata())
                                if (self.no_author_for_proxy_reg_count.is_set or self.no_author_for_proxy_reg_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_author_for_proxy_reg_count.get_name_leafdata())
                                if (self.not_lma_for_this_mn_count.is_set or self.not_lma_for_this_mn_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.not_lma_for_this_mn_count.get_name_leafdata())
                                if (self.pba_count.is_set or self.pba_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pba_count.get_name_leafdata())
                                if (self.pba_drop_count.is_set or self.pba_drop_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pba_drop_count.get_name_leafdata())
                                if (self.proxy_reg_not_enabled_count.is_set or self.proxy_reg_not_enabled_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.proxy_reg_not_enabled_count.get_name_leafdata())
                                if (self.received_hnps_do_not_match_bce_hnps_count.is_set or self.received_hnps_do_not_match_bce_hnps_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.received_hnps_do_not_match_bce_hnps_count.get_name_leafdata())
                                if (self.reg_type_failure_count.is_set or self.reg_type_failure_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.reg_type_failure_count.get_name_leafdata())
                                if (self.resource_failure_count.is_set or self.resource_failure_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.resource_failure_count.get_name_leafdata())
                                if (self.timestamp_lower_than_previous_accepted_count.is_set or self.timestamp_lower_than_previous_accepted_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.timestamp_lower_than_previous_accepted_count.get_name_leafdata())
                                if (self.timestamp_mismatch_count.is_set or self.timestamp_mismatch_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.timestamp_mismatch_count.get_name_leafdata())
                                if (self.unknown_count.is_set or self.unknown_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unknown_count.get_name_leafdata())
                                if (self.unspecified_failure_count.is_set or self.unspecified_failure_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unspecified_failure_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "accepted-count" or name == "admin-failure-count" or name == "authen-failure-count" or name == "bad-sequence-failure-count" or name == "gre-key-opt-required-count" or name == "home-reg-failure-count" or name == "home-subnet-failure-count" or name == "missing-access-tech-type-opt-count" or name == "missing-hi-opt-count" or name == "missing-hnp-opt-count" or name == "missing-mn-id-opt-count" or name == "multiple-ipv4-ho-a-not-supported-count" or name == "no-author-for-hnp-count" or name == "no-author-for-ipv4-hoa-count" or name == "no-author-for-ipv4-mobility-count" or name == "no-author-for-ipv6-mobility-count" or name == "no-author-for-proxy-reg-count" or name == "not-lma-for-this-mn-count" or name == "pba-count" or name == "pba-drop-count" or name == "proxy-reg-not-enabled-count" or name == "received-hnps-do-not-match-bce-hnps-count" or name == "reg-type-failure-count" or name == "resource-failure-count" or name == "timestamp-lower-than-previous-accepted-count" or name == "timestamp-mismatch-count" or name == "unknown-count" or name == "unspecified-failure-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "accepted-count"):
                                    self.accepted_count = value
                                    self.accepted_count.value_namespace = name_space
                                    self.accepted_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "admin-failure-count"):
                                    self.admin_failure_count = value
                                    self.admin_failure_count.value_namespace = name_space
                                    self.admin_failure_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "authen-failure-count"):
                                    self.authen_failure_count = value
                                    self.authen_failure_count.value_namespace = name_space
                                    self.authen_failure_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "bad-sequence-failure-count"):
                                    self.bad_sequence_failure_count = value
                                    self.bad_sequence_failure_count.value_namespace = name_space
                                    self.bad_sequence_failure_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "gre-key-opt-required-count"):
                                    self.gre_key_opt_required_count = value
                                    self.gre_key_opt_required_count.value_namespace = name_space
                                    self.gre_key_opt_required_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "home-reg-failure-count"):
                                    self.home_reg_failure_count = value
                                    self.home_reg_failure_count.value_namespace = name_space
                                    self.home_reg_failure_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "home-subnet-failure-count"):
                                    self.home_subnet_failure_count = value
                                    self.home_subnet_failure_count.value_namespace = name_space
                                    self.home_subnet_failure_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "missing-access-tech-type-opt-count"):
                                    self.missing_access_tech_type_opt_count = value
                                    self.missing_access_tech_type_opt_count.value_namespace = name_space
                                    self.missing_access_tech_type_opt_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "missing-hi-opt-count"):
                                    self.missing_hi_opt_count = value
                                    self.missing_hi_opt_count.value_namespace = name_space
                                    self.missing_hi_opt_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "missing-hnp-opt-count"):
                                    self.missing_hnp_opt_count = value
                                    self.missing_hnp_opt_count.value_namespace = name_space
                                    self.missing_hnp_opt_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "missing-mn-id-opt-count"):
                                    self.missing_mn_id_opt_count = value
                                    self.missing_mn_id_opt_count.value_namespace = name_space
                                    self.missing_mn_id_opt_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "multiple-ipv4-ho-a-not-supported-count"):
                                    self.multiple_ipv4_ho_a_not_supported_count = value
                                    self.multiple_ipv4_ho_a_not_supported_count.value_namespace = name_space
                                    self.multiple_ipv4_ho_a_not_supported_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-author-for-hnp-count"):
                                    self.no_author_for_hnp_count = value
                                    self.no_author_for_hnp_count.value_namespace = name_space
                                    self.no_author_for_hnp_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-author-for-ipv4-hoa-count"):
                                    self.no_author_for_ipv4_hoa_count = value
                                    self.no_author_for_ipv4_hoa_count.value_namespace = name_space
                                    self.no_author_for_ipv4_hoa_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-author-for-ipv4-mobility-count"):
                                    self.no_author_for_ipv4_mobility_count = value
                                    self.no_author_for_ipv4_mobility_count.value_namespace = name_space
                                    self.no_author_for_ipv4_mobility_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-author-for-ipv6-mobility-count"):
                                    self.no_author_for_ipv6_mobility_count = value
                                    self.no_author_for_ipv6_mobility_count.value_namespace = name_space
                                    self.no_author_for_ipv6_mobility_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-author-for-proxy-reg-count"):
                                    self.no_author_for_proxy_reg_count = value
                                    self.no_author_for_proxy_reg_count.value_namespace = name_space
                                    self.no_author_for_proxy_reg_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "not-lma-for-this-mn-count"):
                                    self.not_lma_for_this_mn_count = value
                                    self.not_lma_for_this_mn_count.value_namespace = name_space
                                    self.not_lma_for_this_mn_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pba-count"):
                                    self.pba_count = value
                                    self.pba_count.value_namespace = name_space
                                    self.pba_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pba-drop-count"):
                                    self.pba_drop_count = value
                                    self.pba_drop_count.value_namespace = name_space
                                    self.pba_drop_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "proxy-reg-not-enabled-count"):
                                    self.proxy_reg_not_enabled_count = value
                                    self.proxy_reg_not_enabled_count.value_namespace = name_space
                                    self.proxy_reg_not_enabled_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "received-hnps-do-not-match-bce-hnps-count"):
                                    self.received_hnps_do_not_match_bce_hnps_count = value
                                    self.received_hnps_do_not_match_bce_hnps_count.value_namespace = name_space
                                    self.received_hnps_do_not_match_bce_hnps_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "reg-type-failure-count"):
                                    self.reg_type_failure_count = value
                                    self.reg_type_failure_count.value_namespace = name_space
                                    self.reg_type_failure_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "resource-failure-count"):
                                    self.resource_failure_count = value
                                    self.resource_failure_count.value_namespace = name_space
                                    self.resource_failure_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "timestamp-lower-than-previous-accepted-count"):
                                    self.timestamp_lower_than_previous_accepted_count = value
                                    self.timestamp_lower_than_previous_accepted_count.value_namespace = name_space
                                    self.timestamp_lower_than_previous_accepted_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "timestamp-mismatch-count"):
                                    self.timestamp_mismatch_count = value
                                    self.timestamp_mismatch_count.value_namespace = name_space
                                    self.timestamp_mismatch_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "unknown-count"):
                                    self.unknown_count = value
                                    self.unknown_count.value_namespace = name_space
                                    self.unknown_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "unspecified-failure-count"):
                                    self.unspecified_failure_count = value
                                    self.unspecified_failure_count.value_namespace = name_space
                                    self.unspecified_failure_count.value_namespace_prefix = name_space_prefix


                        class PbriSendStatistics(Entity):
                            """
                            PBRI Send Statistics
                            
                            .. attribute:: admin_reason_count
                            
                            	Count of Revoc Trigger \- Administrative Reason
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_different_att_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Different ATT
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_same_att_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Same ATT
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_unknown_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Unknown
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: network_session_termination_count
                            
                            	Count of Revoc Trigger \- Access Network Session Termination
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_of_sync_bce_state_count
                            
                            	Count of Revoc Trigger \- Possible Out\-of\-Sync BCE State
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pbri_count
                            
                            	Count of PBRIs
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbri_drop_count
                            
                            	Count of PBRIs dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: per_peer_policy_count
                            
                            	Count of Revoc Trigger \- Per\-Peer Policy
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: revoking_mn_local_policy_count
                            
                            	Count of Revoc Trigger \- Revoking Mobility Node Local Policy
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unspecified_count
                            
                            	Count of Revoc Trigger \- Unspecified
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: user_session_termination_count
                            
                            	Count of Revoc Trigger \- User Init Session Terminatation
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriSendStatistics, self).__init__()

                                self.yang_name = "pbri-send-statistics"
                                self.yang_parent_name = "protocol-statistics"

                                self.admin_reason_count = YLeaf(YType.uint32, "admin-reason-count")

                                self.mag_handover_different_att_count = YLeaf(YType.uint32, "mag-handover-different-att-count")

                                self.mag_handover_same_att_count = YLeaf(YType.uint32, "mag-handover-same-att-count")

                                self.mag_handover_unknown_count = YLeaf(YType.uint32, "mag-handover-unknown-count")

                                self.network_session_termination_count = YLeaf(YType.uint32, "network-session-termination-count")

                                self.out_of_sync_bce_state_count = YLeaf(YType.uint32, "out-of-sync-bce-state-count")

                                self.pbri_count = YLeaf(YType.uint64, "pbri-count")

                                self.pbri_drop_count = YLeaf(YType.uint32, "pbri-drop-count")

                                self.per_peer_policy_count = YLeaf(YType.uint32, "per-peer-policy-count")

                                self.revoking_mn_local_policy_count = YLeaf(YType.uint32, "revoking-mn-local-policy-count")

                                self.unspecified_count = YLeaf(YType.uint32, "unspecified-count")

                                self.user_session_termination_count = YLeaf(YType.uint32, "user-session-termination-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("admin_reason_count",
                                                "mag_handover_different_att_count",
                                                "mag_handover_same_att_count",
                                                "mag_handover_unknown_count",
                                                "network_session_termination_count",
                                                "out_of_sync_bce_state_count",
                                                "pbri_count",
                                                "pbri_drop_count",
                                                "per_peer_policy_count",
                                                "revoking_mn_local_policy_count",
                                                "unspecified_count",
                                                "user_session_termination_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriSendStatistics, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriSendStatistics, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.admin_reason_count.is_set or
                                    self.mag_handover_different_att_count.is_set or
                                    self.mag_handover_same_att_count.is_set or
                                    self.mag_handover_unknown_count.is_set or
                                    self.network_session_termination_count.is_set or
                                    self.out_of_sync_bce_state_count.is_set or
                                    self.pbri_count.is_set or
                                    self.pbri_drop_count.is_set or
                                    self.per_peer_policy_count.is_set or
                                    self.revoking_mn_local_policy_count.is_set or
                                    self.unspecified_count.is_set or
                                    self.user_session_termination_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.admin_reason_count.yfilter != YFilter.not_set or
                                    self.mag_handover_different_att_count.yfilter != YFilter.not_set or
                                    self.mag_handover_same_att_count.yfilter != YFilter.not_set or
                                    self.mag_handover_unknown_count.yfilter != YFilter.not_set or
                                    self.network_session_termination_count.yfilter != YFilter.not_set or
                                    self.out_of_sync_bce_state_count.yfilter != YFilter.not_set or
                                    self.pbri_count.yfilter != YFilter.not_set or
                                    self.pbri_drop_count.yfilter != YFilter.not_set or
                                    self.per_peer_policy_count.yfilter != YFilter.not_set or
                                    self.revoking_mn_local_policy_count.yfilter != YFilter.not_set or
                                    self.unspecified_count.yfilter != YFilter.not_set or
                                    self.user_session_termination_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pbri-send-statistics" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.admin_reason_count.is_set or self.admin_reason_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.admin_reason_count.get_name_leafdata())
                                if (self.mag_handover_different_att_count.is_set or self.mag_handover_different_att_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mag_handover_different_att_count.get_name_leafdata())
                                if (self.mag_handover_same_att_count.is_set or self.mag_handover_same_att_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mag_handover_same_att_count.get_name_leafdata())
                                if (self.mag_handover_unknown_count.is_set or self.mag_handover_unknown_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mag_handover_unknown_count.get_name_leafdata())
                                if (self.network_session_termination_count.is_set or self.network_session_termination_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.network_session_termination_count.get_name_leafdata())
                                if (self.out_of_sync_bce_state_count.is_set or self.out_of_sync_bce_state_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_of_sync_bce_state_count.get_name_leafdata())
                                if (self.pbri_count.is_set or self.pbri_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbri_count.get_name_leafdata())
                                if (self.pbri_drop_count.is_set or self.pbri_drop_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbri_drop_count.get_name_leafdata())
                                if (self.per_peer_policy_count.is_set or self.per_peer_policy_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.per_peer_policy_count.get_name_leafdata())
                                if (self.revoking_mn_local_policy_count.is_set or self.revoking_mn_local_policy_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.revoking_mn_local_policy_count.get_name_leafdata())
                                if (self.unspecified_count.is_set or self.unspecified_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unspecified_count.get_name_leafdata())
                                if (self.user_session_termination_count.is_set or self.user_session_termination_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.user_session_termination_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "admin-reason-count" or name == "mag-handover-different-att-count" or name == "mag-handover-same-att-count" or name == "mag-handover-unknown-count" or name == "network-session-termination-count" or name == "out-of-sync-bce-state-count" or name == "pbri-count" or name == "pbri-drop-count" or name == "per-peer-policy-count" or name == "revoking-mn-local-policy-count" or name == "unspecified-count" or name == "user-session-termination-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "admin-reason-count"):
                                    self.admin_reason_count = value
                                    self.admin_reason_count.value_namespace = name_space
                                    self.admin_reason_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mag-handover-different-att-count"):
                                    self.mag_handover_different_att_count = value
                                    self.mag_handover_different_att_count.value_namespace = name_space
                                    self.mag_handover_different_att_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mag-handover-same-att-count"):
                                    self.mag_handover_same_att_count = value
                                    self.mag_handover_same_att_count.value_namespace = name_space
                                    self.mag_handover_same_att_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mag-handover-unknown-count"):
                                    self.mag_handover_unknown_count = value
                                    self.mag_handover_unknown_count.value_namespace = name_space
                                    self.mag_handover_unknown_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "network-session-termination-count"):
                                    self.network_session_termination_count = value
                                    self.network_session_termination_count.value_namespace = name_space
                                    self.network_session_termination_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-of-sync-bce-state-count"):
                                    self.out_of_sync_bce_state_count = value
                                    self.out_of_sync_bce_state_count.value_namespace = name_space
                                    self.out_of_sync_bce_state_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbri-count"):
                                    self.pbri_count = value
                                    self.pbri_count.value_namespace = name_space
                                    self.pbri_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbri-drop-count"):
                                    self.pbri_drop_count = value
                                    self.pbri_drop_count.value_namespace = name_space
                                    self.pbri_drop_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "per-peer-policy-count"):
                                    self.per_peer_policy_count = value
                                    self.per_peer_policy_count.value_namespace = name_space
                                    self.per_peer_policy_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "revoking-mn-local-policy-count"):
                                    self.revoking_mn_local_policy_count = value
                                    self.revoking_mn_local_policy_count.value_namespace = name_space
                                    self.revoking_mn_local_policy_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "unspecified-count"):
                                    self.unspecified_count = value
                                    self.unspecified_count.value_namespace = name_space
                                    self.unspecified_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "user-session-termination-count"):
                                    self.user_session_termination_count = value
                                    self.user_session_termination_count.value_namespace = name_space
                                    self.user_session_termination_count.value_namespace_prefix = name_space_prefix


                        class PbriReceiveStatistics(Entity):
                            """
                            PBRI Receive Statistics
                            
                            .. attribute:: admin_reason_count
                            
                            	Count of Revoc Trigger \- Administrative Reason
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_different_att_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Different ATT
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_same_att_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Same ATT
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_unknown_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Unknown
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: network_session_termination_count
                            
                            	Count of Revoc Trigger \- Access Network Session Termination
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_of_sync_bce_state_count
                            
                            	Count of Revoc Trigger \- Possible Out\-of\-Sync BCE State
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pbri_count
                            
                            	Count of PBRIs
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbri_drop_count
                            
                            	Count of PBRIs dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: per_peer_policy_count
                            
                            	Count of Revoc Trigger \- Per\-Peer Policy
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: revoking_mn_local_policy_count
                            
                            	Count of Revoc Trigger \- Revoking Mobility Node Local Policy
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unspecified_count
                            
                            	Count of Revoc Trigger \- Unspecified
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: user_session_termination_count
                            
                            	Count of Revoc Trigger \- User Init Session Terminatation
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriReceiveStatistics, self).__init__()

                                self.yang_name = "pbri-receive-statistics"
                                self.yang_parent_name = "protocol-statistics"

                                self.admin_reason_count = YLeaf(YType.uint32, "admin-reason-count")

                                self.mag_handover_different_att_count = YLeaf(YType.uint32, "mag-handover-different-att-count")

                                self.mag_handover_same_att_count = YLeaf(YType.uint32, "mag-handover-same-att-count")

                                self.mag_handover_unknown_count = YLeaf(YType.uint32, "mag-handover-unknown-count")

                                self.network_session_termination_count = YLeaf(YType.uint32, "network-session-termination-count")

                                self.out_of_sync_bce_state_count = YLeaf(YType.uint32, "out-of-sync-bce-state-count")

                                self.pbri_count = YLeaf(YType.uint64, "pbri-count")

                                self.pbri_drop_count = YLeaf(YType.uint32, "pbri-drop-count")

                                self.per_peer_policy_count = YLeaf(YType.uint32, "per-peer-policy-count")

                                self.revoking_mn_local_policy_count = YLeaf(YType.uint32, "revoking-mn-local-policy-count")

                                self.unspecified_count = YLeaf(YType.uint32, "unspecified-count")

                                self.user_session_termination_count = YLeaf(YType.uint32, "user-session-termination-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("admin_reason_count",
                                                "mag_handover_different_att_count",
                                                "mag_handover_same_att_count",
                                                "mag_handover_unknown_count",
                                                "network_session_termination_count",
                                                "out_of_sync_bce_state_count",
                                                "pbri_count",
                                                "pbri_drop_count",
                                                "per_peer_policy_count",
                                                "revoking_mn_local_policy_count",
                                                "unspecified_count",
                                                "user_session_termination_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriReceiveStatistics, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriReceiveStatistics, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.admin_reason_count.is_set or
                                    self.mag_handover_different_att_count.is_set or
                                    self.mag_handover_same_att_count.is_set or
                                    self.mag_handover_unknown_count.is_set or
                                    self.network_session_termination_count.is_set or
                                    self.out_of_sync_bce_state_count.is_set or
                                    self.pbri_count.is_set or
                                    self.pbri_drop_count.is_set or
                                    self.per_peer_policy_count.is_set or
                                    self.revoking_mn_local_policy_count.is_set or
                                    self.unspecified_count.is_set or
                                    self.user_session_termination_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.admin_reason_count.yfilter != YFilter.not_set or
                                    self.mag_handover_different_att_count.yfilter != YFilter.not_set or
                                    self.mag_handover_same_att_count.yfilter != YFilter.not_set or
                                    self.mag_handover_unknown_count.yfilter != YFilter.not_set or
                                    self.network_session_termination_count.yfilter != YFilter.not_set or
                                    self.out_of_sync_bce_state_count.yfilter != YFilter.not_set or
                                    self.pbri_count.yfilter != YFilter.not_set or
                                    self.pbri_drop_count.yfilter != YFilter.not_set or
                                    self.per_peer_policy_count.yfilter != YFilter.not_set or
                                    self.revoking_mn_local_policy_count.yfilter != YFilter.not_set or
                                    self.unspecified_count.yfilter != YFilter.not_set or
                                    self.user_session_termination_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pbri-receive-statistics" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.admin_reason_count.is_set or self.admin_reason_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.admin_reason_count.get_name_leafdata())
                                if (self.mag_handover_different_att_count.is_set or self.mag_handover_different_att_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mag_handover_different_att_count.get_name_leafdata())
                                if (self.mag_handover_same_att_count.is_set or self.mag_handover_same_att_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mag_handover_same_att_count.get_name_leafdata())
                                if (self.mag_handover_unknown_count.is_set or self.mag_handover_unknown_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mag_handover_unknown_count.get_name_leafdata())
                                if (self.network_session_termination_count.is_set or self.network_session_termination_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.network_session_termination_count.get_name_leafdata())
                                if (self.out_of_sync_bce_state_count.is_set or self.out_of_sync_bce_state_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_of_sync_bce_state_count.get_name_leafdata())
                                if (self.pbri_count.is_set or self.pbri_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbri_count.get_name_leafdata())
                                if (self.pbri_drop_count.is_set or self.pbri_drop_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbri_drop_count.get_name_leafdata())
                                if (self.per_peer_policy_count.is_set or self.per_peer_policy_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.per_peer_policy_count.get_name_leafdata())
                                if (self.revoking_mn_local_policy_count.is_set or self.revoking_mn_local_policy_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.revoking_mn_local_policy_count.get_name_leafdata())
                                if (self.unspecified_count.is_set or self.unspecified_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unspecified_count.get_name_leafdata())
                                if (self.user_session_termination_count.is_set or self.user_session_termination_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.user_session_termination_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "admin-reason-count" or name == "mag-handover-different-att-count" or name == "mag-handover-same-att-count" or name == "mag-handover-unknown-count" or name == "network-session-termination-count" or name == "out-of-sync-bce-state-count" or name == "pbri-count" or name == "pbri-drop-count" or name == "per-peer-policy-count" or name == "revoking-mn-local-policy-count" or name == "unspecified-count" or name == "user-session-termination-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "admin-reason-count"):
                                    self.admin_reason_count = value
                                    self.admin_reason_count.value_namespace = name_space
                                    self.admin_reason_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mag-handover-different-att-count"):
                                    self.mag_handover_different_att_count = value
                                    self.mag_handover_different_att_count.value_namespace = name_space
                                    self.mag_handover_different_att_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mag-handover-same-att-count"):
                                    self.mag_handover_same_att_count = value
                                    self.mag_handover_same_att_count.value_namespace = name_space
                                    self.mag_handover_same_att_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mag-handover-unknown-count"):
                                    self.mag_handover_unknown_count = value
                                    self.mag_handover_unknown_count.value_namespace = name_space
                                    self.mag_handover_unknown_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "network-session-termination-count"):
                                    self.network_session_termination_count = value
                                    self.network_session_termination_count.value_namespace = name_space
                                    self.network_session_termination_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-of-sync-bce-state-count"):
                                    self.out_of_sync_bce_state_count = value
                                    self.out_of_sync_bce_state_count.value_namespace = name_space
                                    self.out_of_sync_bce_state_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbri-count"):
                                    self.pbri_count = value
                                    self.pbri_count.value_namespace = name_space
                                    self.pbri_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbri-drop-count"):
                                    self.pbri_drop_count = value
                                    self.pbri_drop_count.value_namespace = name_space
                                    self.pbri_drop_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "per-peer-policy-count"):
                                    self.per_peer_policy_count = value
                                    self.per_peer_policy_count.value_namespace = name_space
                                    self.per_peer_policy_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "revoking-mn-local-policy-count"):
                                    self.revoking_mn_local_policy_count = value
                                    self.revoking_mn_local_policy_count.value_namespace = name_space
                                    self.revoking_mn_local_policy_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "unspecified-count"):
                                    self.unspecified_count = value
                                    self.unspecified_count.value_namespace = name_space
                                    self.unspecified_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "user-session-termination-count"):
                                    self.user_session_termination_count = value
                                    self.user_session_termination_count.value_namespace = name_space
                                    self.user_session_termination_count.value_namespace_prefix = name_space_prefix


                        class PbraSendStatistics(Entity):
                            """
                            PBRA Send Statistics
                            
                            .. attribute:: hoa_required_count
                            
                            	Count of Revoc Status \- IPv4 Home Address Option Required
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mn_attached_count
                            
                            	Count of Revoc Status \- Revocation Failed \- MN is Attached
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mn_identity_required_count
                            
                            	Count of Revoc Status \- Revoked Mobile Node Identity Required
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_global_revoc_count
                            
                            	Count of Revoc Status \- Global Revocation NOT Authorized
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_binding_count
                            
                            	Count of Revoc Status \- Binding Does Not Exist
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: partial_success_count
                            
                            	Count of Revoc Status \- Partial Success
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pbr_not_supported_count
                            
                            	Count of Revoc Status \- Proxy Binding Revocation NOT Supported
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pbra_count
                            
                            	Count of PBRAs
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbra_drop_count
                            
                            	Count of PBRAs dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: revoc_function_not_supported_count
                            
                            	Count of Revoc Status \- Revocation Function NOT Supported
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: success_count
                            
                            	Count of Revoc Status \- Success
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_revoc_trigger_count
                            
                            	Count of Revoc Status \- Revocation Trigger NOT supported
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraSendStatistics, self).__init__()

                                self.yang_name = "pbra-send-statistics"
                                self.yang_parent_name = "protocol-statistics"

                                self.hoa_required_count = YLeaf(YType.uint32, "hoa-required-count")

                                self.mn_attached_count = YLeaf(YType.uint32, "mn-attached-count")

                                self.mn_identity_required_count = YLeaf(YType.uint32, "mn-identity-required-count")

                                self.no_author_for_global_revoc_count = YLeaf(YType.uint32, "no-author-for-global-revoc-count")

                                self.no_binding_count = YLeaf(YType.uint32, "no-binding-count")

                                self.partial_success_count = YLeaf(YType.uint32, "partial-success-count")

                                self.pbr_not_supported_count = YLeaf(YType.uint32, "pbr-not-supported-count")

                                self.pbra_count = YLeaf(YType.uint64, "pbra-count")

                                self.pbra_drop_count = YLeaf(YType.uint32, "pbra-drop-count")

                                self.revoc_function_not_supported_count = YLeaf(YType.uint32, "revoc-function-not-supported-count")

                                self.success_count = YLeaf(YType.uint32, "success-count")

                                self.unknown_revoc_trigger_count = YLeaf(YType.uint32, "unknown-revoc-trigger-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("hoa_required_count",
                                                "mn_attached_count",
                                                "mn_identity_required_count",
                                                "no_author_for_global_revoc_count",
                                                "no_binding_count",
                                                "partial_success_count",
                                                "pbr_not_supported_count",
                                                "pbra_count",
                                                "pbra_drop_count",
                                                "revoc_function_not_supported_count",
                                                "success_count",
                                                "unknown_revoc_trigger_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraSendStatistics, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraSendStatistics, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.hoa_required_count.is_set or
                                    self.mn_attached_count.is_set or
                                    self.mn_identity_required_count.is_set or
                                    self.no_author_for_global_revoc_count.is_set or
                                    self.no_binding_count.is_set or
                                    self.partial_success_count.is_set or
                                    self.pbr_not_supported_count.is_set or
                                    self.pbra_count.is_set or
                                    self.pbra_drop_count.is_set or
                                    self.revoc_function_not_supported_count.is_set or
                                    self.success_count.is_set or
                                    self.unknown_revoc_trigger_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.hoa_required_count.yfilter != YFilter.not_set or
                                    self.mn_attached_count.yfilter != YFilter.not_set or
                                    self.mn_identity_required_count.yfilter != YFilter.not_set or
                                    self.no_author_for_global_revoc_count.yfilter != YFilter.not_set or
                                    self.no_binding_count.yfilter != YFilter.not_set or
                                    self.partial_success_count.yfilter != YFilter.not_set or
                                    self.pbr_not_supported_count.yfilter != YFilter.not_set or
                                    self.pbra_count.yfilter != YFilter.not_set or
                                    self.pbra_drop_count.yfilter != YFilter.not_set or
                                    self.revoc_function_not_supported_count.yfilter != YFilter.not_set or
                                    self.success_count.yfilter != YFilter.not_set or
                                    self.unknown_revoc_trigger_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pbra-send-statistics" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.hoa_required_count.is_set or self.hoa_required_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hoa_required_count.get_name_leafdata())
                                if (self.mn_attached_count.is_set or self.mn_attached_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mn_attached_count.get_name_leafdata())
                                if (self.mn_identity_required_count.is_set or self.mn_identity_required_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mn_identity_required_count.get_name_leafdata())
                                if (self.no_author_for_global_revoc_count.is_set or self.no_author_for_global_revoc_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_author_for_global_revoc_count.get_name_leafdata())
                                if (self.no_binding_count.is_set or self.no_binding_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_binding_count.get_name_leafdata())
                                if (self.partial_success_count.is_set or self.partial_success_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.partial_success_count.get_name_leafdata())
                                if (self.pbr_not_supported_count.is_set or self.pbr_not_supported_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbr_not_supported_count.get_name_leafdata())
                                if (self.pbra_count.is_set or self.pbra_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbra_count.get_name_leafdata())
                                if (self.pbra_drop_count.is_set or self.pbra_drop_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbra_drop_count.get_name_leafdata())
                                if (self.revoc_function_not_supported_count.is_set or self.revoc_function_not_supported_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.revoc_function_not_supported_count.get_name_leafdata())
                                if (self.success_count.is_set or self.success_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.success_count.get_name_leafdata())
                                if (self.unknown_revoc_trigger_count.is_set or self.unknown_revoc_trigger_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unknown_revoc_trigger_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "hoa-required-count" or name == "mn-attached-count" or name == "mn-identity-required-count" or name == "no-author-for-global-revoc-count" or name == "no-binding-count" or name == "partial-success-count" or name == "pbr-not-supported-count" or name == "pbra-count" or name == "pbra-drop-count" or name == "revoc-function-not-supported-count" or name == "success-count" or name == "unknown-revoc-trigger-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "hoa-required-count"):
                                    self.hoa_required_count = value
                                    self.hoa_required_count.value_namespace = name_space
                                    self.hoa_required_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mn-attached-count"):
                                    self.mn_attached_count = value
                                    self.mn_attached_count.value_namespace = name_space
                                    self.mn_attached_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mn-identity-required-count"):
                                    self.mn_identity_required_count = value
                                    self.mn_identity_required_count.value_namespace = name_space
                                    self.mn_identity_required_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-author-for-global-revoc-count"):
                                    self.no_author_for_global_revoc_count = value
                                    self.no_author_for_global_revoc_count.value_namespace = name_space
                                    self.no_author_for_global_revoc_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-binding-count"):
                                    self.no_binding_count = value
                                    self.no_binding_count.value_namespace = name_space
                                    self.no_binding_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "partial-success-count"):
                                    self.partial_success_count = value
                                    self.partial_success_count.value_namespace = name_space
                                    self.partial_success_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbr-not-supported-count"):
                                    self.pbr_not_supported_count = value
                                    self.pbr_not_supported_count.value_namespace = name_space
                                    self.pbr_not_supported_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbra-count"):
                                    self.pbra_count = value
                                    self.pbra_count.value_namespace = name_space
                                    self.pbra_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbra-drop-count"):
                                    self.pbra_drop_count = value
                                    self.pbra_drop_count.value_namespace = name_space
                                    self.pbra_drop_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "revoc-function-not-supported-count"):
                                    self.revoc_function_not_supported_count = value
                                    self.revoc_function_not_supported_count.value_namespace = name_space
                                    self.revoc_function_not_supported_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "success-count"):
                                    self.success_count = value
                                    self.success_count.value_namespace = name_space
                                    self.success_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "unknown-revoc-trigger-count"):
                                    self.unknown_revoc_trigger_count = value
                                    self.unknown_revoc_trigger_count.value_namespace = name_space
                                    self.unknown_revoc_trigger_count.value_namespace_prefix = name_space_prefix


                        class PbraReceiveStatistics(Entity):
                            """
                            PBRA Receive Statistics
                            
                            .. attribute:: hoa_required_count
                            
                            	Count of Revoc Status \- IPv4 Home Address Option Required
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mn_attached_count
                            
                            	Count of Revoc Status \- Revocation Failed \- MN is Attached
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mn_identity_required_count
                            
                            	Count of Revoc Status \- Revoked Mobile Node Identity Required
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_global_revoc_count
                            
                            	Count of Revoc Status \- Global Revocation NOT Authorized
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_binding_count
                            
                            	Count of Revoc Status \- Binding Does Not Exist
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: partial_success_count
                            
                            	Count of Revoc Status \- Partial Success
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pbr_not_supported_count
                            
                            	Count of Revoc Status \- Proxy Binding Revocation NOT Supported
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pbra_count
                            
                            	Count of PBRAs
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbra_drop_count
                            
                            	Count of PBRAs dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: revoc_function_not_supported_count
                            
                            	Count of Revoc Status \- Revocation Function NOT Supported
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: success_count
                            
                            	Count of Revoc Status \- Success
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_revoc_trigger_count
                            
                            	Count of Revoc Status \- Revocation Trigger NOT supported
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraReceiveStatistics, self).__init__()

                                self.yang_name = "pbra-receive-statistics"
                                self.yang_parent_name = "protocol-statistics"

                                self.hoa_required_count = YLeaf(YType.uint32, "hoa-required-count")

                                self.mn_attached_count = YLeaf(YType.uint32, "mn-attached-count")

                                self.mn_identity_required_count = YLeaf(YType.uint32, "mn-identity-required-count")

                                self.no_author_for_global_revoc_count = YLeaf(YType.uint32, "no-author-for-global-revoc-count")

                                self.no_binding_count = YLeaf(YType.uint32, "no-binding-count")

                                self.partial_success_count = YLeaf(YType.uint32, "partial-success-count")

                                self.pbr_not_supported_count = YLeaf(YType.uint32, "pbr-not-supported-count")

                                self.pbra_count = YLeaf(YType.uint64, "pbra-count")

                                self.pbra_drop_count = YLeaf(YType.uint32, "pbra-drop-count")

                                self.revoc_function_not_supported_count = YLeaf(YType.uint32, "revoc-function-not-supported-count")

                                self.success_count = YLeaf(YType.uint32, "success-count")

                                self.unknown_revoc_trigger_count = YLeaf(YType.uint32, "unknown-revoc-trigger-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("hoa_required_count",
                                                "mn_attached_count",
                                                "mn_identity_required_count",
                                                "no_author_for_global_revoc_count",
                                                "no_binding_count",
                                                "partial_success_count",
                                                "pbr_not_supported_count",
                                                "pbra_count",
                                                "pbra_drop_count",
                                                "revoc_function_not_supported_count",
                                                "success_count",
                                                "unknown_revoc_trigger_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraReceiveStatistics, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraReceiveStatistics, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.hoa_required_count.is_set or
                                    self.mn_attached_count.is_set or
                                    self.mn_identity_required_count.is_set or
                                    self.no_author_for_global_revoc_count.is_set or
                                    self.no_binding_count.is_set or
                                    self.partial_success_count.is_set or
                                    self.pbr_not_supported_count.is_set or
                                    self.pbra_count.is_set or
                                    self.pbra_drop_count.is_set or
                                    self.revoc_function_not_supported_count.is_set or
                                    self.success_count.is_set or
                                    self.unknown_revoc_trigger_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.hoa_required_count.yfilter != YFilter.not_set or
                                    self.mn_attached_count.yfilter != YFilter.not_set or
                                    self.mn_identity_required_count.yfilter != YFilter.not_set or
                                    self.no_author_for_global_revoc_count.yfilter != YFilter.not_set or
                                    self.no_binding_count.yfilter != YFilter.not_set or
                                    self.partial_success_count.yfilter != YFilter.not_set or
                                    self.pbr_not_supported_count.yfilter != YFilter.not_set or
                                    self.pbra_count.yfilter != YFilter.not_set or
                                    self.pbra_drop_count.yfilter != YFilter.not_set or
                                    self.revoc_function_not_supported_count.yfilter != YFilter.not_set or
                                    self.success_count.yfilter != YFilter.not_set or
                                    self.unknown_revoc_trigger_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pbra-receive-statistics" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.hoa_required_count.is_set or self.hoa_required_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hoa_required_count.get_name_leafdata())
                                if (self.mn_attached_count.is_set or self.mn_attached_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mn_attached_count.get_name_leafdata())
                                if (self.mn_identity_required_count.is_set or self.mn_identity_required_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mn_identity_required_count.get_name_leafdata())
                                if (self.no_author_for_global_revoc_count.is_set or self.no_author_for_global_revoc_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_author_for_global_revoc_count.get_name_leafdata())
                                if (self.no_binding_count.is_set or self.no_binding_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_binding_count.get_name_leafdata())
                                if (self.partial_success_count.is_set or self.partial_success_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.partial_success_count.get_name_leafdata())
                                if (self.pbr_not_supported_count.is_set or self.pbr_not_supported_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbr_not_supported_count.get_name_leafdata())
                                if (self.pbra_count.is_set or self.pbra_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbra_count.get_name_leafdata())
                                if (self.pbra_drop_count.is_set or self.pbra_drop_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbra_drop_count.get_name_leafdata())
                                if (self.revoc_function_not_supported_count.is_set or self.revoc_function_not_supported_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.revoc_function_not_supported_count.get_name_leafdata())
                                if (self.success_count.is_set or self.success_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.success_count.get_name_leafdata())
                                if (self.unknown_revoc_trigger_count.is_set or self.unknown_revoc_trigger_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unknown_revoc_trigger_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "hoa-required-count" or name == "mn-attached-count" or name == "mn-identity-required-count" or name == "no-author-for-global-revoc-count" or name == "no-binding-count" or name == "partial-success-count" or name == "pbr-not-supported-count" or name == "pbra-count" or name == "pbra-drop-count" or name == "revoc-function-not-supported-count" or name == "success-count" or name == "unknown-revoc-trigger-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "hoa-required-count"):
                                    self.hoa_required_count = value
                                    self.hoa_required_count.value_namespace = name_space
                                    self.hoa_required_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mn-attached-count"):
                                    self.mn_attached_count = value
                                    self.mn_attached_count.value_namespace = name_space
                                    self.mn_attached_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mn-identity-required-count"):
                                    self.mn_identity_required_count = value
                                    self.mn_identity_required_count.value_namespace = name_space
                                    self.mn_identity_required_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-author-for-global-revoc-count"):
                                    self.no_author_for_global_revoc_count = value
                                    self.no_author_for_global_revoc_count.value_namespace = name_space
                                    self.no_author_for_global_revoc_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-binding-count"):
                                    self.no_binding_count = value
                                    self.no_binding_count.value_namespace = name_space
                                    self.no_binding_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "partial-success-count"):
                                    self.partial_success_count = value
                                    self.partial_success_count.value_namespace = name_space
                                    self.partial_success_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbr-not-supported-count"):
                                    self.pbr_not_supported_count = value
                                    self.pbr_not_supported_count.value_namespace = name_space
                                    self.pbr_not_supported_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbra-count"):
                                    self.pbra_count = value
                                    self.pbra_count.value_namespace = name_space
                                    self.pbra_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbra-drop-count"):
                                    self.pbra_drop_count = value
                                    self.pbra_drop_count.value_namespace = name_space
                                    self.pbra_drop_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "revoc-function-not-supported-count"):
                                    self.revoc_function_not_supported_count = value
                                    self.revoc_function_not_supported_count.value_namespace = name_space
                                    self.revoc_function_not_supported_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "success-count"):
                                    self.success_count = value
                                    self.success_count.value_namespace = name_space
                                    self.success_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "unknown-revoc-trigger-count"):
                                    self.unknown_revoc_trigger_count = value
                                    self.unknown_revoc_trigger_count.value_namespace = name_space
                                    self.unknown_revoc_trigger_count.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.pba_send_statistics is not None and self.pba_send_statistics.has_data()) or
                                (self.pbra_receive_statistics is not None and self.pbra_receive_statistics.has_data()) or
                                (self.pbra_send_statistics is not None and self.pbra_send_statistics.has_data()) or
                                (self.pbri_receive_statistics is not None and self.pbri_receive_statistics.has_data()) or
                                (self.pbri_send_statistics is not None and self.pbri_send_statistics.has_data()) or
                                (self.pbu_receive_statistics is not None and self.pbu_receive_statistics.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.pba_send_statistics is not None and self.pba_send_statistics.has_operation()) or
                                (self.pbra_receive_statistics is not None and self.pbra_receive_statistics.has_operation()) or
                                (self.pbra_send_statistics is not None and self.pbra_send_statistics.has_operation()) or
                                (self.pbri_receive_statistics is not None and self.pbri_receive_statistics.has_operation()) or
                                (self.pbri_send_statistics is not None and self.pbri_send_statistics.has_operation()) or
                                (self.pbu_receive_statistics is not None and self.pbu_receive_statistics.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "protocol-statistics" + path_buffer

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

                            if (child_yang_name == "pba-send-statistics"):
                                if (self.pba_send_statistics is None):
                                    self.pba_send_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbaSendStatistics()
                                    self.pba_send_statistics.parent = self
                                    self._children_name_map["pba_send_statistics"] = "pba-send-statistics"
                                return self.pba_send_statistics

                            if (child_yang_name == "pbra-receive-statistics"):
                                if (self.pbra_receive_statistics is None):
                                    self.pbra_receive_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraReceiveStatistics()
                                    self.pbra_receive_statistics.parent = self
                                    self._children_name_map["pbra_receive_statistics"] = "pbra-receive-statistics"
                                return self.pbra_receive_statistics

                            if (child_yang_name == "pbra-send-statistics"):
                                if (self.pbra_send_statistics is None):
                                    self.pbra_send_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraSendStatistics()
                                    self.pbra_send_statistics.parent = self
                                    self._children_name_map["pbra_send_statistics"] = "pbra-send-statistics"
                                return self.pbra_send_statistics

                            if (child_yang_name == "pbri-receive-statistics"):
                                if (self.pbri_receive_statistics is None):
                                    self.pbri_receive_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriReceiveStatistics()
                                    self.pbri_receive_statistics.parent = self
                                    self._children_name_map["pbri_receive_statistics"] = "pbri-receive-statistics"
                                return self.pbri_receive_statistics

                            if (child_yang_name == "pbri-send-statistics"):
                                if (self.pbri_send_statistics is None):
                                    self.pbri_send_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriSendStatistics()
                                    self.pbri_send_statistics.parent = self
                                    self._children_name_map["pbri_send_statistics"] = "pbri-send-statistics"
                                return self.pbri_send_statistics

                            if (child_yang_name == "pbu-receive-statistics"):
                                if (self.pbu_receive_statistics is None):
                                    self.pbu_receive_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbuReceiveStatistics()
                                    self.pbu_receive_statistics.parent = self
                                    self._children_name_map["pbu_receive_statistics"] = "pbu-receive-statistics"
                                return self.pbu_receive_statistics

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "pba-send-statistics" or name == "pbra-receive-statistics" or name == "pbra-send-statistics" or name == "pbri-receive-statistics" or name == "pbri-send-statistics" or name == "pbu-receive-statistics"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class AccountingStatistics(Entity):
                        """
                        LMA Accounting Statistics
                        
                        .. attribute:: accounting_start_sent_count
                        
                        	Count of Accounting Start Records Sent
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: accounting_stop_sent_count
                        
                        	Count of Accounting Stop Records Sent
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: accounting_update_sent_count
                        
                        	Count of Accounting Update Records Sent
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.AccountingStatistics, self).__init__()

                            self.yang_name = "accounting-statistics"
                            self.yang_parent_name = "customer-statistic"

                            self.accounting_start_sent_count = YLeaf(YType.uint64, "accounting-start-sent-count")

                            self.accounting_stop_sent_count = YLeaf(YType.uint64, "accounting-stop-sent-count")

                            self.accounting_update_sent_count = YLeaf(YType.uint64, "accounting-update-sent-count")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("accounting_start_sent_count",
                                            "accounting_stop_sent_count",
                                            "accounting_update_sent_count") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.AccountingStatistics, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.AccountingStatistics, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.accounting_start_sent_count.is_set or
                                self.accounting_stop_sent_count.is_set or
                                self.accounting_update_sent_count.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.accounting_start_sent_count.yfilter != YFilter.not_set or
                                self.accounting_stop_sent_count.yfilter != YFilter.not_set or
                                self.accounting_update_sent_count.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "accounting-statistics" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.accounting_start_sent_count.is_set or self.accounting_start_sent_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.accounting_start_sent_count.get_name_leafdata())
                            if (self.accounting_stop_sent_count.is_set or self.accounting_stop_sent_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.accounting_stop_sent_count.get_name_leafdata())
                            if (self.accounting_update_sent_count.is_set or self.accounting_update_sent_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.accounting_update_sent_count.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "accounting-start-sent-count" or name == "accounting-stop-sent-count" or name == "accounting-update-sent-count"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "accounting-start-sent-count"):
                                self.accounting_start_sent_count = value
                                self.accounting_start_sent_count.value_namespace = name_space
                                self.accounting_start_sent_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "accounting-stop-sent-count"):
                                self.accounting_stop_sent_count = value
                                self.accounting_stop_sent_count.value_namespace = name_space
                                self.accounting_stop_sent_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "accounting-update-sent-count"):
                                self.accounting_update_sent_count = value
                                self.accounting_update_sent_count.value_namespace = name_space
                                self.accounting_update_sent_count.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.customer_name.is_set or
                            self.bce_count.is_set or
                            self.handoff_count.is_set or
                            self.ipv4_mnp_count.is_set or
                            self.ipv6_mnp_count.is_set or
                            self.lma_identifier.is_set or
                            (self.accounting_statistics is not None and self.accounting_statistics.has_data()) or
                            (self.protocol_statistics is not None and self.protocol_statistics.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.customer_name.yfilter != YFilter.not_set or
                            self.bce_count.yfilter != YFilter.not_set or
                            self.handoff_count.yfilter != YFilter.not_set or
                            self.ipv4_mnp_count.yfilter != YFilter.not_set or
                            self.ipv6_mnp_count.yfilter != YFilter.not_set or
                            self.lma_identifier.yfilter != YFilter.not_set or
                            (self.accounting_statistics is not None and self.accounting_statistics.has_operation()) or
                            (self.protocol_statistics is not None and self.protocol_statistics.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "customer-statistic" + "[customer-name='" + self.customer_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/customer-statistics/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.customer_name.is_set or self.customer_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.customer_name.get_name_leafdata())
                        if (self.bce_count.is_set or self.bce_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bce_count.get_name_leafdata())
                        if (self.handoff_count.is_set or self.handoff_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.handoff_count.get_name_leafdata())
                        if (self.ipv4_mnp_count.is_set or self.ipv4_mnp_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_mnp_count.get_name_leafdata())
                        if (self.ipv6_mnp_count.is_set or self.ipv6_mnp_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_mnp_count.get_name_leafdata())
                        if (self.lma_identifier.is_set or self.lma_identifier.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lma_identifier.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "accounting-statistics"):
                            if (self.accounting_statistics is None):
                                self.accounting_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.AccountingStatistics()
                                self.accounting_statistics.parent = self
                                self._children_name_map["accounting_statistics"] = "accounting-statistics"
                            return self.accounting_statistics

                        if (child_yang_name == "protocol-statistics"):
                            if (self.protocol_statistics is None):
                                self.protocol_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics()
                                self.protocol_statistics.parent = self
                                self._children_name_map["protocol_statistics"] = "protocol-statistics"
                            return self.protocol_statistics

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "accounting-statistics" or name == "protocol-statistics" or name == "customer-name" or name == "bce-count" or name == "handoff-count" or name == "ipv4-mnp-count" or name == "ipv6-mnp-count" or name == "lma-identifier"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "customer-name"):
                            self.customer_name = value
                            self.customer_name.value_namespace = name_space
                            self.customer_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "bce-count"):
                            self.bce_count = value
                            self.bce_count.value_namespace = name_space
                            self.bce_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "handoff-count"):
                            self.handoff_count = value
                            self.handoff_count.value_namespace = name_space
                            self.handoff_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4-mnp-count"):
                            self.ipv4_mnp_count = value
                            self.ipv4_mnp_count.value_namespace = name_space
                            self.ipv4_mnp_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-mnp-count"):
                            self.ipv6_mnp_count = value
                            self.ipv6_mnp_count.value_namespace = name_space
                            self.ipv6_mnp_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "lma-identifier"):
                            self.lma_identifier = value
                            self.lma_identifier.value_namespace = name_space
                            self.lma_identifier.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.customer_statistic:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.customer_statistic:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "customer-statistics" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "customer-statistic"):
                        for c in self.customer_statistic:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.customer_statistic.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "customer-statistic"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Global_(Entity):
                """
                Global Statistics
                
                .. attribute:: accounting_statistics
                
                	LMA Accounting Statistics
                	**type**\:   :py:class:`AccountingStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.AccountingStatistics>`
                
                .. attribute:: bce_count
                
                	Count of Bindings
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: handoff_count
                
                	Count of Handoffs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: lma_identifier
                
                	LMA Identifier
                	**type**\:  str
                
                .. attribute:: multi_tenant_count
                
                	Count of Multi Tenants
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: packet_statistics
                
                	Packet Statistics
                	**type**\:   :py:class:`PacketStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.PacketStatistics>`
                
                .. attribute:: protocol_statistics
                
                	LMA Protocol Statistics
                	**type**\:   :py:class:`ProtocolStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.ProtocolStatistics>`
                
                .. attribute:: single_tenant_count
                
                	Count of Single Tenants
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-mobileip-oper'
                _revision = '2016-03-10'

                def __init__(self):
                    super(Pmipv6.Lma.Statistics.Global_, self).__init__()

                    self.yang_name = "global"
                    self.yang_parent_name = "statistics"

                    self.bce_count = YLeaf(YType.uint32, "bce-count")

                    self.handoff_count = YLeaf(YType.uint32, "handoff-count")

                    self.lma_identifier = YLeaf(YType.str, "lma-identifier")

                    self.multi_tenant_count = YLeaf(YType.uint32, "multi-tenant-count")

                    self.single_tenant_count = YLeaf(YType.uint32, "single-tenant-count")

                    self.accounting_statistics = Pmipv6.Lma.Statistics.Global_.AccountingStatistics()
                    self.accounting_statistics.parent = self
                    self._children_name_map["accounting_statistics"] = "accounting-statistics"
                    self._children_yang_names.add("accounting-statistics")

                    self.packet_statistics = Pmipv6.Lma.Statistics.Global_.PacketStatistics()
                    self.packet_statistics.parent = self
                    self._children_name_map["packet_statistics"] = "packet-statistics"
                    self._children_yang_names.add("packet-statistics")

                    self.protocol_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics()
                    self.protocol_statistics.parent = self
                    self._children_name_map["protocol_statistics"] = "protocol-statistics"
                    self._children_yang_names.add("protocol-statistics")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bce_count",
                                    "handoff_count",
                                    "lma_identifier",
                                    "multi_tenant_count",
                                    "single_tenant_count") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Pmipv6.Lma.Statistics.Global_, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Pmipv6.Lma.Statistics.Global_, self).__setattr__(name, value)


                class PacketStatistics(Entity):
                    """
                    Packet Statistics
                    
                    .. attribute:: checksum_errors
                    
                    	Checksumm errors
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_received
                    
                    	Count of received packets
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_received_ipv6
                    
                    	Count of IPv6 received packets
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Count of sent packets
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent_ipv6
                    
                    	Count of IPv6 sent packets
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: receive_drops
                    
                    	Drop count of received packets
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: receive_drops_ipv6
                    
                    	Drop count of IPv6 received packets
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: send_drops
                    
                    	Drop count of sent packets
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: send_drops_ipv6
                    
                    	Drop count of IPv6 sent packets
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.Statistics.Global_.PacketStatistics, self).__init__()

                        self.yang_name = "packet-statistics"
                        self.yang_parent_name = "global"

                        self.checksum_errors = YLeaf(YType.uint64, "checksum-errors")

                        self.packets_received = YLeaf(YType.uint64, "packets-received")

                        self.packets_received_ipv6 = YLeaf(YType.uint64, "packets-received-ipv6")

                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                        self.packets_sent_ipv6 = YLeaf(YType.uint64, "packets-sent-ipv6")

                        self.receive_drops = YLeaf(YType.uint64, "receive-drops")

                        self.receive_drops_ipv6 = YLeaf(YType.uint64, "receive-drops-ipv6")

                        self.send_drops = YLeaf(YType.uint64, "send-drops")

                        self.send_drops_ipv6 = YLeaf(YType.uint64, "send-drops-ipv6")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("checksum_errors",
                                        "packets_received",
                                        "packets_received_ipv6",
                                        "packets_sent",
                                        "packets_sent_ipv6",
                                        "receive_drops",
                                        "receive_drops_ipv6",
                                        "send_drops",
                                        "send_drops_ipv6") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pmipv6.Lma.Statistics.Global_.PacketStatistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pmipv6.Lma.Statistics.Global_.PacketStatistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.checksum_errors.is_set or
                            self.packets_received.is_set or
                            self.packets_received_ipv6.is_set or
                            self.packets_sent.is_set or
                            self.packets_sent_ipv6.is_set or
                            self.receive_drops.is_set or
                            self.receive_drops_ipv6.is_set or
                            self.send_drops.is_set or
                            self.send_drops_ipv6.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.checksum_errors.yfilter != YFilter.not_set or
                            self.packets_received.yfilter != YFilter.not_set or
                            self.packets_received_ipv6.yfilter != YFilter.not_set or
                            self.packets_sent.yfilter != YFilter.not_set or
                            self.packets_sent_ipv6.yfilter != YFilter.not_set or
                            self.receive_drops.yfilter != YFilter.not_set or
                            self.receive_drops_ipv6.yfilter != YFilter.not_set or
                            self.send_drops.yfilter != YFilter.not_set or
                            self.send_drops_ipv6.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "packet-statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.checksum_errors.is_set or self.checksum_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.checksum_errors.get_name_leafdata())
                        if (self.packets_received.is_set or self.packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_received.get_name_leafdata())
                        if (self.packets_received_ipv6.is_set or self.packets_received_ipv6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_received_ipv6.get_name_leafdata())
                        if (self.packets_sent.is_set or self.packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_sent.get_name_leafdata())
                        if (self.packets_sent_ipv6.is_set or self.packets_sent_ipv6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packets_sent_ipv6.get_name_leafdata())
                        if (self.receive_drops.is_set or self.receive_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_drops.get_name_leafdata())
                        if (self.receive_drops_ipv6.is_set or self.receive_drops_ipv6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_drops_ipv6.get_name_leafdata())
                        if (self.send_drops.is_set or self.send_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.send_drops.get_name_leafdata())
                        if (self.send_drops_ipv6.is_set or self.send_drops_ipv6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.send_drops_ipv6.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "checksum-errors" or name == "packets-received" or name == "packets-received-ipv6" or name == "packets-sent" or name == "packets-sent-ipv6" or name == "receive-drops" or name == "receive-drops-ipv6" or name == "send-drops" or name == "send-drops-ipv6"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "checksum-errors"):
                            self.checksum_errors = value
                            self.checksum_errors.value_namespace = name_space
                            self.checksum_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-received"):
                            self.packets_received = value
                            self.packets_received.value_namespace = name_space
                            self.packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-received-ipv6"):
                            self.packets_received_ipv6 = value
                            self.packets_received_ipv6.value_namespace = name_space
                            self.packets_received_ipv6.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-sent"):
                            self.packets_sent = value
                            self.packets_sent.value_namespace = name_space
                            self.packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "packets-sent-ipv6"):
                            self.packets_sent_ipv6 = value
                            self.packets_sent_ipv6.value_namespace = name_space
                            self.packets_sent_ipv6.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-drops"):
                            self.receive_drops = value
                            self.receive_drops.value_namespace = name_space
                            self.receive_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-drops-ipv6"):
                            self.receive_drops_ipv6 = value
                            self.receive_drops_ipv6.value_namespace = name_space
                            self.receive_drops_ipv6.value_namespace_prefix = name_space_prefix
                        if(value_path == "send-drops"):
                            self.send_drops = value
                            self.send_drops.value_namespace = name_space
                            self.send_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "send-drops-ipv6"):
                            self.send_drops_ipv6 = value
                            self.send_drops_ipv6.value_namespace = name_space
                            self.send_drops_ipv6.value_namespace_prefix = name_space_prefix


                class ProtocolStatistics(Entity):
                    """
                    LMA Protocol Statistics
                    
                    .. attribute:: pba_send_statistics
                    
                    	PBA Send Statistics
                    	**type**\:   :py:class:`PbaSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbaSendStatistics>`
                    
                    .. attribute:: pbra_receive_statistics
                    
                    	PBRA Receive Statistics
                    	**type**\:   :py:class:`PbraReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraReceiveStatistics>`
                    
                    .. attribute:: pbra_send_statistics
                    
                    	PBRA Send Statistics
                    	**type**\:   :py:class:`PbraSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraSendStatistics>`
                    
                    .. attribute:: pbri_receive_statistics
                    
                    	PBRI Receive Statistics
                    	**type**\:   :py:class:`PbriReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriReceiveStatistics>`
                    
                    .. attribute:: pbri_send_statistics
                    
                    	PBRI Send Statistics
                    	**type**\:   :py:class:`PbriSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriSendStatistics>`
                    
                    .. attribute:: pbu_receive_statistics
                    
                    	PBU Receive Statistics
                    	**type**\:   :py:class:`PbuReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbuReceiveStatistics>`
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics, self).__init__()

                        self.yang_name = "protocol-statistics"
                        self.yang_parent_name = "global"

                        self.pba_send_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbaSendStatistics()
                        self.pba_send_statistics.parent = self
                        self._children_name_map["pba_send_statistics"] = "pba-send-statistics"
                        self._children_yang_names.add("pba-send-statistics")

                        self.pbra_receive_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraReceiveStatistics()
                        self.pbra_receive_statistics.parent = self
                        self._children_name_map["pbra_receive_statistics"] = "pbra-receive-statistics"
                        self._children_yang_names.add("pbra-receive-statistics")

                        self.pbra_send_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraSendStatistics()
                        self.pbra_send_statistics.parent = self
                        self._children_name_map["pbra_send_statistics"] = "pbra-send-statistics"
                        self._children_yang_names.add("pbra-send-statistics")

                        self.pbri_receive_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriReceiveStatistics()
                        self.pbri_receive_statistics.parent = self
                        self._children_name_map["pbri_receive_statistics"] = "pbri-receive-statistics"
                        self._children_yang_names.add("pbri-receive-statistics")

                        self.pbri_send_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriSendStatistics()
                        self.pbri_send_statistics.parent = self
                        self._children_name_map["pbri_send_statistics"] = "pbri-send-statistics"
                        self._children_yang_names.add("pbri-send-statistics")

                        self.pbu_receive_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbuReceiveStatistics()
                        self.pbu_receive_statistics.parent = self
                        self._children_name_map["pbu_receive_statistics"] = "pbu-receive-statistics"
                        self._children_yang_names.add("pbu-receive-statistics")


                    class PbuReceiveStatistics(Entity):
                        """
                        PBU Receive Statistics
                        
                        .. attribute:: pbu_count
                        
                        	Count of PBUs
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pbu_drop_count
                        
                        	Count of PBUs Dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbuReceiveStatistics, self).__init__()

                            self.yang_name = "pbu-receive-statistics"
                            self.yang_parent_name = "protocol-statistics"

                            self.pbu_count = YLeaf(YType.uint64, "pbu-count")

                            self.pbu_drop_count = YLeaf(YType.uint32, "pbu-drop-count")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("pbu_count",
                                            "pbu_drop_count") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbuReceiveStatistics, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbuReceiveStatistics, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.pbu_count.is_set or
                                self.pbu_drop_count.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.pbu_count.yfilter != YFilter.not_set or
                                self.pbu_drop_count.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pbu-receive-statistics" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/protocol-statistics/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.pbu_count.is_set or self.pbu_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pbu_count.get_name_leafdata())
                            if (self.pbu_drop_count.is_set or self.pbu_drop_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pbu_drop_count.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "pbu-count" or name == "pbu-drop-count"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "pbu-count"):
                                self.pbu_count = value
                                self.pbu_count.value_namespace = name_space
                                self.pbu_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "pbu-drop-count"):
                                self.pbu_drop_count = value
                                self.pbu_drop_count.value_namespace = name_space
                                self.pbu_drop_count.value_namespace_prefix = name_space_prefix


                    class PbaSendStatistics(Entity):
                        """
                        PBA Send Statistics
                        
                        .. attribute:: accepted_count
                        
                        	Count of Status Code \- Binding Update accepted
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: admin_failure_count
                        
                        	Count of Status Code \- Administratively prohibited
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_failure_count
                        
                        	Count of Status Code \- Auth Fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_sequence_failure_count
                        
                        	Count of Status Code \- Sequence number out of window
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: gre_key_opt_required_count
                        
                        	Count of Status Code \- GRE Key option is required
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: home_reg_failure_count
                        
                        	Count of Status Code \- Home registration not supported
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: home_subnet_failure_count
                        
                        	Count of Status Code \- Not home subnet
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing_access_tech_type_opt_count
                        
                        	Count of Status Code \- Missing ATT option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing_hi_opt_count
                        
                        	Count of Status Code \- Missing Handoff Indicator
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing_hnp_opt_count
                        
                        	Count of Status Code \- Missing Home Network Prefix option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing_mn_id_opt_count
                        
                        	Count of Status Code \- Missing MN identifier option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: multiple_ipv4_ho_a_not_supported_count
                        
                        	Count of Status Code \- Multiple IPv4 HoA not supported
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_author_for_hnp_count
                        
                        	Count of Status Code \- Not authorized for HNP
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_author_for_ipv4_hoa_count
                        
                        	Count of Status Code \- Not authorized for IPv4 HoA
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_author_for_ipv4_mobility_count
                        
                        	Count of Status Code \- Not authorized for IPv4 mobility
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_author_for_ipv6_mobility_count
                        
                        	Count of Status Code \- Not authorized for IPv6 mobility
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_author_for_proxy_reg_count
                        
                        	Count of Status Code \- MAG not auth.for proxyreg
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: not_lma_for_this_mn_count
                        
                        	Count of Status Code \- Not LMA for this Mobile Node
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pba_count
                        
                        	Count of PBAs
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pba_drop_count
                        
                        	Count of PBAs dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: proxy_reg_not_enabled_count
                        
                        	Count of Status Code \- Proxy Registration not enabled
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_hnps_do_not_match_bce_hnps_count
                        
                        	Count of Status Code \- Recevied HNPs do not match with BCE
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reg_type_failure_count
                        
                        	Count of Status Code \- Registration type change
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: resource_failure_count
                        
                        	Count of Status Code \- Insufficient resources
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timestamp_lower_than_previous_accepted_count
                        
                        	Count of Status Code \- Timestamp lower than previous accepted
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timestamp_mismatch_count
                        
                        	Count of Status Code \- Invalid timestamp value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_count
                        
                        	Count of Status Code \- Last BA status code sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unspecified_failure_count
                        
                        	Count of Status Code \- Reason unspecified
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbaSendStatistics, self).__init__()

                            self.yang_name = "pba-send-statistics"
                            self.yang_parent_name = "protocol-statistics"

                            self.accepted_count = YLeaf(YType.uint32, "accepted-count")

                            self.admin_failure_count = YLeaf(YType.uint32, "admin-failure-count")

                            self.authen_failure_count = YLeaf(YType.uint32, "authen-failure-count")

                            self.bad_sequence_failure_count = YLeaf(YType.uint32, "bad-sequence-failure-count")

                            self.gre_key_opt_required_count = YLeaf(YType.uint32, "gre-key-opt-required-count")

                            self.home_reg_failure_count = YLeaf(YType.uint32, "home-reg-failure-count")

                            self.home_subnet_failure_count = YLeaf(YType.uint32, "home-subnet-failure-count")

                            self.missing_access_tech_type_opt_count = YLeaf(YType.uint32, "missing-access-tech-type-opt-count")

                            self.missing_hi_opt_count = YLeaf(YType.uint32, "missing-hi-opt-count")

                            self.missing_hnp_opt_count = YLeaf(YType.uint32, "missing-hnp-opt-count")

                            self.missing_mn_id_opt_count = YLeaf(YType.uint32, "missing-mn-id-opt-count")

                            self.multiple_ipv4_ho_a_not_supported_count = YLeaf(YType.uint32, "multiple-ipv4-ho-a-not-supported-count")

                            self.no_author_for_hnp_count = YLeaf(YType.uint32, "no-author-for-hnp-count")

                            self.no_author_for_ipv4_hoa_count = YLeaf(YType.uint32, "no-author-for-ipv4-hoa-count")

                            self.no_author_for_ipv4_mobility_count = YLeaf(YType.uint32, "no-author-for-ipv4-mobility-count")

                            self.no_author_for_ipv6_mobility_count = YLeaf(YType.uint32, "no-author-for-ipv6-mobility-count")

                            self.no_author_for_proxy_reg_count = YLeaf(YType.uint32, "no-author-for-proxy-reg-count")

                            self.not_lma_for_this_mn_count = YLeaf(YType.uint32, "not-lma-for-this-mn-count")

                            self.pba_count = YLeaf(YType.uint64, "pba-count")

                            self.pba_drop_count = YLeaf(YType.uint32, "pba-drop-count")

                            self.proxy_reg_not_enabled_count = YLeaf(YType.uint32, "proxy-reg-not-enabled-count")

                            self.received_hnps_do_not_match_bce_hnps_count = YLeaf(YType.uint32, "received-hnps-do-not-match-bce-hnps-count")

                            self.reg_type_failure_count = YLeaf(YType.uint32, "reg-type-failure-count")

                            self.resource_failure_count = YLeaf(YType.uint32, "resource-failure-count")

                            self.timestamp_lower_than_previous_accepted_count = YLeaf(YType.uint32, "timestamp-lower-than-previous-accepted-count")

                            self.timestamp_mismatch_count = YLeaf(YType.uint32, "timestamp-mismatch-count")

                            self.unknown_count = YLeaf(YType.uint32, "unknown-count")

                            self.unspecified_failure_count = YLeaf(YType.uint32, "unspecified-failure-count")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("accepted_count",
                                            "admin_failure_count",
                                            "authen_failure_count",
                                            "bad_sequence_failure_count",
                                            "gre_key_opt_required_count",
                                            "home_reg_failure_count",
                                            "home_subnet_failure_count",
                                            "missing_access_tech_type_opt_count",
                                            "missing_hi_opt_count",
                                            "missing_hnp_opt_count",
                                            "missing_mn_id_opt_count",
                                            "multiple_ipv4_ho_a_not_supported_count",
                                            "no_author_for_hnp_count",
                                            "no_author_for_ipv4_hoa_count",
                                            "no_author_for_ipv4_mobility_count",
                                            "no_author_for_ipv6_mobility_count",
                                            "no_author_for_proxy_reg_count",
                                            "not_lma_for_this_mn_count",
                                            "pba_count",
                                            "pba_drop_count",
                                            "proxy_reg_not_enabled_count",
                                            "received_hnps_do_not_match_bce_hnps_count",
                                            "reg_type_failure_count",
                                            "resource_failure_count",
                                            "timestamp_lower_than_previous_accepted_count",
                                            "timestamp_mismatch_count",
                                            "unknown_count",
                                            "unspecified_failure_count") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbaSendStatistics, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbaSendStatistics, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.accepted_count.is_set or
                                self.admin_failure_count.is_set or
                                self.authen_failure_count.is_set or
                                self.bad_sequence_failure_count.is_set or
                                self.gre_key_opt_required_count.is_set or
                                self.home_reg_failure_count.is_set or
                                self.home_subnet_failure_count.is_set or
                                self.missing_access_tech_type_opt_count.is_set or
                                self.missing_hi_opt_count.is_set or
                                self.missing_hnp_opt_count.is_set or
                                self.missing_mn_id_opt_count.is_set or
                                self.multiple_ipv4_ho_a_not_supported_count.is_set or
                                self.no_author_for_hnp_count.is_set or
                                self.no_author_for_ipv4_hoa_count.is_set or
                                self.no_author_for_ipv4_mobility_count.is_set or
                                self.no_author_for_ipv6_mobility_count.is_set or
                                self.no_author_for_proxy_reg_count.is_set or
                                self.not_lma_for_this_mn_count.is_set or
                                self.pba_count.is_set or
                                self.pba_drop_count.is_set or
                                self.proxy_reg_not_enabled_count.is_set or
                                self.received_hnps_do_not_match_bce_hnps_count.is_set or
                                self.reg_type_failure_count.is_set or
                                self.resource_failure_count.is_set or
                                self.timestamp_lower_than_previous_accepted_count.is_set or
                                self.timestamp_mismatch_count.is_set or
                                self.unknown_count.is_set or
                                self.unspecified_failure_count.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.accepted_count.yfilter != YFilter.not_set or
                                self.admin_failure_count.yfilter != YFilter.not_set or
                                self.authen_failure_count.yfilter != YFilter.not_set or
                                self.bad_sequence_failure_count.yfilter != YFilter.not_set or
                                self.gre_key_opt_required_count.yfilter != YFilter.not_set or
                                self.home_reg_failure_count.yfilter != YFilter.not_set or
                                self.home_subnet_failure_count.yfilter != YFilter.not_set or
                                self.missing_access_tech_type_opt_count.yfilter != YFilter.not_set or
                                self.missing_hi_opt_count.yfilter != YFilter.not_set or
                                self.missing_hnp_opt_count.yfilter != YFilter.not_set or
                                self.missing_mn_id_opt_count.yfilter != YFilter.not_set or
                                self.multiple_ipv4_ho_a_not_supported_count.yfilter != YFilter.not_set or
                                self.no_author_for_hnp_count.yfilter != YFilter.not_set or
                                self.no_author_for_ipv4_hoa_count.yfilter != YFilter.not_set or
                                self.no_author_for_ipv4_mobility_count.yfilter != YFilter.not_set or
                                self.no_author_for_ipv6_mobility_count.yfilter != YFilter.not_set or
                                self.no_author_for_proxy_reg_count.yfilter != YFilter.not_set or
                                self.not_lma_for_this_mn_count.yfilter != YFilter.not_set or
                                self.pba_count.yfilter != YFilter.not_set or
                                self.pba_drop_count.yfilter != YFilter.not_set or
                                self.proxy_reg_not_enabled_count.yfilter != YFilter.not_set or
                                self.received_hnps_do_not_match_bce_hnps_count.yfilter != YFilter.not_set or
                                self.reg_type_failure_count.yfilter != YFilter.not_set or
                                self.resource_failure_count.yfilter != YFilter.not_set or
                                self.timestamp_lower_than_previous_accepted_count.yfilter != YFilter.not_set or
                                self.timestamp_mismatch_count.yfilter != YFilter.not_set or
                                self.unknown_count.yfilter != YFilter.not_set or
                                self.unspecified_failure_count.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pba-send-statistics" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/protocol-statistics/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.accepted_count.is_set or self.accepted_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.accepted_count.get_name_leafdata())
                            if (self.admin_failure_count.is_set or self.admin_failure_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.admin_failure_count.get_name_leafdata())
                            if (self.authen_failure_count.is_set or self.authen_failure_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.authen_failure_count.get_name_leafdata())
                            if (self.bad_sequence_failure_count.is_set or self.bad_sequence_failure_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bad_sequence_failure_count.get_name_leafdata())
                            if (self.gre_key_opt_required_count.is_set or self.gre_key_opt_required_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.gre_key_opt_required_count.get_name_leafdata())
                            if (self.home_reg_failure_count.is_set or self.home_reg_failure_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.home_reg_failure_count.get_name_leafdata())
                            if (self.home_subnet_failure_count.is_set or self.home_subnet_failure_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.home_subnet_failure_count.get_name_leafdata())
                            if (self.missing_access_tech_type_opt_count.is_set or self.missing_access_tech_type_opt_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.missing_access_tech_type_opt_count.get_name_leafdata())
                            if (self.missing_hi_opt_count.is_set or self.missing_hi_opt_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.missing_hi_opt_count.get_name_leafdata())
                            if (self.missing_hnp_opt_count.is_set or self.missing_hnp_opt_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.missing_hnp_opt_count.get_name_leafdata())
                            if (self.missing_mn_id_opt_count.is_set or self.missing_mn_id_opt_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.missing_mn_id_opt_count.get_name_leafdata())
                            if (self.multiple_ipv4_ho_a_not_supported_count.is_set or self.multiple_ipv4_ho_a_not_supported_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.multiple_ipv4_ho_a_not_supported_count.get_name_leafdata())
                            if (self.no_author_for_hnp_count.is_set or self.no_author_for_hnp_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_author_for_hnp_count.get_name_leafdata())
                            if (self.no_author_for_ipv4_hoa_count.is_set or self.no_author_for_ipv4_hoa_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_author_for_ipv4_hoa_count.get_name_leafdata())
                            if (self.no_author_for_ipv4_mobility_count.is_set or self.no_author_for_ipv4_mobility_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_author_for_ipv4_mobility_count.get_name_leafdata())
                            if (self.no_author_for_ipv6_mobility_count.is_set or self.no_author_for_ipv6_mobility_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_author_for_ipv6_mobility_count.get_name_leafdata())
                            if (self.no_author_for_proxy_reg_count.is_set or self.no_author_for_proxy_reg_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_author_for_proxy_reg_count.get_name_leafdata())
                            if (self.not_lma_for_this_mn_count.is_set or self.not_lma_for_this_mn_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.not_lma_for_this_mn_count.get_name_leafdata())
                            if (self.pba_count.is_set or self.pba_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pba_count.get_name_leafdata())
                            if (self.pba_drop_count.is_set or self.pba_drop_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pba_drop_count.get_name_leafdata())
                            if (self.proxy_reg_not_enabled_count.is_set or self.proxy_reg_not_enabled_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.proxy_reg_not_enabled_count.get_name_leafdata())
                            if (self.received_hnps_do_not_match_bce_hnps_count.is_set or self.received_hnps_do_not_match_bce_hnps_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_hnps_do_not_match_bce_hnps_count.get_name_leafdata())
                            if (self.reg_type_failure_count.is_set or self.reg_type_failure_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reg_type_failure_count.get_name_leafdata())
                            if (self.resource_failure_count.is_set or self.resource_failure_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.resource_failure_count.get_name_leafdata())
                            if (self.timestamp_lower_than_previous_accepted_count.is_set or self.timestamp_lower_than_previous_accepted_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.timestamp_lower_than_previous_accepted_count.get_name_leafdata())
                            if (self.timestamp_mismatch_count.is_set or self.timestamp_mismatch_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.timestamp_mismatch_count.get_name_leafdata())
                            if (self.unknown_count.is_set or self.unknown_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unknown_count.get_name_leafdata())
                            if (self.unspecified_failure_count.is_set or self.unspecified_failure_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unspecified_failure_count.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "accepted-count" or name == "admin-failure-count" or name == "authen-failure-count" or name == "bad-sequence-failure-count" or name == "gre-key-opt-required-count" or name == "home-reg-failure-count" or name == "home-subnet-failure-count" or name == "missing-access-tech-type-opt-count" or name == "missing-hi-opt-count" or name == "missing-hnp-opt-count" or name == "missing-mn-id-opt-count" or name == "multiple-ipv4-ho-a-not-supported-count" or name == "no-author-for-hnp-count" or name == "no-author-for-ipv4-hoa-count" or name == "no-author-for-ipv4-mobility-count" or name == "no-author-for-ipv6-mobility-count" or name == "no-author-for-proxy-reg-count" or name == "not-lma-for-this-mn-count" or name == "pba-count" or name == "pba-drop-count" or name == "proxy-reg-not-enabled-count" or name == "received-hnps-do-not-match-bce-hnps-count" or name == "reg-type-failure-count" or name == "resource-failure-count" or name == "timestamp-lower-than-previous-accepted-count" or name == "timestamp-mismatch-count" or name == "unknown-count" or name == "unspecified-failure-count"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "accepted-count"):
                                self.accepted_count = value
                                self.accepted_count.value_namespace = name_space
                                self.accepted_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "admin-failure-count"):
                                self.admin_failure_count = value
                                self.admin_failure_count.value_namespace = name_space
                                self.admin_failure_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "authen-failure-count"):
                                self.authen_failure_count = value
                                self.authen_failure_count.value_namespace = name_space
                                self.authen_failure_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "bad-sequence-failure-count"):
                                self.bad_sequence_failure_count = value
                                self.bad_sequence_failure_count.value_namespace = name_space
                                self.bad_sequence_failure_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "gre-key-opt-required-count"):
                                self.gre_key_opt_required_count = value
                                self.gre_key_opt_required_count.value_namespace = name_space
                                self.gre_key_opt_required_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "home-reg-failure-count"):
                                self.home_reg_failure_count = value
                                self.home_reg_failure_count.value_namespace = name_space
                                self.home_reg_failure_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "home-subnet-failure-count"):
                                self.home_subnet_failure_count = value
                                self.home_subnet_failure_count.value_namespace = name_space
                                self.home_subnet_failure_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "missing-access-tech-type-opt-count"):
                                self.missing_access_tech_type_opt_count = value
                                self.missing_access_tech_type_opt_count.value_namespace = name_space
                                self.missing_access_tech_type_opt_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "missing-hi-opt-count"):
                                self.missing_hi_opt_count = value
                                self.missing_hi_opt_count.value_namespace = name_space
                                self.missing_hi_opt_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "missing-hnp-opt-count"):
                                self.missing_hnp_opt_count = value
                                self.missing_hnp_opt_count.value_namespace = name_space
                                self.missing_hnp_opt_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "missing-mn-id-opt-count"):
                                self.missing_mn_id_opt_count = value
                                self.missing_mn_id_opt_count.value_namespace = name_space
                                self.missing_mn_id_opt_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "multiple-ipv4-ho-a-not-supported-count"):
                                self.multiple_ipv4_ho_a_not_supported_count = value
                                self.multiple_ipv4_ho_a_not_supported_count.value_namespace = name_space
                                self.multiple_ipv4_ho_a_not_supported_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-author-for-hnp-count"):
                                self.no_author_for_hnp_count = value
                                self.no_author_for_hnp_count.value_namespace = name_space
                                self.no_author_for_hnp_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-author-for-ipv4-hoa-count"):
                                self.no_author_for_ipv4_hoa_count = value
                                self.no_author_for_ipv4_hoa_count.value_namespace = name_space
                                self.no_author_for_ipv4_hoa_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-author-for-ipv4-mobility-count"):
                                self.no_author_for_ipv4_mobility_count = value
                                self.no_author_for_ipv4_mobility_count.value_namespace = name_space
                                self.no_author_for_ipv4_mobility_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-author-for-ipv6-mobility-count"):
                                self.no_author_for_ipv6_mobility_count = value
                                self.no_author_for_ipv6_mobility_count.value_namespace = name_space
                                self.no_author_for_ipv6_mobility_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-author-for-proxy-reg-count"):
                                self.no_author_for_proxy_reg_count = value
                                self.no_author_for_proxy_reg_count.value_namespace = name_space
                                self.no_author_for_proxy_reg_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "not-lma-for-this-mn-count"):
                                self.not_lma_for_this_mn_count = value
                                self.not_lma_for_this_mn_count.value_namespace = name_space
                                self.not_lma_for_this_mn_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "pba-count"):
                                self.pba_count = value
                                self.pba_count.value_namespace = name_space
                                self.pba_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "pba-drop-count"):
                                self.pba_drop_count = value
                                self.pba_drop_count.value_namespace = name_space
                                self.pba_drop_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "proxy-reg-not-enabled-count"):
                                self.proxy_reg_not_enabled_count = value
                                self.proxy_reg_not_enabled_count.value_namespace = name_space
                                self.proxy_reg_not_enabled_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-hnps-do-not-match-bce-hnps-count"):
                                self.received_hnps_do_not_match_bce_hnps_count = value
                                self.received_hnps_do_not_match_bce_hnps_count.value_namespace = name_space
                                self.received_hnps_do_not_match_bce_hnps_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "reg-type-failure-count"):
                                self.reg_type_failure_count = value
                                self.reg_type_failure_count.value_namespace = name_space
                                self.reg_type_failure_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "resource-failure-count"):
                                self.resource_failure_count = value
                                self.resource_failure_count.value_namespace = name_space
                                self.resource_failure_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "timestamp-lower-than-previous-accepted-count"):
                                self.timestamp_lower_than_previous_accepted_count = value
                                self.timestamp_lower_than_previous_accepted_count.value_namespace = name_space
                                self.timestamp_lower_than_previous_accepted_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "timestamp-mismatch-count"):
                                self.timestamp_mismatch_count = value
                                self.timestamp_mismatch_count.value_namespace = name_space
                                self.timestamp_mismatch_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "unknown-count"):
                                self.unknown_count = value
                                self.unknown_count.value_namespace = name_space
                                self.unknown_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "unspecified-failure-count"):
                                self.unspecified_failure_count = value
                                self.unspecified_failure_count.value_namespace = name_space
                                self.unspecified_failure_count.value_namespace_prefix = name_space_prefix


                    class PbriSendStatistics(Entity):
                        """
                        PBRI Send Statistics
                        
                        .. attribute:: admin_reason_count
                        
                        	Count of Revoc Trigger \- Administrative Reason
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mag_handover_different_att_count
                        
                        	Count of Revoc Trigger \- Inter MAG Handover Different ATT
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mag_handover_same_att_count
                        
                        	Count of Revoc Trigger \- Inter MAG Handover Same ATT
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mag_handover_unknown_count
                        
                        	Count of Revoc Trigger \- Inter MAG Handover Unknown
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: network_session_termination_count
                        
                        	Count of Revoc Trigger \- Access Network Session Termination
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: out_of_sync_bce_state_count
                        
                        	Count of Revoc Trigger \- Possible Out\-of\-Sync BCE State
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pbri_count
                        
                        	Count of PBRIs
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pbri_drop_count
                        
                        	Count of PBRIs dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: per_peer_policy_count
                        
                        	Count of Revoc Trigger \- Per\-Peer Policy
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: revoking_mn_local_policy_count
                        
                        	Count of Revoc Trigger \- Revoking Mobility Node Local Policy
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unspecified_count
                        
                        	Count of Revoc Trigger \- Unspecified
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: user_session_termination_count
                        
                        	Count of Revoc Trigger \- User Init Session Terminatation
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriSendStatistics, self).__init__()

                            self.yang_name = "pbri-send-statistics"
                            self.yang_parent_name = "protocol-statistics"

                            self.admin_reason_count = YLeaf(YType.uint32, "admin-reason-count")

                            self.mag_handover_different_att_count = YLeaf(YType.uint32, "mag-handover-different-att-count")

                            self.mag_handover_same_att_count = YLeaf(YType.uint32, "mag-handover-same-att-count")

                            self.mag_handover_unknown_count = YLeaf(YType.uint32, "mag-handover-unknown-count")

                            self.network_session_termination_count = YLeaf(YType.uint32, "network-session-termination-count")

                            self.out_of_sync_bce_state_count = YLeaf(YType.uint32, "out-of-sync-bce-state-count")

                            self.pbri_count = YLeaf(YType.uint64, "pbri-count")

                            self.pbri_drop_count = YLeaf(YType.uint32, "pbri-drop-count")

                            self.per_peer_policy_count = YLeaf(YType.uint32, "per-peer-policy-count")

                            self.revoking_mn_local_policy_count = YLeaf(YType.uint32, "revoking-mn-local-policy-count")

                            self.unspecified_count = YLeaf(YType.uint32, "unspecified-count")

                            self.user_session_termination_count = YLeaf(YType.uint32, "user-session-termination-count")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("admin_reason_count",
                                            "mag_handover_different_att_count",
                                            "mag_handover_same_att_count",
                                            "mag_handover_unknown_count",
                                            "network_session_termination_count",
                                            "out_of_sync_bce_state_count",
                                            "pbri_count",
                                            "pbri_drop_count",
                                            "per_peer_policy_count",
                                            "revoking_mn_local_policy_count",
                                            "unspecified_count",
                                            "user_session_termination_count") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriSendStatistics, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriSendStatistics, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.admin_reason_count.is_set or
                                self.mag_handover_different_att_count.is_set or
                                self.mag_handover_same_att_count.is_set or
                                self.mag_handover_unknown_count.is_set or
                                self.network_session_termination_count.is_set or
                                self.out_of_sync_bce_state_count.is_set or
                                self.pbri_count.is_set or
                                self.pbri_drop_count.is_set or
                                self.per_peer_policy_count.is_set or
                                self.revoking_mn_local_policy_count.is_set or
                                self.unspecified_count.is_set or
                                self.user_session_termination_count.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.admin_reason_count.yfilter != YFilter.not_set or
                                self.mag_handover_different_att_count.yfilter != YFilter.not_set or
                                self.mag_handover_same_att_count.yfilter != YFilter.not_set or
                                self.mag_handover_unknown_count.yfilter != YFilter.not_set or
                                self.network_session_termination_count.yfilter != YFilter.not_set or
                                self.out_of_sync_bce_state_count.yfilter != YFilter.not_set or
                                self.pbri_count.yfilter != YFilter.not_set or
                                self.pbri_drop_count.yfilter != YFilter.not_set or
                                self.per_peer_policy_count.yfilter != YFilter.not_set or
                                self.revoking_mn_local_policy_count.yfilter != YFilter.not_set or
                                self.unspecified_count.yfilter != YFilter.not_set or
                                self.user_session_termination_count.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pbri-send-statistics" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/protocol-statistics/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.admin_reason_count.is_set or self.admin_reason_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.admin_reason_count.get_name_leafdata())
                            if (self.mag_handover_different_att_count.is_set or self.mag_handover_different_att_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mag_handover_different_att_count.get_name_leafdata())
                            if (self.mag_handover_same_att_count.is_set or self.mag_handover_same_att_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mag_handover_same_att_count.get_name_leafdata())
                            if (self.mag_handover_unknown_count.is_set or self.mag_handover_unknown_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mag_handover_unknown_count.get_name_leafdata())
                            if (self.network_session_termination_count.is_set or self.network_session_termination_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.network_session_termination_count.get_name_leafdata())
                            if (self.out_of_sync_bce_state_count.is_set or self.out_of_sync_bce_state_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.out_of_sync_bce_state_count.get_name_leafdata())
                            if (self.pbri_count.is_set or self.pbri_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pbri_count.get_name_leafdata())
                            if (self.pbri_drop_count.is_set or self.pbri_drop_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pbri_drop_count.get_name_leafdata())
                            if (self.per_peer_policy_count.is_set or self.per_peer_policy_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.per_peer_policy_count.get_name_leafdata())
                            if (self.revoking_mn_local_policy_count.is_set or self.revoking_mn_local_policy_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.revoking_mn_local_policy_count.get_name_leafdata())
                            if (self.unspecified_count.is_set or self.unspecified_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unspecified_count.get_name_leafdata())
                            if (self.user_session_termination_count.is_set or self.user_session_termination_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.user_session_termination_count.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "admin-reason-count" or name == "mag-handover-different-att-count" or name == "mag-handover-same-att-count" or name == "mag-handover-unknown-count" or name == "network-session-termination-count" or name == "out-of-sync-bce-state-count" or name == "pbri-count" or name == "pbri-drop-count" or name == "per-peer-policy-count" or name == "revoking-mn-local-policy-count" or name == "unspecified-count" or name == "user-session-termination-count"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "admin-reason-count"):
                                self.admin_reason_count = value
                                self.admin_reason_count.value_namespace = name_space
                                self.admin_reason_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "mag-handover-different-att-count"):
                                self.mag_handover_different_att_count = value
                                self.mag_handover_different_att_count.value_namespace = name_space
                                self.mag_handover_different_att_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "mag-handover-same-att-count"):
                                self.mag_handover_same_att_count = value
                                self.mag_handover_same_att_count.value_namespace = name_space
                                self.mag_handover_same_att_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "mag-handover-unknown-count"):
                                self.mag_handover_unknown_count = value
                                self.mag_handover_unknown_count.value_namespace = name_space
                                self.mag_handover_unknown_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "network-session-termination-count"):
                                self.network_session_termination_count = value
                                self.network_session_termination_count.value_namespace = name_space
                                self.network_session_termination_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "out-of-sync-bce-state-count"):
                                self.out_of_sync_bce_state_count = value
                                self.out_of_sync_bce_state_count.value_namespace = name_space
                                self.out_of_sync_bce_state_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "pbri-count"):
                                self.pbri_count = value
                                self.pbri_count.value_namespace = name_space
                                self.pbri_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "pbri-drop-count"):
                                self.pbri_drop_count = value
                                self.pbri_drop_count.value_namespace = name_space
                                self.pbri_drop_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "per-peer-policy-count"):
                                self.per_peer_policy_count = value
                                self.per_peer_policy_count.value_namespace = name_space
                                self.per_peer_policy_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "revoking-mn-local-policy-count"):
                                self.revoking_mn_local_policy_count = value
                                self.revoking_mn_local_policy_count.value_namespace = name_space
                                self.revoking_mn_local_policy_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "unspecified-count"):
                                self.unspecified_count = value
                                self.unspecified_count.value_namespace = name_space
                                self.unspecified_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "user-session-termination-count"):
                                self.user_session_termination_count = value
                                self.user_session_termination_count.value_namespace = name_space
                                self.user_session_termination_count.value_namespace_prefix = name_space_prefix


                    class PbriReceiveStatistics(Entity):
                        """
                        PBRI Receive Statistics
                        
                        .. attribute:: admin_reason_count
                        
                        	Count of Revoc Trigger \- Administrative Reason
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mag_handover_different_att_count
                        
                        	Count of Revoc Trigger \- Inter MAG Handover Different ATT
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mag_handover_same_att_count
                        
                        	Count of Revoc Trigger \- Inter MAG Handover Same ATT
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mag_handover_unknown_count
                        
                        	Count of Revoc Trigger \- Inter MAG Handover Unknown
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: network_session_termination_count
                        
                        	Count of Revoc Trigger \- Access Network Session Termination
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: out_of_sync_bce_state_count
                        
                        	Count of Revoc Trigger \- Possible Out\-of\-Sync BCE State
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pbri_count
                        
                        	Count of PBRIs
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pbri_drop_count
                        
                        	Count of PBRIs dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: per_peer_policy_count
                        
                        	Count of Revoc Trigger \- Per\-Peer Policy
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: revoking_mn_local_policy_count
                        
                        	Count of Revoc Trigger \- Revoking Mobility Node Local Policy
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unspecified_count
                        
                        	Count of Revoc Trigger \- Unspecified
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: user_session_termination_count
                        
                        	Count of Revoc Trigger \- User Init Session Terminatation
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriReceiveStatistics, self).__init__()

                            self.yang_name = "pbri-receive-statistics"
                            self.yang_parent_name = "protocol-statistics"

                            self.admin_reason_count = YLeaf(YType.uint32, "admin-reason-count")

                            self.mag_handover_different_att_count = YLeaf(YType.uint32, "mag-handover-different-att-count")

                            self.mag_handover_same_att_count = YLeaf(YType.uint32, "mag-handover-same-att-count")

                            self.mag_handover_unknown_count = YLeaf(YType.uint32, "mag-handover-unknown-count")

                            self.network_session_termination_count = YLeaf(YType.uint32, "network-session-termination-count")

                            self.out_of_sync_bce_state_count = YLeaf(YType.uint32, "out-of-sync-bce-state-count")

                            self.pbri_count = YLeaf(YType.uint64, "pbri-count")

                            self.pbri_drop_count = YLeaf(YType.uint32, "pbri-drop-count")

                            self.per_peer_policy_count = YLeaf(YType.uint32, "per-peer-policy-count")

                            self.revoking_mn_local_policy_count = YLeaf(YType.uint32, "revoking-mn-local-policy-count")

                            self.unspecified_count = YLeaf(YType.uint32, "unspecified-count")

                            self.user_session_termination_count = YLeaf(YType.uint32, "user-session-termination-count")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("admin_reason_count",
                                            "mag_handover_different_att_count",
                                            "mag_handover_same_att_count",
                                            "mag_handover_unknown_count",
                                            "network_session_termination_count",
                                            "out_of_sync_bce_state_count",
                                            "pbri_count",
                                            "pbri_drop_count",
                                            "per_peer_policy_count",
                                            "revoking_mn_local_policy_count",
                                            "unspecified_count",
                                            "user_session_termination_count") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriReceiveStatistics, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriReceiveStatistics, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.admin_reason_count.is_set or
                                self.mag_handover_different_att_count.is_set or
                                self.mag_handover_same_att_count.is_set or
                                self.mag_handover_unknown_count.is_set or
                                self.network_session_termination_count.is_set or
                                self.out_of_sync_bce_state_count.is_set or
                                self.pbri_count.is_set or
                                self.pbri_drop_count.is_set or
                                self.per_peer_policy_count.is_set or
                                self.revoking_mn_local_policy_count.is_set or
                                self.unspecified_count.is_set or
                                self.user_session_termination_count.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.admin_reason_count.yfilter != YFilter.not_set or
                                self.mag_handover_different_att_count.yfilter != YFilter.not_set or
                                self.mag_handover_same_att_count.yfilter != YFilter.not_set or
                                self.mag_handover_unknown_count.yfilter != YFilter.not_set or
                                self.network_session_termination_count.yfilter != YFilter.not_set or
                                self.out_of_sync_bce_state_count.yfilter != YFilter.not_set or
                                self.pbri_count.yfilter != YFilter.not_set or
                                self.pbri_drop_count.yfilter != YFilter.not_set or
                                self.per_peer_policy_count.yfilter != YFilter.not_set or
                                self.revoking_mn_local_policy_count.yfilter != YFilter.not_set or
                                self.unspecified_count.yfilter != YFilter.not_set or
                                self.user_session_termination_count.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pbri-receive-statistics" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/protocol-statistics/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.admin_reason_count.is_set or self.admin_reason_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.admin_reason_count.get_name_leafdata())
                            if (self.mag_handover_different_att_count.is_set or self.mag_handover_different_att_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mag_handover_different_att_count.get_name_leafdata())
                            if (self.mag_handover_same_att_count.is_set or self.mag_handover_same_att_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mag_handover_same_att_count.get_name_leafdata())
                            if (self.mag_handover_unknown_count.is_set or self.mag_handover_unknown_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mag_handover_unknown_count.get_name_leafdata())
                            if (self.network_session_termination_count.is_set or self.network_session_termination_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.network_session_termination_count.get_name_leafdata())
                            if (self.out_of_sync_bce_state_count.is_set or self.out_of_sync_bce_state_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.out_of_sync_bce_state_count.get_name_leafdata())
                            if (self.pbri_count.is_set or self.pbri_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pbri_count.get_name_leafdata())
                            if (self.pbri_drop_count.is_set or self.pbri_drop_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pbri_drop_count.get_name_leafdata())
                            if (self.per_peer_policy_count.is_set or self.per_peer_policy_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.per_peer_policy_count.get_name_leafdata())
                            if (self.revoking_mn_local_policy_count.is_set or self.revoking_mn_local_policy_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.revoking_mn_local_policy_count.get_name_leafdata())
                            if (self.unspecified_count.is_set or self.unspecified_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unspecified_count.get_name_leafdata())
                            if (self.user_session_termination_count.is_set or self.user_session_termination_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.user_session_termination_count.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "admin-reason-count" or name == "mag-handover-different-att-count" or name == "mag-handover-same-att-count" or name == "mag-handover-unknown-count" or name == "network-session-termination-count" or name == "out-of-sync-bce-state-count" or name == "pbri-count" or name == "pbri-drop-count" or name == "per-peer-policy-count" or name == "revoking-mn-local-policy-count" or name == "unspecified-count" or name == "user-session-termination-count"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "admin-reason-count"):
                                self.admin_reason_count = value
                                self.admin_reason_count.value_namespace = name_space
                                self.admin_reason_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "mag-handover-different-att-count"):
                                self.mag_handover_different_att_count = value
                                self.mag_handover_different_att_count.value_namespace = name_space
                                self.mag_handover_different_att_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "mag-handover-same-att-count"):
                                self.mag_handover_same_att_count = value
                                self.mag_handover_same_att_count.value_namespace = name_space
                                self.mag_handover_same_att_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "mag-handover-unknown-count"):
                                self.mag_handover_unknown_count = value
                                self.mag_handover_unknown_count.value_namespace = name_space
                                self.mag_handover_unknown_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "network-session-termination-count"):
                                self.network_session_termination_count = value
                                self.network_session_termination_count.value_namespace = name_space
                                self.network_session_termination_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "out-of-sync-bce-state-count"):
                                self.out_of_sync_bce_state_count = value
                                self.out_of_sync_bce_state_count.value_namespace = name_space
                                self.out_of_sync_bce_state_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "pbri-count"):
                                self.pbri_count = value
                                self.pbri_count.value_namespace = name_space
                                self.pbri_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "pbri-drop-count"):
                                self.pbri_drop_count = value
                                self.pbri_drop_count.value_namespace = name_space
                                self.pbri_drop_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "per-peer-policy-count"):
                                self.per_peer_policy_count = value
                                self.per_peer_policy_count.value_namespace = name_space
                                self.per_peer_policy_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "revoking-mn-local-policy-count"):
                                self.revoking_mn_local_policy_count = value
                                self.revoking_mn_local_policy_count.value_namespace = name_space
                                self.revoking_mn_local_policy_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "unspecified-count"):
                                self.unspecified_count = value
                                self.unspecified_count.value_namespace = name_space
                                self.unspecified_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "user-session-termination-count"):
                                self.user_session_termination_count = value
                                self.user_session_termination_count.value_namespace = name_space
                                self.user_session_termination_count.value_namespace_prefix = name_space_prefix


                    class PbraSendStatistics(Entity):
                        """
                        PBRA Send Statistics
                        
                        .. attribute:: hoa_required_count
                        
                        	Count of Revoc Status \- IPv4 Home Address Option Required
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mn_attached_count
                        
                        	Count of Revoc Status \- Revocation Failed \- MN is Attached
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mn_identity_required_count
                        
                        	Count of Revoc Status \- Revoked Mobile Node Identity Required
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_author_for_global_revoc_count
                        
                        	Count of Revoc Status \- Global Revocation NOT Authorized
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_binding_count
                        
                        	Count of Revoc Status \- Binding Does Not Exist
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: partial_success_count
                        
                        	Count of Revoc Status \- Partial Success
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pbr_not_supported_count
                        
                        	Count of Revoc Status \- Proxy Binding Revocation NOT Supported
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pbra_count
                        
                        	Count of PBRAs
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pbra_drop_count
                        
                        	Count of PBRAs dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: revoc_function_not_supported_count
                        
                        	Count of Revoc Status \- Revocation Function NOT Supported
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: success_count
                        
                        	Count of Revoc Status \- Success
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_revoc_trigger_count
                        
                        	Count of Revoc Status \- Revocation Trigger NOT supported
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraSendStatistics, self).__init__()

                            self.yang_name = "pbra-send-statistics"
                            self.yang_parent_name = "protocol-statistics"

                            self.hoa_required_count = YLeaf(YType.uint32, "hoa-required-count")

                            self.mn_attached_count = YLeaf(YType.uint32, "mn-attached-count")

                            self.mn_identity_required_count = YLeaf(YType.uint32, "mn-identity-required-count")

                            self.no_author_for_global_revoc_count = YLeaf(YType.uint32, "no-author-for-global-revoc-count")

                            self.no_binding_count = YLeaf(YType.uint32, "no-binding-count")

                            self.partial_success_count = YLeaf(YType.uint32, "partial-success-count")

                            self.pbr_not_supported_count = YLeaf(YType.uint32, "pbr-not-supported-count")

                            self.pbra_count = YLeaf(YType.uint64, "pbra-count")

                            self.pbra_drop_count = YLeaf(YType.uint32, "pbra-drop-count")

                            self.revoc_function_not_supported_count = YLeaf(YType.uint32, "revoc-function-not-supported-count")

                            self.success_count = YLeaf(YType.uint32, "success-count")

                            self.unknown_revoc_trigger_count = YLeaf(YType.uint32, "unknown-revoc-trigger-count")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("hoa_required_count",
                                            "mn_attached_count",
                                            "mn_identity_required_count",
                                            "no_author_for_global_revoc_count",
                                            "no_binding_count",
                                            "partial_success_count",
                                            "pbr_not_supported_count",
                                            "pbra_count",
                                            "pbra_drop_count",
                                            "revoc_function_not_supported_count",
                                            "success_count",
                                            "unknown_revoc_trigger_count") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraSendStatistics, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraSendStatistics, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.hoa_required_count.is_set or
                                self.mn_attached_count.is_set or
                                self.mn_identity_required_count.is_set or
                                self.no_author_for_global_revoc_count.is_set or
                                self.no_binding_count.is_set or
                                self.partial_success_count.is_set or
                                self.pbr_not_supported_count.is_set or
                                self.pbra_count.is_set or
                                self.pbra_drop_count.is_set or
                                self.revoc_function_not_supported_count.is_set or
                                self.success_count.is_set or
                                self.unknown_revoc_trigger_count.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.hoa_required_count.yfilter != YFilter.not_set or
                                self.mn_attached_count.yfilter != YFilter.not_set or
                                self.mn_identity_required_count.yfilter != YFilter.not_set or
                                self.no_author_for_global_revoc_count.yfilter != YFilter.not_set or
                                self.no_binding_count.yfilter != YFilter.not_set or
                                self.partial_success_count.yfilter != YFilter.not_set or
                                self.pbr_not_supported_count.yfilter != YFilter.not_set or
                                self.pbra_count.yfilter != YFilter.not_set or
                                self.pbra_drop_count.yfilter != YFilter.not_set or
                                self.revoc_function_not_supported_count.yfilter != YFilter.not_set or
                                self.success_count.yfilter != YFilter.not_set or
                                self.unknown_revoc_trigger_count.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pbra-send-statistics" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/protocol-statistics/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.hoa_required_count.is_set or self.hoa_required_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hoa_required_count.get_name_leafdata())
                            if (self.mn_attached_count.is_set or self.mn_attached_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mn_attached_count.get_name_leafdata())
                            if (self.mn_identity_required_count.is_set or self.mn_identity_required_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mn_identity_required_count.get_name_leafdata())
                            if (self.no_author_for_global_revoc_count.is_set or self.no_author_for_global_revoc_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_author_for_global_revoc_count.get_name_leafdata())
                            if (self.no_binding_count.is_set or self.no_binding_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_binding_count.get_name_leafdata())
                            if (self.partial_success_count.is_set or self.partial_success_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.partial_success_count.get_name_leafdata())
                            if (self.pbr_not_supported_count.is_set or self.pbr_not_supported_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pbr_not_supported_count.get_name_leafdata())
                            if (self.pbra_count.is_set or self.pbra_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pbra_count.get_name_leafdata())
                            if (self.pbra_drop_count.is_set or self.pbra_drop_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pbra_drop_count.get_name_leafdata())
                            if (self.revoc_function_not_supported_count.is_set or self.revoc_function_not_supported_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.revoc_function_not_supported_count.get_name_leafdata())
                            if (self.success_count.is_set or self.success_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.success_count.get_name_leafdata())
                            if (self.unknown_revoc_trigger_count.is_set or self.unknown_revoc_trigger_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unknown_revoc_trigger_count.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "hoa-required-count" or name == "mn-attached-count" or name == "mn-identity-required-count" or name == "no-author-for-global-revoc-count" or name == "no-binding-count" or name == "partial-success-count" or name == "pbr-not-supported-count" or name == "pbra-count" or name == "pbra-drop-count" or name == "revoc-function-not-supported-count" or name == "success-count" or name == "unknown-revoc-trigger-count"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "hoa-required-count"):
                                self.hoa_required_count = value
                                self.hoa_required_count.value_namespace = name_space
                                self.hoa_required_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "mn-attached-count"):
                                self.mn_attached_count = value
                                self.mn_attached_count.value_namespace = name_space
                                self.mn_attached_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "mn-identity-required-count"):
                                self.mn_identity_required_count = value
                                self.mn_identity_required_count.value_namespace = name_space
                                self.mn_identity_required_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-author-for-global-revoc-count"):
                                self.no_author_for_global_revoc_count = value
                                self.no_author_for_global_revoc_count.value_namespace = name_space
                                self.no_author_for_global_revoc_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-binding-count"):
                                self.no_binding_count = value
                                self.no_binding_count.value_namespace = name_space
                                self.no_binding_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "partial-success-count"):
                                self.partial_success_count = value
                                self.partial_success_count.value_namespace = name_space
                                self.partial_success_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "pbr-not-supported-count"):
                                self.pbr_not_supported_count = value
                                self.pbr_not_supported_count.value_namespace = name_space
                                self.pbr_not_supported_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "pbra-count"):
                                self.pbra_count = value
                                self.pbra_count.value_namespace = name_space
                                self.pbra_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "pbra-drop-count"):
                                self.pbra_drop_count = value
                                self.pbra_drop_count.value_namespace = name_space
                                self.pbra_drop_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "revoc-function-not-supported-count"):
                                self.revoc_function_not_supported_count = value
                                self.revoc_function_not_supported_count.value_namespace = name_space
                                self.revoc_function_not_supported_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "success-count"):
                                self.success_count = value
                                self.success_count.value_namespace = name_space
                                self.success_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "unknown-revoc-trigger-count"):
                                self.unknown_revoc_trigger_count = value
                                self.unknown_revoc_trigger_count.value_namespace = name_space
                                self.unknown_revoc_trigger_count.value_namespace_prefix = name_space_prefix


                    class PbraReceiveStatistics(Entity):
                        """
                        PBRA Receive Statistics
                        
                        .. attribute:: hoa_required_count
                        
                        	Count of Revoc Status \- IPv4 Home Address Option Required
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mn_attached_count
                        
                        	Count of Revoc Status \- Revocation Failed \- MN is Attached
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mn_identity_required_count
                        
                        	Count of Revoc Status \- Revoked Mobile Node Identity Required
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_author_for_global_revoc_count
                        
                        	Count of Revoc Status \- Global Revocation NOT Authorized
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_binding_count
                        
                        	Count of Revoc Status \- Binding Does Not Exist
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: partial_success_count
                        
                        	Count of Revoc Status \- Partial Success
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pbr_not_supported_count
                        
                        	Count of Revoc Status \- Proxy Binding Revocation NOT Supported
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pbra_count
                        
                        	Count of PBRAs
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pbra_drop_count
                        
                        	Count of PBRAs dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: revoc_function_not_supported_count
                        
                        	Count of Revoc Status \- Revocation Function NOT Supported
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: success_count
                        
                        	Count of Revoc Status \- Success
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_revoc_trigger_count
                        
                        	Count of Revoc Status \- Revocation Trigger NOT supported
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraReceiveStatistics, self).__init__()

                            self.yang_name = "pbra-receive-statistics"
                            self.yang_parent_name = "protocol-statistics"

                            self.hoa_required_count = YLeaf(YType.uint32, "hoa-required-count")

                            self.mn_attached_count = YLeaf(YType.uint32, "mn-attached-count")

                            self.mn_identity_required_count = YLeaf(YType.uint32, "mn-identity-required-count")

                            self.no_author_for_global_revoc_count = YLeaf(YType.uint32, "no-author-for-global-revoc-count")

                            self.no_binding_count = YLeaf(YType.uint32, "no-binding-count")

                            self.partial_success_count = YLeaf(YType.uint32, "partial-success-count")

                            self.pbr_not_supported_count = YLeaf(YType.uint32, "pbr-not-supported-count")

                            self.pbra_count = YLeaf(YType.uint64, "pbra-count")

                            self.pbra_drop_count = YLeaf(YType.uint32, "pbra-drop-count")

                            self.revoc_function_not_supported_count = YLeaf(YType.uint32, "revoc-function-not-supported-count")

                            self.success_count = YLeaf(YType.uint32, "success-count")

                            self.unknown_revoc_trigger_count = YLeaf(YType.uint32, "unknown-revoc-trigger-count")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("hoa_required_count",
                                            "mn_attached_count",
                                            "mn_identity_required_count",
                                            "no_author_for_global_revoc_count",
                                            "no_binding_count",
                                            "partial_success_count",
                                            "pbr_not_supported_count",
                                            "pbra_count",
                                            "pbra_drop_count",
                                            "revoc_function_not_supported_count",
                                            "success_count",
                                            "unknown_revoc_trigger_count") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraReceiveStatistics, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraReceiveStatistics, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.hoa_required_count.is_set or
                                self.mn_attached_count.is_set or
                                self.mn_identity_required_count.is_set or
                                self.no_author_for_global_revoc_count.is_set or
                                self.no_binding_count.is_set or
                                self.partial_success_count.is_set or
                                self.pbr_not_supported_count.is_set or
                                self.pbra_count.is_set or
                                self.pbra_drop_count.is_set or
                                self.revoc_function_not_supported_count.is_set or
                                self.success_count.is_set or
                                self.unknown_revoc_trigger_count.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.hoa_required_count.yfilter != YFilter.not_set or
                                self.mn_attached_count.yfilter != YFilter.not_set or
                                self.mn_identity_required_count.yfilter != YFilter.not_set or
                                self.no_author_for_global_revoc_count.yfilter != YFilter.not_set or
                                self.no_binding_count.yfilter != YFilter.not_set or
                                self.partial_success_count.yfilter != YFilter.not_set or
                                self.pbr_not_supported_count.yfilter != YFilter.not_set or
                                self.pbra_count.yfilter != YFilter.not_set or
                                self.pbra_drop_count.yfilter != YFilter.not_set or
                                self.revoc_function_not_supported_count.yfilter != YFilter.not_set or
                                self.success_count.yfilter != YFilter.not_set or
                                self.unknown_revoc_trigger_count.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pbra-receive-statistics" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/protocol-statistics/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.hoa_required_count.is_set or self.hoa_required_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hoa_required_count.get_name_leafdata())
                            if (self.mn_attached_count.is_set or self.mn_attached_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mn_attached_count.get_name_leafdata())
                            if (self.mn_identity_required_count.is_set or self.mn_identity_required_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mn_identity_required_count.get_name_leafdata())
                            if (self.no_author_for_global_revoc_count.is_set or self.no_author_for_global_revoc_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_author_for_global_revoc_count.get_name_leafdata())
                            if (self.no_binding_count.is_set or self.no_binding_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_binding_count.get_name_leafdata())
                            if (self.partial_success_count.is_set or self.partial_success_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.partial_success_count.get_name_leafdata())
                            if (self.pbr_not_supported_count.is_set or self.pbr_not_supported_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pbr_not_supported_count.get_name_leafdata())
                            if (self.pbra_count.is_set or self.pbra_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pbra_count.get_name_leafdata())
                            if (self.pbra_drop_count.is_set or self.pbra_drop_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pbra_drop_count.get_name_leafdata())
                            if (self.revoc_function_not_supported_count.is_set or self.revoc_function_not_supported_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.revoc_function_not_supported_count.get_name_leafdata())
                            if (self.success_count.is_set or self.success_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.success_count.get_name_leafdata())
                            if (self.unknown_revoc_trigger_count.is_set or self.unknown_revoc_trigger_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unknown_revoc_trigger_count.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "hoa-required-count" or name == "mn-attached-count" or name == "mn-identity-required-count" or name == "no-author-for-global-revoc-count" or name == "no-binding-count" or name == "partial-success-count" or name == "pbr-not-supported-count" or name == "pbra-count" or name == "pbra-drop-count" or name == "revoc-function-not-supported-count" or name == "success-count" or name == "unknown-revoc-trigger-count"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "hoa-required-count"):
                                self.hoa_required_count = value
                                self.hoa_required_count.value_namespace = name_space
                                self.hoa_required_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "mn-attached-count"):
                                self.mn_attached_count = value
                                self.mn_attached_count.value_namespace = name_space
                                self.mn_attached_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "mn-identity-required-count"):
                                self.mn_identity_required_count = value
                                self.mn_identity_required_count.value_namespace = name_space
                                self.mn_identity_required_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-author-for-global-revoc-count"):
                                self.no_author_for_global_revoc_count = value
                                self.no_author_for_global_revoc_count.value_namespace = name_space
                                self.no_author_for_global_revoc_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-binding-count"):
                                self.no_binding_count = value
                                self.no_binding_count.value_namespace = name_space
                                self.no_binding_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "partial-success-count"):
                                self.partial_success_count = value
                                self.partial_success_count.value_namespace = name_space
                                self.partial_success_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "pbr-not-supported-count"):
                                self.pbr_not_supported_count = value
                                self.pbr_not_supported_count.value_namespace = name_space
                                self.pbr_not_supported_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "pbra-count"):
                                self.pbra_count = value
                                self.pbra_count.value_namespace = name_space
                                self.pbra_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "pbra-drop-count"):
                                self.pbra_drop_count = value
                                self.pbra_drop_count.value_namespace = name_space
                                self.pbra_drop_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "revoc-function-not-supported-count"):
                                self.revoc_function_not_supported_count = value
                                self.revoc_function_not_supported_count.value_namespace = name_space
                                self.revoc_function_not_supported_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "success-count"):
                                self.success_count = value
                                self.success_count.value_namespace = name_space
                                self.success_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "unknown-revoc-trigger-count"):
                                self.unknown_revoc_trigger_count = value
                                self.unknown_revoc_trigger_count.value_namespace = name_space
                                self.unknown_revoc_trigger_count.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.pba_send_statistics is not None and self.pba_send_statistics.has_data()) or
                            (self.pbra_receive_statistics is not None and self.pbra_receive_statistics.has_data()) or
                            (self.pbra_send_statistics is not None and self.pbra_send_statistics.has_data()) or
                            (self.pbri_receive_statistics is not None and self.pbri_receive_statistics.has_data()) or
                            (self.pbri_send_statistics is not None and self.pbri_send_statistics.has_data()) or
                            (self.pbu_receive_statistics is not None and self.pbu_receive_statistics.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.pba_send_statistics is not None and self.pba_send_statistics.has_operation()) or
                            (self.pbra_receive_statistics is not None and self.pbra_receive_statistics.has_operation()) or
                            (self.pbra_send_statistics is not None and self.pbra_send_statistics.has_operation()) or
                            (self.pbri_receive_statistics is not None and self.pbri_receive_statistics.has_operation()) or
                            (self.pbri_send_statistics is not None and self.pbri_send_statistics.has_operation()) or
                            (self.pbu_receive_statistics is not None and self.pbu_receive_statistics.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "protocol-statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "pba-send-statistics"):
                            if (self.pba_send_statistics is None):
                                self.pba_send_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbaSendStatistics()
                                self.pba_send_statistics.parent = self
                                self._children_name_map["pba_send_statistics"] = "pba-send-statistics"
                            return self.pba_send_statistics

                        if (child_yang_name == "pbra-receive-statistics"):
                            if (self.pbra_receive_statistics is None):
                                self.pbra_receive_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraReceiveStatistics()
                                self.pbra_receive_statistics.parent = self
                                self._children_name_map["pbra_receive_statistics"] = "pbra-receive-statistics"
                            return self.pbra_receive_statistics

                        if (child_yang_name == "pbra-send-statistics"):
                            if (self.pbra_send_statistics is None):
                                self.pbra_send_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraSendStatistics()
                                self.pbra_send_statistics.parent = self
                                self._children_name_map["pbra_send_statistics"] = "pbra-send-statistics"
                            return self.pbra_send_statistics

                        if (child_yang_name == "pbri-receive-statistics"):
                            if (self.pbri_receive_statistics is None):
                                self.pbri_receive_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriReceiveStatistics()
                                self.pbri_receive_statistics.parent = self
                                self._children_name_map["pbri_receive_statistics"] = "pbri-receive-statistics"
                            return self.pbri_receive_statistics

                        if (child_yang_name == "pbri-send-statistics"):
                            if (self.pbri_send_statistics is None):
                                self.pbri_send_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriSendStatistics()
                                self.pbri_send_statistics.parent = self
                                self._children_name_map["pbri_send_statistics"] = "pbri-send-statistics"
                            return self.pbri_send_statistics

                        if (child_yang_name == "pbu-receive-statistics"):
                            if (self.pbu_receive_statistics is None):
                                self.pbu_receive_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbuReceiveStatistics()
                                self.pbu_receive_statistics.parent = self
                                self._children_name_map["pbu_receive_statistics"] = "pbu-receive-statistics"
                            return self.pbu_receive_statistics

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "pba-send-statistics" or name == "pbra-receive-statistics" or name == "pbra-send-statistics" or name == "pbri-receive-statistics" or name == "pbri-send-statistics" or name == "pbu-receive-statistics"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class AccountingStatistics(Entity):
                    """
                    LMA Accounting Statistics
                    
                    .. attribute:: accounting_start_sent_count
                    
                    	Count of Accounting Start Records Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: accounting_stop_sent_count
                    
                    	Count of Accounting Stop Records Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: accounting_update_sent_count
                    
                    	Count of Accounting Update Records Sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.Statistics.Global_.AccountingStatistics, self).__init__()

                        self.yang_name = "accounting-statistics"
                        self.yang_parent_name = "global"

                        self.accounting_start_sent_count = YLeaf(YType.uint64, "accounting-start-sent-count")

                        self.accounting_stop_sent_count = YLeaf(YType.uint64, "accounting-stop-sent-count")

                        self.accounting_update_sent_count = YLeaf(YType.uint64, "accounting-update-sent-count")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("accounting_start_sent_count",
                                        "accounting_stop_sent_count",
                                        "accounting_update_sent_count") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pmipv6.Lma.Statistics.Global_.AccountingStatistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pmipv6.Lma.Statistics.Global_.AccountingStatistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.accounting_start_sent_count.is_set or
                            self.accounting_stop_sent_count.is_set or
                            self.accounting_update_sent_count.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.accounting_start_sent_count.yfilter != YFilter.not_set or
                            self.accounting_stop_sent_count.yfilter != YFilter.not_set or
                            self.accounting_update_sent_count.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "accounting-statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.accounting_start_sent_count.is_set or self.accounting_start_sent_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accounting_start_sent_count.get_name_leafdata())
                        if (self.accounting_stop_sent_count.is_set or self.accounting_stop_sent_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accounting_stop_sent_count.get_name_leafdata())
                        if (self.accounting_update_sent_count.is_set or self.accounting_update_sent_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accounting_update_sent_count.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "accounting-start-sent-count" or name == "accounting-stop-sent-count" or name == "accounting-update-sent-count"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "accounting-start-sent-count"):
                            self.accounting_start_sent_count = value
                            self.accounting_start_sent_count.value_namespace = name_space
                            self.accounting_start_sent_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "accounting-stop-sent-count"):
                            self.accounting_stop_sent_count = value
                            self.accounting_stop_sent_count.value_namespace = name_space
                            self.accounting_stop_sent_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "accounting-update-sent-count"):
                            self.accounting_update_sent_count = value
                            self.accounting_update_sent_count.value_namespace = name_space
                            self.accounting_update_sent_count.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.bce_count.is_set or
                        self.handoff_count.is_set or
                        self.lma_identifier.is_set or
                        self.multi_tenant_count.is_set or
                        self.single_tenant_count.is_set or
                        (self.accounting_statistics is not None and self.accounting_statistics.has_data()) or
                        (self.packet_statistics is not None and self.packet_statistics.has_data()) or
                        (self.protocol_statistics is not None and self.protocol_statistics.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bce_count.yfilter != YFilter.not_set or
                        self.handoff_count.yfilter != YFilter.not_set or
                        self.lma_identifier.yfilter != YFilter.not_set or
                        self.multi_tenant_count.yfilter != YFilter.not_set or
                        self.single_tenant_count.yfilter != YFilter.not_set or
                        (self.accounting_statistics is not None and self.accounting_statistics.has_operation()) or
                        (self.packet_statistics is not None and self.packet_statistics.has_operation()) or
                        (self.protocol_statistics is not None and self.protocol_statistics.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "global" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bce_count.is_set or self.bce_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bce_count.get_name_leafdata())
                    if (self.handoff_count.is_set or self.handoff_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.handoff_count.get_name_leafdata())
                    if (self.lma_identifier.is_set or self.lma_identifier.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.lma_identifier.get_name_leafdata())
                    if (self.multi_tenant_count.is_set or self.multi_tenant_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.multi_tenant_count.get_name_leafdata())
                    if (self.single_tenant_count.is_set or self.single_tenant_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.single_tenant_count.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "accounting-statistics"):
                        if (self.accounting_statistics is None):
                            self.accounting_statistics = Pmipv6.Lma.Statistics.Global_.AccountingStatistics()
                            self.accounting_statistics.parent = self
                            self._children_name_map["accounting_statistics"] = "accounting-statistics"
                        return self.accounting_statistics

                    if (child_yang_name == "packet-statistics"):
                        if (self.packet_statistics is None):
                            self.packet_statistics = Pmipv6.Lma.Statistics.Global_.PacketStatistics()
                            self.packet_statistics.parent = self
                            self._children_name_map["packet_statistics"] = "packet-statistics"
                        return self.packet_statistics

                    if (child_yang_name == "protocol-statistics"):
                        if (self.protocol_statistics is None):
                            self.protocol_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics()
                            self.protocol_statistics.parent = self
                            self._children_name_map["protocol_statistics"] = "protocol-statistics"
                        return self.protocol_statistics

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "accounting-statistics" or name == "packet-statistics" or name == "protocol-statistics" or name == "bce-count" or name == "handoff-count" or name == "lma-identifier" or name == "multi-tenant-count" or name == "single-tenant-count"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bce-count"):
                        self.bce_count = value
                        self.bce_count.value_namespace = name_space
                        self.bce_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "handoff-count"):
                        self.handoff_count = value
                        self.handoff_count.value_namespace = name_space
                        self.handoff_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "lma-identifier"):
                        self.lma_identifier = value
                        self.lma_identifier.value_namespace = name_space
                        self.lma_identifier.value_namespace_prefix = name_space_prefix
                    if(value_path == "multi-tenant-count"):
                        self.multi_tenant_count = value
                        self.multi_tenant_count.value_namespace = name_space
                        self.multi_tenant_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "single-tenant-count"):
                        self.single_tenant_count = value
                        self.single_tenant_count.value_namespace = name_space
                        self.single_tenant_count.value_namespace_prefix = name_space_prefix


            class MagStatistics(Entity):
                """
                Table of MAGStatistics
                
                .. attribute:: mag_statistic
                
                	Peer MAG statistics
                	**type**\: list of    :py:class:`MagStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics.MagStatistic>`
                
                

                """

                _prefix = 'ip-mobileip-oper'
                _revision = '2016-03-10'

                def __init__(self):
                    super(Pmipv6.Lma.Statistics.MagStatistics, self).__init__()

                    self.yang_name = "mag-statistics"
                    self.yang_parent_name = "statistics"

                    self.mag_statistic = YList(self)

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
                                super(Pmipv6.Lma.Statistics.MagStatistics, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Pmipv6.Lma.Statistics.MagStatistics, self).__setattr__(name, value)


                class MagStatistic(Entity):
                    """
                    Peer MAG statistics
                    
                    .. attribute:: mag_name  <key>
                    
                    	Peer MAG Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: lma_identifier
                    
                    	LMA Identifier
                    	**type**\:  str
                    
                    .. attribute:: protocol_statistics
                    
                    	LMA Protocol Statistics
                    	**type**\:   :py:class:`ProtocolStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics>`
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic, self).__init__()

                        self.yang_name = "mag-statistic"
                        self.yang_parent_name = "mag-statistics"

                        self.mag_name = YLeaf(YType.str, "mag-name")

                        self.lma_identifier = YLeaf(YType.str, "lma-identifier")

                        self.protocol_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics()
                        self.protocol_statistics.parent = self
                        self._children_name_map["protocol_statistics"] = "protocol-statistics"
                        self._children_yang_names.add("protocol-statistics")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("mag_name",
                                        "lma_identifier") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic, self).__setattr__(name, value)


                    class ProtocolStatistics(Entity):
                        """
                        LMA Protocol Statistics
                        
                        .. attribute:: pba_send_statistics
                        
                        	PBA Send Statistics
                        	**type**\:   :py:class:`PbaSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbaSendStatistics>`
                        
                        .. attribute:: pbra_receive_statistics
                        
                        	PBRA Receive Statistics
                        	**type**\:   :py:class:`PbraReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraReceiveStatistics>`
                        
                        .. attribute:: pbra_send_statistics
                        
                        	PBRA Send Statistics
                        	**type**\:   :py:class:`PbraSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraSendStatistics>`
                        
                        .. attribute:: pbri_receive_statistics
                        
                        	PBRI Receive Statistics
                        	**type**\:   :py:class:`PbriReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriReceiveStatistics>`
                        
                        .. attribute:: pbri_send_statistics
                        
                        	PBRI Send Statistics
                        	**type**\:   :py:class:`PbriSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriSendStatistics>`
                        
                        .. attribute:: pbu_receive_statistics
                        
                        	PBU Receive Statistics
                        	**type**\:   :py:class:`PbuReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbuReceiveStatistics>`
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics, self).__init__()

                            self.yang_name = "protocol-statistics"
                            self.yang_parent_name = "mag-statistic"

                            self.pba_send_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbaSendStatistics()
                            self.pba_send_statistics.parent = self
                            self._children_name_map["pba_send_statistics"] = "pba-send-statistics"
                            self._children_yang_names.add("pba-send-statistics")

                            self.pbra_receive_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraReceiveStatistics()
                            self.pbra_receive_statistics.parent = self
                            self._children_name_map["pbra_receive_statistics"] = "pbra-receive-statistics"
                            self._children_yang_names.add("pbra-receive-statistics")

                            self.pbra_send_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraSendStatistics()
                            self.pbra_send_statistics.parent = self
                            self._children_name_map["pbra_send_statistics"] = "pbra-send-statistics"
                            self._children_yang_names.add("pbra-send-statistics")

                            self.pbri_receive_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriReceiveStatistics()
                            self.pbri_receive_statistics.parent = self
                            self._children_name_map["pbri_receive_statistics"] = "pbri-receive-statistics"
                            self._children_yang_names.add("pbri-receive-statistics")

                            self.pbri_send_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriSendStatistics()
                            self.pbri_send_statistics.parent = self
                            self._children_name_map["pbri_send_statistics"] = "pbri-send-statistics"
                            self._children_yang_names.add("pbri-send-statistics")

                            self.pbu_receive_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbuReceiveStatistics()
                            self.pbu_receive_statistics.parent = self
                            self._children_name_map["pbu_receive_statistics"] = "pbu-receive-statistics"
                            self._children_yang_names.add("pbu-receive-statistics")


                        class PbuReceiveStatistics(Entity):
                            """
                            PBU Receive Statistics
                            
                            .. attribute:: pbu_count
                            
                            	Count of PBUs
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbu_drop_count
                            
                            	Count of PBUs Dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbuReceiveStatistics, self).__init__()

                                self.yang_name = "pbu-receive-statistics"
                                self.yang_parent_name = "protocol-statistics"

                                self.pbu_count = YLeaf(YType.uint64, "pbu-count")

                                self.pbu_drop_count = YLeaf(YType.uint32, "pbu-drop-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("pbu_count",
                                                "pbu_drop_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbuReceiveStatistics, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbuReceiveStatistics, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.pbu_count.is_set or
                                    self.pbu_drop_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.pbu_count.yfilter != YFilter.not_set or
                                    self.pbu_drop_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pbu-receive-statistics" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.pbu_count.is_set or self.pbu_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbu_count.get_name_leafdata())
                                if (self.pbu_drop_count.is_set or self.pbu_drop_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbu_drop_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "pbu-count" or name == "pbu-drop-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "pbu-count"):
                                    self.pbu_count = value
                                    self.pbu_count.value_namespace = name_space
                                    self.pbu_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbu-drop-count"):
                                    self.pbu_drop_count = value
                                    self.pbu_drop_count.value_namespace = name_space
                                    self.pbu_drop_count.value_namespace_prefix = name_space_prefix


                        class PbaSendStatistics(Entity):
                            """
                            PBA Send Statistics
                            
                            .. attribute:: accepted_count
                            
                            	Count of Status Code \- Binding Update accepted
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: admin_failure_count
                            
                            	Count of Status Code \- Administratively prohibited
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_failure_count
                            
                            	Count of Status Code \- Auth Fail
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bad_sequence_failure_count
                            
                            	Count of Status Code \- Sequence number out of window
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: gre_key_opt_required_count
                            
                            	Count of Status Code \- GRE Key option is required
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: home_reg_failure_count
                            
                            	Count of Status Code \- Home registration not supported
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: home_subnet_failure_count
                            
                            	Count of Status Code \- Not home subnet
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: missing_access_tech_type_opt_count
                            
                            	Count of Status Code \- Missing ATT option
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: missing_hi_opt_count
                            
                            	Count of Status Code \- Missing Handoff Indicator
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: missing_hnp_opt_count
                            
                            	Count of Status Code \- Missing Home Network Prefix option
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: missing_mn_id_opt_count
                            
                            	Count of Status Code \- Missing MN identifier option
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: multiple_ipv4_ho_a_not_supported_count
                            
                            	Count of Status Code \- Multiple IPv4 HoA not supported
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_hnp_count
                            
                            	Count of Status Code \- Not authorized for HNP
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_ipv4_hoa_count
                            
                            	Count of Status Code \- Not authorized for IPv4 HoA
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_ipv4_mobility_count
                            
                            	Count of Status Code \- Not authorized for IPv4 mobility
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_ipv6_mobility_count
                            
                            	Count of Status Code \- Not authorized for IPv6 mobility
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_proxy_reg_count
                            
                            	Count of Status Code \- MAG not auth.for proxyreg
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: not_lma_for_this_mn_count
                            
                            	Count of Status Code \- Not LMA for this Mobile Node
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pba_count
                            
                            	Count of PBAs
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pba_drop_count
                            
                            	Count of PBAs dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: proxy_reg_not_enabled_count
                            
                            	Count of Status Code \- Proxy Registration not enabled
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: received_hnps_do_not_match_bce_hnps_count
                            
                            	Count of Status Code \- Recevied HNPs do not match with BCE
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: reg_type_failure_count
                            
                            	Count of Status Code \- Registration type change
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: resource_failure_count
                            
                            	Count of Status Code \- Insufficient resources
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: timestamp_lower_than_previous_accepted_count
                            
                            	Count of Status Code \- Timestamp lower than previous accepted
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: timestamp_mismatch_count
                            
                            	Count of Status Code \- Invalid timestamp value
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_count
                            
                            	Count of Status Code \- Last BA status code sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unspecified_failure_count
                            
                            	Count of Status Code \- Reason unspecified
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbaSendStatistics, self).__init__()

                                self.yang_name = "pba-send-statistics"
                                self.yang_parent_name = "protocol-statistics"

                                self.accepted_count = YLeaf(YType.uint32, "accepted-count")

                                self.admin_failure_count = YLeaf(YType.uint32, "admin-failure-count")

                                self.authen_failure_count = YLeaf(YType.uint32, "authen-failure-count")

                                self.bad_sequence_failure_count = YLeaf(YType.uint32, "bad-sequence-failure-count")

                                self.gre_key_opt_required_count = YLeaf(YType.uint32, "gre-key-opt-required-count")

                                self.home_reg_failure_count = YLeaf(YType.uint32, "home-reg-failure-count")

                                self.home_subnet_failure_count = YLeaf(YType.uint32, "home-subnet-failure-count")

                                self.missing_access_tech_type_opt_count = YLeaf(YType.uint32, "missing-access-tech-type-opt-count")

                                self.missing_hi_opt_count = YLeaf(YType.uint32, "missing-hi-opt-count")

                                self.missing_hnp_opt_count = YLeaf(YType.uint32, "missing-hnp-opt-count")

                                self.missing_mn_id_opt_count = YLeaf(YType.uint32, "missing-mn-id-opt-count")

                                self.multiple_ipv4_ho_a_not_supported_count = YLeaf(YType.uint32, "multiple-ipv4-ho-a-not-supported-count")

                                self.no_author_for_hnp_count = YLeaf(YType.uint32, "no-author-for-hnp-count")

                                self.no_author_for_ipv4_hoa_count = YLeaf(YType.uint32, "no-author-for-ipv4-hoa-count")

                                self.no_author_for_ipv4_mobility_count = YLeaf(YType.uint32, "no-author-for-ipv4-mobility-count")

                                self.no_author_for_ipv6_mobility_count = YLeaf(YType.uint32, "no-author-for-ipv6-mobility-count")

                                self.no_author_for_proxy_reg_count = YLeaf(YType.uint32, "no-author-for-proxy-reg-count")

                                self.not_lma_for_this_mn_count = YLeaf(YType.uint32, "not-lma-for-this-mn-count")

                                self.pba_count = YLeaf(YType.uint64, "pba-count")

                                self.pba_drop_count = YLeaf(YType.uint32, "pba-drop-count")

                                self.proxy_reg_not_enabled_count = YLeaf(YType.uint32, "proxy-reg-not-enabled-count")

                                self.received_hnps_do_not_match_bce_hnps_count = YLeaf(YType.uint32, "received-hnps-do-not-match-bce-hnps-count")

                                self.reg_type_failure_count = YLeaf(YType.uint32, "reg-type-failure-count")

                                self.resource_failure_count = YLeaf(YType.uint32, "resource-failure-count")

                                self.timestamp_lower_than_previous_accepted_count = YLeaf(YType.uint32, "timestamp-lower-than-previous-accepted-count")

                                self.timestamp_mismatch_count = YLeaf(YType.uint32, "timestamp-mismatch-count")

                                self.unknown_count = YLeaf(YType.uint32, "unknown-count")

                                self.unspecified_failure_count = YLeaf(YType.uint32, "unspecified-failure-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("accepted_count",
                                                "admin_failure_count",
                                                "authen_failure_count",
                                                "bad_sequence_failure_count",
                                                "gre_key_opt_required_count",
                                                "home_reg_failure_count",
                                                "home_subnet_failure_count",
                                                "missing_access_tech_type_opt_count",
                                                "missing_hi_opt_count",
                                                "missing_hnp_opt_count",
                                                "missing_mn_id_opt_count",
                                                "multiple_ipv4_ho_a_not_supported_count",
                                                "no_author_for_hnp_count",
                                                "no_author_for_ipv4_hoa_count",
                                                "no_author_for_ipv4_mobility_count",
                                                "no_author_for_ipv6_mobility_count",
                                                "no_author_for_proxy_reg_count",
                                                "not_lma_for_this_mn_count",
                                                "pba_count",
                                                "pba_drop_count",
                                                "proxy_reg_not_enabled_count",
                                                "received_hnps_do_not_match_bce_hnps_count",
                                                "reg_type_failure_count",
                                                "resource_failure_count",
                                                "timestamp_lower_than_previous_accepted_count",
                                                "timestamp_mismatch_count",
                                                "unknown_count",
                                                "unspecified_failure_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbaSendStatistics, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbaSendStatistics, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.accepted_count.is_set or
                                    self.admin_failure_count.is_set or
                                    self.authen_failure_count.is_set or
                                    self.bad_sequence_failure_count.is_set or
                                    self.gre_key_opt_required_count.is_set or
                                    self.home_reg_failure_count.is_set or
                                    self.home_subnet_failure_count.is_set or
                                    self.missing_access_tech_type_opt_count.is_set or
                                    self.missing_hi_opt_count.is_set or
                                    self.missing_hnp_opt_count.is_set or
                                    self.missing_mn_id_opt_count.is_set or
                                    self.multiple_ipv4_ho_a_not_supported_count.is_set or
                                    self.no_author_for_hnp_count.is_set or
                                    self.no_author_for_ipv4_hoa_count.is_set or
                                    self.no_author_for_ipv4_mobility_count.is_set or
                                    self.no_author_for_ipv6_mobility_count.is_set or
                                    self.no_author_for_proxy_reg_count.is_set or
                                    self.not_lma_for_this_mn_count.is_set or
                                    self.pba_count.is_set or
                                    self.pba_drop_count.is_set or
                                    self.proxy_reg_not_enabled_count.is_set or
                                    self.received_hnps_do_not_match_bce_hnps_count.is_set or
                                    self.reg_type_failure_count.is_set or
                                    self.resource_failure_count.is_set or
                                    self.timestamp_lower_than_previous_accepted_count.is_set or
                                    self.timestamp_mismatch_count.is_set or
                                    self.unknown_count.is_set or
                                    self.unspecified_failure_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.accepted_count.yfilter != YFilter.not_set or
                                    self.admin_failure_count.yfilter != YFilter.not_set or
                                    self.authen_failure_count.yfilter != YFilter.not_set or
                                    self.bad_sequence_failure_count.yfilter != YFilter.not_set or
                                    self.gre_key_opt_required_count.yfilter != YFilter.not_set or
                                    self.home_reg_failure_count.yfilter != YFilter.not_set or
                                    self.home_subnet_failure_count.yfilter != YFilter.not_set or
                                    self.missing_access_tech_type_opt_count.yfilter != YFilter.not_set or
                                    self.missing_hi_opt_count.yfilter != YFilter.not_set or
                                    self.missing_hnp_opt_count.yfilter != YFilter.not_set or
                                    self.missing_mn_id_opt_count.yfilter != YFilter.not_set or
                                    self.multiple_ipv4_ho_a_not_supported_count.yfilter != YFilter.not_set or
                                    self.no_author_for_hnp_count.yfilter != YFilter.not_set or
                                    self.no_author_for_ipv4_hoa_count.yfilter != YFilter.not_set or
                                    self.no_author_for_ipv4_mobility_count.yfilter != YFilter.not_set or
                                    self.no_author_for_ipv6_mobility_count.yfilter != YFilter.not_set or
                                    self.no_author_for_proxy_reg_count.yfilter != YFilter.not_set or
                                    self.not_lma_for_this_mn_count.yfilter != YFilter.not_set or
                                    self.pba_count.yfilter != YFilter.not_set or
                                    self.pba_drop_count.yfilter != YFilter.not_set or
                                    self.proxy_reg_not_enabled_count.yfilter != YFilter.not_set or
                                    self.received_hnps_do_not_match_bce_hnps_count.yfilter != YFilter.not_set or
                                    self.reg_type_failure_count.yfilter != YFilter.not_set or
                                    self.resource_failure_count.yfilter != YFilter.not_set or
                                    self.timestamp_lower_than_previous_accepted_count.yfilter != YFilter.not_set or
                                    self.timestamp_mismatch_count.yfilter != YFilter.not_set or
                                    self.unknown_count.yfilter != YFilter.not_set or
                                    self.unspecified_failure_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pba-send-statistics" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.accepted_count.is_set or self.accepted_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.accepted_count.get_name_leafdata())
                                if (self.admin_failure_count.is_set or self.admin_failure_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.admin_failure_count.get_name_leafdata())
                                if (self.authen_failure_count.is_set or self.authen_failure_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.authen_failure_count.get_name_leafdata())
                                if (self.bad_sequence_failure_count.is_set or self.bad_sequence_failure_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bad_sequence_failure_count.get_name_leafdata())
                                if (self.gre_key_opt_required_count.is_set or self.gre_key_opt_required_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.gre_key_opt_required_count.get_name_leafdata())
                                if (self.home_reg_failure_count.is_set or self.home_reg_failure_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.home_reg_failure_count.get_name_leafdata())
                                if (self.home_subnet_failure_count.is_set or self.home_subnet_failure_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.home_subnet_failure_count.get_name_leafdata())
                                if (self.missing_access_tech_type_opt_count.is_set or self.missing_access_tech_type_opt_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.missing_access_tech_type_opt_count.get_name_leafdata())
                                if (self.missing_hi_opt_count.is_set or self.missing_hi_opt_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.missing_hi_opt_count.get_name_leafdata())
                                if (self.missing_hnp_opt_count.is_set or self.missing_hnp_opt_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.missing_hnp_opt_count.get_name_leafdata())
                                if (self.missing_mn_id_opt_count.is_set or self.missing_mn_id_opt_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.missing_mn_id_opt_count.get_name_leafdata())
                                if (self.multiple_ipv4_ho_a_not_supported_count.is_set or self.multiple_ipv4_ho_a_not_supported_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.multiple_ipv4_ho_a_not_supported_count.get_name_leafdata())
                                if (self.no_author_for_hnp_count.is_set or self.no_author_for_hnp_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_author_for_hnp_count.get_name_leafdata())
                                if (self.no_author_for_ipv4_hoa_count.is_set or self.no_author_for_ipv4_hoa_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_author_for_ipv4_hoa_count.get_name_leafdata())
                                if (self.no_author_for_ipv4_mobility_count.is_set or self.no_author_for_ipv4_mobility_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_author_for_ipv4_mobility_count.get_name_leafdata())
                                if (self.no_author_for_ipv6_mobility_count.is_set or self.no_author_for_ipv6_mobility_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_author_for_ipv6_mobility_count.get_name_leafdata())
                                if (self.no_author_for_proxy_reg_count.is_set or self.no_author_for_proxy_reg_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_author_for_proxy_reg_count.get_name_leafdata())
                                if (self.not_lma_for_this_mn_count.is_set or self.not_lma_for_this_mn_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.not_lma_for_this_mn_count.get_name_leafdata())
                                if (self.pba_count.is_set or self.pba_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pba_count.get_name_leafdata())
                                if (self.pba_drop_count.is_set or self.pba_drop_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pba_drop_count.get_name_leafdata())
                                if (self.proxy_reg_not_enabled_count.is_set or self.proxy_reg_not_enabled_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.proxy_reg_not_enabled_count.get_name_leafdata())
                                if (self.received_hnps_do_not_match_bce_hnps_count.is_set or self.received_hnps_do_not_match_bce_hnps_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.received_hnps_do_not_match_bce_hnps_count.get_name_leafdata())
                                if (self.reg_type_failure_count.is_set or self.reg_type_failure_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.reg_type_failure_count.get_name_leafdata())
                                if (self.resource_failure_count.is_set or self.resource_failure_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.resource_failure_count.get_name_leafdata())
                                if (self.timestamp_lower_than_previous_accepted_count.is_set or self.timestamp_lower_than_previous_accepted_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.timestamp_lower_than_previous_accepted_count.get_name_leafdata())
                                if (self.timestamp_mismatch_count.is_set or self.timestamp_mismatch_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.timestamp_mismatch_count.get_name_leafdata())
                                if (self.unknown_count.is_set or self.unknown_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unknown_count.get_name_leafdata())
                                if (self.unspecified_failure_count.is_set or self.unspecified_failure_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unspecified_failure_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "accepted-count" or name == "admin-failure-count" or name == "authen-failure-count" or name == "bad-sequence-failure-count" or name == "gre-key-opt-required-count" or name == "home-reg-failure-count" or name == "home-subnet-failure-count" or name == "missing-access-tech-type-opt-count" or name == "missing-hi-opt-count" or name == "missing-hnp-opt-count" or name == "missing-mn-id-opt-count" or name == "multiple-ipv4-ho-a-not-supported-count" or name == "no-author-for-hnp-count" or name == "no-author-for-ipv4-hoa-count" or name == "no-author-for-ipv4-mobility-count" or name == "no-author-for-ipv6-mobility-count" or name == "no-author-for-proxy-reg-count" or name == "not-lma-for-this-mn-count" or name == "pba-count" or name == "pba-drop-count" or name == "proxy-reg-not-enabled-count" or name == "received-hnps-do-not-match-bce-hnps-count" or name == "reg-type-failure-count" or name == "resource-failure-count" or name == "timestamp-lower-than-previous-accepted-count" or name == "timestamp-mismatch-count" or name == "unknown-count" or name == "unspecified-failure-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "accepted-count"):
                                    self.accepted_count = value
                                    self.accepted_count.value_namespace = name_space
                                    self.accepted_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "admin-failure-count"):
                                    self.admin_failure_count = value
                                    self.admin_failure_count.value_namespace = name_space
                                    self.admin_failure_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "authen-failure-count"):
                                    self.authen_failure_count = value
                                    self.authen_failure_count.value_namespace = name_space
                                    self.authen_failure_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "bad-sequence-failure-count"):
                                    self.bad_sequence_failure_count = value
                                    self.bad_sequence_failure_count.value_namespace = name_space
                                    self.bad_sequence_failure_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "gre-key-opt-required-count"):
                                    self.gre_key_opt_required_count = value
                                    self.gre_key_opt_required_count.value_namespace = name_space
                                    self.gre_key_opt_required_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "home-reg-failure-count"):
                                    self.home_reg_failure_count = value
                                    self.home_reg_failure_count.value_namespace = name_space
                                    self.home_reg_failure_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "home-subnet-failure-count"):
                                    self.home_subnet_failure_count = value
                                    self.home_subnet_failure_count.value_namespace = name_space
                                    self.home_subnet_failure_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "missing-access-tech-type-opt-count"):
                                    self.missing_access_tech_type_opt_count = value
                                    self.missing_access_tech_type_opt_count.value_namespace = name_space
                                    self.missing_access_tech_type_opt_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "missing-hi-opt-count"):
                                    self.missing_hi_opt_count = value
                                    self.missing_hi_opt_count.value_namespace = name_space
                                    self.missing_hi_opt_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "missing-hnp-opt-count"):
                                    self.missing_hnp_opt_count = value
                                    self.missing_hnp_opt_count.value_namespace = name_space
                                    self.missing_hnp_opt_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "missing-mn-id-opt-count"):
                                    self.missing_mn_id_opt_count = value
                                    self.missing_mn_id_opt_count.value_namespace = name_space
                                    self.missing_mn_id_opt_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "multiple-ipv4-ho-a-not-supported-count"):
                                    self.multiple_ipv4_ho_a_not_supported_count = value
                                    self.multiple_ipv4_ho_a_not_supported_count.value_namespace = name_space
                                    self.multiple_ipv4_ho_a_not_supported_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-author-for-hnp-count"):
                                    self.no_author_for_hnp_count = value
                                    self.no_author_for_hnp_count.value_namespace = name_space
                                    self.no_author_for_hnp_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-author-for-ipv4-hoa-count"):
                                    self.no_author_for_ipv4_hoa_count = value
                                    self.no_author_for_ipv4_hoa_count.value_namespace = name_space
                                    self.no_author_for_ipv4_hoa_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-author-for-ipv4-mobility-count"):
                                    self.no_author_for_ipv4_mobility_count = value
                                    self.no_author_for_ipv4_mobility_count.value_namespace = name_space
                                    self.no_author_for_ipv4_mobility_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-author-for-ipv6-mobility-count"):
                                    self.no_author_for_ipv6_mobility_count = value
                                    self.no_author_for_ipv6_mobility_count.value_namespace = name_space
                                    self.no_author_for_ipv6_mobility_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-author-for-proxy-reg-count"):
                                    self.no_author_for_proxy_reg_count = value
                                    self.no_author_for_proxy_reg_count.value_namespace = name_space
                                    self.no_author_for_proxy_reg_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "not-lma-for-this-mn-count"):
                                    self.not_lma_for_this_mn_count = value
                                    self.not_lma_for_this_mn_count.value_namespace = name_space
                                    self.not_lma_for_this_mn_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pba-count"):
                                    self.pba_count = value
                                    self.pba_count.value_namespace = name_space
                                    self.pba_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pba-drop-count"):
                                    self.pba_drop_count = value
                                    self.pba_drop_count.value_namespace = name_space
                                    self.pba_drop_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "proxy-reg-not-enabled-count"):
                                    self.proxy_reg_not_enabled_count = value
                                    self.proxy_reg_not_enabled_count.value_namespace = name_space
                                    self.proxy_reg_not_enabled_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "received-hnps-do-not-match-bce-hnps-count"):
                                    self.received_hnps_do_not_match_bce_hnps_count = value
                                    self.received_hnps_do_not_match_bce_hnps_count.value_namespace = name_space
                                    self.received_hnps_do_not_match_bce_hnps_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "reg-type-failure-count"):
                                    self.reg_type_failure_count = value
                                    self.reg_type_failure_count.value_namespace = name_space
                                    self.reg_type_failure_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "resource-failure-count"):
                                    self.resource_failure_count = value
                                    self.resource_failure_count.value_namespace = name_space
                                    self.resource_failure_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "timestamp-lower-than-previous-accepted-count"):
                                    self.timestamp_lower_than_previous_accepted_count = value
                                    self.timestamp_lower_than_previous_accepted_count.value_namespace = name_space
                                    self.timestamp_lower_than_previous_accepted_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "timestamp-mismatch-count"):
                                    self.timestamp_mismatch_count = value
                                    self.timestamp_mismatch_count.value_namespace = name_space
                                    self.timestamp_mismatch_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "unknown-count"):
                                    self.unknown_count = value
                                    self.unknown_count.value_namespace = name_space
                                    self.unknown_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "unspecified-failure-count"):
                                    self.unspecified_failure_count = value
                                    self.unspecified_failure_count.value_namespace = name_space
                                    self.unspecified_failure_count.value_namespace_prefix = name_space_prefix


                        class PbriSendStatistics(Entity):
                            """
                            PBRI Send Statistics
                            
                            .. attribute:: admin_reason_count
                            
                            	Count of Revoc Trigger \- Administrative Reason
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_different_att_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Different ATT
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_same_att_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Same ATT
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_unknown_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Unknown
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: network_session_termination_count
                            
                            	Count of Revoc Trigger \- Access Network Session Termination
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_of_sync_bce_state_count
                            
                            	Count of Revoc Trigger \- Possible Out\-of\-Sync BCE State
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pbri_count
                            
                            	Count of PBRIs
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbri_drop_count
                            
                            	Count of PBRIs dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: per_peer_policy_count
                            
                            	Count of Revoc Trigger \- Per\-Peer Policy
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: revoking_mn_local_policy_count
                            
                            	Count of Revoc Trigger \- Revoking Mobility Node Local Policy
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unspecified_count
                            
                            	Count of Revoc Trigger \- Unspecified
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: user_session_termination_count
                            
                            	Count of Revoc Trigger \- User Init Session Terminatation
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriSendStatistics, self).__init__()

                                self.yang_name = "pbri-send-statistics"
                                self.yang_parent_name = "protocol-statistics"

                                self.admin_reason_count = YLeaf(YType.uint32, "admin-reason-count")

                                self.mag_handover_different_att_count = YLeaf(YType.uint32, "mag-handover-different-att-count")

                                self.mag_handover_same_att_count = YLeaf(YType.uint32, "mag-handover-same-att-count")

                                self.mag_handover_unknown_count = YLeaf(YType.uint32, "mag-handover-unknown-count")

                                self.network_session_termination_count = YLeaf(YType.uint32, "network-session-termination-count")

                                self.out_of_sync_bce_state_count = YLeaf(YType.uint32, "out-of-sync-bce-state-count")

                                self.pbri_count = YLeaf(YType.uint64, "pbri-count")

                                self.pbri_drop_count = YLeaf(YType.uint32, "pbri-drop-count")

                                self.per_peer_policy_count = YLeaf(YType.uint32, "per-peer-policy-count")

                                self.revoking_mn_local_policy_count = YLeaf(YType.uint32, "revoking-mn-local-policy-count")

                                self.unspecified_count = YLeaf(YType.uint32, "unspecified-count")

                                self.user_session_termination_count = YLeaf(YType.uint32, "user-session-termination-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("admin_reason_count",
                                                "mag_handover_different_att_count",
                                                "mag_handover_same_att_count",
                                                "mag_handover_unknown_count",
                                                "network_session_termination_count",
                                                "out_of_sync_bce_state_count",
                                                "pbri_count",
                                                "pbri_drop_count",
                                                "per_peer_policy_count",
                                                "revoking_mn_local_policy_count",
                                                "unspecified_count",
                                                "user_session_termination_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriSendStatistics, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriSendStatistics, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.admin_reason_count.is_set or
                                    self.mag_handover_different_att_count.is_set or
                                    self.mag_handover_same_att_count.is_set or
                                    self.mag_handover_unknown_count.is_set or
                                    self.network_session_termination_count.is_set or
                                    self.out_of_sync_bce_state_count.is_set or
                                    self.pbri_count.is_set or
                                    self.pbri_drop_count.is_set or
                                    self.per_peer_policy_count.is_set or
                                    self.revoking_mn_local_policy_count.is_set or
                                    self.unspecified_count.is_set or
                                    self.user_session_termination_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.admin_reason_count.yfilter != YFilter.not_set or
                                    self.mag_handover_different_att_count.yfilter != YFilter.not_set or
                                    self.mag_handover_same_att_count.yfilter != YFilter.not_set or
                                    self.mag_handover_unknown_count.yfilter != YFilter.not_set or
                                    self.network_session_termination_count.yfilter != YFilter.not_set or
                                    self.out_of_sync_bce_state_count.yfilter != YFilter.not_set or
                                    self.pbri_count.yfilter != YFilter.not_set or
                                    self.pbri_drop_count.yfilter != YFilter.not_set or
                                    self.per_peer_policy_count.yfilter != YFilter.not_set or
                                    self.revoking_mn_local_policy_count.yfilter != YFilter.not_set or
                                    self.unspecified_count.yfilter != YFilter.not_set or
                                    self.user_session_termination_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pbri-send-statistics" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.admin_reason_count.is_set or self.admin_reason_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.admin_reason_count.get_name_leafdata())
                                if (self.mag_handover_different_att_count.is_set or self.mag_handover_different_att_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mag_handover_different_att_count.get_name_leafdata())
                                if (self.mag_handover_same_att_count.is_set or self.mag_handover_same_att_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mag_handover_same_att_count.get_name_leafdata())
                                if (self.mag_handover_unknown_count.is_set or self.mag_handover_unknown_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mag_handover_unknown_count.get_name_leafdata())
                                if (self.network_session_termination_count.is_set or self.network_session_termination_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.network_session_termination_count.get_name_leafdata())
                                if (self.out_of_sync_bce_state_count.is_set or self.out_of_sync_bce_state_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_of_sync_bce_state_count.get_name_leafdata())
                                if (self.pbri_count.is_set or self.pbri_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbri_count.get_name_leafdata())
                                if (self.pbri_drop_count.is_set or self.pbri_drop_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbri_drop_count.get_name_leafdata())
                                if (self.per_peer_policy_count.is_set or self.per_peer_policy_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.per_peer_policy_count.get_name_leafdata())
                                if (self.revoking_mn_local_policy_count.is_set or self.revoking_mn_local_policy_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.revoking_mn_local_policy_count.get_name_leafdata())
                                if (self.unspecified_count.is_set or self.unspecified_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unspecified_count.get_name_leafdata())
                                if (self.user_session_termination_count.is_set or self.user_session_termination_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.user_session_termination_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "admin-reason-count" or name == "mag-handover-different-att-count" or name == "mag-handover-same-att-count" or name == "mag-handover-unknown-count" or name == "network-session-termination-count" or name == "out-of-sync-bce-state-count" or name == "pbri-count" or name == "pbri-drop-count" or name == "per-peer-policy-count" or name == "revoking-mn-local-policy-count" or name == "unspecified-count" or name == "user-session-termination-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "admin-reason-count"):
                                    self.admin_reason_count = value
                                    self.admin_reason_count.value_namespace = name_space
                                    self.admin_reason_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mag-handover-different-att-count"):
                                    self.mag_handover_different_att_count = value
                                    self.mag_handover_different_att_count.value_namespace = name_space
                                    self.mag_handover_different_att_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mag-handover-same-att-count"):
                                    self.mag_handover_same_att_count = value
                                    self.mag_handover_same_att_count.value_namespace = name_space
                                    self.mag_handover_same_att_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mag-handover-unknown-count"):
                                    self.mag_handover_unknown_count = value
                                    self.mag_handover_unknown_count.value_namespace = name_space
                                    self.mag_handover_unknown_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "network-session-termination-count"):
                                    self.network_session_termination_count = value
                                    self.network_session_termination_count.value_namespace = name_space
                                    self.network_session_termination_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-of-sync-bce-state-count"):
                                    self.out_of_sync_bce_state_count = value
                                    self.out_of_sync_bce_state_count.value_namespace = name_space
                                    self.out_of_sync_bce_state_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbri-count"):
                                    self.pbri_count = value
                                    self.pbri_count.value_namespace = name_space
                                    self.pbri_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbri-drop-count"):
                                    self.pbri_drop_count = value
                                    self.pbri_drop_count.value_namespace = name_space
                                    self.pbri_drop_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "per-peer-policy-count"):
                                    self.per_peer_policy_count = value
                                    self.per_peer_policy_count.value_namespace = name_space
                                    self.per_peer_policy_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "revoking-mn-local-policy-count"):
                                    self.revoking_mn_local_policy_count = value
                                    self.revoking_mn_local_policy_count.value_namespace = name_space
                                    self.revoking_mn_local_policy_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "unspecified-count"):
                                    self.unspecified_count = value
                                    self.unspecified_count.value_namespace = name_space
                                    self.unspecified_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "user-session-termination-count"):
                                    self.user_session_termination_count = value
                                    self.user_session_termination_count.value_namespace = name_space
                                    self.user_session_termination_count.value_namespace_prefix = name_space_prefix


                        class PbriReceiveStatistics(Entity):
                            """
                            PBRI Receive Statistics
                            
                            .. attribute:: admin_reason_count
                            
                            	Count of Revoc Trigger \- Administrative Reason
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_different_att_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Different ATT
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_same_att_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Same ATT
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_unknown_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Unknown
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: network_session_termination_count
                            
                            	Count of Revoc Trigger \- Access Network Session Termination
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_of_sync_bce_state_count
                            
                            	Count of Revoc Trigger \- Possible Out\-of\-Sync BCE State
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pbri_count
                            
                            	Count of PBRIs
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbri_drop_count
                            
                            	Count of PBRIs dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: per_peer_policy_count
                            
                            	Count of Revoc Trigger \- Per\-Peer Policy
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: revoking_mn_local_policy_count
                            
                            	Count of Revoc Trigger \- Revoking Mobility Node Local Policy
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unspecified_count
                            
                            	Count of Revoc Trigger \- Unspecified
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: user_session_termination_count
                            
                            	Count of Revoc Trigger \- User Init Session Terminatation
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriReceiveStatistics, self).__init__()

                                self.yang_name = "pbri-receive-statistics"
                                self.yang_parent_name = "protocol-statistics"

                                self.admin_reason_count = YLeaf(YType.uint32, "admin-reason-count")

                                self.mag_handover_different_att_count = YLeaf(YType.uint32, "mag-handover-different-att-count")

                                self.mag_handover_same_att_count = YLeaf(YType.uint32, "mag-handover-same-att-count")

                                self.mag_handover_unknown_count = YLeaf(YType.uint32, "mag-handover-unknown-count")

                                self.network_session_termination_count = YLeaf(YType.uint32, "network-session-termination-count")

                                self.out_of_sync_bce_state_count = YLeaf(YType.uint32, "out-of-sync-bce-state-count")

                                self.pbri_count = YLeaf(YType.uint64, "pbri-count")

                                self.pbri_drop_count = YLeaf(YType.uint32, "pbri-drop-count")

                                self.per_peer_policy_count = YLeaf(YType.uint32, "per-peer-policy-count")

                                self.revoking_mn_local_policy_count = YLeaf(YType.uint32, "revoking-mn-local-policy-count")

                                self.unspecified_count = YLeaf(YType.uint32, "unspecified-count")

                                self.user_session_termination_count = YLeaf(YType.uint32, "user-session-termination-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("admin_reason_count",
                                                "mag_handover_different_att_count",
                                                "mag_handover_same_att_count",
                                                "mag_handover_unknown_count",
                                                "network_session_termination_count",
                                                "out_of_sync_bce_state_count",
                                                "pbri_count",
                                                "pbri_drop_count",
                                                "per_peer_policy_count",
                                                "revoking_mn_local_policy_count",
                                                "unspecified_count",
                                                "user_session_termination_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriReceiveStatistics, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriReceiveStatistics, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.admin_reason_count.is_set or
                                    self.mag_handover_different_att_count.is_set or
                                    self.mag_handover_same_att_count.is_set or
                                    self.mag_handover_unknown_count.is_set or
                                    self.network_session_termination_count.is_set or
                                    self.out_of_sync_bce_state_count.is_set or
                                    self.pbri_count.is_set or
                                    self.pbri_drop_count.is_set or
                                    self.per_peer_policy_count.is_set or
                                    self.revoking_mn_local_policy_count.is_set or
                                    self.unspecified_count.is_set or
                                    self.user_session_termination_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.admin_reason_count.yfilter != YFilter.not_set or
                                    self.mag_handover_different_att_count.yfilter != YFilter.not_set or
                                    self.mag_handover_same_att_count.yfilter != YFilter.not_set or
                                    self.mag_handover_unknown_count.yfilter != YFilter.not_set or
                                    self.network_session_termination_count.yfilter != YFilter.not_set or
                                    self.out_of_sync_bce_state_count.yfilter != YFilter.not_set or
                                    self.pbri_count.yfilter != YFilter.not_set or
                                    self.pbri_drop_count.yfilter != YFilter.not_set or
                                    self.per_peer_policy_count.yfilter != YFilter.not_set or
                                    self.revoking_mn_local_policy_count.yfilter != YFilter.not_set or
                                    self.unspecified_count.yfilter != YFilter.not_set or
                                    self.user_session_termination_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pbri-receive-statistics" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.admin_reason_count.is_set or self.admin_reason_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.admin_reason_count.get_name_leafdata())
                                if (self.mag_handover_different_att_count.is_set or self.mag_handover_different_att_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mag_handover_different_att_count.get_name_leafdata())
                                if (self.mag_handover_same_att_count.is_set or self.mag_handover_same_att_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mag_handover_same_att_count.get_name_leafdata())
                                if (self.mag_handover_unknown_count.is_set or self.mag_handover_unknown_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mag_handover_unknown_count.get_name_leafdata())
                                if (self.network_session_termination_count.is_set or self.network_session_termination_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.network_session_termination_count.get_name_leafdata())
                                if (self.out_of_sync_bce_state_count.is_set or self.out_of_sync_bce_state_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_of_sync_bce_state_count.get_name_leafdata())
                                if (self.pbri_count.is_set or self.pbri_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbri_count.get_name_leafdata())
                                if (self.pbri_drop_count.is_set or self.pbri_drop_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbri_drop_count.get_name_leafdata())
                                if (self.per_peer_policy_count.is_set or self.per_peer_policy_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.per_peer_policy_count.get_name_leafdata())
                                if (self.revoking_mn_local_policy_count.is_set or self.revoking_mn_local_policy_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.revoking_mn_local_policy_count.get_name_leafdata())
                                if (self.unspecified_count.is_set or self.unspecified_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unspecified_count.get_name_leafdata())
                                if (self.user_session_termination_count.is_set or self.user_session_termination_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.user_session_termination_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "admin-reason-count" or name == "mag-handover-different-att-count" or name == "mag-handover-same-att-count" or name == "mag-handover-unknown-count" or name == "network-session-termination-count" or name == "out-of-sync-bce-state-count" or name == "pbri-count" or name == "pbri-drop-count" or name == "per-peer-policy-count" or name == "revoking-mn-local-policy-count" or name == "unspecified-count" or name == "user-session-termination-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "admin-reason-count"):
                                    self.admin_reason_count = value
                                    self.admin_reason_count.value_namespace = name_space
                                    self.admin_reason_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mag-handover-different-att-count"):
                                    self.mag_handover_different_att_count = value
                                    self.mag_handover_different_att_count.value_namespace = name_space
                                    self.mag_handover_different_att_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mag-handover-same-att-count"):
                                    self.mag_handover_same_att_count = value
                                    self.mag_handover_same_att_count.value_namespace = name_space
                                    self.mag_handover_same_att_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mag-handover-unknown-count"):
                                    self.mag_handover_unknown_count = value
                                    self.mag_handover_unknown_count.value_namespace = name_space
                                    self.mag_handover_unknown_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "network-session-termination-count"):
                                    self.network_session_termination_count = value
                                    self.network_session_termination_count.value_namespace = name_space
                                    self.network_session_termination_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-of-sync-bce-state-count"):
                                    self.out_of_sync_bce_state_count = value
                                    self.out_of_sync_bce_state_count.value_namespace = name_space
                                    self.out_of_sync_bce_state_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbri-count"):
                                    self.pbri_count = value
                                    self.pbri_count.value_namespace = name_space
                                    self.pbri_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbri-drop-count"):
                                    self.pbri_drop_count = value
                                    self.pbri_drop_count.value_namespace = name_space
                                    self.pbri_drop_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "per-peer-policy-count"):
                                    self.per_peer_policy_count = value
                                    self.per_peer_policy_count.value_namespace = name_space
                                    self.per_peer_policy_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "revoking-mn-local-policy-count"):
                                    self.revoking_mn_local_policy_count = value
                                    self.revoking_mn_local_policy_count.value_namespace = name_space
                                    self.revoking_mn_local_policy_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "unspecified-count"):
                                    self.unspecified_count = value
                                    self.unspecified_count.value_namespace = name_space
                                    self.unspecified_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "user-session-termination-count"):
                                    self.user_session_termination_count = value
                                    self.user_session_termination_count.value_namespace = name_space
                                    self.user_session_termination_count.value_namespace_prefix = name_space_prefix


                        class PbraSendStatistics(Entity):
                            """
                            PBRA Send Statistics
                            
                            .. attribute:: hoa_required_count
                            
                            	Count of Revoc Status \- IPv4 Home Address Option Required
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mn_attached_count
                            
                            	Count of Revoc Status \- Revocation Failed \- MN is Attached
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mn_identity_required_count
                            
                            	Count of Revoc Status \- Revoked Mobile Node Identity Required
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_global_revoc_count
                            
                            	Count of Revoc Status \- Global Revocation NOT Authorized
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_binding_count
                            
                            	Count of Revoc Status \- Binding Does Not Exist
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: partial_success_count
                            
                            	Count of Revoc Status \- Partial Success
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pbr_not_supported_count
                            
                            	Count of Revoc Status \- Proxy Binding Revocation NOT Supported
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pbra_count
                            
                            	Count of PBRAs
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbra_drop_count
                            
                            	Count of PBRAs dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: revoc_function_not_supported_count
                            
                            	Count of Revoc Status \- Revocation Function NOT Supported
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: success_count
                            
                            	Count of Revoc Status \- Success
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_revoc_trigger_count
                            
                            	Count of Revoc Status \- Revocation Trigger NOT supported
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraSendStatistics, self).__init__()

                                self.yang_name = "pbra-send-statistics"
                                self.yang_parent_name = "protocol-statistics"

                                self.hoa_required_count = YLeaf(YType.uint32, "hoa-required-count")

                                self.mn_attached_count = YLeaf(YType.uint32, "mn-attached-count")

                                self.mn_identity_required_count = YLeaf(YType.uint32, "mn-identity-required-count")

                                self.no_author_for_global_revoc_count = YLeaf(YType.uint32, "no-author-for-global-revoc-count")

                                self.no_binding_count = YLeaf(YType.uint32, "no-binding-count")

                                self.partial_success_count = YLeaf(YType.uint32, "partial-success-count")

                                self.pbr_not_supported_count = YLeaf(YType.uint32, "pbr-not-supported-count")

                                self.pbra_count = YLeaf(YType.uint64, "pbra-count")

                                self.pbra_drop_count = YLeaf(YType.uint32, "pbra-drop-count")

                                self.revoc_function_not_supported_count = YLeaf(YType.uint32, "revoc-function-not-supported-count")

                                self.success_count = YLeaf(YType.uint32, "success-count")

                                self.unknown_revoc_trigger_count = YLeaf(YType.uint32, "unknown-revoc-trigger-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("hoa_required_count",
                                                "mn_attached_count",
                                                "mn_identity_required_count",
                                                "no_author_for_global_revoc_count",
                                                "no_binding_count",
                                                "partial_success_count",
                                                "pbr_not_supported_count",
                                                "pbra_count",
                                                "pbra_drop_count",
                                                "revoc_function_not_supported_count",
                                                "success_count",
                                                "unknown_revoc_trigger_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraSendStatistics, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraSendStatistics, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.hoa_required_count.is_set or
                                    self.mn_attached_count.is_set or
                                    self.mn_identity_required_count.is_set or
                                    self.no_author_for_global_revoc_count.is_set or
                                    self.no_binding_count.is_set or
                                    self.partial_success_count.is_set or
                                    self.pbr_not_supported_count.is_set or
                                    self.pbra_count.is_set or
                                    self.pbra_drop_count.is_set or
                                    self.revoc_function_not_supported_count.is_set or
                                    self.success_count.is_set or
                                    self.unknown_revoc_trigger_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.hoa_required_count.yfilter != YFilter.not_set or
                                    self.mn_attached_count.yfilter != YFilter.not_set or
                                    self.mn_identity_required_count.yfilter != YFilter.not_set or
                                    self.no_author_for_global_revoc_count.yfilter != YFilter.not_set or
                                    self.no_binding_count.yfilter != YFilter.not_set or
                                    self.partial_success_count.yfilter != YFilter.not_set or
                                    self.pbr_not_supported_count.yfilter != YFilter.not_set or
                                    self.pbra_count.yfilter != YFilter.not_set or
                                    self.pbra_drop_count.yfilter != YFilter.not_set or
                                    self.revoc_function_not_supported_count.yfilter != YFilter.not_set or
                                    self.success_count.yfilter != YFilter.not_set or
                                    self.unknown_revoc_trigger_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pbra-send-statistics" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.hoa_required_count.is_set or self.hoa_required_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hoa_required_count.get_name_leafdata())
                                if (self.mn_attached_count.is_set or self.mn_attached_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mn_attached_count.get_name_leafdata())
                                if (self.mn_identity_required_count.is_set or self.mn_identity_required_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mn_identity_required_count.get_name_leafdata())
                                if (self.no_author_for_global_revoc_count.is_set or self.no_author_for_global_revoc_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_author_for_global_revoc_count.get_name_leafdata())
                                if (self.no_binding_count.is_set or self.no_binding_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_binding_count.get_name_leafdata())
                                if (self.partial_success_count.is_set or self.partial_success_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.partial_success_count.get_name_leafdata())
                                if (self.pbr_not_supported_count.is_set or self.pbr_not_supported_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbr_not_supported_count.get_name_leafdata())
                                if (self.pbra_count.is_set or self.pbra_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbra_count.get_name_leafdata())
                                if (self.pbra_drop_count.is_set or self.pbra_drop_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbra_drop_count.get_name_leafdata())
                                if (self.revoc_function_not_supported_count.is_set or self.revoc_function_not_supported_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.revoc_function_not_supported_count.get_name_leafdata())
                                if (self.success_count.is_set or self.success_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.success_count.get_name_leafdata())
                                if (self.unknown_revoc_trigger_count.is_set or self.unknown_revoc_trigger_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unknown_revoc_trigger_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "hoa-required-count" or name == "mn-attached-count" or name == "mn-identity-required-count" or name == "no-author-for-global-revoc-count" or name == "no-binding-count" or name == "partial-success-count" or name == "pbr-not-supported-count" or name == "pbra-count" or name == "pbra-drop-count" or name == "revoc-function-not-supported-count" or name == "success-count" or name == "unknown-revoc-trigger-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "hoa-required-count"):
                                    self.hoa_required_count = value
                                    self.hoa_required_count.value_namespace = name_space
                                    self.hoa_required_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mn-attached-count"):
                                    self.mn_attached_count = value
                                    self.mn_attached_count.value_namespace = name_space
                                    self.mn_attached_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mn-identity-required-count"):
                                    self.mn_identity_required_count = value
                                    self.mn_identity_required_count.value_namespace = name_space
                                    self.mn_identity_required_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-author-for-global-revoc-count"):
                                    self.no_author_for_global_revoc_count = value
                                    self.no_author_for_global_revoc_count.value_namespace = name_space
                                    self.no_author_for_global_revoc_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-binding-count"):
                                    self.no_binding_count = value
                                    self.no_binding_count.value_namespace = name_space
                                    self.no_binding_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "partial-success-count"):
                                    self.partial_success_count = value
                                    self.partial_success_count.value_namespace = name_space
                                    self.partial_success_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbr-not-supported-count"):
                                    self.pbr_not_supported_count = value
                                    self.pbr_not_supported_count.value_namespace = name_space
                                    self.pbr_not_supported_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbra-count"):
                                    self.pbra_count = value
                                    self.pbra_count.value_namespace = name_space
                                    self.pbra_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbra-drop-count"):
                                    self.pbra_drop_count = value
                                    self.pbra_drop_count.value_namespace = name_space
                                    self.pbra_drop_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "revoc-function-not-supported-count"):
                                    self.revoc_function_not_supported_count = value
                                    self.revoc_function_not_supported_count.value_namespace = name_space
                                    self.revoc_function_not_supported_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "success-count"):
                                    self.success_count = value
                                    self.success_count.value_namespace = name_space
                                    self.success_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "unknown-revoc-trigger-count"):
                                    self.unknown_revoc_trigger_count = value
                                    self.unknown_revoc_trigger_count.value_namespace = name_space
                                    self.unknown_revoc_trigger_count.value_namespace_prefix = name_space_prefix


                        class PbraReceiveStatistics(Entity):
                            """
                            PBRA Receive Statistics
                            
                            .. attribute:: hoa_required_count
                            
                            	Count of Revoc Status \- IPv4 Home Address Option Required
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mn_attached_count
                            
                            	Count of Revoc Status \- Revocation Failed \- MN is Attached
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mn_identity_required_count
                            
                            	Count of Revoc Status \- Revoked Mobile Node Identity Required
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_global_revoc_count
                            
                            	Count of Revoc Status \- Global Revocation NOT Authorized
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_binding_count
                            
                            	Count of Revoc Status \- Binding Does Not Exist
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: partial_success_count
                            
                            	Count of Revoc Status \- Partial Success
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pbr_not_supported_count
                            
                            	Count of Revoc Status \- Proxy Binding Revocation NOT Supported
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pbra_count
                            
                            	Count of PBRAs
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbra_drop_count
                            
                            	Count of PBRAs dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: revoc_function_not_supported_count
                            
                            	Count of Revoc Status \- Revocation Function NOT Supported
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: success_count
                            
                            	Count of Revoc Status \- Success
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_revoc_trigger_count
                            
                            	Count of Revoc Status \- Revocation Trigger NOT supported
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraReceiveStatistics, self).__init__()

                                self.yang_name = "pbra-receive-statistics"
                                self.yang_parent_name = "protocol-statistics"

                                self.hoa_required_count = YLeaf(YType.uint32, "hoa-required-count")

                                self.mn_attached_count = YLeaf(YType.uint32, "mn-attached-count")

                                self.mn_identity_required_count = YLeaf(YType.uint32, "mn-identity-required-count")

                                self.no_author_for_global_revoc_count = YLeaf(YType.uint32, "no-author-for-global-revoc-count")

                                self.no_binding_count = YLeaf(YType.uint32, "no-binding-count")

                                self.partial_success_count = YLeaf(YType.uint32, "partial-success-count")

                                self.pbr_not_supported_count = YLeaf(YType.uint32, "pbr-not-supported-count")

                                self.pbra_count = YLeaf(YType.uint64, "pbra-count")

                                self.pbra_drop_count = YLeaf(YType.uint32, "pbra-drop-count")

                                self.revoc_function_not_supported_count = YLeaf(YType.uint32, "revoc-function-not-supported-count")

                                self.success_count = YLeaf(YType.uint32, "success-count")

                                self.unknown_revoc_trigger_count = YLeaf(YType.uint32, "unknown-revoc-trigger-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("hoa_required_count",
                                                "mn_attached_count",
                                                "mn_identity_required_count",
                                                "no_author_for_global_revoc_count",
                                                "no_binding_count",
                                                "partial_success_count",
                                                "pbr_not_supported_count",
                                                "pbra_count",
                                                "pbra_drop_count",
                                                "revoc_function_not_supported_count",
                                                "success_count",
                                                "unknown_revoc_trigger_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraReceiveStatistics, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraReceiveStatistics, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.hoa_required_count.is_set or
                                    self.mn_attached_count.is_set or
                                    self.mn_identity_required_count.is_set or
                                    self.no_author_for_global_revoc_count.is_set or
                                    self.no_binding_count.is_set or
                                    self.partial_success_count.is_set or
                                    self.pbr_not_supported_count.is_set or
                                    self.pbra_count.is_set or
                                    self.pbra_drop_count.is_set or
                                    self.revoc_function_not_supported_count.is_set or
                                    self.success_count.is_set or
                                    self.unknown_revoc_trigger_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.hoa_required_count.yfilter != YFilter.not_set or
                                    self.mn_attached_count.yfilter != YFilter.not_set or
                                    self.mn_identity_required_count.yfilter != YFilter.not_set or
                                    self.no_author_for_global_revoc_count.yfilter != YFilter.not_set or
                                    self.no_binding_count.yfilter != YFilter.not_set or
                                    self.partial_success_count.yfilter != YFilter.not_set or
                                    self.pbr_not_supported_count.yfilter != YFilter.not_set or
                                    self.pbra_count.yfilter != YFilter.not_set or
                                    self.pbra_drop_count.yfilter != YFilter.not_set or
                                    self.revoc_function_not_supported_count.yfilter != YFilter.not_set or
                                    self.success_count.yfilter != YFilter.not_set or
                                    self.unknown_revoc_trigger_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pbra-receive-statistics" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.hoa_required_count.is_set or self.hoa_required_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hoa_required_count.get_name_leafdata())
                                if (self.mn_attached_count.is_set or self.mn_attached_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mn_attached_count.get_name_leafdata())
                                if (self.mn_identity_required_count.is_set or self.mn_identity_required_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mn_identity_required_count.get_name_leafdata())
                                if (self.no_author_for_global_revoc_count.is_set or self.no_author_for_global_revoc_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_author_for_global_revoc_count.get_name_leafdata())
                                if (self.no_binding_count.is_set or self.no_binding_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.no_binding_count.get_name_leafdata())
                                if (self.partial_success_count.is_set or self.partial_success_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.partial_success_count.get_name_leafdata())
                                if (self.pbr_not_supported_count.is_set or self.pbr_not_supported_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbr_not_supported_count.get_name_leafdata())
                                if (self.pbra_count.is_set or self.pbra_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbra_count.get_name_leafdata())
                                if (self.pbra_drop_count.is_set or self.pbra_drop_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pbra_drop_count.get_name_leafdata())
                                if (self.revoc_function_not_supported_count.is_set or self.revoc_function_not_supported_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.revoc_function_not_supported_count.get_name_leafdata())
                                if (self.success_count.is_set or self.success_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.success_count.get_name_leafdata())
                                if (self.unknown_revoc_trigger_count.is_set or self.unknown_revoc_trigger_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unknown_revoc_trigger_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "hoa-required-count" or name == "mn-attached-count" or name == "mn-identity-required-count" or name == "no-author-for-global-revoc-count" or name == "no-binding-count" or name == "partial-success-count" or name == "pbr-not-supported-count" or name == "pbra-count" or name == "pbra-drop-count" or name == "revoc-function-not-supported-count" or name == "success-count" or name == "unknown-revoc-trigger-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "hoa-required-count"):
                                    self.hoa_required_count = value
                                    self.hoa_required_count.value_namespace = name_space
                                    self.hoa_required_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mn-attached-count"):
                                    self.mn_attached_count = value
                                    self.mn_attached_count.value_namespace = name_space
                                    self.mn_attached_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "mn-identity-required-count"):
                                    self.mn_identity_required_count = value
                                    self.mn_identity_required_count.value_namespace = name_space
                                    self.mn_identity_required_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-author-for-global-revoc-count"):
                                    self.no_author_for_global_revoc_count = value
                                    self.no_author_for_global_revoc_count.value_namespace = name_space
                                    self.no_author_for_global_revoc_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "no-binding-count"):
                                    self.no_binding_count = value
                                    self.no_binding_count.value_namespace = name_space
                                    self.no_binding_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "partial-success-count"):
                                    self.partial_success_count = value
                                    self.partial_success_count.value_namespace = name_space
                                    self.partial_success_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbr-not-supported-count"):
                                    self.pbr_not_supported_count = value
                                    self.pbr_not_supported_count.value_namespace = name_space
                                    self.pbr_not_supported_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbra-count"):
                                    self.pbra_count = value
                                    self.pbra_count.value_namespace = name_space
                                    self.pbra_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "pbra-drop-count"):
                                    self.pbra_drop_count = value
                                    self.pbra_drop_count.value_namespace = name_space
                                    self.pbra_drop_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "revoc-function-not-supported-count"):
                                    self.revoc_function_not_supported_count = value
                                    self.revoc_function_not_supported_count.value_namespace = name_space
                                    self.revoc_function_not_supported_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "success-count"):
                                    self.success_count = value
                                    self.success_count.value_namespace = name_space
                                    self.success_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "unknown-revoc-trigger-count"):
                                    self.unknown_revoc_trigger_count = value
                                    self.unknown_revoc_trigger_count.value_namespace = name_space
                                    self.unknown_revoc_trigger_count.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.pba_send_statistics is not None and self.pba_send_statistics.has_data()) or
                                (self.pbra_receive_statistics is not None and self.pbra_receive_statistics.has_data()) or
                                (self.pbra_send_statistics is not None and self.pbra_send_statistics.has_data()) or
                                (self.pbri_receive_statistics is not None and self.pbri_receive_statistics.has_data()) or
                                (self.pbri_send_statistics is not None and self.pbri_send_statistics.has_data()) or
                                (self.pbu_receive_statistics is not None and self.pbu_receive_statistics.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.pba_send_statistics is not None and self.pba_send_statistics.has_operation()) or
                                (self.pbra_receive_statistics is not None and self.pbra_receive_statistics.has_operation()) or
                                (self.pbra_send_statistics is not None and self.pbra_send_statistics.has_operation()) or
                                (self.pbri_receive_statistics is not None and self.pbri_receive_statistics.has_operation()) or
                                (self.pbri_send_statistics is not None and self.pbri_send_statistics.has_operation()) or
                                (self.pbu_receive_statistics is not None and self.pbu_receive_statistics.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "protocol-statistics" + path_buffer

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

                            if (child_yang_name == "pba-send-statistics"):
                                if (self.pba_send_statistics is None):
                                    self.pba_send_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbaSendStatistics()
                                    self.pba_send_statistics.parent = self
                                    self._children_name_map["pba_send_statistics"] = "pba-send-statistics"
                                return self.pba_send_statistics

                            if (child_yang_name == "pbra-receive-statistics"):
                                if (self.pbra_receive_statistics is None):
                                    self.pbra_receive_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraReceiveStatistics()
                                    self.pbra_receive_statistics.parent = self
                                    self._children_name_map["pbra_receive_statistics"] = "pbra-receive-statistics"
                                return self.pbra_receive_statistics

                            if (child_yang_name == "pbra-send-statistics"):
                                if (self.pbra_send_statistics is None):
                                    self.pbra_send_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraSendStatistics()
                                    self.pbra_send_statistics.parent = self
                                    self._children_name_map["pbra_send_statistics"] = "pbra-send-statistics"
                                return self.pbra_send_statistics

                            if (child_yang_name == "pbri-receive-statistics"):
                                if (self.pbri_receive_statistics is None):
                                    self.pbri_receive_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriReceiveStatistics()
                                    self.pbri_receive_statistics.parent = self
                                    self._children_name_map["pbri_receive_statistics"] = "pbri-receive-statistics"
                                return self.pbri_receive_statistics

                            if (child_yang_name == "pbri-send-statistics"):
                                if (self.pbri_send_statistics is None):
                                    self.pbri_send_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriSendStatistics()
                                    self.pbri_send_statistics.parent = self
                                    self._children_name_map["pbri_send_statistics"] = "pbri-send-statistics"
                                return self.pbri_send_statistics

                            if (child_yang_name == "pbu-receive-statistics"):
                                if (self.pbu_receive_statistics is None):
                                    self.pbu_receive_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbuReceiveStatistics()
                                    self.pbu_receive_statistics.parent = self
                                    self._children_name_map["pbu_receive_statistics"] = "pbu-receive-statistics"
                                return self.pbu_receive_statistics

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "pba-send-statistics" or name == "pbra-receive-statistics" or name == "pbra-send-statistics" or name == "pbri-receive-statistics" or name == "pbri-send-statistics" or name == "pbu-receive-statistics"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.mag_name.is_set or
                            self.lma_identifier.is_set or
                            (self.protocol_statistics is not None and self.protocol_statistics.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.mag_name.yfilter != YFilter.not_set or
                            self.lma_identifier.yfilter != YFilter.not_set or
                            (self.protocol_statistics is not None and self.protocol_statistics.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "mag-statistic" + "[mag-name='" + self.mag_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/mag-statistics/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.mag_name.is_set or self.mag_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mag_name.get_name_leafdata())
                        if (self.lma_identifier.is_set or self.lma_identifier.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lma_identifier.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "protocol-statistics"):
                            if (self.protocol_statistics is None):
                                self.protocol_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics()
                                self.protocol_statistics.parent = self
                                self._children_name_map["protocol_statistics"] = "protocol-statistics"
                            return self.protocol_statistics

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "protocol-statistics" or name == "mag-name" or name == "lma-identifier"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "mag-name"):
                            self.mag_name = value
                            self.mag_name.value_namespace = name_space
                            self.mag_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "lma-identifier"):
                            self.lma_identifier = value
                            self.lma_identifier.value_namespace = name_space
                            self.lma_identifier.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.mag_statistic:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.mag_statistic:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "mag-statistics" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "mag-statistic"):
                        for c in self.mag_statistic:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.mag_statistic.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mag-statistic"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.customer_statistics is not None and self.customer_statistics.has_data()) or
                    (self.global_ is not None and self.global_.has_data()) or
                    (self.mag_statistics is not None and self.mag_statistics.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.customer_statistics is not None and self.customer_statistics.has_operation()) or
                    (self.global_ is not None and self.global_.has_operation()) or
                    (self.mag_statistics is not None and self.mag_statistics.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "statistics" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "customer-statistics"):
                    if (self.customer_statistics is None):
                        self.customer_statistics = Pmipv6.Lma.Statistics.CustomerStatistics()
                        self.customer_statistics.parent = self
                        self._children_name_map["customer_statistics"] = "customer-statistics"
                    return self.customer_statistics

                if (child_yang_name == "global"):
                    if (self.global_ is None):
                        self.global_ = Pmipv6.Lma.Statistics.Global_()
                        self.global_.parent = self
                        self._children_name_map["global_"] = "global"
                    return self.global_

                if (child_yang_name == "mag-statistics"):
                    if (self.mag_statistics is None):
                        self.mag_statistics = Pmipv6.Lma.Statistics.MagStatistics()
                        self.mag_statistics.parent = self
                        self._children_name_map["mag_statistics"] = "mag-statistics"
                    return self.mag_statistics

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "customer-statistics" or name == "global" or name == "mag-statistics"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Bindings(Entity):
            """
            Table of Binding
            
            .. attribute:: binding
            
            	Binding Parameters
            	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Bindings.Binding>`
            
            

            """

            _prefix = 'ip-mobileip-oper'
            _revision = '2016-03-10'

            def __init__(self):
                super(Pmipv6.Lma.Bindings, self).__init__()

                self.yang_name = "bindings"
                self.yang_parent_name = "lma"

                self.binding = YList(self)

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
                            super(Pmipv6.Lma.Bindings, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Pmipv6.Lma.Bindings, self).__setattr__(name, value)


            class Binding(Entity):
                """
                Binding Parameters
                
                .. attribute:: apn
                
                	Access Point Network
                	**type**\:  str
                
                .. attribute:: att
                
                	MN ATT
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: coa
                
                	COA entries
                	**type**\: list of    :py:class:`Coa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Bindings.Binding.Coa>`
                
                .. attribute:: customer_name
                
                	Customer String
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: customer_name_xr
                
                	Customer name
                	**type**\:  str
                
                .. attribute:: dflt
                
                	MN Default Router
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: dmnp_v4
                
                	IPv4 DMNP prefixes
                	**type**\: list of    :py:class:`DmnpV4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Bindings.Binding.DmnpV4>`
                
                .. attribute:: dmnp_v6
                
                	IPv6 DMNP prefixes
                	**type**\: list of    :py:class:`DmnpV6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Bindings.Binding.DmnpV6>`
                
                .. attribute:: down_stream_grekey
                
                	DownStream GRE Key
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: hnps
                
                	MN Home Network Prefixes
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: hoa
                
                	MN HOA
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ignore_home_address
                
                	Ignore HoA/HNP
                	**type**\:  bool
                
                .. attribute:: imsi_string
                
                	IMSI String
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: liferem
                
                	Life Time Remaining
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: lifetime
                
                	Life Time of Binding
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: llid
                
                	Link Layer Identifier
                	**type**\:  str
                
                .. attribute:: mag_name
                
                	Peer MAG ID
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: mnnai
                
                	Mobile Node Identifier
                	**type**\:  str
                
                .. attribute:: nai_string
                
                	NAI String
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: num_coa
                
                	COA count
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: num_dmnp_v4
                
                	IPv4 DMNP count
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: num_dmnp_v6
                
                	IPv6 DMNP count
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: num_hnps
                
                	HNP count
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: peer_id
                
                	Peer Identifier
                	**type**\:  str
                
                .. attribute:: phyintf
                
                	Access Interface
                	**type**\:  str
                
                .. attribute:: prefix_len
                
                	Prefix Length
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: refresh
                
                	Refresh Time of Binding
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: refresh_rem
                
                	Refresh Time Remaining
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: state
                
                	State Name
                	**type**\:  str
                
                .. attribute:: tunnel
                
                	Tunnel Interface
                	**type**\:  str
                
                .. attribute:: up_stream_grekey
                
                	Upstream GRE Key
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrfid
                
                	VRF ID of Access Interface
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-mobileip-oper'
                _revision = '2016-03-10'

                def __init__(self):
                    super(Pmipv6.Lma.Bindings.Binding, self).__init__()

                    self.yang_name = "binding"
                    self.yang_parent_name = "bindings"

                    self.apn = YLeaf(YType.str, "apn")

                    self.att = YLeaf(YType.uint16, "att")

                    self.customer_name = YLeaf(YType.str, "customer-name")

                    self.customer_name_xr = YLeaf(YType.str, "customer-name-xr")

                    self.dflt = YLeaf(YType.str, "dflt")

                    self.down_stream_grekey = YLeaf(YType.uint32, "down-stream-grekey")

                    self.hnps = YLeaf(YType.str, "hnps")

                    self.hoa = YLeaf(YType.str, "hoa")

                    self.ignore_home_address = YLeaf(YType.boolean, "ignore-home-address")

                    self.imsi_string = YLeaf(YType.str, "imsi-string")

                    self.liferem = YLeaf(YType.uint32, "liferem")

                    self.lifetime = YLeaf(YType.uint32, "lifetime")

                    self.llid = YLeaf(YType.str, "llid")

                    self.mag_name = YLeaf(YType.str, "mag-name")

                    self.mnnai = YLeaf(YType.str, "mnnai")

                    self.nai_string = YLeaf(YType.str, "nai-string")

                    self.num_coa = YLeaf(YType.uint8, "num-coa")

                    self.num_dmnp_v4 = YLeaf(YType.uint8, "num-dmnp-v4")

                    self.num_dmnp_v6 = YLeaf(YType.uint8, "num-dmnp-v6")

                    self.num_hnps = YLeaf(YType.uint8, "num-hnps")

                    self.peer_id = YLeaf(YType.str, "peer-id")

                    self.phyintf = YLeaf(YType.str, "phyintf")

                    self.prefix_len = YLeaf(YType.uint8, "prefix-len")

                    self.refresh = YLeaf(YType.uint32, "refresh")

                    self.refresh_rem = YLeaf(YType.uint32, "refresh-rem")

                    self.state = YLeaf(YType.str, "state")

                    self.tunnel = YLeaf(YType.str, "tunnel")

                    self.up_stream_grekey = YLeaf(YType.uint32, "up-stream-grekey")

                    self.vrfid = YLeaf(YType.uint32, "vrfid")

                    self.coa = YList(self)
                    self.dmnp_v4 = YList(self)
                    self.dmnp_v6 = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("apn",
                                    "att",
                                    "customer_name",
                                    "customer_name_xr",
                                    "dflt",
                                    "down_stream_grekey",
                                    "hnps",
                                    "hoa",
                                    "ignore_home_address",
                                    "imsi_string",
                                    "liferem",
                                    "lifetime",
                                    "llid",
                                    "mag_name",
                                    "mnnai",
                                    "nai_string",
                                    "num_coa",
                                    "num_dmnp_v4",
                                    "num_dmnp_v6",
                                    "num_hnps",
                                    "peer_id",
                                    "phyintf",
                                    "prefix_len",
                                    "refresh",
                                    "refresh_rem",
                                    "state",
                                    "tunnel",
                                    "up_stream_grekey",
                                    "vrfid") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Pmipv6.Lma.Bindings.Binding, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Pmipv6.Lma.Bindings.Binding, self).__setattr__(name, value)


                class Coa(Entity):
                    """
                    COA entries
                    
                    .. attribute:: att
                    
                    	MN ATT
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: cdma_nai
                    
                    	CDMA NAI
                    	**type**\:  str
                    
                    .. attribute:: coa_v4
                    
                    	IPv4 CoA
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: coa_v6
                    
                    	IPv6 CoA
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: color
                    
                    	Label Color
                    	**type**\:  str
                    
                    .. attribute:: dnkey
                    
                    	down key for coa tunnel
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: e_label
                    
                    	Egress Label
                    	**type**\:  str
                    
                    .. attribute:: imsi
                    
                    	IMSI or IMSI NAI
                    	**type**\:  str
                    
                    .. attribute:: lifetime
                    
                    	Life Time of coa
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lifetime_remaining
                    
                    	Life Time remain of coa
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: llid
                    
                    	Link Layer Identifier
                    	**type**\:  str
                    
                    .. attribute:: msisdn
                    
                    	MSISDN
                    	**type**\:  str
                    
                    .. attribute:: peer_name
                    
                    	Peer Name
                    	**type**\:  str
                    
                    .. attribute:: pgw_apn
                    
                    	Subscriber APN on PWG
                    	**type**\:  str
                    
                    .. attribute:: pgw_trans_vrf
                    
                    	Subscriber Transport VRF on PGW
                    	**type**\:  str
                    
                    .. attribute:: pstate
                    
                    	COA STATE
                    	**type**\:  str
                    
                    .. attribute:: refresh
                    
                    	refresh Time of coa
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: refresh_rem
                    
                    	refresh Time remain of coa
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: roa_min_tf
                    
                    	Roaming Intf
                    	**type**\:  str
                    
                    .. attribute:: tunnel
                    
                    	Tunnel Interface
                    	**type**\:  str
                    
                    .. attribute:: upkey
                    
                    	up key for coa tunnel
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.Bindings.Binding.Coa, self).__init__()

                        self.yang_name = "coa"
                        self.yang_parent_name = "binding"

                        self.att = YLeaf(YType.uint16, "att")

                        self.cdma_nai = YLeaf(YType.str, "cdma-nai")

                        self.coa_v4 = YLeaf(YType.str, "coa-v4")

                        self.coa_v6 = YLeaf(YType.str, "coa-v6")

                        self.color = YLeaf(YType.str, "color")

                        self.dnkey = YLeaf(YType.uint32, "dnkey")

                        self.e_label = YLeaf(YType.str, "e-label")

                        self.imsi = YLeaf(YType.str, "imsi")

                        self.lifetime = YLeaf(YType.uint32, "lifetime")

                        self.lifetime_remaining = YLeaf(YType.uint32, "lifetime-remaining")

                        self.llid = YLeaf(YType.str, "llid")

                        self.msisdn = YLeaf(YType.str, "msisdn")

                        self.peer_name = YLeaf(YType.str, "peer-name")

                        self.pgw_apn = YLeaf(YType.str, "pgw-apn")

                        self.pgw_trans_vrf = YLeaf(YType.str, "pgw-trans-vrf")

                        self.pstate = YLeaf(YType.str, "pstate")

                        self.refresh = YLeaf(YType.uint32, "refresh")

                        self.refresh_rem = YLeaf(YType.uint32, "refresh-rem")

                        self.roa_min_tf = YLeaf(YType.str, "roa-min-tf")

                        self.tunnel = YLeaf(YType.str, "tunnel")

                        self.upkey = YLeaf(YType.uint32, "upkey")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("att",
                                        "cdma_nai",
                                        "coa_v4",
                                        "coa_v6",
                                        "color",
                                        "dnkey",
                                        "e_label",
                                        "imsi",
                                        "lifetime",
                                        "lifetime_remaining",
                                        "llid",
                                        "msisdn",
                                        "peer_name",
                                        "pgw_apn",
                                        "pgw_trans_vrf",
                                        "pstate",
                                        "refresh",
                                        "refresh_rem",
                                        "roa_min_tf",
                                        "tunnel",
                                        "upkey") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pmipv6.Lma.Bindings.Binding.Coa, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pmipv6.Lma.Bindings.Binding.Coa, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.att.is_set or
                            self.cdma_nai.is_set or
                            self.coa_v4.is_set or
                            self.coa_v6.is_set or
                            self.color.is_set or
                            self.dnkey.is_set or
                            self.e_label.is_set or
                            self.imsi.is_set or
                            self.lifetime.is_set or
                            self.lifetime_remaining.is_set or
                            self.llid.is_set or
                            self.msisdn.is_set or
                            self.peer_name.is_set or
                            self.pgw_apn.is_set or
                            self.pgw_trans_vrf.is_set or
                            self.pstate.is_set or
                            self.refresh.is_set or
                            self.refresh_rem.is_set or
                            self.roa_min_tf.is_set or
                            self.tunnel.is_set or
                            self.upkey.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.att.yfilter != YFilter.not_set or
                            self.cdma_nai.yfilter != YFilter.not_set or
                            self.coa_v4.yfilter != YFilter.not_set or
                            self.coa_v6.yfilter != YFilter.not_set or
                            self.color.yfilter != YFilter.not_set or
                            self.dnkey.yfilter != YFilter.not_set or
                            self.e_label.yfilter != YFilter.not_set or
                            self.imsi.yfilter != YFilter.not_set or
                            self.lifetime.yfilter != YFilter.not_set or
                            self.lifetime_remaining.yfilter != YFilter.not_set or
                            self.llid.yfilter != YFilter.not_set or
                            self.msisdn.yfilter != YFilter.not_set or
                            self.peer_name.yfilter != YFilter.not_set or
                            self.pgw_apn.yfilter != YFilter.not_set or
                            self.pgw_trans_vrf.yfilter != YFilter.not_set or
                            self.pstate.yfilter != YFilter.not_set or
                            self.refresh.yfilter != YFilter.not_set or
                            self.refresh_rem.yfilter != YFilter.not_set or
                            self.roa_min_tf.yfilter != YFilter.not_set or
                            self.tunnel.yfilter != YFilter.not_set or
                            self.upkey.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "coa" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/bindings/binding/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.att.is_set or self.att.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.att.get_name_leafdata())
                        if (self.cdma_nai.is_set or self.cdma_nai.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cdma_nai.get_name_leafdata())
                        if (self.coa_v4.is_set or self.coa_v4.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.coa_v4.get_name_leafdata())
                        if (self.coa_v6.is_set or self.coa_v6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.coa_v6.get_name_leafdata())
                        if (self.color.is_set or self.color.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.color.get_name_leafdata())
                        if (self.dnkey.is_set or self.dnkey.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dnkey.get_name_leafdata())
                        if (self.e_label.is_set or self.e_label.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.e_label.get_name_leafdata())
                        if (self.imsi.is_set or self.imsi.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.imsi.get_name_leafdata())
                        if (self.lifetime.is_set or self.lifetime.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lifetime.get_name_leafdata())
                        if (self.lifetime_remaining.is_set or self.lifetime_remaining.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lifetime_remaining.get_name_leafdata())
                        if (self.llid.is_set or self.llid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.llid.get_name_leafdata())
                        if (self.msisdn.is_set or self.msisdn.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.msisdn.get_name_leafdata())
                        if (self.peer_name.is_set or self.peer_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_name.get_name_leafdata())
                        if (self.pgw_apn.is_set or self.pgw_apn.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pgw_apn.get_name_leafdata())
                        if (self.pgw_trans_vrf.is_set or self.pgw_trans_vrf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pgw_trans_vrf.get_name_leafdata())
                        if (self.pstate.is_set or self.pstate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pstate.get_name_leafdata())
                        if (self.refresh.is_set or self.refresh.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.refresh.get_name_leafdata())
                        if (self.refresh_rem.is_set or self.refresh_rem.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.refresh_rem.get_name_leafdata())
                        if (self.roa_min_tf.is_set or self.roa_min_tf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.roa_min_tf.get_name_leafdata())
                        if (self.tunnel.is_set or self.tunnel.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tunnel.get_name_leafdata())
                        if (self.upkey.is_set or self.upkey.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.upkey.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "att" or name == "cdma-nai" or name == "coa-v4" or name == "coa-v6" or name == "color" or name == "dnkey" or name == "e-label" or name == "imsi" or name == "lifetime" or name == "lifetime-remaining" or name == "llid" or name == "msisdn" or name == "peer-name" or name == "pgw-apn" or name == "pgw-trans-vrf" or name == "pstate" or name == "refresh" or name == "refresh-rem" or name == "roa-min-tf" or name == "tunnel" or name == "upkey"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "att"):
                            self.att = value
                            self.att.value_namespace = name_space
                            self.att.value_namespace_prefix = name_space_prefix
                        if(value_path == "cdma-nai"):
                            self.cdma_nai = value
                            self.cdma_nai.value_namespace = name_space
                            self.cdma_nai.value_namespace_prefix = name_space_prefix
                        if(value_path == "coa-v4"):
                            self.coa_v4 = value
                            self.coa_v4.value_namespace = name_space
                            self.coa_v4.value_namespace_prefix = name_space_prefix
                        if(value_path == "coa-v6"):
                            self.coa_v6 = value
                            self.coa_v6.value_namespace = name_space
                            self.coa_v6.value_namespace_prefix = name_space_prefix
                        if(value_path == "color"):
                            self.color = value
                            self.color.value_namespace = name_space
                            self.color.value_namespace_prefix = name_space_prefix
                        if(value_path == "dnkey"):
                            self.dnkey = value
                            self.dnkey.value_namespace = name_space
                            self.dnkey.value_namespace_prefix = name_space_prefix
                        if(value_path == "e-label"):
                            self.e_label = value
                            self.e_label.value_namespace = name_space
                            self.e_label.value_namespace_prefix = name_space_prefix
                        if(value_path == "imsi"):
                            self.imsi = value
                            self.imsi.value_namespace = name_space
                            self.imsi.value_namespace_prefix = name_space_prefix
                        if(value_path == "lifetime"):
                            self.lifetime = value
                            self.lifetime.value_namespace = name_space
                            self.lifetime.value_namespace_prefix = name_space_prefix
                        if(value_path == "lifetime-remaining"):
                            self.lifetime_remaining = value
                            self.lifetime_remaining.value_namespace = name_space
                            self.lifetime_remaining.value_namespace_prefix = name_space_prefix
                        if(value_path == "llid"):
                            self.llid = value
                            self.llid.value_namespace = name_space
                            self.llid.value_namespace_prefix = name_space_prefix
                        if(value_path == "msisdn"):
                            self.msisdn = value
                            self.msisdn.value_namespace = name_space
                            self.msisdn.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-name"):
                            self.peer_name = value
                            self.peer_name.value_namespace = name_space
                            self.peer_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "pgw-apn"):
                            self.pgw_apn = value
                            self.pgw_apn.value_namespace = name_space
                            self.pgw_apn.value_namespace_prefix = name_space_prefix
                        if(value_path == "pgw-trans-vrf"):
                            self.pgw_trans_vrf = value
                            self.pgw_trans_vrf.value_namespace = name_space
                            self.pgw_trans_vrf.value_namespace_prefix = name_space_prefix
                        if(value_path == "pstate"):
                            self.pstate = value
                            self.pstate.value_namespace = name_space
                            self.pstate.value_namespace_prefix = name_space_prefix
                        if(value_path == "refresh"):
                            self.refresh = value
                            self.refresh.value_namespace = name_space
                            self.refresh.value_namespace_prefix = name_space_prefix
                        if(value_path == "refresh-rem"):
                            self.refresh_rem = value
                            self.refresh_rem.value_namespace = name_space
                            self.refresh_rem.value_namespace_prefix = name_space_prefix
                        if(value_path == "roa-min-tf"):
                            self.roa_min_tf = value
                            self.roa_min_tf.value_namespace = name_space
                            self.roa_min_tf.value_namespace_prefix = name_space_prefix
                        if(value_path == "tunnel"):
                            self.tunnel = value
                            self.tunnel.value_namespace = name_space
                            self.tunnel.value_namespace_prefix = name_space_prefix
                        if(value_path == "upkey"):
                            self.upkey = value
                            self.upkey.value_namespace = name_space
                            self.upkey.value_namespace_prefix = name_space_prefix


                class DmnpV4(Entity):
                    """
                    IPv4 DMNP prefixes
                    
                    .. attribute:: pfxlen
                    
                    	IPv4 prefix length
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: prefix
                    
                    	IPv4 prefix
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.Bindings.Binding.DmnpV4, self).__init__()

                        self.yang_name = "dmnp-v4"
                        self.yang_parent_name = "binding"

                        self.pfxlen = YLeaf(YType.uint8, "pfxlen")

                        self.prefix = YLeaf(YType.str, "prefix")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("pfxlen",
                                        "prefix") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pmipv6.Lma.Bindings.Binding.DmnpV4, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pmipv6.Lma.Bindings.Binding.DmnpV4, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.pfxlen.is_set or
                            self.prefix.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.pfxlen.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "dmnp-v4" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/bindings/binding/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.pfxlen.is_set or self.pfxlen.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pfxlen.get_name_leafdata())
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "pfxlen" or name == "prefix"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "pfxlen"):
                            self.pfxlen = value
                            self.pfxlen.value_namespace = name_space
                            self.pfxlen.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix


                class DmnpV6(Entity):
                    """
                    IPv6 DMNP prefixes
                    
                    .. attribute:: pfxlen
                    
                    	IPv6 prefix length
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: prefix
                    
                    	IPv6 prefix
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.Bindings.Binding.DmnpV6, self).__init__()

                        self.yang_name = "dmnp-v6"
                        self.yang_parent_name = "binding"

                        self.pfxlen = YLeaf(YType.uint8, "pfxlen")

                        self.prefix = YLeaf(YType.str, "prefix")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("pfxlen",
                                        "prefix") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pmipv6.Lma.Bindings.Binding.DmnpV6, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pmipv6.Lma.Bindings.Binding.DmnpV6, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.pfxlen.is_set or
                            self.prefix.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.pfxlen.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "dmnp-v6" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/bindings/binding/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.pfxlen.is_set or self.pfxlen.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pfxlen.get_name_leafdata())
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "pfxlen" or name == "prefix"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "pfxlen"):
                            self.pfxlen = value
                            self.pfxlen.value_namespace = name_space
                            self.pfxlen.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.coa:
                        if (c.has_data()):
                            return True
                    for c in self.dmnp_v4:
                        if (c.has_data()):
                            return True
                    for c in self.dmnp_v6:
                        if (c.has_data()):
                            return True
                    return (
                        self.apn.is_set or
                        self.att.is_set or
                        self.customer_name.is_set or
                        self.customer_name_xr.is_set or
                        self.dflt.is_set or
                        self.down_stream_grekey.is_set or
                        self.hnps.is_set or
                        self.hoa.is_set or
                        self.ignore_home_address.is_set or
                        self.imsi_string.is_set or
                        self.liferem.is_set or
                        self.lifetime.is_set or
                        self.llid.is_set or
                        self.mag_name.is_set or
                        self.mnnai.is_set or
                        self.nai_string.is_set or
                        self.num_coa.is_set or
                        self.num_dmnp_v4.is_set or
                        self.num_dmnp_v6.is_set or
                        self.num_hnps.is_set or
                        self.peer_id.is_set or
                        self.phyintf.is_set or
                        self.prefix_len.is_set or
                        self.refresh.is_set or
                        self.refresh_rem.is_set or
                        self.state.is_set or
                        self.tunnel.is_set or
                        self.up_stream_grekey.is_set or
                        self.vrfid.is_set)

                def has_operation(self):
                    for c in self.coa:
                        if (c.has_operation()):
                            return True
                    for c in self.dmnp_v4:
                        if (c.has_operation()):
                            return True
                    for c in self.dmnp_v6:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.apn.yfilter != YFilter.not_set or
                        self.att.yfilter != YFilter.not_set or
                        self.customer_name.yfilter != YFilter.not_set or
                        self.customer_name_xr.yfilter != YFilter.not_set or
                        self.dflt.yfilter != YFilter.not_set or
                        self.down_stream_grekey.yfilter != YFilter.not_set or
                        self.hnps.yfilter != YFilter.not_set or
                        self.hoa.yfilter != YFilter.not_set or
                        self.ignore_home_address.yfilter != YFilter.not_set or
                        self.imsi_string.yfilter != YFilter.not_set or
                        self.liferem.yfilter != YFilter.not_set or
                        self.lifetime.yfilter != YFilter.not_set or
                        self.llid.yfilter != YFilter.not_set or
                        self.mag_name.yfilter != YFilter.not_set or
                        self.mnnai.yfilter != YFilter.not_set or
                        self.nai_string.yfilter != YFilter.not_set or
                        self.num_coa.yfilter != YFilter.not_set or
                        self.num_dmnp_v4.yfilter != YFilter.not_set or
                        self.num_dmnp_v6.yfilter != YFilter.not_set or
                        self.num_hnps.yfilter != YFilter.not_set or
                        self.peer_id.yfilter != YFilter.not_set or
                        self.phyintf.yfilter != YFilter.not_set or
                        self.prefix_len.yfilter != YFilter.not_set or
                        self.refresh.yfilter != YFilter.not_set or
                        self.refresh_rem.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set or
                        self.tunnel.yfilter != YFilter.not_set or
                        self.up_stream_grekey.yfilter != YFilter.not_set or
                        self.vrfid.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "binding" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/bindings/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.apn.is_set or self.apn.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.apn.get_name_leafdata())
                    if (self.att.is_set or self.att.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.att.get_name_leafdata())
                    if (self.customer_name.is_set or self.customer_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.customer_name.get_name_leafdata())
                    if (self.customer_name_xr.is_set or self.customer_name_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.customer_name_xr.get_name_leafdata())
                    if (self.dflt.is_set or self.dflt.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dflt.get_name_leafdata())
                    if (self.down_stream_grekey.is_set or self.down_stream_grekey.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.down_stream_grekey.get_name_leafdata())
                    if (self.hnps.is_set or self.hnps.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hnps.get_name_leafdata())
                    if (self.hoa.is_set or self.hoa.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hoa.get_name_leafdata())
                    if (self.ignore_home_address.is_set or self.ignore_home_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ignore_home_address.get_name_leafdata())
                    if (self.imsi_string.is_set or self.imsi_string.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.imsi_string.get_name_leafdata())
                    if (self.liferem.is_set or self.liferem.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.liferem.get_name_leafdata())
                    if (self.lifetime.is_set or self.lifetime.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.lifetime.get_name_leafdata())
                    if (self.llid.is_set or self.llid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.llid.get_name_leafdata())
                    if (self.mag_name.is_set or self.mag_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mag_name.get_name_leafdata())
                    if (self.mnnai.is_set or self.mnnai.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mnnai.get_name_leafdata())
                    if (self.nai_string.is_set or self.nai_string.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nai_string.get_name_leafdata())
                    if (self.num_coa.is_set or self.num_coa.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.num_coa.get_name_leafdata())
                    if (self.num_dmnp_v4.is_set or self.num_dmnp_v4.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.num_dmnp_v4.get_name_leafdata())
                    if (self.num_dmnp_v6.is_set or self.num_dmnp_v6.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.num_dmnp_v6.get_name_leafdata())
                    if (self.num_hnps.is_set or self.num_hnps.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.num_hnps.get_name_leafdata())
                    if (self.peer_id.is_set or self.peer_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peer_id.get_name_leafdata())
                    if (self.phyintf.is_set or self.phyintf.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.phyintf.get_name_leafdata())
                    if (self.prefix_len.is_set or self.prefix_len.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_len.get_name_leafdata())
                    if (self.refresh.is_set or self.refresh.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.refresh.get_name_leafdata())
                    if (self.refresh_rem.is_set or self.refresh_rem.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.refresh_rem.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())
                    if (self.tunnel.is_set or self.tunnel.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tunnel.get_name_leafdata())
                    if (self.up_stream_grekey.is_set or self.up_stream_grekey.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.up_stream_grekey.get_name_leafdata())
                    if (self.vrfid.is_set or self.vrfid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrfid.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "coa"):
                        for c in self.coa:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Pmipv6.Lma.Bindings.Binding.Coa()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.coa.append(c)
                        return c

                    if (child_yang_name == "dmnp-v4"):
                        for c in self.dmnp_v4:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Pmipv6.Lma.Bindings.Binding.DmnpV4()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.dmnp_v4.append(c)
                        return c

                    if (child_yang_name == "dmnp-v6"):
                        for c in self.dmnp_v6:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Pmipv6.Lma.Bindings.Binding.DmnpV6()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.dmnp_v6.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "coa" or name == "dmnp-v4" or name == "dmnp-v6" or name == "apn" or name == "att" or name == "customer-name" or name == "customer-name-xr" or name == "dflt" or name == "down-stream-grekey" or name == "hnps" or name == "hoa" or name == "ignore-home-address" or name == "imsi-string" or name == "liferem" or name == "lifetime" or name == "llid" or name == "mag-name" or name == "mnnai" or name == "nai-string" or name == "num-coa" or name == "num-dmnp-v4" or name == "num-dmnp-v6" or name == "num-hnps" or name == "peer-id" or name == "phyintf" or name == "prefix-len" or name == "refresh" or name == "refresh-rem" or name == "state" or name == "tunnel" or name == "up-stream-grekey" or name == "vrfid"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "apn"):
                        self.apn = value
                        self.apn.value_namespace = name_space
                        self.apn.value_namespace_prefix = name_space_prefix
                    if(value_path == "att"):
                        self.att = value
                        self.att.value_namespace = name_space
                        self.att.value_namespace_prefix = name_space_prefix
                    if(value_path == "customer-name"):
                        self.customer_name = value
                        self.customer_name.value_namespace = name_space
                        self.customer_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "customer-name-xr"):
                        self.customer_name_xr = value
                        self.customer_name_xr.value_namespace = name_space
                        self.customer_name_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "dflt"):
                        self.dflt = value
                        self.dflt.value_namespace = name_space
                        self.dflt.value_namespace_prefix = name_space_prefix
                    if(value_path == "down-stream-grekey"):
                        self.down_stream_grekey = value
                        self.down_stream_grekey.value_namespace = name_space
                        self.down_stream_grekey.value_namespace_prefix = name_space_prefix
                    if(value_path == "hnps"):
                        self.hnps = value
                        self.hnps.value_namespace = name_space
                        self.hnps.value_namespace_prefix = name_space_prefix
                    if(value_path == "hoa"):
                        self.hoa = value
                        self.hoa.value_namespace = name_space
                        self.hoa.value_namespace_prefix = name_space_prefix
                    if(value_path == "ignore-home-address"):
                        self.ignore_home_address = value
                        self.ignore_home_address.value_namespace = name_space
                        self.ignore_home_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "imsi-string"):
                        self.imsi_string = value
                        self.imsi_string.value_namespace = name_space
                        self.imsi_string.value_namespace_prefix = name_space_prefix
                    if(value_path == "liferem"):
                        self.liferem = value
                        self.liferem.value_namespace = name_space
                        self.liferem.value_namespace_prefix = name_space_prefix
                    if(value_path == "lifetime"):
                        self.lifetime = value
                        self.lifetime.value_namespace = name_space
                        self.lifetime.value_namespace_prefix = name_space_prefix
                    if(value_path == "llid"):
                        self.llid = value
                        self.llid.value_namespace = name_space
                        self.llid.value_namespace_prefix = name_space_prefix
                    if(value_path == "mag-name"):
                        self.mag_name = value
                        self.mag_name.value_namespace = name_space
                        self.mag_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "mnnai"):
                        self.mnnai = value
                        self.mnnai.value_namespace = name_space
                        self.mnnai.value_namespace_prefix = name_space_prefix
                    if(value_path == "nai-string"):
                        self.nai_string = value
                        self.nai_string.value_namespace = name_space
                        self.nai_string.value_namespace_prefix = name_space_prefix
                    if(value_path == "num-coa"):
                        self.num_coa = value
                        self.num_coa.value_namespace = name_space
                        self.num_coa.value_namespace_prefix = name_space_prefix
                    if(value_path == "num-dmnp-v4"):
                        self.num_dmnp_v4 = value
                        self.num_dmnp_v4.value_namespace = name_space
                        self.num_dmnp_v4.value_namespace_prefix = name_space_prefix
                    if(value_path == "num-dmnp-v6"):
                        self.num_dmnp_v6 = value
                        self.num_dmnp_v6.value_namespace = name_space
                        self.num_dmnp_v6.value_namespace_prefix = name_space_prefix
                    if(value_path == "num-hnps"):
                        self.num_hnps = value
                        self.num_hnps.value_namespace = name_space
                        self.num_hnps.value_namespace_prefix = name_space_prefix
                    if(value_path == "peer-id"):
                        self.peer_id = value
                        self.peer_id.value_namespace = name_space
                        self.peer_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "phyintf"):
                        self.phyintf = value
                        self.phyintf.value_namespace = name_space
                        self.phyintf.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix-len"):
                        self.prefix_len = value
                        self.prefix_len.value_namespace = name_space
                        self.prefix_len.value_namespace_prefix = name_space_prefix
                    if(value_path == "refresh"):
                        self.refresh = value
                        self.refresh.value_namespace = name_space
                        self.refresh.value_namespace_prefix = name_space_prefix
                    if(value_path == "refresh-rem"):
                        self.refresh_rem = value
                        self.refresh_rem.value_namespace = name_space
                        self.refresh_rem.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix
                    if(value_path == "tunnel"):
                        self.tunnel = value
                        self.tunnel.value_namespace = name_space
                        self.tunnel.value_namespace_prefix = name_space_prefix
                    if(value_path == "up-stream-grekey"):
                        self.up_stream_grekey = value
                        self.up_stream_grekey.value_namespace = name_space
                        self.up_stream_grekey.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrfid"):
                        self.vrfid = value
                        self.vrfid.value_namespace = name_space
                        self.vrfid.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.binding:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.binding:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "bindings" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "binding"):
                    for c in self.binding:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Pmipv6.Lma.Bindings.Binding()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.binding.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "binding"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Heartbeats(Entity):
            """
            Table of Heartbeat
            
            .. attribute:: heartbeat
            
            	Heartbeat information
            	**type**\: list of    :py:class:`Heartbeat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Heartbeats.Heartbeat>`
            
            

            """

            _prefix = 'ip-mobileip-oper'
            _revision = '2016-03-10'

            def __init__(self):
                super(Pmipv6.Lma.Heartbeats, self).__init__()

                self.yang_name = "heartbeats"
                self.yang_parent_name = "lma"

                self.heartbeat = YList(self)

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
                            super(Pmipv6.Lma.Heartbeats, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Pmipv6.Lma.Heartbeats, self).__setattr__(name, value)


            class Heartbeat(Entity):
                """
                Heartbeat information
                
                .. attribute:: peer_addr  <key>
                
                	IPv4 or IPv6 address
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: customer_name
                
                	Customer Name
                	**type**\:  str
                
                .. attribute:: destination_ipv4_address
                
                	Destination IPv4 Address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: destination_ipv6_address
                
                	Destination IPv6 Address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: destination_port
                
                	Destination Port
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ipv6_path
                
                	IPv6 Path
                	**type**\:  bool
                
                .. attribute:: source_ipv4_address
                
                	Source IPv4 Address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: source_ipv6_address
                
                	Source IPv6 Address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: source_port
                
                	Source Port
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: status
                
                	Path Status
                	**type**\:  bool
                
                .. attribute:: vrf
                
                	VRF Name
                	**type**\:  str
                
                

                """

                _prefix = 'ip-mobileip-oper'
                _revision = '2016-03-10'

                def __init__(self):
                    super(Pmipv6.Lma.Heartbeats.Heartbeat, self).__init__()

                    self.yang_name = "heartbeat"
                    self.yang_parent_name = "heartbeats"

                    self.peer_addr = YLeaf(YType.str, "peer-addr")

                    self.customer_name = YLeaf(YType.str, "customer-name")

                    self.destination_ipv4_address = YLeaf(YType.str, "destination-ipv4-address")

                    self.destination_ipv6_address = YLeaf(YType.str, "destination-ipv6-address")

                    self.destination_port = YLeaf(YType.uint32, "destination-port")

                    self.ipv6_path = YLeaf(YType.boolean, "ipv6-path")

                    self.source_ipv4_address = YLeaf(YType.str, "source-ipv4-address")

                    self.source_ipv6_address = YLeaf(YType.str, "source-ipv6-address")

                    self.source_port = YLeaf(YType.uint32, "source-port")

                    self.status = YLeaf(YType.boolean, "status")

                    self.vrf = YLeaf(YType.str, "vrf")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("peer_addr",
                                    "customer_name",
                                    "destination_ipv4_address",
                                    "destination_ipv6_address",
                                    "destination_port",
                                    "ipv6_path",
                                    "source_ipv4_address",
                                    "source_ipv6_address",
                                    "source_port",
                                    "status",
                                    "vrf") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Pmipv6.Lma.Heartbeats.Heartbeat, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Pmipv6.Lma.Heartbeats.Heartbeat, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.peer_addr.is_set or
                        self.customer_name.is_set or
                        self.destination_ipv4_address.is_set or
                        self.destination_ipv6_address.is_set or
                        self.destination_port.is_set or
                        self.ipv6_path.is_set or
                        self.source_ipv4_address.is_set or
                        self.source_ipv6_address.is_set or
                        self.source_port.is_set or
                        self.status.is_set or
                        self.vrf.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.peer_addr.yfilter != YFilter.not_set or
                        self.customer_name.yfilter != YFilter.not_set or
                        self.destination_ipv4_address.yfilter != YFilter.not_set or
                        self.destination_ipv6_address.yfilter != YFilter.not_set or
                        self.destination_port.yfilter != YFilter.not_set or
                        self.ipv6_path.yfilter != YFilter.not_set or
                        self.source_ipv4_address.yfilter != YFilter.not_set or
                        self.source_ipv6_address.yfilter != YFilter.not_set or
                        self.source_port.yfilter != YFilter.not_set or
                        self.status.yfilter != YFilter.not_set or
                        self.vrf.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "heartbeat" + "[peer-addr='" + self.peer_addr.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/heartbeats/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.peer_addr.is_set or self.peer_addr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peer_addr.get_name_leafdata())
                    if (self.customer_name.is_set or self.customer_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.customer_name.get_name_leafdata())
                    if (self.destination_ipv4_address.is_set or self.destination_ipv4_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_ipv4_address.get_name_leafdata())
                    if (self.destination_ipv6_address.is_set or self.destination_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_ipv6_address.get_name_leafdata())
                    if (self.destination_port.is_set or self.destination_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_port.get_name_leafdata())
                    if (self.ipv6_path.is_set or self.ipv6_path.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipv6_path.get_name_leafdata())
                    if (self.source_ipv4_address.is_set or self.source_ipv4_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_ipv4_address.get_name_leafdata())
                    if (self.source_ipv6_address.is_set or self.source_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_ipv6_address.get_name_leafdata())
                    if (self.source_port.is_set or self.source_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_port.get_name_leafdata())
                    if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.status.get_name_leafdata())
                    if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "peer-addr" or name == "customer-name" or name == "destination-ipv4-address" or name == "destination-ipv6-address" or name == "destination-port" or name == "ipv6-path" or name == "source-ipv4-address" or name == "source-ipv6-address" or name == "source-port" or name == "status" or name == "vrf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "peer-addr"):
                        self.peer_addr = value
                        self.peer_addr.value_namespace = name_space
                        self.peer_addr.value_namespace_prefix = name_space_prefix
                    if(value_path == "customer-name"):
                        self.customer_name = value
                        self.customer_name.value_namespace = name_space
                        self.customer_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-ipv4-address"):
                        self.destination_ipv4_address = value
                        self.destination_ipv4_address.value_namespace = name_space
                        self.destination_ipv4_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-ipv6-address"):
                        self.destination_ipv6_address = value
                        self.destination_ipv6_address.value_namespace = name_space
                        self.destination_ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-port"):
                        self.destination_port = value
                        self.destination_port.value_namespace = name_space
                        self.destination_port.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipv6-path"):
                        self.ipv6_path = value
                        self.ipv6_path.value_namespace = name_space
                        self.ipv6_path.value_namespace_prefix = name_space_prefix
                    if(value_path == "source-ipv4-address"):
                        self.source_ipv4_address = value
                        self.source_ipv4_address.value_namespace = name_space
                        self.source_ipv4_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "source-ipv6-address"):
                        self.source_ipv6_address = value
                        self.source_ipv6_address.value_namespace = name_space
                        self.source_ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "source-port"):
                        self.source_port = value
                        self.source_port.value_namespace = name_space
                        self.source_port.value_namespace_prefix = name_space_prefix
                    if(value_path == "status"):
                        self.status = value
                        self.status.value_namespace = name_space
                        self.status.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf"):
                        self.vrf = value
                        self.vrf.value_namespace = name_space
                        self.vrf.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.heartbeat:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.heartbeat:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "heartbeats" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "heartbeat"):
                    for c in self.heartbeat:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Pmipv6.Lma.Heartbeats.Heartbeat()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.heartbeat.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "heartbeat"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class ConfigVariables(Entity):
            """
            Global Configuration Variables
            
            .. attribute:: customer_variables
            
            	Table of CustomerVariables
            	**type**\:   :py:class:`CustomerVariables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.CustomerVariables>`
            
            .. attribute:: global_variables
            
            	Global Configuration Variables
            	**type**\:   :py:class:`GlobalVariables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.GlobalVariables>`
            
            

            """

            _prefix = 'ip-mobileip-oper'
            _revision = '2016-03-10'

            def __init__(self):
                super(Pmipv6.Lma.ConfigVariables, self).__init__()

                self.yang_name = "config-variables"
                self.yang_parent_name = "lma"

                self.customer_variables = Pmipv6.Lma.ConfigVariables.CustomerVariables()
                self.customer_variables.parent = self
                self._children_name_map["customer_variables"] = "customer-variables"
                self._children_yang_names.add("customer-variables")

                self.global_variables = Pmipv6.Lma.ConfigVariables.GlobalVariables()
                self.global_variables.parent = self
                self._children_name_map["global_variables"] = "global-variables"
                self._children_yang_names.add("global-variables")


            class CustomerVariables(Entity):
                """
                Table of CustomerVariables
                
                .. attribute:: customer_variable
                
                	Customer name string
                	**type**\: list of    :py:class:`CustomerVariable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable>`
                
                

                """

                _prefix = 'ip-mobileip-oper'
                _revision = '2016-03-10'

                def __init__(self):
                    super(Pmipv6.Lma.ConfigVariables.CustomerVariables, self).__init__()

                    self.yang_name = "customer-variables"
                    self.yang_parent_name = "config-variables"

                    self.customer_variable = YList(self)

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
                                super(Pmipv6.Lma.ConfigVariables.CustomerVariables, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Pmipv6.Lma.ConfigVariables.CustomerVariables, self).__setattr__(name, value)


                class CustomerVariable(Entity):
                    """
                    Customer name string
                    
                    .. attribute:: customer_name  <key>
                    
                    	Customer name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: auth_option
                    
                    	Authentication Option
                    	**type**\:  bool
                    
                    .. attribute:: cust_name
                    
                    	Customer Name
                    	**type**\:  str
                    
                    .. attribute:: mll_service
                    
                    	MLL service parameters
                    	**type**\:   :py:class:`MllService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable.MllService>`
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable, self).__init__()

                        self.yang_name = "customer-variable"
                        self.yang_parent_name = "customer-variables"

                        self.customer_name = YLeaf(YType.str, "customer-name")

                        self.auth_option = YLeaf(YType.boolean, "auth-option")

                        self.cust_name = YLeaf(YType.str, "cust-name")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.mll_service = Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable.MllService()
                        self.mll_service.parent = self
                        self._children_name_map["mll_service"] = "mll-service"
                        self._children_yang_names.add("mll-service")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("customer_name",
                                        "auth_option",
                                        "cust_name",
                                        "vrf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable, self).__setattr__(name, value)


                    class MllService(Entity):
                        """
                        MLL service parameters
                        
                        .. attribute:: ignore_hoa
                        
                        	Ignore Home Address
                        	**type**\:  bool
                        
                        .. attribute:: mnp_cust_max
                        
                        	Max prefixes per Customer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mnp_ipv4_cust_cur
                        
                        	Current IPv4 prefixes per Customer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mnp_ipv4_cust_max
                        
                        	Max IPv4 prefixes per Customer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mnp_ipv4_lmn_max
                        
                        	Max IPv4 prefixes per LMN
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: mnp_ipv6_cust_cur
                        
                        	Current IPv6 prefixes per Customer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mnp_ipv6_cust_max
                        
                        	Max IPv6 prefixes per Customer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mnp_ipv6_lmn_max
                        
                        	Max IPv6 prefixes per LMN
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: mnp_lmn_max
                        
                        	Max prefixes per LMN
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable.MllService, self).__init__()

                            self.yang_name = "mll-service"
                            self.yang_parent_name = "customer-variable"

                            self.ignore_hoa = YLeaf(YType.boolean, "ignore-hoa")

                            self.mnp_cust_max = YLeaf(YType.uint32, "mnp-cust-max")

                            self.mnp_ipv4_cust_cur = YLeaf(YType.uint32, "mnp-ipv4-cust-cur")

                            self.mnp_ipv4_cust_max = YLeaf(YType.uint32, "mnp-ipv4-cust-max")

                            self.mnp_ipv4_lmn_max = YLeaf(YType.uint16, "mnp-ipv4-lmn-max")

                            self.mnp_ipv6_cust_cur = YLeaf(YType.uint32, "mnp-ipv6-cust-cur")

                            self.mnp_ipv6_cust_max = YLeaf(YType.uint32, "mnp-ipv6-cust-max")

                            self.mnp_ipv6_lmn_max = YLeaf(YType.uint16, "mnp-ipv6-lmn-max")

                            self.mnp_lmn_max = YLeaf(YType.uint16, "mnp-lmn-max")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ignore_hoa",
                                            "mnp_cust_max",
                                            "mnp_ipv4_cust_cur",
                                            "mnp_ipv4_cust_max",
                                            "mnp_ipv4_lmn_max",
                                            "mnp_ipv6_cust_cur",
                                            "mnp_ipv6_cust_max",
                                            "mnp_ipv6_lmn_max",
                                            "mnp_lmn_max") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable.MllService, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable.MllService, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ignore_hoa.is_set or
                                self.mnp_cust_max.is_set or
                                self.mnp_ipv4_cust_cur.is_set or
                                self.mnp_ipv4_cust_max.is_set or
                                self.mnp_ipv4_lmn_max.is_set or
                                self.mnp_ipv6_cust_cur.is_set or
                                self.mnp_ipv6_cust_max.is_set or
                                self.mnp_ipv6_lmn_max.is_set or
                                self.mnp_lmn_max.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ignore_hoa.yfilter != YFilter.not_set or
                                self.mnp_cust_max.yfilter != YFilter.not_set or
                                self.mnp_ipv4_cust_cur.yfilter != YFilter.not_set or
                                self.mnp_ipv4_cust_max.yfilter != YFilter.not_set or
                                self.mnp_ipv4_lmn_max.yfilter != YFilter.not_set or
                                self.mnp_ipv6_cust_cur.yfilter != YFilter.not_set or
                                self.mnp_ipv6_cust_max.yfilter != YFilter.not_set or
                                self.mnp_ipv6_lmn_max.yfilter != YFilter.not_set or
                                self.mnp_lmn_max.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "mll-service" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ignore_hoa.is_set or self.ignore_hoa.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ignore_hoa.get_name_leafdata())
                            if (self.mnp_cust_max.is_set or self.mnp_cust_max.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mnp_cust_max.get_name_leafdata())
                            if (self.mnp_ipv4_cust_cur.is_set or self.mnp_ipv4_cust_cur.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mnp_ipv4_cust_cur.get_name_leafdata())
                            if (self.mnp_ipv4_cust_max.is_set or self.mnp_ipv4_cust_max.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mnp_ipv4_cust_max.get_name_leafdata())
                            if (self.mnp_ipv4_lmn_max.is_set or self.mnp_ipv4_lmn_max.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mnp_ipv4_lmn_max.get_name_leafdata())
                            if (self.mnp_ipv6_cust_cur.is_set or self.mnp_ipv6_cust_cur.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mnp_ipv6_cust_cur.get_name_leafdata())
                            if (self.mnp_ipv6_cust_max.is_set or self.mnp_ipv6_cust_max.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mnp_ipv6_cust_max.get_name_leafdata())
                            if (self.mnp_ipv6_lmn_max.is_set or self.mnp_ipv6_lmn_max.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mnp_ipv6_lmn_max.get_name_leafdata())
                            if (self.mnp_lmn_max.is_set or self.mnp_lmn_max.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mnp_lmn_max.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ignore-hoa" or name == "mnp-cust-max" or name == "mnp-ipv4-cust-cur" or name == "mnp-ipv4-cust-max" or name == "mnp-ipv4-lmn-max" or name == "mnp-ipv6-cust-cur" or name == "mnp-ipv6-cust-max" or name == "mnp-ipv6-lmn-max" or name == "mnp-lmn-max"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ignore-hoa"):
                                self.ignore_hoa = value
                                self.ignore_hoa.value_namespace = name_space
                                self.ignore_hoa.value_namespace_prefix = name_space_prefix
                            if(value_path == "mnp-cust-max"):
                                self.mnp_cust_max = value
                                self.mnp_cust_max.value_namespace = name_space
                                self.mnp_cust_max.value_namespace_prefix = name_space_prefix
                            if(value_path == "mnp-ipv4-cust-cur"):
                                self.mnp_ipv4_cust_cur = value
                                self.mnp_ipv4_cust_cur.value_namespace = name_space
                                self.mnp_ipv4_cust_cur.value_namespace_prefix = name_space_prefix
                            if(value_path == "mnp-ipv4-cust-max"):
                                self.mnp_ipv4_cust_max = value
                                self.mnp_ipv4_cust_max.value_namespace = name_space
                                self.mnp_ipv4_cust_max.value_namespace_prefix = name_space_prefix
                            if(value_path == "mnp-ipv4-lmn-max"):
                                self.mnp_ipv4_lmn_max = value
                                self.mnp_ipv4_lmn_max.value_namespace = name_space
                                self.mnp_ipv4_lmn_max.value_namespace_prefix = name_space_prefix
                            if(value_path == "mnp-ipv6-cust-cur"):
                                self.mnp_ipv6_cust_cur = value
                                self.mnp_ipv6_cust_cur.value_namespace = name_space
                                self.mnp_ipv6_cust_cur.value_namespace_prefix = name_space_prefix
                            if(value_path == "mnp-ipv6-cust-max"):
                                self.mnp_ipv6_cust_max = value
                                self.mnp_ipv6_cust_max.value_namespace = name_space
                                self.mnp_ipv6_cust_max.value_namespace_prefix = name_space_prefix
                            if(value_path == "mnp-ipv6-lmn-max"):
                                self.mnp_ipv6_lmn_max = value
                                self.mnp_ipv6_lmn_max.value_namespace = name_space
                                self.mnp_ipv6_lmn_max.value_namespace_prefix = name_space_prefix
                            if(value_path == "mnp-lmn-max"):
                                self.mnp_lmn_max = value
                                self.mnp_lmn_max.value_namespace = name_space
                                self.mnp_lmn_max.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.customer_name.is_set or
                            self.auth_option.is_set or
                            self.cust_name.is_set or
                            self.vrf_name.is_set or
                            (self.mll_service is not None and self.mll_service.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.customer_name.yfilter != YFilter.not_set or
                            self.auth_option.yfilter != YFilter.not_set or
                            self.cust_name.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set or
                            (self.mll_service is not None and self.mll_service.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "customer-variable" + "[customer-name='" + self.customer_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/customer-variables/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.customer_name.is_set or self.customer_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.customer_name.get_name_leafdata())
                        if (self.auth_option.is_set or self.auth_option.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auth_option.get_name_leafdata())
                        if (self.cust_name.is_set or self.cust_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cust_name.get_name_leafdata())
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "mll-service"):
                            if (self.mll_service is None):
                                self.mll_service = Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable.MllService()
                                self.mll_service.parent = self
                                self._children_name_map["mll_service"] = "mll-service"
                            return self.mll_service

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "mll-service" or name == "customer-name" or name == "auth-option" or name == "cust-name" or name == "vrf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "customer-name"):
                            self.customer_name = value
                            self.customer_name.value_namespace = name_space
                            self.customer_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "auth-option"):
                            self.auth_option = value
                            self.auth_option.value_namespace = name_space
                            self.auth_option.value_namespace_prefix = name_space_prefix
                        if(value_path == "cust-name"):
                            self.cust_name = value
                            self.cust_name.value_namespace = name_space
                            self.cust_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.customer_variable:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.customer_variable:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "customer-variables" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "customer-variable"):
                        for c in self.customer_variable:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.customer_variable.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "customer-variable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class GlobalVariables(Entity):
                """
                Global Configuration Variables
                
                .. attribute:: aaa_accounting
                
                	AAA Accounting
                	**type**\:  bool
                
                .. attribute:: apn
                
                	APN Present
                	**type**\:  bool
                
                .. attribute:: apn_name
                
                	APN Name
                	**type**\:  str
                
                .. attribute:: count
                
                	Number of Networks/Intf
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: cust
                
                	Customer parameters
                	**type**\: list of    :py:class:`Cust <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.GlobalVariables.Cust>`
                
                .. attribute:: customers
                
                	Number of Customers
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ddp
                
                	Discover Detach Period
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ddr
                
                	Discover Detach Retries
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: ddt
                
                	Discover Detach Timeout
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: default_mn
                
                	Default MN Enabled
                	**type**\:  bool
                
                .. attribute:: discover_mn
                
                	Discover MN Detachment
                	**type**\:  bool
                
                .. attribute:: domain
                
                	Domain Name
                	**type**\:  str
                
                .. attribute:: intf
                
                	MAG Access List
                	**type**\: list of    :py:class:`Intf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.GlobalVariables.Intf>`
                
                .. attribute:: learn_mag
                
                	Learn MAG
                	**type**\:  bool
                
                .. attribute:: local_routing
                
                	Local Routing
                	**type**\:  bool
                
                .. attribute:: mll_service
                
                	MLL service parameters
                	**type**\:   :py:class:`MllService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.GlobalVariables.MllService>`
                
                .. attribute:: network
                
                	LMA Network Parameters
                	**type**\: list of    :py:class:`Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.GlobalVariables.Network>`
                
                .. attribute:: num_network
                
                	Number of Networks
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: parameters
                
                	Domain Parameters
                	**type**\:   :py:class:`Parameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters>`
                
                .. attribute:: peer
                
                	Peer Parameters
                	**type**\: list of    :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.GlobalVariables.Peer>`
                
                .. attribute:: peers
                
                	Number of Peers
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: profile
                
                	Default MN Profile Name
                	**type**\:  str
                
                .. attribute:: role
                
                	Role Type
                	**type**\:   :py:class:`Pmipv6Role <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6Role>`
                
                .. attribute:: selfid
                
                	Self ID
                	**type**\:  str
                
                .. attribute:: service
                
                	Service
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: session_mgr
                
                	Session Manager
                	**type**\:  bool
                
                

                """

                _prefix = 'ip-mobileip-oper'
                _revision = '2016-03-10'

                def __init__(self):
                    super(Pmipv6.Lma.ConfigVariables.GlobalVariables, self).__init__()

                    self.yang_name = "global-variables"
                    self.yang_parent_name = "config-variables"

                    self.aaa_accounting = YLeaf(YType.boolean, "aaa-accounting")

                    self.apn = YLeaf(YType.boolean, "apn")

                    self.apn_name = YLeaf(YType.str, "apn-name")

                    self.count = YLeaf(YType.uint32, "count")

                    self.customers = YLeaf(YType.uint32, "customers")

                    self.ddp = YLeaf(YType.uint32, "ddp")

                    self.ddr = YLeaf(YType.uint8, "ddr")

                    self.ddt = YLeaf(YType.uint32, "ddt")

                    self.default_mn = YLeaf(YType.boolean, "default-mn")

                    self.discover_mn = YLeaf(YType.boolean, "discover-mn")

                    self.domain = YLeaf(YType.str, "domain")

                    self.learn_mag = YLeaf(YType.boolean, "learn-mag")

                    self.local_routing = YLeaf(YType.boolean, "local-routing")

                    self.num_network = YLeaf(YType.uint32, "num-network")

                    self.peers = YLeaf(YType.uint32, "peers")

                    self.profile = YLeaf(YType.str, "profile")

                    self.role = YLeaf(YType.enumeration, "role")

                    self.selfid = YLeaf(YType.str, "selfid")

                    self.service = YLeaf(YType.uint8, "service")

                    self.session_mgr = YLeaf(YType.boolean, "session-mgr")

                    self.mll_service = Pmipv6.Lma.ConfigVariables.GlobalVariables.MllService()
                    self.mll_service.parent = self
                    self._children_name_map["mll_service"] = "mll-service"
                    self._children_yang_names.add("mll-service")

                    self.parameters = Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters()
                    self.parameters.parent = self
                    self._children_name_map["parameters"] = "parameters"
                    self._children_yang_names.add("parameters")

                    self.cust = YList(self)
                    self.intf = YList(self)
                    self.network = YList(self)
                    self.peer = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("aaa_accounting",
                                    "apn",
                                    "apn_name",
                                    "count",
                                    "customers",
                                    "ddp",
                                    "ddr",
                                    "ddt",
                                    "default_mn",
                                    "discover_mn",
                                    "domain",
                                    "learn_mag",
                                    "local_routing",
                                    "num_network",
                                    "peers",
                                    "profile",
                                    "role",
                                    "selfid",
                                    "service",
                                    "session_mgr") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Pmipv6.Lma.ConfigVariables.GlobalVariables, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Pmipv6.Lma.ConfigVariables.GlobalVariables, self).__setattr__(name, value)


                class Parameters(Entity):
                    """
                    Domain Parameters
                    
                    .. attribute:: auth_option
                    
                    	Authentication Option
                    	**type**\:  bool
                    
                    .. attribute:: bri_init
                    
                    	BRI Init Delay time
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: bri_max
                    
                    	BRI Max Delay time
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: bri_retries
                    
                    	BRI Max Retries
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: create_time
                    
                    	BCE Create Wait Timer
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: delete_time
                    
                    	BCE Delete Hold Timer
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: down_grekey
                    
                    	Downstream GRE Key
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: encap
                    
                    	Encapsulation Type
                    	**type**\:   :py:class:`Pmipv6Encap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6Encap>`
                    
                    .. attribute:: hnp
                    
                    	Allowed HNPs per MN Intf
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: max_bindings
                    
                    	Allowed Max. Bindings
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ref_time
                    
                    	BCE Refresh Time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reg_time
                    
                    	BCE Registration Lifetime
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ret_max
                    
                    	Refresh Retransmit Max
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: retx
                    
                    	Refresh Retransmit Init
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: self_id
                    
                    	Self Identifier
                    	**type**\:   :py:class:`SelfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters.SelfId>`
                    
                    .. attribute:: timestamp
                    
                    	Timestamp method in use
                    	**type**\:  bool
                    
                    .. attribute:: up_grekey
                    
                    	Upstream GRE Key
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: window
                    
                    	Timestamp Validity Window
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters, self).__init__()

                        self.yang_name = "parameters"
                        self.yang_parent_name = "global-variables"

                        self.auth_option = YLeaf(YType.boolean, "auth-option")

                        self.bri_init = YLeaf(YType.uint16, "bri-init")

                        self.bri_max = YLeaf(YType.uint16, "bri-max")

                        self.bri_retries = YLeaf(YType.uint16, "bri-retries")

                        self.create_time = YLeaf(YType.uint16, "create-time")

                        self.delete_time = YLeaf(YType.uint16, "delete-time")

                        self.down_grekey = YLeaf(YType.uint32, "down-grekey")

                        self.encap = YLeaf(YType.enumeration, "encap")

                        self.hnp = YLeaf(YType.uint8, "hnp")

                        self.max_bindings = YLeaf(YType.uint32, "max-bindings")

                        self.ref_time = YLeaf(YType.uint32, "ref-time")

                        self.reg_time = YLeaf(YType.uint32, "reg-time")

                        self.ret_max = YLeaf(YType.uint16, "ret-max")

                        self.retx = YLeaf(YType.uint16, "retx")

                        self.timestamp = YLeaf(YType.boolean, "timestamp")

                        self.up_grekey = YLeaf(YType.uint32, "up-grekey")

                        self.window = YLeaf(YType.uint64, "window")

                        self.self_id = Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters.SelfId()
                        self.self_id.parent = self
                        self._children_name_map["self_id"] = "self-id"
                        self._children_yang_names.add("self-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("auth_option",
                                        "bri_init",
                                        "bri_max",
                                        "bri_retries",
                                        "create_time",
                                        "delete_time",
                                        "down_grekey",
                                        "encap",
                                        "hnp",
                                        "max_bindings",
                                        "ref_time",
                                        "reg_time",
                                        "ret_max",
                                        "retx",
                                        "timestamp",
                                        "up_grekey",
                                        "window") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters, self).__setattr__(name, value)


                    class SelfId(Entity):
                        """
                        Self Identifier
                        
                        .. attribute:: addr_type
                        
                        	IPV4 or IPV6 or Both
                        	**type**\:   :py:class:`Pmipv6Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6Addr>`
                        
                        .. attribute:: address
                        
                        	IPV6 address of LMA/MAG
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: entity_
                        
                        	Identifier of PMIP Node
                        	**type**\:  str
                        
                        .. attribute:: ipv4_address
                        
                        	IPV4 addrress of LMA/MAG
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters.SelfId, self).__init__()

                            self.yang_name = "self-id"
                            self.yang_parent_name = "parameters"

                            self.addr_type = YLeaf(YType.enumeration, "addr-type")

                            self.address = YLeaf(YType.str, "address")

                            self.entity_ = YLeaf(YType.str, "entity")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("addr_type",
                                            "address",
                                            "entity_",
                                            "ipv4_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters.SelfId, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters.SelfId, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.addr_type.is_set or
                                self.address.is_set or
                                self.entity_.is_set or
                                self.ipv4_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.addr_type.yfilter != YFilter.not_set or
                                self.address.yfilter != YFilter.not_set or
                                self.entity_.yfilter != YFilter.not_set or
                                self.ipv4_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "self-id" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/global-variables/parameters/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.addr_type.is_set or self.addr_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.addr_type.get_name_leafdata())
                            if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.address.get_name_leafdata())
                            if (self.entity_.is_set or self.entity_.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.entity_.get_name_leafdata())
                            if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "addr-type" or name == "address" or name == "entity" or name == "ipv4-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "addr-type"):
                                self.addr_type = value
                                self.addr_type.value_namespace = name_space
                                self.addr_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "address"):
                                self.address = value
                                self.address.value_namespace = name_space
                                self.address.value_namespace_prefix = name_space_prefix
                            if(value_path == "entity"):
                                self.entity_ = value
                                self.entity_.value_namespace = name_space
                                self.entity_.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-address"):
                                self.ipv4_address = value
                                self.ipv4_address.value_namespace = name_space
                                self.ipv4_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.auth_option.is_set or
                            self.bri_init.is_set or
                            self.bri_max.is_set or
                            self.bri_retries.is_set or
                            self.create_time.is_set or
                            self.delete_time.is_set or
                            self.down_grekey.is_set or
                            self.encap.is_set or
                            self.hnp.is_set or
                            self.max_bindings.is_set or
                            self.ref_time.is_set or
                            self.reg_time.is_set or
                            self.ret_max.is_set or
                            self.retx.is_set or
                            self.timestamp.is_set or
                            self.up_grekey.is_set or
                            self.window.is_set or
                            (self.self_id is not None and self.self_id.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.auth_option.yfilter != YFilter.not_set or
                            self.bri_init.yfilter != YFilter.not_set or
                            self.bri_max.yfilter != YFilter.not_set or
                            self.bri_retries.yfilter != YFilter.not_set or
                            self.create_time.yfilter != YFilter.not_set or
                            self.delete_time.yfilter != YFilter.not_set or
                            self.down_grekey.yfilter != YFilter.not_set or
                            self.encap.yfilter != YFilter.not_set or
                            self.hnp.yfilter != YFilter.not_set or
                            self.max_bindings.yfilter != YFilter.not_set or
                            self.ref_time.yfilter != YFilter.not_set or
                            self.reg_time.yfilter != YFilter.not_set or
                            self.ret_max.yfilter != YFilter.not_set or
                            self.retx.yfilter != YFilter.not_set or
                            self.timestamp.yfilter != YFilter.not_set or
                            self.up_grekey.yfilter != YFilter.not_set or
                            self.window.yfilter != YFilter.not_set or
                            (self.self_id is not None and self.self_id.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "parameters" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/global-variables/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.auth_option.is_set or self.auth_option.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auth_option.get_name_leafdata())
                        if (self.bri_init.is_set or self.bri_init.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bri_init.get_name_leafdata())
                        if (self.bri_max.is_set or self.bri_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bri_max.get_name_leafdata())
                        if (self.bri_retries.is_set or self.bri_retries.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bri_retries.get_name_leafdata())
                        if (self.create_time.is_set or self.create_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.create_time.get_name_leafdata())
                        if (self.delete_time.is_set or self.delete_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.delete_time.get_name_leafdata())
                        if (self.down_grekey.is_set or self.down_grekey.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.down_grekey.get_name_leafdata())
                        if (self.encap.is_set or self.encap.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.encap.get_name_leafdata())
                        if (self.hnp.is_set or self.hnp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hnp.get_name_leafdata())
                        if (self.max_bindings.is_set or self.max_bindings.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max_bindings.get_name_leafdata())
                        if (self.ref_time.is_set or self.ref_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ref_time.get_name_leafdata())
                        if (self.reg_time.is_set or self.reg_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reg_time.get_name_leafdata())
                        if (self.ret_max.is_set or self.ret_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ret_max.get_name_leafdata())
                        if (self.retx.is_set or self.retx.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.retx.get_name_leafdata())
                        if (self.timestamp.is_set or self.timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.timestamp.get_name_leafdata())
                        if (self.up_grekey.is_set or self.up_grekey.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.up_grekey.get_name_leafdata())
                        if (self.window.is_set or self.window.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.window.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "self-id"):
                            if (self.self_id is None):
                                self.self_id = Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters.SelfId()
                                self.self_id.parent = self
                                self._children_name_map["self_id"] = "self-id"
                            return self.self_id

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "self-id" or name == "auth-option" or name == "bri-init" or name == "bri-max" or name == "bri-retries" or name == "create-time" or name == "delete-time" or name == "down-grekey" or name == "encap" or name == "hnp" or name == "max-bindings" or name == "ref-time" or name == "reg-time" or name == "ret-max" or name == "retx" or name == "timestamp" or name == "up-grekey" or name == "window"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "auth-option"):
                            self.auth_option = value
                            self.auth_option.value_namespace = name_space
                            self.auth_option.value_namespace_prefix = name_space_prefix
                        if(value_path == "bri-init"):
                            self.bri_init = value
                            self.bri_init.value_namespace = name_space
                            self.bri_init.value_namespace_prefix = name_space_prefix
                        if(value_path == "bri-max"):
                            self.bri_max = value
                            self.bri_max.value_namespace = name_space
                            self.bri_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "bri-retries"):
                            self.bri_retries = value
                            self.bri_retries.value_namespace = name_space
                            self.bri_retries.value_namespace_prefix = name_space_prefix
                        if(value_path == "create-time"):
                            self.create_time = value
                            self.create_time.value_namespace = name_space
                            self.create_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "delete-time"):
                            self.delete_time = value
                            self.delete_time.value_namespace = name_space
                            self.delete_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "down-grekey"):
                            self.down_grekey = value
                            self.down_grekey.value_namespace = name_space
                            self.down_grekey.value_namespace_prefix = name_space_prefix
                        if(value_path == "encap"):
                            self.encap = value
                            self.encap.value_namespace = name_space
                            self.encap.value_namespace_prefix = name_space_prefix
                        if(value_path == "hnp"):
                            self.hnp = value
                            self.hnp.value_namespace = name_space
                            self.hnp.value_namespace_prefix = name_space_prefix
                        if(value_path == "max-bindings"):
                            self.max_bindings = value
                            self.max_bindings.value_namespace = name_space
                            self.max_bindings.value_namespace_prefix = name_space_prefix
                        if(value_path == "ref-time"):
                            self.ref_time = value
                            self.ref_time.value_namespace = name_space
                            self.ref_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "reg-time"):
                            self.reg_time = value
                            self.reg_time.value_namespace = name_space
                            self.reg_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "ret-max"):
                            self.ret_max = value
                            self.ret_max.value_namespace = name_space
                            self.ret_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "retx"):
                            self.retx = value
                            self.retx.value_namespace = name_space
                            self.retx.value_namespace_prefix = name_space_prefix
                        if(value_path == "timestamp"):
                            self.timestamp = value
                            self.timestamp.value_namespace = name_space
                            self.timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "up-grekey"):
                            self.up_grekey = value
                            self.up_grekey.value_namespace = name_space
                            self.up_grekey.value_namespace_prefix = name_space_prefix
                        if(value_path == "window"):
                            self.window = value
                            self.window.value_namespace = name_space
                            self.window.value_namespace_prefix = name_space_prefix


                class MllService(Entity):
                    """
                    MLL service parameters
                    
                    .. attribute:: ignore_hoa
                    
                    	Ignore Home Address
                    	**type**\:  bool
                    
                    .. attribute:: mnp_cust_max
                    
                    	Max prefixes per Customer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mnp_ipv4_cust_cur
                    
                    	Current IPv4 prefixes per Customer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mnp_ipv4_cust_max
                    
                    	Max IPv4 prefixes per Customer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mnp_ipv4_lmn_max
                    
                    	Max IPv4 prefixes per LMN
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: mnp_ipv6_cust_cur
                    
                    	Current IPv6 prefixes per Customer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mnp_ipv6_cust_max
                    
                    	Max IPv6 prefixes per Customer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mnp_ipv6_lmn_max
                    
                    	Max IPv6 prefixes per LMN
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: mnp_lmn_max
                    
                    	Max prefixes per LMN
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.ConfigVariables.GlobalVariables.MllService, self).__init__()

                        self.yang_name = "mll-service"
                        self.yang_parent_name = "global-variables"

                        self.ignore_hoa = YLeaf(YType.boolean, "ignore-hoa")

                        self.mnp_cust_max = YLeaf(YType.uint32, "mnp-cust-max")

                        self.mnp_ipv4_cust_cur = YLeaf(YType.uint32, "mnp-ipv4-cust-cur")

                        self.mnp_ipv4_cust_max = YLeaf(YType.uint32, "mnp-ipv4-cust-max")

                        self.mnp_ipv4_lmn_max = YLeaf(YType.uint16, "mnp-ipv4-lmn-max")

                        self.mnp_ipv6_cust_cur = YLeaf(YType.uint32, "mnp-ipv6-cust-cur")

                        self.mnp_ipv6_cust_max = YLeaf(YType.uint32, "mnp-ipv6-cust-max")

                        self.mnp_ipv6_lmn_max = YLeaf(YType.uint16, "mnp-ipv6-lmn-max")

                        self.mnp_lmn_max = YLeaf(YType.uint16, "mnp-lmn-max")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ignore_hoa",
                                        "mnp_cust_max",
                                        "mnp_ipv4_cust_cur",
                                        "mnp_ipv4_cust_max",
                                        "mnp_ipv4_lmn_max",
                                        "mnp_ipv6_cust_cur",
                                        "mnp_ipv6_cust_max",
                                        "mnp_ipv6_lmn_max",
                                        "mnp_lmn_max") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pmipv6.Lma.ConfigVariables.GlobalVariables.MllService, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pmipv6.Lma.ConfigVariables.GlobalVariables.MllService, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.ignore_hoa.is_set or
                            self.mnp_cust_max.is_set or
                            self.mnp_ipv4_cust_cur.is_set or
                            self.mnp_ipv4_cust_max.is_set or
                            self.mnp_ipv4_lmn_max.is_set or
                            self.mnp_ipv6_cust_cur.is_set or
                            self.mnp_ipv6_cust_max.is_set or
                            self.mnp_ipv6_lmn_max.is_set or
                            self.mnp_lmn_max.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ignore_hoa.yfilter != YFilter.not_set or
                            self.mnp_cust_max.yfilter != YFilter.not_set or
                            self.mnp_ipv4_cust_cur.yfilter != YFilter.not_set or
                            self.mnp_ipv4_cust_max.yfilter != YFilter.not_set or
                            self.mnp_ipv4_lmn_max.yfilter != YFilter.not_set or
                            self.mnp_ipv6_cust_cur.yfilter != YFilter.not_set or
                            self.mnp_ipv6_cust_max.yfilter != YFilter.not_set or
                            self.mnp_ipv6_lmn_max.yfilter != YFilter.not_set or
                            self.mnp_lmn_max.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "mll-service" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/global-variables/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ignore_hoa.is_set or self.ignore_hoa.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ignore_hoa.get_name_leafdata())
                        if (self.mnp_cust_max.is_set or self.mnp_cust_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mnp_cust_max.get_name_leafdata())
                        if (self.mnp_ipv4_cust_cur.is_set or self.mnp_ipv4_cust_cur.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mnp_ipv4_cust_cur.get_name_leafdata())
                        if (self.mnp_ipv4_cust_max.is_set or self.mnp_ipv4_cust_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mnp_ipv4_cust_max.get_name_leafdata())
                        if (self.mnp_ipv4_lmn_max.is_set or self.mnp_ipv4_lmn_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mnp_ipv4_lmn_max.get_name_leafdata())
                        if (self.mnp_ipv6_cust_cur.is_set or self.mnp_ipv6_cust_cur.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mnp_ipv6_cust_cur.get_name_leafdata())
                        if (self.mnp_ipv6_cust_max.is_set or self.mnp_ipv6_cust_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mnp_ipv6_cust_max.get_name_leafdata())
                        if (self.mnp_ipv6_lmn_max.is_set or self.mnp_ipv6_lmn_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mnp_ipv6_lmn_max.get_name_leafdata())
                        if (self.mnp_lmn_max.is_set or self.mnp_lmn_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mnp_lmn_max.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ignore-hoa" or name == "mnp-cust-max" or name == "mnp-ipv4-cust-cur" or name == "mnp-ipv4-cust-max" or name == "mnp-ipv4-lmn-max" or name == "mnp-ipv6-cust-cur" or name == "mnp-ipv6-cust-max" or name == "mnp-ipv6-lmn-max" or name == "mnp-lmn-max"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ignore-hoa"):
                            self.ignore_hoa = value
                            self.ignore_hoa.value_namespace = name_space
                            self.ignore_hoa.value_namespace_prefix = name_space_prefix
                        if(value_path == "mnp-cust-max"):
                            self.mnp_cust_max = value
                            self.mnp_cust_max.value_namespace = name_space
                            self.mnp_cust_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "mnp-ipv4-cust-cur"):
                            self.mnp_ipv4_cust_cur = value
                            self.mnp_ipv4_cust_cur.value_namespace = name_space
                            self.mnp_ipv4_cust_cur.value_namespace_prefix = name_space_prefix
                        if(value_path == "mnp-ipv4-cust-max"):
                            self.mnp_ipv4_cust_max = value
                            self.mnp_ipv4_cust_max.value_namespace = name_space
                            self.mnp_ipv4_cust_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "mnp-ipv4-lmn-max"):
                            self.mnp_ipv4_lmn_max = value
                            self.mnp_ipv4_lmn_max.value_namespace = name_space
                            self.mnp_ipv4_lmn_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "mnp-ipv6-cust-cur"):
                            self.mnp_ipv6_cust_cur = value
                            self.mnp_ipv6_cust_cur.value_namespace = name_space
                            self.mnp_ipv6_cust_cur.value_namespace_prefix = name_space_prefix
                        if(value_path == "mnp-ipv6-cust-max"):
                            self.mnp_ipv6_cust_max = value
                            self.mnp_ipv6_cust_max.value_namespace = name_space
                            self.mnp_ipv6_cust_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "mnp-ipv6-lmn-max"):
                            self.mnp_ipv6_lmn_max = value
                            self.mnp_ipv6_lmn_max.value_namespace = name_space
                            self.mnp_ipv6_lmn_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "mnp-lmn-max"):
                            self.mnp_lmn_max = value
                            self.mnp_lmn_max.value_namespace = name_space
                            self.mnp_lmn_max.value_namespace_prefix = name_space_prefix


                class Intf(Entity):
                    """
                    MAG Access List
                    
                    .. attribute:: apn
                    
                    	APN Present
                    	**type**\:  bool
                    
                    .. attribute:: apn_name
                    
                    	APN Name
                    	**type**\:  str
                    
                    .. attribute:: interface
                    
                    	Access Interface Name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Intf, self).__init__()

                        self.yang_name = "intf"
                        self.yang_parent_name = "global-variables"

                        self.apn = YLeaf(YType.boolean, "apn")

                        self.apn_name = YLeaf(YType.str, "apn-name")

                        self.interface = YLeaf(YType.str, "interface")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("apn",
                                        "apn_name",
                                        "interface") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Intf, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Intf, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.apn.is_set or
                            self.apn_name.is_set or
                            self.interface.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.apn.yfilter != YFilter.not_set or
                            self.apn_name.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "intf" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/global-variables/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.apn.is_set or self.apn.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.apn.get_name_leafdata())
                        if (self.apn_name.is_set or self.apn_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.apn_name.get_name_leafdata())
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "apn" or name == "apn-name" or name == "interface"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "apn"):
                            self.apn = value
                            self.apn.value_namespace = name_space
                            self.apn.value_namespace_prefix = name_space_prefix
                        if(value_path == "apn-name"):
                            self.apn_name = value
                            self.apn_name.value_namespace = name_space
                            self.apn_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix


                class Peer(Entity):
                    """
                    Peer Parameters
                    
                    .. attribute:: auth
                    
                    	Authentication Option
                    	**type**\:  bool
                    
                    .. attribute:: encap
                    
                    	Encapsulation Type
                    	**type**\:   :py:class:`Pmipv6Encap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6Encap>`
                    
                    .. attribute:: interface
                    
                    	Peer static tunnel intf
                    	**type**\:  str
                    
                    .. attribute:: peer
                    
                    	Peer Name
                    	**type**\:  str
                    
                    .. attribute:: statictunnel
                    
                    	Static tunnel Present
                    	**type**\:  bool
                    
                    .. attribute:: vrf
                    
                    	VRF Present
                    	**type**\:  bool
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Peer, self).__init__()

                        self.yang_name = "peer"
                        self.yang_parent_name = "global-variables"

                        self.auth = YLeaf(YType.boolean, "auth")

                        self.encap = YLeaf(YType.enumeration, "encap")

                        self.interface = YLeaf(YType.str, "interface")

                        self.peer = YLeaf(YType.str, "peer")

                        self.statictunnel = YLeaf(YType.boolean, "statictunnel")

                        self.vrf = YLeaf(YType.boolean, "vrf")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("auth",
                                        "encap",
                                        "interface",
                                        "peer",
                                        "statictunnel",
                                        "vrf",
                                        "vrf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Peer, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Peer, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.auth.is_set or
                            self.encap.is_set or
                            self.interface.is_set or
                            self.peer.is_set or
                            self.statictunnel.is_set or
                            self.vrf.is_set or
                            self.vrf_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.auth.yfilter != YFilter.not_set or
                            self.encap.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.peer.yfilter != YFilter.not_set or
                            self.statictunnel.yfilter != YFilter.not_set or
                            self.vrf.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "peer" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/global-variables/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.auth.is_set or self.auth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auth.get_name_leafdata())
                        if (self.encap.is_set or self.encap.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.encap.get_name_leafdata())
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.peer.is_set or self.peer.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer.get_name_leafdata())
                        if (self.statictunnel.is_set or self.statictunnel.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.statictunnel.get_name_leafdata())
                        if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf.get_name_leafdata())
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "auth" or name == "encap" or name == "interface" or name == "peer" or name == "statictunnel" or name == "vrf" or name == "vrf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "auth"):
                            self.auth = value
                            self.auth.value_namespace = name_space
                            self.auth.value_namespace_prefix = name_space_prefix
                        if(value_path == "encap"):
                            self.encap = value
                            self.encap.value_namespace = name_space
                            self.encap.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer"):
                            self.peer = value
                            self.peer.value_namespace = name_space
                            self.peer.value_namespace_prefix = name_space_prefix
                        if(value_path == "statictunnel"):
                            self.statictunnel = value
                            self.statictunnel.value_namespace = name_space
                            self.statictunnel.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf"):
                            self.vrf = value
                            self.vrf.value_namespace = name_space
                            self.vrf.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix


                class Network(Entity):
                    """
                    LMA Network Parameters
                    
                    .. attribute:: ipv4
                    
                    	IPv4 Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 Address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: mrnet
                    
                    	num of mrnet
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: network
                    
                    	Network Name
                    	**type**\:  str
                    
                    .. attribute:: v4pfx_len
                    
                    	v4 prefix len
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: v4pool
                    
                    	IPV4 pool Present
                    	**type**\:  bool
                    
                    .. attribute:: v6pfx_len
                    
                    	v6 prefix len
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: v6pool
                    
                    	IPV6 pool Present
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Network, self).__init__()

                        self.yang_name = "network"
                        self.yang_parent_name = "global-variables"

                        self.ipv4 = YLeaf(YType.str, "ipv4")

                        self.ipv6 = YLeaf(YType.str, "ipv6")

                        self.mrnet = YLeaf(YType.uint8, "mrnet")

                        self.network = YLeaf(YType.str, "network")

                        self.v4pfx_len = YLeaf(YType.uint8, "v4pfx-len")

                        self.v4pool = YLeaf(YType.boolean, "v4pool")

                        self.v6pfx_len = YLeaf(YType.uint8, "v6pfx-len")

                        self.v6pool = YLeaf(YType.boolean, "v6pool")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ipv4",
                                        "ipv6",
                                        "mrnet",
                                        "network",
                                        "v4pfx_len",
                                        "v4pool",
                                        "v6pfx_len",
                                        "v6pool") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Network, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Network, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.ipv4.is_set or
                            self.ipv6.is_set or
                            self.mrnet.is_set or
                            self.network.is_set or
                            self.v4pfx_len.is_set or
                            self.v4pool.is_set or
                            self.v6pfx_len.is_set or
                            self.v6pool.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ipv4.yfilter != YFilter.not_set or
                            self.ipv6.yfilter != YFilter.not_set or
                            self.mrnet.yfilter != YFilter.not_set or
                            self.network.yfilter != YFilter.not_set or
                            self.v4pfx_len.yfilter != YFilter.not_set or
                            self.v4pool.yfilter != YFilter.not_set or
                            self.v6pfx_len.yfilter != YFilter.not_set or
                            self.v6pool.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "network" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/global-variables/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ipv4.is_set or self.ipv4.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4.get_name_leafdata())
                        if (self.ipv6.is_set or self.ipv6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6.get_name_leafdata())
                        if (self.mrnet.is_set or self.mrnet.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mrnet.get_name_leafdata())
                        if (self.network.is_set or self.network.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.network.get_name_leafdata())
                        if (self.v4pfx_len.is_set or self.v4pfx_len.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.v4pfx_len.get_name_leafdata())
                        if (self.v4pool.is_set or self.v4pool.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.v4pool.get_name_leafdata())
                        if (self.v6pfx_len.is_set or self.v6pfx_len.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.v6pfx_len.get_name_leafdata())
                        if (self.v6pool.is_set or self.v6pool.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.v6pool.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipv4" or name == "ipv6" or name == "mrnet" or name == "network" or name == "v4pfx-len" or name == "v4pool" or name == "v6pfx-len" or name == "v6pool"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ipv4"):
                            self.ipv4 = value
                            self.ipv4.value_namespace = name_space
                            self.ipv4.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6"):
                            self.ipv6 = value
                            self.ipv6.value_namespace = name_space
                            self.ipv6.value_namespace_prefix = name_space_prefix
                        if(value_path == "mrnet"):
                            self.mrnet = value
                            self.mrnet.value_namespace = name_space
                            self.mrnet.value_namespace_prefix = name_space_prefix
                        if(value_path == "network"):
                            self.network = value
                            self.network.value_namespace = name_space
                            self.network.value_namespace_prefix = name_space_prefix
                        if(value_path == "v4pfx-len"):
                            self.v4pfx_len = value
                            self.v4pfx_len.value_namespace = name_space
                            self.v4pfx_len.value_namespace_prefix = name_space_prefix
                        if(value_path == "v4pool"):
                            self.v4pool = value
                            self.v4pool.value_namespace = name_space
                            self.v4pool.value_namespace_prefix = name_space_prefix
                        if(value_path == "v6pfx-len"):
                            self.v6pfx_len = value
                            self.v6pfx_len.value_namespace = name_space
                            self.v6pfx_len.value_namespace_prefix = name_space_prefix
                        if(value_path == "v6pool"):
                            self.v6pool = value
                            self.v6pool.value_namespace = name_space
                            self.v6pool.value_namespace_prefix = name_space_prefix


                class Cust(Entity):
                    """
                    Customer parameters
                    
                    .. attribute:: auth_option
                    
                    	Authentication Option
                    	**type**\:  bool
                    
                    .. attribute:: cust
                    
                    	Customer Present
                    	**type**\:  bool
                    
                    .. attribute:: cust_name
                    
                    	CUSTOMER Name
                    	**type**\:  str
                    
                    .. attribute:: heart_beat
                    
                    	HeartBeat Option
                    	**type**\:  bool
                    
                    .. attribute:: reg_time
                    
                    	BCE Registration Lifetime
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: t_vrf
                    
                    	Transport VRF Present
                    	**type**\:  bool
                    
                    .. attribute:: t_vrf_name
                    
                    	Transport VRF Name
                    	**type**\:  str
                    
                    .. attribute:: vrf
                    
                    	Customer VRF Present
                    	**type**\:  bool
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Cust, self).__init__()

                        self.yang_name = "cust"
                        self.yang_parent_name = "global-variables"

                        self.auth_option = YLeaf(YType.boolean, "auth-option")

                        self.cust = YLeaf(YType.boolean, "cust")

                        self.cust_name = YLeaf(YType.str, "cust-name")

                        self.heart_beat = YLeaf(YType.boolean, "heart-beat")

                        self.reg_time = YLeaf(YType.uint32, "reg-time")

                        self.t_vrf = YLeaf(YType.boolean, "t-vrf")

                        self.t_vrf_name = YLeaf(YType.str, "t-vrf-name")

                        self.vrf = YLeaf(YType.boolean, "vrf")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("auth_option",
                                        "cust",
                                        "cust_name",
                                        "heart_beat",
                                        "reg_time",
                                        "t_vrf",
                                        "t_vrf_name",
                                        "vrf",
                                        "vrf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Cust, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Cust, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.auth_option.is_set or
                            self.cust.is_set or
                            self.cust_name.is_set or
                            self.heart_beat.is_set or
                            self.reg_time.is_set or
                            self.t_vrf.is_set or
                            self.t_vrf_name.is_set or
                            self.vrf.is_set or
                            self.vrf_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.auth_option.yfilter != YFilter.not_set or
                            self.cust.yfilter != YFilter.not_set or
                            self.cust_name.yfilter != YFilter.not_set or
                            self.heart_beat.yfilter != YFilter.not_set or
                            self.reg_time.yfilter != YFilter.not_set or
                            self.t_vrf.yfilter != YFilter.not_set or
                            self.t_vrf_name.yfilter != YFilter.not_set or
                            self.vrf.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "cust" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/global-variables/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.auth_option.is_set or self.auth_option.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auth_option.get_name_leafdata())
                        if (self.cust.is_set or self.cust.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cust.get_name_leafdata())
                        if (self.cust_name.is_set or self.cust_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cust_name.get_name_leafdata())
                        if (self.heart_beat.is_set or self.heart_beat.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.heart_beat.get_name_leafdata())
                        if (self.reg_time.is_set or self.reg_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reg_time.get_name_leafdata())
                        if (self.t_vrf.is_set or self.t_vrf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.t_vrf.get_name_leafdata())
                        if (self.t_vrf_name.is_set or self.t_vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.t_vrf_name.get_name_leafdata())
                        if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf.get_name_leafdata())
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "auth-option" or name == "cust" or name == "cust-name" or name == "heart-beat" or name == "reg-time" or name == "t-vrf" or name == "t-vrf-name" or name == "vrf" or name == "vrf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "auth-option"):
                            self.auth_option = value
                            self.auth_option.value_namespace = name_space
                            self.auth_option.value_namespace_prefix = name_space_prefix
                        if(value_path == "cust"):
                            self.cust = value
                            self.cust.value_namespace = name_space
                            self.cust.value_namespace_prefix = name_space_prefix
                        if(value_path == "cust-name"):
                            self.cust_name = value
                            self.cust_name.value_namespace = name_space
                            self.cust_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "heart-beat"):
                            self.heart_beat = value
                            self.heart_beat.value_namespace = name_space
                            self.heart_beat.value_namespace_prefix = name_space_prefix
                        if(value_path == "reg-time"):
                            self.reg_time = value
                            self.reg_time.value_namespace = name_space
                            self.reg_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "t-vrf"):
                            self.t_vrf = value
                            self.t_vrf.value_namespace = name_space
                            self.t_vrf.value_namespace_prefix = name_space_prefix
                        if(value_path == "t-vrf-name"):
                            self.t_vrf_name = value
                            self.t_vrf_name.value_namespace = name_space
                            self.t_vrf_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf"):
                            self.vrf = value
                            self.vrf.value_namespace = name_space
                            self.vrf.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.cust:
                        if (c.has_data()):
                            return True
                    for c in self.intf:
                        if (c.has_data()):
                            return True
                    for c in self.network:
                        if (c.has_data()):
                            return True
                    for c in self.peer:
                        if (c.has_data()):
                            return True
                    return (
                        self.aaa_accounting.is_set or
                        self.apn.is_set or
                        self.apn_name.is_set or
                        self.count.is_set or
                        self.customers.is_set or
                        self.ddp.is_set or
                        self.ddr.is_set or
                        self.ddt.is_set or
                        self.default_mn.is_set or
                        self.discover_mn.is_set or
                        self.domain.is_set or
                        self.learn_mag.is_set or
                        self.local_routing.is_set or
                        self.num_network.is_set or
                        self.peers.is_set or
                        self.profile.is_set or
                        self.role.is_set or
                        self.selfid.is_set or
                        self.service.is_set or
                        self.session_mgr.is_set or
                        (self.mll_service is not None and self.mll_service.has_data()) or
                        (self.parameters is not None and self.parameters.has_data()))

                def has_operation(self):
                    for c in self.cust:
                        if (c.has_operation()):
                            return True
                    for c in self.intf:
                        if (c.has_operation()):
                            return True
                    for c in self.network:
                        if (c.has_operation()):
                            return True
                    for c in self.peer:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.aaa_accounting.yfilter != YFilter.not_set or
                        self.apn.yfilter != YFilter.not_set or
                        self.apn_name.yfilter != YFilter.not_set or
                        self.count.yfilter != YFilter.not_set or
                        self.customers.yfilter != YFilter.not_set or
                        self.ddp.yfilter != YFilter.not_set or
                        self.ddr.yfilter != YFilter.not_set or
                        self.ddt.yfilter != YFilter.not_set or
                        self.default_mn.yfilter != YFilter.not_set or
                        self.discover_mn.yfilter != YFilter.not_set or
                        self.domain.yfilter != YFilter.not_set or
                        self.learn_mag.yfilter != YFilter.not_set or
                        self.local_routing.yfilter != YFilter.not_set or
                        self.num_network.yfilter != YFilter.not_set or
                        self.peers.yfilter != YFilter.not_set or
                        self.profile.yfilter != YFilter.not_set or
                        self.role.yfilter != YFilter.not_set or
                        self.selfid.yfilter != YFilter.not_set or
                        self.service.yfilter != YFilter.not_set or
                        self.session_mgr.yfilter != YFilter.not_set or
                        (self.mll_service is not None and self.mll_service.has_operation()) or
                        (self.parameters is not None and self.parameters.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "global-variables" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.aaa_accounting.is_set or self.aaa_accounting.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.aaa_accounting.get_name_leafdata())
                    if (self.apn.is_set or self.apn.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.apn.get_name_leafdata())
                    if (self.apn_name.is_set or self.apn_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.apn_name.get_name_leafdata())
                    if (self.count.is_set or self.count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.count.get_name_leafdata())
                    if (self.customers.is_set or self.customers.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.customers.get_name_leafdata())
                    if (self.ddp.is_set or self.ddp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ddp.get_name_leafdata())
                    if (self.ddr.is_set or self.ddr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ddr.get_name_leafdata())
                    if (self.ddt.is_set or self.ddt.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ddt.get_name_leafdata())
                    if (self.default_mn.is_set or self.default_mn.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.default_mn.get_name_leafdata())
                    if (self.discover_mn.is_set or self.discover_mn.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discover_mn.get_name_leafdata())
                    if (self.domain.is_set or self.domain.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.domain.get_name_leafdata())
                    if (self.learn_mag.is_set or self.learn_mag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.learn_mag.get_name_leafdata())
                    if (self.local_routing.is_set or self.local_routing.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.local_routing.get_name_leafdata())
                    if (self.num_network.is_set or self.num_network.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.num_network.get_name_leafdata())
                    if (self.peers.is_set or self.peers.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peers.get_name_leafdata())
                    if (self.profile.is_set or self.profile.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.profile.get_name_leafdata())
                    if (self.role.is_set or self.role.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.role.get_name_leafdata())
                    if (self.selfid.is_set or self.selfid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.selfid.get_name_leafdata())
                    if (self.service.is_set or self.service.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.service.get_name_leafdata())
                    if (self.session_mgr.is_set or self.session_mgr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.session_mgr.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "cust"):
                        for c in self.cust:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Pmipv6.Lma.ConfigVariables.GlobalVariables.Cust()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.cust.append(c)
                        return c

                    if (child_yang_name == "intf"):
                        for c in self.intf:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Pmipv6.Lma.ConfigVariables.GlobalVariables.Intf()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.intf.append(c)
                        return c

                    if (child_yang_name == "mll-service"):
                        if (self.mll_service is None):
                            self.mll_service = Pmipv6.Lma.ConfigVariables.GlobalVariables.MllService()
                            self.mll_service.parent = self
                            self._children_name_map["mll_service"] = "mll-service"
                        return self.mll_service

                    if (child_yang_name == "network"):
                        for c in self.network:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Pmipv6.Lma.ConfigVariables.GlobalVariables.Network()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.network.append(c)
                        return c

                    if (child_yang_name == "parameters"):
                        if (self.parameters is None):
                            self.parameters = Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters()
                            self.parameters.parent = self
                            self._children_name_map["parameters"] = "parameters"
                        return self.parameters

                    if (child_yang_name == "peer"):
                        for c in self.peer:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Pmipv6.Lma.ConfigVariables.GlobalVariables.Peer()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.peer.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "cust" or name == "intf" or name == "mll-service" or name == "network" or name == "parameters" or name == "peer" or name == "aaa-accounting" or name == "apn" or name == "apn-name" or name == "count" or name == "customers" or name == "ddp" or name == "ddr" or name == "ddt" or name == "default-mn" or name == "discover-mn" or name == "domain" or name == "learn-mag" or name == "local-routing" or name == "num-network" or name == "peers" or name == "profile" or name == "role" or name == "selfid" or name == "service" or name == "session-mgr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "aaa-accounting"):
                        self.aaa_accounting = value
                        self.aaa_accounting.value_namespace = name_space
                        self.aaa_accounting.value_namespace_prefix = name_space_prefix
                    if(value_path == "apn"):
                        self.apn = value
                        self.apn.value_namespace = name_space
                        self.apn.value_namespace_prefix = name_space_prefix
                    if(value_path == "apn-name"):
                        self.apn_name = value
                        self.apn_name.value_namespace = name_space
                        self.apn_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "count"):
                        self.count = value
                        self.count.value_namespace = name_space
                        self.count.value_namespace_prefix = name_space_prefix
                    if(value_path == "customers"):
                        self.customers = value
                        self.customers.value_namespace = name_space
                        self.customers.value_namespace_prefix = name_space_prefix
                    if(value_path == "ddp"):
                        self.ddp = value
                        self.ddp.value_namespace = name_space
                        self.ddp.value_namespace_prefix = name_space_prefix
                    if(value_path == "ddr"):
                        self.ddr = value
                        self.ddr.value_namespace = name_space
                        self.ddr.value_namespace_prefix = name_space_prefix
                    if(value_path == "ddt"):
                        self.ddt = value
                        self.ddt.value_namespace = name_space
                        self.ddt.value_namespace_prefix = name_space_prefix
                    if(value_path == "default-mn"):
                        self.default_mn = value
                        self.default_mn.value_namespace = name_space
                        self.default_mn.value_namespace_prefix = name_space_prefix
                    if(value_path == "discover-mn"):
                        self.discover_mn = value
                        self.discover_mn.value_namespace = name_space
                        self.discover_mn.value_namespace_prefix = name_space_prefix
                    if(value_path == "domain"):
                        self.domain = value
                        self.domain.value_namespace = name_space
                        self.domain.value_namespace_prefix = name_space_prefix
                    if(value_path == "learn-mag"):
                        self.learn_mag = value
                        self.learn_mag.value_namespace = name_space
                        self.learn_mag.value_namespace_prefix = name_space_prefix
                    if(value_path == "local-routing"):
                        self.local_routing = value
                        self.local_routing.value_namespace = name_space
                        self.local_routing.value_namespace_prefix = name_space_prefix
                    if(value_path == "num-network"):
                        self.num_network = value
                        self.num_network.value_namespace = name_space
                        self.num_network.value_namespace_prefix = name_space_prefix
                    if(value_path == "peers"):
                        self.peers = value
                        self.peers.value_namespace = name_space
                        self.peers.value_namespace_prefix = name_space_prefix
                    if(value_path == "profile"):
                        self.profile = value
                        self.profile.value_namespace = name_space
                        self.profile.value_namespace_prefix = name_space_prefix
                    if(value_path == "role"):
                        self.role = value
                        self.role.value_namespace = name_space
                        self.role.value_namespace_prefix = name_space_prefix
                    if(value_path == "selfid"):
                        self.selfid = value
                        self.selfid.value_namespace = name_space
                        self.selfid.value_namespace_prefix = name_space_prefix
                    if(value_path == "service"):
                        self.service = value
                        self.service.value_namespace = name_space
                        self.service.value_namespace_prefix = name_space_prefix
                    if(value_path == "session-mgr"):
                        self.session_mgr = value
                        self.session_mgr.value_namespace = name_space
                        self.session_mgr.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.customer_variables is not None and self.customer_variables.has_data()) or
                    (self.global_variables is not None and self.global_variables.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.customer_variables is not None and self.customer_variables.has_operation()) or
                    (self.global_variables is not None and self.global_variables.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "config-variables" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "customer-variables"):
                    if (self.customer_variables is None):
                        self.customer_variables = Pmipv6.Lma.ConfigVariables.CustomerVariables()
                        self.customer_variables.parent = self
                        self._children_name_map["customer_variables"] = "customer-variables"
                    return self.customer_variables

                if (child_yang_name == "global-variables"):
                    if (self.global_variables is None):
                        self.global_variables = Pmipv6.Lma.ConfigVariables.GlobalVariables()
                        self.global_variables.parent = self
                        self._children_name_map["global_variables"] = "global-variables"
                    return self.global_variables

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "customer-variables" or name == "global-variables"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.bindings is not None and self.bindings.has_data()) or
                (self.config_variables is not None and self.config_variables.has_data()) or
                (self.heartbeats is not None and self.heartbeats.has_data()) or
                (self.statistics is not None and self.statistics.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.bindings is not None and self.bindings.has_operation()) or
                (self.config_variables is not None and self.config_variables.has_operation()) or
                (self.heartbeats is not None and self.heartbeats.has_operation()) or
                (self.statistics is not None and self.statistics.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "lma" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "bindings"):
                if (self.bindings is None):
                    self.bindings = Pmipv6.Lma.Bindings()
                    self.bindings.parent = self
                    self._children_name_map["bindings"] = "bindings"
                return self.bindings

            if (child_yang_name == "config-variables"):
                if (self.config_variables is None):
                    self.config_variables = Pmipv6.Lma.ConfigVariables()
                    self.config_variables.parent = self
                    self._children_name_map["config_variables"] = "config-variables"
                return self.config_variables

            if (child_yang_name == "heartbeats"):
                if (self.heartbeats is None):
                    self.heartbeats = Pmipv6.Lma.Heartbeats()
                    self.heartbeats.parent = self
                    self._children_name_map["heartbeats"] = "heartbeats"
                return self.heartbeats

            if (child_yang_name == "statistics"):
                if (self.statistics is None):
                    self.statistics = Pmipv6.Lma.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                return self.statistics

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bindings" or name == "config-variables" or name == "heartbeats" or name == "statistics"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.lma is not None and self.lma.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.lma is not None and self.lma.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-mobileip-oper:pmipv6" + path_buffer

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

        if (child_yang_name == "lma"):
            if (self.lma is None):
                self.lma = Pmipv6.Lma()
                self.lma.parent = self
                self._children_name_map["lma"] = "lma"
            return self.lma

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "lma"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Pmipv6()
        return self._top_entity

