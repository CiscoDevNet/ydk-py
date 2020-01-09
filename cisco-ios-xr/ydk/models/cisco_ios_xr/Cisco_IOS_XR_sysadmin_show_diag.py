""" Cisco_IOS_XR_sysadmin_show_diag 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

This module holds diag data for chassis, card, fan, power.

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




class Diag(_Entity_):
    """
    diag data
    
    .. attribute:: default
    
    	
    	**type**\:  :py:class:`Default <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Default>`
    
    	**config**\: False
    
    .. attribute:: fans
    
    	
    	**type**\:  :py:class:`Fans <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Fans>`
    
    	**config**\: False
    
    .. attribute:: power_supply
    
    	
    	**type**\:  :py:class:`PowerSupply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.PowerSupply>`
    
    	**config**\: False
    
    .. attribute:: chassis
    
    	
    	**type**\:  :py:class:`Chassis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Chassis>`
    
    	**config**\: False
    
    .. attribute:: summary
    
    	
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Summary>`
    
    	**config**\: False
    
    .. attribute:: eeprom
    
    	
    	**type**\:  :py:class:`Eeprom <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Eeprom>`
    
    	**config**\: False
    
    .. attribute:: detail
    
    	
    	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Detail>`
    
    	**config**\: False
    
    

    """

    _prefix = 'show_diag'
    _revision = '2017-04-12'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Diag, self).__init__()
        self._top_entity = None

        self.yang_name = "diag"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-show-diag"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("default", ("default", Diag.Default)), ("fans", ("fans", Diag.Fans)), ("power-supply", ("power_supply", Diag.PowerSupply)), ("chassis", ("chassis", Diag.Chassis)), ("summary", ("summary", Diag.Summary)), ("eeprom", ("eeprom", Diag.Eeprom)), ("detail", ("detail", Diag.Detail))])
        self._leafs = OrderedDict()

        self.default = Diag.Default()
        self.default.parent = self
        self._children_name_map["default"] = "default"

        self.fans = Diag.Fans()
        self.fans.parent = self
        self._children_name_map["fans"] = "fans"

        self.power_supply = Diag.PowerSupply()
        self.power_supply.parent = self
        self._children_name_map["power_supply"] = "power-supply"

        self.chassis = Diag.Chassis()
        self.chassis.parent = self
        self._children_name_map["chassis"] = "chassis"

        self.summary = Diag.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"

        self.eeprom = Diag.Eeprom()
        self.eeprom.parent = self
        self._children_name_map["eeprom"] = "eeprom"

        self.detail = Diag.Detail()
        self.detail.parent = self
        self._children_name_map["detail"] = "detail"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Diag, [], name, value)


    class Default(_Entity_):
        """
        
        
        .. attribute:: default_list
        
        	
        	**type**\: list of  		 :py:class:`DefaultList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Default.DefaultList>`
        
        	**config**\: False
        
        

        """

        _prefix = 'show_diag'
        _revision = '2017-04-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Diag.Default, self).__init__()

            self.yang_name = "default"
            self.yang_parent_name = "diag"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("default_list", ("default_list", Diag.Default.DefaultList))])
            self._leafs = OrderedDict()

            self.default_list = YList(self)
            self._segment_path = lambda: "default"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Diag.Default, [], name, value)


        class DefaultList(_Entity_):
            """
            
            
            .. attribute:: location  (key)
            
            	
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: default_data
            
            	
            	**type**\:  :py:class:`DefaultData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Default.DefaultList.DefaultData>`
            
            	**config**\: False
            
            

            """

            _prefix = 'show_diag'
            _revision = '2017-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Diag.Default.DefaultList, self).__init__()

                self.yang_name = "default_list"
                self.yang_parent_name = "default"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['location']
                self._child_classes = OrderedDict([("default-data", ("default_data", Diag.Default.DefaultList.DefaultData))])
                self._leafs = OrderedDict([
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ])
                self.location = None

                self.default_data = Diag.Default.DefaultList.DefaultData()
                self.default_data.parent = self
                self._children_name_map["default_data"] = "default-data"
                self._segment_path = lambda: "default_list" + "[location='" + str(self.location) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag/default/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Diag.Default.DefaultList, ['location'], name, value)


            class DefaultData(_Entity_):
                """
                
                
                .. attribute:: default_out_list
                
                	
                	**type**\: list of str
                
                	**config**\: False
                
                

                """

                _prefix = 'show_diag'
                _revision = '2017-04-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Diag.Default.DefaultList.DefaultData, self).__init__()

                    self.yang_name = "default-data"
                    self.yang_parent_name = "default_list"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('default_out_list', (YLeafList(YType.str, 'default_out_list'), ['str'])),
                    ])
                    self.default_out_list = []
                    self._segment_path = lambda: "default-data"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Default.DefaultList.DefaultData, ['default_out_list'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                    return meta._meta_table['Diag.Default.DefaultList.DefaultData']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                return meta._meta_table['Diag.Default.DefaultList']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
            return meta._meta_table['Diag.Default']['meta_info']


    class Fans(_Entity_):
        """
        
        
        .. attribute:: fans_list
        
        	
        	**type**\: list of  		 :py:class:`FansList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Fans.FansList>`
        
        	**config**\: False
        
        

        """

        _prefix = 'show_diag'
        _revision = '2017-04-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Diag.Fans, self).__init__()

            self.yang_name = "fans"
            self.yang_parent_name = "diag"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("fans_list", ("fans_list", Diag.Fans.FansList))])
            self._leafs = OrderedDict()

            self.fans_list = YList(self)
            self._segment_path = lambda: "fans"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Diag.Fans, [], name, value)


        class FansList(_Entity_):
            """
            
            
            .. attribute:: location  (key)
            
            	
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: default_data
            
            	
            	**type**\:  :py:class:`DefaultData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Fans.FansList.DefaultData>`
            
            	**config**\: False
            
            

            """

            _prefix = 'show_diag'
            _revision = '2017-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Diag.Fans.FansList, self).__init__()

                self.yang_name = "fans_list"
                self.yang_parent_name = "fans"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['location']
                self._child_classes = OrderedDict([("default-data", ("default_data", Diag.Fans.FansList.DefaultData))])
                self._leafs = OrderedDict([
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ])
                self.location = None

                self.default_data = Diag.Fans.FansList.DefaultData()
                self.default_data.parent = self
                self._children_name_map["default_data"] = "default-data"
                self._segment_path = lambda: "fans_list" + "[location='" + str(self.location) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag/fans/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Diag.Fans.FansList, ['location'], name, value)


            class DefaultData(_Entity_):
                """
                
                
                .. attribute:: default_out_list
                
                	
                	**type**\: list of str
                
                	**config**\: False
                
                

                """

                _prefix = 'show_diag'
                _revision = '2017-04-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Diag.Fans.FansList.DefaultData, self).__init__()

                    self.yang_name = "default-data"
                    self.yang_parent_name = "fans_list"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('default_out_list', (YLeafList(YType.str, 'default_out_list'), ['str'])),
                    ])
                    self.default_out_list = []
                    self._segment_path = lambda: "default-data"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Fans.FansList.DefaultData, ['default_out_list'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                    return meta._meta_table['Diag.Fans.FansList.DefaultData']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                return meta._meta_table['Diag.Fans.FansList']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
            return meta._meta_table['Diag.Fans']['meta_info']


    class PowerSupply(_Entity_):
        """
        
        
        .. attribute:: pwr_list
        
        	
        	**type**\: list of  		 :py:class:`PwrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.PowerSupply.PwrList>`
        
        	**config**\: False
        
        

        """

        _prefix = 'show_diag'
        _revision = '2017-04-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Diag.PowerSupply, self).__init__()

            self.yang_name = "power-supply"
            self.yang_parent_name = "diag"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pwr_list", ("pwr_list", Diag.PowerSupply.PwrList))])
            self._leafs = OrderedDict()

            self.pwr_list = YList(self)
            self._segment_path = lambda: "power-supply"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Diag.PowerSupply, [], name, value)


        class PwrList(_Entity_):
            """
            
            
            .. attribute:: location  (key)
            
            	
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: default_data
            
            	
            	**type**\:  :py:class:`DefaultData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.PowerSupply.PwrList.DefaultData>`
            
            	**config**\: False
            
            

            """

            _prefix = 'show_diag'
            _revision = '2017-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Diag.PowerSupply.PwrList, self).__init__()

                self.yang_name = "pwr_list"
                self.yang_parent_name = "power-supply"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['location']
                self._child_classes = OrderedDict([("default-data", ("default_data", Diag.PowerSupply.PwrList.DefaultData))])
                self._leafs = OrderedDict([
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ])
                self.location = None

                self.default_data = Diag.PowerSupply.PwrList.DefaultData()
                self.default_data.parent = self
                self._children_name_map["default_data"] = "default-data"
                self._segment_path = lambda: "pwr_list" + "[location='" + str(self.location) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag/power-supply/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Diag.PowerSupply.PwrList, ['location'], name, value)


            class DefaultData(_Entity_):
                """
                
                
                .. attribute:: default_out_list
                
                	
                	**type**\: list of str
                
                	**config**\: False
                
                

                """

                _prefix = 'show_diag'
                _revision = '2017-04-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Diag.PowerSupply.PwrList.DefaultData, self).__init__()

                    self.yang_name = "default-data"
                    self.yang_parent_name = "pwr_list"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('default_out_list', (YLeafList(YType.str, 'default_out_list'), ['str'])),
                    ])
                    self.default_out_list = []
                    self._segment_path = lambda: "default-data"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.PowerSupply.PwrList.DefaultData, ['default_out_list'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                    return meta._meta_table['Diag.PowerSupply.PwrList.DefaultData']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                return meta._meta_table['Diag.PowerSupply.PwrList']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
            return meta._meta_table['Diag.PowerSupply']['meta_info']


    class Chassis(_Entity_):
        """
        
        
        .. attribute:: chassis_cnt
        
        	
        	**type**\:  :py:class:`ChassisCnt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Chassis.ChassisCnt>`
        
        	**config**\: False
        
        .. attribute:: chassis_eeprom_cnt
        
        	
        	**type**\:  :py:class:`ChassisEepromCnt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Chassis.ChassisEepromCnt>`
        
        	**config**\: False
        
        

        """

        _prefix = 'show_diag'
        _revision = '2017-04-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Diag.Chassis, self).__init__()

            self.yang_name = "chassis"
            self.yang_parent_name = "diag"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("chassis_cnt", ("chassis_cnt", Diag.Chassis.ChassisCnt)), ("chassis_eeprom_cnt", ("chassis_eeprom_cnt", Diag.Chassis.ChassisEepromCnt))])
            self._leafs = OrderedDict()

            self.chassis_cnt = Diag.Chassis.ChassisCnt()
            self.chassis_cnt.parent = self
            self._children_name_map["chassis_cnt"] = "chassis_cnt"

            self.chassis_eeprom_cnt = Diag.Chassis.ChassisEepromCnt()
            self.chassis_eeprom_cnt.parent = self
            self._children_name_map["chassis_eeprom_cnt"] = "chassis_eeprom_cnt"
            self._segment_path = lambda: "chassis"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Diag.Chassis, [], name, value)


        class ChassisCnt(_Entity_):
            """
            
            
            .. attribute:: chassis_list
            
            	
            	**type**\: list of  		 :py:class:`ChassisList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Chassis.ChassisCnt.ChassisList>`
            
            	**config**\: False
            
            

            """

            _prefix = 'show_diag'
            _revision = '2017-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Diag.Chassis.ChassisCnt, self).__init__()

                self.yang_name = "chassis_cnt"
                self.yang_parent_name = "chassis"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("chassis_list", ("chassis_list", Diag.Chassis.ChassisCnt.ChassisList))])
                self._leafs = OrderedDict()

                self.chassis_list = YList(self)
                self._segment_path = lambda: "chassis_cnt"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag/chassis/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Diag.Chassis.ChassisCnt, [], name, value)


            class ChassisList(_Entity_):
                """
                
                
                .. attribute:: location  (key)
                
                	
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: default_data
                
                	
                	**type**\:  :py:class:`DefaultData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Chassis.ChassisCnt.ChassisList.DefaultData>`
                
                	**config**\: False
                
                

                """

                _prefix = 'show_diag'
                _revision = '2017-04-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Diag.Chassis.ChassisCnt.ChassisList, self).__init__()

                    self.yang_name = "chassis_list"
                    self.yang_parent_name = "chassis_cnt"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['location']
                    self._child_classes = OrderedDict([("default-data", ("default_data", Diag.Chassis.ChassisCnt.ChassisList.DefaultData))])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ])
                    self.location = None

                    self.default_data = Diag.Chassis.ChassisCnt.ChassisList.DefaultData()
                    self.default_data.parent = self
                    self._children_name_map["default_data"] = "default-data"
                    self._segment_path = lambda: "chassis_list" + "[location='" + str(self.location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag/chassis/chassis_cnt/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Chassis.ChassisCnt.ChassisList, ['location'], name, value)


                class DefaultData(_Entity_):
                    """
                    
                    
                    .. attribute:: default_out_list
                    
                    	
                    	**type**\: list of str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'show_diag'
                    _revision = '2017-04-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Diag.Chassis.ChassisCnt.ChassisList.DefaultData, self).__init__()

                        self.yang_name = "default-data"
                        self.yang_parent_name = "chassis_list"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('default_out_list', (YLeafList(YType.str, 'default_out_list'), ['str'])),
                        ])
                        self.default_out_list = []
                        self._segment_path = lambda: "default-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diag.Chassis.ChassisCnt.ChassisList.DefaultData, ['default_out_list'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                        return meta._meta_table['Diag.Chassis.ChassisCnt.ChassisList.DefaultData']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                    return meta._meta_table['Diag.Chassis.ChassisCnt.ChassisList']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                return meta._meta_table['Diag.Chassis.ChassisCnt']['meta_info']


        class ChassisEepromCnt(_Entity_):
            """
            
            
            .. attribute:: chassis_eeprom_list
            
            	
            	**type**\: list of  		 :py:class:`ChassisEepromList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Chassis.ChassisEepromCnt.ChassisEepromList>`
            
            	**config**\: False
            
            

            """

            _prefix = 'show_diag'
            _revision = '2017-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Diag.Chassis.ChassisEepromCnt, self).__init__()

                self.yang_name = "chassis_eeprom_cnt"
                self.yang_parent_name = "chassis"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("chassis_eeprom_list", ("chassis_eeprom_list", Diag.Chassis.ChassisEepromCnt.ChassisEepromList))])
                self._leafs = OrderedDict()

                self.chassis_eeprom_list = YList(self)
                self._segment_path = lambda: "chassis_eeprom_cnt"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag/chassis/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Diag.Chassis.ChassisEepromCnt, [], name, value)


            class ChassisEepromList(_Entity_):
                """
                
                
                .. attribute:: location  (key)
                
                	
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: eeprom_data
                
                	
                	**type**\:  :py:class:`EepromData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Chassis.ChassisEepromCnt.ChassisEepromList.EepromData>`
                
                	**config**\: False
                
                

                """

                _prefix = 'show_diag'
                _revision = '2017-04-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Diag.Chassis.ChassisEepromCnt.ChassisEepromList, self).__init__()

                    self.yang_name = "chassis_eeprom_list"
                    self.yang_parent_name = "chassis_eeprom_cnt"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['location']
                    self._child_classes = OrderedDict([("eeprom-data", ("eeprom_data", Diag.Chassis.ChassisEepromCnt.ChassisEepromList.EepromData))])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ])
                    self.location = None

                    self.eeprom_data = Diag.Chassis.ChassisEepromCnt.ChassisEepromList.EepromData()
                    self.eeprom_data.parent = self
                    self._children_name_map["eeprom_data"] = "eeprom-data"
                    self._segment_path = lambda: "chassis_eeprom_list" + "[location='" + str(self.location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag/chassis/chassis_eeprom_cnt/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Chassis.ChassisEepromCnt.ChassisEepromList, ['location'], name, value)


                class EepromData(_Entity_):
                    """
                    
                    
                    .. attribute:: raw_list
                    
                    	
                    	**type**\: list of str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'show_diag'
                    _revision = '2017-04-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Diag.Chassis.ChassisEepromCnt.ChassisEepromList.EepromData, self).__init__()

                        self.yang_name = "eeprom-data"
                        self.yang_parent_name = "chassis_eeprom_list"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('raw_list', (YLeafList(YType.str, 'raw_list'), ['str'])),
                        ])
                        self.raw_list = []
                        self._segment_path = lambda: "eeprom-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diag.Chassis.ChassisEepromCnt.ChassisEepromList.EepromData, ['raw_list'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                        return meta._meta_table['Diag.Chassis.ChassisEepromCnt.ChassisEepromList.EepromData']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                    return meta._meta_table['Diag.Chassis.ChassisEepromCnt.ChassisEepromList']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                return meta._meta_table['Diag.Chassis.ChassisEepromCnt']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
            return meta._meta_table['Diag.Chassis']['meta_info']


    class Summary(_Entity_):
        """
        
        
        .. attribute:: summary_list
        
        	
        	**type**\: list of  		 :py:class:`SummaryList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Summary.SummaryList>`
        
        	**config**\: False
        
        

        """

        _prefix = 'show_diag'
        _revision = '2017-04-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Diag.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "diag"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("summary_list", ("summary_list", Diag.Summary.SummaryList))])
            self._leafs = OrderedDict()

            self.summary_list = YList(self)
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Diag.Summary, [], name, value)


        class SummaryList(_Entity_):
            """
            
            
            .. attribute:: location  (key)
            
            	
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: summary_data
            
            	
            	**type**\:  :py:class:`SummaryData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Summary.SummaryList.SummaryData>`
            
            	**config**\: False
            
            

            """

            _prefix = 'show_diag'
            _revision = '2017-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Diag.Summary.SummaryList, self).__init__()

                self.yang_name = "summary_list"
                self.yang_parent_name = "summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['location']
                self._child_classes = OrderedDict([("summary-data", ("summary_data", Diag.Summary.SummaryList.SummaryData))])
                self._leafs = OrderedDict([
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ])
                self.location = None

                self.summary_data = Diag.Summary.SummaryList.SummaryData()
                self.summary_data.parent = self
                self._children_name_map["summary_data"] = "summary-data"
                self._segment_path = lambda: "summary_list" + "[location='" + str(self.location) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag/summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Diag.Summary.SummaryList, ['location'], name, value)


            class SummaryData(_Entity_):
                """
                
                
                .. attribute:: summary_out_list
                
                	
                	**type**\: list of str
                
                	**config**\: False
                
                

                """

                _prefix = 'show_diag'
                _revision = '2017-04-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Diag.Summary.SummaryList.SummaryData, self).__init__()

                    self.yang_name = "summary-data"
                    self.yang_parent_name = "summary_list"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('summary_out_list', (YLeafList(YType.str, 'summary_out_list'), ['str'])),
                    ])
                    self.summary_out_list = []
                    self._segment_path = lambda: "summary-data"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Summary.SummaryList.SummaryData, ['summary_out_list'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                    return meta._meta_table['Diag.Summary.SummaryList.SummaryData']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                return meta._meta_table['Diag.Summary.SummaryList']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
            return meta._meta_table['Diag.Summary']['meta_info']


    class Eeprom(_Entity_):
        """
        
        
        .. attribute:: eeprom_list
        
        	
        	**type**\: list of  		 :py:class:`EepromList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Eeprom.EepromList>`
        
        	**config**\: False
        
        

        """

        _prefix = 'show_diag'
        _revision = '2017-04-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Diag.Eeprom, self).__init__()

            self.yang_name = "eeprom"
            self.yang_parent_name = "diag"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("eeprom_list", ("eeprom_list", Diag.Eeprom.EepromList))])
            self._leafs = OrderedDict()

            self.eeprom_list = YList(self)
            self._segment_path = lambda: "eeprom"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Diag.Eeprom, [], name, value)


        class EepromList(_Entity_):
            """
            
            
            .. attribute:: location  (key)
            
            	
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: eeprom_data
            
            	
            	**type**\:  :py:class:`EepromData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Eeprom.EepromList.EepromData>`
            
            	**config**\: False
            
            

            """

            _prefix = 'show_diag'
            _revision = '2017-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Diag.Eeprom.EepromList, self).__init__()

                self.yang_name = "eeprom_list"
                self.yang_parent_name = "eeprom"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['location']
                self._child_classes = OrderedDict([("eeprom-data", ("eeprom_data", Diag.Eeprom.EepromList.EepromData))])
                self._leafs = OrderedDict([
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ])
                self.location = None

                self.eeprom_data = Diag.Eeprom.EepromList.EepromData()
                self.eeprom_data.parent = self
                self._children_name_map["eeprom_data"] = "eeprom-data"
                self._segment_path = lambda: "eeprom_list" + "[location='" + str(self.location) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag/eeprom/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Diag.Eeprom.EepromList, ['location'], name, value)


            class EepromData(_Entity_):
                """
                
                
                .. attribute:: raw_list
                
                	
                	**type**\: list of str
                
                	**config**\: False
                
                

                """

                _prefix = 'show_diag'
                _revision = '2017-04-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Diag.Eeprom.EepromList.EepromData, self).__init__()

                    self.yang_name = "eeprom-data"
                    self.yang_parent_name = "eeprom_list"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('raw_list', (YLeafList(YType.str, 'raw_list'), ['str'])),
                    ])
                    self.raw_list = []
                    self._segment_path = lambda: "eeprom-data"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Eeprom.EepromList.EepromData, ['raw_list'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                    return meta._meta_table['Diag.Eeprom.EepromList.EepromData']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                return meta._meta_table['Diag.Eeprom.EepromList']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
            return meta._meta_table['Diag.Eeprom']['meta_info']


    class Detail(_Entity_):
        """
        
        
        .. attribute:: detail_list
        
        	
        	**type**\: list of  		 :py:class:`DetailList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Detail.DetailList>`
        
        	**config**\: False
        
        

        """

        _prefix = 'show_diag'
        _revision = '2017-04-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Diag.Detail, self).__init__()

            self.yang_name = "detail"
            self.yang_parent_name = "diag"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("detail_list", ("detail_list", Diag.Detail.DetailList))])
            self._leafs = OrderedDict()

            self.detail_list = YList(self)
            self._segment_path = lambda: "detail"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Diag.Detail, [], name, value)


        class DetailList(_Entity_):
            """
            
            
            .. attribute:: location  (key)
            
            	
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: detail_data
            
            	
            	**type**\:  :py:class:`DetailData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_diag.Diag.Detail.DetailList.DetailData>`
            
            	**config**\: False
            
            

            """

            _prefix = 'show_diag'
            _revision = '2017-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Diag.Detail.DetailList, self).__init__()

                self.yang_name = "detail_list"
                self.yang_parent_name = "detail"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['location']
                self._child_classes = OrderedDict([("detail-data", ("detail_data", Diag.Detail.DetailList.DetailData))])
                self._leafs = OrderedDict([
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ])
                self.location = None

                self.detail_data = Diag.Detail.DetailList.DetailData()
                self.detail_data.parent = self
                self._children_name_map["detail_data"] = "detail-data"
                self._segment_path = lambda: "detail_list" + "[location='" + str(self.location) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-diag:diag/detail/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Diag.Detail.DetailList, ['location'], name, value)


            class DetailData(_Entity_):
                """
                
                
                .. attribute:: detail_out_list
                
                	
                	**type**\: list of str
                
                	**config**\: False
                
                

                """

                _prefix = 'show_diag'
                _revision = '2017-04-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Diag.Detail.DetailList.DetailData, self).__init__()

                    self.yang_name = "detail-data"
                    self.yang_parent_name = "detail_list"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('detail_out_list', (YLeafList(YType.str, 'detail_out_list'), ['str'])),
                    ])
                    self.detail_out_list = []
                    self._segment_path = lambda: "detail-data"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Detail.DetailList.DetailData, ['detail_out_list'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                    return meta._meta_table['Diag.Detail.DetailList.DetailData']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
                return meta._meta_table['Diag.Detail.DetailList']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
            return meta._meta_table['Diag.Detail']['meta_info']

    def clone_ptr(self):
        self._top_entity = Diag()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_diag as meta
        return meta._meta_table['Diag']['meta_info']


