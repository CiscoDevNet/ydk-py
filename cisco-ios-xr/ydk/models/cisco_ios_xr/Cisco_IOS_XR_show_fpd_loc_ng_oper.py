""" Cisco_IOS_XR_show_fpd_loc_ng_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR show\-fpd\-loc\-ng package operational data.

This module contains definitions
for the following management objects\:
  show\-fpd\: Show hw\-module fpd

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ShowFpd(Entity):
    """
    Show hw\-module fpd
    
    .. attribute:: locations
    
    	location table
    	**type**\:  :py:class:`Locations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.Locations>`
    
    .. attribute:: hw_module_fpd
    
    	Display fpds on all locations \-show hw\-module fpd
    	**type**\:  :py:class:`HwModuleFpd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HwModuleFpd>`
    
    .. attribute:: help_locations
    
    	help location table
    	**type**\:  :py:class:`HelpLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HelpLocations>`
    
    .. attribute:: hw_module_fpd_help_fpd
    
    	Display help\-fpd \-show hw\-module fpd help\-fpd
    	**type**\:  :py:class:`HwModuleFpdHelpFpd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HwModuleFpdHelpFpd>`
    
    .. attribute:: package
    
    	gets fpd package info
    	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.Package>`
    
    .. attribute:: location_help
    
    	fpd upgradable locations
    	**type**\:  :py:class:`LocationHelp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.LocationHelp>`
    
    

    """

    _prefix = 'show-fpd-loc-ng-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(ShowFpd, self).__init__()
        self._top_entity = None

        self.yang_name = "show-fpd"
        self.yang_parent_name = "Cisco-IOS-XR-show-fpd-loc-ng-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("locations", ("locations", ShowFpd.Locations)), ("hw-module-fpd", ("hw_module_fpd", ShowFpd.HwModuleFpd)), ("help-locations", ("help_locations", ShowFpd.HelpLocations)), ("hw-module-fpd-help-fpd", ("hw_module_fpd_help_fpd", ShowFpd.HwModuleFpdHelpFpd)), ("package", ("package", ShowFpd.Package)), ("location-help", ("location_help", ShowFpd.LocationHelp))])
        self._leafs = OrderedDict()

        self.locations = ShowFpd.Locations()
        self.locations.parent = self
        self._children_name_map["locations"] = "locations"

        self.hw_module_fpd = ShowFpd.HwModuleFpd()
        self.hw_module_fpd.parent = self
        self._children_name_map["hw_module_fpd"] = "hw-module-fpd"

        self.help_locations = ShowFpd.HelpLocations()
        self.help_locations.parent = self
        self._children_name_map["help_locations"] = "help-locations"

        self.hw_module_fpd_help_fpd = ShowFpd.HwModuleFpdHelpFpd()
        self.hw_module_fpd_help_fpd.parent = self
        self._children_name_map["hw_module_fpd_help_fpd"] = "hw-module-fpd-help-fpd"

        self.package = ShowFpd.Package()
        self.package.parent = self
        self._children_name_map["package"] = "package"

        self.location_help = ShowFpd.LocationHelp()
        self.location_help.parent = self
        self._children_name_map["location_help"] = "location-help"
        self._segment_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ShowFpd, [], name, value)


    class Locations(Entity):
        """
        location table
        
        .. attribute:: location
        
        	location
        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.Locations.Location>`
        
        

        """

        _prefix = 'show-fpd-loc-ng-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(ShowFpd.Locations, self).__init__()

            self.yang_name = "locations"
            self.yang_parent_name = "show-fpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("location", ("location", ShowFpd.Locations.Location))])
            self._leafs = OrderedDict()

            self.location = YList(self)
            self._segment_path = lambda: "locations"
            self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ShowFpd.Locations, [], name, value)


        class Location(Entity):
            """
            location
            
            .. attribute:: location_name  (key)
            
            	Fpd location
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: details
            
            	Display fpds on given locations
            	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.Locations.Location.Details>`
            
            

            """

            _prefix = 'show-fpd-loc-ng-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(ShowFpd.Locations.Location, self).__init__()

                self.yang_name = "location"
                self.yang_parent_name = "locations"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['location_name']
                self._child_classes = OrderedDict([("details", ("details", ShowFpd.Locations.Location.Details))])
                self._leafs = OrderedDict([
                    ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                ])
                self.location_name = None

                self.details = ShowFpd.Locations.Location.Details()
                self.details.parent = self
                self._children_name_map["details"] = "details"
                self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/locations/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ShowFpd.Locations.Location, ['location_name'], name, value)


            class Details(Entity):
                """
                Display fpds on given locations
                
                .. attribute:: detail
                
                	Display fpds detail
                	**type**\: list of  		 :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.Locations.Location.Details.Detail>`
                
                

                """

                _prefix = 'show-fpd-loc-ng-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(ShowFpd.Locations.Location.Details, self).__init__()

                    self.yang_name = "details"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("detail", ("detail", ShowFpd.Locations.Location.Details.Detail))])
                    self._leafs = OrderedDict()

                    self.detail = YList(self)
                    self._segment_path = lambda: "details"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ShowFpd.Locations.Location.Details, [], name, value)


                class Detail(Entity):
                    """
                    Display fpds detail
                    
                    .. attribute:: fpd_name  (key)
                    
                    	Fpd Name
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: upgrade_status
                    
                    	Either Upgrading or free used by CTC 
                    	**type**\: str
                    
                    .. attribute:: fpd_info_detaile
                    
                    	 fpd list with all detailes
                    	**type**\: list of  		 :py:class:`FpdInfoDetaile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.Locations.Location.Details.Detail.FpdInfoDetaile>`
                    
                    

                    """

                    _prefix = 'show-fpd-loc-ng-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ShowFpd.Locations.Location.Details.Detail, self).__init__()

                        self.yang_name = "detail"
                        self.yang_parent_name = "details"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['fpd_name']
                        self._child_classes = OrderedDict([("fpd-info-detaile", ("fpd_info_detaile", ShowFpd.Locations.Location.Details.Detail.FpdInfoDetaile))])
                        self._leafs = OrderedDict([
                            ('fpd_name', (YLeaf(YType.str, 'fpd-name'), ['str'])),
                            ('upgrade_status', (YLeaf(YType.str, 'upgrade-status'), ['str'])),
                        ])
                        self.fpd_name = None
                        self.upgrade_status = None

                        self.fpd_info_detaile = YList(self)
                        self._segment_path = lambda: "detail" + "[fpd-name='" + str(self.fpd_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ShowFpd.Locations.Location.Details.Detail, ['fpd_name', 'upgrade_status'], name, value)


                    class FpdInfoDetaile(Entity):
                        """
                         fpd list with all detailes
                        
                        .. attribute:: location
                        
                        	fpd location
                        	**type**\: str
                        
                        .. attribute:: card_name
                        
                        	Name of card on which fpd is located
                        	**type**\: str
                        
                        .. attribute:: fpd_name
                        
                        	fpd name
                        	**type**\: str
                        
                        .. attribute:: hw_version
                        
                        	hadware version
                        	**type**\: str
                        
                        .. attribute:: secure_boot_attr
                        
                        	secure boot attribur
                        	**type**\: str
                        
                        .. attribute:: status
                        
                        	status of the fpd
                        	**type**\: str
                        
                        .. attribute:: running_version
                        
                        	image running version 
                        	**type**\: str
                        
                        .. attribute:: programd_version
                        
                        	image programd version
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'show-fpd-loc-ng-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ShowFpd.Locations.Location.Details.Detail.FpdInfoDetaile, self).__init__()

                            self.yang_name = "fpd-info-detaile"
                            self.yang_parent_name = "detail"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location', (YLeaf(YType.str, 'location'), ['str'])),
                                ('card_name', (YLeaf(YType.str, 'card-name'), ['str'])),
                                ('fpd_name', (YLeaf(YType.str, 'fpd-name'), ['str'])),
                                ('hw_version', (YLeaf(YType.str, 'hw-version'), ['str'])),
                                ('secure_boot_attr', (YLeaf(YType.str, 'secure-boot-attr'), ['str'])),
                                ('status', (YLeaf(YType.str, 'status'), ['str'])),
                                ('running_version', (YLeaf(YType.str, 'running-version'), ['str'])),
                                ('programd_version', (YLeaf(YType.str, 'programd-version'), ['str'])),
                            ])
                            self.location = None
                            self.card_name = None
                            self.fpd_name = None
                            self.hw_version = None
                            self.secure_boot_attr = None
                            self.status = None
                            self.running_version = None
                            self.programd_version = None
                            self._segment_path = lambda: "fpd-info-detaile"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ShowFpd.Locations.Location.Details.Detail.FpdInfoDetaile, ['location', 'card_name', 'fpd_name', 'hw_version', 'secure_boot_attr', 'status', 'running_version', 'programd_version'], name, value)


    class HwModuleFpd(Entity):
        """
        Display fpds on all locations \-show hw\-module
        fpd
        
        .. attribute:: upgrade_status
        
        	Either Upgrading or free used by CTC 
        	**type**\: str
        
        .. attribute:: fpd_info_detaile
        
        	 fpd list with all detailes
        	**type**\: list of  		 :py:class:`FpdInfoDetaile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HwModuleFpd.FpdInfoDetaile>`
        
        

        """

        _prefix = 'show-fpd-loc-ng-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(ShowFpd.HwModuleFpd, self).__init__()

            self.yang_name = "hw-module-fpd"
            self.yang_parent_name = "show-fpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("fpd-info-detaile", ("fpd_info_detaile", ShowFpd.HwModuleFpd.FpdInfoDetaile))])
            self._leafs = OrderedDict([
                ('upgrade_status', (YLeaf(YType.str, 'upgrade-status'), ['str'])),
            ])
            self.upgrade_status = None

            self.fpd_info_detaile = YList(self)
            self._segment_path = lambda: "hw-module-fpd"
            self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ShowFpd.HwModuleFpd, ['upgrade_status'], name, value)


        class FpdInfoDetaile(Entity):
            """
             fpd list with all detailes
            
            .. attribute:: location
            
            	fpd location
            	**type**\: str
            
            .. attribute:: card_name
            
            	Name of card on which fpd is located
            	**type**\: str
            
            .. attribute:: fpd_name
            
            	fpd name
            	**type**\: str
            
            .. attribute:: hw_version
            
            	hadware version
            	**type**\: str
            
            .. attribute:: secure_boot_attr
            
            	secure boot attribur
            	**type**\: str
            
            .. attribute:: status
            
            	status of the fpd
            	**type**\: str
            
            .. attribute:: running_version
            
            	image running version 
            	**type**\: str
            
            .. attribute:: programd_version
            
            	image programd version
            	**type**\: str
            
            

            """

            _prefix = 'show-fpd-loc-ng-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(ShowFpd.HwModuleFpd.FpdInfoDetaile, self).__init__()

                self.yang_name = "fpd-info-detaile"
                self.yang_parent_name = "hw-module-fpd"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ('card_name', (YLeaf(YType.str, 'card-name'), ['str'])),
                    ('fpd_name', (YLeaf(YType.str, 'fpd-name'), ['str'])),
                    ('hw_version', (YLeaf(YType.str, 'hw-version'), ['str'])),
                    ('secure_boot_attr', (YLeaf(YType.str, 'secure-boot-attr'), ['str'])),
                    ('status', (YLeaf(YType.str, 'status'), ['str'])),
                    ('running_version', (YLeaf(YType.str, 'running-version'), ['str'])),
                    ('programd_version', (YLeaf(YType.str, 'programd-version'), ['str'])),
                ])
                self.location = None
                self.card_name = None
                self.fpd_name = None
                self.hw_version = None
                self.secure_boot_attr = None
                self.status = None
                self.running_version = None
                self.programd_version = None
                self._segment_path = lambda: "fpd-info-detaile"
                self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/hw-module-fpd/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ShowFpd.HwModuleFpd.FpdInfoDetaile, ['location', 'card_name', 'fpd_name', 'hw_version', 'secure_boot_attr', 'status', 'running_version', 'programd_version'], name, value)


    class HelpLocations(Entity):
        """
        help location table
        
        .. attribute:: help_location
        
        	location
        	**type**\: list of  		 :py:class:`HelpLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HelpLocations.HelpLocation>`
        
        

        """

        _prefix = 'show-fpd-loc-ng-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(ShowFpd.HelpLocations, self).__init__()

            self.yang_name = "help-locations"
            self.yang_parent_name = "show-fpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("help-location", ("help_location", ShowFpd.HelpLocations.HelpLocation))])
            self._leafs = OrderedDict()

            self.help_location = YList(self)
            self._segment_path = lambda: "help-locations"
            self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ShowFpd.HelpLocations, [], name, value)


        class HelpLocation(Entity):
            """
            location
            
            .. attribute:: location_name  (key)
            
            	Fpd location
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: help_fpd
            
            	Display fpds on given locations
            	**type**\:  :py:class:`HelpFpd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HelpLocations.HelpLocation.HelpFpd>`
            
            

            """

            _prefix = 'show-fpd-loc-ng-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(ShowFpd.HelpLocations.HelpLocation, self).__init__()

                self.yang_name = "help-location"
                self.yang_parent_name = "help-locations"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['location_name']
                self._child_classes = OrderedDict([("help-fpd", ("help_fpd", ShowFpd.HelpLocations.HelpLocation.HelpFpd))])
                self._leafs = OrderedDict([
                    ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                ])
                self.location_name = None

                self.help_fpd = ShowFpd.HelpLocations.HelpLocation.HelpFpd()
                self.help_fpd.parent = self
                self._children_name_map["help_fpd"] = "help-fpd"
                self._segment_path = lambda: "help-location" + "[location-name='" + str(self.location_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/help-locations/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ShowFpd.HelpLocations.HelpLocation, ['location_name'], name, value)


            class HelpFpd(Entity):
                """
                Display fpds on given locations
                
                .. attribute:: fpd_name
                
                	Fpd name list
                	**type**\: list of  		 :py:class:`FpdName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HelpLocations.HelpLocation.HelpFpd.FpdName>`
                
                

                """

                _prefix = 'show-fpd-loc-ng-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(ShowFpd.HelpLocations.HelpLocation.HelpFpd, self).__init__()

                    self.yang_name = "help-fpd"
                    self.yang_parent_name = "help-location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("fpd-name", ("fpd_name", ShowFpd.HelpLocations.HelpLocation.HelpFpd.FpdName))])
                    self._leafs = OrderedDict()

                    self.fpd_name = YList(self)
                    self._segment_path = lambda: "help-fpd"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ShowFpd.HelpLocations.HelpLocation.HelpFpd, [], name, value)


                class FpdName(Entity):
                    """
                    Fpd name list
                    
                    .. attribute:: location
                    
                    	fpd location
                    	**type**\: str
                    
                    .. attribute:: fpd_name
                    
                    	fpd name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'show-fpd-loc-ng-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ShowFpd.HelpLocations.HelpLocation.HelpFpd.FpdName, self).__init__()

                        self.yang_name = "fpd-name"
                        self.yang_parent_name = "help-fpd"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                            ('fpd_name', (YLeaf(YType.str, 'fpd-name'), ['str'])),
                        ])
                        self.location = None
                        self.fpd_name = None
                        self._segment_path = lambda: "fpd-name"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ShowFpd.HelpLocations.HelpLocation.HelpFpd.FpdName, ['location', 'fpd_name'], name, value)


    class HwModuleFpdHelpFpd(Entity):
        """
        Display help\-fpd \-show hw\-module fpd help\-fpd
        
        .. attribute:: fpd_name
        
        	Fpd name list
        	**type**\: list of  		 :py:class:`FpdName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HwModuleFpdHelpFpd.FpdName>`
        
        

        """

        _prefix = 'show-fpd-loc-ng-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(ShowFpd.HwModuleFpdHelpFpd, self).__init__()

            self.yang_name = "hw-module-fpd-help-fpd"
            self.yang_parent_name = "show-fpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("fpd-name", ("fpd_name", ShowFpd.HwModuleFpdHelpFpd.FpdName))])
            self._leafs = OrderedDict()

            self.fpd_name = YList(self)
            self._segment_path = lambda: "hw-module-fpd-help-fpd"
            self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ShowFpd.HwModuleFpdHelpFpd, [], name, value)


        class FpdName(Entity):
            """
            Fpd name list
            
            .. attribute:: location
            
            	fpd location
            	**type**\: str
            
            .. attribute:: fpd_name
            
            	fpd name
            	**type**\: str
            
            

            """

            _prefix = 'show-fpd-loc-ng-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(ShowFpd.HwModuleFpdHelpFpd.FpdName, self).__init__()

                self.yang_name = "fpd-name"
                self.yang_parent_name = "hw-module-fpd-help-fpd"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ('fpd_name', (YLeaf(YType.str, 'fpd-name'), ['str'])),
                ])
                self.location = None
                self.fpd_name = None
                self._segment_path = lambda: "fpd-name"
                self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/hw-module-fpd-help-fpd/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ShowFpd.HwModuleFpdHelpFpd.FpdName, ['location', 'fpd_name'], name, value)


    class Package(Entity):
        """
        gets fpd package info
        
        .. attribute:: fpd_pkg_data
        
        	 fpd pkg list 
        	**type**\: list of  		 :py:class:`FpdPkgData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.Package.FpdPkgData>`
        
        

        """

        _prefix = 'show-fpd-loc-ng-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(ShowFpd.Package, self).__init__()

            self.yang_name = "package"
            self.yang_parent_name = "show-fpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("fpd-pkg-data", ("fpd_pkg_data", ShowFpd.Package.FpdPkgData))])
            self._leafs = OrderedDict()

            self.fpd_pkg_data = YList(self)
            self._segment_path = lambda: "package"
            self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ShowFpd.Package, [], name, value)


        class FpdPkgData(Entity):
            """
             fpd pkg list 
            
            .. attribute:: card_type
            
            	card type
            	**type**\: str
            
            .. attribute:: fpd_desc
            
            	fpd desc
            	**type**\: str
            
            .. attribute:: upgrade_method
            
            	reload or not
            	**type**\: str
            
            .. attribute:: fpd_ver
            
            	fpd version
            	**type**\: str
            
            .. attribute:: min_sw_ver
            
            	minimum sw version
            	**type**\: str
            
            .. attribute:: min_hw_ver
            
            	minimum hw version
            	**type**\: str
            
            

            """

            _prefix = 'show-fpd-loc-ng-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(ShowFpd.Package.FpdPkgData, self).__init__()

                self.yang_name = "fpd-pkg-data"
                self.yang_parent_name = "package"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('card_type', (YLeaf(YType.str, 'card-type'), ['str'])),
                    ('fpd_desc', (YLeaf(YType.str, 'fpd-desc'), ['str'])),
                    ('upgrade_method', (YLeaf(YType.str, 'upgrade-method'), ['str'])),
                    ('fpd_ver', (YLeaf(YType.str, 'fpd-ver'), ['str'])),
                    ('min_sw_ver', (YLeaf(YType.str, 'min-sw-ver'), ['str'])),
                    ('min_hw_ver', (YLeaf(YType.str, 'min-hw-ver'), ['str'])),
                ])
                self.card_type = None
                self.fpd_desc = None
                self.upgrade_method = None
                self.fpd_ver = None
                self.min_sw_ver = None
                self.min_hw_ver = None
                self._segment_path = lambda: "fpd-pkg-data"
                self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/package/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ShowFpd.Package.FpdPkgData, ['card_type', 'fpd_desc', 'upgrade_method', 'fpd_ver', 'min_sw_ver', 'min_hw_ver'], name, value)


    class LocationHelp(Entity):
        """
        fpd upgradable locations
        
        .. attribute:: location_name
        
        	card location list
        	**type**\: list of  		 :py:class:`LocationName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.LocationHelp.LocationName>`
        
        

        """

        _prefix = 'show-fpd-loc-ng-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(ShowFpd.LocationHelp, self).__init__()

            self.yang_name = "location-help"
            self.yang_parent_name = "show-fpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("location-name", ("location_name", ShowFpd.LocationHelp.LocationName))])
            self._leafs = OrderedDict()

            self.location_name = YList(self)
            self._segment_path = lambda: "location-help"
            self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ShowFpd.LocationHelp, [], name, value)


        class LocationName(Entity):
            """
            card location list
            
            .. attribute:: location_name
            
            	card location
            	**type**\: str
            
            

            """

            _prefix = 'show-fpd-loc-ng-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(ShowFpd.LocationHelp.LocationName, self).__init__()

                self.yang_name = "location-name"
                self.yang_parent_name = "location-help"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('location_name', (YLeaf(YType.str, 'location-name'), ['str'])),
                ])
                self.location_name = None
                self._segment_path = lambda: "location-name"
                self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/location-help/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ShowFpd.LocationHelp.LocationName, ['location_name'], name, value)

    def clone_ptr(self):
        self._top_entity = ShowFpd()
        return self._top_entity

