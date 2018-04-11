""" Cisco_IOS_XR_show_fpd_loc_ng_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR show\-fpd\-loc\-ng package operational data.

This module contains definitions
for the following management objects\:
  show\-fpd\: Show hw\-module fpd

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
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
        self._child_container_classes = OrderedDict([("locations", ("locations", ShowFpd.Locations)), ("hw-module-fpd", ("hw_module_fpd", ShowFpd.HwModuleFpd)), ("help-locations", ("help_locations", ShowFpd.HelpLocations)), ("hw-module-fpd-help-fpd", ("hw_module_fpd_help_fpd", ShowFpd.HwModuleFpdHelpFpd)), ("package", ("package", ShowFpd.Package)), ("location-help", ("location_help", ShowFpd.LocationHelp))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.locations = ShowFpd.Locations()
        self.locations.parent = self
        self._children_name_map["locations"] = "locations"
        self._children_yang_names.add("locations")

        self.hw_module_fpd = ShowFpd.HwModuleFpd()
        self.hw_module_fpd.parent = self
        self._children_name_map["hw_module_fpd"] = "hw-module-fpd"
        self._children_yang_names.add("hw-module-fpd")

        self.help_locations = ShowFpd.HelpLocations()
        self.help_locations.parent = self
        self._children_name_map["help_locations"] = "help-locations"
        self._children_yang_names.add("help-locations")

        self.hw_module_fpd_help_fpd = ShowFpd.HwModuleFpdHelpFpd()
        self.hw_module_fpd_help_fpd.parent = self
        self._children_name_map["hw_module_fpd_help_fpd"] = "hw-module-fpd-help-fpd"
        self._children_yang_names.add("hw-module-fpd-help-fpd")

        self.package = ShowFpd.Package()
        self.package.parent = self
        self._children_name_map["package"] = "package"
        self._children_yang_names.add("package")

        self.location_help = ShowFpd.LocationHelp()
        self.location_help.parent = self
        self._children_name_map["location_help"] = "location-help"
        self._children_yang_names.add("location-help")
        self._segment_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd"


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
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("location", ("location", ShowFpd.Locations.Location))])
            self._leafs = OrderedDict()

            self.location = YList(self)
            self._segment_path = lambda: "locations"
            self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ShowFpd.Locations, [], name, value)


        class Location(Entity):
            """
            location
            
            .. attribute:: location_name  (key)
            
            	Fpd location
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: fpd
            
            	Display fpds on given locations
            	**type**\: list of  		 :py:class:`Fpd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.Locations.Location.Fpd>`
            
            

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
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("fpd", ("fpd", ShowFpd.Locations.Location.Fpd))])
                self._leafs = OrderedDict([
                    ('location_name', YLeaf(YType.str, 'location-name')),
                ])
                self.location_name = None

                self.fpd = YList(self)
                self._segment_path = lambda: "location" + "[location-name='" + str(self.location_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/locations/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ShowFpd.Locations.Location, ['location_name'], name, value)


            class Fpd(Entity):
                """
                Display fpds on given locations
                
                .. attribute:: fpd_name  (key)
                
                	Fpd Name
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: fpd_info_detaile
                
                	 fpd list with all detailes
                	**type**\: list of  		 :py:class:`FpdInfoDetaile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.Locations.Location.Fpd.FpdInfoDetaile>`
                
                

                """

                _prefix = 'show-fpd-loc-ng-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(ShowFpd.Locations.Location.Fpd, self).__init__()

                    self.yang_name = "fpd"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['fpd_name']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("fpd-info-detaile", ("fpd_info_detaile", ShowFpd.Locations.Location.Fpd.FpdInfoDetaile))])
                    self._leafs = OrderedDict([
                        ('fpd_name', YLeaf(YType.str, 'fpd-name')),
                    ])
                    self.fpd_name = None

                    self.fpd_info_detaile = YList(self)
                    self._segment_path = lambda: "fpd" + "[fpd-name='" + str(self.fpd_name) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(ShowFpd.Locations.Location.Fpd, ['fpd_name'], name, value)


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
                        super(ShowFpd.Locations.Location.Fpd.FpdInfoDetaile, self).__init__()

                        self.yang_name = "fpd-info-detaile"
                        self.yang_parent_name = "fpd"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('location', YLeaf(YType.str, 'location')),
                            ('card_name', YLeaf(YType.str, 'card-name')),
                            ('fpd_name', YLeaf(YType.str, 'fpd-name')),
                            ('hw_version', YLeaf(YType.str, 'hw-version')),
                            ('secure_boot_attr', YLeaf(YType.str, 'secure-boot-attr')),
                            ('status', YLeaf(YType.str, 'status')),
                            ('running_version', YLeaf(YType.str, 'running-version')),
                            ('programd_version', YLeaf(YType.str, 'programd-version')),
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

                    def __setattr__(self, name, value):
                        self._perform_setattr(ShowFpd.Locations.Location.Fpd.FpdInfoDetaile, ['location', 'card_name', 'fpd_name', 'hw_version', 'secure_boot_attr', 'status', 'running_version', 'programd_version'], name, value)


    class HwModuleFpd(Entity):
        """
        Display fpds on all locations \-show hw\-module
        fpd
        
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
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("fpd-info-detaile", ("fpd_info_detaile", ShowFpd.HwModuleFpd.FpdInfoDetaile))])
            self._leafs = OrderedDict()

            self.fpd_info_detaile = YList(self)
            self._segment_path = lambda: "hw-module-fpd"
            self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ShowFpd.HwModuleFpd, [], name, value)


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
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('location', YLeaf(YType.str, 'location')),
                    ('card_name', YLeaf(YType.str, 'card-name')),
                    ('fpd_name', YLeaf(YType.str, 'fpd-name')),
                    ('hw_version', YLeaf(YType.str, 'hw-version')),
                    ('secure_boot_attr', YLeaf(YType.str, 'secure-boot-attr')),
                    ('status', YLeaf(YType.str, 'status')),
                    ('running_version', YLeaf(YType.str, 'running-version')),
                    ('programd_version', YLeaf(YType.str, 'programd-version')),
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
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("help-location", ("help_location", ShowFpd.HelpLocations.HelpLocation))])
            self._leafs = OrderedDict()

            self.help_location = YList(self)
            self._segment_path = lambda: "help-locations"
            self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self._segment_path()

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
                self._child_container_classes = OrderedDict([("help-fpd", ("help_fpd", ShowFpd.HelpLocations.HelpLocation.HelpFpd))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('location_name', YLeaf(YType.str, 'location-name')),
                ])
                self.location_name = None

                self.help_fpd = ShowFpd.HelpLocations.HelpLocation.HelpFpd()
                self.help_fpd.parent = self
                self._children_name_map["help_fpd"] = "help-fpd"
                self._children_yang_names.add("help-fpd")
                self._segment_path = lambda: "help-location" + "[location-name='" + str(self.location_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/help-locations/%s" % self._segment_path()

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
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("fpd-name", ("fpd_name", ShowFpd.HelpLocations.HelpLocation.HelpFpd.FpdName))])
                    self._leafs = OrderedDict()

                    self.fpd_name = YList(self)
                    self._segment_path = lambda: "help-fpd"

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
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('location', YLeaf(YType.str, 'location')),
                            ('fpd_name', YLeaf(YType.str, 'fpd-name')),
                        ])
                        self.location = None
                        self.fpd_name = None
                        self._segment_path = lambda: "fpd-name"

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
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("fpd-name", ("fpd_name", ShowFpd.HwModuleFpdHelpFpd.FpdName))])
            self._leafs = OrderedDict()

            self.fpd_name = YList(self)
            self._segment_path = lambda: "hw-module-fpd-help-fpd"
            self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self._segment_path()

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
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('location', YLeaf(YType.str, 'location')),
                    ('fpd_name', YLeaf(YType.str, 'fpd-name')),
                ])
                self.location = None
                self.fpd_name = None
                self._segment_path = lambda: "fpd-name"
                self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/hw-module-fpd-help-fpd/%s" % self._segment_path()

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
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("fpd-pkg-data", ("fpd_pkg_data", ShowFpd.Package.FpdPkgData))])
            self._leafs = OrderedDict()

            self.fpd_pkg_data = YList(self)
            self._segment_path = lambda: "package"
            self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self._segment_path()

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
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('card_type', YLeaf(YType.str, 'card-type')),
                    ('fpd_desc', YLeaf(YType.str, 'fpd-desc')),
                    ('upgrade_method', YLeaf(YType.str, 'upgrade-method')),
                    ('fpd_ver', YLeaf(YType.str, 'fpd-ver')),
                    ('min_sw_ver', YLeaf(YType.str, 'min-sw-ver')),
                    ('min_hw_ver', YLeaf(YType.str, 'min-hw-ver')),
                ])
                self.card_type = None
                self.fpd_desc = None
                self.upgrade_method = None
                self.fpd_ver = None
                self.min_sw_ver = None
                self.min_hw_ver = None
                self._segment_path = lambda: "fpd-pkg-data"
                self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/package/%s" % self._segment_path()

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
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("location-name", ("location_name", ShowFpd.LocationHelp.LocationName))])
            self._leafs = OrderedDict()

            self.location_name = YList(self)
            self._segment_path = lambda: "location-help"
            self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self._segment_path()

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
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('location_name', YLeaf(YType.str, 'location-name')),
                ])
                self.location_name = None
                self._segment_path = lambda: "location-name"
                self._absolute_path = lambda: "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/location-help/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ShowFpd.LocationHelp.LocationName, ['location_name'], name, value)

    def clone_ptr(self):
        self._top_entity = ShowFpd()
        return self._top_entity

