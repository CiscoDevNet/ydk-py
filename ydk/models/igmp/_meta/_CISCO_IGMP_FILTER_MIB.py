


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOIGMPFILTERMIB.CIgmpFilterEditor.CIgmpFilterApplyStatus_Enum' : _MetaInfoEnum('CIgmpFilterApplyStatus_Enum', 'ydk.models.igmp.CISCO_IGMP_FILTER_MIB',
        {
            'someOtherError':'SOMEOTHERERROR',
            'succeeded':'SUCCEEDED',
            'inconsistentEdit':'INCONSISTENTEDIT',
            'entryPresentError':'ENTRYPRESENTERROR',
            'entryNotPresentError':'ENTRYNOTPRESENTERROR',
        }, 'CISCO-IGMP-FILTER-MIB', _yang_ns._namespaces['CISCO-IGMP-FILTER-MIB']),
    'CISCOIGMPFILTERMIB.CIgmpFilterEditor.CIgmpFilterEditOperation_Enum' : _MetaInfoEnum('CIgmpFilterEditOperation_Enum', 'ydk.models.igmp.CISCO_IGMP_FILTER_MIB',
        {
            'none':'NONE',
            'add':'ADD',
            'delete':'DELETE',
            'modify':'MODIFY',
        }, 'CISCO-IGMP-FILTER-MIB', _yang_ns._namespaces['CISCO-IGMP-FILTER-MIB']),
    'CISCOIGMPFILTERMIB.CIgmpFilterEditor.CIgmpFilterEditProfileAction_Enum' : _MetaInfoEnum('CIgmpFilterEditProfileAction_Enum', 'ydk.models.igmp.CISCO_IGMP_FILTER_MIB',
        {
            'permit':'PERMIT',
            'deny':'DENY',
        }, 'CISCO-IGMP-FILTER-MIB', _yang_ns._namespaces['CISCO-IGMP-FILTER-MIB']),
    'CISCOIGMPFILTERMIB.CIgmpFilterEditor' : {
        'meta_info' : _MetaInfoClass('CISCOIGMPFILTERMIB.CIgmpFilterEditor',
            False, 
            [
            _MetaInfoClassMember('cIgmpFilterApplyStatus', REFERENCE_ENUM_CLASS, 'CIgmpFilterApplyStatus_Enum' , 'ydk.models.igmp.CISCO_IGMP_FILTER_MIB', 'CISCOIGMPFILTERMIB.CIgmpFilterEditor.CIgmpFilterApplyStatus_Enum', 
                [], [], 
                '''                The current status of an 'add', 'delete' or 'modify'
                operation. If no apply is currently active, the status 
                represented is that of the most recently completed 'add', 
                'delete' or 'modify' operation.
                
                The value of this objects indicates succeeded(2) state 
                initially when no 'add', 'delete', 'modify' operation
                has been carried out.
                
                The possible values are:
                   someOtherError - the 'add', 'delete' or 'modify' failed 
                   due to undefined error(s) in apply operation.
                   (e.g., insufficient memory). 
                
                   succeeded - the 'add', 'delete' or 'modify' operation
                   was successful. (This value is also used when no
                   apply has been invoked since the last time the local 
                   system restarted.)
                
                   inconsistentEdit - the 'add', 'delete' or 'modify' failed
                   due to inconsistency of the data.
                
                   entryPresentError - the 'add' operation failed  as the 
                   corresponding entry already exists in cIgmpFilterTable.
                
                   entryNotPresentError - the 'modify' operation failed 
                   as no corresponding entry exists in cIgmpFilterTable.
                ''',
                'cigmpfilterapplystatus',
                'CISCO-IGMP-FILTER-MIB', False),
            _MetaInfoClassMember('cIgmpFilterEditEndAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Buffer object to edit corresponding object
                cIgmpFilterEndAddress in cIgmpFilterTable 
                to establish end address of filtering 
                range for a profile.
                ''',
                'cigmpfiltereditendaddress',
                'CISCO-IGMP-FILTER-MIB', False),
            _MetaInfoClassMember('cIgmpFilterEditEndAddressType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                Buffer object to edit corresponding object
                cIgmpFilterEndAddressType in cIgmpFilterTable.
                
                This object describes the type of Internet     
                address used to determine the start address 
                of IP multicast group for a profile.
                ''',
                'cigmpfiltereditendaddresstype',
                'CISCO-IGMP-FILTER-MIB', False),
            _MetaInfoClassMember('cIgmpFilterEditOperation', REFERENCE_ENUM_CLASS, 'CIgmpFilterEditOperation_Enum' , 'ydk.models.igmp.CISCO_IGMP_FILTER_MIB', 'CISCOIGMPFILTERMIB.CIgmpFilterEditor.CIgmpFilterEditOperation_Enum', 
                [], [], 
                '''                The function of this object is to allow user to
                apply the changes in cIgmpFilterEditor objects to 
                cIgmpFilterTable. 
                
                This object always has the value 'none' when read.
                When written each value causes the appropriate action:
                
                'add' - tries to insert the information contained 
                in cIgmpFilterEditor objects into  cIgmpFilterTable.
                If the entry already exists in the table the 'add' 
                fails.        
                
                'delete' - tries to delete corresponding entry from
                cIgmpFilterTable. If a user completely deletes a profile
                that has corresponding entries in the
                cIgmpFilterInterfaceTable, then all the interfaces mapped
                to corresponding profile will be cleared and set to zero.
                
                'modify' - Mode of operation used to edit an entry in
                 cIgmpFilterTable. If the corresponding entry does not 
                 exist, modify operation fails. This mode allows user to
                 extend/truncate a contiguous filtered range, type of
                 Internet addressing and filtering action for a profile. 
                
                'none' - no operation is performed.
                ''',
                'cigmpfiltereditoperation',
                'CISCO-IGMP-FILTER-MIB', False),
            _MetaInfoClassMember('cIgmpFilterEditProfileAction', REFERENCE_ENUM_CLASS, 'CIgmpFilterEditProfileAction_Enum' , 'ydk.models.igmp.CISCO_IGMP_FILTER_MIB', 'CISCOIGMPFILTERMIB.CIgmpFilterEditor.CIgmpFilterEditProfileAction_Enum', 
                [], [], 
                '''                Buffer object to edit corresponding object in
                cIgmpFilterTable to determine filtering action
                of each profile.
                ''',
                'cigmpfiltereditprofileaction',
                'CISCO-IGMP-FILTER-MIB', False),
            _MetaInfoClassMember('cIgmpFilterEditProfileIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Buffer object to edit corresponding object
                cIgmpFilterProfileIndex in cIgmpFilterTable.
                
                Maximum value this object can be set to is 
                determined by cIgmpFilterMaxProfiles object.
                ''',
                'cigmpfiltereditprofileindex',
                'CISCO-IGMP-FILTER-MIB', False),
            _MetaInfoClassMember('cIgmpFilterEditSpinLock', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                This object is used to facilitate modification of
                IGMP Filter Editor Group in the CISCO-IGMP-FILTER-MIB 
                module by multiple managers.  In particular, it is 
                useful when modifying the value of the cIgmpFilterEditor 
                object. 
                
                The procedure for modifying the cIgmpFilterEditor 
                object is as follows: 
                
                    1.  Retrieve the value of cIgmpFilterEditSpinLock and 
                        of object within cIgmpFilterEditor group. 
                
                    2.  Generate new values for 'writeable' objects
                        in the cIgmpFilterEditor group except for 
                        cIgmpFilterEditSpinLock object.
                
                    3.  Set the value of cIgmpFilterEditSpinLock to the 
                        retrieved value, and the value of objects in 
                        cIgmpFilterEditor to the new value. If the set
                        fails for the cIgmpFilterEditSpinLock object,
                        go back to step 1. 
                
                The cIgmpFilterApplyStatus and cIgmpFilterEditSpinLock 
                should be read together by NMS to make sure that the 
                result is associated with its configuration request.
                
                To add/delete or modify a profile ( through cIgmpFilterEditor
                objects ) following procedure may be followed as an example.:
                
                    1.  GET(cIgmpFilterEditSpinLock.0) and save in sValue.
                    2.  SET(cIgmpFilterEditSpinLock.0 = sValue,
                            cIgmpFilterEditProfileIndex.0 = validProfileNumber,
                            cIgmpFilterEditStartAddress.0 = validStartAddress,
                            cIgmpFilterEditEndAddress.0 = validEndAddress,
                            cIgmpFilterEditOperation.0 =  validOperation)
                    3.  If the SET in step 2 is not successful go back
                        to step 1.
                    4.  If the SET in step 2 is successful, user should 
                        GET(cIgmpFilterEditSpinLock.0) and 
                        GET(cIgmpFilterApplyStatus.0) simultaneously.
                
                    5.  The cIgmpFilterApplyStatus.0 reflects the outcome of
                        step 2 only if
                        cIgmpFilterEditSpinLock.0 = sValue + 1 or
                        cIgmpFilterEditSpinLock.0 = 0 if sValue reaches
                        value at which cIgmpFilterEditSpinLock wraps 
                        around.
                ''',
                'cigmpfiltereditspinlock',
                'CISCO-IGMP-FILTER-MIB', False),
            _MetaInfoClassMember('cIgmpFilterEditStartAddress', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Buffer object to edit corresponding object
                cIgmpFilterStartAddress in cIgmpFilterTable
                  to establish start address of filtering
                range for a profile.
                ''',
                'cigmpfiltereditstartaddress',
                'CISCO-IGMP-FILTER-MIB', False),
            _MetaInfoClassMember('cIgmpFilterEditStartAddressType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                Buffer object to edit corresponding object
                cIgmpFilterStartAddressType in cIgmpFilterTable.
                
                This object describes the type of Internet  
                address used to determine the start address 
                of IP multicast group for a profile.
                ''',
                'cigmpfiltereditstartaddresstype',
                'CISCO-IGMP-FILTER-MIB', False),
            ],
            'CISCO-IGMP-FILTER-MIB',
            'cIgmpFilterEditor',
            _yang_ns._namespaces['CISCO-IGMP-FILTER-MIB'],
        'ydk.models.igmp.CISCO_IGMP_FILTER_MIB'
        ),
    },
    'CISCOIGMPFILTERMIB.CIgmpFilterGeneral' : {
        'meta_info' : _MetaInfoClass('CISCOIGMPFILTERMIB.CIgmpFilterGeneral',
            False, 
            [
            _MetaInfoClassMember('cIgmpFilterEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object controls whether the IGMP filtering
                is enabled on the device. A false(2) value will 
                prevent the IGMP filtering action on the device.
                ''',
                'cigmpfilterenable',
                'CISCO-IGMP-FILTER-MIB', False),
            _MetaInfoClassMember('cIgmpFilterMaxProfiles', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the maximum number of profiles supported by
                this device.  A value of zero indicates no limitation on
                the number of profiles.
                ''',
                'cigmpfiltermaxprofiles',
                'CISCO-IGMP-FILTER-MIB', False),
            ],
            'CISCO-IGMP-FILTER-MIB',
            'cIgmpFilterGeneral',
            _yang_ns._namespaces['CISCO-IGMP-FILTER-MIB'],
        'ydk.models.igmp.CISCO_IGMP_FILTER_MIB'
        ),
    },
    'CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable.CIgmpFilterInterfaceEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable.CIgmpFilterInterfaceEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-IGMP-FILTER-MIB', True),
            _MetaInfoClassMember('cIgmpFilterInterfaceProfileIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Specifies which IGMP filter profile applies to this
                interface. If the value of this MIB object matches the 
                value of cIgmpFilterProfileIndex in cIgmpFilterTable, 
                the corresponding profile configuration will apply to
                this interface. 
                
                Agent returns inconsistentValue if this profile 
                does not exist in cIgmpFilterTable. 
                A value of zero indicates no profile is associated
                with corresponding interface.
                
                The filtering action on each interface is also
                defined by the associated profile.
                ''',
                'cigmpfilterinterfaceprofileindex',
                'CISCO-IGMP-FILTER-MIB', False),
            ],
            'CISCO-IGMP-FILTER-MIB',
            'cIgmpFilterInterfaceEntry',
            _yang_ns._namespaces['CISCO-IGMP-FILTER-MIB'],
        'ydk.models.igmp.CISCO_IGMP_FILTER_MIB'
        ),
    },
    'CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable' : {
        'meta_info' : _MetaInfoClass('CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable',
            False, 
            [
            _MetaInfoClassMember('cIgmpFilterInterfaceEntry', REFERENCE_LIST, 'CIgmpFilterInterfaceEntry' , 'ydk.models.igmp.CISCO_IGMP_FILTER_MIB', 'CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable.CIgmpFilterInterfaceEntry', 
                [], [], 
                '''                Each entry contains the configuration for associating
                the IGMP filter profile index with the interface.
                
                An entry is created for each of the IGMP filter capable 
                interface on the system.
                
                The entry is removed on removal of corresponding 
                interface from system.
                ''',
                'cigmpfilterinterfaceentry',
                'CISCO-IGMP-FILTER-MIB', False),
            ],
            'CISCO-IGMP-FILTER-MIB',
            'cIgmpFilterInterfaceTable',
            _yang_ns._namespaces['CISCO-IGMP-FILTER-MIB'],
        'ydk.models.igmp.CISCO_IGMP_FILTER_MIB'
        ),
    },
    'CISCOIGMPFILTERMIB.CIgmpFilterTable.CIgmpFilterEntry.CIgmpFilterProfileAction_Enum' : _MetaInfoEnum('CIgmpFilterProfileAction_Enum', 'ydk.models.igmp.CISCO_IGMP_FILTER_MIB',
        {
            'permit':'PERMIT',
            'deny':'DENY',
        }, 'CISCO-IGMP-FILTER-MIB', _yang_ns._namespaces['CISCO-IGMP-FILTER-MIB']),
    'CISCOIGMPFILTERMIB.CIgmpFilterTable.CIgmpFilterEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIGMPFILTERMIB.CIgmpFilterTable.CIgmpFilterEntry',
            False, 
            [
            _MetaInfoClassMember('cIgmpFilterProfileIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Index identifying this entry.
                ''',
                'cigmpfilterprofileindex',
                'CISCO-IGMP-FILTER-MIB', True),
            _MetaInfoClassMember('cIgmpFilterStartAddress', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                This object describes the start of the IP multicast
                group address of a contiguous range which will be
                subjected to filtering operation.
                ''',
                'cigmpfilterstartaddress',
                'CISCO-IGMP-FILTER-MIB', True),
            _MetaInfoClassMember('cIgmpFilterStartAddressType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                This object describes the type of Internet
                address used to determine the start address 
                of IP multicast group for a profile.
                ''',
                'cigmpfilterstartaddresstype',
                'CISCO-IGMP-FILTER-MIB', True),
            _MetaInfoClassMember('cIgmpFilterEndAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the end of the IP multicast
                group address of a contiguous range which will be 
                subjected to filtering operation.
                ''',
                'cigmpfilterendaddress',
                'CISCO-IGMP-FILTER-MIB', False),
            _MetaInfoClassMember('cIgmpFilterEndAddressType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                This object indicates the type of Internet
                address used to determine the end address 
                of IP multicast group for a profile.
                ''',
                'cigmpfilterendaddresstype',
                'CISCO-IGMP-FILTER-MIB', False),
            _MetaInfoClassMember('cIgmpFilterProfileAction', REFERENCE_ENUM_CLASS, 'CIgmpFilterProfileAction_Enum' , 'ydk.models.igmp.CISCO_IGMP_FILTER_MIB', 'CISCOIGMPFILTERMIB.CIgmpFilterTable.CIgmpFilterEntry.CIgmpFilterProfileAction_Enum', 
                [], [], 
                '''                This object defines the action for
                filtering IGMP reports for this profile.
                
                If the object is set to deny(2):
                then all IGMP reports associated to IP multicast
                groups included in the profile identified by
                cIgmpFilterInterfaceProfileIndex will be dropped.
                
                If the object is set to permit(1):
                then all IGMP reports associated to IP multicast
                groups not included in the profile identified by
                cIgmpFilterInterfaceProfileIndex will be dropped.
                ''',
                'cigmpfilterprofileaction',
                'CISCO-IGMP-FILTER-MIB', False),
            ],
            'CISCO-IGMP-FILTER-MIB',
            'cIgmpFilterEntry',
            _yang_ns._namespaces['CISCO-IGMP-FILTER-MIB'],
        'ydk.models.igmp.CISCO_IGMP_FILTER_MIB'
        ),
    },
    'CISCOIGMPFILTERMIB.CIgmpFilterTable' : {
        'meta_info' : _MetaInfoClass('CISCOIGMPFILTERMIB.CIgmpFilterTable',
            False, 
            [
            _MetaInfoClassMember('cIgmpFilterEntry', REFERENCE_LIST, 'CIgmpFilterEntry' , 'ydk.models.igmp.CISCO_IGMP_FILTER_MIB', 'CISCOIGMPFILTERMIB.CIgmpFilterTable.CIgmpFilterEntry', 
                [], [], 
                '''                An entry (conceptual row) in the cIgmpFilterTable.
                
                The creation, deletion or modification of an entry
                is controlled through the MIB objects defined under
                cIgmpFilterEditor group.
                ''',
                'cigmpfilterentry',
                'CISCO-IGMP-FILTER-MIB', False),
            ],
            'CISCO-IGMP-FILTER-MIB',
            'cIgmpFilterTable',
            _yang_ns._namespaces['CISCO-IGMP-FILTER-MIB'],
        'ydk.models.igmp.CISCO_IGMP_FILTER_MIB'
        ),
    },
    'CISCOIGMPFILTERMIB' : {
        'meta_info' : _MetaInfoClass('CISCOIGMPFILTERMIB',
            False, 
            [
            _MetaInfoClassMember('cIgmpFilterEditor', REFERENCE_CLASS, 'CIgmpFilterEditor' , 'ydk.models.igmp.CISCO_IGMP_FILTER_MIB', 'CISCOIGMPFILTERMIB.CIgmpFilterEditor', 
                [], [], 
                '''                ''',
                'cigmpfiltereditor',
                'CISCO-IGMP-FILTER-MIB', False),
            _MetaInfoClassMember('cIgmpFilterGeneral', REFERENCE_CLASS, 'CIgmpFilterGeneral' , 'ydk.models.igmp.CISCO_IGMP_FILTER_MIB', 'CISCOIGMPFILTERMIB.CIgmpFilterGeneral', 
                [], [], 
                '''                ''',
                'cigmpfiltergeneral',
                'CISCO-IGMP-FILTER-MIB', False),
            _MetaInfoClassMember('cIgmpFilterInterfaceTable', REFERENCE_CLASS, 'CIgmpFilterInterfaceTable' , 'ydk.models.igmp.CISCO_IGMP_FILTER_MIB', 'CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable', 
                [], [], 
                '''                This table contains the list of interfaces that can
                support IGMP filter feature.
                ''',
                'cigmpfilterinterfacetable',
                'CISCO-IGMP-FILTER-MIB', False),
            _MetaInfoClassMember('cIgmpFilterTable', REFERENCE_CLASS, 'CIgmpFilterTable' , 'ydk.models.igmp.CISCO_IGMP_FILTER_MIB', 'CISCOIGMPFILTERMIB.CIgmpFilterTable', 
                [], [], 
                '''                This table contains entries that identify lists of
                IP Multicast groups for each profile configured on
                the device. 
                
                Each entry contains a range of contiguous IP
                Multicast groups associated to a profile index.
                Multiple cIgmpFilterEntry may be associated
                with the same cIgmpFilterProfileIndex.
                
                All the cIgmpFilterEntry with  the same profile index 
                are subjected to the same IGMP filtering action as 
                defined in cIgmpFilterProfileAction.
                
                Each profile index may be associated with zero or more 
                interfaces through cIgmpFilterInterfaceIfIndex
                object in cIgmpFilterInterfaceTable.
                The maximum number of entries is determined by
                cIgmpFilterMaxProfiles.
                ''',
                'cigmpfiltertable',
                'CISCO-IGMP-FILTER-MIB', False),
            ],
            'CISCO-IGMP-FILTER-MIB',
            'CISCO-IGMP-FILTER-MIB',
            _yang_ns._namespaces['CISCO-IGMP-FILTER-MIB'],
        'ydk.models.igmp.CISCO_IGMP_FILTER_MIB'
        ),
    },
}
_meta_table['CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable.CIgmpFilterInterfaceEntry']['meta_info'].parent =_meta_table['CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable']['meta_info']
_meta_table['CISCOIGMPFILTERMIB.CIgmpFilterTable.CIgmpFilterEntry']['meta_info'].parent =_meta_table['CISCOIGMPFILTERMIB.CIgmpFilterTable']['meta_info']
_meta_table['CISCOIGMPFILTERMIB.CIgmpFilterEditor']['meta_info'].parent =_meta_table['CISCOIGMPFILTERMIB']['meta_info']
_meta_table['CISCOIGMPFILTERMIB.CIgmpFilterGeneral']['meta_info'].parent =_meta_table['CISCOIGMPFILTERMIB']['meta_info']
_meta_table['CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable']['meta_info'].parent =_meta_table['CISCOIGMPFILTERMIB']['meta_info']
_meta_table['CISCOIGMPFILTERMIB.CIgmpFilterTable']['meta_info'].parent =_meta_table['CISCOIGMPFILTERMIB']['meta_info']
