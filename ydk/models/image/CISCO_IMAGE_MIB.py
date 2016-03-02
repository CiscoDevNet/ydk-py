""" CISCO_IMAGE_MIB 

Router image MIB which identify the capabilities
and characteristics of the image

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class CISCOIMAGEMIB(object):
    """
    
    
    .. attribute:: ciscoimagetable
    
    	A table provides content information describing the executing IOS image
    	**type**\: :py:class:`CiscoImageTable <ydk.models.image.CISCO_IMAGE_MIB.CISCOIMAGEMIB.CiscoImageTable>`
    
    

    """

    _prefix = 'cisco-image'
    _revision = '1995-08-15'

    def __init__(self):
        self.ciscoimagetable = CISCOIMAGEMIB.CiscoImageTable()
        self.ciscoimagetable.parent = self


    class CiscoImageTable(object):
        """
        A table provides content information describing the
        executing IOS image.
        
        .. attribute:: ciscoimageentry
        
        	A image characteristic string entry
        	**type**\: list of :py:class:`CiscoImageEntry <ydk.models.image.CISCO_IMAGE_MIB.CISCOIMAGEMIB.CiscoImageTable.CiscoImageEntry>`
        
        

        """

        _prefix = 'cisco-image'
        _revision = '1995-08-15'

        def __init__(self):
            self.parent = None
            self.ciscoimageentry = YList()
            self.ciscoimageentry.parent = self
            self.ciscoimageentry.name = 'ciscoimageentry'


        class CiscoImageEntry(object):
            """
            A image characteristic string entry.
            
            .. attribute:: ciscoimageindex
            
            	A sequence number for each string stored in the IOS image
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoimagestring
            
            	The string of this entry
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            

            """

            _prefix = 'cisco-image'
            _revision = '1995-08-15'

            def __init__(self):
                self.parent = None
                self.ciscoimageindex = None
                self.ciscoimagestring = None

            @property
            def _common_path(self):
                if self.ciscoimageindex is None:
                    raise YPYDataValidationError('Key property ciscoimageindex is None')

                return '/CISCO-IMAGE-MIB:CISCO-IMAGE-MIB/CISCO-IMAGE-MIB:ciscoImageTable/CISCO-IMAGE-MIB:ciscoImageEntry[CISCO-IMAGE-MIB:ciscoImageIndex = ' + str(self.ciscoimageindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscoimageindex is not None:
                    return True

                if self.ciscoimagestring is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.image._meta import _CISCO_IMAGE_MIB as meta
                return meta._meta_table['CISCOIMAGEMIB.CiscoImageTable.CiscoImageEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IMAGE-MIB:CISCO-IMAGE-MIB/CISCO-IMAGE-MIB:ciscoImageTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscoimageentry is not None:
                for child_ref in self.ciscoimageentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.image._meta import _CISCO_IMAGE_MIB as meta
            return meta._meta_table['CISCOIMAGEMIB.CiscoImageTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IMAGE-MIB:CISCO-IMAGE-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ciscoimagetable is not None and self.ciscoimagetable._has_data():
            return True

        if self.ciscoimagetable is not None and self.ciscoimagetable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.image._meta import _CISCO_IMAGE_MIB as meta
        return meta._meta_table['CISCOIMAGEMIB']['meta_info']


