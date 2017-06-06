""" CISCO_IMAGE_MIB 

Router image MIB which identify the capabilities
and characteristics of the image

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoImageMib(object):
    """
    
    
    .. attribute:: ciscoimagetable
    
    	A table provides content information describing the executing IOS image
    	**type**\:   :py:class:`Ciscoimagetable <ydk.models.cisco_ios_xe.CISCO_IMAGE_MIB.CiscoImageMib.Ciscoimagetable>`
    
    

    """

    _prefix = 'CISCO-IMAGE-MIB'
    _revision = '1995-08-15'

    def __init__(self):
        self.ciscoimagetable = CiscoImageMib.Ciscoimagetable()
        self.ciscoimagetable.parent = self


    class Ciscoimagetable(object):
        """
        A table provides content information describing the
        executing IOS image.
        
        .. attribute:: ciscoimageentry
        
        	A image characteristic string entry
        	**type**\: list of    :py:class:`Ciscoimageentry <ydk.models.cisco_ios_xe.CISCO_IMAGE_MIB.CiscoImageMib.Ciscoimagetable.Ciscoimageentry>`
        
        

        """

        _prefix = 'CISCO-IMAGE-MIB'
        _revision = '1995-08-15'

        def __init__(self):
            self.parent = None
            self.ciscoimageentry = YList()
            self.ciscoimageentry.parent = self
            self.ciscoimageentry.name = 'ciscoimageentry'


        class Ciscoimageentry(object):
            """
            A image characteristic string entry.
            
            .. attribute:: ciscoimageindex  <key>
            
            	A sequence number for each string stored in the IOS image
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoimagestring
            
            	The string of this entry
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-IMAGE-MIB'
            _revision = '1995-08-15'

            def __init__(self):
                self.parent = None
                self.ciscoimageindex = None
                self.ciscoimagestring = None

            @property
            def _common_path(self):
                if self.ciscoimageindex is None:
                    raise YPYModelError('Key property ciscoimageindex is None')

                return '/CISCO-IMAGE-MIB:CISCO-IMAGE-MIB/CISCO-IMAGE-MIB:ciscoImageTable/CISCO-IMAGE-MIB:ciscoImageEntry[CISCO-IMAGE-MIB:ciscoImageIndex = ' + str(self.ciscoimageindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ciscoimageindex is not None:
                    return True

                if self.ciscoimagestring is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IMAGE_MIB as meta
                return meta._meta_table['CiscoImageMib.Ciscoimagetable.Ciscoimageentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IMAGE-MIB:CISCO-IMAGE-MIB/CISCO-IMAGE-MIB:ciscoImageTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ciscoimageentry is not None:
                for child_ref in self.ciscoimageentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IMAGE_MIB as meta
            return meta._meta_table['CiscoImageMib.Ciscoimagetable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IMAGE-MIB:CISCO-IMAGE-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ciscoimagetable is not None and self.ciscoimagetable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IMAGE_MIB as meta
        return meta._meta_table['CiscoImageMib']['meta_info']


