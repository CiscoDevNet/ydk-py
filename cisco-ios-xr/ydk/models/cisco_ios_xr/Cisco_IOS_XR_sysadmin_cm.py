""" Cisco_IOS_XR_sysadmin_cm 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

The System Admin Manager (CM)

Copyright(c) 2010\-2017 by Cisco Systems, Inc.
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



class AreaType(Enum):
    """
    AreaType (Enum Class)

    .. data:: SYSTEM = 0

    .. data:: RACK = 1

    .. data:: UNKNOWN = 2

    """

    SYSTEM = Enum.YLeaf(0, "SYSTEM")

    RACK = Enum.YLeaf(1, "RACK")

    UNKNOWN = Enum.YLeaf(2, "UNKNOWN")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
        return meta._meta_table['AreaType']



class NodeInventory(_Entity_):
    """
    System Admin Manager Node Inventory. All accesses are
    read\-only. CLI show command looks like show node\-inventory
    location <location>
    
    .. attribute:: summary
    
    	System Admin Manager Node Inventory. All accesses are read\-only. CLI show command looks like show node\-inventory location <location>
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.NodeInventory.Summary>`
    
    	**config**\: False
    
    .. attribute:: detail
    
    	System Admin Manager Node Inventory. All accesses are read\-only. CLI show command looks like show node\-inventory location <location>
    	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.NodeInventory.Detail>`
    
    	**config**\: False
    
    

    """

    _prefix = 'cmh'
    _revision = '2018-07-03'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(NodeInventory, self).__init__()
        self._top_entity = None

        self.yang_name = "node-inventory"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-cm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("summary", ("summary", NodeInventory.Summary)), ("detail", ("detail", NodeInventory.Detail))])
        self._leafs = OrderedDict()

        self.summary = NodeInventory.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"

        self.detail = NodeInventory.Detail()
        self.detail.parent = self
        self._children_name_map["detail"] = "detail"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-cm:node-inventory"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(NodeInventory, [], name, value)


    class Summary(_Entity_):
        """
        System Admin Manager Node Inventory. All accesses are
        read\-only. CLI show command looks like show node\-inventory
        location <location>
        
        .. attribute:: node_locations
        
        	
        	**type**\: list of  		 :py:class:`NodeLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.NodeInventory.Summary.NodeLocations>`
        
        	**config**\: False
        
        

        """

        _prefix = 'cmh'
        _revision = '2018-07-03'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(NodeInventory.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "node-inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node_locations", ("node_locations", NodeInventory.Summary.NodeLocations))])
            self._leafs = OrderedDict()

            self.node_locations = YList(self)
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-cm:node-inventory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NodeInventory.Summary, [], name, value)


        class NodeLocations(_Entity_):
            """
            
            
            .. attribute:: node_location  (key)
            
            	
            	**type**\: str
            
            	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
            
            	**config**\: False
            
            .. attribute:: nodei
            
            	
            	**type**\: list of  		 :py:class:`Nodei <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.NodeInventory.Summary.NodeLocations.Nodei>`
            
            	**config**\: False
            
            

            """

            _prefix = 'cmh'
            _revision = '2018-07-03'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(NodeInventory.Summary.NodeLocations, self).__init__()

                self.yang_name = "node_locations"
                self.yang_parent_name = "summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_location']
                self._child_classes = OrderedDict([("nodei", ("nodei", NodeInventory.Summary.NodeLocations.Nodei))])
                self._leafs = OrderedDict([
                    ('node_location', (YLeaf(YType.str, 'node_location'), ['str'])),
                ])
                self.node_location = None

                self.nodei = YList(self)
                self._segment_path = lambda: "node_locations" + "[node_location='" + str(self.node_location) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-cm:node-inventory/summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NodeInventory.Summary.NodeLocations, ['node_location'], name, value)


            class Nodei(_Entity_):
                """
                
                
                .. attribute:: ip_address  (key)
                
                	IP address of the node
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: type
                
                	Node Type
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: mac_address
                
                	Node MAC
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                	**config**\: False
                
                .. attribute:: card_serial
                
                	Card serial# the node belongs to
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: nti
                
                	Node NTI
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'cmh'
                _revision = '2018-07-03'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(NodeInventory.Summary.NodeLocations.Nodei, self).__init__()

                    self.yang_name = "nodei"
                    self.yang_parent_name = "node_locations"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['ip_address']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ip_address', (YLeaf(YType.str, 'ip_address'), ['str','str'])),
                        ('type', (YLeaf(YType.str, 'type'), ['str'])),
                        ('mac_address', (YLeaf(YType.str, 'mac_address'), ['str'])),
                        ('card_serial', (YLeaf(YType.str, 'card_serial'), ['str'])),
                        ('nti', (YLeaf(YType.uint32, 'nti'), ['int'])),
                    ])
                    self.ip_address = None
                    self.type = None
                    self.mac_address = None
                    self.card_serial = None
                    self.nti = None
                    self._segment_path = lambda: "nodei" + "[ip_address='" + str(self.ip_address) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(NodeInventory.Summary.NodeLocations.Nodei, ['ip_address', 'type', 'mac_address', 'card_serial', 'nti'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
                    return meta._meta_table['NodeInventory.Summary.NodeLocations.Nodei']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
                return meta._meta_table['NodeInventory.Summary.NodeLocations']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
            return meta._meta_table['NodeInventory.Summary']['meta_info']


    class Detail(_Entity_):
        """
        System Admin Manager Node Inventory. All accesses are
        read\-only. CLI show command looks like show node\-inventory
        location <location>
        
        .. attribute:: node_locations
        
        	
        	**type**\: list of  		 :py:class:`NodeLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.NodeInventory.Detail.NodeLocations>`
        
        	**config**\: False
        
        

        """

        _prefix = 'cmh'
        _revision = '2018-07-03'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(NodeInventory.Detail, self).__init__()

            self.yang_name = "detail"
            self.yang_parent_name = "node-inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node_locations", ("node_locations", NodeInventory.Detail.NodeLocations))])
            self._leafs = OrderedDict()

            self.node_locations = YList(self)
            self._segment_path = lambda: "detail"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-cm:node-inventory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NodeInventory.Detail, [], name, value)


        class NodeLocations(_Entity_):
            """
            
            
            .. attribute:: node_location  (key)
            
            	
            	**type**\: str
            
            	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
            
            	**config**\: False
            
            .. attribute:: nodei
            
            	
            	**type**\: list of  		 :py:class:`Nodei <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.NodeInventory.Detail.NodeLocations.Nodei>`
            
            	**config**\: False
            
            

            """

            _prefix = 'cmh'
            _revision = '2018-07-03'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(NodeInventory.Detail.NodeLocations, self).__init__()

                self.yang_name = "node_locations"
                self.yang_parent_name = "detail"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_location']
                self._child_classes = OrderedDict([("nodei", ("nodei", NodeInventory.Detail.NodeLocations.Nodei))])
                self._leafs = OrderedDict([
                    ('node_location', (YLeaf(YType.str, 'node_location'), ['str'])),
                ])
                self.node_location = None

                self.nodei = YList(self)
                self._segment_path = lambda: "node_locations" + "[node_location='" + str(self.node_location) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-cm:node-inventory/detail/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NodeInventory.Detail.NodeLocations, ['node_location'], name, value)


            class Nodei(_Entity_):
                """
                
                
                .. attribute:: ip_address  (key)
                
                	IP address of the node
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: type
                
                	Node Type
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: mac_address
                
                	Node MAC
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                	**config**\: False
                
                .. attribute:: card_serial
                
                	Card serial# the node belongs to
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: nti
                
                	Node NTI
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: restart
                
                	Node in Restart
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: data
                
                	Node Data
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: sdr
                
                	SDR Name the node belongs to
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'cmh'
                _revision = '2018-07-03'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(NodeInventory.Detail.NodeLocations.Nodei, self).__init__()

                    self.yang_name = "nodei"
                    self.yang_parent_name = "node_locations"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['ip_address']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ip_address', (YLeaf(YType.str, 'ip_address'), ['str','str'])),
                        ('type', (YLeaf(YType.str, 'type'), ['str'])),
                        ('mac_address', (YLeaf(YType.str, 'mac_address'), ['str'])),
                        ('card_serial', (YLeaf(YType.str, 'card_serial'), ['str'])),
                        ('nti', (YLeaf(YType.uint32, 'nti'), ['int'])),
                        ('restart', (YLeaf(YType.boolean, 'restart'), ['bool'])),
                        ('data', (YLeaf(YType.str, 'data'), ['str'])),
                        ('sdr', (YLeaf(YType.str, 'sdr'), ['str'])),
                    ])
                    self.ip_address = None
                    self.type = None
                    self.mac_address = None
                    self.card_serial = None
                    self.nti = None
                    self.restart = None
                    self.data = None
                    self.sdr = None
                    self._segment_path = lambda: "nodei" + "[ip_address='" + str(self.ip_address) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(NodeInventory.Detail.NodeLocations.Nodei, ['ip_address', 'type', 'mac_address', 'card_serial', 'nti', 'restart', 'data', 'sdr'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
                    return meta._meta_table['NodeInventory.Detail.NodeLocations.Nodei']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
                return meta._meta_table['NodeInventory.Detail.NodeLocations']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
            return meta._meta_table['NodeInventory.Detail']['meta_info']

    def clone_ptr(self):
        self._top_entity = NodeInventory()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
        return meta._meta_table['NodeInventory']['meta_info']


class CardInventory(_Entity_):
    """
    System Admin Manager Card Inventory. All accesses are
    read\-only. CLI show command looks like show card\-inventory
    location <location>
    
    .. attribute:: card_locations
    
    	
    	**type**\: list of  		 :py:class:`CardLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.CardInventory.CardLocations>`
    
    	**config**\: False
    
    

    """

    _prefix = 'cmh'
    _revision = '2018-07-03'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(CardInventory, self).__init__()
        self._top_entity = None

        self.yang_name = "card-inventory"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-cm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("card_locations", ("card_locations", CardInventory.CardLocations))])
        self._leafs = OrderedDict()

        self.card_locations = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-cm:card-inventory"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CardInventory, [], name, value)


    class CardLocations(_Entity_):
        """
        
        
        .. attribute:: card_location  (key)
        
        	
        	**type**\: str
        
        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
        
        	**config**\: False
        
        .. attribute:: cardi
        
        	
        	**type**\: list of  		 :py:class:`Cardi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.CardInventory.CardLocations.Cardi>`
        
        	**config**\: False
        
        

        """

        _prefix = 'cmh'
        _revision = '2018-07-03'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(CardInventory.CardLocations, self).__init__()

            self.yang_name = "card_locations"
            self.yang_parent_name = "card-inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['card_location']
            self._child_classes = OrderedDict([("cardi", ("cardi", CardInventory.CardLocations.Cardi))])
            self._leafs = OrderedDict([
                ('card_location', (YLeaf(YType.str, 'card_location'), ['str'])),
            ])
            self.card_location = None

            self.cardi = YList(self)
            self._segment_path = lambda: "card_locations" + "[card_location='" + str(self.card_location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-cm:card-inventory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CardInventory.CardLocations, ['card_location'], name, value)


        class Cardi(_Entity_):
            """
            
            
            .. attribute:: card_serial  (key)
            
            	Serial Number of the Card
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: node_id
            
            	Node name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: card_type
            
            	Card Type
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: hw_state
            
            	Card State
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: sw_state
            
            	Card Software State
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: slot
            
            	Card Slot Number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cti
            
            	Card CTI
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'cmh'
            _revision = '2018-07-03'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(CardInventory.CardLocations.Cardi, self).__init__()

                self.yang_name = "cardi"
                self.yang_parent_name = "card_locations"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['card_serial']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('card_serial', (YLeaf(YType.str, 'card_serial'), ['str'])),
                    ('node_id', (YLeaf(YType.str, 'node_id'), ['str'])),
                    ('card_type', (YLeaf(YType.str, 'card_type'), ['str'])),
                    ('hw_state', (YLeaf(YType.str, 'hw_state'), ['str'])),
                    ('sw_state', (YLeaf(YType.str, 'sw_state'), ['str'])),
                    ('slot', (YLeaf(YType.uint32, 'slot'), ['int'])),
                    ('cti', (YLeaf(YType.uint32, 'cti'), ['int'])),
                ])
                self.card_serial = None
                self.node_id = None
                self.card_type = None
                self.hw_state = None
                self.sw_state = None
                self.slot = None
                self.cti = None
                self._segment_path = lambda: "cardi" + "[card_serial='" + str(self.card_serial) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CardInventory.CardLocations.Cardi, ['card_serial', 'node_id', 'card_type', 'hw_state', 'sw_state', 'slot', 'cti'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
                return meta._meta_table['CardInventory.CardLocations.Cardi']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
            return meta._meta_table['CardInventory.CardLocations']['meta_info']

    def clone_ptr(self):
        self._top_entity = CardInventory()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
        return meta._meta_table['CardInventory']['meta_info']


class RackInventory(_Entity_):
    """
    System Admin Manager Rack Inventory
    
    .. attribute:: rack_locations
    
    	
    	**type**\: list of  		 :py:class:`RackLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.RackInventory.RackLocations>`
    
    	**config**\: False
    
    

    """

    _prefix = 'cmh'
    _revision = '2018-07-03'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(RackInventory, self).__init__()
        self._top_entity = None

        self.yang_name = "rack-inventory"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-cm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("rack_locations", ("rack_locations", RackInventory.RackLocations))])
        self._leafs = OrderedDict()

        self.rack_locations = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-cm:rack-inventory"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(RackInventory, [], name, value)


    class RackLocations(_Entity_):
        """
        
        
        .. attribute:: rack_location  (key)
        
        	
        	**type**\: str
        
        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
        
        	**config**\: False
        
        .. attribute:: racki
        
        	
        	**type**\: list of  		 :py:class:`Racki <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.RackInventory.RackLocations.Racki>`
        
        	**config**\: False
        
        

        """

        _prefix = 'cmh'
        _revision = '2018-07-03'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(RackInventory.RackLocations, self).__init__()

            self.yang_name = "rack_locations"
            self.yang_parent_name = "rack-inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['rack_location']
            self._child_classes = OrderedDict([("racki", ("racki", RackInventory.RackLocations.Racki))])
            self._leafs = OrderedDict([
                ('rack_location', (YLeaf(YType.str, 'rack_location'), ['str'])),
            ])
            self.rack_location = None

            self.racki = YList(self)
            self._segment_path = lambda: "rack_locations" + "[rack_location='" + str(self.rack_location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-cm:rack-inventory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RackInventory.RackLocations, ['rack_location'], name, value)


        class Racki(_Entity_):
            """
            
            
            .. attribute:: rack_serial  (key)
            
            	Serial Number of the Rack
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rack_number
            
            	Rack Number
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: rack_state
            
            	Rack State
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'cmh'
            _revision = '2018-07-03'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(RackInventory.RackLocations.Racki, self).__init__()

                self.yang_name = "racki"
                self.yang_parent_name = "rack_locations"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['rack_serial']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rack_serial', (YLeaf(YType.str, 'rack_serial'), ['str'])),
                    ('rack_number', (YLeaf(YType.int32, 'rack_number'), ['int'])),
                    ('rack_state', (YLeaf(YType.int32, 'rack_state'), ['int'])),
                ])
                self.rack_serial = None
                self.rack_number = None
                self.rack_state = None
                self._segment_path = lambda: "racki" + "[rack_serial='" + str(self.rack_serial) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RackInventory.RackLocations.Racki, ['rack_serial', 'rack_number', 'rack_state'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
                return meta._meta_table['RackInventory.RackLocations.Racki']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
            return meta._meta_table['RackInventory.RackLocations']['meta_info']

    def clone_ptr(self):
        self._top_entity = RackInventory()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
        return meta._meta_table['RackInventory']['meta_info']


class SystemServiceInventory(_Entity_):
    """
    System Admin Manager System Services Inventory
    
    .. attribute:: ssvc_locations
    
    	
    	**type**\: list of  		 :py:class:`SsvcLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.SystemServiceInventory.SsvcLocations>`
    
    	**config**\: False
    
    

    """

    _prefix = 'cmh'
    _revision = '2018-07-03'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(SystemServiceInventory, self).__init__()
        self._top_entity = None

        self.yang_name = "system-service-inventory"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-cm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ssvc_locations", ("ssvc_locations", SystemServiceInventory.SsvcLocations))])
        self._leafs = OrderedDict()

        self.ssvc_locations = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-cm:system-service-inventory"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SystemServiceInventory, [], name, value)


    class SsvcLocations(_Entity_):
        """
        
        
        .. attribute:: ssvc_location  (key)
        
        	
        	**type**\: str
        
        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
        
        	**config**\: False
        
        .. attribute:: ssvci
        
        	
        	**type**\: list of  		 :py:class:`Ssvci <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.SystemServiceInventory.SsvcLocations.Ssvci>`
        
        	**config**\: False
        
        

        """

        _prefix = 'cmh'
        _revision = '2018-07-03'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SystemServiceInventory.SsvcLocations, self).__init__()

            self.yang_name = "ssvc_locations"
            self.yang_parent_name = "system-service-inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['ssvc_location']
            self._child_classes = OrderedDict([("ssvci", ("ssvci", SystemServiceInventory.SsvcLocations.Ssvci))])
            self._leafs = OrderedDict([
                ('ssvc_location', (YLeaf(YType.str, 'ssvc_location'), ['str'])),
            ])
            self.ssvc_location = None

            self.ssvci = YList(self)
            self._segment_path = lambda: "ssvc_locations" + "[ssvc_location='" + str(self.ssvc_location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-cm:system-service-inventory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SystemServiceInventory.SsvcLocations, ['ssvc_location'], name, value)


        class Ssvci(_Entity_):
            """
            
            
            .. attribute:: svc_name  (key)
            
            	Service Name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: placement_first
            
            	Serial Number of the first card selected
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: nodeid_first
            
            	Node id of the first card selected
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: placement_second
            
            	Serial Number of the second card selected
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: nodeid_second
            
            	Node id of the second card selected
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: svc_load
            
            	Service Load
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'cmh'
            _revision = '2018-07-03'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SystemServiceInventory.SsvcLocations.Ssvci, self).__init__()

                self.yang_name = "ssvci"
                self.yang_parent_name = "ssvc_locations"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['svc_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('svc_name', (YLeaf(YType.str, 'svc_name'), ['str'])),
                    ('placement_first', (YLeaf(YType.str, 'placement_first'), ['str'])),
                    ('nodeid_first', (YLeaf(YType.str, 'nodeid_first'), ['str'])),
                    ('placement_second', (YLeaf(YType.str, 'placement_second'), ['str'])),
                    ('nodeid_second', (YLeaf(YType.str, 'nodeid_second'), ['str'])),
                    ('svc_load', (YLeaf(YType.uint8, 'svc_load'), ['int'])),
                ])
                self.svc_name = None
                self.placement_first = None
                self.nodeid_first = None
                self.placement_second = None
                self.nodeid_second = None
                self.svc_load = None
                self._segment_path = lambda: "ssvci" + "[svc_name='" + str(self.svc_name) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SystemServiceInventory.SsvcLocations.Ssvci, ['svc_name', 'placement_first', 'nodeid_first', 'placement_second', 'nodeid_second', 'svc_load'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
                return meta._meta_table['SystemServiceInventory.SsvcLocations.Ssvci']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
            return meta._meta_table['SystemServiceInventory.SsvcLocations']['meta_info']

    def clone_ptr(self):
        self._top_entity = SystemServiceInventory()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
        return meta._meta_table['SystemServiceInventory']['meta_info']


class RackServiceInventory(_Entity_):
    """
    System Admin Manager Rack Services Inventory
    
    .. attribute:: rsvc_locations
    
    	
    	**type**\: list of  		 :py:class:`RsvcLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.RackServiceInventory.RsvcLocations>`
    
    	**config**\: False
    
    

    """

    _prefix = 'cmh'
    _revision = '2018-07-03'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(RackServiceInventory, self).__init__()
        self._top_entity = None

        self.yang_name = "rack-service-inventory"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-cm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("rsvc_locations", ("rsvc_locations", RackServiceInventory.RsvcLocations))])
        self._leafs = OrderedDict()

        self.rsvc_locations = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-cm:rack-service-inventory"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(RackServiceInventory, [], name, value)


    class RsvcLocations(_Entity_):
        """
        
        
        .. attribute:: rsvc_location  (key)
        
        	
        	**type**\: str
        
        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
        
        	**config**\: False
        
        .. attribute:: rsvci
        
        	
        	**type**\: list of  		 :py:class:`Rsvci <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.RackServiceInventory.RsvcLocations.Rsvci>`
        
        	**config**\: False
        
        

        """

        _prefix = 'cmh'
        _revision = '2018-07-03'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(RackServiceInventory.RsvcLocations, self).__init__()

            self.yang_name = "rsvc_locations"
            self.yang_parent_name = "rack-service-inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['rsvc_location']
            self._child_classes = OrderedDict([("rsvci", ("rsvci", RackServiceInventory.RsvcLocations.Rsvci))])
            self._leafs = OrderedDict([
                ('rsvc_location', (YLeaf(YType.str, 'rsvc_location'), ['str'])),
            ])
            self.rsvc_location = None

            self.rsvci = YList(self)
            self._segment_path = lambda: "rsvc_locations" + "[rsvc_location='" + str(self.rsvc_location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-cm:rack-service-inventory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RackServiceInventory.RsvcLocations, ['rsvc_location'], name, value)


        class Rsvci(_Entity_):
            """
            
            
            .. attribute:: svc_name  (key)
            
            	Service Name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: placement_first
            
            	Serial Number of the first card selected
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: nodeid_first
            
            	Node id of the first card selected
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: placement_second
            
            	Serial Number of the second card selected
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: nodeid_second
            
            	Node id of the second card selected
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: svc_load
            
            	Service Load
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'cmh'
            _revision = '2018-07-03'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(RackServiceInventory.RsvcLocations.Rsvci, self).__init__()

                self.yang_name = "rsvci"
                self.yang_parent_name = "rsvc_locations"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['svc_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('svc_name', (YLeaf(YType.str, 'svc_name'), ['str'])),
                    ('placement_first', (YLeaf(YType.str, 'placement_first'), ['str'])),
                    ('nodeid_first', (YLeaf(YType.str, 'nodeid_first'), ['str'])),
                    ('placement_second', (YLeaf(YType.str, 'placement_second'), ['str'])),
                    ('nodeid_second', (YLeaf(YType.str, 'nodeid_second'), ['str'])),
                    ('svc_load', (YLeaf(YType.uint8, 'svc_load'), ['int'])),
                ])
                self.svc_name = None
                self.placement_first = None
                self.nodeid_first = None
                self.placement_second = None
                self.nodeid_second = None
                self.svc_load = None
                self._segment_path = lambda: "rsvci" + "[svc_name='" + str(self.svc_name) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RackServiceInventory.RsvcLocations.Rsvci, ['svc_name', 'placement_first', 'nodeid_first', 'placement_second', 'nodeid_second', 'svc_load'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
                return meta._meta_table['RackServiceInventory.RsvcLocations.Rsvci']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
            return meta._meta_table['RackServiceInventory.RsvcLocations']['meta_info']

    def clone_ptr(self):
        self._top_entity = RackServiceInventory()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
        return meta._meta_table['RackServiceInventory']['meta_info']


class SdrInventory(_Entity_):
    """
    System Admin Manager SDR Inventory
    
    .. attribute:: sdr_locations
    
    	
    	**type**\: list of  		 :py:class:`SdrLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.SdrInventory.SdrLocations>`
    
    	**config**\: False
    
    

    """

    _prefix = 'cmh'
    _revision = '2018-07-03'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(SdrInventory, self).__init__()
        self._top_entity = None

        self.yang_name = "sdr-inventory"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-cm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("sdr_locations", ("sdr_locations", SdrInventory.SdrLocations))])
        self._leafs = OrderedDict()

        self.sdr_locations = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-cm:sdr-inventory"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SdrInventory, [], name, value)


    class SdrLocations(_Entity_):
        """
        
        
        .. attribute:: sdr_location  (key)
        
        	
        	**type**\: str
        
        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
        
        	**config**\: False
        
        .. attribute:: sdri
        
        	
        	**type**\: list of  		 :py:class:`Sdri <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.SdrInventory.SdrLocations.Sdri>`
        
        	**config**\: False
        
        

        """

        _prefix = 'cmh'
        _revision = '2018-07-03'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SdrInventory.SdrLocations, self).__init__()

            self.yang_name = "sdr_locations"
            self.yang_parent_name = "sdr-inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['sdr_location']
            self._child_classes = OrderedDict([("sdri", ("sdri", SdrInventory.SdrLocations.Sdri))])
            self._leafs = OrderedDict([
                ('sdr_location', (YLeaf(YType.str, 'sdr_location'), ['str'])),
            ])
            self.sdr_location = None

            self.sdri = YList(self)
            self._segment_path = lambda: "sdr_locations" + "[sdr_location='" + str(self.sdr_location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-cm:sdr-inventory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SdrInventory.SdrLocations, ['sdr_location'], name, value)


        class Sdri(_Entity_):
            """
            
            
            .. attribute:: sdr_name  (key)
            
            	SDR NAME
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: sdr_id
            
            	SDR ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sdr_vlan_baseid
            
            	SDR VLAN ID
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: sdr_version
            
            	SDR Image Version
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'cmh'
            _revision = '2018-07-03'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SdrInventory.SdrLocations.Sdri, self).__init__()

                self.yang_name = "sdri"
                self.yang_parent_name = "sdr_locations"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['sdr_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('sdr_name', (YLeaf(YType.str, 'sdr_name'), ['str'])),
                    ('sdr_id', (YLeaf(YType.uint32, 'sdr_id'), ['int'])),
                    ('sdr_vlan_baseid', (YLeaf(YType.uint8, 'sdr_vlan_baseid'), ['int'])),
                    ('sdr_version', (YLeaf(YType.uint64, 'sdr_version'), ['int'])),
                ])
                self.sdr_name = None
                self.sdr_id = None
                self.sdr_vlan_baseid = None
                self.sdr_version = None
                self._segment_path = lambda: "sdri" + "[sdr_name='" + str(self.sdr_name) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SdrInventory.SdrLocations.Sdri, ['sdr_name', 'sdr_id', 'sdr_vlan_baseid', 'sdr_version'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
                return meta._meta_table['SdrInventory.SdrLocations.Sdri']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
            return meta._meta_table['SdrInventory.SdrLocations']['meta_info']

    def clone_ptr(self):
        self._top_entity = SdrInventory()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
        return meta._meta_table['SdrInventory']['meta_info']


class LeaderStatistics(_Entity_):
    """
    System Admin Manager Leader Statistics
    
    .. attribute:: ldr_locations
    
    	
    	**type**\: list of  		 :py:class:`LdrLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.LeaderStatistics.LdrLocations>`
    
    	**config**\: False
    
    

    """

    _prefix = 'cmh'
    _revision = '2018-07-03'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(LeaderStatistics, self).__init__()
        self._top_entity = None

        self.yang_name = "leader-statistics"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-cm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ldr_locations", ("ldr_locations", LeaderStatistics.LdrLocations))])
        self._leafs = OrderedDict()

        self.ldr_locations = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-cm:leader-statistics"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(LeaderStatistics, [], name, value)


    class LdrLocations(_Entity_):
        """
        
        
        .. attribute:: ldr_location  (key)
        
        	
        	**type**\: str
        
        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
        
        	**config**\: False
        
        .. attribute:: syslead
        
        	Primary System Leader
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: bkup_syslead
        
        	Backup System Leader
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: racklead
        
        	Primary Rack Leader
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: bkup_racklead
        
        	Backup Rack Leader
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: l1_dis
        
        	L1 DIS
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: l2_dis
        
        	L2 DIS
        	**type**\: str
        
        	**config**\: False
        
        

        """

        _prefix = 'cmh'
        _revision = '2018-07-03'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(LeaderStatistics.LdrLocations, self).__init__()

            self.yang_name = "ldr_locations"
            self.yang_parent_name = "leader-statistics"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['ldr_location']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ldr_location', (YLeaf(YType.str, 'ldr_location'), ['str'])),
                ('syslead', (YLeaf(YType.str, 'syslead'), ['str'])),
                ('bkup_syslead', (YLeaf(YType.str, 'bkup_syslead'), ['str'])),
                ('racklead', (YLeaf(YType.str, 'racklead'), ['str'])),
                ('bkup_racklead', (YLeaf(YType.str, 'bkup_racklead'), ['str'])),
                ('l1_dis', (YLeaf(YType.str, 'l1_dis'), ['str'])),
                ('l2_dis', (YLeaf(YType.str, 'l2_dis'), ['str'])),
            ])
            self.ldr_location = None
            self.syslead = None
            self.bkup_syslead = None
            self.racklead = None
            self.bkup_racklead = None
            self.l1_dis = None
            self.l2_dis = None
            self._segment_path = lambda: "ldr_locations" + "[ldr_location='" + str(self.ldr_location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-cm:leader-statistics/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LeaderStatistics.LdrLocations, ['ldr_location', 'syslead', 'bkup_syslead', 'racklead', 'bkup_racklead', 'l1_dis', 'l2_dis'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
            return meta._meta_table['LeaderStatistics.LdrLocations']['meta_info']

    def clone_ptr(self):
        self._top_entity = LeaderStatistics()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
        return meta._meta_table['LeaderStatistics']['meta_info']


class TopologyNeighbors(_Entity_):
    """
    System Admin Manager Neighbors of a location
    
    .. attribute:: nbr_locations
    
    	
    	**type**\: list of  		 :py:class:`NbrLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.TopologyNeighbors.NbrLocations>`
    
    	**config**\: False
    
    

    """

    _prefix = 'cmh'
    _revision = '2018-07-03'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(TopologyNeighbors, self).__init__()
        self._top_entity = None

        self.yang_name = "topology-neighbors"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-cm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nbr_locations", ("nbr_locations", TopologyNeighbors.NbrLocations))])
        self._leafs = OrderedDict()

        self.nbr_locations = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-cm:topology-neighbors"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(TopologyNeighbors, [], name, value)


    class NbrLocations(_Entity_):
        """
        
        
        .. attribute:: nbr_location  (key)
        
        	
        	**type**\: str
        
        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
        
        	**config**\: False
        
        .. attribute:: nbri
        
        	
        	**type**\: list of  		 :py:class:`Nbri <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_cm.TopologyNeighbors.NbrLocations.Nbri>`
        
        	**config**\: False
        
        

        """

        _prefix = 'cmh'
        _revision = '2018-07-03'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(TopologyNeighbors.NbrLocations, self).__init__()

            self.yang_name = "nbr_locations"
            self.yang_parent_name = "topology-neighbors"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['nbr_location']
            self._child_classes = OrderedDict([("nbri", ("nbri", TopologyNeighbors.NbrLocations.Nbri))])
            self._leafs = OrderedDict([
                ('nbr_location', (YLeaf(YType.str, 'nbr_location'), ['str'])),
            ])
            self.nbr_location = None

            self.nbri = YList(self)
            self._segment_path = lambda: "nbr_locations" + "[nbr_location='" + str(self.nbr_location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-cm:topology-neighbors/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TopologyNeighbors.NbrLocations, ['nbr_location'], name, value)


        class Nbri(_Entity_):
            """
            
            
            .. attribute:: nbr_system_id  (key)
            
            	Neighbor System ID
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: nbr_area_type  (key)
            
            	Neighbor Area Type
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: nbr_interface
            
            	Adjacency Interface
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: nbr_state
            
            	Neighbor State
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: nbr_holdtime
            
            	Neighbor Hold Time
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: nbr_uptime
            
            	Neighbor Up Time
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'cmh'
            _revision = '2018-07-03'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(TopologyNeighbors.NbrLocations.Nbri, self).__init__()

                self.yang_name = "nbri"
                self.yang_parent_name = "nbr_locations"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['nbr_system_id','nbr_area_type']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('nbr_system_id', (YLeaf(YType.str, 'nbr_system_id'), ['str'])),
                    ('nbr_area_type', (YLeaf(YType.str, 'nbr_area_type'), ['str'])),
                    ('nbr_interface', (YLeaf(YType.str, 'nbr_interface'), ['str'])),
                    ('nbr_state', (YLeaf(YType.str, 'nbr_state'), ['str'])),
                    ('nbr_holdtime', (YLeaf(YType.uint64, 'nbr_holdtime'), ['int'])),
                    ('nbr_uptime', (YLeaf(YType.str, 'nbr_uptime'), ['str'])),
                ])
                self.nbr_system_id = None
                self.nbr_area_type = None
                self.nbr_interface = None
                self.nbr_state = None
                self.nbr_holdtime = None
                self.nbr_uptime = None
                self._segment_path = lambda: "nbri" + "[nbr_system_id='" + str(self.nbr_system_id) + "']" + "[nbr_area_type='" + str(self.nbr_area_type) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TopologyNeighbors.NbrLocations.Nbri, ['nbr_system_id', 'nbr_area_type', 'nbr_interface', 'nbr_state', 'nbr_holdtime', 'nbr_uptime'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
                return meta._meta_table['TopologyNeighbors.NbrLocations.Nbri']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
            return meta._meta_table['TopologyNeighbors.NbrLocations']['meta_info']

    def clone_ptr(self):
        self._top_entity = TopologyNeighbors()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
        return meta._meta_table['TopologyNeighbors']['meta_info']


class Placement(_Entity_):
    """
    
    
    

    """

    _prefix = 'cmh'
    _revision = '2018-07-03'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Placement, self).__init__()
        self._top_entity = None

        self.yang_name = "placement"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-cm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-cm:placement"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = Placement()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_cm as meta
        return meta._meta_table['Placement']['meta_info']


