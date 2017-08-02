""" Cisco_IOS_XR_sdr_invmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR sdr\-invmgr package operational data.

This module contains definitions
for the following management objects\:
  sdr\-inventory\: SDR information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SdrInventory(Entity):
    """
    SDR information
    
    .. attribute:: racks
    
    	RackTable
    	**type**\:   :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks>`
    
    

    """

    _prefix = 'sdr-invmgr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SdrInventory, self).__init__()
        self._top_entity = None

        self.yang_name = "sdr-inventory"
        self.yang_parent_name = "Cisco-IOS-XR-sdr-invmgr-oper"

        self.racks = SdrInventory.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._children_yang_names.add("racks")


    class Racks(Entity):
        """
        RackTable
        
        .. attribute:: rack
        
        	Rack name
        	**type**\: list of    :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks.Rack>`
        
        

        """

        _prefix = 'sdr-invmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SdrInventory.Racks, self).__init__()

            self.yang_name = "racks"
            self.yang_parent_name = "sdr-inventory"

            self.rack = YList(self)

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
                        super(SdrInventory.Racks, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SdrInventory.Racks, self).__setattr__(name, value)


        class Rack(Entity):
            """
            Rack name
            
            .. attribute:: name  <key>
            
            	Rack name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: slot
            
            	Slot name
            	**type**\: list of    :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks.Rack.Slot>`
            
            

            """

            _prefix = 'sdr-invmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SdrInventory.Racks.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "racks"

                self.name = YLeaf(YType.str, "name")

                self.slot = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SdrInventory.Racks.Rack, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SdrInventory.Racks.Rack, self).__setattr__(name, value)


            class Slot(Entity):
                """
                Slot name
                
                .. attribute:: name  <key>
                
                	Slot name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: card
                
                	Card
                	**type**\: list of    :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks.Rack.Slot.Card>`
                
                

                """

                _prefix = 'sdr-invmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SdrInventory.Racks.Rack.Slot, self).__init__()

                    self.yang_name = "slot"
                    self.yang_parent_name = "rack"

                    self.name = YLeaf(YType.str, "name")

                    self.card = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SdrInventory.Racks.Rack.Slot, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SdrInventory.Racks.Rack.Slot, self).__setattr__(name, value)


                class Card(Entity):
                    """
                    Card
                    
                    .. attribute:: name  <key>
                    
                    	Card
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attributes
                    
                    	Attributes
                    	**type**\:   :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks.Rack.Slot.Card.Attributes>`
                    
                    

                    """

                    _prefix = 'sdr-invmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SdrInventory.Racks.Rack.Slot.Card, self).__init__()

                        self.yang_name = "card"
                        self.yang_parent_name = "slot"

                        self.name = YLeaf(YType.str, "name")

                        self.attributes = SdrInventory.Racks.Rack.Slot.Card.Attributes()
                        self.attributes.parent = self
                        self._children_name_map["attributes"] = "attributes"
                        self._children_yang_names.add("attributes")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SdrInventory.Racks.Rack.Slot.Card, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SdrInventory.Racks.Rack.Slot.Card, self).__setattr__(name, value)


                    class Attributes(Entity):
                        """
                        Attributes
                        
                        .. attribute:: card_admin_state
                        
                        	Card Admin State
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: card_state
                        
                        	CardState
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: card_state_string
                        
                        	Card State String
                        	**type**\:  str
                        
                        .. attribute:: card_type
                        
                        	CardType
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: card_type_string
                        
                        	Card Type String
                        	**type**\:  str
                        
                        .. attribute:: config_state
                        
                        	ConfigState
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: config_state_string
                        
                        	Config State String
                        	**type**\:  str
                        
                        .. attribute:: ctype
                        
                        	CType
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: monitor
                        
                        	Monitor
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: node_name_string
                        
                        	Node Name String
                        	**type**\:  str
                        
                        .. attribute:: pi_slot_number
                        
                        	Pi Slot Number
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: power
                        
                        	Power
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: shutdown
                        
                        	Shutdown
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: vm_state
                        
                        	VM State information
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        

                        """

                        _prefix = 'sdr-invmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SdrInventory.Racks.Rack.Slot.Card.Attributes, self).__init__()

                            self.yang_name = "attributes"
                            self.yang_parent_name = "card"

                            self.card_admin_state = YLeaf(YType.int32, "card-admin-state")

                            self.card_state = YLeaf(YType.int32, "card-state")

                            self.card_state_string = YLeaf(YType.str, "card-state-string")

                            self.card_type = YLeaf(YType.int32, "card-type")

                            self.card_type_string = YLeaf(YType.str, "card-type-string")

                            self.config_state = YLeaf(YType.int32, "config-state")

                            self.config_state_string = YLeaf(YType.str, "config-state-string")

                            self.ctype = YLeaf(YType.int32, "ctype")

                            self.monitor = YLeaf(YType.int32, "monitor")

                            self.node_name_string = YLeaf(YType.str, "node-name-string")

                            self.pi_slot_number = YLeaf(YType.int32, "pi-slot-number")

                            self.power = YLeaf(YType.int32, "power")

                            self.shutdown = YLeaf(YType.int32, "shutdown")

                            self.vm_state = YLeaf(YType.int32, "vm-state")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("card_admin_state",
                                            "card_state",
                                            "card_state_string",
                                            "card_type",
                                            "card_type_string",
                                            "config_state",
                                            "config_state_string",
                                            "ctype",
                                            "monitor",
                                            "node_name_string",
                                            "pi_slot_number",
                                            "power",
                                            "shutdown",
                                            "vm_state") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SdrInventory.Racks.Rack.Slot.Card.Attributes, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SdrInventory.Racks.Rack.Slot.Card.Attributes, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.card_admin_state.is_set or
                                self.card_state.is_set or
                                self.card_state_string.is_set or
                                self.card_type.is_set or
                                self.card_type_string.is_set or
                                self.config_state.is_set or
                                self.config_state_string.is_set or
                                self.ctype.is_set or
                                self.monitor.is_set or
                                self.node_name_string.is_set or
                                self.pi_slot_number.is_set or
                                self.power.is_set or
                                self.shutdown.is_set or
                                self.vm_state.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.card_admin_state.yfilter != YFilter.not_set or
                                self.card_state.yfilter != YFilter.not_set or
                                self.card_state_string.yfilter != YFilter.not_set or
                                self.card_type.yfilter != YFilter.not_set or
                                self.card_type_string.yfilter != YFilter.not_set or
                                self.config_state.yfilter != YFilter.not_set or
                                self.config_state_string.yfilter != YFilter.not_set or
                                self.ctype.yfilter != YFilter.not_set or
                                self.monitor.yfilter != YFilter.not_set or
                                self.node_name_string.yfilter != YFilter.not_set or
                                self.pi_slot_number.yfilter != YFilter.not_set or
                                self.power.yfilter != YFilter.not_set or
                                self.shutdown.yfilter != YFilter.not_set or
                                self.vm_state.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "attributes" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.card_admin_state.is_set or self.card_admin_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.card_admin_state.get_name_leafdata())
                            if (self.card_state.is_set or self.card_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.card_state.get_name_leafdata())
                            if (self.card_state_string.is_set or self.card_state_string.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.card_state_string.get_name_leafdata())
                            if (self.card_type.is_set or self.card_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.card_type.get_name_leafdata())
                            if (self.card_type_string.is_set or self.card_type_string.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.card_type_string.get_name_leafdata())
                            if (self.config_state.is_set or self.config_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.config_state.get_name_leafdata())
                            if (self.config_state_string.is_set or self.config_state_string.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.config_state_string.get_name_leafdata())
                            if (self.ctype.is_set or self.ctype.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ctype.get_name_leafdata())
                            if (self.monitor.is_set or self.monitor.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.monitor.get_name_leafdata())
                            if (self.node_name_string.is_set or self.node_name_string.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.node_name_string.get_name_leafdata())
                            if (self.pi_slot_number.is_set or self.pi_slot_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pi_slot_number.get_name_leafdata())
                            if (self.power.is_set or self.power.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.power.get_name_leafdata())
                            if (self.shutdown.is_set or self.shutdown.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.shutdown.get_name_leafdata())
                            if (self.vm_state.is_set or self.vm_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vm_state.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "card-admin-state" or name == "card-state" or name == "card-state-string" or name == "card-type" or name == "card-type-string" or name == "config-state" or name == "config-state-string" or name == "ctype" or name == "monitor" or name == "node-name-string" or name == "pi-slot-number" or name == "power" or name == "shutdown" or name == "vm-state"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "card-admin-state"):
                                self.card_admin_state = value
                                self.card_admin_state.value_namespace = name_space
                                self.card_admin_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "card-state"):
                                self.card_state = value
                                self.card_state.value_namespace = name_space
                                self.card_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "card-state-string"):
                                self.card_state_string = value
                                self.card_state_string.value_namespace = name_space
                                self.card_state_string.value_namespace_prefix = name_space_prefix
                            if(value_path == "card-type"):
                                self.card_type = value
                                self.card_type.value_namespace = name_space
                                self.card_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "card-type-string"):
                                self.card_type_string = value
                                self.card_type_string.value_namespace = name_space
                                self.card_type_string.value_namespace_prefix = name_space_prefix
                            if(value_path == "config-state"):
                                self.config_state = value
                                self.config_state.value_namespace = name_space
                                self.config_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "config-state-string"):
                                self.config_state_string = value
                                self.config_state_string.value_namespace = name_space
                                self.config_state_string.value_namespace_prefix = name_space_prefix
                            if(value_path == "ctype"):
                                self.ctype = value
                                self.ctype.value_namespace = name_space
                                self.ctype.value_namespace_prefix = name_space_prefix
                            if(value_path == "monitor"):
                                self.monitor = value
                                self.monitor.value_namespace = name_space
                                self.monitor.value_namespace_prefix = name_space_prefix
                            if(value_path == "node-name-string"):
                                self.node_name_string = value
                                self.node_name_string.value_namespace = name_space
                                self.node_name_string.value_namespace_prefix = name_space_prefix
                            if(value_path == "pi-slot-number"):
                                self.pi_slot_number = value
                                self.pi_slot_number.value_namespace = name_space
                                self.pi_slot_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "power"):
                                self.power = value
                                self.power.value_namespace = name_space
                                self.power.value_namespace_prefix = name_space_prefix
                            if(value_path == "shutdown"):
                                self.shutdown = value
                                self.shutdown.value_namespace = name_space
                                self.shutdown.value_namespace_prefix = name_space_prefix
                            if(value_path == "vm-state"):
                                self.vm_state = value
                                self.vm_state.value_namespace = name_space
                                self.vm_state.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.name.is_set or
                            (self.attributes is not None and self.attributes.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            (self.attributes is not None and self.attributes.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "card" + "[name='" + self.name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "attributes"):
                            if (self.attributes is None):
                                self.attributes = SdrInventory.Racks.Rack.Slot.Card.Attributes()
                                self.attributes.parent = self
                                self._children_name_map["attributes"] = "attributes"
                            return self.attributes

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "attributes" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.card:
                        if (c.has_data()):
                            return True
                    return self.name.is_set

                def has_operation(self):
                    for c in self.card:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "slot" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "card"):
                        for c in self.card:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SdrInventory.Racks.Rack.Slot.Card()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.card.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "card" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.slot:
                    if (c.has_data()):
                        return True
                return self.name.is_set

            def has_operation(self):
                for c in self.slot:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rack" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-sdr-invmgr-oper:sdr-inventory/racks/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "slot"):
                    for c in self.slot:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = SdrInventory.Racks.Rack.Slot()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.slot.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "slot" or name == "name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rack:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rack:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "racks" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-sdr-invmgr-oper:sdr-inventory/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rack"):
                for c in self.rack:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SdrInventory.Racks.Rack()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rack.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rack"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.racks is not None and self.racks.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.racks is not None and self.racks.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-sdr-invmgr-oper:sdr-inventory" + path_buffer

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

        if (child_yang_name == "racks"):
            if (self.racks is None):
                self.racks = SdrInventory.Racks()
                self.racks.parent = self
                self._children_name_map["racks"] = "racks"
            return self.racks

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "racks"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SdrInventory()
        return self._top_entity

