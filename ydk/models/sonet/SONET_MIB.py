""" SONET_MIB 

The MIB module to describe SONET/SDH interface objects.

Copyright (C) The Internet Society (2003).  This version
of this MIB module is part of RFC 3592;  see the RFC
itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class SONETMIB(object):
    """
    
    
    .. attribute:: sonetfarendlinecurrenttable
    
    	The SONET/SDH Far End Line Current table
    	**type**\: :py:class:`SonetFarEndLineCurrentTable <ydk.models.sonet.SONET_MIB.SONETMIB.SonetFarEndLineCurrentTable>`
    
    .. attribute:: sonetfarendlineintervaltable
    
    	The SONET/SDH Far End Line Interval table
    	**type**\: :py:class:`SonetFarEndLineIntervalTable <ydk.models.sonet.SONET_MIB.SONETMIB.SonetFarEndLineIntervalTable>`
    
    .. attribute:: sonetfarendpathcurrenttable
    
    	The SONET/SDH Far End Path Current table
    	**type**\: :py:class:`SonetFarEndPathCurrentTable <ydk.models.sonet.SONET_MIB.SONETMIB.SonetFarEndPathCurrentTable>`
    
    .. attribute:: sonetfarendpathintervaltable
    
    	The SONET/SDH Far End Path Interval table
    	**type**\: :py:class:`SonetFarEndPathIntervalTable <ydk.models.sonet.SONET_MIB.SONETMIB.SonetFarEndPathIntervalTable>`
    
    .. attribute:: sonetfarendvtcurrenttable
    
    	The SONET/SDH Far End VT Current table
    	**type**\: :py:class:`SonetFarEndVTCurrentTable <ydk.models.sonet.SONET_MIB.SONETMIB.SonetFarEndVTCurrentTable>`
    
    .. attribute:: sonetfarendvtintervaltable
    
    	The SONET/SDH Far End VT Interval table
    	**type**\: :py:class:`SonetFarEndVTIntervalTable <ydk.models.sonet.SONET_MIB.SONETMIB.SonetFarEndVTIntervalTable>`
    
    .. attribute:: sonetlinecurrenttable
    
    	The SONET/SDH Line Current table
    	**type**\: :py:class:`SonetLineCurrentTable <ydk.models.sonet.SONET_MIB.SONETMIB.SonetLineCurrentTable>`
    
    .. attribute:: sonetlineintervaltable
    
    	The SONET/SDH Line Interval table
    	**type**\: :py:class:`SonetLineIntervalTable <ydk.models.sonet.SONET_MIB.SONETMIB.SonetLineIntervalTable>`
    
    .. attribute:: sonetmedium
    
    	
    	**type**\: :py:class:`SonetMedium <ydk.models.sonet.SONET_MIB.SONETMIB.SonetMedium>`
    
    .. attribute:: sonetmediumtable
    
    	The SONET/SDH Medium table
    	**type**\: :py:class:`SonetMediumTable <ydk.models.sonet.SONET_MIB.SONETMIB.SonetMediumTable>`
    
    .. attribute:: sonetpathcurrenttable
    
    	The SONET/SDH Path Current table
    	**type**\: :py:class:`SonetPathCurrentTable <ydk.models.sonet.SONET_MIB.SONETMIB.SonetPathCurrentTable>`
    
    .. attribute:: sonetpathintervaltable
    
    	The SONET/SDH Path Interval table
    	**type**\: :py:class:`SonetPathIntervalTable <ydk.models.sonet.SONET_MIB.SONETMIB.SonetPathIntervalTable>`
    
    .. attribute:: sonetsectioncurrenttable
    
    	The SONET/SDH Section Current table
    	**type**\: :py:class:`SonetSectionCurrentTable <ydk.models.sonet.SONET_MIB.SONETMIB.SonetSectionCurrentTable>`
    
    .. attribute:: sonetsectionintervaltable
    
    	The SONET/SDH Section Interval table
    	**type**\: :py:class:`SonetSectionIntervalTable <ydk.models.sonet.SONET_MIB.SONETMIB.SonetSectionIntervalTable>`
    
    .. attribute:: sonetvtcurrenttable
    
    	The SONET/SDH VT Current table
    	**type**\: :py:class:`SonetVTCurrentTable <ydk.models.sonet.SONET_MIB.SONETMIB.SonetVTCurrentTable>`
    
    .. attribute:: sonetvtintervaltable
    
    	The SONET/SDH VT Interval table
    	**type**\: :py:class:`SonetVTIntervalTable <ydk.models.sonet.SONET_MIB.SONETMIB.SonetVTIntervalTable>`
    
    

    """

    _prefix = 'sonet-mib'
    _revision = '2003-08-11'

    def __init__(self):
        self.sonetfarendlinecurrenttable = SONETMIB.SonetFarEndLineCurrentTable()
        self.sonetfarendlinecurrenttable.parent = self
        self.sonetfarendlineintervaltable = SONETMIB.SonetFarEndLineIntervalTable()
        self.sonetfarendlineintervaltable.parent = self
        self.sonetfarendpathcurrenttable = SONETMIB.SonetFarEndPathCurrentTable()
        self.sonetfarendpathcurrenttable.parent = self
        self.sonetfarendpathintervaltable = SONETMIB.SonetFarEndPathIntervalTable()
        self.sonetfarendpathintervaltable.parent = self
        self.sonetfarendvtcurrenttable = SONETMIB.SonetFarEndVTCurrentTable()
        self.sonetfarendvtcurrenttable.parent = self
        self.sonetfarendvtintervaltable = SONETMIB.SonetFarEndVTIntervalTable()
        self.sonetfarendvtintervaltable.parent = self
        self.sonetlinecurrenttable = SONETMIB.SonetLineCurrentTable()
        self.sonetlinecurrenttable.parent = self
        self.sonetlineintervaltable = SONETMIB.SonetLineIntervalTable()
        self.sonetlineintervaltable.parent = self
        self.sonetmedium = SONETMIB.SonetMedium()
        self.sonetmedium.parent = self
        self.sonetmediumtable = SONETMIB.SonetMediumTable()
        self.sonetmediumtable.parent = self
        self.sonetpathcurrenttable = SONETMIB.SonetPathCurrentTable()
        self.sonetpathcurrenttable.parent = self
        self.sonetpathintervaltable = SONETMIB.SonetPathIntervalTable()
        self.sonetpathintervaltable.parent = self
        self.sonetsectioncurrenttable = SONETMIB.SonetSectionCurrentTable()
        self.sonetsectioncurrenttable.parent = self
        self.sonetsectionintervaltable = SONETMIB.SonetSectionIntervalTable()
        self.sonetsectionintervaltable.parent = self
        self.sonetvtcurrenttable = SONETMIB.SonetVTCurrentTable()
        self.sonetvtcurrenttable.parent = self
        self.sonetvtintervaltable = SONETMIB.SonetVTIntervalTable()
        self.sonetvtintervaltable.parent = self


    class SonetFarEndLineCurrentTable(object):
        """
        The SONET/SDH Far End Line Current table.
        
        .. attribute:: sonetfarendlinecurrententry
        
        	An entry in the SONET/SDH Far End Line Current table
        	**type**\: list of :py:class:`SonetFarEndLineCurrentEntry <ydk.models.sonet.SONET_MIB.SONETMIB.SonetFarEndLineCurrentTable.SonetFarEndLineCurrentEntry>`
        
        

        """

        _prefix = 'sonet-mib'
        _revision = '2003-08-11'

        def __init__(self):
            self.parent = None
            self.sonetfarendlinecurrententry = YList()
            self.sonetfarendlinecurrententry.parent = self
            self.sonetfarendlinecurrententry.name = 'sonetfarendlinecurrententry'


        class SonetFarEndLineCurrentEntry(object):
            """
            An entry in the SONET/SDH Far End Line Current table.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: sonetfarendlinecurrentcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH Medium/Section/Line interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlinecurrentess
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlinecurrentsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH Medium/Section/Line interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlinecurrentuass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH Medium/Section/Line interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'sonet-mib'
            _revision = '2003-08-11'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.sonetfarendlinecurrentcvs = None
                self.sonetfarendlinecurrentess = None
                self.sonetfarendlinecurrentsess = None
                self.sonetfarendlinecurrentuass = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetFarEndLineCurrentTable/SONET-MIB:sonetFarEndLineCurrentEntry[SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.sonetfarendlinecurrentcvs is not None:
                    return True

                if self.sonetfarendlinecurrentess is not None:
                    return True

                if self.sonetfarendlinecurrentsess is not None:
                    return True

                if self.sonetfarendlinecurrentuass is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _SONET_MIB as meta
                return meta._meta_table['SONETMIB.SonetFarEndLineCurrentTable.SonetFarEndLineCurrentEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetFarEndLineCurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sonetfarendlinecurrententry is not None:
                for child_ref in self.sonetfarendlinecurrententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _SONET_MIB as meta
            return meta._meta_table['SONETMIB.SonetFarEndLineCurrentTable']['meta_info']


    class SonetFarEndLineIntervalTable(object):
        """
        The SONET/SDH Far End Line Interval table.
        
        .. attribute:: sonetfarendlineintervalentry
        
        	An entry in the SONET/SDH Far End Line Interval table
        	**type**\: list of :py:class:`SonetFarEndLineIntervalEntry <ydk.models.sonet.SONET_MIB.SONETMIB.SonetFarEndLineIntervalTable.SonetFarEndLineIntervalEntry>`
        
        

        """

        _prefix = 'sonet-mib'
        _revision = '2003-08-11'

        def __init__(self):
            self.parent = None
            self.sonetfarendlineintervalentry = YList()
            self.sonetfarendlineintervalentry.parent = self
            self.sonetfarendlineintervalentry.name = 'sonetfarendlineintervalentry'


        class SonetFarEndLineIntervalEntry(object):
            """
            An entry in the SONET/SDH Far
            End Line Interval table.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: sonetfarendlineintervalnumber
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: sonetfarendlineintervalcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH Line interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlineintervaless
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH Line interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlineintervalsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH Line interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlineintervaluass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH Line interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendlineintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            

            """

            _prefix = 'sonet-mib'
            _revision = '2003-08-11'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.sonetfarendlineintervalnumber = None
                self.sonetfarendlineintervalcvs = None
                self.sonetfarendlineintervaless = None
                self.sonetfarendlineintervalsess = None
                self.sonetfarendlineintervaluass = None
                self.sonetfarendlineintervalvaliddata = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')
                if self.sonetfarendlineintervalnumber is None:
                    raise YPYDataValidationError('Key property sonetfarendlineintervalnumber is None')

                return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetFarEndLineIntervalTable/SONET-MIB:sonetFarEndLineIntervalEntry[SONET-MIB:ifIndex = ' + str(self.ifindex) + '][SONET-MIB:sonetFarEndLineIntervalNumber = ' + str(self.sonetfarendlineintervalnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.sonetfarendlineintervalnumber is not None:
                    return True

                if self.sonetfarendlineintervalcvs is not None:
                    return True

                if self.sonetfarendlineintervaless is not None:
                    return True

                if self.sonetfarendlineintervalsess is not None:
                    return True

                if self.sonetfarendlineintervaluass is not None:
                    return True

                if self.sonetfarendlineintervalvaliddata is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _SONET_MIB as meta
                return meta._meta_table['SONETMIB.SonetFarEndLineIntervalTable.SonetFarEndLineIntervalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetFarEndLineIntervalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sonetfarendlineintervalentry is not None:
                for child_ref in self.sonetfarendlineintervalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _SONET_MIB as meta
            return meta._meta_table['SONETMIB.SonetFarEndLineIntervalTable']['meta_info']


    class SonetFarEndPathCurrentTable(object):
        """
        The SONET/SDH Far End Path Current table.
        
        .. attribute:: sonetfarendpathcurrententry
        
        	An entry in the SONET/SDH Far End Path Current table
        	**type**\: list of :py:class:`SonetFarEndPathCurrentEntry <ydk.models.sonet.SONET_MIB.SONETMIB.SonetFarEndPathCurrentTable.SonetFarEndPathCurrentEntry>`
        
        

        """

        _prefix = 'sonet-mib'
        _revision = '2003-08-11'

        def __init__(self):
            self.parent = None
            self.sonetfarendpathcurrententry = YList()
            self.sonetfarendpathcurrententry.parent = self
            self.sonetfarendpathcurrententry.name = 'sonetfarendpathcurrententry'


        class SonetFarEndPathCurrentEntry(object):
            """
            An entry in the SONET/SDH Far End Path Current table.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: sonetfarendpathcurrentcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH Path interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathcurrentess
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathcurrentsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH Path interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathcurrentuass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH Path interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'sonet-mib'
            _revision = '2003-08-11'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.sonetfarendpathcurrentcvs = None
                self.sonetfarendpathcurrentess = None
                self.sonetfarendpathcurrentsess = None
                self.sonetfarendpathcurrentuass = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetFarEndPathCurrentTable/SONET-MIB:sonetFarEndPathCurrentEntry[SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.sonetfarendpathcurrentcvs is not None:
                    return True

                if self.sonetfarendpathcurrentess is not None:
                    return True

                if self.sonetfarendpathcurrentsess is not None:
                    return True

                if self.sonetfarendpathcurrentuass is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _SONET_MIB as meta
                return meta._meta_table['SONETMIB.SonetFarEndPathCurrentTable.SonetFarEndPathCurrentEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetFarEndPathCurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sonetfarendpathcurrententry is not None:
                for child_ref in self.sonetfarendpathcurrententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _SONET_MIB as meta
            return meta._meta_table['SONETMIB.SonetFarEndPathCurrentTable']['meta_info']


    class SonetFarEndPathIntervalTable(object):
        """
        The SONET/SDH Far End Path Interval table.
        
        .. attribute:: sonetfarendpathintervalentry
        
        	An entry in the SONET/SDH Far End Path Interval table
        	**type**\: list of :py:class:`SonetFarEndPathIntervalEntry <ydk.models.sonet.SONET_MIB.SONETMIB.SonetFarEndPathIntervalTable.SonetFarEndPathIntervalEntry>`
        
        

        """

        _prefix = 'sonet-mib'
        _revision = '2003-08-11'

        def __init__(self):
            self.parent = None
            self.sonetfarendpathintervalentry = YList()
            self.sonetfarendpathintervalentry.parent = self
            self.sonetfarendpathintervalentry.name = 'sonetfarendpathintervalentry'


        class SonetFarEndPathIntervalEntry(object):
            """
            An entry in the SONET/SDH Far
            End Path Interval table.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: sonetfarendpathintervalnumber
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: sonetfarendpathintervalcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH Path interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathintervaless
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH Path interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathintervalsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH Path interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathintervaluass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH Path interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendpathintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            

            """

            _prefix = 'sonet-mib'
            _revision = '2003-08-11'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.sonetfarendpathintervalnumber = None
                self.sonetfarendpathintervalcvs = None
                self.sonetfarendpathintervaless = None
                self.sonetfarendpathintervalsess = None
                self.sonetfarendpathintervaluass = None
                self.sonetfarendpathintervalvaliddata = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')
                if self.sonetfarendpathintervalnumber is None:
                    raise YPYDataValidationError('Key property sonetfarendpathintervalnumber is None')

                return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetFarEndPathIntervalTable/SONET-MIB:sonetFarEndPathIntervalEntry[SONET-MIB:ifIndex = ' + str(self.ifindex) + '][SONET-MIB:sonetFarEndPathIntervalNumber = ' + str(self.sonetfarendpathintervalnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.sonetfarendpathintervalnumber is not None:
                    return True

                if self.sonetfarendpathintervalcvs is not None:
                    return True

                if self.sonetfarendpathintervaless is not None:
                    return True

                if self.sonetfarendpathintervalsess is not None:
                    return True

                if self.sonetfarendpathintervaluass is not None:
                    return True

                if self.sonetfarendpathintervalvaliddata is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _SONET_MIB as meta
                return meta._meta_table['SONETMIB.SonetFarEndPathIntervalTable.SonetFarEndPathIntervalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetFarEndPathIntervalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sonetfarendpathintervalentry is not None:
                for child_ref in self.sonetfarendpathintervalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _SONET_MIB as meta
            return meta._meta_table['SONETMIB.SonetFarEndPathIntervalTable']['meta_info']


    class SonetFarEndVTCurrentTable(object):
        """
        The SONET/SDH Far End VT Current table.
        
        .. attribute:: sonetfarendvtcurrententry
        
        	An entry in the SONET/SDH Far End VT Current table
        	**type**\: list of :py:class:`SonetFarEndVTCurrentEntry <ydk.models.sonet.SONET_MIB.SONETMIB.SonetFarEndVTCurrentTable.SonetFarEndVTCurrentEntry>`
        
        

        """

        _prefix = 'sonet-mib'
        _revision = '2003-08-11'

        def __init__(self):
            self.parent = None
            self.sonetfarendvtcurrententry = YList()
            self.sonetfarendvtcurrententry.parent = self
            self.sonetfarendvtcurrententry.name = 'sonetfarendvtcurrententry'


        class SonetFarEndVTCurrentEntry(object):
            """
            An entry in the SONET/SDH Far End VT Current table.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: sonetfarendvtcurrentcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH VT interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtcurrentess
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtcurrentsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH VT interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtcurrentuass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH VT interface in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'sonet-mib'
            _revision = '2003-08-11'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.sonetfarendvtcurrentcvs = None
                self.sonetfarendvtcurrentess = None
                self.sonetfarendvtcurrentsess = None
                self.sonetfarendvtcurrentuass = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetFarEndVTCurrentTable/SONET-MIB:sonetFarEndVTCurrentEntry[SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.sonetfarendvtcurrentcvs is not None:
                    return True

                if self.sonetfarendvtcurrentess is not None:
                    return True

                if self.sonetfarendvtcurrentsess is not None:
                    return True

                if self.sonetfarendvtcurrentuass is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _SONET_MIB as meta
                return meta._meta_table['SONETMIB.SonetFarEndVTCurrentTable.SonetFarEndVTCurrentEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetFarEndVTCurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sonetfarendvtcurrententry is not None:
                for child_ref in self.sonetfarendvtcurrententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _SONET_MIB as meta
            return meta._meta_table['SONETMIB.SonetFarEndVTCurrentTable']['meta_info']


    class SonetFarEndVTIntervalTable(object):
        """
        The SONET/SDH Far End VT Interval table.
        
        .. attribute:: sonetfarendvtintervalentry
        
        	An entry in the SONET/SDH Far End VT Interval table
        	**type**\: list of :py:class:`SonetFarEndVTIntervalEntry <ydk.models.sonet.SONET_MIB.SONETMIB.SonetFarEndVTIntervalTable.SonetFarEndVTIntervalEntry>`
        
        

        """

        _prefix = 'sonet-mib'
        _revision = '2003-08-11'

        def __init__(self):
            self.parent = None
            self.sonetfarendvtintervalentry = YList()
            self.sonetfarendvtintervalentry.parent = self
            self.sonetfarendvtintervalentry.name = 'sonetfarendvtintervalentry'


        class SonetFarEndVTIntervalEntry(object):
            """
            An entry in the SONET/SDH Far
            End VT Interval table.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: sonetfarendvtintervalnumber
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: sonetfarendvtintervalcvs
            
            	The counter associated with the number of Far End Coding Violations reported via the far end block error count encountered by a SONET/SDH VT interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtintervaless
            
            	The counter associated with the number of Far End Errored Seconds encountered by a SONET/SDH VT interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtintervalsess
            
            	The counter associated with the number of Far End Severely Errored Seconds encountered by a SONET/SDH VT interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtintervaluass
            
            	The counter associated with the number of Far End Unavailable Seconds encountered by a SONET/SDH VT interface in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetfarendvtintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            

            """

            _prefix = 'sonet-mib'
            _revision = '2003-08-11'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.sonetfarendvtintervalnumber = None
                self.sonetfarendvtintervalcvs = None
                self.sonetfarendvtintervaless = None
                self.sonetfarendvtintervalsess = None
                self.sonetfarendvtintervaluass = None
                self.sonetfarendvtintervalvaliddata = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')
                if self.sonetfarendvtintervalnumber is None:
                    raise YPYDataValidationError('Key property sonetfarendvtintervalnumber is None')

                return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetFarEndVTIntervalTable/SONET-MIB:sonetFarEndVTIntervalEntry[SONET-MIB:ifIndex = ' + str(self.ifindex) + '][SONET-MIB:sonetFarEndVTIntervalNumber = ' + str(self.sonetfarendvtintervalnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.sonetfarendvtintervalnumber is not None:
                    return True

                if self.sonetfarendvtintervalcvs is not None:
                    return True

                if self.sonetfarendvtintervaless is not None:
                    return True

                if self.sonetfarendvtintervalsess is not None:
                    return True

                if self.sonetfarendvtintervaluass is not None:
                    return True

                if self.sonetfarendvtintervalvaliddata is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _SONET_MIB as meta
                return meta._meta_table['SONETMIB.SonetFarEndVTIntervalTable.SonetFarEndVTIntervalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetFarEndVTIntervalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sonetfarendvtintervalentry is not None:
                for child_ref in self.sonetfarendvtintervalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _SONET_MIB as meta
            return meta._meta_table['SONETMIB.SonetFarEndVTIntervalTable']['meta_info']


    class SonetLineCurrentTable(object):
        """
        The SONET/SDH Line Current table.
        
        .. attribute:: sonetlinecurrententry
        
        	An entry in the SONET/SDH Line Current table
        	**type**\: list of :py:class:`SonetLineCurrentEntry <ydk.models.sonet.SONET_MIB.SONETMIB.SonetLineCurrentTable.SonetLineCurrentEntry>`
        
        

        """

        _prefix = 'sonet-mib'
        _revision = '2003-08-11'

        def __init__(self):
            self.parent = None
            self.sonetlinecurrententry = YList()
            self.sonetlinecurrententry.parent = self
            self.sonetlinecurrententry.name = 'sonetlinecurrententry'


        class SonetLineCurrentEntry(object):
            """
            An entry in the SONET/SDH Line Current table.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: sonetlinecurrentcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Line in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlinecurrentess
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Line in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlinecurrentsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Line in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlinecurrentstatus
            
            	This variable indicates the status of the interface. The sonetLineCurrentStatus is a bit map represented as a sum, therefore, it can represent multiple defects simultaneously. The sonetLineNoDefect should be set if and only if no other flag is set.  The various bit positions are\:  1   sonetLineNoDefect  2   sonetLineAIS  4   sonetLineRDI
            	**type**\: int
            
            	**range:** 1..6
            
            .. attribute:: sonetlinecurrentuass
            
            	The counter associated with the number of Unavailable Seconds encountered by a SONET/SDH Line in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'sonet-mib'
            _revision = '2003-08-11'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.sonetlinecurrentcvs = None
                self.sonetlinecurrentess = None
                self.sonetlinecurrentsess = None
                self.sonetlinecurrentstatus = None
                self.sonetlinecurrentuass = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetLineCurrentTable/SONET-MIB:sonetLineCurrentEntry[SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.sonetlinecurrentcvs is not None:
                    return True

                if self.sonetlinecurrentess is not None:
                    return True

                if self.sonetlinecurrentsess is not None:
                    return True

                if self.sonetlinecurrentstatus is not None:
                    return True

                if self.sonetlinecurrentuass is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _SONET_MIB as meta
                return meta._meta_table['SONETMIB.SonetLineCurrentTable.SonetLineCurrentEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetLineCurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sonetlinecurrententry is not None:
                for child_ref in self.sonetlinecurrententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _SONET_MIB as meta
            return meta._meta_table['SONETMIB.SonetLineCurrentTable']['meta_info']


    class SonetLineIntervalTable(object):
        """
        The SONET/SDH Line Interval table.
        
        .. attribute:: sonetlineintervalentry
        
        	An entry in the SONET/SDH Line Interval table
        	**type**\: list of :py:class:`SonetLineIntervalEntry <ydk.models.sonet.SONET_MIB.SONETMIB.SonetLineIntervalTable.SonetLineIntervalEntry>`
        
        

        """

        _prefix = 'sonet-mib'
        _revision = '2003-08-11'

        def __init__(self):
            self.parent = None
            self.sonetlineintervalentry = YList()
            self.sonetlineintervalentry.parent = self
            self.sonetlineintervalentry.name = 'sonetlineintervalentry'


        class SonetLineIntervalEntry(object):
            """
            An entry in the SONET/SDH Line Interval table.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: sonetlineintervalnumber
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: sonetlineintervalcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Line in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlineintervaless
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Line in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlineintervalsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Line in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlineintervaluass
            
            	The counter associated with the number of Unavailable Seconds encountered by a SONET/SDH Line in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetlineintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            

            """

            _prefix = 'sonet-mib'
            _revision = '2003-08-11'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.sonetlineintervalnumber = None
                self.sonetlineintervalcvs = None
                self.sonetlineintervaless = None
                self.sonetlineintervalsess = None
                self.sonetlineintervaluass = None
                self.sonetlineintervalvaliddata = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')
                if self.sonetlineintervalnumber is None:
                    raise YPYDataValidationError('Key property sonetlineintervalnumber is None')

                return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetLineIntervalTable/SONET-MIB:sonetLineIntervalEntry[SONET-MIB:ifIndex = ' + str(self.ifindex) + '][SONET-MIB:sonetLineIntervalNumber = ' + str(self.sonetlineintervalnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.sonetlineintervalnumber is not None:
                    return True

                if self.sonetlineintervalcvs is not None:
                    return True

                if self.sonetlineintervaless is not None:
                    return True

                if self.sonetlineintervalsess is not None:
                    return True

                if self.sonetlineintervaluass is not None:
                    return True

                if self.sonetlineintervalvaliddata is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _SONET_MIB as meta
                return meta._meta_table['SONETMIB.SonetLineIntervalTable.SonetLineIntervalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetLineIntervalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sonetlineintervalentry is not None:
                for child_ref in self.sonetlineintervalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _SONET_MIB as meta
            return meta._meta_table['SONETMIB.SonetLineIntervalTable']['meta_info']


    class SonetMedium(object):
        """
        
        
        .. attribute:: sonetsesthresholdset
        
        	An enumerated integer indicating which recognized set of SES thresholds that the agent uses for determining severely errored seconds and unavailable time.  other(1)   None of the following.  bellcore1991(2)   Bellcore TR\-NWT\-000253, 1991 [TR253], or   ANSI T1M1.3/93\-005R2, 1993 [T1M1.3].   See also Appendix B.  ansi1993(3)   ANSI T1.231, 1993 [T1.231a], or   Bellcore GR\-253\-CORE, Issue 2, 1995 [GR253]  itu1995(4)   ITU Recommendation G.826, 1995 [G.826]  ansi1997(5)   ANSI T1.231, 1997 [T1.231b]  If a manager changes the value of this object then the SES statistics collected prior to this change must be invalidated
        	**type**\: :py:class:`SonetSESthresholdSet_Enum <ydk.models.sonet.SONET_MIB.SONETMIB.SonetMedium.SonetSESthresholdSet_Enum>`
        
        

        """

        _prefix = 'sonet-mib'
        _revision = '2003-08-11'

        def __init__(self):
            self.parent = None
            self.sonetsesthresholdset = None

        class SonetSESthresholdSet_Enum(Enum):
            """
            SonetSESthresholdSet_Enum

            An enumerated integer indicating which
            recognized set of SES thresholds that
            the agent uses for determining severely
            errored seconds and unavailable time.
            
            other(1)
              None of the following.
            
            bellcore1991(2)
              Bellcore TR\-NWT\-000253, 1991 [TR253], or
              ANSI T1M1.3/93\-005R2, 1993 [T1M1.3].
              See also Appendix B.
            
            ansi1993(3)
              ANSI T1.231, 1993 [T1.231a], or
              Bellcore GR\-253\-CORE, Issue 2, 1995 [GR253]
            
            itu1995(4)
              ITU Recommendation G.826, 1995 [G.826]
            
            ansi1997(5)
              ANSI T1.231, 1997 [T1.231b]
            
            If a manager changes the value of this
            object then the SES statistics collected
            prior to this change must be invalidated.

            """

            OTHER = 1

            BELLCORE1991 = 2

            ANSI1993 = 3

            ITU1995 = 4

            ANSI1997 = 5


            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _SONET_MIB as meta
                return meta._meta_table['SONETMIB.SonetMedium.SonetSESthresholdSet_Enum']


        @property
        def _common_path(self):

            return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetMedium'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sonetsesthresholdset is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _SONET_MIB as meta
            return meta._meta_table['SONETMIB.SonetMedium']['meta_info']


    class SonetMediumTable(object):
        """
        The SONET/SDH Medium table.
        
        .. attribute:: sonetmediumentry
        
        	An entry in the SONET/SDH Medium table
        	**type**\: list of :py:class:`SonetMediumEntry <ydk.models.sonet.SONET_MIB.SONETMIB.SonetMediumTable.SonetMediumEntry>`
        
        

        """

        _prefix = 'sonet-mib'
        _revision = '2003-08-11'

        def __init__(self):
            self.parent = None
            self.sonetmediumentry = YList()
            self.sonetmediumentry.parent = self
            self.sonetmediumentry.name = 'sonetmediumentry'


        class SonetMediumEntry(object):
            """
            An entry in the SONET/SDH Medium table.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: sonetmediumcircuitidentifier
            
            	This variable contains the transmission vendor's circuit identifier, for the purpose of facilitating troubleshooting. Note that the circuit identifier, if available, is also represented by ifPhysAddress
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: sonetmediuminvalidintervals
            
            	The number of intervals in the range from 0 to sonetMediumValidIntervals for which no data is available. This object will typically be zero except in cases where the data for some intervals are not available (e.g., in proxy situations)
            	**type**\: int
            
            	**range:** 0..96
            
            .. attribute:: sonetmediumlinecoding
            
            	This variable describes the line coding for this interface. The B3ZS and CMI are used for electrical SONET/SDH signals (STS\-1 and STS\-3). The Non\-Return to Zero (NRZ) and the Return to Zero are used for optical SONET/SDH signals
            	**type**\: :py:class:`SonetMediumLineCoding_Enum <ydk.models.sonet.SONET_MIB.SONETMIB.SonetMediumTable.SonetMediumEntry.SonetMediumLineCoding_Enum>`
            
            .. attribute:: sonetmediumlinetype
            
            	This variable describes the line type for this interface. The line types are Short and Long Range Single Mode fiber or Multi\-Mode fiber interfaces, and coax and UTP for electrical interfaces.  The value sonetOther should be used when the Line Type is not one of the listed values
            	**type**\: :py:class:`SonetMediumLineType_Enum <ydk.models.sonet.SONET_MIB.SONETMIB.SonetMediumTable.SonetMediumEntry.SonetMediumLineType_Enum>`
            
            .. attribute:: sonetmediumloopbackconfig
            
            	The current loopback state of the SONET/SDH interface.  The values mean\:    sonetNoLoop      Not in the loopback state. A device that is not      capable of performing a loopback on this interface      shall always return this value.    sonetFacilityLoop      The received signal at this interface is looped back      out through the corresponding transmitter in the return      direction.    sonetTerminalLoop      The signal that is about to be transmitted is connected      to the associated incoming receiver.    sonetOtherLoop      Loopbacks that are not defined here
            	**type**\: :py:class:`SonetMediumLoopbackConfig_Bits <ydk.models.sonet.SONET_MIB.SONETMIB.SonetMediumTable.SonetMediumEntry.SonetMediumLoopbackConfig_Bits>`
            
            .. attribute:: sonetmediumtimeelapsed
            
            	The number of seconds, including partial seconds, that have elapsed since the beginning of the current measurement period. If, for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, the agent will return the maximum value
            	**type**\: int
            
            	**range:** 1..900
            
            .. attribute:: sonetmediumtype
            
            	This variable identifies whether a SONET or a SDH signal is used across this interface
            	**type**\: :py:class:`SonetMediumType_Enum <ydk.models.sonet.SONET_MIB.SONETMIB.SonetMediumTable.SonetMediumEntry.SonetMediumType_Enum>`
            
            .. attribute:: sonetmediumvalidintervals
            
            	The number of previous 15\-minute intervals for which data was collected. A SONET/SDH interface must be capable of supporting at least n intervals. The minimum value of n is 4. The default of n is 32. The maximum value of n is 96. The value will be <n> unless the measurement was (re\-)started within the last (<n>\*15) minutes, in which case the value will be the number of complete 15 minute intervals for which the agent has at least some data. In certain cases (e.g., in the case where the agent is a proxy) it is possible that some intervals are unavailable.  In this case, this interval is the maximum interval number for which data is available. 
            	**type**\: int
            
            	**range:** 0..96
            
            

            """

            _prefix = 'sonet-mib'
            _revision = '2003-08-11'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.sonetmediumcircuitidentifier = None
                self.sonetmediuminvalidintervals = None
                self.sonetmediumlinecoding = None
                self.sonetmediumlinetype = None
                self.sonetmediumloopbackconfig = SONETMIB.SonetMediumTable.SonetMediumEntry.SonetMediumLoopbackConfig_Bits()
                self.sonetmediumtimeelapsed = None
                self.sonetmediumtype = None
                self.sonetmediumvalidintervals = None

            class SonetMediumLineCoding_Enum(Enum):
                """
                SonetMediumLineCoding_Enum

                This variable describes the line coding for
                this interface. The B3ZS and CMI are used for
                electrical SONET/SDH signals (STS\-1 and STS\-3).
                The Non\-Return to Zero (NRZ) and the Return
                to Zero are used for optical SONET/SDH signals.

                """

                SONETMEDIUMOTHER = 1

                SONETMEDIUMB3ZS = 2

                SONETMEDIUMCMI = 3

                SONETMEDIUMNRZ = 4

                SONETMEDIUMRZ = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _SONET_MIB as meta
                    return meta._meta_table['SONETMIB.SonetMediumTable.SonetMediumEntry.SonetMediumLineCoding_Enum']


            class SonetMediumLineType_Enum(Enum):
                """
                SonetMediumLineType_Enum

                This variable describes the line type for
                this interface. The line types are
                Short and Long Range
                Single Mode fiber or Multi\-Mode fiber interfaces,
                and coax and UTP for electrical interfaces.  The
                value sonetOther should be used when the Line Type is
                not one of the listed values.

                """

                SONETOTHER = 1

                SONETSHORTSINGLEMODE = 2

                SONETLONGSINGLEMODE = 3

                SONETMULTIMODE = 4

                SONETCOAX = 5

                SONETUTP = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _SONET_MIB as meta
                    return meta._meta_table['SONETMIB.SonetMediumTable.SonetMediumEntry.SonetMediumLineType_Enum']


            class SonetMediumType_Enum(Enum):
                """
                SonetMediumType_Enum

                This variable identifies whether a SONET
                or a SDH signal is used across this interface.

                """

                SONET = 1

                SDH = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _SONET_MIB as meta
                    return meta._meta_table['SONETMIB.SonetMediumTable.SonetMediumEntry.SonetMediumType_Enum']


            class SonetMediumLoopbackConfig_Bits(FixedBitsDict):
                """
                SonetMediumLoopbackConfig_Bits

                The current loopback state of the SONET/SDH interface.  The
                values mean\:
                
                  sonetNoLoop
                     Not in the loopback state. A device that is not
                     capable of performing a loopback on this interface
                     shall always return this value.
                
                  sonetFacilityLoop
                     The received signal at this interface is looped back
                     out through the corresponding transmitter in the return
                     direction.
                
                  sonetTerminalLoop
                     The signal that is about to be transmitted is connected
                     to the associated incoming receiver.
                
                  sonetOtherLoop
                     Loopbacks that are not defined here.
                Keys are:- sonetFacilityLoop , sonetNoLoop , sonetTerminalLoop , sonetOtherLoop

                """

                def __init__(self):
                    self._dictionary = { 
                        'sonetFacilityLoop':False,
                        'sonetNoLoop':False,
                        'sonetTerminalLoop':False,
                        'sonetOtherLoop':False,
                    }
                    self._pos_map = { 
                        'sonetFacilityLoop':1,
                        'sonetNoLoop':0,
                        'sonetTerminalLoop':2,
                        'sonetOtherLoop':3,
                    }

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetMediumTable/SONET-MIB:sonetMediumEntry[SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.sonetmediumcircuitidentifier is not None:
                    return True

                if self.sonetmediuminvalidintervals is not None:
                    return True

                if self.sonetmediumlinecoding is not None:
                    return True

                if self.sonetmediumlinetype is not None:
                    return True

                if self.sonetmediumloopbackconfig is not None:
                    if self.sonetmediumloopbackconfig._has_data():
                        return True

                if self.sonetmediumtimeelapsed is not None:
                    return True

                if self.sonetmediumtype is not None:
                    return True

                if self.sonetmediumvalidintervals is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _SONET_MIB as meta
                return meta._meta_table['SONETMIB.SonetMediumTable.SonetMediumEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetMediumTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sonetmediumentry is not None:
                for child_ref in self.sonetmediumentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _SONET_MIB as meta
            return meta._meta_table['SONETMIB.SonetMediumTable']['meta_info']


    class SonetPathCurrentTable(object):
        """
        The SONET/SDH Path Current table.
        
        .. attribute:: sonetpathcurrententry
        
        	An entry in the SONET/SDH Path Current table
        	**type**\: list of :py:class:`SonetPathCurrentEntry <ydk.models.sonet.SONET_MIB.SONETMIB.SonetPathCurrentTable.SonetPathCurrentEntry>`
        
        

        """

        _prefix = 'sonet-mib'
        _revision = '2003-08-11'

        def __init__(self):
            self.parent = None
            self.sonetpathcurrententry = YList()
            self.sonetpathcurrententry.parent = self
            self.sonetpathcurrententry.name = 'sonetpathcurrententry'


        class SonetPathCurrentEntry(object):
            """
            An entry in the SONET/SDH Path Current table.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cspsignallingtransportmode
            
            	This object represents the mode used to transport DS0  Signalling information for T1 byteSynchronous mapping (GR253). In signallingTransferMode(2), the robbed\-bit signalling  is transferred to the VT header. In clearMode(3), only  the framing bit is transferred to the VT header.           The initial value is signallingTransferMode(2)  if csTributaryMappingType is byteSynchronous.  For asynchronous mapping, it is  notApplicable(1).  The value notApplicable(1) can not be set
            	**type**\: :py:class:`CspSignallingTransportMode_Enum <ydk.models.sonet.SONET_MIB.SONETMIB.SonetPathCurrentTable.SonetPathCurrentEntry.CspSignallingTransportMode_Enum>`
            
            .. attribute:: cspsonetpathpayload
            
            	Specifies the payload carried by the SONET/SDH Path. The payload specification corresponds to C2 (Signal Label) overhead byte in SONET/SDH Path Overhead\: unequipped(1)    \: Path is not provisioned to carry any payload. unspecified(2)   \: Path is carrying an unspecifed payload. ds3(3)           \: Path is carrying a DS3 path as payload. vt15vc11(4)      \: Path is carrying SONET\-VT1.5/SDH\-VC11 payload. vt2vc12(5)       \: Path is carrying SONET\-VT2/SDH\-VC12 as payload. atmCell(6)       \: Path is carrying ATM Cells as payload. hdlcFr(7)        \: Path is carrying Frame Relay (HDLC) payload. e3(8)            \: Path is carrying an E3 path as payload. vtStructured(9)  \: Path is carrying VTGs/TUG3s/TUG2s which may                    each carry a different payload.  A write operation on this object will result in update to C2 overhead byte in the Path Overhead
            	**type**\: :py:class:`CspSonetPathPayload_Enum <ydk.models.sonet.SONET_MIB.SONETMIB.SonetPathCurrentTable.SonetPathCurrentEntry.CspSonetPathPayload_Enum>`
            
            .. attribute:: csptributarygroupingtype
            
            	This object represents the method used to group VCs into an STM\-1 signal. Applicable only to SDH.  au3Grouping\: STM1<\-AU\-3<\-TUG\-2<\-TU\-12<\-VC12 or              STM1<\-AU\-3<\-TUG\-2<\-TU\-11<\-VC11.  au4Grouping\: STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-12<\-VC12 or              STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-11<\-VC11.  The initial value is au3Grouping(2) for SDH and  notApplicable(1) for SONET
            	**type**\: :py:class:`CspTributaryGroupingType_Enum <ydk.models.sonet.SONET_MIB.SONETMIB.SonetPathCurrentTable.SonetPathCurrentEntry.CspTributaryGroupingType_Enum>`
            
            .. attribute:: csptributarymappingtype
            
            	This object represents the VT/VC mapping type. asynchronous\: In this mode, the channel structure of                DS1/E1 is neither visible nor preserved.  byteSynchronous\: In this mode, the DS0 signals inside                   the VT/VC can be found and extracted                   from the frame. The initial value is asynchronous(1)
            	**type**\: :py:class:`CspTributaryMappingType_Enum <ydk.models.sonet.SONET_MIB.SONETMIB.SonetPathCurrentTable.SonetPathCurrentEntry.CspTributaryMappingType_Enum>`
            
            .. attribute:: sonetpathcurrentcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Path in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathcurrentess
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Path in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathcurrentsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Path in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathcurrentstatus
            
            	This variable indicates the status of the interface. The sonetPathCurrentStatus is a bit map represented as a sum, therefore, it can represent multiple defects simultaneously. The sonetPathNoDefect should be set if and only if no other flag is set.  The various bit positions are\:    1   sonetPathNoDefect    2   sonetPathSTSLOP    4   sonetPathSTSAIS    8   sonetPathSTSRDI   16   sonetPathUnequipped   32   sonetPathSignalLabelMismatch
            	**type**\: int
            
            	**range:** 1..62
            
            .. attribute:: sonetpathcurrentuass
            
            	The counter associated with the number of Unavailable Seconds encountered by a Path in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathcurrentwidth
            
            	A value that indicates the type of the SONET/SDH Path.  For SONET, the assigned types are the STS\-Nc SPEs, where N = 1, 3, 12, 24, 48, 192 and 768. STS\-1 is equal to 51.84 Mbps.  For SDH, the assigned types are the STM\-Nc VCs, where N = 1, 4, 16, 64 and 256
            	**type**\: :py:class:`SonetPathCurrentWidth_Enum <ydk.models.sonet.SONET_MIB.SONETMIB.SonetPathCurrentTable.SonetPathCurrentEntry.SonetPathCurrentWidth_Enum>`
            
            

            """

            _prefix = 'sonet-mib'
            _revision = '2003-08-11'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cspsignallingtransportmode = None
                self.cspsonetpathpayload = None
                self.csptributarygroupingtype = None
                self.csptributarymappingtype = None
                self.sonetpathcurrentcvs = None
                self.sonetpathcurrentess = None
                self.sonetpathcurrentsess = None
                self.sonetpathcurrentstatus = None
                self.sonetpathcurrentuass = None
                self.sonetpathcurrentwidth = None

            class CspSignallingTransportMode_Enum(Enum):
                """
                CspSignallingTransportMode_Enum

                This object represents the mode used to transport DS0 
                Signalling information for T1 byteSynchronous mapping
                (GR253).
                In signallingTransferMode(2), the robbed\-bit signalling 
                is transferred to the VT header. In clearMode(3), only 
                the framing bit is transferred to the VT header.
                         
                The initial value is signallingTransferMode(2) 
                if csTributaryMappingType is byteSynchronous. 
                For asynchronous mapping, it is 
                notApplicable(1).
                
                The value notApplicable(1) can not be set.

                """

                NOTAPPLICABLE = 1

                SIGNALLINGTRANSFERMODE = 2

                CLEARMODE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _SONET_MIB as meta
                    return meta._meta_table['SONETMIB.SonetPathCurrentTable.SonetPathCurrentEntry.CspSignallingTransportMode_Enum']


            class CspSonetPathPayload_Enum(Enum):
                """
                CspSonetPathPayload_Enum

                Specifies the payload carried by the SONET/SDH Path.
                The payload specification corresponds to C2 (Signal Label)
                overhead byte in SONET/SDH Path Overhead\:
                unequipped(1)    \: Path is not provisioned to carry any payload.
                unspecified(2)   \: Path is carrying an unspecifed payload.
                ds3(3)           \: Path is carrying a DS3 path as payload.
                vt15vc11(4)      \: Path is carrying SONET\-VT1.5/SDH\-VC11 payload.
                vt2vc12(5)       \: Path is carrying SONET\-VT2/SDH\-VC12 as payload.
                atmCell(6)       \: Path is carrying ATM Cells as payload.
                hdlcFr(7)        \: Path is carrying Frame Relay (HDLC) payload.
                e3(8)            \: Path is carrying an E3 path as payload.
                vtStructured(9)  \: Path is carrying VTGs/TUG3s/TUG2s which may
                                   each carry a different payload. 
                A write operation on this object will result in update to
                C2 overhead byte in the Path Overhead.

                """

                UNEQUIPPED = 1

                UNSPECIFIED = 2

                DS3 = 3

                VT15VC11 = 4

                VT2VC12 = 5

                ATMCELL = 6

                HDLCFR = 7

                E3 = 8

                VTSTRUCTURED = 9


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _SONET_MIB as meta
                    return meta._meta_table['SONETMIB.SonetPathCurrentTable.SonetPathCurrentEntry.CspSonetPathPayload_Enum']


            class CspTributaryGroupingType_Enum(Enum):
                """
                CspTributaryGroupingType_Enum

                This object represents the method used to group VCs into
                an STM\-1 signal. Applicable only to SDH.
                
                au3Grouping\: STM1<\-AU\-3<\-TUG\-2<\-TU\-12<\-VC12 or
                             STM1<\-AU\-3<\-TUG\-2<\-TU\-11<\-VC11.
                
                au4Grouping\: STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-12<\-VC12 or
                             STM1<\-AU\-4<\-TUG\-3<\-TUG\-2<\-TU\-11<\-VC11.
                
                The initial value is au3Grouping(2) for SDH and 
                notApplicable(1) for SONET.

                """

                NOTAPPLICABLE = 1

                AU3GROUPING = 2

                AU4GROUPING = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _SONET_MIB as meta
                    return meta._meta_table['SONETMIB.SonetPathCurrentTable.SonetPathCurrentEntry.CspTributaryGroupingType_Enum']


            class CspTributaryMappingType_Enum(Enum):
                """
                CspTributaryMappingType_Enum

                This object represents the VT/VC mapping type.
                asynchronous\: In this mode, the channel structure of 
                              DS1/E1 is neither visible nor preserved.
                
                byteSynchronous\: In this mode, the DS0 signals inside 
                                 the VT/VC can be found and extracted 
                                 from the frame.
                The initial value is asynchronous(1).

                """

                ASYNCHRONOUS = 1

                BYTESYNCHRONOUS = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _SONET_MIB as meta
                    return meta._meta_table['SONETMIB.SonetPathCurrentTable.SonetPathCurrentEntry.CspTributaryMappingType_Enum']


            class SonetPathCurrentWidth_Enum(Enum):
                """
                SonetPathCurrentWidth_Enum

                A value that indicates the type of the SONET/SDH
                Path.  For SONET, the assigned types are
                the STS\-Nc SPEs, where N = 1, 3, 12, 24, 48, 192 and 768.
                STS\-1 is equal to 51.84 Mbps.  For SDH, the assigned
                types are the STM\-Nc VCs, where N = 1, 4, 16, 64 and 256.

                """

                STS1 = 1

                STS3CSTM1 = 2

                STS12CSTM4 = 3

                STS24C = 4

                STS48CSTM16 = 5

                STS192CSTM64 = 6

                STS768CSTM256 = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _SONET_MIB as meta
                    return meta._meta_table['SONETMIB.SonetPathCurrentTable.SonetPathCurrentEntry.SonetPathCurrentWidth_Enum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetPathCurrentTable/SONET-MIB:sonetPathCurrentEntry[SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.cspsignallingtransportmode is not None:
                    return True

                if self.cspsonetpathpayload is not None:
                    return True

                if self.csptributarygroupingtype is not None:
                    return True

                if self.csptributarymappingtype is not None:
                    return True

                if self.sonetpathcurrentcvs is not None:
                    return True

                if self.sonetpathcurrentess is not None:
                    return True

                if self.sonetpathcurrentsess is not None:
                    return True

                if self.sonetpathcurrentstatus is not None:
                    return True

                if self.sonetpathcurrentuass is not None:
                    return True

                if self.sonetpathcurrentwidth is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _SONET_MIB as meta
                return meta._meta_table['SONETMIB.SonetPathCurrentTable.SonetPathCurrentEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetPathCurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sonetpathcurrententry is not None:
                for child_ref in self.sonetpathcurrententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _SONET_MIB as meta
            return meta._meta_table['SONETMIB.SonetPathCurrentTable']['meta_info']


    class SonetPathIntervalTable(object):
        """
        The SONET/SDH Path Interval table.
        
        .. attribute:: sonetpathintervalentry
        
        	An entry in the SONET/SDH Path Interval table
        	**type**\: list of :py:class:`SonetPathIntervalEntry <ydk.models.sonet.SONET_MIB.SONETMIB.SonetPathIntervalTable.SonetPathIntervalEntry>`
        
        

        """

        _prefix = 'sonet-mib'
        _revision = '2003-08-11'

        def __init__(self):
            self.parent = None
            self.sonetpathintervalentry = YList()
            self.sonetpathintervalentry.parent = self
            self.sonetpathintervalentry.name = 'sonetpathintervalentry'


        class SonetPathIntervalEntry(object):
            """
            An entry in the SONET/SDH Path Interval table.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: sonetpathintervalnumber
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: sonetpathintervalcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Path in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathintervaless
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Path in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathintervalsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Path in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathintervaluass
            
            	The counter associated with the number of Unavailable Seconds encountered by a Path in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetpathintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            

            """

            _prefix = 'sonet-mib'
            _revision = '2003-08-11'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.sonetpathintervalnumber = None
                self.sonetpathintervalcvs = None
                self.sonetpathintervaless = None
                self.sonetpathintervalsess = None
                self.sonetpathintervaluass = None
                self.sonetpathintervalvaliddata = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')
                if self.sonetpathintervalnumber is None:
                    raise YPYDataValidationError('Key property sonetpathintervalnumber is None')

                return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetPathIntervalTable/SONET-MIB:sonetPathIntervalEntry[SONET-MIB:ifIndex = ' + str(self.ifindex) + '][SONET-MIB:sonetPathIntervalNumber = ' + str(self.sonetpathintervalnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.sonetpathintervalnumber is not None:
                    return True

                if self.sonetpathintervalcvs is not None:
                    return True

                if self.sonetpathintervaless is not None:
                    return True

                if self.sonetpathintervalsess is not None:
                    return True

                if self.sonetpathintervaluass is not None:
                    return True

                if self.sonetpathintervalvaliddata is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _SONET_MIB as meta
                return meta._meta_table['SONETMIB.SonetPathIntervalTable.SonetPathIntervalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetPathIntervalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sonetpathintervalentry is not None:
                for child_ref in self.sonetpathintervalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _SONET_MIB as meta
            return meta._meta_table['SONETMIB.SonetPathIntervalTable']['meta_info']


    class SonetSectionCurrentTable(object):
        """
        The SONET/SDH Section Current table.
        
        .. attribute:: sonetsectioncurrententry
        
        	An entry in the SONET/SDH Section Current table
        	**type**\: list of :py:class:`SonetSectionCurrentEntry <ydk.models.sonet.SONET_MIB.SONETMIB.SonetSectionCurrentTable.SonetSectionCurrentEntry>`
        
        

        """

        _prefix = 'sonet-mib'
        _revision = '2003-08-11'

        def __init__(self):
            self.parent = None
            self.sonetsectioncurrententry = YList()
            self.sonetsectioncurrententry.parent = self
            self.sonetsectioncurrententry.name = 'sonetsectioncurrententry'


        class SonetSectionCurrentEntry(object):
            """
            An entry in the SONET/SDH Section Current table.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: sonetsectioncurrentcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Section in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectioncurrentess
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Section in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectioncurrentsefss
            
            	The counter associated with the number of Severely Errored Framing Seconds encountered by a SONET/SDH Section in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectioncurrentsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Section in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectioncurrentstatus
            
            	This variable indicates the status of the interface. The sonetSectionCurrentStatus is a bit map represented as a sum, therefore, it can represent multiple defects simultaneously. The sonetSectionNoDefect should be set if and only if no other flag is set.  The various bit positions are\:       1   sonetSectionNoDefect       2   sonetSectionLOS       4   sonetSectionLOF
            	**type**\: int
            
            	**range:** 1..6
            
            

            """

            _prefix = 'sonet-mib'
            _revision = '2003-08-11'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.sonetsectioncurrentcvs = None
                self.sonetsectioncurrentess = None
                self.sonetsectioncurrentsefss = None
                self.sonetsectioncurrentsess = None
                self.sonetsectioncurrentstatus = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetSectionCurrentTable/SONET-MIB:sonetSectionCurrentEntry[SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.sonetsectioncurrentcvs is not None:
                    return True

                if self.sonetsectioncurrentess is not None:
                    return True

                if self.sonetsectioncurrentsefss is not None:
                    return True

                if self.sonetsectioncurrentsess is not None:
                    return True

                if self.sonetsectioncurrentstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _SONET_MIB as meta
                return meta._meta_table['SONETMIB.SonetSectionCurrentTable.SonetSectionCurrentEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetSectionCurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sonetsectioncurrententry is not None:
                for child_ref in self.sonetsectioncurrententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _SONET_MIB as meta
            return meta._meta_table['SONETMIB.SonetSectionCurrentTable']['meta_info']


    class SonetSectionIntervalTable(object):
        """
        The SONET/SDH Section Interval table.
        
        .. attribute:: sonetsectionintervalentry
        
        	An entry in the SONET/SDH Section Interval table
        	**type**\: list of :py:class:`SonetSectionIntervalEntry <ydk.models.sonet.SONET_MIB.SONETMIB.SonetSectionIntervalTable.SonetSectionIntervalEntry>`
        
        

        """

        _prefix = 'sonet-mib'
        _revision = '2003-08-11'

        def __init__(self):
            self.parent = None
            self.sonetsectionintervalentry = YList()
            self.sonetsectionintervalentry.parent = self
            self.sonetsectionintervalentry.name = 'sonetsectionintervalentry'


        class SonetSectionIntervalEntry(object):
            """
            An entry in the SONET/SDH Section Interval table.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: sonetsectionintervalnumber
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: sonetsectionintervalcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH Section in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectionintervaless
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH Section in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectionintervalsefss
            
            	The counter associated with the number of Severely Errored Framing Seconds encountered by a SONET/SDH Section in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectionintervalsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH Section in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetsectionintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            

            """

            _prefix = 'sonet-mib'
            _revision = '2003-08-11'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.sonetsectionintervalnumber = None
                self.sonetsectionintervalcvs = None
                self.sonetsectionintervaless = None
                self.sonetsectionintervalsefss = None
                self.sonetsectionintervalsess = None
                self.sonetsectionintervalvaliddata = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')
                if self.sonetsectionintervalnumber is None:
                    raise YPYDataValidationError('Key property sonetsectionintervalnumber is None')

                return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetSectionIntervalTable/SONET-MIB:sonetSectionIntervalEntry[SONET-MIB:ifIndex = ' + str(self.ifindex) + '][SONET-MIB:sonetSectionIntervalNumber = ' + str(self.sonetsectionintervalnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.sonetsectionintervalnumber is not None:
                    return True

                if self.sonetsectionintervalcvs is not None:
                    return True

                if self.sonetsectionintervaless is not None:
                    return True

                if self.sonetsectionintervalsefss is not None:
                    return True

                if self.sonetsectionintervalsess is not None:
                    return True

                if self.sonetsectionintervalvaliddata is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _SONET_MIB as meta
                return meta._meta_table['SONETMIB.SonetSectionIntervalTable.SonetSectionIntervalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetSectionIntervalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sonetsectionintervalentry is not None:
                for child_ref in self.sonetsectionintervalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _SONET_MIB as meta
            return meta._meta_table['SONETMIB.SonetSectionIntervalTable']['meta_info']


    class SonetVTCurrentTable(object):
        """
        The SONET/SDH VT Current table.
        
        .. attribute:: sonetvtcurrententry
        
        	An entry in the SONET/SDH VT Current table
        	**type**\: list of :py:class:`SonetVTCurrentEntry <ydk.models.sonet.SONET_MIB.SONETMIB.SonetVTCurrentTable.SonetVTCurrentEntry>`
        
        

        """

        _prefix = 'sonet-mib'
        _revision = '2003-08-11'

        def __init__(self):
            self.parent = None
            self.sonetvtcurrententry = YList()
            self.sonetvtcurrententry.parent = self
            self.sonetvtcurrententry.name = 'sonetvtcurrententry'


        class SonetVTCurrentEntry(object):
            """
            An entry in the SONET/SDH VT Current table.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: sonetvtcurrentcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH VT in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtcurrentess
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH VT in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtcurrentsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH VT in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtcurrentstatus
            
            	This variable indicates the status of the interface. The sonetVTCurrentStatus is a bit map represented as a sum, therefore, it can represent multiple defects and failures simultaneously. The sonetVTNoDefect should be set if and only if no other flag is set.  The various bit positions are\:    1   sonetVTNoDefect    2   sonetVTLOP    4   sonetVTPathAIS    8   sonetVTPathRDI   16   sonetVTPathRFI   32   sonetVTUnequipped   64   sonetVTSignalLabelMismatch
            	**type**\: int
            
            	**range:** 1..126
            
            .. attribute:: sonetvtcurrentuass
            
            	The counter associated with the number of Unavailable Seconds encountered by a VT in the current 15 minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtcurrentwidth
            
            	A value that indicates the type of the SONET VT and SDH VC.  Assigned widths are VT1.5/VC11, VT2/VC12, VT3, VT6/VC2, and VT6c
            	**type**\: :py:class:`SonetVTCurrentWidth_Enum <ydk.models.sonet.SONET_MIB.SONETMIB.SonetVTCurrentTable.SonetVTCurrentEntry.SonetVTCurrentWidth_Enum>`
            
            

            """

            _prefix = 'sonet-mib'
            _revision = '2003-08-11'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.sonetvtcurrentcvs = None
                self.sonetvtcurrentess = None
                self.sonetvtcurrentsess = None
                self.sonetvtcurrentstatus = None
                self.sonetvtcurrentuass = None
                self.sonetvtcurrentwidth = None

            class SonetVTCurrentWidth_Enum(Enum):
                """
                SonetVTCurrentWidth_Enum

                A value that indicates the type of the SONET
                VT and SDH VC.  Assigned widths are
                VT1.5/VC11, VT2/VC12, VT3, VT6/VC2, and VT6c.

                """

                VTWIDTH15VC11 = 1

                VTWIDTH2VC12 = 2

                VTWIDTH3 = 3

                VTWIDTH6VC2 = 4

                VTWIDTH6C = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.sonet._meta import _SONET_MIB as meta
                    return meta._meta_table['SONETMIB.SonetVTCurrentTable.SonetVTCurrentEntry.SonetVTCurrentWidth_Enum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetVTCurrentTable/SONET-MIB:sonetVTCurrentEntry[SONET-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.sonetvtcurrentcvs is not None:
                    return True

                if self.sonetvtcurrentess is not None:
                    return True

                if self.sonetvtcurrentsess is not None:
                    return True

                if self.sonetvtcurrentstatus is not None:
                    return True

                if self.sonetvtcurrentuass is not None:
                    return True

                if self.sonetvtcurrentwidth is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _SONET_MIB as meta
                return meta._meta_table['SONETMIB.SonetVTCurrentTable.SonetVTCurrentEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetVTCurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sonetvtcurrententry is not None:
                for child_ref in self.sonetvtcurrententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _SONET_MIB as meta
            return meta._meta_table['SONETMIB.SonetVTCurrentTable']['meta_info']


    class SonetVTIntervalTable(object):
        """
        The SONET/SDH VT Interval table.
        
        .. attribute:: sonetvtintervalentry
        
        	An entry in the SONET/SDH VT Interval table
        	**type**\: list of :py:class:`SonetVTIntervalEntry <ydk.models.sonet.SONET_MIB.SONETMIB.SonetVTIntervalTable.SonetVTIntervalEntry>`
        
        

        """

        _prefix = 'sonet-mib'
        _revision = '2003-08-11'

        def __init__(self):
            self.parent = None
            self.sonetvtintervalentry = YList()
            self.sonetvtintervalentry.parent = self
            self.sonetvtintervalentry.name = 'sonetvtintervalentry'


        class SonetVTIntervalEntry(object):
            """
            An entry in the SONET/SDH VT Interval table.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: sonetvtintervalnumber
            
            	A number between 1 and 96, which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: sonetvtintervalcvs
            
            	The counter associated with the number of Coding Violations encountered by a SONET/SDH VT in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtintervaless
            
            	The counter associated with the number of Errored Seconds encountered by a SONET/SDH VT in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtintervalsess
            
            	The counter associated with the number of Severely Errored Seconds encountered by a SONET/SDH VT in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtintervaluass
            
            	The counter associated with the number of Unavailable Seconds encountered by a VT in a particular 15\-minute interval in the past 24 hours
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonetvtintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            

            """

            _prefix = 'sonet-mib'
            _revision = '2003-08-11'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.sonetvtintervalnumber = None
                self.sonetvtintervalcvs = None
                self.sonetvtintervaless = None
                self.sonetvtintervalsess = None
                self.sonetvtintervaluass = None
                self.sonetvtintervalvaliddata = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')
                if self.sonetvtintervalnumber is None:
                    raise YPYDataValidationError('Key property sonetvtintervalnumber is None')

                return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetVTIntervalTable/SONET-MIB:sonetVTIntervalEntry[SONET-MIB:ifIndex = ' + str(self.ifindex) + '][SONET-MIB:sonetVTIntervalNumber = ' + str(self.sonetvtintervalnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.sonetvtintervalnumber is not None:
                    return True

                if self.sonetvtintervalcvs is not None:
                    return True

                if self.sonetvtintervaless is not None:
                    return True

                if self.sonetvtintervalsess is not None:
                    return True

                if self.sonetvtintervaluass is not None:
                    return True

                if self.sonetvtintervalvaliddata is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.sonet._meta import _SONET_MIB as meta
                return meta._meta_table['SONETMIB.SonetVTIntervalTable.SonetVTIntervalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SONET-MIB:SONET-MIB/SONET-MIB:sonetVTIntervalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sonetvtintervalentry is not None:
                for child_ref in self.sonetvtintervalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.sonet._meta import _SONET_MIB as meta
            return meta._meta_table['SONETMIB.SonetVTIntervalTable']['meta_info']

    @property
    def _common_path(self):

        return '/SONET-MIB:SONET-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.sonetfarendlinecurrenttable is not None and self.sonetfarendlinecurrenttable._has_data():
            return True

        if self.sonetfarendlinecurrenttable is not None and self.sonetfarendlinecurrenttable.is_presence():
            return True

        if self.sonetfarendlineintervaltable is not None and self.sonetfarendlineintervaltable._has_data():
            return True

        if self.sonetfarendlineintervaltable is not None and self.sonetfarendlineintervaltable.is_presence():
            return True

        if self.sonetfarendpathcurrenttable is not None and self.sonetfarendpathcurrenttable._has_data():
            return True

        if self.sonetfarendpathcurrenttable is not None and self.sonetfarendpathcurrenttable.is_presence():
            return True

        if self.sonetfarendpathintervaltable is not None and self.sonetfarendpathintervaltable._has_data():
            return True

        if self.sonetfarendpathintervaltable is not None and self.sonetfarendpathintervaltable.is_presence():
            return True

        if self.sonetfarendvtcurrenttable is not None and self.sonetfarendvtcurrenttable._has_data():
            return True

        if self.sonetfarendvtcurrenttable is not None and self.sonetfarendvtcurrenttable.is_presence():
            return True

        if self.sonetfarendvtintervaltable is not None and self.sonetfarendvtintervaltable._has_data():
            return True

        if self.sonetfarendvtintervaltable is not None and self.sonetfarendvtintervaltable.is_presence():
            return True

        if self.sonetlinecurrenttable is not None and self.sonetlinecurrenttable._has_data():
            return True

        if self.sonetlinecurrenttable is not None and self.sonetlinecurrenttable.is_presence():
            return True

        if self.sonetlineintervaltable is not None and self.sonetlineintervaltable._has_data():
            return True

        if self.sonetlineintervaltable is not None and self.sonetlineintervaltable.is_presence():
            return True

        if self.sonetmedium is not None and self.sonetmedium._has_data():
            return True

        if self.sonetmedium is not None and self.sonetmedium.is_presence():
            return True

        if self.sonetmediumtable is not None and self.sonetmediumtable._has_data():
            return True

        if self.sonetmediumtable is not None and self.sonetmediumtable.is_presence():
            return True

        if self.sonetpathcurrenttable is not None and self.sonetpathcurrenttable._has_data():
            return True

        if self.sonetpathcurrenttable is not None and self.sonetpathcurrenttable.is_presence():
            return True

        if self.sonetpathintervaltable is not None and self.sonetpathintervaltable._has_data():
            return True

        if self.sonetpathintervaltable is not None and self.sonetpathintervaltable.is_presence():
            return True

        if self.sonetsectioncurrenttable is not None and self.sonetsectioncurrenttable._has_data():
            return True

        if self.sonetsectioncurrenttable is not None and self.sonetsectioncurrenttable.is_presence():
            return True

        if self.sonetsectionintervaltable is not None and self.sonetsectionintervaltable._has_data():
            return True

        if self.sonetsectionintervaltable is not None and self.sonetsectionintervaltable.is_presence():
            return True

        if self.sonetvtcurrenttable is not None and self.sonetvtcurrenttable._has_data():
            return True

        if self.sonetvtcurrenttable is not None and self.sonetvtcurrenttable.is_presence():
            return True

        if self.sonetvtintervaltable is not None and self.sonetvtintervaltable._has_data():
            return True

        if self.sonetvtintervaltable is not None and self.sonetvtintervaltable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.sonet._meta import _SONET_MIB as meta
        return meta._meta_table['SONETMIB']['meta_info']


