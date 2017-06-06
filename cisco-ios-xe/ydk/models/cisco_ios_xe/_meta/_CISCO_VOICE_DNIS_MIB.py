


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoVoiceDnisMib.Cvdnismappingtable.Cvdnismappingentry.CvdnismappingrefreshEnum' : _MetaInfoEnum('CvdnismappingrefreshEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB',
        {
            'idle':'idle',
            'refresh':'refresh',
        }, 'CISCO-VOICE-DNIS-MIB', _yang_ns._namespaces['CISCO-VOICE-DNIS-MIB']),
    'CiscoVoiceDnisMib.Cvdnismappingtable.Cvdnismappingentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDnisMib.Cvdnismappingtable.Cvdnismappingentry',
            False, 
            [
            _MetaInfoClassMember('cvDnisMappingName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                The name which uniquely identifies a DNIS mapping. 
                ''',
                'cvdnismappingname',
                'CISCO-VOICE-DNIS-MIB', True),
            _MetaInfoClassMember('cvDnisMappingRefresh', REFERENCE_ENUM_CLASS, 'CvdnismappingrefreshEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB', 'CiscoVoiceDnisMib.Cvdnismappingtable.Cvdnismappingentry.CvdnismappingrefreshEnum', 
                [], [], 
                '''                Whenever there is a need to re-read the contents of the
                file specified by cvDnisMappingUrl, this object can be
                set to refresh(2). This will cause the contents of the
                file to be re-read and correspondingly update the
                cvDnisNodeTable. After the completion of this operation,
                the value of this object is reset to idle(1). The only
                operation allowed on this object is setting it to
                refresh(2). This can only be done when the current value
                is idle(1) and the rowstatus is active(1).
                
                idle       - The refreshing process is idle and the user
                             can modify this object to refresh.
                refresh    - The refreshing process is currently busy and
                             the user have to wait till the object
                             becomes idle to issue new refresh.
                ''',
                'cvdnismappingrefresh',
                'CISCO-VOICE-DNIS-MIB', False),
            _MetaInfoClassMember('cvDnisMappingStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object is used to create a new row or modify or
                delete an existing row in this table. When making the
                status active(1), if a valid cvDnisMappingUrl is present
                the contents of the url is downloaded and during that
                time cvDnisMappingRefresh is set to refresh(2). When
                cvDnisMappingRefresh is set to refresh(2), only the
                destroy(6) operation is allowed.
                ''',
                'cvdnismappingstatus',
                'CISCO-VOICE-DNIS-MIB', False),
            _MetaInfoClassMember('cvDnisMappingUrl', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The url specifies a file location. The file contains
                individual DNIS entries that belong to the DNIS map 
                name specified by cvDnisMappingName.
                
                Once a url is created and associated with a map name (the
                association is complete when the row is made active(1)),
                it cannot be modified while cvDnisMappingStatus is
                active. If a different url needs to be associated with
                the current map name, the row status should be made
                notInService(2) and this object has to be modified to
                associate a new url. When a new association is made all
                the DNIS entries corresponding to the old association
                will be deleted from the cvDnisNodeTable.
                
                The url is read when the row status is made active(1) or
                when the row status is active and the object 
                 cvDnisMappingRefresh is explicitly set to refresh(2). 
                 If the url is not accessible then a
                cvDnisMappingUrlInaccessible notification will be
                generted. 
                ''',
                'cvdnismappingurl',
                'CISCO-VOICE-DNIS-MIB', False),
            _MetaInfoClassMember('cvDnisMappingUrlAccessError', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ASCII text describing the error on last access of the url
                specified in cvDnisMappingUrl.
                
                If the url access does not succeed, then this object is
                populated with an error message indicating the reason for
                failure. If the url access succeeds, this object is set
                to null string.
                ''',
                'cvdnismappingurlaccesserror',
                'CISCO-VOICE-DNIS-MIB', False),
            ],
            'CISCO-VOICE-DNIS-MIB',
            'cvDnisMappingEntry',
            _yang_ns._namespaces['CISCO-VOICE-DNIS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB'
        ),
    },
    'CiscoVoiceDnisMib.Cvdnismappingtable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDnisMib.Cvdnismappingtable',
            False, 
            [
            _MetaInfoClassMember('cvDnisMappingEntry', REFERENCE_LIST, 'Cvdnismappingentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB', 'CiscoVoiceDnisMib.Cvdnismappingtable.Cvdnismappingentry', 
                [], [], 
                '''                Information about a single DNIS mapping. There is a
                unique DNIS map name. New DNIS mapping can be created
                using cvDnisMappingStatus.
                
                The entry can be created with or without a file location 
                specified by cvDnisMappingUrl. The mapping file contains
                DNIS name and VXML page per line. For example, a 
                cvDnisMappingUrl could be tftp://someserver/dnismap.txt.
                This file is a text file and the content format is
                  dnis <dnisname> url <urlname>.
                An example of the contents of the file itself can be
                  dnis 18004251234 url http://www.b.com/p/vwelcome.vxml
                  dnis 18004253421 url http://www.c.com/j/vxmlintf.vxml
                If a mapping file location is specified, then new rows
                corresponding to this map name are created and populated
                in cvDnisNodeTable from the contents of the file. The
                rows corresponding to this map name in cvDnisNodeTable
                cannot be created or modified or deleted but can be
                read. 
                
                If a mapping file location is not specified in
                cvDnisMappingUrl, then individual DNIS entries
                corresponding to this map name can be created, modified
                and deleted in cvDnisNodeTable. 
                
                Deleting an entry deletes all the related entries in
                cvDnisNodeTable. 
                ''',
                'cvdnismappingentry',
                'CISCO-VOICE-DNIS-MIB', False),
            ],
            'CISCO-VOICE-DNIS-MIB',
            'cvDnisMappingTable',
            _yang_ns._namespaces['CISCO-VOICE-DNIS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB'
        ),
    },
    'CiscoVoiceDnisMib.Cvdnisnodetable.Cvdnisnodeentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDnisMib.Cvdnisnodetable.Cvdnisnodeentry',
            False, 
            [
            _MetaInfoClassMember('cvDnisMappingName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                ''',
                'cvdnismappingname',
                'CISCO-VOICE-DNIS-MIB', True),
            _MetaInfoClassMember('cvDnisNumber', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The individual DNIS name. It is unique within a DNIS
                mapping.
                ''',
                'cvdnisnumber',
                'CISCO-VOICE-DNIS-MIB', True),
            _MetaInfoClassMember('cvDnisNodeModifiable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the object in a particular
                row is modifiable. The object is set to true(1) if the
                corresponding map name (defined in cvDnisMappingTable)
                does not have any file name provided in the
                cvDnisMappingUrl object. Otherwise this object is set to
                false(2) and the row becomes read only.  
                ''',
                'cvdnisnodemodifiable',
                'CISCO-VOICE-DNIS-MIB', False),
            _MetaInfoClassMember('cvDnisNodeStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object is used to create a new row or modify or
                delete an existing row in this table. The objects in a
                row can be modified or deleted while the row status is
                active(1) and cvDnisNodeModifiable is true(1). The row
                status cannot be set to notInService(2) or
                createAndWait(5). 
                ''',
                'cvdnisnodestatus',
                'CISCO-VOICE-DNIS-MIB', False),
            _MetaInfoClassMember('cvDnisNodeUrl', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The url specifies a VXML page. This page contains
                voice XML links to play audio data.
                
                This url which is a VXML page is not read immediately
                when the row is made active(1), but only when a call that
                requires the use of this DNIS comes through.
                ''',
                'cvdnisnodeurl',
                'CISCO-VOICE-DNIS-MIB', False),
            ],
            'CISCO-VOICE-DNIS-MIB',
            'cvDnisNodeEntry',
            _yang_ns._namespaces['CISCO-VOICE-DNIS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB'
        ),
    },
    'CiscoVoiceDnisMib.Cvdnisnodetable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDnisMib.Cvdnisnodetable',
            False, 
            [
            _MetaInfoClassMember('cvDnisNodeEntry', REFERENCE_LIST, 'Cvdnisnodeentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB', 'CiscoVoiceDnisMib.Cvdnisnodetable.Cvdnisnodeentry', 
                [], [], 
                '''                Each entry is a DNIS name and the location of the
                associated VXML page. New DNIS entries can be created or
                the existing entries can be modified or deleted only if
                the corresponding map name (defined in
                cvDnisMappingTable) does not have any file name provided
                in the cvDnisMappingUrl object. 
                
                If a file name is provided in cvDnisMappingUrl
                corresponding to this entry's map name, then this row
                will have read permission only.
                ''',
                'cvdnisnodeentry',
                'CISCO-VOICE-DNIS-MIB', False),
            ],
            'CISCO-VOICE-DNIS-MIB',
            'cvDnisNodeTable',
            _yang_ns._namespaces['CISCO-VOICE-DNIS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB'
        ),
    },
    'CiscoVoiceDnisMib' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDnisMib',
            False, 
            [
            _MetaInfoClassMember('cvDnisMappingTable', REFERENCE_CLASS, 'Cvdnismappingtable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB', 'CiscoVoiceDnisMib.Cvdnismappingtable', 
                [], [], 
                '''                The table contains the map name and a url specifying
                a file name. The file contains DNIS entries that belong
                to the DNIS mapping.
                ''',
                'cvdnismappingtable',
                'CISCO-VOICE-DNIS-MIB', False),
            _MetaInfoClassMember('cvDnisNodeTable', REFERENCE_CLASS, 'Cvdnisnodetable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB', 'CiscoVoiceDnisMib.Cvdnisnodetable', 
                [], [], 
                '''                The table contains a DNIS name and a url. The url is a
                pointer to a VXML page for the DNIS name. 
                ''',
                'cvdnisnodetable',
                'CISCO-VOICE-DNIS-MIB', False),
            ],
            'CISCO-VOICE-DNIS-MIB',
            'CISCO-VOICE-DNIS-MIB',
            _yang_ns._namespaces['CISCO-VOICE-DNIS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB'
        ),
    },
}
_meta_table['CiscoVoiceDnisMib.Cvdnismappingtable.Cvdnismappingentry']['meta_info'].parent =_meta_table['CiscoVoiceDnisMib.Cvdnismappingtable']['meta_info']
_meta_table['CiscoVoiceDnisMib.Cvdnisnodetable.Cvdnisnodeentry']['meta_info'].parent =_meta_table['CiscoVoiceDnisMib.Cvdnisnodetable']['meta_info']
_meta_table['CiscoVoiceDnisMib.Cvdnismappingtable']['meta_info'].parent =_meta_table['CiscoVoiceDnisMib']['meta_info']
_meta_table['CiscoVoiceDnisMib.Cvdnisnodetable']['meta_info'].parent =_meta_table['CiscoVoiceDnisMib']['meta_info']
