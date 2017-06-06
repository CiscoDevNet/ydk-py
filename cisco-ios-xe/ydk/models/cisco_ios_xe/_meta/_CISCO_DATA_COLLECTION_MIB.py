


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CdcfilexferstatusEnum' : _MetaInfoEnum('CdcfilexferstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB',
        {
            'notStarted':'notStarted',
            'success':'success',
            'aborted':'aborted',
            'fileOpenFailRemote':'fileOpenFailRemote',
            'badDomainName':'badDomainName',
            'unreachableIpAddress':'unreachableIpAddress',
            'networkFailed':'networkFailed',
            'fileWriteFailed':'fileWriteFailed',
            'authFailed':'authFailed',
        }, 'CISCO-DATA-COLLECTION-MIB', _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB']),
    'CdcfileformatEnum' : _MetaInfoEnum('CdcfileformatEnum', 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB',
        {
            'cdcBulkASCII':'cdcBulkASCII',
            'cdcBulkBinary':'cdcBulkBinary',
            'cdcSchemaASCII':'cdcSchemaASCII',
        }, 'CISCO-DATA-COLLECTION-MIB', _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB']),
    'CiscoDataCollectionMib.Cdcvfile' : {
        'meta_info' : _MetaInfoClass('CiscoDataCollectionMib.Cdcvfile',
            False, 
            [
            _MetaInfoClassMember('cdcVFileMaxSizeHitsLimit', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                A global limit for the number of consecutive times the
                maximum VFile size (cdcVFileMaxSize) is exceeded for a
                given VFile. When this limit is exceeded the offending
                cdcVFileEntry is moved to the error state (see
                cdcVFileOperStatus).
                ''',
                'cdcvfilemaxsizehitslimit',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFilePersistentStorage', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object's value reads 'true', if the agent
                implementation of this MIB supports placement of VFiles in
                application specified persistent storage locations. Otherwise 
                the value is 'false'.
                ''',
                'cdcvfilepersistentstorage',
                'CISCO-DATA-COLLECTION-MIB', False),
            ],
            'CISCO-DATA-COLLECTION-MIB',
            'cdcVFile',
            _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB'
        ),
    },
    'CiscoDataCollectionMib.Cdcvfiletable.Cdcvfileentry.CdcvfileadminstatusEnum' : _MetaInfoEnum('CdcvfileadminstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'CISCO-DATA-COLLECTION-MIB', _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB']),
    'CiscoDataCollectionMib.Cdcvfiletable.Cdcvfileentry.CdcvfilecollectmodeEnum' : _MetaInfoEnum('CdcvfilecollectmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB',
        {
            'auto':'auto',
            'manual':'manual',
        }, 'CISCO-DATA-COLLECTION-MIB', _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB']),
    'CiscoDataCollectionMib.Cdcvfiletable.Cdcvfileentry.CdcvfilecommandEnum' : _MetaInfoEnum('CdcvfilecommandEnum', 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB',
        {
            'idle':'idle',
            'swapToNewFile':'swapToNewFile',
            'collectNow':'collectNow',
        }, 'CISCO-DATA-COLLECTION-MIB', _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB']),
    'CiscoDataCollectionMib.Cdcvfiletable.Cdcvfileentry.CdcvfileerrorcodeEnum' : _MetaInfoEnum('CdcvfileerrorcodeEnum', 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB',
        {
            'noError':'noError',
            'otherError':'otherError',
            'noSpace':'noSpace',
            'openError':'openError',
            'tooSmallMaxSize':'tooSmallMaxSize',
            'tooManyMaxSizeHits':'tooManyMaxSizeHits',
            'noResource':'noResource',
        }, 'CISCO-DATA-COLLECTION-MIB', _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB']),
    'CiscoDataCollectionMib.Cdcvfiletable.Cdcvfileentry.CdcvfileoperstatusEnum' : _MetaInfoEnum('CdcvfileoperstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
            'error':'error',
        }, 'CISCO-DATA-COLLECTION-MIB', _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB']),
    'CiscoDataCollectionMib.Cdcvfiletable.Cdcvfileentry' : {
        'meta_info' : _MetaInfoClass('CiscoDataCollectionMib.Cdcvfiletable.Cdcvfileentry',
            False, 
            [
            _MetaInfoClassMember('cdcVFileIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An arbitrary integer for uniquely identifying this
                entry. When creating a row, the application should pick a
                random number. 
                
                If the configuration in this entry is persisted across
                system/agent restarts then the same value of cdcVFileIndex
                must be assigned to this entry after the restart.
                ''',
                'cdcvfileindex',
                'CISCO-DATA-COLLECTION-MIB', True),
            _MetaInfoClassMember('cdcVFileAdminStatus', REFERENCE_ENUM_CLASS, 'CdcvfileadminstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcvfiletable.Cdcvfileentry.CdcvfileadminstatusEnum', 
                [], [], 
                '''                A control object to indicate the administratively desired
                state of data collection for this entry. On setting the value
                to 'disabled' data collection operations for this
                 entry are stopped, the current VFile is frozen and it's
                 transfer is initiated. 
                
                Modifying the value of cdcVFileAdminStatus to 'disabled' does
                not remove or change the current configuration as represented
                by the active rows in this table.
                ''',
                'cdcvfileadminstatus',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileCollectionErrorEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to 'true', cdcVFileCollectionError notification will
                be sent out in the event of a data collection error.
                ''',
                'cdcvfilecollectionerrorenable',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileCollectionPeriod', ATTRIBUTE, 'int' , None, None, 
                [('60', '604800')], [], 
                '''                Specifies the period of a collection interval. The value
                of this object is used only when the data collection mode is
                 automatic (see cdcVFileCollectMode).
                
                A periodic timer (one per entry) is started when this
                entry is 'activated'. The time at which this entry is
                'activated' is called the 'activation time' for this entry,
                and is internally maintained by the agent.
                
                When this periodic timer expires, the current VFile is
                frozen and a new VFile is created for data collection. 
                Transfer is then initiated for the frozen VFile.  
                In addition, the internally maintained counter for counting
                the number of consecutive times the size of a VFile has
                exceeded the maximum limit, is reset to zero. (See
                cdcVFileMaxSize) 
                
                This object's value may be modified at any time, and the
                 new value takes effect immediately. i.e setting a new
                 value can cause the current collection interval to terminate
                 and a new collection interval to start.
                ''',
                'cdcvfilecollectionperiod',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileCollectMode', REFERENCE_ENUM_CLASS, 'CdcvfilecollectmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcvfiletable.Cdcvfileentry.CdcvfilecollectmodeEnum', 
                [], [], 
                '''                Determines the mode of data collection.
                
                'auto'         Data is periodically fetched for all data
                               groups associated with this entry. This is
                               done at data group specific periodic intervals
                               (cdcDGPollPeriod).
                               The data thus collected, is formatted and
                               stored into the current VFile.  
                               In addition at regular intervals (see
                               cdcVFileCollectPeriod) a new VFile 
                               is created to store data, and the current
                               VFile is frozen and transferred.
                
                'manual'       Data for all data groups is fetched and
                               collected into the current VFile only when 
                               cdcVFileCommand is set to 'collectNow'. 
                
                This object's value cannot be modified while the entry
                is in the 'activated' state.
                ''',
                'cdcvfilecollectmode',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileCommand', REFERENCE_ENUM_CLASS, 'CdcvfilecommandEnum' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcvfiletable.Cdcvfileentry.CdcvfilecommandEnum', 
                [], [], 
                '''                An object for controlling collection of data.
                
                'idle'            Indicates that no command is in progress.
                
                'swapToNewFile'   When written, the current VFile is frozen,
                                  and a new VFile is created for collecting
                                  data.
                		   If the data collection mode is automatic
                                  (see cdcVFileCollectMode), then the current 
                                  collection interval is stopped and a new
                                  collection interval is started 
                		   (see cdcVFileCollectPeriod).  
                                  
                'collectNow'      When written, base object values for
                                  all associated data groups are fetched 
                                  and stored into the current VFile. This
                                  value can only be written when the
                                  collection mode is 'manual' (see 
                                  cdcVFileCollectMode).
                ''',
                'cdcvfilecommand',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileCurrentSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The size of the current VFile.
                ''',
                'cdcvfilecurrentsize',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileDescription', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A string that can be used for administrative purposes. 
                This object's value may be modified at any time.
                ''',
                'cdcvfiledescription',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileErrorCode', REFERENCE_ENUM_CLASS, 'CdcvfileerrorcodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcvfiletable.Cdcvfileentry.CdcvfileerrorcodeEnum', 
                [], [], 
                '''                A value indicating the type of error that has occurred during
                data collection operations for this entry.
                
                noError                The value is 'noError' when
                                       the corresponding value of
                                       cdcVFileOperStatus is not 'error'.
                
                otherError             Any error other than one of the 
                                       following listed errors.
                
                noSpace                There is no space left to write into
                                       the current VFile. 
                
                openError              Could not open VFile for writing. One
                                       possible reason could be the existence
                                       of another file by the same name in
                                       the agent's filesystem. 
                
                tooSmallMaxSize        Indicates that cdcVFileMaxSize is 
                                       too small for data collection. The 
                                       cdcVFileMaxSize configured for this
                                       VFile is not sufficient even to hold 
                                       the data collected in one poll.
                
                tooManyMaxSizeHits     Indicates that data collection
                                       operations are stopped because
                                       the value of cdcVFileMaxSizeHitsLimit
                                       has been exceeded. 
                
                noResource             Some kind of resource was unavailable
                                       while collecting data. For
                                       e.g. unavailability of dynamic memory.
                ''',
                'cdcvfileerrorcode',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileFormat', REFERENCE_ENUM_CLASS, 'CdcfileformatEnum' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CdcfileformatEnum', 
                [], [], 
                '''                The format in which data is stored into the current VFile.
                
                This object's value cannot be modified while the entry
                is in the 'activated' state.
                ''',
                'cdcvfileformat',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileMaxSize', ATTRIBUTE, 'int' , None, None, 
                [('512', '4294967295')], [], 
                '''                The maximum size of a VFile. 
                
                The agent maintains an internal counter for each
                cdcVFileEntry. This counter counts the number of consecutive
                times the size of a VFile has exceeded the value of this
                object. When the value of this counter exceeds the value of
                cdcVFileMaxSizeHitsLimit, this entry is moved to the 'error'
                state (see cdcVFileOperStatus).
                However if the value of cdcVFileMaxSizeHitsLimit is not
                exceeded, then the current VFile is frozen, and a new VFile
                is created for data collection.
                
                If the data collection mode is automatic (see
                cdcVFileCollectMode), then the current collection interval is
                stopped and a new collection interval is started.
                
                This object's value may be modified at any time. The new
                size limit MUST be checked against the size of the current
                VFile at the time of modification, and appropriate action
                taken.
                ''',
                'cdcvfilemaxsize',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileName', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The base-name of the VFiles (created by data collection
                operations corresponding to this entry) into which data is to
                be collected. 
                
                When a VFile is created, it's full name is obtained by the
                concatentation of a suffix to this value. The suffix will be
                chosen by the agent such that the VFiles created for this
                entry have unique names. For e.g. the suffix could be a
                string representation of the date and time when the VFile was
                created. 
                
                If VFiles are to be placed in the agent's local filesystem
                (provided the agent supports it) then this value should also
                contain the absolute path of the location as a prefix to the
                base name.
                
                An agent will respond with inconsistentValue to
                a management set operation which attempts to modify the value
                of this object to the same value as already held by another
                instance of cdcVFileName, or wrongValue if the new value 
                is invalid for use as a file name on the local file 
                system (e.g., many file systems do not support white 
                space embedded in file names).
                
                This object's value may be modified at any time. However
                the new name will be used only when the next VFile is
                created for this entry.
                ''',
                'cdcvfilename',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileOperStatus', REFERENCE_ENUM_CLASS, 'CdcvfileoperstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcvfiletable.Cdcvfileentry.CdcvfileoperstatusEnum', 
                [], [], 
                '''                A status object to indicate the operational state of
                collection for this entry.
                
                When the value of cdcVFileAdminStatus is modified to be
                'enabled', the value of this object will change to 'enabled'
                providing it is possible to begin collecting data. If at any
                point of time data cannot be collected because of some error,
                then the value of this object is changed to 'error' and all
                collection operations stop, as if cdcVFileAdminStatus has
                been set to 'disabled'. More information about the nature of
                the error can be obtained by retrieving the value of
                cdcVFileErrorCode. 
                
                When the value of cdcVFileAdminStatus is modified to be
                'disabled', the value of this object will change to
                'disabled' and data collection operations are stopped for
                this entry.
                ''',
                'cdcvfileoperstatus',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileRetentionPeriod', ATTRIBUTE, 'int' , None, None, 
                [('60', '86400')], [], 
                '''                The time for which a frozen VFile is retained by the
                agent. When a VFile is frozen, a timer (one per frozen VFile)
                is started to keep track of the retention period for the
                 VFile. Once this timer expires, the VFile is deleted.
                Till the expiry of the retention period, information 
                about frozen VFiles is maintained in 
                cdcVFileMgmtTable.
                
                This object's value may be modified at any time, however
                the new value will take effect only for new frozen VFiles.
                ''',
                'cdcvfileretentionperiod',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. 
                A valid cdcVFileName is only mandatory object for setting
                this object to 'active'. But collection of data in to active
                vfile starts only on setting cdcVFileAdminStatus 
                to 'enabled'.
                Setting this object to 'destroy' stops all data collection
                operations for this entry, deletes all VFiles and removes
                this entry from cdcVFileTable.
                ''',
                'cdcvfilerowstatus',
                'CISCO-DATA-COLLECTION-MIB', False),
            ],
            'CISCO-DATA-COLLECTION-MIB',
            'cdcVFileEntry',
            _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB'
        ),
    },
    'CiscoDataCollectionMib.Cdcvfiletable' : {
        'meta_info' : _MetaInfoClass('CiscoDataCollectionMib.Cdcvfiletable',
            False, 
            [
            _MetaInfoClassMember('cdcVFileEntry', REFERENCE_LIST, 'Cdcvfileentry' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcvfiletable.Cdcvfileentry', 
                [], [], 
                '''                An entry in the cdcVFileTable. Each entry contains
                application specified configuration that is used to create
                 virtual files (VFile) and start data collection operations.
                
                 A VFile is used to store data (values of base object
                instances) as selected by entities called data groups.
                A data group is defined in cdcDGTable. 
                
                An entry in this table is said to be 'activated' when the
                corresponding instances of cdcVFileRowStatus is 'active' AND
                cdcVFileOperStatus is 'enabled'. The value of sysUpTime.0 when
                the condition evaluates to 'true' is called the activation
                time of the entry. The activation time for each entry is
                maintained internally by the agent.
                ''',
                'cdcvfileentry',
                'CISCO-DATA-COLLECTION-MIB', False),
            ],
            'CISCO-DATA-COLLECTION-MIB',
            'cdcVFileTable',
            _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB'
        ),
    },
    'CiscoDataCollectionMib.Cdcvfilemgmttable.Cdcvfilemgmtentry.CdcvfilemgmtcommandEnum' : _MetaInfoEnum('CdcvfilemgmtcommandEnum', 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB',
        {
            'idle':'idle',
            'delete':'delete',
            'transfer':'transfer',
            'abortTransfer':'abortTransfer',
        }, 'CISCO-DATA-COLLECTION-MIB', _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB']),
    'CiscoDataCollectionMib.Cdcvfilemgmttable.Cdcvfilemgmtentry' : {
        'meta_info' : _MetaInfoClass('CiscoDataCollectionMib.Cdcvfilemgmttable.Cdcvfilemgmtentry',
            False, 
            [
            _MetaInfoClassMember('cdcVFileIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'cdcvfileindex',
                'CISCO-DATA-COLLECTION-MIB', True),
            _MetaInfoClassMember('cdcVFileMgmtIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This value is a running counter starting at 1,
                generated by the agent so that the combination of 
                cdcVFileIndex and cdcVFileMgmtIndex uniquely
                identifies a frozen VFile. The deleted file indicies
                do not get reused.
                
                This object's value needs to be unique only across the
                set of frozen VFiles corresponding to a cdcVFileEntry
                (identified by cdcVFileIndex).
                ''',
                'cdcvfilemgmtindex',
                'CISCO-DATA-COLLECTION-MIB', True),
            _MetaInfoClassMember('cdcVFileMgmtCommand', REFERENCE_ENUM_CLASS, 'CdcvfilemgmtcommandEnum' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcvfilemgmttable.Cdcvfilemgmtentry.CdcvfilemgmtcommandEnum', 
                [], [], 
                '''                A control to manage VFiles. 
                
                idle           This value can be only be read. It indicates
                               that no management action is currently being
                               performed on this VFile.
                
                delete         This value is only written, and is used to
                               delete the frozen VFile. Writing this value
                               will cause this entry to be removed from this
                               table. 
                
                transfer       This value can be both read and written.
                               When read it means that the VFile is in the
                               process of being transferred. When written, it
                               initiates a transfer for the VFile.
                
                abortTransfer  This value can only be written, and is used
                               to abort an ongoing transfer.
                ''',
                'cdcvfilemgmtcommand',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileMgmtLastXferStatus', REFERENCE_ENUM_CLASS, 'CdcfilexferstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CdcfilexferstatusEnum', 
                [], [], 
                '''                Indicates the status of the last completed transfer.
                ''',
                'cdcvfilemgmtlastxferstatus',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileMgmtLastXferURL', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Indicates the URL of the destination to which the last
                (completed) transfer was initiated.
                ''',
                'cdcvfilemgmtlastxferurl',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileMgmtName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The full name of the VFile. If the VFile is stored as a file
                in the agent's filesystem, then this value also contains the
                absolute path of the file.
                ''',
                'cdcvfilemgmtname',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileMgmtTimestamp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The timestamp when this VFile was created, in the date-time
                format.
                ''',
                'cdcvfilemgmttimestamp',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileMgmtTimeToLive', ATTRIBUTE, 'int' , None, None, 
                [('60', '86400')], [], 
                '''                The time left before this VFile is deleted (see
                cdcVFileRetentionPeriod).
                ''',
                'cdcvfilemgmttimetolive',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileMgmtXferURL', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The complete URL of the destination to which this VFile will
                be transferred in the next attempt. The URL also includes the
                complete filename of the remote file that will be
                created. When the default value of this object is 
                retained this VFile will be transferred to the URL  
                specified in cdcFileXferConfPriUrl or cdcFileXferConfSecUrl,
                as the case may be.
                
                 However an application can specify a different URL, in which
                case the VFile will be transferred to this new URL the next
                time transfer is initiated. 
                
                This object's value may be modified at any time.
                ''',
                'cdcvfilemgmtxferurl',
                'CISCO-DATA-COLLECTION-MIB', False),
            ],
            'CISCO-DATA-COLLECTION-MIB',
            'cdcVFileMgmtEntry',
            _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB'
        ),
    },
    'CiscoDataCollectionMib.Cdcvfilemgmttable' : {
        'meta_info' : _MetaInfoClass('CiscoDataCollectionMib.Cdcvfilemgmttable',
            False, 
            [
            _MetaInfoClassMember('cdcVFileMgmtEntry', REFERENCE_LIST, 'Cdcvfilemgmtentry' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcvfilemgmttable.Cdcvfilemgmtentry', 
                [], [], 
                '''                An entry in cdcVFileMgmtTable. Each entry corresponds to a
                frozen VFile. An entry is created in this table, whenever a
                VFile is frozen. An entry is removed from this table whenever
                a frozen VFile is deleted either because the retention period
                elapsed or because it was adminstratively deleted.
                
                If the configuration specified in cdcVFileEntry is persisted
                across system/agent restarts AND the VFiles created as a
                result of that configuration are persisted across restarts,
                then this table must be populated with entries corresponding
                to those persisted VFiles. However any state related to an
                entry, like time to live etc. need not be maintained
                across restarts.
                ''',
                'cdcvfilemgmtentry',
                'CISCO-DATA-COLLECTION-MIB', False),
            ],
            'CISCO-DATA-COLLECTION-MIB',
            'cdcVFileMgmtTable',
            _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB'
        ),
    },
    'CiscoDataCollectionMib.Cdcdgtable.Cdcdgentry.CdcdgtypeEnum' : _MetaInfoEnum('CdcdgtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB',
        {
            'object':'object',
            'table':'table',
        }, 'CISCO-DATA-COLLECTION-MIB', _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB']),
    'CiscoDataCollectionMib.Cdcdgtable.Cdcdgentry' : {
        'meta_info' : _MetaInfoClass('CiscoDataCollectionMib.Cdcdgtable.Cdcdgentry',
            False, 
            [
            _MetaInfoClassMember('cdcDGIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An arbitrary integer used to uniquely identify this entry.
                When creating an entry, a management application should pick a
                random number.
                ''',
                'cdcdgindex',
                'CISCO-DATA-COLLECTION-MIB', True),
            _MetaInfoClassMember('cdcDGComment', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A descriptive string. This object's value may be modified at
                any time.
                ''',
                'cdcdgcomment',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGContextName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The management context from which to obtain data for this
                data group.
                
                This object's value may be modified at any time. The change
                takes effect the next time data is fetched for this data
                group.
                ''',
                'cdcdgcontextname',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGInstGrpIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Corresponds to a value of cdcDGInstanceGrpIndex, thus
                identifying a set of entries in cdcDGInstanceTable, having
                this value of cdcDGInstanceGrpIndex. This object's value is
                used only when cdcDGType is of type 'table'. 
                
                The set of entries in cdcDGInstanceTable, in turn identifies
                the set of instances of the base objects, whose values need
                to fetched. If the value is 0, then all instances of the base
                objects will be fetched.
                 
                 This object's value may be modified at any time. The change
                takes effect the next time data is fetched for this data
                group.
                ''',
                'cdcdginstgrpindex',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGObject', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The fully instantiated name of the MIB object whose value
                needs to be fetched. This object's value is used only when
                cdcDGType is of type 'object'. 
                
                This object's value may be modified at any time. The change
                takes effect the next time data is fetched for this data
                group.
                ''',
                'cdcdgobject',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGObjectGrpIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Corresponds to a value of cdcDGBaseObjectGrpIndex, thus
                identifying a set of entries in cdcDGBaseObjectTable, having
                this value of cdcDGBaseObjectGrpIndex. This object's value is
                used only when cdcDGType is of type 'table'. 
                
                This set of entries in cdcDGBaseObjectTable in turn
                 identifies the set of base objects, that makes up the columns
                 of this 'table' type data group.   
                
                This object's value may be modified at any time. The change
                takes effect the next time data is fetched for this data
                group.
                ''',
                'cdcdgobjectgrpindex',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGPollPeriod', ATTRIBUTE, 'int' , None, None, 
                [('1', '86400')], [], 
                '''                Specifies the time intervals at which the data should be
                fetched for this data group.
                This object's value is used only when the collection
                mode of the associated cdcVFileEntry is automatic (see
                cdcVFileCollectMode). 
                
                A periodic timer is started for this data group when
                cdcDGRowStatus is set to 'active', provided the associated
                cdcVFileEntry has already been 'activated', otherwise it is
                started when the associated cdcVFileEntry is finally
                activated. 
                
                The time interval after which the first expiration of this
                timer should occur, is calculated as follows:
                
                (value of sysUpTime.0) + 
                (value of cdcPollPeriod for this entry - 
                   (value of sysUpTime.0 - VFile activation time for the
                    associated cdcVFileEntry) % cdcPollPeriod)
                
                Subsequent expirations of the periodic timer can occur as per
                the value specified in cdcDGPollPeriod. This helps in
                synchronizing periodic polling of the data groups with
                respect to the VFile activation time.
                
                This object's value may be modified at any time, and the
                change must take effect immediately. i.e. if the periodic
                timer has been started, it's expiry time may need to be
                re-adjusted.
                ''',
                'cdcdgpollperiod',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row.
                
                This object cannot be set to 'active' until values have been
                assigned to  cdcDGVFileIndex & cdcDGColGrpIndex.
                ''',
                'cdcdgrowstatus',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGTargetTag', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The tag for the target from which to obtain the data for
                this data group.
                
                A length of 0 indicates the local system.  In this case,
                access to the objects of this data group is under
                the security credentials of the requester that set
                cdcDGRowStatus to 'active'. Those credentials are
                the input parameters for isAccessAllowed from the
                Architecture for Describing SNMP Management Frameworks.
                
                Otherwise a search is carried out for an entry in the
                snmpTargetAddrTable whose snmpTargetAddrTagList contains the
                tag specified by the value of this object. The security
                credentials (snmpTargetParamsEntry) of the first entry that
                satisfies the above criteria, are passed as input parameters
                for isAccessAllowed. 
                
                This object's value may be modified at any time. The change
                takes effect the next time data is fetched for this data
                group.
                ''',
                'cdcdgtargettag',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGType', REFERENCE_ENUM_CLASS, 'CdcdgtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcdgtable.Cdcdgentry.CdcdgtypeEnum', 
                [], [], 
                '''                Identifies the type of this data group.
                object         Data is a single MIB object. The fully
                               instantiated OID is specified in
                               cdcDGBaseObject.
                
                table          Data is a logical table. The columns of
                               this table correspond to the base objects
                               specified in cdcDGBaseObjectTable, and the
                               rows correspond to the values of the instances
                               specified in cdcDGInstanceTable.
                
                This object's value cannot be modified while the value of
                cdcDGRowStatus is 'active'.
                ''',
                'cdcdgtype',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGVFileIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Corresponds to a value of cdcVFileIndex.
                It is used to associate this data group with a
                cdcVFileEntry. The values of the base objects for 
                this data group are stored into the current VFile of the
                associated cdcVFileEntry. 
                
                This object's value may be modified at any time. The change
                takes effect the next time data is fetched for this data
                group.
                ''',
                'cdcdgvfileindex',
                'CISCO-DATA-COLLECTION-MIB', False),
            ],
            'CISCO-DATA-COLLECTION-MIB',
            'cdcDGEntry',
            _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB'
        ),
    },
    'CiscoDataCollectionMib.Cdcdgtable' : {
        'meta_info' : _MetaInfoClass('CiscoDataCollectionMib.Cdcdgtable',
            False, 
            [
            _MetaInfoClassMember('cdcDGEntry', REFERENCE_LIST, 'Cdcdgentry' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcdgtable.Cdcdgentry', 
                [], [], 
                '''                An entry in this table. Each entry corresponds to a data
                group. A data group is used to select data that needs to be
                collected into VFiles. The selection is done by specifying
                the base objects and their instances for which the values
                need to be fetched.
                
                Data is collected only for those data groups, that have
                the corresponding instance of cdcDGRowStatus set to
                'active'. 
                
                In order for data to be collected, each data group has to
                be associated with a cdcVFileEntry (see cdcDGVFileIndex). If
                the data collection mode of the associated cdcVFileEntry is
                automatic, then data is fetched and stored into the current
                VFile of the associated cdcVFileEntry at periodic
                intervals (cdcDGPollPeriod).
                ''',
                'cdcdgentry',
                'CISCO-DATA-COLLECTION-MIB', False),
            ],
            'CISCO-DATA-COLLECTION-MIB',
            'cdcDGTable',
            _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB'
        ),
    },
    'CiscoDataCollectionMib.Cdcdgbaseobjecttable.Cdcdgbaseobjectentry' : {
        'meta_info' : _MetaInfoClass('CiscoDataCollectionMib.Cdcdgbaseobjecttable.Cdcdgbaseobjectentry',
            False, 
            [
            _MetaInfoClassMember('cdcDGBaseObjectGrpIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object's value when combined with the value of
                cdcDGBaseObjectIndex uniquely identifies an entry in
                this table. An application must use the same value (can
                 be randomly picked) for this object while creating a group of
                entries that collectively identifies the set of base
                objects for a data group.
                ''',
                'cdcdgbaseobjectgrpindex',
                'CISCO-DATA-COLLECTION-MIB', True),
            _MetaInfoClassMember('cdcDGBaseObjectIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object's value when combined with the value of
                cdcDGBaseObjectGrpIndex uniquely identifies an entry in
                this table.
                
                A managment application can assign incremental values
                starting from one, when creating each entry in a group of
                entries (as identified by the value of
                cdcDGBaseObjectGrpIndex).
                ''',
                'cdcdgbaseobjectindex',
                'CISCO-DATA-COLLECTION-MIB', True),
            _MetaInfoClassMember('cdcDGBaseObjectList', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                The list component of a {subtree, list} tuple.
                
                This object's value may be modified at any time. The change
                takes effect the next time data is fetched for this data
                group.
                ''',
                'cdcdgbaseobjectlist',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGBaseObjectRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row.
                
                This object cannot be set to 'active' until values have been
                assigned to cdcDGBaseObjectSubtree & cdcDGBaseObjectList.
                ''',
                'cdcdgbaseobjectrowstatus',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGBaseObjectSubtree', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The subtree component of a {subtree, list} tuple.
                
                This object's value may be modified at any time. The change
                takes effect the next time data is fetched for this data
                group.
                ''',
                'cdcdgbaseobjectsubtree',
                'CISCO-DATA-COLLECTION-MIB', False),
            ],
            'CISCO-DATA-COLLECTION-MIB',
            'cdcDGBaseObjectEntry',
            _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB'
        ),
    },
    'CiscoDataCollectionMib.Cdcdgbaseobjecttable' : {
        'meta_info' : _MetaInfoClass('CiscoDataCollectionMib.Cdcdgbaseobjecttable',
            False, 
            [
            _MetaInfoClassMember('cdcDGBaseObjectEntry', REFERENCE_LIST, 'Cdcdgbaseobjectentry' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcdgbaseobjecttable.Cdcdgbaseobjectentry', 
                [], [], 
                '''                An individual entry in this table. Each entry is a 
                {subtree, list} tuple. Each tuple identifies a set of 
                base objects for the associated data group.
                ''',
                'cdcdgbaseobjectentry',
                'CISCO-DATA-COLLECTION-MIB', False),
            ],
            'CISCO-DATA-COLLECTION-MIB',
            'cdcDGBaseObjectTable',
            _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB'
        ),
    },
    'CiscoDataCollectionMib.Cdcdginstancetable.Cdcdginstanceentry.CdcdginstancetypeEnum' : _MetaInfoEnum('CdcdginstancetypeEnum', 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB',
        {
            'individual':'individual',
            'range':'range',
            'repititions':'repititions',
            'subTree':'subTree',
            'other':'other',
        }, 'CISCO-DATA-COLLECTION-MIB', _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB']),
    'CiscoDataCollectionMib.Cdcdginstancetable.Cdcdginstanceentry' : {
        'meta_info' : _MetaInfoClass('CiscoDataCollectionMib.Cdcdginstancetable.Cdcdginstanceentry',
            False, 
            [
            _MetaInfoClassMember('cdcDGInstanceGrpIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object's value when combined with the value of
                cdcDGInstanceIndex uniquely identifies an entry in
                this table. An application must use the same value (can
                 be randomly picked) for this object while creating a group of
                entries that collectively identifies the set of instances for a
                data group.
                ''',
                'cdcdginstancegrpindex',
                'CISCO-DATA-COLLECTION-MIB', True),
            _MetaInfoClassMember('cdcDGInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object's value when combined with the value of
                cdcDGInstanceGrpIndex uniquely identifies an entry in
                this table.
                
                A managment application can assign incremental values
                starting from one, when creating each entry within a group
                of entries (as identified by the value of
                cdcDGInstanceGrpIndex).
                ''',
                'cdcdginstanceindex',
                'CISCO-DATA-COLLECTION-MIB', True),
            _MetaInfoClassMember('cdcDGInstanceNumRepititions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Specifies the number of lexicographically consecutive object
                instances to fetch. 
                This value is used only when the value of cdcDGInstanceType
                is of type 'repititions'.  
                
                This object's value may be modified at any time. The change
                takes effect the next time data is fetched for this data
                group.
                ''',
                'cdcdginstancenumrepititions',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGInstanceOid', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                Contains the OBJECT IDENTIFIER fragment that identifies the
                instances of the base objects that need to be collected.
                
                If cdcDGInstanceType is 'individual' then this value
                should be the OID fragment that, when appended to each base
                MIB object gives the fully instantiated OID to be fetched.
                
                If cdcDGInstanceType is 'range' then this value
                should be the OID fragment that, when appended to each base
                MIB object gives the start of a range of object instances
                that needs to be fetched.
                
                If cdcDGInstanceType is 'subTree' then this value
                should be the OID fragment that, when appended to each base
                MIB gives the sub-tree under which all leaf object instances
                need to be fetched.
                
                This object's value may be modified at any time. The change
                takes effect the next time data is fetched for this data
                group.
                ''',
                'cdcdginstanceoid',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGInstanceOidEnd', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                Contains the OID fragment that, when appended to each base
                object gives the end of the range of object instances that
                needs to be fetched. 
                This value is used only when the value of cdcDGInstanceType
                is of type 'range'. 
                
                This object's value may be modified at any time. The change
                takes effect the next time data is fetched for this data
                group.
                ''',
                'cdcdginstanceoidend',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGInstanceOtherPtr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                Contains a pointer to a row in another MIB table that
                contains MIB specific criteria for selecting instances. 
                This value is used only when the value of cdcDGInstanceType
                is of type 'other'. 
                
                This object's value may be modified at any time. The change
                takes effect the next time data is fetched for this data
                group.
                ''',
                'cdcdginstanceotherptr',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGInstanceRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row.
                ''',
                'cdcdginstancerowstatus',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGInstanceType', REFERENCE_ENUM_CLASS, 'CdcdginstancetypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcdginstancetable.Cdcdginstanceentry.CdcdginstancetypeEnum', 
                [], [], 
                '''                Specifies the way in which the instances are to be used while
                collecting data.
                
                
                individual     The value of cdcDGInstanceOid is
                               appended to each base object of the
                               associated data group, thus giving the exact
                               instance of the objects to be collected.
                
                range          The value of cdcDGInstanceOid is
                               appended to each base object in the
                               associated data group, thus giving the
                               starting object instance of the range.
                               The value of cdcDGInstanceEndOid
                               is appended to to each base object in the
                               associated data group, thus giving the
                               last object instances of the range. 
                
                repititions      The value of cdcDGInstanceOid is
                               appended to each base object in the
                               associated data group, thus giving the
                               first object instance of the next 'n'
                               instances that need to be collected.
                               The value of 'n' is set in
                               cdcDGInstanceNumRepititions.
                
                subTree        The value of cdcDGInstanceOid is
                               appended to each base object in the
                               associated data group, thus identifying the
                               OBJECT IDENTFIFIER sub-tree, whose leaf
                               instances need to be collected.
                
                other          The value of cdcDGInstanceOtherPtr points to a
                               row (in another MIB table) that contains MIB
                               specific instance selection criteria. A MIB
                               defined for such purposes should describe
                               the selection criteria.
                
                This object's value cannot be modified while the value of
                cdcDGInstanceStatus is 'active'.
                ''',
                'cdcdginstancetype',
                'CISCO-DATA-COLLECTION-MIB', False),
            ],
            'CISCO-DATA-COLLECTION-MIB',
            'cdcDGInstanceEntry',
            _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB'
        ),
    },
    'CiscoDataCollectionMib.Cdcdginstancetable' : {
        'meta_info' : _MetaInfoClass('CiscoDataCollectionMib.Cdcdginstancetable',
            False, 
            [
            _MetaInfoClassMember('cdcDGInstanceEntry', REFERENCE_LIST, 'Cdcdginstanceentry' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcdginstancetable.Cdcdginstanceentry', 
                [], [], 
                '''                An entry in this table. Each entry identifies one or more
                instances of the base objects that need to be fetched.
                An instance is represented by an OID fragment.
                ''',
                'cdcdginstanceentry',
                'CISCO-DATA-COLLECTION-MIB', False),
            ],
            'CISCO-DATA-COLLECTION-MIB',
            'cdcDGInstanceTable',
            _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB'
        ),
    },
    'CiscoDataCollectionMib.Cdcfilexferconftable.Cdcfilexferconfentry' : {
        'meta_info' : _MetaInfoClass('CiscoDataCollectionMib.Cdcfilexferconftable.Cdcfilexferconfentry',
            False, 
            [
            _MetaInfoClassMember('cdcVFileIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'cdcvfileindex',
                'CISCO-DATA-COLLECTION-MIB', True),
            _MetaInfoClassMember('cdcFileXferConfFailureEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to 'true', cdcFileXferComplete notification will
                be sent out in the event of a file transfer failure.
                ''',
                'cdcfilexferconffailureenable',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcFileXferConfPriUrl', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The URL which specifies the primary destination to which
                the file has to be transferred. The URL should contain the
                base-name of the remote file, the suffix will be carried over
                from the name of the VFile being tranferred, and will be
                automatically appended by the agent.
                
                This object's value may be modified at any time.
                ''',
                'cdcfilexferconfpriurl',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcFileXferConfRetryCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '256')], [], 
                '''                Maximum number of times, transfer has to be retried. If the
                retry count exceeds this value, then no further attempts will
                be made.
                
                 This object's value may be modified at any time.
                ''',
                'cdcfilexferconfretrycount',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcFileXferConfRetryPeriod', ATTRIBUTE, 'int' , None, None, 
                [('60', '86400')], [], 
                '''                Specifies the time interval after which transfer has to be
                retried. Transfer needs to be retried only if in a previous
                 attempt the file could not be successfully transferred to
                 either the primary destination or the secondary destination.
                
                This object's value may be modified at any time.
                ''',
                'cdcfilexferconfretryperiod',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcFileXferConfSecUrl', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The URL which specifies the secondary destination to which
                the file has to be transferred if the transfer to the 
                primary destination fails. Failure occurs when the file
                 cannot be transferred in it's entirety to the specified
                 destination for some reason. Some common reasons for such
                 failures are listed out in CdcFileXferStatus. 
                
                 The specified URL should contain the base-name of the remote
                file, the suffix will be carried over from the name of the
                VFile being tranferred, and will be automatically appended by
                the agent. 
                
                This object's value may be modified at any time.
                ''',
                'cdcfilexferconfsecurl',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcFileXferConfSuccessEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set to 'true', cdcFileXferComplete notification will
                be sent out in the event of a successful file transfer.
                ''',
                'cdcfilexferconfsuccessenable',
                'CISCO-DATA-COLLECTION-MIB', False),
            ],
            'CISCO-DATA-COLLECTION-MIB',
            'cdcFileXferConfEntry',
            _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB'
        ),
    },
    'CiscoDataCollectionMib.Cdcfilexferconftable' : {
        'meta_info' : _MetaInfoClass('CiscoDataCollectionMib.Cdcfilexferconftable',
            False, 
            [
            _MetaInfoClassMember('cdcFileXferConfEntry', REFERENCE_LIST, 'Cdcfilexferconfentry' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcfilexferconftable.Cdcfilexferconfentry', 
                [], [], 
                '''                An individual entry in the cdcFileXferConfTable. Each entry
                identifies a primary and an optional secondary destination.
                
                An entry is automatically created in this table, whenever an
                entry is created in the cdcVFileTable. The application needs
                to specify the URLs of the destination to which frozen VFiles
                are transferred. 
                
                When a VFile is frozen, transfer will be first initiated to
                the primary destination, if the transfer fails, then transfer
                is initiated to the secondary destination. If this too fails,
                then the cycle is repeated again after a specified time
                period (value of cdcFileXferConfRetryPeriod) elapses.
                ''',
                'cdcfilexferconfentry',
                'CISCO-DATA-COLLECTION-MIB', False),
            ],
            'CISCO-DATA-COLLECTION-MIB',
            'cdcFileXferConfTable',
            _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB'
        ),
    },
    'CiscoDataCollectionMib' : {
        'meta_info' : _MetaInfoClass('CiscoDataCollectionMib',
            False, 
            [
            _MetaInfoClassMember('cdcDGBaseObjectTable', REFERENCE_CLASS, 'Cdcdgbaseobjecttable' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcdgbaseobjecttable', 
                [], [], 
                '''                A table specifying the base objects of a 'table' type
                data group.
                ''',
                'cdcdgbaseobjecttable',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGInstanceTable', REFERENCE_CLASS, 'Cdcdginstancetable' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcdginstancetable', 
                [], [], 
                '''                Identifies the instances of the base objects that need to
                be fetched for a 'table' type data group.
                
                The agent is not responsible for verifying that the instances
                specified for a data group do not overlap.
                ''',
                'cdcdginstancetable',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcDGTable', REFERENCE_CLASS, 'Cdcdgtable' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcdgtable', 
                [], [], 
                '''                A table for specifying data groups.
                ''',
                'cdcdgtable',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcFileXferConfTable', REFERENCE_CLASS, 'Cdcfilexferconftable' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcfilexferconftable', 
                [], [], 
                '''                A table for configuring file transfer operations.
                ''',
                'cdcfilexferconftable',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFile', REFERENCE_CLASS, 'Cdcvfile' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcvfile', 
                [], [], 
                '''                ''',
                'cdcvfile',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileMgmtTable', REFERENCE_CLASS, 'Cdcvfilemgmttable' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcvfilemgmttable', 
                [], [], 
                '''                A table to manage frozen VFiles.
                ''',
                'cdcvfilemgmttable',
                'CISCO-DATA-COLLECTION-MIB', False),
            _MetaInfoClassMember('cdcVFileTable', REFERENCE_CLASS, 'Cdcvfiletable' , 'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CiscoDataCollectionMib.Cdcvfiletable', 
                [], [], 
                '''                A table for setting up VFiles for collecting data.
                ''',
                'cdcvfiletable',
                'CISCO-DATA-COLLECTION-MIB', False),
            ],
            'CISCO-DATA-COLLECTION-MIB',
            'CISCO-DATA-COLLECTION-MIB',
            _yang_ns._namespaces['CISCO-DATA-COLLECTION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB'
        ),
    },
}
_meta_table['CiscoDataCollectionMib.Cdcvfiletable.Cdcvfileentry']['meta_info'].parent =_meta_table['CiscoDataCollectionMib.Cdcvfiletable']['meta_info']
_meta_table['CiscoDataCollectionMib.Cdcvfilemgmttable.Cdcvfilemgmtentry']['meta_info'].parent =_meta_table['CiscoDataCollectionMib.Cdcvfilemgmttable']['meta_info']
_meta_table['CiscoDataCollectionMib.Cdcdgtable.Cdcdgentry']['meta_info'].parent =_meta_table['CiscoDataCollectionMib.Cdcdgtable']['meta_info']
_meta_table['CiscoDataCollectionMib.Cdcdgbaseobjecttable.Cdcdgbaseobjectentry']['meta_info'].parent =_meta_table['CiscoDataCollectionMib.Cdcdgbaseobjecttable']['meta_info']
_meta_table['CiscoDataCollectionMib.Cdcdginstancetable.Cdcdginstanceentry']['meta_info'].parent =_meta_table['CiscoDataCollectionMib.Cdcdginstancetable']['meta_info']
_meta_table['CiscoDataCollectionMib.Cdcfilexferconftable.Cdcfilexferconfentry']['meta_info'].parent =_meta_table['CiscoDataCollectionMib.Cdcfilexferconftable']['meta_info']
_meta_table['CiscoDataCollectionMib.Cdcvfile']['meta_info'].parent =_meta_table['CiscoDataCollectionMib']['meta_info']
_meta_table['CiscoDataCollectionMib.Cdcvfiletable']['meta_info'].parent =_meta_table['CiscoDataCollectionMib']['meta_info']
_meta_table['CiscoDataCollectionMib.Cdcvfilemgmttable']['meta_info'].parent =_meta_table['CiscoDataCollectionMib']['meta_info']
_meta_table['CiscoDataCollectionMib.Cdcdgtable']['meta_info'].parent =_meta_table['CiscoDataCollectionMib']['meta_info']
_meta_table['CiscoDataCollectionMib.Cdcdgbaseobjecttable']['meta_info'].parent =_meta_table['CiscoDataCollectionMib']['meta_info']
_meta_table['CiscoDataCollectionMib.Cdcdginstancetable']['meta_info'].parent =_meta_table['CiscoDataCollectionMib']['meta_info']
_meta_table['CiscoDataCollectionMib.Cdcfilexferconftable']['meta_info'].parent =_meta_table['CiscoDataCollectionMib']['meta_info']
