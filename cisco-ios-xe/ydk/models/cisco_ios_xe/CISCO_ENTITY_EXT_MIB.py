""" CISCO_ENTITY_EXT_MIB 

This MIB is an extension of the ENTITY\-MIB
specified in RFC2737.

This MIB module contains  Cisco\-defined  extensions 
to the  entityPhysicalTable to represent information
related to entities of class module(entPhysicalClass
= 'module') which have a Processor.

A processor module is defined as a physical entity
that has a CPU, RAM and NVRAM  so that
it can independently
   \- load a bootable image
   \- save configuration.
This module is the entry point for external
applications like SNMP Manager, CLI, FTP etc.

Line card is an interface card         with at least a 
Processor and RAM. This might be referred to as 
Service Module in some cisco products.

A configuration register is  a 16 bit 
software register.
The configuration register is mainly used to 
check for instructions on where to find the Cisco 
Operating System software.
Some other functions of configuration register are\:
 \- To select a boot source and default boot filename.
 \- To enable or disable the Break function.
 \- To control broadcast addresses.
 \- To set the console terminal baud rate.
 \- To load operating software from Flash memory.
 \- To allow us to manually boot the system using the 
   boot command at the bootstrap program prompt.

Booting is the process of initializing the
hardware and starting the Operating System.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoEntityExtMib(Entity):
    """
    
    
    .. attribute:: ceextconfigregtable
    
    	The ceExtConfigRegTable extends the ENTITY\-MIB entPhysicalTable
    	**type**\:   :py:class:`Ceextconfigregtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB.CiscoEntityExtMib.Ceextconfigregtable>`
    
    .. attribute:: ceextentityledtable
    
    	A table containing information of LED on an entity
    	**type**\:   :py:class:`Ceextentityledtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB.CiscoEntityExtMib.Ceextentityledtable>`
    
    .. attribute:: ceextphysicalprocessortable
    
    	The ceExtPhysicalProcessorTable extends the ENTITY\-MIB entPhysicalTable for modules (Non FRUs(Field Replacable Units) or FRUs)
    	**type**\:   :py:class:`Ceextphysicalprocessortable <ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB.CiscoEntityExtMib.Ceextphysicalprocessortable>`
    
    

    """

    _prefix = 'CISCO-ENTITY-EXT-MIB'
    _revision = '2008-11-24'

    def __init__(self):
        super(CiscoEntityExtMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ENTITY-EXT-MIB"
        self.yang_parent_name = "CISCO-ENTITY-EXT-MIB"

        self.ceextconfigregtable = CiscoEntityExtMib.Ceextconfigregtable()
        self.ceextconfigregtable.parent = self
        self._children_name_map["ceextconfigregtable"] = "ceExtConfigRegTable"
        self._children_yang_names.add("ceExtConfigRegTable")

        self.ceextentityledtable = CiscoEntityExtMib.Ceextentityledtable()
        self.ceextentityledtable.parent = self
        self._children_name_map["ceextentityledtable"] = "ceExtEntityLEDTable"
        self._children_yang_names.add("ceExtEntityLEDTable")

        self.ceextphysicalprocessortable = CiscoEntityExtMib.Ceextphysicalprocessortable()
        self.ceextphysicalprocessortable.parent = self
        self._children_name_map["ceextphysicalprocessortable"] = "ceExtPhysicalProcessorTable"
        self._children_yang_names.add("ceExtPhysicalProcessorTable")


    class Ceextphysicalprocessortable(Entity):
        """
        The ceExtPhysicalProcessorTable extends
        the ENTITY\-MIB entPhysicalTable for modules
        (Non FRUs(Field Replacable Units) or FRUs).
        
        .. attribute:: ceextphysicalprocessorentry
        
        	A ceExtPhysicalProcessorTable entry extends a corresponding entPhysicalTable entry of class module(entPhysicalClass = 'module').  A processor module or line card which  has a processor will have an entry in this table.  A processor module or line card having multiple processors and is a SMP(Symmetric multi processor) system will have only  one entry corresponding to all the processors  since the resources defined below are shared.  A processor module or line card having multiple processors and is not an SMP system would register the processors as separate entities.  Entries are created by the agent at the system power\-up or module insertion.  Entries are removed when the module is reset or removed
        	**type**\: list of    :py:class:`Ceextphysicalprocessorentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB.CiscoEntityExtMib.Ceextphysicalprocessortable.Ceextphysicalprocessorentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-EXT-MIB'
        _revision = '2008-11-24'

        def __init__(self):
            super(CiscoEntityExtMib.Ceextphysicalprocessortable, self).__init__()

            self.yang_name = "ceExtPhysicalProcessorTable"
            self.yang_parent_name = "CISCO-ENTITY-EXT-MIB"

            self.ceextphysicalprocessorentry = YList(self)

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
                        super(CiscoEntityExtMib.Ceextphysicalprocessortable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityExtMib.Ceextphysicalprocessortable, self).__setattr__(name, value)


        class Ceextphysicalprocessorentry(Entity):
            """
            A ceExtPhysicalProcessorTable entry extends
            a corresponding entPhysicalTable entry of class
            module(entPhysicalClass = 'module').
            
            A processor module or line card which 
            has a processor will have an entry in
            this table.
            
            A processor module or line card having
            multiple processors and is a SMP(Symmetric
            multi processor) system will have only 
            one entry corresponding to all the processors 
            since the resources defined below are shared.
            
            A processor module or line card having
            multiple processors and is not an SMP system
            would register the processors as separate entities.
            
            Entries are created by the agent at the system power\-up
            or module insertion.
            
            Entries are removed when the module is reset or removed.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceexthcprocessorram
            
            	This object represents the total number of bytes of RAM available on the Processor. This object is a 64\-bit version of ceExtProcessorRam
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: ceextnvramsize
            
            	Total number of bytes of NVRAM in the entity.  A value of 0 for this object means the entity does not support NVRAM or NVRAM information  is not available
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: ceextnvramused
            
            	Number of bytes of NVRAM in use. This object is irrelevant if ceExtNVRAMSize is 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: ceextprocessorram
            
            	Total number of bytes of RAM available on the Processor
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: ceextprocessorramoverflow
            
            	This object represents the upper 32\-bit of ceExtProcessorRam. This object needs to be supported only if the available RAM bytes exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            

            """

            _prefix = 'CISCO-ENTITY-EXT-MIB'
            _revision = '2008-11-24'

            def __init__(self):
                super(CiscoEntityExtMib.Ceextphysicalprocessortable.Ceextphysicalprocessorentry, self).__init__()

                self.yang_name = "ceExtPhysicalProcessorEntry"
                self.yang_parent_name = "ceExtPhysicalProcessorTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceexthcprocessorram = YLeaf(YType.uint64, "ceExtHCProcessorRam")

                self.ceextnvramsize = YLeaf(YType.uint32, "ceExtNVRAMSize")

                self.ceextnvramused = YLeaf(YType.uint32, "ceExtNVRAMUsed")

                self.ceextprocessorram = YLeaf(YType.uint32, "ceExtProcessorRam")

                self.ceextprocessorramoverflow = YLeaf(YType.uint32, "ceExtProcessorRamOverflow")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "ceexthcprocessorram",
                                "ceextnvramsize",
                                "ceextnvramused",
                                "ceextprocessorram",
                                "ceextprocessorramoverflow") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityExtMib.Ceextphysicalprocessortable.Ceextphysicalprocessorentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityExtMib.Ceextphysicalprocessortable.Ceextphysicalprocessorentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.ceexthcprocessorram.is_set or
                    self.ceextnvramsize.is_set or
                    self.ceextnvramused.is_set or
                    self.ceextprocessorram.is_set or
                    self.ceextprocessorramoverflow.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.ceexthcprocessorram.yfilter != YFilter.not_set or
                    self.ceextnvramsize.yfilter != YFilter.not_set or
                    self.ceextnvramused.yfilter != YFilter.not_set or
                    self.ceextprocessorram.yfilter != YFilter.not_set or
                    self.ceextprocessorramoverflow.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ceExtPhysicalProcessorEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/ceExtPhysicalProcessorTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.ceexthcprocessorram.is_set or self.ceexthcprocessorram.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceexthcprocessorram.get_name_leafdata())
                if (self.ceextnvramsize.is_set or self.ceextnvramsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceextnvramsize.get_name_leafdata())
                if (self.ceextnvramused.is_set or self.ceextnvramused.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceextnvramused.get_name_leafdata())
                if (self.ceextprocessorram.is_set or self.ceextprocessorram.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceextprocessorram.get_name_leafdata())
                if (self.ceextprocessorramoverflow.is_set or self.ceextprocessorramoverflow.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceextprocessorramoverflow.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "ceExtHCProcessorRam" or name == "ceExtNVRAMSize" or name == "ceExtNVRAMUsed" or name == "ceExtProcessorRam" or name == "ceExtProcessorRamOverflow"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ceExtHCProcessorRam"):
                    self.ceexthcprocessorram = value
                    self.ceexthcprocessorram.value_namespace = name_space
                    self.ceexthcprocessorram.value_namespace_prefix = name_space_prefix
                if(value_path == "ceExtNVRAMSize"):
                    self.ceextnvramsize = value
                    self.ceextnvramsize.value_namespace = name_space
                    self.ceextnvramsize.value_namespace_prefix = name_space_prefix
                if(value_path == "ceExtNVRAMUsed"):
                    self.ceextnvramused = value
                    self.ceextnvramused.value_namespace = name_space
                    self.ceextnvramused.value_namespace_prefix = name_space_prefix
                if(value_path == "ceExtProcessorRam"):
                    self.ceextprocessorram = value
                    self.ceextprocessorram.value_namespace = name_space
                    self.ceextprocessorram.value_namespace_prefix = name_space_prefix
                if(value_path == "ceExtProcessorRamOverflow"):
                    self.ceextprocessorramoverflow = value
                    self.ceextprocessorramoverflow.value_namespace = name_space
                    self.ceextprocessorramoverflow.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ceextphysicalprocessorentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ceextphysicalprocessorentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ceExtPhysicalProcessorTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ceExtPhysicalProcessorEntry"):
                for c in self.ceextphysicalprocessorentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityExtMib.Ceextphysicalprocessortable.Ceextphysicalprocessorentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ceextphysicalprocessorentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ceExtPhysicalProcessorEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ceextconfigregtable(Entity):
        """
        The ceExtConfigRegTable extends
        the ENTITY\-MIB entPhysicalTable.
        
        .. attribute:: ceextconfigregentry
        
        	A ceExtConfigRegTable entry extends a corresponding entPhysicalTable entry of class module which has a configuration register.  Entries are created by the agent at the system power\-up or module insertion.  Entries are removed when the module is reset or  removed
        	**type**\: list of    :py:class:`Ceextconfigregentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB.CiscoEntityExtMib.Ceextconfigregtable.Ceextconfigregentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-EXT-MIB'
        _revision = '2008-11-24'

        def __init__(self):
            super(CiscoEntityExtMib.Ceextconfigregtable, self).__init__()

            self.yang_name = "ceExtConfigRegTable"
            self.yang_parent_name = "CISCO-ENTITY-EXT-MIB"

            self.ceextconfigregentry = YList(self)

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
                        super(CiscoEntityExtMib.Ceextconfigregtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityExtMib.Ceextconfigregtable, self).__setattr__(name, value)


        class Ceextconfigregentry(Entity):
            """
            A ceExtConfigRegTable entry extends
            a corresponding entPhysicalTable entry of class
            module which has a configuration register.
            
            Entries are created by the agent at the system power\-up
            or module insertion.
            
            Entries are removed when the module is reset or 
            removed.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceextconfigregister
            
            	The value of configuration register with which the processor module booted
            	**type**\:  str
            
            .. attribute:: ceextconfigregnext
            
            	The value of configuration register in the processor module at next reboot. Just after  the reboot this has the same value as  ceExtConfigRegister
            	**type**\:  str
            
            .. attribute:: ceextkickstartimagelist
            
            	The list of system kickstart images which can be used for booting
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ceextsysbootimagelist
            
            	The list of system boot images which can be used for booting
            	**type**\:  str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-ENTITY-EXT-MIB'
            _revision = '2008-11-24'

            def __init__(self):
                super(CiscoEntityExtMib.Ceextconfigregtable.Ceextconfigregentry, self).__init__()

                self.yang_name = "ceExtConfigRegEntry"
                self.yang_parent_name = "ceExtConfigRegTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceextconfigregister = YLeaf(YType.str, "ceExtConfigRegister")

                self.ceextconfigregnext = YLeaf(YType.str, "ceExtConfigRegNext")

                self.ceextkickstartimagelist = YLeaf(YType.str, "ceExtKickstartImageList")

                self.ceextsysbootimagelist = YLeaf(YType.str, "ceExtSysBootImageList")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "ceextconfigregister",
                                "ceextconfigregnext",
                                "ceextkickstartimagelist",
                                "ceextsysbootimagelist") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityExtMib.Ceextconfigregtable.Ceextconfigregentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityExtMib.Ceextconfigregtable.Ceextconfigregentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.ceextconfigregister.is_set or
                    self.ceextconfigregnext.is_set or
                    self.ceextkickstartimagelist.is_set or
                    self.ceextsysbootimagelist.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.ceextconfigregister.yfilter != YFilter.not_set or
                    self.ceextconfigregnext.yfilter != YFilter.not_set or
                    self.ceextkickstartimagelist.yfilter != YFilter.not_set or
                    self.ceextsysbootimagelist.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ceExtConfigRegEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/ceExtConfigRegTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.ceextconfigregister.is_set or self.ceextconfigregister.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceextconfigregister.get_name_leafdata())
                if (self.ceextconfigregnext.is_set or self.ceextconfigregnext.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceextconfigregnext.get_name_leafdata())
                if (self.ceextkickstartimagelist.is_set or self.ceextkickstartimagelist.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceextkickstartimagelist.get_name_leafdata())
                if (self.ceextsysbootimagelist.is_set or self.ceextsysbootimagelist.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceextsysbootimagelist.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "ceExtConfigRegister" or name == "ceExtConfigRegNext" or name == "ceExtKickstartImageList" or name == "ceExtSysBootImageList"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ceExtConfigRegister"):
                    self.ceextconfigregister = value
                    self.ceextconfigregister.value_namespace = name_space
                    self.ceextconfigregister.value_namespace_prefix = name_space_prefix
                if(value_path == "ceExtConfigRegNext"):
                    self.ceextconfigregnext = value
                    self.ceextconfigregnext.value_namespace = name_space
                    self.ceextconfigregnext.value_namespace_prefix = name_space_prefix
                if(value_path == "ceExtKickstartImageList"):
                    self.ceextkickstartimagelist = value
                    self.ceextkickstartimagelist.value_namespace = name_space
                    self.ceextkickstartimagelist.value_namespace_prefix = name_space_prefix
                if(value_path == "ceExtSysBootImageList"):
                    self.ceextsysbootimagelist = value
                    self.ceextsysbootimagelist.value_namespace = name_space
                    self.ceextsysbootimagelist.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ceextconfigregentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ceextconfigregentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ceExtConfigRegTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ceExtConfigRegEntry"):
                for c in self.ceextconfigregentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityExtMib.Ceextconfigregtable.Ceextconfigregentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ceextconfigregentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ceExtConfigRegEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ceextentityledtable(Entity):
        """
        A table containing information of LED on an entity.
        
        .. attribute:: ceextentityledentry
        
        	An entry (conceptual row) in the ceExtEntityLEDTable, containing information about an LED on an entity, identified by  entPhysicalIndex
        	**type**\: list of    :py:class:`Ceextentityledentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB.CiscoEntityExtMib.Ceextentityledtable.Ceextentityledentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-EXT-MIB'
        _revision = '2008-11-24'

        def __init__(self):
            super(CiscoEntityExtMib.Ceextentityledtable, self).__init__()

            self.yang_name = "ceExtEntityLEDTable"
            self.yang_parent_name = "CISCO-ENTITY-EXT-MIB"

            self.ceextentityledentry = YList(self)

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
                        super(CiscoEntityExtMib.Ceextentityledtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityExtMib.Ceextentityledtable, self).__setattr__(name, value)


        class Ceextentityledentry(Entity):
            """
            An entry (conceptual row) in the ceExtEntityLEDTable,
            containing information about an LED on an entity, identified by 
            entPhysicalIndex.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceextentityledtype  <key>
            
            	The type of LED on this entity. 'status' \- indicates the entity status. 'system' \- indicates the overall system status.  'active' \- the redundancy status of a module, for e.g.            supervisor module.  'power'  \- indicates sufficient power availability for all             modules. 'battery'\- indicates the battery status
            	**type**\:   :py:class:`Ceextentityledtype <ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB.CiscoEntityExtMib.Ceextentityledtable.Ceextentityledentry.Ceextentityledtype>`
            
            .. attribute:: ceextentityledcolor
            
            	The color of the LED
            	**type**\:   :py:class:`Ceextentityledcolor <ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB.CiscoEntityExtMib.Ceextentityledtable.Ceextentityledentry.Ceextentityledcolor>`
            
            

            """

            _prefix = 'CISCO-ENTITY-EXT-MIB'
            _revision = '2008-11-24'

            def __init__(self):
                super(CiscoEntityExtMib.Ceextentityledtable.Ceextentityledentry, self).__init__()

                self.yang_name = "ceExtEntityLEDEntry"
                self.yang_parent_name = "ceExtEntityLEDTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceextentityledtype = YLeaf(YType.enumeration, "ceExtEntityLEDType")

                self.ceextentityledcolor = YLeaf(YType.enumeration, "ceExtEntityLEDColor")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "ceextentityledtype",
                                "ceextentityledcolor") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityExtMib.Ceextentityledtable.Ceextentityledentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityExtMib.Ceextentityledtable.Ceextentityledentry, self).__setattr__(name, value)

            class Ceextentityledcolor(Enum):
                """
                Ceextentityledcolor

                The color of the LED.

                .. data:: off = 1

                .. data:: green = 2

                .. data:: amber = 3

                .. data:: red = 4

                """

                off = Enum.YLeaf(1, "off")

                green = Enum.YLeaf(2, "green")

                amber = Enum.YLeaf(3, "amber")

                red = Enum.YLeaf(4, "red")


            class Ceextentityledtype(Enum):
                """
                Ceextentityledtype

                The type of LED on this entity.

                'status' \- indicates the entity status.

                'system' \- indicates the overall system status. 

                'active' \- the redundancy status of a module, for e.g.

                           supervisor module. 

                'power'  \- indicates sufficient power availability for all 

                           modules.

                'battery'\- indicates the battery status.

                .. data:: status = 1

                .. data:: system = 2

                .. data:: active = 3

                .. data:: power = 4

                .. data:: battery = 5

                """

                status = Enum.YLeaf(1, "status")

                system = Enum.YLeaf(2, "system")

                active = Enum.YLeaf(3, "active")

                power = Enum.YLeaf(4, "power")

                battery = Enum.YLeaf(5, "battery")


            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.ceextentityledtype.is_set or
                    self.ceextentityledcolor.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.ceextentityledtype.yfilter != YFilter.not_set or
                    self.ceextentityledcolor.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ceExtEntityLEDEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[ceExtEntityLEDType='" + self.ceextentityledtype.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/ceExtEntityLEDTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.ceextentityledtype.is_set or self.ceextentityledtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceextentityledtype.get_name_leafdata())
                if (self.ceextentityledcolor.is_set or self.ceextentityledcolor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceextentityledcolor.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "ceExtEntityLEDType" or name == "ceExtEntityLEDColor"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ceExtEntityLEDType"):
                    self.ceextentityledtype = value
                    self.ceextentityledtype.value_namespace = name_space
                    self.ceextentityledtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ceExtEntityLEDColor"):
                    self.ceextentityledcolor = value
                    self.ceextentityledcolor.value_namespace = name_space
                    self.ceextentityledcolor.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ceextentityledentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ceextentityledentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ceExtEntityLEDTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ceExtEntityLEDEntry"):
                for c in self.ceextentityledentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityExtMib.Ceextentityledtable.Ceextentityledentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ceextentityledentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ceExtEntityLEDEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ceextconfigregtable is not None and self.ceextconfigregtable.has_data()) or
            (self.ceextentityledtable is not None and self.ceextentityledtable.has_data()) or
            (self.ceextphysicalprocessortable is not None and self.ceextphysicalprocessortable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ceextconfigregtable is not None and self.ceextconfigregtable.has_operation()) or
            (self.ceextentityledtable is not None and self.ceextentityledtable.has_operation()) or
            (self.ceextphysicalprocessortable is not None and self.ceextphysicalprocessortable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB" + path_buffer

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

        if (child_yang_name == "ceExtConfigRegTable"):
            if (self.ceextconfigregtable is None):
                self.ceextconfigregtable = CiscoEntityExtMib.Ceextconfigregtable()
                self.ceextconfigregtable.parent = self
                self._children_name_map["ceextconfigregtable"] = "ceExtConfigRegTable"
            return self.ceextconfigregtable

        if (child_yang_name == "ceExtEntityLEDTable"):
            if (self.ceextentityledtable is None):
                self.ceextentityledtable = CiscoEntityExtMib.Ceextentityledtable()
                self.ceextentityledtable.parent = self
                self._children_name_map["ceextentityledtable"] = "ceExtEntityLEDTable"
            return self.ceextentityledtable

        if (child_yang_name == "ceExtPhysicalProcessorTable"):
            if (self.ceextphysicalprocessortable is None):
                self.ceextphysicalprocessortable = CiscoEntityExtMib.Ceextphysicalprocessortable()
                self.ceextphysicalprocessortable.parent = self
                self._children_name_map["ceextphysicalprocessortable"] = "ceExtPhysicalProcessorTable"
            return self.ceextphysicalprocessortable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ceExtConfigRegTable" or name == "ceExtEntityLEDTable" or name == "ceExtPhysicalProcessorTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoEntityExtMib()
        return self._top_entity

