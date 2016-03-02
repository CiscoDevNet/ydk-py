""" SNMP_NOTIFICATION_MIB 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum

class SnmpNotifyFilterTypeType_Enum(Enum):
    """
    SnmpNotifyFilterTypeType_Enum

    """

    INCLUDED = 1

    EXCLUDED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.snmp._meta import _SNMP_NOTIFICATION_MIB as meta
        return meta._meta_table['SnmpNotifyFilterTypeType_Enum']


class SnmpNotifyTypeType_Enum(Enum):
    """
    SnmpNotifyTypeType_Enum

    """

    TRAP = 1

    INFORM = 2


    @staticmethod
    def _meta_info():
        from ydk.models.snmp._meta import _SNMP_NOTIFICATION_MIB as meta
        return meta._meta_table['SnmpNotifyTypeType_Enum']



class SNMPNOTIFICATIONMIB(object):
    """
    
    
    .. attribute:: snmpnotifyfilterprofiletable
    
    	
    	**type**\: :py:class:`SnmpNotifyFilterProfileTable <ydk.models.snmp.SNMP_NOTIFICATION_MIB.SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable>`
    
    .. attribute:: snmpnotifyfiltertable
    
    	
    	**type**\: :py:class:`SnmpNotifyFilterTable <ydk.models.snmp.SNMP_NOTIFICATION_MIB.SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable>`
    
    .. attribute:: snmpnotifytable
    
    	
    	**type**\: :py:class:`SnmpNotifyTable <ydk.models.snmp.SNMP_NOTIFICATION_MIB.SNMPNOTIFICATIONMIB.SnmpNotifyTable>`
    
    

    """

    _prefix = 'SNMP_NOTIFICATION_MIB'
    _revision = '2002-10-14'

    def __init__(self):
        self.snmpnotifyfilterprofiletable = None
        self.snmpnotifyfiltertable = None
        self.snmpnotifytable = SNMPNOTIFICATIONMIB.SnmpNotifyTable()
        self.snmpnotifytable.parent = self


    class SnmpNotifyFilterProfileTable(object):
        """
        
        
        .. attribute:: snmpnotifyfilterprofileentry
        
        	
        	**type**\: list of :py:class:`SnmpNotifyFilterProfileEntry <ydk.models.snmp.SNMP_NOTIFICATION_MIB.SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable.SnmpNotifyFilterProfileEntry>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'SNMP_NOTIFICATION_MIB'
        _revision = '2002-10-14'

        def __init__(self):
            self.parent = None
            self.snmpnotifyfilterprofileentry = YList()
            self.snmpnotifyfilterprofileentry.parent = self
            self.snmpnotifyfilterprofileentry.name = 'snmpnotifyfilterprofileentry'


        class SnmpNotifyFilterProfileEntry(object):
            """
            
            
            .. attribute:: snmptargetparamsname
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: snmpnotifyfilterprofilename
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: snmpnotifyfilterprofilestortype
            
            	
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'SNMP_NOTIFICATION_MIB'
            _revision = '2002-10-14'

            def __init__(self):
                self.parent = None
                self.snmptargetparamsname = None
                self.snmpnotifyfilterprofilename = None
                self.snmpnotifyfilterprofilestortype = None

            @property
            def _common_path(self):
                if self.snmptargetparamsname is None:
                    raise YPYDataValidationError('Key property snmptargetparamsname is None')

                return '/SNMP-NOTIFICATION-MIB:SNMP-NOTIFICATION-MIB/SNMP-NOTIFICATION-MIB:snmpNotifyFilterProfileTable/SNMP-NOTIFICATION-MIB:snmpNotifyFilterProfileEntry[SNMP-NOTIFICATION-MIB:snmpTargetParamsName = ' + str(self.snmptargetparamsname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.snmptargetparamsname is not None:
                    return True

                if self.snmpnotifyfilterprofilename is not None:
                    return True

                if self.snmpnotifyfilterprofilestortype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.snmp._meta import _SNMP_NOTIFICATION_MIB as meta
                return meta._meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable.SnmpNotifyFilterProfileEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SNMP-NOTIFICATION-MIB:SNMP-NOTIFICATION-MIB/SNMP-NOTIFICATION-MIB:snmpNotifyFilterProfileTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.snmpnotifyfilterprofileentry is not None:
                for child_ref in self.snmpnotifyfilterprofileentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return True

        @staticmethod
        def _meta_info():
            from ydk.models.snmp._meta import _SNMP_NOTIFICATION_MIB as meta
            return meta._meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable']['meta_info']


    class SnmpNotifyFilterTable(object):
        """
        
        
        .. attribute:: snmpnotifyfilterentry
        
        	
        	**type**\: list of :py:class:`SnmpNotifyFilterEntry <ydk.models.snmp.SNMP_NOTIFICATION_MIB.SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable.SnmpNotifyFilterEntry>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'SNMP_NOTIFICATION_MIB'
        _revision = '2002-10-14'

        def __init__(self):
            self.parent = None
            self.snmpnotifyfilterentry = YList()
            self.snmpnotifyfilterentry.parent = self
            self.snmpnotifyfilterentry.name = 'snmpnotifyfilterentry'


        class SnmpNotifyFilterEntry(object):
            """
            
            
            .. attribute:: snmpnotifyfilterprofilename
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: snmpnotifyfiltersubtree
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: snmpnotifyfiltermask
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: snmpnotifyfilterstoragetype
            
            	
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: snmpnotifyfiltertype
            
            	
            	**type**\: :py:class:`SnmpNotifyFilterTypeType_Enum <ydk.models.snmp.SNMP_NOTIFICATION_MIB.SnmpNotifyFilterTypeType_Enum>`
            
            

            """

            _prefix = 'SNMP_NOTIFICATION_MIB'
            _revision = '2002-10-14'

            def __init__(self):
                self.parent = None
                self.snmpnotifyfilterprofilename = None
                self.snmpnotifyfiltersubtree = None
                self.snmpnotifyfiltermask = None
                self.snmpnotifyfilterstoragetype = None
                self.snmpnotifyfiltertype = None

            @property
            def _common_path(self):
                if self.snmpnotifyfilterprofilename is None:
                    raise YPYDataValidationError('Key property snmpnotifyfilterprofilename is None')
                if self.snmpnotifyfiltersubtree is None:
                    raise YPYDataValidationError('Key property snmpnotifyfiltersubtree is None')

                return '/SNMP-NOTIFICATION-MIB:SNMP-NOTIFICATION-MIB/SNMP-NOTIFICATION-MIB:snmpNotifyFilterTable/SNMP-NOTIFICATION-MIB:snmpNotifyFilterEntry[SNMP-NOTIFICATION-MIB:snmpNotifyFilterProfileName = ' + str(self.snmpnotifyfilterprofilename) + '][SNMP-NOTIFICATION-MIB:snmpNotifyFilterSubtree = ' + str(self.snmpnotifyfiltersubtree) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.snmpnotifyfilterprofilename is not None:
                    return True

                if self.snmpnotifyfiltersubtree is not None:
                    return True

                if self.snmpnotifyfiltermask is not None:
                    return True

                if self.snmpnotifyfilterstoragetype is not None:
                    return True

                if self.snmpnotifyfiltertype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.snmp._meta import _SNMP_NOTIFICATION_MIB as meta
                return meta._meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable.SnmpNotifyFilterEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SNMP-NOTIFICATION-MIB:SNMP-NOTIFICATION-MIB/SNMP-NOTIFICATION-MIB:snmpNotifyFilterTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.snmpnotifyfilterentry is not None:
                for child_ref in self.snmpnotifyfilterentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return True

        @staticmethod
        def _meta_info():
            from ydk.models.snmp._meta import _SNMP_NOTIFICATION_MIB as meta
            return meta._meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable']['meta_info']


    class SnmpNotifyTable(object):
        """
        
        
        .. attribute:: snmpnotifyentry
        
        	
        	**type**\: list of :py:class:`SnmpNotifyEntry <ydk.models.snmp.SNMP_NOTIFICATION_MIB.SNMPNOTIFICATIONMIB.SnmpNotifyTable.SnmpNotifyEntry>`
        
        

        """

        _prefix = 'SNMP_NOTIFICATION_MIB'
        _revision = '2002-10-14'

        def __init__(self):
            self.parent = None
            self.snmpnotifyentry = YList()
            self.snmpnotifyentry.parent = self
            self.snmpnotifyentry.name = 'snmpnotifyentry'


        class SnmpNotifyEntry(object):
            """
            
            
            .. attribute:: snmpnotifyname
            
            	
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: snmpnotifystoragetype
            
            	
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: snmpnotifytag
            
            	
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: snmpnotifytype
            
            	
            	**type**\: :py:class:`SnmpNotifyTypeType_Enum <ydk.models.snmp.SNMP_NOTIFICATION_MIB.SnmpNotifyTypeType_Enum>`
            
            

            """

            _prefix = 'SNMP_NOTIFICATION_MIB'
            _revision = '2002-10-14'

            def __init__(self):
                self.parent = None
                self.snmpnotifyname = None
                self.snmpnotifystoragetype = None
                self.snmpnotifytag = None
                self.snmpnotifytype = None

            @property
            def _common_path(self):
                if self.snmpnotifyname is None:
                    raise YPYDataValidationError('Key property snmpnotifyname is None')

                return '/SNMP-NOTIFICATION-MIB:SNMP-NOTIFICATION-MIB/SNMP-NOTIFICATION-MIB:snmpNotifyTable/SNMP-NOTIFICATION-MIB:snmpNotifyEntry[SNMP-NOTIFICATION-MIB:snmpNotifyName = ' + str(self.snmpnotifyname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.snmpnotifyname is not None:
                    return True

                if self.snmpnotifystoragetype is not None:
                    return True

                if self.snmpnotifytag is not None:
                    return True

                if self.snmpnotifytype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.snmp._meta import _SNMP_NOTIFICATION_MIB as meta
                return meta._meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyTable.SnmpNotifyEntry']['meta_info']

        @property
        def _common_path(self):

            return '/SNMP-NOTIFICATION-MIB:SNMP-NOTIFICATION-MIB/SNMP-NOTIFICATION-MIB:snmpNotifyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.snmpnotifyentry is not None:
                for child_ref in self.snmpnotifyentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.snmp._meta import _SNMP_NOTIFICATION_MIB as meta
            return meta._meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyTable']['meta_info']

    @property
    def _common_path(self):

        return '/SNMP-NOTIFICATION-MIB:SNMP-NOTIFICATION-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.snmpnotifyfilterprofiletable is not None and self.snmpnotifyfilterprofiletable._has_data():
            return True

        if self.snmpnotifyfilterprofiletable is not None and self.snmpnotifyfilterprofiletable.is_presence():
            return True

        if self.snmpnotifyfiltertable is not None and self.snmpnotifyfiltertable._has_data():
            return True

        if self.snmpnotifyfiltertable is not None and self.snmpnotifyfiltertable.is_presence():
            return True

        if self.snmpnotifytable is not None and self.snmpnotifytable._has_data():
            return True

        if self.snmpnotifytable is not None and self.snmpnotifytable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.snmp._meta import _SNMP_NOTIFICATION_MIB as meta
        return meta._meta_table['SNMPNOTIFICATIONMIB']['meta_info']


