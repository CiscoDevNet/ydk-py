""" CISCO_DATA_COLLECTION_MIB 

The MIB module allows a management application to
select a set of MIB object instances whose values need 
to be collected on a periodic basis. The term 'data' in 
the context of this MIB is used to generically refer to 
the values of the selected set of object instances. 

Once the required setup is done, the MIB implementation 
carries out the following periodic tasks\:
  \- collects the required object values into local
    file\-like entities called VFiles (virtual files).
  \- transfers the VFiles to specified locations.
  \- carries out VFile management operations.

Some of the key features of this MIB are\:
  a) Allows grouping of MIB objects into groups called 
     data groups. The constraint is that the MIB objects 
     grouped into a data group, need to have the same 
     semantic MIB index. So it is possible to group MIB 
     objects belonging to different MIB tables into a 
     single data group as long as the above constraint is 
     met.
     For e.g. it is possible to group ifInOctets from 
     ifTable, ifHCInOctets from ifXTable, 
     dot3StatsExcessiveCollisions from dot3StatsTable 
     into a single data group.

  b) Allows the application to specify a set of instances 
     (of the MIB objects in a data group) whose values 
     need to be collected. 

  c) The required data can be collected for each such 
     data group on a periodic basis into a virtual file
     (VFile). A VFile is an abstraction of a file. 

  d) The format of the contents of the VFile, can be 
     specified by the application. 

  e) An application can also specify a collection period. 
     A collection period is an interval of time during 
     which data is collected into a VFile. After the 
     collection period ends, the VFile is frozen, and a 
     new VFile is created for storing data. The frozen 
     VFile is then transferred to a specified destination. 
     An application can choose to retain such frozen 
     VFiles on the device for a certain period of time, 
     called the retention period. 

         Data Collection MIB vs Bulkfile MIB
         \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
   The data collection MIB can pretty much do what the
   CISCO\-BULK\-FILE\-MIB (Bulkfile MIB) can do. The 'manual' 
   mode of the Data collection MIB is similar to the way 
   in which the Bulkfile MIB operates.

   However the data collection MIB is mainly targetted 
   for medium to high\-end platforms which have sufficient
   local storage (volatile or permanent) to store VFiles.
   Locally storing VFiles, helps minimize loss of data 
   during temporary network outages. If the local store 
   is permament, then the collected data is also available 
   across agent restarts.  

   The data collection MIB has more powerful data 
   selection features than the Bulkfile MIB. It allows 
   grouping of MIB objects from different tables into 
   data groups. It also incorporates a more flexible 
   instance selection mechanism, where the application 
   is not restricted to fetching an entire MIB table. 

                Definitions\:
                \*\*\*\*\*\*\*\*\*\*\*\*
    Base objects\: 
    \*\*\*\*\*\*\*\*\*\*\*\*\*
    MIB objects whose values an application needs to 
    collect.

    Data group\:
    \*\*\*\*\*\*\*\*\*\*\*
    A group of base objects. Can be of 2 types\: 'object' 
    and 'table'. An 'object' type data group can consist 
    of only one fully instantiated base object. A 'table'
    type data group can consist of more than one base
    objects, each a columnar object in a conceptual
    table. In addition a 'table' type data group can
    specify the instances of the base objects whose 
    values need to be collected. In the context of this 
    MIB, collecting data for a data group means fetching 
    the values of the associated base object instances 
    and storing them into VFiles.

    Virtual File (VFile)\:
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
    A VFile is a file like entity used to collect data. 
    An agent might choose to implement a VFile as a 
    simple in\-memory buffer, or it might choose to
    use a file in it's filesystem. An application does
    not really need to know the location of a VFile 
    \- the MIB provides mechanisms to transfer the 
    VFile to application specified locations. However 
    if the implementation supports it, the application 
    can specify the location of the VFiles.

    Current VFile\:
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*
    The VFile into which data is currently being 
     collected.

    Frozen VFile\:
    \*\*\*\*\*\*\*\*\*\*\*\*\*
    A VFile which is no longer used for collecting 
    data. Only frozen VFiles can be transferred to 
    specified destinations.

    Collection interval\:
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
    A collection interval is associated with a VFile.
    It is the interval of time over which a VFile 
    is used to collect data. 
    This interval of time can be specified by the 
    application. However there are conditions under 
    which a collection interval can be shorter than 
    the specified time. For e.g. a collection 
    interval is prematurely terminated when the 
    maximum size of a VFile is exceeded, or when 
    there is an error condition.

    Polling period\:
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
    A polling period is associated with a data 
    group. It determines the frequency at which 
    the base objects of a data group should
    be fetched and stored into a VFile.

    Data collection operations\:
    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
    A generic term used to refer to operations 
    that are carried out while collecting data. 
    These include\:
       \- Periodically creating new VFiles for 
         collecting data.
       \- Transferring frozen VFiles either 
         automatically or on demand.
       \- Fetching base object values and storing 
         them into current VFiles, either periodically 
         or on demand.
       \- Deleting frozen VFiles, either periodically 
         or on demand.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CdcFileFormat(Enum):
    """
    CdcFileFormat (Enum Class)

    The file formats supported are\:

    cdcBulkASCII        ASCII format similar to

                        the 'bulkASCII' format of the

                        CISCO\-BULK\-FILE\-MIB. 

    cdcBulkBinary       Binary format similar to

                        the 'bulkBinary' format of the

                        CISCO\-BULK\-FILE\-MIB.  

    cdcSchemaASCII      Again an ASCII format, but contains

                        parser friendly hints for parsing data

                        values. 

    Format descriptions \:

    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

    The below description applies to cdcBulkASCII & cdcBulkBinary

    and is extracted from CISCO\-BULK\-FILE\-MIB. Some differences are

    highlighted below\:

    1) Data for a single data group can be collected more than

       once into the same VFile (due to periodic polling). Each

       such instance of a data group, can be treated much like

       different 'table' types in the CISCO\-BULK\-FILE\-MIB. 

    2) Every object & table tag contains an additional sysUpTime

       field. Similarly each row tag contains the value of the

       sysUpTime when the data for that row was collected.

     The rest of the description is taken from the

     CISCO\-BULK\-FILE\-MIB. 

     The file contains two types of fields\: tags and data. Tags

     identify portions of the file and are discussed in detail

     below.  All other information is in data fields.

     Note\: For efficiency and compactness data fields are not

     tagged with a type.  The interpreter of the data must thus

     know or have access to appropriate MIB syntax descriptions to

     understand the file. 

     All data fields are positional relative to a tag and every

     data field has a length prefix.  All initial length prefixes

     are one byte.  For any data type the distinguished length

     value 255 indicates that the data content is null, that is,

     no data content value was available and there are no

     additional bytes in the data field. 

     INTEGER data fields include all data that maps to ASN.1

     INTEGER, regardless of length and whether signed or unsigned.

     They have a length prefix value of zero to eight, followed by

     that many bytes of data, high\-order byte first.  High order

     bytes that are all zero are omitted, thus a length of zero

     indicates a value of zero.  For signed numbers, leading bytes

     of all ones (hex FF) are omitted if the next remaining byte

     has the high bit on.  This implies that the file parser must

     know the difference between signed and unsigned integers.

     OCTET STRING values have a length prefix value of zero to two

     for a subsequent unsigned byte count for the number of bytes

     in the OCTET STRING itself, which immediately follows the

     byte count.  The byte count can thus range from zero to 65,535.

     OBJECT IDENTIFIER values have a length of zero to 128, for

     the number of sub\-identifiers.  Each subsequent

     sub\-identifier is encoded as an unsigned INTEGER of 0\-4 bytes.

     The bulk binary file layout directly reflects the contents of

     the cbfDefineFileObjectTable.  It has tagged sections

     corresponding to cbfDefineObjectClass with a few additional

     tags for utility purposes. 

     A tag is one byte with one of the following values\:

          \-2      row

          \-1      prefix

           0      reserved

           2      table

     The prefix tag changes the default OID prefix that is assumed

     to precede all OIDs that are not MIB object data values.  The

     prefix tag may appear anywhere another tag could appear.  A

     prefix tag is followed by one OID data field.  The default

     prefix is 1.3.6.1. A file need not set the prefix to the

     default value.  Note that when changing the prefix, the

     default portion must be included at the beginning of the new

     prefix.  Typically the prefix will change for each table or

     group of scalar objects. 

     A table tag is followed by one INTEGER data field whose value

     is the number of columns in the table (including the

     sysUpTime column), as implemented by the agent. This is

     followed by an OID field containing the sysUpTime OID. This

     is followed by one OID data field for each column.  This is

     the OID for the column minus the prefix and the instance

     (typically one subidentifier). 

     The OIDs are then followed by one row for each row in the

     table. A row starts with a row tag, one OID data field

     containing only the instance portion of the OIDs for the

     objects in that row and one data field indicating the

     sysUpTime when the row was sampled.

     Following this is one data field of appropriate type for each 

     column.

     The bulk ASCII form mechanically translates bulk binary into

     human\-readable text.

     The indicator for a null value is '~'.

     An INTEGER becomes the integer value with a preceding '\-' for

     negative values and no leading zeros.

     An OCTET STRING becomes the byte values in hexadecimal, lower

     case, two characters per byte (that is, with leading zeros),

     no delimiters between bytes.

     An OBJECT IDENTIFIER becomes the usual dotted decimal form.

     A tag becomes the tag's name, spelled out fully in lower

     case, followed by one blank and the data field(s) for the

     tag, separated by spaces and ending with a carriage

     return/line feed.  All tags are at the beginning of a 'line'

     that is terminated with a carriage return/line feed that

     immediately precedes the next tag or the end of file.

    .. data:: cdcBulkASCII = 1

    .. data:: cdcBulkBinary = 2

    .. data:: cdcSchemaASCII = 3

    """

    cdcBulkASCII = Enum.YLeaf(1, "cdcBulkASCII")

    cdcBulkBinary = Enum.YLeaf(2, "cdcBulkBinary")

    cdcSchemaASCII = Enum.YLeaf(3, "cdcSchemaASCII")


class CdcFileXferStatus(Enum):
    """
    CdcFileXferStatus (Enum Class)

    The status of a file transfer. The different values are given

    below\: 

    notStarted             File transfer has not started.

    success                File transfer has successfully

                           completed.

    aborted                File transfer has been aborted.

    fileOpenFailRemote     Remote file could not be opened.

    badDomainName          Bad domain name given in the URL.

    unreachableIpAddress   IP address given in the URL could not

                           be reached.

    networkFailure         Transfer failed due to a network

                           failure.

    fileWriteFailed        A write on the remote file has

                           failed.

    authFailed             Authentication failed. For instance

                           incorrect password in CdcUrl incase

                           of FTP(File Transfer Protocol).

    .. data:: notStarted = 1

    .. data:: success = 2

    .. data:: aborted = 3

    .. data:: fileOpenFailRemote = 4

    .. data:: badDomainName = 5

    .. data:: unreachableIpAddress = 6

    .. data:: networkFailed = 7

    .. data:: fileWriteFailed = 8

    .. data:: authFailed = 9

    """

    notStarted = Enum.YLeaf(1, "notStarted")

    success = Enum.YLeaf(2, "success")

    aborted = Enum.YLeaf(3, "aborted")

    fileOpenFailRemote = Enum.YLeaf(4, "fileOpenFailRemote")

    badDomainName = Enum.YLeaf(5, "badDomainName")

    unreachableIpAddress = Enum.YLeaf(6, "unreachableIpAddress")

    networkFailed = Enum.YLeaf(7, "networkFailed")

    fileWriteFailed = Enum.YLeaf(8, "fileWriteFailed")

    authFailed = Enum.YLeaf(9, "authFailed")



class CISCODATACOLLECTIONMIB(Entity):
    """
    
    
    .. attribute:: cdcvfile
    
    	
    	**type**\:  :py:class:`CdcVFile <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcVFile>`
    
    	**config**\: False
    
    .. attribute:: cdcvfiletable
    
    	A table for setting up VFiles for collecting data
    	**type**\:  :py:class:`CdcVFileTable <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcVFileTable>`
    
    	**config**\: False
    
    .. attribute:: cdcvfilemgmttable
    
    	A table to manage frozen VFiles
    	**type**\:  :py:class:`CdcVFileMgmtTable <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcVFileMgmtTable>`
    
    	**config**\: False
    
    .. attribute:: cdcdgtable
    
    	A table for specifying data groups
    	**type**\:  :py:class:`CdcDGTable <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcDGTable>`
    
    	**config**\: False
    
    .. attribute:: cdcdgbaseobjecttable
    
    	A table specifying the base objects of a 'table' type data group
    	**type**\:  :py:class:`CdcDGBaseObjectTable <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcDGBaseObjectTable>`
    
    	**config**\: False
    
    .. attribute:: cdcdginstancetable
    
    	Identifies the instances of the base objects that need to be fetched for a 'table' type data group.  The agent is not responsible for verifying that the instances specified for a data group do not overlap
    	**type**\:  :py:class:`CdcDGInstanceTable <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcDGInstanceTable>`
    
    	**config**\: False
    
    .. attribute:: cdcfilexferconftable
    
    	A table for configuring file transfer operations
    	**type**\:  :py:class:`CdcFileXferConfTable <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcFileXferConfTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-DATA-COLLECTION-MIB'
    _revision = '2002-10-30'

    def __init__(self):
        super(CISCODATACOLLECTIONMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-DATA-COLLECTION-MIB"
        self.yang_parent_name = "CISCO-DATA-COLLECTION-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cdcVFile", ("cdcvfile", CISCODATACOLLECTIONMIB.CdcVFile)), ("cdcVFileTable", ("cdcvfiletable", CISCODATACOLLECTIONMIB.CdcVFileTable)), ("cdcVFileMgmtTable", ("cdcvfilemgmttable", CISCODATACOLLECTIONMIB.CdcVFileMgmtTable)), ("cdcDGTable", ("cdcdgtable", CISCODATACOLLECTIONMIB.CdcDGTable)), ("cdcDGBaseObjectTable", ("cdcdgbaseobjecttable", CISCODATACOLLECTIONMIB.CdcDGBaseObjectTable)), ("cdcDGInstanceTable", ("cdcdginstancetable", CISCODATACOLLECTIONMIB.CdcDGInstanceTable)), ("cdcFileXferConfTable", ("cdcfilexferconftable", CISCODATACOLLECTIONMIB.CdcFileXferConfTable))])
        self._leafs = OrderedDict()

        self.cdcvfile = CISCODATACOLLECTIONMIB.CdcVFile()
        self.cdcvfile.parent = self
        self._children_name_map["cdcvfile"] = "cdcVFile"

        self.cdcvfiletable = CISCODATACOLLECTIONMIB.CdcVFileTable()
        self.cdcvfiletable.parent = self
        self._children_name_map["cdcvfiletable"] = "cdcVFileTable"

        self.cdcvfilemgmttable = CISCODATACOLLECTIONMIB.CdcVFileMgmtTable()
        self.cdcvfilemgmttable.parent = self
        self._children_name_map["cdcvfilemgmttable"] = "cdcVFileMgmtTable"

        self.cdcdgtable = CISCODATACOLLECTIONMIB.CdcDGTable()
        self.cdcdgtable.parent = self
        self._children_name_map["cdcdgtable"] = "cdcDGTable"

        self.cdcdgbaseobjecttable = CISCODATACOLLECTIONMIB.CdcDGBaseObjectTable()
        self.cdcdgbaseobjecttable.parent = self
        self._children_name_map["cdcdgbaseobjecttable"] = "cdcDGBaseObjectTable"

        self.cdcdginstancetable = CISCODATACOLLECTIONMIB.CdcDGInstanceTable()
        self.cdcdginstancetable.parent = self
        self._children_name_map["cdcdginstancetable"] = "cdcDGInstanceTable"

        self.cdcfilexferconftable = CISCODATACOLLECTIONMIB.CdcFileXferConfTable()
        self.cdcfilexferconftable.parent = self
        self._children_name_map["cdcfilexferconftable"] = "cdcFileXferConfTable"
        self._segment_path = lambda: "CISCO-DATA-COLLECTION-MIB:CISCO-DATA-COLLECTION-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCODATACOLLECTIONMIB, [], name, value)


    class CdcVFile(Entity):
        """
        
        
        .. attribute:: cdcvfilepersistentstorage
        
        	This object's value reads 'true', if the agent implementation of this MIB supports placement of VFiles in application specified persistent storage locations. Otherwise  the value is 'false'
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: cdcvfilemaxsizehitslimit
        
        	A global limit for the number of consecutive times the maximum VFile size (cdcVFileMaxSize) is exceeded for a given VFile. When this limit is exceeded the offending cdcVFileEntry is moved to the error state (see cdcVFileOperStatus)
        	**type**\: int
        
        	**range:** 1..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DATA-COLLECTION-MIB'
        _revision = '2002-10-30'

        def __init__(self):
            super(CISCODATACOLLECTIONMIB.CdcVFile, self).__init__()

            self.yang_name = "cdcVFile"
            self.yang_parent_name = "CISCO-DATA-COLLECTION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cdcvfilepersistentstorage', (YLeaf(YType.boolean, 'cdcVFilePersistentStorage'), ['bool'])),
                ('cdcvfilemaxsizehitslimit', (YLeaf(YType.uint32, 'cdcVFileMaxSizeHitsLimit'), ['int'])),
            ])
            self.cdcvfilepersistentstorage = None
            self.cdcvfilemaxsizehitslimit = None
            self._segment_path = lambda: "cdcVFile"
            self._absolute_path = lambda: "CISCO-DATA-COLLECTION-MIB:CISCO-DATA-COLLECTION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODATACOLLECTIONMIB.CdcVFile, ['cdcvfilepersistentstorage', 'cdcvfilemaxsizehitslimit'], name, value)



    class CdcVFileTable(Entity):
        """
        A table for setting up VFiles for collecting data.
        
        .. attribute:: cdcvfileentry
        
        	An entry in the cdcVFileTable. Each entry contains application specified configuration that is used to create  virtual files (VFile) and start data collection operations.   A VFile is used to store data (values of base object instances) as selected by entities called data groups. A data group is defined in cdcDGTable.   An entry in this table is said to be 'activated' when the corresponding instances of cdcVFileRowStatus is 'active' AND cdcVFileOperStatus is 'enabled'. The value of sysUpTime.0 when the condition evaluates to 'true' is called the activation time of the entry. The activation time for each entry is maintained internally by the agent
        	**type**\: list of  		 :py:class:`CdcVFileEntry <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcVFileTable.CdcVFileEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DATA-COLLECTION-MIB'
        _revision = '2002-10-30'

        def __init__(self):
            super(CISCODATACOLLECTIONMIB.CdcVFileTable, self).__init__()

            self.yang_name = "cdcVFileTable"
            self.yang_parent_name = "CISCO-DATA-COLLECTION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdcVFileEntry", ("cdcvfileentry", CISCODATACOLLECTIONMIB.CdcVFileTable.CdcVFileEntry))])
            self._leafs = OrderedDict()

            self.cdcvfileentry = YList(self)
            self._segment_path = lambda: "cdcVFileTable"
            self._absolute_path = lambda: "CISCO-DATA-COLLECTION-MIB:CISCO-DATA-COLLECTION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODATACOLLECTIONMIB.CdcVFileTable, [], name, value)


        class CdcVFileEntry(Entity):
            """
            An entry in the cdcVFileTable. Each entry contains
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
            
            .. attribute:: cdcvfileindex  (key)
            
            	An arbitrary integer for uniquely identifying this entry. When creating a row, the application should pick a random number.   If the configuration in this entry is persisted across system/agent restarts then the same value of cdcVFileIndex must be assigned to this entry after the restart
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cdcvfilename
            
            	The base\-name of the VFiles (created by data collection operations corresponding to this entry) into which data is to be collected.   When a VFile is created, it's full name is obtained by the concatentation of a suffix to this value. The suffix will be chosen by the agent such that the VFiles created for this entry have unique names. For e.g. the suffix could be a string representation of the date and time when the VFile was created.   If VFiles are to be placed in the agent's local filesystem (provided the agent supports it) then this value should also contain the absolute path of the location as a prefix to the base name.  An agent will respond with inconsistentValue to a management set operation which attempts to modify the value of this object to the same value as already held by another instance of cdcVFileName, or wrongValue if the new value  is invalid for use as a file name on the local file  system (e.g., many file systems do not support white  space embedded in file names).  This object's value may be modified at any time. However the new name will be used only when the next VFile is created for this entry
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdcvfiledescription
            
            	A string that can be used for administrative purposes.  This object's value may be modified at any time
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdcvfilecommand
            
            	An object for controlling collection of data.  'idle'            Indicates that no command is in progress.  'swapToNewFile'   When written, the current VFile is frozen,                   and a new VFile is created for collecting                   data. 		   If the data collection mode is automatic                   (see cdcVFileCollectMode), then the current                    collection interval is stopped and a new                   collection interval is started  		   (see cdcVFileCollectPeriod).                      'collectNow'      When written, base object values for                   all associated data groups are fetched                    and stored into the current VFile. This                   value can only be written when the                   collection mode is 'manual' (see                    cdcVFileCollectMode)
            	**type**\:  :py:class:`CdcVFileCommand <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcVFileTable.CdcVFileEntry.CdcVFileCommand>`
            
            	**config**\: False
            
            .. attribute:: cdcvfilemaxsize
            
            	The maximum size of a VFile.   The agent maintains an internal counter for each cdcVFileEntry. This counter counts the number of consecutive times the size of a VFile has exceeded the value of this object. When the value of this counter exceeds the value of cdcVFileMaxSizeHitsLimit, this entry is moved to the 'error' state (see cdcVFileOperStatus). However if the value of cdcVFileMaxSizeHitsLimit is not exceeded, then the current VFile is frozen, and a new VFile is created for data collection.  If the data collection mode is automatic (see cdcVFileCollectMode), then the current collection interval is stopped and a new collection interval is started.  This object's value may be modified at any time. The new size limit MUST be checked against the size of the current VFile at the time of modification, and appropriate action taken
            	**type**\: int
            
            	**range:** 512..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cdcvfilecurrentsize
            
            	The size of the current VFile
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cdcvfileformat
            
            	The format in which data is stored into the current VFile.  This object's value cannot be modified while the entry is in the 'activated' state
            	**type**\:  :py:class:`CdcFileFormat <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CdcFileFormat>`
            
            	**config**\: False
            
            .. attribute:: cdcvfilecollectmode
            
            	Determines the mode of data collection.  'auto'         Data is periodically fetched for all data                groups associated with this entry. This is                done at data group specific periodic intervals                (cdcDGPollPeriod).                The data thus collected, is formatted and                stored into the current VFile.                  In addition at regular intervals (see                cdcVFileCollectPeriod) a new VFile                 is created to store data, and the current                VFile is frozen and transferred.  'manual'       Data for all data groups is fetched and                collected into the current VFile only when                 cdcVFileCommand is set to 'collectNow'.   This object's value cannot be modified while the entry is in the 'activated' state
            	**type**\:  :py:class:`CdcVFileCollectMode <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcVFileTable.CdcVFileEntry.CdcVFileCollectMode>`
            
            	**config**\: False
            
            .. attribute:: cdcvfilecollectionperiod
            
            	Specifies the period of a collection interval. The value of this object is used only when the data collection mode is  automatic (see cdcVFileCollectMode).  A periodic timer (one per entry) is started when this entry is 'activated'. The time at which this entry is 'activated' is called the 'activation time' for this entry, and is internally maintained by the agent.  When this periodic timer expires, the current VFile is frozen and a new VFile is created for data collection.  Transfer is then initiated for the frozen VFile.   In addition, the internally maintained counter for counting the number of consecutive times the size of a VFile has exceeded the maximum limit, is reset to zero. (See cdcVFileMaxSize)   This object's value may be modified at any time, and the  new value takes effect immediately. i.e setting a new  value can cause the current collection interval to terminate  and a new collection interval to start
            	**type**\: int
            
            	**range:** 60..604800
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cdcvfileretentionperiod
            
            	The time for which a frozen VFile is retained by the agent. When a VFile is frozen, a timer (one per frozen VFile) is started to keep track of the retention period for the  VFile. Once this timer expires, the VFile is deleted. Till the expiry of the retention period, information  about frozen VFiles is maintained in  cdcVFileMgmtTable.  This object's value may be modified at any time, however the new value will take effect only for new frozen VFiles
            	**type**\: int
            
            	**range:** 60..86400
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cdcvfileadminstatus
            
            	A control object to indicate the administratively desired state of data collection for this entry. On setting the value to 'disabled' data collection operations for this  entry are stopped, the current VFile is frozen and it's  transfer is initiated.   Modifying the value of cdcVFileAdminStatus to 'disabled' does not remove or change the current configuration as represented by the active rows in this table
            	**type**\:  :py:class:`CdcVFileAdminStatus <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcVFileTable.CdcVFileEntry.CdcVFileAdminStatus>`
            
            	**config**\: False
            
            .. attribute:: cdcvfileoperstatus
            
            	A status object to indicate the operational state of collection for this entry.  When the value of cdcVFileAdminStatus is modified to be 'enabled', the value of this object will change to 'enabled' providing it is possible to begin collecting data. If at any point of time data cannot be collected because of some error, then the value of this object is changed to 'error' and all collection operations stop, as if cdcVFileAdminStatus has been set to 'disabled'. More information about the nature of the error can be obtained by retrieving the value of cdcVFileErrorCode.   When the value of cdcVFileAdminStatus is modified to be 'disabled', the value of this object will change to 'disabled' and data collection operations are stopped for this entry
            	**type**\:  :py:class:`CdcVFileOperStatus <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcVFileTable.CdcVFileEntry.CdcVFileOperStatus>`
            
            	**config**\: False
            
            .. attribute:: cdcvfileerrorcode
            
            	A value indicating the type of error that has occurred during data collection operations for this entry.  noError                The value is 'noError' when                        the corresponding value of                        cdcVFileOperStatus is not 'error'.  otherError             Any error other than one of the                         following listed errors.  noSpace                There is no space left to write into                        the current VFile.   openError              Could not open VFile for writing. One                        possible reason could be the existence                        of another file by the same name in                        the agent's filesystem.   tooSmallMaxSize        Indicates that cdcVFileMaxSize is                         too small for data collection. The                         cdcVFileMaxSize configured for this                        VFile is not sufficient even to hold                         the data collected in one poll.  tooManyMaxSizeHits     Indicates that data collection                        operations are stopped because                        the value of cdcVFileMaxSizeHitsLimit                        has been exceeded.   noResource             Some kind of resource was unavailable                        while collecting data. For                        e.g. unavailability of dynamic memory
            	**type**\:  :py:class:`CdcVFileErrorCode <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcVFileTable.CdcVFileEntry.CdcVFileErrorCode>`
            
            	**config**\: False
            
            .. attribute:: cdcvfilecollectionerrorenable
            
            	When set to 'true', cdcVFileCollectionError notification will be sent out in the event of a data collection error
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdcvfilerowstatus
            
            	The status of this conceptual row.  A valid cdcVFileName is only mandatory object for setting this object to 'active'. But collection of data in to active vfile starts only on setting cdcVFileAdminStatus  to 'enabled'. Setting this object to 'destroy' stops all data collection operations for this entry, deletes all VFiles and removes this entry from cdcVFileTable
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DATA-COLLECTION-MIB'
            _revision = '2002-10-30'

            def __init__(self):
                super(CISCODATACOLLECTIONMIB.CdcVFileTable.CdcVFileEntry, self).__init__()

                self.yang_name = "cdcVFileEntry"
                self.yang_parent_name = "cdcVFileTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdcvfileindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdcvfileindex', (YLeaf(YType.uint32, 'cdcVFileIndex'), ['int'])),
                    ('cdcvfilename', (YLeaf(YType.str, 'cdcVFileName'), ['str'])),
                    ('cdcvfiledescription', (YLeaf(YType.str, 'cdcVFileDescription'), ['str'])),
                    ('cdcvfilecommand', (YLeaf(YType.enumeration, 'cdcVFileCommand'), [('ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CISCODATACOLLECTIONMIB', 'CdcVFileTable.CdcVFileEntry.CdcVFileCommand')])),
                    ('cdcvfilemaxsize', (YLeaf(YType.uint32, 'cdcVFileMaxSize'), ['int'])),
                    ('cdcvfilecurrentsize', (YLeaf(YType.uint32, 'cdcVFileCurrentSize'), ['int'])),
                    ('cdcvfileformat', (YLeaf(YType.enumeration, 'cdcVFileFormat'), [('ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CdcFileFormat', '')])),
                    ('cdcvfilecollectmode', (YLeaf(YType.enumeration, 'cdcVFileCollectMode'), [('ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CISCODATACOLLECTIONMIB', 'CdcVFileTable.CdcVFileEntry.CdcVFileCollectMode')])),
                    ('cdcvfilecollectionperiod', (YLeaf(YType.uint32, 'cdcVFileCollectionPeriod'), ['int'])),
                    ('cdcvfileretentionperiod', (YLeaf(YType.uint32, 'cdcVFileRetentionPeriod'), ['int'])),
                    ('cdcvfileadminstatus', (YLeaf(YType.enumeration, 'cdcVFileAdminStatus'), [('ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CISCODATACOLLECTIONMIB', 'CdcVFileTable.CdcVFileEntry.CdcVFileAdminStatus')])),
                    ('cdcvfileoperstatus', (YLeaf(YType.enumeration, 'cdcVFileOperStatus'), [('ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CISCODATACOLLECTIONMIB', 'CdcVFileTable.CdcVFileEntry.CdcVFileOperStatus')])),
                    ('cdcvfileerrorcode', (YLeaf(YType.enumeration, 'cdcVFileErrorCode'), [('ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CISCODATACOLLECTIONMIB', 'CdcVFileTable.CdcVFileEntry.CdcVFileErrorCode')])),
                    ('cdcvfilecollectionerrorenable', (YLeaf(YType.boolean, 'cdcVFileCollectionErrorEnable'), ['bool'])),
                    ('cdcvfilerowstatus', (YLeaf(YType.enumeration, 'cdcVFileRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.cdcvfileindex = None
                self.cdcvfilename = None
                self.cdcvfiledescription = None
                self.cdcvfilecommand = None
                self.cdcvfilemaxsize = None
                self.cdcvfilecurrentsize = None
                self.cdcvfileformat = None
                self.cdcvfilecollectmode = None
                self.cdcvfilecollectionperiod = None
                self.cdcvfileretentionperiod = None
                self.cdcvfileadminstatus = None
                self.cdcvfileoperstatus = None
                self.cdcvfileerrorcode = None
                self.cdcvfilecollectionerrorenable = None
                self.cdcvfilerowstatus = None
                self._segment_path = lambda: "cdcVFileEntry" + "[cdcVFileIndex='" + str(self.cdcvfileindex) + "']"
                self._absolute_path = lambda: "CISCO-DATA-COLLECTION-MIB:CISCO-DATA-COLLECTION-MIB/cdcVFileTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODATACOLLECTIONMIB.CdcVFileTable.CdcVFileEntry, ['cdcvfileindex', 'cdcvfilename', 'cdcvfiledescription', 'cdcvfilecommand', 'cdcvfilemaxsize', 'cdcvfilecurrentsize', 'cdcvfileformat', 'cdcvfilecollectmode', 'cdcvfilecollectionperiod', 'cdcvfileretentionperiod', 'cdcvfileadminstatus', 'cdcvfileoperstatus', 'cdcvfileerrorcode', 'cdcvfilecollectionerrorenable', 'cdcvfilerowstatus'], name, value)

            class CdcVFileAdminStatus(Enum):
                """
                CdcVFileAdminStatus (Enum Class)

                A control object to indicate the administratively desired

                state of data collection for this entry. On setting the value

                to 'disabled' data collection operations for this

                 entry are stopped, the current VFile is frozen and it's

                 transfer is initiated. 

                Modifying the value of cdcVFileAdminStatus to 'disabled' does

                not remove or change the current configuration as represented

                by the active rows in this table.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")


            class CdcVFileCollectMode(Enum):
                """
                CdcVFileCollectMode (Enum Class)

                Determines the mode of data collection.

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

                .. data:: auto = 1

                .. data:: manual = 2

                """

                auto = Enum.YLeaf(1, "auto")

                manual = Enum.YLeaf(2, "manual")


            class CdcVFileCommand(Enum):
                """
                CdcVFileCommand (Enum Class)

                An object for controlling collection of data.

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

                .. data:: idle = 1

                .. data:: swapToNewFile = 2

                .. data:: collectNow = 3

                """

                idle = Enum.YLeaf(1, "idle")

                swapToNewFile = Enum.YLeaf(2, "swapToNewFile")

                collectNow = Enum.YLeaf(3, "collectNow")


            class CdcVFileErrorCode(Enum):
                """
                CdcVFileErrorCode (Enum Class)

                A value indicating the type of error that has occurred during

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

                .. data:: noError = 1

                .. data:: otherError = 2

                .. data:: noSpace = 3

                .. data:: openError = 4

                .. data:: tooSmallMaxSize = 5

                .. data:: tooManyMaxSizeHits = 6

                .. data:: noResource = 7

                """

                noError = Enum.YLeaf(1, "noError")

                otherError = Enum.YLeaf(2, "otherError")

                noSpace = Enum.YLeaf(3, "noSpace")

                openError = Enum.YLeaf(4, "openError")

                tooSmallMaxSize = Enum.YLeaf(5, "tooSmallMaxSize")

                tooManyMaxSizeHits = Enum.YLeaf(6, "tooManyMaxSizeHits")

                noResource = Enum.YLeaf(7, "noResource")


            class CdcVFileOperStatus(Enum):
                """
                CdcVFileOperStatus (Enum Class)

                A status object to indicate the operational state of

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

                .. data:: enabled = 1

                .. data:: disabled = 2

                .. data:: error = 3

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")

                error = Enum.YLeaf(3, "error")





    class CdcVFileMgmtTable(Entity):
        """
        A table to manage frozen VFiles.
        
        .. attribute:: cdcvfilemgmtentry
        
        	An entry in cdcVFileMgmtTable. Each entry corresponds to a frozen VFile. An entry is created in this table, whenever a VFile is frozen. An entry is removed from this table whenever a frozen VFile is deleted either because the retention period elapsed or because it was adminstratively deleted.  If the configuration specified in cdcVFileEntry is persisted across system/agent restarts AND the VFiles created as a result of that configuration are persisted across restarts, then this table must be populated with entries corresponding to those persisted VFiles. However any state related to an entry, like time to live etc. need not be maintained across restarts
        	**type**\: list of  		 :py:class:`CdcVFileMgmtEntry <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcVFileMgmtTable.CdcVFileMgmtEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DATA-COLLECTION-MIB'
        _revision = '2002-10-30'

        def __init__(self):
            super(CISCODATACOLLECTIONMIB.CdcVFileMgmtTable, self).__init__()

            self.yang_name = "cdcVFileMgmtTable"
            self.yang_parent_name = "CISCO-DATA-COLLECTION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdcVFileMgmtEntry", ("cdcvfilemgmtentry", CISCODATACOLLECTIONMIB.CdcVFileMgmtTable.CdcVFileMgmtEntry))])
            self._leafs = OrderedDict()

            self.cdcvfilemgmtentry = YList(self)
            self._segment_path = lambda: "cdcVFileMgmtTable"
            self._absolute_path = lambda: "CISCO-DATA-COLLECTION-MIB:CISCO-DATA-COLLECTION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODATACOLLECTIONMIB.CdcVFileMgmtTable, [], name, value)


        class CdcVFileMgmtEntry(Entity):
            """
            An entry in cdcVFileMgmtTable. Each entry corresponds to a
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
            
            .. attribute:: cdcvfileindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cdcvfileindex <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcVFileTable.CdcVFileEntry>`
            
            	**config**\: False
            
            .. attribute:: cdcvfilemgmtindex  (key)
            
            	This value is a running counter starting at 1, generated by the agent so that the combination of  cdcVFileIndex and cdcVFileMgmtIndex uniquely identifies a frozen VFile. The deleted file indicies do not get reused.  This object's value needs to be unique only across the set of frozen VFiles corresponding to a cdcVFileEntry (identified by cdcVFileIndex)
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cdcvfilemgmtname
            
            	The full name of the VFile. If the VFile is stored as a file in the agent's filesystem, then this value also contains the absolute path of the file
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdcvfilemgmttimestamp
            
            	The timestamp when this VFile was created, in the date\-time format
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdcvfilemgmttimetolive
            
            	The time left before this VFile is deleted (see cdcVFileRetentionPeriod)
            	**type**\: int
            
            	**range:** 60..86400
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cdcvfilemgmtcommand
            
            	A control to manage VFiles.   idle           This value can be only be read. It indicates                that no management action is currently being                performed on this VFile.  delete         This value is only written, and is used to                delete the frozen VFile. Writing this value                will cause this entry to be removed from this                table.   transfer       This value can be both read and written.                When read it means that the VFile is in the                process of being transferred. When written, it                initiates a transfer for the VFile.  abortTransfer  This value can only be written, and is used                to abort an ongoing transfer
            	**type**\:  :py:class:`CdcVFileMgmtCommand <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcVFileMgmtTable.CdcVFileMgmtEntry.CdcVFileMgmtCommand>`
            
            	**config**\: False
            
            .. attribute:: cdcvfilemgmtxferurl
            
            	The complete URL of the destination to which this VFile will be transferred in the next attempt. The URL also includes the complete filename of the remote file that will be created. When the default value of this object is  retained this VFile will be transferred to the URL   specified in cdcFileXferConfPriUrl or cdcFileXferConfSecUrl, as the case may be.   However an application can specify a different URL, in which case the VFile will be transferred to this new URL the next time transfer is initiated.   This object's value may be modified at any time
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdcvfilemgmtlastxferstatus
            
            	Indicates the status of the last completed transfer
            	**type**\:  :py:class:`CdcFileXferStatus <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CdcFileXferStatus>`
            
            	**config**\: False
            
            .. attribute:: cdcvfilemgmtlastxferurl
            
            	Indicates the URL of the destination to which the last (completed) transfer was initiated
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DATA-COLLECTION-MIB'
            _revision = '2002-10-30'

            def __init__(self):
                super(CISCODATACOLLECTIONMIB.CdcVFileMgmtTable.CdcVFileMgmtEntry, self).__init__()

                self.yang_name = "cdcVFileMgmtEntry"
                self.yang_parent_name = "cdcVFileMgmtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdcvfileindex','cdcvfilemgmtindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdcvfileindex', (YLeaf(YType.str, 'cdcVFileIndex'), ['int'])),
                    ('cdcvfilemgmtindex', (YLeaf(YType.uint32, 'cdcVFileMgmtIndex'), ['int'])),
                    ('cdcvfilemgmtname', (YLeaf(YType.str, 'cdcVFileMgmtName'), ['str'])),
                    ('cdcvfilemgmttimestamp', (YLeaf(YType.str, 'cdcVFileMgmtTimestamp'), ['str'])),
                    ('cdcvfilemgmttimetolive', (YLeaf(YType.uint32, 'cdcVFileMgmtTimeToLive'), ['int'])),
                    ('cdcvfilemgmtcommand', (YLeaf(YType.enumeration, 'cdcVFileMgmtCommand'), [('ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CISCODATACOLLECTIONMIB', 'CdcVFileMgmtTable.CdcVFileMgmtEntry.CdcVFileMgmtCommand')])),
                    ('cdcvfilemgmtxferurl', (YLeaf(YType.str, 'cdcVFileMgmtXferURL'), ['str'])),
                    ('cdcvfilemgmtlastxferstatus', (YLeaf(YType.enumeration, 'cdcVFileMgmtLastXferStatus'), [('ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CdcFileXferStatus', '')])),
                    ('cdcvfilemgmtlastxferurl', (YLeaf(YType.str, 'cdcVFileMgmtLastXferURL'), ['str'])),
                ])
                self.cdcvfileindex = None
                self.cdcvfilemgmtindex = None
                self.cdcvfilemgmtname = None
                self.cdcvfilemgmttimestamp = None
                self.cdcvfilemgmttimetolive = None
                self.cdcvfilemgmtcommand = None
                self.cdcvfilemgmtxferurl = None
                self.cdcvfilemgmtlastxferstatus = None
                self.cdcvfilemgmtlastxferurl = None
                self._segment_path = lambda: "cdcVFileMgmtEntry" + "[cdcVFileIndex='" + str(self.cdcvfileindex) + "']" + "[cdcVFileMgmtIndex='" + str(self.cdcvfilemgmtindex) + "']"
                self._absolute_path = lambda: "CISCO-DATA-COLLECTION-MIB:CISCO-DATA-COLLECTION-MIB/cdcVFileMgmtTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODATACOLLECTIONMIB.CdcVFileMgmtTable.CdcVFileMgmtEntry, ['cdcvfileindex', 'cdcvfilemgmtindex', 'cdcvfilemgmtname', 'cdcvfilemgmttimestamp', 'cdcvfilemgmttimetolive', 'cdcvfilemgmtcommand', 'cdcvfilemgmtxferurl', 'cdcvfilemgmtlastxferstatus', 'cdcvfilemgmtlastxferurl'], name, value)

            class CdcVFileMgmtCommand(Enum):
                """
                CdcVFileMgmtCommand (Enum Class)

                A control to manage VFiles. 

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

                .. data:: idle = 1

                .. data:: delete = 2

                .. data:: transfer = 3

                .. data:: abortTransfer = 4

                """

                idle = Enum.YLeaf(1, "idle")

                delete = Enum.YLeaf(2, "delete")

                transfer = Enum.YLeaf(3, "transfer")

                abortTransfer = Enum.YLeaf(4, "abortTransfer")





    class CdcDGTable(Entity):
        """
        A table for specifying data groups.
        
        .. attribute:: cdcdgentry
        
        	An entry in this table. Each entry corresponds to a data group. A data group is used to select data that needs to be collected into VFiles. The selection is done by specifying the base objects and their instances for which the values need to be fetched.  Data is collected only for those data groups, that have the corresponding instance of cdcDGRowStatus set to 'active'.   In order for data to be collected, each data group has to be associated with a cdcVFileEntry (see cdcDGVFileIndex). If the data collection mode of the associated cdcVFileEntry is automatic, then data is fetched and stored into the current VFile of the associated cdcVFileEntry at periodic intervals (cdcDGPollPeriod)
        	**type**\: list of  		 :py:class:`CdcDGEntry <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcDGTable.CdcDGEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DATA-COLLECTION-MIB'
        _revision = '2002-10-30'

        def __init__(self):
            super(CISCODATACOLLECTIONMIB.CdcDGTable, self).__init__()

            self.yang_name = "cdcDGTable"
            self.yang_parent_name = "CISCO-DATA-COLLECTION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdcDGEntry", ("cdcdgentry", CISCODATACOLLECTIONMIB.CdcDGTable.CdcDGEntry))])
            self._leafs = OrderedDict()

            self.cdcdgentry = YList(self)
            self._segment_path = lambda: "cdcDGTable"
            self._absolute_path = lambda: "CISCO-DATA-COLLECTION-MIB:CISCO-DATA-COLLECTION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODATACOLLECTIONMIB.CdcDGTable, [], name, value)


        class CdcDGEntry(Entity):
            """
            An entry in this table. Each entry corresponds to a data
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
            
            .. attribute:: cdcdgindex  (key)
            
            	An arbitrary integer used to uniquely identify this entry. When creating an entry, a management application should pick a random number
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cdcdgcomment
            
            	A descriptive string. This object's value may be modified at any time
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdcdgtype
            
            	Identifies the type of this data group. object         Data is a single MIB object. The fully                instantiated OID is specified in                cdcDGBaseObject.  table          Data is a logical table. The columns of                this table correspond to the base objects                specified in cdcDGBaseObjectTable, and the                rows correspond to the values of the instances                specified in cdcDGInstanceTable.  This object's value cannot be modified while the value of cdcDGRowStatus is 'active'
            	**type**\:  :py:class:`CdcDGType <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcDGTable.CdcDGEntry.CdcDGType>`
            
            	**config**\: False
            
            .. attribute:: cdcdgvfileindex
            
            	Corresponds to a value of cdcVFileIndex. It is used to associate this data group with a cdcVFileEntry. The values of the base objects for  this data group are stored into the current VFile of the associated cdcVFileEntry.   This object's value may be modified at any time. The change takes effect the next time data is fetched for this data group
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cdcdgtargettag
            
            	The tag for the target from which to obtain the data for this data group.  A length of 0 indicates the local system.  In this case, access to the objects of this data group is under the security credentials of the requester that set cdcDGRowStatus to 'active'. Those credentials are the input parameters for isAccessAllowed from the Architecture for Describing SNMP Management Frameworks.  Otherwise a search is carried out for an entry in the snmpTargetAddrTable whose snmpTargetAddrTagList contains the tag specified by the value of this object. The security credentials (snmpTargetParamsEntry) of the first entry that satisfies the above criteria, are passed as input parameters for isAccessAllowed.   This object's value may be modified at any time. The change takes effect the next time data is fetched for this data group
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdcdgcontextname
            
            	The management context from which to obtain data for this data group.  This object's value may be modified at any time. The change takes effect the next time data is fetched for this data group
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cdcdgobject
            
            	The fully instantiated name of the MIB object whose value needs to be fetched. This object's value is used only when cdcDGType is of type 'object'.   This object's value may be modified at any time. The change takes effect the next time data is fetched for this data group
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: cdcdgobjectgrpindex
            
            	Corresponds to a value of cdcDGBaseObjectGrpIndex, thus identifying a set of entries in cdcDGBaseObjectTable, having this value of cdcDGBaseObjectGrpIndex. This object's value is used only when cdcDGType is of type 'table'.   This set of entries in cdcDGBaseObjectTable in turn  identifies the set of base objects, that makes up the columns  of this 'table' type data group.     This object's value may be modified at any time. The change takes effect the next time data is fetched for this data group
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cdcdginstgrpindex
            
            	Corresponds to a value of cdcDGInstanceGrpIndex, thus identifying a set of entries in cdcDGInstanceTable, having this value of cdcDGInstanceGrpIndex. This object's value is used only when cdcDGType is of type 'table'.   The set of entries in cdcDGInstanceTable, in turn identifies the set of instances of the base objects, whose values need to fetched. If the value is 0, then all instances of the base objects will be fetched.    This object's value may be modified at any time. The change takes effect the next time data is fetched for this data group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdcdgpollperiod
            
            	Specifies the time intervals at which the data should be fetched for this data group. This object's value is used only when the collection mode of the associated cdcVFileEntry is automatic (see cdcVFileCollectMode).   A periodic timer is started for this data group when cdcDGRowStatus is set to 'active', provided the associated cdcVFileEntry has already been 'activated', otherwise it is started when the associated cdcVFileEntry is finally activated.   The time interval after which the first expiration of this timer should occur, is calculated as follows\:  (value of sysUpTime.0) +  (value of cdcPollPeriod for this entry \-     (value of sysUpTime.0 \- VFile activation time for the     associated cdcVFileEntry) % cdcPollPeriod)  Subsequent expirations of the periodic timer can occur as per the value specified in cdcDGPollPeriod. This helps in synchronizing periodic polling of the data groups with respect to the VFile activation time.  This object's value may be modified at any time, and the change must take effect immediately. i.e. if the periodic timer has been started, it's expiry time may need to be re\-adjusted
            	**type**\: int
            
            	**range:** 1..86400
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cdcdgrowstatus
            
            	The status of this conceptual row.  This object cannot be set to 'active' until values have been assigned to  cdcDGVFileIndex & cdcDGColGrpIndex
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DATA-COLLECTION-MIB'
            _revision = '2002-10-30'

            def __init__(self):
                super(CISCODATACOLLECTIONMIB.CdcDGTable.CdcDGEntry, self).__init__()

                self.yang_name = "cdcDGEntry"
                self.yang_parent_name = "cdcDGTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdcdgindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdcdgindex', (YLeaf(YType.uint32, 'cdcDGIndex'), ['int'])),
                    ('cdcdgcomment', (YLeaf(YType.str, 'cdcDGComment'), ['str'])),
                    ('cdcdgtype', (YLeaf(YType.enumeration, 'cdcDGType'), [('ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CISCODATACOLLECTIONMIB', 'CdcDGTable.CdcDGEntry.CdcDGType')])),
                    ('cdcdgvfileindex', (YLeaf(YType.uint32, 'cdcDGVFileIndex'), ['int'])),
                    ('cdcdgtargettag', (YLeaf(YType.str, 'cdcDGTargetTag'), ['str'])),
                    ('cdcdgcontextname', (YLeaf(YType.str, 'cdcDGContextName'), ['str'])),
                    ('cdcdgobject', (YLeaf(YType.str, 'cdcDGObject'), ['str'])),
                    ('cdcdgobjectgrpindex', (YLeaf(YType.uint32, 'cdcDGObjectGrpIndex'), ['int'])),
                    ('cdcdginstgrpindex', (YLeaf(YType.uint32, 'cdcDGInstGrpIndex'), ['int'])),
                    ('cdcdgpollperiod', (YLeaf(YType.uint32, 'cdcDGPollPeriod'), ['int'])),
                    ('cdcdgrowstatus', (YLeaf(YType.enumeration, 'cdcDGRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.cdcdgindex = None
                self.cdcdgcomment = None
                self.cdcdgtype = None
                self.cdcdgvfileindex = None
                self.cdcdgtargettag = None
                self.cdcdgcontextname = None
                self.cdcdgobject = None
                self.cdcdgobjectgrpindex = None
                self.cdcdginstgrpindex = None
                self.cdcdgpollperiod = None
                self.cdcdgrowstatus = None
                self._segment_path = lambda: "cdcDGEntry" + "[cdcDGIndex='" + str(self.cdcdgindex) + "']"
                self._absolute_path = lambda: "CISCO-DATA-COLLECTION-MIB:CISCO-DATA-COLLECTION-MIB/cdcDGTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODATACOLLECTIONMIB.CdcDGTable.CdcDGEntry, ['cdcdgindex', 'cdcdgcomment', 'cdcdgtype', 'cdcdgvfileindex', 'cdcdgtargettag', 'cdcdgcontextname', 'cdcdgobject', 'cdcdgobjectgrpindex', 'cdcdginstgrpindex', 'cdcdgpollperiod', 'cdcdgrowstatus'], name, value)

            class CdcDGType(Enum):
                """
                CdcDGType (Enum Class)

                Identifies the type of this data group.

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

                .. data:: object = 1

                .. data:: table = 2

                """

                object = Enum.YLeaf(1, "object")

                table = Enum.YLeaf(2, "table")





    class CdcDGBaseObjectTable(Entity):
        """
        A table specifying the base objects of a 'table' type
        data group.
        
        .. attribute:: cdcdgbaseobjectentry
        
        	An individual entry in this table. Each entry is a  {subtree, list} tuple. Each tuple identifies a set of  base objects for the associated data group
        	**type**\: list of  		 :py:class:`CdcDGBaseObjectEntry <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcDGBaseObjectTable.CdcDGBaseObjectEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DATA-COLLECTION-MIB'
        _revision = '2002-10-30'

        def __init__(self):
            super(CISCODATACOLLECTIONMIB.CdcDGBaseObjectTable, self).__init__()

            self.yang_name = "cdcDGBaseObjectTable"
            self.yang_parent_name = "CISCO-DATA-COLLECTION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdcDGBaseObjectEntry", ("cdcdgbaseobjectentry", CISCODATACOLLECTIONMIB.CdcDGBaseObjectTable.CdcDGBaseObjectEntry))])
            self._leafs = OrderedDict()

            self.cdcdgbaseobjectentry = YList(self)
            self._segment_path = lambda: "cdcDGBaseObjectTable"
            self._absolute_path = lambda: "CISCO-DATA-COLLECTION-MIB:CISCO-DATA-COLLECTION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODATACOLLECTIONMIB.CdcDGBaseObjectTable, [], name, value)


        class CdcDGBaseObjectEntry(Entity):
            """
            An individual entry in this table. Each entry is a 
            {subtree, list} tuple. Each tuple identifies a set of 
            base objects for the associated data group.
            
            .. attribute:: cdcdgbaseobjectgrpindex  (key)
            
            	This object's value when combined with the value of cdcDGBaseObjectIndex uniquely identifies an entry in this table. An application must use the same value (can  be randomly picked) for this object while creating a group of entries that collectively identifies the set of base objects for a data group
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cdcdgbaseobjectindex  (key)
            
            	This object's value when combined with the value of cdcDGBaseObjectGrpIndex uniquely identifies an entry in this table.  A managment application can assign incremental values starting from one, when creating each entry in a group of entries (as identified by the value of cdcDGBaseObjectGrpIndex)
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cdcdgbaseobjectsubtree
            
            	The subtree component of a {subtree, list} tuple.  This object's value may be modified at any time. The change takes effect the next time data is fetched for this data group
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: cdcdgbaseobjectlist
            
            	The list component of a {subtree, list} tuple.  This object's value may be modified at any time. The change takes effect the next time data is fetched for this data group
            	**type**\: str
            
            	**length:** 0..16
            
            	**config**\: False
            
            .. attribute:: cdcdgbaseobjectrowstatus
            
            	The status of this conceptual row.  This object cannot be set to 'active' until values have been assigned to cdcDGBaseObjectSubtree & cdcDGBaseObjectList
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DATA-COLLECTION-MIB'
            _revision = '2002-10-30'

            def __init__(self):
                super(CISCODATACOLLECTIONMIB.CdcDGBaseObjectTable.CdcDGBaseObjectEntry, self).__init__()

                self.yang_name = "cdcDGBaseObjectEntry"
                self.yang_parent_name = "cdcDGBaseObjectTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdcdgbaseobjectgrpindex','cdcdgbaseobjectindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdcdgbaseobjectgrpindex', (YLeaf(YType.uint32, 'cdcDGBaseObjectGrpIndex'), ['int'])),
                    ('cdcdgbaseobjectindex', (YLeaf(YType.uint32, 'cdcDGBaseObjectIndex'), ['int'])),
                    ('cdcdgbaseobjectsubtree', (YLeaf(YType.str, 'cdcDGBaseObjectSubtree'), ['str'])),
                    ('cdcdgbaseobjectlist', (YLeaf(YType.str, 'cdcDGBaseObjectList'), ['str'])),
                    ('cdcdgbaseobjectrowstatus', (YLeaf(YType.enumeration, 'cdcDGBaseObjectRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.cdcdgbaseobjectgrpindex = None
                self.cdcdgbaseobjectindex = None
                self.cdcdgbaseobjectsubtree = None
                self.cdcdgbaseobjectlist = None
                self.cdcdgbaseobjectrowstatus = None
                self._segment_path = lambda: "cdcDGBaseObjectEntry" + "[cdcDGBaseObjectGrpIndex='" + str(self.cdcdgbaseobjectgrpindex) + "']" + "[cdcDGBaseObjectIndex='" + str(self.cdcdgbaseobjectindex) + "']"
                self._absolute_path = lambda: "CISCO-DATA-COLLECTION-MIB:CISCO-DATA-COLLECTION-MIB/cdcDGBaseObjectTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODATACOLLECTIONMIB.CdcDGBaseObjectTable.CdcDGBaseObjectEntry, ['cdcdgbaseobjectgrpindex', 'cdcdgbaseobjectindex', 'cdcdgbaseobjectsubtree', 'cdcdgbaseobjectlist', 'cdcdgbaseobjectrowstatus'], name, value)




    class CdcDGInstanceTable(Entity):
        """
        Identifies the instances of the base objects that need to
        be fetched for a 'table' type data group.
        
        The agent is not responsible for verifying that the instances
        specified for a data group do not overlap.
        
        .. attribute:: cdcdginstanceentry
        
        	An entry in this table. Each entry identifies one or more instances of the base objects that need to be fetched. An instance is represented by an OID fragment
        	**type**\: list of  		 :py:class:`CdcDGInstanceEntry <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcDGInstanceTable.CdcDGInstanceEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DATA-COLLECTION-MIB'
        _revision = '2002-10-30'

        def __init__(self):
            super(CISCODATACOLLECTIONMIB.CdcDGInstanceTable, self).__init__()

            self.yang_name = "cdcDGInstanceTable"
            self.yang_parent_name = "CISCO-DATA-COLLECTION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdcDGInstanceEntry", ("cdcdginstanceentry", CISCODATACOLLECTIONMIB.CdcDGInstanceTable.CdcDGInstanceEntry))])
            self._leafs = OrderedDict()

            self.cdcdginstanceentry = YList(self)
            self._segment_path = lambda: "cdcDGInstanceTable"
            self._absolute_path = lambda: "CISCO-DATA-COLLECTION-MIB:CISCO-DATA-COLLECTION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODATACOLLECTIONMIB.CdcDGInstanceTable, [], name, value)


        class CdcDGInstanceEntry(Entity):
            """
            An entry in this table. Each entry identifies one or more
            instances of the base objects that need to be fetched.
            An instance is represented by an OID fragment.
            
            .. attribute:: cdcdginstancegrpindex  (key)
            
            	This object's value when combined with the value of cdcDGInstanceIndex uniquely identifies an entry in this table. An application must use the same value (can  be randomly picked) for this object while creating a group of entries that collectively identifies the set of instances for a data group
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cdcdginstanceindex  (key)
            
            	This object's value when combined with the value of cdcDGInstanceGrpIndex uniquely identifies an entry in this table.  A managment application can assign incremental values starting from one, when creating each entry within a group of entries (as identified by the value of cdcDGInstanceGrpIndex)
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cdcdginstancetype
            
            	Specifies the way in which the instances are to be used while collecting data.   individual     The value of cdcDGInstanceOid is                appended to each base object of the                associated data group, thus giving the exact                instance of the objects to be collected.  range          The value of cdcDGInstanceOid is                appended to each base object in the                associated data group, thus giving the                starting object instance of the range.                The value of cdcDGInstanceEndOid                is appended to to each base object in the                associated data group, thus giving the                last object instances of the range.   repititions      The value of cdcDGInstanceOid is                appended to each base object in the                associated data group, thus giving the                first object instance of the next 'n'                instances that need to be collected.                The value of 'n' is set in                cdcDGInstanceNumRepititions.  subTree        The value of cdcDGInstanceOid is                appended to each base object in the                associated data group, thus identifying the                OBJECT IDENTFIFIER sub\-tree, whose leaf                instances need to be collected.  other          The value of cdcDGInstanceOtherPtr points to a                row (in another MIB table) that contains MIB                specific instance selection criteria. A MIB                defined for such purposes should describe                the selection criteria.  This object's value cannot be modified while the value of cdcDGInstanceStatus is 'active'
            	**type**\:  :py:class:`CdcDGInstanceType <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcDGInstanceTable.CdcDGInstanceEntry.CdcDGInstanceType>`
            
            	**config**\: False
            
            .. attribute:: cdcdginstanceoid
            
            	Contains the OBJECT IDENTIFIER fragment that identifies the instances of the base objects that need to be collected.  If cdcDGInstanceType is 'individual' then this value should be the OID fragment that, when appended to each base MIB object gives the fully instantiated OID to be fetched.  If cdcDGInstanceType is 'range' then this value should be the OID fragment that, when appended to each base MIB object gives the start of a range of object instances that needs to be fetched.  If cdcDGInstanceType is 'subTree' then this value should be the OID fragment that, when appended to each base MIB gives the sub\-tree under which all leaf object instances need to be fetched.  This object's value may be modified at any time. The change takes effect the next time data is fetched for this data group
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: cdcdginstanceoidend
            
            	Contains the OID fragment that, when appended to each base object gives the end of the range of object instances that needs to be fetched.  This value is used only when the value of cdcDGInstanceType is of type 'range'.   This object's value may be modified at any time. The change takes effect the next time data is fetched for this data group
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: cdcdginstancenumrepititions
            
            	Specifies the number of lexicographically consecutive object instances to fetch.  This value is used only when the value of cdcDGInstanceType is of type 'repititions'.    This object's value may be modified at any time. The change takes effect the next time data is fetched for this data group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cdcdginstanceotherptr
            
            	Contains a pointer to a row in another MIB table that contains MIB specific criteria for selecting instances.  This value is used only when the value of cdcDGInstanceType is of type 'other'.   This object's value may be modified at any time. The change takes effect the next time data is fetched for this data group
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: cdcdginstancerowstatus
            
            	The status of this conceptual row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DATA-COLLECTION-MIB'
            _revision = '2002-10-30'

            def __init__(self):
                super(CISCODATACOLLECTIONMIB.CdcDGInstanceTable.CdcDGInstanceEntry, self).__init__()

                self.yang_name = "cdcDGInstanceEntry"
                self.yang_parent_name = "cdcDGInstanceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdcdginstancegrpindex','cdcdginstanceindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdcdginstancegrpindex', (YLeaf(YType.uint32, 'cdcDGInstanceGrpIndex'), ['int'])),
                    ('cdcdginstanceindex', (YLeaf(YType.uint32, 'cdcDGInstanceIndex'), ['int'])),
                    ('cdcdginstancetype', (YLeaf(YType.enumeration, 'cdcDGInstanceType'), [('ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB', 'CISCODATACOLLECTIONMIB', 'CdcDGInstanceTable.CdcDGInstanceEntry.CdcDGInstanceType')])),
                    ('cdcdginstanceoid', (YLeaf(YType.str, 'cdcDGInstanceOid'), ['str'])),
                    ('cdcdginstanceoidend', (YLeaf(YType.str, 'cdcDGInstanceOidEnd'), ['str'])),
                    ('cdcdginstancenumrepititions', (YLeaf(YType.uint32, 'cdcDGInstanceNumRepititions'), ['int'])),
                    ('cdcdginstanceotherptr', (YLeaf(YType.str, 'cdcDGInstanceOtherPtr'), ['str'])),
                    ('cdcdginstancerowstatus', (YLeaf(YType.enumeration, 'cdcDGInstanceRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.cdcdginstancegrpindex = None
                self.cdcdginstanceindex = None
                self.cdcdginstancetype = None
                self.cdcdginstanceoid = None
                self.cdcdginstanceoidend = None
                self.cdcdginstancenumrepititions = None
                self.cdcdginstanceotherptr = None
                self.cdcdginstancerowstatus = None
                self._segment_path = lambda: "cdcDGInstanceEntry" + "[cdcDGInstanceGrpIndex='" + str(self.cdcdginstancegrpindex) + "']" + "[cdcDGInstanceIndex='" + str(self.cdcdginstanceindex) + "']"
                self._absolute_path = lambda: "CISCO-DATA-COLLECTION-MIB:CISCO-DATA-COLLECTION-MIB/cdcDGInstanceTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODATACOLLECTIONMIB.CdcDGInstanceTable.CdcDGInstanceEntry, ['cdcdginstancegrpindex', 'cdcdginstanceindex', 'cdcdginstancetype', 'cdcdginstanceoid', 'cdcdginstanceoidend', 'cdcdginstancenumrepititions', 'cdcdginstanceotherptr', 'cdcdginstancerowstatus'], name, value)

            class CdcDGInstanceType(Enum):
                """
                CdcDGInstanceType (Enum Class)

                Specifies the way in which the instances are to be used while

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

                               OBJECT IDENTFIFIER sub\-tree, whose leaf

                               instances need to be collected.

                other          The value of cdcDGInstanceOtherPtr points to a

                               row (in another MIB table) that contains MIB

                               specific instance selection criteria. A MIB

                               defined for such purposes should describe

                               the selection criteria.

                This object's value cannot be modified while the value of

                cdcDGInstanceStatus is 'active'.

                .. data:: individual = 1

                .. data:: range = 2

                .. data:: repititions = 3

                .. data:: subTree = 4

                .. data:: other = 5

                """

                individual = Enum.YLeaf(1, "individual")

                range = Enum.YLeaf(2, "range")

                repititions = Enum.YLeaf(3, "repititions")

                subTree = Enum.YLeaf(4, "subTree")

                other = Enum.YLeaf(5, "other")





    class CdcFileXferConfTable(Entity):
        """
        A table for configuring file transfer operations.
        
        .. attribute:: cdcfilexferconfentry
        
        	An individual entry in the cdcFileXferConfTable. Each entry identifies a primary and an optional secondary destination.  An entry is automatically created in this table, whenever an entry is created in the cdcVFileTable. The application needs to specify the URLs of the destination to which frozen VFiles are transferred.   When a VFile is frozen, transfer will be first initiated to the primary destination, if the transfer fails, then transfer is initiated to the secondary destination. If this too fails, then the cycle is repeated again after a specified time period (value of cdcFileXferConfRetryPeriod) elapses
        	**type**\: list of  		 :py:class:`CdcFileXferConfEntry <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcFileXferConfTable.CdcFileXferConfEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-DATA-COLLECTION-MIB'
        _revision = '2002-10-30'

        def __init__(self):
            super(CISCODATACOLLECTIONMIB.CdcFileXferConfTable, self).__init__()

            self.yang_name = "cdcFileXferConfTable"
            self.yang_parent_name = "CISCO-DATA-COLLECTION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cdcFileXferConfEntry", ("cdcfilexferconfentry", CISCODATACOLLECTIONMIB.CdcFileXferConfTable.CdcFileXferConfEntry))])
            self._leafs = OrderedDict()

            self.cdcfilexferconfentry = YList(self)
            self._segment_path = lambda: "cdcFileXferConfTable"
            self._absolute_path = lambda: "CISCO-DATA-COLLECTION-MIB:CISCO-DATA-COLLECTION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCODATACOLLECTIONMIB.CdcFileXferConfTable, [], name, value)


        class CdcFileXferConfEntry(Entity):
            """
            An individual entry in the cdcFileXferConfTable. Each entry
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
            
            .. attribute:: cdcvfileindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cdcvfileindex <ydk.models.cisco_ios_xe.CISCO_DATA_COLLECTION_MIB.CISCODATACOLLECTIONMIB.CdcVFileTable.CdcVFileEntry>`
            
            	**config**\: False
            
            .. attribute:: cdcfilexferconfpriurl
            
            	The URL which specifies the primary destination to which the file has to be transferred. The URL should contain the base\-name of the remote file, the suffix will be carried over from the name of the VFile being tranferred, and will be automatically appended by the agent.  This object's value may be modified at any time
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdcfilexferconfsecurl
            
            	The URL which specifies the secondary destination to which the file has to be transferred if the transfer to the  primary destination fails. Failure occurs when the file  cannot be transferred in it's entirety to the specified  destination for some reason. Some common reasons for such  failures are listed out in CdcFileXferStatus.    The specified URL should contain the base\-name of the remote file, the suffix will be carried over from the name of the VFile being tranferred, and will be automatically appended by the agent.   This object's value may be modified at any time
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cdcfilexferconfretryperiod
            
            	Specifies the time interval after which transfer has to be retried. Transfer needs to be retried only if in a previous  attempt the file could not be successfully transferred to  either the primary destination or the secondary destination.  This object's value may be modified at any time
            	**type**\: int
            
            	**range:** 60..86400
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cdcfilexferconfretrycount
            
            	Maximum number of times, transfer has to be retried. If the retry count exceeds this value, then no further attempts will be made.   This object's value may be modified at any time
            	**type**\: int
            
            	**range:** 0..256
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cdcfilexferconfsuccessenable
            
            	When set to 'true', cdcFileXferComplete notification will be sent out in the event of a successful file transfer
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cdcfilexferconffailureenable
            
            	When set to 'true', cdcFileXferComplete notification will be sent out in the event of a file transfer failure
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-DATA-COLLECTION-MIB'
            _revision = '2002-10-30'

            def __init__(self):
                super(CISCODATACOLLECTIONMIB.CdcFileXferConfTable.CdcFileXferConfEntry, self).__init__()

                self.yang_name = "cdcFileXferConfEntry"
                self.yang_parent_name = "cdcFileXferConfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdcvfileindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdcvfileindex', (YLeaf(YType.str, 'cdcVFileIndex'), ['int'])),
                    ('cdcfilexferconfpriurl', (YLeaf(YType.str, 'cdcFileXferConfPriUrl'), ['str'])),
                    ('cdcfilexferconfsecurl', (YLeaf(YType.str, 'cdcFileXferConfSecUrl'), ['str'])),
                    ('cdcfilexferconfretryperiod', (YLeaf(YType.uint32, 'cdcFileXferConfRetryPeriod'), ['int'])),
                    ('cdcfilexferconfretrycount', (YLeaf(YType.uint32, 'cdcFileXferConfRetryCount'), ['int'])),
                    ('cdcfilexferconfsuccessenable', (YLeaf(YType.boolean, 'cdcFileXferConfSuccessEnable'), ['bool'])),
                    ('cdcfilexferconffailureenable', (YLeaf(YType.boolean, 'cdcFileXferConfFailureEnable'), ['bool'])),
                ])
                self.cdcvfileindex = None
                self.cdcfilexferconfpriurl = None
                self.cdcfilexferconfsecurl = None
                self.cdcfilexferconfretryperiod = None
                self.cdcfilexferconfretrycount = None
                self.cdcfilexferconfsuccessenable = None
                self.cdcfilexferconffailureenable = None
                self._segment_path = lambda: "cdcFileXferConfEntry" + "[cdcVFileIndex='" + str(self.cdcvfileindex) + "']"
                self._absolute_path = lambda: "CISCO-DATA-COLLECTION-MIB:CISCO-DATA-COLLECTION-MIB/cdcFileXferConfTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCODATACOLLECTIONMIB.CdcFileXferConfTable.CdcFileXferConfEntry, ['cdcvfileindex', 'cdcfilexferconfpriurl', 'cdcfilexferconfsecurl', 'cdcfilexferconfretryperiod', 'cdcfilexferconfretrycount', 'cdcfilexferconfsuccessenable', 'cdcfilexferconffailureenable'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCODATACOLLECTIONMIB()
        return self._top_entity



