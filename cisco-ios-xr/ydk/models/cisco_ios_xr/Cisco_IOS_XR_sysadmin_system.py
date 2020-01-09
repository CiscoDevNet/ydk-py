""" Cisco_IOS_XR_sysadmin_system 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

This module defines the system users authentication
credentials and virtual IP that can be modified in
runtime.

Copyright(c) 2011\-2017 by Cisco Systems, Inc.
All rights reserved.

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




class Mgmt(_Entity_):
    """
    
    
    .. attribute:: ipv4
    
    	
    	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_system.Mgmt.Ipv4>`
    
    .. attribute:: ipv6
    
    	
    	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_system.Mgmt.Ipv6>`
    
    

    """

    _prefix = 'calvados_system'
    _revision = '2018-04-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Mgmt, self).__init__()
        self._top_entity = None

        self.yang_name = "mgmt"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-system"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ipv4", ("ipv4", Mgmt.Ipv4)), ("ipv6", ("ipv6", Mgmt.Ipv6))])
        self._leafs = OrderedDict()

        self.ipv4 = Mgmt.Ipv4()
        self.ipv4.parent = self
        self._children_name_map["ipv4"] = "ipv4"

        self.ipv6 = Mgmt.Ipv6()
        self.ipv6.parent = self
        self._children_name_map["ipv6"] = "ipv6"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-system:mgmt"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Mgmt, [], name, value)


    class Ipv4(_Entity_):
        """
        
        
        .. attribute:: address
        
        	
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2])))?
        
        .. attribute:: subnet_mask_ip
        
        	
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        

        """

        _prefix = 'calvados_system'
        _revision = '2018-04-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Mgmt.Ipv4, self).__init__()

            self.yang_name = "ipv4"
            self.yang_parent_name = "mgmt"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                ('subnet_mask_ip', (YLeaf(YType.str, 'subnet-mask-ip'), ['str','str'])),
            ])
            self.address = None
            self.subnet_mask_ip = None
            self._segment_path = lambda: "ipv4"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-system:mgmt/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mgmt.Ipv4, ['address', 'subnet_mask_ip'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_system as meta
            return meta._meta_table['Mgmt.Ipv4']['meta_info']


    class Ipv6(_Entity_):
        """
        
        
        .. attribute:: address
        
        	
        	**type**\: str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))?
        
        .. attribute:: prefix
        
        	
        	**type**\: int
        
        	**range:** 0..128
        
        

        """

        _prefix = 'calvados_system'
        _revision = '2018-04-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Mgmt.Ipv6, self).__init__()

            self.yang_name = "ipv6"
            self.yang_parent_name = "mgmt"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                ('prefix', (YLeaf(YType.uint8, 'prefix'), ['int'])),
            ])
            self.address = None
            self.prefix = None
            self._segment_path = lambda: "ipv6"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-system:mgmt/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mgmt.Ipv6, ['address', 'prefix'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_system as meta
            return meta._meta_table['Mgmt.Ipv6']['meta_info']

    def clone_ptr(self):
        self._top_entity = Mgmt()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_system as meta
        return meta._meta_table['Mgmt']['meta_info']


