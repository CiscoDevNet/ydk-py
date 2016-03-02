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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class CISCOENTITYEXTMIB(object):
    """
    
    
    .. attribute:: ceextconfigregtable
    
    	The ceExtConfigRegTable extends the ENTITY\-MIB entPhysicalTable
    	**type**\: :py:class:`CeExtConfigRegTable <ydk.models.entity.CISCO_ENTITY_EXT_MIB.CISCOENTITYEXTMIB.CeExtConfigRegTable>`
    
    .. attribute:: ceextentityledtable
    
    	A table containing information of LED on an entity
    	**type**\: :py:class:`CeExtEntityLEDTable <ydk.models.entity.CISCO_ENTITY_EXT_MIB.CISCOENTITYEXTMIB.CeExtEntityLEDTable>`
    
    .. attribute:: ceextphysicalprocessortable
    
    	The ceExtPhysicalProcessorTable extends the ENTITY\-MIB entPhysicalTable for modules (Non FRUs(Field Replacable Units) or FRUs)
    	**type**\: :py:class:`CeExtPhysicalProcessorTable <ydk.models.entity.CISCO_ENTITY_EXT_MIB.CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable>`
    
    

    """

    _prefix = 'cisco-entity'
    _revision = '2008-11-24'

    def __init__(self):
        self.ceextconfigregtable = CISCOENTITYEXTMIB.CeExtConfigRegTable()
        self.ceextconfigregtable.parent = self
        self.ceextentityledtable = CISCOENTITYEXTMIB.CeExtEntityLEDTable()
        self.ceextentityledtable.parent = self
        self.ceextphysicalprocessortable = CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable()
        self.ceextphysicalprocessortable.parent = self


    class CeExtConfigRegTable(object):
        """
        The ceExtConfigRegTable extends
        the ENTITY\-MIB entPhysicalTable.
        
        .. attribute:: ceextconfigregentry
        
        	A ceExtConfigRegTable entry extends a corresponding entPhysicalTable entry of class module which has a configuration register.  Entries are created by the agent at the system power\-up or module insertion.  Entries are removed when the module is reset or  removed
        	**type**\: list of :py:class:`CeExtConfigRegEntry <ydk.models.entity.CISCO_ENTITY_EXT_MIB.CISCOENTITYEXTMIB.CeExtConfigRegTable.CeExtConfigRegEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2008-11-24'

        def __init__(self):
            self.parent = None
            self.ceextconfigregentry = YList()
            self.ceextconfigregentry.parent = self
            self.ceextconfigregentry.name = 'ceextconfigregentry'


        class CeExtConfigRegEntry(object):
            """
            A ceExtConfigRegTable entry extends
            a corresponding entPhysicalTable entry of class
            module which has a configuration register.
            
            Entries are created by the agent at the system power\-up
            or module insertion.
            
            Entries are removed when the module is reset or 
            removed.
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ceextconfigregister
            
            	The value of configuration register with which the processor module booted
            	**type**\: str
            
            .. attribute:: ceextconfigregnext
            
            	The value of configuration register in the processor module at next reboot. Just after  the reboot this has the same value as  ceExtConfigRegister
            	**type**\: str
            
            .. attribute:: ceextkickstartimagelist
            
            	The list of system kickstart images which can be used for booting
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ceextsysbootimagelist
            
            	The list of system boot images which can be used for booting
            	**type**\: str
            
            	**range:** 0..255
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2008-11-24'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.ceextconfigregister = None
                self.ceextconfigregnext = None
                self.ceextkickstartimagelist = None
                self.ceextsysbootimagelist = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/CISCO-ENTITY-EXT-MIB:ceExtConfigRegTable/CISCO-ENTITY-EXT-MIB:ceExtConfigRegEntry[CISCO-ENTITY-EXT-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.entphysicalindex is not None:
                    return True

                if self.ceextconfigregister is not None:
                    return True

                if self.ceextconfigregnext is not None:
                    return True

                if self.ceextkickstartimagelist is not None:
                    return True

                if self.ceextsysbootimagelist is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_EXT_MIB as meta
                return meta._meta_table['CISCOENTITYEXTMIB.CeExtConfigRegTable.CeExtConfigRegEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/CISCO-ENTITY-EXT-MIB:ceExtConfigRegTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ceextconfigregentry is not None:
                for child_ref in self.ceextconfigregentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_EXT_MIB as meta
            return meta._meta_table['CISCOENTITYEXTMIB.CeExtConfigRegTable']['meta_info']


    class CeExtEntityLEDTable(object):
        """
        A table containing information of LED on an entity.
        
        .. attribute:: ceextentityledentry
        
        	An entry (conceptual row) in the ceExtEntityLEDTable, containing information about an LED on an entity, identified by  entPhysicalIndex
        	**type**\: list of :py:class:`CeExtEntityLEDEntry <ydk.models.entity.CISCO_ENTITY_EXT_MIB.CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2008-11-24'

        def __init__(self):
            self.parent = None
            self.ceextentityledentry = YList()
            self.ceextentityledentry.parent = self
            self.ceextentityledentry.name = 'ceextentityledentry'


        class CeExtEntityLEDEntry(object):
            """
            An entry (conceptual row) in the ceExtEntityLEDTable,
            containing information about an LED on an entity, identified by 
            entPhysicalIndex.
            
            .. attribute:: ceextentityledtype
            
            	The type of LED on this entity. 'status' \- indicates the entity status. 'system' \- indicates the overall system status.  'active' \- the redundancy status of a module, for e.g.            supervisor module.  'power'  \- indicates sufficient power availability for all             modules. 'battery'\- indicates the battery status
            	**type**\: :py:class:`CeExtEntityLEDType_Enum <ydk.models.entity.CISCO_ENTITY_EXT_MIB.CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry.CeExtEntityLEDType_Enum>`
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ceextentityledcolor
            
            	The color of the LED
            	**type**\: :py:class:`CeExtEntityLEDColor_Enum <ydk.models.entity.CISCO_ENTITY_EXT_MIB.CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry.CeExtEntityLEDColor_Enum>`
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2008-11-24'

            def __init__(self):
                self.parent = None
                self.ceextentityledtype = None
                self.entphysicalindex = None
                self.ceextentityledcolor = None

            class CeExtEntityLEDColor_Enum(Enum):
                """
                CeExtEntityLEDColor_Enum

                The color of the LED.

                """

                OFF = 1

                GREEN = 2

                AMBER = 3

                RED = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.entity._meta import _CISCO_ENTITY_EXT_MIB as meta
                    return meta._meta_table['CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry.CeExtEntityLEDColor_Enum']


            class CeExtEntityLEDType_Enum(Enum):
                """
                CeExtEntityLEDType_Enum

                The type of LED on this entity.
                'status' \- indicates the entity status.
                'system' \- indicates the overall system status. 
                'active' \- the redundancy status of a module, for e.g.
                           supervisor module. 
                'power'  \- indicates sufficient power availability for all 
                           modules.
                'battery'\- indicates the battery status.

                """

                STATUS = 1

                SYSTEM = 2

                ACTIVE = 3

                POWER = 4

                BATTERY = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.entity._meta import _CISCO_ENTITY_EXT_MIB as meta
                    return meta._meta_table['CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry.CeExtEntityLEDType_Enum']


            @property
            def _common_path(self):
                if self.ceextentityledtype is None:
                    raise YPYDataValidationError('Key property ceextentityledtype is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/CISCO-ENTITY-EXT-MIB:ceExtEntityLEDTable/CISCO-ENTITY-EXT-MIB:ceExtEntityLEDEntry[CISCO-ENTITY-EXT-MIB:ceExtEntityLEDType = ' + str(self.ceextentityledtype) + '][CISCO-ENTITY-EXT-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ceextentityledtype is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.ceextentityledcolor is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_EXT_MIB as meta
                return meta._meta_table['CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/CISCO-ENTITY-EXT-MIB:ceExtEntityLEDTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ceextentityledentry is not None:
                for child_ref in self.ceextentityledentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_EXT_MIB as meta
            return meta._meta_table['CISCOENTITYEXTMIB.CeExtEntityLEDTable']['meta_info']


    class CeExtPhysicalProcessorTable(object):
        """
        The ceExtPhysicalProcessorTable extends
        the ENTITY\-MIB entPhysicalTable for modules
        (Non FRUs(Field Replacable Units) or FRUs).
        
        .. attribute:: ceextphysicalprocessorentry
        
        	A ceExtPhysicalProcessorTable entry extends a corresponding entPhysicalTable entry of class module(entPhysicalClass = 'module').  A processor module or line card which  has a processor will have an entry in this table.  A processor module or line card having multiple processors and is a SMP(Symmetric multi processor) system will have only  one entry corresponding to all the processors  since the resources defined below are shared.  A processor module or line card having multiple processors and is not an SMP system would register the processors as separate entities.  Entries are created by the agent at the system power\-up or module insertion.  Entries are removed when the module is reset or removed
        	**type**\: list of :py:class:`CeExtPhysicalProcessorEntry <ydk.models.entity.CISCO_ENTITY_EXT_MIB.CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable.CeExtPhysicalProcessorEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2008-11-24'

        def __init__(self):
            self.parent = None
            self.ceextphysicalprocessorentry = YList()
            self.ceextphysicalprocessorentry.parent = self
            self.ceextphysicalprocessorentry.name = 'ceextphysicalprocessorentry'


        class CeExtPhysicalProcessorEntry(object):
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
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ceexthcprocessorram
            
            	This object represents the total number of bytes of RAM available on the Processor. This object is a 64\-bit version of ceExtProcessorRam
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceextnvramsize
            
            	Total number of bytes of NVRAM in the entity.  A value of 0 for this object means the entity does not support NVRAM or NVRAM information  is not available
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceextnvramused
            
            	Number of bytes of NVRAM in use. This object is irrelevant if ceExtNVRAMSize is 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceextprocessorram
            
            	Total number of bytes of RAM available on the Processor
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceextprocessorramoverflow
            
            	This object represents the upper 32\-bit of ceExtProcessorRam. This object needs to be supported only if the available RAM bytes exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2008-11-24'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.ceexthcprocessorram = None
                self.ceextnvramsize = None
                self.ceextnvramused = None
                self.ceextprocessorram = None
                self.ceextprocessorramoverflow = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/CISCO-ENTITY-EXT-MIB:ceExtPhysicalProcessorTable/CISCO-ENTITY-EXT-MIB:ceExtPhysicalProcessorEntry[CISCO-ENTITY-EXT-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.entphysicalindex is not None:
                    return True

                if self.ceexthcprocessorram is not None:
                    return True

                if self.ceextnvramsize is not None:
                    return True

                if self.ceextnvramused is not None:
                    return True

                if self.ceextprocessorram is not None:
                    return True

                if self.ceextprocessorramoverflow is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_EXT_MIB as meta
                return meta._meta_table['CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable.CeExtPhysicalProcessorEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB/CISCO-ENTITY-EXT-MIB:ceExtPhysicalProcessorTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ceextphysicalprocessorentry is not None:
                for child_ref in self.ceextphysicalprocessorentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_EXT_MIB as meta
            return meta._meta_table['CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-ENTITY-EXT-MIB:CISCO-ENTITY-EXT-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ceextconfigregtable is not None and self.ceextconfigregtable._has_data():
            return True

        if self.ceextconfigregtable is not None and self.ceextconfigregtable.is_presence():
            return True

        if self.ceextentityledtable is not None and self.ceextentityledtable._has_data():
            return True

        if self.ceextentityledtable is not None and self.ceextentityledtable.is_presence():
            return True

        if self.ceextphysicalprocessortable is not None and self.ceextphysicalprocessortable._has_data():
            return True

        if self.ceextphysicalprocessortable is not None and self.ceextphysicalprocessortable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_EXT_MIB as meta
        return meta._meta_table['CISCOENTITYEXTMIB']['meta_info']


