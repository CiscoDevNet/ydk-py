""" CISCO_IMAGE_LICENSE_MGMT_MIB 

The MIB module for managing the running image level
of a Cisco device. Cisco's licensing mechanism provides
flexibility to run a device on a chosen image level.
This mechanism is referred to as image level licensing.
Image level licensing leverages the universal image
based licensing solution.

The image level licensing mechanism works as follows \- 

A universal image that contains all levels of software
packages is loaded on to the device. At boot time, the
device determines the highest level of license and brings
up the appropriate software features or subsystems.
The user can configure the image level with which the
device has to boot. The system will verify whether the
appropriate license is available for the configured image
level. The image level for the next boot will be determined
based on the availability of the license. The following
scenarios explains some use\-cases of image level licensing\:

Scenario 1\:
\- Customer selects advsecurityk9 based image.
\- Manufacturing installs advsecurity license on the device.
\- This device will run all features that are part of the
base advsecurity license.
\- Customer upgrades to advipservicesk9 license.
\- The next boot level is set to advipservicesk9.
\- The device will run advsecurityk9 feature until the
next reboot. After reboot the device will run 
advipservicesk9 features.

Scenario 2\:
\- Customer selects advipservicesk9 based image.
\- Manufacturing installs advipservices and advsecurity
license on the device.
\- This device will run all features that are part of the
base advipservices license.
\- No upgrades available for advipservices license.

The user has to accept the End User License Agreement(EULA)
before using this MIB to configure the image level. 

This MIB should be used in conjuntion with
CISCO\-LICENSE\-MGMT\-MIB module to achieve the image level
licensing functionality.

This MIB module defines objects which provides the different
image levels supported by the device and the license required
to enable a particular image level. It also defines objects
to let the user configure the required image level. The MIB 
module contains notification which will be triggered when
the user changes the image level for next boot. 

The CISCO\-LICENSE\-MGMT\-MIB module should be used to export
the EULA and to configure the required license.

This MIB module is defined generically so it can be used for
both stand\-alone as well as stackable devices. The
entPhysicalIndex imported from ENTITY\-MIB is used to identify
the device uniquely.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoImageLicenseMgmtMib(Entity):
    """
    
    
    .. attribute:: cilmbootimageleveltable
    
    	A table that contains the configuration information of current and next boot image level. This table contains entries for each software module running in an image  loaded in the device. The software module is identified by cilmModuleName and the device is identified by  entPhysicalIndex
    	**type**\:   :py:class:`Cilmbootimageleveltable <ydk.models.cisco_ios_xe.CISCO_IMAGE_LICENSE_MGMT_MIB.CiscoImageLicenseMgmtMib.Cilmbootimageleveltable>`
    
    .. attribute:: cilmimageleveltolicensemaptable
    
    	This table contains the mapping between different image levels of each modules in the image and the license required to run the modules at a particular image level. This table can be used to identify the different image levels and the appropriate licenses  required for each
    	**type**\:   :py:class:`Cilmimageleveltolicensemaptable <ydk.models.cisco_ios_xe.CISCO_IMAGE_LICENSE_MGMT_MIB.CiscoImageLicenseMgmtMib.Cilmimageleveltolicensemaptable>`
    
    .. attribute:: cilmnotifcntl
    
    	
    	**type**\:   :py:class:`Cilmnotifcntl <ydk.models.cisco_ios_xe.CISCO_IMAGE_LICENSE_MGMT_MIB.CiscoImageLicenseMgmtMib.Cilmnotifcntl>`
    
    .. attribute:: ciscoimagelicensemgmtmibobjects
    
    	
    	**type**\:   :py:class:`Ciscoimagelicensemgmtmibobjects <ydk.models.cisco_ios_xe.CISCO_IMAGE_LICENSE_MGMT_MIB.CiscoImageLicenseMgmtMib.Ciscoimagelicensemgmtmibobjects>`
    
    

    """

    _prefix = 'CISCO-IMAGE-LICENSE-MGMT-MIB'
    _revision = '2007-10-16'

    def __init__(self):
        super(CiscoImageLicenseMgmtMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IMAGE-LICENSE-MGMT-MIB"
        self.yang_parent_name = "CISCO-IMAGE-LICENSE-MGMT-MIB"

        self.cilmbootimageleveltable = CiscoImageLicenseMgmtMib.Cilmbootimageleveltable()
        self.cilmbootimageleveltable.parent = self
        self._children_name_map["cilmbootimageleveltable"] = "cilmBootImageLevelTable"
        self._children_yang_names.add("cilmBootImageLevelTable")

        self.cilmimageleveltolicensemaptable = CiscoImageLicenseMgmtMib.Cilmimageleveltolicensemaptable()
        self.cilmimageleveltolicensemaptable.parent = self
        self._children_name_map["cilmimageleveltolicensemaptable"] = "cilmImageLevelToLicenseMapTable"
        self._children_yang_names.add("cilmImageLevelToLicenseMapTable")

        self.cilmnotifcntl = CiscoImageLicenseMgmtMib.Cilmnotifcntl()
        self.cilmnotifcntl.parent = self
        self._children_name_map["cilmnotifcntl"] = "cilmNotifCntl"
        self._children_yang_names.add("cilmNotifCntl")

        self.ciscoimagelicensemgmtmibobjects = CiscoImageLicenseMgmtMib.Ciscoimagelicensemgmtmibobjects()
        self.ciscoimagelicensemgmtmibobjects.parent = self
        self._children_name_map["ciscoimagelicensemgmtmibobjects"] = "ciscoImageLicenseMgmtMIBObjects"
        self._children_yang_names.add("ciscoImageLicenseMgmtMIBObjects")


    class Ciscoimagelicensemgmtmibobjects(Entity):
        """
        
        
        .. attribute:: cilmeulaaccepted
        
        	This object when set to TRUE means that the user has accepted the END USER LICENSE AGREEMENT. This object has to be set to TRUE by the user before using the objects in the cilmBootImageLevelTable to configure the license
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-IMAGE-LICENSE-MGMT-MIB'
        _revision = '2007-10-16'

        def __init__(self):
            super(CiscoImageLicenseMgmtMib.Ciscoimagelicensemgmtmibobjects, self).__init__()

            self.yang_name = "ciscoImageLicenseMgmtMIBObjects"
            self.yang_parent_name = "CISCO-IMAGE-LICENSE-MGMT-MIB"

            self.cilmeulaaccepted = YLeaf(YType.boolean, "cilmEULAAccepted")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cilmeulaaccepted") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoImageLicenseMgmtMib.Ciscoimagelicensemgmtmibobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoImageLicenseMgmtMib.Ciscoimagelicensemgmtmibobjects, self).__setattr__(name, value)

        def has_data(self):
            return self.cilmeulaaccepted.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cilmeulaaccepted.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoImageLicenseMgmtMIBObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cilmeulaaccepted.is_set or self.cilmeulaaccepted.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cilmeulaaccepted.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cilmEULAAccepted"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cilmEULAAccepted"):
                self.cilmeulaaccepted = value
                self.cilmeulaaccepted.value_namespace = name_space
                self.cilmeulaaccepted.value_namespace_prefix = name_space_prefix


    class Cilmnotifcntl(Entity):
        """
        
        
        .. attribute:: cilmimagelevelchangednotif
        
        	Specify whether or not a notification should be generated on the detection of change in next boot image level.  If set to TRUE, cilmBootImageLevelChanged notification will be generated. It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the  notification to be delivered
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-IMAGE-LICENSE-MGMT-MIB'
        _revision = '2007-10-16'

        def __init__(self):
            super(CiscoImageLicenseMgmtMib.Cilmnotifcntl, self).__init__()

            self.yang_name = "cilmNotifCntl"
            self.yang_parent_name = "CISCO-IMAGE-LICENSE-MGMT-MIB"

            self.cilmimagelevelchangednotif = YLeaf(YType.boolean, "cilmImageLevelChangedNotif")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cilmimagelevelchangednotif") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoImageLicenseMgmtMib.Cilmnotifcntl, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoImageLicenseMgmtMib.Cilmnotifcntl, self).__setattr__(name, value)

        def has_data(self):
            return self.cilmimagelevelchangednotif.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cilmimagelevelchangednotif.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cilmNotifCntl" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cilmimagelevelchangednotif.is_set or self.cilmimagelevelchangednotif.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cilmimagelevelchangednotif.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cilmImageLevelChangedNotif"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cilmImageLevelChangedNotif"):
                self.cilmimagelevelchangednotif = value
                self.cilmimagelevelchangednotif.value_namespace = name_space
                self.cilmimagelevelchangednotif.value_namespace_prefix = name_space_prefix


    class Cilmbootimageleveltable(Entity):
        """
        A table that contains the configuration information of
        current and next boot image level. This table contains
        entries for each software module running in an image 
        loaded in the device. The software module is identified by
        cilmModuleName and the device is identified by 
        entPhysicalIndex.
        
        .. attribute:: cilmbootimagelevelentry
        
        	An entry in the table for each module containing the list of objects that define the configuration of next boot level. The following information is specified by the objects present in the table.  \- Current image level. \- Configured image level for the next boot. \- Actual image level for the next boot. \- License store index for the current license. \- License index of the current license. \- License store index for the next boot license. \- License index of the next boot license
        	**type**\: list of    :py:class:`Cilmbootimagelevelentry <ydk.models.cisco_ios_xe.CISCO_IMAGE_LICENSE_MGMT_MIB.CiscoImageLicenseMgmtMib.Cilmbootimageleveltable.Cilmbootimagelevelentry>`
        
        

        """

        _prefix = 'CISCO-IMAGE-LICENSE-MGMT-MIB'
        _revision = '2007-10-16'

        def __init__(self):
            super(CiscoImageLicenseMgmtMib.Cilmbootimageleveltable, self).__init__()

            self.yang_name = "cilmBootImageLevelTable"
            self.yang_parent_name = "CISCO-IMAGE-LICENSE-MGMT-MIB"

            self.cilmbootimagelevelentry = YList(self)

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
                        super(CiscoImageLicenseMgmtMib.Cilmbootimageleveltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoImageLicenseMgmtMib.Cilmbootimageleveltable, self).__setattr__(name, value)


        class Cilmbootimagelevelentry(Entity):
            """
            An entry in the table for each module containing the
            list of objects that define the configuration of next
            boot level. The following information is specified by
            the objects present in the table.
            
            \- Current image level.
            \- Configured image level for the next boot.
            \- Actual image level for the next boot.
            \- License store index for the current license.
            \- License index of the current license.
            \- License store index for the next boot license.
            \- License index of the next boot license.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cilmmodulename  <key>
            
            	This object is used as one of the two indices in cilmBootImageLevelTable. This object indicates the module name of the software package. There can be multiple modules in an image performing specific functionality. For example, in a wireless image there can be two modules \- a base image module and a wireless module
            	**type**\:  str
            
            .. attribute:: cilmconfiguredbootimagelevel
            
            	This object indicates the configured image level of the module for the next boot.  Note\: The configured next boot image level may not  be the actual next boot image level. The actual next boot image level is denoted by cilmNextBootImageLevel which is determined based on the license availability
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cilmcurrentimagelevel
            
            	This object indicates the current image level that the module is running
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cilmcurrentlicenseindex
            
            	This object indicates the license index of the currently used license. This object has the same value as clmgmtLicenseIndex and uniquely identifies an entry in clmgmtLicenseInfoTable in CISCO\-LICENSE\-MGMT\-MIB.  Note\: The license index can be '0' if no license is installed and device is running base image
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cilmcurrentlicensestoreindex
            
            	This object indicates the license store index where the currently used license is stored. This object has the same value as clmgmtLicenseStoreIndex object and uniquely identifies an entry in clmgmtLicenseStoreInfoTable in CISCO\-LICENSE\-MGMT\-MIB.  Note\: The license store index can be '0' if no license is installed and device is running base image
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cilmnextbootimagelevel
            
            	This object indicates the next boot image level. The next boot image level can be different from configured level. The next boot image level is determined based on the availability of required license
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cilmnextbootlicenseindex
            
            	This object indicates the license index of the next boot license. This object has the same value as clmgmtLicenseIndex and uniquely identifies an entry in clmgmtLicenseInfoTable in CISCO\-LICENSE\-MGMT\-MIB.  Note\: The license index can be '0' if no license is installed for the next boot
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cilmnextbootlicensestoreindex
            
            	This object indicates the license store index where the next boot license is stored. This object has the same value as clmgmtLicenseStoreIndex object and uniquely identifies an entry in clmgmtLicenseStoreInfoTable in CISCO\-LICENSE\-MGMT\-MIB.  Note\: The license store index can be '0' if no license is installed for the next boot
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IMAGE-LICENSE-MGMT-MIB'
            _revision = '2007-10-16'

            def __init__(self):
                super(CiscoImageLicenseMgmtMib.Cilmbootimageleveltable.Cilmbootimagelevelentry, self).__init__()

                self.yang_name = "cilmBootImageLevelEntry"
                self.yang_parent_name = "cilmBootImageLevelTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cilmmodulename = YLeaf(YType.str, "cilmModuleName")

                self.cilmconfiguredbootimagelevel = YLeaf(YType.str, "cilmConfiguredBootImageLevel")

                self.cilmcurrentimagelevel = YLeaf(YType.str, "cilmCurrentImageLevel")

                self.cilmcurrentlicenseindex = YLeaf(YType.uint32, "cilmCurrentLicenseIndex")

                self.cilmcurrentlicensestoreindex = YLeaf(YType.uint32, "cilmCurrentLicenseStoreIndex")

                self.cilmnextbootimagelevel = YLeaf(YType.str, "cilmNextBootImageLevel")

                self.cilmnextbootlicenseindex = YLeaf(YType.uint32, "cilmNextBootLicenseIndex")

                self.cilmnextbootlicensestoreindex = YLeaf(YType.uint32, "cilmNextBootLicenseStoreIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cilmmodulename",
                                "cilmconfiguredbootimagelevel",
                                "cilmcurrentimagelevel",
                                "cilmcurrentlicenseindex",
                                "cilmcurrentlicensestoreindex",
                                "cilmnextbootimagelevel",
                                "cilmnextbootlicenseindex",
                                "cilmnextbootlicensestoreindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoImageLicenseMgmtMib.Cilmbootimageleveltable.Cilmbootimagelevelentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoImageLicenseMgmtMib.Cilmbootimageleveltable.Cilmbootimagelevelentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cilmmodulename.is_set or
                    self.cilmconfiguredbootimagelevel.is_set or
                    self.cilmcurrentimagelevel.is_set or
                    self.cilmcurrentlicenseindex.is_set or
                    self.cilmcurrentlicensestoreindex.is_set or
                    self.cilmnextbootimagelevel.is_set or
                    self.cilmnextbootlicenseindex.is_set or
                    self.cilmnextbootlicensestoreindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cilmmodulename.yfilter != YFilter.not_set or
                    self.cilmconfiguredbootimagelevel.yfilter != YFilter.not_set or
                    self.cilmcurrentimagelevel.yfilter != YFilter.not_set or
                    self.cilmcurrentlicenseindex.yfilter != YFilter.not_set or
                    self.cilmcurrentlicensestoreindex.yfilter != YFilter.not_set or
                    self.cilmnextbootimagelevel.yfilter != YFilter.not_set or
                    self.cilmnextbootlicenseindex.yfilter != YFilter.not_set or
                    self.cilmnextbootlicensestoreindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cilmBootImageLevelEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cilmModuleName='" + self.cilmmodulename.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/cilmBootImageLevelTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cilmmodulename.is_set or self.cilmmodulename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cilmmodulename.get_name_leafdata())
                if (self.cilmconfiguredbootimagelevel.is_set or self.cilmconfiguredbootimagelevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cilmconfiguredbootimagelevel.get_name_leafdata())
                if (self.cilmcurrentimagelevel.is_set or self.cilmcurrentimagelevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cilmcurrentimagelevel.get_name_leafdata())
                if (self.cilmcurrentlicenseindex.is_set or self.cilmcurrentlicenseindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cilmcurrentlicenseindex.get_name_leafdata())
                if (self.cilmcurrentlicensestoreindex.is_set or self.cilmcurrentlicensestoreindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cilmcurrentlicensestoreindex.get_name_leafdata())
                if (self.cilmnextbootimagelevel.is_set or self.cilmnextbootimagelevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cilmnextbootimagelevel.get_name_leafdata())
                if (self.cilmnextbootlicenseindex.is_set or self.cilmnextbootlicenseindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cilmnextbootlicenseindex.get_name_leafdata())
                if (self.cilmnextbootlicensestoreindex.is_set or self.cilmnextbootlicensestoreindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cilmnextbootlicensestoreindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cilmModuleName" or name == "cilmConfiguredBootImageLevel" or name == "cilmCurrentImageLevel" or name == "cilmCurrentLicenseIndex" or name == "cilmCurrentLicenseStoreIndex" or name == "cilmNextBootImageLevel" or name == "cilmNextBootLicenseIndex" or name == "cilmNextBootLicenseStoreIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cilmModuleName"):
                    self.cilmmodulename = value
                    self.cilmmodulename.value_namespace = name_space
                    self.cilmmodulename.value_namespace_prefix = name_space_prefix
                if(value_path == "cilmConfiguredBootImageLevel"):
                    self.cilmconfiguredbootimagelevel = value
                    self.cilmconfiguredbootimagelevel.value_namespace = name_space
                    self.cilmconfiguredbootimagelevel.value_namespace_prefix = name_space_prefix
                if(value_path == "cilmCurrentImageLevel"):
                    self.cilmcurrentimagelevel = value
                    self.cilmcurrentimagelevel.value_namespace = name_space
                    self.cilmcurrentimagelevel.value_namespace_prefix = name_space_prefix
                if(value_path == "cilmCurrentLicenseIndex"):
                    self.cilmcurrentlicenseindex = value
                    self.cilmcurrentlicenseindex.value_namespace = name_space
                    self.cilmcurrentlicenseindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cilmCurrentLicenseStoreIndex"):
                    self.cilmcurrentlicensestoreindex = value
                    self.cilmcurrentlicensestoreindex.value_namespace = name_space
                    self.cilmcurrentlicensestoreindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cilmNextBootImageLevel"):
                    self.cilmnextbootimagelevel = value
                    self.cilmnextbootimagelevel.value_namespace = name_space
                    self.cilmnextbootimagelevel.value_namespace_prefix = name_space_prefix
                if(value_path == "cilmNextBootLicenseIndex"):
                    self.cilmnextbootlicenseindex = value
                    self.cilmnextbootlicenseindex.value_namespace = name_space
                    self.cilmnextbootlicenseindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cilmNextBootLicenseStoreIndex"):
                    self.cilmnextbootlicensestoreindex = value
                    self.cilmnextbootlicensestoreindex.value_namespace = name_space
                    self.cilmnextbootlicensestoreindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cilmbootimagelevelentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cilmbootimagelevelentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cilmBootImageLevelTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cilmBootImageLevelEntry"):
                for c in self.cilmbootimagelevelentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoImageLicenseMgmtMib.Cilmbootimageleveltable.Cilmbootimagelevelentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cilmbootimagelevelentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cilmBootImageLevelEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cilmimageleveltolicensemaptable(Entity):
        """
        This table contains the mapping between different
        image levels of each modules in the image and the
        license required to run the modules at a particular
        image level. This table can be used to identify the
        different image levels and the appropriate licenses 
        required for each.
        
        .. attribute:: cilmimageleveltolicensemapentry
        
        	An entry in the table containing the following information. \- The image levels at the which the modules can be run. \- The license required to the run a module at a particular image level. \- The priority of the license
        	**type**\: list of    :py:class:`Cilmimageleveltolicensemapentry <ydk.models.cisco_ios_xe.CISCO_IMAGE_LICENSE_MGMT_MIB.CiscoImageLicenseMgmtMib.Cilmimageleveltolicensemaptable.Cilmimageleveltolicensemapentry>`
        
        

        """

        _prefix = 'CISCO-IMAGE-LICENSE-MGMT-MIB'
        _revision = '2007-10-16'

        def __init__(self):
            super(CiscoImageLicenseMgmtMib.Cilmimageleveltolicensemaptable, self).__init__()

            self.yang_name = "cilmImageLevelToLicenseMapTable"
            self.yang_parent_name = "CISCO-IMAGE-LICENSE-MGMT-MIB"

            self.cilmimageleveltolicensemapentry = YList(self)

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
                        super(CiscoImageLicenseMgmtMib.Cilmimageleveltolicensemaptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoImageLicenseMgmtMib.Cilmimageleveltolicensemaptable, self).__setattr__(name, value)


        class Cilmimageleveltolicensemapentry(Entity):
            """
            An entry in the table containing the following
            information.
            \- The image levels at the which the modules can be run.
            \- The license required to the run a module at a
            particular image level.
            \- The priority of the license.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cilmmodulename  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`cilmmodulename <ydk.models.cisco_ios_xe.CISCO_IMAGE_LICENSE_MGMT_MIB.CiscoImageLicenseMgmtMib.Cilmbootimageleveltable.Cilmbootimagelevelentry>`
            
            .. attribute:: cilmimagelicensemapindex  <key>
            
            	This is a running index used to identify an entry of this table
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cilmimagelicenseimagelevel
            
            	This object indicates the image level at which a module can be run. A module can be run at different image levels. An entry will be created in this table for every module and image level combination
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cilmimagelicensename
            
            	This object indicates the list of licenses needed to be installed for the module to run at the image level mentioned by cilmImageLicenseImageLevel object of this entry
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cilmimagelicensepriority
            
            	This object indicates the priority of the image level mentioned by cilmImageLicenseImageLevel object of this entry. The image level with the highest priority license will be considered as the default level in the absense of next boot image level configuration. For example if there are three licenses l1, l2 and l3 in the ascending order of priority, then by default l1 will be the level at which the module will be running. If the next boot level is configured then the configuration will override the priority. The highest priority license supports a feature set which is a super set of all other licenses
            	**type**\:  int
            
            	**range:** 1..255
            
            

            """

            _prefix = 'CISCO-IMAGE-LICENSE-MGMT-MIB'
            _revision = '2007-10-16'

            def __init__(self):
                super(CiscoImageLicenseMgmtMib.Cilmimageleveltolicensemaptable.Cilmimageleveltolicensemapentry, self).__init__()

                self.yang_name = "cilmImageLevelToLicenseMapEntry"
                self.yang_parent_name = "cilmImageLevelToLicenseMapTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cilmmodulename = YLeaf(YType.str, "cilmModuleName")

                self.cilmimagelicensemapindex = YLeaf(YType.uint32, "cilmImageLicenseMapIndex")

                self.cilmimagelicenseimagelevel = YLeaf(YType.str, "cilmImageLicenseImageLevel")

                self.cilmimagelicensename = YLeaf(YType.str, "cilmImageLicenseName")

                self.cilmimagelicensepriority = YLeaf(YType.uint32, "cilmImageLicensePriority")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cilmmodulename",
                                "cilmimagelicensemapindex",
                                "cilmimagelicenseimagelevel",
                                "cilmimagelicensename",
                                "cilmimagelicensepriority") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoImageLicenseMgmtMib.Cilmimageleveltolicensemaptable.Cilmimageleveltolicensemapentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoImageLicenseMgmtMib.Cilmimageleveltolicensemaptable.Cilmimageleveltolicensemapentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cilmmodulename.is_set or
                    self.cilmimagelicensemapindex.is_set or
                    self.cilmimagelicenseimagelevel.is_set or
                    self.cilmimagelicensename.is_set or
                    self.cilmimagelicensepriority.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cilmmodulename.yfilter != YFilter.not_set or
                    self.cilmimagelicensemapindex.yfilter != YFilter.not_set or
                    self.cilmimagelicenseimagelevel.yfilter != YFilter.not_set or
                    self.cilmimagelicensename.yfilter != YFilter.not_set or
                    self.cilmimagelicensepriority.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cilmImageLevelToLicenseMapEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cilmModuleName='" + self.cilmmodulename.get() + "']" + "[cilmImageLicenseMapIndex='" + self.cilmimagelicensemapindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/cilmImageLevelToLicenseMapTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cilmmodulename.is_set or self.cilmmodulename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cilmmodulename.get_name_leafdata())
                if (self.cilmimagelicensemapindex.is_set or self.cilmimagelicensemapindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cilmimagelicensemapindex.get_name_leafdata())
                if (self.cilmimagelicenseimagelevel.is_set or self.cilmimagelicenseimagelevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cilmimagelicenseimagelevel.get_name_leafdata())
                if (self.cilmimagelicensename.is_set or self.cilmimagelicensename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cilmimagelicensename.get_name_leafdata())
                if (self.cilmimagelicensepriority.is_set or self.cilmimagelicensepriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cilmimagelicensepriority.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cilmModuleName" or name == "cilmImageLicenseMapIndex" or name == "cilmImageLicenseImageLevel" or name == "cilmImageLicenseName" or name == "cilmImageLicensePriority"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cilmModuleName"):
                    self.cilmmodulename = value
                    self.cilmmodulename.value_namespace = name_space
                    self.cilmmodulename.value_namespace_prefix = name_space_prefix
                if(value_path == "cilmImageLicenseMapIndex"):
                    self.cilmimagelicensemapindex = value
                    self.cilmimagelicensemapindex.value_namespace = name_space
                    self.cilmimagelicensemapindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cilmImageLicenseImageLevel"):
                    self.cilmimagelicenseimagelevel = value
                    self.cilmimagelicenseimagelevel.value_namespace = name_space
                    self.cilmimagelicenseimagelevel.value_namespace_prefix = name_space_prefix
                if(value_path == "cilmImageLicenseName"):
                    self.cilmimagelicensename = value
                    self.cilmimagelicensename.value_namespace = name_space
                    self.cilmimagelicensename.value_namespace_prefix = name_space_prefix
                if(value_path == "cilmImageLicensePriority"):
                    self.cilmimagelicensepriority = value
                    self.cilmimagelicensepriority.value_namespace = name_space
                    self.cilmimagelicensepriority.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cilmimageleveltolicensemapentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cilmimageleveltolicensemapentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cilmImageLevelToLicenseMapTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cilmImageLevelToLicenseMapEntry"):
                for c in self.cilmimageleveltolicensemapentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoImageLicenseMgmtMib.Cilmimageleveltolicensemaptable.Cilmimageleveltolicensemapentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cilmimageleveltolicensemapentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cilmImageLevelToLicenseMapEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cilmbootimageleveltable is not None and self.cilmbootimageleveltable.has_data()) or
            (self.cilmimageleveltolicensemaptable is not None and self.cilmimageleveltolicensemaptable.has_data()) or
            (self.cilmnotifcntl is not None and self.cilmnotifcntl.has_data()) or
            (self.ciscoimagelicensemgmtmibobjects is not None and self.ciscoimagelicensemgmtmibobjects.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cilmbootimageleveltable is not None and self.cilmbootimageleveltable.has_operation()) or
            (self.cilmimageleveltolicensemaptable is not None and self.cilmimageleveltolicensemaptable.has_operation()) or
            (self.cilmnotifcntl is not None and self.cilmnotifcntl.has_operation()) or
            (self.ciscoimagelicensemgmtmibobjects is not None and self.ciscoimagelicensemgmtmibobjects.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB" + path_buffer

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

        if (child_yang_name == "cilmBootImageLevelTable"):
            if (self.cilmbootimageleveltable is None):
                self.cilmbootimageleveltable = CiscoImageLicenseMgmtMib.Cilmbootimageleveltable()
                self.cilmbootimageleveltable.parent = self
                self._children_name_map["cilmbootimageleveltable"] = "cilmBootImageLevelTable"
            return self.cilmbootimageleveltable

        if (child_yang_name == "cilmImageLevelToLicenseMapTable"):
            if (self.cilmimageleveltolicensemaptable is None):
                self.cilmimageleveltolicensemaptable = CiscoImageLicenseMgmtMib.Cilmimageleveltolicensemaptable()
                self.cilmimageleveltolicensemaptable.parent = self
                self._children_name_map["cilmimageleveltolicensemaptable"] = "cilmImageLevelToLicenseMapTable"
            return self.cilmimageleveltolicensemaptable

        if (child_yang_name == "cilmNotifCntl"):
            if (self.cilmnotifcntl is None):
                self.cilmnotifcntl = CiscoImageLicenseMgmtMib.Cilmnotifcntl()
                self.cilmnotifcntl.parent = self
                self._children_name_map["cilmnotifcntl"] = "cilmNotifCntl"
            return self.cilmnotifcntl

        if (child_yang_name == "ciscoImageLicenseMgmtMIBObjects"):
            if (self.ciscoimagelicensemgmtmibobjects is None):
                self.ciscoimagelicensemgmtmibobjects = CiscoImageLicenseMgmtMib.Ciscoimagelicensemgmtmibobjects()
                self.ciscoimagelicensemgmtmibobjects.parent = self
                self._children_name_map["ciscoimagelicensemgmtmibobjects"] = "ciscoImageLicenseMgmtMIBObjects"
            return self.ciscoimagelicensemgmtmibobjects

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cilmBootImageLevelTable" or name == "cilmImageLevelToLicenseMapTable" or name == "cilmNotifCntl" or name == "ciscoImageLicenseMgmtMIBObjects"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoImageLicenseMgmtMib()
        return self._top_entity

