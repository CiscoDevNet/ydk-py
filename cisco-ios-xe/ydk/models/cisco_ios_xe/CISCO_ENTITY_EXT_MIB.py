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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOENTITYEXTMIB(Entity):
    """
    
    
    .. attribute:: ceextphysicalprocessortable
    
    	The ceExtPhysicalProcessorTable extends the ENTITY\-MIB entPhysicalTable for modules (Non FRUs(Field Replacable Units) or FRUs)
    	**type**\:  :py:class:`CeExtPhysicalProcessorTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB.CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable>`
    
    	**config**\: False
    
    .. attribute:: ceextconfigregtable
    
    	The ceExtConfigRegTable extends the ENTITY\-MIB entPhysicalTable
    	**type**\:  :py:class:`CeExtConfigRegTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB.CISCOENTITYEXTMIB.CeExtConfigRegTable>`
    
    	**config**\: False
    
    .. attribute:: ceextentityledtable
    
    	A table containing information of LED on an entity
    	**type**\:  :py:class:`CeExtEntityLEDTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB.CISCOENTITYEXTMIB.CeExtEntityLEDTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-ENTITY-EXT-MIB'
    _revision = '2008-11-24'

    def __init__(self):
        super(CISCOENTITYEXTMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ENTITY-EXT-MIB"
        self.yang_parent_name = "CISCO-ENTITY-EXT-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ceExtPhysicalProcessorTable", ("ceextphysicalprocessortable", CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable)), ("ceExtConfigRegTable", ("ceextconfigregtable", CISCOENTITYEXTMIB.CeExtConfigRegTable)), ("ceExtEntityLEDTable", ("ceextentityledtable", CISCOENTITYEXTMIB.CeExtEntityLEDTable))])
        self._leafs = OrderedDict()

        self.ceextphysicalprocessortable = CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable()
        self.ceextphysicalprocessortable.parent = self
        self._children_name_map["ceextphysicalprocessortable"] = "ceExtPhysicalProcessorTable"

        self.ceextconfigregtable = CISCOENTITYEXTMIB.CeExtConfigRegTable()
        self.ceextconfigregtable.parent = self
        self._children_name_map["ceextconfigregtable"] = "ceExtConfigRegTable"

        self.ceextentityledtable = CISCOENTITYEXTMIB.CeExtEntityLEDTable()
        self.ceextentityledtable.parent = self
        self._children_name_map["ceextentityledtable"] = "ceExtEntityLEDTable"
        self._segment_path = lambda: "CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOENTITYEXTMIB, [], name, value)


    class CeExtPhysicalProcessorTable(Entity):
        """
        The ceExtPhysicalProcessorTable extends
        the ENTITY\-MIB entPhysicalTable for modules
        (Non FRUs(Field Replacable Units) or FRUs).
        
        .. attribute:: ceextphysicalprocessorentry
        
        	A ceExtPhysicalProcessorTable entry extends a corresponding entPhysicalTable entry of class module(entPhysicalClass = 'module').  A processor module or line card which  has a processor will have an entry in this table.  A processor module or line card having multiple processors and is a SMP(Symmetric multi processor) system will have only  one entry corresponding to all the processors  since the resources defined below are shared.  A processor module or line card having multiple processors and is not an SMP system would register the processors as separate entities.  Entries are created by the agent at the system power\-up or module insertion.  Entries are removed when the module is reset or removed
        	**type**\: list of  		 :py:class:`CeExtPhysicalProcessorEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB.CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable.CeExtPhysicalProcessorEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-ENTITY-EXT-MIB'
        _revision = '2008-11-24'

        def __init__(self):
            super(CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable, self).__init__()

            self.yang_name = "ceExtPhysicalProcessorTable"
            self.yang_parent_name = "CISCO-ENTITY-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ceExtPhysicalProcessorEntry", ("ceextphysicalprocessorentry", CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable.CeExtPhysicalProcessorEntry))])
            self._leafs = OrderedDict()

            self.ceextphysicalprocessorentry = YList(self)
            self._segment_path = lambda: "ceExtPhysicalProcessorTable"
            self._absolute_path = lambda: "CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable, [], name, value)


        class CeExtPhysicalProcessorEntry(Entity):
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
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: ceextprocessorram
            
            	Total number of bytes of RAM available on the Processor
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: ceextnvramsize
            
            	Total number of bytes of NVRAM in the entity.  A value of 0 for this object means the entity does not support NVRAM or NVRAM information  is not available
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: ceextnvramused
            
            	Number of bytes of NVRAM in use. This object is irrelevant if ceExtNVRAMSize is 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: ceextprocessorramoverflow
            
            	This object represents the upper 32\-bit of ceExtProcessorRam. This object needs to be supported only if the available RAM bytes exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: ceexthcprocessorram
            
            	This object represents the total number of bytes of RAM available on the Processor. This object is a 64\-bit version of ceExtProcessorRam
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            

            """

            _prefix = 'CISCO-ENTITY-EXT-MIB'
            _revision = '2008-11-24'

            def __init__(self):
                super(CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable.CeExtPhysicalProcessorEntry, self).__init__()

                self.yang_name = "ceExtPhysicalProcessorEntry"
                self.yang_parent_name = "ceExtPhysicalProcessorTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('ceextprocessorram', (YLeaf(YType.uint32, 'ceExtProcessorRam'), ['int'])),
                    ('ceextnvramsize', (YLeaf(YType.uint32, 'ceExtNVRAMSize'), ['int'])),
                    ('ceextnvramused', (YLeaf(YType.uint32, 'ceExtNVRAMUsed'), ['int'])),
                    ('ceextprocessorramoverflow', (YLeaf(YType.uint32, 'ceExtProcessorRamOverflow'), ['int'])),
                    ('ceexthcprocessorram', (YLeaf(YType.uint64, 'ceExtHCProcessorRam'), ['int'])),
                ])
                self.entphysicalindex = None
                self.ceextprocessorram = None
                self.ceextnvramsize = None
                self.ceextnvramused = None
                self.ceextprocessorramoverflow = None
                self.ceexthcprocessorram = None
                self._segment_path = lambda: "ceExtPhysicalProcessorEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/ceExtPhysicalProcessorTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable.CeExtPhysicalProcessorEntry, ['entphysicalindex', 'ceextprocessorram', 'ceextnvramsize', 'ceextnvramused', 'ceextprocessorramoverflow', 'ceexthcprocessorram'], name, value)




    class CeExtConfigRegTable(Entity):
        """
        The ceExtConfigRegTable extends
        the ENTITY\-MIB entPhysicalTable.
        
        .. attribute:: ceextconfigregentry
        
        	A ceExtConfigRegTable entry extends a corresponding entPhysicalTable entry of class module which has a configuration register.  Entries are created by the agent at the system power\-up or module insertion.  Entries are removed when the module is reset or  removed
        	**type**\: list of  		 :py:class:`CeExtConfigRegEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB.CISCOENTITYEXTMIB.CeExtConfigRegTable.CeExtConfigRegEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-ENTITY-EXT-MIB'
        _revision = '2008-11-24'

        def __init__(self):
            super(CISCOENTITYEXTMIB.CeExtConfigRegTable, self).__init__()

            self.yang_name = "ceExtConfigRegTable"
            self.yang_parent_name = "CISCO-ENTITY-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ceExtConfigRegEntry", ("ceextconfigregentry", CISCOENTITYEXTMIB.CeExtConfigRegTable.CeExtConfigRegEntry))])
            self._leafs = OrderedDict()

            self.ceextconfigregentry = YList(self)
            self._segment_path = lambda: "ceExtConfigRegTable"
            self._absolute_path = lambda: "CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYEXTMIB.CeExtConfigRegTable, [], name, value)


        class CeExtConfigRegEntry(Entity):
            """
            A ceExtConfigRegTable entry extends
            a corresponding entPhysicalTable entry of class
            module which has a configuration register.
            
            Entries are created by the agent at the system power\-up
            or module insertion.
            
            Entries are removed when the module is reset or 
            removed.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: ceextconfigregister
            
            	The value of configuration register with which the processor module booted
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: ceextconfigregnext
            
            	The value of configuration register in the processor module at next reboot. Just after  the reboot this has the same value as  ceExtConfigRegister
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: ceextsysbootimagelist
            
            	The list of system boot images which can be used for booting
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: ceextkickstartimagelist
            
            	The list of system kickstart images which can be used for booting
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-ENTITY-EXT-MIB'
            _revision = '2008-11-24'

            def __init__(self):
                super(CISCOENTITYEXTMIB.CeExtConfigRegTable.CeExtConfigRegEntry, self).__init__()

                self.yang_name = "ceExtConfigRegEntry"
                self.yang_parent_name = "ceExtConfigRegTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('ceextconfigregister', (YLeaf(YType.str, 'ceExtConfigRegister'), ['str'])),
                    ('ceextconfigregnext', (YLeaf(YType.str, 'ceExtConfigRegNext'), ['str'])),
                    ('ceextsysbootimagelist', (YLeaf(YType.str, 'ceExtSysBootImageList'), ['str'])),
                    ('ceextkickstartimagelist', (YLeaf(YType.str, 'ceExtKickstartImageList'), ['str'])),
                ])
                self.entphysicalindex = None
                self.ceextconfigregister = None
                self.ceextconfigregnext = None
                self.ceextsysbootimagelist = None
                self.ceextkickstartimagelist = None
                self._segment_path = lambda: "ceExtConfigRegEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/ceExtConfigRegTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYEXTMIB.CeExtConfigRegTable.CeExtConfigRegEntry, ['entphysicalindex', 'ceextconfigregister', 'ceextconfigregnext', 'ceextsysbootimagelist', 'ceextkickstartimagelist'], name, value)




    class CeExtEntityLEDTable(Entity):
        """
        A table containing information of LED on an entity.
        
        .. attribute:: ceextentityledentry
        
        	An entry (conceptual row) in the ceExtEntityLEDTable, containing information about an LED on an entity, identified by  entPhysicalIndex
        	**type**\: list of  		 :py:class:`CeExtEntityLEDEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB.CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-ENTITY-EXT-MIB'
        _revision = '2008-11-24'

        def __init__(self):
            super(CISCOENTITYEXTMIB.CeExtEntityLEDTable, self).__init__()

            self.yang_name = "ceExtEntityLEDTable"
            self.yang_parent_name = "CISCO-ENTITY-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ceExtEntityLEDEntry", ("ceextentityledentry", CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry))])
            self._leafs = OrderedDict()

            self.ceextentityledentry = YList(self)
            self._segment_path = lambda: "ceExtEntityLEDTable"
            self._absolute_path = lambda: "CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYEXTMIB.CeExtEntityLEDTable, [], name, value)


        class CeExtEntityLEDEntry(Entity):
            """
            An entry (conceptual row) in the ceExtEntityLEDTable,
            containing information about an LED on an entity, identified by 
            entPhysicalIndex.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: ceextentityledtype  (key)
            
            	The type of LED on this entity. 'status' \- indicates the entity status. 'system' \- indicates the overall system status.  'active' \- the redundancy status of a module, for e.g.            supervisor module.  'power'  \- indicates sufficient power availability for all             modules. 'battery'\- indicates the battery status
            	**type**\:  :py:class:`CeExtEntityLEDType <ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB.CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry.CeExtEntityLEDType>`
            
            	**config**\: False
            
            .. attribute:: ceextentityledcolor
            
            	The color of the LED
            	**type**\:  :py:class:`CeExtEntityLEDColor <ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB.CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry.CeExtEntityLEDColor>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-ENTITY-EXT-MIB'
            _revision = '2008-11-24'

            def __init__(self):
                super(CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry, self).__init__()

                self.yang_name = "ceExtEntityLEDEntry"
                self.yang_parent_name = "ceExtEntityLEDTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ceextentityledtype']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('ceextentityledtype', (YLeaf(YType.enumeration, 'ceExtEntityLEDType'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB', 'CISCOENTITYEXTMIB', 'CeExtEntityLEDTable.CeExtEntityLEDEntry.CeExtEntityLEDType')])),
                    ('ceextentityledcolor', (YLeaf(YType.enumeration, 'ceExtEntityLEDColor'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB', 'CISCOENTITYEXTMIB', 'CeExtEntityLEDTable.CeExtEntityLEDEntry.CeExtEntityLEDColor')])),
                ])
                self.entphysicalindex = None
                self.ceextentityledtype = None
                self.ceextentityledcolor = None
                self._segment_path = lambda: "ceExtEntityLEDEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[ceExtEntityLEDType='" + str(self.ceextentityledtype) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/ceExtEntityLEDTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry, ['entphysicalindex', 'ceextentityledtype', 'ceextentityledcolor'], name, value)

            class CeExtEntityLEDColor(Enum):
                """
                CeExtEntityLEDColor (Enum Class)

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


            class CeExtEntityLEDType(Enum):
                """
                CeExtEntityLEDType (Enum Class)

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




    def clone_ptr(self):
        self._top_entity = CISCOENTITYEXTMIB()
        return self._top_entity



