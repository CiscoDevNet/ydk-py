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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOIMAGELICENSEMGMTMIB(Entity):
    """
    
    
    .. attribute:: ciscoimagelicensemgmtmibobjects
    
    	
    	**type**\:  :py:class:`Ciscoimagelicensemgmtmibobjects <ydk.models.cisco_ios_xe.CISCO_IMAGE_LICENSE_MGMT_MIB.CISCOIMAGELICENSEMGMTMIB.Ciscoimagelicensemgmtmibobjects>`
    
    .. attribute:: cilmnotifcntl
    
    	
    	**type**\:  :py:class:`Cilmnotifcntl <ydk.models.cisco_ios_xe.CISCO_IMAGE_LICENSE_MGMT_MIB.CISCOIMAGELICENSEMGMTMIB.Cilmnotifcntl>`
    
    .. attribute:: cilmbootimageleveltable
    
    	A table that contains the configuration information of current and next boot image level. This table contains entries for each software module running in an image  loaded in the device. The software module is identified by cilmModuleName and the device is identified by  entPhysicalIndex
    	**type**\:  :py:class:`Cilmbootimageleveltable <ydk.models.cisco_ios_xe.CISCO_IMAGE_LICENSE_MGMT_MIB.CISCOIMAGELICENSEMGMTMIB.Cilmbootimageleveltable>`
    
    .. attribute:: cilmimageleveltolicensemaptable
    
    	This table contains the mapping between different image levels of each modules in the image and the license required to run the modules at a particular image level. This table can be used to identify the different image levels and the appropriate licenses  required for each
    	**type**\:  :py:class:`Cilmimageleveltolicensemaptable <ydk.models.cisco_ios_xe.CISCO_IMAGE_LICENSE_MGMT_MIB.CISCOIMAGELICENSEMGMTMIB.Cilmimageleveltolicensemaptable>`
    
    

    """

    _prefix = 'CISCO-IMAGE-LICENSE-MGMT-MIB'
    _revision = '2007-10-16'

    def __init__(self):
        super(CISCOIMAGELICENSEMGMTMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IMAGE-LICENSE-MGMT-MIB"
        self.yang_parent_name = "CISCO-IMAGE-LICENSE-MGMT-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ciscoImageLicenseMgmtMIBObjects", ("ciscoimagelicensemgmtmibobjects", CISCOIMAGELICENSEMGMTMIB.Ciscoimagelicensemgmtmibobjects)), ("cilmNotifCntl", ("cilmnotifcntl", CISCOIMAGELICENSEMGMTMIB.Cilmnotifcntl)), ("cilmBootImageLevelTable", ("cilmbootimageleveltable", CISCOIMAGELICENSEMGMTMIB.Cilmbootimageleveltable)), ("cilmImageLevelToLicenseMapTable", ("cilmimageleveltolicensemaptable", CISCOIMAGELICENSEMGMTMIB.Cilmimageleveltolicensemaptable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ciscoimagelicensemgmtmibobjects = CISCOIMAGELICENSEMGMTMIB.Ciscoimagelicensemgmtmibobjects()
        self.ciscoimagelicensemgmtmibobjects.parent = self
        self._children_name_map["ciscoimagelicensemgmtmibobjects"] = "ciscoImageLicenseMgmtMIBObjects"
        self._children_yang_names.add("ciscoImageLicenseMgmtMIBObjects")

        self.cilmnotifcntl = CISCOIMAGELICENSEMGMTMIB.Cilmnotifcntl()
        self.cilmnotifcntl.parent = self
        self._children_name_map["cilmnotifcntl"] = "cilmNotifCntl"
        self._children_yang_names.add("cilmNotifCntl")

        self.cilmbootimageleveltable = CISCOIMAGELICENSEMGMTMIB.Cilmbootimageleveltable()
        self.cilmbootimageleveltable.parent = self
        self._children_name_map["cilmbootimageleveltable"] = "cilmBootImageLevelTable"
        self._children_yang_names.add("cilmBootImageLevelTable")

        self.cilmimageleveltolicensemaptable = CISCOIMAGELICENSEMGMTMIB.Cilmimageleveltolicensemaptable()
        self.cilmimageleveltolicensemaptable.parent = self
        self._children_name_map["cilmimageleveltolicensemaptable"] = "cilmImageLevelToLicenseMapTable"
        self._children_yang_names.add("cilmImageLevelToLicenseMapTable")
        self._segment_path = lambda: "CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB"


    class Ciscoimagelicensemgmtmibobjects(Entity):
        """
        
        
        .. attribute:: cilmeulaaccepted
        
        	This object when set to TRUE means that the user has accepted the END USER LICENSE AGREEMENT. This object has to be set to TRUE by the user before using the objects in the cilmBootImageLevelTable to configure the license
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-IMAGE-LICENSE-MGMT-MIB'
        _revision = '2007-10-16'

        def __init__(self):
            super(CISCOIMAGELICENSEMGMTMIB.Ciscoimagelicensemgmtmibobjects, self).__init__()

            self.yang_name = "ciscoImageLicenseMgmtMIBObjects"
            self.yang_parent_name = "CISCO-IMAGE-LICENSE-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cilmeulaaccepted', YLeaf(YType.boolean, 'cilmEULAAccepted')),
            ])
            self.cilmeulaaccepted = None
            self._segment_path = lambda: "ciscoImageLicenseMgmtMIBObjects"
            self._absolute_path = lambda: "CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIMAGELICENSEMGMTMIB.Ciscoimagelicensemgmtmibobjects, ['cilmeulaaccepted'], name, value)


    class Cilmnotifcntl(Entity):
        """
        
        
        .. attribute:: cilmimagelevelchangednotif
        
        	Specify whether or not a notification should be generated on the detection of change in next boot image level.  If set to TRUE, cilmBootImageLevelChanged notification will be generated. It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the  notification to be delivered
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-IMAGE-LICENSE-MGMT-MIB'
        _revision = '2007-10-16'

        def __init__(self):
            super(CISCOIMAGELICENSEMGMTMIB.Cilmnotifcntl, self).__init__()

            self.yang_name = "cilmNotifCntl"
            self.yang_parent_name = "CISCO-IMAGE-LICENSE-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cilmimagelevelchangednotif', YLeaf(YType.boolean, 'cilmImageLevelChangedNotif')),
            ])
            self.cilmimagelevelchangednotif = None
            self._segment_path = lambda: "cilmNotifCntl"
            self._absolute_path = lambda: "CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIMAGELICENSEMGMTMIB.Cilmnotifcntl, ['cilmimagelevelchangednotif'], name, value)


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
        	**type**\: list of  		 :py:class:`Cilmbootimagelevelentry <ydk.models.cisco_ios_xe.CISCO_IMAGE_LICENSE_MGMT_MIB.CISCOIMAGELICENSEMGMTMIB.Cilmbootimageleveltable.Cilmbootimagelevelentry>`
        
        

        """

        _prefix = 'CISCO-IMAGE-LICENSE-MGMT-MIB'
        _revision = '2007-10-16'

        def __init__(self):
            super(CISCOIMAGELICENSEMGMTMIB.Cilmbootimageleveltable, self).__init__()

            self.yang_name = "cilmBootImageLevelTable"
            self.yang_parent_name = "CISCO-IMAGE-LICENSE-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cilmBootImageLevelEntry", ("cilmbootimagelevelentry", CISCOIMAGELICENSEMGMTMIB.Cilmbootimageleveltable.Cilmbootimagelevelentry))])
            self._leafs = OrderedDict()

            self.cilmbootimagelevelentry = YList(self)
            self._segment_path = lambda: "cilmBootImageLevelTable"
            self._absolute_path = lambda: "CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIMAGELICENSEMGMTMIB.Cilmbootimageleveltable, [], name, value)


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
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cilmmodulename  (key)
            
            	This object is used as one of the two indices in cilmBootImageLevelTable. This object indicates the module name of the software package. There can be multiple modules in an image performing specific functionality. For example, in a wireless image there can be two modules \- a base image module and a wireless module
            	**type**\: str
            
            .. attribute:: cilmcurrentimagelevel
            
            	This object indicates the current image level that the module is running
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cilmconfiguredbootimagelevel
            
            	This object indicates the configured image level of the module for the next boot.  Note\: The configured next boot image level may not  be the actual next boot image level. The actual next boot image level is denoted by cilmNextBootImageLevel which is determined based on the license availability
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cilmnextbootimagelevel
            
            	This object indicates the next boot image level. The next boot image level can be different from configured level. The next boot image level is determined based on the availability of required license
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cilmcurrentlicensestoreindex
            
            	This object indicates the license store index where the currently used license is stored. This object has the same value as clmgmtLicenseStoreIndex object and uniquely identifies an entry in clmgmtLicenseStoreInfoTable in CISCO\-LICENSE\-MGMT\-MIB.  Note\: The license store index can be '0' if no license is installed and device is running base image
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cilmcurrentlicenseindex
            
            	This object indicates the license index of the currently used license. This object has the same value as clmgmtLicenseIndex and uniquely identifies an entry in clmgmtLicenseInfoTable in CISCO\-LICENSE\-MGMT\-MIB.  Note\: The license index can be '0' if no license is installed and device is running base image
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cilmnextbootlicensestoreindex
            
            	This object indicates the license store index where the next boot license is stored. This object has the same value as clmgmtLicenseStoreIndex object and uniquely identifies an entry in clmgmtLicenseStoreInfoTable in CISCO\-LICENSE\-MGMT\-MIB.  Note\: The license store index can be '0' if no license is installed for the next boot
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cilmnextbootlicenseindex
            
            	This object indicates the license index of the next boot license. This object has the same value as clmgmtLicenseIndex and uniquely identifies an entry in clmgmtLicenseInfoTable in CISCO\-LICENSE\-MGMT\-MIB.  Note\: The license index can be '0' if no license is installed for the next boot
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IMAGE-LICENSE-MGMT-MIB'
            _revision = '2007-10-16'

            def __init__(self):
                super(CISCOIMAGELICENSEMGMTMIB.Cilmbootimageleveltable.Cilmbootimagelevelentry, self).__init__()

                self.yang_name = "cilmBootImageLevelEntry"
                self.yang_parent_name = "cilmBootImageLevelTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cilmmodulename']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cilmmodulename', YLeaf(YType.str, 'cilmModuleName')),
                    ('cilmcurrentimagelevel', YLeaf(YType.str, 'cilmCurrentImageLevel')),
                    ('cilmconfiguredbootimagelevel', YLeaf(YType.str, 'cilmConfiguredBootImageLevel')),
                    ('cilmnextbootimagelevel', YLeaf(YType.str, 'cilmNextBootImageLevel')),
                    ('cilmcurrentlicensestoreindex', YLeaf(YType.uint32, 'cilmCurrentLicenseStoreIndex')),
                    ('cilmcurrentlicenseindex', YLeaf(YType.uint32, 'cilmCurrentLicenseIndex')),
                    ('cilmnextbootlicensestoreindex', YLeaf(YType.uint32, 'cilmNextBootLicenseStoreIndex')),
                    ('cilmnextbootlicenseindex', YLeaf(YType.uint32, 'cilmNextBootLicenseIndex')),
                ])
                self.entphysicalindex = None
                self.cilmmodulename = None
                self.cilmcurrentimagelevel = None
                self.cilmconfiguredbootimagelevel = None
                self.cilmnextbootimagelevel = None
                self.cilmcurrentlicensestoreindex = None
                self.cilmcurrentlicenseindex = None
                self.cilmnextbootlicensestoreindex = None
                self.cilmnextbootlicenseindex = None
                self._segment_path = lambda: "cilmBootImageLevelEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cilmModuleName='" + str(self.cilmmodulename) + "']"
                self._absolute_path = lambda: "CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/cilmBootImageLevelTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIMAGELICENSEMGMTMIB.Cilmbootimageleveltable.Cilmbootimagelevelentry, ['entphysicalindex', 'cilmmodulename', 'cilmcurrentimagelevel', 'cilmconfiguredbootimagelevel', 'cilmnextbootimagelevel', 'cilmcurrentlicensestoreindex', 'cilmcurrentlicenseindex', 'cilmnextbootlicensestoreindex', 'cilmnextbootlicenseindex'], name, value)


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
        	**type**\: list of  		 :py:class:`Cilmimageleveltolicensemapentry <ydk.models.cisco_ios_xe.CISCO_IMAGE_LICENSE_MGMT_MIB.CISCOIMAGELICENSEMGMTMIB.Cilmimageleveltolicensemaptable.Cilmimageleveltolicensemapentry>`
        
        

        """

        _prefix = 'CISCO-IMAGE-LICENSE-MGMT-MIB'
        _revision = '2007-10-16'

        def __init__(self):
            super(CISCOIMAGELICENSEMGMTMIB.Cilmimageleveltolicensemaptable, self).__init__()

            self.yang_name = "cilmImageLevelToLicenseMapTable"
            self.yang_parent_name = "CISCO-IMAGE-LICENSE-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cilmImageLevelToLicenseMapEntry", ("cilmimageleveltolicensemapentry", CISCOIMAGELICENSEMGMTMIB.Cilmimageleveltolicensemaptable.Cilmimageleveltolicensemapentry))])
            self._leafs = OrderedDict()

            self.cilmimageleveltolicensemapentry = YList(self)
            self._segment_path = lambda: "cilmImageLevelToLicenseMapTable"
            self._absolute_path = lambda: "CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIMAGELICENSEMGMTMIB.Cilmimageleveltolicensemaptable, [], name, value)


        class Cilmimageleveltolicensemapentry(Entity):
            """
            An entry in the table containing the following
            information.
            \- The image levels at the which the modules can be run.
            \- The license required to the run a module at a
            particular image level.
            \- The priority of the license.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cilmmodulename  (key)
            
            	
            	**type**\: str
            
            	**refers to**\:  :py:class:`cilmmodulename <ydk.models.cisco_ios_xe.CISCO_IMAGE_LICENSE_MGMT_MIB.CISCOIMAGELICENSEMGMTMIB.Cilmbootimageleveltable.Cilmbootimagelevelentry>`
            
            .. attribute:: cilmimagelicensemapindex  (key)
            
            	This is a running index used to identify an entry of this table
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cilmimagelicenseimagelevel
            
            	This object indicates the image level at which a module can be run. A module can be run at different image levels. An entry will be created in this table for every module and image level combination
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cilmimagelicensename
            
            	This object indicates the list of licenses needed to be installed for the module to run at the image level mentioned by cilmImageLicenseImageLevel object of this entry
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cilmimagelicensepriority
            
            	This object indicates the priority of the image level mentioned by cilmImageLicenseImageLevel object of this entry. The image level with the highest priority license will be considered as the default level in the absense of next boot image level configuration. For example if there are three licenses l1, l2 and l3 in the ascending order of priority, then by default l1 will be the level at which the module will be running. If the next boot level is configured then the configuration will override the priority. The highest priority license supports a feature set which is a super set of all other licenses
            	**type**\: int
            
            	**range:** 1..255
            
            

            """

            _prefix = 'CISCO-IMAGE-LICENSE-MGMT-MIB'
            _revision = '2007-10-16'

            def __init__(self):
                super(CISCOIMAGELICENSEMGMTMIB.Cilmimageleveltolicensemaptable.Cilmimageleveltolicensemapentry, self).__init__()

                self.yang_name = "cilmImageLevelToLicenseMapEntry"
                self.yang_parent_name = "cilmImageLevelToLicenseMapTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cilmmodulename','cilmimagelicensemapindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cilmmodulename', YLeaf(YType.str, 'cilmModuleName')),
                    ('cilmimagelicensemapindex', YLeaf(YType.uint32, 'cilmImageLicenseMapIndex')),
                    ('cilmimagelicenseimagelevel', YLeaf(YType.str, 'cilmImageLicenseImageLevel')),
                    ('cilmimagelicensename', YLeaf(YType.str, 'cilmImageLicenseName')),
                    ('cilmimagelicensepriority', YLeaf(YType.uint32, 'cilmImageLicensePriority')),
                ])
                self.entphysicalindex = None
                self.cilmmodulename = None
                self.cilmimagelicensemapindex = None
                self.cilmimagelicenseimagelevel = None
                self.cilmimagelicensename = None
                self.cilmimagelicensepriority = None
                self._segment_path = lambda: "cilmImageLevelToLicenseMapEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cilmModuleName='" + str(self.cilmmodulename) + "']" + "[cilmImageLicenseMapIndex='" + str(self.cilmimagelicensemapindex) + "']"
                self._absolute_path = lambda: "CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/cilmImageLevelToLicenseMapTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIMAGELICENSEMGMTMIB.Cilmimageleveltolicensemaptable.Cilmimageleveltolicensemapentry, ['entphysicalindex', 'cilmmodulename', 'cilmimagelicensemapindex', 'cilmimagelicenseimagelevel', 'cilmimagelicensename', 'cilmimagelicensepriority'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOIMAGELICENSEMGMTMIB()
        return self._top_entity

