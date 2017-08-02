""" CISCO_VOICE_DNIS_MIB 

The MIB module provides management support for Dialer
Number Information Service (DNIS) mapping.  A DNIS
entry is associated with a Voice XML (VXML) page to
provide audio play back features. Multiple DNIS
entries can be grouped together to form a DNIS
mapping with a unique map name.

\*\*\* ABBREVIATIONS, ACRONYMS, AND SYMBOLS \*\*\*

DNIS \- Dialer Number Information Service

XML  \- Extensible Markup Language

VXML \- Voice XML

URL  \- Uniform Resource Locator  

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoVoiceDnisMib(Entity):
    """
    
    
    .. attribute:: cvdnismappingtable
    
    	The table contains the map name and a url specifying a file name. The file contains DNIS entries that belong to the DNIS mapping
    	**type**\:   :py:class:`Cvdnismappingtable <ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB.CiscoVoiceDnisMib.Cvdnismappingtable>`
    
    .. attribute:: cvdnisnodetable
    
    	The table contains a DNIS name and a url. The url is a pointer to a VXML page for the DNIS name. 
    	**type**\:   :py:class:`Cvdnisnodetable <ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB.CiscoVoiceDnisMib.Cvdnisnodetable>`
    
    

    """

    _prefix = 'CISCO-VOICE-DNIS-MIB'
    _revision = '2002-05-01'

    def __init__(self):
        super(CiscoVoiceDnisMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-VOICE-DNIS-MIB"
        self.yang_parent_name = "CISCO-VOICE-DNIS-MIB"

        self.cvdnismappingtable = CiscoVoiceDnisMib.Cvdnismappingtable()
        self.cvdnismappingtable.parent = self
        self._children_name_map["cvdnismappingtable"] = "cvDnisMappingTable"
        self._children_yang_names.add("cvDnisMappingTable")

        self.cvdnisnodetable = CiscoVoiceDnisMib.Cvdnisnodetable()
        self.cvdnisnodetable.parent = self
        self._children_name_map["cvdnisnodetable"] = "cvDnisNodeTable"
        self._children_yang_names.add("cvDnisNodeTable")


    class Cvdnismappingtable(Entity):
        """
        The table contains the map name and a url specifying
        a file name. The file contains DNIS entries that belong
        to the DNIS mapping.
        
        .. attribute:: cvdnismappingentry
        
        	Information about a single DNIS mapping. There is a unique DNIS map name. New DNIS mapping can be created using cvDnisMappingStatus.  The entry can be created with or without a file location  specified by cvDnisMappingUrl. The mapping file contains DNIS name and VXML page per line. For example, a  cvDnisMappingUrl could be tftp\://someserver/dnismap.txt. This file is a text file and the content format is   dnis <dnisname> url <urlname>. An example of the contents of the file itself can be   dnis 18004251234 url http\://www.b.com/p/vwelcome.vxml   dnis 18004253421 url http\://www.c.com/j/vxmlintf.vxml If a mapping file location is specified, then new rows corresponding to this map name are created and populated in cvDnisNodeTable from the contents of the file. The rows corresponding to this map name in cvDnisNodeTable cannot be created or modified or deleted but can be read.   If a mapping file location is not specified in cvDnisMappingUrl, then individual DNIS entries corresponding to this map name can be created, modified and deleted in cvDnisNodeTable.   Deleting an entry deletes all the related entries in cvDnisNodeTable. 
        	**type**\: list of    :py:class:`Cvdnismappingentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB.CiscoVoiceDnisMib.Cvdnismappingtable.Cvdnismappingentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DNIS-MIB'
        _revision = '2002-05-01'

        def __init__(self):
            super(CiscoVoiceDnisMib.Cvdnismappingtable, self).__init__()

            self.yang_name = "cvDnisMappingTable"
            self.yang_parent_name = "CISCO-VOICE-DNIS-MIB"

            self.cvdnismappingentry = YList(self)

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
                        super(CiscoVoiceDnisMib.Cvdnismappingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDnisMib.Cvdnismappingtable, self).__setattr__(name, value)


        class Cvdnismappingentry(Entity):
            """
            Information about a single DNIS mapping. There is a
            unique DNIS map name. New DNIS mapping can be created
            using cvDnisMappingStatus.
            
            The entry can be created with or without a file location 
            specified by cvDnisMappingUrl. The mapping file contains
            DNIS name and VXML page per line. For example, a 
            cvDnisMappingUrl could be tftp\://someserver/dnismap.txt.
            This file is a text file and the content format is
              dnis <dnisname> url <urlname>.
            An example of the contents of the file itself can be
              dnis 18004251234 url http\://www.b.com/p/vwelcome.vxml
              dnis 18004253421 url http\://www.c.com/j/vxmlintf.vxml
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
            
            .. attribute:: cvdnismappingname  <key>
            
            	The name which uniquely identifies a DNIS mapping. 
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: cvdnismappingrefresh
            
            	Whenever there is a need to re\-read the contents of the file specified by cvDnisMappingUrl, this object can be set to refresh(2). This will cause the contents of the file to be re\-read and correspondingly update the cvDnisNodeTable. After the completion of this operation, the value of this object is reset to idle(1). The only operation allowed on this object is setting it to refresh(2). This can only be done when the current value is idle(1) and the rowstatus is active(1).  idle       \- The refreshing process is idle and the user              can modify this object to refresh. refresh    \- The refreshing process is currently busy and              the user have to wait till the object              becomes idle to issue new refresh
            	**type**\:   :py:class:`Cvdnismappingrefresh <ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB.CiscoVoiceDnisMib.Cvdnismappingtable.Cvdnismappingentry.Cvdnismappingrefresh>`
            
            .. attribute:: cvdnismappingstatus
            
            	This object is used to create a new row or modify or delete an existing row in this table. When making the status active(1), if a valid cvDnisMappingUrl is present the contents of the url is downloaded and during that time cvDnisMappingRefresh is set to refresh(2). When cvDnisMappingRefresh is set to refresh(2), only the destroy(6) operation is allowed
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cvdnismappingurl
            
            	The url specifies a file location. The file contains individual DNIS entries that belong to the DNIS map  name specified by cvDnisMappingName.  Once a url is created and associated with a map name (the association is complete when the row is made active(1)), it cannot be modified while cvDnisMappingStatus is active. If a different url needs to be associated with the current map name, the row status should be made notInService(2) and this object has to be modified to associate a new url. When a new association is made all the DNIS entries corresponding to the old association will be deleted from the cvDnisNodeTable.  The url is read when the row status is made active(1) or when the row status is active and the object   cvDnisMappingRefresh is explicitly set to refresh(2).   If the url is not accessible then a cvDnisMappingUrlInaccessible notification will be generted. 
            	**type**\:  str
            
            .. attribute:: cvdnismappingurlaccesserror
            
            	ASCII text describing the error on last access of the url specified in cvDnisMappingUrl.  If the url access does not succeed, then this object is populated with an error message indicating the reason for failure. If the url access succeeds, this object is set to null string
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-VOICE-DNIS-MIB'
            _revision = '2002-05-01'

            def __init__(self):
                super(CiscoVoiceDnisMib.Cvdnismappingtable.Cvdnismappingentry, self).__init__()

                self.yang_name = "cvDnisMappingEntry"
                self.yang_parent_name = "cvDnisMappingTable"

                self.cvdnismappingname = YLeaf(YType.str, "cvDnisMappingName")

                self.cvdnismappingrefresh = YLeaf(YType.enumeration, "cvDnisMappingRefresh")

                self.cvdnismappingstatus = YLeaf(YType.enumeration, "cvDnisMappingStatus")

                self.cvdnismappingurl = YLeaf(YType.str, "cvDnisMappingUrl")

                self.cvdnismappingurlaccesserror = YLeaf(YType.str, "cvDnisMappingUrlAccessError")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvdnismappingname",
                                "cvdnismappingrefresh",
                                "cvdnismappingstatus",
                                "cvdnismappingurl",
                                "cvdnismappingurlaccesserror") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDnisMib.Cvdnismappingtable.Cvdnismappingentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDnisMib.Cvdnismappingtable.Cvdnismappingentry, self).__setattr__(name, value)

            class Cvdnismappingrefresh(Enum):
                """
                Cvdnismappingrefresh

                Whenever there is a need to re\-read the contents of the

                file specified by cvDnisMappingUrl, this object can be

                set to refresh(2). This will cause the contents of the

                file to be re\-read and correspondingly update the

                cvDnisNodeTable. After the completion of this operation,

                the value of this object is reset to idle(1). The only

                operation allowed on this object is setting it to

                refresh(2). This can only be done when the current value

                is idle(1) and the rowstatus is active(1).

                idle       \- The refreshing process is idle and the user

                             can modify this object to refresh.

                refresh    \- The refreshing process is currently busy and

                             the user have to wait till the object

                             becomes idle to issue new refresh.

                .. data:: idle = 1

                .. data:: refresh = 2

                """

                idle = Enum.YLeaf(1, "idle")

                refresh = Enum.YLeaf(2, "refresh")


            def has_data(self):
                return (
                    self.cvdnismappingname.is_set or
                    self.cvdnismappingrefresh.is_set or
                    self.cvdnismappingstatus.is_set or
                    self.cvdnismappingurl.is_set or
                    self.cvdnismappingurlaccesserror.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvdnismappingname.yfilter != YFilter.not_set or
                    self.cvdnismappingrefresh.yfilter != YFilter.not_set or
                    self.cvdnismappingstatus.yfilter != YFilter.not_set or
                    self.cvdnismappingurl.yfilter != YFilter.not_set or
                    self.cvdnismappingurlaccesserror.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvDnisMappingEntry" + "[cvDnisMappingName='" + self.cvdnismappingname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DNIS-MIB:CISCO-VOICE-DNIS-MIB/cvDnisMappingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvdnismappingname.is_set or self.cvdnismappingname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvdnismappingname.get_name_leafdata())
                if (self.cvdnismappingrefresh.is_set or self.cvdnismappingrefresh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvdnismappingrefresh.get_name_leafdata())
                if (self.cvdnismappingstatus.is_set or self.cvdnismappingstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvdnismappingstatus.get_name_leafdata())
                if (self.cvdnismappingurl.is_set or self.cvdnismappingurl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvdnismappingurl.get_name_leafdata())
                if (self.cvdnismappingurlaccesserror.is_set or self.cvdnismappingurlaccesserror.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvdnismappingurlaccesserror.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvDnisMappingName" or name == "cvDnisMappingRefresh" or name == "cvDnisMappingStatus" or name == "cvDnisMappingUrl" or name == "cvDnisMappingUrlAccessError"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvDnisMappingName"):
                    self.cvdnismappingname = value
                    self.cvdnismappingname.value_namespace = name_space
                    self.cvdnismappingname.value_namespace_prefix = name_space_prefix
                if(value_path == "cvDnisMappingRefresh"):
                    self.cvdnismappingrefresh = value
                    self.cvdnismappingrefresh.value_namespace = name_space
                    self.cvdnismappingrefresh.value_namespace_prefix = name_space_prefix
                if(value_path == "cvDnisMappingStatus"):
                    self.cvdnismappingstatus = value
                    self.cvdnismappingstatus.value_namespace = name_space
                    self.cvdnismappingstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cvDnisMappingUrl"):
                    self.cvdnismappingurl = value
                    self.cvdnismappingurl.value_namespace = name_space
                    self.cvdnismappingurl.value_namespace_prefix = name_space_prefix
                if(value_path == "cvDnisMappingUrlAccessError"):
                    self.cvdnismappingurlaccesserror = value
                    self.cvdnismappingurlaccesserror.value_namespace = name_space
                    self.cvdnismappingurlaccesserror.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvdnismappingentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvdnismappingentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvDnisMappingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DNIS-MIB:CISCO-VOICE-DNIS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvDnisMappingEntry"):
                for c in self.cvdnismappingentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDnisMib.Cvdnismappingtable.Cvdnismappingentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvdnismappingentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvDnisMappingEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvdnisnodetable(Entity):
        """
        The table contains a DNIS name and a url. The url is a
        pointer to a VXML page for the DNIS name. 
        
        .. attribute:: cvdnisnodeentry
        
        	Each entry is a DNIS name and the location of the associated VXML page. New DNIS entries can be created or the existing entries can be modified or deleted only if the corresponding map name (defined in cvDnisMappingTable) does not have any file name provided in the cvDnisMappingUrl object.   If a file name is provided in cvDnisMappingUrl corresponding to this entry's map name, then this row will have read permission only
        	**type**\: list of    :py:class:`Cvdnisnodeentry <ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB.CiscoVoiceDnisMib.Cvdnisnodetable.Cvdnisnodeentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-DNIS-MIB'
        _revision = '2002-05-01'

        def __init__(self):
            super(CiscoVoiceDnisMib.Cvdnisnodetable, self).__init__()

            self.yang_name = "cvDnisNodeTable"
            self.yang_parent_name = "CISCO-VOICE-DNIS-MIB"

            self.cvdnisnodeentry = YList(self)

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
                        super(CiscoVoiceDnisMib.Cvdnisnodetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceDnisMib.Cvdnisnodetable, self).__setattr__(name, value)


        class Cvdnisnodeentry(Entity):
            """
            Each entry is a DNIS name and the location of the
            associated VXML page. New DNIS entries can be created or
            the existing entries can be modified or deleted only if
            the corresponding map name (defined in
            cvDnisMappingTable) does not have any file name provided
            in the cvDnisMappingUrl object. 
            
            If a file name is provided in cvDnisMappingUrl
            corresponding to this entry's map name, then this row
            will have read permission only.
            
            .. attribute:: cvdnismappingname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`cvdnismappingname <ydk.models.cisco_ios_xe.CISCO_VOICE_DNIS_MIB.CiscoVoiceDnisMib.Cvdnismappingtable.Cvdnismappingentry>`
            
            .. attribute:: cvdnisnumber  <key>
            
            	The individual DNIS name. It is unique within a DNIS mapping
            	**type**\:  str
            
            .. attribute:: cvdnisnodemodifiable
            
            	This object specifies whether the object in a particular row is modifiable. The object is set to true(1) if the corresponding map name (defined in cvDnisMappingTable) does not have any file name provided in the cvDnisMappingUrl object. Otherwise this object is set to false(2) and the row becomes read only.  
            	**type**\:  bool
            
            .. attribute:: cvdnisnodestatus
            
            	This object is used to create a new row or modify or delete an existing row in this table. The objects in a row can be modified or deleted while the row status is active(1) and cvDnisNodeModifiable is true(1). The row status cannot be set to notInService(2) or createAndWait(5). 
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cvdnisnodeurl
            
            	The url specifies a VXML page. This page contains voice XML links to play audio data.  This url which is a VXML page is not read immediately when the row is made active(1), but only when a call that requires the use of this DNIS comes through
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-VOICE-DNIS-MIB'
            _revision = '2002-05-01'

            def __init__(self):
                super(CiscoVoiceDnisMib.Cvdnisnodetable.Cvdnisnodeentry, self).__init__()

                self.yang_name = "cvDnisNodeEntry"
                self.yang_parent_name = "cvDnisNodeTable"

                self.cvdnismappingname = YLeaf(YType.str, "cvDnisMappingName")

                self.cvdnisnumber = YLeaf(YType.str, "cvDnisNumber")

                self.cvdnisnodemodifiable = YLeaf(YType.boolean, "cvDnisNodeModifiable")

                self.cvdnisnodestatus = YLeaf(YType.enumeration, "cvDnisNodeStatus")

                self.cvdnisnodeurl = YLeaf(YType.str, "cvDnisNodeUrl")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvdnismappingname",
                                "cvdnisnumber",
                                "cvdnisnodemodifiable",
                                "cvdnisnodestatus",
                                "cvdnisnodeurl") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceDnisMib.Cvdnisnodetable.Cvdnisnodeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceDnisMib.Cvdnisnodetable.Cvdnisnodeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cvdnismappingname.is_set or
                    self.cvdnisnumber.is_set or
                    self.cvdnisnodemodifiable.is_set or
                    self.cvdnisnodestatus.is_set or
                    self.cvdnisnodeurl.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvdnismappingname.yfilter != YFilter.not_set or
                    self.cvdnisnumber.yfilter != YFilter.not_set or
                    self.cvdnisnodemodifiable.yfilter != YFilter.not_set or
                    self.cvdnisnodestatus.yfilter != YFilter.not_set or
                    self.cvdnisnodeurl.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvDnisNodeEntry" + "[cvDnisMappingName='" + self.cvdnismappingname.get() + "']" + "[cvDnisNumber='" + self.cvdnisnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-DNIS-MIB:CISCO-VOICE-DNIS-MIB/cvDnisNodeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvdnismappingname.is_set or self.cvdnismappingname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvdnismappingname.get_name_leafdata())
                if (self.cvdnisnumber.is_set or self.cvdnisnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvdnisnumber.get_name_leafdata())
                if (self.cvdnisnodemodifiable.is_set or self.cvdnisnodemodifiable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvdnisnodemodifiable.get_name_leafdata())
                if (self.cvdnisnodestatus.is_set or self.cvdnisnodestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvdnisnodestatus.get_name_leafdata())
                if (self.cvdnisnodeurl.is_set or self.cvdnisnodeurl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvdnisnodeurl.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvDnisMappingName" or name == "cvDnisNumber" or name == "cvDnisNodeModifiable" or name == "cvDnisNodeStatus" or name == "cvDnisNodeUrl"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvDnisMappingName"):
                    self.cvdnismappingname = value
                    self.cvdnismappingname.value_namespace = name_space
                    self.cvdnismappingname.value_namespace_prefix = name_space_prefix
                if(value_path == "cvDnisNumber"):
                    self.cvdnisnumber = value
                    self.cvdnisnumber.value_namespace = name_space
                    self.cvdnisnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "cvDnisNodeModifiable"):
                    self.cvdnisnodemodifiable = value
                    self.cvdnisnodemodifiable.value_namespace = name_space
                    self.cvdnisnodemodifiable.value_namespace_prefix = name_space_prefix
                if(value_path == "cvDnisNodeStatus"):
                    self.cvdnisnodestatus = value
                    self.cvdnisnodestatus.value_namespace = name_space
                    self.cvdnisnodestatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cvDnisNodeUrl"):
                    self.cvdnisnodeurl = value
                    self.cvdnisnodeurl.value_namespace = name_space
                    self.cvdnisnodeurl.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvdnisnodeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvdnisnodeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvDnisNodeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-DNIS-MIB:CISCO-VOICE-DNIS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvDnisNodeEntry"):
                for c in self.cvdnisnodeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceDnisMib.Cvdnisnodetable.Cvdnisnodeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvdnisnodeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvDnisNodeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cvdnismappingtable is not None and self.cvdnismappingtable.has_data()) or
            (self.cvdnisnodetable is not None and self.cvdnisnodetable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cvdnismappingtable is not None and self.cvdnismappingtable.has_operation()) or
            (self.cvdnisnodetable is not None and self.cvdnisnodetable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-VOICE-DNIS-MIB:CISCO-VOICE-DNIS-MIB" + path_buffer

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

        if (child_yang_name == "cvDnisMappingTable"):
            if (self.cvdnismappingtable is None):
                self.cvdnismappingtable = CiscoVoiceDnisMib.Cvdnismappingtable()
                self.cvdnismappingtable.parent = self
                self._children_name_map["cvdnismappingtable"] = "cvDnisMappingTable"
            return self.cvdnismappingtable

        if (child_yang_name == "cvDnisNodeTable"):
            if (self.cvdnisnodetable is None):
                self.cvdnisnodetable = CiscoVoiceDnisMib.Cvdnisnodetable()
                self.cvdnisnodetable.parent = self
                self._children_name_map["cvdnisnodetable"] = "cvDnisNodeTable"
            return self.cvdnisnodetable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cvDnisMappingTable" or name == "cvDnisNodeTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoVoiceDnisMib()
        return self._top_entity

