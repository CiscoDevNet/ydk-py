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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoImageLicenseMgmtMib(object):
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
        self.cilmbootimageleveltable = CiscoImageLicenseMgmtMib.Cilmbootimageleveltable()
        self.cilmbootimageleveltable.parent = self
        self.cilmimageleveltolicensemaptable = CiscoImageLicenseMgmtMib.Cilmimageleveltolicensemaptable()
        self.cilmimageleveltolicensemaptable.parent = self
        self.cilmnotifcntl = CiscoImageLicenseMgmtMib.Cilmnotifcntl()
        self.cilmnotifcntl.parent = self
        self.ciscoimagelicensemgmtmibobjects = CiscoImageLicenseMgmtMib.Ciscoimagelicensemgmtmibobjects()
        self.ciscoimagelicensemgmtmibobjects.parent = self


    class Ciscoimagelicensemgmtmibobjects(object):
        """
        
        
        .. attribute:: cilmeulaaccepted
        
        	This object when set to TRUE means that the user has accepted the END USER LICENSE AGREEMENT. This object has to be set to TRUE by the user before using the objects in the cilmBootImageLevelTable to configure the license
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-IMAGE-LICENSE-MGMT-MIB'
        _revision = '2007-10-16'

        def __init__(self):
            self.parent = None
            self.cilmeulaaccepted = None

        @property
        def _common_path(self):

            return '/CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/CISCO-IMAGE-LICENSE-MGMT-MIB:ciscoImageLicenseMgmtMIBObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cilmeulaaccepted is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IMAGE_LICENSE_MGMT_MIB as meta
            return meta._meta_table['CiscoImageLicenseMgmtMib.Ciscoimagelicensemgmtmibobjects']['meta_info']


    class Cilmnotifcntl(object):
        """
        
        
        .. attribute:: cilmimagelevelchangednotif
        
        	Specify whether or not a notification should be generated on the detection of change in next boot image level.  If set to TRUE, cilmBootImageLevelChanged notification will be generated. It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the  notification to be delivered
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-IMAGE-LICENSE-MGMT-MIB'
        _revision = '2007-10-16'

        def __init__(self):
            self.parent = None
            self.cilmimagelevelchangednotif = None

        @property
        def _common_path(self):

            return '/CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/CISCO-IMAGE-LICENSE-MGMT-MIB:cilmNotifCntl'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cilmimagelevelchangednotif is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IMAGE_LICENSE_MGMT_MIB as meta
            return meta._meta_table['CiscoImageLicenseMgmtMib.Cilmnotifcntl']['meta_info']


    class Cilmbootimageleveltable(object):
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
            self.parent = None
            self.cilmbootimagelevelentry = YList()
            self.cilmbootimagelevelentry.parent = self
            self.cilmbootimagelevelentry.name = 'cilmbootimagelevelentry'


        class Cilmbootimagelevelentry(object):
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
                self.parent = None
                self.entphysicalindex = None
                self.cilmmodulename = None
                self.cilmconfiguredbootimagelevel = None
                self.cilmcurrentimagelevel = None
                self.cilmcurrentlicenseindex = None
                self.cilmcurrentlicensestoreindex = None
                self.cilmnextbootimagelevel = None
                self.cilmnextbootlicenseindex = None
                self.cilmnextbootlicensestoreindex = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')
                if self.cilmmodulename is None:
                    raise YPYModelError('Key property cilmmodulename is None')

                return '/CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/CISCO-IMAGE-LICENSE-MGMT-MIB:cilmBootImageLevelTable/CISCO-IMAGE-LICENSE-MGMT-MIB:cilmBootImageLevelEntry[CISCO-IMAGE-LICENSE-MGMT-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + '][CISCO-IMAGE-LICENSE-MGMT-MIB:cilmModuleName = ' + str(self.cilmmodulename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cilmmodulename is not None:
                    return True

                if self.cilmconfiguredbootimagelevel is not None:
                    return True

                if self.cilmcurrentimagelevel is not None:
                    return True

                if self.cilmcurrentlicenseindex is not None:
                    return True

                if self.cilmcurrentlicensestoreindex is not None:
                    return True

                if self.cilmnextbootimagelevel is not None:
                    return True

                if self.cilmnextbootlicenseindex is not None:
                    return True

                if self.cilmnextbootlicensestoreindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IMAGE_LICENSE_MGMT_MIB as meta
                return meta._meta_table['CiscoImageLicenseMgmtMib.Cilmbootimageleveltable.Cilmbootimagelevelentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/CISCO-IMAGE-LICENSE-MGMT-MIB:cilmBootImageLevelTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cilmbootimagelevelentry is not None:
                for child_ref in self.cilmbootimagelevelentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IMAGE_LICENSE_MGMT_MIB as meta
            return meta._meta_table['CiscoImageLicenseMgmtMib.Cilmbootimageleveltable']['meta_info']


    class Cilmimageleveltolicensemaptable(object):
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
            self.parent = None
            self.cilmimageleveltolicensemapentry = YList()
            self.cilmimageleveltolicensemapentry.parent = self
            self.cilmimageleveltolicensemapentry.name = 'cilmimageleveltolicensemapentry'


        class Cilmimageleveltolicensemapentry(object):
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
                self.parent = None
                self.entphysicalindex = None
                self.cilmmodulename = None
                self.cilmimagelicensemapindex = None
                self.cilmimagelicenseimagelevel = None
                self.cilmimagelicensename = None
                self.cilmimagelicensepriority = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')
                if self.cilmmodulename is None:
                    raise YPYModelError('Key property cilmmodulename is None')
                if self.cilmimagelicensemapindex is None:
                    raise YPYModelError('Key property cilmimagelicensemapindex is None')

                return '/CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/CISCO-IMAGE-LICENSE-MGMT-MIB:cilmImageLevelToLicenseMapTable/CISCO-IMAGE-LICENSE-MGMT-MIB:cilmImageLevelToLicenseMapEntry[CISCO-IMAGE-LICENSE-MGMT-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + '][CISCO-IMAGE-LICENSE-MGMT-MIB:cilmModuleName = ' + str(self.cilmmodulename) + '][CISCO-IMAGE-LICENSE-MGMT-MIB:cilmImageLicenseMapIndex = ' + str(self.cilmimagelicensemapindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cilmmodulename is not None:
                    return True

                if self.cilmimagelicensemapindex is not None:
                    return True

                if self.cilmimagelicenseimagelevel is not None:
                    return True

                if self.cilmimagelicensename is not None:
                    return True

                if self.cilmimagelicensepriority is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IMAGE_LICENSE_MGMT_MIB as meta
                return meta._meta_table['CiscoImageLicenseMgmtMib.Cilmimageleveltolicensemaptable.Cilmimageleveltolicensemapentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB/CISCO-IMAGE-LICENSE-MGMT-MIB:cilmImageLevelToLicenseMapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cilmimageleveltolicensemapentry is not None:
                for child_ref in self.cilmimageleveltolicensemapentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IMAGE_LICENSE_MGMT_MIB as meta
            return meta._meta_table['CiscoImageLicenseMgmtMib.Cilmimageleveltolicensemaptable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IMAGE-LICENSE-MGMT-MIB:CISCO-IMAGE-LICENSE-MGMT-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cilmbootimageleveltable is not None and self.cilmbootimageleveltable._has_data():
            return True

        if self.cilmimageleveltolicensemaptable is not None and self.cilmimageleveltolicensemaptable._has_data():
            return True

        if self.cilmnotifcntl is not None and self.cilmnotifcntl._has_data():
            return True

        if self.ciscoimagelicensemgmtmibobjects is not None and self.ciscoimagelicensemgmtmibobjects._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IMAGE_LICENSE_MGMT_MIB as meta
        return meta._meta_table['CiscoImageLicenseMgmtMib']['meta_info']


