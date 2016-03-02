


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOIMAGELICENSEMGMTMIB.CilmBootImageLevelTable.CilmBootImageLevelEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIMAGELICENSEMGMTMIB.CilmBootImageLevelTable.CilmBootImageLevelEntry',
            False, 
            [
            _MetaInfoClassMember('cilmModuleName', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                This object is used as one of the two indices in
                cilmBootImageLevelTable. This object indicates the module
                name of the software package. There can be multiple
                modules in an image performing specific functionality.
                For example, in a wireless image there can be two modules
                - a base image module and a wireless module.
                ''',
                'cilmmodulename',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', True),
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', True),
            _MetaInfoClassMember('cilmConfiguredBootImageLevel', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the configured image level
                of the module for the next boot.
                
                Note: The configured next boot image level may not 
                be the actual next boot image level. The actual next
                boot image level is denoted by cilmNextBootImageLevel
                which is determined based on the license availability.
                ''',
                'cilmconfiguredbootimagelevel',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('cilmCurrentImageLevel', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the current image level that
                the module is running.
                ''',
                'cilmcurrentimagelevel',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('cilmCurrentLicenseIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the license index of the currently used
                license. This object has the same value as clmgmtLicenseIndex and
                uniquely identifies an entry in clmgmtLicenseInfoTable in
                CISCO-LICENSE-MGMT-MIB.
                
                Note: The license index can be '0' if no license is
                installed and device is running base image.
                ''',
                'cilmcurrentlicenseindex',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('cilmCurrentLicenseStoreIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the license store index where the
                currently used license is stored. This object has the same
                value as clmgmtLicenseStoreIndex object and uniquely
                identifies an entry in clmgmtLicenseStoreInfoTable in
                CISCO-LICENSE-MGMT-MIB.
                
                Note: The license store index can be '0' if no license is
                installed and device is running base image.
                ''',
                'cilmcurrentlicensestoreindex',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('cilmNextBootImageLevel', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the next boot image level. The
                next boot image level can be different from configured
                level. The next boot image level is determined based
                on the availability of required license.
                ''',
                'cilmnextbootimagelevel',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('cilmNextBootLicenseIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the license index of the next boot
                license. This object has the same value as clmgmtLicenseIndex
                and uniquely identifies an entry in clmgmtLicenseInfoTable in
                CISCO-LICENSE-MGMT-MIB.
                
                Note: The license index can be '0' if no license is
                installed for the next boot.
                ''',
                'cilmnextbootlicenseindex',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('cilmNextBootLicenseStoreIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the license store index where the
                next boot license is stored. This object has the same
                value as clmgmtLicenseStoreIndex object and uniquely
                identifies an entry in clmgmtLicenseStoreInfoTable in
                CISCO-LICENSE-MGMT-MIB.
                
                Note: The license store index can be '0' if no license is
                installed for the next boot.
                ''',
                'cilmnextbootlicensestoreindex',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-IMAGE-LICENSE-MGMT-MIB',
            'cilmBootImageLevelEntry',
            _yang_ns._namespaces['CISCO-IMAGE-LICENSE-MGMT-MIB'],
        'ydk.models.image.CISCO_IMAGE_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOIMAGELICENSEMGMTMIB.CilmBootImageLevelTable' : {
        'meta_info' : _MetaInfoClass('CISCOIMAGELICENSEMGMTMIB.CilmBootImageLevelTable',
            False, 
            [
            _MetaInfoClassMember('cilmBootImageLevelEntry', REFERENCE_LIST, 'CilmBootImageLevelEntry' , 'ydk.models.image.CISCO_IMAGE_LICENSE_MGMT_MIB', 'CISCOIMAGELICENSEMGMTMIB.CilmBootImageLevelTable.CilmBootImageLevelEntry', 
                [], [], 
                '''                An entry in the table for each module containing the
                list of objects that define the configuration of next
                boot level. The following information is specified by
                the objects present in the table.
                
                - Current image level.
                - Configured image level for the next boot.
                - Actual image level for the next boot.
                - License store index for the current license.
                - License index of the current license.
                - License store index for the next boot license.
                - License index of the next boot license.
                ''',
                'cilmbootimagelevelentry',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-IMAGE-LICENSE-MGMT-MIB',
            'cilmBootImageLevelTable',
            _yang_ns._namespaces['CISCO-IMAGE-LICENSE-MGMT-MIB'],
        'ydk.models.image.CISCO_IMAGE_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOIMAGELICENSEMGMTMIB.CilmImageLevelToLicenseMapTable.CilmImageLevelToLicenseMapEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIMAGELICENSEMGMTMIB.CilmImageLevelToLicenseMapTable.CilmImageLevelToLicenseMapEntry',
            False, 
            [
            _MetaInfoClassMember('cilmImageLicenseMapIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This is a running index used to identify an entry
                of this table.
                ''',
                'cilmimagelicensemapindex',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', True),
            _MetaInfoClassMember('cilmModuleName', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                ''',
                'cilmmodulename',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', True),
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', True),
            _MetaInfoClassMember('cilmImageLicenseImageLevel', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the image level at which
                a module can be run. A module can be run at
                different image levels. An entry will be created
                in this table for every module and image level
                combination.
                ''',
                'cilmimagelicenseimagelevel',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('cilmImageLicenseName', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the list of licenses needed to
                be installed for the module to run at the image level
                mentioned by cilmImageLicenseImageLevel object of this
                entry.
                ''',
                'cilmimagelicensename',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('cilmImageLicensePriority', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                This object indicates the priority of the image level
                mentioned by cilmImageLicenseImageLevel object of this
                entry. The image level with the highest priority license
                will be considered as the default level in the absense of
                next boot image level configuration. For example if there
                are three licenses l1, l2 and l3 in the ascending order of
                priority, then by default l1 will be the level at which the
                module will be running. If the next boot level is configured
                then the configuration will override the priority. The highest
                priority license supports a feature set which is a super set of
                all other licenses.
                ''',
                'cilmimagelicensepriority',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-IMAGE-LICENSE-MGMT-MIB',
            'cilmImageLevelToLicenseMapEntry',
            _yang_ns._namespaces['CISCO-IMAGE-LICENSE-MGMT-MIB'],
        'ydk.models.image.CISCO_IMAGE_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOIMAGELICENSEMGMTMIB.CilmImageLevelToLicenseMapTable' : {
        'meta_info' : _MetaInfoClass('CISCOIMAGELICENSEMGMTMIB.CilmImageLevelToLicenseMapTable',
            False, 
            [
            _MetaInfoClassMember('cilmImageLevelToLicenseMapEntry', REFERENCE_LIST, 'CilmImageLevelToLicenseMapEntry' , 'ydk.models.image.CISCO_IMAGE_LICENSE_MGMT_MIB', 'CISCOIMAGELICENSEMGMTMIB.CilmImageLevelToLicenseMapTable.CilmImageLevelToLicenseMapEntry', 
                [], [], 
                '''                An entry in the table containing the following
                information.
                - The image levels at the which the modules can be run.
                - The license required to the run a module at a
                particular image level.
                - The priority of the license.
                ''',
                'cilmimageleveltolicensemapentry',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-IMAGE-LICENSE-MGMT-MIB',
            'cilmImageLevelToLicenseMapTable',
            _yang_ns._namespaces['CISCO-IMAGE-LICENSE-MGMT-MIB'],
        'ydk.models.image.CISCO_IMAGE_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOIMAGELICENSEMGMTMIB.CilmNotifCntl' : {
        'meta_info' : _MetaInfoClass('CISCOIMAGELICENSEMGMTMIB.CilmNotifCntl',
            False, 
            [
            _MetaInfoClassMember('cilmImageLevelChangedNotif', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify whether or not a notification should be
                generated on the detection of change in next boot
                image level.
                
                If set to TRUE, cilmBootImageLevelChanged notification
                will be generated. It is the responsibility of the
                management entity to ensure that the SNMP administrative
                model is configured in such a way as to allow the 
                notification to be delivered.
                ''',
                'cilmimagelevelchangednotif',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-IMAGE-LICENSE-MGMT-MIB',
            'cilmNotifCntl',
            _yang_ns._namespaces['CISCO-IMAGE-LICENSE-MGMT-MIB'],
        'ydk.models.image.CISCO_IMAGE_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOIMAGELICENSEMGMTMIB.CiscoImageLicenseMgmtMIBObjects' : {
        'meta_info' : _MetaInfoClass('CISCOIMAGELICENSEMGMTMIB.CiscoImageLicenseMgmtMIBObjects',
            False, 
            [
            _MetaInfoClassMember('cilmEULAAccepted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object when set to TRUE means that the user has
                accepted the END USER LICENSE AGREEMENT. This object
                has to be set to TRUE by the user before using the
                objects in the cilmBootImageLevelTable to configure
                the license.
                ''',
                'cilmeulaaccepted',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-IMAGE-LICENSE-MGMT-MIB',
            'ciscoImageLicenseMgmtMIBObjects',
            _yang_ns._namespaces['CISCO-IMAGE-LICENSE-MGMT-MIB'],
        'ydk.models.image.CISCO_IMAGE_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOIMAGELICENSEMGMTMIB' : {
        'meta_info' : _MetaInfoClass('CISCOIMAGELICENSEMGMTMIB',
            False, 
            [
            _MetaInfoClassMember('cilmBootImageLevelTable', REFERENCE_CLASS, 'CilmBootImageLevelTable' , 'ydk.models.image.CISCO_IMAGE_LICENSE_MGMT_MIB', 'CISCOIMAGELICENSEMGMTMIB.CilmBootImageLevelTable', 
                [], [], 
                '''                A table that contains the configuration information of
                current and next boot image level. This table contains
                entries for each software module running in an image 
                loaded in the device. The software module is identified by
                cilmModuleName and the device is identified by 
                entPhysicalIndex.
                ''',
                'cilmbootimageleveltable',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('cilmImageLevelToLicenseMapTable', REFERENCE_CLASS, 'CilmImageLevelToLicenseMapTable' , 'ydk.models.image.CISCO_IMAGE_LICENSE_MGMT_MIB', 'CISCOIMAGELICENSEMGMTMIB.CilmImageLevelToLicenseMapTable', 
                [], [], 
                '''                This table contains the mapping between different
                image levels of each modules in the image and the
                license required to run the modules at a particular
                image level. This table can be used to identify the
                different image levels and the appropriate licenses 
                required for each.
                ''',
                'cilmimageleveltolicensemaptable',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('cilmNotifCntl', REFERENCE_CLASS, 'CilmNotifCntl' , 'ydk.models.image.CISCO_IMAGE_LICENSE_MGMT_MIB', 'CISCOIMAGELICENSEMGMTMIB.CilmNotifCntl', 
                [], [], 
                '''                ''',
                'cilmnotifcntl',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('ciscoImageLicenseMgmtMIBObjects', REFERENCE_CLASS, 'CiscoImageLicenseMgmtMIBObjects' , 'ydk.models.image.CISCO_IMAGE_LICENSE_MGMT_MIB', 'CISCOIMAGELICENSEMGMTMIB.CiscoImageLicenseMgmtMIBObjects', 
                [], [], 
                '''                ''',
                'ciscoimagelicensemgmtmibobjects',
                'CISCO-IMAGE-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-IMAGE-LICENSE-MGMT-MIB',
            'CISCO-IMAGE-LICENSE-MGMT-MIB',
            _yang_ns._namespaces['CISCO-IMAGE-LICENSE-MGMT-MIB'],
        'ydk.models.image.CISCO_IMAGE_LICENSE_MGMT_MIB'
        ),
    },
}
_meta_table['CISCOIMAGELICENSEMGMTMIB.CilmBootImageLevelTable.CilmBootImageLevelEntry']['meta_info'].parent =_meta_table['CISCOIMAGELICENSEMGMTMIB.CilmBootImageLevelTable']['meta_info']
_meta_table['CISCOIMAGELICENSEMGMTMIB.CilmImageLevelToLicenseMapTable.CilmImageLevelToLicenseMapEntry']['meta_info'].parent =_meta_table['CISCOIMAGELICENSEMGMTMIB.CilmImageLevelToLicenseMapTable']['meta_info']
_meta_table['CISCOIMAGELICENSEMGMTMIB.CilmBootImageLevelTable']['meta_info'].parent =_meta_table['CISCOIMAGELICENSEMGMTMIB']['meta_info']
_meta_table['CISCOIMAGELICENSEMGMTMIB.CilmImageLevelToLicenseMapTable']['meta_info'].parent =_meta_table['CISCOIMAGELICENSEMGMTMIB']['meta_info']
_meta_table['CISCOIMAGELICENSEMGMTMIB.CilmNotifCntl']['meta_info'].parent =_meta_table['CISCOIMAGELICENSEMGMTMIB']['meta_info']
_meta_table['CISCOIMAGELICENSEMGMTMIB.CiscoImageLicenseMgmtMIBObjects']['meta_info'].parent =_meta_table['CISCOIMAGELICENSEMGMTMIB']['meta_info']
