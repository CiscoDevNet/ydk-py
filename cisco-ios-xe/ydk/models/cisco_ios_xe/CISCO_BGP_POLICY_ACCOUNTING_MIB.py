""" CISCO_BGP_POLICY_ACCOUNTING_MIB 

BGP policy based accounting information

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoBgpPolicyAccountingMib(Entity):
    """
    
    
    .. attribute:: cbpaccttable
    
    	The cbpAcctTable provides statistics about ingress and egress  traffic on an interface. This data could be used for purposes  like billing
    	**type**\:   :py:class:`Cbpaccttable <ydk.models.cisco_ios_xe.CISCO_BGP_POLICY_ACCOUNTING_MIB.CiscoBgpPolicyAccountingMib.Cbpaccttable>`
    
    

    """

    _prefix = 'CISCO-BGP-POLICY-ACCOUNTING-MIB'
    _revision = '2002-07-26'

    def __init__(self):
        super(CiscoBgpPolicyAccountingMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-BGP-POLICY-ACCOUNTING-MIB"
        self.yang_parent_name = "CISCO-BGP-POLICY-ACCOUNTING-MIB"

        self.cbpaccttable = CiscoBgpPolicyAccountingMib.Cbpaccttable()
        self.cbpaccttable.parent = self
        self._children_name_map["cbpaccttable"] = "cbpAcctTable"
        self._children_yang_names.add("cbpAcctTable")


    class Cbpaccttable(Entity):
        """
        The cbpAcctTable provides statistics about ingress and egress 
        traffic on an interface. This data could be used for purposes 
        like billing.
        
        .. attribute:: cbpacctentry
        
        	Each cbpAcctEntry provides statistics for traffic of interest on an ingress and/or egress interfaces. The traffic of interest  may be used for purposes like billing, and is referred to from  here on in the MIB by the term 'traffic\-type', which corresponds to cbpAcctTrafficIndex. Traffic\-types are configured by the user on a per interface basis.  The statistics include ingress packet counts, ingress octet counts, egress packet counts and egress octet counts. Entries  are created when traffic\-type is configured on an interface. Entries are deleted automatically when the user  removes the corresponding traffic\-type configuration from an interface
        	**type**\: list of    :py:class:`Cbpacctentry <ydk.models.cisco_ios_xe.CISCO_BGP_POLICY_ACCOUNTING_MIB.CiscoBgpPolicyAccountingMib.Cbpaccttable.Cbpacctentry>`
        
        

        """

        _prefix = 'CISCO-BGP-POLICY-ACCOUNTING-MIB'
        _revision = '2002-07-26'

        def __init__(self):
            super(CiscoBgpPolicyAccountingMib.Cbpaccttable, self).__init__()

            self.yang_name = "cbpAcctTable"
            self.yang_parent_name = "CISCO-BGP-POLICY-ACCOUNTING-MIB"

            self.cbpacctentry = YList(self)

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
                        super(CiscoBgpPolicyAccountingMib.Cbpaccttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoBgpPolicyAccountingMib.Cbpaccttable, self).__setattr__(name, value)


        class Cbpacctentry(Entity):
            """
            Each cbpAcctEntry provides statistics for traffic of interest
            on an ingress and/or egress interfaces. The traffic of interest 
            may be used for purposes like billing, and is referred to from 
            here on in the MIB by the term 'traffic\-type', which corresponds
            to cbpAcctTrafficIndex. Traffic\-types are configured by the user
            on a per interface basis.
            
            The statistics include ingress packet counts, ingress octet
            counts, egress packet counts and egress octet counts. Entries 
            are created when traffic\-type is configured on an interface.
            Entries are deleted automatically when the user 
            removes the corresponding traffic\-type configuration from an
            interface.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cbpaccttrafficindex  <key>
            
            	An integer value greater than 0, that uniquely identifies a traffic\-type. The traffic\-type has no intrinsic meaning. It just means the traffic coming into an interface can be differentiated into different types. It is up to the user to give meaning to and configure the various traffic\-types on an  interface
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cbpacctinoctetcount
            
            	The total number of octets received for a particular traffic\-type on an interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbpacctinpacketcount
            
            	The total number of packets received for a particular traffic\-type on an interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbpacctoutoctetcount
            
            	The total number of octets transmitted for a particular traffic\-type on an interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cbpacctoutpacketcount
            
            	The total number of packets transmitted for a particular traffic\-type on an interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'CISCO-BGP-POLICY-ACCOUNTING-MIB'
            _revision = '2002-07-26'

            def __init__(self):
                super(CiscoBgpPolicyAccountingMib.Cbpaccttable.Cbpacctentry, self).__init__()

                self.yang_name = "cbpAcctEntry"
                self.yang_parent_name = "cbpAcctTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cbpaccttrafficindex = YLeaf(YType.int32, "cbpAcctTrafficIndex")

                self.cbpacctinoctetcount = YLeaf(YType.uint64, "cbpAcctInOctetCount")

                self.cbpacctinpacketcount = YLeaf(YType.uint64, "cbpAcctInPacketCount")

                self.cbpacctoutoctetcount = YLeaf(YType.uint64, "cbpAcctOutOctetCount")

                self.cbpacctoutpacketcount = YLeaf(YType.uint64, "cbpAcctOutPacketCount")

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
                                "cbpaccttrafficindex",
                                "cbpacctinoctetcount",
                                "cbpacctinpacketcount",
                                "cbpacctoutoctetcount",
                                "cbpacctoutpacketcount") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoBgpPolicyAccountingMib.Cbpaccttable.Cbpacctentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoBgpPolicyAccountingMib.Cbpaccttable.Cbpacctentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cbpaccttrafficindex.is_set or
                    self.cbpacctinoctetcount.is_set or
                    self.cbpacctinpacketcount.is_set or
                    self.cbpacctoutoctetcount.is_set or
                    self.cbpacctoutpacketcount.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cbpaccttrafficindex.yfilter != YFilter.not_set or
                    self.cbpacctinoctetcount.yfilter != YFilter.not_set or
                    self.cbpacctinpacketcount.yfilter != YFilter.not_set or
                    self.cbpacctoutoctetcount.yfilter != YFilter.not_set or
                    self.cbpacctoutpacketcount.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cbpAcctEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[cbpAcctTrafficIndex='" + self.cbpaccttrafficindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-BGP-POLICY-ACCOUNTING-MIB:CISCO-BGP-POLICY-ACCOUNTING-MIB/cbpAcctTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cbpaccttrafficindex.is_set or self.cbpaccttrafficindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbpaccttrafficindex.get_name_leafdata())
                if (self.cbpacctinoctetcount.is_set or self.cbpacctinoctetcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbpacctinoctetcount.get_name_leafdata())
                if (self.cbpacctinpacketcount.is_set or self.cbpacctinpacketcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbpacctinpacketcount.get_name_leafdata())
                if (self.cbpacctoutoctetcount.is_set or self.cbpacctoutoctetcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbpacctoutoctetcount.get_name_leafdata())
                if (self.cbpacctoutpacketcount.is_set or self.cbpacctoutpacketcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbpacctoutpacketcount.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cbpAcctTrafficIndex" or name == "cbpAcctInOctetCount" or name == "cbpAcctInPacketCount" or name == "cbpAcctOutOctetCount" or name == "cbpAcctOutPacketCount"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cbpAcctTrafficIndex"):
                    self.cbpaccttrafficindex = value
                    self.cbpaccttrafficindex.value_namespace = name_space
                    self.cbpaccttrafficindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cbpAcctInOctetCount"):
                    self.cbpacctinoctetcount = value
                    self.cbpacctinoctetcount.value_namespace = name_space
                    self.cbpacctinoctetcount.value_namespace_prefix = name_space_prefix
                if(value_path == "cbpAcctInPacketCount"):
                    self.cbpacctinpacketcount = value
                    self.cbpacctinpacketcount.value_namespace = name_space
                    self.cbpacctinpacketcount.value_namespace_prefix = name_space_prefix
                if(value_path == "cbpAcctOutOctetCount"):
                    self.cbpacctoutoctetcount = value
                    self.cbpacctoutoctetcount.value_namespace = name_space
                    self.cbpacctoutoctetcount.value_namespace_prefix = name_space_prefix
                if(value_path == "cbpAcctOutPacketCount"):
                    self.cbpacctoutpacketcount = value
                    self.cbpacctoutpacketcount.value_namespace = name_space
                    self.cbpacctoutpacketcount.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cbpacctentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cbpacctentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cbpAcctTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-BGP-POLICY-ACCOUNTING-MIB:CISCO-BGP-POLICY-ACCOUNTING-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cbpAcctEntry"):
                for c in self.cbpacctentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoBgpPolicyAccountingMib.Cbpaccttable.Cbpacctentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cbpacctentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cbpAcctEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.cbpaccttable is not None and self.cbpaccttable.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cbpaccttable is not None and self.cbpaccttable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-BGP-POLICY-ACCOUNTING-MIB:CISCO-BGP-POLICY-ACCOUNTING-MIB" + path_buffer

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

        if (child_yang_name == "cbpAcctTable"):
            if (self.cbpaccttable is None):
                self.cbpaccttable = CiscoBgpPolicyAccountingMib.Cbpaccttable()
                self.cbpaccttable.parent = self
                self._children_name_map["cbpaccttable"] = "cbpAcctTable"
            return self.cbpaccttable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cbpAcctTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoBgpPolicyAccountingMib()
        return self._top_entity

