""" Cisco_IOS_XR_sysadmin_controllers_ncs5501 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

This module defines the top level container for
all hardware devices managed in Sysadmin.

Copyright(c) 2015\-2016 by Cisco Systems, Inc.
All rights reserved.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Controller(Entity):
    """
    
    
    .. attribute:: fabric
    
    	Fabric resource commands
    	**type**\:  :py:class:`Fabric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric>`
    
    .. attribute:: card_mgr
    
    	
    	**type**\:  :py:class:`CardMgr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr>`
    
    

    """

    _prefix = 'calvados_controllers'
    _revision = '2017-10-11'

    def __init__(self):
        super(Controller, self).__init__()
        self._top_entity = None

        self.yang_name = "controller"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-controllers-ncs5501"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("fabric", ("fabric", Controller.Fabric)), ("card_mgr", ("card_mgr", Controller.CardMgr))])
        self._leafs = OrderedDict()

        self.fabric = Controller.Fabric()
        self.fabric.parent = self
        self._children_name_map["fabric"] = "fabric"

        self.card_mgr = Controller.CardMgr()
        self.card_mgr.parent = self
        self._children_name_map["card_mgr"] = "card_mgr"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Controller, [], name, value)


    class Fabric(Entity):
        """
        Fabric resource commands
        
        .. attribute:: oper
        
        	
        	**type**\:  :py:class:`Oper <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper>`
        
        	**config**\: False
        
        

        """

        _prefix = 'calvados_controllers'
        _revision = '2017-10-11'

        def __init__(self):
            super(Controller.Fabric, self).__init__()

            self.yang_name = "fabric"
            self.yang_parent_name = "controller"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("oper", ("oper", Controller.Fabric.Oper))])
            self._leafs = OrderedDict()

            self.oper = Controller.Fabric.Oper()
            self.oper.parent = self
            self._children_name_map["oper"] = "oper"
            self._segment_path = lambda: "fabric"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Controller.Fabric, [], name, value)


        class Oper(Entity):
            """
            
            
            .. attribute:: fgid
            
            	FGID management information
            	**type**\:  :py:class:`Fgid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid>`
            
            	**config**\: False
            
            

            """

            _prefix = 'calvados_controllers'
            _revision = '2017-10-11'

            def __init__(self):
                super(Controller.Fabric.Oper, self).__init__()

                self.yang_name = "oper"
                self.yang_parent_name = "fabric"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("fgid", ("fgid", Controller.Fabric.Oper.Fgid))])
                self._leafs = OrderedDict()

                self.fgid = Controller.Fabric.Oper.Fgid()
                self.fgid.parent = self
                self._children_name_map["fgid"] = "fgid"
                self._segment_path = lambda: "oper"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Controller.Fabric.Oper, [], name, value)


            class Fgid(Entity):
                """
                FGID management information
                
                .. attribute:: information
                
                	
                	**type**\:  :py:class:`Information <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Information>`
                
                	**config**\: False
                
                .. attribute:: resource
                
                	
                	**type**\:  :py:class:`Resource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Resource>`
                
                	**config**\: False
                
                .. attribute:: statistics
                
                	
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Statistics>`
                
                	**config**\: False
                
                .. attribute:: fgid_mgr
                
                	
                	**type**\:  :py:class:`FgidMgr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.FgidMgr>`
                
                	**config**\: False
                
                .. attribute:: program_error
                
                	
                	**type**\: list of  		 :py:class:`ProgramError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.ProgramError>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Controller.Fabric.Oper.Fgid, self).__init__()

                    self.yang_name = "fgid"
                    self.yang_parent_name = "oper"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("information", ("information", Controller.Fabric.Oper.Fgid.Information)), ("resource", ("resource", Controller.Fabric.Oper.Fgid.Resource)), ("statistics", ("statistics", Controller.Fabric.Oper.Fgid.Statistics)), ("fgid_mgr", ("fgid_mgr", Controller.Fabric.Oper.Fgid.FgidMgr)), ("program_error", ("program_error", Controller.Fabric.Oper.Fgid.ProgramError))])
                    self._leafs = OrderedDict()

                    self.information = Controller.Fabric.Oper.Fgid.Information()
                    self.information.parent = self
                    self._children_name_map["information"] = "information"

                    self.resource = Controller.Fabric.Oper.Fgid.Resource()
                    self.resource.parent = self
                    self._children_name_map["resource"] = "resource"

                    self.statistics = Controller.Fabric.Oper.Fgid.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"

                    self.fgid_mgr = Controller.Fabric.Oper.Fgid.FgidMgr()
                    self.fgid_mgr.parent = self
                    self._children_name_map["fgid_mgr"] = "fgid_mgr"

                    self.program_error = YList(self)
                    self._segment_path = lambda: "fgid"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.Fabric.Oper.Fgid, [], name, value)


                class Information(Entity):
                    """
                    
                    
                    .. attribute:: id
                    
                    	
                    	**type**\: list of  		 :py:class:`Id <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Information.Id>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.Fabric.Oper.Fgid.Information, self).__init__()

                        self.yang_name = "information"
                        self.yang_parent_name = "fgid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("id", ("id", Controller.Fabric.Oper.Fgid.Information.Id))])
                        self._leafs = OrderedDict()

                        self.id = YList(self)
                        self._segment_path = lambda: "information"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Fabric.Oper.Fgid.Information, [], name, value)


                    class Id(Entity):
                        """
                        
                        
                        .. attribute:: fgid_id  (key)
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..128000
                        
                        	**config**\: False
                        
                        .. attribute:: hex_bitmaps
                        
                        	
                        	**type**\: list of  		 :py:class:`HexBitmaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Information.Id.HexBitmaps>`
                        
                        	**config**\: False
                        
                        .. attribute:: binary_bitmaps
                        
                        	
                        	**type**\: list of  		 :py:class:`BinaryBitmaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Information.Id.BinaryBitmaps>`
                        
                        	**config**\: False
                        
                        .. attribute:: total_asso_fabricq_ids
                        
                        	
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: asso_fabricq_ids
                        
                        	
                        	**type**\: list of  		 :py:class:`AssoFabricqIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Information.Id.AssoFabricqIds>`
                        
                        	**config**\: False
                        
                        .. attribute:: asso_client_info
                        
                        	
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: drivers
                        
                        	
                        	**type**\: list of  		 :py:class:`Drivers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Information.Id.Drivers>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.Fabric.Oper.Fgid.Information.Id, self).__init__()

                            self.yang_name = "id"
                            self.yang_parent_name = "information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['fgid_id']
                            self._child_classes = OrderedDict([("hex_bitmaps", ("hex_bitmaps", Controller.Fabric.Oper.Fgid.Information.Id.HexBitmaps)), ("binary_bitmaps", ("binary_bitmaps", Controller.Fabric.Oper.Fgid.Information.Id.BinaryBitmaps)), ("asso_fabricq_ids", ("asso_fabricq_ids", Controller.Fabric.Oper.Fgid.Information.Id.AssoFabricqIds)), ("drivers", ("drivers", Controller.Fabric.Oper.Fgid.Information.Id.Drivers))])
                            self._leafs = OrderedDict([
                                ('fgid_id', (YLeaf(YType.int32, 'fgid_id'), ['int'])),
                                ('total_asso_fabricq_ids', (YLeaf(YType.int32, 'total_asso_fabricq_ids'), ['int'])),
                                ('asso_client_info', (YLeaf(YType.str, 'asso_client_info'), ['str'])),
                            ])
                            self.fgid_id = None
                            self.total_asso_fabricq_ids = None
                            self.asso_client_info = None

                            self.hex_bitmaps = YList(self)
                            self.binary_bitmaps = YList(self)
                            self.asso_fabricq_ids = YList(self)
                            self.drivers = YList(self)
                            self._segment_path = lambda: "id" + "[fgid_id='" + str(self.fgid_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/information/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Fabric.Oper.Fgid.Information.Id, [u'fgid_id', u'total_asso_fabricq_ids', u'asso_client_info'], name, value)


                        class HexBitmaps(Entity):
                            """
                            
                            
                            .. attribute:: rack_number  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: bitmap
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.Fabric.Oper.Fgid.Information.Id.HexBitmaps, self).__init__()

                                self.yang_name = "hex_bitmaps"
                                self.yang_parent_name = "id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['rack_number']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('rack_number', (YLeaf(YType.int32, 'rack_number'), ['int'])),
                                    ('bitmap', (YLeaf(YType.str, 'bitmap'), ['str'])),
                                ])
                                self.rack_number = None
                                self.bitmap = None
                                self._segment_path = lambda: "hex_bitmaps" + "[rack_number='" + str(self.rack_number) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Fabric.Oper.Fgid.Information.Id.HexBitmaps, [u'rack_number', u'bitmap'], name, value)



                        class BinaryBitmaps(Entity):
                            """
                            
                            
                            .. attribute:: rack_number  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: bitmap
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.Fabric.Oper.Fgid.Information.Id.BinaryBitmaps, self).__init__()

                                self.yang_name = "binary_bitmaps"
                                self.yang_parent_name = "id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['rack_number']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('rack_number', (YLeaf(YType.int32, 'rack_number'), ['int'])),
                                    ('bitmap', (YLeaf(YType.str, 'bitmap'), ['str'])),
                                ])
                                self.rack_number = None
                                self.bitmap = None
                                self._segment_path = lambda: "binary_bitmaps" + "[rack_number='" + str(self.rack_number) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Fabric.Oper.Fgid.Information.Id.BinaryBitmaps, [u'rack_number', u'bitmap'], name, value)



                        class AssoFabricqIds(Entity):
                            """
                            
                            
                            .. attribute:: fabricq_id  (key)
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.Fabric.Oper.Fgid.Information.Id.AssoFabricqIds, self).__init__()

                                self.yang_name = "asso_fabricq_ids"
                                self.yang_parent_name = "id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['fabricq_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('fabricq_id', (YLeaf(YType.str, 'fabricq_id'), ['str'])),
                                ])
                                self.fabricq_id = None
                                self._segment_path = lambda: "asso_fabricq_ids" + "[fabricq_id='" + str(self.fabricq_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Fabric.Oper.Fgid.Information.Id.AssoFabricqIds, [u'fabricq_id'], name, value)



                        class Drivers(Entity):
                            """
                            
                            
                            .. attribute:: rack_number  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: clients
                            
                            	
                            	**type**\: list of  		 :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Information.Id.Drivers.Clients>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.Fabric.Oper.Fgid.Information.Id.Drivers, self).__init__()

                                self.yang_name = "drivers"
                                self.yang_parent_name = "id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['rack_number']
                                self._child_classes = OrderedDict([("clients", ("clients", Controller.Fabric.Oper.Fgid.Information.Id.Drivers.Clients))])
                                self._leafs = OrderedDict([
                                    ('rack_number', (YLeaf(YType.int32, 'rack_number'), ['int'])),
                                ])
                                self.rack_number = None

                                self.clients = YList(self)
                                self._segment_path = lambda: "drivers" + "[rack_number='" + str(self.rack_number) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Fabric.Oper.Fgid.Information.Id.Drivers, [u'rack_number'], name, value)


                            class Clients(Entity):
                                """
                                
                                
                                .. attribute:: client_idx  (key)
                                
                                	
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_0
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_0_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_1
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_1_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_2
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_2_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_3
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_3_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_4
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_4_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_5
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_5_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_6
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_6_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_7
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_7_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_8
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_8_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_9
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_9_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_10
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_10_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_11
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_11_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_12
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_12_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_13
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_13_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_14
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_14_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_15
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_15_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_16
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_16_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_17
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_17_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_18
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_18_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_19
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_19_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_20
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_20_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_21
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_21_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_22
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_22_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_23
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_23_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_24
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_24_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_25
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_25_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_26
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_26_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_27
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_27_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_28
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_28_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_29
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_29_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_30
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_30_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_31
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_31_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_32
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_32_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_33
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_33_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_34
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_34_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: show_asic_35
                                
                                	
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: asic_35_bitmap
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers'
                                _revision = '2017-10-11'

                                def __init__(self):
                                    super(Controller.Fabric.Oper.Fgid.Information.Id.Drivers.Clients, self).__init__()

                                    self.yang_name = "clients"
                                    self.yang_parent_name = "drivers"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['client_idx']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('client_idx', (YLeaf(YType.int32, 'client_idx'), ['int'])),
                                        ('show_asic_0', (YLeaf(YType.boolean, 'show_asic_0'), ['bool'])),
                                        ('asic_0_bitmap', (YLeaf(YType.str, 'asic_0_bitmap'), ['str'])),
                                        ('show_asic_1', (YLeaf(YType.boolean, 'show_asic_1'), ['bool'])),
                                        ('asic_1_bitmap', (YLeaf(YType.str, 'asic_1_bitmap'), ['str'])),
                                        ('show_asic_2', (YLeaf(YType.boolean, 'show_asic_2'), ['bool'])),
                                        ('asic_2_bitmap', (YLeaf(YType.str, 'asic_2_bitmap'), ['str'])),
                                        ('show_asic_3', (YLeaf(YType.boolean, 'show_asic_3'), ['bool'])),
                                        ('asic_3_bitmap', (YLeaf(YType.str, 'asic_3_bitmap'), ['str'])),
                                        ('show_asic_4', (YLeaf(YType.boolean, 'show_asic_4'), ['bool'])),
                                        ('asic_4_bitmap', (YLeaf(YType.str, 'asic_4_bitmap'), ['str'])),
                                        ('show_asic_5', (YLeaf(YType.boolean, 'show_asic_5'), ['bool'])),
                                        ('asic_5_bitmap', (YLeaf(YType.str, 'asic_5_bitmap'), ['str'])),
                                        ('show_asic_6', (YLeaf(YType.boolean, 'show_asic_6'), ['bool'])),
                                        ('asic_6_bitmap', (YLeaf(YType.str, 'asic_6_bitmap'), ['str'])),
                                        ('show_asic_7', (YLeaf(YType.boolean, 'show_asic_7'), ['bool'])),
                                        ('asic_7_bitmap', (YLeaf(YType.str, 'asic_7_bitmap'), ['str'])),
                                        ('show_asic_8', (YLeaf(YType.boolean, 'show_asic_8'), ['bool'])),
                                        ('asic_8_bitmap', (YLeaf(YType.str, 'asic_8_bitmap'), ['str'])),
                                        ('show_asic_9', (YLeaf(YType.boolean, 'show_asic_9'), ['bool'])),
                                        ('asic_9_bitmap', (YLeaf(YType.str, 'asic_9_bitmap'), ['str'])),
                                        ('show_asic_10', (YLeaf(YType.boolean, 'show_asic_10'), ['bool'])),
                                        ('asic_10_bitmap', (YLeaf(YType.str, 'asic_10_bitmap'), ['str'])),
                                        ('show_asic_11', (YLeaf(YType.boolean, 'show_asic_11'), ['bool'])),
                                        ('asic_11_bitmap', (YLeaf(YType.str, 'asic_11_bitmap'), ['str'])),
                                        ('show_asic_12', (YLeaf(YType.boolean, 'show_asic_12'), ['bool'])),
                                        ('asic_12_bitmap', (YLeaf(YType.str, 'asic_12_bitmap'), ['str'])),
                                        ('show_asic_13', (YLeaf(YType.boolean, 'show_asic_13'), ['bool'])),
                                        ('asic_13_bitmap', (YLeaf(YType.str, 'asic_13_bitmap'), ['str'])),
                                        ('show_asic_14', (YLeaf(YType.boolean, 'show_asic_14'), ['bool'])),
                                        ('asic_14_bitmap', (YLeaf(YType.str, 'asic_14_bitmap'), ['str'])),
                                        ('show_asic_15', (YLeaf(YType.boolean, 'show_asic_15'), ['bool'])),
                                        ('asic_15_bitmap', (YLeaf(YType.str, 'asic_15_bitmap'), ['str'])),
                                        ('show_asic_16', (YLeaf(YType.boolean, 'show_asic_16'), ['bool'])),
                                        ('asic_16_bitmap', (YLeaf(YType.str, 'asic_16_bitmap'), ['str'])),
                                        ('show_asic_17', (YLeaf(YType.boolean, 'show_asic_17'), ['bool'])),
                                        ('asic_17_bitmap', (YLeaf(YType.str, 'asic_17_bitmap'), ['str'])),
                                        ('show_asic_18', (YLeaf(YType.boolean, 'show_asic_18'), ['bool'])),
                                        ('asic_18_bitmap', (YLeaf(YType.str, 'asic_18_bitmap'), ['str'])),
                                        ('show_asic_19', (YLeaf(YType.boolean, 'show_asic_19'), ['bool'])),
                                        ('asic_19_bitmap', (YLeaf(YType.str, 'asic_19_bitmap'), ['str'])),
                                        ('show_asic_20', (YLeaf(YType.boolean, 'show_asic_20'), ['bool'])),
                                        ('asic_20_bitmap', (YLeaf(YType.str, 'asic_20_bitmap'), ['str'])),
                                        ('show_asic_21', (YLeaf(YType.boolean, 'show_asic_21'), ['bool'])),
                                        ('asic_21_bitmap', (YLeaf(YType.str, 'asic_21_bitmap'), ['str'])),
                                        ('show_asic_22', (YLeaf(YType.boolean, 'show_asic_22'), ['bool'])),
                                        ('asic_22_bitmap', (YLeaf(YType.str, 'asic_22_bitmap'), ['str'])),
                                        ('show_asic_23', (YLeaf(YType.boolean, 'show_asic_23'), ['bool'])),
                                        ('asic_23_bitmap', (YLeaf(YType.str, 'asic_23_bitmap'), ['str'])),
                                        ('show_asic_24', (YLeaf(YType.boolean, 'show_asic_24'), ['bool'])),
                                        ('asic_24_bitmap', (YLeaf(YType.str, 'asic_24_bitmap'), ['str'])),
                                        ('show_asic_25', (YLeaf(YType.boolean, 'show_asic_25'), ['bool'])),
                                        ('asic_25_bitmap', (YLeaf(YType.str, 'asic_25_bitmap'), ['str'])),
                                        ('show_asic_26', (YLeaf(YType.boolean, 'show_asic_26'), ['bool'])),
                                        ('asic_26_bitmap', (YLeaf(YType.str, 'asic_26_bitmap'), ['str'])),
                                        ('show_asic_27', (YLeaf(YType.boolean, 'show_asic_27'), ['bool'])),
                                        ('asic_27_bitmap', (YLeaf(YType.str, 'asic_27_bitmap'), ['str'])),
                                        ('show_asic_28', (YLeaf(YType.boolean, 'show_asic_28'), ['bool'])),
                                        ('asic_28_bitmap', (YLeaf(YType.str, 'asic_28_bitmap'), ['str'])),
                                        ('show_asic_29', (YLeaf(YType.boolean, 'show_asic_29'), ['bool'])),
                                        ('asic_29_bitmap', (YLeaf(YType.str, 'asic_29_bitmap'), ['str'])),
                                        ('show_asic_30', (YLeaf(YType.boolean, 'show_asic_30'), ['bool'])),
                                        ('asic_30_bitmap', (YLeaf(YType.str, 'asic_30_bitmap'), ['str'])),
                                        ('show_asic_31', (YLeaf(YType.boolean, 'show_asic_31'), ['bool'])),
                                        ('asic_31_bitmap', (YLeaf(YType.str, 'asic_31_bitmap'), ['str'])),
                                        ('show_asic_32', (YLeaf(YType.boolean, 'show_asic_32'), ['bool'])),
                                        ('asic_32_bitmap', (YLeaf(YType.str, 'asic_32_bitmap'), ['str'])),
                                        ('show_asic_33', (YLeaf(YType.boolean, 'show_asic_33'), ['bool'])),
                                        ('asic_33_bitmap', (YLeaf(YType.str, 'asic_33_bitmap'), ['str'])),
                                        ('show_asic_34', (YLeaf(YType.boolean, 'show_asic_34'), ['bool'])),
                                        ('asic_34_bitmap', (YLeaf(YType.str, 'asic_34_bitmap'), ['str'])),
                                        ('show_asic_35', (YLeaf(YType.boolean, 'show_asic_35'), ['bool'])),
                                        ('asic_35_bitmap', (YLeaf(YType.str, 'asic_35_bitmap'), ['str'])),
                                    ])
                                    self.client_idx = None
                                    self.show_asic_0 = None
                                    self.asic_0_bitmap = None
                                    self.show_asic_1 = None
                                    self.asic_1_bitmap = None
                                    self.show_asic_2 = None
                                    self.asic_2_bitmap = None
                                    self.show_asic_3 = None
                                    self.asic_3_bitmap = None
                                    self.show_asic_4 = None
                                    self.asic_4_bitmap = None
                                    self.show_asic_5 = None
                                    self.asic_5_bitmap = None
                                    self.show_asic_6 = None
                                    self.asic_6_bitmap = None
                                    self.show_asic_7 = None
                                    self.asic_7_bitmap = None
                                    self.show_asic_8 = None
                                    self.asic_8_bitmap = None
                                    self.show_asic_9 = None
                                    self.asic_9_bitmap = None
                                    self.show_asic_10 = None
                                    self.asic_10_bitmap = None
                                    self.show_asic_11 = None
                                    self.asic_11_bitmap = None
                                    self.show_asic_12 = None
                                    self.asic_12_bitmap = None
                                    self.show_asic_13 = None
                                    self.asic_13_bitmap = None
                                    self.show_asic_14 = None
                                    self.asic_14_bitmap = None
                                    self.show_asic_15 = None
                                    self.asic_15_bitmap = None
                                    self.show_asic_16 = None
                                    self.asic_16_bitmap = None
                                    self.show_asic_17 = None
                                    self.asic_17_bitmap = None
                                    self.show_asic_18 = None
                                    self.asic_18_bitmap = None
                                    self.show_asic_19 = None
                                    self.asic_19_bitmap = None
                                    self.show_asic_20 = None
                                    self.asic_20_bitmap = None
                                    self.show_asic_21 = None
                                    self.asic_21_bitmap = None
                                    self.show_asic_22 = None
                                    self.asic_22_bitmap = None
                                    self.show_asic_23 = None
                                    self.asic_23_bitmap = None
                                    self.show_asic_24 = None
                                    self.asic_24_bitmap = None
                                    self.show_asic_25 = None
                                    self.asic_25_bitmap = None
                                    self.show_asic_26 = None
                                    self.asic_26_bitmap = None
                                    self.show_asic_27 = None
                                    self.asic_27_bitmap = None
                                    self.show_asic_28 = None
                                    self.asic_28_bitmap = None
                                    self.show_asic_29 = None
                                    self.asic_29_bitmap = None
                                    self.show_asic_30 = None
                                    self.asic_30_bitmap = None
                                    self.show_asic_31 = None
                                    self.asic_31_bitmap = None
                                    self.show_asic_32 = None
                                    self.asic_32_bitmap = None
                                    self.show_asic_33 = None
                                    self.asic_33_bitmap = None
                                    self.show_asic_34 = None
                                    self.asic_34_bitmap = None
                                    self.show_asic_35 = None
                                    self.asic_35_bitmap = None
                                    self._segment_path = lambda: "clients" + "[client_idx='" + str(self.client_idx) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Fabric.Oper.Fgid.Information.Id.Drivers.Clients, [u'client_idx', u'show_asic_0', u'asic_0_bitmap', u'show_asic_1', u'asic_1_bitmap', u'show_asic_2', u'asic_2_bitmap', u'show_asic_3', u'asic_3_bitmap', u'show_asic_4', u'asic_4_bitmap', u'show_asic_5', u'asic_5_bitmap', u'show_asic_6', u'asic_6_bitmap', u'show_asic_7', u'asic_7_bitmap', u'show_asic_8', u'asic_8_bitmap', u'show_asic_9', u'asic_9_bitmap', u'show_asic_10', u'asic_10_bitmap', u'show_asic_11', u'asic_11_bitmap', u'show_asic_12', u'asic_12_bitmap', u'show_asic_13', u'asic_13_bitmap', u'show_asic_14', u'asic_14_bitmap', u'show_asic_15', u'asic_15_bitmap', u'show_asic_16', u'asic_16_bitmap', u'show_asic_17', u'asic_17_bitmap', u'show_asic_18', u'asic_18_bitmap', u'show_asic_19', u'asic_19_bitmap', u'show_asic_20', u'asic_20_bitmap', u'show_asic_21', u'asic_21_bitmap', u'show_asic_22', u'asic_22_bitmap', u'show_asic_23', u'asic_23_bitmap', u'show_asic_24', u'asic_24_bitmap', u'show_asic_25', u'asic_25_bitmap', u'show_asic_26', u'asic_26_bitmap', u'show_asic_27', u'asic_27_bitmap', u'show_asic_28', u'asic_28_bitmap', u'show_asic_29', u'asic_29_bitmap', u'show_asic_30', u'asic_30_bitmap', u'show_asic_31', u'asic_31_bitmap', u'show_asic_32', u'asic_32_bitmap', u'show_asic_33', u'asic_33_bitmap', u'show_asic_34', u'asic_34_bitmap', u'show_asic_35', u'asic_35_bitmap'], name, value)






                class Resource(Entity):
                    """
                    
                    
                    .. attribute:: sdr
                    
                    	
                    	**type**\: list of  		 :py:class:`Sdr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Resource.Sdr>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.Fabric.Oper.Fgid.Resource, self).__init__()

                        self.yang_name = "resource"
                        self.yang_parent_name = "fgid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sdr", ("sdr", Controller.Fabric.Oper.Fgid.Resource.Sdr))])
                        self._leafs = OrderedDict()

                        self.sdr = YList(self)
                        self._segment_path = lambda: "resource"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Fabric.Oper.Fgid.Resource, [], name, value)


                    class Sdr(Entity):
                        """
                        
                        
                        .. attribute:: sdr_name  (key)
                        
                        	
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: description
                        
                        	
                        	**type**\: str
                        
                        	**config**\: False
                        
                        	**default value**\: Secure Domain Router name.
                        
                        .. attribute:: application
                        
                        	
                        	**type**\: list of  		 :py:class:`Application <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Resource.Sdr.Application>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.Fabric.Oper.Fgid.Resource.Sdr, self).__init__()

                            self.yang_name = "sdr"
                            self.yang_parent_name = "resource"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['sdr_name']
                            self._child_classes = OrderedDict([("application", ("application", Controller.Fabric.Oper.Fgid.Resource.Sdr.Application))])
                            self._leafs = OrderedDict([
                                ('sdr_name', (YLeaf(YType.str, 'sdr_name'), ['str'])),
                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ])
                            self.sdr_name = None
                            self.description = None

                            self.application = YList(self)
                            self._segment_path = lambda: "sdr" + "[sdr_name='" + str(self.sdr_name) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/resource/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Fabric.Oper.Fgid.Resource.Sdr, [u'sdr_name', u'description'], name, value)


                        class Application(Entity):
                            """
                            
                            
                            .. attribute:: app_name  (key)
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: description
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            	**default value**\: application.
                            
                            .. attribute:: ids_range
                            
                            	
                            	**type**\: list of  		 :py:class:`IdsRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Resource.Sdr.Application.IdsRange>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.Fabric.Oper.Fgid.Resource.Sdr.Application, self).__init__()

                                self.yang_name = "application"
                                self.yang_parent_name = "sdr"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['app_name']
                                self._child_classes = OrderedDict([("ids_range", ("ids_range", Controller.Fabric.Oper.Fgid.Resource.Sdr.Application.IdsRange))])
                                self._leafs = OrderedDict([
                                    ('app_name', (YLeaf(YType.str, 'app_name'), ['str'])),
                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ])
                                self.app_name = None
                                self.description = None

                                self.ids_range = YList(self)
                                self._segment_path = lambda: "application" + "[app_name='" + str(self.app_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Fabric.Oper.Fgid.Resource.Sdr.Application, [u'app_name', u'description'], name, value)


                            class IdsRange(Entity):
                                """
                                
                                
                                .. attribute:: id  (key)
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..128000
                                
                                	**config**\: False
                                
                                .. attribute:: elements  (key)
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..128000
                                
                                	**config**\: False
                                
                                .. attribute:: fgid_ids
                                
                                	
                                	**type**\: list of  		 :py:class:`FgidIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Resource.Sdr.Application.IdsRange.FgidIds>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers'
                                _revision = '2017-10-11'

                                def __init__(self):
                                    super(Controller.Fabric.Oper.Fgid.Resource.Sdr.Application.IdsRange, self).__init__()

                                    self.yang_name = "ids_range"
                                    self.yang_parent_name = "application"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['id','elements']
                                    self._child_classes = OrderedDict([("fgid_ids", ("fgid_ids", Controller.Fabric.Oper.Fgid.Resource.Sdr.Application.IdsRange.FgidIds))])
                                    self._leafs = OrderedDict([
                                        ('id', (YLeaf(YType.int32, 'id'), ['int'])),
                                        ('elements', (YLeaf(YType.int32, 'elements'), ['int'])),
                                    ])
                                    self.id = None
                                    self.elements = None

                                    self.fgid_ids = YList(self)
                                    self._segment_path = lambda: "ids_range" + "[id='" + str(self.id) + "']" + "[elements='" + str(self.elements) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Fabric.Oper.Fgid.Resource.Sdr.Application.IdsRange, [u'id', u'elements'], name, value)


                                class FgidIds(Entity):
                                    """
                                    
                                    
                                    .. attribute:: fgid_id  (key)
                                    
                                    	
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: line_idx  (key)
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: sdr_name_h
                                    
                                    	
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: app_name_h
                                    
                                    	
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers'
                                    _revision = '2017-10-11'

                                    def __init__(self):
                                        super(Controller.Fabric.Oper.Fgid.Resource.Sdr.Application.IdsRange.FgidIds, self).__init__()

                                        self.yang_name = "fgid_ids"
                                        self.yang_parent_name = "ids_range"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['fgid_id','line_idx']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('fgid_id', (YLeaf(YType.str, 'fgid_id'), ['str'])),
                                            ('line_idx', (YLeaf(YType.int32, 'line_idx'), ['int'])),
                                            ('sdr_name_h', (YLeaf(YType.str, 'sdr_name_h'), ['str'])),
                                            ('app_name_h', (YLeaf(YType.str, 'app_name_h'), ['str'])),
                                        ])
                                        self.fgid_id = None
                                        self.line_idx = None
                                        self.sdr_name_h = None
                                        self.app_name_h = None
                                        self._segment_path = lambda: "fgid_ids" + "[fgid_id='" + str(self.fgid_id) + "']" + "[line_idx='" + str(self.line_idx) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.Fabric.Oper.Fgid.Resource.Sdr.Application.IdsRange.FgidIds, [u'fgid_id', u'line_idx', u'sdr_name_h', u'app_name_h'], name, value)







                class Statistics(Entity):
                    """
                    
                    
                    .. attribute:: all
                    
                    	
                    	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Statistics.All>`
                    
                    	**config**\: False
                    
                    .. attribute:: sdr
                    
                    	
                    	**type**\:  :py:class:`Sdr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Statistics.Sdr>`
                    
                    	**config**\: False
                    
                    .. attribute:: pool
                    
                    	
                    	**type**\:  :py:class:`Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Statistics.Pool>`
                    
                    	**config**\: False
                    
                    .. attribute:: system
                    
                    	
                    	**type**\:  :py:class:`System <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Statistics.System>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.Fabric.Oper.Fgid.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "fgid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("all", ("all", Controller.Fabric.Oper.Fgid.Statistics.All)), ("sdr", ("sdr", Controller.Fabric.Oper.Fgid.Statistics.Sdr)), ("pool", ("pool", Controller.Fabric.Oper.Fgid.Statistics.Pool)), ("system", ("system", Controller.Fabric.Oper.Fgid.Statistics.System))])
                        self._leafs = OrderedDict()

                        self.all = Controller.Fabric.Oper.Fgid.Statistics.All()
                        self.all.parent = self
                        self._children_name_map["all"] = "all"

                        self.sdr = Controller.Fabric.Oper.Fgid.Statistics.Sdr()
                        self.sdr.parent = self
                        self._children_name_map["sdr"] = "sdr"

                        self.pool = Controller.Fabric.Oper.Fgid.Statistics.Pool()
                        self.pool.parent = self
                        self._children_name_map["pool"] = "pool"

                        self.system = Controller.Fabric.Oper.Fgid.Statistics.System()
                        self.system.parent = self
                        self._children_name_map["system"] = "system"
                        self._segment_path = lambda: "statistics"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Fabric.Oper.Fgid.Statistics, [], name, value)


                    class All(Entity):
                        """
                        
                        
                        .. attribute:: stats_list
                        
                        	
                        	**type**\: list of  		 :py:class:`StatsList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Statistics.All.StatsList>`
                        
                        	**config**\: False
                        
                        .. attribute:: sdr_list
                        
                        	
                        	**type**\: list of  		 :py:class:`SdrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Statistics.All.SdrList>`
                        
                        	**config**\: False
                        
                        .. attribute:: pool_list
                        
                        	
                        	**type**\: list of  		 :py:class:`PoolList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Statistics.All.PoolList>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.Fabric.Oper.Fgid.Statistics.All, self).__init__()

                            self.yang_name = "all"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("stats_list", ("stats_list", Controller.Fabric.Oper.Fgid.Statistics.All.StatsList)), ("sdr_list", ("sdr_list", Controller.Fabric.Oper.Fgid.Statistics.All.SdrList)), ("pool_list", ("pool_list", Controller.Fabric.Oper.Fgid.Statistics.All.PoolList))])
                            self._leafs = OrderedDict()

                            self.stats_list = YList(self)
                            self.sdr_list = YList(self)
                            self.pool_list = YList(self)
                            self._segment_path = lambda: "all"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/statistics/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Fabric.Oper.Fgid.Statistics.All, [], name, value)


                        class StatsList(Entity):
                            """
                            
                            
                            .. attribute:: system_stats  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: system_total_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: system_inuse_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: system_hwm_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.Fabric.Oper.Fgid.Statistics.All.StatsList, self).__init__()

                                self.yang_name = "stats_list"
                                self.yang_parent_name = "all"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = ['system_stats']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('system_stats', (YLeaf(YType.int32, 'system_stats'), ['int'])),
                                    ('system_total_fgids', (YLeaf(YType.uint32, 'system_total_fgids'), ['int'])),
                                    ('system_inuse_fgids', (YLeaf(YType.uint32, 'system_inuse_fgids'), ['int'])),
                                    ('system_hwm_fgids', (YLeaf(YType.uint32, 'system_hwm_fgids'), ['int'])),
                                ])
                                self.system_stats = None
                                self.system_total_fgids = None
                                self.system_inuse_fgids = None
                                self.system_hwm_fgids = None
                                self._segment_path = lambda: "stats_list" + "[system_stats='" + str(self.system_stats) + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/statistics/all/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Fabric.Oper.Fgid.Statistics.All.StatsList, [u'system_stats', u'system_total_fgids', u'system_inuse_fgids', u'system_hwm_fgids'], name, value)



                        class SdrList(Entity):
                            """
                            
                            
                            .. attribute:: sdr_name  (key)
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: description
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            	**default value**\: Secure Domain Router name.
                            
                            .. attribute:: sdr_total_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: sdr_inuse_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: sdr_hwm_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: application
                            
                            	
                            	**type**\: list of  		 :py:class:`Application <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Statistics.All.SdrList.Application>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.Fabric.Oper.Fgid.Statistics.All.SdrList, self).__init__()

                                self.yang_name = "sdr_list"
                                self.yang_parent_name = "all"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = ['sdr_name']
                                self._child_classes = OrderedDict([("application", ("application", Controller.Fabric.Oper.Fgid.Statistics.All.SdrList.Application))])
                                self._leafs = OrderedDict([
                                    ('sdr_name', (YLeaf(YType.str, 'sdr_name'), ['str'])),
                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                    ('sdr_total_fgids', (YLeaf(YType.uint32, 'sdr_total_fgids'), ['int'])),
                                    ('sdr_inuse_fgids', (YLeaf(YType.uint32, 'sdr_inuse_fgids'), ['int'])),
                                    ('sdr_hwm_fgids', (YLeaf(YType.uint32, 'sdr_hwm_fgids'), ['int'])),
                                ])
                                self.sdr_name = None
                                self.description = None
                                self.sdr_total_fgids = None
                                self.sdr_inuse_fgids = None
                                self.sdr_hwm_fgids = None

                                self.application = YList(self)
                                self._segment_path = lambda: "sdr_list" + "[sdr_name='" + str(self.sdr_name) + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/statistics/all/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Fabric.Oper.Fgid.Statistics.All.SdrList, [u'sdr_name', u'description', u'sdr_total_fgids', u'sdr_inuse_fgids', u'sdr_hwm_fgids'], name, value)


                            class Application(Entity):
                                """
                                
                                
                                .. attribute:: app_name  (key)
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: description
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                	**default value**\: application.
                                
                                .. attribute:: app_id
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: pool_id
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: inuse_fgids
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: hwm_fgids
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers'
                                _revision = '2017-10-11'

                                def __init__(self):
                                    super(Controller.Fabric.Oper.Fgid.Statistics.All.SdrList.Application, self).__init__()

                                    self.yang_name = "application"
                                    self.yang_parent_name = "sdr_list"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['app_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('app_name', (YLeaf(YType.str, 'app_name'), ['str'])),
                                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                        ('app_id', (YLeaf(YType.uint32, 'app_id'), ['int'])),
                                        ('pool_id', (YLeaf(YType.uint32, 'pool_id'), ['int'])),
                                        ('inuse_fgids', (YLeaf(YType.uint32, 'inuse_fgids'), ['int'])),
                                        ('hwm_fgids', (YLeaf(YType.uint32, 'hwm_fgids'), ['int'])),
                                    ])
                                    self.app_name = None
                                    self.description = None
                                    self.app_id = None
                                    self.pool_id = None
                                    self.inuse_fgids = None
                                    self.hwm_fgids = None
                                    self._segment_path = lambda: "application" + "[app_name='" + str(self.app_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Fabric.Oper.Fgid.Statistics.All.SdrList.Application, [u'app_name', u'description', u'app_id', u'pool_id', u'inuse_fgids', u'hwm_fgids'], name, value)




                        class PoolList(Entity):
                            """
                            
                            
                            .. attribute:: pool_id  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: pool_name
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: pool_type
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: start_fgid
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: total_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: current_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: hwm_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.Fabric.Oper.Fgid.Statistics.All.PoolList, self).__init__()

                                self.yang_name = "pool_list"
                                self.yang_parent_name = "all"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = ['pool_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('pool_id', (YLeaf(YType.uint32, 'pool_id'), ['int'])),
                                    ('pool_name', (YLeaf(YType.str, 'pool_name'), ['str'])),
                                    ('pool_type', (YLeaf(YType.str, 'pool_type'), ['str'])),
                                    ('start_fgid', (YLeaf(YType.str, 'start_fgid'), ['str'])),
                                    ('total_fgids', (YLeaf(YType.uint32, 'total_fgids'), ['int'])),
                                    ('current_fgids', (YLeaf(YType.uint32, 'current_fgids'), ['int'])),
                                    ('hwm_fgids', (YLeaf(YType.uint32, 'hwm_fgids'), ['int'])),
                                ])
                                self.pool_id = None
                                self.pool_name = None
                                self.pool_type = None
                                self.start_fgid = None
                                self.total_fgids = None
                                self.current_fgids = None
                                self.hwm_fgids = None
                                self._segment_path = lambda: "pool_list" + "[pool_id='" + str(self.pool_id) + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/statistics/all/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Fabric.Oper.Fgid.Statistics.All.PoolList, [u'pool_id', u'pool_name', u'pool_type', u'start_fgid', u'total_fgids', u'current_fgids', u'hwm_fgids'], name, value)




                    class Sdr(Entity):
                        """
                        
                        
                        .. attribute:: sdr_list
                        
                        	
                        	**type**\: list of  		 :py:class:`SdrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Statistics.Sdr.SdrList>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.Fabric.Oper.Fgid.Statistics.Sdr, self).__init__()

                            self.yang_name = "sdr"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sdr_list", ("sdr_list", Controller.Fabric.Oper.Fgid.Statistics.Sdr.SdrList))])
                            self._leafs = OrderedDict()

                            self.sdr_list = YList(self)
                            self._segment_path = lambda: "sdr"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/statistics/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Fabric.Oper.Fgid.Statistics.Sdr, [], name, value)


                        class SdrList(Entity):
                            """
                            
                            
                            .. attribute:: sdr_name  (key)
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: description
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            	**default value**\: Secure Domain Router name.
                            
                            .. attribute:: sdr_total_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: sdr_inuse_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: sdr_hwm_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: application
                            
                            	
                            	**type**\: list of  		 :py:class:`Application <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Statistics.Sdr.SdrList.Application>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.Fabric.Oper.Fgid.Statistics.Sdr.SdrList, self).__init__()

                                self.yang_name = "sdr_list"
                                self.yang_parent_name = "sdr"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = ['sdr_name']
                                self._child_classes = OrderedDict([("application", ("application", Controller.Fabric.Oper.Fgid.Statistics.Sdr.SdrList.Application))])
                                self._leafs = OrderedDict([
                                    ('sdr_name', (YLeaf(YType.str, 'sdr_name'), ['str'])),
                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                    ('sdr_total_fgids', (YLeaf(YType.uint32, 'sdr_total_fgids'), ['int'])),
                                    ('sdr_inuse_fgids', (YLeaf(YType.uint32, 'sdr_inuse_fgids'), ['int'])),
                                    ('sdr_hwm_fgids', (YLeaf(YType.uint32, 'sdr_hwm_fgids'), ['int'])),
                                ])
                                self.sdr_name = None
                                self.description = None
                                self.sdr_total_fgids = None
                                self.sdr_inuse_fgids = None
                                self.sdr_hwm_fgids = None

                                self.application = YList(self)
                                self._segment_path = lambda: "sdr_list" + "[sdr_name='" + str(self.sdr_name) + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/statistics/sdr/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Fabric.Oper.Fgid.Statistics.Sdr.SdrList, [u'sdr_name', u'description', u'sdr_total_fgids', u'sdr_inuse_fgids', u'sdr_hwm_fgids'], name, value)


                            class Application(Entity):
                                """
                                
                                
                                .. attribute:: app_name  (key)
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: description
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                	**default value**\: application.
                                
                                .. attribute:: app_id
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: pool_id
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: inuse_fgids
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: hwm_fgids
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers'
                                _revision = '2017-10-11'

                                def __init__(self):
                                    super(Controller.Fabric.Oper.Fgid.Statistics.Sdr.SdrList.Application, self).__init__()

                                    self.yang_name = "application"
                                    self.yang_parent_name = "sdr_list"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['app_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('app_name', (YLeaf(YType.str, 'app_name'), ['str'])),
                                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                        ('app_id', (YLeaf(YType.uint32, 'app_id'), ['int'])),
                                        ('pool_id', (YLeaf(YType.uint32, 'pool_id'), ['int'])),
                                        ('inuse_fgids', (YLeaf(YType.uint32, 'inuse_fgids'), ['int'])),
                                        ('hwm_fgids', (YLeaf(YType.uint32, 'hwm_fgids'), ['int'])),
                                    ])
                                    self.app_name = None
                                    self.description = None
                                    self.app_id = None
                                    self.pool_id = None
                                    self.inuse_fgids = None
                                    self.hwm_fgids = None
                                    self._segment_path = lambda: "application" + "[app_name='" + str(self.app_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Fabric.Oper.Fgid.Statistics.Sdr.SdrList.Application, [u'app_name', u'description', u'app_id', u'pool_id', u'inuse_fgids', u'hwm_fgids'], name, value)





                    class Pool(Entity):
                        """
                        
                        
                        .. attribute:: pool_list
                        
                        	
                        	**type**\: list of  		 :py:class:`PoolList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Statistics.Pool.PoolList>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.Fabric.Oper.Fgid.Statistics.Pool, self).__init__()

                            self.yang_name = "pool"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("pool_list", ("pool_list", Controller.Fabric.Oper.Fgid.Statistics.Pool.PoolList))])
                            self._leafs = OrderedDict()

                            self.pool_list = YList(self)
                            self._segment_path = lambda: "pool"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/statistics/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Fabric.Oper.Fgid.Statistics.Pool, [], name, value)


                        class PoolList(Entity):
                            """
                            
                            
                            .. attribute:: pool_id  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: pool_name
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: pool_type
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: start_fgid
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: total_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: current_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: hwm_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.Fabric.Oper.Fgid.Statistics.Pool.PoolList, self).__init__()

                                self.yang_name = "pool_list"
                                self.yang_parent_name = "pool"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = ['pool_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('pool_id', (YLeaf(YType.uint32, 'pool_id'), ['int'])),
                                    ('pool_name', (YLeaf(YType.str, 'pool_name'), ['str'])),
                                    ('pool_type', (YLeaf(YType.str, 'pool_type'), ['str'])),
                                    ('start_fgid', (YLeaf(YType.str, 'start_fgid'), ['str'])),
                                    ('total_fgids', (YLeaf(YType.uint32, 'total_fgids'), ['int'])),
                                    ('current_fgids', (YLeaf(YType.uint32, 'current_fgids'), ['int'])),
                                    ('hwm_fgids', (YLeaf(YType.uint32, 'hwm_fgids'), ['int'])),
                                ])
                                self.pool_id = None
                                self.pool_name = None
                                self.pool_type = None
                                self.start_fgid = None
                                self.total_fgids = None
                                self.current_fgids = None
                                self.hwm_fgids = None
                                self._segment_path = lambda: "pool_list" + "[pool_id='" + str(self.pool_id) + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/statistics/pool/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Fabric.Oper.Fgid.Statistics.Pool.PoolList, [u'pool_id', u'pool_name', u'pool_type', u'start_fgid', u'total_fgids', u'current_fgids', u'hwm_fgids'], name, value)




                    class System(Entity):
                        """
                        
                        
                        .. attribute:: stats_list
                        
                        	
                        	**type**\: list of  		 :py:class:`StatsList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.Statistics.System.StatsList>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.Fabric.Oper.Fgid.Statistics.System, self).__init__()

                            self.yang_name = "system"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("stats_list", ("stats_list", Controller.Fabric.Oper.Fgid.Statistics.System.StatsList))])
                            self._leafs = OrderedDict()

                            self.stats_list = YList(self)
                            self._segment_path = lambda: "system"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/statistics/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Fabric.Oper.Fgid.Statistics.System, [], name, value)


                        class StatsList(Entity):
                            """
                            
                            
                            .. attribute:: system_stats  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: system_total_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: system_inuse_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: system_hwm_fgids
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.Fabric.Oper.Fgid.Statistics.System.StatsList, self).__init__()

                                self.yang_name = "stats_list"
                                self.yang_parent_name = "system"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = ['system_stats']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('system_stats', (YLeaf(YType.int32, 'system_stats'), ['int'])),
                                    ('system_total_fgids', (YLeaf(YType.uint32, 'system_total_fgids'), ['int'])),
                                    ('system_inuse_fgids', (YLeaf(YType.uint32, 'system_inuse_fgids'), ['int'])),
                                    ('system_hwm_fgids', (YLeaf(YType.uint32, 'system_hwm_fgids'), ['int'])),
                                ])
                                self.system_stats = None
                                self.system_total_fgids = None
                                self.system_inuse_fgids = None
                                self.system_hwm_fgids = None
                                self._segment_path = lambda: "stats_list" + "[system_stats='" + str(self.system_stats) + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/statistics/system/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Fabric.Oper.Fgid.Statistics.System.StatsList, [u'system_stats', u'system_total_fgids', u'system_inuse_fgids', u'system_hwm_fgids'], name, value)





                class FgidMgr(Entity):
                    """
                    
                    
                    .. attribute:: trace
                    
                    	show traceable processes
                    	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.FgidMgr.Trace>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.Fabric.Oper.Fgid.FgidMgr, self).__init__()

                        self.yang_name = "fgid_mgr"
                        self.yang_parent_name = "fgid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("trace", ("trace", Controller.Fabric.Oper.Fgid.FgidMgr.Trace))])
                        self._leafs = OrderedDict()

                        self.trace = YList(self)
                        self._segment_path = lambda: "fgid_mgr"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Fabric.Oper.Fgid.FgidMgr, [], name, value)


                    class Trace(Entity):
                        """
                        show traceable processes
                        
                        .. attribute:: buffer  (key)
                        
                        	
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: location
                        
                        	
                        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.FgidMgr.Trace.Location>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.Fabric.Oper.Fgid.FgidMgr.Trace, self).__init__()

                            self.yang_name = "trace"
                            self.yang_parent_name = "fgid_mgr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['buffer']
                            self._child_classes = OrderedDict([("location", ("location", Controller.Fabric.Oper.Fgid.FgidMgr.Trace.Location))])
                            self._leafs = OrderedDict([
                                ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
                            ])
                            self.buffer = None

                            self.location = YList(self)
                            self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/fgid_mgr/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Fabric.Oper.Fgid.FgidMgr.Trace, [u'buffer'], name, value)


                        class Location(Entity):
                            """
                            
                            
                            .. attribute:: location_name  (key)
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: all_options
                            
                            	
                            	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.FgidMgr.Trace.Location.AllOptions>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.Fabric.Oper.Fgid.FgidMgr.Trace.Location, self).__init__()

                                self.yang_name = "location"
                                self.yang_parent_name = "trace"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['location_name']
                                self._child_classes = OrderedDict([("all-options", ("all_options", Controller.Fabric.Oper.Fgid.FgidMgr.Trace.Location.AllOptions))])
                                self._leafs = OrderedDict([
                                    ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                                ])
                                self.location_name = None

                                self.all_options = YList(self)
                                self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.Fabric.Oper.Fgid.FgidMgr.Trace.Location, [u'location_name'], name, value)


                            class AllOptions(Entity):
                                """
                                
                                
                                .. attribute:: option  (key)
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: trace_blocks
                                
                                	
                                	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.FgidMgr.Trace.Location.AllOptions.TraceBlocks>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers'
                                _revision = '2017-10-11'

                                def __init__(self):
                                    super(Controller.Fabric.Oper.Fgid.FgidMgr.Trace.Location.AllOptions, self).__init__()

                                    self.yang_name = "all-options"
                                    self.yang_parent_name = "location"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['option']
                                    self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", Controller.Fabric.Oper.Fgid.FgidMgr.Trace.Location.AllOptions.TraceBlocks))])
                                    self._leafs = OrderedDict([
                                        ('option', (YLeaf(YType.str, 'option'), ['str'])),
                                    ])
                                    self.option = None

                                    self.trace_blocks = YList(self)
                                    self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.Fabric.Oper.Fgid.FgidMgr.Trace.Location.AllOptions, [u'option'], name, value)


                                class TraceBlocks(Entity):
                                    """
                                    
                                    
                                    .. attribute:: data
                                    
                                    	Trace output block
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers'
                                    _revision = '2017-10-11'

                                    def __init__(self):
                                        super(Controller.Fabric.Oper.Fgid.FgidMgr.Trace.Location.AllOptions.TraceBlocks, self).__init__()

                                        self.yang_name = "trace-blocks"
                                        self.yang_parent_name = "all-options"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('data', (YLeaf(YType.str, 'data'), ['str'])),
                                        ])
                                        self.data = None
                                        self._segment_path = lambda: "trace-blocks"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.Fabric.Oper.Fgid.FgidMgr.Trace.Location.AllOptions.TraceBlocks, [u'data'], name, value)







                class ProgramError(Entity):
                    """
                    
                    
                    .. attribute:: start  (key)
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..128000
                    
                    	**config**\: False
                    
                    .. attribute:: end  (key)
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..128000
                    
                    	**config**\: False
                    
                    .. attribute:: rack
                    
                    	
                    	**type**\: list of  		 :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.Fabric.Oper.Fgid.ProgramError.Rack>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.Fabric.Oper.Fgid.ProgramError, self).__init__()

                        self.yang_name = "program_error"
                        self.yang_parent_name = "fgid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['start','end']
                        self._child_classes = OrderedDict([("rack", ("rack", Controller.Fabric.Oper.Fgid.ProgramError.Rack))])
                        self._leafs = OrderedDict([
                            ('start', (YLeaf(YType.int32, 'start'), ['int'])),
                            ('end', (YLeaf(YType.int32, 'end'), ['int'])),
                        ])
                        self.start = None
                        self.end = None

                        self.rack = YList(self)
                        self._segment_path = lambda: "program_error" + "[start='" + str(self.start) + "']" + "[end='" + str(self.end) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/fabric/oper/fgid/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.Fabric.Oper.Fgid.ProgramError, [u'start', u'end'], name, value)


                    class Rack(Entity):
                        """
                        
                        
                        .. attribute:: rack_id  (key)
                        
                        	
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: rack_id_str
                        
                        	
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: fgids_in_error
                        
                        	
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: found_fgids_in_error
                        
                        	
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: total_error_fgids
                        
                        	
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: incorrect_fgids_range
                        
                        	
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: cmd_not_supported
                        
                        	
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.Fabric.Oper.Fgid.ProgramError.Rack, self).__init__()

                            self.yang_name = "rack"
                            self.yang_parent_name = "program_error"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['rack_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rack_id', (YLeaf(YType.int32, 'rack_id'), ['int'])),
                                ('rack_id_str', (YLeaf(YType.str, 'rack_id_str'), ['str'])),
                                ('fgids_in_error', (YLeaf(YType.str, 'fgids_in_error'), ['str'])),
                                ('found_fgids_in_error', (YLeaf(YType.boolean, 'found_fgids_in_error'), ['bool'])),
                                ('total_error_fgids', (YLeaf(YType.int32, 'total_error_fgids'), ['int'])),
                                ('incorrect_fgids_range', (YLeaf(YType.boolean, 'incorrect_fgids_range'), ['bool'])),
                                ('cmd_not_supported', (YLeaf(YType.boolean, 'cmd_not_supported'), ['bool'])),
                            ])
                            self.rack_id = None
                            self.rack_id_str = None
                            self.fgids_in_error = None
                            self.found_fgids_in_error = None
                            self.total_error_fgids = None
                            self.incorrect_fgids_range = None
                            self.cmd_not_supported = None
                            self._segment_path = lambda: "rack" + "[rack_id='" + str(self.rack_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.Fabric.Oper.Fgid.ProgramError.Rack, [u'rack_id', u'rack_id_str', u'fgids_in_error', u'found_fgids_in_error', u'total_error_fgids', u'incorrect_fgids_range', u'cmd_not_supported'], name, value)







    class CardMgr(Entity):
        """
        
        
        .. attribute:: trace
        
        	show traceable processes
        	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Trace>`
        
        	**config**\: False
        
        .. attribute:: inventory
        
        	
        	**type**\:  :py:class:`Inventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Inventory>`
        
        	**config**\: False
        
        .. attribute:: event_history
        
        	
        	**type**\:  :py:class:`EventHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.EventHistory>`
        
        	**config**\: False
        
        .. attribute:: notif_history
        
        	
        	**type**\:  :py:class:`NotifHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.NotifHistory>`
        
        	**config**\: False
        
        .. attribute:: oir_history
        
        	
        	**type**\:  :py:class:`OirHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.OirHistory>`
        
        	**config**\: False
        
        .. attribute:: iofpga
        
        	
        	**type**\:  :py:class:`Iofpga <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga>`
        
        	**config**\: False
        
        .. attribute:: bootloader
        
        	
        	**type**\:  :py:class:`Bootloader <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Bootloader>`
        
        	**config**\: False
        
        

        """

        _prefix = 'calvados_controllers'
        _revision = '2017-10-11'

        def __init__(self):
            super(Controller.CardMgr, self).__init__()

            self.yang_name = "card_mgr"
            self.yang_parent_name = "controller"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("trace", ("trace", Controller.CardMgr.Trace)), ("inventory", ("inventory", Controller.CardMgr.Inventory)), ("event-history", ("event_history", Controller.CardMgr.EventHistory)), ("notif-history", ("notif_history", Controller.CardMgr.NotifHistory)), ("oir-history", ("oir_history", Controller.CardMgr.OirHistory)), ("iofpga", ("iofpga", Controller.CardMgr.Iofpga)), ("bootloader", ("bootloader", Controller.CardMgr.Bootloader))])
            self._leafs = OrderedDict()

            self.inventory = Controller.CardMgr.Inventory()
            self.inventory.parent = self
            self._children_name_map["inventory"] = "inventory"

            self.event_history = Controller.CardMgr.EventHistory()
            self.event_history.parent = self
            self._children_name_map["event_history"] = "event-history"

            self.notif_history = Controller.CardMgr.NotifHistory()
            self.notif_history.parent = self
            self._children_name_map["notif_history"] = "notif-history"

            self.oir_history = Controller.CardMgr.OirHistory()
            self.oir_history.parent = self
            self._children_name_map["oir_history"] = "oir-history"

            self.iofpga = Controller.CardMgr.Iofpga()
            self.iofpga.parent = self
            self._children_name_map["iofpga"] = "iofpga"

            self.bootloader = Controller.CardMgr.Bootloader()
            self.bootloader.parent = self
            self._children_name_map["bootloader"] = "bootloader"

            self.trace = YList(self)
            self._segment_path = lambda: "card_mgr"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Controller.CardMgr, [], name, value)


        class Trace(Entity):
            """
            show traceable processes
            
            .. attribute:: buffer  (key)
            
            	
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Trace.Location>`
            
            	**config**\: False
            
            

            """

            _prefix = 'calvados_controllers'
            _revision = '2017-10-11'

            def __init__(self):
                super(Controller.CardMgr.Trace, self).__init__()

                self.yang_name = "trace"
                self.yang_parent_name = "card_mgr"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['buffer']
                self._child_classes = OrderedDict([("location", ("location", Controller.CardMgr.Trace.Location))])
                self._leafs = OrderedDict([
                    ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
                ])
                self.buffer = None

                self.location = YList(self)
                self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Controller.CardMgr.Trace, [u'buffer'], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: all_options
                
                	
                	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Trace.Location.AllOptions>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Controller.CardMgr.Trace.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "trace"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("all-options", ("all_options", Controller.CardMgr.Trace.Location.AllOptions))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                    ])
                    self.location_name = None

                    self.all_options = YList(self)
                    self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.CardMgr.Trace.Location, [u'location_name'], name, value)


                class AllOptions(Entity):
                    """
                    
                    
                    .. attribute:: option  (key)
                    
                    	
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: trace_blocks
                    
                    	
                    	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Trace.Location.AllOptions.TraceBlocks>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.CardMgr.Trace.Location.AllOptions, self).__init__()

                        self.yang_name = "all-options"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['option']
                        self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", Controller.CardMgr.Trace.Location.AllOptions.TraceBlocks))])
                        self._leafs = OrderedDict([
                            ('option', (YLeaf(YType.str, 'option'), ['str'])),
                        ])
                        self.option = None

                        self.trace_blocks = YList(self)
                        self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.CardMgr.Trace.Location.AllOptions, [u'option'], name, value)


                    class TraceBlocks(Entity):
                        """
                        
                        
                        .. attribute:: data
                        
                        	Trace output block
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.CardMgr.Trace.Location.AllOptions.TraceBlocks, self).__init__()

                            self.yang_name = "trace-blocks"
                            self.yang_parent_name = "all-options"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('data', (YLeaf(YType.str, 'data'), ['str'])),
                            ])
                            self.data = None
                            self._segment_path = lambda: "trace-blocks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.CardMgr.Trace.Location.AllOptions.TraceBlocks, [u'data'], name, value)






        class Inventory(Entity):
            """
            
            
            .. attribute:: summary
            
            	
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Inventory.Summary>`
            
            	**config**\: False
            
            .. attribute:: detail
            
            	
            	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Inventory.Detail>`
            
            	**config**\: False
            
            

            """

            _prefix = 'calvados_controllers'
            _revision = '2017-10-11'

            def __init__(self):
                super(Controller.CardMgr.Inventory, self).__init__()

                self.yang_name = "inventory"
                self.yang_parent_name = "card_mgr"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("summary", ("summary", Controller.CardMgr.Inventory.Summary)), ("detail", ("detail", Controller.CardMgr.Inventory.Detail))])
                self._leafs = OrderedDict()

                self.summary = Controller.CardMgr.Inventory.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"

                self.detail = Controller.CardMgr.Inventory.Detail()
                self.detail.parent = self
                self._children_name_map["detail"] = "detail"
                self._segment_path = lambda: "inventory"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Controller.CardMgr.Inventory, [], name, value)


            class Summary(Entity):
                """
                
                
                .. attribute:: card_mgr_inv_summary
                
                	
                	**type**\: list of  		 :py:class:`CardMgrInvSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Inventory.Summary.CardMgrInvSummary>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Controller.CardMgr.Inventory.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "inventory"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("card_mgr_inv_summary", ("card_mgr_inv_summary", Controller.CardMgr.Inventory.Summary.CardMgrInvSummary))])
                    self._leafs = OrderedDict()

                    self.card_mgr_inv_summary = YList(self)
                    self._segment_path = lambda: "summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/inventory/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.CardMgr.Inventory.Summary, [], name, value)


                class CardMgrInvSummary(Entity):
                    """
                    
                    
                    .. attribute:: location  (key)
                    
                    	
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    	**config**\: False
                    
                    .. attribute:: card_mgr_inv_pid_string
                    
                    	
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: card_mgr_inv_slot_number
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: card_mgr_inv_serial_number
                    
                    	
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: card_mgr_inv_hw_version
                    
                    	
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: card_mgr_inv_card_state
                    
                    	
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.CardMgr.Inventory.Summary.CardMgrInvSummary, self).__init__()

                        self.yang_name = "card_mgr_inv_summary"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['location']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                            ('card_mgr_inv_pid_string', (YLeaf(YType.str, 'card_mgr_inv_PID_string'), ['str'])),
                            ('card_mgr_inv_slot_number', (YLeaf(YType.uint32, 'card_mgr_inv_slot_number'), ['int'])),
                            ('card_mgr_inv_serial_number', (YLeaf(YType.str, 'card_mgr_inv_serial_number'), ['str'])),
                            ('card_mgr_inv_hw_version', (YLeaf(YType.str, 'card_mgr_inv_hw_version'), ['str'])),
                            ('card_mgr_inv_card_state', (YLeaf(YType.str, 'card_mgr_inv_card_state'), ['str'])),
                        ])
                        self.location = None
                        self.card_mgr_inv_pid_string = None
                        self.card_mgr_inv_slot_number = None
                        self.card_mgr_inv_serial_number = None
                        self.card_mgr_inv_hw_version = None
                        self.card_mgr_inv_card_state = None
                        self._segment_path = lambda: "card_mgr_inv_summary" + "[location='" + str(self.location) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/inventory/summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.CardMgr.Inventory.Summary.CardMgrInvSummary, [u'location', u'card_mgr_inv_pid_string', u'card_mgr_inv_slot_number', u'card_mgr_inv_serial_number', u'card_mgr_inv_hw_version', u'card_mgr_inv_card_state'], name, value)




            class Detail(Entity):
                """
                
                
                .. attribute:: card_mgr_inv_detail
                
                	
                	**type**\: list of  		 :py:class:`CardMgrInvDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Inventory.Detail.CardMgrInvDetail>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Controller.CardMgr.Inventory.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "inventory"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("card_mgr_inv_detail", ("card_mgr_inv_detail", Controller.CardMgr.Inventory.Detail.CardMgrInvDetail))])
                    self._leafs = OrderedDict()

                    self.card_mgr_inv_detail = YList(self)
                    self._segment_path = lambda: "detail"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/inventory/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.CardMgr.Inventory.Detail, [], name, value)


                class CardMgrInvDetail(Entity):
                    """
                    
                    
                    .. attribute:: location  (key)
                    
                    	
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: card_mgr_inv_detail_list
                    
                    	
                    	**type**\:  :py:class:`CardMgrInvDetailList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Inventory.Detail.CardMgrInvDetail.CardMgrInvDetailList>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.CardMgr.Inventory.Detail.CardMgrInvDetail, self).__init__()

                        self.yang_name = "card_mgr_inv_detail"
                        self.yang_parent_name = "detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['location']
                        self._child_classes = OrderedDict([("card_mgr_inv_detail_list", ("card_mgr_inv_detail_list", Controller.CardMgr.Inventory.Detail.CardMgrInvDetail.CardMgrInvDetailList))])
                        self._leafs = OrderedDict([
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                        ])
                        self.location = None

                        self.card_mgr_inv_detail_list = Controller.CardMgr.Inventory.Detail.CardMgrInvDetail.CardMgrInvDetailList()
                        self.card_mgr_inv_detail_list.parent = self
                        self._children_name_map["card_mgr_inv_detail_list"] = "card_mgr_inv_detail_list"
                        self._segment_path = lambda: "card_mgr_inv_detail" + "[location='" + str(self.location) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/inventory/detail/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.CardMgr.Inventory.Detail.CardMgrInvDetail, [u'location'], name, value)


                    class CardMgrInvDetailList(Entity):
                        """
                        
                        
                        .. attribute:: card_mgr_inv_detail_values
                        
                        	
                        	**type**\: list of str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.CardMgr.Inventory.Detail.CardMgrInvDetail.CardMgrInvDetailList, self).__init__()

                            self.yang_name = "card_mgr_inv_detail_list"
                            self.yang_parent_name = "card_mgr_inv_detail"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('card_mgr_inv_detail_values', (YLeafList(YType.str, 'card_mgr_inv_detail_values'), ['str'])),
                            ])
                            self.card_mgr_inv_detail_values = []
                            self._segment_path = lambda: "card_mgr_inv_detail_list"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.CardMgr.Inventory.Detail.CardMgrInvDetail.CardMgrInvDetailList, [u'card_mgr_inv_detail_values'], name, value)






        class EventHistory(Entity):
            """
            
            
            .. attribute:: brief
            
            	
            	**type**\:  :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.EventHistory.Brief>`
            
            	**config**\: False
            
            .. attribute:: detail
            
            	
            	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.EventHistory.Detail>`
            
            	**config**\: False
            
            

            """

            _prefix = 'calvados_controllers'
            _revision = '2017-10-11'

            def __init__(self):
                super(Controller.CardMgr.EventHistory, self).__init__()

                self.yang_name = "event-history"
                self.yang_parent_name = "card_mgr"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("brief", ("brief", Controller.CardMgr.EventHistory.Brief)), ("detail", ("detail", Controller.CardMgr.EventHistory.Detail))])
                self._leafs = OrderedDict()

                self.brief = Controller.CardMgr.EventHistory.Brief()
                self.brief.parent = self
                self._children_name_map["brief"] = "brief"

                self.detail = Controller.CardMgr.EventHistory.Detail()
                self.detail.parent = self
                self._children_name_map["detail"] = "detail"
                self._segment_path = lambda: "event-history"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Controller.CardMgr.EventHistory, [], name, value)


            class Brief(Entity):
                """
                
                
                .. attribute:: location
                
                	
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.EventHistory.Brief.Location>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Controller.CardMgr.EventHistory.Brief, self).__init__()

                    self.yang_name = "brief"
                    self.yang_parent_name = "event-history"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("location", ("location", Controller.CardMgr.EventHistory.Brief.Location))])
                    self._leafs = OrderedDict()

                    self.location = YList(self)
                    self._segment_path = lambda: "brief"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/event-history/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.CardMgr.EventHistory.Brief, [], name, value)


                class Location(Entity):
                    """
                    
                    
                    .. attribute:: location  (key)
                    
                    	
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: card_event_hist_brief
                    
                    	
                    	**type**\:  :py:class:`CardEventHistBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.EventHistory.Brief.Location.CardEventHistBrief>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.CardMgr.EventHistory.Brief.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "brief"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['location']
                        self._child_classes = OrderedDict([("card_event_hist_brief", ("card_event_hist_brief", Controller.CardMgr.EventHistory.Brief.Location.CardEventHistBrief))])
                        self._leafs = OrderedDict([
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                        ])
                        self.location = None

                        self.card_event_hist_brief = Controller.CardMgr.EventHistory.Brief.Location.CardEventHistBrief()
                        self.card_event_hist_brief.parent = self
                        self._children_name_map["card_event_hist_brief"] = "card_event_hist_brief"
                        self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/event-history/brief/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.CardMgr.EventHistory.Brief.Location, [u'location'], name, value)


                    class CardEventHistBrief(Entity):
                        """
                        
                        
                        .. attribute:: card_event_hist_brief_values
                        
                        	
                        	**type**\: list of str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.CardMgr.EventHistory.Brief.Location.CardEventHistBrief, self).__init__()

                            self.yang_name = "card_event_hist_brief"
                            self.yang_parent_name = "location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('card_event_hist_brief_values', (YLeafList(YType.str, 'card_event_hist_brief_values'), ['str'])),
                            ])
                            self.card_event_hist_brief_values = []
                            self._segment_path = lambda: "card_event_hist_brief"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.CardMgr.EventHistory.Brief.Location.CardEventHistBrief, [u'card_event_hist_brief_values'], name, value)





            class Detail(Entity):
                """
                
                
                .. attribute:: location
                
                	
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.EventHistory.Detail.Location>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Controller.CardMgr.EventHistory.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "event-history"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("location", ("location", Controller.CardMgr.EventHistory.Detail.Location))])
                    self._leafs = OrderedDict()

                    self.location = YList(self)
                    self._segment_path = lambda: "detail"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/event-history/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.CardMgr.EventHistory.Detail, [], name, value)


                class Location(Entity):
                    """
                    
                    
                    .. attribute:: location  (key)
                    
                    	
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: card_event_hist_detail
                    
                    	
                    	**type**\:  :py:class:`CardEventHistDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.EventHistory.Detail.Location.CardEventHistDetail>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.CardMgr.EventHistory.Detail.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['location']
                        self._child_classes = OrderedDict([("card_event_hist_detail", ("card_event_hist_detail", Controller.CardMgr.EventHistory.Detail.Location.CardEventHistDetail))])
                        self._leafs = OrderedDict([
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                        ])
                        self.location = None

                        self.card_event_hist_detail = Controller.CardMgr.EventHistory.Detail.Location.CardEventHistDetail()
                        self.card_event_hist_detail.parent = self
                        self._children_name_map["card_event_hist_detail"] = "card_event_hist_detail"
                        self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/event-history/detail/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.CardMgr.EventHistory.Detail.Location, [u'location'], name, value)


                    class CardEventHistDetail(Entity):
                        """
                        
                        
                        .. attribute:: card_event_hist_detail_values
                        
                        	
                        	**type**\: list of str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.CardMgr.EventHistory.Detail.Location.CardEventHistDetail, self).__init__()

                            self.yang_name = "card_event_hist_detail"
                            self.yang_parent_name = "location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('card_event_hist_detail_values', (YLeafList(YType.str, 'card_event_hist_detail_values'), ['str'])),
                            ])
                            self.card_event_hist_detail_values = []
                            self._segment_path = lambda: "card_event_hist_detail"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.CardMgr.EventHistory.Detail.Location.CardEventHistDetail, [u'card_event_hist_detail_values'], name, value)






        class NotifHistory(Entity):
            """
            
            
            .. attribute:: brief
            
            	
            	**type**\:  :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.NotifHistory.Brief>`
            
            	**config**\: False
            
            .. attribute:: detail
            
            	
            	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.NotifHistory.Detail>`
            
            	**config**\: False
            
            

            """

            _prefix = 'calvados_controllers'
            _revision = '2017-10-11'

            def __init__(self):
                super(Controller.CardMgr.NotifHistory, self).__init__()

                self.yang_name = "notif-history"
                self.yang_parent_name = "card_mgr"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("brief", ("brief", Controller.CardMgr.NotifHistory.Brief)), ("detail", ("detail", Controller.CardMgr.NotifHistory.Detail))])
                self._leafs = OrderedDict()

                self.brief = Controller.CardMgr.NotifHistory.Brief()
                self.brief.parent = self
                self._children_name_map["brief"] = "brief"

                self.detail = Controller.CardMgr.NotifHistory.Detail()
                self.detail.parent = self
                self._children_name_map["detail"] = "detail"
                self._segment_path = lambda: "notif-history"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Controller.CardMgr.NotifHistory, [], name, value)


            class Brief(Entity):
                """
                
                
                .. attribute:: location
                
                	
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.NotifHistory.Brief.Location>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Controller.CardMgr.NotifHistory.Brief, self).__init__()

                    self.yang_name = "brief"
                    self.yang_parent_name = "notif-history"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("location", ("location", Controller.CardMgr.NotifHistory.Brief.Location))])
                    self._leafs = OrderedDict()

                    self.location = YList(self)
                    self._segment_path = lambda: "brief"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/notif-history/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.CardMgr.NotifHistory.Brief, [], name, value)


                class Location(Entity):
                    """
                    
                    
                    .. attribute:: location  (key)
                    
                    	
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: card_notif_hist_brief
                    
                    	
                    	**type**\:  :py:class:`CardNotifHistBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.NotifHistory.Brief.Location.CardNotifHistBrief>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.CardMgr.NotifHistory.Brief.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "brief"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['location']
                        self._child_classes = OrderedDict([("card_notif_hist_brief", ("card_notif_hist_brief", Controller.CardMgr.NotifHistory.Brief.Location.CardNotifHistBrief))])
                        self._leafs = OrderedDict([
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                        ])
                        self.location = None

                        self.card_notif_hist_brief = Controller.CardMgr.NotifHistory.Brief.Location.CardNotifHistBrief()
                        self.card_notif_hist_brief.parent = self
                        self._children_name_map["card_notif_hist_brief"] = "card_notif_hist_brief"
                        self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/notif-history/brief/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.CardMgr.NotifHistory.Brief.Location, [u'location'], name, value)


                    class CardNotifHistBrief(Entity):
                        """
                        
                        
                        .. attribute:: card_notif_hist_brief_values
                        
                        	
                        	**type**\: list of str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.CardMgr.NotifHistory.Brief.Location.CardNotifHistBrief, self).__init__()

                            self.yang_name = "card_notif_hist_brief"
                            self.yang_parent_name = "location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('card_notif_hist_brief_values', (YLeafList(YType.str, 'card_notif_hist_brief_values'), ['str'])),
                            ])
                            self.card_notif_hist_brief_values = []
                            self._segment_path = lambda: "card_notif_hist_brief"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.CardMgr.NotifHistory.Brief.Location.CardNotifHistBrief, [u'card_notif_hist_brief_values'], name, value)





            class Detail(Entity):
                """
                
                
                .. attribute:: location
                
                	
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.NotifHistory.Detail.Location>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Controller.CardMgr.NotifHistory.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "notif-history"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("location", ("location", Controller.CardMgr.NotifHistory.Detail.Location))])
                    self._leafs = OrderedDict()

                    self.location = YList(self)
                    self._segment_path = lambda: "detail"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/notif-history/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.CardMgr.NotifHistory.Detail, [], name, value)


                class Location(Entity):
                    """
                    
                    
                    .. attribute:: location  (key)
                    
                    	
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: card_notif_hist_detail
                    
                    	
                    	**type**\:  :py:class:`CardNotifHistDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.NotifHistory.Detail.Location.CardNotifHistDetail>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.CardMgr.NotifHistory.Detail.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['location']
                        self._child_classes = OrderedDict([("card_notif_hist_detail", ("card_notif_hist_detail", Controller.CardMgr.NotifHistory.Detail.Location.CardNotifHistDetail))])
                        self._leafs = OrderedDict([
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                        ])
                        self.location = None

                        self.card_notif_hist_detail = Controller.CardMgr.NotifHistory.Detail.Location.CardNotifHistDetail()
                        self.card_notif_hist_detail.parent = self
                        self._children_name_map["card_notif_hist_detail"] = "card_notif_hist_detail"
                        self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/notif-history/detail/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.CardMgr.NotifHistory.Detail.Location, [u'location'], name, value)


                    class CardNotifHistDetail(Entity):
                        """
                        
                        
                        .. attribute:: card_notif_hist_detail_values
                        
                        	
                        	**type**\: list of str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.CardMgr.NotifHistory.Detail.Location.CardNotifHistDetail, self).__init__()

                            self.yang_name = "card_notif_hist_detail"
                            self.yang_parent_name = "location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('card_notif_hist_detail_values', (YLeafList(YType.str, 'card_notif_hist_detail_values'), ['str'])),
                            ])
                            self.card_notif_hist_detail_values = []
                            self._segment_path = lambda: "card_notif_hist_detail"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.CardMgr.NotifHistory.Detail.Location.CardNotifHistDetail, [u'card_notif_hist_detail_values'], name, value)






        class OirHistory(Entity):
            """
            
            
            .. attribute:: rack
            
            	
            	**type**\: list of  		 :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.OirHistory.Rack>`
            
            	**config**\: False
            
            

            """

            _prefix = 'calvados_controllers'
            _revision = '2017-10-11'

            def __init__(self):
                super(Controller.CardMgr.OirHistory, self).__init__()

                self.yang_name = "oir-history"
                self.yang_parent_name = "card_mgr"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rack", ("rack", Controller.CardMgr.OirHistory.Rack))])
                self._leafs = OrderedDict()

                self.rack = YList(self)
                self._segment_path = lambda: "oir-history"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Controller.CardMgr.OirHistory, [], name, value)


            class Rack(Entity):
                """
                
                
                .. attribute:: rack  (key)
                
                	
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: card_oir_hist
                
                	
                	**type**\:  :py:class:`CardOirHist <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.OirHistory.Rack.CardOirHist>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Controller.CardMgr.OirHistory.Rack, self).__init__()

                    self.yang_name = "rack"
                    self.yang_parent_name = "oir-history"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['rack']
                    self._child_classes = OrderedDict([("card_oir_hist", ("card_oir_hist", Controller.CardMgr.OirHistory.Rack.CardOirHist))])
                    self._leafs = OrderedDict([
                        ('rack', (YLeaf(YType.str, 'rack'), ['str'])),
                    ])
                    self.rack = None

                    self.card_oir_hist = Controller.CardMgr.OirHistory.Rack.CardOirHist()
                    self.card_oir_hist.parent = self
                    self._children_name_map["card_oir_hist"] = "card_oir_hist"
                    self._segment_path = lambda: "rack" + "[rack='" + str(self.rack) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/oir-history/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.CardMgr.OirHistory.Rack, [u'rack'], name, value)


                class CardOirHist(Entity):
                    """
                    
                    
                    .. attribute:: card_oir_events
                    
                    	
                    	**type**\: list of str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.CardMgr.OirHistory.Rack.CardOirHist, self).__init__()

                        self.yang_name = "card_oir_hist"
                        self.yang_parent_name = "rack"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('card_oir_events', (YLeafList(YType.str, 'card_oir_events'), ['str'])),
                        ])
                        self.card_oir_events = []
                        self._segment_path = lambda: "card_oir_hist"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.CardMgr.OirHistory.Rack.CardOirHist, [u'card_oir_events'], name, value)





        class Iofpga(Entity):
            """
            
            
            .. attribute:: register
            
            	
            	**type**\:  :py:class:`Register <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register>`
            
            	**config**\: False
            
            .. attribute:: flash
            
            	
            	**type**\:  :py:class:`Flash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Flash>`
            
            	**config**\: False
            
            

            """

            _prefix = 'calvados_controllers'
            _revision = '2017-10-11'

            def __init__(self):
                super(Controller.CardMgr.Iofpga, self).__init__()

                self.yang_name = "iofpga"
                self.yang_parent_name = "card_mgr"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("register", ("register", Controller.CardMgr.Iofpga.Register)), ("flash", ("flash", Controller.CardMgr.Iofpga.Flash))])
                self._leafs = OrderedDict()

                self.register = Controller.CardMgr.Iofpga.Register()
                self.register.parent = self
                self._children_name_map["register"] = "register"

                self.flash = Controller.CardMgr.Iofpga.Flash()
                self.flash.parent = self
                self._children_name_map["flash"] = "flash"
                self._segment_path = lambda: "iofpga"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Controller.CardMgr.Iofpga, [], name, value)


            class Register(Entity):
                """
                
                
                .. attribute:: cpu
                
                	
                	**type**\:  :py:class:`Cpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Cpu>`
                
                	**config**\: False
                
                .. attribute:: mb
                
                	
                	**type**\:  :py:class:`Mb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Mb>`
                
                	**config**\: False
                
                .. attribute:: dc
                
                	
                	**type**\:  :py:class:`Dc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Dc>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Controller.CardMgr.Iofpga.Register, self).__init__()

                    self.yang_name = "register"
                    self.yang_parent_name = "iofpga"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("cpu", ("cpu", Controller.CardMgr.Iofpga.Register.Cpu)), ("mb", ("mb", Controller.CardMgr.Iofpga.Register.Mb)), ("dc", ("dc", Controller.CardMgr.Iofpga.Register.Dc))])
                    self._leafs = OrderedDict()

                    self.cpu = Controller.CardMgr.Iofpga.Register.Cpu()
                    self.cpu.parent = self
                    self._children_name_map["cpu"] = "cpu"

                    self.mb = Controller.CardMgr.Iofpga.Register.Mb()
                    self.mb.parent = self
                    self._children_name_map["mb"] = "mb"

                    self.dc = Controller.CardMgr.Iofpga.Register.Dc()
                    self.dc.parent = self
                    self._children_name_map["dc"] = "dc"
                    self._segment_path = lambda: "register"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/iofpga/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.CardMgr.Iofpga.Register, [], name, value)


                class Cpu(Entity):
                    """
                    
                    
                    .. attribute:: register_location
                    
                    	
                    	**type**\: list of  		 :py:class:`RegisterLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.CardMgr.Iofpga.Register.Cpu, self).__init__()

                        self.yang_name = "cpu"
                        self.yang_parent_name = "register"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("register_location", ("register_location", Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation))])
                        self._leafs = OrderedDict()

                        self.register_location = YList(self)
                        self._segment_path = lambda: "cpu"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/iofpga/register/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.CardMgr.Iofpga.Register.Cpu, [], name, value)


                    class RegisterLocation(Entity):
                        """
                        
                        
                        .. attribute:: register_location  (key)
                        
                        	
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: iofpga_block_number
                        
                        	
                        	**type**\: list of  		 :py:class:`IofpgaBlockNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaBlockNumber>`
                        
                        	**config**\: False
                        
                        .. attribute:: iofpga_offset
                        
                        	
                        	**type**\: list of  		 :py:class:`IofpgaOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaOffset>`
                        
                        	**config**\: False
                        
                        .. attribute:: iofpga_address
                        
                        	
                        	**type**\: list of  		 :py:class:`IofpgaAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaAddress>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation, self).__init__()

                            self.yang_name = "register_location"
                            self.yang_parent_name = "cpu"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['register_location']
                            self._child_classes = OrderedDict([("iofpga_block_number", ("iofpga_block_number", Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaBlockNumber)), ("iofpga_offset", ("iofpga_offset", Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaOffset)), ("iofpga_address", ("iofpga_address", Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaAddress))])
                            self._leafs = OrderedDict([
                                ('register_location', (YLeaf(YType.str, 'register_location'), ['str'])),
                            ])
                            self.register_location = None

                            self.iofpga_block_number = YList(self)
                            self.iofpga_offset = YList(self)
                            self.iofpga_address = YList(self)
                            self._segment_path = lambda: "register_location" + "[register_location='" + str(self.register_location) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/iofpga/register/cpu/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation, [u'register_location'], name, value)


                        class IofpgaBlockNumber(Entity):
                            """
                            
                            
                            .. attribute:: iofpga_block_num  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: block_location
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: iofpga_block_nm
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: iofpga_register_number
                            
                            	
                            	**type**\: list of  		 :py:class:`IofpgaRegisterNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaBlockNumber, self).__init__()

                                self.yang_name = "iofpga_block_number"
                                self.yang_parent_name = "register_location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['iofpga_block_num']
                                self._child_classes = OrderedDict([("iofpga_register_number", ("iofpga_register_number", Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber))])
                                self._leafs = OrderedDict([
                                    ('iofpga_block_num', (YLeaf(YType.uint32, 'iofpga_block_num'), ['int'])),
                                    ('block_location', (YLeaf(YType.str, 'block_location'), ['str'])),
                                    ('iofpga_block_nm', (YLeaf(YType.str, 'iofpga_block_nm'), ['str'])),
                                ])
                                self.iofpga_block_num = None
                                self.block_location = None
                                self.iofpga_block_nm = None

                                self.iofpga_register_number = YList(self)
                                self._segment_path = lambda: "iofpga_block_number" + "[iofpga_block_num='" + str(self.iofpga_block_num) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaBlockNumber, [u'iofpga_block_num', u'block_location', u'iofpga_block_nm'], name, value)


                            class IofpgaRegisterNumber(Entity):
                                """
                                
                                
                                .. attribute:: index  (key)
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: iofpga_register_name
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: iofpga_data
                                
                                	
                                	**type**\: list of  		 :py:class:`IofpgaData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber.IofpgaData>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers'
                                _revision = '2017-10-11'

                                def __init__(self):
                                    super(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber, self).__init__()

                                    self.yang_name = "iofpga_register_number"
                                    self.yang_parent_name = "iofpga_block_number"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['index']
                                    self._child_classes = OrderedDict([("iofpga_data", ("iofpga_data", Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber.IofpgaData))])
                                    self._leafs = OrderedDict([
                                        ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                        ('iofpga_register_name', (YLeaf(YType.str, 'iofpga_register_name'), ['str'])),
                                    ])
                                    self.index = None
                                    self.iofpga_register_name = None

                                    self.iofpga_data = YList(self)
                                    self._segment_path = lambda: "iofpga_register_number" + "[index='" + str(self.index) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber, [u'index', u'iofpga_register_name'], name, value)


                                class IofpgaData(Entity):
                                    """
                                    
                                    
                                    .. attribute:: name
                                    
                                    	
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: offset
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: value
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers'
                                    _revision = '2017-10-11'

                                    def __init__(self):
                                        super(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber.IofpgaData, self).__init__()

                                        self.yang_name = "iofpga_data"
                                        self.yang_parent_name = "iofpga_register_number"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('offset', (YLeaf(YType.uint32, 'offset'), ['int'])),
                                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                        ])
                                        self.name = None
                                        self.offset = None
                                        self.value = None
                                        self._segment_path = lambda: "iofpga_data"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber.IofpgaData, [u'name', u'offset', u'value'], name, value)





                        class IofpgaOffset(Entity):
                            """
                            
                            
                            .. attribute:: hex_offset  (key)
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: iofpga_reg_offset_data
                            
                            	
                            	**type**\: list of  		 :py:class:`IofpgaRegOffsetData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaOffset.IofpgaRegOffsetData>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaOffset, self).__init__()

                                self.yang_name = "iofpga_offset"
                                self.yang_parent_name = "register_location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['hex_offset']
                                self._child_classes = OrderedDict([("iofpga_reg_offset_data", ("iofpga_reg_offset_data", Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaOffset.IofpgaRegOffsetData))])
                                self._leafs = OrderedDict([
                                    ('hex_offset', (YLeaf(YType.str, 'hex_offset'), ['str'])),
                                ])
                                self.hex_offset = None

                                self.iofpga_reg_offset_data = YList(self)
                                self._segment_path = lambda: "iofpga_offset" + "[hex_offset='" + str(self.hex_offset) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaOffset, [u'hex_offset'], name, value)


                            class IofpgaRegOffsetData(Entity):
                                """
                                
                                
                                .. attribute:: iofpga_reg_off_addr
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: reg_off_value
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers'
                                _revision = '2017-10-11'

                                def __init__(self):
                                    super(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaOffset.IofpgaRegOffsetData, self).__init__()

                                    self.yang_name = "iofpga_reg_offset_data"
                                    self.yang_parent_name = "iofpga_offset"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('iofpga_reg_off_addr', (YLeaf(YType.uint32, 'iofpga_reg_off_addr'), ['int'])),
                                        ('reg_off_value', (YLeaf(YType.str, 'reg_off_value'), ['str'])),
                                    ])
                                    self.iofpga_reg_off_addr = None
                                    self.reg_off_value = None
                                    self._segment_path = lambda: "iofpga_reg_offset_data"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaOffset.IofpgaRegOffsetData, [u'iofpga_reg_off_addr', u'reg_off_value'], name, value)




                        class IofpgaAddress(Entity):
                            """
                            
                            
                            .. attribute:: start_hex_addr  (key)
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: end_hex_addr  (key)
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: iofpga_reg_range_addr_list
                            
                            	
                            	**type**\: list of  		 :py:class:`IofpgaRegRangeAddrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaAddress, self).__init__()

                                self.yang_name = "iofpga_address"
                                self.yang_parent_name = "register_location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['start_hex_addr','end_hex_addr']
                                self._child_classes = OrderedDict([("iofpga_reg_range_addr_list", ("iofpga_reg_range_addr_list", Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList))])
                                self._leafs = OrderedDict([
                                    ('start_hex_addr', (YLeaf(YType.str, 'start_hex_addr'), ['str'])),
                                    ('end_hex_addr', (YLeaf(YType.str, 'end_hex_addr'), ['str'])),
                                ])
                                self.start_hex_addr = None
                                self.end_hex_addr = None

                                self.iofpga_reg_range_addr_list = YList(self)
                                self._segment_path = lambda: "iofpga_address" + "[start_hex_addr='" + str(self.start_hex_addr) + "']" + "[end_hex_addr='" + str(self.end_hex_addr) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaAddress, [u'start_hex_addr', u'end_hex_addr'], name, value)


                            class IofpgaRegRangeAddrList(Entity):
                                """
                                
                                
                                .. attribute:: iofpga_reg_range_addr  (key)
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: iofpga_reg_data
                                
                                	
                                	**type**\: list of  		 :py:class:`IofpgaRegData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList.IofpgaRegData>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers'
                                _revision = '2017-10-11'

                                def __init__(self):
                                    super(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList, self).__init__()

                                    self.yang_name = "iofpga_reg_range_addr_list"
                                    self.yang_parent_name = "iofpga_address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['iofpga_reg_range_addr']
                                    self._child_classes = OrderedDict([("iofpga_reg_data", ("iofpga_reg_data", Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList.IofpgaRegData))])
                                    self._leafs = OrderedDict([
                                        ('iofpga_reg_range_addr', (YLeaf(YType.uint32, 'iofpga_reg_range_addr'), ['int'])),
                                    ])
                                    self.iofpga_reg_range_addr = None

                                    self.iofpga_reg_data = YList(self)
                                    self._segment_path = lambda: "iofpga_reg_range_addr_list" + "[iofpga_reg_range_addr='" + str(self.iofpga_reg_range_addr) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList, [u'iofpga_reg_range_addr'], name, value)


                                class IofpgaRegData(Entity):
                                    """
                                    
                                    
                                    .. attribute:: iofpga_reg_addr
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: reg_value
                                    
                                    	
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers'
                                    _revision = '2017-10-11'

                                    def __init__(self):
                                        super(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList.IofpgaRegData, self).__init__()

                                        self.yang_name = "iofpga_reg_data"
                                        self.yang_parent_name = "iofpga_reg_range_addr_list"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('iofpga_reg_addr', (YLeaf(YType.uint32, 'iofpga_reg_addr'), ['int'])),
                                            ('reg_value', (YLeaf(YType.str, 'reg_value'), ['str'])),
                                        ])
                                        self.iofpga_reg_addr = None
                                        self.reg_value = None
                                        self._segment_path = lambda: "iofpga_reg_data"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.CardMgr.Iofpga.Register.Cpu.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList.IofpgaRegData, [u'iofpga_reg_addr', u'reg_value'], name, value)







                class Mb(Entity):
                    """
                    
                    
                    .. attribute:: register_location
                    
                    	
                    	**type**\: list of  		 :py:class:`RegisterLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.CardMgr.Iofpga.Register.Mb, self).__init__()

                        self.yang_name = "mb"
                        self.yang_parent_name = "register"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("register_location", ("register_location", Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation))])
                        self._leafs = OrderedDict()

                        self.register_location = YList(self)
                        self._segment_path = lambda: "mb"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/iofpga/register/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.CardMgr.Iofpga.Register.Mb, [], name, value)


                    class RegisterLocation(Entity):
                        """
                        
                        
                        .. attribute:: register_location  (key)
                        
                        	
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: iofpga_block_number
                        
                        	
                        	**type**\: list of  		 :py:class:`IofpgaBlockNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaBlockNumber>`
                        
                        	**config**\: False
                        
                        .. attribute:: iofpga_offset
                        
                        	
                        	**type**\: list of  		 :py:class:`IofpgaOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaOffset>`
                        
                        	**config**\: False
                        
                        .. attribute:: iofpga_address
                        
                        	
                        	**type**\: list of  		 :py:class:`IofpgaAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaAddress>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation, self).__init__()

                            self.yang_name = "register_location"
                            self.yang_parent_name = "mb"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['register_location']
                            self._child_classes = OrderedDict([("iofpga_block_number", ("iofpga_block_number", Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaBlockNumber)), ("iofpga_offset", ("iofpga_offset", Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaOffset)), ("iofpga_address", ("iofpga_address", Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaAddress))])
                            self._leafs = OrderedDict([
                                ('register_location', (YLeaf(YType.str, 'register_location'), ['str'])),
                            ])
                            self.register_location = None

                            self.iofpga_block_number = YList(self)
                            self.iofpga_offset = YList(self)
                            self.iofpga_address = YList(self)
                            self._segment_path = lambda: "register_location" + "[register_location='" + str(self.register_location) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/iofpga/register/mb/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation, [u'register_location'], name, value)


                        class IofpgaBlockNumber(Entity):
                            """
                            
                            
                            .. attribute:: iofpga_block_num  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: block_location
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: iofpga_block_nm
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: iofpga_register_number
                            
                            	
                            	**type**\: list of  		 :py:class:`IofpgaRegisterNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaBlockNumber, self).__init__()

                                self.yang_name = "iofpga_block_number"
                                self.yang_parent_name = "register_location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['iofpga_block_num']
                                self._child_classes = OrderedDict([("iofpga_register_number", ("iofpga_register_number", Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber))])
                                self._leafs = OrderedDict([
                                    ('iofpga_block_num', (YLeaf(YType.uint32, 'iofpga_block_num'), ['int'])),
                                    ('block_location', (YLeaf(YType.str, 'block_location'), ['str'])),
                                    ('iofpga_block_nm', (YLeaf(YType.str, 'iofpga_block_nm'), ['str'])),
                                ])
                                self.iofpga_block_num = None
                                self.block_location = None
                                self.iofpga_block_nm = None

                                self.iofpga_register_number = YList(self)
                                self._segment_path = lambda: "iofpga_block_number" + "[iofpga_block_num='" + str(self.iofpga_block_num) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaBlockNumber, [u'iofpga_block_num', u'block_location', u'iofpga_block_nm'], name, value)


                            class IofpgaRegisterNumber(Entity):
                                """
                                
                                
                                .. attribute:: index  (key)
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: iofpga_register_name
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: iofpga_data
                                
                                	
                                	**type**\: list of  		 :py:class:`IofpgaData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber.IofpgaData>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers'
                                _revision = '2017-10-11'

                                def __init__(self):
                                    super(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber, self).__init__()

                                    self.yang_name = "iofpga_register_number"
                                    self.yang_parent_name = "iofpga_block_number"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['index']
                                    self._child_classes = OrderedDict([("iofpga_data", ("iofpga_data", Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber.IofpgaData))])
                                    self._leafs = OrderedDict([
                                        ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                        ('iofpga_register_name', (YLeaf(YType.str, 'iofpga_register_name'), ['str'])),
                                    ])
                                    self.index = None
                                    self.iofpga_register_name = None

                                    self.iofpga_data = YList(self)
                                    self._segment_path = lambda: "iofpga_register_number" + "[index='" + str(self.index) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber, [u'index', u'iofpga_register_name'], name, value)


                                class IofpgaData(Entity):
                                    """
                                    
                                    
                                    .. attribute:: name
                                    
                                    	
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: offset
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: value
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers'
                                    _revision = '2017-10-11'

                                    def __init__(self):
                                        super(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber.IofpgaData, self).__init__()

                                        self.yang_name = "iofpga_data"
                                        self.yang_parent_name = "iofpga_register_number"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('offset', (YLeaf(YType.uint32, 'offset'), ['int'])),
                                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                        ])
                                        self.name = None
                                        self.offset = None
                                        self.value = None
                                        self._segment_path = lambda: "iofpga_data"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber.IofpgaData, [u'name', u'offset', u'value'], name, value)





                        class IofpgaOffset(Entity):
                            """
                            
                            
                            .. attribute:: hex_offset  (key)
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: iofpga_reg_offset_data
                            
                            	
                            	**type**\: list of  		 :py:class:`IofpgaRegOffsetData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaOffset.IofpgaRegOffsetData>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaOffset, self).__init__()

                                self.yang_name = "iofpga_offset"
                                self.yang_parent_name = "register_location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['hex_offset']
                                self._child_classes = OrderedDict([("iofpga_reg_offset_data", ("iofpga_reg_offset_data", Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaOffset.IofpgaRegOffsetData))])
                                self._leafs = OrderedDict([
                                    ('hex_offset', (YLeaf(YType.str, 'hex_offset'), ['str'])),
                                ])
                                self.hex_offset = None

                                self.iofpga_reg_offset_data = YList(self)
                                self._segment_path = lambda: "iofpga_offset" + "[hex_offset='" + str(self.hex_offset) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaOffset, [u'hex_offset'], name, value)


                            class IofpgaRegOffsetData(Entity):
                                """
                                
                                
                                .. attribute:: iofpga_reg_off_addr
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: reg_off_value
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers'
                                _revision = '2017-10-11'

                                def __init__(self):
                                    super(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaOffset.IofpgaRegOffsetData, self).__init__()

                                    self.yang_name = "iofpga_reg_offset_data"
                                    self.yang_parent_name = "iofpga_offset"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('iofpga_reg_off_addr', (YLeaf(YType.uint32, 'iofpga_reg_off_addr'), ['int'])),
                                        ('reg_off_value', (YLeaf(YType.str, 'reg_off_value'), ['str'])),
                                    ])
                                    self.iofpga_reg_off_addr = None
                                    self.reg_off_value = None
                                    self._segment_path = lambda: "iofpga_reg_offset_data"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaOffset.IofpgaRegOffsetData, [u'iofpga_reg_off_addr', u'reg_off_value'], name, value)




                        class IofpgaAddress(Entity):
                            """
                            
                            
                            .. attribute:: start_hex_addr  (key)
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: end_hex_addr  (key)
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: iofpga_reg_range_addr_list
                            
                            	
                            	**type**\: list of  		 :py:class:`IofpgaRegRangeAddrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaAddress, self).__init__()

                                self.yang_name = "iofpga_address"
                                self.yang_parent_name = "register_location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['start_hex_addr','end_hex_addr']
                                self._child_classes = OrderedDict([("iofpga_reg_range_addr_list", ("iofpga_reg_range_addr_list", Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList))])
                                self._leafs = OrderedDict([
                                    ('start_hex_addr', (YLeaf(YType.str, 'start_hex_addr'), ['str'])),
                                    ('end_hex_addr', (YLeaf(YType.str, 'end_hex_addr'), ['str'])),
                                ])
                                self.start_hex_addr = None
                                self.end_hex_addr = None

                                self.iofpga_reg_range_addr_list = YList(self)
                                self._segment_path = lambda: "iofpga_address" + "[start_hex_addr='" + str(self.start_hex_addr) + "']" + "[end_hex_addr='" + str(self.end_hex_addr) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaAddress, [u'start_hex_addr', u'end_hex_addr'], name, value)


                            class IofpgaRegRangeAddrList(Entity):
                                """
                                
                                
                                .. attribute:: iofpga_reg_range_addr  (key)
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: iofpga_reg_data
                                
                                	
                                	**type**\: list of  		 :py:class:`IofpgaRegData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList.IofpgaRegData>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers'
                                _revision = '2017-10-11'

                                def __init__(self):
                                    super(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList, self).__init__()

                                    self.yang_name = "iofpga_reg_range_addr_list"
                                    self.yang_parent_name = "iofpga_address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['iofpga_reg_range_addr']
                                    self._child_classes = OrderedDict([("iofpga_reg_data", ("iofpga_reg_data", Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList.IofpgaRegData))])
                                    self._leafs = OrderedDict([
                                        ('iofpga_reg_range_addr', (YLeaf(YType.uint32, 'iofpga_reg_range_addr'), ['int'])),
                                    ])
                                    self.iofpga_reg_range_addr = None

                                    self.iofpga_reg_data = YList(self)
                                    self._segment_path = lambda: "iofpga_reg_range_addr_list" + "[iofpga_reg_range_addr='" + str(self.iofpga_reg_range_addr) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList, [u'iofpga_reg_range_addr'], name, value)


                                class IofpgaRegData(Entity):
                                    """
                                    
                                    
                                    .. attribute:: iofpga_reg_addr
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: reg_value
                                    
                                    	
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers'
                                    _revision = '2017-10-11'

                                    def __init__(self):
                                        super(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList.IofpgaRegData, self).__init__()

                                        self.yang_name = "iofpga_reg_data"
                                        self.yang_parent_name = "iofpga_reg_range_addr_list"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('iofpga_reg_addr', (YLeaf(YType.uint32, 'iofpga_reg_addr'), ['int'])),
                                            ('reg_value', (YLeaf(YType.str, 'reg_value'), ['str'])),
                                        ])
                                        self.iofpga_reg_addr = None
                                        self.reg_value = None
                                        self._segment_path = lambda: "iofpga_reg_data"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.CardMgr.Iofpga.Register.Mb.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList.IofpgaRegData, [u'iofpga_reg_addr', u'reg_value'], name, value)







                class Dc(Entity):
                    """
                    
                    
                    .. attribute:: register_location
                    
                    	
                    	**type**\: list of  		 :py:class:`RegisterLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.CardMgr.Iofpga.Register.Dc, self).__init__()

                        self.yang_name = "dc"
                        self.yang_parent_name = "register"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("register_location", ("register_location", Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation))])
                        self._leafs = OrderedDict()

                        self.register_location = YList(self)
                        self._segment_path = lambda: "dc"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/iofpga/register/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.CardMgr.Iofpga.Register.Dc, [], name, value)


                    class RegisterLocation(Entity):
                        """
                        
                        
                        .. attribute:: register_location  (key)
                        
                        	
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: iofpga_block_number
                        
                        	
                        	**type**\: list of  		 :py:class:`IofpgaBlockNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaBlockNumber>`
                        
                        	**config**\: False
                        
                        .. attribute:: iofpga_offset
                        
                        	
                        	**type**\: list of  		 :py:class:`IofpgaOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaOffset>`
                        
                        	**config**\: False
                        
                        .. attribute:: iofpga_address
                        
                        	
                        	**type**\: list of  		 :py:class:`IofpgaAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaAddress>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation, self).__init__()

                            self.yang_name = "register_location"
                            self.yang_parent_name = "dc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['register_location']
                            self._child_classes = OrderedDict([("iofpga_block_number", ("iofpga_block_number", Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaBlockNumber)), ("iofpga_offset", ("iofpga_offset", Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaOffset)), ("iofpga_address", ("iofpga_address", Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaAddress))])
                            self._leafs = OrderedDict([
                                ('register_location', (YLeaf(YType.str, 'register_location'), ['str'])),
                            ])
                            self.register_location = None

                            self.iofpga_block_number = YList(self)
                            self.iofpga_offset = YList(self)
                            self.iofpga_address = YList(self)
                            self._segment_path = lambda: "register_location" + "[register_location='" + str(self.register_location) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/iofpga/register/dc/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation, [u'register_location'], name, value)


                        class IofpgaBlockNumber(Entity):
                            """
                            
                            
                            .. attribute:: iofpga_block_num  (key)
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: block_location
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: iofpga_block_nm
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: iofpga_register_number
                            
                            	
                            	**type**\: list of  		 :py:class:`IofpgaRegisterNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaBlockNumber, self).__init__()

                                self.yang_name = "iofpga_block_number"
                                self.yang_parent_name = "register_location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['iofpga_block_num']
                                self._child_classes = OrderedDict([("iofpga_register_number", ("iofpga_register_number", Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber))])
                                self._leafs = OrderedDict([
                                    ('iofpga_block_num', (YLeaf(YType.uint32, 'iofpga_block_num'), ['int'])),
                                    ('block_location', (YLeaf(YType.str, 'block_location'), ['str'])),
                                    ('iofpga_block_nm', (YLeaf(YType.str, 'iofpga_block_nm'), ['str'])),
                                ])
                                self.iofpga_block_num = None
                                self.block_location = None
                                self.iofpga_block_nm = None

                                self.iofpga_register_number = YList(self)
                                self._segment_path = lambda: "iofpga_block_number" + "[iofpga_block_num='" + str(self.iofpga_block_num) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaBlockNumber, [u'iofpga_block_num', u'block_location', u'iofpga_block_nm'], name, value)


                            class IofpgaRegisterNumber(Entity):
                                """
                                
                                
                                .. attribute:: index  (key)
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: iofpga_register_name
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: iofpga_data
                                
                                	
                                	**type**\: list of  		 :py:class:`IofpgaData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber.IofpgaData>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers'
                                _revision = '2017-10-11'

                                def __init__(self):
                                    super(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber, self).__init__()

                                    self.yang_name = "iofpga_register_number"
                                    self.yang_parent_name = "iofpga_block_number"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['index']
                                    self._child_classes = OrderedDict([("iofpga_data", ("iofpga_data", Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber.IofpgaData))])
                                    self._leafs = OrderedDict([
                                        ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                        ('iofpga_register_name', (YLeaf(YType.str, 'iofpga_register_name'), ['str'])),
                                    ])
                                    self.index = None
                                    self.iofpga_register_name = None

                                    self.iofpga_data = YList(self)
                                    self._segment_path = lambda: "iofpga_register_number" + "[index='" + str(self.index) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber, [u'index', u'iofpga_register_name'], name, value)


                                class IofpgaData(Entity):
                                    """
                                    
                                    
                                    .. attribute:: name
                                    
                                    	
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: offset
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: value
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers'
                                    _revision = '2017-10-11'

                                    def __init__(self):
                                        super(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber.IofpgaData, self).__init__()

                                        self.yang_name = "iofpga_data"
                                        self.yang_parent_name = "iofpga_register_number"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('offset', (YLeaf(YType.uint32, 'offset'), ['int'])),
                                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                        ])
                                        self.name = None
                                        self.offset = None
                                        self.value = None
                                        self._segment_path = lambda: "iofpga_data"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaBlockNumber.IofpgaRegisterNumber.IofpgaData, [u'name', u'offset', u'value'], name, value)





                        class IofpgaOffset(Entity):
                            """
                            
                            
                            .. attribute:: hex_offset  (key)
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: iofpga_reg_offset_data
                            
                            	
                            	**type**\: list of  		 :py:class:`IofpgaRegOffsetData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaOffset.IofpgaRegOffsetData>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaOffset, self).__init__()

                                self.yang_name = "iofpga_offset"
                                self.yang_parent_name = "register_location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['hex_offset']
                                self._child_classes = OrderedDict([("iofpga_reg_offset_data", ("iofpga_reg_offset_data", Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaOffset.IofpgaRegOffsetData))])
                                self._leafs = OrderedDict([
                                    ('hex_offset', (YLeaf(YType.str, 'hex_offset'), ['str'])),
                                ])
                                self.hex_offset = None

                                self.iofpga_reg_offset_data = YList(self)
                                self._segment_path = lambda: "iofpga_offset" + "[hex_offset='" + str(self.hex_offset) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaOffset, [u'hex_offset'], name, value)


                            class IofpgaRegOffsetData(Entity):
                                """
                                
                                
                                .. attribute:: iofpga_reg_off_addr
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: reg_off_value
                                
                                	
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers'
                                _revision = '2017-10-11'

                                def __init__(self):
                                    super(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaOffset.IofpgaRegOffsetData, self).__init__()

                                    self.yang_name = "iofpga_reg_offset_data"
                                    self.yang_parent_name = "iofpga_offset"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('iofpga_reg_off_addr', (YLeaf(YType.uint32, 'iofpga_reg_off_addr'), ['int'])),
                                        ('reg_off_value', (YLeaf(YType.str, 'reg_off_value'), ['str'])),
                                    ])
                                    self.iofpga_reg_off_addr = None
                                    self.reg_off_value = None
                                    self._segment_path = lambda: "iofpga_reg_offset_data"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaOffset.IofpgaRegOffsetData, [u'iofpga_reg_off_addr', u'reg_off_value'], name, value)




                        class IofpgaAddress(Entity):
                            """
                            
                            
                            .. attribute:: start_hex_addr  (key)
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: end_hex_addr  (key)
                            
                            	
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: iofpga_reg_range_addr_list
                            
                            	
                            	**type**\: list of  		 :py:class:`IofpgaRegRangeAddrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaAddress, self).__init__()

                                self.yang_name = "iofpga_address"
                                self.yang_parent_name = "register_location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['start_hex_addr','end_hex_addr']
                                self._child_classes = OrderedDict([("iofpga_reg_range_addr_list", ("iofpga_reg_range_addr_list", Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList))])
                                self._leafs = OrderedDict([
                                    ('start_hex_addr', (YLeaf(YType.str, 'start_hex_addr'), ['str'])),
                                    ('end_hex_addr', (YLeaf(YType.str, 'end_hex_addr'), ['str'])),
                                ])
                                self.start_hex_addr = None
                                self.end_hex_addr = None

                                self.iofpga_reg_range_addr_list = YList(self)
                                self._segment_path = lambda: "iofpga_address" + "[start_hex_addr='" + str(self.start_hex_addr) + "']" + "[end_hex_addr='" + str(self.end_hex_addr) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaAddress, [u'start_hex_addr', u'end_hex_addr'], name, value)


                            class IofpgaRegRangeAddrList(Entity):
                                """
                                
                                
                                .. attribute:: iofpga_reg_range_addr  (key)
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: iofpga_reg_data
                                
                                	
                                	**type**\: list of  		 :py:class:`IofpgaRegData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList.IofpgaRegData>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'calvados_controllers'
                                _revision = '2017-10-11'

                                def __init__(self):
                                    super(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList, self).__init__()

                                    self.yang_name = "iofpga_reg_range_addr_list"
                                    self.yang_parent_name = "iofpga_address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['iofpga_reg_range_addr']
                                    self._child_classes = OrderedDict([("iofpga_reg_data", ("iofpga_reg_data", Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList.IofpgaRegData))])
                                    self._leafs = OrderedDict([
                                        ('iofpga_reg_range_addr', (YLeaf(YType.uint32, 'iofpga_reg_range_addr'), ['int'])),
                                    ])
                                    self.iofpga_reg_range_addr = None

                                    self.iofpga_reg_data = YList(self)
                                    self._segment_path = lambda: "iofpga_reg_range_addr_list" + "[iofpga_reg_range_addr='" + str(self.iofpga_reg_range_addr) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList, [u'iofpga_reg_range_addr'], name, value)


                                class IofpgaRegData(Entity):
                                    """
                                    
                                    
                                    .. attribute:: iofpga_reg_addr
                                    
                                    	
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: reg_value
                                    
                                    	
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'calvados_controllers'
                                    _revision = '2017-10-11'

                                    def __init__(self):
                                        super(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList.IofpgaRegData, self).__init__()

                                        self.yang_name = "iofpga_reg_data"
                                        self.yang_parent_name = "iofpga_reg_range_addr_list"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('iofpga_reg_addr', (YLeaf(YType.uint32, 'iofpga_reg_addr'), ['int'])),
                                            ('reg_value', (YLeaf(YType.str, 'reg_value'), ['str'])),
                                        ])
                                        self.iofpga_reg_addr = None
                                        self.reg_value = None
                                        self._segment_path = lambda: "iofpga_reg_data"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Controller.CardMgr.Iofpga.Register.Dc.RegisterLocation.IofpgaAddress.IofpgaRegRangeAddrList.IofpgaRegData, [u'iofpga_reg_addr', u'reg_value'], name, value)








            class Flash(Entity):
                """
                
                
                .. attribute:: info
                
                	
                	**type**\:  :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Flash.Info>`
                
                	**config**\: False
                
                .. attribute:: status
                
                	
                	**type**\:  :py:class:`Status <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Flash.Status>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Controller.CardMgr.Iofpga.Flash, self).__init__()

                    self.yang_name = "flash"
                    self.yang_parent_name = "iofpga"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("info", ("info", Controller.CardMgr.Iofpga.Flash.Info)), ("status", ("status", Controller.CardMgr.Iofpga.Flash.Status))])
                    self._leafs = OrderedDict()

                    self.info = Controller.CardMgr.Iofpga.Flash.Info()
                    self.info.parent = self
                    self._children_name_map["info"] = "info"

                    self.status = Controller.CardMgr.Iofpga.Flash.Status()
                    self.status.parent = self
                    self._children_name_map["status"] = "status"
                    self._segment_path = lambda: "flash"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/iofpga/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.CardMgr.Iofpga.Flash, [], name, value)


                class Info(Entity):
                    """
                    
                    
                    .. attribute:: flash_location
                    
                    	
                    	**type**\: list of  		 :py:class:`FlashLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Flash.Info.FlashLocation>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.CardMgr.Iofpga.Flash.Info, self).__init__()

                        self.yang_name = "info"
                        self.yang_parent_name = "flash"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("flash_location", ("flash_location", Controller.CardMgr.Iofpga.Flash.Info.FlashLocation))])
                        self._leafs = OrderedDict()

                        self.flash_location = YList(self)
                        self._segment_path = lambda: "info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/iofpga/flash/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.CardMgr.Iofpga.Flash.Info, [], name, value)


                    class FlashLocation(Entity):
                        """
                        
                        
                        .. attribute:: flash_location  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        .. attribute:: iofpga_flash_info
                        
                        	
                        	**type**\:  :py:class:`IofpgaFlashInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Flash.Info.FlashLocation.IofpgaFlashInfo>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.CardMgr.Iofpga.Flash.Info.FlashLocation, self).__init__()

                            self.yang_name = "flash_location"
                            self.yang_parent_name = "info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['flash_location']
                            self._child_classes = OrderedDict([("iofpga_flash_info", ("iofpga_flash_info", Controller.CardMgr.Iofpga.Flash.Info.FlashLocation.IofpgaFlashInfo))])
                            self._leafs = OrderedDict([
                                ('flash_location', (YLeaf(YType.str, 'flash_location'), ['str'])),
                            ])
                            self.flash_location = None

                            self.iofpga_flash_info = Controller.CardMgr.Iofpga.Flash.Info.FlashLocation.IofpgaFlashInfo()
                            self.iofpga_flash_info.parent = self
                            self._children_name_map["iofpga_flash_info"] = "iofpga_flash_info"
                            self._segment_path = lambda: "flash_location" + "[flash_location='" + str(self.flash_location) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/iofpga/flash/info/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.CardMgr.Iofpga.Flash.Info.FlashLocation, [u'flash_location'], name, value)


                        class IofpgaFlashInfo(Entity):
                            """
                            
                            
                            .. attribute:: iofpga_flash_info_values
                            
                            	
                            	**type**\: list of str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.CardMgr.Iofpga.Flash.Info.FlashLocation.IofpgaFlashInfo, self).__init__()

                                self.yang_name = "iofpga_flash_info"
                                self.yang_parent_name = "flash_location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('iofpga_flash_info_values', (YLeafList(YType.str, 'iofpga_flash_info_values'), ['str'])),
                                ])
                                self.iofpga_flash_info_values = []
                                self._segment_path = lambda: "iofpga_flash_info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.CardMgr.Iofpga.Flash.Info.FlashLocation.IofpgaFlashInfo, [u'iofpga_flash_info_values'], name, value)





                class Status(Entity):
                    """
                    
                    
                    .. attribute:: flash_location
                    
                    	
                    	**type**\: list of  		 :py:class:`FlashLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Flash.Status.FlashLocation>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.CardMgr.Iofpga.Flash.Status, self).__init__()

                        self.yang_name = "status"
                        self.yang_parent_name = "flash"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("flash_location", ("flash_location", Controller.CardMgr.Iofpga.Flash.Status.FlashLocation))])
                        self._leafs = OrderedDict()

                        self.flash_location = YList(self)
                        self._segment_path = lambda: "status"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/iofpga/flash/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.CardMgr.Iofpga.Flash.Status, [], name, value)


                    class FlashLocation(Entity):
                        """
                        
                        
                        .. attribute:: flash_location  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        .. attribute:: iofpga_flash_status
                        
                        	
                        	**type**\:  :py:class:`IofpgaFlashStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Iofpga.Flash.Status.FlashLocation.IofpgaFlashStatus>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.CardMgr.Iofpga.Flash.Status.FlashLocation, self).__init__()

                            self.yang_name = "flash_location"
                            self.yang_parent_name = "status"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['flash_location']
                            self._child_classes = OrderedDict([("iofpga_flash_status", ("iofpga_flash_status", Controller.CardMgr.Iofpga.Flash.Status.FlashLocation.IofpgaFlashStatus))])
                            self._leafs = OrderedDict([
                                ('flash_location', (YLeaf(YType.str, 'flash_location'), ['str'])),
                            ])
                            self.flash_location = None

                            self.iofpga_flash_status = Controller.CardMgr.Iofpga.Flash.Status.FlashLocation.IofpgaFlashStatus()
                            self.iofpga_flash_status.parent = self
                            self._children_name_map["iofpga_flash_status"] = "iofpga_flash_status"
                            self._segment_path = lambda: "flash_location" + "[flash_location='" + str(self.flash_location) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/iofpga/flash/status/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.CardMgr.Iofpga.Flash.Status.FlashLocation, [u'flash_location'], name, value)


                        class IofpgaFlashStatus(Entity):
                            """
                            
                            
                            .. attribute:: iofpga_flash_status_values
                            
                            	
                            	**type**\: list of str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.CardMgr.Iofpga.Flash.Status.FlashLocation.IofpgaFlashStatus, self).__init__()

                                self.yang_name = "iofpga_flash_status"
                                self.yang_parent_name = "flash_location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('iofpga_flash_status_values', (YLeafList(YType.str, 'iofpga_flash_status_values'), ['str'])),
                                ])
                                self.iofpga_flash_status_values = []
                                self._segment_path = lambda: "iofpga_flash_status"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.CardMgr.Iofpga.Flash.Status.FlashLocation.IofpgaFlashStatus, [u'iofpga_flash_status_values'], name, value)







        class Bootloader(Entity):
            """
            
            
            .. attribute:: flash
            
            	
            	**type**\:  :py:class:`Flash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Bootloader.Flash>`
            
            	**config**\: False
            
            

            """

            _prefix = 'calvados_controllers'
            _revision = '2017-10-11'

            def __init__(self):
                super(Controller.CardMgr.Bootloader, self).__init__()

                self.yang_name = "bootloader"
                self.yang_parent_name = "card_mgr"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("flash", ("flash", Controller.CardMgr.Bootloader.Flash))])
                self._leafs = OrderedDict()

                self.flash = Controller.CardMgr.Bootloader.Flash()
                self.flash.parent = self
                self._children_name_map["flash"] = "flash"
                self._segment_path = lambda: "bootloader"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Controller.CardMgr.Bootloader, [], name, value)


            class Flash(Entity):
                """
                
                
                .. attribute:: info
                
                	
                	**type**\:  :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Bootloader.Flash.Info>`
                
                	**config**\: False
                
                .. attribute:: status
                
                	
                	**type**\:  :py:class:`Status <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Bootloader.Flash.Status>`
                
                	**config**\: False
                
                

                """

                _prefix = 'calvados_controllers'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Controller.CardMgr.Bootloader.Flash, self).__init__()

                    self.yang_name = "flash"
                    self.yang_parent_name = "bootloader"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("info", ("info", Controller.CardMgr.Bootloader.Flash.Info)), ("status", ("status", Controller.CardMgr.Bootloader.Flash.Status))])
                    self._leafs = OrderedDict()

                    self.info = Controller.CardMgr.Bootloader.Flash.Info()
                    self.info.parent = self
                    self._children_name_map["info"] = "info"

                    self.status = Controller.CardMgr.Bootloader.Flash.Status()
                    self.status.parent = self
                    self._children_name_map["status"] = "status"
                    self._segment_path = lambda: "flash"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/bootloader/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Controller.CardMgr.Bootloader.Flash, [], name, value)


                class Info(Entity):
                    """
                    
                    
                    .. attribute:: flash_location
                    
                    	
                    	**type**\: list of  		 :py:class:`FlashLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Bootloader.Flash.Info.FlashLocation>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.CardMgr.Bootloader.Flash.Info, self).__init__()

                        self.yang_name = "info"
                        self.yang_parent_name = "flash"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("flash_location", ("flash_location", Controller.CardMgr.Bootloader.Flash.Info.FlashLocation))])
                        self._leafs = OrderedDict()

                        self.flash_location = YList(self)
                        self._segment_path = lambda: "info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/bootloader/flash/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.CardMgr.Bootloader.Flash.Info, [], name, value)


                    class FlashLocation(Entity):
                        """
                        
                        
                        .. attribute:: flash_location  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        .. attribute:: bootldr_flash_info
                        
                        	
                        	**type**\:  :py:class:`BootldrFlashInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Bootloader.Flash.Info.FlashLocation.BootldrFlashInfo>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.CardMgr.Bootloader.Flash.Info.FlashLocation, self).__init__()

                            self.yang_name = "flash_location"
                            self.yang_parent_name = "info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['flash_location']
                            self._child_classes = OrderedDict([("bootldr_flash_info", ("bootldr_flash_info", Controller.CardMgr.Bootloader.Flash.Info.FlashLocation.BootldrFlashInfo))])
                            self._leafs = OrderedDict([
                                ('flash_location', (YLeaf(YType.str, 'flash_location'), ['str'])),
                            ])
                            self.flash_location = None

                            self.bootldr_flash_info = Controller.CardMgr.Bootloader.Flash.Info.FlashLocation.BootldrFlashInfo()
                            self.bootldr_flash_info.parent = self
                            self._children_name_map["bootldr_flash_info"] = "bootldr_flash_info"
                            self._segment_path = lambda: "flash_location" + "[flash_location='" + str(self.flash_location) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/bootloader/flash/info/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.CardMgr.Bootloader.Flash.Info.FlashLocation, [u'flash_location'], name, value)


                        class BootldrFlashInfo(Entity):
                            """
                            
                            
                            .. attribute:: bootldr_flash_info_values
                            
                            	
                            	**type**\: list of str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.CardMgr.Bootloader.Flash.Info.FlashLocation.BootldrFlashInfo, self).__init__()

                                self.yang_name = "bootldr_flash_info"
                                self.yang_parent_name = "flash_location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('bootldr_flash_info_values', (YLeafList(YType.str, 'bootldr_flash_info_values'), ['str'])),
                                ])
                                self.bootldr_flash_info_values = []
                                self._segment_path = lambda: "bootldr_flash_info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.CardMgr.Bootloader.Flash.Info.FlashLocation.BootldrFlashInfo, [u'bootldr_flash_info_values'], name, value)





                class Status(Entity):
                    """
                    
                    
                    .. attribute:: flash_location
                    
                    	
                    	**type**\: list of  		 :py:class:`FlashLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Bootloader.Flash.Status.FlashLocation>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'calvados_controllers'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Controller.CardMgr.Bootloader.Flash.Status, self).__init__()

                        self.yang_name = "status"
                        self.yang_parent_name = "flash"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("flash_location", ("flash_location", Controller.CardMgr.Bootloader.Flash.Status.FlashLocation))])
                        self._leafs = OrderedDict()

                        self.flash_location = YList(self)
                        self._segment_path = lambda: "status"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/bootloader/flash/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Controller.CardMgr.Bootloader.Flash.Status, [], name, value)


                    class FlashLocation(Entity):
                        """
                        
                        
                        .. attribute:: flash_location  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                        
                        	**config**\: False
                        
                        .. attribute:: bootldr_flash_status
                        
                        	
                        	**type**\:  :py:class:`BootldrFlashStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_controllers_ncs5501.Controller.CardMgr.Bootloader.Flash.Status.FlashLocation.BootldrFlashStatus>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'calvados_controllers'
                        _revision = '2017-10-11'

                        def __init__(self):
                            super(Controller.CardMgr.Bootloader.Flash.Status.FlashLocation, self).__init__()

                            self.yang_name = "flash_location"
                            self.yang_parent_name = "status"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['flash_location']
                            self._child_classes = OrderedDict([("bootldr_flash_status", ("bootldr_flash_status", Controller.CardMgr.Bootloader.Flash.Status.FlashLocation.BootldrFlashStatus))])
                            self._leafs = OrderedDict([
                                ('flash_location', (YLeaf(YType.str, 'flash_location'), ['str'])),
                            ])
                            self.flash_location = None

                            self.bootldr_flash_status = Controller.CardMgr.Bootloader.Flash.Status.FlashLocation.BootldrFlashStatus()
                            self.bootldr_flash_status.parent = self
                            self._children_name_map["bootldr_flash_status"] = "bootldr_flash_status"
                            self._segment_path = lambda: "flash_location" + "[flash_location='" + str(self.flash_location) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-controllers-ncs5501:controller/card_mgr/bootloader/flash/status/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Controller.CardMgr.Bootloader.Flash.Status.FlashLocation, [u'flash_location'], name, value)


                        class BootldrFlashStatus(Entity):
                            """
                            
                            
                            .. attribute:: bootldr_flash_status_values
                            
                            	
                            	**type**\: list of str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'calvados_controllers'
                            _revision = '2017-10-11'

                            def __init__(self):
                                super(Controller.CardMgr.Bootloader.Flash.Status.FlashLocation.BootldrFlashStatus, self).__init__()

                                self.yang_name = "bootldr_flash_status"
                                self.yang_parent_name = "flash_location"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('bootldr_flash_status_values', (YLeafList(YType.str, 'bootldr_flash_status_values'), ['str'])),
                                ])
                                self.bootldr_flash_status_values = []
                                self._segment_path = lambda: "bootldr_flash_status"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Controller.CardMgr.Bootloader.Flash.Status.FlashLocation.BootldrFlashStatus, [u'bootldr_flash_status_values'], name, value)







    def clone_ptr(self):
        self._top_entity = Controller()
        return self._top_entity



