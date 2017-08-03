""" CISCO_ETHERLIKE_EXT_MIB 

The MIB module to describe generic objects for
ethernet\-like network interfaces. 

This MIB provides ethernet\-like network interfaces 
information that are either excluded by EtherLike\-MIB 
or specific to Cisco products.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoEtherlikeExtMib(Entity):
    """
    
    
    .. attribute:: ceedot3pauseexttable
    
    	A list of additional descriptive and status information about the MAC Control PAUSE  function on the ethernet\-like interfaces  attached to a particular system, in extension to dot3PauseTable in EtherLike\-MIB. There will be  one row in this table for each ethernet\-like  interface in the system which supports the MAC  Control PAUSE function
    	**type**\:   :py:class:`Ceedot3Pauseexttable <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CiscoEtherlikeExtMib.Ceedot3Pauseexttable>`
    
    .. attribute:: ceesubinterfacetable
    
    	This table provides the subinterface related information associated to the Ethernet\-like interfaces.  The subinterface is a division of one physical interface into multiple logical interfaces. As an example of what a typical subinterface setup might look like on a device, a single Ethernet port such as GigabitEthernet0/0 would be subdivided into Gi0/0.1, Gi0/0.2, Gi0/0.3 and so on, each one performing as if it were a separate interface
    	**type**\:   :py:class:`Ceesubinterfacetable <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CiscoEtherlikeExtMib.Ceesubinterfacetable>`
    
    

    """

    _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
    _revision = '2010-06-04'

    def __init__(self):
        super(CiscoEtherlikeExtMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ETHERLIKE-EXT-MIB"
        self.yang_parent_name = "CISCO-ETHERLIKE-EXT-MIB"

        self.ceedot3pauseexttable = CiscoEtherlikeExtMib.Ceedot3Pauseexttable()
        self.ceedot3pauseexttable.parent = self
        self._children_name_map["ceedot3pauseexttable"] = "ceeDot3PauseExtTable"
        self._children_yang_names.add("ceeDot3PauseExtTable")

        self.ceesubinterfacetable = CiscoEtherlikeExtMib.Ceesubinterfacetable()
        self.ceesubinterfacetable.parent = self
        self._children_name_map["ceesubinterfacetable"] = "ceeSubInterfaceTable"
        self._children_yang_names.add("ceeSubInterfaceTable")


    class Ceedot3Pauseexttable(Entity):
        """
        A list of additional descriptive and status
        information about the MAC Control PAUSE 
        function on the ethernet\-like interfaces 
        attached to a particular system, in extension to
        dot3PauseTable in EtherLike\-MIB. There will be 
        one row in this table for each ethernet\-like 
        interface in the system which supports the MAC 
        Control PAUSE function.
        
        .. attribute:: ceedot3pauseextentry
        
        	An entry in the table, containing additional information about the MAC Control PAUSE function  on a single ethernet\-like interface, in extension  to dot3PauseEntry in Etherlike\-MIB
        	**type**\: list of    :py:class:`Ceedot3Pauseextentry <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CiscoEtherlikeExtMib.Ceedot3Pauseexttable.Ceedot3Pauseextentry>`
        
        

        """

        _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
        _revision = '2010-06-04'

        def __init__(self):
            super(CiscoEtherlikeExtMib.Ceedot3Pauseexttable, self).__init__()

            self.yang_name = "ceeDot3PauseExtTable"
            self.yang_parent_name = "CISCO-ETHERLIKE-EXT-MIB"

            self.ceedot3pauseextentry = YList(self)

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
                        super(CiscoEtherlikeExtMib.Ceedot3Pauseexttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEtherlikeExtMib.Ceedot3Pauseexttable, self).__setattr__(name, value)


        class Ceedot3Pauseextentry(Entity):
            """
            An entry in the table, containing additional
            information about the MAC Control PAUSE function 
            on a single ethernet\-like interface, in extension 
            to dot3PauseEntry in Etherlike\-MIB.
            
            .. attribute:: dot3statsindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`dot3statsindex <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Statstable.Dot3Statsentry>`
            
            .. attribute:: ceedot3pauseextadminmode
            
            	Indicates preference to send or process pause frames on this interface. txDesired(0)  \-  indicates preference to send pause                   frames, but autonegotiates flow                   control. This bit can only be                   turned on when the corresponding                   instance of dot3PauseAdminMode                   has the value of 'enabledXmit' or                   'enabledXmitAndRcv'. rxDesired(1)  \-  indicates preference to process                   pause frames, but autonegotiates                   flow control. This bit can only be                   turned on when the corresponding                   instance of dot3PauseAdminMode                   has the value of 'enabledRcv' or                   'enabledXmitAndRcv'
            	**type**\:   :py:class:`Ceedot3Pauseextadminmode <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CiscoEtherlikeExtMib.Ceedot3Pauseexttable.Ceedot3Pauseextentry.Ceedot3Pauseextadminmode>`
            
            .. attribute:: ceedot3pauseextopermode
            
            	Provides additional information about the flow control operational status on this interface. txDisagree(0) \- the transmit pause function on                  this interface is disabled due to                  disagreement from the far end on                  negotiation. rxDisagree(1) \- the receive pause function on                   this interface is disabled due to                  disagreement from the far end on                  negotiation. txDesired(2)  \- the transmit pause function on                  this interface is desired. rxDesired(3)  \- the receive pause function on                   this interface is desired
            	**type**\:   :py:class:`Ceedot3Pauseextopermode <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CiscoEtherlikeExtMib.Ceedot3Pauseexttable.Ceedot3Pauseextentry.Ceedot3Pauseextopermode>`
            
            

            """

            _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
            _revision = '2010-06-04'

            def __init__(self):
                super(CiscoEtherlikeExtMib.Ceedot3Pauseexttable.Ceedot3Pauseextentry, self).__init__()

                self.yang_name = "ceeDot3PauseExtEntry"
                self.yang_parent_name = "ceeDot3PauseExtTable"

                self.dot3statsindex = YLeaf(YType.str, "dot3StatsIndex")

                self.ceedot3pauseextadminmode = YLeaf(YType.bits, "ceeDot3PauseExtAdminMode")

                self.ceedot3pauseextopermode = YLeaf(YType.bits, "ceeDot3PauseExtOperMode")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot3statsindex",
                                "ceedot3pauseextadminmode",
                                "ceedot3pauseextopermode") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEtherlikeExtMib.Ceedot3Pauseexttable.Ceedot3Pauseextentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEtherlikeExtMib.Ceedot3Pauseexttable.Ceedot3Pauseextentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot3statsindex.is_set or
                    self.ceedot3pauseextadminmode.is_set or
                    self.ceedot3pauseextopermode.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot3statsindex.yfilter != YFilter.not_set or
                    self.ceedot3pauseextadminmode.yfilter != YFilter.not_set or
                    self.ceedot3pauseextopermode.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ceeDot3PauseExtEntry" + "[dot3StatsIndex='" + self.dot3statsindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/ceeDot3PauseExtTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot3statsindex.is_set or self.dot3statsindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statsindex.get_name_leafdata())
                if (self.ceedot3pauseextadminmode.is_set or self.ceedot3pauseextadminmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceedot3pauseextadminmode.get_name_leafdata())
                if (self.ceedot3pauseextopermode.is_set or self.ceedot3pauseextopermode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceedot3pauseextopermode.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot3StatsIndex" or name == "ceeDot3PauseExtAdminMode" or name == "ceeDot3PauseExtOperMode"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot3StatsIndex"):
                    self.dot3statsindex = value
                    self.dot3statsindex.value_namespace = name_space
                    self.dot3statsindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ceeDot3PauseExtAdminMode"):
                    self.ceedot3pauseextadminmode[value] = True
                if(value_path == "ceeDot3PauseExtOperMode"):
                    self.ceedot3pauseextopermode[value] = True

        def has_data(self):
            for c in self.ceedot3pauseextentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ceedot3pauseextentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ceeDot3PauseExtTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ceeDot3PauseExtEntry"):
                for c in self.ceedot3pauseextentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEtherlikeExtMib.Ceedot3Pauseexttable.Ceedot3Pauseextentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ceedot3pauseextentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ceeDot3PauseExtEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ceesubinterfacetable(Entity):
        """
        This table provides the subinterface related information
        associated to the Ethernet\-like interfaces.
        
        The subinterface is a division of one physical interface into
        multiple logical interfaces. As an example of what a typical
        subinterface setup might look like on a device, a single
        Ethernet port such as GigabitEthernet0/0 would be subdivided
        into Gi0/0.1, Gi0/0.2, Gi0/0.3 and so on, each one performing as
        if it were a separate interface.
        
        .. attribute:: ceesubinterfaceentry
        
        	This table contains a row for each Ethernet\-like interface by it's ifTable ifIndex in the system, which supports the sub\-interface.  An entry is created by an agent, when it detects a Ethernet\-like interface is created in ifTable and it  can support sub\-interface.  An entry is deleted by an agent, when the ifTable entry associated to the Ethernet\-like interface is deleted. Typically, when the card is removed from the device
        	**type**\: list of    :py:class:`Ceesubinterfaceentry <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CiscoEtherlikeExtMib.Ceesubinterfacetable.Ceesubinterfaceentry>`
        
        

        """

        _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
        _revision = '2010-06-04'

        def __init__(self):
            super(CiscoEtherlikeExtMib.Ceesubinterfacetable, self).__init__()

            self.yang_name = "ceeSubInterfaceTable"
            self.yang_parent_name = "CISCO-ETHERLIKE-EXT-MIB"

            self.ceesubinterfaceentry = YList(self)

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
                        super(CiscoEtherlikeExtMib.Ceesubinterfacetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEtherlikeExtMib.Ceesubinterfacetable, self).__setattr__(name, value)


        class Ceesubinterfaceentry(Entity):
            """
            This table contains a row for each Ethernet\-like interface
            by it's ifTable ifIndex in the system, which supports the
            sub\-interface.
            
            An entry is created by an agent, when it detects a
            Ethernet\-like interface is created in ifTable and it 
            can support sub\-interface.
            
            An entry is deleted by an agent, when the ifTable entry
            associated to the Ethernet\-like interface is deleted.
            Typically, when the card is removed from the device.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: ceesubinterfacecount
            
            	This object represents the number of subinterfaces created on a Ethernet\-like interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: subifs
            
            

            """

            _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
            _revision = '2010-06-04'

            def __init__(self):
                super(CiscoEtherlikeExtMib.Ceesubinterfacetable.Ceesubinterfaceentry, self).__init__()

                self.yang_name = "ceeSubInterfaceEntry"
                self.yang_parent_name = "ceeSubInterfaceTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.ceesubinterfacecount = YLeaf(YType.uint32, "ceeSubInterfaceCount")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "ceesubinterfacecount") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEtherlikeExtMib.Ceesubinterfacetable.Ceesubinterfaceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEtherlikeExtMib.Ceesubinterfacetable.Ceesubinterfaceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.ceesubinterfacecount.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.ceesubinterfacecount.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ceeSubInterfaceEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/ceeSubInterfaceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.ceesubinterfacecount.is_set or self.ceesubinterfacecount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceesubinterfacecount.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "ceeSubInterfaceCount"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ceeSubInterfaceCount"):
                    self.ceesubinterfacecount = value
                    self.ceesubinterfacecount.value_namespace = name_space
                    self.ceesubinterfacecount.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ceesubinterfaceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ceesubinterfaceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ceeSubInterfaceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ceeSubInterfaceEntry"):
                for c in self.ceesubinterfaceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEtherlikeExtMib.Ceesubinterfacetable.Ceesubinterfaceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ceesubinterfaceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ceeSubInterfaceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ceedot3pauseexttable is not None and self.ceedot3pauseexttable.has_data()) or
            (self.ceesubinterfacetable is not None and self.ceesubinterfacetable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ceedot3pauseexttable is not None and self.ceedot3pauseexttable.has_operation()) or
            (self.ceesubinterfacetable is not None and self.ceesubinterfacetable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB" + path_buffer

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

        if (child_yang_name == "ceeDot3PauseExtTable"):
            if (self.ceedot3pauseexttable is None):
                self.ceedot3pauseexttable = CiscoEtherlikeExtMib.Ceedot3Pauseexttable()
                self.ceedot3pauseexttable.parent = self
                self._children_name_map["ceedot3pauseexttable"] = "ceeDot3PauseExtTable"
            return self.ceedot3pauseexttable

        if (child_yang_name == "ceeSubInterfaceTable"):
            if (self.ceesubinterfacetable is None):
                self.ceesubinterfacetable = CiscoEtherlikeExtMib.Ceesubinterfacetable()
                self.ceesubinterfacetable.parent = self
                self._children_name_map["ceesubinterfacetable"] = "ceeSubInterfaceTable"
            return self.ceesubinterfacetable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ceeDot3PauseExtTable" or name == "ceeSubInterfaceTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoEtherlikeExtMib()
        return self._top_entity

