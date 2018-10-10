""" Cisco_IOS_XR_sysadmin_vm_mgr 

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

Copyright(c) 2012\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class VM(Entity):
    """
    VM Info
    
    .. attribute:: all_locations
    
    	
    	**type**\: list of  		 :py:class:`AllLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm_mgr.VM.AllLocations>`
    
    

    """

    _prefix = 'vmmh'
    _revision = '2017-04-12'

    def __init__(self):
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


    class AllLocations(Entity):
        """
        
        
        .. attribute:: location  (key)
        
        	
        	**type**\: str
        
        .. attribute:: all_uiids
        
        	
        	**type**\: list of  		 :py:class:`AllUiids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm_mgr.VM.AllLocations.AllUiids>`
        
        

        """

        _prefix = 'vmmh'
        _revision = '2017-04-12'

        def __init__(self):
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


        class AllUiids(Entity):
            """
            
            
            .. attribute:: uiid  (key)
            
            	Unique Immutable ID
            	**type**\: str
            
            .. attribute:: id
            
            	ID of the VM
            	**type**\: str
            
            .. attribute:: status
            
            	Status of the VM
            	**type**\: str
            
            .. attribute:: ipaddr
            
            	CE IP address
            	**type**\: str
            
            .. attribute:: hb_interval_s
            
            	Heartbeat interval sec
            	**type**\: str
            
            .. attribute:: hb_interval_ns
            
            	Heartbeat interval nsec
            	**type**\: str
            
            .. attribute:: last_hb_sent
            
            	Last heartbeat sent
            	**type**\: str
            
            .. attribute:: last_hb_rec
            
            	Last heartbeat received
            	**type**\: str
            
            .. attribute:: role
            
            	ISSU role
            	**type**\: str
            
            

            """

            _prefix = 'vmmh'
            _revision = '2017-04-12'

            def __init__(self):
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
                    ('hb_interval_s', (YLeaf(YType.str, 'hb_interval_s'), ['str'])),
                    ('hb_interval_ns', (YLeaf(YType.str, 'hb_interval_ns'), ['str'])),
                    ('last_hb_sent', (YLeaf(YType.str, 'last_hb_sent'), ['str'])),
                    ('last_hb_rec', (YLeaf(YType.str, 'last_hb_rec'), ['str'])),
                    ('role', (YLeaf(YType.str, 'role'), ['str'])),
                ])
                self.uiid = None
                self.id = None
                self.status = None
                self.ipaddr = None
                self.hb_interval_s = None
                self.hb_interval_ns = None
                self.last_hb_sent = None
                self.last_hb_rec = None
                self.role = None
                self._segment_path = lambda: "all-uiids" + "[uiid='" + str(self.uiid) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(VM.AllLocations.AllUiids, ['uiid', 'id', 'status', 'ipaddr', 'hb_interval_s', 'hb_interval_ns', 'last_hb_sent', 'last_hb_rec', 'role'], name, value)

    def clone_ptr(self):
        self._top_entity = VM()
        return self._top_entity

