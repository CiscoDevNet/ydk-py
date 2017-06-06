""" Cisco_IOS_XR_show_fpd_loc_ng_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR show\-fpd\-loc\-ng package operational data.

This module contains definitions
for the following management objects\:
  show\-fpd\: Show hw\-module fpd

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class ShowFpd(object):
    """
    Show hw\-module fpd
    
    .. attribute:: help_locations
    
    	help location table
    	**type**\:   :py:class:`HelpLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HelpLocations>`
    
    .. attribute:: hw_module_fpd
    
    	Display fpds on all locations \-show hw\-module fpd
    	**type**\:   :py:class:`HwModuleFpd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HwModuleFpd>`
    
    .. attribute:: hw_module_fpd_help_fpd
    
    	Display help\-fpd \-show hw\-module fpd help\-fpd
    	**type**\:   :py:class:`HwModuleFpdHelpFpd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HwModuleFpdHelpFpd>`
    
    .. attribute:: location_help
    
    	fpd upgradable locations
    	**type**\:   :py:class:`LocationHelp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.LocationHelp>`
    
    .. attribute:: locations
    
    	location table
    	**type**\:   :py:class:`Locations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.Locations>`
    
    .. attribute:: package
    
    	gets fpd package info
    	**type**\:   :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.Package>`
    
    

    """

    _prefix = 'show-fpd-loc-ng-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.help_locations = ShowFpd.HelpLocations()
        self.help_locations.parent = self
        self.hw_module_fpd = ShowFpd.HwModuleFpd()
        self.hw_module_fpd.parent = self
        self.hw_module_fpd_help_fpd = ShowFpd.HwModuleFpdHelpFpd()
        self.hw_module_fpd_help_fpd.parent = self
        self.location_help = ShowFpd.LocationHelp()
        self.location_help.parent = self
        self.locations = ShowFpd.Locations()
        self.locations.parent = self
        self.package = ShowFpd.Package()
        self.package.parent = self


    class Locations(object):
        """
        location table
        
        .. attribute:: location
        
        	location
        	**type**\: list of    :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.Locations.Location>`
        
        

        """

        _prefix = 'show-fpd-loc-ng-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.location = YList()
            self.location.parent = self
            self.location.name = 'location'


        class Location(object):
            """
            location
            
            .. attribute:: location_name  <key>
            
            	Fpd location
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: fpd
            
            	Display fpds on given locations
            	**type**\: list of    :py:class:`Fpd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.Locations.Location.Fpd>`
            
            

            """

            _prefix = 'show-fpd-loc-ng-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.location_name = None
                self.fpd = YList()
                self.fpd.parent = self
                self.fpd.name = 'fpd'


            class Fpd(object):
                """
                Display fpds on given locations
                
                .. attribute:: fpd_name  <key>
                
                	Fpd Name
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: fpd_info_detaile
                
                	 fpd list with all detailes
                	**type**\: list of    :py:class:`FpdInfoDetaile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.Locations.Location.Fpd.FpdInfoDetaile>`
                
                

                """

                _prefix = 'show-fpd-loc-ng-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.fpd_name = None
                    self.fpd_info_detaile = YList()
                    self.fpd_info_detaile.parent = self
                    self.fpd_info_detaile.name = 'fpd_info_detaile'


                class FpdInfoDetaile(object):
                    """
                     fpd list with all detailes
                    
                    .. attribute:: card_name
                    
                    	Name of card on which fpd is located
                    	**type**\:  str
                    
                    .. attribute:: fpd_name
                    
                    	fpd name
                    	**type**\:  str
                    
                    .. attribute:: hw_version
                    
                    	hadware version
                    	**type**\:  str
                    
                    .. attribute:: location
                    
                    	fpd location
                    	**type**\:  str
                    
                    .. attribute:: programd_version
                    
                    	image programd version
                    	**type**\:  str
                    
                    .. attribute:: running_version
                    
                    	image running version 
                    	**type**\:  str
                    
                    .. attribute:: secure_boot_attr
                    
                    	secure boot attribur
                    	**type**\:  str
                    
                    .. attribute:: status
                    
                    	status of the fpd
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'show-fpd-loc-ng-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.card_name = None
                        self.fpd_name = None
                        self.hw_version = None
                        self.location = None
                        self.programd_version = None
                        self.running_version = None
                        self.secure_boot_attr = None
                        self.status = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-show-fpd-loc-ng-oper:fpd-info-detaile'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.card_name is not None:
                            return True

                        if self.fpd_name is not None:
                            return True

                        if self.hw_version is not None:
                            return True

                        if self.location is not None:
                            return True

                        if self.programd_version is not None:
                            return True

                        if self.running_version is not None:
                            return True

                        if self.secure_boot_attr is not None:
                            return True

                        if self.status is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_show_fpd_loc_ng_oper as meta
                        return meta._meta_table['ShowFpd.Locations.Location.Fpd.FpdInfoDetaile']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.fpd_name is None:
                        raise YPYModelError('Key property fpd_name is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-show-fpd-loc-ng-oper:fpd[Cisco-IOS-XR-show-fpd-loc-ng-oper:fpd-name = ' + str(self.fpd_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.fpd_name is not None:
                        return True

                    if self.fpd_info_detaile is not None:
                        for child_ref in self.fpd_info_detaile:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_show_fpd_loc_ng_oper as meta
                    return meta._meta_table['ShowFpd.Locations.Location.Fpd']['meta_info']

            @property
            def _common_path(self):
                if self.location_name is None:
                    raise YPYModelError('Key property location_name is None')

                return '/Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/Cisco-IOS-XR-show-fpd-loc-ng-oper:locations/Cisco-IOS-XR-show-fpd-loc-ng-oper:location[Cisco-IOS-XR-show-fpd-loc-ng-oper:location-name = ' + str(self.location_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.location_name is not None:
                    return True

                if self.fpd is not None:
                    for child_ref in self.fpd:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_show_fpd_loc_ng_oper as meta
                return meta._meta_table['ShowFpd.Locations.Location']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/Cisco-IOS-XR-show-fpd-loc-ng-oper:locations'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.location is not None:
                for child_ref in self.location:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_show_fpd_loc_ng_oper as meta
            return meta._meta_table['ShowFpd.Locations']['meta_info']


    class HwModuleFpd(object):
        """
        Display fpds on all locations \-show hw\-module
        fpd
        
        .. attribute:: fpd_info_detaile
        
        	 fpd list with all detailes
        	**type**\: list of    :py:class:`FpdInfoDetaile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HwModuleFpd.FpdInfoDetaile>`
        
        

        """

        _prefix = 'show-fpd-loc-ng-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.fpd_info_detaile = YList()
            self.fpd_info_detaile.parent = self
            self.fpd_info_detaile.name = 'fpd_info_detaile'


        class FpdInfoDetaile(object):
            """
             fpd list with all detailes
            
            .. attribute:: card_name
            
            	Name of card on which fpd is located
            	**type**\:  str
            
            .. attribute:: fpd_name
            
            	fpd name
            	**type**\:  str
            
            .. attribute:: hw_version
            
            	hadware version
            	**type**\:  str
            
            .. attribute:: location
            
            	fpd location
            	**type**\:  str
            
            .. attribute:: programd_version
            
            	image programd version
            	**type**\:  str
            
            .. attribute:: running_version
            
            	image running version 
            	**type**\:  str
            
            .. attribute:: secure_boot_attr
            
            	secure boot attribur
            	**type**\:  str
            
            .. attribute:: status
            
            	status of the fpd
            	**type**\:  str
            
            

            """

            _prefix = 'show-fpd-loc-ng-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.card_name = None
                self.fpd_name = None
                self.hw_version = None
                self.location = None
                self.programd_version = None
                self.running_version = None
                self.secure_boot_attr = None
                self.status = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/Cisco-IOS-XR-show-fpd-loc-ng-oper:hw-module-fpd/Cisco-IOS-XR-show-fpd-loc-ng-oper:fpd-info-detaile'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.card_name is not None:
                    return True

                if self.fpd_name is not None:
                    return True

                if self.hw_version is not None:
                    return True

                if self.location is not None:
                    return True

                if self.programd_version is not None:
                    return True

                if self.running_version is not None:
                    return True

                if self.secure_boot_attr is not None:
                    return True

                if self.status is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_show_fpd_loc_ng_oper as meta
                return meta._meta_table['ShowFpd.HwModuleFpd.FpdInfoDetaile']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/Cisco-IOS-XR-show-fpd-loc-ng-oper:hw-module-fpd'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.fpd_info_detaile is not None:
                for child_ref in self.fpd_info_detaile:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_show_fpd_loc_ng_oper as meta
            return meta._meta_table['ShowFpd.HwModuleFpd']['meta_info']


    class HelpLocations(object):
        """
        help location table
        
        .. attribute:: help_location
        
        	location
        	**type**\: list of    :py:class:`HelpLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HelpLocations.HelpLocation>`
        
        

        """

        _prefix = 'show-fpd-loc-ng-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.help_location = YList()
            self.help_location.parent = self
            self.help_location.name = 'help_location'


        class HelpLocation(object):
            """
            location
            
            .. attribute:: location_name  <key>
            
            	Fpd location
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: help_fpd
            
            	Display fpds on given locations
            	**type**\:   :py:class:`HelpFpd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HelpLocations.HelpLocation.HelpFpd>`
            
            

            """

            _prefix = 'show-fpd-loc-ng-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.location_name = None
                self.help_fpd = ShowFpd.HelpLocations.HelpLocation.HelpFpd()
                self.help_fpd.parent = self


            class HelpFpd(object):
                """
                Display fpds on given locations
                
                .. attribute:: fpd_name
                
                	Fpd name list
                	**type**\: list of    :py:class:`FpdName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HelpLocations.HelpLocation.HelpFpd.FpdName>`
                
                

                """

                _prefix = 'show-fpd-loc-ng-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.fpd_name = YList()
                    self.fpd_name.parent = self
                    self.fpd_name.name = 'fpd_name'


                class FpdName(object):
                    """
                    Fpd name list
                    
                    .. attribute:: fpd_name
                    
                    	fpd name
                    	**type**\:  str
                    
                    .. attribute:: location
                    
                    	fpd location
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'show-fpd-loc-ng-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.fpd_name = None
                        self.location = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-show-fpd-loc-ng-oper:fpd-name'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.fpd_name is not None:
                            return True

                        if self.location is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_show_fpd_loc_ng_oper as meta
                        return meta._meta_table['ShowFpd.HelpLocations.HelpLocation.HelpFpd.FpdName']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-show-fpd-loc-ng-oper:help-fpd'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.fpd_name is not None:
                        for child_ref in self.fpd_name:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_show_fpd_loc_ng_oper as meta
                    return meta._meta_table['ShowFpd.HelpLocations.HelpLocation.HelpFpd']['meta_info']

            @property
            def _common_path(self):
                if self.location_name is None:
                    raise YPYModelError('Key property location_name is None')

                return '/Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/Cisco-IOS-XR-show-fpd-loc-ng-oper:help-locations/Cisco-IOS-XR-show-fpd-loc-ng-oper:help-location[Cisco-IOS-XR-show-fpd-loc-ng-oper:location-name = ' + str(self.location_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.location_name is not None:
                    return True

                if self.help_fpd is not None and self.help_fpd._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_show_fpd_loc_ng_oper as meta
                return meta._meta_table['ShowFpd.HelpLocations.HelpLocation']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/Cisco-IOS-XR-show-fpd-loc-ng-oper:help-locations'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.help_location is not None:
                for child_ref in self.help_location:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_show_fpd_loc_ng_oper as meta
            return meta._meta_table['ShowFpd.HelpLocations']['meta_info']


    class HwModuleFpdHelpFpd(object):
        """
        Display help\-fpd \-show hw\-module fpd help\-fpd
        
        .. attribute:: fpd_name
        
        	Fpd name list
        	**type**\: list of    :py:class:`FpdName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HwModuleFpdHelpFpd.FpdName>`
        
        

        """

        _prefix = 'show-fpd-loc-ng-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.fpd_name = YList()
            self.fpd_name.parent = self
            self.fpd_name.name = 'fpd_name'


        class FpdName(object):
            """
            Fpd name list
            
            .. attribute:: fpd_name
            
            	fpd name
            	**type**\:  str
            
            .. attribute:: location
            
            	fpd location
            	**type**\:  str
            
            

            """

            _prefix = 'show-fpd-loc-ng-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.fpd_name = None
                self.location = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/Cisco-IOS-XR-show-fpd-loc-ng-oper:hw-module-fpd-help-fpd/Cisco-IOS-XR-show-fpd-loc-ng-oper:fpd-name'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.fpd_name is not None:
                    return True

                if self.location is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_show_fpd_loc_ng_oper as meta
                return meta._meta_table['ShowFpd.HwModuleFpdHelpFpd.FpdName']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/Cisco-IOS-XR-show-fpd-loc-ng-oper:hw-module-fpd-help-fpd'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.fpd_name is not None:
                for child_ref in self.fpd_name:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_show_fpd_loc_ng_oper as meta
            return meta._meta_table['ShowFpd.HwModuleFpdHelpFpd']['meta_info']


    class Package(object):
        """
        gets fpd package info
        
        .. attribute:: fpd_pkg_data
        
        	 fpd pkg list 
        	**type**\: list of    :py:class:`FpdPkgData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.Package.FpdPkgData>`
        
        

        """

        _prefix = 'show-fpd-loc-ng-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.fpd_pkg_data = YList()
            self.fpd_pkg_data.parent = self
            self.fpd_pkg_data.name = 'fpd_pkg_data'


        class FpdPkgData(object):
            """
             fpd pkg list 
            
            .. attribute:: card_type
            
            	card type
            	**type**\:  str
            
            .. attribute:: fpd_desc
            
            	fpd desc
            	**type**\:  str
            
            .. attribute:: fpd_ver
            
            	fpd version
            	**type**\:  str
            
            .. attribute:: min_hw_ver
            
            	minimum hw version
            	**type**\:  str
            
            .. attribute:: min_sw_ver
            
            	minimum sw version
            	**type**\:  str
            
            .. attribute:: upgrade_method
            
            	reload or not
            	**type**\:  str
            
            

            """

            _prefix = 'show-fpd-loc-ng-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.card_type = None
                self.fpd_desc = None
                self.fpd_ver = None
                self.min_hw_ver = None
                self.min_sw_ver = None
                self.upgrade_method = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/Cisco-IOS-XR-show-fpd-loc-ng-oper:package/Cisco-IOS-XR-show-fpd-loc-ng-oper:fpd-pkg-data'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.card_type is not None:
                    return True

                if self.fpd_desc is not None:
                    return True

                if self.fpd_ver is not None:
                    return True

                if self.min_hw_ver is not None:
                    return True

                if self.min_sw_ver is not None:
                    return True

                if self.upgrade_method is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_show_fpd_loc_ng_oper as meta
                return meta._meta_table['ShowFpd.Package.FpdPkgData']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/Cisco-IOS-XR-show-fpd-loc-ng-oper:package'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.fpd_pkg_data is not None:
                for child_ref in self.fpd_pkg_data:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_show_fpd_loc_ng_oper as meta
            return meta._meta_table['ShowFpd.Package']['meta_info']


    class LocationHelp(object):
        """
        fpd upgradable locations
        
        .. attribute:: location_name
        
        	card location list
        	**type**\: list of    :py:class:`LocationName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.LocationHelp.LocationName>`
        
        

        """

        _prefix = 'show-fpd-loc-ng-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.location_name = YList()
            self.location_name.parent = self
            self.location_name.name = 'location_name'


        class LocationName(object):
            """
            card location list
            
            .. attribute:: location_name
            
            	card location
            	**type**\:  str
            
            

            """

            _prefix = 'show-fpd-loc-ng-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.location_name = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/Cisco-IOS-XR-show-fpd-loc-ng-oper:location-help/Cisco-IOS-XR-show-fpd-loc-ng-oper:location-name'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.location_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_show_fpd_loc_ng_oper as meta
                return meta._meta_table['ShowFpd.LocationHelp.LocationName']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/Cisco-IOS-XR-show-fpd-loc-ng-oper:location-help'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.location_name is not None:
                for child_ref in self.location_name:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_show_fpd_loc_ng_oper as meta
            return meta._meta_table['ShowFpd.LocationHelp']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.help_locations is not None and self.help_locations._has_data():
            return True

        if self.hw_module_fpd is not None and self.hw_module_fpd._has_data():
            return True

        if self.hw_module_fpd_help_fpd is not None and self.hw_module_fpd_help_fpd._has_data():
            return True

        if self.location_help is not None and self.location_help._has_data():
            return True

        if self.locations is not None and self.locations._has_data():
            return True

        if self.package is not None and self.package._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_show_fpd_loc_ng_oper as meta
        return meta._meta_table['ShowFpd']['meta_info']


