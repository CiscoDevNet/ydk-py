""" CISCO_BULK_FILE_MIB 

The MIB module for creating and deleting bulk files of
SNMP data for file transfer.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoBulkFileMib(Entity):
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
        super(CiscoBulkFileMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-BULK-FILE-MIB"
        self.yang_parent_name = "CISCO-BULK-FILE-MIB"

        self.cbfdefine = CiscoBulkFileMib.Cbfdefine()
        self.cbfdefine.parent = self
        self._children_name_map["cbfdefine"] = "cbfDefine"
        self._children_yang_names.add("cbfDefine")

        self.cbfdefinefiletable = CiscoBulkFileMib.Cbfdefinefiletable()
        self.cbfdefinefiletable.parent = self
        self._children_name_map["cbfdefinefiletable"] = "cbfDefineFileTable"
        self._children_yang_names.add("cbfDefineFileTable")

        self.cbfdefineobjecttable = CiscoBulkFileMib.Cbfdefineobjecttable()
        self.cbfdefineobjecttable.parent = self
        self._children_name_map["cbfdefineobjecttable"] = "cbfDefineObjectTable"
        self._children_yang_names.add("cbfDefineObjectTable")

        self.cbfstatus = CiscoBulkFileMib.Cbfstatus()
        self.cbfstatus.parent = self
        self._children_name_map["cbfstatus"] = "cbfStatus"
        self._children_yang_names.add("cbfStatus")

        self.cbfstatusfiletable = CiscoBulkFileMib.Cbfstatusfiletable()
        self.cbfstatusfiletable.parent = self
        self._children_name_map["cbfstatusfiletable"] = "cbfStatusFileTable"
        self._children_yang_names.add("cbfStatusFileTable")


    class Cbfdefine(Entity):
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
            super(CiscoBulkFileMib.Cbfdefine, self).__init__()

            self.yang_name = "cbfDefine"
            self.yang_parent_name = "CISCO-BULK-FILE-MIB"

            self.cbfdefinefiles = YLeaf(YType.uint32, "cbfDefineFiles")

            self.cbfdefinefilesrefused = YLeaf(YType.uint32, "cbfDefineFilesRefused")

            self.cbfdefinehighfiles = YLeaf(YType.uint32, "cbfDefineHighFiles")

            self.cbfdefinehighobjects = YLeaf(YType.uint32, "cbfDefineHighObjects")

            self.cbfdefinemaxfiles = YLeaf(YType.uint32, "cbfDefineMaxFiles")

            self.cbfdefinemaxobjects = YLeaf(YType.uint32, "cbfDefineMaxObjects")

            self.cbfdefineobjects = YLeaf(YType.uint32, "cbfDefineObjects")

            self.cbfdefineobjectsrefused = YLeaf(YType.uint32, "cbfDefineObjectsRefused")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cbfdefinefiles",
                            "cbfdefinefilesrefused",
                            "cbfdefinehighfiles",
                            "cbfdefinehighobjects",
                            "cbfdefinemaxfiles",
                            "cbfdefinemaxobjects",
                            "cbfdefineobjects",
                            "cbfdefineobjectsrefused") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoBulkFileMib.Cbfdefine, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoBulkFileMib.Cbfdefine, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cbfdefinefiles.is_set or
                self.cbfdefinefilesrefused.is_set or
                self.cbfdefinehighfiles.is_set or
                self.cbfdefinehighobjects.is_set or
                self.cbfdefinemaxfiles.is_set or
                self.cbfdefinemaxobjects.is_set or
                self.cbfdefineobjects.is_set or
                self.cbfdefineobjectsrefused.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cbfdefinefiles.yfilter != YFilter.not_set or
                self.cbfdefinefilesrefused.yfilter != YFilter.not_set or
                self.cbfdefinehighfiles.yfilter != YFilter.not_set or
                self.cbfdefinehighobjects.yfilter != YFilter.not_set or
                self.cbfdefinemaxfiles.yfilter != YFilter.not_set or
                self.cbfdefinemaxobjects.yfilter != YFilter.not_set or
                self.cbfdefineobjects.yfilter != YFilter.not_set or
                self.cbfdefineobjectsrefused.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cbfDefine" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cbfdefinefiles.is_set or self.cbfdefinefiles.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cbfdefinefiles.get_name_leafdata())
            if (self.cbfdefinefilesrefused.is_set or self.cbfdefinefilesrefused.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cbfdefinefilesrefused.get_name_leafdata())
            if (self.cbfdefinehighfiles.is_set or self.cbfdefinehighfiles.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cbfdefinehighfiles.get_name_leafdata())
            if (self.cbfdefinehighobjects.is_set or self.cbfdefinehighobjects.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cbfdefinehighobjects.get_name_leafdata())
            if (self.cbfdefinemaxfiles.is_set or self.cbfdefinemaxfiles.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cbfdefinemaxfiles.get_name_leafdata())
            if (self.cbfdefinemaxobjects.is_set or self.cbfdefinemaxobjects.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cbfdefinemaxobjects.get_name_leafdata())
            if (self.cbfdefineobjects.is_set or self.cbfdefineobjects.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cbfdefineobjects.get_name_leafdata())
            if (self.cbfdefineobjectsrefused.is_set or self.cbfdefineobjectsrefused.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cbfdefineobjectsrefused.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cbfDefineFiles" or name == "cbfDefineFilesRefused" or name == "cbfDefineHighFiles" or name == "cbfDefineHighObjects" or name == "cbfDefineMaxFiles" or name == "cbfDefineMaxObjects" or name == "cbfDefineObjects" or name == "cbfDefineObjectsRefused"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cbfDefineFiles"):
                self.cbfdefinefiles = value
                self.cbfdefinefiles.value_namespace = name_space
                self.cbfdefinefiles.value_namespace_prefix = name_space_prefix
            if(value_path == "cbfDefineFilesRefused"):
                self.cbfdefinefilesrefused = value
                self.cbfdefinefilesrefused.value_namespace = name_space
                self.cbfdefinefilesrefused.value_namespace_prefix = name_space_prefix
            if(value_path == "cbfDefineHighFiles"):
                self.cbfdefinehighfiles = value
                self.cbfdefinehighfiles.value_namespace = name_space
                self.cbfdefinehighfiles.value_namespace_prefix = name_space_prefix
            if(value_path == "cbfDefineHighObjects"):
                self.cbfdefinehighobjects = value
                self.cbfdefinehighobjects.value_namespace = name_space
                self.cbfdefinehighobjects.value_namespace_prefix = name_space_prefix
            if(value_path == "cbfDefineMaxFiles"):
                self.cbfdefinemaxfiles = value
                self.cbfdefinemaxfiles.value_namespace = name_space
                self.cbfdefinemaxfiles.value_namespace_prefix = name_space_prefix
            if(value_path == "cbfDefineMaxObjects"):
                self.cbfdefinemaxobjects = value
                self.cbfdefinemaxobjects.value_namespace = name_space
                self.cbfdefinemaxobjects.value_namespace_prefix = name_space_prefix
            if(value_path == "cbfDefineObjects"):
                self.cbfdefineobjects = value
                self.cbfdefineobjects.value_namespace = name_space
                self.cbfdefineobjects.value_namespace_prefix = name_space_prefix
            if(value_path == "cbfDefineObjectsRefused"):
                self.cbfdefineobjectsrefused = value
                self.cbfdefineobjectsrefused.value_namespace = name_space
                self.cbfdefineobjectsrefused.value_namespace_prefix = name_space_prefix


    class Cbfstatus(Entity):
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
            super(CiscoBulkFileMib.Cbfstatus, self).__init__()

            self.yang_name = "cbfStatus"
            self.yang_parent_name = "CISCO-BULK-FILE-MIB"

            self.cbfstatusfiles = YLeaf(YType.uint32, "cbfStatusFiles")

            self.cbfstatusfilesbumped = YLeaf(YType.uint32, "cbfStatusFilesBumped")

            self.cbfstatushighfiles = YLeaf(YType.uint32, "cbfStatusHighFiles")

            self.cbfstatusmaxfiles = YLeaf(YType.uint32, "cbfStatusMaxFiles")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cbfstatusfiles",
                            "cbfstatusfilesbumped",
                            "cbfstatushighfiles",
                            "cbfstatusmaxfiles") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoBulkFileMib.Cbfstatus, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoBulkFileMib.Cbfstatus, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cbfstatusfiles.is_set or
                self.cbfstatusfilesbumped.is_set or
                self.cbfstatushighfiles.is_set or
                self.cbfstatusmaxfiles.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cbfstatusfiles.yfilter != YFilter.not_set or
                self.cbfstatusfilesbumped.yfilter != YFilter.not_set or
                self.cbfstatushighfiles.yfilter != YFilter.not_set or
                self.cbfstatusmaxfiles.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cbfStatus" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cbfstatusfiles.is_set or self.cbfstatusfiles.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cbfstatusfiles.get_name_leafdata())
            if (self.cbfstatusfilesbumped.is_set or self.cbfstatusfilesbumped.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cbfstatusfilesbumped.get_name_leafdata())
            if (self.cbfstatushighfiles.is_set or self.cbfstatushighfiles.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cbfstatushighfiles.get_name_leafdata())
            if (self.cbfstatusmaxfiles.is_set or self.cbfstatusmaxfiles.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cbfstatusmaxfiles.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cbfStatusFiles" or name == "cbfStatusFilesBumped" or name == "cbfStatusHighFiles" or name == "cbfStatusMaxFiles"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cbfStatusFiles"):
                self.cbfstatusfiles = value
                self.cbfstatusfiles.value_namespace = name_space
                self.cbfstatusfiles.value_namespace_prefix = name_space_prefix
            if(value_path == "cbfStatusFilesBumped"):
                self.cbfstatusfilesbumped = value
                self.cbfstatusfilesbumped.value_namespace = name_space
                self.cbfstatusfilesbumped.value_namespace_prefix = name_space_prefix
            if(value_path == "cbfStatusHighFiles"):
                self.cbfstatushighfiles = value
                self.cbfstatushighfiles.value_namespace = name_space
                self.cbfstatushighfiles.value_namespace_prefix = name_space_prefix
            if(value_path == "cbfStatusMaxFiles"):
                self.cbfstatusmaxfiles = value
                self.cbfstatusmaxfiles.value_namespace = name_space
                self.cbfstatusmaxfiles.value_namespace_prefix = name_space_prefix


    class Cbfdefinefiletable(Entity):
        """
        A table of bulk file definition and creation controls.
        
        .. attribute:: cbfdefinefileentry
        
        	Information for creation of a bulk file.  To creat a bulk file an application creates an entry in this table and corresponding entries in cbfDefineObjectTable.  When the entry in this table and the corresponding entries in cbfDefineObjectTable are 'active' the appliction uses cbfDefineFileNow to create the file and a corresponding entry in cbfStatusFileTable.  Deleting an entry in cbfDefineFileTable deletes all corresponding entries in cbfDefineObjectTable and cbfStatusFileTable.  An entry may not be modified or deleted while its cbfDefineFileNow has the value 'running'
        	**type**\: list of    :py:class:`Cbfdefinefileentry <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry>`
        
        

        """

        _prefix = 'CISCO-BULK-FILE-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CiscoBulkFileMib.Cbfdefinefiletable, self).__init__()

            self.yang_name = "cbfDefineFileTable"
            self.yang_parent_name = "CISCO-BULK-FILE-MIB"

            self.cbfdefinefileentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoBulkFileMib.Cbfdefinefiletable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoBulkFileMib.Cbfdefinefiletable, self).__setattr__(name, value)


        class Cbfdefinefileentry(Entity):
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
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cbfdefinefileformat
            
            	The format of the data in the file\:  StandardBER        standard SNMP ASN.1 BER bulkBinary        a binary format specified with this MIB bulkASCII        a human\-readable form of bulkBinary variantBERWithCksum ASN.1 BER encoding with checksum variantBinWithCksum a binary format with checksum      A given system may support any or all of these
            	**type**\:   :py:class:`Cbfdefinefileformat <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry.Cbfdefinefileformat>`
            
            .. attribute:: cbfdefinefilename
            
            	The file name which is to be created.  Explicit device or path choices in the value of this object override cbfDefineFileStorage
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cbfdefinefilenotifyoncompletion
            
            	This controls the cbfDefineFileCompletion notification.  If true, cbfDefineFileCompletion notification will be generated. It is the responsibility of the  management entity to ensure that the SNMP administrative  model is configured in such a way as to allow the  notification to be delivered
            	**type**\:  bool
            
            .. attribute:: cbfdefinefilenow
            
            	The control to cause file creation.  The only values that can be set are 'create' and 'forcedCreate'. These can be set only  when the value is 'ready'.  Setting it to 'create' begins a  file creation and creates a corresponding entry in  cbfStatusFileTable. The system may choose to use an already  existing copy of the file instead of creating a new one. This may happen if there has been no configuration change on the  system and a request to recreate the file is received.  Setting this object to 'forcedCreate' forces the system to  create a new copy of the file.  The value is 'notActve' as long as cbfDefineFileEntryStatus or any corresponding cbfDefineObjectEntryStatus is not active.  When cbfDefineFileEntryStatus becomes active and all corresponding cbfDefineObjectEntryStatuses are active this  object automatically goes to 'ready'
            	**type**\:   :py:class:`Cbfdefinefilenow <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry.Cbfdefinefilenow>`
            
            .. attribute:: cbfdefinefilestorage
            
            	The type of file storage to use\:  ephemeral        data exists in small amounts until read volatile        data exists in volatile memory permanent        data survives reboot  An ephemeral file is suitable to be read only one time.  Note that this value is taken as advisory and may be overridden by explicit device or path choices in cbfDefineFile.  A given system may support any or all of these
            	**type**\:   :py:class:`Cbfdefinefilestorage <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry.Cbfdefinefilestorage>`
            
            

            """

            _prefix = 'CISCO-BULK-FILE-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                super(CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry, self).__init__()

                self.yang_name = "cbfDefineFileEntry"
                self.yang_parent_name = "cbfDefineFileTable"

                self.cbfdefinefileindex = YLeaf(YType.uint32, "cbfDefineFileIndex")

                self.cbfdefinefileentrystatus = YLeaf(YType.enumeration, "cbfDefineFileEntryStatus")

                self.cbfdefinefileformat = YLeaf(YType.enumeration, "cbfDefineFileFormat")

                self.cbfdefinefilename = YLeaf(YType.str, "cbfDefineFileName")

                self.cbfdefinefilenotifyoncompletion = YLeaf(YType.boolean, "cbfDefineFileNotifyOnCompletion")

                self.cbfdefinefilenow = YLeaf(YType.enumeration, "cbfDefineFileNow")

                self.cbfdefinefilestorage = YLeaf(YType.enumeration, "cbfDefineFileStorage")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cbfdefinefileindex",
                                "cbfdefinefileentrystatus",
                                "cbfdefinefileformat",
                                "cbfdefinefilename",
                                "cbfdefinefilenotifyoncompletion",
                                "cbfdefinefilenow",
                                "cbfdefinefilestorage") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry, self).__setattr__(name, value)

            class Cbfdefinefileformat(Enum):
                """
                Cbfdefinefileformat

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


            class Cbfdefinefilenow(Enum):
                """
                Cbfdefinefilenow

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


            class Cbfdefinefilestorage(Enum):
                """
                Cbfdefinefilestorage

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


            def has_data(self):
                return (
                    self.cbfdefinefileindex.is_set or
                    self.cbfdefinefileentrystatus.is_set or
                    self.cbfdefinefileformat.is_set or
                    self.cbfdefinefilename.is_set or
                    self.cbfdefinefilenotifyoncompletion.is_set or
                    self.cbfdefinefilenow.is_set or
                    self.cbfdefinefilestorage.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cbfdefinefileindex.yfilter != YFilter.not_set or
                    self.cbfdefinefileentrystatus.yfilter != YFilter.not_set or
                    self.cbfdefinefileformat.yfilter != YFilter.not_set or
                    self.cbfdefinefilename.yfilter != YFilter.not_set or
                    self.cbfdefinefilenotifyoncompletion.yfilter != YFilter.not_set or
                    self.cbfdefinefilenow.yfilter != YFilter.not_set or
                    self.cbfdefinefilestorage.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cbfDefineFileEntry" + "[cbfDefineFileIndex='" + self.cbfdefinefileindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/cbfDefineFileTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cbfdefinefileindex.is_set or self.cbfdefinefileindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfdefinefileindex.get_name_leafdata())
                if (self.cbfdefinefileentrystatus.is_set or self.cbfdefinefileentrystatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfdefinefileentrystatus.get_name_leafdata())
                if (self.cbfdefinefileformat.is_set or self.cbfdefinefileformat.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfdefinefileformat.get_name_leafdata())
                if (self.cbfdefinefilename.is_set or self.cbfdefinefilename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfdefinefilename.get_name_leafdata())
                if (self.cbfdefinefilenotifyoncompletion.is_set or self.cbfdefinefilenotifyoncompletion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfdefinefilenotifyoncompletion.get_name_leafdata())
                if (self.cbfdefinefilenow.is_set or self.cbfdefinefilenow.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfdefinefilenow.get_name_leafdata())
                if (self.cbfdefinefilestorage.is_set or self.cbfdefinefilestorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfdefinefilestorage.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cbfDefineFileIndex" or name == "cbfDefineFileEntryStatus" or name == "cbfDefineFileFormat" or name == "cbfDefineFileName" or name == "cbfDefineFileNotifyOnCompletion" or name == "cbfDefineFileNow" or name == "cbfDefineFileStorage"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cbfDefineFileIndex"):
                    self.cbfdefinefileindex = value
                    self.cbfdefinefileindex.value_namespace = name_space
                    self.cbfdefinefileindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cbfDefineFileEntryStatus"):
                    self.cbfdefinefileentrystatus = value
                    self.cbfdefinefileentrystatus.value_namespace = name_space
                    self.cbfdefinefileentrystatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cbfDefineFileFormat"):
                    self.cbfdefinefileformat = value
                    self.cbfdefinefileformat.value_namespace = name_space
                    self.cbfdefinefileformat.value_namespace_prefix = name_space_prefix
                if(value_path == "cbfDefineFileName"):
                    self.cbfdefinefilename = value
                    self.cbfdefinefilename.value_namespace = name_space
                    self.cbfdefinefilename.value_namespace_prefix = name_space_prefix
                if(value_path == "cbfDefineFileNotifyOnCompletion"):
                    self.cbfdefinefilenotifyoncompletion = value
                    self.cbfdefinefilenotifyoncompletion.value_namespace = name_space
                    self.cbfdefinefilenotifyoncompletion.value_namespace_prefix = name_space_prefix
                if(value_path == "cbfDefineFileNow"):
                    self.cbfdefinefilenow = value
                    self.cbfdefinefilenow.value_namespace = name_space
                    self.cbfdefinefilenow.value_namespace_prefix = name_space_prefix
                if(value_path == "cbfDefineFileStorage"):
                    self.cbfdefinefilestorage = value
                    self.cbfdefinefilestorage.value_namespace = name_space
                    self.cbfdefinefilestorage.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cbfdefinefileentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cbfdefinefileentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cbfDefineFileTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cbfDefineFileEntry"):
                for c in self.cbfdefinefileentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoBulkFileMib.Cbfdefinefiletable.Cbfdefinefileentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cbfdefinefileentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cbfDefineFileEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cbfdefineobjecttable(Entity):
        """
        A table of objects to go in bulk files.
        
        .. attribute:: cbfdefineobjectentry
        
        	Information about one object for a particular file.  An application uses cbfDefineObjectEntryStatus to create entries in this table in correspondence with entries in cbfDefineFileTable, which must be created first.  Entries in this table may not be changed, created or deleted while the corresponding value of cbfDefineFileNow is 'running'
        	**type**\: list of    :py:class:`Cbfdefineobjectentry <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfdefineobjecttable.Cbfdefineobjectentry>`
        
        

        """

        _prefix = 'CISCO-BULK-FILE-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CiscoBulkFileMib.Cbfdefineobjecttable, self).__init__()

            self.yang_name = "cbfDefineObjectTable"
            self.yang_parent_name = "CISCO-BULK-FILE-MIB"

            self.cbfdefineobjectentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoBulkFileMib.Cbfdefineobjecttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoBulkFileMib.Cbfdefineobjecttable, self).__setattr__(name, value)


        class Cbfdefineobjectentry(Entity):
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
            	**type**\:   :py:class:`Cbfdefineobjectclass <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfdefineobjecttable.Cbfdefineobjectentry.Cbfdefineobjectclass>`
            
            .. attribute:: cbfdefineobjectentrystatus
            
            	The control that allows creation, modification, and deletion of entries.  For detailed rules see the DESCRIPTION for cbfDefineObjectEntry
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
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
                super(CiscoBulkFileMib.Cbfdefineobjecttable.Cbfdefineobjectentry, self).__init__()

                self.yang_name = "cbfDefineObjectEntry"
                self.yang_parent_name = "cbfDefineObjectTable"

                self.cbfdefinefileindex = YLeaf(YType.str, "cbfDefineFileIndex")

                self.cbfdefineobjectindex = YLeaf(YType.uint32, "cbfDefineObjectIndex")

                self.cbfdefineobjectclass = YLeaf(YType.enumeration, "cbfDefineObjectClass")

                self.cbfdefineobjectentrystatus = YLeaf(YType.enumeration, "cbfDefineObjectEntryStatus")

                self.cbfdefineobjectid = YLeaf(YType.str, "cbfDefineObjectID")

                self.cbfdefineobjectlastpolledinst = YLeaf(YType.str, "cbfDefineObjectLastPolledInst")

                self.cbfdefineobjectnumentries = YLeaf(YType.uint32, "cbfDefineObjectNumEntries")

                self.cbfdefineobjecttableinstance = YLeaf(YType.str, "cbfDefineObjectTableInstance")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cbfdefinefileindex",
                                "cbfdefineobjectindex",
                                "cbfdefineobjectclass",
                                "cbfdefineobjectentrystatus",
                                "cbfdefineobjectid",
                                "cbfdefineobjectlastpolledinst",
                                "cbfdefineobjectnumentries",
                                "cbfdefineobjecttableinstance") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoBulkFileMib.Cbfdefineobjecttable.Cbfdefineobjectentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoBulkFileMib.Cbfdefineobjecttable.Cbfdefineobjectentry, self).__setattr__(name, value)

            class Cbfdefineobjectclass(Enum):
                """
                Cbfdefineobjectclass

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


            def has_data(self):
                return (
                    self.cbfdefinefileindex.is_set or
                    self.cbfdefineobjectindex.is_set or
                    self.cbfdefineobjectclass.is_set or
                    self.cbfdefineobjectentrystatus.is_set or
                    self.cbfdefineobjectid.is_set or
                    self.cbfdefineobjectlastpolledinst.is_set or
                    self.cbfdefineobjectnumentries.is_set or
                    self.cbfdefineobjecttableinstance.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cbfdefinefileindex.yfilter != YFilter.not_set or
                    self.cbfdefineobjectindex.yfilter != YFilter.not_set or
                    self.cbfdefineobjectclass.yfilter != YFilter.not_set or
                    self.cbfdefineobjectentrystatus.yfilter != YFilter.not_set or
                    self.cbfdefineobjectid.yfilter != YFilter.not_set or
                    self.cbfdefineobjectlastpolledinst.yfilter != YFilter.not_set or
                    self.cbfdefineobjectnumentries.yfilter != YFilter.not_set or
                    self.cbfdefineobjecttableinstance.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cbfDefineObjectEntry" + "[cbfDefineFileIndex='" + self.cbfdefinefileindex.get() + "']" + "[cbfDefineObjectIndex='" + self.cbfdefineobjectindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/cbfDefineObjectTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cbfdefinefileindex.is_set or self.cbfdefinefileindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfdefinefileindex.get_name_leafdata())
                if (self.cbfdefineobjectindex.is_set or self.cbfdefineobjectindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfdefineobjectindex.get_name_leafdata())
                if (self.cbfdefineobjectclass.is_set or self.cbfdefineobjectclass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfdefineobjectclass.get_name_leafdata())
                if (self.cbfdefineobjectentrystatus.is_set or self.cbfdefineobjectentrystatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfdefineobjectentrystatus.get_name_leafdata())
                if (self.cbfdefineobjectid.is_set or self.cbfdefineobjectid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfdefineobjectid.get_name_leafdata())
                if (self.cbfdefineobjectlastpolledinst.is_set or self.cbfdefineobjectlastpolledinst.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfdefineobjectlastpolledinst.get_name_leafdata())
                if (self.cbfdefineobjectnumentries.is_set or self.cbfdefineobjectnumentries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfdefineobjectnumentries.get_name_leafdata())
                if (self.cbfdefineobjecttableinstance.is_set or self.cbfdefineobjecttableinstance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfdefineobjecttableinstance.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cbfDefineFileIndex" or name == "cbfDefineObjectIndex" or name == "cbfDefineObjectClass" or name == "cbfDefineObjectEntryStatus" or name == "cbfDefineObjectID" or name == "cbfDefineObjectLastPolledInst" or name == "cbfDefineObjectNumEntries" or name == "cbfDefineObjectTableInstance"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cbfDefineFileIndex"):
                    self.cbfdefinefileindex = value
                    self.cbfdefinefileindex.value_namespace = name_space
                    self.cbfdefinefileindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cbfDefineObjectIndex"):
                    self.cbfdefineobjectindex = value
                    self.cbfdefineobjectindex.value_namespace = name_space
                    self.cbfdefineobjectindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cbfDefineObjectClass"):
                    self.cbfdefineobjectclass = value
                    self.cbfdefineobjectclass.value_namespace = name_space
                    self.cbfdefineobjectclass.value_namespace_prefix = name_space_prefix
                if(value_path == "cbfDefineObjectEntryStatus"):
                    self.cbfdefineobjectentrystatus = value
                    self.cbfdefineobjectentrystatus.value_namespace = name_space
                    self.cbfdefineobjectentrystatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cbfDefineObjectID"):
                    self.cbfdefineobjectid = value
                    self.cbfdefineobjectid.value_namespace = name_space
                    self.cbfdefineobjectid.value_namespace_prefix = name_space_prefix
                if(value_path == "cbfDefineObjectLastPolledInst"):
                    self.cbfdefineobjectlastpolledinst = value
                    self.cbfdefineobjectlastpolledinst.value_namespace = name_space
                    self.cbfdefineobjectlastpolledinst.value_namespace_prefix = name_space_prefix
                if(value_path == "cbfDefineObjectNumEntries"):
                    self.cbfdefineobjectnumentries = value
                    self.cbfdefineobjectnumentries.value_namespace = name_space
                    self.cbfdefineobjectnumentries.value_namespace_prefix = name_space_prefix
                if(value_path == "cbfDefineObjectTableInstance"):
                    self.cbfdefineobjecttableinstance = value
                    self.cbfdefineobjecttableinstance.value_namespace = name_space
                    self.cbfdefineobjecttableinstance.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cbfdefineobjectentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cbfdefineobjectentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cbfDefineObjectTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cbfDefineObjectEntry"):
                for c in self.cbfdefineobjectentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoBulkFileMib.Cbfdefineobjecttable.Cbfdefineobjectentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cbfdefineobjectentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cbfDefineObjectEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cbfstatusfiletable(Entity):
        """
        A table of bulk file status.
        
        .. attribute:: cbfstatusfileentry
        
        	Status for a particular file.  An entry exists in this table for each time cbfDefineFileNow has been set to 'create' and the corresponding entry here has not been explicitly deleted by the application or bumped to make room for a new entry.  Deleting an entry with cbfStatusFileState 'running' aborts the file creation attempt.  It is implementation and file\-system specific whether deleting the entry also deletes the file
        	**type**\: list of    :py:class:`Cbfstatusfileentry <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfstatusfiletable.Cbfstatusfileentry>`
        
        

        """

        _prefix = 'CISCO-BULK-FILE-MIB'
        _revision = '2002-06-10'

        def __init__(self):
            super(CiscoBulkFileMib.Cbfstatusfiletable, self).__init__()

            self.yang_name = "cbfStatusFileTable"
            self.yang_parent_name = "CISCO-BULK-FILE-MIB"

            self.cbfstatusfileentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoBulkFileMib.Cbfstatusfiletable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoBulkFileMib.Cbfstatusfiletable, self).__setattr__(name, value)


        class Cbfstatusfileentry(Entity):
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
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cbfstatusfilestate
            
            	The file state\:  running    data is being written to the file ready      the file is ready to be read emptied    an ephemeral file was successfully consumed noSpace    no data due to insufficient file space badName    no data due to a name or path problem writeErr   no data due to fatal file write error noMem      no data due to insufficient dynamic memory buffErr    implementation buffer too small aborted    short terminated by operator command  Only the 'ready' state implies that the file is available for transfer.  The disposition of files after an error is implementation and file\-syste specific
            	**type**\:   :py:class:`Cbfstatusfilestate <ydk.models.cisco_ios_xe.CISCO_BULK_FILE_MIB.CiscoBulkFileMib.Cbfstatusfiletable.Cbfstatusfileentry.Cbfstatusfilestate>`
            
            

            """

            _prefix = 'CISCO-BULK-FILE-MIB'
            _revision = '2002-06-10'

            def __init__(self):
                super(CiscoBulkFileMib.Cbfstatusfiletable.Cbfstatusfileentry, self).__init__()

                self.yang_name = "cbfStatusFileEntry"
                self.yang_parent_name = "cbfStatusFileTable"

                self.cbfdefinefileindex = YLeaf(YType.str, "cbfDefineFileIndex")

                self.cbfstatusfileindex = YLeaf(YType.uint32, "cbfStatusFileIndex")

                self.cbfstatusfilecompletiontime = YLeaf(YType.uint32, "cbfStatusFileCompletionTime")

                self.cbfstatusfileentrystatus = YLeaf(YType.enumeration, "cbfStatusFileEntryStatus")

                self.cbfstatusfilestate = YLeaf(YType.enumeration, "cbfStatusFileState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cbfdefinefileindex",
                                "cbfstatusfileindex",
                                "cbfstatusfilecompletiontime",
                                "cbfstatusfileentrystatus",
                                "cbfstatusfilestate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoBulkFileMib.Cbfstatusfiletable.Cbfstatusfileentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoBulkFileMib.Cbfstatusfiletable.Cbfstatusfileentry, self).__setattr__(name, value)

            class Cbfstatusfilestate(Enum):
                """
                Cbfstatusfilestate

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


            def has_data(self):
                return (
                    self.cbfdefinefileindex.is_set or
                    self.cbfstatusfileindex.is_set or
                    self.cbfstatusfilecompletiontime.is_set or
                    self.cbfstatusfileentrystatus.is_set or
                    self.cbfstatusfilestate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cbfdefinefileindex.yfilter != YFilter.not_set or
                    self.cbfstatusfileindex.yfilter != YFilter.not_set or
                    self.cbfstatusfilecompletiontime.yfilter != YFilter.not_set or
                    self.cbfstatusfileentrystatus.yfilter != YFilter.not_set or
                    self.cbfstatusfilestate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cbfStatusFileEntry" + "[cbfDefineFileIndex='" + self.cbfdefinefileindex.get() + "']" + "[cbfStatusFileIndex='" + self.cbfstatusfileindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/cbfStatusFileTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cbfdefinefileindex.is_set or self.cbfdefinefileindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfdefinefileindex.get_name_leafdata())
                if (self.cbfstatusfileindex.is_set or self.cbfstatusfileindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfstatusfileindex.get_name_leafdata())
                if (self.cbfstatusfilecompletiontime.is_set or self.cbfstatusfilecompletiontime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfstatusfilecompletiontime.get_name_leafdata())
                if (self.cbfstatusfileentrystatus.is_set or self.cbfstatusfileentrystatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfstatusfileentrystatus.get_name_leafdata())
                if (self.cbfstatusfilestate.is_set or self.cbfstatusfilestate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbfstatusfilestate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cbfDefineFileIndex" or name == "cbfStatusFileIndex" or name == "cbfStatusFileCompletionTime" or name == "cbfStatusFileEntryStatus" or name == "cbfStatusFileState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cbfDefineFileIndex"):
                    self.cbfdefinefileindex = value
                    self.cbfdefinefileindex.value_namespace = name_space
                    self.cbfdefinefileindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cbfStatusFileIndex"):
                    self.cbfstatusfileindex = value
                    self.cbfstatusfileindex.value_namespace = name_space
                    self.cbfstatusfileindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cbfStatusFileCompletionTime"):
                    self.cbfstatusfilecompletiontime = value
                    self.cbfstatusfilecompletiontime.value_namespace = name_space
                    self.cbfstatusfilecompletiontime.value_namespace_prefix = name_space_prefix
                if(value_path == "cbfStatusFileEntryStatus"):
                    self.cbfstatusfileentrystatus = value
                    self.cbfstatusfileentrystatus.value_namespace = name_space
                    self.cbfstatusfileentrystatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cbfStatusFileState"):
                    self.cbfstatusfilestate = value
                    self.cbfstatusfilestate.value_namespace = name_space
                    self.cbfstatusfilestate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cbfstatusfileentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cbfstatusfileentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cbfStatusFileTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cbfStatusFileEntry"):
                for c in self.cbfstatusfileentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoBulkFileMib.Cbfstatusfiletable.Cbfstatusfileentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cbfstatusfileentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cbfStatusFileEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cbfdefine is not None and self.cbfdefine.has_data()) or
            (self.cbfdefinefiletable is not None and self.cbfdefinefiletable.has_data()) or
            (self.cbfdefineobjecttable is not None and self.cbfdefineobjecttable.has_data()) or
            (self.cbfstatus is not None and self.cbfstatus.has_data()) or
            (self.cbfstatusfiletable is not None and self.cbfstatusfiletable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cbfdefine is not None and self.cbfdefine.has_operation()) or
            (self.cbfdefinefiletable is not None and self.cbfdefinefiletable.has_operation()) or
            (self.cbfdefineobjecttable is not None and self.cbfdefineobjecttable.has_operation()) or
            (self.cbfstatus is not None and self.cbfstatus.has_operation()) or
            (self.cbfstatusfiletable is not None and self.cbfstatusfiletable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-BULK-FILE-MIB:CISCO-BULK-FILE-MIB" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "cbfDefine"):
            if (self.cbfdefine is None):
                self.cbfdefine = CiscoBulkFileMib.Cbfdefine()
                self.cbfdefine.parent = self
                self._children_name_map["cbfdefine"] = "cbfDefine"
            return self.cbfdefine

        if (child_yang_name == "cbfDefineFileTable"):
            if (self.cbfdefinefiletable is None):
                self.cbfdefinefiletable = CiscoBulkFileMib.Cbfdefinefiletable()
                self.cbfdefinefiletable.parent = self
                self._children_name_map["cbfdefinefiletable"] = "cbfDefineFileTable"
            return self.cbfdefinefiletable

        if (child_yang_name == "cbfDefineObjectTable"):
            if (self.cbfdefineobjecttable is None):
                self.cbfdefineobjecttable = CiscoBulkFileMib.Cbfdefineobjecttable()
                self.cbfdefineobjecttable.parent = self
                self._children_name_map["cbfdefineobjecttable"] = "cbfDefineObjectTable"
            return self.cbfdefineobjecttable

        if (child_yang_name == "cbfStatus"):
            if (self.cbfstatus is None):
                self.cbfstatus = CiscoBulkFileMib.Cbfstatus()
                self.cbfstatus.parent = self
                self._children_name_map["cbfstatus"] = "cbfStatus"
            return self.cbfstatus

        if (child_yang_name == "cbfStatusFileTable"):
            if (self.cbfstatusfiletable is None):
                self.cbfstatusfiletable = CiscoBulkFileMib.Cbfstatusfiletable()
                self.cbfstatusfiletable.parent = self
                self._children_name_map["cbfstatusfiletable"] = "cbfStatusFileTable"
            return self.cbfstatusfiletable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cbfDefine" or name == "cbfDefineFileTable" or name == "cbfDefineObjectTable" or name == "cbfStatus" or name == "cbfStatusFileTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoBulkFileMib()
        return self._top_entity

