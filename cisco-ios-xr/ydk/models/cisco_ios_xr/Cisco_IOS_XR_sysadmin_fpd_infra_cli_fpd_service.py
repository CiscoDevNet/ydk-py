""" Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd_service 

This module contains definitions
for the Calvados model objects.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Location(_Entity_):
    """
    
    
    .. attribute:: loc  (key)
    
    	
    	**type**\: str
    
    	**config**\: False
    
    .. attribute:: fpd2
    
    	
    	**type**\: list of  		 :py:class:`Fpd2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd_service.Location.Fpd2>`
    
    	**config**\: False
    
    

    """

    _prefix = 'upgrade'
    _revision = '2017-05-01'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Location, self).__init__()
        self._top_entity = None

        self.yang_name = "location"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd-service"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = ['loc']
        self._child_classes = OrderedDict([("fpd2", ("fpd2", Location.Fpd2))])
        self._leafs = OrderedDict([
            ('loc', (YLeaf(YType.str, 'loc'), ['str'])),
        ])
        self.loc = None

        self.fpd2 = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd-service:location" + "[loc='" + str(self.loc) + "']"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Location, ['loc'], name, value)


    class Fpd2(_Entity_):
        """
        
        
        .. attribute:: name  (key)
        
        	
        	**type**\: str
        
        	**config**\: False
        
        

        """

        _prefix = 'upgrade'
        _revision = '2017-05-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Location.Fpd2, self).__init__()

            self.yang_name = "fpd2"
            self.yang_parent_name = "location"
            self.is_top_level_class = False
            self.has_list_ancestor = True
            self.ylist_key_names = ['name']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
            ])
            self.name = None
            self._segment_path = lambda: "fpd2" + "[name='" + str(self.name) + "']"
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Location.Fpd2, ['name'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd_service as meta
            return meta._meta_table['Location.Fpd2']['meta_info']

    def clone_ptr(self):
        self._top_entity = Location()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd_service as meta
        return meta._meta_table['Location']['meta_info']


