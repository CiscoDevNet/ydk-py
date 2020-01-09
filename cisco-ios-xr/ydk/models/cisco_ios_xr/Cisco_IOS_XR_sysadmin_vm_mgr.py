""" Cisco_IOS_XR_sysadmin_vm_mgr 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

Copyright(c) 2012\-2017 by Cisco Systems, Inc.
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




class VM(_Entity_):
    """
    VM Info
    
    .. attribute:: all_locations
    
    	
    	**type**\: list of  		 :py:class:`AllLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm_mgr.VM.AllLocations>`
    
    	**config**\: False
    
    

    """

    _prefix = 'vmmh'
    _revision = '2018-07-13'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(VM, self).__init__()
        self._top_entity = None

        self.yang_name = "VM"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-vm-mgr"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("all-locations", ("all_locations", VM.AllLocations))])
        self._leafs = OrderedDict()

        self.all_locations = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-vm-mgr:VM"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(VM, [], name, value)


    class AllLocations(_Entity_):
        """
        
        
        .. attribute:: location  (key)
        
        	
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: all_uiids
        
        	
        	**type**\: list of  		 :py:class:`AllUiids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm_mgr.VM.AllLocations.AllUiids>`
        
        	**config**\: False
        
        

        """

        _prefix = 'vmmh'
        _revision = '2018-07-13'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(VM.AllLocations, self).__init__()

            self.yang_name = "all-locations"
            self.yang_parent_name = "VM"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['location']
            self._child_classes = OrderedDict([("all-uiids", ("all_uiids", VM.AllLocations.AllUiids))])
            self._leafs = OrderedDict([
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
            ])
            self.location = None

            self.all_uiids = YList(self)
            self._segment_path = lambda: "all-locations" + "[location='" + str(self.location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-vm-mgr:VM/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(VM.AllLocations, ['location'], name, value)


        class AllUiids(_Entity_):
            """
            
            
            .. attribute:: uiid  (key)
            
            	Unique Immutable ID
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: id
            
            	ID of the VM
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: status
            
            	Status of the VM
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: ipaddr
            
            	CE IP address
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: last_hb_sent
            
            	Last heartbeat sent
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: last_hb_rec
            
            	Last heartbeat received
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'vmmh'
            _revision = '2018-07-13'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(VM.AllLocations.AllUiids, self).__init__()

                self.yang_name = "all-uiids"
                self.yang_parent_name = "all-locations"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['uiid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('uiid', (YLeaf(YType.str, 'uiid'), ['str'])),
                    ('id', (YLeaf(YType.str, 'id'), ['str'])),
                    ('status', (YLeaf(YType.str, 'status'), ['str'])),
                    ('ipaddr', (YLeaf(YType.str, 'ipaddr'), ['str'])),
                    ('last_hb_sent', (YLeaf(YType.str, 'last_hb_sent'), ['str'])),
                    ('last_hb_rec', (YLeaf(YType.str, 'last_hb_rec'), ['str'])),
                ])
                self.uiid = None
                self.id = None
                self.status = None
                self.ipaddr = None
                self.last_hb_sent = None
                self.last_hb_rec = None
                self._segment_path = lambda: "all-uiids" + "[uiid='" + str(self.uiid) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(VM.AllLocations.AllUiids, ['uiid', 'id', 'status', 'ipaddr', 'last_hb_sent', 'last_hb_rec'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_vm_mgr as meta
                return meta._meta_table['VM.AllLocations.AllUiids']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_vm_mgr as meta
            return meta._meta_table['VM.AllLocations']['meta_info']

    def clone_ptr(self):
        self._top_entity = VM()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_vm_mgr as meta
        return meta._meta_table['VM']['meta_info']


