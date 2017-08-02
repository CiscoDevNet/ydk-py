""" Cisco_IOS_XR_subscriber_pppoe_ma_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-pppoe\-ma package operational data.

This module contains definitions
for the following management objects\:
  pppoe\: PPPoE operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class PppoeMaLimitState(Enum):
    """
    PppoeMaLimitState

    Pppoe ma limit state

    .. data:: ok = 0

    	OK State

    .. data:: warning = 1

    	Warn State

    .. data:: block = 2

    	Block State

    """

    ok = Enum.YLeaf(0, "ok")

    warning = Enum.YLeaf(1, "warning")

    block = Enum.YLeaf(2, "block")


class PppoeMaSessionIdbSrgState(Enum):
    """
    PppoeMaSessionIdbSrgState

    Pppoe ma session idb srg state

    .. data:: none = 0

    	SRG-None state

    .. data:: active = 1

    	SRG-Active state

    .. data:: standby = 2

    	SRG-Standby state

    """

    none = Enum.YLeaf(0, "none")

    active = Enum.YLeaf(1, "active")

    standby = Enum.YLeaf(2, "standby")


class PppoeMaThrottleState(Enum):
    """
    PppoeMaThrottleState

    Pppoe ma throttle state

    .. data:: idle = 0

    	Idle State

    .. data:: monitor = 1

    	Monitor State

    .. data:: block = 2

    	Block State

    """

    idle = Enum.YLeaf(0, "idle")

    monitor = Enum.YLeaf(1, "monitor")

    block = Enum.YLeaf(2, "block")



class Pppoe(Entity):
    """
    PPPoE operational data
    
    .. attribute:: access_interface_statistics
    
    	PPPoE access interface statistics information
    	**type**\:   :py:class:`AccessInterfaceStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics>`
    
    .. attribute:: nodes
    
    	Per\-node PPPoE operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes>`
    
    

    """

    _prefix = 'subscriber-pppoe-ma-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Pppoe, self).__init__()
        self._top_entity = None

        self.yang_name = "pppoe"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-pppoe-ma-oper"

        self.access_interface_statistics = Pppoe.AccessInterfaceStatistics()
        self.access_interface_statistics.parent = self
        self._children_name_map["access_interface_statistics"] = "access-interface-statistics"
        self._children_yang_names.add("access-interface-statistics")

        self.nodes = Pppoe.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class AccessInterfaceStatistics(Entity):
        """
        PPPoE access interface statistics information
        
        .. attribute:: access_interface_statistic
        
        	Statistics information for a PPPoE\-enabled access interface
        	**type**\: list of    :py:class:`AccessInterfaceStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic>`
        
        

        """

        _prefix = 'subscriber-pppoe-ma-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Pppoe.AccessInterfaceStatistics, self).__init__()

            self.yang_name = "access-interface-statistics"
            self.yang_parent_name = "pppoe"

            self.access_interface_statistic = YList(self)

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
                        super(Pppoe.AccessInterfaceStatistics, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Pppoe.AccessInterfaceStatistics, self).__setattr__(name, value)


        class AccessInterfaceStatistic(Entity):
            """
            Statistics information for a PPPoE\-enabled
            access interface
            
            .. attribute:: interface_name  <key>
            
            	PPPoE Access Interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: packet_counts
            
            	Packet Counts
            	**type**\:   :py:class:`PacketCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts>`
            
            

            """

            _prefix = 'subscriber-pppoe-ma-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic, self).__init__()

                self.yang_name = "access-interface-statistic"
                self.yang_parent_name = "access-interface-statistics"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.packet_counts = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts()
                self.packet_counts.parent = self
                self._children_name_map["packet_counts"] = "packet-counts"
                self._children_yang_names.add("packet-counts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic, self).__setattr__(name, value)


            class PacketCounts(Entity):
                """
                Packet Counts
                
                .. attribute:: other
                
                	Other counts
                	**type**\:   :py:class:`Other <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other>`
                
                .. attribute:: padi
                
                	PADI counts
                	**type**\:   :py:class:`Padi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi>`
                
                .. attribute:: pado
                
                	PADO counts
                	**type**\:   :py:class:`Pado <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado>`
                
                .. attribute:: padr
                
                	PADR counts
                	**type**\:   :py:class:`Padr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr>`
                
                .. attribute:: pads_error
                
                	PADS Error counts
                	**type**\:   :py:class:`PadsError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError>`
                
                .. attribute:: pads_success
                
                	PADS Success counts
                	**type**\:   :py:class:`PadsSuccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess>`
                
                .. attribute:: padt
                
                	PADT counts
                	**type**\:   :py:class:`Padt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt>`
                
                .. attribute:: session_state
                
                	Session Stage counts
                	**type**\:   :py:class:`SessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts, self).__init__()

                    self.yang_name = "packet-counts"
                    self.yang_parent_name = "access-interface-statistic"

                    self.other = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other()
                    self.other.parent = self
                    self._children_name_map["other"] = "other"
                    self._children_yang_names.add("other")

                    self.padi = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi()
                    self.padi.parent = self
                    self._children_name_map["padi"] = "padi"
                    self._children_yang_names.add("padi")

                    self.pado = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado()
                    self.pado.parent = self
                    self._children_name_map["pado"] = "pado"
                    self._children_yang_names.add("pado")

                    self.padr = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr()
                    self.padr.parent = self
                    self._children_name_map["padr"] = "padr"
                    self._children_yang_names.add("padr")

                    self.pads_error = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError()
                    self.pads_error.parent = self
                    self._children_name_map["pads_error"] = "pads-error"
                    self._children_yang_names.add("pads-error")

                    self.pads_success = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess()
                    self.pads_success.parent = self
                    self._children_name_map["pads_success"] = "pads-success"
                    self._children_yang_names.add("pads-success")

                    self.padt = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt()
                    self.padt.parent = self
                    self._children_name_map["padt"] = "padt"
                    self._children_yang_names.add("padt")

                    self.session_state = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState()
                    self.session_state.parent = self
                    self._children_name_map["session_state"] = "session-state"
                    self._children_yang_names.add("session-state")


                class Padi(Entity):
                    """
                    PADI counts
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi, self).__init__()

                        self.yang_name = "padi"
                        self.yang_parent_name = "packet-counts"

                        self.dropped = YLeaf(YType.uint32, "dropped")

                        self.received = YLeaf(YType.uint32, "received")

                        self.sent = YLeaf(YType.uint32, "sent")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dropped",
                                        "received",
                                        "sent") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.dropped.is_set or
                            self.received.is_set or
                            self.sent.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dropped.yfilter != YFilter.not_set or
                            self.received.yfilter != YFilter.not_set or
                            self.sent.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "padi" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dropped.get_name_leafdata())
                        if (self.received.is_set or self.received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received.get_name_leafdata())
                        if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sent.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dropped" or name == "received" or name == "sent"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dropped"):
                            self.dropped = value
                            self.dropped.value_namespace = name_space
                            self.dropped.value_namespace_prefix = name_space_prefix
                        if(value_path == "received"):
                            self.received = value
                            self.received.value_namespace = name_space
                            self.received.value_namespace_prefix = name_space_prefix
                        if(value_path == "sent"):
                            self.sent = value
                            self.sent.value_namespace = name_space
                            self.sent.value_namespace_prefix = name_space_prefix


                class Pado(Entity):
                    """
                    PADO counts
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado, self).__init__()

                        self.yang_name = "pado"
                        self.yang_parent_name = "packet-counts"

                        self.dropped = YLeaf(YType.uint32, "dropped")

                        self.received = YLeaf(YType.uint32, "received")

                        self.sent = YLeaf(YType.uint32, "sent")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dropped",
                                        "received",
                                        "sent") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.dropped.is_set or
                            self.received.is_set or
                            self.sent.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dropped.yfilter != YFilter.not_set or
                            self.received.yfilter != YFilter.not_set or
                            self.sent.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pado" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dropped.get_name_leafdata())
                        if (self.received.is_set or self.received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received.get_name_leafdata())
                        if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sent.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dropped" or name == "received" or name == "sent"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dropped"):
                            self.dropped = value
                            self.dropped.value_namespace = name_space
                            self.dropped.value_namespace_prefix = name_space_prefix
                        if(value_path == "received"):
                            self.received = value
                            self.received.value_namespace = name_space
                            self.received.value_namespace_prefix = name_space_prefix
                        if(value_path == "sent"):
                            self.sent = value
                            self.sent.value_namespace = name_space
                            self.sent.value_namespace_prefix = name_space_prefix


                class Padr(Entity):
                    """
                    PADR counts
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr, self).__init__()

                        self.yang_name = "padr"
                        self.yang_parent_name = "packet-counts"

                        self.dropped = YLeaf(YType.uint32, "dropped")

                        self.received = YLeaf(YType.uint32, "received")

                        self.sent = YLeaf(YType.uint32, "sent")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dropped",
                                        "received",
                                        "sent") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.dropped.is_set or
                            self.received.is_set or
                            self.sent.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dropped.yfilter != YFilter.not_set or
                            self.received.yfilter != YFilter.not_set or
                            self.sent.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "padr" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dropped.get_name_leafdata())
                        if (self.received.is_set or self.received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received.get_name_leafdata())
                        if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sent.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dropped" or name == "received" or name == "sent"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dropped"):
                            self.dropped = value
                            self.dropped.value_namespace = name_space
                            self.dropped.value_namespace_prefix = name_space_prefix
                        if(value_path == "received"):
                            self.received = value
                            self.received.value_namespace = name_space
                            self.received.value_namespace_prefix = name_space_prefix
                        if(value_path == "sent"):
                            self.sent = value
                            self.sent.value_namespace = name_space
                            self.sent.value_namespace_prefix = name_space_prefix


                class PadsSuccess(Entity):
                    """
                    PADS Success counts
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess, self).__init__()

                        self.yang_name = "pads-success"
                        self.yang_parent_name = "packet-counts"

                        self.dropped = YLeaf(YType.uint32, "dropped")

                        self.received = YLeaf(YType.uint32, "received")

                        self.sent = YLeaf(YType.uint32, "sent")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dropped",
                                        "received",
                                        "sent") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.dropped.is_set or
                            self.received.is_set or
                            self.sent.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dropped.yfilter != YFilter.not_set or
                            self.received.yfilter != YFilter.not_set or
                            self.sent.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pads-success" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dropped.get_name_leafdata())
                        if (self.received.is_set or self.received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received.get_name_leafdata())
                        if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sent.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dropped" or name == "received" or name == "sent"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dropped"):
                            self.dropped = value
                            self.dropped.value_namespace = name_space
                            self.dropped.value_namespace_prefix = name_space_prefix
                        if(value_path == "received"):
                            self.received = value
                            self.received.value_namespace = name_space
                            self.received.value_namespace_prefix = name_space_prefix
                        if(value_path == "sent"):
                            self.sent = value
                            self.sent.value_namespace = name_space
                            self.sent.value_namespace_prefix = name_space_prefix


                class PadsError(Entity):
                    """
                    PADS Error counts
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError, self).__init__()

                        self.yang_name = "pads-error"
                        self.yang_parent_name = "packet-counts"

                        self.dropped = YLeaf(YType.uint32, "dropped")

                        self.received = YLeaf(YType.uint32, "received")

                        self.sent = YLeaf(YType.uint32, "sent")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dropped",
                                        "received",
                                        "sent") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.dropped.is_set or
                            self.received.is_set or
                            self.sent.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dropped.yfilter != YFilter.not_set or
                            self.received.yfilter != YFilter.not_set or
                            self.sent.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pads-error" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dropped.get_name_leafdata())
                        if (self.received.is_set or self.received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received.get_name_leafdata())
                        if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sent.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dropped" or name == "received" or name == "sent"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dropped"):
                            self.dropped = value
                            self.dropped.value_namespace = name_space
                            self.dropped.value_namespace_prefix = name_space_prefix
                        if(value_path == "received"):
                            self.received = value
                            self.received.value_namespace = name_space
                            self.received.value_namespace_prefix = name_space_prefix
                        if(value_path == "sent"):
                            self.sent = value
                            self.sent.value_namespace = name_space
                            self.sent.value_namespace_prefix = name_space_prefix


                class Padt(Entity):
                    """
                    PADT counts
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt, self).__init__()

                        self.yang_name = "padt"
                        self.yang_parent_name = "packet-counts"

                        self.dropped = YLeaf(YType.uint32, "dropped")

                        self.received = YLeaf(YType.uint32, "received")

                        self.sent = YLeaf(YType.uint32, "sent")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dropped",
                                        "received",
                                        "sent") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.dropped.is_set or
                            self.received.is_set or
                            self.sent.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dropped.yfilter != YFilter.not_set or
                            self.received.yfilter != YFilter.not_set or
                            self.sent.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "padt" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dropped.get_name_leafdata())
                        if (self.received.is_set or self.received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received.get_name_leafdata())
                        if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sent.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dropped" or name == "received" or name == "sent"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dropped"):
                            self.dropped = value
                            self.dropped.value_namespace = name_space
                            self.dropped.value_namespace_prefix = name_space_prefix
                        if(value_path == "received"):
                            self.received = value
                            self.received.value_namespace = name_space
                            self.received.value_namespace_prefix = name_space_prefix
                        if(value_path == "sent"):
                            self.sent = value
                            self.sent.value_namespace = name_space
                            self.sent.value_namespace_prefix = name_space_prefix


                class SessionState(Entity):
                    """
                    Session Stage counts
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState, self).__init__()

                        self.yang_name = "session-state"
                        self.yang_parent_name = "packet-counts"

                        self.dropped = YLeaf(YType.uint32, "dropped")

                        self.received = YLeaf(YType.uint32, "received")

                        self.sent = YLeaf(YType.uint32, "sent")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dropped",
                                        "received",
                                        "sent") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.dropped.is_set or
                            self.received.is_set or
                            self.sent.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dropped.yfilter != YFilter.not_set or
                            self.received.yfilter != YFilter.not_set or
                            self.sent.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session-state" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dropped.get_name_leafdata())
                        if (self.received.is_set or self.received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received.get_name_leafdata())
                        if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sent.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dropped" or name == "received" or name == "sent"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dropped"):
                            self.dropped = value
                            self.dropped.value_namespace = name_space
                            self.dropped.value_namespace_prefix = name_space_prefix
                        if(value_path == "received"):
                            self.received = value
                            self.received.value_namespace = name_space
                            self.received.value_namespace_prefix = name_space_prefix
                        if(value_path == "sent"):
                            self.sent = value
                            self.sent.value_namespace = name_space
                            self.sent.value_namespace_prefix = name_space_prefix


                class Other(Entity):
                    """
                    Other counts
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other, self).__init__()

                        self.yang_name = "other"
                        self.yang_parent_name = "packet-counts"

                        self.dropped = YLeaf(YType.uint32, "dropped")

                        self.received = YLeaf(YType.uint32, "received")

                        self.sent = YLeaf(YType.uint32, "sent")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dropped",
                                        "received",
                                        "sent") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.dropped.is_set or
                            self.received.is_set or
                            self.sent.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dropped.yfilter != YFilter.not_set or
                            self.received.yfilter != YFilter.not_set or
                            self.sent.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "other" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dropped.get_name_leafdata())
                        if (self.received.is_set or self.received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received.get_name_leafdata())
                        if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sent.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dropped" or name == "received" or name == "sent"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dropped"):
                            self.dropped = value
                            self.dropped.value_namespace = name_space
                            self.dropped.value_namespace_prefix = name_space_prefix
                        if(value_path == "received"):
                            self.received = value
                            self.received.value_namespace = name_space
                            self.received.value_namespace_prefix = name_space_prefix
                        if(value_path == "sent"):
                            self.sent = value
                            self.sent.value_namespace = name_space
                            self.sent.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.other is not None and self.other.has_data()) or
                        (self.padi is not None and self.padi.has_data()) or
                        (self.pado is not None and self.pado.has_data()) or
                        (self.padr is not None and self.padr.has_data()) or
                        (self.pads_error is not None and self.pads_error.has_data()) or
                        (self.pads_success is not None and self.pads_success.has_data()) or
                        (self.padt is not None and self.padt.has_data()) or
                        (self.session_state is not None and self.session_state.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.other is not None and self.other.has_operation()) or
                        (self.padi is not None and self.padi.has_operation()) or
                        (self.pado is not None and self.pado.has_operation()) or
                        (self.padr is not None and self.padr.has_operation()) or
                        (self.pads_error is not None and self.pads_error.has_operation()) or
                        (self.pads_success is not None and self.pads_success.has_operation()) or
                        (self.padt is not None and self.padt.has_operation()) or
                        (self.session_state is not None and self.session_state.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "packet-counts" + path_buffer

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

                    if (child_yang_name == "other"):
                        if (self.other is None):
                            self.other = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other()
                            self.other.parent = self
                            self._children_name_map["other"] = "other"
                        return self.other

                    if (child_yang_name == "padi"):
                        if (self.padi is None):
                            self.padi = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi()
                            self.padi.parent = self
                            self._children_name_map["padi"] = "padi"
                        return self.padi

                    if (child_yang_name == "pado"):
                        if (self.pado is None):
                            self.pado = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado()
                            self.pado.parent = self
                            self._children_name_map["pado"] = "pado"
                        return self.pado

                    if (child_yang_name == "padr"):
                        if (self.padr is None):
                            self.padr = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr()
                            self.padr.parent = self
                            self._children_name_map["padr"] = "padr"
                        return self.padr

                    if (child_yang_name == "pads-error"):
                        if (self.pads_error is None):
                            self.pads_error = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError()
                            self.pads_error.parent = self
                            self._children_name_map["pads_error"] = "pads-error"
                        return self.pads_error

                    if (child_yang_name == "pads-success"):
                        if (self.pads_success is None):
                            self.pads_success = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess()
                            self.pads_success.parent = self
                            self._children_name_map["pads_success"] = "pads-success"
                        return self.pads_success

                    if (child_yang_name == "padt"):
                        if (self.padt is None):
                            self.padt = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt()
                            self.padt.parent = self
                            self._children_name_map["padt"] = "padt"
                        return self.padt

                    if (child_yang_name == "session-state"):
                        if (self.session_state is None):
                            self.session_state = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState()
                            self.session_state.parent = self
                            self._children_name_map["session_state"] = "session-state"
                        return self.session_state

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "other" or name == "padi" or name == "pado" or name == "padr" or name == "pads-error" or name == "pads-success" or name == "padt" or name == "session-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.interface_name.is_set or
                    (self.packet_counts is not None and self.packet_counts.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    (self.packet_counts is not None and self.packet_counts.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "access-interface-statistic" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe/access-interface-statistics/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "packet-counts"):
                    if (self.packet_counts is None):
                        self.packet_counts = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts()
                        self.packet_counts.parent = self
                        self._children_name_map["packet_counts"] = "packet-counts"
                    return self.packet_counts

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "packet-counts" or name == "interface-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.access_interface_statistic:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.access_interface_statistic:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "access-interface-statistics" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "access-interface-statistic"):
                for c in self.access_interface_statistic:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.access_interface_statistic.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "access-interface-statistic"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Nodes(Entity):
        """
        Per\-node PPPoE operational data
        
        .. attribute:: node
        
        	PPPoE operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node>`
        
        

        """

        _prefix = 'subscriber-pppoe-ma-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Pppoe.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "pppoe"

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
                        super(Pppoe.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Pppoe.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            PPPoE operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: access_interface
            
            	PPPoE access interface information
            	**type**\:   :py:class:`AccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.AccessInterface>`
            
            .. attribute:: bba_groups
            
            	PPPoE BBA\-Group information
            	**type**\:   :py:class:`BbaGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups>`
            
            .. attribute:: interfaces
            
            	Per interface PPPoE operational data
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Interfaces>`
            
            .. attribute:: statistics
            
            	PPPoE statistics for a given node
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics>`
            
            .. attribute:: summary_total
            
            	PPPoE statistics for a given node
            	**type**\:   :py:class:`SummaryTotal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.SummaryTotal>`
            
            

            """

            _prefix = 'subscriber-pppoe-ma-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Pppoe.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.access_interface = Pppoe.Nodes.Node.AccessInterface()
                self.access_interface.parent = self
                self._children_name_map["access_interface"] = "access-interface"
                self._children_yang_names.add("access-interface")

                self.bba_groups = Pppoe.Nodes.Node.BbaGroups()
                self.bba_groups.parent = self
                self._children_name_map["bba_groups"] = "bba-groups"
                self._children_yang_names.add("bba-groups")

                self.interfaces = Pppoe.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.statistics = Pppoe.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")

                self.summary_total = Pppoe.Nodes.Node.SummaryTotal()
                self.summary_total.parent = self
                self._children_name_map["summary_total"] = "summary-total"
                self._children_yang_names.add("summary-total")

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
                            super(Pppoe.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Pppoe.Nodes.Node, self).__setattr__(name, value)


            class Statistics(Entity):
                """
                PPPoE statistics for a given node
                
                .. attribute:: packet_counts
                
                	Packet Counts
                	**type**\:   :py:class:`PacketCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts>`
                
                .. attribute:: packet_error_counts
                
                	Packet Error Counts
                	**type**\:   :py:class:`PacketErrorCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketErrorCounts>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Pppoe.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"

                    self.packet_counts = Pppoe.Nodes.Node.Statistics.PacketCounts()
                    self.packet_counts.parent = self
                    self._children_name_map["packet_counts"] = "packet-counts"
                    self._children_yang_names.add("packet-counts")

                    self.packet_error_counts = Pppoe.Nodes.Node.Statistics.PacketErrorCounts()
                    self.packet_error_counts.parent = self
                    self._children_name_map["packet_error_counts"] = "packet-error-counts"
                    self._children_yang_names.add("packet-error-counts")


                class PacketCounts(Entity):
                    """
                    Packet Counts
                    
                    .. attribute:: other
                    
                    	Other counts
                    	**type**\:   :py:class:`Other <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Other>`
                    
                    .. attribute:: padi
                    
                    	PADI counts
                    	**type**\:   :py:class:`Padi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Padi>`
                    
                    .. attribute:: pado
                    
                    	PADO counts
                    	**type**\:   :py:class:`Pado <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Pado>`
                    
                    .. attribute:: padr
                    
                    	PADR counts
                    	**type**\:   :py:class:`Padr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Padr>`
                    
                    .. attribute:: pads_error
                    
                    	PADS Error counts
                    	**type**\:   :py:class:`PadsError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError>`
                    
                    .. attribute:: pads_success
                    
                    	PADS Success counts
                    	**type**\:   :py:class:`PadsSuccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess>`
                    
                    .. attribute:: padt
                    
                    	PADT counts
                    	**type**\:   :py:class:`Padt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Padt>`
                    
                    .. attribute:: session_state
                    
                    	Session Stage counts
                    	**type**\:   :py:class:`SessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.Nodes.Node.Statistics.PacketCounts, self).__init__()

                        self.yang_name = "packet-counts"
                        self.yang_parent_name = "statistics"

                        self.other = Pppoe.Nodes.Node.Statistics.PacketCounts.Other()
                        self.other.parent = self
                        self._children_name_map["other"] = "other"
                        self._children_yang_names.add("other")

                        self.padi = Pppoe.Nodes.Node.Statistics.PacketCounts.Padi()
                        self.padi.parent = self
                        self._children_name_map["padi"] = "padi"
                        self._children_yang_names.add("padi")

                        self.pado = Pppoe.Nodes.Node.Statistics.PacketCounts.Pado()
                        self.pado.parent = self
                        self._children_name_map["pado"] = "pado"
                        self._children_yang_names.add("pado")

                        self.padr = Pppoe.Nodes.Node.Statistics.PacketCounts.Padr()
                        self.padr.parent = self
                        self._children_name_map["padr"] = "padr"
                        self._children_yang_names.add("padr")

                        self.pads_error = Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError()
                        self.pads_error.parent = self
                        self._children_name_map["pads_error"] = "pads-error"
                        self._children_yang_names.add("pads-error")

                        self.pads_success = Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess()
                        self.pads_success.parent = self
                        self._children_name_map["pads_success"] = "pads-success"
                        self._children_yang_names.add("pads-success")

                        self.padt = Pppoe.Nodes.Node.Statistics.PacketCounts.Padt()
                        self.padt.parent = self
                        self._children_name_map["padt"] = "padt"
                        self._children_yang_names.add("padt")

                        self.session_state = Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState()
                        self.session_state.parent = self
                        self._children_name_map["session_state"] = "session-state"
                        self._children_yang_names.add("session-state")


                    class Padi(Entity):
                        """
                        PADI counts
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Statistics.PacketCounts.Padi, self).__init__()

                            self.yang_name = "padi"
                            self.yang_parent_name = "packet-counts"

                            self.dropped = YLeaf(YType.uint32, "dropped")

                            self.received = YLeaf(YType.uint32, "received")

                            self.sent = YLeaf(YType.uint32, "sent")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("dropped",
                                            "received",
                                            "sent") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pppoe.Nodes.Node.Statistics.PacketCounts.Padi, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pppoe.Nodes.Node.Statistics.PacketCounts.Padi, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.dropped.is_set or
                                self.received.is_set or
                                self.sent.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dropped.yfilter != YFilter.not_set or
                                self.received.yfilter != YFilter.not_set or
                                self.sent.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "padi" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped.get_name_leafdata())
                            if (self.received.is_set or self.received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received.get_name_leafdata())
                            if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dropped" or name == "received" or name == "sent"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "dropped"):
                                self.dropped = value
                                self.dropped.value_namespace = name_space
                                self.dropped.value_namespace_prefix = name_space_prefix
                            if(value_path == "received"):
                                self.received = value
                                self.received.value_namespace = name_space
                                self.received.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent"):
                                self.sent = value
                                self.sent.value_namespace = name_space
                                self.sent.value_namespace_prefix = name_space_prefix


                    class Pado(Entity):
                        """
                        PADO counts
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Statistics.PacketCounts.Pado, self).__init__()

                            self.yang_name = "pado"
                            self.yang_parent_name = "packet-counts"

                            self.dropped = YLeaf(YType.uint32, "dropped")

                            self.received = YLeaf(YType.uint32, "received")

                            self.sent = YLeaf(YType.uint32, "sent")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("dropped",
                                            "received",
                                            "sent") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pppoe.Nodes.Node.Statistics.PacketCounts.Pado, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pppoe.Nodes.Node.Statistics.PacketCounts.Pado, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.dropped.is_set or
                                self.received.is_set or
                                self.sent.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dropped.yfilter != YFilter.not_set or
                                self.received.yfilter != YFilter.not_set or
                                self.sent.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pado" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped.get_name_leafdata())
                            if (self.received.is_set or self.received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received.get_name_leafdata())
                            if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dropped" or name == "received" or name == "sent"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "dropped"):
                                self.dropped = value
                                self.dropped.value_namespace = name_space
                                self.dropped.value_namespace_prefix = name_space_prefix
                            if(value_path == "received"):
                                self.received = value
                                self.received.value_namespace = name_space
                                self.received.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent"):
                                self.sent = value
                                self.sent.value_namespace = name_space
                                self.sent.value_namespace_prefix = name_space_prefix


                    class Padr(Entity):
                        """
                        PADR counts
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Statistics.PacketCounts.Padr, self).__init__()

                            self.yang_name = "padr"
                            self.yang_parent_name = "packet-counts"

                            self.dropped = YLeaf(YType.uint32, "dropped")

                            self.received = YLeaf(YType.uint32, "received")

                            self.sent = YLeaf(YType.uint32, "sent")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("dropped",
                                            "received",
                                            "sent") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pppoe.Nodes.Node.Statistics.PacketCounts.Padr, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pppoe.Nodes.Node.Statistics.PacketCounts.Padr, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.dropped.is_set or
                                self.received.is_set or
                                self.sent.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dropped.yfilter != YFilter.not_set or
                                self.received.yfilter != YFilter.not_set or
                                self.sent.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "padr" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped.get_name_leafdata())
                            if (self.received.is_set or self.received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received.get_name_leafdata())
                            if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dropped" or name == "received" or name == "sent"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "dropped"):
                                self.dropped = value
                                self.dropped.value_namespace = name_space
                                self.dropped.value_namespace_prefix = name_space_prefix
                            if(value_path == "received"):
                                self.received = value
                                self.received.value_namespace = name_space
                                self.received.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent"):
                                self.sent = value
                                self.sent.value_namespace = name_space
                                self.sent.value_namespace_prefix = name_space_prefix


                    class PadsSuccess(Entity):
                        """
                        PADS Success counts
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess, self).__init__()

                            self.yang_name = "pads-success"
                            self.yang_parent_name = "packet-counts"

                            self.dropped = YLeaf(YType.uint32, "dropped")

                            self.received = YLeaf(YType.uint32, "received")

                            self.sent = YLeaf(YType.uint32, "sent")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("dropped",
                                            "received",
                                            "sent") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.dropped.is_set or
                                self.received.is_set or
                                self.sent.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dropped.yfilter != YFilter.not_set or
                                self.received.yfilter != YFilter.not_set or
                                self.sent.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pads-success" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped.get_name_leafdata())
                            if (self.received.is_set or self.received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received.get_name_leafdata())
                            if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dropped" or name == "received" or name == "sent"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "dropped"):
                                self.dropped = value
                                self.dropped.value_namespace = name_space
                                self.dropped.value_namespace_prefix = name_space_prefix
                            if(value_path == "received"):
                                self.received = value
                                self.received.value_namespace = name_space
                                self.received.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent"):
                                self.sent = value
                                self.sent.value_namespace = name_space
                                self.sent.value_namespace_prefix = name_space_prefix


                    class PadsError(Entity):
                        """
                        PADS Error counts
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError, self).__init__()

                            self.yang_name = "pads-error"
                            self.yang_parent_name = "packet-counts"

                            self.dropped = YLeaf(YType.uint32, "dropped")

                            self.received = YLeaf(YType.uint32, "received")

                            self.sent = YLeaf(YType.uint32, "sent")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("dropped",
                                            "received",
                                            "sent") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.dropped.is_set or
                                self.received.is_set or
                                self.sent.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dropped.yfilter != YFilter.not_set or
                                self.received.yfilter != YFilter.not_set or
                                self.sent.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pads-error" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped.get_name_leafdata())
                            if (self.received.is_set or self.received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received.get_name_leafdata())
                            if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dropped" or name == "received" or name == "sent"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "dropped"):
                                self.dropped = value
                                self.dropped.value_namespace = name_space
                                self.dropped.value_namespace_prefix = name_space_prefix
                            if(value_path == "received"):
                                self.received = value
                                self.received.value_namespace = name_space
                                self.received.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent"):
                                self.sent = value
                                self.sent.value_namespace = name_space
                                self.sent.value_namespace_prefix = name_space_prefix


                    class Padt(Entity):
                        """
                        PADT counts
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Statistics.PacketCounts.Padt, self).__init__()

                            self.yang_name = "padt"
                            self.yang_parent_name = "packet-counts"

                            self.dropped = YLeaf(YType.uint32, "dropped")

                            self.received = YLeaf(YType.uint32, "received")

                            self.sent = YLeaf(YType.uint32, "sent")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("dropped",
                                            "received",
                                            "sent") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pppoe.Nodes.Node.Statistics.PacketCounts.Padt, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pppoe.Nodes.Node.Statistics.PacketCounts.Padt, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.dropped.is_set or
                                self.received.is_set or
                                self.sent.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dropped.yfilter != YFilter.not_set or
                                self.received.yfilter != YFilter.not_set or
                                self.sent.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "padt" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped.get_name_leafdata())
                            if (self.received.is_set or self.received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received.get_name_leafdata())
                            if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dropped" or name == "received" or name == "sent"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "dropped"):
                                self.dropped = value
                                self.dropped.value_namespace = name_space
                                self.dropped.value_namespace_prefix = name_space_prefix
                            if(value_path == "received"):
                                self.received = value
                                self.received.value_namespace = name_space
                                self.received.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent"):
                                self.sent = value
                                self.sent.value_namespace = name_space
                                self.sent.value_namespace_prefix = name_space_prefix


                    class SessionState(Entity):
                        """
                        Session Stage counts
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState, self).__init__()

                            self.yang_name = "session-state"
                            self.yang_parent_name = "packet-counts"

                            self.dropped = YLeaf(YType.uint32, "dropped")

                            self.received = YLeaf(YType.uint32, "received")

                            self.sent = YLeaf(YType.uint32, "sent")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("dropped",
                                            "received",
                                            "sent") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.dropped.is_set or
                                self.received.is_set or
                                self.sent.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dropped.yfilter != YFilter.not_set or
                                self.received.yfilter != YFilter.not_set or
                                self.sent.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "session-state" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped.get_name_leafdata())
                            if (self.received.is_set or self.received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received.get_name_leafdata())
                            if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dropped" or name == "received" or name == "sent"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "dropped"):
                                self.dropped = value
                                self.dropped.value_namespace = name_space
                                self.dropped.value_namespace_prefix = name_space_prefix
                            if(value_path == "received"):
                                self.received = value
                                self.received.value_namespace = name_space
                                self.received.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent"):
                                self.sent = value
                                self.sent.value_namespace = name_space
                                self.sent.value_namespace_prefix = name_space_prefix


                    class Other(Entity):
                        """
                        Other counts
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Statistics.PacketCounts.Other, self).__init__()

                            self.yang_name = "other"
                            self.yang_parent_name = "packet-counts"

                            self.dropped = YLeaf(YType.uint32, "dropped")

                            self.received = YLeaf(YType.uint32, "received")

                            self.sent = YLeaf(YType.uint32, "sent")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("dropped",
                                            "received",
                                            "sent") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pppoe.Nodes.Node.Statistics.PacketCounts.Other, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pppoe.Nodes.Node.Statistics.PacketCounts.Other, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.dropped.is_set or
                                self.received.is_set or
                                self.sent.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dropped.yfilter != YFilter.not_set or
                                self.received.yfilter != YFilter.not_set or
                                self.sent.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "other" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.dropped.is_set or self.dropped.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped.get_name_leafdata())
                            if (self.received.is_set or self.received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received.get_name_leafdata())
                            if (self.sent.is_set or self.sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sent.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dropped" or name == "received" or name == "sent"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "dropped"):
                                self.dropped = value
                                self.dropped.value_namespace = name_space
                                self.dropped.value_namespace_prefix = name_space_prefix
                            if(value_path == "received"):
                                self.received = value
                                self.received.value_namespace = name_space
                                self.received.value_namespace_prefix = name_space_prefix
                            if(value_path == "sent"):
                                self.sent = value
                                self.sent.value_namespace = name_space
                                self.sent.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.other is not None and self.other.has_data()) or
                            (self.padi is not None and self.padi.has_data()) or
                            (self.pado is not None and self.pado.has_data()) or
                            (self.padr is not None and self.padr.has_data()) or
                            (self.pads_error is not None and self.pads_error.has_data()) or
                            (self.pads_success is not None and self.pads_success.has_data()) or
                            (self.padt is not None and self.padt.has_data()) or
                            (self.session_state is not None and self.session_state.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.other is not None and self.other.has_operation()) or
                            (self.padi is not None and self.padi.has_operation()) or
                            (self.pado is not None and self.pado.has_operation()) or
                            (self.padr is not None and self.padr.has_operation()) or
                            (self.pads_error is not None and self.pads_error.has_operation()) or
                            (self.pads_success is not None and self.pads_success.has_operation()) or
                            (self.padt is not None and self.padt.has_operation()) or
                            (self.session_state is not None and self.session_state.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "packet-counts" + path_buffer

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

                        if (child_yang_name == "other"):
                            if (self.other is None):
                                self.other = Pppoe.Nodes.Node.Statistics.PacketCounts.Other()
                                self.other.parent = self
                                self._children_name_map["other"] = "other"
                            return self.other

                        if (child_yang_name == "padi"):
                            if (self.padi is None):
                                self.padi = Pppoe.Nodes.Node.Statistics.PacketCounts.Padi()
                                self.padi.parent = self
                                self._children_name_map["padi"] = "padi"
                            return self.padi

                        if (child_yang_name == "pado"):
                            if (self.pado is None):
                                self.pado = Pppoe.Nodes.Node.Statistics.PacketCounts.Pado()
                                self.pado.parent = self
                                self._children_name_map["pado"] = "pado"
                            return self.pado

                        if (child_yang_name == "padr"):
                            if (self.padr is None):
                                self.padr = Pppoe.Nodes.Node.Statistics.PacketCounts.Padr()
                                self.padr.parent = self
                                self._children_name_map["padr"] = "padr"
                            return self.padr

                        if (child_yang_name == "pads-error"):
                            if (self.pads_error is None):
                                self.pads_error = Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError()
                                self.pads_error.parent = self
                                self._children_name_map["pads_error"] = "pads-error"
                            return self.pads_error

                        if (child_yang_name == "pads-success"):
                            if (self.pads_success is None):
                                self.pads_success = Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess()
                                self.pads_success.parent = self
                                self._children_name_map["pads_success"] = "pads-success"
                            return self.pads_success

                        if (child_yang_name == "padt"):
                            if (self.padt is None):
                                self.padt = Pppoe.Nodes.Node.Statistics.PacketCounts.Padt()
                                self.padt.parent = self
                                self._children_name_map["padt"] = "padt"
                            return self.padt

                        if (child_yang_name == "session-state"):
                            if (self.session_state is None):
                                self.session_state = Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState()
                                self.session_state.parent = self
                                self._children_name_map["session_state"] = "session-state"
                            return self.session_state

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "other" or name == "padi" or name == "pado" or name == "padr" or name == "pads-error" or name == "pads-success" or name == "padt" or name == "session-state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class PacketErrorCounts(Entity):
                    """
                    Packet Error Counts
                    
                    .. attribute:: bad_packet_length
                    
                    	Bad packet length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bad_tag_length_field
                    
                    	Bad tag\-length field
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bad_vendor_tag_length_field
                    
                    	Bad vendor tag length field
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: duplicate_host_uniq_tag_received
                    
                    	Duplicate Host\-Uniq tag received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: duplicate_relay_session_id_tag_received
                    
                    	Duplicate Relay Session ID tag received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_ale_tag
                    
                    	Invalid ALE tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_dsl_tag
                    
                    	Invalid DSL tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_iana_code_invendor_tag
                    
                    	Invalid IANA code in vendor tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_iwf_tag
                    
                    	Invalid IWF tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_max_payload_tag
                    
                    	Invalid Max\-Payload tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_peer_mac
                    
                    	Invalid Peer MAC
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_service_name
                    
                    	Invalid Service Name
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_version_type_value
                    
                    	Invalid version\-type value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_vlan_tags
                    
                    	Invalid VLAN Tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_ale_tags
                    
                    	Multiple ALE tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_circuit_id_tags
                    
                    	Multiple Circuit\-ID tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_host_uniq_tags
                    
                    	Multiple Host\-Uniq tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_iwf_tags
                    
                    	Multiple IWF tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_max_payload_tags
                    
                    	Multiple Max\-Payload tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_of_the_same_dsl_tag
                    
                    	Multiple of the same DSL tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_relay_session_id_tags
                    
                    	Multiple relay\-session\-id tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_remote_id_tags
                    
                    	Multiple Remote\-ID tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_service_name_tags
                    
                    	Multiple Service\-Name tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_vendor_specific_tags
                    
                    	Multiple Vendor\-specific tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_iana_code_invendor_tag
                    
                    	No IANA code in vendor tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_interface_handle
                    
                    	No interface handle
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_packet_mac_address
                    
                    	No packet mac\-address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_packet_payload
                    
                    	No packet payload
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_service_name_tag
                    
                    	No Service\-Name Tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_space_left_in_packet
                    
                    	No space left in packet
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packet_on_srg_slave
                    
                    	Packet Received on SRG Slave
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packet_too_long
                    
                    	Packet too long
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pado_received
                    
                    	PADO received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pads_received
                    
                    	PADS received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: padt_before_pads_sent
                    
                    	PADT before PADS sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: padt_for_unknown_session
                    
                    	PADT for unknown session
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: padt_with_wrong_peer_mac
                    
                    	PADT with wrong peer\-mac
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: padt_with_wrong_vlan_tags
                    
                    	PADT with wrong VLAN tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_stage_packet_for_unknown_session
                    
                    	Session\-stage packet for unknown session
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_stage_packet_with_no_error
                    
                    	Session\-stage packet with no error
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_stage_packet_with_wrong_mac
                    
                    	Session\-stage packet with wrong mac
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_stage_packet_with_wrong_vlan_tags
                    
                    	Session\-stage packet with wrong VLAN tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tag_too_short
                    
                    	Tag too short
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unexpected_ac_name_tag
                    
                    	Unexpected AC\-Name tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unexpected_error_tags
                    
                    	Unexpected error tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unexpected_session_id_in_packet
                    
                    	Unexpected Session\-ID in packet
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_interface
                    
                    	Unknown interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_packet_type_received
                    
                    	Unknown packet type received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_tag_received
                    
                    	Unknown tag received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknownvendor_tag
                    
                    	Unknown vendor\-tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vendor_tag_too_short
                    
                    	Vendor tag too short
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: zero_length_host_uniq
                    
                    	Zero\-length Host\-Uniq tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.Nodes.Node.Statistics.PacketErrorCounts, self).__init__()

                        self.yang_name = "packet-error-counts"
                        self.yang_parent_name = "statistics"

                        self.bad_packet_length = YLeaf(YType.uint32, "bad-packet-length")

                        self.bad_tag_length_field = YLeaf(YType.uint32, "bad-tag-length-field")

                        self.bad_vendor_tag_length_field = YLeaf(YType.uint32, "bad-vendor-tag-length-field")

                        self.duplicate_host_uniq_tag_received = YLeaf(YType.uint32, "duplicate-host-uniq-tag-received")

                        self.duplicate_relay_session_id_tag_received = YLeaf(YType.uint32, "duplicate-relay-session-id-tag-received")

                        self.invalid_ale_tag = YLeaf(YType.uint32, "invalid-ale-tag")

                        self.invalid_dsl_tag = YLeaf(YType.uint32, "invalid-dsl-tag")

                        self.invalid_iana_code_invendor_tag = YLeaf(YType.uint32, "invalid-iana-code-invendor-tag")

                        self.invalid_iwf_tag = YLeaf(YType.uint32, "invalid-iwf-tag")

                        self.invalid_max_payload_tag = YLeaf(YType.uint32, "invalid-max-payload-tag")

                        self.invalid_peer_mac = YLeaf(YType.uint32, "invalid-peer-mac")

                        self.invalid_service_name = YLeaf(YType.uint32, "invalid-service-name")

                        self.invalid_version_type_value = YLeaf(YType.uint32, "invalid-version-type-value")

                        self.invalid_vlan_tags = YLeaf(YType.uint32, "invalid-vlan-tags")

                        self.multiple_ale_tags = YLeaf(YType.uint32, "multiple-ale-tags")

                        self.multiple_circuit_id_tags = YLeaf(YType.uint32, "multiple-circuit-id-tags")

                        self.multiple_host_uniq_tags = YLeaf(YType.uint32, "multiple-host-uniq-tags")

                        self.multiple_iwf_tags = YLeaf(YType.uint32, "multiple-iwf-tags")

                        self.multiple_max_payload_tags = YLeaf(YType.uint32, "multiple-max-payload-tags")

                        self.multiple_of_the_same_dsl_tag = YLeaf(YType.uint32, "multiple-of-the-same-dsl-tag")

                        self.multiple_relay_session_id_tags = YLeaf(YType.uint32, "multiple-relay-session-id-tags")

                        self.multiple_remote_id_tags = YLeaf(YType.uint32, "multiple-remote-id-tags")

                        self.multiple_service_name_tags = YLeaf(YType.uint32, "multiple-service-name-tags")

                        self.multiple_vendor_specific_tags = YLeaf(YType.uint32, "multiple-vendor-specific-tags")

                        self.no_iana_code_invendor_tag = YLeaf(YType.uint32, "no-iana-code-invendor-tag")

                        self.no_interface_handle = YLeaf(YType.uint32, "no-interface-handle")

                        self.no_packet_mac_address = YLeaf(YType.uint32, "no-packet-mac-address")

                        self.no_packet_payload = YLeaf(YType.uint32, "no-packet-payload")

                        self.no_service_name_tag = YLeaf(YType.uint32, "no-service-name-tag")

                        self.no_space_left_in_packet = YLeaf(YType.uint32, "no-space-left-in-packet")

                        self.packet_on_srg_slave = YLeaf(YType.uint32, "packet-on-srg-slave")

                        self.packet_too_long = YLeaf(YType.uint32, "packet-too-long")

                        self.pado_received = YLeaf(YType.uint32, "pado-received")

                        self.pads_received = YLeaf(YType.uint32, "pads-received")

                        self.padt_before_pads_sent = YLeaf(YType.uint32, "padt-before-pads-sent")

                        self.padt_for_unknown_session = YLeaf(YType.uint32, "padt-for-unknown-session")

                        self.padt_with_wrong_peer_mac = YLeaf(YType.uint32, "padt-with-wrong-peer-mac")

                        self.padt_with_wrong_vlan_tags = YLeaf(YType.uint32, "padt-with-wrong-vlan-tags")

                        self.session_stage_packet_for_unknown_session = YLeaf(YType.uint32, "session-stage-packet-for-unknown-session")

                        self.session_stage_packet_with_no_error = YLeaf(YType.uint32, "session-stage-packet-with-no-error")

                        self.session_stage_packet_with_wrong_mac = YLeaf(YType.uint32, "session-stage-packet-with-wrong-mac")

                        self.session_stage_packet_with_wrong_vlan_tags = YLeaf(YType.uint32, "session-stage-packet-with-wrong-vlan-tags")

                        self.tag_too_short = YLeaf(YType.uint32, "tag-too-short")

                        self.unexpected_ac_name_tag = YLeaf(YType.uint32, "unexpected-ac-name-tag")

                        self.unexpected_error_tags = YLeaf(YType.uint32, "unexpected-error-tags")

                        self.unexpected_session_id_in_packet = YLeaf(YType.uint32, "unexpected-session-id-in-packet")

                        self.unknown_interface = YLeaf(YType.uint32, "unknown-interface")

                        self.unknown_packet_type_received = YLeaf(YType.uint32, "unknown-packet-type-received")

                        self.unknown_tag_received = YLeaf(YType.uint32, "unknown-tag-received")

                        self.unknownvendor_tag = YLeaf(YType.uint32, "unknownvendor-tag")

                        self.vendor_tag_too_short = YLeaf(YType.uint32, "vendor-tag-too-short")

                        self.zero_length_host_uniq = YLeaf(YType.uint32, "zero-length-host-uniq")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("bad_packet_length",
                                        "bad_tag_length_field",
                                        "bad_vendor_tag_length_field",
                                        "duplicate_host_uniq_tag_received",
                                        "duplicate_relay_session_id_tag_received",
                                        "invalid_ale_tag",
                                        "invalid_dsl_tag",
                                        "invalid_iana_code_invendor_tag",
                                        "invalid_iwf_tag",
                                        "invalid_max_payload_tag",
                                        "invalid_peer_mac",
                                        "invalid_service_name",
                                        "invalid_version_type_value",
                                        "invalid_vlan_tags",
                                        "multiple_ale_tags",
                                        "multiple_circuit_id_tags",
                                        "multiple_host_uniq_tags",
                                        "multiple_iwf_tags",
                                        "multiple_max_payload_tags",
                                        "multiple_of_the_same_dsl_tag",
                                        "multiple_relay_session_id_tags",
                                        "multiple_remote_id_tags",
                                        "multiple_service_name_tags",
                                        "multiple_vendor_specific_tags",
                                        "no_iana_code_invendor_tag",
                                        "no_interface_handle",
                                        "no_packet_mac_address",
                                        "no_packet_payload",
                                        "no_service_name_tag",
                                        "no_space_left_in_packet",
                                        "packet_on_srg_slave",
                                        "packet_too_long",
                                        "pado_received",
                                        "pads_received",
                                        "padt_before_pads_sent",
                                        "padt_for_unknown_session",
                                        "padt_with_wrong_peer_mac",
                                        "padt_with_wrong_vlan_tags",
                                        "session_stage_packet_for_unknown_session",
                                        "session_stage_packet_with_no_error",
                                        "session_stage_packet_with_wrong_mac",
                                        "session_stage_packet_with_wrong_vlan_tags",
                                        "tag_too_short",
                                        "unexpected_ac_name_tag",
                                        "unexpected_error_tags",
                                        "unexpected_session_id_in_packet",
                                        "unknown_interface",
                                        "unknown_packet_type_received",
                                        "unknown_tag_received",
                                        "unknownvendor_tag",
                                        "vendor_tag_too_short",
                                        "zero_length_host_uniq") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pppoe.Nodes.Node.Statistics.PacketErrorCounts, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pppoe.Nodes.Node.Statistics.PacketErrorCounts, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.bad_packet_length.is_set or
                            self.bad_tag_length_field.is_set or
                            self.bad_vendor_tag_length_field.is_set or
                            self.duplicate_host_uniq_tag_received.is_set or
                            self.duplicate_relay_session_id_tag_received.is_set or
                            self.invalid_ale_tag.is_set or
                            self.invalid_dsl_tag.is_set or
                            self.invalid_iana_code_invendor_tag.is_set or
                            self.invalid_iwf_tag.is_set or
                            self.invalid_max_payload_tag.is_set or
                            self.invalid_peer_mac.is_set or
                            self.invalid_service_name.is_set or
                            self.invalid_version_type_value.is_set or
                            self.invalid_vlan_tags.is_set or
                            self.multiple_ale_tags.is_set or
                            self.multiple_circuit_id_tags.is_set or
                            self.multiple_host_uniq_tags.is_set or
                            self.multiple_iwf_tags.is_set or
                            self.multiple_max_payload_tags.is_set or
                            self.multiple_of_the_same_dsl_tag.is_set or
                            self.multiple_relay_session_id_tags.is_set or
                            self.multiple_remote_id_tags.is_set or
                            self.multiple_service_name_tags.is_set or
                            self.multiple_vendor_specific_tags.is_set or
                            self.no_iana_code_invendor_tag.is_set or
                            self.no_interface_handle.is_set or
                            self.no_packet_mac_address.is_set or
                            self.no_packet_payload.is_set or
                            self.no_service_name_tag.is_set or
                            self.no_space_left_in_packet.is_set or
                            self.packet_on_srg_slave.is_set or
                            self.packet_too_long.is_set or
                            self.pado_received.is_set or
                            self.pads_received.is_set or
                            self.padt_before_pads_sent.is_set or
                            self.padt_for_unknown_session.is_set or
                            self.padt_with_wrong_peer_mac.is_set or
                            self.padt_with_wrong_vlan_tags.is_set or
                            self.session_stage_packet_for_unknown_session.is_set or
                            self.session_stage_packet_with_no_error.is_set or
                            self.session_stage_packet_with_wrong_mac.is_set or
                            self.session_stage_packet_with_wrong_vlan_tags.is_set or
                            self.tag_too_short.is_set or
                            self.unexpected_ac_name_tag.is_set or
                            self.unexpected_error_tags.is_set or
                            self.unexpected_session_id_in_packet.is_set or
                            self.unknown_interface.is_set or
                            self.unknown_packet_type_received.is_set or
                            self.unknown_tag_received.is_set or
                            self.unknownvendor_tag.is_set or
                            self.vendor_tag_too_short.is_set or
                            self.zero_length_host_uniq.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.bad_packet_length.yfilter != YFilter.not_set or
                            self.bad_tag_length_field.yfilter != YFilter.not_set or
                            self.bad_vendor_tag_length_field.yfilter != YFilter.not_set or
                            self.duplicate_host_uniq_tag_received.yfilter != YFilter.not_set or
                            self.duplicate_relay_session_id_tag_received.yfilter != YFilter.not_set or
                            self.invalid_ale_tag.yfilter != YFilter.not_set or
                            self.invalid_dsl_tag.yfilter != YFilter.not_set or
                            self.invalid_iana_code_invendor_tag.yfilter != YFilter.not_set or
                            self.invalid_iwf_tag.yfilter != YFilter.not_set or
                            self.invalid_max_payload_tag.yfilter != YFilter.not_set or
                            self.invalid_peer_mac.yfilter != YFilter.not_set or
                            self.invalid_service_name.yfilter != YFilter.not_set or
                            self.invalid_version_type_value.yfilter != YFilter.not_set or
                            self.invalid_vlan_tags.yfilter != YFilter.not_set or
                            self.multiple_ale_tags.yfilter != YFilter.not_set or
                            self.multiple_circuit_id_tags.yfilter != YFilter.not_set or
                            self.multiple_host_uniq_tags.yfilter != YFilter.not_set or
                            self.multiple_iwf_tags.yfilter != YFilter.not_set or
                            self.multiple_max_payload_tags.yfilter != YFilter.not_set or
                            self.multiple_of_the_same_dsl_tag.yfilter != YFilter.not_set or
                            self.multiple_relay_session_id_tags.yfilter != YFilter.not_set or
                            self.multiple_remote_id_tags.yfilter != YFilter.not_set or
                            self.multiple_service_name_tags.yfilter != YFilter.not_set or
                            self.multiple_vendor_specific_tags.yfilter != YFilter.not_set or
                            self.no_iana_code_invendor_tag.yfilter != YFilter.not_set or
                            self.no_interface_handle.yfilter != YFilter.not_set or
                            self.no_packet_mac_address.yfilter != YFilter.not_set or
                            self.no_packet_payload.yfilter != YFilter.not_set or
                            self.no_service_name_tag.yfilter != YFilter.not_set or
                            self.no_space_left_in_packet.yfilter != YFilter.not_set or
                            self.packet_on_srg_slave.yfilter != YFilter.not_set or
                            self.packet_too_long.yfilter != YFilter.not_set or
                            self.pado_received.yfilter != YFilter.not_set or
                            self.pads_received.yfilter != YFilter.not_set or
                            self.padt_before_pads_sent.yfilter != YFilter.not_set or
                            self.padt_for_unknown_session.yfilter != YFilter.not_set or
                            self.padt_with_wrong_peer_mac.yfilter != YFilter.not_set or
                            self.padt_with_wrong_vlan_tags.yfilter != YFilter.not_set or
                            self.session_stage_packet_for_unknown_session.yfilter != YFilter.not_set or
                            self.session_stage_packet_with_no_error.yfilter != YFilter.not_set or
                            self.session_stage_packet_with_wrong_mac.yfilter != YFilter.not_set or
                            self.session_stage_packet_with_wrong_vlan_tags.yfilter != YFilter.not_set or
                            self.tag_too_short.yfilter != YFilter.not_set or
                            self.unexpected_ac_name_tag.yfilter != YFilter.not_set or
                            self.unexpected_error_tags.yfilter != YFilter.not_set or
                            self.unexpected_session_id_in_packet.yfilter != YFilter.not_set or
                            self.unknown_interface.yfilter != YFilter.not_set or
                            self.unknown_packet_type_received.yfilter != YFilter.not_set or
                            self.unknown_tag_received.yfilter != YFilter.not_set or
                            self.unknownvendor_tag.yfilter != YFilter.not_set or
                            self.vendor_tag_too_short.yfilter != YFilter.not_set or
                            self.zero_length_host_uniq.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "packet-error-counts" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.bad_packet_length.is_set or self.bad_packet_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bad_packet_length.get_name_leafdata())
                        if (self.bad_tag_length_field.is_set or self.bad_tag_length_field.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bad_tag_length_field.get_name_leafdata())
                        if (self.bad_vendor_tag_length_field.is_set or self.bad_vendor_tag_length_field.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bad_vendor_tag_length_field.get_name_leafdata())
                        if (self.duplicate_host_uniq_tag_received.is_set or self.duplicate_host_uniq_tag_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.duplicate_host_uniq_tag_received.get_name_leafdata())
                        if (self.duplicate_relay_session_id_tag_received.is_set or self.duplicate_relay_session_id_tag_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.duplicate_relay_session_id_tag_received.get_name_leafdata())
                        if (self.invalid_ale_tag.is_set or self.invalid_ale_tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_ale_tag.get_name_leafdata())
                        if (self.invalid_dsl_tag.is_set or self.invalid_dsl_tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_dsl_tag.get_name_leafdata())
                        if (self.invalid_iana_code_invendor_tag.is_set or self.invalid_iana_code_invendor_tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_iana_code_invendor_tag.get_name_leafdata())
                        if (self.invalid_iwf_tag.is_set or self.invalid_iwf_tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_iwf_tag.get_name_leafdata())
                        if (self.invalid_max_payload_tag.is_set or self.invalid_max_payload_tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_max_payload_tag.get_name_leafdata())
                        if (self.invalid_peer_mac.is_set or self.invalid_peer_mac.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_peer_mac.get_name_leafdata())
                        if (self.invalid_service_name.is_set or self.invalid_service_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_service_name.get_name_leafdata())
                        if (self.invalid_version_type_value.is_set or self.invalid_version_type_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_version_type_value.get_name_leafdata())
                        if (self.invalid_vlan_tags.is_set or self.invalid_vlan_tags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_vlan_tags.get_name_leafdata())
                        if (self.multiple_ale_tags.is_set or self.multiple_ale_tags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multiple_ale_tags.get_name_leafdata())
                        if (self.multiple_circuit_id_tags.is_set or self.multiple_circuit_id_tags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multiple_circuit_id_tags.get_name_leafdata())
                        if (self.multiple_host_uniq_tags.is_set or self.multiple_host_uniq_tags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multiple_host_uniq_tags.get_name_leafdata())
                        if (self.multiple_iwf_tags.is_set or self.multiple_iwf_tags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multiple_iwf_tags.get_name_leafdata())
                        if (self.multiple_max_payload_tags.is_set or self.multiple_max_payload_tags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multiple_max_payload_tags.get_name_leafdata())
                        if (self.multiple_of_the_same_dsl_tag.is_set or self.multiple_of_the_same_dsl_tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multiple_of_the_same_dsl_tag.get_name_leafdata())
                        if (self.multiple_relay_session_id_tags.is_set or self.multiple_relay_session_id_tags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multiple_relay_session_id_tags.get_name_leafdata())
                        if (self.multiple_remote_id_tags.is_set or self.multiple_remote_id_tags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multiple_remote_id_tags.get_name_leafdata())
                        if (self.multiple_service_name_tags.is_set or self.multiple_service_name_tags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multiple_service_name_tags.get_name_leafdata())
                        if (self.multiple_vendor_specific_tags.is_set or self.multiple_vendor_specific_tags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multiple_vendor_specific_tags.get_name_leafdata())
                        if (self.no_iana_code_invendor_tag.is_set or self.no_iana_code_invendor_tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.no_iana_code_invendor_tag.get_name_leafdata())
                        if (self.no_interface_handle.is_set or self.no_interface_handle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.no_interface_handle.get_name_leafdata())
                        if (self.no_packet_mac_address.is_set or self.no_packet_mac_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.no_packet_mac_address.get_name_leafdata())
                        if (self.no_packet_payload.is_set or self.no_packet_payload.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.no_packet_payload.get_name_leafdata())
                        if (self.no_service_name_tag.is_set or self.no_service_name_tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.no_service_name_tag.get_name_leafdata())
                        if (self.no_space_left_in_packet.is_set or self.no_space_left_in_packet.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.no_space_left_in_packet.get_name_leafdata())
                        if (self.packet_on_srg_slave.is_set or self.packet_on_srg_slave.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packet_on_srg_slave.get_name_leafdata())
                        if (self.packet_too_long.is_set or self.packet_too_long.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.packet_too_long.get_name_leafdata())
                        if (self.pado_received.is_set or self.pado_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pado_received.get_name_leafdata())
                        if (self.pads_received.is_set or self.pads_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pads_received.get_name_leafdata())
                        if (self.padt_before_pads_sent.is_set or self.padt_before_pads_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.padt_before_pads_sent.get_name_leafdata())
                        if (self.padt_for_unknown_session.is_set or self.padt_for_unknown_session.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.padt_for_unknown_session.get_name_leafdata())
                        if (self.padt_with_wrong_peer_mac.is_set or self.padt_with_wrong_peer_mac.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.padt_with_wrong_peer_mac.get_name_leafdata())
                        if (self.padt_with_wrong_vlan_tags.is_set or self.padt_with_wrong_vlan_tags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.padt_with_wrong_vlan_tags.get_name_leafdata())
                        if (self.session_stage_packet_for_unknown_session.is_set or self.session_stage_packet_for_unknown_session.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_stage_packet_for_unknown_session.get_name_leafdata())
                        if (self.session_stage_packet_with_no_error.is_set or self.session_stage_packet_with_no_error.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_stage_packet_with_no_error.get_name_leafdata())
                        if (self.session_stage_packet_with_wrong_mac.is_set or self.session_stage_packet_with_wrong_mac.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_stage_packet_with_wrong_mac.get_name_leafdata())
                        if (self.session_stage_packet_with_wrong_vlan_tags.is_set or self.session_stage_packet_with_wrong_vlan_tags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_stage_packet_with_wrong_vlan_tags.get_name_leafdata())
                        if (self.tag_too_short.is_set or self.tag_too_short.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tag_too_short.get_name_leafdata())
                        if (self.unexpected_ac_name_tag.is_set or self.unexpected_ac_name_tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unexpected_ac_name_tag.get_name_leafdata())
                        if (self.unexpected_error_tags.is_set or self.unexpected_error_tags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unexpected_error_tags.get_name_leafdata())
                        if (self.unexpected_session_id_in_packet.is_set or self.unexpected_session_id_in_packet.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unexpected_session_id_in_packet.get_name_leafdata())
                        if (self.unknown_interface.is_set or self.unknown_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unknown_interface.get_name_leafdata())
                        if (self.unknown_packet_type_received.is_set or self.unknown_packet_type_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unknown_packet_type_received.get_name_leafdata())
                        if (self.unknown_tag_received.is_set or self.unknown_tag_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unknown_tag_received.get_name_leafdata())
                        if (self.unknownvendor_tag.is_set or self.unknownvendor_tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unknownvendor_tag.get_name_leafdata())
                        if (self.vendor_tag_too_short.is_set or self.vendor_tag_too_short.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vendor_tag_too_short.get_name_leafdata())
                        if (self.zero_length_host_uniq.is_set or self.zero_length_host_uniq.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.zero_length_host_uniq.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bad-packet-length" or name == "bad-tag-length-field" or name == "bad-vendor-tag-length-field" or name == "duplicate-host-uniq-tag-received" or name == "duplicate-relay-session-id-tag-received" or name == "invalid-ale-tag" or name == "invalid-dsl-tag" or name == "invalid-iana-code-invendor-tag" or name == "invalid-iwf-tag" or name == "invalid-max-payload-tag" or name == "invalid-peer-mac" or name == "invalid-service-name" or name == "invalid-version-type-value" or name == "invalid-vlan-tags" or name == "multiple-ale-tags" or name == "multiple-circuit-id-tags" or name == "multiple-host-uniq-tags" or name == "multiple-iwf-tags" or name == "multiple-max-payload-tags" or name == "multiple-of-the-same-dsl-tag" or name == "multiple-relay-session-id-tags" or name == "multiple-remote-id-tags" or name == "multiple-service-name-tags" or name == "multiple-vendor-specific-tags" or name == "no-iana-code-invendor-tag" or name == "no-interface-handle" or name == "no-packet-mac-address" or name == "no-packet-payload" or name == "no-service-name-tag" or name == "no-space-left-in-packet" or name == "packet-on-srg-slave" or name == "packet-too-long" or name == "pado-received" or name == "pads-received" or name == "padt-before-pads-sent" or name == "padt-for-unknown-session" or name == "padt-with-wrong-peer-mac" or name == "padt-with-wrong-vlan-tags" or name == "session-stage-packet-for-unknown-session" or name == "session-stage-packet-with-no-error" or name == "session-stage-packet-with-wrong-mac" or name == "session-stage-packet-with-wrong-vlan-tags" or name == "tag-too-short" or name == "unexpected-ac-name-tag" or name == "unexpected-error-tags" or name == "unexpected-session-id-in-packet" or name == "unknown-interface" or name == "unknown-packet-type-received" or name == "unknown-tag-received" or name == "unknownvendor-tag" or name == "vendor-tag-too-short" or name == "zero-length-host-uniq"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "bad-packet-length"):
                            self.bad_packet_length = value
                            self.bad_packet_length.value_namespace = name_space
                            self.bad_packet_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "bad-tag-length-field"):
                            self.bad_tag_length_field = value
                            self.bad_tag_length_field.value_namespace = name_space
                            self.bad_tag_length_field.value_namespace_prefix = name_space_prefix
                        if(value_path == "bad-vendor-tag-length-field"):
                            self.bad_vendor_tag_length_field = value
                            self.bad_vendor_tag_length_field.value_namespace = name_space
                            self.bad_vendor_tag_length_field.value_namespace_prefix = name_space_prefix
                        if(value_path == "duplicate-host-uniq-tag-received"):
                            self.duplicate_host_uniq_tag_received = value
                            self.duplicate_host_uniq_tag_received.value_namespace = name_space
                            self.duplicate_host_uniq_tag_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "duplicate-relay-session-id-tag-received"):
                            self.duplicate_relay_session_id_tag_received = value
                            self.duplicate_relay_session_id_tag_received.value_namespace = name_space
                            self.duplicate_relay_session_id_tag_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-ale-tag"):
                            self.invalid_ale_tag = value
                            self.invalid_ale_tag.value_namespace = name_space
                            self.invalid_ale_tag.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-dsl-tag"):
                            self.invalid_dsl_tag = value
                            self.invalid_dsl_tag.value_namespace = name_space
                            self.invalid_dsl_tag.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-iana-code-invendor-tag"):
                            self.invalid_iana_code_invendor_tag = value
                            self.invalid_iana_code_invendor_tag.value_namespace = name_space
                            self.invalid_iana_code_invendor_tag.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-iwf-tag"):
                            self.invalid_iwf_tag = value
                            self.invalid_iwf_tag.value_namespace = name_space
                            self.invalid_iwf_tag.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-max-payload-tag"):
                            self.invalid_max_payload_tag = value
                            self.invalid_max_payload_tag.value_namespace = name_space
                            self.invalid_max_payload_tag.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-peer-mac"):
                            self.invalid_peer_mac = value
                            self.invalid_peer_mac.value_namespace = name_space
                            self.invalid_peer_mac.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-service-name"):
                            self.invalid_service_name = value
                            self.invalid_service_name.value_namespace = name_space
                            self.invalid_service_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-version-type-value"):
                            self.invalid_version_type_value = value
                            self.invalid_version_type_value.value_namespace = name_space
                            self.invalid_version_type_value.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-vlan-tags"):
                            self.invalid_vlan_tags = value
                            self.invalid_vlan_tags.value_namespace = name_space
                            self.invalid_vlan_tags.value_namespace_prefix = name_space_prefix
                        if(value_path == "multiple-ale-tags"):
                            self.multiple_ale_tags = value
                            self.multiple_ale_tags.value_namespace = name_space
                            self.multiple_ale_tags.value_namespace_prefix = name_space_prefix
                        if(value_path == "multiple-circuit-id-tags"):
                            self.multiple_circuit_id_tags = value
                            self.multiple_circuit_id_tags.value_namespace = name_space
                            self.multiple_circuit_id_tags.value_namespace_prefix = name_space_prefix
                        if(value_path == "multiple-host-uniq-tags"):
                            self.multiple_host_uniq_tags = value
                            self.multiple_host_uniq_tags.value_namespace = name_space
                            self.multiple_host_uniq_tags.value_namespace_prefix = name_space_prefix
                        if(value_path == "multiple-iwf-tags"):
                            self.multiple_iwf_tags = value
                            self.multiple_iwf_tags.value_namespace = name_space
                            self.multiple_iwf_tags.value_namespace_prefix = name_space_prefix
                        if(value_path == "multiple-max-payload-tags"):
                            self.multiple_max_payload_tags = value
                            self.multiple_max_payload_tags.value_namespace = name_space
                            self.multiple_max_payload_tags.value_namespace_prefix = name_space_prefix
                        if(value_path == "multiple-of-the-same-dsl-tag"):
                            self.multiple_of_the_same_dsl_tag = value
                            self.multiple_of_the_same_dsl_tag.value_namespace = name_space
                            self.multiple_of_the_same_dsl_tag.value_namespace_prefix = name_space_prefix
                        if(value_path == "multiple-relay-session-id-tags"):
                            self.multiple_relay_session_id_tags = value
                            self.multiple_relay_session_id_tags.value_namespace = name_space
                            self.multiple_relay_session_id_tags.value_namespace_prefix = name_space_prefix
                        if(value_path == "multiple-remote-id-tags"):
                            self.multiple_remote_id_tags = value
                            self.multiple_remote_id_tags.value_namespace = name_space
                            self.multiple_remote_id_tags.value_namespace_prefix = name_space_prefix
                        if(value_path == "multiple-service-name-tags"):
                            self.multiple_service_name_tags = value
                            self.multiple_service_name_tags.value_namespace = name_space
                            self.multiple_service_name_tags.value_namespace_prefix = name_space_prefix
                        if(value_path == "multiple-vendor-specific-tags"):
                            self.multiple_vendor_specific_tags = value
                            self.multiple_vendor_specific_tags.value_namespace = name_space
                            self.multiple_vendor_specific_tags.value_namespace_prefix = name_space_prefix
                        if(value_path == "no-iana-code-invendor-tag"):
                            self.no_iana_code_invendor_tag = value
                            self.no_iana_code_invendor_tag.value_namespace = name_space
                            self.no_iana_code_invendor_tag.value_namespace_prefix = name_space_prefix
                        if(value_path == "no-interface-handle"):
                            self.no_interface_handle = value
                            self.no_interface_handle.value_namespace = name_space
                            self.no_interface_handle.value_namespace_prefix = name_space_prefix
                        if(value_path == "no-packet-mac-address"):
                            self.no_packet_mac_address = value
                            self.no_packet_mac_address.value_namespace = name_space
                            self.no_packet_mac_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "no-packet-payload"):
                            self.no_packet_payload = value
                            self.no_packet_payload.value_namespace = name_space
                            self.no_packet_payload.value_namespace_prefix = name_space_prefix
                        if(value_path == "no-service-name-tag"):
                            self.no_service_name_tag = value
                            self.no_service_name_tag.value_namespace = name_space
                            self.no_service_name_tag.value_namespace_prefix = name_space_prefix
                        if(value_path == "no-space-left-in-packet"):
                            self.no_space_left_in_packet = value
                            self.no_space_left_in_packet.value_namespace = name_space
                            self.no_space_left_in_packet.value_namespace_prefix = name_space_prefix
                        if(value_path == "packet-on-srg-slave"):
                            self.packet_on_srg_slave = value
                            self.packet_on_srg_slave.value_namespace = name_space
                            self.packet_on_srg_slave.value_namespace_prefix = name_space_prefix
                        if(value_path == "packet-too-long"):
                            self.packet_too_long = value
                            self.packet_too_long.value_namespace = name_space
                            self.packet_too_long.value_namespace_prefix = name_space_prefix
                        if(value_path == "pado-received"):
                            self.pado_received = value
                            self.pado_received.value_namespace = name_space
                            self.pado_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "pads-received"):
                            self.pads_received = value
                            self.pads_received.value_namespace = name_space
                            self.pads_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "padt-before-pads-sent"):
                            self.padt_before_pads_sent = value
                            self.padt_before_pads_sent.value_namespace = name_space
                            self.padt_before_pads_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "padt-for-unknown-session"):
                            self.padt_for_unknown_session = value
                            self.padt_for_unknown_session.value_namespace = name_space
                            self.padt_for_unknown_session.value_namespace_prefix = name_space_prefix
                        if(value_path == "padt-with-wrong-peer-mac"):
                            self.padt_with_wrong_peer_mac = value
                            self.padt_with_wrong_peer_mac.value_namespace = name_space
                            self.padt_with_wrong_peer_mac.value_namespace_prefix = name_space_prefix
                        if(value_path == "padt-with-wrong-vlan-tags"):
                            self.padt_with_wrong_vlan_tags = value
                            self.padt_with_wrong_vlan_tags.value_namespace = name_space
                            self.padt_with_wrong_vlan_tags.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-stage-packet-for-unknown-session"):
                            self.session_stage_packet_for_unknown_session = value
                            self.session_stage_packet_for_unknown_session.value_namespace = name_space
                            self.session_stage_packet_for_unknown_session.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-stage-packet-with-no-error"):
                            self.session_stage_packet_with_no_error = value
                            self.session_stage_packet_with_no_error.value_namespace = name_space
                            self.session_stage_packet_with_no_error.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-stage-packet-with-wrong-mac"):
                            self.session_stage_packet_with_wrong_mac = value
                            self.session_stage_packet_with_wrong_mac.value_namespace = name_space
                            self.session_stage_packet_with_wrong_mac.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-stage-packet-with-wrong-vlan-tags"):
                            self.session_stage_packet_with_wrong_vlan_tags = value
                            self.session_stage_packet_with_wrong_vlan_tags.value_namespace = name_space
                            self.session_stage_packet_with_wrong_vlan_tags.value_namespace_prefix = name_space_prefix
                        if(value_path == "tag-too-short"):
                            self.tag_too_short = value
                            self.tag_too_short.value_namespace = name_space
                            self.tag_too_short.value_namespace_prefix = name_space_prefix
                        if(value_path == "unexpected-ac-name-tag"):
                            self.unexpected_ac_name_tag = value
                            self.unexpected_ac_name_tag.value_namespace = name_space
                            self.unexpected_ac_name_tag.value_namespace_prefix = name_space_prefix
                        if(value_path == "unexpected-error-tags"):
                            self.unexpected_error_tags = value
                            self.unexpected_error_tags.value_namespace = name_space
                            self.unexpected_error_tags.value_namespace_prefix = name_space_prefix
                        if(value_path == "unexpected-session-id-in-packet"):
                            self.unexpected_session_id_in_packet = value
                            self.unexpected_session_id_in_packet.value_namespace = name_space
                            self.unexpected_session_id_in_packet.value_namespace_prefix = name_space_prefix
                        if(value_path == "unknown-interface"):
                            self.unknown_interface = value
                            self.unknown_interface.value_namespace = name_space
                            self.unknown_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "unknown-packet-type-received"):
                            self.unknown_packet_type_received = value
                            self.unknown_packet_type_received.value_namespace = name_space
                            self.unknown_packet_type_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "unknown-tag-received"):
                            self.unknown_tag_received = value
                            self.unknown_tag_received.value_namespace = name_space
                            self.unknown_tag_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "unknownvendor-tag"):
                            self.unknownvendor_tag = value
                            self.unknownvendor_tag.value_namespace = name_space
                            self.unknownvendor_tag.value_namespace_prefix = name_space_prefix
                        if(value_path == "vendor-tag-too-short"):
                            self.vendor_tag_too_short = value
                            self.vendor_tag_too_short.value_namespace = name_space
                            self.vendor_tag_too_short.value_namespace_prefix = name_space_prefix
                        if(value_path == "zero-length-host-uniq"):
                            self.zero_length_host_uniq = value
                            self.zero_length_host_uniq.value_namespace = name_space
                            self.zero_length_host_uniq.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.packet_counts is not None and self.packet_counts.has_data()) or
                        (self.packet_error_counts is not None and self.packet_error_counts.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.packet_counts is not None and self.packet_counts.has_operation()) or
                        (self.packet_error_counts is not None and self.packet_error_counts.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "statistics" + path_buffer

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

                    if (child_yang_name == "packet-counts"):
                        if (self.packet_counts is None):
                            self.packet_counts = Pppoe.Nodes.Node.Statistics.PacketCounts()
                            self.packet_counts.parent = self
                            self._children_name_map["packet_counts"] = "packet-counts"
                        return self.packet_counts

                    if (child_yang_name == "packet-error-counts"):
                        if (self.packet_error_counts is None):
                            self.packet_error_counts = Pppoe.Nodes.Node.Statistics.PacketErrorCounts()
                            self.packet_error_counts.parent = self
                            self._children_name_map["packet_error_counts"] = "packet-error-counts"
                        return self.packet_error_counts

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "packet-counts" or name == "packet-error-counts"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class AccessInterface(Entity):
                """
                PPPoE access interface information
                
                .. attribute:: summaries
                
                	PPPoE access interface summary information
                	**type**\:   :py:class:`Summaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.AccessInterface.Summaries>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Pppoe.Nodes.Node.AccessInterface, self).__init__()

                    self.yang_name = "access-interface"
                    self.yang_parent_name = "node"

                    self.summaries = Pppoe.Nodes.Node.AccessInterface.Summaries()
                    self.summaries.parent = self
                    self._children_name_map["summaries"] = "summaries"
                    self._children_yang_names.add("summaries")


                class Summaries(Entity):
                    """
                    PPPoE access interface summary information
                    
                    .. attribute:: summary
                    
                    	Summary information for a PPPoE\-enabled access interface
                    	**type**\: list of    :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.AccessInterface.Summaries.Summary>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.Nodes.Node.AccessInterface.Summaries, self).__init__()

                        self.yang_name = "summaries"
                        self.yang_parent_name = "access-interface"

                        self.summary = YList(self)

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
                                    super(Pppoe.Nodes.Node.AccessInterface.Summaries, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pppoe.Nodes.Node.AccessInterface.Summaries, self).__setattr__(name, value)


                    class Summary(Entity):
                        """
                        Summary information for a PPPoE\-enabled
                        access interface
                        
                        .. attribute:: interface_name  <key>
                        
                        	PPPoE Access Interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: bba_group_name
                        
                        	BBA Group
                        	**type**\:  str
                        
                        .. attribute:: incomplete_sessions
                        
                        	Incomplete Session Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_name_xr
                        
                        	Interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: interface_state
                        
                        	Interface State
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_ready
                        
                        	Is Ready
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: mac_address
                        
                        	Mac Address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: sessions
                        
                        	Session Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.AccessInterface.Summaries.Summary, self).__init__()

                            self.yang_name = "summary"
                            self.yang_parent_name = "summaries"

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.bba_group_name = YLeaf(YType.str, "bba-group-name")

                            self.incomplete_sessions = YLeaf(YType.uint32, "incomplete-sessions")

                            self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                            self.interface_state = YLeaf(YType.uint32, "interface-state")

                            self.is_ready = YLeaf(YType.int32, "is-ready")

                            self.mac_address = YLeaf(YType.str, "mac-address")

                            self.sessions = YLeaf(YType.uint32, "sessions")

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
                                            "bba_group_name",
                                            "incomplete_sessions",
                                            "interface_name_xr",
                                            "interface_state",
                                            "is_ready",
                                            "mac_address",
                                            "sessions") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pppoe.Nodes.Node.AccessInterface.Summaries.Summary, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pppoe.Nodes.Node.AccessInterface.Summaries.Summary, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.interface_name.is_set or
                                self.bba_group_name.is_set or
                                self.incomplete_sessions.is_set or
                                self.interface_name_xr.is_set or
                                self.interface_state.is_set or
                                self.is_ready.is_set or
                                self.mac_address.is_set or
                                self.sessions.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.bba_group_name.yfilter != YFilter.not_set or
                                self.incomplete_sessions.yfilter != YFilter.not_set or
                                self.interface_name_xr.yfilter != YFilter.not_set or
                                self.interface_state.yfilter != YFilter.not_set or
                                self.is_ready.yfilter != YFilter.not_set or
                                self.mac_address.yfilter != YFilter.not_set or
                                self.sessions.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "summary" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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
                            if (self.bba_group_name.is_set or self.bba_group_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bba_group_name.get_name_leafdata())
                            if (self.incomplete_sessions.is_set or self.incomplete_sessions.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.incomplete_sessions.get_name_leafdata())
                            if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name_xr.get_name_leafdata())
                            if (self.interface_state.is_set or self.interface_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_state.get_name_leafdata())
                            if (self.is_ready.is_set or self.is_ready.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_ready.get_name_leafdata())
                            if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mac_address.get_name_leafdata())
                            if (self.sessions.is_set or self.sessions.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sessions.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-name" or name == "bba-group-name" or name == "incomplete-sessions" or name == "interface-name-xr" or name == "interface-state" or name == "is-ready" or name == "mac-address" or name == "sessions"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "bba-group-name"):
                                self.bba_group_name = value
                                self.bba_group_name.value_namespace = name_space
                                self.bba_group_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "incomplete-sessions"):
                                self.incomplete_sessions = value
                                self.incomplete_sessions.value_namespace = name_space
                                self.incomplete_sessions.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-name-xr"):
                                self.interface_name_xr = value
                                self.interface_name_xr.value_namespace = name_space
                                self.interface_name_xr.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-state"):
                                self.interface_state = value
                                self.interface_state.value_namespace = name_space
                                self.interface_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-ready"):
                                self.is_ready = value
                                self.is_ready.value_namespace = name_space
                                self.is_ready.value_namespace_prefix = name_space_prefix
                            if(value_path == "mac-address"):
                                self.mac_address = value
                                self.mac_address.value_namespace = name_space
                                self.mac_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "sessions"):
                                self.sessions = value
                                self.sessions.value_namespace = name_space
                                self.sessions.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.summary:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.summary:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "summaries" + path_buffer

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

                        if (child_yang_name == "summary"):
                            for c in self.summary:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Pppoe.Nodes.Node.AccessInterface.Summaries.Summary()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.summary.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "summary"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.summaries is not None and self.summaries.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.summaries is not None and self.summaries.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "access-interface" + path_buffer

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

                    if (child_yang_name == "summaries"):
                        if (self.summaries is None):
                            self.summaries = Pppoe.Nodes.Node.AccessInterface.Summaries()
                            self.summaries.parent = self
                            self._children_name_map["summaries"] = "summaries"
                        return self.summaries

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "summaries"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Interfaces(Entity):
                """
                Per interface PPPoE operational data
                
                .. attribute:: interface
                
                	Data for a PPPoE interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Pppoe.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"

                    self.interface = YList(self)

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
                                super(Pppoe.Nodes.Node.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Pppoe.Nodes.Node.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    Data for a PPPoE interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	PPPoE Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: access_interface_name
                    
                    	Access Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: bba_group_name
                    
                    	BBA Group
                    	**type**\:  str
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: is_complete
                    
                    	Is Complete
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: local_mac_address
                    
                    	Local Mac\-Address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: peer_mac_address
                    
                    	Peer Mac\-Address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: srg_state
                    
                    	SRG state
                    	**type**\:   :py:class:`PppoeMaSessionIdbSrgState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaSessionIdbSrgState>`
                    
                    .. attribute:: tags
                    
                    	Tags
                    	**type**\:   :py:class:`Tags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Interfaces.Interface.Tags>`
                    
                    .. attribute:: vlan_inner_id
                    
                    	VLAN Inner ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: vlan_outer_id
                    
                    	VLAN Outer ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.access_interface_name = YLeaf(YType.str, "access-interface-name")

                        self.bba_group_name = YLeaf(YType.str, "bba-group-name")

                        self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                        self.is_complete = YLeaf(YType.int32, "is-complete")

                        self.local_mac_address = YLeaf(YType.str, "local-mac-address")

                        self.peer_mac_address = YLeaf(YType.str, "peer-mac-address")

                        self.session_id = YLeaf(YType.uint16, "session-id")

                        self.srg_state = YLeaf(YType.enumeration, "srg-state")

                        self.vlan_inner_id = YLeaf(YType.uint16, "vlan-inner-id")

                        self.vlan_outer_id = YLeaf(YType.uint16, "vlan-outer-id")

                        self.tags = Pppoe.Nodes.Node.Interfaces.Interface.Tags()
                        self.tags.parent = self
                        self._children_name_map["tags"] = "tags"
                        self._children_yang_names.add("tags")

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
                                        "access_interface_name",
                                        "bba_group_name",
                                        "interface_name_xr",
                                        "is_complete",
                                        "local_mac_address",
                                        "peer_mac_address",
                                        "session_id",
                                        "srg_state",
                                        "vlan_inner_id",
                                        "vlan_outer_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pppoe.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pppoe.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)


                    class Tags(Entity):
                        """
                        Tags
                        
                        .. attribute:: access_loop_encapsulation
                        
                        	Access Loop Encapsulation
                        	**type**\:   :py:class:`AccessLoopEncapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation>`
                        
                        .. attribute:: circuit_id
                        
                        	Circuit ID
                        	**type**\:  str
                        
                        .. attribute:: dsl_actual_delay_down
                        
                        	DSL Actual Delay Down
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_actual_delay_up
                        
                        	DSL Actual Delay Up
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_actual_down
                        
                        	DSL Actual Down
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_actual_up
                        
                        	DSL Actual Up
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_attain_down
                        
                        	DSL Attain Down
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_attain_up
                        
                        	DSL Attain Up
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_max_delay_down
                        
                        	DSL Max Delay Down
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_max_delay_up
                        
                        	DSL Max Delay Up
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_max_down
                        
                        	DSL Max Down
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_max_up
                        
                        	DSL Max Up
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_min_down
                        
                        	DSL Min Down
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_min_down_low
                        
                        	DSL Min Down Low
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_min_up
                        
                        	DSL Min Up
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_min_up_low
                        
                        	DSL Min Up Low
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: host_uniq
                        
                        	Host Uniq
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: is_iwf
                        
                        	Is IWF
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: max_payload
                        
                        	Max Payload
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: relay_session_id
                        
                        	Relay Session ID
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: remote_id
                        
                        	Remote ID
                        	**type**\:  str
                        
                        .. attribute:: service_name
                        
                        	Service Name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.Interfaces.Interface.Tags, self).__init__()

                            self.yang_name = "tags"
                            self.yang_parent_name = "interface"

                            self.circuit_id = YLeaf(YType.str, "circuit-id")

                            self.dsl_actual_delay_down = YLeaf(YType.uint32, "dsl-actual-delay-down")

                            self.dsl_actual_delay_up = YLeaf(YType.uint32, "dsl-actual-delay-up")

                            self.dsl_actual_down = YLeaf(YType.uint32, "dsl-actual-down")

                            self.dsl_actual_up = YLeaf(YType.uint32, "dsl-actual-up")

                            self.dsl_attain_down = YLeaf(YType.uint32, "dsl-attain-down")

                            self.dsl_attain_up = YLeaf(YType.uint32, "dsl-attain-up")

                            self.dsl_max_delay_down = YLeaf(YType.uint32, "dsl-max-delay-down")

                            self.dsl_max_delay_up = YLeaf(YType.uint32, "dsl-max-delay-up")

                            self.dsl_max_down = YLeaf(YType.uint32, "dsl-max-down")

                            self.dsl_max_up = YLeaf(YType.uint32, "dsl-max-up")

                            self.dsl_min_down = YLeaf(YType.uint32, "dsl-min-down")

                            self.dsl_min_down_low = YLeaf(YType.uint32, "dsl-min-down-low")

                            self.dsl_min_up = YLeaf(YType.uint32, "dsl-min-up")

                            self.dsl_min_up_low = YLeaf(YType.uint32, "dsl-min-up-low")

                            self.host_uniq = YLeaf(YType.str, "host-uniq")

                            self.is_iwf = YLeaf(YType.int32, "is-iwf")

                            self.max_payload = YLeaf(YType.uint16, "max-payload")

                            self.relay_session_id = YLeaf(YType.str, "relay-session-id")

                            self.remote_id = YLeaf(YType.str, "remote-id")

                            self.service_name = YLeaf(YType.str, "service-name")

                            self.access_loop_encapsulation = Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation()
                            self.access_loop_encapsulation.parent = self
                            self._children_name_map["access_loop_encapsulation"] = "access-loop-encapsulation"
                            self._children_yang_names.add("access-loop-encapsulation")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("circuit_id",
                                            "dsl_actual_delay_down",
                                            "dsl_actual_delay_up",
                                            "dsl_actual_down",
                                            "dsl_actual_up",
                                            "dsl_attain_down",
                                            "dsl_attain_up",
                                            "dsl_max_delay_down",
                                            "dsl_max_delay_up",
                                            "dsl_max_down",
                                            "dsl_max_up",
                                            "dsl_min_down",
                                            "dsl_min_down_low",
                                            "dsl_min_up",
                                            "dsl_min_up_low",
                                            "host_uniq",
                                            "is_iwf",
                                            "max_payload",
                                            "relay_session_id",
                                            "remote_id",
                                            "service_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Pppoe.Nodes.Node.Interfaces.Interface.Tags, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pppoe.Nodes.Node.Interfaces.Interface.Tags, self).__setattr__(name, value)


                        class AccessLoopEncapsulation(Entity):
                            """
                            Access Loop Encapsulation
                            
                            .. attribute:: data_link
                            
                            	Data Link
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: encaps1
                            
                            	Encaps 1
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: encaps2
                            
                            	Encaps 2
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation, self).__init__()

                                self.yang_name = "access-loop-encapsulation"
                                self.yang_parent_name = "tags"

                                self.data_link = YLeaf(YType.uint8, "data-link")

                                self.encaps1 = YLeaf(YType.uint8, "encaps1")

                                self.encaps2 = YLeaf(YType.uint8, "encaps2")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("data_link",
                                                "encaps1",
                                                "encaps2") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.data_link.is_set or
                                    self.encaps1.is_set or
                                    self.encaps2.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.data_link.yfilter != YFilter.not_set or
                                    self.encaps1.yfilter != YFilter.not_set or
                                    self.encaps2.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "access-loop-encapsulation" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.data_link.is_set or self.data_link.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.data_link.get_name_leafdata())
                                if (self.encaps1.is_set or self.encaps1.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.encaps1.get_name_leafdata())
                                if (self.encaps2.is_set or self.encaps2.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.encaps2.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "data-link" or name == "encaps1" or name == "encaps2"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "data-link"):
                                    self.data_link = value
                                    self.data_link.value_namespace = name_space
                                    self.data_link.value_namespace_prefix = name_space_prefix
                                if(value_path == "encaps1"):
                                    self.encaps1 = value
                                    self.encaps1.value_namespace = name_space
                                    self.encaps1.value_namespace_prefix = name_space_prefix
                                if(value_path == "encaps2"):
                                    self.encaps2 = value
                                    self.encaps2.value_namespace = name_space
                                    self.encaps2.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.circuit_id.is_set or
                                self.dsl_actual_delay_down.is_set or
                                self.dsl_actual_delay_up.is_set or
                                self.dsl_actual_down.is_set or
                                self.dsl_actual_up.is_set or
                                self.dsl_attain_down.is_set or
                                self.dsl_attain_up.is_set or
                                self.dsl_max_delay_down.is_set or
                                self.dsl_max_delay_up.is_set or
                                self.dsl_max_down.is_set or
                                self.dsl_max_up.is_set or
                                self.dsl_min_down.is_set or
                                self.dsl_min_down_low.is_set or
                                self.dsl_min_up.is_set or
                                self.dsl_min_up_low.is_set or
                                self.host_uniq.is_set or
                                self.is_iwf.is_set or
                                self.max_payload.is_set or
                                self.relay_session_id.is_set or
                                self.remote_id.is_set or
                                self.service_name.is_set or
                                (self.access_loop_encapsulation is not None and self.access_loop_encapsulation.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.circuit_id.yfilter != YFilter.not_set or
                                self.dsl_actual_delay_down.yfilter != YFilter.not_set or
                                self.dsl_actual_delay_up.yfilter != YFilter.not_set or
                                self.dsl_actual_down.yfilter != YFilter.not_set or
                                self.dsl_actual_up.yfilter != YFilter.not_set or
                                self.dsl_attain_down.yfilter != YFilter.not_set or
                                self.dsl_attain_up.yfilter != YFilter.not_set or
                                self.dsl_max_delay_down.yfilter != YFilter.not_set or
                                self.dsl_max_delay_up.yfilter != YFilter.not_set or
                                self.dsl_max_down.yfilter != YFilter.not_set or
                                self.dsl_max_up.yfilter != YFilter.not_set or
                                self.dsl_min_down.yfilter != YFilter.not_set or
                                self.dsl_min_down_low.yfilter != YFilter.not_set or
                                self.dsl_min_up.yfilter != YFilter.not_set or
                                self.dsl_min_up_low.yfilter != YFilter.not_set or
                                self.host_uniq.yfilter != YFilter.not_set or
                                self.is_iwf.yfilter != YFilter.not_set or
                                self.max_payload.yfilter != YFilter.not_set or
                                self.relay_session_id.yfilter != YFilter.not_set or
                                self.remote_id.yfilter != YFilter.not_set or
                                self.service_name.yfilter != YFilter.not_set or
                                (self.access_loop_encapsulation is not None and self.access_loop_encapsulation.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tags" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.circuit_id.is_set or self.circuit_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.circuit_id.get_name_leafdata())
                            if (self.dsl_actual_delay_down.is_set or self.dsl_actual_delay_down.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dsl_actual_delay_down.get_name_leafdata())
                            if (self.dsl_actual_delay_up.is_set or self.dsl_actual_delay_up.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dsl_actual_delay_up.get_name_leafdata())
                            if (self.dsl_actual_down.is_set or self.dsl_actual_down.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dsl_actual_down.get_name_leafdata())
                            if (self.dsl_actual_up.is_set or self.dsl_actual_up.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dsl_actual_up.get_name_leafdata())
                            if (self.dsl_attain_down.is_set or self.dsl_attain_down.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dsl_attain_down.get_name_leafdata())
                            if (self.dsl_attain_up.is_set or self.dsl_attain_up.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dsl_attain_up.get_name_leafdata())
                            if (self.dsl_max_delay_down.is_set or self.dsl_max_delay_down.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dsl_max_delay_down.get_name_leafdata())
                            if (self.dsl_max_delay_up.is_set or self.dsl_max_delay_up.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dsl_max_delay_up.get_name_leafdata())
                            if (self.dsl_max_down.is_set or self.dsl_max_down.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dsl_max_down.get_name_leafdata())
                            if (self.dsl_max_up.is_set or self.dsl_max_up.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dsl_max_up.get_name_leafdata())
                            if (self.dsl_min_down.is_set or self.dsl_min_down.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dsl_min_down.get_name_leafdata())
                            if (self.dsl_min_down_low.is_set or self.dsl_min_down_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dsl_min_down_low.get_name_leafdata())
                            if (self.dsl_min_up.is_set or self.dsl_min_up.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dsl_min_up.get_name_leafdata())
                            if (self.dsl_min_up_low.is_set or self.dsl_min_up_low.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dsl_min_up_low.get_name_leafdata())
                            if (self.host_uniq.is_set or self.host_uniq.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.host_uniq.get_name_leafdata())
                            if (self.is_iwf.is_set or self.is_iwf.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_iwf.get_name_leafdata())
                            if (self.max_payload.is_set or self.max_payload.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.max_payload.get_name_leafdata())
                            if (self.relay_session_id.is_set or self.relay_session_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.relay_session_id.get_name_leafdata())
                            if (self.remote_id.is_set or self.remote_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.remote_id.get_name_leafdata())
                            if (self.service_name.is_set or self.service_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.service_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "access-loop-encapsulation"):
                                if (self.access_loop_encapsulation is None):
                                    self.access_loop_encapsulation = Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation()
                                    self.access_loop_encapsulation.parent = self
                                    self._children_name_map["access_loop_encapsulation"] = "access-loop-encapsulation"
                                return self.access_loop_encapsulation

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "access-loop-encapsulation" or name == "circuit-id" or name == "dsl-actual-delay-down" or name == "dsl-actual-delay-up" or name == "dsl-actual-down" or name == "dsl-actual-up" or name == "dsl-attain-down" or name == "dsl-attain-up" or name == "dsl-max-delay-down" or name == "dsl-max-delay-up" or name == "dsl-max-down" or name == "dsl-max-up" or name == "dsl-min-down" or name == "dsl-min-down-low" or name == "dsl-min-up" or name == "dsl-min-up-low" or name == "host-uniq" or name == "is-iwf" or name == "max-payload" or name == "relay-session-id" or name == "remote-id" or name == "service-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "circuit-id"):
                                self.circuit_id = value
                                self.circuit_id.value_namespace = name_space
                                self.circuit_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "dsl-actual-delay-down"):
                                self.dsl_actual_delay_down = value
                                self.dsl_actual_delay_down.value_namespace = name_space
                                self.dsl_actual_delay_down.value_namespace_prefix = name_space_prefix
                            if(value_path == "dsl-actual-delay-up"):
                                self.dsl_actual_delay_up = value
                                self.dsl_actual_delay_up.value_namespace = name_space
                                self.dsl_actual_delay_up.value_namespace_prefix = name_space_prefix
                            if(value_path == "dsl-actual-down"):
                                self.dsl_actual_down = value
                                self.dsl_actual_down.value_namespace = name_space
                                self.dsl_actual_down.value_namespace_prefix = name_space_prefix
                            if(value_path == "dsl-actual-up"):
                                self.dsl_actual_up = value
                                self.dsl_actual_up.value_namespace = name_space
                                self.dsl_actual_up.value_namespace_prefix = name_space_prefix
                            if(value_path == "dsl-attain-down"):
                                self.dsl_attain_down = value
                                self.dsl_attain_down.value_namespace = name_space
                                self.dsl_attain_down.value_namespace_prefix = name_space_prefix
                            if(value_path == "dsl-attain-up"):
                                self.dsl_attain_up = value
                                self.dsl_attain_up.value_namespace = name_space
                                self.dsl_attain_up.value_namespace_prefix = name_space_prefix
                            if(value_path == "dsl-max-delay-down"):
                                self.dsl_max_delay_down = value
                                self.dsl_max_delay_down.value_namespace = name_space
                                self.dsl_max_delay_down.value_namespace_prefix = name_space_prefix
                            if(value_path == "dsl-max-delay-up"):
                                self.dsl_max_delay_up = value
                                self.dsl_max_delay_up.value_namespace = name_space
                                self.dsl_max_delay_up.value_namespace_prefix = name_space_prefix
                            if(value_path == "dsl-max-down"):
                                self.dsl_max_down = value
                                self.dsl_max_down.value_namespace = name_space
                                self.dsl_max_down.value_namespace_prefix = name_space_prefix
                            if(value_path == "dsl-max-up"):
                                self.dsl_max_up = value
                                self.dsl_max_up.value_namespace = name_space
                                self.dsl_max_up.value_namespace_prefix = name_space_prefix
                            if(value_path == "dsl-min-down"):
                                self.dsl_min_down = value
                                self.dsl_min_down.value_namespace = name_space
                                self.dsl_min_down.value_namespace_prefix = name_space_prefix
                            if(value_path == "dsl-min-down-low"):
                                self.dsl_min_down_low = value
                                self.dsl_min_down_low.value_namespace = name_space
                                self.dsl_min_down_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "dsl-min-up"):
                                self.dsl_min_up = value
                                self.dsl_min_up.value_namespace = name_space
                                self.dsl_min_up.value_namespace_prefix = name_space_prefix
                            if(value_path == "dsl-min-up-low"):
                                self.dsl_min_up_low = value
                                self.dsl_min_up_low.value_namespace = name_space
                                self.dsl_min_up_low.value_namespace_prefix = name_space_prefix
                            if(value_path == "host-uniq"):
                                self.host_uniq = value
                                self.host_uniq.value_namespace = name_space
                                self.host_uniq.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-iwf"):
                                self.is_iwf = value
                                self.is_iwf.value_namespace = name_space
                                self.is_iwf.value_namespace_prefix = name_space_prefix
                            if(value_path == "max-payload"):
                                self.max_payload = value
                                self.max_payload.value_namespace = name_space
                                self.max_payload.value_namespace_prefix = name_space_prefix
                            if(value_path == "relay-session-id"):
                                self.relay_session_id = value
                                self.relay_session_id.value_namespace = name_space
                                self.relay_session_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "remote-id"):
                                self.remote_id = value
                                self.remote_id.value_namespace = name_space
                                self.remote_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "service-name"):
                                self.service_name = value
                                self.service_name.value_namespace = name_space
                                self.service_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.access_interface_name.is_set or
                            self.bba_group_name.is_set or
                            self.interface_name_xr.is_set or
                            self.is_complete.is_set or
                            self.local_mac_address.is_set or
                            self.peer_mac_address.is_set or
                            self.session_id.is_set or
                            self.srg_state.is_set or
                            self.vlan_inner_id.is_set or
                            self.vlan_outer_id.is_set or
                            (self.tags is not None and self.tags.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.access_interface_name.yfilter != YFilter.not_set or
                            self.bba_group_name.yfilter != YFilter.not_set or
                            self.interface_name_xr.yfilter != YFilter.not_set or
                            self.is_complete.yfilter != YFilter.not_set or
                            self.local_mac_address.yfilter != YFilter.not_set or
                            self.peer_mac_address.yfilter != YFilter.not_set or
                            self.session_id.yfilter != YFilter.not_set or
                            self.srg_state.yfilter != YFilter.not_set or
                            self.vlan_inner_id.yfilter != YFilter.not_set or
                            self.vlan_outer_id.yfilter != YFilter.not_set or
                            (self.tags is not None and self.tags.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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
                        if (self.access_interface_name.is_set or self.access_interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_interface_name.get_name_leafdata())
                        if (self.bba_group_name.is_set or self.bba_group_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bba_group_name.get_name_leafdata())
                        if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name_xr.get_name_leafdata())
                        if (self.is_complete.is_set or self.is_complete.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_complete.get_name_leafdata())
                        if (self.local_mac_address.is_set or self.local_mac_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_mac_address.get_name_leafdata())
                        if (self.peer_mac_address.is_set or self.peer_mac_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_mac_address.get_name_leafdata())
                        if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_id.get_name_leafdata())
                        if (self.srg_state.is_set or self.srg_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srg_state.get_name_leafdata())
                        if (self.vlan_inner_id.is_set or self.vlan_inner_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vlan_inner_id.get_name_leafdata())
                        if (self.vlan_outer_id.is_set or self.vlan_outer_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vlan_outer_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "tags"):
                            if (self.tags is None):
                                self.tags = Pppoe.Nodes.Node.Interfaces.Interface.Tags()
                                self.tags.parent = self
                                self._children_name_map["tags"] = "tags"
                            return self.tags

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "tags" or name == "interface-name" or name == "access-interface-name" or name == "bba-group-name" or name == "interface-name-xr" or name == "is-complete" or name == "local-mac-address" or name == "peer-mac-address" or name == "session-id" or name == "srg-state" or name == "vlan-inner-id" or name == "vlan-outer-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "access-interface-name"):
                            self.access_interface_name = value
                            self.access_interface_name.value_namespace = name_space
                            self.access_interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "bba-group-name"):
                            self.bba_group_name = value
                            self.bba_group_name.value_namespace = name_space
                            self.bba_group_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name-xr"):
                            self.interface_name_xr = value
                            self.interface_name_xr.value_namespace = name_space
                            self.interface_name_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-complete"):
                            self.is_complete = value
                            self.is_complete.value_namespace = name_space
                            self.is_complete.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-mac-address"):
                            self.local_mac_address = value
                            self.local_mac_address.value_namespace = name_space
                            self.local_mac_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-mac-address"):
                            self.peer_mac_address = value
                            self.peer_mac_address.value_namespace = name_space
                            self.peer_mac_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-id"):
                            self.session_id = value
                            self.session_id.value_namespace = name_space
                            self.session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "srg-state"):
                            self.srg_state = value
                            self.srg_state.value_namespace = name_space
                            self.srg_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "vlan-inner-id"):
                            self.vlan_inner_id = value
                            self.vlan_inner_id.value_namespace = name_space
                            self.vlan_inner_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "vlan-outer-id"):
                            self.vlan_outer_id = value
                            self.vlan_outer_id.value_namespace = name_space
                            self.vlan_outer_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interfaces" + path_buffer

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

                    if (child_yang_name == "interface"):
                        for c in self.interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Pppoe.Nodes.Node.Interfaces.Interface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class BbaGroups(Entity):
                """
                PPPoE BBA\-Group information
                
                .. attribute:: bba_group
                
                	PPPoE BBA\-Group information
                	**type**\: list of    :py:class:`BbaGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Pppoe.Nodes.Node.BbaGroups, self).__init__()

                    self.yang_name = "bba-groups"
                    self.yang_parent_name = "node"

                    self.bba_group = YList(self)

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
                                super(Pppoe.Nodes.Node.BbaGroups, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Pppoe.Nodes.Node.BbaGroups, self).__setattr__(name, value)


                class BbaGroup(Entity):
                    """
                    PPPoE BBA\-Group information
                    
                    .. attribute:: bba_group_name  <key>
                    
                    	BBA Group
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: limit_config
                    
                    	BBA\-Group limit configuration information
                    	**type**\:   :py:class:`LimitConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig>`
                    
                    .. attribute:: limits
                    
                    	PPPoE session limit information
                    	**type**\:   :py:class:`Limits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits>`
                    
                    .. attribute:: throttle_config
                    
                    	BBA\-Group throttle configuration information
                    	**type**\:   :py:class:`ThrottleConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig>`
                    
                    .. attribute:: throttles
                    
                    	PPPoE throttle information
                    	**type**\:   :py:class:`Throttles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup, self).__init__()

                        self.yang_name = "bba-group"
                        self.yang_parent_name = "bba-groups"

                        self.bba_group_name = YLeaf(YType.str, "bba-group-name")

                        self.limit_config = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig()
                        self.limit_config.parent = self
                        self._children_name_map["limit_config"] = "limit-config"
                        self._children_yang_names.add("limit-config")

                        self.limits = Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits()
                        self.limits.parent = self
                        self._children_name_map["limits"] = "limits"
                        self._children_yang_names.add("limits")

                        self.throttle_config = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig()
                        self.throttle_config.parent = self
                        self._children_name_map["throttle_config"] = "throttle-config"
                        self._children_yang_names.add("throttle-config")

                        self.throttles = Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles()
                        self.throttles.parent = self
                        self._children_name_map["throttles"] = "throttles"
                        self._children_yang_names.add("throttles")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("bba_group_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Pppoe.Nodes.Node.BbaGroups.BbaGroup, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup, self).__setattr__(name, value)


                    class LimitConfig(Entity):
                        """
                        BBA\-Group limit configuration information
                        
                        .. attribute:: access_intf
                        
                        	Access Interface
                        	**type**\:   :py:class:`AccessIntf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf>`
                        
                        .. attribute:: card
                        
                        	Card
                        	**type**\:   :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card>`
                        
                        .. attribute:: circuit_id
                        
                        	Circuit ID
                        	**type**\:   :py:class:`CircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId>`
                        
                        .. attribute:: circuit_id_and_remote_id
                        
                        	Circuit ID and Remote ID
                        	**type**\:   :py:class:`CircuitIdAndRemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId>`
                        
                        .. attribute:: inner_vlan_id
                        
                        	Inner VLAN ID
                        	**type**\:   :py:class:`InnerVlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId>`
                        
                        .. attribute:: mac
                        
                        	MAC
                        	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac>`
                        
                        .. attribute:: mac_access_interface
                        
                        	MAC Access Interface
                        	**type**\:   :py:class:`MacAccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface>`
                        
                        .. attribute:: mac_iwf
                        
                        	MAC IWF
                        	**type**\:   :py:class:`MacIwf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf>`
                        
                        .. attribute:: mac_iwf_access_interface
                        
                        	MAC IWF Access Interface
                        	**type**\:   :py:class:`MacIwfAccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface>`
                        
                        .. attribute:: outer_vlan_id
                        
                        	Outer VLAN ID
                        	**type**\:   :py:class:`OuterVlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId>`
                        
                        .. attribute:: remote_id
                        
                        	Remote ID
                        	**type**\:   :py:class:`RemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId>`
                        
                        .. attribute:: vlan_id
                        
                        	VLAN ID
                        	**type**\:   :py:class:`VlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId>`
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig, self).__init__()

                            self.yang_name = "limit-config"
                            self.yang_parent_name = "bba-group"

                            self.access_intf = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf()
                            self.access_intf.parent = self
                            self._children_name_map["access_intf"] = "access-intf"
                            self._children_yang_names.add("access-intf")

                            self.card = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card()
                            self.card.parent = self
                            self._children_name_map["card"] = "card"
                            self._children_yang_names.add("card")

                            self.circuit_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId()
                            self.circuit_id.parent = self
                            self._children_name_map["circuit_id"] = "circuit-id"
                            self._children_yang_names.add("circuit-id")

                            self.circuit_id_and_remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId()
                            self.circuit_id_and_remote_id.parent = self
                            self._children_name_map["circuit_id_and_remote_id"] = "circuit-id-and-remote-id"
                            self._children_yang_names.add("circuit-id-and-remote-id")

                            self.inner_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId()
                            self.inner_vlan_id.parent = self
                            self._children_name_map["inner_vlan_id"] = "inner-vlan-id"
                            self._children_yang_names.add("inner-vlan-id")

                            self.mac = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac()
                            self.mac.parent = self
                            self._children_name_map["mac"] = "mac"
                            self._children_yang_names.add("mac")

                            self.mac_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface()
                            self.mac_access_interface.parent = self
                            self._children_name_map["mac_access_interface"] = "mac-access-interface"
                            self._children_yang_names.add("mac-access-interface")

                            self.mac_iwf = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf()
                            self.mac_iwf.parent = self
                            self._children_name_map["mac_iwf"] = "mac-iwf"
                            self._children_yang_names.add("mac-iwf")

                            self.mac_iwf_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface()
                            self.mac_iwf_access_interface.parent = self
                            self._children_name_map["mac_iwf_access_interface"] = "mac-iwf-access-interface"
                            self._children_yang_names.add("mac-iwf-access-interface")

                            self.outer_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId()
                            self.outer_vlan_id.parent = self
                            self._children_name_map["outer_vlan_id"] = "outer-vlan-id"
                            self._children_yang_names.add("outer-vlan-id")

                            self.remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId()
                            self.remote_id.parent = self
                            self._children_name_map["remote_id"] = "remote-id"
                            self._children_yang_names.add("remote-id")

                            self.vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId()
                            self.vlan_id.parent = self
                            self._children_name_map["vlan_id"] = "vlan-id"
                            self._children_yang_names.add("vlan-id")


                        class Card(Entity):
                            """
                            Card
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card, self).__init__()

                                self.yang_name = "card"
                                self.yang_parent_name = "limit-config"

                                self.max_limit = YLeaf(YType.uint32, "max-limit")

                                self.radius_override_enabled = YLeaf(YType.int32, "radius-override-enabled")

                                self.threshold = YLeaf(YType.uint32, "threshold")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("max_limit",
                                                "radius_override_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.max_limit.is_set or
                                    self.radius_override_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.max_limit.yfilter != YFilter.not_set or
                                    self.radius_override_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "card" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.max_limit.is_set or self.max_limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_limit.get_name_leafdata())
                                if (self.radius_override_enabled.is_set or self.radius_override_enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.radius_override_enabled.get_name_leafdata())
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "max-limit" or name == "radius-override-enabled" or name == "threshold"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "max-limit"):
                                    self.max_limit = value
                                    self.max_limit.value_namespace = name_space
                                    self.max_limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "radius-override-enabled"):
                                    self.radius_override_enabled = value
                                    self.radius_override_enabled.value_namespace = name_space
                                    self.radius_override_enabled.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


                        class AccessIntf(Entity):
                            """
                            Access Interface
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf, self).__init__()

                                self.yang_name = "access-intf"
                                self.yang_parent_name = "limit-config"

                                self.max_limit = YLeaf(YType.uint32, "max-limit")

                                self.radius_override_enabled = YLeaf(YType.int32, "radius-override-enabled")

                                self.threshold = YLeaf(YType.uint32, "threshold")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("max_limit",
                                                "radius_override_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.max_limit.is_set or
                                    self.radius_override_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.max_limit.yfilter != YFilter.not_set or
                                    self.radius_override_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "access-intf" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.max_limit.is_set or self.max_limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_limit.get_name_leafdata())
                                if (self.radius_override_enabled.is_set or self.radius_override_enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.radius_override_enabled.get_name_leafdata())
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "max-limit" or name == "radius-override-enabled" or name == "threshold"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "max-limit"):
                                    self.max_limit = value
                                    self.max_limit.value_namespace = name_space
                                    self.max_limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "radius-override-enabled"):
                                    self.radius_override_enabled = value
                                    self.radius_override_enabled.value_namespace = name_space
                                    self.radius_override_enabled.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


                        class Mac(Entity):
                            """
                            MAC
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac, self).__init__()

                                self.yang_name = "mac"
                                self.yang_parent_name = "limit-config"

                                self.max_limit = YLeaf(YType.uint32, "max-limit")

                                self.radius_override_enabled = YLeaf(YType.int32, "radius-override-enabled")

                                self.threshold = YLeaf(YType.uint32, "threshold")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("max_limit",
                                                "radius_override_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.max_limit.is_set or
                                    self.radius_override_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.max_limit.yfilter != YFilter.not_set or
                                    self.radius_override_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mac" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.max_limit.is_set or self.max_limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_limit.get_name_leafdata())
                                if (self.radius_override_enabled.is_set or self.radius_override_enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.radius_override_enabled.get_name_leafdata())
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "max-limit" or name == "radius-override-enabled" or name == "threshold"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "max-limit"):
                                    self.max_limit = value
                                    self.max_limit.value_namespace = name_space
                                    self.max_limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "radius-override-enabled"):
                                    self.radius_override_enabled = value
                                    self.radius_override_enabled.value_namespace = name_space
                                    self.radius_override_enabled.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


                        class MacIwf(Entity):
                            """
                            MAC IWF
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf, self).__init__()

                                self.yang_name = "mac-iwf"
                                self.yang_parent_name = "limit-config"

                                self.max_limit = YLeaf(YType.uint32, "max-limit")

                                self.radius_override_enabled = YLeaf(YType.int32, "radius-override-enabled")

                                self.threshold = YLeaf(YType.uint32, "threshold")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("max_limit",
                                                "radius_override_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.max_limit.is_set or
                                    self.radius_override_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.max_limit.yfilter != YFilter.not_set or
                                    self.radius_override_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mac-iwf" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.max_limit.is_set or self.max_limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_limit.get_name_leafdata())
                                if (self.radius_override_enabled.is_set or self.radius_override_enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.radius_override_enabled.get_name_leafdata())
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "max-limit" or name == "radius-override-enabled" or name == "threshold"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "max-limit"):
                                    self.max_limit = value
                                    self.max_limit.value_namespace = name_space
                                    self.max_limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "radius-override-enabled"):
                                    self.radius_override_enabled = value
                                    self.radius_override_enabled.value_namespace = name_space
                                    self.radius_override_enabled.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


                        class MacAccessInterface(Entity):
                            """
                            MAC Access Interface
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface, self).__init__()

                                self.yang_name = "mac-access-interface"
                                self.yang_parent_name = "limit-config"

                                self.max_limit = YLeaf(YType.uint32, "max-limit")

                                self.radius_override_enabled = YLeaf(YType.int32, "radius-override-enabled")

                                self.threshold = YLeaf(YType.uint32, "threshold")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("max_limit",
                                                "radius_override_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.max_limit.is_set or
                                    self.radius_override_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.max_limit.yfilter != YFilter.not_set or
                                    self.radius_override_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mac-access-interface" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.max_limit.is_set or self.max_limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_limit.get_name_leafdata())
                                if (self.radius_override_enabled.is_set or self.radius_override_enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.radius_override_enabled.get_name_leafdata())
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "max-limit" or name == "radius-override-enabled" or name == "threshold"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "max-limit"):
                                    self.max_limit = value
                                    self.max_limit.value_namespace = name_space
                                    self.max_limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "radius-override-enabled"):
                                    self.radius_override_enabled = value
                                    self.radius_override_enabled.value_namespace = name_space
                                    self.radius_override_enabled.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


                        class MacIwfAccessInterface(Entity):
                            """
                            MAC IWF Access Interface
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface, self).__init__()

                                self.yang_name = "mac-iwf-access-interface"
                                self.yang_parent_name = "limit-config"

                                self.max_limit = YLeaf(YType.uint32, "max-limit")

                                self.radius_override_enabled = YLeaf(YType.int32, "radius-override-enabled")

                                self.threshold = YLeaf(YType.uint32, "threshold")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("max_limit",
                                                "radius_override_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.max_limit.is_set or
                                    self.radius_override_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.max_limit.yfilter != YFilter.not_set or
                                    self.radius_override_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mac-iwf-access-interface" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.max_limit.is_set or self.max_limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_limit.get_name_leafdata())
                                if (self.radius_override_enabled.is_set or self.radius_override_enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.radius_override_enabled.get_name_leafdata())
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "max-limit" or name == "radius-override-enabled" or name == "threshold"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "max-limit"):
                                    self.max_limit = value
                                    self.max_limit.value_namespace = name_space
                                    self.max_limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "radius-override-enabled"):
                                    self.radius_override_enabled = value
                                    self.radius_override_enabled.value_namespace = name_space
                                    self.radius_override_enabled.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


                        class CircuitId(Entity):
                            """
                            Circuit ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId, self).__init__()

                                self.yang_name = "circuit-id"
                                self.yang_parent_name = "limit-config"

                                self.max_limit = YLeaf(YType.uint32, "max-limit")

                                self.radius_override_enabled = YLeaf(YType.int32, "radius-override-enabled")

                                self.threshold = YLeaf(YType.uint32, "threshold")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("max_limit",
                                                "radius_override_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.max_limit.is_set or
                                    self.radius_override_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.max_limit.yfilter != YFilter.not_set or
                                    self.radius_override_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "circuit-id" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.max_limit.is_set or self.max_limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_limit.get_name_leafdata())
                                if (self.radius_override_enabled.is_set or self.radius_override_enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.radius_override_enabled.get_name_leafdata())
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "max-limit" or name == "radius-override-enabled" or name == "threshold"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "max-limit"):
                                    self.max_limit = value
                                    self.max_limit.value_namespace = name_space
                                    self.max_limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "radius-override-enabled"):
                                    self.radius_override_enabled = value
                                    self.radius_override_enabled.value_namespace = name_space
                                    self.radius_override_enabled.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


                        class RemoteId(Entity):
                            """
                            Remote ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId, self).__init__()

                                self.yang_name = "remote-id"
                                self.yang_parent_name = "limit-config"

                                self.max_limit = YLeaf(YType.uint32, "max-limit")

                                self.radius_override_enabled = YLeaf(YType.int32, "radius-override-enabled")

                                self.threshold = YLeaf(YType.uint32, "threshold")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("max_limit",
                                                "radius_override_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.max_limit.is_set or
                                    self.radius_override_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.max_limit.yfilter != YFilter.not_set or
                                    self.radius_override_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "remote-id" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.max_limit.is_set or self.max_limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_limit.get_name_leafdata())
                                if (self.radius_override_enabled.is_set or self.radius_override_enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.radius_override_enabled.get_name_leafdata())
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "max-limit" or name == "radius-override-enabled" or name == "threshold"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "max-limit"):
                                    self.max_limit = value
                                    self.max_limit.value_namespace = name_space
                                    self.max_limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "radius-override-enabled"):
                                    self.radius_override_enabled = value
                                    self.radius_override_enabled.value_namespace = name_space
                                    self.radius_override_enabled.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


                        class CircuitIdAndRemoteId(Entity):
                            """
                            Circuit ID and Remote ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId, self).__init__()

                                self.yang_name = "circuit-id-and-remote-id"
                                self.yang_parent_name = "limit-config"

                                self.max_limit = YLeaf(YType.uint32, "max-limit")

                                self.radius_override_enabled = YLeaf(YType.int32, "radius-override-enabled")

                                self.threshold = YLeaf(YType.uint32, "threshold")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("max_limit",
                                                "radius_override_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.max_limit.is_set or
                                    self.radius_override_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.max_limit.yfilter != YFilter.not_set or
                                    self.radius_override_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "circuit-id-and-remote-id" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.max_limit.is_set or self.max_limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_limit.get_name_leafdata())
                                if (self.radius_override_enabled.is_set or self.radius_override_enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.radius_override_enabled.get_name_leafdata())
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "max-limit" or name == "radius-override-enabled" or name == "threshold"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "max-limit"):
                                    self.max_limit = value
                                    self.max_limit.value_namespace = name_space
                                    self.max_limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "radius-override-enabled"):
                                    self.radius_override_enabled = value
                                    self.radius_override_enabled.value_namespace = name_space
                                    self.radius_override_enabled.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


                        class OuterVlanId(Entity):
                            """
                            Outer VLAN ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId, self).__init__()

                                self.yang_name = "outer-vlan-id"
                                self.yang_parent_name = "limit-config"

                                self.max_limit = YLeaf(YType.uint32, "max-limit")

                                self.radius_override_enabled = YLeaf(YType.int32, "radius-override-enabled")

                                self.threshold = YLeaf(YType.uint32, "threshold")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("max_limit",
                                                "radius_override_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.max_limit.is_set or
                                    self.radius_override_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.max_limit.yfilter != YFilter.not_set or
                                    self.radius_override_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "outer-vlan-id" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.max_limit.is_set or self.max_limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_limit.get_name_leafdata())
                                if (self.radius_override_enabled.is_set or self.radius_override_enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.radius_override_enabled.get_name_leafdata())
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "max-limit" or name == "radius-override-enabled" or name == "threshold"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "max-limit"):
                                    self.max_limit = value
                                    self.max_limit.value_namespace = name_space
                                    self.max_limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "radius-override-enabled"):
                                    self.radius_override_enabled = value
                                    self.radius_override_enabled.value_namespace = name_space
                                    self.radius_override_enabled.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


                        class InnerVlanId(Entity):
                            """
                            Inner VLAN ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId, self).__init__()

                                self.yang_name = "inner-vlan-id"
                                self.yang_parent_name = "limit-config"

                                self.max_limit = YLeaf(YType.uint32, "max-limit")

                                self.radius_override_enabled = YLeaf(YType.int32, "radius-override-enabled")

                                self.threshold = YLeaf(YType.uint32, "threshold")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("max_limit",
                                                "radius_override_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.max_limit.is_set or
                                    self.radius_override_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.max_limit.yfilter != YFilter.not_set or
                                    self.radius_override_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "inner-vlan-id" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.max_limit.is_set or self.max_limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_limit.get_name_leafdata())
                                if (self.radius_override_enabled.is_set or self.radius_override_enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.radius_override_enabled.get_name_leafdata())
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "max-limit" or name == "radius-override-enabled" or name == "threshold"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "max-limit"):
                                    self.max_limit = value
                                    self.max_limit.value_namespace = name_space
                                    self.max_limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "radius-override-enabled"):
                                    self.radius_override_enabled = value
                                    self.radius_override_enabled.value_namespace = name_space
                                    self.radius_override_enabled.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix


                        class VlanId(Entity):
                            """
                            VLAN ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId, self).__init__()

                                self.yang_name = "vlan-id"
                                self.yang_parent_name = "limit-config"

                                self.max_limit = YLeaf(YType.uint32, "max-limit")

                                self.radius_override_enabled = YLeaf(YType.int32, "radius-override-enabled")

                                self.threshold = YLeaf(YType.uint32, "threshold")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("max_limit",
                                                "radius_override_enabled",
                                                "threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.max_limit.is_set or
                                    self.radius_override_enabled.is_set or
                                    self.threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.max_limit.yfilter != YFilter.not_set or
                                    self.radius_override_enabled.yfilter != YFilter.not_set or
                                    self.threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "vlan-id" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.max_limit.is_set or self.max_limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max_limit.get_name_leafdata())
                                if (self.radius_override_enabled.is_set or self.radius_override_enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.radius_override_enabled.get_name_leafdata())
                                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "max-limit" or name == "radius-override-enabled" or name == "threshold"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "max-limit"):
                                    self.max_limit = value
                                    self.max_limit.value_namespace = name_space
                                    self.max_limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "radius-override-enabled"):
                                    self.radius_override_enabled = value
                                    self.radius_override_enabled.value_namespace = name_space
                                    self.radius_override_enabled.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold"):
                                    self.threshold = value
                                    self.threshold.value_namespace = name_space
                                    self.threshold.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.access_intf is not None and self.access_intf.has_data()) or
                                (self.card is not None and self.card.has_data()) or
                                (self.circuit_id is not None and self.circuit_id.has_data()) or
                                (self.circuit_id_and_remote_id is not None and self.circuit_id_and_remote_id.has_data()) or
                                (self.inner_vlan_id is not None and self.inner_vlan_id.has_data()) or
                                (self.mac is not None and self.mac.has_data()) or
                                (self.mac_access_interface is not None and self.mac_access_interface.has_data()) or
                                (self.mac_iwf is not None and self.mac_iwf.has_data()) or
                                (self.mac_iwf_access_interface is not None and self.mac_iwf_access_interface.has_data()) or
                                (self.outer_vlan_id is not None and self.outer_vlan_id.has_data()) or
                                (self.remote_id is not None and self.remote_id.has_data()) or
                                (self.vlan_id is not None and self.vlan_id.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.access_intf is not None and self.access_intf.has_operation()) or
                                (self.card is not None and self.card.has_operation()) or
                                (self.circuit_id is not None and self.circuit_id.has_operation()) or
                                (self.circuit_id_and_remote_id is not None and self.circuit_id_and_remote_id.has_operation()) or
                                (self.inner_vlan_id is not None and self.inner_vlan_id.has_operation()) or
                                (self.mac is not None and self.mac.has_operation()) or
                                (self.mac_access_interface is not None and self.mac_access_interface.has_operation()) or
                                (self.mac_iwf is not None and self.mac_iwf.has_operation()) or
                                (self.mac_iwf_access_interface is not None and self.mac_iwf_access_interface.has_operation()) or
                                (self.outer_vlan_id is not None and self.outer_vlan_id.has_operation()) or
                                (self.remote_id is not None and self.remote_id.has_operation()) or
                                (self.vlan_id is not None and self.vlan_id.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "limit-config" + path_buffer

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

                            if (child_yang_name == "access-intf"):
                                if (self.access_intf is None):
                                    self.access_intf = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf()
                                    self.access_intf.parent = self
                                    self._children_name_map["access_intf"] = "access-intf"
                                return self.access_intf

                            if (child_yang_name == "card"):
                                if (self.card is None):
                                    self.card = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card()
                                    self.card.parent = self
                                    self._children_name_map["card"] = "card"
                                return self.card

                            if (child_yang_name == "circuit-id"):
                                if (self.circuit_id is None):
                                    self.circuit_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId()
                                    self.circuit_id.parent = self
                                    self._children_name_map["circuit_id"] = "circuit-id"
                                return self.circuit_id

                            if (child_yang_name == "circuit-id-and-remote-id"):
                                if (self.circuit_id_and_remote_id is None):
                                    self.circuit_id_and_remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId()
                                    self.circuit_id_and_remote_id.parent = self
                                    self._children_name_map["circuit_id_and_remote_id"] = "circuit-id-and-remote-id"
                                return self.circuit_id_and_remote_id

                            if (child_yang_name == "inner-vlan-id"):
                                if (self.inner_vlan_id is None):
                                    self.inner_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId()
                                    self.inner_vlan_id.parent = self
                                    self._children_name_map["inner_vlan_id"] = "inner-vlan-id"
                                return self.inner_vlan_id

                            if (child_yang_name == "mac"):
                                if (self.mac is None):
                                    self.mac = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac()
                                    self.mac.parent = self
                                    self._children_name_map["mac"] = "mac"
                                return self.mac

                            if (child_yang_name == "mac-access-interface"):
                                if (self.mac_access_interface is None):
                                    self.mac_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface()
                                    self.mac_access_interface.parent = self
                                    self._children_name_map["mac_access_interface"] = "mac-access-interface"
                                return self.mac_access_interface

                            if (child_yang_name == "mac-iwf"):
                                if (self.mac_iwf is None):
                                    self.mac_iwf = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf()
                                    self.mac_iwf.parent = self
                                    self._children_name_map["mac_iwf"] = "mac-iwf"
                                return self.mac_iwf

                            if (child_yang_name == "mac-iwf-access-interface"):
                                if (self.mac_iwf_access_interface is None):
                                    self.mac_iwf_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface()
                                    self.mac_iwf_access_interface.parent = self
                                    self._children_name_map["mac_iwf_access_interface"] = "mac-iwf-access-interface"
                                return self.mac_iwf_access_interface

                            if (child_yang_name == "outer-vlan-id"):
                                if (self.outer_vlan_id is None):
                                    self.outer_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId()
                                    self.outer_vlan_id.parent = self
                                    self._children_name_map["outer_vlan_id"] = "outer-vlan-id"
                                return self.outer_vlan_id

                            if (child_yang_name == "remote-id"):
                                if (self.remote_id is None):
                                    self.remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId()
                                    self.remote_id.parent = self
                                    self._children_name_map["remote_id"] = "remote-id"
                                return self.remote_id

                            if (child_yang_name == "vlan-id"):
                                if (self.vlan_id is None):
                                    self.vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId()
                                    self.vlan_id.parent = self
                                    self._children_name_map["vlan_id"] = "vlan-id"
                                return self.vlan_id

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "access-intf" or name == "card" or name == "circuit-id" or name == "circuit-id-and-remote-id" or name == "inner-vlan-id" or name == "mac" or name == "mac-access-interface" or name == "mac-iwf" or name == "mac-iwf-access-interface" or name == "outer-vlan-id" or name == "remote-id" or name == "vlan-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Limits(Entity):
                        """
                        PPPoE session limit information
                        
                        .. attribute:: limit
                        
                        	PPPoE session limit state
                        	**type**\: list of    :py:class:`Limit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit>`
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits, self).__init__()

                            self.yang_name = "limits"
                            self.yang_parent_name = "bba-group"

                            self.limit = YList(self)

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
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits, self).__setattr__(name, value)


                        class Limit(Entity):
                            """
                            PPPoE session limit state
                            
                            .. attribute:: circuit_id
                            
                            	Circuit ID
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: inner_vlan_id
                            
                            	Inner VLAN ID
                            	**type**\:  int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: interface_name
                            
                            	Access Interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: iwf
                            
                            	IWF flag
                            	**type**\:  bool
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: outer_vlan_id
                            
                            	Outer VLAN ID
                            	**type**\:  int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: override_limit
                            
                            	Overridden limit if set
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_set
                            
                            	Overridden limit has been set
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: session_count
                            
                            	Session Count
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: state
                            
                            	State
                            	**type**\:   :py:class:`PppoeMaLimitState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaLimitState>`
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit, self).__init__()

                                self.yang_name = "limit"
                                self.yang_parent_name = "limits"

                                self.circuit_id = YLeaf(YType.str, "circuit-id")

                                self.inner_vlan_id = YLeaf(YType.uint32, "inner-vlan-id")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.iwf = YLeaf(YType.boolean, "iwf")

                                self.mac_address = YLeaf(YType.str, "mac-address")

                                self.outer_vlan_id = YLeaf(YType.uint32, "outer-vlan-id")

                                self.override_limit = YLeaf(YType.uint32, "override-limit")

                                self.radius_override_set = YLeaf(YType.int32, "radius-override-set")

                                self.remote_id = YLeaf(YType.str, "remote-id")

                                self.session_count = YLeaf(YType.uint32, "session-count")

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
                                    if name in ("circuit_id",
                                                "inner_vlan_id",
                                                "interface_name",
                                                "iwf",
                                                "mac_address",
                                                "outer_vlan_id",
                                                "override_limit",
                                                "radius_override_set",
                                                "remote_id",
                                                "session_count",
                                                "state") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.circuit_id.is_set or
                                    self.inner_vlan_id.is_set or
                                    self.interface_name.is_set or
                                    self.iwf.is_set or
                                    self.mac_address.is_set or
                                    self.outer_vlan_id.is_set or
                                    self.override_limit.is_set or
                                    self.radius_override_set.is_set or
                                    self.remote_id.is_set or
                                    self.session_count.is_set or
                                    self.state.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.circuit_id.yfilter != YFilter.not_set or
                                    self.inner_vlan_id.yfilter != YFilter.not_set or
                                    self.interface_name.yfilter != YFilter.not_set or
                                    self.iwf.yfilter != YFilter.not_set or
                                    self.mac_address.yfilter != YFilter.not_set or
                                    self.outer_vlan_id.yfilter != YFilter.not_set or
                                    self.override_limit.yfilter != YFilter.not_set or
                                    self.radius_override_set.yfilter != YFilter.not_set or
                                    self.remote_id.yfilter != YFilter.not_set or
                                    self.session_count.yfilter != YFilter.not_set or
                                    self.state.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "limit" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.circuit_id.is_set or self.circuit_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.circuit_id.get_name_leafdata())
                                if (self.inner_vlan_id.is_set or self.inner_vlan_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.inner_vlan_id.get_name_leafdata())
                                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                                if (self.iwf.is_set or self.iwf.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.iwf.get_name_leafdata())
                                if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mac_address.get_name_leafdata())
                                if (self.outer_vlan_id.is_set or self.outer_vlan_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.outer_vlan_id.get_name_leafdata())
                                if (self.override_limit.is_set or self.override_limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.override_limit.get_name_leafdata())
                                if (self.radius_override_set.is_set or self.radius_override_set.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.radius_override_set.get_name_leafdata())
                                if (self.remote_id.is_set or self.remote_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.remote_id.get_name_leafdata())
                                if (self.session_count.is_set or self.session_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_count.get_name_leafdata())
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
                                if(name == "circuit-id" or name == "inner-vlan-id" or name == "interface-name" or name == "iwf" or name == "mac-address" or name == "outer-vlan-id" or name == "override-limit" or name == "radius-override-set" or name == "remote-id" or name == "session-count" or name == "state"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "circuit-id"):
                                    self.circuit_id = value
                                    self.circuit_id.value_namespace = name_space
                                    self.circuit_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "inner-vlan-id"):
                                    self.inner_vlan_id = value
                                    self.inner_vlan_id.value_namespace = name_space
                                    self.inner_vlan_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "interface-name"):
                                    self.interface_name = value
                                    self.interface_name.value_namespace = name_space
                                    self.interface_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "iwf"):
                                    self.iwf = value
                                    self.iwf.value_namespace = name_space
                                    self.iwf.value_namespace_prefix = name_space_prefix
                                if(value_path == "mac-address"):
                                    self.mac_address = value
                                    self.mac_address.value_namespace = name_space
                                    self.mac_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "outer-vlan-id"):
                                    self.outer_vlan_id = value
                                    self.outer_vlan_id.value_namespace = name_space
                                    self.outer_vlan_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "override-limit"):
                                    self.override_limit = value
                                    self.override_limit.value_namespace = name_space
                                    self.override_limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "radius-override-set"):
                                    self.radius_override_set = value
                                    self.radius_override_set.value_namespace = name_space
                                    self.radius_override_set.value_namespace_prefix = name_space_prefix
                                if(value_path == "remote-id"):
                                    self.remote_id = value
                                    self.remote_id.value_namespace = name_space
                                    self.remote_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "session-count"):
                                    self.session_count = value
                                    self.session_count.value_namespace = name_space
                                    self.session_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "state"):
                                    self.state = value
                                    self.state.value_namespace = name_space
                                    self.state.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.limit:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.limit:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "limits" + path_buffer

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

                            if (child_yang_name == "limit"):
                                for c in self.limit:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.limit.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "limit"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Throttles(Entity):
                        """
                        PPPoE throttle information
                        
                        .. attribute:: throttle
                        
                        	PPPoE session throttle state
                        	**type**\: list of    :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle>`
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles, self).__init__()

                            self.yang_name = "throttles"
                            self.yang_parent_name = "bba-group"

                            self.throttle = YList(self)

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
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles, self).__setattr__(name, value)


                        class Throttle(Entity):
                            """
                            PPPoE session throttle state
                            
                            .. attribute:: circuit_id
                            
                            	Circuit ID
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: inner_vlan_id
                            
                            	Inner VLAN ID
                            	**type**\:  int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: interface_name
                            
                            	Access Interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: iwf
                            
                            	IWF flag
                            	**type**\:  bool
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: outer_vlan_id
                            
                            	Outer VLAN ID
                            	**type**\:  int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: padi_count
                            
                            	PADI Count
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: padr_count
                            
                            	PADR Count
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: since_reset
                            
                            	Number of seconds since counters reset
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: state
                            
                            	State
                            	**type**\:   :py:class:`PppoeMaThrottleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaThrottleState>`
                            
                            .. attribute:: time_left
                            
                            	Time left in seconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle, self).__init__()

                                self.yang_name = "throttle"
                                self.yang_parent_name = "throttles"

                                self.circuit_id = YLeaf(YType.str, "circuit-id")

                                self.inner_vlan_id = YLeaf(YType.uint32, "inner-vlan-id")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.iwf = YLeaf(YType.boolean, "iwf")

                                self.mac_address = YLeaf(YType.str, "mac-address")

                                self.outer_vlan_id = YLeaf(YType.uint32, "outer-vlan-id")

                                self.padi_count = YLeaf(YType.uint32, "padi-count")

                                self.padr_count = YLeaf(YType.uint32, "padr-count")

                                self.remote_id = YLeaf(YType.str, "remote-id")

                                self.since_reset = YLeaf(YType.uint32, "since-reset")

                                self.state = YLeaf(YType.enumeration, "state")

                                self.time_left = YLeaf(YType.uint32, "time-left")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("circuit_id",
                                                "inner_vlan_id",
                                                "interface_name",
                                                "iwf",
                                                "mac_address",
                                                "outer_vlan_id",
                                                "padi_count",
                                                "padr_count",
                                                "remote_id",
                                                "since_reset",
                                                "state",
                                                "time_left") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.circuit_id.is_set or
                                    self.inner_vlan_id.is_set or
                                    self.interface_name.is_set or
                                    self.iwf.is_set or
                                    self.mac_address.is_set or
                                    self.outer_vlan_id.is_set or
                                    self.padi_count.is_set or
                                    self.padr_count.is_set or
                                    self.remote_id.is_set or
                                    self.since_reset.is_set or
                                    self.state.is_set or
                                    self.time_left.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.circuit_id.yfilter != YFilter.not_set or
                                    self.inner_vlan_id.yfilter != YFilter.not_set or
                                    self.interface_name.yfilter != YFilter.not_set or
                                    self.iwf.yfilter != YFilter.not_set or
                                    self.mac_address.yfilter != YFilter.not_set or
                                    self.outer_vlan_id.yfilter != YFilter.not_set or
                                    self.padi_count.yfilter != YFilter.not_set or
                                    self.padr_count.yfilter != YFilter.not_set or
                                    self.remote_id.yfilter != YFilter.not_set or
                                    self.since_reset.yfilter != YFilter.not_set or
                                    self.state.yfilter != YFilter.not_set or
                                    self.time_left.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "throttle" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.circuit_id.is_set or self.circuit_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.circuit_id.get_name_leafdata())
                                if (self.inner_vlan_id.is_set or self.inner_vlan_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.inner_vlan_id.get_name_leafdata())
                                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                                if (self.iwf.is_set or self.iwf.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.iwf.get_name_leafdata())
                                if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mac_address.get_name_leafdata())
                                if (self.outer_vlan_id.is_set or self.outer_vlan_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.outer_vlan_id.get_name_leafdata())
                                if (self.padi_count.is_set or self.padi_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.padi_count.get_name_leafdata())
                                if (self.padr_count.is_set or self.padr_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.padr_count.get_name_leafdata())
                                if (self.remote_id.is_set or self.remote_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.remote_id.get_name_leafdata())
                                if (self.since_reset.is_set or self.since_reset.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.since_reset.get_name_leafdata())
                                if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.state.get_name_leafdata())
                                if (self.time_left.is_set or self.time_left.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_left.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "circuit-id" or name == "inner-vlan-id" or name == "interface-name" or name == "iwf" or name == "mac-address" or name == "outer-vlan-id" or name == "padi-count" or name == "padr-count" or name == "remote-id" or name == "since-reset" or name == "state" or name == "time-left"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "circuit-id"):
                                    self.circuit_id = value
                                    self.circuit_id.value_namespace = name_space
                                    self.circuit_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "inner-vlan-id"):
                                    self.inner_vlan_id = value
                                    self.inner_vlan_id.value_namespace = name_space
                                    self.inner_vlan_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "interface-name"):
                                    self.interface_name = value
                                    self.interface_name.value_namespace = name_space
                                    self.interface_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "iwf"):
                                    self.iwf = value
                                    self.iwf.value_namespace = name_space
                                    self.iwf.value_namespace_prefix = name_space_prefix
                                if(value_path == "mac-address"):
                                    self.mac_address = value
                                    self.mac_address.value_namespace = name_space
                                    self.mac_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "outer-vlan-id"):
                                    self.outer_vlan_id = value
                                    self.outer_vlan_id.value_namespace = name_space
                                    self.outer_vlan_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "padi-count"):
                                    self.padi_count = value
                                    self.padi_count.value_namespace = name_space
                                    self.padi_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "padr-count"):
                                    self.padr_count = value
                                    self.padr_count.value_namespace = name_space
                                    self.padr_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "remote-id"):
                                    self.remote_id = value
                                    self.remote_id.value_namespace = name_space
                                    self.remote_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "since-reset"):
                                    self.since_reset = value
                                    self.since_reset.value_namespace = name_space
                                    self.since_reset.value_namespace_prefix = name_space_prefix
                                if(value_path == "state"):
                                    self.state = value
                                    self.state.value_namespace = name_space
                                    self.state.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-left"):
                                    self.time_left = value
                                    self.time_left.value_namespace = name_space
                                    self.time_left.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.throttle:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.throttle:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "throttles" + path_buffer

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

                            if (child_yang_name == "throttle"):
                                for c in self.throttle:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.throttle.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "throttle"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class ThrottleConfig(Entity):
                        """
                        BBA\-Group throttle configuration information
                        
                        .. attribute:: circuit_id
                        
                        	Circuit ID
                        	**type**\:   :py:class:`CircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId>`
                        
                        .. attribute:: circuit_id_and_remote_id
                        
                        	Circuit ID and Remote ID
                        	**type**\:   :py:class:`CircuitIdAndRemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId>`
                        
                        .. attribute:: inner_vlan_id
                        
                        	Inner VLAN ID
                        	**type**\:   :py:class:`InnerVlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId>`
                        
                        .. attribute:: mac
                        
                        	MAC
                        	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac>`
                        
                        .. attribute:: mac_access_interface
                        
                        	MAC Access Interface
                        	**type**\:   :py:class:`MacAccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface>`
                        
                        .. attribute:: mac_iwf_access_interface
                        
                        	MAC IWF Access Interface
                        	**type**\:   :py:class:`MacIwfAccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface>`
                        
                        .. attribute:: outer_vlan_id
                        
                        	Outer VLAN ID
                        	**type**\:   :py:class:`OuterVlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId>`
                        
                        .. attribute:: remote_id
                        
                        	Remote ID
                        	**type**\:   :py:class:`RemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId>`
                        
                        .. attribute:: vlan_id
                        
                        	VLAN ID
                        	**type**\:   :py:class:`VlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId>`
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig, self).__init__()

                            self.yang_name = "throttle-config"
                            self.yang_parent_name = "bba-group"

                            self.circuit_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId()
                            self.circuit_id.parent = self
                            self._children_name_map["circuit_id"] = "circuit-id"
                            self._children_yang_names.add("circuit-id")

                            self.circuit_id_and_remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId()
                            self.circuit_id_and_remote_id.parent = self
                            self._children_name_map["circuit_id_and_remote_id"] = "circuit-id-and-remote-id"
                            self._children_yang_names.add("circuit-id-and-remote-id")

                            self.inner_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId()
                            self.inner_vlan_id.parent = self
                            self._children_name_map["inner_vlan_id"] = "inner-vlan-id"
                            self._children_yang_names.add("inner-vlan-id")

                            self.mac = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac()
                            self.mac.parent = self
                            self._children_name_map["mac"] = "mac"
                            self._children_yang_names.add("mac")

                            self.mac_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface()
                            self.mac_access_interface.parent = self
                            self._children_name_map["mac_access_interface"] = "mac-access-interface"
                            self._children_yang_names.add("mac-access-interface")

                            self.mac_iwf_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface()
                            self.mac_iwf_access_interface.parent = self
                            self._children_name_map["mac_iwf_access_interface"] = "mac-iwf-access-interface"
                            self._children_yang_names.add("mac-iwf-access-interface")

                            self.outer_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId()
                            self.outer_vlan_id.parent = self
                            self._children_name_map["outer_vlan_id"] = "outer-vlan-id"
                            self._children_yang_names.add("outer-vlan-id")

                            self.remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId()
                            self.remote_id.parent = self
                            self._children_name_map["remote_id"] = "remote-id"
                            self._children_yang_names.add("remote-id")

                            self.vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId()
                            self.vlan_id.parent = self
                            self._children_name_map["vlan_id"] = "vlan-id"
                            self._children_yang_names.add("vlan-id")


                        class Mac(Entity):
                            """
                            MAC
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac, self).__init__()

                                self.yang_name = "mac"
                                self.yang_parent_name = "throttle-config"

                                self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                                self.limit = YLeaf(YType.uint32, "limit")

                                self.request_period = YLeaf(YType.uint32, "request-period")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("blocking_period",
                                                "limit",
                                                "request_period") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.blocking_period.is_set or
                                    self.limit.is_set or
                                    self.request_period.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.blocking_period.yfilter != YFilter.not_set or
                                    self.limit.yfilter != YFilter.not_set or
                                    self.request_period.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mac" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.blocking_period.get_name_leafdata())
                                if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.limit.get_name_leafdata())
                                if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.request_period.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "blocking-period" or name == "limit" or name == "request-period"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "blocking-period"):
                                    self.blocking_period = value
                                    self.blocking_period.value_namespace = name_space
                                    self.blocking_period.value_namespace_prefix = name_space_prefix
                                if(value_path == "limit"):
                                    self.limit = value
                                    self.limit.value_namespace = name_space
                                    self.limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "request-period"):
                                    self.request_period = value
                                    self.request_period.value_namespace = name_space
                                    self.request_period.value_namespace_prefix = name_space_prefix


                        class MacAccessInterface(Entity):
                            """
                            MAC Access Interface
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface, self).__init__()

                                self.yang_name = "mac-access-interface"
                                self.yang_parent_name = "throttle-config"

                                self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                                self.limit = YLeaf(YType.uint32, "limit")

                                self.request_period = YLeaf(YType.uint32, "request-period")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("blocking_period",
                                                "limit",
                                                "request_period") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.blocking_period.is_set or
                                    self.limit.is_set or
                                    self.request_period.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.blocking_period.yfilter != YFilter.not_set or
                                    self.limit.yfilter != YFilter.not_set or
                                    self.request_period.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mac-access-interface" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.blocking_period.get_name_leafdata())
                                if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.limit.get_name_leafdata())
                                if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.request_period.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "blocking-period" or name == "limit" or name == "request-period"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "blocking-period"):
                                    self.blocking_period = value
                                    self.blocking_period.value_namespace = name_space
                                    self.blocking_period.value_namespace_prefix = name_space_prefix
                                if(value_path == "limit"):
                                    self.limit = value
                                    self.limit.value_namespace = name_space
                                    self.limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "request-period"):
                                    self.request_period = value
                                    self.request_period.value_namespace = name_space
                                    self.request_period.value_namespace_prefix = name_space_prefix


                        class MacIwfAccessInterface(Entity):
                            """
                            MAC IWF Access Interface
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface, self).__init__()

                                self.yang_name = "mac-iwf-access-interface"
                                self.yang_parent_name = "throttle-config"

                                self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                                self.limit = YLeaf(YType.uint32, "limit")

                                self.request_period = YLeaf(YType.uint32, "request-period")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("blocking_period",
                                                "limit",
                                                "request_period") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.blocking_period.is_set or
                                    self.limit.is_set or
                                    self.request_period.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.blocking_period.yfilter != YFilter.not_set or
                                    self.limit.yfilter != YFilter.not_set or
                                    self.request_period.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mac-iwf-access-interface" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.blocking_period.get_name_leafdata())
                                if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.limit.get_name_leafdata())
                                if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.request_period.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "blocking-period" or name == "limit" or name == "request-period"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "blocking-period"):
                                    self.blocking_period = value
                                    self.blocking_period.value_namespace = name_space
                                    self.blocking_period.value_namespace_prefix = name_space_prefix
                                if(value_path == "limit"):
                                    self.limit = value
                                    self.limit.value_namespace = name_space
                                    self.limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "request-period"):
                                    self.request_period = value
                                    self.request_period.value_namespace = name_space
                                    self.request_period.value_namespace_prefix = name_space_prefix


                        class CircuitId(Entity):
                            """
                            Circuit ID
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId, self).__init__()

                                self.yang_name = "circuit-id"
                                self.yang_parent_name = "throttle-config"

                                self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                                self.limit = YLeaf(YType.uint32, "limit")

                                self.request_period = YLeaf(YType.uint32, "request-period")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("blocking_period",
                                                "limit",
                                                "request_period") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.blocking_period.is_set or
                                    self.limit.is_set or
                                    self.request_period.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.blocking_period.yfilter != YFilter.not_set or
                                    self.limit.yfilter != YFilter.not_set or
                                    self.request_period.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "circuit-id" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.blocking_period.get_name_leafdata())
                                if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.limit.get_name_leafdata())
                                if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.request_period.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "blocking-period" or name == "limit" or name == "request-period"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "blocking-period"):
                                    self.blocking_period = value
                                    self.blocking_period.value_namespace = name_space
                                    self.blocking_period.value_namespace_prefix = name_space_prefix
                                if(value_path == "limit"):
                                    self.limit = value
                                    self.limit.value_namespace = name_space
                                    self.limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "request-period"):
                                    self.request_period = value
                                    self.request_period.value_namespace = name_space
                                    self.request_period.value_namespace_prefix = name_space_prefix


                        class RemoteId(Entity):
                            """
                            Remote ID
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId, self).__init__()

                                self.yang_name = "remote-id"
                                self.yang_parent_name = "throttle-config"

                                self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                                self.limit = YLeaf(YType.uint32, "limit")

                                self.request_period = YLeaf(YType.uint32, "request-period")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("blocking_period",
                                                "limit",
                                                "request_period") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.blocking_period.is_set or
                                    self.limit.is_set or
                                    self.request_period.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.blocking_period.yfilter != YFilter.not_set or
                                    self.limit.yfilter != YFilter.not_set or
                                    self.request_period.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "remote-id" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.blocking_period.get_name_leafdata())
                                if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.limit.get_name_leafdata())
                                if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.request_period.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "blocking-period" or name == "limit" or name == "request-period"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "blocking-period"):
                                    self.blocking_period = value
                                    self.blocking_period.value_namespace = name_space
                                    self.blocking_period.value_namespace_prefix = name_space_prefix
                                if(value_path == "limit"):
                                    self.limit = value
                                    self.limit.value_namespace = name_space
                                    self.limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "request-period"):
                                    self.request_period = value
                                    self.request_period.value_namespace = name_space
                                    self.request_period.value_namespace_prefix = name_space_prefix


                        class CircuitIdAndRemoteId(Entity):
                            """
                            Circuit ID and Remote ID
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId, self).__init__()

                                self.yang_name = "circuit-id-and-remote-id"
                                self.yang_parent_name = "throttle-config"

                                self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                                self.limit = YLeaf(YType.uint32, "limit")

                                self.request_period = YLeaf(YType.uint32, "request-period")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("blocking_period",
                                                "limit",
                                                "request_period") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.blocking_period.is_set or
                                    self.limit.is_set or
                                    self.request_period.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.blocking_period.yfilter != YFilter.not_set or
                                    self.limit.yfilter != YFilter.not_set or
                                    self.request_period.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "circuit-id-and-remote-id" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.blocking_period.get_name_leafdata())
                                if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.limit.get_name_leafdata())
                                if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.request_period.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "blocking-period" or name == "limit" or name == "request-period"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "blocking-period"):
                                    self.blocking_period = value
                                    self.blocking_period.value_namespace = name_space
                                    self.blocking_period.value_namespace_prefix = name_space_prefix
                                if(value_path == "limit"):
                                    self.limit = value
                                    self.limit.value_namespace = name_space
                                    self.limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "request-period"):
                                    self.request_period = value
                                    self.request_period.value_namespace = name_space
                                    self.request_period.value_namespace_prefix = name_space_prefix


                        class OuterVlanId(Entity):
                            """
                            Outer VLAN ID
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId, self).__init__()

                                self.yang_name = "outer-vlan-id"
                                self.yang_parent_name = "throttle-config"

                                self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                                self.limit = YLeaf(YType.uint32, "limit")

                                self.request_period = YLeaf(YType.uint32, "request-period")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("blocking_period",
                                                "limit",
                                                "request_period") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.blocking_period.is_set or
                                    self.limit.is_set or
                                    self.request_period.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.blocking_period.yfilter != YFilter.not_set or
                                    self.limit.yfilter != YFilter.not_set or
                                    self.request_period.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "outer-vlan-id" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.blocking_period.get_name_leafdata())
                                if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.limit.get_name_leafdata())
                                if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.request_period.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "blocking-period" or name == "limit" or name == "request-period"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "blocking-period"):
                                    self.blocking_period = value
                                    self.blocking_period.value_namespace = name_space
                                    self.blocking_period.value_namespace_prefix = name_space_prefix
                                if(value_path == "limit"):
                                    self.limit = value
                                    self.limit.value_namespace = name_space
                                    self.limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "request-period"):
                                    self.request_period = value
                                    self.request_period.value_namespace = name_space
                                    self.request_period.value_namespace_prefix = name_space_prefix


                        class InnerVlanId(Entity):
                            """
                            Inner VLAN ID
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId, self).__init__()

                                self.yang_name = "inner-vlan-id"
                                self.yang_parent_name = "throttle-config"

                                self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                                self.limit = YLeaf(YType.uint32, "limit")

                                self.request_period = YLeaf(YType.uint32, "request-period")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("blocking_period",
                                                "limit",
                                                "request_period") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.blocking_period.is_set or
                                    self.limit.is_set or
                                    self.request_period.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.blocking_period.yfilter != YFilter.not_set or
                                    self.limit.yfilter != YFilter.not_set or
                                    self.request_period.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "inner-vlan-id" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.blocking_period.get_name_leafdata())
                                if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.limit.get_name_leafdata())
                                if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.request_period.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "blocking-period" or name == "limit" or name == "request-period"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "blocking-period"):
                                    self.blocking_period = value
                                    self.blocking_period.value_namespace = name_space
                                    self.blocking_period.value_namespace_prefix = name_space_prefix
                                if(value_path == "limit"):
                                    self.limit = value
                                    self.limit.value_namespace = name_space
                                    self.limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "request-period"):
                                    self.request_period = value
                                    self.request_period.value_namespace = name_space
                                    self.request_period.value_namespace_prefix = name_space_prefix


                        class VlanId(Entity):
                            """
                            VLAN ID
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId, self).__init__()

                                self.yang_name = "vlan-id"
                                self.yang_parent_name = "throttle-config"

                                self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                                self.limit = YLeaf(YType.uint32, "limit")

                                self.request_period = YLeaf(YType.uint32, "request-period")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("blocking_period",
                                                "limit",
                                                "request_period") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.blocking_period.is_set or
                                    self.limit.is_set or
                                    self.request_period.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.blocking_period.yfilter != YFilter.not_set or
                                    self.limit.yfilter != YFilter.not_set or
                                    self.request_period.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "vlan-id" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.blocking_period.get_name_leafdata())
                                if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.limit.get_name_leafdata())
                                if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.request_period.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "blocking-period" or name == "limit" or name == "request-period"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "blocking-period"):
                                    self.blocking_period = value
                                    self.blocking_period.value_namespace = name_space
                                    self.blocking_period.value_namespace_prefix = name_space_prefix
                                if(value_path == "limit"):
                                    self.limit = value
                                    self.limit.value_namespace = name_space
                                    self.limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "request-period"):
                                    self.request_period = value
                                    self.request_period.value_namespace = name_space
                                    self.request_period.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.circuit_id is not None and self.circuit_id.has_data()) or
                                (self.circuit_id_and_remote_id is not None and self.circuit_id_and_remote_id.has_data()) or
                                (self.inner_vlan_id is not None and self.inner_vlan_id.has_data()) or
                                (self.mac is not None and self.mac.has_data()) or
                                (self.mac_access_interface is not None and self.mac_access_interface.has_data()) or
                                (self.mac_iwf_access_interface is not None and self.mac_iwf_access_interface.has_data()) or
                                (self.outer_vlan_id is not None and self.outer_vlan_id.has_data()) or
                                (self.remote_id is not None and self.remote_id.has_data()) or
                                (self.vlan_id is not None and self.vlan_id.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.circuit_id is not None and self.circuit_id.has_operation()) or
                                (self.circuit_id_and_remote_id is not None and self.circuit_id_and_remote_id.has_operation()) or
                                (self.inner_vlan_id is not None and self.inner_vlan_id.has_operation()) or
                                (self.mac is not None and self.mac.has_operation()) or
                                (self.mac_access_interface is not None and self.mac_access_interface.has_operation()) or
                                (self.mac_iwf_access_interface is not None and self.mac_iwf_access_interface.has_operation()) or
                                (self.outer_vlan_id is not None and self.outer_vlan_id.has_operation()) or
                                (self.remote_id is not None and self.remote_id.has_operation()) or
                                (self.vlan_id is not None and self.vlan_id.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "throttle-config" + path_buffer

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

                            if (child_yang_name == "circuit-id"):
                                if (self.circuit_id is None):
                                    self.circuit_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId()
                                    self.circuit_id.parent = self
                                    self._children_name_map["circuit_id"] = "circuit-id"
                                return self.circuit_id

                            if (child_yang_name == "circuit-id-and-remote-id"):
                                if (self.circuit_id_and_remote_id is None):
                                    self.circuit_id_and_remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId()
                                    self.circuit_id_and_remote_id.parent = self
                                    self._children_name_map["circuit_id_and_remote_id"] = "circuit-id-and-remote-id"
                                return self.circuit_id_and_remote_id

                            if (child_yang_name == "inner-vlan-id"):
                                if (self.inner_vlan_id is None):
                                    self.inner_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId()
                                    self.inner_vlan_id.parent = self
                                    self._children_name_map["inner_vlan_id"] = "inner-vlan-id"
                                return self.inner_vlan_id

                            if (child_yang_name == "mac"):
                                if (self.mac is None):
                                    self.mac = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac()
                                    self.mac.parent = self
                                    self._children_name_map["mac"] = "mac"
                                return self.mac

                            if (child_yang_name == "mac-access-interface"):
                                if (self.mac_access_interface is None):
                                    self.mac_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface()
                                    self.mac_access_interface.parent = self
                                    self._children_name_map["mac_access_interface"] = "mac-access-interface"
                                return self.mac_access_interface

                            if (child_yang_name == "mac-iwf-access-interface"):
                                if (self.mac_iwf_access_interface is None):
                                    self.mac_iwf_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface()
                                    self.mac_iwf_access_interface.parent = self
                                    self._children_name_map["mac_iwf_access_interface"] = "mac-iwf-access-interface"
                                return self.mac_iwf_access_interface

                            if (child_yang_name == "outer-vlan-id"):
                                if (self.outer_vlan_id is None):
                                    self.outer_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId()
                                    self.outer_vlan_id.parent = self
                                    self._children_name_map["outer_vlan_id"] = "outer-vlan-id"
                                return self.outer_vlan_id

                            if (child_yang_name == "remote-id"):
                                if (self.remote_id is None):
                                    self.remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId()
                                    self.remote_id.parent = self
                                    self._children_name_map["remote_id"] = "remote-id"
                                return self.remote_id

                            if (child_yang_name == "vlan-id"):
                                if (self.vlan_id is None):
                                    self.vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId()
                                    self.vlan_id.parent = self
                                    self._children_name_map["vlan_id"] = "vlan-id"
                                return self.vlan_id

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "circuit-id" or name == "circuit-id-and-remote-id" or name == "inner-vlan-id" or name == "mac" or name == "mac-access-interface" or name == "mac-iwf-access-interface" or name == "outer-vlan-id" or name == "remote-id" or name == "vlan-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.bba_group_name.is_set or
                            (self.limit_config is not None and self.limit_config.has_data()) or
                            (self.limits is not None and self.limits.has_data()) or
                            (self.throttle_config is not None and self.throttle_config.has_data()) or
                            (self.throttles is not None and self.throttles.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.bba_group_name.yfilter != YFilter.not_set or
                            (self.limit_config is not None and self.limit_config.has_operation()) or
                            (self.limits is not None and self.limits.has_operation()) or
                            (self.throttle_config is not None and self.throttle_config.has_operation()) or
                            (self.throttles is not None and self.throttles.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bba-group" + "[bba-group-name='" + self.bba_group_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.bba_group_name.is_set or self.bba_group_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bba_group_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "limit-config"):
                            if (self.limit_config is None):
                                self.limit_config = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig()
                                self.limit_config.parent = self
                                self._children_name_map["limit_config"] = "limit-config"
                            return self.limit_config

                        if (child_yang_name == "limits"):
                            if (self.limits is None):
                                self.limits = Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits()
                                self.limits.parent = self
                                self._children_name_map["limits"] = "limits"
                            return self.limits

                        if (child_yang_name == "throttle-config"):
                            if (self.throttle_config is None):
                                self.throttle_config = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig()
                                self.throttle_config.parent = self
                                self._children_name_map["throttle_config"] = "throttle-config"
                            return self.throttle_config

                        if (child_yang_name == "throttles"):
                            if (self.throttles is None):
                                self.throttles = Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles()
                                self.throttles.parent = self
                                self._children_name_map["throttles"] = "throttles"
                            return self.throttles

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "limit-config" or name == "limits" or name == "throttle-config" or name == "throttles" or name == "bba-group-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "bba-group-name"):
                            self.bba_group_name = value
                            self.bba_group_name.value_namespace = name_space
                            self.bba_group_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.bba_group:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.bba_group:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bba-groups" + path_buffer

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

                    if (child_yang_name == "bba-group"):
                        for c in self.bba_group:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Pppoe.Nodes.Node.BbaGroups.BbaGroup()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.bba_group.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bba-group"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class SummaryTotal(Entity):
                """
                PPPoE statistics for a given node
                
                .. attribute:: complete_sessions
                
                	Complete Session Count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: flow_control_disconnected_sessions
                
                	Flow Control Disconnected Count
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: flow_control_dropped_sessions
                
                	Flow Control Drop Count
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: flow_control_in_flight_sessions
                
                	Flow Control In\-Flight Count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: flow_control_limit
                
                	Flow Control credit limit
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: flow_control_successful_sessions
                
                	Flow Control Success Count, sessions completing call flow
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: incomplete_sessions
                
                	Incomplete Session Count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: not_ready_access_interfaces
                
                	Not Ready Access Interface Count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pppoema_subscriber_infra_flow_control
                
                	PPPoEMASubscriberInfraFlowControl
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ready_access_interfaces
                
                	Ready Access Interface Count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Pppoe.Nodes.Node.SummaryTotal, self).__init__()

                    self.yang_name = "summary-total"
                    self.yang_parent_name = "node"

                    self.complete_sessions = YLeaf(YType.uint32, "complete-sessions")

                    self.flow_control_disconnected_sessions = YLeaf(YType.uint64, "flow-control-disconnected-sessions")

                    self.flow_control_dropped_sessions = YLeaf(YType.uint64, "flow-control-dropped-sessions")

                    self.flow_control_in_flight_sessions = YLeaf(YType.uint32, "flow-control-in-flight-sessions")

                    self.flow_control_limit = YLeaf(YType.uint32, "flow-control-limit")

                    self.flow_control_successful_sessions = YLeaf(YType.uint64, "flow-control-successful-sessions")

                    self.incomplete_sessions = YLeaf(YType.uint32, "incomplete-sessions")

                    self.not_ready_access_interfaces = YLeaf(YType.uint32, "not-ready-access-interfaces")

                    self.pppoema_subscriber_infra_flow_control = YLeaf(YType.uint32, "pppoema-subscriber-infra-flow-control")

                    self.ready_access_interfaces = YLeaf(YType.uint32, "ready-access-interfaces")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("complete_sessions",
                                    "flow_control_disconnected_sessions",
                                    "flow_control_dropped_sessions",
                                    "flow_control_in_flight_sessions",
                                    "flow_control_limit",
                                    "flow_control_successful_sessions",
                                    "incomplete_sessions",
                                    "not_ready_access_interfaces",
                                    "pppoema_subscriber_infra_flow_control",
                                    "ready_access_interfaces") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Pppoe.Nodes.Node.SummaryTotal, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Pppoe.Nodes.Node.SummaryTotal, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.complete_sessions.is_set or
                        self.flow_control_disconnected_sessions.is_set or
                        self.flow_control_dropped_sessions.is_set or
                        self.flow_control_in_flight_sessions.is_set or
                        self.flow_control_limit.is_set or
                        self.flow_control_successful_sessions.is_set or
                        self.incomplete_sessions.is_set or
                        self.not_ready_access_interfaces.is_set or
                        self.pppoema_subscriber_infra_flow_control.is_set or
                        self.ready_access_interfaces.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.complete_sessions.yfilter != YFilter.not_set or
                        self.flow_control_disconnected_sessions.yfilter != YFilter.not_set or
                        self.flow_control_dropped_sessions.yfilter != YFilter.not_set or
                        self.flow_control_in_flight_sessions.yfilter != YFilter.not_set or
                        self.flow_control_limit.yfilter != YFilter.not_set or
                        self.flow_control_successful_sessions.yfilter != YFilter.not_set or
                        self.incomplete_sessions.yfilter != YFilter.not_set or
                        self.not_ready_access_interfaces.yfilter != YFilter.not_set or
                        self.pppoema_subscriber_infra_flow_control.yfilter != YFilter.not_set or
                        self.ready_access_interfaces.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "summary-total" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.complete_sessions.is_set or self.complete_sessions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.complete_sessions.get_name_leafdata())
                    if (self.flow_control_disconnected_sessions.is_set or self.flow_control_disconnected_sessions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flow_control_disconnected_sessions.get_name_leafdata())
                    if (self.flow_control_dropped_sessions.is_set or self.flow_control_dropped_sessions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flow_control_dropped_sessions.get_name_leafdata())
                    if (self.flow_control_in_flight_sessions.is_set or self.flow_control_in_flight_sessions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flow_control_in_flight_sessions.get_name_leafdata())
                    if (self.flow_control_limit.is_set or self.flow_control_limit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flow_control_limit.get_name_leafdata())
                    if (self.flow_control_successful_sessions.is_set or self.flow_control_successful_sessions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flow_control_successful_sessions.get_name_leafdata())
                    if (self.incomplete_sessions.is_set or self.incomplete_sessions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.incomplete_sessions.get_name_leafdata())
                    if (self.not_ready_access_interfaces.is_set or self.not_ready_access_interfaces.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.not_ready_access_interfaces.get_name_leafdata())
                    if (self.pppoema_subscriber_infra_flow_control.is_set or self.pppoema_subscriber_infra_flow_control.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pppoema_subscriber_infra_flow_control.get_name_leafdata())
                    if (self.ready_access_interfaces.is_set or self.ready_access_interfaces.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ready_access_interfaces.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "complete-sessions" or name == "flow-control-disconnected-sessions" or name == "flow-control-dropped-sessions" or name == "flow-control-in-flight-sessions" or name == "flow-control-limit" or name == "flow-control-successful-sessions" or name == "incomplete-sessions" or name == "not-ready-access-interfaces" or name == "pppoema-subscriber-infra-flow-control" or name == "ready-access-interfaces"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "complete-sessions"):
                        self.complete_sessions = value
                        self.complete_sessions.value_namespace = name_space
                        self.complete_sessions.value_namespace_prefix = name_space_prefix
                    if(value_path == "flow-control-disconnected-sessions"):
                        self.flow_control_disconnected_sessions = value
                        self.flow_control_disconnected_sessions.value_namespace = name_space
                        self.flow_control_disconnected_sessions.value_namespace_prefix = name_space_prefix
                    if(value_path == "flow-control-dropped-sessions"):
                        self.flow_control_dropped_sessions = value
                        self.flow_control_dropped_sessions.value_namespace = name_space
                        self.flow_control_dropped_sessions.value_namespace_prefix = name_space_prefix
                    if(value_path == "flow-control-in-flight-sessions"):
                        self.flow_control_in_flight_sessions = value
                        self.flow_control_in_flight_sessions.value_namespace = name_space
                        self.flow_control_in_flight_sessions.value_namespace_prefix = name_space_prefix
                    if(value_path == "flow-control-limit"):
                        self.flow_control_limit = value
                        self.flow_control_limit.value_namespace = name_space
                        self.flow_control_limit.value_namespace_prefix = name_space_prefix
                    if(value_path == "flow-control-successful-sessions"):
                        self.flow_control_successful_sessions = value
                        self.flow_control_successful_sessions.value_namespace = name_space
                        self.flow_control_successful_sessions.value_namespace_prefix = name_space_prefix
                    if(value_path == "incomplete-sessions"):
                        self.incomplete_sessions = value
                        self.incomplete_sessions.value_namespace = name_space
                        self.incomplete_sessions.value_namespace_prefix = name_space_prefix
                    if(value_path == "not-ready-access-interfaces"):
                        self.not_ready_access_interfaces = value
                        self.not_ready_access_interfaces.value_namespace = name_space
                        self.not_ready_access_interfaces.value_namespace_prefix = name_space_prefix
                    if(value_path == "pppoema-subscriber-infra-flow-control"):
                        self.pppoema_subscriber_infra_flow_control = value
                        self.pppoema_subscriber_infra_flow_control.value_namespace = name_space
                        self.pppoema_subscriber_infra_flow_control.value_namespace_prefix = name_space_prefix
                    if(value_path == "ready-access-interfaces"):
                        self.ready_access_interfaces = value
                        self.ready_access_interfaces.value_namespace = name_space
                        self.ready_access_interfaces.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.access_interface is not None and self.access_interface.has_data()) or
                    (self.bba_groups is not None and self.bba_groups.has_data()) or
                    (self.interfaces is not None and self.interfaces.has_data()) or
                    (self.statistics is not None and self.statistics.has_data()) or
                    (self.summary_total is not None and self.summary_total.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.access_interface is not None and self.access_interface.has_operation()) or
                    (self.bba_groups is not None and self.bba_groups.has_operation()) or
                    (self.interfaces is not None and self.interfaces.has_operation()) or
                    (self.statistics is not None and self.statistics.has_operation()) or
                    (self.summary_total is not None and self.summary_total.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "access-interface"):
                    if (self.access_interface is None):
                        self.access_interface = Pppoe.Nodes.Node.AccessInterface()
                        self.access_interface.parent = self
                        self._children_name_map["access_interface"] = "access-interface"
                    return self.access_interface

                if (child_yang_name == "bba-groups"):
                    if (self.bba_groups is None):
                        self.bba_groups = Pppoe.Nodes.Node.BbaGroups()
                        self.bba_groups.parent = self
                        self._children_name_map["bba_groups"] = "bba-groups"
                    return self.bba_groups

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = Pppoe.Nodes.Node.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                if (child_yang_name == "statistics"):
                    if (self.statistics is None):
                        self.statistics = Pppoe.Nodes.Node.Statistics()
                        self.statistics.parent = self
                        self._children_name_map["statistics"] = "statistics"
                    return self.statistics

                if (child_yang_name == "summary-total"):
                    if (self.summary_total is None):
                        self.summary_total = Pppoe.Nodes.Node.SummaryTotal()
                        self.summary_total.parent = self
                        self._children_name_map["summary_total"] = "summary-total"
                    return self.summary_total

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "access-interface" or name == "bba-groups" or name == "interfaces" or name == "statistics" or name == "summary-total" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe/%s" % self.get_segment_path()
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
                c = Pppoe.Nodes.Node()
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
        return (
            (self.access_interface_statistics is not None and self.access_interface_statistics.has_data()) or
            (self.nodes is not None and self.nodes.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.access_interface_statistics is not None and self.access_interface_statistics.has_operation()) or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe" + path_buffer

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

        if (child_yang_name == "access-interface-statistics"):
            if (self.access_interface_statistics is None):
                self.access_interface_statistics = Pppoe.AccessInterfaceStatistics()
                self.access_interface_statistics.parent = self
                self._children_name_map["access_interface_statistics"] = "access-interface-statistics"
            return self.access_interface_statistics

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = Pppoe.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "access-interface-statistics" or name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Pppoe()
        return self._top_entity

