""" Cisco_IOS_XR_show_fpd_loc_ng_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR show\-fpd\-loc\-ng package operational data.

This module contains definitions
for the following management objects\:
  show\-fpd\: Show hw\-module fpd

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ShowFpd(Entity):
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
        super(ShowFpd, self).__init__()
        self._top_entity = None

        self.yang_name = "show-fpd"
        self.yang_parent_name = "Cisco-IOS-XR-show-fpd-loc-ng-oper"

        self.help_locations = ShowFpd.HelpLocations()
        self.help_locations.parent = self
        self._children_name_map["help_locations"] = "help-locations"
        self._children_yang_names.add("help-locations")

        self.hw_module_fpd = ShowFpd.HwModuleFpd()
        self.hw_module_fpd.parent = self
        self._children_name_map["hw_module_fpd"] = "hw-module-fpd"
        self._children_yang_names.add("hw-module-fpd")

        self.hw_module_fpd_help_fpd = ShowFpd.HwModuleFpdHelpFpd()
        self.hw_module_fpd_help_fpd.parent = self
        self._children_name_map["hw_module_fpd_help_fpd"] = "hw-module-fpd-help-fpd"
        self._children_yang_names.add("hw-module-fpd-help-fpd")

        self.location_help = ShowFpd.LocationHelp()
        self.location_help.parent = self
        self._children_name_map["location_help"] = "location-help"
        self._children_yang_names.add("location-help")

        self.locations = ShowFpd.Locations()
        self.locations.parent = self
        self._children_name_map["locations"] = "locations"
        self._children_yang_names.add("locations")

        self.package = ShowFpd.Package()
        self.package.parent = self
        self._children_name_map["package"] = "package"
        self._children_yang_names.add("package")


    class Locations(Entity):
        """
        location table
        
        .. attribute:: location
        
        	location
        	**type**\: list of    :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.Locations.Location>`
        
        

        """

        _prefix = 'show-fpd-loc-ng-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ShowFpd.Locations, self).__init__()

            self.yang_name = "locations"
            self.yang_parent_name = "show-fpd"

            self.location = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ShowFpd.Locations, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ShowFpd.Locations, self).__setattr__(name, value)


        class Location(Entity):
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
                super(ShowFpd.Locations.Location, self).__init__()

                self.yang_name = "location"
                self.yang_parent_name = "locations"

                self.location_name = YLeaf(YType.str, "location-name")

                self.fpd = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("location_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ShowFpd.Locations.Location, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ShowFpd.Locations.Location, self).__setattr__(name, value)


            class Fpd(Entity):
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
                    super(ShowFpd.Locations.Location.Fpd, self).__init__()

                    self.yang_name = "fpd"
                    self.yang_parent_name = "location"

                    self.fpd_name = YLeaf(YType.str, "fpd-name")

                    self.fpd_info_detaile = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("fpd_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ShowFpd.Locations.Location.Fpd, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ShowFpd.Locations.Location.Fpd, self).__setattr__(name, value)


                class FpdInfoDetaile(Entity):
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
                        super(ShowFpd.Locations.Location.Fpd.FpdInfoDetaile, self).__init__()

                        self.yang_name = "fpd-info-detaile"
                        self.yang_parent_name = "fpd"

                        self.card_name = YLeaf(YType.str, "card-name")

                        self.fpd_name = YLeaf(YType.str, "fpd-name")

                        self.hw_version = YLeaf(YType.str, "hw-version")

                        self.location = YLeaf(YType.str, "location")

                        self.programd_version = YLeaf(YType.str, "programd-version")

                        self.running_version = YLeaf(YType.str, "running-version")

                        self.secure_boot_attr = YLeaf(YType.str, "secure-boot-attr")

                        self.status = YLeaf(YType.str, "status")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("card_name",
                                        "fpd_name",
                                        "hw_version",
                                        "location",
                                        "programd_version",
                                        "running_version",
                                        "secure_boot_attr",
                                        "status") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ShowFpd.Locations.Location.Fpd.FpdInfoDetaile, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ShowFpd.Locations.Location.Fpd.FpdInfoDetaile, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.card_name.is_set or
                            self.fpd_name.is_set or
                            self.hw_version.is_set or
                            self.location.is_set or
                            self.programd_version.is_set or
                            self.running_version.is_set or
                            self.secure_boot_attr.is_set or
                            self.status.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.card_name.yfilter != YFilter.not_set or
                            self.fpd_name.yfilter != YFilter.not_set or
                            self.hw_version.yfilter != YFilter.not_set or
                            self.location.yfilter != YFilter.not_set or
                            self.programd_version.yfilter != YFilter.not_set or
                            self.running_version.yfilter != YFilter.not_set or
                            self.secure_boot_attr.yfilter != YFilter.not_set or
                            self.status.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "fpd-info-detaile" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.card_name.is_set or self.card_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.card_name.get_name_leafdata())
                        if (self.fpd_name.is_set or self.fpd_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fpd_name.get_name_leafdata())
                        if (self.hw_version.is_set or self.hw_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hw_version.get_name_leafdata())
                        if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.location.get_name_leafdata())
                        if (self.programd_version.is_set or self.programd_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.programd_version.get_name_leafdata())
                        if (self.running_version.is_set or self.running_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.running_version.get_name_leafdata())
                        if (self.secure_boot_attr.is_set or self.secure_boot_attr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.secure_boot_attr.get_name_leafdata())
                        if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.status.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "card-name" or name == "fpd-name" or name == "hw-version" or name == "location" or name == "programd-version" or name == "running-version" or name == "secure-boot-attr" or name == "status"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "card-name"):
                            self.card_name = value
                            self.card_name.value_namespace = name_space
                            self.card_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "fpd-name"):
                            self.fpd_name = value
                            self.fpd_name.value_namespace = name_space
                            self.fpd_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "hw-version"):
                            self.hw_version = value
                            self.hw_version.value_namespace = name_space
                            self.hw_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "location"):
                            self.location = value
                            self.location.value_namespace = name_space
                            self.location.value_namespace_prefix = name_space_prefix
                        if(value_path == "programd-version"):
                            self.programd_version = value
                            self.programd_version.value_namespace = name_space
                            self.programd_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "running-version"):
                            self.running_version = value
                            self.running_version.value_namespace = name_space
                            self.running_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "secure-boot-attr"):
                            self.secure_boot_attr = value
                            self.secure_boot_attr.value_namespace = name_space
                            self.secure_boot_attr.value_namespace_prefix = name_space_prefix
                        if(value_path == "status"):
                            self.status = value
                            self.status.value_namespace = name_space
                            self.status.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.fpd_info_detaile:
                        if (c.has_data()):
                            return True
                    return self.fpd_name.is_set

                def has_operation(self):
                    for c in self.fpd_info_detaile:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.fpd_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "fpd" + "[fpd-name='" + self.fpd_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.fpd_name.is_set or self.fpd_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fpd_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "fpd-info-detaile"):
                        for c in self.fpd_info_detaile:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ShowFpd.Locations.Location.Fpd.FpdInfoDetaile()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.fpd_info_detaile.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "fpd-info-detaile" or name == "fpd-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "fpd-name"):
                        self.fpd_name = value
                        self.fpd_name.value_namespace = name_space
                        self.fpd_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.fpd:
                    if (c.has_data()):
                        return True
                return self.location_name.is_set

            def has_operation(self):
                for c in self.fpd:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.location_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "location" + "[location-name='" + self.location_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/locations/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.location_name.is_set or self.location_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.location_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "fpd"):
                    for c in self.fpd:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ShowFpd.Locations.Location.Fpd()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.fpd.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "fpd" or name == "location-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "location-name"):
                    self.location_name = value
                    self.location_name.value_namespace = name_space
                    self.location_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.location:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.location:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "locations" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "location"):
                for c in self.location:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ShowFpd.Locations.Location()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.location.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "location"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class HwModuleFpd(Entity):
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
            super(ShowFpd.HwModuleFpd, self).__init__()

            self.yang_name = "hw-module-fpd"
            self.yang_parent_name = "show-fpd"

            self.fpd_info_detaile = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ShowFpd.HwModuleFpd, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ShowFpd.HwModuleFpd, self).__setattr__(name, value)


        class FpdInfoDetaile(Entity):
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
                super(ShowFpd.HwModuleFpd.FpdInfoDetaile, self).__init__()

                self.yang_name = "fpd-info-detaile"
                self.yang_parent_name = "hw-module-fpd"

                self.card_name = YLeaf(YType.str, "card-name")

                self.fpd_name = YLeaf(YType.str, "fpd-name")

                self.hw_version = YLeaf(YType.str, "hw-version")

                self.location = YLeaf(YType.str, "location")

                self.programd_version = YLeaf(YType.str, "programd-version")

                self.running_version = YLeaf(YType.str, "running-version")

                self.secure_boot_attr = YLeaf(YType.str, "secure-boot-attr")

                self.status = YLeaf(YType.str, "status")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("card_name",
                                "fpd_name",
                                "hw_version",
                                "location",
                                "programd_version",
                                "running_version",
                                "secure_boot_attr",
                                "status") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ShowFpd.HwModuleFpd.FpdInfoDetaile, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ShowFpd.HwModuleFpd.FpdInfoDetaile, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.card_name.is_set or
                    self.fpd_name.is_set or
                    self.hw_version.is_set or
                    self.location.is_set or
                    self.programd_version.is_set or
                    self.running_version.is_set or
                    self.secure_boot_attr.is_set or
                    self.status.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.card_name.yfilter != YFilter.not_set or
                    self.fpd_name.yfilter != YFilter.not_set or
                    self.hw_version.yfilter != YFilter.not_set or
                    self.location.yfilter != YFilter.not_set or
                    self.programd_version.yfilter != YFilter.not_set or
                    self.running_version.yfilter != YFilter.not_set or
                    self.secure_boot_attr.yfilter != YFilter.not_set or
                    self.status.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "fpd-info-detaile" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/hw-module-fpd/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.card_name.is_set or self.card_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.card_name.get_name_leafdata())
                if (self.fpd_name.is_set or self.fpd_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.fpd_name.get_name_leafdata())
                if (self.hw_version.is_set or self.hw_version.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hw_version.get_name_leafdata())
                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.location.get_name_leafdata())
                if (self.programd_version.is_set or self.programd_version.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.programd_version.get_name_leafdata())
                if (self.running_version.is_set or self.running_version.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.running_version.get_name_leafdata())
                if (self.secure_boot_attr.is_set or self.secure_boot_attr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.secure_boot_attr.get_name_leafdata())
                if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.status.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "card-name" or name == "fpd-name" or name == "hw-version" or name == "location" or name == "programd-version" or name == "running-version" or name == "secure-boot-attr" or name == "status"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "card-name"):
                    self.card_name = value
                    self.card_name.value_namespace = name_space
                    self.card_name.value_namespace_prefix = name_space_prefix
                if(value_path == "fpd-name"):
                    self.fpd_name = value
                    self.fpd_name.value_namespace = name_space
                    self.fpd_name.value_namespace_prefix = name_space_prefix
                if(value_path == "hw-version"):
                    self.hw_version = value
                    self.hw_version.value_namespace = name_space
                    self.hw_version.value_namespace_prefix = name_space_prefix
                if(value_path == "location"):
                    self.location = value
                    self.location.value_namespace = name_space
                    self.location.value_namespace_prefix = name_space_prefix
                if(value_path == "programd-version"):
                    self.programd_version = value
                    self.programd_version.value_namespace = name_space
                    self.programd_version.value_namespace_prefix = name_space_prefix
                if(value_path == "running-version"):
                    self.running_version = value
                    self.running_version.value_namespace = name_space
                    self.running_version.value_namespace_prefix = name_space_prefix
                if(value_path == "secure-boot-attr"):
                    self.secure_boot_attr = value
                    self.secure_boot_attr.value_namespace = name_space
                    self.secure_boot_attr.value_namespace_prefix = name_space_prefix
                if(value_path == "status"):
                    self.status = value
                    self.status.value_namespace = name_space
                    self.status.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.fpd_info_detaile:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.fpd_info_detaile:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "hw-module-fpd" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "fpd-info-detaile"):
                for c in self.fpd_info_detaile:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ShowFpd.HwModuleFpd.FpdInfoDetaile()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.fpd_info_detaile.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "fpd-info-detaile"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class HelpLocations(Entity):
        """
        help location table
        
        .. attribute:: help_location
        
        	location
        	**type**\: list of    :py:class:`HelpLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HelpLocations.HelpLocation>`
        
        

        """

        _prefix = 'show-fpd-loc-ng-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ShowFpd.HelpLocations, self).__init__()

            self.yang_name = "help-locations"
            self.yang_parent_name = "show-fpd"

            self.help_location = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ShowFpd.HelpLocations, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ShowFpd.HelpLocations, self).__setattr__(name, value)


        class HelpLocation(Entity):
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
                super(ShowFpd.HelpLocations.HelpLocation, self).__init__()

                self.yang_name = "help-location"
                self.yang_parent_name = "help-locations"

                self.location_name = YLeaf(YType.str, "location-name")

                self.help_fpd = ShowFpd.HelpLocations.HelpLocation.HelpFpd()
                self.help_fpd.parent = self
                self._children_name_map["help_fpd"] = "help-fpd"
                self._children_yang_names.add("help-fpd")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("location_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ShowFpd.HelpLocations.HelpLocation, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ShowFpd.HelpLocations.HelpLocation, self).__setattr__(name, value)


            class HelpFpd(Entity):
                """
                Display fpds on given locations
                
                .. attribute:: fpd_name
                
                	Fpd name list
                	**type**\: list of    :py:class:`FpdName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HelpLocations.HelpLocation.HelpFpd.FpdName>`
                
                

                """

                _prefix = 'show-fpd-loc-ng-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ShowFpd.HelpLocations.HelpLocation.HelpFpd, self).__init__()

                    self.yang_name = "help-fpd"
                    self.yang_parent_name = "help-location"

                    self.fpd_name = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ShowFpd.HelpLocations.HelpLocation.HelpFpd, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ShowFpd.HelpLocations.HelpLocation.HelpFpd, self).__setattr__(name, value)


                class FpdName(Entity):
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
                        super(ShowFpd.HelpLocations.HelpLocation.HelpFpd.FpdName, self).__init__()

                        self.yang_name = "fpd-name"
                        self.yang_parent_name = "help-fpd"

                        self.fpd_name = YLeaf(YType.str, "fpd-name")

                        self.location = YLeaf(YType.str, "location")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("fpd_name",
                                        "location") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ShowFpd.HelpLocations.HelpLocation.HelpFpd.FpdName, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ShowFpd.HelpLocations.HelpLocation.HelpFpd.FpdName, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.fpd_name.is_set or
                            self.location.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.fpd_name.yfilter != YFilter.not_set or
                            self.location.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "fpd-name" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.fpd_name.is_set or self.fpd_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fpd_name.get_name_leafdata())
                        if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.location.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "fpd-name" or name == "location"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "fpd-name"):
                            self.fpd_name = value
                            self.fpd_name.value_namespace = name_space
                            self.fpd_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "location"):
                            self.location = value
                            self.location.value_namespace = name_space
                            self.location.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.fpd_name:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.fpd_name:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "help-fpd" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "fpd-name"):
                        for c in self.fpd_name:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ShowFpd.HelpLocations.HelpLocation.HelpFpd.FpdName()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.fpd_name.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "fpd-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.location_name.is_set or
                    (self.help_fpd is not None and self.help_fpd.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.location_name.yfilter != YFilter.not_set or
                    (self.help_fpd is not None and self.help_fpd.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "help-location" + "[location-name='" + self.location_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/help-locations/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.location_name.is_set or self.location_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.location_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "help-fpd"):
                    if (self.help_fpd is None):
                        self.help_fpd = ShowFpd.HelpLocations.HelpLocation.HelpFpd()
                        self.help_fpd.parent = self
                        self._children_name_map["help_fpd"] = "help-fpd"
                    return self.help_fpd

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "help-fpd" or name == "location-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "location-name"):
                    self.location_name = value
                    self.location_name.value_namespace = name_space
                    self.location_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.help_location:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.help_location:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "help-locations" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "help-location"):
                for c in self.help_location:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ShowFpd.HelpLocations.HelpLocation()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.help_location.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "help-location"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class HwModuleFpdHelpFpd(Entity):
        """
        Display help\-fpd \-show hw\-module fpd help\-fpd
        
        .. attribute:: fpd_name
        
        	Fpd name list
        	**type**\: list of    :py:class:`FpdName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.HwModuleFpdHelpFpd.FpdName>`
        
        

        """

        _prefix = 'show-fpd-loc-ng-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ShowFpd.HwModuleFpdHelpFpd, self).__init__()

            self.yang_name = "hw-module-fpd-help-fpd"
            self.yang_parent_name = "show-fpd"

            self.fpd_name = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ShowFpd.HwModuleFpdHelpFpd, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ShowFpd.HwModuleFpdHelpFpd, self).__setattr__(name, value)


        class FpdName(Entity):
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
                super(ShowFpd.HwModuleFpdHelpFpd.FpdName, self).__init__()

                self.yang_name = "fpd-name"
                self.yang_parent_name = "hw-module-fpd-help-fpd"

                self.fpd_name = YLeaf(YType.str, "fpd-name")

                self.location = YLeaf(YType.str, "location")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("fpd_name",
                                "location") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ShowFpd.HwModuleFpdHelpFpd.FpdName, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ShowFpd.HwModuleFpdHelpFpd.FpdName, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.fpd_name.is_set or
                    self.location.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.fpd_name.yfilter != YFilter.not_set or
                    self.location.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "fpd-name" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/hw-module-fpd-help-fpd/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.fpd_name.is_set or self.fpd_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.fpd_name.get_name_leafdata())
                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.location.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "fpd-name" or name == "location"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "fpd-name"):
                    self.fpd_name = value
                    self.fpd_name.value_namespace = name_space
                    self.fpd_name.value_namespace_prefix = name_space_prefix
                if(value_path == "location"):
                    self.location = value
                    self.location.value_namespace = name_space
                    self.location.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.fpd_name:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.fpd_name:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "hw-module-fpd-help-fpd" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "fpd-name"):
                for c in self.fpd_name:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ShowFpd.HwModuleFpdHelpFpd.FpdName()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.fpd_name.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "fpd-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Package(Entity):
        """
        gets fpd package info
        
        .. attribute:: fpd_pkg_data
        
        	 fpd pkg list 
        	**type**\: list of    :py:class:`FpdPkgData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.Package.FpdPkgData>`
        
        

        """

        _prefix = 'show-fpd-loc-ng-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ShowFpd.Package, self).__init__()

            self.yang_name = "package"
            self.yang_parent_name = "show-fpd"

            self.fpd_pkg_data = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ShowFpd.Package, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ShowFpd.Package, self).__setattr__(name, value)


        class FpdPkgData(Entity):
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
                super(ShowFpd.Package.FpdPkgData, self).__init__()

                self.yang_name = "fpd-pkg-data"
                self.yang_parent_name = "package"

                self.card_type = YLeaf(YType.str, "card-type")

                self.fpd_desc = YLeaf(YType.str, "fpd-desc")

                self.fpd_ver = YLeaf(YType.str, "fpd-ver")

                self.min_hw_ver = YLeaf(YType.str, "min-hw-ver")

                self.min_sw_ver = YLeaf(YType.str, "min-sw-ver")

                self.upgrade_method = YLeaf(YType.str, "upgrade-method")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("card_type",
                                "fpd_desc",
                                "fpd_ver",
                                "min_hw_ver",
                                "min_sw_ver",
                                "upgrade_method") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ShowFpd.Package.FpdPkgData, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ShowFpd.Package.FpdPkgData, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.card_type.is_set or
                    self.fpd_desc.is_set or
                    self.fpd_ver.is_set or
                    self.min_hw_ver.is_set or
                    self.min_sw_ver.is_set or
                    self.upgrade_method.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.card_type.yfilter != YFilter.not_set or
                    self.fpd_desc.yfilter != YFilter.not_set or
                    self.fpd_ver.yfilter != YFilter.not_set or
                    self.min_hw_ver.yfilter != YFilter.not_set or
                    self.min_sw_ver.yfilter != YFilter.not_set or
                    self.upgrade_method.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "fpd-pkg-data" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/package/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.card_type.is_set or self.card_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.card_type.get_name_leafdata())
                if (self.fpd_desc.is_set or self.fpd_desc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.fpd_desc.get_name_leafdata())
                if (self.fpd_ver.is_set or self.fpd_ver.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.fpd_ver.get_name_leafdata())
                if (self.min_hw_ver.is_set or self.min_hw_ver.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.min_hw_ver.get_name_leafdata())
                if (self.min_sw_ver.is_set or self.min_sw_ver.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.min_sw_ver.get_name_leafdata())
                if (self.upgrade_method.is_set or self.upgrade_method.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.upgrade_method.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "card-type" or name == "fpd-desc" or name == "fpd-ver" or name == "min-hw-ver" or name == "min-sw-ver" or name == "upgrade-method"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "card-type"):
                    self.card_type = value
                    self.card_type.value_namespace = name_space
                    self.card_type.value_namespace_prefix = name_space_prefix
                if(value_path == "fpd-desc"):
                    self.fpd_desc = value
                    self.fpd_desc.value_namespace = name_space
                    self.fpd_desc.value_namespace_prefix = name_space_prefix
                if(value_path == "fpd-ver"):
                    self.fpd_ver = value
                    self.fpd_ver.value_namespace = name_space
                    self.fpd_ver.value_namespace_prefix = name_space_prefix
                if(value_path == "min-hw-ver"):
                    self.min_hw_ver = value
                    self.min_hw_ver.value_namespace = name_space
                    self.min_hw_ver.value_namespace_prefix = name_space_prefix
                if(value_path == "min-sw-ver"):
                    self.min_sw_ver = value
                    self.min_sw_ver.value_namespace = name_space
                    self.min_sw_ver.value_namespace_prefix = name_space_prefix
                if(value_path == "upgrade-method"):
                    self.upgrade_method = value
                    self.upgrade_method.value_namespace = name_space
                    self.upgrade_method.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.fpd_pkg_data:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.fpd_pkg_data:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "package" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "fpd-pkg-data"):
                for c in self.fpd_pkg_data:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ShowFpd.Package.FpdPkgData()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.fpd_pkg_data.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "fpd-pkg-data"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class LocationHelp(Entity):
        """
        fpd upgradable locations
        
        .. attribute:: location_name
        
        	card location list
        	**type**\: list of    :py:class:`LocationName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_show_fpd_loc_ng_oper.ShowFpd.LocationHelp.LocationName>`
        
        

        """

        _prefix = 'show-fpd-loc-ng-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ShowFpd.LocationHelp, self).__init__()

            self.yang_name = "location-help"
            self.yang_parent_name = "show-fpd"

            self.location_name = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ShowFpd.LocationHelp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ShowFpd.LocationHelp, self).__setattr__(name, value)


        class LocationName(Entity):
            """
            card location list
            
            .. attribute:: location_name
            
            	card location
            	**type**\:  str
            
            

            """

            _prefix = 'show-fpd-loc-ng-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ShowFpd.LocationHelp.LocationName, self).__init__()

                self.yang_name = "location-name"
                self.yang_parent_name = "location-help"

                self.location_name = YLeaf(YType.str, "location-name")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("location_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ShowFpd.LocationHelp.LocationName, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ShowFpd.LocationHelp.LocationName, self).__setattr__(name, value)

            def has_data(self):
                return self.location_name.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.location_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "location-name" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/location-help/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.location_name.is_set or self.location_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.location_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "location-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "location-name"):
                    self.location_name = value
                    self.location_name.value_namespace = name_space
                    self.location_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.location_name:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.location_name:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "location-help" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "location-name"):
                for c in self.location_name:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ShowFpd.LocationHelp.LocationName()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.location_name.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "location-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.help_locations is not None and self.help_locations.has_data()) or
            (self.hw_module_fpd is not None and self.hw_module_fpd.has_data()) or
            (self.hw_module_fpd_help_fpd is not None and self.hw_module_fpd_help_fpd.has_data()) or
            (self.location_help is not None and self.location_help.has_data()) or
            (self.locations is not None and self.locations.has_data()) or
            (self.package is not None and self.package.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.help_locations is not None and self.help_locations.has_operation()) or
            (self.hw_module_fpd is not None and self.hw_module_fpd.has_operation()) or
            (self.hw_module_fpd_help_fpd is not None and self.hw_module_fpd_help_fpd.has_operation()) or
            (self.location_help is not None and self.location_help.has_operation()) or
            (self.locations is not None and self.locations.has_operation()) or
            (self.package is not None and self.package.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-show-fpd-loc-ng-oper:show-fpd" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "help-locations"):
            if (self.help_locations is None):
                self.help_locations = ShowFpd.HelpLocations()
                self.help_locations.parent = self
                self._children_name_map["help_locations"] = "help-locations"
            return self.help_locations

        if (child_yang_name == "hw-module-fpd"):
            if (self.hw_module_fpd is None):
                self.hw_module_fpd = ShowFpd.HwModuleFpd()
                self.hw_module_fpd.parent = self
                self._children_name_map["hw_module_fpd"] = "hw-module-fpd"
            return self.hw_module_fpd

        if (child_yang_name == "hw-module-fpd-help-fpd"):
            if (self.hw_module_fpd_help_fpd is None):
                self.hw_module_fpd_help_fpd = ShowFpd.HwModuleFpdHelpFpd()
                self.hw_module_fpd_help_fpd.parent = self
                self._children_name_map["hw_module_fpd_help_fpd"] = "hw-module-fpd-help-fpd"
            return self.hw_module_fpd_help_fpd

        if (child_yang_name == "location-help"):
            if (self.location_help is None):
                self.location_help = ShowFpd.LocationHelp()
                self.location_help.parent = self
                self._children_name_map["location_help"] = "location-help"
            return self.location_help

        if (child_yang_name == "locations"):
            if (self.locations is None):
                self.locations = ShowFpd.Locations()
                self.locations.parent = self
                self._children_name_map["locations"] = "locations"
            return self.locations

        if (child_yang_name == "package"):
            if (self.package is None):
                self.package = ShowFpd.Package()
                self.package.parent = self
                self._children_name_map["package"] = "package"
            return self.package

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "help-locations" or name == "hw-module-fpd" or name == "hw-module-fpd-help-fpd" or name == "location-help" or name == "locations" or name == "package"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ShowFpd()
        return self._top_entity

