""" CISCO_IETF_ATM2_PVCTRAP_MIB 

This MIB Module is a supplement to the
ATM\-MIB.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIetfAtm2PvctrapMib(Entity):
    """
    
    
    .. attribute:: atmcurrentlyfailingpvcltable
    
    	A table indicating all VCLs for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and an atmVclOperStatus with a value other than `up'
    	**type**\:   :py:class:`Atmcurrentlyfailingpvcltable <ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB.CiscoIetfAtm2PvctrapMib.Atmcurrentlyfailingpvcltable>`
    
    

    """

    _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB'
    _revision = '1998-02-03'

    def __init__(self):
        super(CiscoIetfAtm2PvctrapMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-ATM2-PVCTRAP-MIB"
        self.yang_parent_name = "CISCO-IETF-ATM2-PVCTRAP-MIB"

        self.atmcurrentlyfailingpvcltable = CiscoIetfAtm2PvctrapMib.Atmcurrentlyfailingpvcltable()
        self.atmcurrentlyfailingpvcltable.parent = self
        self._children_name_map["atmcurrentlyfailingpvcltable"] = "atmCurrentlyFailingPVclTable"
        self._children_yang_names.add("atmCurrentlyFailingPVclTable")


    class Atmcurrentlyfailingpvcltable(Entity):
        """
        A table indicating all VCLs for which there is an
        active row in the atmVclTable having an atmVclConnKind
        value of `pvc' and an atmVclOperStatus with a value
        other than `up'.
        
        .. attribute:: atmcurrentlyfailingpvclentry
        
        	Each entry in this table represents a VCL for which the atmVclRowStatus is `active', the atmVclConnKind is `pvc', and the atmVclOperStatus is other than `up'
        	**type**\: list of    :py:class:`Atmcurrentlyfailingpvclentry <ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB.CiscoIetfAtm2PvctrapMib.Atmcurrentlyfailingpvcltable.Atmcurrentlyfailingpvclentry>`
        
        

        """

        _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB'
        _revision = '1998-02-03'

        def __init__(self):
            super(CiscoIetfAtm2PvctrapMib.Atmcurrentlyfailingpvcltable, self).__init__()

            self.yang_name = "atmCurrentlyFailingPVclTable"
            self.yang_parent_name = "CISCO-IETF-ATM2-PVCTRAP-MIB"

            self.atmcurrentlyfailingpvclentry = YList(self)

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
                        super(CiscoIetfAtm2PvctrapMib.Atmcurrentlyfailingpvcltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfAtm2PvctrapMib.Atmcurrentlyfailingpvcltable, self).__setattr__(name, value)


        class Atmcurrentlyfailingpvclentry(Entity):
            """
            Each entry in this table represents a VCL for which
            the atmVclRowStatus is `active', the atmVclConnKind is
            `pvc', and the atmVclOperStatus is other than `up'.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: atmvclvci  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`atmvclvci <ydk.models.cisco_ios_xe.ATM_MIB.AtmMib.Atmvcltable.Atmvclentry>`
            
            .. attribute:: atmcurrentlyfailingpvcltimestamp
            
            	The time at which this PVCL began to fail
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: atmpreviouslyfailedpvcltimestamp
            
            	The time at which this PVCL began to fail during the PVC Notification interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-ATM2-PVCTRAP-MIB'
            _revision = '1998-02-03'

            def __init__(self):
                super(CiscoIetfAtm2PvctrapMib.Atmcurrentlyfailingpvcltable.Atmcurrentlyfailingpvclentry, self).__init__()

                self.yang_name = "atmCurrentlyFailingPVclEntry"
                self.yang_parent_name = "atmCurrentlyFailingPVclTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.atmvclvci = YLeaf(YType.str, "atmVclVci")

                self.atmcurrentlyfailingpvcltimestamp = YLeaf(YType.uint32, "atmCurrentlyFailingPVclTimeStamp")

                self.atmpreviouslyfailedpvcltimestamp = YLeaf(YType.uint32, "atmPreviouslyFailedPVclTimeStamp")

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
                                "atmvclvpi",
                                "atmvclvci",
                                "atmcurrentlyfailingpvcltimestamp",
                                "atmpreviouslyfailedpvcltimestamp") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfAtm2PvctrapMib.Atmcurrentlyfailingpvcltable.Atmcurrentlyfailingpvclentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfAtm2PvctrapMib.Atmcurrentlyfailingpvcltable.Atmcurrentlyfailingpvclentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.atmvclvpi.is_set or
                    self.atmvclvci.is_set or
                    self.atmcurrentlyfailingpvcltimestamp.is_set or
                    self.atmpreviouslyfailedpvcltimestamp.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.atmvclvpi.yfilter != YFilter.not_set or
                    self.atmvclvci.yfilter != YFilter.not_set or
                    self.atmcurrentlyfailingpvcltimestamp.yfilter != YFilter.not_set or
                    self.atmpreviouslyfailedpvcltimestamp.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "atmCurrentlyFailingPVclEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[atmVclVci='" + self.atmvclvci.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-ATM2-PVCTRAP-MIB:CISCO-IETF-ATM2-PVCTRAP-MIB/atmCurrentlyFailingPVclTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.atmvclvpi.is_set or self.atmvclvpi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvpi.get_name_leafdata())
                if (self.atmvclvci.is_set or self.atmvclvci.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmvclvci.get_name_leafdata())
                if (self.atmcurrentlyfailingpvcltimestamp.is_set or self.atmcurrentlyfailingpvcltimestamp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmcurrentlyfailingpvcltimestamp.get_name_leafdata())
                if (self.atmpreviouslyfailedpvcltimestamp.is_set or self.atmpreviouslyfailedpvcltimestamp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atmpreviouslyfailedpvcltimestamp.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "atmVclVpi" or name == "atmVclVci" or name == "atmCurrentlyFailingPVclTimeStamp" or name == "atmPreviouslyFailedPVclTimeStamp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVclVpi"):
                    self.atmvclvpi = value
                    self.atmvclvpi.value_namespace = name_space
                    self.atmvclvpi.value_namespace_prefix = name_space_prefix
                if(value_path == "atmVclVci"):
                    self.atmvclvci = value
                    self.atmvclvci.value_namespace = name_space
                    self.atmvclvci.value_namespace_prefix = name_space_prefix
                if(value_path == "atmCurrentlyFailingPVclTimeStamp"):
                    self.atmcurrentlyfailingpvcltimestamp = value
                    self.atmcurrentlyfailingpvcltimestamp.value_namespace = name_space
                    self.atmcurrentlyfailingpvcltimestamp.value_namespace_prefix = name_space_prefix
                if(value_path == "atmPreviouslyFailedPVclTimeStamp"):
                    self.atmpreviouslyfailedpvcltimestamp = value
                    self.atmpreviouslyfailedpvcltimestamp.value_namespace = name_space
                    self.atmpreviouslyfailedpvcltimestamp.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.atmcurrentlyfailingpvclentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.atmcurrentlyfailingpvclentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "atmCurrentlyFailingPVclTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-ATM2-PVCTRAP-MIB:CISCO-IETF-ATM2-PVCTRAP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "atmCurrentlyFailingPVclEntry"):
                for c in self.atmcurrentlyfailingpvclentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfAtm2PvctrapMib.Atmcurrentlyfailingpvcltable.Atmcurrentlyfailingpvclentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.atmcurrentlyfailingpvclentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "atmCurrentlyFailingPVclEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.atmcurrentlyfailingpvcltable is not None and self.atmcurrentlyfailingpvcltable.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.atmcurrentlyfailingpvcltable is not None and self.atmcurrentlyfailingpvcltable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IETF-ATM2-PVCTRAP-MIB:CISCO-IETF-ATM2-PVCTRAP-MIB" + path_buffer

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

        if (child_yang_name == "atmCurrentlyFailingPVclTable"):
            if (self.atmcurrentlyfailingpvcltable is None):
                self.atmcurrentlyfailingpvcltable = CiscoIetfAtm2PvctrapMib.Atmcurrentlyfailingpvcltable()
                self.atmcurrentlyfailingpvcltable.parent = self
                self._children_name_map["atmcurrentlyfailingpvcltable"] = "atmCurrentlyFailingPVclTable"
            return self.atmcurrentlyfailingpvcltable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "atmCurrentlyFailingPVclTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIetfAtm2PvctrapMib()
        return self._top_entity

