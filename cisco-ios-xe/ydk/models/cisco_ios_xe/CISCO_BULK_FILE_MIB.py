""" CISCO_BULK_FILE_MIB 

The MIB module for creating and deleting bulk files of
SNMP data for file transfer.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOBULKFILEMIB(Entity):
    """
    
    
    .. attribute:: cbfdefine
    
    	
    	**type**\:  :py:class:`CbfDefine <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CISCOBULKFILEMIB.CbfDefine>`
    
    	**config**\: False
    
    .. attribute:: cbfstatus
    
    	
    	**type**\:  :py:class:`CbfStatus <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CISCOBULKFILEMIB.CbfStatus>`
    
    	**config**\: False
    
    .. attribute:: cbfdefinefiletable
    
    	A table of bulk file definition and creation controls
    	**type**\:  :py:class:`CbfDefineFileTable <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CISCOBULKFILEMIB.CbfDefineFileTable>`
    
    	**config**\: False
    
    .. attribute:: cbfdefineobjecttable
    
    	A table of objects to go in bulk files
    	**type**\:  :py:class:`CbfDefineObjectTable <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CISCOBULKFILEMIB.CbfDefineObjectTable>`
    
    	**config**\: False
    
    .. attribute:: cbfstatusfiletable
    
    	A table of bulk file status
    	**type**\:  :py:class:`CbfStatusFileTable <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CISCOBULKFILEMIB.CbfStatusFileTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-BULK-FILE-MIB'
    _revision = '2002-06-10'

    def __init__(self):
        super(CISCOBULKFILEMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-BULK-FILE-MIB"
        self.yang_parent_name = "CISCO-BULK-FILE-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cbfDefine", ("cbfdefine", CISCOBULKFILEMIB.CbfDefine)), ("cbfStatus", ("cbfstatus", CISCOBULKFILEMIB.CbfStatus)), ("cbfDefineFileTable", ("cbfdefinefiletable", CISCOBULKFILEMIB.CbfDefineFileTable)), ("cbfDefineObjectTable", ("cbfdefineobjecttable", CISCOBULKFILEMIB.CbfDefineObjectTable)), ("cbfStatusFileTable", ("cbfstatusfiletable", CISCOBULKFILEMIB.CbfStatusFileTable))])
        self._leafs = OrderedDict()

        self.cbfdefine = CISCOBULKFILEMIB.CbfDefine()
        self.cbfdefine.parent = self
        self._children_name_map["cbfdefine"] = "cbfDefine"

        self.cbfstatus = CISCOBULKFILEMIB.CbfStatus()
        self.cbfstatus.parent = self
        self._children_name_map["cbfstatus"] = "cbfStatus"

        self.cbfdefinefiletable = CISCOBULKFILEMIB.CbfDefineFileTable()
        self.cbfdefinefiletable.parent = self
        self._children_name_map["cbfdefinefiletable"] = "cbfDefineFileTable"

        self.cbfdefineobjecttable = CISCOBULKFILEMIB.CbfDefineObjectTable()
        self.cbfdefineobjecttable.parent = self
        self._children_name_map["cbfdefineobjecttable"] = "cbfDefineObjectTable"

        self.cbfstatusfiletable = CISCOBULKFILEMIB.CbfStatusFileTable()
        self.cbfstatusfiletable.parent = self
        self._children_name_map["cbfstatusfiletable"] = "cbfStatusFileTable"
        self._segment_path = lambda: "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOBULKFILEMIB, [], name, value)


    class CbfDefine(Entity):
        """
        
        
        .. attribute:: cbfdefinemaxfiles
        
        	The maximum number of file definitions this system can hold in cbfDefineFileTable.  A value of 0 indicates no configured limit.  This object may be read\-only on some systems.  Changing this number does not disturb existing entries
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cbfdefinefiles
        
        	The current number of file definitions in cbfDefineFileTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cbfdefinehighfiles
        
        	The maximum value of cbfDefineFiles since system  initialization
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cbfdefinefilesrefused
        
        	The number of attempts to create a file definition that failed due to exceeding cbfDefineMaxFiles
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cbfdefinemaxobjects
        
        	The maximum total number of object selections to go with file definitions this system, that is, the total number of objects this system can hold in cbfDefineObjectTable.  A value of 0 indicates no configured limit.  This object may be read\-only on some systems.  Changing this number does not disturb existing entries
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cbfdefineobjects
        
        	The current number of object selections in  cbfDefineObjectTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cbfdefinehighobjects
        
        	The maximum value of cbfDefineObjects since system  initialization
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cbfdefineobjectsrefused
        
        	The number of attempts to create an object selection that failed due to exceeding cbfDefineMaxObjects
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-BULK-FILE-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CISCOBULKFILEMIB.CbfDefine, self).__init__()

            self.yang_name = "cbfDefine"
            self.yang_parent_name = "CISCO-BULK-FILE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cbfdefinemaxfiles', (YLeaf(YType.uint32, 'cbfDefineMaxFiles'), ['int'])),
                ('cbfdefinefiles', (YLeaf(YType.uint32, 'cbfDefineFiles'), ['int'])),
                ('cbfdefinehighfiles', (YLeaf(YType.uint32, 'cbfDefineHighFiles'), ['int'])),
                ('cbfdefinefilesrefused', (YLeaf(YType.uint32, 'cbfDefineFilesRefused'), ['int'])),
                ('cbfdefinemaxobjects', (YLeaf(YType.uint32, 'cbfDefineMaxObjects'), ['int'])),
                ('cbfdefineobjects', (YLeaf(YType.uint32, 'cbfDefineObjects'), ['int'])),
                ('cbfdefinehighobjects', (YLeaf(YType.uint32, 'cbfDefineHighObjects'), ['int'])),
                ('cbfdefineobjectsrefused', (YLeaf(YType.uint32, 'cbfDefineObjectsRefused'), ['int'])),
            ])
            self.cbfdefinemaxfiles = None
            self.cbfdefinefiles = None
            self.cbfdefinehighfiles = None
            self.cbfdefinefilesrefused = None
            self.cbfdefinemaxobjects = None
            self.cbfdefineobjects = None
            self.cbfdefinehighobjects = None
            self.cbfdefineobjectsrefused = None
            self._segment_path = lambda: "cbfDefine"
            self._absolute_path = lambda: "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBULKFILEMIB.CbfDefine, ['cbfdefinemaxfiles', 'cbfdefinefiles', 'cbfdefinehighfiles', 'cbfdefinefilesrefused', 'cbfdefinemaxobjects', 'cbfdefineobjects', 'cbfdefinehighobjects', 'cbfdefineobjectsrefused'], name, value)



    class CbfStatus(Entity):
        """
        
        
        .. attribute:: cbfstatusmaxfiles
        
        	The maximum number of file statuses this system can hold in cbfStatusFileTable.  A value of 0 indicates no configured limit.  This object may be read\-only on some systems.  Changing this number deletes the oldest finished entries until the new limit is satisfied
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cbfstatusfiles
        
        	The current number of file statuses in cbfStatusFileTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cbfstatushighfiles
        
        	The maximum value of cbfStatusFiles since system  initialization
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cbfstatusfilesbumped
        
        	The number times the oldest entry was deleted due to exceeding cbfStatusMaxFiles
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-BULK-FILE-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CISCOBULKFILEMIB.CbfStatus, self).__init__()

            self.yang_name = "cbfStatus"
            self.yang_parent_name = "CISCO-BULK-FILE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cbfstatusmaxfiles', (YLeaf(YType.uint32, 'cbfStatusMaxFiles'), ['int'])),
                ('cbfstatusfiles', (YLeaf(YType.uint32, 'cbfStatusFiles'), ['int'])),
                ('cbfstatushighfiles', (YLeaf(YType.uint32, 'cbfStatusHighFiles'), ['int'])),
                ('cbfstatusfilesbumped', (YLeaf(YType.uint32, 'cbfStatusFilesBumped'), ['int'])),
            ])
            self.cbfstatusmaxfiles = None
            self.cbfstatusfiles = None
            self.cbfstatushighfiles = None
            self.cbfstatusfilesbumped = None
            self._segment_path = lambda: "cbfStatus"
            self._absolute_path = lambda: "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBULKFILEMIB.CbfStatus, ['cbfstatusmaxfiles', 'cbfstatusfiles', 'cbfstatushighfiles', 'cbfstatusfilesbumped'], name, value)



    class CbfDefineFileTable(Entity):
        """
        A table of bulk file definition and creation controls.
        
        .. attribute:: cbfdefinefileentry
        
        	Information for creation of a bulk file.  To creat a bulk file an application creates an entry in this table and corresponding entries in cbfDefineObjectTable.  When the entry in this table and the corresponding entries in cbfDefineObjectTable are 'active' the appliction uses cbfDefineFileNow to create the file and a corresponding entry in cbfStatusFileTable.  Deleting an entry in cbfDefineFileTable deletes all corresponding entries in cbfDefineObjectTable and cbfStatusFileTable.  An entry may not be modified or deleted while its cbfDefineFileNow has the value 'running'
        	**type**\: list of  		 :py:class:`CbfDefineFileEntry <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CISCOBULKFILEMIB.CbfDefineFileTable.CbfDefineFileEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-BULK-FILE-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CISCOBULKFILEMIB.CbfDefineFileTable, self).__init__()

            self.yang_name = "cbfDefineFileTable"
            self.yang_parent_name = "CISCO-BULK-FILE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cbfDefineFileEntry", ("cbfdefinefileentry", CISCOBULKFILEMIB.CbfDefineFileTable.CbfDefineFileEntry))])
            self._leafs = OrderedDict()

            self.cbfdefinefileentry = YList(self)
            self._segment_path = lambda: "cbfDefineFileTable"
            self._absolute_path = lambda: "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBULKFILEMIB.CbfDefineFileTable, [], name, value)


        class CbfDefineFileEntry(Entity):
            """
            Information for creation of a bulk file.
            
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
            
            .. attribute:: cbfdefinefileindex  (key)
            
            	An arbitrary integer to uniquely identify this entry.  To create an entry a management application should pick a random number
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cbfdefinefilename
            
            	The file name which is to be created.  Explicit device or path choices in the value of this object override cbfDefineFileStorage
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cbfdefinefilestorage
            
            	The type of file storage to use\:  ephemeral        data exists in small amounts until read volatile        data exists in volatile memory permanent        data survives reboot  An ephemeral file is suitable to be read only one time.  Note that this value is taken as advisory and may be overridden by explicit device or path choices in cbfDefineFile.  A given system may support any or all of these
            	**type**\:  :py:class:`CbfDefineFileStorage <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CISCOBULKFILEMIB.CbfDefineFileTable.CbfDefineFileEntry.CbfDefineFileStorage>`
            
            	**config**\: False
            
            .. attribute:: cbfdefinefileformat
            
            	The format of the data in the file\:  StandardBER        standard SNMP ASN.1 BER bulkBinary        a binary format specified with this MIB bulkASCII        a human\-readable form of bulkBinary variantBERWithCksum ASN.1 BER encoding with checksum variantBinWithCksum a binary format with checksum      A given system may support any or all of these
            	**type**\:  :py:class:`CbfDefineFileFormat <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CISCOBULKFILEMIB.CbfDefineFileTable.CbfDefineFileEntry.CbfDefineFileFormat>`
            
            	**config**\: False
            
            .. attribute:: cbfdefinefilenow
            
            	The control to cause file creation.  The only values that can be set are 'create' and 'forcedCreate'. These can be set only  when the value is 'ready'.  Setting it to 'create' begins a  file creation and creates a corresponding entry in  cbfStatusFileTable. The system may choose to use an already  existing copy of the file instead of creating a new one. This may happen if there has been no configuration change on the  system and a request to recreate the file is received.  Setting this object to 'forcedCreate' forces the system to  create a new copy of the file.  The value is 'notActve' as long as cbfDefineFileEntryStatus or any corresponding cbfDefineObjectEntryStatus is not active.  When cbfDefineFileEntryStatus becomes active and all corresponding cbfDefineObjectEntryStatuses are active this  object automatically goes to 'ready'
            	**type**\:  :py:class:`CbfDefineFileNow <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CISCOBULKFILEMIB.CbfDefineFileTable.CbfDefineFileEntry.CbfDefineFileNow>`
            
            	**config**\: False
            
            .. attribute:: cbfdefinefileentrystatus
            
            	The control that allows creation, modification, and deletion of entries.  For detailed rules see the DESCRIPTION for cbfDefineFileEntry
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: cbfdefinefilenotifyoncompletion
            
            	This controls the cbfDefineFileCompletion notification.  If true, cbfDefineFileCompletion notification will be generated. It is the responsibility of the  management entity to ensure that the SNMP administrative  model is configured in such a way as to allow the  notification to be delivered
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-BULK-FILE-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                super(CISCOBULKFILEMIB.CbfDefineFileTable.CbfDefineFileEntry, self).__init__()

                self.yang_name = "cbfDefineFileEntry"
                self.yang_parent_name = "cbfDefineFileTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cbfdefinefileindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cbfdefinefileindex', (YLeaf(YType.uint32, 'cbfDefineFileIndex'), ['int'])),
                    ('cbfdefinefilename', (YLeaf(YType.str, 'cbfDefineFileName'), ['str'])),
                    ('cbfdefinefilestorage', (YLeaf(YType.enumeration, 'cbfDefineFileStorage'), [('ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CISCOBULKFILEMIB', 'CbfDefineFileTable.CbfDefineFileEntry.CbfDefineFileStorage')])),
                    ('cbfdefinefileformat', (YLeaf(YType.enumeration, 'cbfDefineFileFormat'), [('ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CISCOBULKFILEMIB', 'CbfDefineFileTable.CbfDefineFileEntry.CbfDefineFileFormat')])),
                    ('cbfdefinefilenow', (YLeaf(YType.enumeration, 'cbfDefineFileNow'), [('ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CISCOBULKFILEMIB', 'CbfDefineFileTable.CbfDefineFileEntry.CbfDefineFileNow')])),
                    ('cbfdefinefileentrystatus', (YLeaf(YType.enumeration, 'cbfDefineFileEntryStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('cbfdefinefilenotifyoncompletion', (YLeaf(YType.boolean, 'cbfDefineFileNotifyOnCompletion'), ['bool'])),
                ])
                self.cbfdefinefileindex = None
                self.cbfdefinefilename = None
                self.cbfdefinefilestorage = None
                self.cbfdefinefileformat = None
                self.cbfdefinefilenow = None
                self.cbfdefinefileentrystatus = None
                self.cbfdefinefilenotifyoncompletion = None
                self._segment_path = lambda: "cbfDefineFileEntry" + "[cbfDefineFileIndex='" + str(self.cbfdefinefileindex) + "']"
                self._absolute_path = lambda: "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/cbfDefineFileTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBULKFILEMIB.CbfDefineFileTable.CbfDefineFileEntry, ['cbfdefinefileindex', 'cbfdefinefilename', 'cbfdefinefilestorage', 'cbfdefinefileformat', 'cbfdefinefilenow', 'cbfdefinefileentrystatus', 'cbfdefinefilenotifyoncompletion'], name, value)

            class CbfDefineFileFormat(Enum):
                """
                CbfDefineFileFormat (Enum Class)

                The format of the data in the file\:

                StandardBER        standard SNMP ASN.1 BER

                bulkBinary        a binary format specified with this MIB

                bulkASCII        a human\-readable form of bulkBinary

                variantBERWithCksum ASN.1 BER encoding with checksum

                variantBinWithCksum a binary format with checksum

                    A given system may support any or all of these.

                .. data:: standardBER = 1

                .. data:: bulkBinary = 2

                .. data:: bulkASCII = 3

                .. data:: variantBERWithCksum = 4

                .. data:: variantBinWithCksum = 5

                """

                standardBER = Enum.YLeaf(1, "standardBER")

                bulkBinary = Enum.YLeaf(2, "bulkBinary")

                bulkASCII = Enum.YLeaf(3, "bulkASCII")

                variantBERWithCksum = Enum.YLeaf(4, "variantBERWithCksum")

                variantBinWithCksum = Enum.YLeaf(5, "variantBinWithCksum")


            class CbfDefineFileNow(Enum):
                """
                CbfDefineFileNow (Enum Class)

                The control to cause file creation.  The only values that can

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

                .. data:: notActive = 1

                .. data:: ready = 2

                .. data:: create = 3

                .. data:: running = 4

                .. data:: forcedCreate = 5

                """

                notActive = Enum.YLeaf(1, "notActive")

                ready = Enum.YLeaf(2, "ready")

                create = Enum.YLeaf(3, "create")

                running = Enum.YLeaf(4, "running")

                forcedCreate = Enum.YLeaf(5, "forcedCreate")


            class CbfDefineFileStorage(Enum):
                """
                CbfDefineFileStorage (Enum Class)

                The type of file storage to use\:

                ephemeral        data exists in small amounts until read

                volatile        data exists in volatile memory

                permanent        data survives reboot

                An ephemeral file is suitable to be read only one time.

                Note that this value is taken as advisory and may be overridden

                by explicit device or path choices in cbfDefineFile.

                A given system may support any or all of these.

                .. data:: ephemeral = 1

                .. data:: volatile = 2

                .. data:: permanent = 3

                """

                ephemeral = Enum.YLeaf(1, "ephemeral")

                volatile = Enum.YLeaf(2, "volatile")

                permanent = Enum.YLeaf(3, "permanent")





    class CbfDefineObjectTable(Entity):
        """
        A table of objects to go in bulk files.
        
        .. attribute:: cbfdefineobjectentry
        
        	Information about one object for a particular file.  An application uses cbfDefineObjectEntryStatus to create entries in this table in correspondence with entries in cbfDefineFileTable, which must be created first.  Entries in this table may not be changed, created or deleted while the corresponding value of cbfDefineFileNow is 'running'
        	**type**\: list of  		 :py:class:`CbfDefineObjectEntry <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CISCOBULKFILEMIB.CbfDefineObjectTable.CbfDefineObjectEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-BULK-FILE-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CISCOBULKFILEMIB.CbfDefineObjectTable, self).__init__()

            self.yang_name = "cbfDefineObjectTable"
            self.yang_parent_name = "CISCO-BULK-FILE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cbfDefineObjectEntry", ("cbfdefineobjectentry", CISCOBULKFILEMIB.CbfDefineObjectTable.CbfDefineObjectEntry))])
            self._leafs = OrderedDict()

            self.cbfdefineobjectentry = YList(self)
            self._segment_path = lambda: "cbfDefineObjectTable"
            self._absolute_path = lambda: "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBULKFILEMIB.CbfDefineObjectTable, [], name, value)


        class CbfDefineObjectEntry(Entity):
            """
            Information about one object for a particular file.
            
            An application uses cbfDefineObjectEntryStatus to create entries
            in this table in correspondence with entries in
            cbfDefineFileTable, which must be created first.
            
            Entries in this table may not be changed, created or deleted
            while the corresponding value of cbfDefineFileNow is 'running'.
            
            .. attribute:: cbfdefinefileindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cbfdefinefileindex <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CISCOBULKFILEMIB.CbfDefineFileTable.CbfDefineFileEntry>`
            
            	**config**\: False
            
            .. attribute:: cbfdefineobjectindex  (key)
            
            	An arbitrary integer to uniquely identify this entry.  The numeric order of the entries controls the order of the objects in the file
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cbfdefineobjectclass
            
            	The meaning of each object class is given below\:  object          a single MIB object is retrieved.  lexicalTable    an entire table or partial table                 is retrieved in lexical order of rows.  leastCpuTable   an entire table is retrieved with                 lowest CPU utilization.                 Lexical ordering of rows may not be                  maintained and is dependent upon                  individual MIB implementation
            	**type**\:  :py:class:`CbfDefineObjectClass <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CISCOBULKFILEMIB.CbfDefineObjectTable.CbfDefineObjectEntry.CbfDefineObjectClass>`
            
            	**config**\: False
            
            .. attribute:: cbfdefineobjectid
            
            	The object identifier of a MIB object to be included in the file.  If cbfDefineObjectClass is 'object' this must be a full OID, including all instance information.  If cbfDefineObjectClass is 'lexicalTable' or 'leastCpuTable' this must be the OID of the table\-defining SEQUENCE OF registration point
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: cbfdefineobjectentrystatus
            
            	The control that allows creation, modification, and deletion of entries.  For detailed rules see the DESCRIPTION for cbfDefineObjectEntry
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: cbfdefineobjecttableinstance
            
            	If cbfDefineObjectClass is 'lexicalTable', then this object represents the starting instance in the cbfDefineObjectID table. The file created will have entries starting from the lexicographically next instance of the OID represented by this object.   For Eg\:  \-\-\-\-\-\-\-         Let us  assume we are polling ifTable and we        have information till the second row(ifIndex.2). Now        we may be interested in 10 rows lexically following        the second row.                So, we set cbfDefineObjectTableInstance as ifIndex.2         and cbfDefineObjectNumEntries as 10.          We will get information for the next 10 rows or        if there are less than 10 populated rows, we will        receive information till the end of the table is         reached.  The default value for this object is zeroDotZero.  If this object has the value of zeroDotZero and  cbfDefineObjectNumEntries has value 0, then the whole table(represented by cbfDefineObjectID) is retrieved.  If this object has the value of zeroDotZero,   cbfDefineObjectNumEntries has value n (>0) and there are  m(>0) entries in the table(represented by cbfDefineObjectID) then the first n entries in the table are retrieved if n < m.  If n >= m, then the whole table is retrieved.  When the value of cbfDefineObjectNumEntries is 0,  it means all the entries in the table(represented  by cbfDefineObjectID) which lexicographically follow  cbfDefineObjectTableInstance are retrieved.  This object is irrelevent if cbfDefineObjectClass is not 'lexicalTable'
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: cbfdefineobjectnumentries
            
            	If cbfDefineObjectClass is 'lexicalTable', then this object represents the maximum number of entries which will be  populated in the file starting from the lexicographically next instance of the OID represented by  cbfDefineObjectTableInstance.   This object is irrelevent if cbfDefineObjectClass is not 'lexicalTable'.  Refer to the description of cbfDefineObjectTableInstance for examples and different scenarios relating to this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbfdefineobjectlastpolledinst
            
            	This object represents the last polled instance in the table.  The value represented by this object will be relevent only if the corresponding cbfStatusFileState is emptied(3) for  ephemeral files or ready(2) for volatile or permanent files.  A value of zeroDotZero indicates an absence of last polled  object.  An NMS can use the value of this object and populate the cbfDefineObjectTableInstance to retrieve a contiguous set of rows in a table
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-BULK-FILE-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                super(CISCOBULKFILEMIB.CbfDefineObjectTable.CbfDefineObjectEntry, self).__init__()

                self.yang_name = "cbfDefineObjectEntry"
                self.yang_parent_name = "cbfDefineObjectTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cbfdefinefileindex','cbfdefineobjectindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cbfdefinefileindex', (YLeaf(YType.str, 'cbfDefineFileIndex'), ['int'])),
                    ('cbfdefineobjectindex', (YLeaf(YType.uint32, 'cbfDefineObjectIndex'), ['int'])),
                    ('cbfdefineobjectclass', (YLeaf(YType.enumeration, 'cbfDefineObjectClass'), [('ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CISCOBULKFILEMIB', 'CbfDefineObjectTable.CbfDefineObjectEntry.CbfDefineObjectClass')])),
                    ('cbfdefineobjectid', (YLeaf(YType.str, 'cbfDefineObjectID'), ['str'])),
                    ('cbfdefineobjectentrystatus', (YLeaf(YType.enumeration, 'cbfDefineObjectEntryStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('cbfdefineobjecttableinstance', (YLeaf(YType.str, 'cbfDefineObjectTableInstance'), ['str'])),
                    ('cbfdefineobjectnumentries', (YLeaf(YType.uint32, 'cbfDefineObjectNumEntries'), ['int'])),
                    ('cbfdefineobjectlastpolledinst', (YLeaf(YType.str, 'cbfDefineObjectLastPolledInst'), ['str'])),
                ])
                self.cbfdefinefileindex = None
                self.cbfdefineobjectindex = None
                self.cbfdefineobjectclass = None
                self.cbfdefineobjectid = None
                self.cbfdefineobjectentrystatus = None
                self.cbfdefineobjecttableinstance = None
                self.cbfdefineobjectnumentries = None
                self.cbfdefineobjectlastpolledinst = None
                self._segment_path = lambda: "cbfDefineObjectEntry" + "[cbfDefineFileIndex='" + str(self.cbfdefinefileindex) + "']" + "[cbfDefineObjectIndex='" + str(self.cbfdefineobjectindex) + "']"
                self._absolute_path = lambda: "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/cbfDefineObjectTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBULKFILEMIB.CbfDefineObjectTable.CbfDefineObjectEntry, ['cbfdefinefileindex', 'cbfdefineobjectindex', 'cbfdefineobjectclass', 'cbfdefineobjectid', 'cbfdefineobjectentrystatus', 'cbfdefineobjecttableinstance', 'cbfdefineobjectnumentries', 'cbfdefineobjectlastpolledinst'], name, value)

            class CbfDefineObjectClass(Enum):
                """
                CbfDefineObjectClass (Enum Class)

                The meaning of each object class is given below\:

                object          a single MIB object is retrieved.

                lexicalTable    an entire table or partial table

                                is retrieved in lexical order of rows.

                leastCpuTable   an entire table is retrieved with

                                lowest CPU utilization.

                                Lexical ordering of rows may not be 

                                maintained and is dependent upon 

                                individual MIB implementation.

                .. data:: object = 1

                .. data:: lexicalTable = 2

                .. data:: leastCpuTable = 3

                """

                object = Enum.YLeaf(1, "object")

                lexicalTable = Enum.YLeaf(2, "lexicalTable")

                leastCpuTable = Enum.YLeaf(3, "leastCpuTable")





    class CbfStatusFileTable(Entity):
        """
        A table of bulk file status.
        
        .. attribute:: cbfstatusfileentry
        
        	Status for a particular file.  An entry exists in this table for each time cbfDefineFileNow has been set to 'create' and the corresponding entry here has not been explicitly deleted by the application or bumped to make room for a new entry.  Deleting an entry with cbfStatusFileState 'running' aborts the file creation attempt.  It is implementation and file\-system specific whether deleting the entry also deletes the file
        	**type**\: list of  		 :py:class:`CbfStatusFileEntry <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CISCOBULKFILEMIB.CbfStatusFileTable.CbfStatusFileEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-BULK-FILE-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CISCOBULKFILEMIB.CbfStatusFileTable, self).__init__()

            self.yang_name = "cbfStatusFileTable"
            self.yang_parent_name = "CISCO-BULK-FILE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cbfStatusFileEntry", ("cbfstatusfileentry", CISCOBULKFILEMIB.CbfStatusFileTable.CbfStatusFileEntry))])
            self._leafs = OrderedDict()

            self.cbfstatusfileentry = YList(self)
            self._segment_path = lambda: "cbfStatusFileTable"
            self._absolute_path = lambda: "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBULKFILEMIB.CbfStatusFileTable, [], name, value)


        class CbfStatusFileEntry(Entity):
            """
            Status for a particular file.
            
            An entry exists in this table for each time cbfDefineFileNow
            has been set to 'create' and the corresponding entry here
            has not been explicitly deleted by the application or bumped
            to make room for a new entry.
            
            Deleting an entry with cbfStatusFileState 'running' aborts
            the file creation attempt.
            
            It is implementation and file\-system specific whether deleting
            the entry also deletes the file.
            
            .. attribute:: cbfdefinefileindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cbfdefinefileindex <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CISCOBULKFILEMIB.CbfDefineFileTable.CbfDefineFileEntry>`
            
            	**config**\: False
            
            .. attribute:: cbfstatusfileindex  (key)
            
            	An arbitrary integer to uniquely identify this file.  The numeric order of the entries implies the creation order of the files
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cbfstatusfilestate
            
            	The file state\:  running    data is being written to the file ready      the file is ready to be read emptied    an ephemeral file was successfully consumed noSpace    no data due to insufficient file space badName    no data due to a name or path problem writeErr   no data due to fatal file write error noMem      no data due to insufficient dynamic memory buffErr    implementation buffer too small aborted    short terminated by operator command  Only the 'ready' state implies that the file is available for transfer.  The disposition of files after an error is implementation and file\-syste specific
            	**type**\:  :py:class:`CbfStatusFileState <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CISCOBULKFILEMIB.CbfStatusFileTable.CbfStatusFileEntry.CbfStatusFileState>`
            
            	**config**\: False
            
            .. attribute:: cbfstatusfilecompletiontime
            
            	The value of sysUpTime when the creation attempt completed. A value of 0 indicates not complete.  For ephemeral files this is the time when cbfStatusFileState goes to 'emptied'.  For others this is the time when the state leaves 'running'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbfstatusfileentrystatus
            
            	The control that allows deletion of entries. For detailed rules see the DESCRIPTION for cbfStatusFileEntry.  This object may not be set to any value other than 'destroy'
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-BULK-FILE-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                super(CISCOBULKFILEMIB.CbfStatusFileTable.CbfStatusFileEntry, self).__init__()

                self.yang_name = "cbfStatusFileEntry"
                self.yang_parent_name = "cbfStatusFileTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cbfdefinefileindex','cbfstatusfileindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cbfdefinefileindex', (YLeaf(YType.str, 'cbfDefineFileIndex'), ['int'])),
                    ('cbfstatusfileindex', (YLeaf(YType.uint32, 'cbfStatusFileIndex'), ['int'])),
                    ('cbfstatusfilestate', (YLeaf(YType.enumeration, 'cbfStatusFileState'), [('ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB', 'CISCOBULKFILEMIB', 'CbfStatusFileTable.CbfStatusFileEntry.CbfStatusFileState')])),
                    ('cbfstatusfilecompletiontime', (YLeaf(YType.uint32, 'cbfStatusFileCompletionTime'), ['int'])),
                    ('cbfstatusfileentrystatus', (YLeaf(YType.enumeration, 'cbfStatusFileEntryStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.cbfdefinefileindex = None
                self.cbfstatusfileindex = None
                self.cbfstatusfilestate = None
                self.cbfstatusfilecompletiontime = None
                self.cbfstatusfileentrystatus = None
                self._segment_path = lambda: "cbfStatusFileEntry" + "[cbfDefineFileIndex='" + str(self.cbfdefinefileindex) + "']" + "[cbfStatusFileIndex='" + str(self.cbfstatusfileindex) + "']"
                self._absolute_path = lambda: "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/cbfStatusFileTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBULKFILEMIB.CbfStatusFileTable.CbfStatusFileEntry, ['cbfdefinefileindex', 'cbfstatusfileindex', 'cbfstatusfilestate', 'cbfstatusfilecompletiontime', 'cbfstatusfileentrystatus'], name, value)

            class CbfStatusFileState(Enum):
                """
                CbfStatusFileState (Enum Class)

                The file state\:

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

                and file\-syste specific.

                .. data:: running = 1

                .. data:: ready = 2

                .. data:: emptied = 3

                .. data:: noSpace = 4

                .. data:: badName = 5

                .. data:: writeErr = 6

                .. data:: noMem = 7

                .. data:: buffErr = 8

                .. data:: aborted = 9

                """

                running = Enum.YLeaf(1, "running")

                ready = Enum.YLeaf(2, "ready")

                emptied = Enum.YLeaf(3, "emptied")

                noSpace = Enum.YLeaf(4, "noSpace")

                badName = Enum.YLeaf(5, "badName")

                writeErr = Enum.YLeaf(6, "writeErr")

                noMem = Enum.YLeaf(7, "noMem")

                buffErr = Enum.YLeaf(8, "buffErr")

                aborted = Enum.YLeaf(9, "aborted")




    def clone_ptr(self):
        self._top_entity = CISCOBULKFILEMIB()
        return self._top_entity



