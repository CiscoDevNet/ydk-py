""" Cisco_IOS_XR_sysadmin_sdr_connect 

This module implements entities for inter sdr connect
feature

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SdrConnect(Entity):
    """
    
    
    .. attribute:: connect
    
    	Connect two Secure Domain Routers
    	**type**\:  :py:class:`Connect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_connect.SdrConnect.Connect>`
    
    

    """

    _prefix = 'inter_sdr_connect'
    _revision = '2017-10-09'

    def __init__(self):
        super(SdrConnect, self).__init__()
        self._top_entity = None

        self.yang_name = "sdr-connect"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-sdr-connect"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("connect", ("connect", SdrConnect.Connect))])
        self._leafs = OrderedDict()

        self.connect = SdrConnect.Connect()
        self.connect.parent = self
        self._children_name_map["connect"] = "connect"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-sdr-connect:sdr-connect"

    def __setattr__(self, name, value):
        self._perform_setattr(SdrConnect, [], name, value)


    class Connect(Entity):
        """
        Connect two Secure Domain Routers
        
        .. attribute:: sdr
        
        	Secure Domain Router connect config
        	**type**\: list of  		 :py:class:`Sdr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_sdr_connect.SdrConnect.Connect.Sdr>`
        
        

        """

        _prefix = 'inter_sdr_connect'
        _revision = '2017-10-09'

        def __init__(self):
            super(SdrConnect.Connect, self).__init__()

            self.yang_name = "connect"
            self.yang_parent_name = "sdr-connect"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("sdr", ("sdr", SdrConnect.Connect.Sdr))])
            self._leafs = OrderedDict()

            self.sdr = YList(self)
            self._segment_path = lambda: "connect"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdr-connect:sdr-connect/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SdrConnect.Connect, [], name, value)


        class Sdr(Entity):
            """
            Secure Domain Router connect config
            
            .. attribute:: sdr_name  (key)
            
            	Name of the Secure Domain Router , 30 max characters
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9\_\-]{1,30}
            
            	**mandatory**\: True
            
            .. attribute:: remote_sdr_name  (key)
            
            	Name of the Remote Secure Domain Router , 30 max characters
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9\_\-]{1,30}
            
            	**mandatory**\: True
            
            .. attribute:: csi_id  (key)
            
            	Index unique for each SDR connection pair
            	**type**\: int
            
            	**range:** 1..15
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'inter_sdr_connect'
            _revision = '2017-10-09'

            def __init__(self):
                super(SdrConnect.Connect.Sdr, self).__init__()

                self.yang_name = "sdr"
                self.yang_parent_name = "connect"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['sdr_name','remote_sdr_name','csi_id']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('sdr_name', YLeaf(YType.str, 'sdr-name')),
                    ('remote_sdr_name', YLeaf(YType.str, 'remote-sdr-name')),
                    ('csi_id', YLeaf(YType.uint32, 'csi-id')),
                ])
                self.sdr_name = None
                self.remote_sdr_name = None
                self.csi_id = None
                self._segment_path = lambda: "sdr" + "[sdr-name='" + str(self.sdr_name) + "']" + "[remote-sdr-name='" + str(self.remote_sdr_name) + "']" + "[csi-id='" + str(self.csi_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-sdr-connect:sdr-connect/connect/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SdrConnect.Connect.Sdr, ['sdr_name', 'remote_sdr_name', 'csi_id'], name, value)

    def clone_ptr(self):
        self._top_entity = SdrConnect()
        return self._top_entity

