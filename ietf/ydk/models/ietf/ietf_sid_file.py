""" ietf_sid_file 

This module define the structure of the .sid files.
.sid files contains the identifiers (SIDs) assigned
to the different items defined in a YANG module.
SIDs are used to encode a data model defined in YANG
using CBOR.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class AssigmentRanges(object):
    """
    Range(s) of SIDs available for assignment to the
    different items defined by the associated module.
    
    .. attribute:: entry_point  <key>
    
    	Lowest SID available for assignment
    	**type**\:  int
    
    	**range:** 0..4294967295
    
    	**mandatory**\: True
    
    .. attribute:: size
    
    	Number of SIDs available for assignment
    	**type**\:  int
    
    	**range:** 0..65535
    
    	**mandatory**\: True
    
    

    """

    _prefix = 'sid'
    _revision = '2015-12-16'

    def __init__(self):
        self.entry_point = None
        self.size = None

    @property
    def _common_path(self):
        if self.entry_point is None:
            raise YPYModelError('Key property entry_point is None')

        return '/ietf-sid-file:assigment-ranges[ietf-sid-file:entry-point = ' + str(self.entry_point) + ']'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.entry_point is not None:
            return True

        if self.size is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_sid_file as meta
        return meta._meta_table['AssigmentRanges']['meta_info']


class Items(object):
    """
    List of items defined by the associated YANG module.
    
    .. attribute:: label  <key>
    
    	Label associated to this item, can be set to\:  \- a module name  \- a submodule name  \- a feature name  \- a base identity encoded as '/<base identity name>'  \- an identity encoded as '/<base identity name>/<identity name>'  \- a schema node path
    	**type**\:  str
    
    	**mandatory**\: True
    
    .. attribute:: type  <key>
    
    	Item type assigned, this field can be set to\:  \- 'Module'  \- 'Submodule'  \- 'feature'  \- 'identity'  \- 'node'  \- 'notification'  \- 'rpc'  \- 'action'
    	**type**\:  str
    
    	**pattern:** Module\|Submodule\|feature\|identity$\|node$\|notification$\|rpc$\|action$
    
    	**mandatory**\: True
    
    .. attribute:: sid
    
    	Identifier assigned to this YANG item
    	**type**\:  int
    
    	**range:** 0..4294967295
    
    	**mandatory**\: True
    
    

    """

    _prefix = 'sid'
    _revision = '2015-12-16'

    def __init__(self):
        self.label = None
        self.type = None
        self.sid = None

    @property
    def _common_path(self):
        if self.label is None:
            raise YPYModelError('Key property label is None')
        if self.type is None:
            raise YPYModelError('Key property type is None')

        return '/ietf-sid-file:items[ietf-sid-file:label = ' + str(self.label) + '][ietf-sid-file:type = ' + str(self.type) + ']'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.label is not None:
            return True

        if self.type is not None:
            return True

        if self.sid is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_sid_file as meta
        return meta._meta_table['Items']['meta_info']


