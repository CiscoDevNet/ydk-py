


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoBulkFileMib.Cbfdefine' : {
        'meta_info' : _MetaInfoClass('CiscoBulkFileMib.Cbfdefine',
            False, 
            [
            _MetaInfoClassMember('cbfDefineFiles', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The current number of file definitions in cbfDefineFileTable.
                ''',
                'cbfdefinefiles',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineFilesRefused', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of attempts to create a file definition that
                failed due to exceeding cbfDefineMaxFiles.
                ''',
                'cbfdefinefilesrefused',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineHighFiles', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum value of cbfDefineFiles since system 
                initialization.
                ''',
                'cbfdefinehighfiles',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineHighObjects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum value of cbfDefineObjects since system 
                initialization.
                ''',
                'cbfdefinehighobjects',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineMaxFiles', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum number of file definitions this system
                can hold in cbfDefineFileTable.  A value of 0 indicates no
                configured limit.
                
                This object may be read-only on some systems.
                
                Changing this number does not disturb existing entries.
                ''',
                'cbfdefinemaxfiles',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineMaxObjects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum total number of object selections to go with
                file definitions this system, that is, the total number
                of objects this system can hold in cbfDefineObjectTable.  A
                value of 0 indicates no configured limit.
                
                This object may be read-only on some systems.
                
                Changing this number does not disturb existing entries.
                ''',
                'cbfdefinemaxobjects',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineObjects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The current number of object selections in 
                cbfDefineObjectTable.
                ''',
                'cbfdefineobjects',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineObjectsRefused', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of attempts to create an object selection that
                failed due to exceeding cbfDefineMaxObjects.
                ''',
                'cbfdefineobjectsrefused',
                'CISCO-BULK-FILE-MIB', False),
            ],
            'CISCO-BULK-FILE-MIB',
            'cbfDefine',
            _yang_ns._namespaces['CISCO-BULK-FILE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB'
        ),
    },
    'CiscoBulkFileMib.Cbfstatus' : {
        'meta_info' : _MetaInfoClass('CiscoBulkFileMib.Cbfstatus',
            False, 
            [
            _MetaInfoClassMember('cbfStatusFiles', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The current number of file statuses in cbfStatusFileTable.
                ''',
                'cbfstatusfiles',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfStatusFilesBumped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number times the oldest entry was deleted due to exceeding
                cbfStatusMaxFiles.
                ''',
                'cbfstatusfilesbumped',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfStatusHighFiles', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum value of cbfStatusFiles since system 
                initialization.
                ''',
                'cbfstatushighfiles',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfStatusMaxFiles', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum number of file statuses this system
                can hold in cbfStatusFileTable.  A value of 0 indicates no
                configured limit.
                
                This object may be read-only on some systems.
                
                Changing this number deletes the oldest finished entries until
                the new limit is satisfied.
                ''',
                'cbfstatusmaxfiles',
                'CISCO-BULK-FILE-MIB', False),
            ],
            'CISCO-BULK-FILE-MIB',
            'cbfStatus',
            _yang_ns._namespaces['CISCO-BULK-FILE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB'
        ),
    },
    'CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry.CbfdefinefileformatEnum' : _MetaInfoEnum('CbfdefinefileformatEnum', 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB',
        {
            'standardBER':'standardBER',
            'bulkBinary':'bulkBinary',
            'bulkASCII':'bulkASCII',
            'variantBERWithCksum':'variantBERWithCksum',
            'variantBinWithCksum':'variantBinWithCksum',
        }, 'CISCO-BULK-FILE-MIB', _yang_ns._namespaces['CISCO-BULK-FILE-MIB']),
    'CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry.CbfdefinefilenowEnum' : _MetaInfoEnum('CbfdefinefilenowEnum', 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB',
        {
            'notActive':'notActive',
            'ready':'ready',
            'create':'create',
            'running':'running',
            'forcedCreate':'forcedCreate',
        }, 'CISCO-BULK-FILE-MIB', _yang_ns._namespaces['CISCO-BULK-FILE-MIB']),
    'CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry.CbfdefinefilestorageEnum' : _MetaInfoEnum('CbfdefinefilestorageEnum', 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB',
        {
            'ephemeral':'ephemeral',
            'volatile':'volatile',
            'permanent':'permanent',
        }, 'CISCO-BULK-FILE-MIB', _yang_ns._namespaces['CISCO-BULK-FILE-MIB']),
    'CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry' : {
        'meta_info' : _MetaInfoClass('CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry',
            False, 
            [
            _MetaInfoClassMember('cbfDefineFileIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An arbitrary integer to uniquely identify this entry.  To
                create an entry a management application should pick a
                random number.
                ''',
                'cbfdefinefileindex',
                'CISCO-BULK-FILE-MIB', True),
            _MetaInfoClassMember('cbfDefineFileEntryStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The control that allows creation, modification, and deletion
                of entries.  For detailed rules see the DESCRIPTION for
                cbfDefineFileEntry.
                ''',
                'cbfdefinefileentrystatus',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineFileFormat', REFERENCE_ENUM_CLASS, 'CbfdefinefileformatEnum' , 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry.CbfdefinefileformatEnum', 
                [], [], 
                '''                The format of the data in the file:
                
                StandardBER        standard SNMP ASN.1 BER
                bulkBinary        a binary format specified with this MIB
                bulkASCII        a human-readable form of bulkBinary
                variantBERWithCksum ASN.1 BER encoding with checksum
                variantBinWithCksum a binary format with checksum
                
                    A given system may support any or all of these.
                ''',
                'cbfdefinefileformat',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineFileName', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The file name which is to be created.
                
                Explicit device or path choices in the value of this object
                override cbfDefineFileStorage.
                ''',
                'cbfdefinefilename',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineFileNotifyOnCompletion', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This controls the cbfDefineFileCompletion notification.
                
                If true, cbfDefineFileCompletion notification
                will be generated. It is the responsibility of the 
                management entity to ensure that the SNMP administrative 
                model is configured in such a way as to allow the 
                notification to be delivered.
                ''',
                'cbfdefinefilenotifyoncompletion',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineFileNow', REFERENCE_ENUM_CLASS, 'CbfdefinefilenowEnum' , 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry.CbfdefinefilenowEnum', 
                [], [], 
                '''                The control to cause file creation.  The only values that can
                be set are 'create' and 'forcedCreate'. These can be set only 
                when the value is 'ready'.  Setting it to 'create' begins a 
                file creation and creates a corresponding entry in 
                cbfStatusFileTable. The system may choose to use an already 
                existing copy of the file instead of creating a new one. This
                may happen if there has been no configuration change on the 
                system and a request to recreate the file is received. 
                Setting this object to 'forcedCreate' forces the system to 
                create a new copy of the file.
                
                The value is 'notActve' as long as cbfDefineFileEntryStatus or
                any corresponding cbfDefineObjectEntryStatus is not active.
                
                When cbfDefineFileEntryStatus becomes active and all
                corresponding cbfDefineObjectEntryStatuses are active this 
                object automatically goes to 'ready'.
                ''',
                'cbfdefinefilenow',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineFileStorage', REFERENCE_ENUM_CLASS, 'CbfdefinefilestorageEnum' , 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry.CbfdefinefilestorageEnum', 
                [], [], 
                '''                The type of file storage to use:
                
                ephemeral        data exists in small amounts until read
                volatile        data exists in volatile memory
                permanent        data survives reboot
                
                An ephemeral file is suitable to be read only one time.
                
                Note that this value is taken as advisory and may be overridden
                by explicit device or path choices in cbfDefineFile.
                
                A given system may support any or all of these.
                ''',
                'cbfdefinefilestorage',
                'CISCO-BULK-FILE-MIB', False),
            ],
            'CISCO-BULK-FILE-MIB',
            'cbfDefineFileEntry',
            _yang_ns._namespaces['CISCO-BULK-FILE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB'
        ),
    },
    'CiscoBulkFileMib.Cbfdefinefiletable' : {
        'meta_info' : _MetaInfoClass('CiscoBulkFileMib.Cbfdefinefiletable',
            False, 
            [
            _MetaInfoClassMember('cbfDefineFileEntry', REFERENCE_LIST, 'Cbfdefinefileentry' , 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry', 
                [], [], 
                '''                Information for creation of a bulk file.
                
                To creat a bulk file an application creates an entry in this
                table and corresponding entries in cbfDefineObjectTable.
                
                When the entry in this table and the corresponding
                entries in cbfDefineObjectTable are 'active' the
                appliction uses cbfDefineFileNow to create the file
                and a corresponding entry in cbfStatusFileTable.
                
                Deleting an entry in cbfDefineFileTable deletes all
                corresponding entries in cbfDefineObjectTable and
                cbfStatusFileTable.
                
                An entry may not be modified or deleted while its
                cbfDefineFileNow has the value 'running'.
                ''',
                'cbfdefinefileentry',
                'CISCO-BULK-FILE-MIB', False),
            ],
            'CISCO-BULK-FILE-MIB',
            'cbfDefineFileTable',
            _yang_ns._namespaces['CISCO-BULK-FILE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB'
        ),
    },
    'CiscoBulkFileMib.Cbfdefineobjecttable.Cbfdefineobjectentry.CbfdefineobjectclassEnum' : _MetaInfoEnum('CbfdefineobjectclassEnum', 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB',
        {
            'object':'object',
            'lexicalTable':'lexicalTable',
            'leastCpuTable':'leastCpuTable',
        }, 'CISCO-BULK-FILE-MIB', _yang_ns._namespaces['CISCO-BULK-FILE-MIB']),
    'CiscoBulkFileMib.Cbfdefineobjecttable.Cbfdefineobjectentry' : {
        'meta_info' : _MetaInfoClass('CiscoBulkFileMib.Cbfdefineobjecttable.Cbfdefineobjectentry',
            False, 
            [
            _MetaInfoClassMember('cbfDefineFileIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'cbfdefinefileindex',
                'CISCO-BULK-FILE-MIB', True),
            _MetaInfoClassMember('cbfDefineObjectIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An arbitrary integer to uniquely identify this entry.
                
                The numeric order of the entries controls the order of
                the objects in the file.
                ''',
                'cbfdefineobjectindex',
                'CISCO-BULK-FILE-MIB', True),
            _MetaInfoClassMember('cbfDefineObjectClass', REFERENCE_ENUM_CLASS, 'CbfdefineobjectclassEnum' , 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CiscoBulkFileMib.Cbfdefineobjecttable.Cbfdefineobjectentry.CbfdefineobjectclassEnum', 
                [], [], 
                '''                The meaning of each object class is given below:
                
                object          a single MIB object is retrieved.
                
                lexicalTable    an entire table or partial table
                                is retrieved in lexical order of rows.
                
                leastCpuTable   an entire table is retrieved with
                                lowest CPU utilization.
                                Lexical ordering of rows may not be 
                                maintained and is dependent upon 
                                individual MIB implementation.
                ''',
                'cbfdefineobjectclass',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineObjectEntryStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The control that allows creation, modification, and deletion
                of entries.  For detailed rules see the DESCRIPTION for
                cbfDefineObjectEntry.
                ''',
                'cbfdefineobjectentrystatus',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineObjectID', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The object identifier of a MIB object to be included in
                the file.
                
                If cbfDefineObjectClass is 'object' this must be a full OID,
                including all instance information.
                
                If cbfDefineObjectClass is 'lexicalTable' or 'leastCpuTable'
                this must be the OID of the table-defining SEQUENCE OF
                registration point.
                ''',
                'cbfdefineobjectid',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineObjectLastPolledInst', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object represents the last polled instance in the
                table.
                
                The value represented by this object will be relevent only
                if the corresponding cbfStatusFileState is emptied(3) for 
                ephemeral files or ready(2) for volatile or permanent files.
                
                A value of zeroDotZero indicates an absence of last polled 
                object.
                
                An NMS can use the value of this object and populate the
                cbfDefineObjectTableInstance to retrieve a contiguous set
                of rows in a table.
                ''',
                'cbfdefineobjectlastpolledinst',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineObjectNumEntries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If cbfDefineObjectClass is 'lexicalTable', then this object
                represents the maximum number of entries which will be 
                populated in the file starting from the lexicographically
                next instance of the OID represented by 
                cbfDefineObjectTableInstance. 
                
                This object is irrelevent if cbfDefineObjectClass is not
                'lexicalTable'.
                
                Refer to the description of cbfDefineObjectTableInstance for
                examples and different scenarios relating to this object.
                ''',
                'cbfdefineobjectnumentries',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineObjectTableInstance', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                If cbfDefineObjectClass is 'lexicalTable', then this object
                represents the starting instance in the cbfDefineObjectID
                table. The file created will have entries starting from
                the lexicographically next instance of the OID represented
                by this object. 
                
                For Eg: 
                -------
                
                       Let us  assume we are polling ifTable and we
                       have information till the second row(ifIndex.2). Now
                       we may be interested in 10 rows lexically following
                       the second row.
                       
                       So, we set cbfDefineObjectTableInstance as ifIndex.2 
                       and cbfDefineObjectNumEntries as 10. 
                
                       We will get information for the next 10 rows or
                       if there are less than 10 populated rows, we will
                       receive information till the end of the table is 
                       reached.
                
                The default value for this object is zeroDotZero.
                
                If this object has the value of zeroDotZero and 
                cbfDefineObjectNumEntries has value 0, then the whole
                table(represented by cbfDefineObjectID) is retrieved.
                
                If this object has the value of zeroDotZero,  
                cbfDefineObjectNumEntries has value n (>0) and there are 
                m(>0) entries in the table(represented by cbfDefineObjectID)
                then the first n entries in the table are retrieved if n < m. 
                If n >= m, then the whole table is retrieved.
                
                When the value of cbfDefineObjectNumEntries is 0, 
                it means all the entries in the table(represented 
                by cbfDefineObjectID) which lexicographically follow 
                cbfDefineObjectTableInstance are retrieved.
                
                This object is irrelevent if cbfDefineObjectClass is not
                'lexicalTable'.
                ''',
                'cbfdefineobjecttableinstance',
                'CISCO-BULK-FILE-MIB', False),
            ],
            'CISCO-BULK-FILE-MIB',
            'cbfDefineObjectEntry',
            _yang_ns._namespaces['CISCO-BULK-FILE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB'
        ),
    },
    'CiscoBulkFileMib.Cbfdefineobjecttable' : {
        'meta_info' : _MetaInfoClass('CiscoBulkFileMib.Cbfdefineobjecttable',
            False, 
            [
            _MetaInfoClassMember('cbfDefineObjectEntry', REFERENCE_LIST, 'Cbfdefineobjectentry' , 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CiscoBulkFileMib.Cbfdefineobjecttable.Cbfdefineobjectentry', 
                [], [], 
                '''                Information about one object for a particular file.
                
                An application uses cbfDefineObjectEntryStatus to create entries
                in this table in correspondence with entries in
                cbfDefineFileTable, which must be created first.
                
                Entries in this table may not be changed, created or deleted
                while the corresponding value of cbfDefineFileNow is 'running'.
                ''',
                'cbfdefineobjectentry',
                'CISCO-BULK-FILE-MIB', False),
            ],
            'CISCO-BULK-FILE-MIB',
            'cbfDefineObjectTable',
            _yang_ns._namespaces['CISCO-BULK-FILE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB'
        ),
    },
    'CiscoBulkFileMib.Cbfstatusfiletable.Cbfstatusfileentry.CbfstatusfilestateEnum' : _MetaInfoEnum('CbfstatusfilestateEnum', 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB',
        {
            'running':'running',
            'ready':'ready',
            'emptied':'emptied',
            'noSpace':'noSpace',
            'badName':'badName',
            'writeErr':'writeErr',
            'noMem':'noMem',
            'buffErr':'buffErr',
            'aborted':'aborted',
        }, 'CISCO-BULK-FILE-MIB', _yang_ns._namespaces['CISCO-BULK-FILE-MIB']),
    'CiscoBulkFileMib.Cbfstatusfiletable.Cbfstatusfileentry' : {
        'meta_info' : _MetaInfoClass('CiscoBulkFileMib.Cbfstatusfiletable.Cbfstatusfileentry',
            False, 
            [
            _MetaInfoClassMember('cbfDefineFileIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'cbfdefinefileindex',
                'CISCO-BULK-FILE-MIB', True),
            _MetaInfoClassMember('cbfStatusFileIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An arbitrary integer to uniquely identify this file.
                
                The numeric order of the entries implies the creation
                order of the files.
                ''',
                'cbfstatusfileindex',
                'CISCO-BULK-FILE-MIB', True),
            _MetaInfoClassMember('cbfStatusFileCompletionTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the creation attempt completed.
                A value of 0 indicates not complete.  For ephemeral files this
                is the time when cbfStatusFileState goes to 'emptied'.  For
                others this is the time when the state leaves 'running'.
                ''',
                'cbfstatusfilecompletiontime',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfStatusFileEntryStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The control that allows deletion of entries. For detailed rules
                see the DESCRIPTION for cbfStatusFileEntry.
                
                This object may not be set to any value other than 'destroy'.
                ''',
                'cbfstatusfileentrystatus',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfStatusFileState', REFERENCE_ENUM_CLASS, 'CbfstatusfilestateEnum' , 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CiscoBulkFileMib.Cbfstatusfiletable.Cbfstatusfileentry.CbfstatusfilestateEnum', 
                [], [], 
                '''                The file state:
                
                running    data is being written to the file
                ready      the file is ready to be read
                emptied    an ephemeral file was successfully consumed
                noSpace    no data due to insufficient file space
                badName    no data due to a name or path problem
                writeErr   no data due to fatal file write error
                noMem      no data due to insufficient dynamic memory
                buffErr    implementation buffer too small
                aborted    short terminated by operator command
                
                Only the 'ready' state implies that the file is available
                for transfer.
                
                The disposition of files after an error is implementation
                and file-syste specific.
                ''',
                'cbfstatusfilestate',
                'CISCO-BULK-FILE-MIB', False),
            ],
            'CISCO-BULK-FILE-MIB',
            'cbfStatusFileEntry',
            _yang_ns._namespaces['CISCO-BULK-FILE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB'
        ),
    },
    'CiscoBulkFileMib.Cbfstatusfiletable' : {
        'meta_info' : _MetaInfoClass('CiscoBulkFileMib.Cbfstatusfiletable',
            False, 
            [
            _MetaInfoClassMember('cbfStatusFileEntry', REFERENCE_LIST, 'Cbfstatusfileentry' , 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CiscoBulkFileMib.Cbfstatusfiletable.Cbfstatusfileentry', 
                [], [], 
                '''                Status for a particular file.
                
                An entry exists in this table for each time cbfDefineFileNow
                has been set to 'create' and the corresponding entry here
                has not been explicitly deleted by the application or bumped
                to make room for a new entry.
                
                Deleting an entry with cbfStatusFileState 'running' aborts
                the file creation attempt.
                
                It is implementation and file-system specific whether deleting
                the entry also deletes the file.
                ''',
                'cbfstatusfileentry',
                'CISCO-BULK-FILE-MIB', False),
            ],
            'CISCO-BULK-FILE-MIB',
            'cbfStatusFileTable',
            _yang_ns._namespaces['CISCO-BULK-FILE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB'
        ),
    },
    'CiscoBulkFileMib' : {
        'meta_info' : _MetaInfoClass('CiscoBulkFileMib',
            False, 
            [
            _MetaInfoClassMember('cbfDefine', REFERENCE_CLASS, 'Cbfdefine' , 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CiscoBulkFileMib.Cbfdefine', 
                [], [], 
                '''                ''',
                'cbfdefine',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineFileTable', REFERENCE_CLASS, 'Cbfdefinefiletable' , 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CiscoBulkFileMib.Cbfdefinefiletable', 
                [], [], 
                '''                A table of bulk file definition and creation controls.
                ''',
                'cbfdefinefiletable',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfDefineObjectTable', REFERENCE_CLASS, 'Cbfdefineobjecttable' , 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CiscoBulkFileMib.Cbfdefineobjecttable', 
                [], [], 
                '''                A table of objects to go in bulk files.
                ''',
                'cbfdefineobjecttable',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfStatus', REFERENCE_CLASS, 'Cbfstatus' , 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CiscoBulkFileMib.Cbfstatus', 
                [], [], 
                '''                ''',
                'cbfstatus',
                'CISCO-BULK-FILE-MIB', False),
            _MetaInfoClassMember('cbfStatusFileTable', REFERENCE_CLASS, 'Cbfstatusfiletable' , 'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CiscoBulkFileMib.Cbfstatusfiletable', 
                [], [], 
                '''                A table of bulk file status.
                ''',
                'cbfstatusfiletable',
                'CISCO-BULK-FILE-MIB', False),
            ],
            'CISCO-BULK-FILE-MIB',
            'CISCO-BULK-FILE-MIB',
            _yang_ns._namespaces['CISCO-BULK-FILE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB'
        ),
    },
}
_meta_table['CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry']['meta_info'].parent =_meta_table['CiscoBulkFileMib.Cbfdefinefiletable']['meta_info']
_meta_table['CiscoBulkFileMib.Cbfdefineobjecttable.Cbfdefineobjectentry']['meta_info'].parent =_meta_table['CiscoBulkFileMib.Cbfdefineobjecttable']['meta_info']
_meta_table['CiscoBulkFileMib.Cbfstatusfiletable.Cbfstatusfileentry']['meta_info'].parent =_meta_table['CiscoBulkFileMib.Cbfstatusfiletable']['meta_info']
_meta_table['CiscoBulkFileMib.Cbfdefine']['meta_info'].parent =_meta_table['CiscoBulkFileMib']['meta_info']
_meta_table['CiscoBulkFileMib.Cbfstatus']['meta_info'].parent =_meta_table['CiscoBulkFileMib']['meta_info']
_meta_table['CiscoBulkFileMib.Cbfdefinefiletable']['meta_info'].parent =_meta_table['CiscoBulkFileMib']['meta_info']
_meta_table['CiscoBulkFileMib.Cbfdefineobjecttable']['meta_info'].parent =_meta_table['CiscoBulkFileMib']['meta_info']
_meta_table['CiscoBulkFileMib.Cbfstatusfiletable']['meta_info'].parent =_meta_table['CiscoBulkFileMib']['meta_info']
