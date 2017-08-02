""" Cisco_IOS_XR_asr9k_lc_fca_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-lc\-fca package operational data.

This module contains definitions
for the following management objects\:
  mpa\-internal\: Management LAN Operational data space
  mpa\: mpa

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SpaFailureReason(Enum):
    """
    SpaFailureReason

    SPA failure reasons

    .. data:: spa_failure_reason_unknown = 1

    	spa failure reason unknown

    .. data:: spa_failure_reason_spi_failure = 2

    	spa failure reason spi failure

    .. data:: spa_failure_reason_boot = 3

    	spa failure reason boot

    .. data:: spa_failure_reason_hw_failed = 4

    	spa failure reason hw failed

    .. data:: spa_failure_reason_sw_failed = 5

    	spa failure reason sw failed

    .. data:: spa_failure_reason_sw_restart = 6

    	spa failure reason sw restart

    .. data:: spa_failure_reason_check_fpd = 7

    	spa failure reason check fpd

    .. data:: spa_failure_reason_read_type = 8

    	spa failure reason read type

    """

    spa_failure_reason_unknown = Enum.YLeaf(1, "spa-failure-reason-unknown")

    spa_failure_reason_spi_failure = Enum.YLeaf(2, "spa-failure-reason-spi-failure")

    spa_failure_reason_boot = Enum.YLeaf(3, "spa-failure-reason-boot")

    spa_failure_reason_hw_failed = Enum.YLeaf(4, "spa-failure-reason-hw-failed")

    spa_failure_reason_sw_failed = Enum.YLeaf(5, "spa-failure-reason-sw-failed")

    spa_failure_reason_sw_restart = Enum.YLeaf(6, "spa-failure-reason-sw-restart")

    spa_failure_reason_check_fpd = Enum.YLeaf(7, "spa-failure-reason-check-fpd")

    spa_failure_reason_read_type = Enum.YLeaf(8, "spa-failure-reason-read-type")


class SpaOperState(Enum):
    """
    SpaOperState

    SPA operational states

    .. data:: spa_state_reset = 1

    	spa state reset

    .. data:: spa_state_failed = 2

    	spa state failed

    .. data:: spa_state_booting = 3

    	spa state booting

    .. data:: spa_state_ready = 4

    	spa state ready

    """

    spa_state_reset = Enum.YLeaf(1, "spa-state-reset")

    spa_state_failed = Enum.YLeaf(2, "spa-state-failed")

    spa_state_booting = Enum.YLeaf(3, "spa-state-booting")

    spa_state_ready = Enum.YLeaf(4, "spa-state-ready")


class SpaResetReason(Enum):
    """
    SpaResetReason

    SPA reset reasons

    .. data:: spa_reset_reason_unknown = 1

    	spa reset reason unknown

    .. data:: spa_reset_reason_manual = 2

    	spa reset reason manual

    .. data:: spa_reset_reason_fpd_upgrade = 3

    	spa reset reason fpd upgrade

    .. data:: spa_reset_reason_audit_fail = 4

    	spa reset reason audit fail

    .. data:: spa_reset_reason_failure = 5

    	spa reset reason failure

    """

    spa_reset_reason_unknown = Enum.YLeaf(1, "spa-reset-reason-unknown")

    spa_reset_reason_manual = Enum.YLeaf(2, "spa-reset-reason-manual")

    spa_reset_reason_fpd_upgrade = Enum.YLeaf(3, "spa-reset-reason-fpd-upgrade")

    spa_reset_reason_audit_fail = Enum.YLeaf(4, "spa-reset-reason-audit-fail")

    spa_reset_reason_failure = Enum.YLeaf(5, "spa-reset-reason-failure")



class MpaInternal(Entity):
    """
    Management LAN Operational data space
    
    .. attribute:: nodes
    
    	Table of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes>`
    
    

    """

    _prefix = 'asr9k-lc-fca-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(MpaInternal, self).__init__()
        self._top_entity = None

        self.yang_name = "mpa-internal"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-lc-fca-oper"

        self.nodes = MpaInternal.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Table of nodes
        
        .. attribute:: node
        
        	Number
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-lc-fca-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MpaInternal.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "mpa-internal"

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
                        super(MpaInternal.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MpaInternal.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Number
            
            .. attribute:: node  <key>
            
            	node number
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: bay
            
            	Number
            	**type**\: list of    :py:class:`Bay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes.Node.Bay>`
            
            

            """

            _prefix = 'asr9k-lc-fca-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MpaInternal.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node = YLeaf(YType.str, "node")

                self.bay = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MpaInternal.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MpaInternal.Nodes.Node, self).__setattr__(name, value)


            class Bay(Entity):
                """
                Number
                
                .. attribute:: number  <key>
                
                	bay number
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ifsubsies
                
                	Table of Ifsubsys
                	**type**\:   :py:class:`Ifsubsies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes.Node.Bay.Ifsubsies>`
                
                

                """

                _prefix = 'asr9k-lc-fca-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MpaInternal.Nodes.Node.Bay, self).__init__()

                    self.yang_name = "bay"
                    self.yang_parent_name = "node"

                    self.number = YLeaf(YType.int32, "number")

                    self.ifsubsies = MpaInternal.Nodes.Node.Bay.Ifsubsies()
                    self.ifsubsies.parent = self
                    self._children_name_map["ifsubsies"] = "ifsubsies"
                    self._children_yang_names.add("ifsubsies")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("number") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MpaInternal.Nodes.Node.Bay, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MpaInternal.Nodes.Node.Bay, self).__setattr__(name, value)


                class Ifsubsies(Entity):
                    """
                    Table of Ifsubsys
                    
                    .. attribute:: ifsubsy
                    
                    	Number
                    	**type**\: list of    :py:class:`Ifsubsy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy>`
                    
                    

                    """

                    _prefix = 'asr9k-lc-fca-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MpaInternal.Nodes.Node.Bay.Ifsubsies, self).__init__()

                        self.yang_name = "ifsubsies"
                        self.yang_parent_name = "bay"

                        self.ifsubsy = YList(self)

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
                                    super(MpaInternal.Nodes.Node.Bay.Ifsubsies, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MpaInternal.Nodes.Node.Bay.Ifsubsies, self).__setattr__(name, value)


                    class Ifsubsy(Entity):
                        """
                        Number
                        
                        .. attribute:: number  <key>
                        
                        	ifsubsys number
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: mpa_internal_info
                        
                        	mpa internal info
                        	**type**\:   :py:class:`MpaInternalInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo>`
                        
                        

                        """

                        _prefix = 'asr9k-lc-fca-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy, self).__init__()

                            self.yang_name = "ifsubsy"
                            self.yang_parent_name = "ifsubsies"

                            self.number = YLeaf(YType.str, "number")

                            self.mpa_internal_info = MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo()
                            self.mpa_internal_info.parent = self
                            self._children_name_map["mpa_internal_info"] = "mpa-internal-info"
                            self._children_yang_names.add("mpa-internal-info")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("number") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy, self).__setattr__(name, value)


                        class MpaInternalInfo(Entity):
                            """
                            mpa internal info
                            
                            .. attribute:: bay
                            
                            	bay
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ep_idprom_data
                            
                            	ep idprom data
                            	**type**\:  str
                            
                            	**length:** 0..256
                            
                            .. attribute:: ep_idprom_major
                            
                            	ep idprom major
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ep_idprom_minor
                            
                            	ep idprom minor
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ep_presence
                            
                            	ep presence
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ep_state
                            
                            	ep state
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ep_type
                            
                            	ep type
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: if_event
                            
                            	if event
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: if_state
                            
                            	if state
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ifsubsys
                            
                            	ifsubsys
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'asr9k-lc-fca-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo, self).__init__()

                                self.yang_name = "mpa-internal-info"
                                self.yang_parent_name = "ifsubsy"

                                self.bay = YLeaf(YType.uint32, "bay")

                                self.ep_idprom_data = YLeaf(YType.str, "ep-idprom-data")

                                self.ep_idprom_major = YLeaf(YType.uint8, "ep-idprom-major")

                                self.ep_idprom_minor = YLeaf(YType.uint8, "ep-idprom-minor")

                                self.ep_presence = YLeaf(YType.uint8, "ep-presence")

                                self.ep_state = YLeaf(YType.uint8, "ep-state")

                                self.ep_type = YLeaf(YType.uint32, "ep-type")

                                self.if_event = YLeaf(YType.uint8, "if-event")

                                self.if_state = YLeaf(YType.uint8, "if-state")

                                self.ifsubsys = YLeaf(YType.uint32, "ifsubsys")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bay",
                                                "ep_idprom_data",
                                                "ep_idprom_major",
                                                "ep_idprom_minor",
                                                "ep_presence",
                                                "ep_state",
                                                "ep_type",
                                                "if_event",
                                                "if_state",
                                                "ifsubsys") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.bay.is_set or
                                    self.ep_idprom_data.is_set or
                                    self.ep_idprom_major.is_set or
                                    self.ep_idprom_minor.is_set or
                                    self.ep_presence.is_set or
                                    self.ep_state.is_set or
                                    self.ep_type.is_set or
                                    self.if_event.is_set or
                                    self.if_state.is_set or
                                    self.ifsubsys.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bay.yfilter != YFilter.not_set or
                                    self.ep_idprom_data.yfilter != YFilter.not_set or
                                    self.ep_idprom_major.yfilter != YFilter.not_set or
                                    self.ep_idprom_minor.yfilter != YFilter.not_set or
                                    self.ep_presence.yfilter != YFilter.not_set or
                                    self.ep_state.yfilter != YFilter.not_set or
                                    self.ep_type.yfilter != YFilter.not_set or
                                    self.if_event.yfilter != YFilter.not_set or
                                    self.if_state.yfilter != YFilter.not_set or
                                    self.ifsubsys.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mpa-internal-info" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bay.is_set or self.bay.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bay.get_name_leafdata())
                                if (self.ep_idprom_data.is_set or self.ep_idprom_data.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ep_idprom_data.get_name_leafdata())
                                if (self.ep_idprom_major.is_set or self.ep_idprom_major.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ep_idprom_major.get_name_leafdata())
                                if (self.ep_idprom_minor.is_set or self.ep_idprom_minor.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ep_idprom_minor.get_name_leafdata())
                                if (self.ep_presence.is_set or self.ep_presence.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ep_presence.get_name_leafdata())
                                if (self.ep_state.is_set or self.ep_state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ep_state.get_name_leafdata())
                                if (self.ep_type.is_set or self.ep_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ep_type.get_name_leafdata())
                                if (self.if_event.is_set or self.if_event.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.if_event.get_name_leafdata())
                                if (self.if_state.is_set or self.if_state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.if_state.get_name_leafdata())
                                if (self.ifsubsys.is_set or self.ifsubsys.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ifsubsys.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bay" or name == "ep-idprom-data" or name == "ep-idprom-major" or name == "ep-idprom-minor" or name == "ep-presence" or name == "ep-state" or name == "ep-type" or name == "if-event" or name == "if-state" or name == "ifsubsys"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bay"):
                                    self.bay = value
                                    self.bay.value_namespace = name_space
                                    self.bay.value_namespace_prefix = name_space_prefix
                                if(value_path == "ep-idprom-data"):
                                    self.ep_idprom_data = value
                                    self.ep_idprom_data.value_namespace = name_space
                                    self.ep_idprom_data.value_namespace_prefix = name_space_prefix
                                if(value_path == "ep-idprom-major"):
                                    self.ep_idprom_major = value
                                    self.ep_idprom_major.value_namespace = name_space
                                    self.ep_idprom_major.value_namespace_prefix = name_space_prefix
                                if(value_path == "ep-idprom-minor"):
                                    self.ep_idprom_minor = value
                                    self.ep_idprom_minor.value_namespace = name_space
                                    self.ep_idprom_minor.value_namespace_prefix = name_space_prefix
                                if(value_path == "ep-presence"):
                                    self.ep_presence = value
                                    self.ep_presence.value_namespace = name_space
                                    self.ep_presence.value_namespace_prefix = name_space_prefix
                                if(value_path == "ep-state"):
                                    self.ep_state = value
                                    self.ep_state.value_namespace = name_space
                                    self.ep_state.value_namespace_prefix = name_space_prefix
                                if(value_path == "ep-type"):
                                    self.ep_type = value
                                    self.ep_type.value_namespace = name_space
                                    self.ep_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "if-event"):
                                    self.if_event = value
                                    self.if_event.value_namespace = name_space
                                    self.if_event.value_namespace_prefix = name_space_prefix
                                if(value_path == "if-state"):
                                    self.if_state = value
                                    self.if_state.value_namespace = name_space
                                    self.if_state.value_namespace_prefix = name_space_prefix
                                if(value_path == "ifsubsys"):
                                    self.ifsubsys = value
                                    self.ifsubsys.value_namespace = name_space
                                    self.ifsubsys.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.number.is_set or
                                (self.mpa_internal_info is not None and self.mpa_internal_info.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.number.yfilter != YFilter.not_set or
                                (self.mpa_internal_info is not None and self.mpa_internal_info.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ifsubsy" + "[number='" + self.number.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.number.is_set or self.number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.number.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "mpa-internal-info"):
                                if (self.mpa_internal_info is None):
                                    self.mpa_internal_info = MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo()
                                    self.mpa_internal_info.parent = self
                                    self._children_name_map["mpa_internal_info"] = "mpa-internal-info"
                                return self.mpa_internal_info

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "mpa-internal-info" or name == "number"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "number"):
                                self.number = value
                                self.number.value_namespace = name_space
                                self.number.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.ifsubsy:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.ifsubsy:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ifsubsies" + path_buffer

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

                        if (child_yang_name == "ifsubsy"):
                            for c in self.ifsubsy:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.ifsubsy.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ifsubsy"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.number.is_set or
                        (self.ifsubsies is not None and self.ifsubsies.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.number.yfilter != YFilter.not_set or
                        (self.ifsubsies is not None and self.ifsubsies.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bay" + "[number='" + self.number.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.number.is_set or self.number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.number.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ifsubsies"):
                        if (self.ifsubsies is None):
                            self.ifsubsies = MpaInternal.Nodes.Node.Bay.Ifsubsies()
                            self.ifsubsies.parent = self
                            self._children_name_map["ifsubsies"] = "ifsubsies"
                        return self.ifsubsies

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ifsubsies" or name == "number"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "number"):
                        self.number = value
                        self.number.value_namespace = name_space
                        self.number.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.bay:
                    if (c.has_data()):
                        return True
                return self.node.is_set

            def has_operation(self):
                for c in self.bay:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.node.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node='" + self.node.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-lc-fca-oper:mpa-internal/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node.is_set or self.node.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bay"):
                    for c in self.bay:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = MpaInternal.Nodes.Node.Bay()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.bay.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bay" or name == "node"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node"):
                    self.node = value
                    self.node.value_namespace = name_space
                    self.node.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-asr9k-lc-fca-oper:mpa-internal/%s" % self.get_segment_path()
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
                c = MpaInternal.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-asr9k-lc-fca-oper:mpa-internal" + path_buffer

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
                self.nodes = MpaInternal.Nodes()
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
        self._top_entity = MpaInternal()
        return self._top_entity

class Mpa(Entity):
    """
    mpa
    
    .. attribute:: nodes
    
    	Table of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.Mpa.Nodes>`
    
    

    """

    _prefix = 'asr9k-lc-fca-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Mpa, self).__init__()
        self._top_entity = None

        self.yang_name = "mpa"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-lc-fca-oper"

        self.nodes = Mpa.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Table of nodes
        
        .. attribute:: node
        
        	Number
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.Mpa.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-lc-fca-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Mpa.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "mpa"

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
                        super(Mpa.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Mpa.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Number
            
            .. attribute:: node  <key>
            
            	node number
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: bay
            
            	Number
            	**type**\: list of    :py:class:`Bay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.Mpa.Nodes.Node.Bay>`
            
            

            """

            _prefix = 'asr9k-lc-fca-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Mpa.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node = YLeaf(YType.str, "node")

                self.bay = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Mpa.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Mpa.Nodes.Node, self).__setattr__(name, value)


            class Bay(Entity):
                """
                Number
                
                .. attribute:: number  <key>
                
                	bay number
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: mpa_detail_table
                
                	Table of Mpa Detail Info
                	**type**\:   :py:class:`MpaDetailTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.Mpa.Nodes.Node.Bay.MpaDetailTable>`
                
                

                """

                _prefix = 'asr9k-lc-fca-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Mpa.Nodes.Node.Bay, self).__init__()

                    self.yang_name = "bay"
                    self.yang_parent_name = "node"

                    self.number = YLeaf(YType.int32, "number")

                    self.mpa_detail_table = Mpa.Nodes.Node.Bay.MpaDetailTable()
                    self.mpa_detail_table.parent = self
                    self._children_name_map["mpa_detail_table"] = "mpa-detail-table"
                    self._children_yang_names.add("mpa-detail-table")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("number") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Mpa.Nodes.Node.Bay, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mpa.Nodes.Node.Bay, self).__setattr__(name, value)


                class MpaDetailTable(Entity):
                    """
                    Table of Mpa Detail Info
                    
                    .. attribute:: mpa_detail
                    
                    	mpa detail status info
                    	**type**\:   :py:class:`MpaDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail>`
                    
                    

                    """

                    _prefix = 'asr9k-lc-fca-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Mpa.Nodes.Node.Bay.MpaDetailTable, self).__init__()

                        self.yang_name = "mpa-detail-table"
                        self.yang_parent_name = "bay"

                        self.mpa_detail = Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail()
                        self.mpa_detail.parent = self
                        self._children_name_map["mpa_detail"] = "mpa-detail"
                        self._children_yang_names.add("mpa-detail")


                    class MpaDetail(Entity):
                        """
                        mpa detail status info
                        
                        .. attribute:: bay_number
                        
                        	BAY number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: insertion_time
                        
                        	Time when SPA last insertedin calendar format\: seconds since00\:00\:00 UTC, January 1, 1970
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: is_spa_admin_up
                        
                        	If SPA admin state is Up
                        	**type**\:  bool
                        
                        .. attribute:: is_spa_in_reset
                        
                        	If SPA in reset
                        	**type**\:  bool
                        
                        .. attribute:: is_spa_inserted
                        
                        	If SPA inserted
                        	**type**\:  bool
                        
                        .. attribute:: is_spa_power_admin_up
                        
                        	If SPA power admin state is Up
                        	**type**\:  bool
                        
                        .. attribute:: is_spa_powered
                        
                        	If SPA powered
                        	**type**\:  bool
                        
                        .. attribute:: last_failure_reason
                        
                        	Last Failure Reason
                        	**type**\:   :py:class:`SpaFailureReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.SpaFailureReason>`
                        
                        .. attribute:: last_ready_time
                        
                        	Time when SPA last reached Ready statein calendar format\: seconds since00\:00\:00 UTC, January 1, 1970
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: last_reset_reason
                        
                        	Last reset reason
                        	**type**\:   :py:class:`SpaResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.SpaResetReason>`
                        
                        .. attribute:: spa_oper_state
                        
                        	SPA operational state
                        	**type**\:   :py:class:`SpaOperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.SpaOperState>`
                        
                        .. attribute:: spa_type
                        
                        	SPA type
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: up_time
                        
                        	Uptime in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'asr9k-lc-fca-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail, self).__init__()

                            self.yang_name = "mpa-detail"
                            self.yang_parent_name = "mpa-detail-table"

                            self.bay_number = YLeaf(YType.uint16, "bay-number")

                            self.insertion_time = YLeaf(YType.uint32, "insertion-time")

                            self.is_spa_admin_up = YLeaf(YType.boolean, "is-spa-admin-up")

                            self.is_spa_in_reset = YLeaf(YType.boolean, "is-spa-in-reset")

                            self.is_spa_inserted = YLeaf(YType.boolean, "is-spa-inserted")

                            self.is_spa_power_admin_up = YLeaf(YType.boolean, "is-spa-power-admin-up")

                            self.is_spa_powered = YLeaf(YType.boolean, "is-spa-powered")

                            self.last_failure_reason = YLeaf(YType.enumeration, "last-failure-reason")

                            self.last_ready_time = YLeaf(YType.uint32, "last-ready-time")

                            self.last_reset_reason = YLeaf(YType.enumeration, "last-reset-reason")

                            self.spa_oper_state = YLeaf(YType.enumeration, "spa-oper-state")

                            self.spa_type = YLeaf(YType.uint16, "spa-type")

                            self.up_time = YLeaf(YType.uint32, "up-time")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("bay_number",
                                            "insertion_time",
                                            "is_spa_admin_up",
                                            "is_spa_in_reset",
                                            "is_spa_inserted",
                                            "is_spa_power_admin_up",
                                            "is_spa_powered",
                                            "last_failure_reason",
                                            "last_ready_time",
                                            "last_reset_reason",
                                            "spa_oper_state",
                                            "spa_type",
                                            "up_time") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.bay_number.is_set or
                                self.insertion_time.is_set or
                                self.is_spa_admin_up.is_set or
                                self.is_spa_in_reset.is_set or
                                self.is_spa_inserted.is_set or
                                self.is_spa_power_admin_up.is_set or
                                self.is_spa_powered.is_set or
                                self.last_failure_reason.is_set or
                                self.last_ready_time.is_set or
                                self.last_reset_reason.is_set or
                                self.spa_oper_state.is_set or
                                self.spa_type.is_set or
                                self.up_time.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.bay_number.yfilter != YFilter.not_set or
                                self.insertion_time.yfilter != YFilter.not_set or
                                self.is_spa_admin_up.yfilter != YFilter.not_set or
                                self.is_spa_in_reset.yfilter != YFilter.not_set or
                                self.is_spa_inserted.yfilter != YFilter.not_set or
                                self.is_spa_power_admin_up.yfilter != YFilter.not_set or
                                self.is_spa_powered.yfilter != YFilter.not_set or
                                self.last_failure_reason.yfilter != YFilter.not_set or
                                self.last_ready_time.yfilter != YFilter.not_set or
                                self.last_reset_reason.yfilter != YFilter.not_set or
                                self.spa_oper_state.yfilter != YFilter.not_set or
                                self.spa_type.yfilter != YFilter.not_set or
                                self.up_time.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "mpa-detail" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.bay_number.is_set or self.bay_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bay_number.get_name_leafdata())
                            if (self.insertion_time.is_set or self.insertion_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.insertion_time.get_name_leafdata())
                            if (self.is_spa_admin_up.is_set or self.is_spa_admin_up.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_spa_admin_up.get_name_leafdata())
                            if (self.is_spa_in_reset.is_set or self.is_spa_in_reset.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_spa_in_reset.get_name_leafdata())
                            if (self.is_spa_inserted.is_set or self.is_spa_inserted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_spa_inserted.get_name_leafdata())
                            if (self.is_spa_power_admin_up.is_set or self.is_spa_power_admin_up.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_spa_power_admin_up.get_name_leafdata())
                            if (self.is_spa_powered.is_set or self.is_spa_powered.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_spa_powered.get_name_leafdata())
                            if (self.last_failure_reason.is_set or self.last_failure_reason.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.last_failure_reason.get_name_leafdata())
                            if (self.last_ready_time.is_set or self.last_ready_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.last_ready_time.get_name_leafdata())
                            if (self.last_reset_reason.is_set or self.last_reset_reason.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.last_reset_reason.get_name_leafdata())
                            if (self.spa_oper_state.is_set or self.spa_oper_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.spa_oper_state.get_name_leafdata())
                            if (self.spa_type.is_set or self.spa_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.spa_type.get_name_leafdata())
                            if (self.up_time.is_set or self.up_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.up_time.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bay-number" or name == "insertion-time" or name == "is-spa-admin-up" or name == "is-spa-in-reset" or name == "is-spa-inserted" or name == "is-spa-power-admin-up" or name == "is-spa-powered" or name == "last-failure-reason" or name == "last-ready-time" or name == "last-reset-reason" or name == "spa-oper-state" or name == "spa-type" or name == "up-time"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "bay-number"):
                                self.bay_number = value
                                self.bay_number.value_namespace = name_space
                                self.bay_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "insertion-time"):
                                self.insertion_time = value
                                self.insertion_time.value_namespace = name_space
                                self.insertion_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-spa-admin-up"):
                                self.is_spa_admin_up = value
                                self.is_spa_admin_up.value_namespace = name_space
                                self.is_spa_admin_up.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-spa-in-reset"):
                                self.is_spa_in_reset = value
                                self.is_spa_in_reset.value_namespace = name_space
                                self.is_spa_in_reset.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-spa-inserted"):
                                self.is_spa_inserted = value
                                self.is_spa_inserted.value_namespace = name_space
                                self.is_spa_inserted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-spa-power-admin-up"):
                                self.is_spa_power_admin_up = value
                                self.is_spa_power_admin_up.value_namespace = name_space
                                self.is_spa_power_admin_up.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-spa-powered"):
                                self.is_spa_powered = value
                                self.is_spa_powered.value_namespace = name_space
                                self.is_spa_powered.value_namespace_prefix = name_space_prefix
                            if(value_path == "last-failure-reason"):
                                self.last_failure_reason = value
                                self.last_failure_reason.value_namespace = name_space
                                self.last_failure_reason.value_namespace_prefix = name_space_prefix
                            if(value_path == "last-ready-time"):
                                self.last_ready_time = value
                                self.last_ready_time.value_namespace = name_space
                                self.last_ready_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "last-reset-reason"):
                                self.last_reset_reason = value
                                self.last_reset_reason.value_namespace = name_space
                                self.last_reset_reason.value_namespace_prefix = name_space_prefix
                            if(value_path == "spa-oper-state"):
                                self.spa_oper_state = value
                                self.spa_oper_state.value_namespace = name_space
                                self.spa_oper_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "spa-type"):
                                self.spa_type = value
                                self.spa_type.value_namespace = name_space
                                self.spa_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "up-time"):
                                self.up_time = value
                                self.up_time.value_namespace = name_space
                                self.up_time.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.mpa_detail is not None and self.mpa_detail.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.mpa_detail is not None and self.mpa_detail.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "mpa-detail-table" + path_buffer

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

                        if (child_yang_name == "mpa-detail"):
                            if (self.mpa_detail is None):
                                self.mpa_detail = Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail()
                                self.mpa_detail.parent = self
                                self._children_name_map["mpa_detail"] = "mpa-detail"
                            return self.mpa_detail

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "mpa-detail"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.number.is_set or
                        (self.mpa_detail_table is not None and self.mpa_detail_table.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.number.yfilter != YFilter.not_set or
                        (self.mpa_detail_table is not None and self.mpa_detail_table.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bay" + "[number='" + self.number.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.number.is_set or self.number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.number.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "mpa-detail-table"):
                        if (self.mpa_detail_table is None):
                            self.mpa_detail_table = Mpa.Nodes.Node.Bay.MpaDetailTable()
                            self.mpa_detail_table.parent = self
                            self._children_name_map["mpa_detail_table"] = "mpa-detail-table"
                        return self.mpa_detail_table

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mpa-detail-table" or name == "number"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "number"):
                        self.number = value
                        self.number.value_namespace = name_space
                        self.number.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.bay:
                    if (c.has_data()):
                        return True
                return self.node.is_set

            def has_operation(self):
                for c in self.bay:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.node.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node='" + self.node.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-lc-fca-oper:mpa/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node.is_set or self.node.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bay"):
                    for c in self.bay:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Mpa.Nodes.Node.Bay()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.bay.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bay" or name == "node"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node"):
                    self.node = value
                    self.node.value_namespace = name_space
                    self.node.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-asr9k-lc-fca-oper:mpa/%s" % self.get_segment_path()
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
                c = Mpa.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-asr9k-lc-fca-oper:mpa" + path_buffer

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
                self.nodes = Mpa.Nodes()
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
        self._top_entity = Mpa()
        return self._top_entity

