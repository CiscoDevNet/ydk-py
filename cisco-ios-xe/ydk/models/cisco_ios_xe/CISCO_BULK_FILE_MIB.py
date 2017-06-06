""" CISCO_BULK_FILE_MIB 

The MIB module for creating and deleting bulk files of
SNMP data for file transfer.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoBulkFileMib(object):
    """
    
    
    .. attribute:: cbfdefine
    
    	
    	**type**\:   :py:class:`Cbfdefine <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfdefine>`
    
    .. attribute:: cbfdefinefiletable
    
    	A table of bulk file definition and creation controls
    	**type**\:   :py:class:`Cbfdefinefiletable <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfdefinefiletable>`
    
    .. attribute:: cbfdefineobjecttable
    
    	A table of objects to go in bulk files
    	**type**\:   :py:class:`Cbfdefineobjecttable <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfdefineobjecttable>`
    
    .. attribute:: cbfstatus
    
    	
    	**type**\:   :py:class:`Cbfstatus <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfstatus>`
    
    .. attribute:: cbfstatusfiletable
    
    	A table of bulk file status
    	**type**\:   :py:class:`Cbfstatusfiletable <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfstatusfiletable>`
    
    

    """

    _prefix = 'CISCO-BULK-FILE-MIB'
    _revision = '2002-06-10'

    def __init__(self):
        self.cbfdefine = CiscoBulkFileMib.Cbfdefine()
        self.cbfdefine.parent = self
        self.cbfdefinefiletable = CiscoBulkFileMib.Cbfdefinefiletable()
        self.cbfdefinefiletable.parent = self
        self.cbfdefineobjecttable = CiscoBulkFileMib.Cbfdefineobjecttable()
        self.cbfdefineobjecttable.parent = self
        self.cbfstatus = CiscoBulkFileMib.Cbfstatus()
        self.cbfstatus.parent = self
        self.cbfstatusfiletable = CiscoBulkFileMib.Cbfstatusfiletable()
        self.cbfstatusfiletable.parent = self


    class Cbfdefine(object):
        """
        
        
        .. attribute:: cbfdefinefiles
        
        	The current number of file definitions in cbfDefineFileTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cbfdefinefilesrefused
        
        	The number of attempts to create a file definition that failed due to exceeding cbfDefineMaxFiles
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cbfdefinehighfiles
        
        	The maximum value of cbfDefineFiles since system  initialization
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cbfdefinehighobjects
        
        	The maximum value of cbfDefineObjects since system  initialization
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cbfdefinemaxfiles
        
        	The maximum number of file definitions this system can hold in cbfDefineFileTable.  A value of 0 indicates no configured limit.  This object may be read\-only on some systems.  Changing this number does not disturb existing entries
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cbfdefinemaxobjects
        
        	The maximum total number of object selections to go with file definitions this system, that is, the total number of objects this system can hold in cbfDefineObjectTable.  A value of 0 indicates no configured limit.  This object may be read\-only on some systems.  Changing this number does not disturb existing entries
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cbfdefineobjects
        
        	The current number of object selections in  cbfDefineObjectTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cbfdefineobjectsrefused
        
        	The number of attempts to create an object selection that failed due to exceeding cbfDefineMaxObjects
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-BULK-FILE-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            self.parent = None
            self.cbfdefinefiles = None
            self.cbfdefinefilesrefused = None
            self.cbfdefinehighfiles = None
            self.cbfdefinehighobjects = None
            self.cbfdefinemaxfiles = None
            self.cbfdefinemaxobjects = None
            self.cbfdefineobjects = None
            self.cbfdefineobjectsrefused = None

        @property
        def _common_path(self):

            return '/CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/CISCO-BULK-FILE-MIB:cbfDefine'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cbfdefinefiles is not None:
                return True

            if self.cbfdefinefilesrefused is not None:
                return True

            if self.cbfdefinehighfiles is not None:
                return True

            if self.cbfdefinehighobjects is not None:
                return True

            if self.cbfdefinemaxfiles is not None:
                return True

            if self.cbfdefinemaxobjects is not None:
                return True

            if self.cbfdefineobjects is not None:
                return True

            if self.cbfdefineobjectsrefused is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_BULK_FILE_MIB as meta
            return meta._meta_table['CiscoBulkFileMib.Cbfdefine']['meta_info']


    class Cbfstatus(object):
        """
        
        
        .. attribute:: cbfstatusfiles
        
        	The current number of file statuses in cbfStatusFileTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cbfstatusfilesbumped
        
        	The number times the oldest entry was deleted due to exceeding cbfStatusMaxFiles
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cbfstatushighfiles
        
        	The maximum value of cbfStatusFiles since system  initialization
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cbfstatusmaxfiles
        
        	The maximum number of file statuses this system can hold in cbfStatusFileTable.  A value of 0 indicates no configured limit.  This object may be read\-only on some systems.  Changing this number deletes the oldest finished entries until the new limit is satisfied
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-BULK-FILE-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            self.parent = None
            self.cbfstatusfiles = None
            self.cbfstatusfilesbumped = None
            self.cbfstatushighfiles = None
            self.cbfstatusmaxfiles = None

        @property
        def _common_path(self):

            return '/CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/CISCO-BULK-FILE-MIB:cbfStatus'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cbfstatusfiles is not None:
                return True

            if self.cbfstatusfilesbumped is not None:
                return True

            if self.cbfstatushighfiles is not None:
                return True

            if self.cbfstatusmaxfiles is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_BULK_FILE_MIB as meta
            return meta._meta_table['CiscoBulkFileMib.Cbfstatus']['meta_info']


    class Cbfdefinefiletable(object):
        """
        A table of bulk file definition and creation controls.
        
        .. attribute:: cbfdefinefileentry
        
        	Information for creation of a bulk file.  To creat a bulk file an application creates an entry in this table and corresponding entries in cbfDefineObjectTable.  When the entry in this table and the corresponding entries in cbfDefineObjectTable are 'active' the appliction uses cbfDefineFileNow to create the file and a corresponding entry in cbfStatusFileTable.  Deleting an entry in cbfDefineFileTable deletes all corresponding entries in cbfDefineObjectTable and cbfStatusFileTable.  An entry may not be modified or deleted while its cbfDefineFileNow has the value 'running'
        	**type**\: list of    :py:class:`Cbfdefinefileentry <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry>`
        
        

        """

        _prefix = 'CISCO-BULK-FILE-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            self.parent = None
            self.cbfdefinefileentry = YList()
            self.cbfdefinefileentry.parent = self
            self.cbfdefinefileentry.name = 'cbfdefinefileentry'


        class Cbfdefinefileentry(object):
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
            
            .. attribute:: cbfdefinefileindex  <key>
            
            	An arbitrary integer to uniquely identify this entry.  To create an entry a management application should pick a random number
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cbfdefinefileentrystatus
            
            	The control that allows creation, modification, and deletion of entries.  For detailed rules see the DESCRIPTION for cbfDefineFileEntry
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cbfdefinefileformat
            
            	The format of the data in the file\:  StandardBER        standard SNMP ASN.1 BER bulkBinary        a binary format specified with this MIB bulkASCII        a human\-readable form of bulkBinary variantBERWithCksum ASN.1 BER encoding with checksum variantBinWithCksum a binary format with checksum      A given system may support any or all of these
            	**type**\:   :py:class:`CbfdefinefileformatEnum <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry.CbfdefinefileformatEnum>`
            
            .. attribute:: cbfdefinefilename
            
            	The file name which is to be created.  Explicit device or path choices in the value of this object override cbfDefineFileStorage
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cbfdefinefilenotifyoncompletion
            
            	This controls the cbfDefineFileCompletion notification.  If true, cbfDefineFileCompletion notification will be generated. It is the responsibility of the  management entity to ensure that the SNMP administrative  model is configured in such a way as to allow the  notification to be delivered
            	**type**\:  bool
            
            .. attribute:: cbfdefinefilenow
            
            	The control to cause file creation.  The only values that can be set are 'create' and 'forcedCreate'. These can be set only  when the value is 'ready'.  Setting it to 'create' begins a  file creation and creates a corresponding entry in  cbfStatusFileTable. The system may choose to use an already  existing copy of the file instead of creating a new one. This may happen if there has been no configuration change on the  system and a request to recreate the file is received.  Setting this object to 'forcedCreate' forces the system to  create a new copy of the file.  The value is 'notActve' as long as cbfDefineFileEntryStatus or any corresponding cbfDefineObjectEntryStatus is not active.  When cbfDefineFileEntryStatus becomes active and all corresponding cbfDefineObjectEntryStatuses are active this  object automatically goes to 'ready'
            	**type**\:   :py:class:`CbfdefinefilenowEnum <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry.CbfdefinefilenowEnum>`
            
            .. attribute:: cbfdefinefilestorage
            
            	The type of file storage to use\:  ephemeral        data exists in small amounts until read volatile        data exists in volatile memory permanent        data survives reboot  An ephemeral file is suitable to be read only one time.  Note that this value is taken as advisory and may be overridden by explicit device or path choices in cbfDefineFile.  A given system may support any or all of these
            	**type**\:   :py:class:`CbfdefinefilestorageEnum <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry.CbfdefinefilestorageEnum>`
            
            

            """

            _prefix = 'CISCO-BULK-FILE-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                self.parent = None
                self.cbfdefinefileindex = None
                self.cbfdefinefileentrystatus = None
                self.cbfdefinefileformat = None
                self.cbfdefinefilename = None
                self.cbfdefinefilenotifyoncompletion = None
                self.cbfdefinefilenow = None
                self.cbfdefinefilestorage = None

            class CbfdefinefileformatEnum(Enum):
                """
                CbfdefinefileformatEnum

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

                standardBER = 1

                bulkBinary = 2

                bulkASCII = 3

                variantBERWithCksum = 4

                variantBinWithCksum = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_BULK_FILE_MIB as meta
                    return meta._meta_table['CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry.CbfdefinefileformatEnum']


            class CbfdefinefilenowEnum(Enum):
                """
                CbfdefinefilenowEnum

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

                notActive = 1

                ready = 2

                create = 3

                running = 4

                forcedCreate = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_BULK_FILE_MIB as meta
                    return meta._meta_table['CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry.CbfdefinefilenowEnum']


            class CbfdefinefilestorageEnum(Enum):
                """
                CbfdefinefilestorageEnum

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

                ephemeral = 1

                volatile = 2

                permanent = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_BULK_FILE_MIB as meta
                    return meta._meta_table['CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry.CbfdefinefilestorageEnum']


            @property
            def _common_path(self):
                if self.cbfdefinefileindex is None:
                    raise YPYModelError('Key property cbfdefinefileindex is None')

                return '/CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/CISCO-BULK-FILE-MIB:cbfDefineFileTable/CISCO-BULK-FILE-MIB:cbfDefineFileEntry[CISCO-BULK-FILE-MIB:cbfDefineFileIndex = ' + str(self.cbfdefinefileindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cbfdefinefileindex is not None:
                    return True

                if self.cbfdefinefileentrystatus is not None:
                    return True

                if self.cbfdefinefileformat is not None:
                    return True

                if self.cbfdefinefilename is not None:
                    return True

                if self.cbfdefinefilenotifyoncompletion is not None:
                    return True

                if self.cbfdefinefilenow is not None:
                    return True

                if self.cbfdefinefilestorage is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_BULK_FILE_MIB as meta
                return meta._meta_table['CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/CISCO-BULK-FILE-MIB:cbfDefineFileTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cbfdefinefileentry is not None:
                for child_ref in self.cbfdefinefileentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_BULK_FILE_MIB as meta
            return meta._meta_table['CiscoBulkFileMib.Cbfdefinefiletable']['meta_info']


    class Cbfdefineobjecttable(object):
        """
        A table of objects to go in bulk files.
        
        .. attribute:: cbfdefineobjectentry
        
        	Information about one object for a particular file.  An application uses cbfDefineObjectEntryStatus to create entries in this table in correspondence with entries in cbfDefineFileTable, which must be created first.  Entries in this table may not be changed, created or deleted while the corresponding value of cbfDefineFileNow is 'running'
        	**type**\: list of    :py:class:`Cbfdefineobjectentry <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfdefineobjecttable.Cbfdefineobjectentry>`
        
        

        """

        _prefix = 'CISCO-BULK-FILE-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            self.parent = None
            self.cbfdefineobjectentry = YList()
            self.cbfdefineobjectentry.parent = self
            self.cbfdefineobjectentry.name = 'cbfdefineobjectentry'


        class Cbfdefineobjectentry(object):
            """
            Information about one object for a particular file.
            
            An application uses cbfDefineObjectEntryStatus to create entries
            in this table in correspondence with entries in
            cbfDefineFileTable, which must be created first.
            
            Entries in this table may not be changed, created or deleted
            while the corresponding value of cbfDefineFileNow is 'running'.
            
            .. attribute:: cbfdefinefileindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cbfdefinefileindex <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry>`
            
            .. attribute:: cbfdefineobjectindex  <key>
            
            	An arbitrary integer to uniquely identify this entry.  The numeric order of the entries controls the order of the objects in the file
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cbfdefineobjectclass
            
            	The meaning of each object class is given below\:  object          a single MIB object is retrieved.  lexicalTable    an entire table or partial table                 is retrieved in lexical order of rows.  leastCpuTable   an entire table is retrieved with                 lowest CPU utilization.                 Lexical ordering of rows may not be                  maintained and is dependent upon                  individual MIB implementation
            	**type**\:   :py:class:`CbfdefineobjectclassEnum <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfdefineobjecttable.Cbfdefineobjectentry.CbfdefineobjectclassEnum>`
            
            .. attribute:: cbfdefineobjectentrystatus
            
            	The control that allows creation, modification, and deletion of entries.  For detailed rules see the DESCRIPTION for cbfDefineObjectEntry
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cbfdefineobjectid
            
            	The object identifier of a MIB object to be included in the file.  If cbfDefineObjectClass is 'object' this must be a full OID, including all instance information.  If cbfDefineObjectClass is 'lexicalTable' or 'leastCpuTable' this must be the OID of the table\-defining SEQUENCE OF registration point
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: cbfdefineobjectlastpolledinst
            
            	This object represents the last polled instance in the table.  The value represented by this object will be relevent only if the corresponding cbfStatusFileState is emptied(3) for  ephemeral files or ready(2) for volatile or permanent files.  A value of zeroDotZero indicates an absence of last polled  object.  An NMS can use the value of this object and populate the cbfDefineObjectTableInstance to retrieve a contiguous set of rows in a table
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: cbfdefineobjectnumentries
            
            	If cbfDefineObjectClass is 'lexicalTable', then this object represents the maximum number of entries which will be  populated in the file starting from the lexicographically next instance of the OID represented by  cbfDefineObjectTableInstance.   This object is irrelevent if cbfDefineObjectClass is not 'lexicalTable'.  Refer to the description of cbfDefineObjectTableInstance for examples and different scenarios relating to this object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbfdefineobjecttableinstance
            
            	If cbfDefineObjectClass is 'lexicalTable', then this object represents the starting instance in the cbfDefineObjectID table. The file created will have entries starting from the lexicographically next instance of the OID represented by this object.   For Eg\:  \-\-\-\-\-\-\-         Let us  assume we are polling ifTable and we        have information till the second row(ifIndex.2). Now        we may be interested in 10 rows lexically following        the second row.                So, we set cbfDefineObjectTableInstance as ifIndex.2         and cbfDefineObjectNumEntries as 10.          We will get information for the next 10 rows or        if there are less than 10 populated rows, we will        receive information till the end of the table is         reached.  The default value for this object is zeroDotZero.  If this object has the value of zeroDotZero and  cbfDefineObjectNumEntries has value 0, then the whole table(represented by cbfDefineObjectID) is retrieved.  If this object has the value of zeroDotZero,   cbfDefineObjectNumEntries has value n (>0) and there are  m(>0) entries in the table(represented by cbfDefineObjectID) then the first n entries in the table are retrieved if n < m.  If n >= m, then the whole table is retrieved.  When the value of cbfDefineObjectNumEntries is 0,  it means all the entries in the table(represented  by cbfDefineObjectID) which lexicographically follow  cbfDefineObjectTableInstance are retrieved.  This object is irrelevent if cbfDefineObjectClass is not 'lexicalTable'
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'CISCO-BULK-FILE-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                self.parent = None
                self.cbfdefinefileindex = None
                self.cbfdefineobjectindex = None
                self.cbfdefineobjectclass = None
                self.cbfdefineobjectentrystatus = None
                self.cbfdefineobjectid = None
                self.cbfdefineobjectlastpolledinst = None
                self.cbfdefineobjectnumentries = None
                self.cbfdefineobjecttableinstance = None

            class CbfdefineobjectclassEnum(Enum):
                """
                CbfdefineobjectclassEnum

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

                object = 1

                lexicalTable = 2

                leastCpuTable = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_BULK_FILE_MIB as meta
                    return meta._meta_table['CiscoBulkFileMib.Cbfdefineobjecttable.Cbfdefineobjectentry.CbfdefineobjectclassEnum']


            @property
            def _common_path(self):
                if self.cbfdefinefileindex is None:
                    raise YPYModelError('Key property cbfdefinefileindex is None')
                if self.cbfdefineobjectindex is None:
                    raise YPYModelError('Key property cbfdefineobjectindex is None')

                return '/CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/CISCO-BULK-FILE-MIB:cbfDefineObjectTable/CISCO-BULK-FILE-MIB:cbfDefineObjectEntry[CISCO-BULK-FILE-MIB:cbfDefineFileIndex = ' + str(self.cbfdefinefileindex) + '][CISCO-BULK-FILE-MIB:cbfDefineObjectIndex = ' + str(self.cbfdefineobjectindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cbfdefinefileindex is not None:
                    return True

                if self.cbfdefineobjectindex is not None:
                    return True

                if self.cbfdefineobjectclass is not None:
                    return True

                if self.cbfdefineobjectentrystatus is not None:
                    return True

                if self.cbfdefineobjectid is not None:
                    return True

                if self.cbfdefineobjectlastpolledinst is not None:
                    return True

                if self.cbfdefineobjectnumentries is not None:
                    return True

                if self.cbfdefineobjecttableinstance is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_BULK_FILE_MIB as meta
                return meta._meta_table['CiscoBulkFileMib.Cbfdefineobjecttable.Cbfdefineobjectentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/CISCO-BULK-FILE-MIB:cbfDefineObjectTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cbfdefineobjectentry is not None:
                for child_ref in self.cbfdefineobjectentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_BULK_FILE_MIB as meta
            return meta._meta_table['CiscoBulkFileMib.Cbfdefineobjecttable']['meta_info']


    class Cbfstatusfiletable(object):
        """
        A table of bulk file status.
        
        .. attribute:: cbfstatusfileentry
        
        	Status for a particular file.  An entry exists in this table for each time cbfDefineFileNow has been set to 'create' and the corresponding entry here has not been explicitly deleted by the application or bumped to make room for a new entry.  Deleting an entry with cbfStatusFileState 'running' aborts the file creation attempt.  It is implementation and file\-system specific whether deleting the entry also deletes the file
        	**type**\: list of    :py:class:`Cbfstatusfileentry <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfstatusfiletable.Cbfstatusfileentry>`
        
        

        """

        _prefix = 'CISCO-BULK-FILE-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            self.parent = None
            self.cbfstatusfileentry = YList()
            self.cbfstatusfileentry.parent = self
            self.cbfstatusfileentry.name = 'cbfstatusfileentry'


        class Cbfstatusfileentry(object):
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
            
            .. attribute:: cbfdefinefileindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cbfdefinefileindex <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry>`
            
            .. attribute:: cbfstatusfileindex  <key>
            
            	An arbitrary integer to uniquely identify this file.  The numeric order of the entries implies the creation order of the files
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cbfstatusfilecompletiontime
            
            	The value of sysUpTime when the creation attempt completed. A value of 0 indicates not complete.  For ephemeral files this is the time when cbfStatusFileState goes to 'emptied'.  For others this is the time when the state leaves 'running'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbfstatusfileentrystatus
            
            	The control that allows deletion of entries. For detailed rules see the DESCRIPTION for cbfStatusFileEntry.  This object may not be set to any value other than 'destroy'
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cbfstatusfilestate
            
            	The file state\:  running    data is being written to the file ready      the file is ready to be read emptied    an ephemeral file was successfully consumed noSpace    no data due to insufficient file space badName    no data due to a name or path problem writeErr   no data due to fatal file write error noMem      no data due to insufficient dynamic memory buffErr    implementation buffer too small aborted    short terminated by operator command  Only the 'ready' state implies that the file is available for transfer.  The disposition of files after an error is implementation and file\-syste specific
            	**type**\:   :py:class:`CbfstatusfilestateEnum <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfstatusfiletable.Cbfstatusfileentry.CbfstatusfilestateEnum>`
            
            

            """

            _prefix = 'CISCO-BULK-FILE-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                self.parent = None
                self.cbfdefinefileindex = None
                self.cbfstatusfileindex = None
                self.cbfstatusfilecompletiontime = None
                self.cbfstatusfileentrystatus = None
                self.cbfstatusfilestate = None

            class CbfstatusfilestateEnum(Enum):
                """
                CbfstatusfilestateEnum

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

                running = 1

                ready = 2

                emptied = 3

                noSpace = 4

                badName = 5

                writeErr = 6

                noMem = 7

                buffErr = 8

                aborted = 9


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_BULK_FILE_MIB as meta
                    return meta._meta_table['CiscoBulkFileMib.Cbfstatusfiletable.Cbfstatusfileentry.CbfstatusfilestateEnum']


            @property
            def _common_path(self):
                if self.cbfdefinefileindex is None:
                    raise YPYModelError('Key property cbfdefinefileindex is None')
                if self.cbfstatusfileindex is None:
                    raise YPYModelError('Key property cbfstatusfileindex is None')

                return '/CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/CISCO-BULK-FILE-MIB:cbfStatusFileTable/CISCO-BULK-FILE-MIB:cbfStatusFileEntry[CISCO-BULK-FILE-MIB:cbfDefineFileIndex = ' + str(self.cbfdefinefileindex) + '][CISCO-BULK-FILE-MIB:cbfStatusFileIndex = ' + str(self.cbfstatusfileindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cbfdefinefileindex is not None:
                    return True

                if self.cbfstatusfileindex is not None:
                    return True

                if self.cbfstatusfilecompletiontime is not None:
                    return True

                if self.cbfstatusfileentrystatus is not None:
                    return True

                if self.cbfstatusfilestate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_BULK_FILE_MIB as meta
                return meta._meta_table['CiscoBulkFileMib.Cbfstatusfiletable.Cbfstatusfileentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/CISCO-BULK-FILE-MIB:cbfStatusFileTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cbfstatusfileentry is not None:
                for child_ref in self.cbfstatusfileentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_BULK_FILE_MIB as meta
            return meta._meta_table['CiscoBulkFileMib.Cbfstatusfiletable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cbfdefine is not None and self.cbfdefine._has_data():
            return True

        if self.cbfdefinefiletable is not None and self.cbfdefinefiletable._has_data():
            return True

        if self.cbfdefineobjecttable is not None and self.cbfdefineobjecttable._has_data():
            return True

        if self.cbfstatus is not None and self.cbfstatus._has_data():
            return True

        if self.cbfstatusfiletable is not None and self.cbfstatusfiletable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_BULK_FILE_MIB as meta
        return meta._meta_table['CiscoBulkFileMib']['meta_info']


