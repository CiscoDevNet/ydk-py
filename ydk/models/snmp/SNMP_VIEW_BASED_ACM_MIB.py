""" SNMP_VIEW_BASED_ACM_MIB 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmp.SNMP_FRAMEWORK_MIB import SnmpSecurityLevel_Enum
from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum

class VacmAccessContextMatchType_Enum(Enum):
    """
    VacmAccessContextMatchType_Enum

    """

    EXACT = 1

    PREFIX = 2


    @staticmethod
    def _meta_info():
        from ydk.models.snmp._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
        return meta._meta_table['VacmAccessContextMatchType_Enum']


class VacmViewTreeFamilyTypeType_Enum(Enum):
    """
    VacmViewTreeFamilyTypeType_Enum

    """

    INCLUDED = 1

    EXCLUDED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.snmp._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
        return meta._meta_table['VacmViewTreeFamilyTypeType_Enum']



class SNMPVIEWBASEDACMMIB(object):
    """
    
    
    .. attribute:: vacmaccesstable
    
    	
    	**type**\: :py:class:`VacmAccessTable <ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB.SNMPVIEWBASEDACMMIB.VacmAccessTable>`
    
    .. attribute:: vacmsecuritytogrouptable
    
    	
    	**type**\: :py:class:`VacmSecurityToGroupTable <ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB.SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable>`
    
    .. attribute:: vacmviewtreefamilytable
    
    	
    	**type**\: :py:class:`VacmViewTreeFamilyTable <ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB.SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable>`
    
    

    """

    _prefix = 'SNMP_VIEW_BASED_ACM_MIB'
    _revision = '2002-10-16'

    def __init__(self):
        self.vacmaccesstable = SNMPVIEWBASEDACMMIB.VacmAccessTable()
        self.vacmaccesstable.parent = self
        self.vacmsecuritytogrouptable = SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable()
        self.vacmsecuritytogrouptable.parent = self
        self.vacmviewtreefamilytable = SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable()
        self.vacmviewtreefamilytable.parent = self


    class VacmAccessTable(object):
        """
        
        
        .. attribute:: vacmaccessentry
        
        	
        	**type**\: list of :py:class:`VacmAccessEntry <ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB.SNMPVIEWBASEDACMMIB.VacmAccessTable.VacmAccessEntry>`
        
        

        """

        _prefix = 'SNMP_VIEW_BASED_ACM_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            self.parent = None
            self.vacmaccessentry = YList()
            self.vacmaccessentry.parent = self
            self.vacmaccessentry.name = 'vacmaccessentry'


        class VacmAccessEntry(object):
            """
            
            
            .. attribute:: vacmaccesscontextprefix
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: vacmaccesssecuritylevel
            
            	
            	**type**\: :py:class:`SnmpSecurityLevel_Enum <ydk.models.snmp.SNMP_FRAMEWORK_MIB.SnmpSecurityLevel_Enum>`
            
            .. attribute:: vacmaccesssecuritymodel
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: vacmgroupname
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: vacmaccesscontextmatch
            
            	
            	**type**\: :py:class:`VacmAccessContextMatchType_Enum <ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB.VacmAccessContextMatchType_Enum>`
            
            .. attribute:: vacmaccessnotifyviewname
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: vacmaccessreadviewname
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: vacmaccessstoragetype
            
            	
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: vacmaccesswriteviewname
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            

            """

            _prefix = 'SNMP_VIEW_BASED_ACM_MIB'
            _revision = '2002-10-16'

            def __init__(self):
                self.parent = None
                self.vacmaccesscontextprefix = None
                self.vacmaccesssecuritylevel = None
                self.vacmaccesssecuritymodel = None
                self.vacmgroupname = None
                self.vacmaccesscontextmatch = None
                self.vacmaccessnotifyviewname = None
                self.vacmaccessreadviewname = None
                self.vacmaccessstoragetype = None
                self.vacmaccesswriteviewname = None

            @property
            def _common_path(self):
                if self.vacmaccesscontextprefix is None:
                    raise YPYDataValidationError('Key property vacmaccesscontextprefix is None')
                if self.vacmaccesssecuritylevel is None:
                    raise YPYDataValidationError('Key property vacmaccesssecuritylevel is None')
                if self.vacmaccesssecuritymodel is None:
                    raise YPYDataValidationError('Key property vacmaccesssecuritymodel is None')
                if self.vacmgroupname is None:
                    raise YPYDataValidationError('Key property vacmgroupname is None')

                return '/SNMP-VIEW-BASED-ACM-MIB:SNMP-VIEW-BASED-ACM-MIB/SNMP-VIEW-BASED-ACM-MIB:vacmAccessTable/SNMP-VIEW-BASED-ACM-MIB:vacmAccessEntry[SNMP-VIEW-BASED-ACM-MIB:vacmAccessContextPrefix = ' + str(self.vacmaccesscontextprefix) + '][SNMP-VIEW-BASED-ACM-MIB:vacmAccessSecurityLevel = ' + str(self.vacmaccesssecuritylevel) + '][SNMP-VIEW-BASED-ACM-MIB:vacmAccessSecurityModel = ' + str(self.vacmaccesssecuritymodel) + '][SNMP-VIEW-BASED-ACM-MIB:vacmGroupName = ' + str(self.vacmgroupname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.vacmaccesscontextprefix is not None:
                    return True

                if self.vacmaccesssecuritylevel is not None:
                    return True

                if self.vacmaccesssecuritymodel is not None:
                    return True

                if self.vacmgroupname is not None:
                    return True

                if self.vacmaccesscontextmatch is not None:
                    return True

                if self.vacmaccessnotifyviewname is not None:
                    return True

                if self.vacmaccessreadviewname is not None:
                    return True

                if self.vacmaccessstoragetype is not None:
                    return True

                if self.vacmaccesswriteviewname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.snmp._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
                return meta._meta_table['SNMPVIEWBASEDACMMIB.VacmAccessTable.VacmAccessEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SNMP-VIEW-BASED-ACM-MIB:SNMP-VIEW-BASED-ACM-MIB/SNMP-VIEW-BASED-ACM-MIB:vacmAccessTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vacmaccessentry is not None:
                for child_ref in self.vacmaccessentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.snmp._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
            return meta._meta_table['SNMPVIEWBASEDACMMIB.VacmAccessTable']['meta_info']


    class VacmSecurityToGroupTable(object):
        """
        
        
        .. attribute:: vacmsecuritytogroupentry
        
        	
        	**type**\: list of :py:class:`VacmSecurityToGroupEntry <ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB.SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable.VacmSecurityToGroupEntry>`
        
        

        """

        _prefix = 'SNMP_VIEW_BASED_ACM_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            self.parent = None
            self.vacmsecuritytogroupentry = YList()
            self.vacmsecuritytogroupentry.parent = self
            self.vacmsecuritytogroupentry.name = 'vacmsecuritytogroupentry'


        class VacmSecurityToGroupEntry(object):
            """
            
            
            .. attribute:: vacmsecuritymodel
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: vacmsecurityname
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: vacmgroupname
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: vacmsecuritytogroupstoragetype
            
            	
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'SNMP_VIEW_BASED_ACM_MIB'
            _revision = '2002-10-16'

            def __init__(self):
                self.parent = None
                self.vacmsecuritymodel = None
                self.vacmsecurityname = None
                self.vacmgroupname = None
                self.vacmsecuritytogroupstoragetype = None

            @property
            def _common_path(self):
                if self.vacmsecuritymodel is None:
                    raise YPYDataValidationError('Key property vacmsecuritymodel is None')
                if self.vacmsecurityname is None:
                    raise YPYDataValidationError('Key property vacmsecurityname is None')

                return '/SNMP-VIEW-BASED-ACM-MIB:SNMP-VIEW-BASED-ACM-MIB/SNMP-VIEW-BASED-ACM-MIB:vacmSecurityToGroupTable/SNMP-VIEW-BASED-ACM-MIB:vacmSecurityToGroupEntry[SNMP-VIEW-BASED-ACM-MIB:vacmSecurityModel = ' + str(self.vacmsecuritymodel) + '][SNMP-VIEW-BASED-ACM-MIB:vacmSecurityName = ' + str(self.vacmsecurityname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.vacmsecuritymodel is not None:
                    return True

                if self.vacmsecurityname is not None:
                    return True

                if self.vacmgroupname is not None:
                    return True

                if self.vacmsecuritytogroupstoragetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.snmp._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
                return meta._meta_table['SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable.VacmSecurityToGroupEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SNMP-VIEW-BASED-ACM-MIB:SNMP-VIEW-BASED-ACM-MIB/SNMP-VIEW-BASED-ACM-MIB:vacmSecurityToGroupTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vacmsecuritytogroupentry is not None:
                for child_ref in self.vacmsecuritytogroupentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.snmp._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
            return meta._meta_table['SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable']['meta_info']


    class VacmViewTreeFamilyTable(object):
        """
        
        
        .. attribute:: vacmviewtreefamilyentry
        
        	
        	**type**\: list of :py:class:`VacmViewTreeFamilyEntry <ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB.SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable.VacmViewTreeFamilyEntry>`
        
        

        """

        _prefix = 'SNMP_VIEW_BASED_ACM_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            self.parent = None
            self.vacmviewtreefamilyentry = YList()
            self.vacmviewtreefamilyentry.parent = self
            self.vacmviewtreefamilyentry.name = 'vacmviewtreefamilyentry'


        class VacmViewTreeFamilyEntry(object):
            """
            
            
            .. attribute:: vacmviewtreefamilysubtree
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: vacmviewtreefamilyviewname
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: vacmviewtreefamilymask
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: vacmviewtreefamilystoragetype
            
            	
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: vacmviewtreefamilytype
            
            	
            	**type**\: :py:class:`VacmViewTreeFamilyTypeType_Enum <ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB.VacmViewTreeFamilyTypeType_Enum>`
            
            

            """

            _prefix = 'SNMP_VIEW_BASED_ACM_MIB'
            _revision = '2002-10-16'

            def __init__(self):
                self.parent = None
                self.vacmviewtreefamilysubtree = None
                self.vacmviewtreefamilyviewname = None
                self.vacmviewtreefamilymask = None
                self.vacmviewtreefamilystoragetype = None
                self.vacmviewtreefamilytype = None

            @property
            def _common_path(self):
                if self.vacmviewtreefamilysubtree is None:
                    raise YPYDataValidationError('Key property vacmviewtreefamilysubtree is None')
                if self.vacmviewtreefamilyviewname is None:
                    raise YPYDataValidationError('Key property vacmviewtreefamilyviewname is None')

                return '/SNMP-VIEW-BASED-ACM-MIB:SNMP-VIEW-BASED-ACM-MIB/SNMP-VIEW-BASED-ACM-MIB:vacmViewTreeFamilyTable/SNMP-VIEW-BASED-ACM-MIB:vacmViewTreeFamilyEntry[SNMP-VIEW-BASED-ACM-MIB:vacmViewTreeFamilySubtree = ' + str(self.vacmviewtreefamilysubtree) + '][SNMP-VIEW-BASED-ACM-MIB:vacmViewTreeFamilyViewName = ' + str(self.vacmviewtreefamilyviewname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.vacmviewtreefamilysubtree is not None:
                    return True

                if self.vacmviewtreefamilyviewname is not None:
                    return True

                if self.vacmviewtreefamilymask is not None:
                    return True

                if self.vacmviewtreefamilystoragetype is not None:
                    return True

                if self.vacmviewtreefamilytype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.snmp._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
                return meta._meta_table['SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable.VacmViewTreeFamilyEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SNMP-VIEW-BASED-ACM-MIB:SNMP-VIEW-BASED-ACM-MIB/SNMP-VIEW-BASED-ACM-MIB:vacmViewTreeFamilyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vacmviewtreefamilyentry is not None:
                for child_ref in self.vacmviewtreefamilyentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.snmp._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
            return meta._meta_table['SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable']['meta_info']

    @property
    def _common_path(self):

        return '/SNMP-VIEW-BASED-ACM-MIB:SNMP-VIEW-BASED-ACM-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.vacmaccesstable is not None and self.vacmaccesstable._has_data():
            return True

        if self.vacmaccesstable is not None and self.vacmaccesstable.is_presence():
            return True

        if self.vacmsecuritytogrouptable is not None and self.vacmsecuritytogrouptable._has_data():
            return True

        if self.vacmsecuritytogrouptable is not None and self.vacmsecuritytogrouptable.is_presence():
            return True

        if self.vacmviewtreefamilytable is not None and self.vacmviewtreefamilytable._has_data():
            return True

        if self.vacmviewtreefamilytable is not None and self.vacmviewtreefamilytable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.snmp._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
        return meta._meta_table['SNMPVIEWBASEDACMMIB']['meta_info']


